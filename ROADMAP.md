# ROADMAP

Improvements for LabNotebook-Summarizer, roughly in priority order. Items marked
**blocker** prevent the tool from running correctly today.

---

## Near term — correctness and blockers

### 1. Fix the `gh` dependency (blocker)

All four GitHub notebook agents (`tumbling-oysters`, `ariana`, `sams`, `grace`) call
`gh api` in Steps 1–2. `gh` is **not installed** on this machine and is not on `PATH`.
Unauthenticated `curl` to `api.github.com` currently returns
`API rate limit exceeded` from this IP, so there is no working fallback either.

Pick one:

- Install and authenticate `gh` (`brew install gh && gh auth login`), and add a
  preflight check to each agent that fails with a clear message if `gh` is missing; or
- Replace `gh api` with a `scripts/fetch_github_posts.py` helper that reads
  `GITHUB_TOKEN` from the environment or a token file, mirroring how
  `publish_digest.py` handles the WordPress token.

The second option is preferable — it removes an undeclared external binary from the
critical path and matches the existing token-handling pattern.

### 2. Resolve the Grace Crandall repo mismatch

[README.md](README.md) lists `RobertsLab/grace-crandall-notebook`, but
[grace-notebook-agent.md](.claude/agents/grace-notebook-agent.md) fetches from
`grace-ac/grace-ac.github.io` (branch `master`). One of these is wrong. Confirm the
live repo, then make README and agent agree.

### 3. Add tests for the two Python scripts

There are no tests. Both scripts have real parsing logic worth pinning:

- `fetch_lab_posts.py` — `strip_html` (script/style stripping, entity unescaping),
  `parse_date` (`Z` suffix, naive datetimes, unparseable input), and the paging
  cutoff/`max_pages` warning behavior.
- `publish_digest.py` — the HTML tag allowlist (that `<script>`, `<iframe>`, inline
  handlers, and `javascript:` URLs are dropped), title extraction from the first
  `# ` heading, and `--dry-run` never touching the token file.

Stdlib `unittest` is enough; no new runtime dependency.

---

## Medium term — reliability

### 4. Deduplicate the four GitHub agent definitions

`ariana`, `sams`, `grace`, and `tumbling-oysters` are ~90 line files that differ only
in repo, branch, post path convention, and front-matter fields. Every fix has to be
made four times. Collapse the shared fetch/parse work into one script driven by a
small per-notebook config (repo, branch, posts path, file extensions, date format),
and reduce each agent to the notebook-specific summarization guidance.

### 5. Make `weekly-lab-digest`'s Google Drive step optional

[weekly-lab-digest/SKILL.md](.claude/skills/weekly-lab-digest/SKILL.md) Step 7 calls
`mcp__claude_ai_Google_Drive__create_file` unconditionally. If that MCP server is not
connected the skill fails after all the real work is done. Make the upload
best-effort: write the file first, then attempt the upload and report if it was
skipped.

### 6. Track what has already been digested

`digests/` contains overlapping runs (`full-lab-digest-2026-07-13.md` and
`-07-14.md` cover mostly the same 7-day window). A small state file recording the
last digest date and the post URLs already covered would let a run report only
what is new, and would avoid re-running expensive literature searches on findings
already written up.

### 7. Cache literature-connector results

The `full-lab-digest` skill runs `literature-connector` sequentially for every
notable finding — the slowest part of a digest, and largely repeated week to week
for ongoing projects. Cache PubMed/Europe PMC responses on disk keyed by query +
date window, with a short TTL.

---

## Longer term — features

### 8. Schedule the weekly run

The digest is generated manually. Automate it as a scheduled Claude Code task (or a
GitHub Action) that runs `full-lab-digest` weekly, commits the result to `digests/`,
and opens the WordPress draft. Keep publishing as `draft` — the human review step is
the point.

### 9. Add a digest index

`digests/` is a flat directory of dated Markdown files with three different naming
conventions. Generate a `digests/README.md` index with date, type, sources covered,
and the cross-notebook themes found — so past digests are browsable without opening
each file.

### 10. Extend cross-notebook analysis across weeks

Cross-notebook pattern detection currently looks only within a single week's five
summaries. The more interesting narratives (an experiment set up in one week and
resolved three weeks later) span weeks. Once item 6 gives durable per-post state,
add a multi-week pass over prior digests.

### 11. Surface figures and data links

Agents already extract figure URLs and classify them local vs. external, but the
combined digest drops most of that. A "Data & Figures" section per digest — linked
project repos, external data, notable figures — would make digests more useful as an
entry point into the actual work.
