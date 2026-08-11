# ROADMAP

Improvements for LabNotebook-Summarizer, roughly in priority order.

Item numbers are stable — completed items move to the "Done" section at the bottom
rather than being renumbered.

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
