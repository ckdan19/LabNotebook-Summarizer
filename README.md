# LabNotebook-Summarizer

A tool that summarizes lab notebook posts from [Roberts Lab](https://robertslab.github.io/) on a weekly basis, connecting ideas across multiple researchers and linking lab findings to recent published literature.

## Overview

LabNotebook-Summarizer aggregates posts from five different lab notebook sources, produces structured Markdown digests, detects cross-notebook patterns and shared themes, and connects findings to recent PubMed and bioRxiv papers — all using Claude Code skills and a Python data-fetching script.

## For Claude Desktop / GUI Users

You do not need to run any Python yourself. The skills and subagents in this repo are triggered by plain English — open the project in Claude and ask for what you want.

### Setup (once)

1. Install the [Claude desktop app](https://claude.ai/download) and sign in.
2. Clone this repository: `git clone https://github.com/ckdan19/LabNotebook-Summarizer.git`
3. In Claude, open a Claude Code session **with this repository as the working directory**. The skills in `.claude/skills/` and subagents in `.claude/agents/` load automatically from the project folder — if you open a different folder, none of the requests below will work.
4. *(Optional but recommended)* Set `GITHUB_TOKEN` in your environment to raise the GitHub API rate limit. Without it, one full digest run uses about 10 of your 60 hourly calls.
5. *(Only if you want to publish)* Save a WordPress.com API token to `~/.config/LabNotebook-Summarizer/wp_token` with `chmod 600`.

Then just type a request in the chat box.

### What you can ask

**Get the full weekly digest** — the main thing this tool does. Runs all five notebooks in parallel, then adds cross-notebook patterns and literature connections.

> "Give me the full lab digest for this week"
>
> "Summarize all five lab notebooks and save the digest"

**Check one notebook** — faster when you only care about one person.

> "What's new in Ariana's notebook this week?"
>
> "What did Sam post recently?"
>
> "Summarize recent Grace Crandall posts"
>
> "What's new in tumbling-oysters?"
>
> "What did the lab post on WordPress this week?"

**Change the time window** — every request defaults to 7 days but accepts any window, including the full digest.

> "What's new in Sam's notebook over the last 3 weeks?"
>
> "Summarize Ariana's posts from the last 30 days"
>
> "Give me a full lab digest for the last 14 days"

**Connect a finding to the literature** — searches PubMed and preprint servers for the last 12 months and labels each paper *Supports*, *Conflicts*, *Adds context*, or *Suggests next step*.

> "Find recent papers on thermal hardening in Pacific oysters, and compare them to our finding that 35°C exposure improved subsequent survival"

This one needs two things from you: the **topic** to search, and the **specific finding** to compare against. If you leave out the finding, Claude will ask for it — it can't categorize papers without something to categorize them against.

**Publish a digest to WordPress** — always creates a **draft**, never a live post, so you review before it goes public.

> "Publish this week's digest to WordPress"
>
> "Post the July 21 digest as a WordPress draft"

**Ask about past digests** — everything generated is kept in `digests/`.

> "What did we cover in last week's digest?"
>
> "Has anyone mentioned GlycogenGlo assays in the past month of digests?"

### What to expect

- A full digest launches five subagents at once and takes a few minutes. Claude will show them running in parallel — that's normal.
- Digests are written to `digests/` as Markdown. Ask Claude to show you the file if you'd rather read it in the chat.
- A source with no posts that week is reported as "no activity" rather than silently dropped.
- Small edits to a post — a fixed typo or link, six diff lines or fewer — are flagged as cosmetic and are not written up as new science.
- If a notebook fetch fails (rate limit, network), Claude will tell you which source failed instead of quietly returning a partial digest.

## Repository Structure

```
LabNotebook-Summarizer/
├── .claude/
│   ├── skills/              # full-lab-digest, weekly-lab-digest, literature-connector, wordpress-publisher
│   └── agents/              # One subagent per notebook source (five total)
├── scripts/
│   ├── fetch_github_notebook.py  # Fetches posts changed in the last N days from a GitHub notebook
│   ├── fetch_lab_posts.py   # Fetches posts from genefish.wordpress.com via WordPress REST API
│   └── publish_digest.py    # Converts a digest to sanitized HTML and posts it as a WP draft
├── text_to_speech/          # Optional, isolated Kokoro / Chatterbox-Nano digest narration
├── digests/                 # Generated digest files (Markdown)
├── memory/                  # Skill documentation and design notes
│   ├── MEMORY.md
│   └── skill-literature-connector.md
├── ROADMAP.md               # Planned improvements, roughly in priority order
└── README.md
```

## Data Sources

The tool currently monitors five notebook sources:

| Source | Platform | Location |
|---|---|---|
| Tumbling Oysters (Steven Roberts) | GitHub | [sr320/tumbling-oysters](https://github.com/sr320/tumbling-oysters) |
| Ariana Huffmyer Lab Notebook | GitHub | [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io) |
| Sam's Notebook (Sam White) | GitHub | [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook) |
| Grace Crandall's Notebook | GitHub | [grace-ac/grace-ac.github.io](https://github.com/grace-ac/grace-ac.github.io) |
| Genefish WordPress | WordPress | [genefish.wordpress.com](https://genefish.wordpress.com) |

## Scripts

### `scripts/fetch_github_notebook.py`

Returns JSON describing every notebook post changed in the last 7 days — or any window, via `--days` — in one of the four GitHub-hosted notebooks, for use by the notebook subagents:

```bash
python3 scripts/fetch_github_notebook.py --notebook sams        # or: ariana, grace, tumbling-oysters
python3 scripts/fetch_github_notebook.py --notebook grace --days 21
```

Each post carries its `content`, `status`, diff line counts, and a `change_class` of `substantive` or `cosmetic`. Cosmetic edits — modified posts whose diff is 6 lines or fewer — report their `patch` and only the opening of the post, so a one-line link fix is not summarized as new science.

Three design points keep this fast and correct:

- **Two API calls locate everything.** A commit listing plus a single `compare` over the whole range replaces one API call per commit.
- **Post bodies are read at the commit SHA**, not off a branch name. `sams-notebook` and `grace-ac.github.io` default to `master` while the other two use `main`; reading at the SHA sidesteps that difference entirely.
- **Long posts are clipped from the middle**, never the end, so front matter and conclusions both survive. A `content_truncated` flag and a warning mark any post this affected.

Set `GITHUB_TOKEN` (or `GH_TOKEN`) to raise the GitHub API rate limit from 60 to 5,000 requests per hour. Without it a full five-source digest run consumes roughly 10 of the 60 available calls. An exhausted limit produces a single actionable error rather than a partial digest.

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

### Digest audio (`text_to_speech/`)

Creates a narrated WAV file from any completed Markdown digest using either Kokoro
or Chatterbox-Nano. The audio layer is optional and isolated: engine dependencies
are installed separately and the existing fetch, digest, and publishing paths do
not import them.

Preview the speech-ready text without installing a model:

```bash
python3 -m text_to_speech digests/full-lab-digest-2026-07-28-7d.md --dry-run
```

See [`text_to_speech/README.md`](text_to_speech/README.md) for Python 3.11 setup,
provider installation, voice options, and generation commands.

## Claude Code Skills

The summarization and analysis work is performed by Claude Code skills in `.claude/skills/`:

| Skill | Description |
|---|---|
| `full-lab-digest` | Runs all five source subagents in parallel and compiles a combined digest with cross-notebook pattern analysis and literature connections |
| `weekly-lab-digest` | Fetches WordPress posts and produces a per-author digest |
| `literature-connector` | Queries PubMed and the preprint servers indexed by Europe PMC (bioRxiv, medRxiv, Research Square, …) for papers published in the last 12 months and categorizes their relationship to a given lab finding (Supports / Conflicts / Adds context / Suggests next step) |
| `wordpress-publisher` | Converts a digest to sanitized HTML and posts it to genefish.wordpress.com as a draft |
| `digest-audio` | Generates an audio version of a completed digest with Kokoro or Chatterbox-Nano |

Each notebook source is read by its own subagent in `.claude/agents/` — `tumbling-oysters-agent`, `ariana-notebook-agent`, `sams-notebook-agent`, `grace-notebook-agent`, and `wordpress-agent`. Ask about a single notebook and Claude uses just that one; `full-lab-digest` launches all five.

### Changing the time window

Every source defaults to a 7-day window, and every source accepts a different one. Ask for the window in plain language and the skill threads it through the subagents, the date range in the header, and the digest footer:

> give me a full lab digest for the last 14 days

The same applies to a single notebook ("what's new in Sam's notebook over the past month"). Under the hood this becomes `--days N` on `fetch_github_notebook.py` or `fetch_lab_posts.py`. The window is also encoded in the digest filename (`full-lab-digest-2026-07-27-14d.md`), so a 14-day digest does not overwrite the 7-day one that ends on the same date.

## Digests

Generated digests are saved to the `digests/` directory as Markdown files, named by date range. Digest types include:

- **`2026-06-30.md`, `2026-07-07.md`** — WordPress-only weekly digests, grouped by author
- **`tumbling-oysters-YYYY-MM-DD.md`** — Focused digests for Steven Roberts' Tumbling Oysters notebook
- **`full-lab-digest-YYYY-MM-DD-Nd.md`** — Full multi-source digests, named by end date and window length (`-7d` by default). Files predating this convention omit the `-Nd` suffix. Each includes:
  - Per-notebook summaries (all five sources)
  - Cross-notebook pattern detection (shared species, assays, and themes)
  - Literature connections via PubMed and bioRxiv

### Example cross-notebook connection (from `full-lab-digest-2026-07-21.md`)

> **Thermal stress in Pacific oysters (*C. gigas*) at 35–36°C** — Two independent notebooks document active heat stress experiments on *C. gigas* this week using overlapping temperature ranges: Ariana's notebook (thermal hardening at Point Whitney) and the Genefish WordPress (Hazel's GlycogenGlo assays, Jesse's mortality assessments, and a 36°C incubator entry).

## Requirements

- Python 3.8+ — stdlib only for `fetch_lab_posts.py` and `fetch_github_notebook.py`
- Python 3.10+ (3.11 recommended) — only for the optional Kokoro/Chatterbox-Nano audio layer
- `python-markdown` (`pip install markdown`) or `pandoc` — only for `publish_digest.py`
- `GITHUB_TOKEN` or `GH_TOKEN` in the environment — optional, but raises the GitHub API rate limit from 60 to 5,000 requests/hour. The `gh` CLI is **not** required.
- Claude Code (for running skills)
- Internet access to the WordPress REST API and GitHub
- A WordPress.com API token at `~/.config/LabNotebook-Summarizer/wp_token` (mode 600) — only for publishing

## Related

- [Roberts Lab](https://robertslab.github.io/)
- [genefish.wordpress.com](https://genefish.wordpress.com)
