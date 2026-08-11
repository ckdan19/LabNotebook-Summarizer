#!/usr/bin/env python3
"""Fetch lab notebook posts from the last N days via the WordPress.com REST API."""

import argparse
import html
import json
import re
import sys
from datetime import datetime, timezone, timedelta
from urllib.parse import urlencode
from urllib.request import urlopen

DEFAULT_SITE = "genefish.wordpress.com"
DEFAULT_DAYS = 7
DEFAULT_PER_PAGE = 100  # largest page size the v1.1 API accepts
DEFAULT_MAX_PAGES = 10
DEFAULT_TIMEOUT = 15

API_BASE = "https://public-api.wordpress.com/rest/v1.1/sites/{site}/posts/"

SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b[^>]*>.*?</\1\s*>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")


def strip_html(raw: str) -> str:
    """Turn a WordPress HTML field into plain text."""
    if not raw:
        return ""
    # Drop <script>/<style> bodies first — removing only the tags would leave their
    # contents behind as prose. Unescape after tag removal so that an escaped
    # "&lt;div&gt;" in the source survives as literal text instead of being stripped.
    text = SCRIPT_STYLE_RE.sub(" ", raw)
    text = TAG_RE.sub(" ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def parse_date(date_str: str):
    """Parse a WordPress date, e.g. "2026-07-06T17:57:23-07:00". None if unparseable."""
    if not date_str:
        return None
    text = date_str.strip()
    if text.endswith(("Z", "z")):
        # fromisoformat cannot read a "Z" suffix before Python 3.11.
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed


def fetch_page(site: str, per_page: int, page: int, timeout: int) -> dict:
    query = urlencode({"number": per_page, "page": page})
    with urlopen(API_BASE.format(site=site) + "?" + query, timeout=timeout) as resp:
        return json.load(resp)


def collect_posts(site: str, cutoff: datetime, per_page: int, max_pages: int, timeout: int):
    """Page through the site's posts (newest first) until one predates the cutoff."""
    posts, warnings = [], []
    complete = False

    for page in range(1, max_pages + 1):
        batch = fetch_page(site, per_page, page, timeout).get("posts") or []
        if not batch:
            complete = True  # ran out of posts entirely
            break

        for post in batch:
            post_date = parse_date(post.get("date"))
            if post_date is None:
                warnings.append(
                    f"Skipped post {post.get('ID', '?')}: unreadable date {post.get('date')!r}"
                )
                continue
            if post_date < cutoff:
                complete = True
                break
            posts.append(
                {
                    "author": (post.get("author") or {}).get("name", "Unknown"),
                    "date": post_date.strftime("%Y-%m-%d"),
                    "title": strip_html(post.get("title", "")),
                    "url": post.get("URL", ""),
                    "content": strip_html(post.get("content") or post.get("excerpt") or ""),
                    # WordPress returns categories as an object keyed by category name;
                    # downstream consumers only need the names.
                    "categories": sorted((post.get("categories") or {}).keys()),
                }
            )

        if complete:
            break
    else:
        warnings.append(
            f"Stopped after {max_pages} pages without reaching the cutoff — "
            "the result may be missing older posts in this window."
        )

    return posts, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", default=DEFAULT_SITE, help="WordPress.com site domain")
    parser.add_argument("--days", type=int, default=DEFAULT_DAYS, help="size of the window in days")
    parser.add_argument("--per-page", type=int, default=DEFAULT_PER_PAGE, help="posts per API page")
    parser.add_argument("--max-pages", type=int, default=DEFAULT_MAX_PAGES, help="page cap")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="per-request seconds")
    args = parser.parse_args()

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)

    try:
        posts, warnings = collect_posts(
            args.site, cutoff, args.per_page, args.max_pages, args.timeout
        )
    except (OSError, json.JSONDecodeError) as e:
        # URLError, HTTPError and socket timeouts are all OSError subclasses.
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    print(
        json.dumps(
            {
                "week_start": cutoff.strftime("%Y-%m-%d"),
                "posts": posts,
                "warnings": warnings,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
