# ROADMAP

Improvements for LabNotebook-Summarizer, roughly in priority order.

Item numbers are stable — completed items move to the "Done" section at the bottom
rather than being renumbered.

---

## Near term — documentation

### 13. Document how to add a new GitHub-hosted notebook

Adding a sixth notebook is currently a read-the-whole-repo job. Every piece of the
work already exists and is generic — `fetch_github_notebook.py` is config-driven,
the agents share one formatting contract, and the archive builder takes a source
list — but nothing says *which* eleven places have to change, so the only way to
find them is to grep for `grace` and imitate. That is exactly the kind of knowledge
that should be a written procedure, especially since the pipeline is meant to keep
running after whoever built it has left the lab.

The deliverable is one document — [docs/adding-a-notebook.md](docs/adding-a-notebook.md),
linked from the README's Data Sources section — walking the touchpoints in dependency
order, with Grace's notebook as the worked example (it is the most instructive: the only
one needing `file_dates`, and the only Jekyll layout among three Quarto sites).

**The document is written.** What remains of this item is the count-free-prose refactor
described at the end; until that lands, the document carries the grep that finds the
hardcoded counts instead.

**Code (three files):**

1. **`NOTEBOOKS` entry** in
   [scripts/fetch_github_notebook.py](scripts/fetch_github_notebook.py) — `repo`,
   `prefix`, `suffix`, plus `file_dates: True` only when the agent needs per-file
   commit history. Worth explaining that `suffix` is matched against the full path,
   so `/index.qmd` pins folder-per-post layouts while `.qmd` also accepts flat files.
2. **A `derive_permalink` branch** in
   [scripts/notebook_parsing.py](scripts/notebook_parsing.py) — the file-path →
   published-URL mapping. This is the one step with no generic fallback: the function
   raises `ValueError` on an unknown source, so the archive build fails loudly rather
   than storing an un-citable post. Note the Jekyll case (the `YYYY-MM-DD-` prefix is
   dropped from the slug) versus the Quarto case (`index.*` is stripped).
3. **`GITHUB_SOURCES` and `DEFAULT_AUTHORS`** in
   [scripts/build_archive.py](scripts/build_archive.py) — one list entry (kept in
   ascending notebook size, so an interrupted build has finished the cheap ones) plus the
   author fallback used when front matter omits `author`. `lab-archive` groups by author,
   so a missing entry files the new notebook's posts under `None`.

**Agent (two files):**

4. **`.claude/agents/<name>-notebook-agent.md`** — copy an existing agent and replace
   only the notebook-specific half. The document should state the seven fields that
   actually differ (fetch config, repo structure, front-matter fields to extract,
   published permalink convention, no-activity message, header, block fields) and that
   everything else belongs in
   [notebook-digest-format.md](.claude/shared/notebook-digest-format.md), not in the
   agent. Also: the agent must skip its own file write when invoked by
   `full-lab-digest`.
5. **The agent roster** at the top of
   [notebook-digest-format.md](.claude/shared/notebook-digest-format.md), which names
   the four current agents.

**Skills and docs (four files):** the source list and agent list in
[full-lab-digest/SKILL.md](.claude/skills/full-lab-digest/SKILL.md) (step 2, the
per-source section template, the Data & Figures source order), the source enumeration
and source-label map in [lab-archive/SKILL.md](.claude/skills/lab-archive/SKILL.md),
the filename-prefix → source mapping in
[digest-index/SKILL.md](.claude/skills/digest-index/SKILL.md), and the Data Sources
table in [README.md](README.md). Plus a `derive_permalink` case in
[tests/test_notebook_parsing.py](tests/test_notebook_parsing.py), and — for anyone
running unattended — a `fetch_github_notebook.py --notebook <name>` entry in
`.claude/settings.local.json` so the fetch does not stop on a permission prompt.

