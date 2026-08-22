#!/usr/bin/env python3
"""Incremental archive builder for all five lab notebook sources.

Walks each source's *entire* history (not the 7-day window the live fetchers use)
into a local SQLite database with a full-text index, so the digest tools can search
across everything the labs have ever published.

The build is incremental and resumable. For the four GitHub notebooks it lists a
repo's whole posts tree in a single git-tree call and compares each file's blob SHA
against what is already stored: unchanged posts are skipped without re-fetching, and
because every processed post is committed as it goes, an interrupted run (a dropped
connection, an exhausted rate limit) simply resumes on the next invocation. The
WordPress notebook has no blob SHA, so it is deduplicated by URL instead.

Run a subset with --sources; with no flag it builds all five. Parsing and URL
derivation are reused wholesale from notebook_parsing — this script only adds the
enumeration, storage, and incremental-skip layers.
"""

import argparse
import base64
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from subprocess import run
from urllib.error import HTTPError
from urllib.parse import quote

# Reuse the GitHub repo/prefix/suffix layout table and HTTP helpers from the live
# fetcher, and the pure parsing helpers from notebook_parsing. Bare imports work
# because this script lives alongside them in scripts/ (sys.path[0]).
from fetch_github_notebook import API, NOTEBOOKS, get_json, headers, rate_limit_message
from fetch_lab_posts import DEFAULT_SITE, collect_posts
from notebook_parsing import derive_permalink, parse_front_matter

REPO_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = REPO_ROOT / ".cache" / "archive.db"

TIMEOUT = 30

# GitHub sources, in ascending size so a partial/interrupted build makes progress
# on the cheap ones first. Each maps to a NOTEBOOKS entry (repo/prefix/suffix).
GITHUB_SOURCES = ["megan", "tumbling-oysters", "grace", "ariana", "sams"]
WORDPRESS_SOURCE = "wordpress"
ALL_SOURCES = GITHUB_SOURCES + [WORDPRESS_SOURCE]

# Front matter carries the author on most posts, but Grace's notebook omits it and
# a few posts elsewhere leave it blank. These are the fallbacks used when the block
# has no author, matching each notebook's single known author.
DEFAULT_AUTHORS = {
    "megan": "Megan Ewing",
    "tumbling-oysters": "Steven Roberts",
    "grace": "Grace Crandall",
    "ariana": "Ariana Huffmyer",
    "sams": "Sam White",
}


class RateLimited(Exception):
    """Raised when a GitHub call exhausts the rate limit, to stop the run cleanly."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------

def init_db(conn: sqlite3.Connection) -> None:
    """Create the posts table, its FTS5 index, and the sync triggers if absent."""
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id         INTEGER PRIMARY KEY,
            source     TEXT NOT NULL,
            author     TEXT,
            date       TEXT,
            url        TEXT NOT NULL,   -- published (display) URL; NOT unique per file
            path        TEXT NOT NULL,  -- repo file path (GitHub) or url (WordPress)
            title      TEXT,
            categories TEXT,          -- JSON array of category strings
            body_text  TEXT,
            blob_sha   TEXT,          -- git blob SHA (GitHub sources); NULL for WordPress
            fetched_at TEXT,
            -- 1 when this post's published URL is shared by another archived post of
            -- the same source, so the URL cannot uniquely resolve to it on the live
            -- site (e.g. Grace's Jekyll `permalink: /:title/` collapses same-slug
            -- posts from different years onto one URL). A future search can surface
            -- this instead of presenting a possibly-stale link silently.
            shadowed   INTEGER NOT NULL DEFAULT 0,
            -- Identity is the repo file path, not the published URL: distinct source
            -- files that derive the same URL must each keep their own row.
            UNIQUE(source, path)
        );

        -- Full-text index over the searchable fields. External-content mode keeps
        -- the text in `posts` (no duplicate copy); the triggers below mirror every
        -- row change into the index so incremental upserts stay searchable.
        CREATE VIRTUAL TABLE IF NOT EXISTS posts_fts USING fts5(
            title, body_text, categories,
            content='posts', content_rowid='id'
        );

        CREATE TRIGGER IF NOT EXISTS posts_ai AFTER INSERT ON posts BEGIN
            INSERT INTO posts_fts(rowid, title, body_text, categories)
            VALUES (new.id, new.title, new.body_text, new.categories);
        END;

        CREATE TRIGGER IF NOT EXISTS posts_ad AFTER DELETE ON posts BEGIN
            INSERT INTO posts_fts(posts_fts, rowid, title, body_text, categories)
            VALUES ('delete', old.id, old.title, old.body_text, old.categories);
        END;

        CREATE TRIGGER IF NOT EXISTS posts_au AFTER UPDATE ON posts BEGIN
            INSERT INTO posts_fts(posts_fts, rowid, title, body_text, categories)
            VALUES ('delete', old.id, old.title, old.body_text, old.categories);
            INSERT INTO posts_fts(rowid, title, body_text, categories)
            VALUES (new.id, new.title, new.body_text, new.categories);
        END;
        """
    )
    conn.commit()


