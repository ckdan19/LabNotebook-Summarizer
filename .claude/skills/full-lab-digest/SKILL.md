# Full Lab Digest Skill

Trigger this skill when the user asks for the **full weekly lab digest**, a **combined digest of all lab notebooks**, or a digest that covers **all sources** / **all notebooks**.

## What this skill does

Runs all six lab-notebook subagents in parallel, collects their summaries, and compiles them into a single Markdown file organized by source. The window defaults to the last 7 days, but the user can request any window ("a full lab digest for the last 14 days").

The skill keeps persistent state in `digests/.digest-state.json` so that a post already covered in a previous digest is never covered again, even if it still falls inside the requested window. That file is committed to the repo (never gitignored) so the de-duplication works across machines and collaborators.

## Steps

1. **Determine the window**: set `days` to the number of days the user asked for (e.g. "the last 14 days", "past month" → 30). If the user did not specify a window, `days` = 7. Use this same `days` value everywhere below.

2. **Launch all six subagents in parallel** in a single message (do NOT run them one at a time). Substitute `days` into the prompt:

   - `tumbling-oysters-agent` — prompt: "Summarize all posts from the last [days] days. Return a structured Markdown summary with a ## header, the post titles/dates/URLs, and 2–3 sentence summaries. If there are no posts, say so explicitly."
   - `ariana-notebook-agent` — same prompt as above
   - `sams-notebook-agent` — same prompt as above
   - `grace-notebook-agent` — same prompt as above
   - `megan-notebook-agent` — same prompt as above
   - `wordpress-agent` — same prompt as above

   Each subagent passes the window to its fetch script as `--days [days]`.

   Wait for **all six** to return before proceeding.

3. **Load digest state and exclude already-covered posts.** The digest tracks which posts have appeared in a previous digest so no post is ever covered twice.

   - **Read the state file** at `digests/.digest-state.json` (path is relative to the repository root). It has this shape:

     ```json
     {
       "last_digest_date": "2026-07-28",
       "digested_urls": [
         "https://robertslab.github.io/sams-notebook/posts/2026/2026-07-22-...-Glo-Assay/",
         "https://grace-ac.github.io/resubmit-crab/"
       ]
     }
     ```

     `digested_urls` is the set of every post URL that has appeared in any previous digest, across all six sources.

   - **If the state file does not exist** (first run): treat `digested_urls` as an empty set, treat every post as new, and do not exclude anything. You will create the file in the state-update step below.

   - **Cross-reference each post** from every subagent summary against `digested_urls`. A post is "already-covered" if its canonical post URL is present in `digested_urls`. Match on the canonical post URL only (the link to the notebook entry itself) — ignore image links, repo-root links, and literature links, which are never tracked. Treat URLs that differ only by a trailing slash as the same URL.

   - **Exclude already-covered posts** from the per-source summaries before compiling the digest. Keep track, per source, of (a) how many posts remain (newly-included) and (b) how many were excluded as already-covered.

   - **Collect the newly-included URLs** across all sources into a running list — you will write these to the state file in the state-update step.

4. **Tally activity**: count how many sources have at least one *newly-included* post ("had activity") and how many have none ("no activity") after the exclusion step above. A source whose posts were all excluded as already-covered counts as "no activity" for this tally.

5. **Determine the date range**: use the `days`-day window ending on today's date.
   - `week_start` = today minus (`days` − 1) days (YYYY-MM-DD) — e.g. today minus 6 for a 7-day window, today minus 13 for a 14-day window
   - `week_end` = today (YYYY-MM-DD)

6. **Assemble the combined digest** using this exact structure:

```
# Full Lab Digest — [week_start] to [week_end] ([days] days)

> [N] of 6 sources had activity in the last [days] days. [M] had none.

---

## Tumbling Oysters (Steven Roberts)

[paste the tumbling-oysters-agent summary verbatim here]

---

## Ariana Huffmyer Lab Notebook

[paste the ariana-notebook-agent summary verbatim here]

---

## Sam's Notebook (Sam White)

[paste the sams-notebook-agent summary verbatim here]

---

## Grace Crandall's Notebook

[paste the grace-notebook-agent summary verbatim here]

---

## Megan Ewing Lab Notebook

[paste the megan-notebook-agent summary verbatim here]

---

## Genefish WordPress

[paste the wordpress-agent summary verbatim here]

---

## Cross-Notebook Patterns & Connections

_This section analyzes the compiled per-source summaries for shared themes, follow-up narratives, apparent contradictions, and multi-week historical connections across the lab's notebooks. Connections are surfaced only when a specific named entity ties the sources together — never from vague thematic similarity._

[cross-notebook analysis — same-window patterns per step 7, plus Historical Connections per step 8]

---

## Data & Figures

_This section consolidates, grouped by source, the figure links and external data/repository links already surfaced in the per-source summaries above. It is a single entry point into the underlying data and figures for this window, not a new analysis._

[consolidated data & figure links — see step 9. Omit this entire section, including the heading and note above, if no figures or data links appear anywhere in the current window's posts.]

---

## Literature Connections

[literature search results — see step 10]

---

> Generated by the `full-lab-digest` skill · [week_start] to [week_end] ([days]-day window)
```

   - Paste each subagent's output verbatim under its `##` header — do **not** rewrite or paraphrase the per-source sections. When a subagent's summary lists individual posts, drop the entries for posts that were excluded as already-covered in step 3, but leave the wording of the surviving entries untouched.
   - If, after the step 3 exclusion, a source has any posts that were excluded as already-covered, add one line at the end of that source's section noting the count, e.g. `_2 posts from this window were already covered in a previous digest and are omitted here._` (Use "1 post ... was" for a single post.)
   - If a subagent reported no activity, or all of its posts were excluded as already-covered, write a single line under that section's header: `_No new posts in the last [days] days._` — followed by the already-covered note above if any posts were excluded.

7. **Write the Cross-Notebook Patterns & Connections section** by analyzing only the six compiled summaries (not the original source content). Look for three specific types of connections:

   - **Shared themes** — the same named topic, organism, assay, or method appearing in two or more summaries in this window. Examples of qualifying shared entities: the same species name, the same assay (e.g., "qPCR"), the same treatment (e.g., "PolyIC immune priming"), the same named project. Vague thematic overlap (e.g., "both involve marine biology" or "both discuss oysters in general") does not qualify.

   - **Temporal narratives** — a result, question, or problem raised in one source that another source appears to follow up on, respond to, or resolve later in the same window. To qualify, there must be a specific shared entity (same organism + assay, same named experiment, same person mentioned in both) and a plausible causal or sequential relationship.

   - **Apparent contradictions** — two sources reporting what looks like conflicting results on a similar topic. For any apparent contradiction, explicitly note: (a) that the finding needs human verification, and (b) what would resolve it (e.g., different methodology, different life stage, different species).

   **Conservatism rules:**
   - Only surface a connection if there is a real, specific shared entity tying the sources together.
   - If a window has no genuine cross-notebook connections, write: `_No cross-notebook connections identified in this window._` — do not manufacture a connection.
   - Do not invent connections from vague thematic similarity.

   Format the section as a bulleted list grouped under the three sub-headings below. Omit any sub-heading that has no findings (do not write "None" under it — simply skip it):

   ```
   ### Shared Themes
   - [bullet per connection]

   ### Temporal Narratives
   - [bullet per narrative]

   ### Apparent Contradictions
   - [bullet per contradiction, each ending with: "⚠️ Needs human verification — [one sentence on what would resolve it]."]

   ### Historical Connections
   - [bullet per multi-week connection — see step 8]
   ```

   If there are no same-window connections at all (Shared Themes, Temporal Narratives, and Apparent Contradictions are all empty), write `_No cross-notebook connections identified in this window._` in place of those three sub-headings — but still run step 8 and append the `### Historical Connections` sub-heading below that line if step 8 finds anything. Only if step 8 also finds nothing is the section body entirely this one line.