**The real friction, which the document should name rather than hide:** the count
"five" is written into prose in a dozen places — "all five subagents", "wait for all
five", "the five compiled summaries", "every post the five notebooks have ever
published" — across `full-lab-digest`, `lab-archive`, `tumbling-oysters-agent`, and
the README. Adding a notebook without updating those leaves instructions that
actively contradict the agent roster, and a skill told to wait for five returns while
six are running. Two options: enumerate the occurrences in the checklist, or make the
prose count-free ("all notebook subagents", "every source listed in step 2") as part
of this item so the next addition is a shorter diff. The second is the better fix and
is cheap to do while writing the document.

Independent of every other roadmap item — no new scripts, no network, no state.

---

## Longer term — features

### 12. Literature links as comments on genefish.wordpress.com posts

A lighter-weight variant of item 9 that puts the connection where the work is instead
of in a separate post: for each new post on genefish.wordpress.com, leave a comment
linking the one or two most relevant recent papers. The comment sits under the post it
is about, so a reader who lands on the notebook entry six months later sees the
literature alongside it.

Two of the three hard parts already exist. The WordPress.com v1.1 API creates comments
at `POST /sites/$site/posts/$post_ID/replies/new` with a single `content` field and a
Bearer token — the same credential `publish_digest.py` already reads from
`~/.config/LabNotebook-Summarizer/wp_token`. `comments_open` is `true` on recent
genefish posts, so nothing needs enabling site-side (re-check rather than assume; the
setting is per-post). And [literature-connector/SKILL.md](.claude/skills/literature-connector/SKILL.md)
already returns relationship-tagged papers with PMID/DOI links and already declines to
stretch a loose match — the right default when the alternative is public text under
someone else's notebook entry.

What is missing:

1. **`scripts/post_comment.py`** — a sibling to `publish_digest.py` reusing
   `read_token`, `sanitize`, `markdown_to_html`, and the token-scrubbing in
   `post_draft`. Takes `--post-id` and a *file path* for the body; comment text never
   becomes a command-line argument, same injection reasoning as the publisher.
2. **Post IDs in the fetch output.** `fetch_lab_posts.py` keeps `URL` but drops `ID`,
   and the comment endpoint is ID-addressed. One field to add.
3. **TOPIC and FINDING inferred from the post body** — the same gap item 9 describes.
   Logistical posts (ordering, meeting notes, equipment) have no finding to connect;
   skip them rather than inventing one.
4. **State**, reusing item 4's mechanism so a post gets at most one literature comment
   even when a later run's window still includes it.

The structural difference from every existing publish path: **comments have no draft
state.** `publish_digest.py` leans on `status: draft` as the human-review gate, and
that gate does not exist here — a POST as the site owner is live and auto-approved
immediately. A comment can be flipped to `unapproved` afterward via
`/sites/$site/comments/$comment_ID`, but that is backwards: public first, reviewed
second. So review moves *before* the POST — the run writes proposed comments to a file
(target post title, post ID, comment body), a human reads it, and only then does
anything get sent. That keeps this a two-step flow rather than an unattended one, which
is the right trade for text appearing under a colleague's name on a public site.

One advantage over item 9: no feedback loop to defend against. Comments are not
returned by the posts endpoint, so a daily fetch never sees its own output and cannot
start connecting its own connections.

Shares items 1–4 of item 9's pipeline; the two should be built as one daily run with a
choice of output surface rather than twice. Depends on item 4 (state) and wants item 5
(cache) for the same reason item 9 does.

### 13. Configurable notebook registry

`NOTEBOOKS` in [fetch_github_notebook.py](scripts/fetch_github_notebook.py) hardcodes the
repo, path prefix/suffix, and permalink scheme for all four GitHub-hosted notebooks, and
`derive_permalink` in [notebook_parsing.py](scripts/notebook_parsing.py) hardcodes a matching
`if source == ...` branch per notebook. Onboarding a new lab member's notebook — or a new
lab entirely — currently means editing both files, adding a fifth subagent modeled on the
existing four, and touching `DEFAULT_AUTHORS` in `build_archive.py`. Moving the per-notebook
config into a small YAML/JSON file (repo, prefix, suffix, permalink template, default author)
would let a new source be added by data, not code, and would let a generic subagent template
read its notebook's config by name instead of one bespoke `.claude/agents/*.md` file per
source — collapsing the "one agent per notebook" pattern item 2 already deduplicated at the
prompt level down to one agent parameterized by config.