def existing_blob_sha(conn: sqlite3.Connection, source: str, path: str):
    """Return the stored blob SHA for a post, or None if it is not archived yet.

    Keyed on the repo file `path` (the archive's identity), not the published URL —
    two files whose URLs collide are still distinct posts with distinct SHAs.
    """
    row = conn.execute(
        "SELECT blob_sha FROM posts WHERE source = ? AND path = ?", (source, path)
    ).fetchone()
    return row[0] if row else None


def path_exists(conn: sqlite3.Connection, source: str, path: str) -> bool:
    return (
        conn.execute(
            "SELECT 1 FROM posts WHERE source = ? AND path = ?", (source, path)
        ).fetchone()
        is not None
    )


def upsert_post(conn: sqlite3.Connection, post: dict) -> None:
    """Insert a post, or update it in place when (source, url) already exists.

    Committed immediately so an interrupted run leaves every processed post durably
    stored — the basis for resumability.
    """
    conn.execute(
        """
        INSERT INTO posts (source, author, date, url, path, title, categories,
                           body_text, blob_sha, fetched_at)
        VALUES (:source, :author, :date, :url, :path, :title, :categories,
                :body_text, :blob_sha, :fetched_at)
        ON CONFLICT(source, path) DO UPDATE SET
            author     = excluded.author,
            date       = excluded.date,
            url        = excluded.url,
            title      = excluded.title,
            categories = excluded.categories,
            body_text  = excluded.body_text,
            blob_sha   = excluded.blob_sha,
            fetched_at = excluded.fetched_at
        """,
        post,
    )
    conn.commit()


# ---------------------------------------------------------------------------
# GitHub sources
# ---------------------------------------------------------------------------

def github_token() -> str:
    """Get a token from `gh auth token` for authenticated (5,000/hour) requests."""
    result = run(["gh", "auth", "token"], capture_output=True, text=True)
    token = result.stdout.strip()
    if result.returncode != 0 or not token:
        raise SystemExit(
            "Could not obtain a GitHub token from `gh auth token`. "
            "Run `gh auth login` first.\n" + result.stderr.strip()
        )
    return token


def call_github(url: str):
    """GET JSON from GitHub, converting an exhausted rate limit into RateLimited."""
    try:
        return get_json(url, TIMEOUT)
    except HTTPError as e:
        message = rate_limit_message(e)
        if message:
            raise RateLimited(message) from e
        raise


