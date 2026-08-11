# Daily Literature Post Skill

Trigger this skill when the user asks to **run the daily literature connection post**, **do today's literature connections**, **run the daily lit post**, or any similar phrasing that means "look at today's lab posts and connect their findings to the published literature."

## What this skill does

Fetches the last day of lab notebook posts, keeps only the ones that describe a **real scientific finding**, runs the `literature-connector` skill against each finding, and assembles the results into a single Markdown post published to WordPress as a **draft**. The draft is tagged with the `auto-literature-connections` category so it is excluded from future daily runs, and every post it processes is recorded in `digests/.literature-state.json` so it is never processed twice.

This is a narrow daily counterpart to `full-lab-digest`: it does not summarize the notebooks, run subagents, or search the archive — it only connects today's genuine findings to external literature.

**Draft only.** This skill never publishes live. It always publishes with `status: draft` (which `publish_digest.py` does unconditionally). Do not change this without an explicit instruction from the user.

## State file — `digests/.literature-state.json`

This skill keeps persistent state in `digests/.literature-state.json` (path relative to the repository root), mirroring the union/persist pattern of `digests/.digest-state.json`. It has this shape:

```json
{
  "last_run_date": "2026-08-10",
  "connected_urls": [
    "https://genefish.wordpress.com/2026/08/09/some-real-finding/"
  ]
}
```

`connected_urls` is the set of every post URL this skill has already processed (turned into a literature section) in any previous run. It is committed to the repo — **never** add it to `.gitignore` — so de-duplication works across machines and collaborators.

- **If the file does not exist** (first run): treat `connected_urls` as an empty set, exclude nothing on that basis, and create the file in the state-update step below.
- Match on the canonical post URL only. Treat URLs that differ solely by a trailing slash as the same URL.

## Steps

### 1. Fetch today's posts

Run:

```
python3 scripts/fetch_lab_posts.py --days 1
```

Parse the JSON `posts` array. Each post has `author`, `date`, `title`, `url`, `content`, and `categories`.

**If `posts` is empty, exit quietly.** Produce no post, write no file, do not touch the state file, and print nothing beyond a brief note that there were no posts today. This is a silent no-op, not an error.

### 2. Exclude already-processed posts (state file)

Read `digests/.literature-state.json` (see above). Drop any fetched post whose canonical `url` is already in `connected_urls`. These have been connected in a previous run and must not be processed again.

### 3. Exclude automated pipeline output (this skill's and full-lab-digest's)

Drop any remaining post that is automated pipeline output — either this skill's own prior drafts, or the `full-lab-digest` skill's published digests. These are aggregated/meta posts, not primary lab findings; connecting them would feed the pipeline its own (or a sibling pipeline's) output. Exclude a post if **any** of the following match:

- **This skill's own drafts (category):** the post's `categories` list (returned by `fetch_lab_posts.py`) contains the exact name `auto-literature-connections`.
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

> Automated draft — each section links a finding from a lab notebook post published in the last day to recent PubMed publications and preprints. **Preprints have not been peer-reviewed.**

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

### 7. Publish as a draft, tagged with the category

Write the assembled Markdown to a file first (so `publish_digest.py` can read it), e.g. `digests/daily-literature-[today].md`, then publish:

```
python3 scripts/publish_digest.py digests/daily-literature-[today].md --category auto-literature-connections
```

`publish_digest.py` always posts with `status: draft` — this is draft-only by design. The `--category auto-literature-connections` flag tags the draft so step 3 of future runs correctly excludes it (WordPress creates the category if it does not already exist).

Confirm the command returned an HTTP 200/201 and a draft URL before proceeding. If publishing fails, report the error and **do not** update the state file (step 8) — the posts were not successfully connected/published, so they should remain eligible for the next run.

### 8. Update the state file

After a successful publish, update `digests/.literature-state.json`:

- Set `last_run_date` to today's date (YYYY-MM-DD).
- Add every post URL **processed this run** to `connected_urls` (union — keep all existing entries, append the new ones, no duplicates). "Processed" means every post that survived steps 2–4 and was evaluated by `literature-connector` in step 5 — **including** posts whose section was omitted for lack of relevant literature. This ensures a logistical-free post with no literature hits is not re-evaluated tomorrow.
- Do not add posts excluded in steps 2–4 as logistical/already-processed/own-output (already-processed ones are already present; logistical and own-output ones were never real candidates).
- If the file did not exist, create it now with `last_run_date` = today and `connected_urls` = the processed URLs.
- Write valid JSON with the same two top-level keys. Keep the file committed — never gitignore it.

### 9. Report back

In the main conversation, report one of:

- **Published:** the draft URL, how many source posts were included, and their titles.
- **Nothing qualified today:** state plainly why (no posts in the window, all posts logistical, all already processed, or no relevant literature found for any finding). Note whether the state file was updated (it is only updated when at least one post was actually evaluated by `literature-connector`).

Never fabricate a published draft or literature results — if a step produced nothing, say so.
