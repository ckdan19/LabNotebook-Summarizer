# ROADMAP

Improvements for LabNotebook-Summarizer, roughly in priority order.

---

## Near term — correctness

### 1. Add tests for the two Python scripts

There are no tests. Both scripts have real parsing logic worth pinning:

- `fetch_lab_posts.py` — `strip_html` (script/style stripping, entity unescaping),
  `parse_date` (`Z` suffix, naive datetimes, unparseable input), and the paging
  cutoff/`max_pages` warning behavior.
- `publish_digest.py` — the HTML tag allowlist (that `<script>`, `<iframe>`, inline
  handlers, and `javascript:` URLs are dropped), title extraction from the first
  `# ` heading, and `--dry-run` never touching the token file.

`fetch_github_notebook.py` is worth covering too: the `substantive` vs. `cosmetic`
classification at the 6-line diff boundary, and middle-clipping of long posts
(that front matter and conclusion both survive, and `content_truncated` is set).

Stdlib `unittest` is enough; no new runtime dependency.

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
add a multi-week pass over prior digests.

### 9. Surface figures and data links

Agents already extract figure URLs and classify them local vs. external, but the
combined digest drops most of that. A "Data & Figures" section per digest — linked
project repos, external data, notable figures — would make digests more useful as an
entry point into the actual work.
