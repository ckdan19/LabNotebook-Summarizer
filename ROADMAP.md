# ROADMAP

Improvements for LabNotebook-Summarizer, roughly in priority order.

Item numbers are stable — completed items move to the "Done" section at the bottom
rather than being renumbered.

---

## Medium term — reliability

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
resolved three weeks later) span weeks. Item 4's durable per-post state is now in
place, so the remaining work is the multi-week pass over prior digests.

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

### 4. Track what has already been digested

`full-lab-digest` reads and writes `digests/.digest-state.json` (`last_digest_date`
plus a `digested_urls` list spanning all five sources, committed to the repo so
de-duplication survives across machines). Posts already covered are excluded from
the per-source summaries before compiling, with a per-source note of how many were
omitted; a missing state file is treated as a first run. Canonical post URLs only
are matched, trailing slash insensitive — image, repo-root, and literature links are
never tracked.
