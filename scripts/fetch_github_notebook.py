#!/usr/bin/env python3
"""Fetch recently changed lab notebook posts from a GitHub-hosted blog.

Two API calls locate every post changed in the window (a commit listing plus one
`compare` over the whole range) instead of one call per commit. Post bodies are
read at the commit SHA rather than off a branch name, so there is no `main` vs
`master` guesswork. Cosmetic edits carry their diff and only a trimmed body, so a
one-line link fix is not mistaken for new science.
"""

import argparse
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone, timedelta
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen

# Shared post-parsing logic, also used by the archive builder. Re-exported here
# so callers and tests can keep referencing fetch_github_notebook.build_post /
# .clip.
from notebook_parsing import build_post, clip

DEFAULT_DAYS = 7
DEFAULT_TIMEOUT = 20
DEFAULT_WORKERS = 4
DEFAULT_MAX_CHARS = 60000
# A modified post whose diff touches no more than this many lines is treated as
# cosmetic (link fix, typo, formatting) — there is no new science in a one-line
# change. Its patch is reported in full, but its body is trimmed hard: enough for
# front matter and context, not enough to reread a 94KB analysis post.
DEFAULT_COSMETIC_LINES = 6
DEFAULT_COSMETIC_MAX_CHARS = 4000

API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"

# Per-notebook post layout. `suffix` is matched against the full path, so
# "/index.qmd" pins Quarto posts to their folder's index file while ".qmd"
# accepts flat post files as well as nested ones.
NOTEBOOKS = {
    "tumbling-oysters": {
        "repo": "sr320/tumbling-oysters",
        "prefix": "posts/",
        "suffix": ".qmd",
    },
    "ariana": {
        "repo": "AHuffmyer/ahuffmyer.github.io",
        "prefix": "posts/",
        "suffix": ".qmd",
    },
    "sams": {
        "repo": "RobertsLab/sams-notebook",
        "prefix": "posts/",
        "suffix": "/index.qmd",
    },
    "grace": {
        "repo": "grace-ac/grace-ac.github.io",
        "prefix": "_posts/",
        "suffix": ".md",
        # Grace's agent flags front-matter dates that disagree with when the
        # file was actually committed, so it needs per-file commit history.
        "file_dates": True,
    },
    "megan": {
        "repo": "meganewing/mewing-notebook",
        "prefix": "posts/",
        # Quarto site with no per-post folder convention: posts are flat `.qmd`
        # files at varying depths (`posts/2026-08/slug.qmd`,
        # `posts/projects/slug.qmd`) plus a few `index.qmd` folders, so match
        # `.qmd` broadly rather than pinning to `/index.qmd` like sams.
        "suffix": ".qmd",
    },
}