def list_tree(repo: str) -> tuple:
    """List every blob in a repo via one recursive git-tree call.

    Returns (entries, warnings). Resolving the default branch is a separate cheap
    metadata call; the tree listing itself is the single bulk call the requirement
    asks for.
    """
    warnings = []
    meta = call_github(f"{API}/repos/{repo}")
    branch = meta.get("default_branch", "main")
    data = call_github(f"{API}/repos/{repo}/git/trees/{quote(branch)}?recursive=1")
    if data.get("truncated"):
        warnings.append(
            f"{repo}: git tree was truncated by the API — some posts may be missing."
        )
    return data.get("tree", []), warnings


def fetch_blob_text(repo: str, sha: str) -> str:
    """Fetch a blob's decoded UTF-8 text by its content-addressed SHA."""
    data = call_github(f"{API}/repos/{repo}/git/blobs/{sha}")
    if data.get("encoding") == "base64":
        return base64.b64decode(data.get("content", "")).decode("utf-8", errors="replace")
    return data.get("content", "")


def _fallback_date(path: str):
    """Pull a YYYY-MM-DD stamp out of a post's filename when front matter lacks one."""
    m = re.search(r"(\d{4}-\d{2}-\d{2})", path)
    return m.group(1) if m else None


def _fallback_title(path: str) -> str:
    """A readable title from the path when front matter has none."""
    name = path[: -len("/index.qmd")] if path.endswith("/index.qmd") else path
    slug = os.path.splitext(os.path.basename(name))[0]
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug)
    return slug.replace("-", " ").replace("_", " ").strip() or slug


def process_github_source(conn: sqlite3.Connection, source: str, counts: dict) -> list:
    """Archive one GitHub notebook, skipping posts whose blob SHA is unchanged."""
    config = NOTEBOOKS[source]
    repo = config["repo"]
    prefix, suffix = config["prefix"], config["suffix"]
    default_author = DEFAULT_AUTHORS.get(source)

    entries, warnings = list_tree(repo)
    matched = [
        e
        for e in entries
        if e.get("type") == "blob"
        and e["path"].startswith(prefix)
        and e["path"].endswith(suffix)
    ]

    for entry in matched:
        path = entry["path"]
        blob_sha = entry["sha"]
        url = derive_permalink(source, path)

        if existing_blob_sha(conn, source, path) == blob_sha:
            counts[source]["skipped"] += 1
            continue

        # SHA differs (or post is new): this is the only place we spend a fetch.
        body = fetch_blob_text(repo, blob_sha)
        fm = parse_front_matter(body, default_author=default_author)
        upsert_post(
            conn,
            {
                "source": source,
                "author": fm["author"] or default_author,
                "date": fm["date"] or _fallback_date(path),
                "url": url,
                "path": path,
                "title": fm["title"] or _fallback_title(path),
                "categories": json.dumps(fm["categories"]),
                "body_text": body,
                "blob_sha": blob_sha,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            },
        )
        counts[source]["added"] += 1

    return warnings


# ---------------------------------------------------------------------------
# WordPress source
# ---------------------------------------------------------------------------

def process_wordpress_source(conn: sqlite3.Connection, counts: dict) -> list:
    """Archive the genefish WordPress notebook by paging through its full history.

    Reuses fetch_lab_posts.collect_posts, but with the day-window cutoff removed:
    a cutoff of the Unix epoch never predates any real post, so paging stops only
    when the site runs out of posts. Deduplicated by URL (no blob SHA exists), so
    already-archived posts are skipped and the run stays resumable.
    """
    source = WORDPRESS_SOURCE
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    # A high page cap so full history is reached; collect_posts warns if it is hit.
    posts, warnings = collect_posts(
        DEFAULT_SITE, cutoff=epoch, per_page=100, max_pages=200, timeout=TIMEOUT
    )

    for post in posts:
        url = post["url"]
        # WordPress has no repo path, so the URL itself is the file identity.
        if not url or path_exists(conn, source, url):
            counts[source]["skipped"] += 1
            continue
        upsert_post(
            conn,
            {
                "source": source,
                "author": post["author"],
                "date": post["date"],
                "url": url,
                "path": url,
                "title": post["title"],
                "categories": json.dumps([]),
                "body_text": post["content"],
                "blob_sha": None,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            },
        )
        counts[source]["added"] += 1

    return warnings


