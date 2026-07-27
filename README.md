# LabNotebook-Summarizer

A tool that summarizes lab notebook posts from [Roberts Lab](https://robertslab.github.io/) on a weekly basis, connecting ideas across multiple researchers and linking lab findings to recent published literature.

## Overview

LabNotebook-Summarizer aggregates posts from five different lab notebook sources, produces structured Markdown digests, detects cross-notebook patterns and shared themes, and connects findings to recent PubMed and bioRxiv papers — all using Claude Code skills and a Python data-fetching script.

## Repository Structure

```
LabNotebook-Summarizer/
├── scripts/
│   └── fetch_lab_posts.py   # Fetches posts from genefish.wordpress.com via WordPress REST API
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

Queries the WordPress REST API for [genefish.wordpress.com](https://genefish.wordpress.com) and returns a JSON list of posts from the last 7 days. Each post includes the author, date, title, URL, and plain-text content.

```bash
python scripts/fetch_lab_posts.py
```

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
  ]
}
```

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

- Python 3.8+ (for `fetch_lab_posts.py`)
- Claude Code (for running skills)
- Internet access to the WordPress REST API and GitHub

## Related

- [Roberts Lab](https://robertslab.github.io/)
- [genefish.wordpress.com](https://genefish.wordpress.com)