8. **Write the Historical Connections subsection** (the `### Historical Connections` sub-heading inside Cross-Notebook Patterns & Connections). Run this **after** the same-window pattern detection in step 7 has finished, because it operates on the findings that step 7 (and the step-10 selection rule) already flagged as notable. This subsection reaches back into the lab's own archive to find multi-week story arcs that the single-window analysis cannot see.

    **Selecting findings to check:** use the **exact same prioritization as step 10's literature-connector selection** — every specific finding named in the Cross-Notebook Patterns & Connections same-window subsections (Shared Themes, Temporal Narratives, Apparent Contradictions), plus the same 2–4 additional substantial standalone findings from the per-source summaries. Do not build a separate list; reuse the step-10 finding set so the two sections stay in sync.

    **Query scope — the prior 8 weeks, excluding the current window.** Define:
    - `hist_start` = `week_start` minus 56 days (YYYY-MM-DD)
    - `hist_end` = `week_start` minus 1 day (YYYY-MM-DD)

    Only archive posts with `date` between `hist_start` and `hist_end` inclusive are eligible. This deliberately excludes the current window (`week_start`…`week_end`) so this subsection never re-surfaces a post already shown in the per-source sections or the same-window analysis above. Note that `posts.date` is `NULL` on a few archived posts; the `BETWEEN` bound evaluates to false for those, so undated posts are intentionally excluded (a post with no date cannot be placed in the 8-week window) — this is expected, not a bug. As a second guard, also discard any archive result whose `url` matches a post already surfaced anywhere in this digest (per-source sections or step 7 bullets), so nothing is duplicated across the digest.

    **Querying the archive — read-only, exactly like `lab-archive`.** Open the same read-only connection and issue only `SELECT`s; never write to or rebuild the database. If `.cache/archive.db` does not exist (or has no `posts` table), do not build it — skip this subsection entirely and note nothing (the rest of the digest proceeds normally). For each selected finding, reduce it to the **specific named entities** it involves (the exact species, the exact assay/method, the named project or experiment) and build an FTS5 `MATCH` string over those entities, following `lab-archive`'s term-derivation and sanitization rules (quote any term containing FTS5 syntax characters, group synonyms with `OR`, use prefix `*` where helpful).

    **Run every finding's query in one script invocation, not one per finding.** These are local, read-only lookups against the same open connection with no external rate limit to respect (unlike step 10's literature searches), so there is no reason to pay a separate tool round-trip per finding. Loop over the full set of match strings in a single Python process and print one structured result per finding (e.g. a JSON object keyed by finding label) so the whole subsection's data comes back in one turn:

    ```python
    import json, sqlite3
    conn = sqlite3.connect("file:.cache/archive.db?mode=ro", uri=True)
    SQL = """
    SELECT p.author, p.source, p.date, p.title, p.url, p.shadowed,
           snippet(posts_fts, 1, '**', '**', ' … ', 12) AS snip
    FROM posts_fts f
    JOIN posts p ON p.id = f.rowid
    WHERE posts_fts MATCH ?
      AND p.date BETWEEN ? AND ?
    ORDER BY p.date DESC, bm25(posts_fts)
    LIMIT 40
    """
    results = {}
    for label, match_string in findings.items():  # one entry per selected finding
        try:
            rows = conn.execute(SQL, (match_string, hist_start, hist_end)).fetchall()
        except sqlite3.OperationalError:
            # FTS5 syntax error — re-quote exactly as lab-archive does, then retry once.
            rows = conn.execute(SQL, (requoted_match_string, hist_start, hist_end)).fetchall()
        results[label] = rows
    print(json.dumps(results, default=str))
    ```

    Each finding's query, date bound, column list, and re-quote-on-syntax-error handling are unchanged from before — only the number of tool round trips changes (one script covering every finding instead of one script per finding). Parse the single JSON result and apply the rest of this step (relevance checks, formatting, omission rules) exactly as below.

    **What counts as a connection (conservatism carries over).** A candidate archive post qualifies **only** if it shares a **real, specific, named entity** with the current finding — the same species, the same assay, the same named project/experiment — **and** reads as though it *sets up*, *follows up on*, *resolves*, or *contradicts* the current finding across the weeks. Apply the same conservatism rule as step 7: never surface a connection built on a vague thematic match ("both about oysters", "both involve stress") — the shared entity must be specific and named. Apply `lab-archive`'s relevance check too: discard incidental keyword hits where the entity is only mentioned in passing.

    **Contradictions get flagged for verification.** If a candidate connection looks like it might be an **apparent contradiction** (the archived post's result appears to conflict with the current finding) rather than a clean set-up/follow-up/resolution, flag it the same way step 7's Apparent Contradictions subsection does: end that bullet with `⚠️ Needs human verification — [one sentence on what would resolve it].`

    **Shadowed posts.** If a qualifying archive post has `shadowed = 1`, append the same caveat `lab-archive` uses next to its link: `⚠️ *shadowed URL — this permalink is shared by another post in the same notebook, so it may not resolve to this exact post on the live site; verify against the source before treating it as a clean live link.*`

    **Omit silently when empty per finding.** Most findings will have no multi-week connection — that is expected. For a finding with no genuine historical connection, **write nothing at all** for it in this subsection (do not add a "none found" line per finding — that would be noise). Only if **no finding** across the whole set yields any connection do you write the single line:
    `_No historical connections identified in the last 8 weeks._`
    (In that case the `### Historical Connections` sub-heading is still shown with just that line, unless the entire Cross-Notebook section collapsed to the "no cross-notebook connections" line per step 7, in which case omit the sub-heading.)

    **Format** each surviving connection as one bullet under `### Historical Connections`, naming the shared entity, the direction of the arc, and citing the archived post by its actual `url` (never reconstruct a URL — cite the `url` the query returned):

    ```
    ### Historical Connections
    - **[shared entity]** — [current finding, and how the archived post sets it up / follows up / resolves / contradicts it]. See [archived post title] · [YYYY-MM-DD] ([author], [source label]): [permalink]
      [⚠️ shadowed-URL caveat, only if shadowed=1]
      [⚠️ Needs human verification — ..., only if this is an apparent contradiction]
    ```

9. **Write the Data & Figures section** by consolidating the figure and data/repository links that the six subagents already surfaced in their per-source summaries. This is a reorganization step only — it uses the compiled summaries you already have and issues no new fetches, subagent runs, or external calls.

   - **Gather the links.** Scan each per-source summary (the verbatim subagent output pasted under each `##` header, after the step-3 exclusion) for two kinds of links:
     - **Figure links** — the entries the subagents list under per-post `Figures:` listings, both local repo-hosted image paths and external image/figure URLs.
     - **Data/repository links** — any linked external dataset, repository, or data-hosting URL the subagent surfaced (e.g., a linked GitHub repo, an OSF/Zenodo/figshare record, a raw data file). Do **not** include the canonical post URL itself, or the repo-root/notebook-home links — those are navigation, not data.

   - **Sort each link into one of two output groups.** The two link kinds above form the **primary group** (this project's own data and figures). Then split out a **secondary group, "Related links (tools, issues)"**: of the links that already qualify under "Data/repository links," route the two kinds that are *references rather than underlying data* into this second group instead of the primary one — **third-party tool/software repositories** (e.g., `github.com/OpenGene/fastp`) and **issue-tracker threads** (e.g., a GitHub issue URL). This is a routing rule only; it does not change what counts as in-scope, and a link the "Data/repository links" bullet already excludes stays excluded.

   - **Only use links that already appear in the compiled summaries.** Never invent a figure or data link, and never reconstruct one from memory — if a subagent did not surface it, it does not go here.

   - **Group by source**, using the same six source labels and order as the per-source sections above (Tumbling Oysters, Ariana Huffmyer, Sam's Notebook, Grace Crandall, Megan Ewing, Genefish WordPress). Under each source, list its **primary** figure and data links first; then, if that source has any tool/issue links, add a `_Related links (tools, issues):_` line followed by those as sub-bullets. Attribute each link to the post it came from (post title or short label) so the entry point stays navigable. Omit a source that has no links in either group (do not write an empty source sub-heading), and omit the `_Related links (tools, issues):_` line for a source that has none.

   - **Deduplicate** obvious repeats — if the same URL appears more than once (e.g., the same figure linked from two posts, or an identical local path), list it once. Treat URLs that differ only by a trailing slash as the same URL.

   - **Skip the whole section if empty.** If no links of any kind (primary or related) exist anywhere in the current window's posts, omit the `## Data & Figures` heading and its explanatory note entirely — do not emit an empty heading or a "none found" line.

   - **Format:**

     ```
     ## Data & Figures

     _This section consolidates, grouped by source, the figure links and external data/repository links already surfaced in the per-source summaries above. It is a single entry point into the underlying data and figures for this window, not a new analysis._

     ### Tumbling Oysters (Steven Roberts)
     - [post title or short label]: [figure/data link]
     - …
     - _Related links (tools, issues):_
       - [post title or short label]: [third-party tool repo or issue-tracker URL]
       - …

     ### Ariana Huffmyer Lab Notebook
     - …
     ```

     (Include only the source sub-headings that have at least one link, and include the `_Related links (tools, issues):_` line only for sources that have at least one tool/issue link.)

10. **Write the Literature Connections section** by running the `literature-connector` skill for each notable finding. This step involves multiple external API calls and will take longer than the rest of the digest — that is expected.

   **Selecting findings to check:**
   - First, include every specific finding already named in the Cross-Notebook Patterns & Connections section (shared themes, temporal narratives, apparent contradictions). These are the highest-priority targets because they are the most scientifically notable and cross-validated.
   - Then scan the six per-source summaries for any additional standalone finding that appears substantial — a concrete experimental result, a surprising observation, or a well-defined molecular/physiological outcome. Aim for at most 2–4 additional standalone findings across all sources; skip routine protocol notes, scheduling updates, or findings already covered by the cross-notebook bullets.

   **For each selected finding**, invoke the `literature-connector` skill exactly as if the user had typed:

   > `/literature-connector` TOPIC: [concise topic phrase] FINDING: [one or two sentences describing the specific lab result]

   Set TOPIC to the biological subject (e.g., `"PolyIC immune priming in Pacific oysters"`) and FINDING to the specific lab result (e.g., `"VIPERIN is upregulated by PolyIC but HSP70 is not, suggesting pathway specificity"`). Run these searches sequentially, not in parallel, to avoid hitting API rate limits.

   **Strict inclusion rule:** Include a finding's literature results in this section **only if the `literature-connector` skill returns at least one relevant paper whose abstract was successfully retrieved.** If the skill returns no relevant papers (or only papers with failed fetches), omit that finding entirely — do not write a placeholder, do not note the absence, just skip it. This rule preserves the no-hallucination guarantee: a finding only appears here if there is real literature to discuss.

   **No-hallucination-on-failed-fetch applies fully.** All constraints from the `literature-connector` skill carry over without modification: do not summarize any paper whose abstract was not retrieved via a successful HTTP response; do not use titles, DOIs, or prior knowledge to reconstruct failed records; report failed fetches only in the header counts inside each finding block, not as content.

   **Format for this section:**

   If at least one finding has relevant literature:

   ```
   ## Literature Connections

   > Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

   ### [Finding label — e.g., "PolyIC immune priming response in Pacific oysters"]

   **Source:** [which notebook(s) the finding came from]
   **Finding:** [1–2 sentence description of the lab result]

   [paste the "Relevant Literature" entries from the literature-connector output here, using the same format: source badge, relationship tag, title, citation line, 2–3 sentence summary]

   **Literature summary:** [paste the 2–4 sentence synthesis paragraph from the literature-connector's Summary section]

   ---

   [repeat block for each finding with relevant literature]
   ```

   If no finding yields any relevant literature after all searches complete, write:
   `_No relevant literature found for any finding in this window._`

   Do not copy the literature-connector's full header block (query strings, retrieval counts, caveats) into the digest — those details belong in the literature-connector's own standalone output, not here. Carry over only the relevant literature entries and the summary paragraph per finding.

11. **Write the file** to:
   `digests/full-lab-digest-[week_end]-[days]d.md`
   (e.g. `digests/full-lab-digest-2026-07-13-7d.md` for a 7-day window, `digests/full-lab-digest-2026-07-27-14d.md` for a 14-day one)

   Always include the `-[days]d` suffix, including for the default 7-day window, so two digests ending on the same date with different windows never overwrite each other. Digests written before this convention have no suffix; leave those filenames alone.

   This path is relative to the repository root, which is the working directory Claude Code starts in.

12. **Update the digest state file** at `digests/.digest-state.json` so future digests know these posts have now been covered.

    - Set `last_digest_date` to today's date (`week_end`, YYYY-MM-DD).
    - Add the newly-included post URLs collected in step 3 to `digested_urls` (union — keep all pre-existing entries, append the new ones, and do not add duplicates). Do **not** add excluded/already-covered URLs again (they are already present), and do not add image, repo-root, or literature URLs.
    - If the state file did not exist (first run), create it now with `last_digest_date` set to today and `digested_urls` set to every post URL included in this digest.
    - Write valid JSON with the same two top-level keys. Keep this file committed alongside the digests — it must persist across machines and collaborators for the tracking to work, so never add it to `.gitignore`.

13. **Return the file path** to the user in the main conversation.