def headers() -> dict:
    h = {"User-Agent": "LabNotebook-Summarizer", "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        # Raises the rate limit from 60 requests/hour to 5,000.
        h["Authorization"] = f"Bearer {token}"
    return h


def get_json(url: str, timeout: int):
    with urlopen(Request(url, headers=headers()), timeout=timeout) as resp:
        return json.load(resp)


def get_text(url: str, timeout: int) -> str:
    with urlopen(Request(url, headers=headers()), timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def rate_limit_message(err: HTTPError) -> str:
    """Turn an exhausted-rate-limit 403/429 into an actionable message."""
    if err.code not in (403, 429):
        return ""
    if err.headers.get("X-RateLimit-Remaining") != "0":
        return ""
    reset = err.headers.get("X-RateLimit-Reset")
    when = ""
    if reset and reset.isdigit():
        when = datetime.fromtimestamp(int(reset), timezone.utc).strftime(" (resets %H:%M UTC)")
    authed = "GITHUB_TOKEN" in os.environ or "GH_TOKEN" in os.environ
    hint = (
        "the authenticated limit of 5,000/hour is exhausted"
        if authed
        else "set GITHUB_TOKEN to raise the limit from 60 to 5,000 requests/hour"
    )
    return f"GitHub API rate limit reached{when} — {hint}."


def list_commits(repo: str, since: str, timeout: int) -> list:
    url = f"{API}/repos/{repo}/commits?since={quote(since)}&per_page=100"
    return get_json(url, timeout)


def changed_files(repo: str, commits: list, timeout: int):
    """All files touched across the commit range, via a single compare call.

    `commits` is newest-first as returned by the API. Comparing the oldest
    commit's first parent against the newest commit covers the whole window; a
    root commit with no parents falls back to comparing against itself.
    """
    warnings = []
    oldest, newest = commits[-1], commits[0]
    parents = oldest.get("parents") or []
    base = parents[0]["sha"] if parents else oldest["sha"]
    data = get_json(f"{API}/repos/{repo}/compare/{base}...{newest['sha']}", timeout)

    if data.get("status") not in ("ahead", "identical", None):
        warnings.append(
            f"Commit range compare returned status {data.get('status')!r} — history may "
            "have been rewritten; file list could be incomplete."
        )
    files = data.get("files") or []
    # The compare endpoint caps its file list at 300 entries.
    if len(files) >= 300:
        warnings.append(
            "Compare returned 300 files (the API maximum) — some changed posts may be missing."
        )
    return files, warnings


def file_commit_dates(repo: str, path: str, since: str, timeout: int) -> list:
    """Commit dates that touched one path in the window, oldest last."""
    url = f"{API}/repos/{repo}/commits?since={quote(since)}&per_page=100&path={quote(path)}"
    return [c["commit"]["committer"]["date"] for c in get_json(url, timeout)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--notebook", choices=sorted(NOTEBOOKS), required=True, help="which notebook to fetch"
    )
    parser.add_argument("--days", type=int, default=DEFAULT_DAYS, help="window size in days")
    parser.add_argument(
        "--cosmetic-lines",
        type=int,
        default=DEFAULT_COSMETIC_LINES,
        help="max changed lines for a modified post to count as cosmetic",
    )
    parser.add_argument(
        "--max-chars", type=int, default=DEFAULT_MAX_CHARS, help="per-post content cap"
    )
    parser.add_argument(
        "--cosmetic-max-chars",
        type=int,
        default=DEFAULT_COSMETIC_MAX_CHARS,
        help="content cap for cosmetically edited posts (front matter plus context)",
    )
    parser.add_argument(
        "--file-dates",
        action="store_true",
        help="also fetch per-file commit dates (one extra call per post)",
    )
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="per-request seconds")
    args = parser.parse_args()

    config = NOTEBOOKS[args.notebook]
    repo = config["repo"]
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=args.days)
    since = cutoff.strftime("%Y-%m-%dT%H:%M:%SZ")
    want_dates = args.file_dates or config.get("file_dates", False)

    result = {
        "notebook": args.notebook,
        "repo": repo,
        "week_start": cutoff.strftime("%Y-%m-%d"),
        "today": now.strftime("%Y-%m-%d"),
    }
    warnings = []

    try:
        commits = list_commits(repo, since, args.timeout)
        result["commits_scanned"] = len(commits)
        if not commits:
            print(json.dumps({**result, "posts": [], "warnings": warnings}, indent=2))
            return

        head_sha = commits[0]["sha"]
        files, compare_warnings = changed_files(repo, commits, args.timeout)
        warnings.extend(compare_warnings)

        matched = [
            f
            for f in files
            if f["filename"].startswith(config["prefix"])
            and f["filename"].endswith(config["suffix"])
        ]
        removed = [f["filename"] for f in matched if f.get("status") == "removed"]
        for path in removed:
            warnings.append(f"Skipped {path}: deleted in this window.")
        matched = [f for f in matched if f.get("status") != "removed"]

        posts = [build_post(repo, f, head_sha, args.cosmetic_lines) for f in matched]

        # Bodies are read at the head SHA, which sidesteps branch-name guessing
        # and pins content to the state the commit range actually produced.
        def fetch_body(post):
            url = f"{RAW}/{repo}/{head_sha}/{quote(post['path'])}"
            text = get_text(url, args.timeout)
            limit = (
                args.cosmetic_max_chars
                if post["change_class"] == "cosmetic"
                else args.max_chars
            )
            text, dropped = clip(text, limit)
            if dropped:
                post["content_truncated"] = True
                if post["change_class"] == "substantive":
                    warnings.append(
                        f"{post['path']}: {dropped} chars omitted from the middle "
                        f"(post exceeds the {limit}-char cap); head and tail are intact."
                    )
            post["content"] = text

        def fetch_dates(post):
            post["commit_dates"] = file_commit_dates(repo, post["path"], since, args.timeout)

        jobs = [(fetch_body, p) for p in posts]
        if want_dates:
            jobs += [(fetch_dates, p) for p in posts]

        if jobs:
            with ThreadPoolExecutor(max_workers=DEFAULT_WORKERS) as pool:
                list(pool.map(lambda job: job[0](job[1]), jobs))

    except HTTPError as e:
        message = rate_limit_message(e) or f"HTTP {e.code} from {e.url}"
        print(json.dumps({**result, "error": message}, indent=2))
        sys.exit(1)
    except (OSError, ValueError, KeyError) as e:
        # URLError and socket timeouts are OSError subclasses; ValueError covers
        # malformed JSON, KeyError an unexpected response shape.
        print(json.dumps({**result, "error": f"{type(e).__name__}: {e}"}, indent=2))
        sys.exit(1)

    posts.sort(key=lambda p: p["path"])
    print(json.dumps({**result, "posts": posts, "warnings": warnings}, indent=2))


if __name__ == "__main__":
    main()
