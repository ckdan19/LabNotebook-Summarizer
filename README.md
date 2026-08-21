# LabNotebook-Summarizer

A tool that summarizes lab notebook posts from [Roberts Lab](https://robertslab.github.io/) on a weekly basis, connecting ideas across multiple researchers and linking lab findings to recent published literature.

## Overview

LabNotebook-Summarizer aggregates posts from five different lab notebook sources, produces structured Markdown digests, detects cross-notebook patterns and shared themes (including multi-week arcs found by looking back through the lab's own archive), and connects findings to recent PubMed and bioRxiv papers — all using Claude Code skills and a small set of Python helper scripts. It also keeps a searchable local archive of every post the five notebooks have ever published, can narrate a digest to audio, and can publish to WordPress.

## For Claude Desktop / GUI Users

You do not need to run any Python yourself. The skills and subagents in this repo are triggered by plain English — open the project in Claude and ask for what you want.

### Setup (once)

1. Install the [Claude desktop app](https://claude.ai/download) and sign in.
2. Clone this repository: `git clone https://github.com/ckdan19/LabNotebook-Summarizer.git`
3. In Claude, open a Claude Code session **with this repository as the working directory**. The skills in `.claude/skills/` and subagents in `.claude/agents/` load automatically from the project folder — if you open a different folder, none of the requests below will work.
4. *(Optional but recommended)* Set `GITHUB_TOKEN` in your environment to raise the GitHub API rate limit. Without it, one full digest run uses about 10 of your 60 hourly calls.
5. *(Only if you want to publish)* Save a WordPress.com API token to `~/.config/LabNotebook-Summarizer/wp_token` with `chmod 600`. The same token is used for publishing posts and for uploading digest audio.
6. *(Only if you want the archive search)* Build the local post archive once with `python3 scripts/build_archive.py` (see [Scripts](#scriptsbuild_archivepy)).

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

**Publish a digest to WordPress** — the `wordpress-publisher` skill creates a **draft**, so you review before it goes public.

> "Publish this week's digest to WordPress"
>
> "Post the July 21 digest as a WordPress draft"

**Run the daily literature post** — a narrow daily counterpart to the full digest. It takes only the last day's posts that describe a real scientific finding, runs the literature connector on each, and assembles them into one post. **This one can publish live**, but only while [`AUTHORIZATION.md`](AUTHORIZATION.md) carries the authorization marker; otherwise it falls back to a draft. See [Automated publishing](#automated-publishing) before running it.

> "Run today's literature connections"
>
> "Do the daily lit post"

**Search the whole lab archive** — not just the digests, but every post the five notebooks have ever published, full-text. Answers come grouped by researcher with a source link for every claim.

> "Has anyone in the lab done DNA methylation analysis on oysters?"
>
> "What do we know about resazurin assays?"

The archive lives in a local SQLite database that you build (and periodically refresh) with `python3 scripts/build_archive.py`. If it hasn't been built, the skill tells you rather than searching nothing.

**Ask about past digests** — everything generated is kept in `digests/`, indexed in [`digests/README.md`](digests/README.md).

> "What did we cover in last week's digest?"
>
> "Has anyone mentioned GlycogenGlo assays in the past month of digests?"
>
> "Update the digest index"

**Narrate and publish digest audio** — generates two spoken editions of the latest full digest (summaries-only and with-analysis), uploads them to the WordPress media library, and publishes a **new, separate** post linking to both. It does not touch the original digest post.

> "Publish audio for the latest digest"

### What to expect

- A full digest launches five subagents at once and takes a few minutes. Claude will show them running in parallel — that's normal.
- Digests are written to `digests/` as Markdown. Ask Claude to show you the file if you'd rather read it in the chat.
- **A post is only ever written up once.** The full digest records every post URL it covers in `digests/.digest-state.json`, so a post that still falls inside the requested window but appeared in an earlier digest is skipped rather than repeated. That file is committed to the repo so the de-duplication holds across machines and collaborators. If you *want* a post covered again, ask Claude to remove its URL from the state file.
- A source with no posts that week is reported as "no activity" rather than silently dropped.
- Small edits to a post — a fixed typo or link, six diff lines or fewer — are flagged as cosmetic and are not written up as new science.
- If a notebook fetch fails (rate limit, network), Claude will tell you which source failed instead of quietly returning a partial digest.
- The full digest's **Historical Connections** subsection needs the local archive. If `.cache/archive.db` has not been built, that one subsection is skipped and the rest of the digest is produced normally — the digest never builds or rebuilds the database on its own.
- Most publishing paths produce a draft. The two exceptions that go live are called out explicitly in [Automated publishing](#automated-publishing).

## Repository Structure

```
LabNotebook-Summarizer/
├── .claude/
│   ├── skills/              # full-lab-digest, weekly-lab-digest, daily-literature-post,
│   │                        #   literature-connector, lab-archive, digest-index,
│   │                        #   wordpress-publisher, digest-audio, digest-audio-publish
│   ├── agents/              # One subagent per notebook source (five total)
│   └── shared/
│       └── notebook-digest-format.md  # Output contract shared by the four GitHub agents
├── scripts/
│   ├── fetch_github_notebook.py  # Fetches posts changed in the last N days from a GitHub notebook
│   ├── fetch_lab_posts.py   # Fetches posts from genefish.wordpress.com via WordPress REST API
│   ├── notebook_parsing.py  # Shared post parsing/classification used by the two fetchers above
│   ├── build_archive.py     # Builds the full-history SQLite archive at .cache/archive.db
│   ├── publish_digest.py    # Converts a digest to sanitized HTML and posts it to WordPress
│   └── upload_media.py      # Uploads a local file (digest audio) to the WP media library
├── text_to_speech/          # Optional, isolated Kokoro / Chatterbox-Nano digest narration
├── tests/                   # Stdlib unittest suite for the scripts and the audio layer
├── digests/                 # Generated digest files (Markdown)
│   ├── README.md            # Auto-generated index of every digest (digest-index skill)
│   ├── .digest-state.json   # URLs already covered, so no post is digested twice
│   └── .literature-state.json  # URLs already connected + the daily-post publish log
├── memory/                  # Skill documentation and design notes
│   ├── MEMORY.md
│   └── skill-literature-connector.md
├── docs/
│   └── adding-a-notebook.md  # How to add a new GitHub-hosted notebook source
├── AUTHORIZATION.md         # The switch that allows the daily literature post to publish live
├── ROADMAP.md               # Planned improvements, roughly in priority order
└── README.md

.cache/archive.db            # Full-history post archive (git-ignored; built on demand)
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

Adding another GitHub-hosted notebook is a documented, eleven-file procedure — see
[docs/adding-a-notebook.md](docs/adding-a-notebook.md).

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

Options: `--notebook` (required: `ariana`, `grace`, `sams`, `tumbling-oysters`), `--days` (7), `--cosmetic-lines` (6 — the changed-line threshold below which a modified post counts as cosmetic), `--max-chars` (60000 — per-post content cap), `--cosmetic-max-chars` (4000 — tighter cap for cosmetic edits), `--file-dates` (fetch per-file commit dates, one extra API call per post), `--timeout` (20).

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

### `scripts/notebook_parsing.py`

Not a command-line tool — a pure helper module (no network, no globals) holding the post-parsing rules shared by `fetch_github_notebook.py` and `build_archive.py`: the cosmetic/substantive classification, the middle-out body clipping, front-matter parsing, and permalink derivation. Both the live fetcher and the archive builder go through it so a post is classified and trimmed identically either way.

### `scripts/build_archive.py`

Walks each source's **entire** history — not the 7-day window the live fetchers use — into a local SQLite database at `.cache/archive.db` with an FTS5 full-text index, so the `lab-archive` skill can search everything the labs have ever published. The database is git-ignored; each clone builds its own.

```bash
python3 scripts/build_archive.py                          # all five sources
python3 scripts/build_archive.py --sources sams grace     # a subset
```

The build is **incremental and resumable**. For the four GitHub notebooks it lists a repo's whole posts tree in a single git-tree call and compares each file's blob SHA against what is already stored, so unchanged posts are skipped without re-fetching. Every processed post is committed as it goes, so an interrupted run — a dropped connection, an exhausted rate limit — simply resumes on the next invocation. The WordPress notebook has no blob SHA, so it is deduplicated by URL instead. Re-run it whenever you want the archive current.

Options: `--sources` (default: all five — `tumbling-oysters`, `grace`, `ariana`, `sams`, `wordpress`). A first full build makes a lot of GitHub API calls; set `GITHUB_TOKEN` before running it.

### `scripts/publish_digest.py`

Converts a Markdown digest to sanitized HTML and posts it to WordPress.com. Used by the `wordpress-publisher`, `daily-literature-post`, and `digest-audio-publish` skills.

```bash
python3 scripts/publish_digest.py digests/full-lab-digest-2026-07-21.md --dry-run
```

The first line of the digest must be a `# ` heading; it becomes the post title and is dropped from the body. `--dry-run` converts and sanitizes without reading the token or contacting the API. Options: `--site`, `--token-file` (default `~/.config/LabNotebook-Summarizer/wp_token`), `--category NAME` (repeatable; created if it does not exist), `--status {draft,publish}`.

Handling notes:

- The token is read by the script and sent only as an `Authorization` header — never in argv (visible via `ps`), never printed, and redacted from any API response it reports.
- Digest content is never passed through a shell; only the file path is a command-line argument. Digests summarize third-party posts, so a title containing `$(...)` must not be interpolatable.
- The HTML body is filtered against a tag allowlist before sending: `<script>`, `<style>`, `<iframe>`, inline event handlers, and non-`http(s)`/`mailto` URLs are dropped.
- **Status defaults to `draft` for every caller.** Publishing live requires an explicit `--status publish`, which only the `daily-literature-post` and `digest-audio-publish` skills pass — see [Automated publishing](#automated-publishing).
- The script always POSTs to `posts/new/`, so it creates a new post and never edits an existing one.

Requires `python-markdown` (`pip install markdown`) or `pandoc`. Neither is a stdlib module, and the script reports a clear error if both are absent.

### `scripts/upload_media.py`

Uploads a local file to the WordPress.com media library and returns its URL. Used by the `digest-audio-publish` skill to host digest narration WAVs before publishing the post that links to them.

```bash
python3 scripts/upload_media.py text_to_speech/output/digest-summaries.wav --dry-run
```

Takes a file **path** only — the bytes are sent as a multipart `media[]` field, never interpolated into a shell command. Token handling mirrors `publish_digest.py`: read from disk by this process, passed only in a request header, never in argv or output. Options: `--site`, `--token-file`, `--title`, `--dry-run` (validates the file and reports what would be uploaded without reading the token or contacting the API).

### Digest audio (`text_to_speech/`)

Creates a narrated WAV file from any completed Markdown digest using either Kokoro
or Chatterbox-Nano. The audio layer is optional and isolated: engine dependencies
are installed separately and the existing fetch, digest, and publishing paths do
not import them.

Preview the speech-ready text without installing a model:

```bash
python3 -m text_to_speech digests/full-lab-digest-2026-07-28-7d.md --dry-run
```

Add `--style conversational` for a more natural spoken script with transitions;
the default `direct` style stays close to the written summary.

See [`text_to_speech/README.md`](text_to_speech/README.md) for Python 3.11 setup,
provider installation, voice options, and generation commands.

## Claude Code Skills

The summarization and analysis work is performed by Claude Code skills in `.claude/skills/`:

| Skill | Description |
|---|---|
| `full-lab-digest` | Runs all five source subagents in parallel and compiles a combined digest with cross-notebook pattern analysis, multi-week **Historical Connections** drawn from the local archive, a consolidated **Data & Figures** section, and literature connections |
| `weekly-lab-digest` | Fetches WordPress posts and produces a per-author digest |
| `daily-literature-post` | Narrow daily counterpart to `full-lab-digest`: keeps only the last day's posts that describe a real scientific finding, runs `literature-connector` on each, and publishes one combined post. Publishes **live** only when authorized (see below); draft otherwise |
| `literature-connector` | Queries PubMed and the preprint servers indexed by Europe PMC (bioRxiv, medRxiv, Research Square, …) for papers published in the last 12 months and categorizes their relationship to a given lab finding (Supports / Conflicts / Adds context / Suggests next step) |
| `lab-archive` | Answers "has anyone done X before" by full-text-searching `.cache/archive.db` — every post the five notebooks have ever published — and reports grouped by researcher with a source link per claim. Read-only; it never builds the database. `full-lab-digest` reads the same database, the same way, for its Historical Connections section |
| `digest-index` | Regenerates `digests/README.md` from scratch as a newest-first index of every digest |
| `wordpress-publisher` | Converts a digest to sanitized HTML and posts it to genefish.wordpress.com as a draft |
| `digest-audio` | Generates an audio version of a completed digest with Kokoro or Chatterbox-Nano |
| `digest-audio-publish` | End-to-end: narrates the latest full digest in two editions, uploads the WAVs to the WP media library, and publishes a **new, separate** live post linking to them and back to the digest |

Each notebook source is read by its own subagent in `.claude/agents/` — `tumbling-oysters-agent`, `ariana-notebook-agent`, `sams-notebook-agent`, `grace-notebook-agent`, and `wordpress-agent`. Ask about a single notebook and Claude uses just that one; `full-lab-digest` launches all five.

### What the full digest adds on top of the five summaries

Beyond pasting each subagent's summary verbatim, `full-lab-digest` derives three sections from the compiled material. All three are conservative by design: each is omitted rather than padded when there is nothing real to report.

**Cross-Notebook Patterns & Connections** — shared themes, temporal narratives, and apparent contradictions found *within* the current window. A connection is surfaced only when a specific named entity ties two sources together (the same species, the same assay, the same named project); vague overlap like "both involve oysters" does not qualify. Apparent contradictions are flagged `⚠️ Needs human verification` along with what would resolve them.

**Historical Connections** — a subsection nested inside the above that looks *past* the current window for multi-week story arcs the single-window analysis cannot see. It read-only-queries the same `.cache/archive.db` the `lab-archive` skill uses, scoped to the **8 weeks ending the day before the current window starts**. Excluding the current window is deliberate: nothing already shown in the per-source sections can reappear here, and any archived post already cited elsewhere in the digest is discarded as a second guard. It reuses exactly the same set of findings the literature search runs on, so the two sections stay in sync. Archived posts whose permalink is shared with another post in the same notebook carry a `⚠️ shadowed URL` caveat.

**Data & Figures** — a consolidated, per-source entry point into the window's underlying figure links and external data/repository links, gathered from what the subagents already surfaced. It is a pure reorganization step: no new fetches, no new subagent runs, and no invented links. Third-party tool repositories and issue-tracker threads are routed to a separate `Related links (tools, issues)` line so they do not crowd out the lab's own data. A source with no links is left out; if the window has no links at all, the section is omitted entirely.

### Changing the time window

Every source defaults to a 7-day window, and every source accepts a different one. Ask for the window in plain language and the skill threads it through the subagents, the date range in the header, and the digest footer:

> give me a full lab digest for the last 14 days

The same applies to a single notebook ("what's new in Sam's notebook over the past month"). Under the hood this becomes `--days N` on `fetch_github_notebook.py` or `fetch_lab_posts.py`. The window is also encoded in the digest filename (`full-lab-digest-2026-07-27-14d.md`), so a 14-day digest does not overwrite the 7-day one that ends on the same date.

## Automated publishing

Most paths in this repo create WordPress **drafts**. Two publish live, and both are deliberately explicit:

- **`daily-literature-post`** publishes live *only* while [`AUTHORIZATION.md`](AUTHORIZATION.md) exists at the repository root and contains the marker line `AUTOMATED PUBLISHING: AUTHORIZED`. If the file is missing, unreadable, or the marker is changed (e.g. to `PAUSED`), the skill falls back to a draft and says so in its report. A second rail caps it at **one post per calendar day**, live or draft, recorded in `digests/.literature-state.json` under `publish_log`, so a double trigger cannot produce duplicates. Live posts are tagged with the `auto-literature-connections` category, which also excludes them from future daily runs.
- **`digest-audio-publish`** publishes its audio post live after showing you the resolved title and a content preview from a `--dry-run` first.

To pause live publishing without touching any code, change `AUTHORIZED` to `PAUSED` on the marker line in `AUTHORIZATION.md` (and scrub any other copy of the phrase from the file — the skill matches it as a plain substring), or delete the file, then commit. `AUTHORIZATION.md` also records who signed off and documents how to disable the cron automation entirely.

Nothing in `AUTHORIZATION.md` affects `full-lab-digest`, `weekly-lab-digest`, or `wordpress-publisher` — those remain draft-only.

## Digests

Generated digests are saved to the `digests/` directory as Markdown files, named by date range, and indexed in [`digests/README.md`](digests/README.md) — a newest-first table regenerated from scratch by the `digest-index` skill. Digest types include:

- **`2026-06-30.md`, `2026-07-07.md`** — WordPress-only weekly digests, grouped by author
- **`tumbling-oysters-YYYY-MM-DD.md`** — Focused digests for Steven Roberts' Tumbling Oysters notebook
- **`daily-literature-YYYY-MM-DD.md`** — Daily literature-connection posts from `daily-literature-post`: only the day's genuine findings, each paired with recent papers
- **`full-lab-digest-YYYY-MM-DD-Nd.md`** — Full multi-source digests, named by end date and window length (`-7d` by default). Files predating this convention omit the `-Nd` suffix. Each includes:
  - Per-notebook summaries (all five sources)
  - Cross-notebook pattern detection (shared species, assays, and themes), including a **Historical Connections** subsection that reaches back into the archive for multi-week story arcs
  - A **Data & Figures** section consolidating the window's figure and data links by source
  - Literature connections via PubMed and bioRxiv

Two state files sit alongside them and are committed so de-duplication holds across machines: `.digest-state.json` (post URLs already digested) and `.literature-state.json` (post URLs already connected to literature, plus the daily post's publish log).

### Example cross-notebook connection (from `full-lab-digest-2026-07-21.md`)

> **Thermal stress in Pacific oysters (*C. gigas*) at 35–36°C** — Two independent notebooks document active heat stress experiments on *C. gigas* this week using overlapping temperature ranges: Ariana's notebook (thermal hardening at Point Whitney) and the Genefish WordPress (Hazel's GlycogenGlo assays, Jesse's mortality assessments, and a 36°C incubator entry).

## Tests

Stdlib `unittest`, no dependencies and no network access — every HTTP call is mocked.

```bash
python3 -m unittest discover -s tests
```

To run a single module:

```bash
python3 -m unittest tests.test_publish_digest
```

The suite covers the parsing and safety logic in the scripts: HTML stripping, date
parsing and paging in `fetch_lab_posts.py`; the sanitizer allowlist, token handling,
and token redaction in `publish_digest.py`; the cosmetic/substantive boundary,
compare-range construction, and post clipping in `fetch_github_notebook.py`; and the
shared classification and clipping helpers in `notebook_parsing.py`. The optional
audio layer is covered too, but its provider tests stub out Kokoro and Chatterbox
rather than loading the real models.

`build_archive.py` and `upload_media.py` have no test module yet — see
[`ROADMAP.md`](ROADMAP.md).

## Requirements

- Python 3.8+ — stdlib only for `fetch_lab_posts.py`, `fetch_github_notebook.py`, `notebook_parsing.py`, `build_archive.py` (SQLite with FTS5, which CPython bundles), and `upload_media.py`
- Python 3.10+ (3.11 recommended) — only for the optional Kokoro/Chatterbox-Nano audio layer
- `python-markdown` (`pip install markdown`) or `pandoc` — only for `publish_digest.py`
- `GITHUB_TOKEN` or `GH_TOKEN` in the environment — optional for the 7-day fetchers, but strongly recommended for `build_archive.py`, since it raises the GitHub API rate limit from 60 to 5,000 requests/hour. The `gh` CLI is **not** required.
- Claude Code (for running skills)
- Internet access to the WordPress REST API and GitHub
- A WordPress.com API token at `~/.config/LabNotebook-Summarizer/wp_token` (mode 600) — only for publishing posts and uploading digest audio
- There is no `sqlite3` CLI requirement; the archive is queried through Python's built-in `sqlite3` module

## Related

- [Roberts Lab](https://robertslab.github.io/)
- [genefish.wordpress.com](https://genefish.wordpress.com)
