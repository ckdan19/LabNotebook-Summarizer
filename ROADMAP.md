# ROADMAP

Improvements for LabNotebook-Summarizer, roughly in priority order.

Item numbers are stable — completed items move to the "Done" section at the bottom
rather than being renumbered.

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

### 8. Extend cross-notebook analysis across weeks

Cross-notebook pattern detection currently looks only within a single window's five
summaries. The more interesting narratives (an experiment set up in one week and
resolved three weeks later) span weeks. Item 4's durable per-post state is now in
place, so the remaining work is the multi-week pass over prior digests — and if item
11 lands first, run the pass over the post archive itself rather than over the digests
written about it.

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
