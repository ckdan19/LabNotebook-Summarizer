# Daily Literature Post Skill

Trigger this skill when the user asks to **run the daily literature connection post**, **do today's literature connections**, **run the daily lit post**, or any similar phrasing that means "look at today's lab posts and connect their findings to the published literature."

## What this skill does

Fetches the last few days of lab notebook posts, keeps only the ones that describe a **real scientific finding**, runs the `literature-connector` skill against each finding, and assembles the results into a single Markdown post published to WordPress. Future daily runs exclude this skill's own posts primarily by a title-prefix match (titles beginning `Daily Literature Connections —`); the post is also tagged with the `auto-literature-connections` category as a second signal, which now sticks (an admin created the category on the site on 2026-08-25; the publishing token can attach the existing category but still cannot create categories — see step 3). Every post it processes is recorded in `digests/.literature-state.json` so it is never processed twice.

This is a narrow daily counterpart to `full-lab-digest`: it does not summarize the notebooks, run subagents, or search the archive — it only connects today's genuine findings to external literature.

**Live publishing is authorization-gated; draft is the safe default.** This skill publishes **live only when a durable authorization file is present**; otherwise it falls back to a draft. Two independent rails protect this (both enforced in step 7):

1. **Authorization file.** Live publishing requires `AUTHORIZATION.md` at the repository root containing a standalone line reading exactly `> AUTOMATED PUBLISHING: AUTHORIZED` (see step 7b for the precise match rule — a mention of the phrase elsewhere in the file's prose does not count). If the file is missing, unreadable, or lacks that exact line, the skill publishes a **draft** and says so in its report. There is no way to publish live without this file — deleting or editing out the marker line instantly reverts the skill to draft-only.
2. **One-post-per-day cap.** The skill publishes at most **one** post per day (live or draft). If the state file already records a publish for today, it refuses to publish again rather than posting a duplicate.

Never publish live by any other route (e.g., hand-passing `--status publish` outside these rails). The rails exist so the pipeline stays safe when it runs unattended after the original author has left the lab. See `AUTHORIZATION.md` for who approved live publishing and how to pause or disable it.

## State file — `digests/.literature-state.json`

This skill keeps persistent state in `digests/.literature-state.json` (path relative to the repository root), mirroring the union/persist pattern of `digests/.digest-state.json`. It has this shape:

```json
{
  "last_run_date": "2026-08-10",
  "connected_urls": [
    "https://genefish.wordpress.com/2026/08/09/some-real-finding/"
  ],
  "publish_log": [
    {"date": "2026-08-10", "status": "draft", "url": "https://genefish.wordpress.com/?p=123"}
  ]
}
```

`connected_urls` is the set of every post URL this skill has already processed (turned into a literature section) in any previous run. It is committed to the repo — **never** add it to `.gitignore` — so de-duplication works across machines and collaborators.

`publish_log` records every post this skill has published, one entry per publish, each with the `date` (YYYY-MM-DD) it was published, the `status` it was published with (`"draft"` or `"publish"`), and the resulting post `url`. It drives the **one-post-per-day cap** (step 7): the number of entries whose `date` equals today is the count of posts already published today.

- **If the file does not exist** (first run): treat `connected_urls` as an empty set and `publish_log` as an empty list, exclude nothing on that basis, and create the file in the state-update step below.
- **If `publish_log` is missing from an older state file:** treat it as an empty list (no publishes recorded yet) and add it when you next write the file.
- Match on the canonical post URL only. Treat URLs that differ solely by a trailing slash as the same URL.

## Steps

### 1. Fetch today's posts

Run:

```
python3 scripts/fetch_lab_posts.py --days 3
```

**If the invoker specified a window, use that number instead of 3.** A request like "run
the daily-literature-post skill over a window of the last 9 days" means `--days 9`. This
is how a catch-up run is performed after an outage (see below). Absent an explicit
window, always use 3.

**Why 3 days and not 1.** The window is deliberately wider than the daily cadence. When
this skill runs unattended, a scheduled run can be delayed or skipped entirely (GitHub
Actions cron is best-effort, and a machine running `cron` can be asleep or offline). With
a 1-day window, a single missed run drops that day's findings **permanently** — the posts
fall outside every subsequent window and are never connected.

A wider window costs nothing because step 2's `connected_urls` check already guarantees a
post is processed at most once, ever. Re-reading a post that was already handled yesterday
is a no-op, so the overlap simply lets a late run catch up on what a missed run skipped.
Do not narrow this back to `--days 1`; the de-duplication, not the window, is what
prevents repeats.

**The window is what bounds that self-healing, so know its limit.** A gap *longer* than
the window is not recovered by it — those posts fall outside every subsequent window and
are lost exactly as they would be with `--days 1`. This is not hypothetical: a CI
permission fault stalled every run from 2026-08-25 to 2026-09-01, an 8-day gap against a
3-day window, and the posts from 2026-08-25 to 2026-08-28 were never evaluated. Recovering
from a gap that long requires an explicit wider window, which is what the paragraph above
is for; the daily workflow exposes it as a `days` dispatch input.

Parse the JSON `posts` array. Each post has `author`, `date`, `title`, `url`, `content`, and `categories`.

**If `posts` is empty, exit quietly.** Produce no post, write no file, do not touch the state file, and print nothing beyond a brief note that there were no posts today. This is a silent no-op, not an error.

### 2. Exclude already-processed posts (state file)

Read `digests/.literature-state.json` (see above). Drop any fetched post whose canonical `url` is already in `connected_urls`. These have been connected in a previous run and must not be processed again.

### 3. Exclude automated pipeline output (this skill's and full-lab-digest's)

Drop any remaining post that is automated pipeline output — either this skill's own prior drafts, or the `full-lab-digest` skill's published digests. These are aggregated/meta posts, not primary lab findings; connecting them would feed the pipeline its own (or a sibling pipeline's) output. Exclude a post if **any** of the following match:

- **This skill's own output (title):** the post's `title` begins with `Daily Literature Connections —` (case-insensitive; the em dash is what step 6's H1 template emits → WordPress title, e.g. `Daily Literature Connections — 2026-08-18`). **This is the reliable check for this skill's own output** — match on it first.
- **This skill's own output (category):** the post's `categories` list (returned by `fetch_lab_posts.py`) contains the exact name `auto-literature-connections`. Since 2026-08-25 the category exists on the site, so posts published by this skill with `--category auto-literature-connections` now come back from the WordPress API with the category attached — this check works as a real second signal. The title check above is still the primary guard; keep both.
- **Full Lab Digest output (title):** the post's `title` begins with `Full Lab Digest —` (case-insensitive; the em dash is what the `full-lab-digest` skill emits as its H1 → WordPress title, e.g. `Full Lab Digest — 2026-08-04 to 2026-08-10 (7 days)`). Match on the title prefix, not on content — do **not** rely on inferring "this is a digest" from the body alone.
- **Full Lab Digest output (category):** the post's `categories` list contains `full-lab-digest`, if present. `full-lab-digest` is normally published via `wordpress-publisher` **without** a `--category`, so it typically lands as `Uncategorized` and this check will usually not fire — the title check above is the reliable one. Keep this category check anyway as belt-and-suspenders in case a digest is ever tagged.

This is a **belt-and-suspenders** check alongside step 2's state-file check — apply both. A post is excluded if the state file (step 2) or **any** of the tests above flag it. Do not treat this as a substitute for step 4's real-finding filter; a digest whose title check somehow fails would still be caught there, but that content-based catch is not guaranteed reliable long-term, which is why the explicit title/category exclusion above exists.

### 4. Keep only posts with a real scientific finding

For each surviving post, read its `content` and decide whether it describes a **real scientific finding** — a concrete experimental result, a measurement, an observation, a molecular/physiological outcome, a data analysis conclusion, etc.

**Exclude** posts that are purely logistical: meeting notes, scheduling or goals updates, equipment or reagent orders, inventory, lab-management notes, protocol drafting with no result yet, and similar. When a post has no genuine finding, **skip it — do not invent one.**

If **every** post today is logistical (nothing survives this filter), treat the day as empty: behave exactly like step 1's empty case — produce nothing, write nothing, touch no state — and report that nothing qualified today.

### 5. Derive TOPIC + FINDING and run `literature-connector` per post

For each surviving post with a real finding:

- Derive a concise **TOPIC** — the biological/scientific subject (e.g., `"PolyIC immune priming in Pacific oysters"`).
- Derive a **FINDING** — one or two sentences describing the specific lab result from the post body (e.g., `"VIPERIN is upregulated by PolyIC but HSP70 is not, suggesting pathway specificity."`).

Then invoke the `literature-connector` skill exactly as if the user had typed:

> `/literature-connector` TOPIC: [topic phrase] FINDING: [finding description]

Run these searches **sequentially, not in parallel**, to avoid hitting the PubMed / Europe PMC rate limits. All of `literature-connector`'s constraints carry over unchanged — most importantly the no-hallucination-on-failed-fetch rule: a paper appears only if its abstract was successfully retrieved.

**Per-post inclusion rule:** a post's section is included in the assembled post **only if** `literature-connector` returns at least one relevant paper whose abstract was successfully retrieved. If a post yields no relevant literature, omit that post's section entirely (do not write a placeholder) — but the post is still recorded as processed in the state file (step 8), since it was genuinely evaluated.

If, after all searches, **no** post yielded any relevant literature, produce no post (nothing to publish), but still record the processed URLs in the state file per step 8, and report that nothing qualified.

### 6. Assemble the Markdown post

Build a single Markdown document with one section per included source post. The first line must be a Markdown `# ` H1 (it becomes the WordPress post title — `publish_digest.py` strips it from the body). Use today's date (`2026-08-10`-style) in the title.

```
# Daily Literature Connections — [today's date]

> Automated draft — each section links a finding from a recent lab notebook post to recent PubMed publications and preprints. **Preprints have not been peer-reviewed.**

---

## [Source post title]

**Source:** [author], [post date] · [post url]
**Finding:** [the FINDING sentence(s) you derived]

[paste the "Relevant Literature" entries from this post's literature-connector output — each with its source badge, relationship tag, title, citation line, and 2–3 sentence summary]

**Literature summary:** [paste the 2–4 sentence synthesis from the literature-connector's Summary section]

---

[repeat one section per included source post]

> Generated by the `daily-literature-post` skill · [today's date] · draft, not peer-reviewed
```

- Preserve `literature-connector`'s **relationship tags** (Supports / Conflicts / Adds context / Suggests next step) and **source badges** (`[PubMed]`, `[bioRxiv preprint — not peer-reviewed]`, etc.) verbatim — do not rewrite them.
- Carry over the **preprint caveat block** from `literature-connector` at the bottom of the assembled post (the blockquote noting coverage is limited to the last 12 months and that preprints are not peer-reviewed) so the caveat travels with the published draft. Do not copy `literature-connector`'s full header block (query strings, retrieval counts) into the post.

### 7. Enforce the daily cap, decide live vs. draft, then publish

Write the assembled Markdown to a file first (so `publish_digest.py` can read it), e.g. `digests/daily-literature-[today].md`. Then run the two safety rails **in this order** before publishing.

#### 7a. Daily cap — refuse a second post today

Read `digests/.literature-state.json` and count the entries in `publish_log` whose `date` equals today (YYYY-MM-DD). **If that count is 1 or more, do not publish anything.** Stop here: produce no new post, leave the state file unchanged, and report in step 9 that the skill has already published today and is refusing a second post per the one-post-per-day cap (quote the existing entry's status and URL). This is a hard stop, not a warning — it prevents duplicate posts if the skill is triggered twice in a day.

If the count is 0, continue.

#### 7b. Authorization check — live only if explicitly authorized

Decide the publish status by inspecting `AUTHORIZATION.md` at the repository root:

- Read the file at `AUTHORIZATION.md` (repo root).
- **Publish live** (`--status publish`) **only if** the file exists, is readable, and at least one line — stripped of leading/trailing whitespace — is **exactly** `> AUTOMATED PUBLISHING: AUTHORIZED` (the blockquote marker line under "Authorization marker"). A match anywhere else in the file — inline in a sentence, inside a code span, in explanatory prose — does **not** count, even if the characters are identical. This is deliberately stricter than a substring search: prose elsewhere in the file (including this very instruction) legitimately contains the phrase, and a substring match would treat that prose as authorization.
- **Otherwise fall back to draft** (`--status draft`): if the file is missing, cannot be read, or no line matches exactly. Do not attempt to "fix" or interpret a near-miss marker — anything other than that exact standalone line means draft.

Remember which mode you chose; you must report it in step 9.

#### 7c. Publish

Publish with the status you determined in 7b:

```
# When AUTHORIZATION.md authorizes live publishing:
python3 scripts/publish_digest.py digests/daily-literature-[today].md --category auto-literature-connections --status publish

# Otherwise (default / unauthorized fallback):
python3 scripts/publish_digest.py digests/daily-literature-[today].md --category auto-literature-connections --status draft
```

`--status draft` is also the script's default, so omitting `--status` is equivalent to the draft command; pass it explicitly here to make the chosen mode unambiguous. The `--category auto-literature-connections` flag tags the post as a secondary signal for step 3. The category was created on the site on 2026-08-25, so the tag now takes effect and posts come back with it attached — the publishing token can attach an existing category but still **cannot create new ones**, so this depends on the category continuing to exist on the site. Step 3's title-prefix check remains the primary guard that excludes this skill's own posts; the category is now a working redundant second layer.

Confirm the command returned an HTTP 200/201 and a URL before proceeding, and note the reported `post_status` (`publish` or `draft`) — it should match the mode you intended. If publishing fails, report the error and **do not** update the state file (step 8) — the posts were not successfully connected/published, so they should remain eligible for the next run.

### 8. Update the state file

After a successful publish, update `digests/.literature-state.json`:

- Set `last_run_date` to today's date (YYYY-MM-DD).
- Add every post URL **processed this run** to `connected_urls` (union — keep all existing entries, append the new ones, no duplicates). "Processed" means every post that survived steps 2–4 and was evaluated by `literature-connector` in step 5 — **including** posts whose section was omitted for lack of relevant literature. This ensures a logistical-free post with no literature hits is not re-evaluated tomorrow.
- **Append one entry to `publish_log`** recording this publish: `{"date": "<today>", "status": "<publish|draft>", "url": "<the URL publish_digest.py returned>"}`. Use the actual `post_status` from the publish output for `status`. This entry is what the step 7a cap reads tomorrow — and, if the skill is somehow triggered again today, what makes 7a refuse a second post.
- Do not add posts excluded in steps 2–4 as logistical/already-processed/own-output (already-processed ones are already present; logistical and own-output ones were never real candidates).
- If the file did not exist, create it now with `last_run_date` = today, `connected_urls` = the processed URLs, and `publish_log` = a list containing the single entry for this publish.
- Write valid JSON with the same three top-level keys (`last_run_date`, `connected_urls`, `publish_log`). Keep the file committed — never gitignore it.

### 9. Report back

In the main conversation, report one of:

- **Published:** the post URL, **whether it went out live or as a draft**, and — when it fell back to draft — the reason (no `AUTHORIZATION.md`, missing/altered `AUTOMATED PUBLISHING: AUTHORIZED` marker, or unreadable file). Also give how many source posts were included and their titles.
- **Refused (daily cap):** the skill already published today. Report that it is refusing a second post per the one-post-per-day cap, and quote today's existing `publish_log` entry (status + URL). The state file is left unchanged.
- **Nothing qualified today:** state plainly why (no posts in the window, all posts logistical, all already processed, or no relevant literature found for any finding). Note whether the state file was updated (it is only updated when at least one post was actually evaluated by `literature-connector`).

Never fabricate a published post or literature results, and never claim a post was published live when it fell back to draft — if a step produced nothing, say so.
