# ROADMAP

Improvements for LabNotebook-Summarizer, roughly in priority order.

Item numbers are stable — completed items move to the "Done" section at the bottom
rather than being renumbered.

---

## Medium term — reliability

### 2. Deduplicate the four GitHub agent definitions

The shared fetch/parse work is already collapsed into `fetch_github_notebook.py`,
driven by the per-notebook `NOTEBOOKS` config. What remains is the agent files
themselves: `ariana`, `sams`, `grace`, and `tumbling-oysters` are still 83–94 line
documents whose output-format, figure-handling, and no-activity instructions are
near-identical, so a change to the summary format is still made four times. Reduce
each to the notebook-specific guidance (permalink convention, project repos,
front-matter quirks) and move the common formatting contract somewhere single —
the `full-lab-digest` skill already specifies the shape it wants back.

### 3. Make `weekly-lab-digest`'s Google Drive step optional

[weekly-lab-digest/SKILL.md](.claude/skills/weekly-lab-digest/SKILL.md) Step 7 calls
`mcp__claude_ai_Google_Drive__create_file` unconditionally. If that MCP server is not
connected the skill fails after all the real work is done. Make the upload
best-effort: write the file first, then attempt the upload and report if it was
skipped.

### 4. Track what has already been digested

`digests/` contains overlapping runs (`full-lab-digest-2026-07-13.md` and
`-07-14.md` cover mostly the same 7-day window). A small state file recording the
last digest date and the post URLs already covered would let a run report only
what is new, and would avoid re-running expensive literature searches on findings
already written up.

### 5. Cache literature-connector results

The `full-lab-digest` skill runs `literature-connector` sequentially for every
notable finding — the slowest part of a digest, and largely repeated week to week
for ongoing projects. Cache PubMed/Europe PMC responses on disk keyed by query +
date window, with a short TTL.

---

## Longer term — features

### 11. Searchable archive of all notebook history

Every path through the repo today is window-scoped: `fetch_github_notebook.py` builds
its file list from `commits?since=...`, `fetch_lab_posts.py` takes `--days`, and
`digests/.digest-state.json` remembers post URLs only in order to *exclude* them. So
the tool answers "what happened last week" but cannot answer the question a lab
actually asks constantly — "has anyone here done this before, and what did they find?"
Sam's 2026-07-30 Glycogen-Glo post is a live example: four samples read above the
standard curve and need re-assay at 2×–6× further dilution, and someone in the lab has
plausibly already solved that. Finding out means manually grepping four GitHub repos
and a WordPress site.

The feature: an incrementally-built local corpus of every post from all five sources —
one row per post with source, author, date, URL, categories, and full text — plus a
`lab-archive` skill that queries it.

1. **`scripts/build_archive.py`** — enumerate each repo's posts directory via the git
   tree API (one call per repo, rather than the per-commit walk the windowed fetch
   needs), fetch bodies, and store in SQLite with an FTS5 index. Stdlib only, matching
   the existing no-new-runtime-dependency stance. Incremental: skip any path whose blob
   SHA is unchanged since the last build, so re-runs are nearly free. WordPress posts
   come from the same REST endpoint `fetch_lab_posts.py` already pages through, with the
   window removed.
2. **Share the parsing.** Front-matter, permalink derivation, and post-body handling
   already exist in `build_post` in `fetch_github_notebook.py`; factor that so the
   archive builder and the windowed fetch use one implementation rather than drifting.
3. **`.claude/skills/lab-archive/SKILL.md`** — takes a plain-English question, runs FTS
   queries, and returns hits grouped by researcher with dates and permalinks. Answers
   cite posts; never paraphrase a result without linking it.
4. **Feed it back into the digest.** A "Prior work in this lab" line per notable
   finding, resolved against the archive.

Keyword FTS is the right first cut: lab vocabulary is unusually precise
(`Glycogen-Glo`, `topGO`, `resazurin`) and exact-term matching beats embeddings on
jargon with no model dependency. If recall proves too tight, embeddings can layer onto
the same table later.

Two things to settle before building it:

- **Backfill cost.** The first build fetches every post body across five sources, which
  is far more GitHub API calls than a weekly run. Needs `GITHUB_TOKEN` and probably a
  resumable build (record completed paths, continue after a rate-limit stop) so a
  failure halfway through does not restart from zero.