# ---------------------------------------------------------------------------
# Summary / main
# ---------------------------------------------------------------------------

def mark_shadowed(conn: sqlite3.Connection, sources: list) -> None:
    """Recompute the `shadowed` flag for the given sources.

    A post is shadowed when its published URL is shared by another archived post of
    the same source: the URL cannot uniquely resolve to it on the live site. We only
    touch rows whose flag actually changes, to avoid needless FTS-trigger churn.
    """
    for source in sources:
        colliding = (
            "SELECT url FROM posts WHERE source = ? "
            "GROUP BY url HAVING COUNT(*) > 1"
        )
        conn.execute(
            f"UPDATE posts SET shadowed = 1 "
            f"WHERE source = ? AND shadowed = 0 AND url IN ({colliding})",
            (source, source),
        )
        conn.execute(
            f"UPDATE posts SET shadowed = 0 "
            f"WHERE source = ? AND shadowed = 1 AND url NOT IN ({colliding})",
            (source, source),
        )
    conn.commit()


def print_summary(conn: sqlite3.Connection, counts: dict, sources: list) -> None:
    totals = dict(
        conn.execute("SELECT source, COUNT(*) FROM posts GROUP BY source").fetchall()
    )
    shadowed = dict(
        conn.execute(
            "SELECT source, COUNT(*) FROM posts WHERE shadowed = 1 GROUP BY source"
        ).fetchall()
    )
    grand_total = sum(totals.values())
    added = sum(counts[s]["added"] for s in sources)
    skipped = sum(counts[s]["skipped"] for s in sources)

    print("\n=== Archive build summary ===")
    print(f"Posts added/updated this run: {added}")
    print(f"Posts skipped (already current): {skipped}")
    print(f"Total posts in archive: {grand_total}")
    print("\nBy source (added + skipped should equal total):")
    for source in sorted(set(sources) | set(totals)):
        c = counts.get(source, {"added": 0, "skipped": 0})
        shadow = shadowed.get(source, 0)
        # A post whose URL collides with a sibling on the live site.
        note = f"  ({shadow} shadowed)" if shadow else ""
        print(
            f"  {source:<18} total={totals.get(source, 0):<5} "
            f"added={c['added']:<5} skipped={c['skipped']:<5}{note}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sources",
        nargs="+",
        choices=ALL_SOURCES,
        default=ALL_SOURCES,
        help="which sources to build (default: all five)",
    )
    args = parser.parse_args()

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    counts = {s: {"added": 0, "skipped": 0} for s in ALL_SOURCES}
    warnings = []
    interrupted = False

    try:
        init_db(conn)
        for source in args.sources:
            if source in GITHUB_SOURCES:
                # Set the token for the reused headers() helper (reads GITHUB_TOKEN).
                os.environ.setdefault("GITHUB_TOKEN", github_token())
                warnings += process_github_source(conn, source, counts)
            else:
                warnings += process_wordpress_source(conn, counts)
    except RateLimited as e:
        interrupted = True
        done = sum(counts[s]["added"] for s in args.sources)
        print(f"\n!! {e.message}", file=sys.stderr)
        print(
            f"!! Stopped mid-run after archiving {done} new post(s) this session. "
            "They are already committed to the database — re-run this script once the "
            "limit resets and it will resume where it left off (unchanged posts are "
            "skipped via their blob SHA).",
            file=sys.stderr,
        )

    # Recompute URL-collision flags for whatever we touched (safe after an
    # interruption too — it only reflects rows already committed).
    mark_shadowed(conn, args.sources)

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")

    print_summary(conn, counts, args.sources)
    conn.close()
    if interrupted:
        sys.exit(1)


if __name__ == "__main__":
    main()
