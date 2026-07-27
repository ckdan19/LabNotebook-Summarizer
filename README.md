# LabNotebook-Summarizer

A tool that summarizes lab notebook posts from [Roberts Lab](https://robertslab.github.io/) on a weekly basis, connecting ideas across multiple researchers and linking lab findings to recent published literature.

## Overview

LabNotebook-Summarizer aggregates posts from five different lab notebook sources, produces structured Markdown digests, detects cross-notebook patterns and shared themes, and connects findings to recent PubMed and bioRxiv papers — all using Claude Code skills and a Python data-fetching script.

## Repository Structure

```
LabNotebook-Summarizer/
├── scripts/
│   ├── fetch_lab_posts.py   # Fetches posts from genefish.wordpress.com via WordPress REST API
│   └── publish_digest.py    # Converts a digest to sanitized HTML and posts it as a WP draft
├── digests/                 # Generated weekly digest files (Markdown)
├── memory/                  # Skill documentation and design notes
│   ├── MEMORY.md
│   └── skill-literature-connector.md
└── README.md
```

## Data Sources

The tool currently monitors five notebook sources:

| Source | Platform | Location |
|---|---|---|
| Tumbling Oysters (Steven Roberts) | GitHub | [sr320/tumbling-oysters](https://github.com/sr320/tumbling-oysters) |
| Ariana Huffmyer Lab Notebook | GitHub | [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io) |
| Sam's Notebook (Sam White) | GitHub | [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook) |
| Grace Crandall's Notebook | GitHub | [RobertsLab/grace-crandall-notebook](https://github.com/RobertsLab/grace-crandall-notebook) |
| Genefish WordPress | WordPress | [genefish.wordpress.com](https://genefish.wordpress.com) |

## Scripts

### `scripts/fetch_lab_posts.py`

Queries the WordPress REST API for [genefish.wordpress.com](https://genefish.wordpress.com) and returns a JSON list of posts from the last 7 days. Each post includes the author, date, title, URL, and plain-text content. The script pages through the API until it reaches the start of the window, so weeks with more posts than a single page are not truncated.

```bash
python3 scripts/fetch_lab_posts.py
```

Options: `--site` (default `genefish.wordpress.com`), `--days` (7), `--per-page` (100), `--max-pages` (10), `--timeout` (15).

Output is JSON written to stdout:

```json
{
  "week_start": "2026-07-07",
  "posts": [
    {
      "author": "Cas Daniel",
      "date": "2026-07-08",
      "title": "Lab Notebook Summarizer: Building a Weekly Digest Tool",
      "url": "https://genefish.wordpress.com/2026/07/08/...",
      "content": "..."
    }
  ],
  "warnings": []
}
```

`warnings` lists non-fatal problems — a post skipped for an unreadable date, or a window that hit `--max-pages` before reaching the cutoff. On a network or API failure the script prints `{"error": "..."}` to stdout and exits 1.

### `scripts/publish_digest.py`

Converts a Markdown digest to sanitized HTML and posts it to WordPress.com as a **draft**. Used by the `wordpress-publisher` skill.

```bash
python3 scripts/publish_digest.py digests/full-lab-digest-2026-07-21.md --dry-run
```

The first line of the digest must be a `# ` heading; it becomes the post title and is dropped from the body. `--dry-run` converts and sanitizes without reading the token or contacting the API. Options: `--site`, `--token-file` (default `~/.config/LabNotebook-Summarizer/wp_token`).

Handling notes:

- The token is read by the script and sent only as an `Authorization` header — never in argv (visible via `ps`), never printed, and redacted from any API response it reports.
- Digest content is never passed through a shell; only the file path is a command-line argument. Digests summarize third-party posts, so a title containing `$(...)` must not be interpolatable.
- The HTML body is filtered against a tag allowlist before sending: `<script>`, `<style>`, `<iframe>`, inline event handlers, and non-`http(s)`/`mailto` URLs are dropped.
- Status is hardcoded to `draft`.

Requires `python-markdown` (`pip install markdown`) or `pandoc`. Neither is a stdlib module, and the script reports a clear error if both are absent.

## Claude Code Skills

The summarization and analysis work is performed by Claude Code skills:

| Skill | Description |
|---|---|
| `weekly-lab-digest` | Fetches WordPress posts and produces a per-author digest |
| `tumbling-oysters-agent` | Reads Steven Roberts' GitHub notebook and summarizes recent posts |
| `full-lab-digest` | Runs all five source subagents in parallel and compiles a combined digest with cross-notebook pattern analysis and literature connections |
| `literature-connector` | Queries PubMed E-utilities for papers published in the last 12 months and categorizes their relationship to a given lab finding (Supports / Conflicts / Adds context / Suggests next step) |

## Digests

Generated digests are saved to the `digests/` directory as Markdown files, named by date range. Digest types include:

- **`2026-06-30.md`, `2026-07-07.md`** — WordPress-only weekly digests, grouped by author
- **`tumbling-oysters-YYYY-MM-DD.md`** — Focused digests for Steven Roberts' Tumbling Oysters notebook
- **`full-lab-digest-YYYY-MM-DD.md`** — Full multi-source weekly digests including:
  - Per-notebook summaries (all five sources)
  - Cross-notebook pattern detection (shared species, assays, and themes)
  - Literature connections via PubMed and bioRxiv

### Example cross-notebook connection (from `full-lab-digest-2026-07-21.md`)

> **Thermal stress in Pacific oysters (*C. gigas*) at 35–36°C** — Two independent notebooks document active heat stress experiments on *C. gigas* this week using overlapping temperature ranges: Ariana's notebook (thermal hardening at Point Whitney) and the Genefish WordPress (Hazel's GlycogenGlo assays, Jesse's mortality assessments, and a 36°C incubator entry).

## Requirements

- Python 3.8+ — stdlib only for `fetch_lab_posts.py`
- `python-markdown` (`pip install markdown`) or `pandoc` — only for `publish_digest.py`
- `gh` (authenticated) and `curl` — used by the GitHub notebook subagents
- Claude Code (for running skills)
- Internet access to the WordPress REST API and GitHub
- A WordPress.com API token at `~/.config/LabNotebook-Summarizer/wp_token` (mode 600) — only for publishing

## Related

- [Roberts Lab](https://robertslab.github.io/)
- [genefish.wordpress.com](https://genefish.wordpress.com)