- **Where the DB lives.** It is a derived artifact, so it should be `.gitignore`d and
  rebuildable from scratch — but that means each clone pays the backfill once. Decide
  that explicitly rather than committing a binary by accident.

Strengthens item 8 (cross-notebook analysis over weeks gets a full-history substrate
instead of a walk over prior digest files) and item 5 (a prior-work check on the
archive is free, where a literature search is not).

### 6. Schedule the weekly run

The digest is generated manually. Automate it as a scheduled Claude Code task (or a
GitHub Action) that runs `full-lab-digest` weekly, commits the result to `digests/`,
and opens the WordPress draft. Keep publishing as `draft` — the human review step is
the point.

### 7. Add a digest index

`digests/` is a flat directory of dated Markdown files with three different naming
conventions. Generate a `digests/README.md` index with date, type, sources covered,
and the cross-notebook themes found — so past digests are browsable without opening
each file.

### 8. Extend cross-notebook analysis across weeks

Cross-notebook pattern detection currently looks only within a single window's five
summaries. The more interesting narratives (an experiment set up in one week and
resolved three weeks later) span weeks. Once item 4 gives durable per-post state,
add a multi-week pass over prior digests — and if item 11 lands first, run the pass
over the post archive itself rather than over the digests written about it.

### 9. Daily literature-connection post on genefish.wordpress.com

Today the literature work only happens inside a weekly/multi-day digest, and the
output lands in `digests/` plus a WordPress draft that a human opens. The feature:
**every day, consider the new posts on genefish.wordpress.com, draft a post that
connects them to recent literature, and put that post back on
genefish.wordpress.com.**

Shape of the daily run:

1. **Fetch the day's posts** — `python3 scripts/fetch_lab_posts.py --days 1`
   (`--days` already exists; the default of 7 is the only thing that needs
   overriding). If `posts` is empty, exit quietly without posting — a no-activity
   day should produce nothing, not an empty post.
2. **Exclude already-connected posts** — reuse the state mechanism from item 4.
   Either extend `digests/.digest-state.json` with a `connected_urls` list or add a
   sibling `digests/.literature-state.json`; a post that already got a connection
   post never gets a second one, even if a later run's window still contains it.
3. **Derive TOPIC and FINDING per post** — `literature-connector` requires both
   (see [literature-connector/SKILL.md](.claude/skills/literature-connector/SKILL.md)),
   and its inputs are currently supplied by a human. The daily run has to infer them
   from the post body. Purely logistical posts (meeting notes, ordering, equipment)
   have no finding to connect; skip them rather than inventing one, and if every post
   that day is logistical, treat the day as empty and post nothing.
4. **Run `literature-connector`** per remaining post and assemble one Markdown post —
   sections per source post, each with the relationship-tagged papers and the
   preprint caveat block the skill already emits.
5. **Publish** via `scripts/publish_digest.py`, same path as
   [wordpress-publisher/SKILL.md](.claude/skills/wordpress-publisher/SKILL.md) — the
   Markdown never touches a shell, only the file path does.

Three things to settle before building it:

- **Feedback loop.** The connection post is published to the same site the daily
  fetch reads, so the next run will see it as a new post and try to connect the
  connections. The fetch has to filter these out — by tag/category applied at
  publish time, by author, or by recording each published post's URL in the state
  file. Whichever is chosen, the filter has to be verified, not assumed; getting it
  wrong produces a self-feeding loop that posts daily forever.
- **Draft vs. live.** `publish_digest.py` hardcodes `status: draft`, and
  `wordpress-publisher` requires explicit per-run confirmation before it sends
  anything. A genuinely daily unattended post needs a deliberate decision to relax
  one or both — a `--status publish` flag plus a standing authorization recorded
  somewhere durable. Defaulting to draft and letting a human hit publish is the safer
  starting point and still delivers the daily drafting.
- **Search volume.** A daily run hits PubMed and Europe PMC every day instead of
  weekly, on largely the same ongoing projects. Item 5's cache stops being a
  nice-to-have here.

Depends on item 4 (state) and pairs with item 6 (the scheduling mechanism is the
same, just at daily cadence).

---

### 10. Surface figures and data links

Agents already extract figure URLs and classify them local vs. external, but the
combined digest drops most of that. A "Data & Figures" section per digest — linked
project repos, external data, notable figures — would make digests more useful as an
entry point into the actual work.

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
