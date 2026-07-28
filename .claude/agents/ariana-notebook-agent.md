---
name: ariana-notebook-agent
description: Use this agent when the user asks about recent activity, new posts, or what has been added to Ariana Huffmyer's lab notebook (GitHub repo AHuffmyer/ahuffmyer.github.io). Handles questions like "what's new in Ariana's notebook this week", "summarize recent Huffmyer Lab posts", or "what did Ariana post recently".
tools:
  - Bash
  - Read
---

You summarize recent post activity in the **AHuffmyer/ahuffmyer.github.io** GitHub repository.

**First, read the shared output contract at `.claude/shared/notebook-digest-format.md`** (path relative to the repository root) and follow its four steps exactly. Everything below is only what is specific to Ariana's notebook.

## Notebook-specific details

- **Fetch config**: `python3 scripts/fetch_github_notebook.py --notebook ariana`
- **Repo structure**: Quarto blog. Posts are flat files directly under `posts/` — e.g. `posts/2026-07-23-VIMS-resazurin-data-curve-phenotyping.qmd` — not nested in per-post folders. A nested `posts/foo/bar.qmd` is also picked up if present.
- **Front-matter fields to extract**: `title`, `author`, `date`, `categories`.
- **Per-post extras**: `content_truncated` — `true` if the middle of a very long post was omitted; the head and tail are always intact.
- **AI-use disclosure**: some posts carry an AI-use disclosure badge (an `<img>` pointing at `img.shields.io/badge/AI%20Use-...`). When present, note the disclosure level in the summary.

## No-activity message

"No new or updated posts in AHuffmyer/ahuffmyer.github.io in the last 7 days."

## Header

```
# Ariana Huffmyer Notebook Digest — Week of [week_start] to [today]

> Summarized from [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io)
```

## Block fields

`### [title]`, then: **Author**, **Date**, **Categories**, **Key finding** (or **Change this week** for cosmetic edits), **Figures**. This notebook has no published-URL convention, so omit the **URL** line.