### 14. Flag notebooks that have gone quiet

Every weekly digest reports a source with zero posts in the window as "no activity" (README,
"What to expect") — accurate, but silent about *how long* it's been quiet. A source that
misses three weeks in a row looks the same as one that missed one. Since `scripts/build_archive.py`
already stores every post's `date` per source in `.cache/archive.db`, a cheap check — most
recent post date per source vs. today — could turn "no activity" into "no activity (last post:
6 weeks ago)" in the digest header, or into a dedicated callout past some threshold (e.g. 21
days). Useful signal for a PI skimming digests: a notebook gone quiet for a month is a
different situation than one that just had an off week.

### 15. Read-only search over the archive without Claude Code

`lab-archive` (item 11) answers "has anyone done this before" questions against
`.cache/archive.db`'s FTS5 index, but only for someone with Claude Code open in this
repository. Lab members who just want to grep old notebook entries have no way in. A small
`scripts/search_archive.py` — takes a query, runs the same FTS5 `MATCH` the skill uses,
prints ranked hits with source/author/date/URL — would make the archive usable from a plain
terminal, and could double as the base for a tiny static HTML page (SQLite FTS5 output is
just rows) if browser-based search across the whole lab's history turns out to be wanted.

### 16. Attach narration to the weekly publish automatically

`digest-audio` and `digest-audio-publish` exist and work — `scripts/upload_media.py` was added
alongside the publish skill recently — but narrating and uploading audio for a digest is
currently a separate, manually triggered step after the weekly digest is written. Once this
pattern has run manually a few times without surprises, `weekly-lab-digest`/`full-lab-digest`
could offer the audio step inline — generate narration, upload via `scripts/upload_media.py`,
and link the WAV from the WordPress draft — as an opt-in flag rather than a fully separate
invocation. Keep it opt-in and best-effort (same lesson item 3 already learned from the
Drive-upload step): a TTS/upload failure should not block the digest itself from being
written or published.

### 17. Surface literature "Conflicts" as a standout

