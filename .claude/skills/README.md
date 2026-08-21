# Claude Code Skills

This directory holds the nine skills that do the actual work in LabNotebook-Summarizer.
Each skill is a single `SKILL.md` file in its own directory; the directory name is the
skill's name. A skill is a prompt-level procedure — Claude reads the `SKILL.md` and
follows it — so a skill is edited like documentation, not like code.

Skills are invoked either by asking in plain language (each `SKILL.md` opens with the
phrasings that should trigger it) or explicitly by name (`/full-lab-digest`). Anything
heavier than a few lines of logic lives in `scripts/` and is *called* by the skill
rather than reimplemented in it.

Related directories:

- [`../agents/`](../agents/) — one subagent per notebook source (five total). Skills that
  need notebook content launch these; they do not fetch posts themselves.
- [`../shared/notebook-digest-format.md`](../shared/notebook-digest-format.md) — the
  output contract the four GitHub agents share.
- [`../../scripts/`](../../scripts/) — the fetch, archive, publish, and upload scripts.

## The nine skills

| Skill | Triggered by | Produces |
|---|---|---|
| [`full-lab-digest`](full-lab-digest/SKILL.md) | "full weekly lab digest", "digest of all notebooks" | `digests/full-lab-digest-<date>-<N>d.md` |
| [`weekly-lab-digest`](weekly-lab-digest/SKILL.md) | "weekly summary", "weekly lab notebook summary" | A per-author WordPress-only digest |
| [`daily-literature-post`](daily-literature-post/SKILL.md) | "run the daily literature connection post" | One WordPress post (live only if authorized) |
| [`literature-connector`](literature-connector/SKILL.md) | "find recent papers", "check the literature" | A categorized literature section |
| [`lab-archive`](lab-archive/SKILL.md) | "has anyone done X before", "search the archive" | An answer grouped by researcher, one link per claim |
| [`digest-index`](digest-index/SKILL.md) | "update the digest index" | `digests/README.md`, rebuilt from scratch |
| [`wordpress-publisher`](wordpress-publisher/SKILL.md) | "publish the digest to WordPress" | A WordPress **draft** |
| [`digest-audio`](digest-audio/SKILL.md) | "narrate the latest digest" | A local WAV of a digest |
| [`digest-audio-publish`](digest-audio-publish/SKILL.md) | "publish audio for the latest digest" | A new live WordPress post linking the audio |

## What each one does

### `full-lab-digest`

