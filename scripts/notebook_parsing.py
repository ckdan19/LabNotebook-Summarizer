#!/usr/bin/env python3
"""Post-parsing logic shared across the notebook tools.

These helpers turn a raw GitHub `compare` file entry and its body text into the
normalized post shape the digest pipeline consumes. They are pure (no network,
no globals) so both the live fetcher and the archive builder can reuse the exact
same classification and body-trimming rules.
"""


def clip(text: str, limit: int) -> tuple:
    """Trim `text` to `limit` chars, keeping both ends.

    Front matter sits at the top of a post and conclusions at the bottom, so a
    plain head-only truncation would drop exactly the part worth summarizing.
    Returns (text, dropped_chars) with dropped_chars 0 when nothing was cut.
    """
    if len(text) <= limit:
        return text, 0
    head = int(limit * 0.7)
    tail = limit - head
    dropped = len(text) - limit
    marker = f"\n\n[... {dropped} characters omitted from the middle of this post ...]\n\n"
    return text[:head] + marker + text[-tail:], dropped


def build_post(repo: str, entry: dict, sha: str, cosmetic_lines: int) -> dict:
    additions = entry.get("additions", 0)
    deletions = entry.get("deletions", 0)
    status = entry.get("status", "modified")
    cosmetic = status == "modified" and (additions + deletions) <= cosmetic_lines

    post = {
        "path": entry["filename"],
        "status": status,
        "additions": additions,
        "deletions": deletions,
        "blob_url": f"https://github.com/{repo}/blob/{sha}/{entry['filename']}",
        "change_class": "cosmetic" if cosmetic else "substantive",
    }
    if entry.get("previous_filename"):
        post["previous_filename"] = entry["previous_filename"]
    if cosmetic:
        # The diff shows what the edit did; the body is still needed for the
        # post's title and categories, but only a trimmed slice of it.
        post["patch"] = entry.get("patch", "")
    return post