`literature-connector` already tags each paper's relationship to a lab finding as *Supports*,
*Conflicts*, *Adds context*, or *Suggests next step*, but every tag is rendered the same way —
one more bullet in a list. A *Conflicts* tag is the highest-value signal of the four: it means
a lab result and a published paper disagree, which is worth a human's attention regardless of
which digest section it happens to land in. Both `full-lab-digest` and `daily-literature-post`
could pull any *Conflicts*-tagged connection into a short callout near the top of the digest
(or the draft's opening paragraph) instead of leaving it to be found while reading through
every per-notebook section in order.

---

## Done

### 1. Add tests for the Python scripts

`tests/` covers all three scripts with stdlib `unittest` — no new runtime
dependency, and no network access (every HTTP call is mocked). Run with
`python3 -m unittest discover -s tests`.

- `fetch_lab_posts.py` — `strip_html`, `parse_date`, the paging cutoff and
  `max_pages` warning, the unreadable-date skip, and the excerpt fallback.
- `publish_digest.py` — the tag allowlist, title extraction, `--dry-run` never
  reading the token, plus token-file permission warnings and the redaction that
  keeps a reflected credential out of error output.
- `fetch_github_notebook.py` — the 6-line cosmetic boundary, middle-clipping,
  compare-range construction, rate-limit messages, and an end-to-end pass over
  `main()` covering path matching and the per-class content caps.

### 2. Deduplicate the four GitHub agent definitions

The common formatting contract now lives in
[.claude/shared/notebook-digest-format.md](.claude/shared/notebook-digest-format.md),
which each agent reads first. `ariana`, `sams`, `grace`, and `tumbling-oysters` are
down to 35–41 lines each and carry only notebook-specific guidance: the
`fetch_github_notebook.py` config name, repo structure, front-matter fields,
permalink convention, no-activity message, header, and block fields. A change to
the summary format is now made once.

### 3. Make `weekly-lab-digest`'s Google Drive step optional

Resolved by dropping the Drive upload entirely rather than making it best-effort.
[weekly-lab-digest/SKILL.md](.claude/skills/weekly-lab-digest/SKILL.md) Step 7 now
just returns the `digests/[week_start].md` path, so the skill no longer depends on
an MCP server being connected. If Drive delivery is wanted again, add it after the
file write and treat a failure as a skipped step, not an error.

### 5. Cache literature-connector results

`literature-connector` now caches PubMed/Europe PMC responses on disk keyed by
query + date window, with a 48-hour TTL, so `full-lab-digest`'s repeated per-finding
searches for ongoing projects hit the cache instead of the network. The cache
directory is `.gitignore`d as a rebuildable derived artifact. See
[literature-connector/SKILL.md](.claude/skills/literature-connector/SKILL.md).

### 7. Add a digest index

The `digest-index` skill generates `digests/README.md` — a browsable index of the
flat `digests/` directory with date, type, sources covered, and cross-notebook
themes per digest, so past digests are scannable without opening each file. See
[digest-index/SKILL.md](.claude/skills/digest-index/SKILL.md).

### 4. Track what has already been digested

`full-lab-digest` reads and writes `digests/.digest-state.json` (`last_digest_date`
plus a `digested_urls` list spanning all five sources, committed to the repo so
de-duplication survives across machines). Posts already covered are excluded from
the per-source summaries before compiling, with a per-source note of how many were
omitted; a missing state file is treated as a first run. Canonical post URLs only
are matched, trailing slash insensitive — image, repo-root, and literature links are
never tracked.

### 11. Searchable archive of all notebook history

`scripts/build_archive.py` builds an incremental local corpus of every post across all
five sources into a git-ignored SQLite database (`.cache/archive.db`) with an FTS5
index — stdlib only, blob-SHA-skip so re-runs are near-free, and resumable across
rate-limit stops. Parsing is shared with the windowed fetch via
`scripts/notebook_parsing.py` rather than duplicated. The `lab-archive` skill answers
plain-English "has anyone here done this before" questions read-only against that DB,
grouped by researcher with a cited link per claim. See
[lab-archive/SKILL.md](.claude/skills/lab-archive/SKILL.md).

### 8. Extend cross-notebook analysis across weeks

`full-lab-digest` now runs a Historical Connections pass (step 8) after the
same-window pattern detection, reaching back into the lab archive (item 11) to surface
multi-week story arcs — an experiment set up in one week and resolved weeks later —
that single-window analysis cannot see. Each surviving connection is a bullet naming
the shared entity and the direction of the arc, citing the archived post by its actual
returned URL; empty findings are omitted silently. See
[full-lab-digest/SKILL.md](.claude/skills/full-lab-digest/SKILL.md).

### 9. Daily literature-connection post on genefish.wordpress.com

The `daily-literature-post` skill fetches the last day of lab posts, keeps only those
describing a real scientific finding, runs `literature-connector` per finding, and
assembles one Markdown post published to WordPress as a **draft**. The draft carries
the `auto-literature-connections` category so it is excluded from future daily runs,
and every processed post is recorded in `digests/.literature-state.json` so it is
never processed twice — closing the feedback loop. Draft-only by design. See
[daily-literature-post/SKILL.md](.claude/skills/daily-literature-post/SKILL.md).

### 6. Schedule the weekly run

The weekly digest now runs on a schedule rather than by hand, running `full-lab-digest`,
committing the result to `digests/`, and opening the WordPress draft. Publishing stays
as `draft` so the human review step is preserved.

### 10. Surface figures and data links

Agents already extract figure URLs and classify them local vs. external, but the
combined digest drops most of that. A "Data & Figures" section per digest — linked
project repos, external data, notable figures — would make digests more useful as an
entry point into the actual work.
