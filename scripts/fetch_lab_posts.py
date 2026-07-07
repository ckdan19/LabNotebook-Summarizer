#!/usr/bin/env python3
"""Fetch genefish lab notebook posts from the last 7 days via WordPress REST API."""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from urllib.request import urlopen
from urllib.error import URLError

API_URL = "https://public-api.wordpress.com/rest/v1.1/sites/genefish.wordpress.com/posts/?number=20"
DAYS = 7


def strip_html(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"&hellip;", "...", text)
    text = re.sub(r"&[a-z]+;", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_date(date_str: str) -> datetime:
    # WordPress returns ISO 8601 with offset, e.g. "2026-07-06T17:57:23-07:00"
    return datetime.fromisoformat(date_str)


def main():
    cutoff = datetime.now(timezone.utc) - timedelta(days=DAYS)

    try:
        with urlopen(API_URL, timeout=15) as resp:
            data = json.load(resp)
    except URLError as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    recent = []
    for post in data.get("posts", []):
        post_date = parse_date(post["date"])
        if post_date < cutoff:
            continue
        recent.append(
            {
                "author": post["author"]["name"],
                "date": post_date.strftime("%Y-%m-%d"),
                "title": post["title"],
                "url": post["URL"],
                "content": strip_html(post.get("content", "") or post.get("excerpt", "")),
            }
        )

    print(json.dumps({"week_start": cutoff.strftime("%Y-%m-%d"), "posts": recent}, indent=2))


if __name__ == "__main__":
    main()
