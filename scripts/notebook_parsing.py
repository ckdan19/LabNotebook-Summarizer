#!/usr/bin/env python3
"""Post-parsing logic shared across the notebook tools.

These helpers turn a raw GitHub `compare` file entry and its body text into the
normalized post shape the digest pipeline consumes. They are pure (no network,
no globals) so both the live fetcher and the archive builder can reuse the exact
same classification and body-trimming rules.
"""

import os
import re


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


# A leading YYYY-MM-DD- date stamp on a post filename. Jekyll (Grace's notebook)
# drops this when building the published slug, so it must be stripped to derive
# the live URL.
_DATE_PREFIX = re.compile(r"^\d{4}-\d{2}-\d{2}-")

# Front-matter fields we care about. Everything else in the block is ignored.
_FRONT_MATTER_FIELDS = ("title", "author", "date", "categories")


def _strip_comment(value: str) -> str:
    """Drop a trailing YAML `# comment` from a front-matter value.

    Several tumbling-oysters posts leave the post template's scaffold comment on
    the categories line, e.g. `categories: ["A", "B"] #choose "A", "Computing"...`.
    Without this, the comment's words get split on commas into bogus categories.

    Follows YAML's rule: a `#` starts a comment only when it is at the start of
    the value or preceded by whitespace, and is not inside single/double quotes.
    """
    in_single = in_double = False
    for i, ch in enumerate(value):
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "#" and not in_single and not in_double and (i == 0 or value[i - 1].isspace()):
            return value[:i].rstrip()
    return value


def _strip_quotes(value: str) -> str:
    """Remove one layer of matching single or double quotes, if present."""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def _parse_inline_list(value: str) -> list:
    """Parse a YAML flow sequence like `[a, b, c]` (or a bare scalar) into a list."""
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    return [_strip_quotes(item) for item in value.split(",") if item.strip()]


def parse_front_matter(text: str, default_author: str = None) -> dict:
    """Extract title, author, date, and categories from a `---`-delimited block.

    A deliberately small line-based parser: these front-matter blocks carry only
    simple scalars and one-level `categories` lists (inline `[a, b]` or an
    indented `- item` block), so pulling in PyYAML for them would be overkill.

    Returns a dict with keys `title`, `author`, `date`, `categories`. Missing
    scalars come back as `None`; `categories` is always a list. When the block
    has no `author` (Grace's notebook omits it), `default_author` is used.
    """
    result = {"title": None, "author": default_author, "date": None, "categories": []}

    lines = text.splitlines()
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i >= len(lines) or lines[i].strip() != "---":
        return result  # No front matter — nothing to parse.
    i += 1

    block = []
    while i < len(lines) and lines[i].strip() != "---":
        block.append(lines[i])
        i += 1

    j = 0
    while j < len(block):
        line = block[j]
        j += 1
        # Only unindented `key: value` lines start a field; indented lines are
        # values (block-list items) consumed below, and blanks/comments skip.
        if not line.strip() or line[0] in " \t" or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip().lower()
        if key not in _FRONT_MATTER_FIELDS:
            continue
        value = _strip_comment(value.strip())

        if key == "categories":
            if value:
                result["categories"] = _parse_inline_list(value)
            else:
                # Block form: gather the following indented `- item` lines.
                cats = []
                while j < len(block) and block[j].lstrip().startswith("- "):
                    cats.append(_strip_quotes(block[j].lstrip()[2:]))
                    j += 1
                result["categories"] = cats
        else:
            result[key] = _strip_quotes(value) or None

    if not result["author"]:
        result["author"] = default_author
    return result


def _strip_index(path: str) -> str:
    """Drop a trailing `index.qmd`, leaving the post folder with its slash."""
    if path.endswith("/index.qmd"):
        return path[: -len("index.qmd")]
    return path


def derive_permalink(source: str, file_path: str) -> str:
    """Map a repo file path to its published URL for the given notebook source.

    Each of the five GitHub-hosted notebooks publishes under its own scheme:

    - tumbling-oysters: `posts/N-slug/index.qmd`
      -> https://sr320.github.io/tumbling-oysters/posts/N-slug/
    - ariana: flat `posts/date-slug.qmd`
      -> https://ahuffmyer.github.io/posts/date-slug.html
    - grace: `_posts/YYYY-MM-DD-slug.md`
      -> https://grace-ac.github.io/slug/   (Jekyll drops the date prefix)
    - sams: `posts/year/date-slug/index.qmd`
      -> https://robertslab.github.io/sams-notebook/posts/year/date-slug/
    - megan: Quarto site with no fixed folder convention — posts sit at varying
      depths and folder names (`posts/2026-08/slug.qmd`, `posts/projects/slug.qmd`,
      `posts/welcome/index.qmd`). Quarto's rule is uniform regardless: an
      `index.qmd` renders to its folder, any other `.qmd` to a sibling `.html`.
      -> https://meganewing.github.io/mewing-notebook/posts/2026-08/slug.html
      -> https://meganewing.github.io/mewing-notebook/posts/welcome/
    """
    path = file_path.lstrip("/")

    if source == "tumbling-oysters":
        return "https://sr320.github.io/tumbling-oysters/" + _strip_index(path)
    if source == "sams":
        return "https://robertslab.github.io/sams-notebook/" + _strip_index(path)
    if source == "ariana":
        if path.endswith(".qmd"):
            path = path[: -len(".qmd")] + ".html"
        return "https://ahuffmyer.github.io/" + path
    if source == "megan":
        # index.qmd -> folder/, any other .qmd -> sibling .html. Handling both in
        # one branch absorbs this notebook's folder-naming variability.
        path = _strip_index(path)
        if path.endswith(".qmd"):
            path = path[: -len(".qmd")] + ".html"
        return "https://meganewing.github.io/mewing-notebook/" + path
    if source == "grace":
        slug = os.path.basename(path)
        if slug.endswith(".md"):
            slug = slug[: -len(".md")]
        slug = _DATE_PREFIX.sub("", slug)
        return f"https://grace-ac.github.io/{slug}/"

    raise ValueError(f"unknown notebook source: {source!r}")