The main entry point. Launches all five notebook subagents **in parallel in a single
message**, then compiles their summaries into one Markdown file organized by source.
The window defaults to 7 days and follows whatever the user asks for ("the last 14
days"); the window is threaded through the subagents' `--days`, the header date range,
and the filename, so a 14-day digest never overwrites the 7-day one ending the same day.

On top of the five verbatim summaries it derives three sections, each omitted rather
than padded when there is nothing real to report: **Cross-Notebook Patterns &
Connections** (only when a specific named entity ties two sources together),
**Historical Connections** (a read-only archive query over the 8 weeks *ending the day
before* the current window), and **Data & Figures** (a pure reorganization of links the
subagents already surfaced — no new fetches, no invented links).

State: `digests/.digest-state.json` records every post URL any digest has covered, so a
post inside the window that has already been digested is excluded. The file is
committed, never gitignored, so de-duplication holds across machines.

### `weekly-lab-digest`

The narrow WordPress-only counterpart: runs `scripts/fetch_lab_posts.py` and groups the
last 7 days of genefish posts by author. No subagents, no archive, no literature.

### `daily-literature-post`

The daily counterpart to `full-lab-digest`, scoped to one job: take the last few days of
posts, keep only those describing a **real scientific finding**, run
`literature-connector` on each, and publish the results as one combined post. It does
not summarize notebooks or search the archive.

This is the only skill that publishes live unattended, and it is gated by two
independent rails (see [Publishing rails](#publishing-rails)).

State: `digests/.literature-state.json` — processed post URLs plus a `publish_log`.

### `literature-connector`

Searches PubMed and the preprint servers indexed by Europe PMC (bioRxiv, medRxiv,
Research Square, Authorea, …) for the last 12 months, then writes a 2–3 sentence,
quote-free characterization of each paper's relationship to a supplied lab finding,
categorized as **Supports**, **Conflicts**, **Adds context**, or **Suggests next step**.
Every entry is labeled with its source so preprints are never mistaken for peer-reviewed
work. When nothing genuinely relevant turns up it says so instead of stretching a loose
match.

Takes two inputs — `TOPIC` and `FINDING`. If the finding is missing, the skill asks for
it rather than guessing; without it there is nothing to categorize against.

Cache: raw API responses are cached under `.cache/literature-connector/`, keyed by
SHA-256 of `<call-type>|<query>|<date window>`. Raw rather than filtered responses are
cached deliberately — the same query can be re-analyzed against a new `FINDING`.

### `lab-archive`

Answers questions about the lab's own accumulated history by full-text-searching
`.cache/archive.db`, the local archive of every post the five notebooks have published,
and reports grouped by researcher with a cited source link for every claim.

**Read-only, strictly.** It opens connections read-only and issues only `SELECT`s.
Populating and refreshing that database is `scripts/build_archive.py`'s job alone — if
the database is missing, the skill reports that rather than building it. There is no
`sqlite3` CLI in this environment; queries go through Python's `sqlite3` module.

### `digest-index`

Regenerates `digests/README.md` as a single newest-first table indexing every digest ever
produced. **Always rebuilt from scratch** — never appended to or edited incrementally,
so the index stays correct when digests are deleted, renamed, or edited.

### `wordpress-publisher`

Hands a digest file to `scripts/publish_digest.py`, which converts the Markdown to
sanitized HTML and POSTs it to the WordPress.com REST API as a **draft**, always.

Credential handling, HTML escaping, and JSON encoding all live in that script and must
not be reimplemented in shell. Digest text is derived from third-party notebook posts,
so interpolating it into a shell command is a command-injection path — a post title
containing `$(...)` or a backtick would execute. The script takes a *file path*; content
never reaches a shell.

### `digest-audio`

Narrates an existing digest. Runs `python -m text_to_speech … --dry-run` first to confirm
the narration reads titles and findings but not URLs, figure paths, or generated-at
metadata, then generates the WAV. Defaults to the `kokoro` provider and the `direct`
style. It never installs an engine automatically — if the optional dependency is
missing it returns the install command from `text_to_speech/README.md`. It also does not
generate a new digest unless asked.

### `digest-audio-publish`

The end-to-end audio flow, standalone from the three skills above: narrate the latest
full digest, upload the WAVs to the WordPress media library via
`scripts/upload_media.py`, and publish a **new, separate** post linking to the audio and
back to the original digest. It never edits the existing digest post.

Prerequisites are verified before anything runs: `.venv-tts/bin/python` must exist (the
engines and model weights live only in that isolated environment — not system
`python3`), `scripts/upload_media.py` must be present, the WordPress token must be at
`~/.config/LabNotebook-Summarizer/wp_token` (read by the scripts themselves — never
echoed or passed on a command line), and the original digest post's URL must be known.
Any missing prerequisite stops the run with a report instead of an automatic install.

## How they compose

```
                     ┌─ tumbling-oysters-agent ─┐
                     ├─ ariana-notebook-agent  ─┤
full-lab-digest ─────┼─ sams-notebook-agent    ─┼──> digests/full-lab-digest-*.md
                     ├─ grace-notebook-agent   ─┤          │
                     └─ wordpress-agent        ─┘          │
                          │                                ├──> wordpress-publisher (draft)
                          ├─ lab-archive query ────────────┤
                          └─ literature-connector ─────────┼──> digest-index
                                                           │
                                                           └──> digest-audio ──> digest-audio-publish (live)

daily-literature-post ──> literature-connector ──> one WordPress post (live if authorized)
weekly-lab-digest ──────> scripts/fetch_lab_posts.py ──> per-author digest
```

`full-lab-digest` reuses the same archive database and the same set of findings that
`lab-archive` and `literature-connector` work from, which is what keeps its derived
sections consistent with the standalone skills.

## Publishing rails

Most paths in this repo produce **drafts**. Two publish live, and both are explicit:

- **`daily-literature-post`** publishes live only while [`AUTHORIZATION.md`](../../AUTHORIZATION.md)
  exists at the repo root and carries the marker line `AUTOMATED PUBLISHING: AUTHORIZED`.
  Missing file, unreadable file, or an altered marker → draft, and the skill says so in
  its report. A second rail caps it at **one post per calendar day**, live or draft,
  recorded in `digests/.literature-state.json`. There is no other route to live
  publishing — hand-passing `--status publish` outside these rails is out of bounds.
- **`digest-audio-publish`** publishes live only after showing the resolved title and a
  `--dry-run` content preview.

Nothing in `AUTHORIZATION.md` affects `full-lab-digest`, `weekly-lab-digest`, or
`wordpress-publisher` — those stay draft-only by construction.

## Conventions for writing or editing a skill

- **One directory, one `SKILL.md`.** The directory name is the skill name.
- **Open with the triggers.** First line after the title states the phrasings that
  should invoke the skill, and — where the skill has a near neighbor — what it
  deliberately does *not* do.
- **Then "What this skill does."** A short prose paragraph, before the numbered steps.
- **Numbered, imperative steps.** Each step is something Claude can actually carry out,
  with the exact command or file path inline.
- **Paths are relative to the repository root**, which is Claude Code's working
  directory. Say so if a command must run from elsewhere.
- **Delegate to `scripts/`.** Anything involving credentials, HTML, JSON, or untrusted
  post text belongs in a script that takes a file path — not in a shell command with
  content interpolated into it.
- **State files are committed; caches are gitignored.** `digests/.digest-state.json` and
  `digests/.literature-state.json` are committed so de-duplication survives across
  machines; `.cache/` is not.
- **Say what happens when something is missing.** Every skill that depends on a
  database, a virtualenv, a token, or a state file spells out the fallback — usually
  "stop and report", never "install it silently".
- **Omit rather than pad.** Derived sections are left out when there is nothing real to
  say.

Adding a new *notebook source* rather than a new skill is a different job — see
[`docs/adding-a-notebook.md`](../../docs/adding-a-notebook.md).
