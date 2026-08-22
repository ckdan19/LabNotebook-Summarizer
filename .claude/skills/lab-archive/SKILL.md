# Lab Archive Search Skill

Trigger this skill when the user asks a **question about the lab's own accumulated history** — phrased like **"has anyone done X before"**, **"what do we know about Y"**, **"has anyone in the lab worked on Z"**, **"did we ever try …"**, or **"search the archive for …"**. It answers by full-text-searching the local archive of every post the six lab notebooks have ever published, and reports back grouped by researcher with a cited source link for every claim.

This is distinct from the notebook agents (which fetch *recent* activity from GitHub/WordPress live) and from `literature-connector` (which searches *external* published literature). This skill searches **only the lab's own archived posts** already captured in `.cache/archive.db`.

## Scope — read-only

This skill **only queries** `.cache/archive.db`. It never creates, writes to, updates, or rebuilds the database — populating and refreshing the archive is `scripts/build_archive.py`'s job exclusively. Open every connection read-only and issue only `SELECT` statements. If the database is missing, do not attempt to build it (see "If the archive is missing" below).

## The database

`.cache/archive.db` is a SQLite database (git-ignored). There is **no `sqlite3` CLI** in this environment — query it with Python's built-in `sqlite3` module via the Bash tool.

Two relevant objects (created by `scripts/build_archive.py`):

- **`posts`** — one row per archived post, with columns:
  - `source` — one of `tumbling-oysters`, `grace`, `ariana`, `sams`, `megan`, `wordpress`
  - `author` — the researcher who wrote the post (this is what we group by)
  - `date` — `YYYY-MM-DD` (may be `NULL` on a few posts)
  - `title`
  - `url` — the **published permalink**, i.e. exactly what `notebook_parsing.derive_permalink(source, path)` produced for this post (for WordPress, the post's own URL). **This is the link to cite** — do not reconstruct URLs yourself.
  - `body_text`, `categories` (a JSON array string)
  - `shadowed` — `1` when this post's `url` is shared by another archived post of the same source, so the URL cannot uniquely resolve to it on the live site (see step 5).
  - `id` — primary key, used to join to the FTS index.
- **`posts_fts`** — an FTS5 full-text index over three columns, in this order: **`title` (col 0)**, **`body_text` (col 1)**, **`categories` (col 2)**. It is an external-content index whose `rowid` equals `posts.id`.

Join them as `posts_fts f JOIN posts p ON p.id = f.rowid`.

## Steps

### 1. Derive FTS5 search terms from the question

Take the user's plain-English question and reduce it to the **content terms** that would actually appear in a notebook post. Drop the question scaffolding ("has anyone", "before", "what do we know about", "did we ever"). Keep species names, genes/proteins, assays, methods, tissues, instruments, and chemicals.

Build an FTS5 `MATCH` string:

- **Group synonyms and near-equivalents with `OR`** so the first pass is reasonably broad but still on-topic. Example: question *"has anyone done DNA methylation analysis on oysters"* → `(methylation OR bisulfite OR "whole genome bisulfite" OR WGBS) AND (oyster OR Crassostrea OR Magallana OR gigas)`.
- **Quote multi-word phrases** that must stay adjacent: `"heat stress"`, `"gene ontology"`.
- Use a trailing `*` for **prefix matching** on word stems where helpful: `methyl*` matches methylation/methylated/methyltransferase.
- Keep the first query to roughly **2–4 concepts** combined with `AND`, each concept optionally an `OR` group of synonyms.

**Sanitize the terms.** FTS5 treats many characters (`-`, `.`, `/`, `(`, `:`, etc.) as syntax. Any bare term containing such a character, or a literal multi-word phrase, must be wrapped in double quotes inside the MATCH string (e.g. `"cGAS-STING"`, `"16S"`). Never pass a raw user string straight into MATCH unquoted. If in doubt, double-quote the term.

Record the exact MATCH string you used — it goes in the output header.

### 2. Query the archive (with a fallback pass, like literature-connector)

Run this query (read-only). Ranking is by FTS5 `bm25`; the `snippet()` call returns matching context from `body_text` with the hit wrapped in `**…**`:

```python
import sqlite3
conn = sqlite3.connect("file:.cache/archive.db?mode=ro", uri=True)
SQL = """
SELECT p.author, p.source, p.date, p.title, p.url, p.shadowed,
       snippet(posts_fts, 1, '**', '**', ' … ', 12) AS snip
FROM posts_fts f
JOIN posts p ON p.id = f.rowid
WHERE posts_fts MATCH ?
ORDER BY bm25(posts_fts)
LIMIT 40
"""
rows = conn.execute(SQL, (match_string,)).fetchall()
```

Notes:
- `snippet`'s second argument `1` selects the `body_text` column for the excerpt. If a row's `body_text` snippet comes back empty, fall back to snippetting the title (column `0`) or just show the title.
- Wrap the `MATCH` call in a try/except: an FTS5 syntax error means a term slipped through unquoted — re-quote and retry rather than crashing.

**Fallback / broadening — mirror literature-connector's pattern.** If the first query returns **no rows** (or only rows that fail the relevance check in step 4):

1. **Broaden once:** drop the most specific `AND` concept (e.g. keep organism + process, drop the specific assay name), and/or add prefix `*` stems and a couple more synonyms to the remaining `OR` groups. Re-run.
2. **Reformulate once more if still empty:** try the next-most-likely vocabulary the labs actually use (e.g. swap a formal term for lab shorthand, or an organism common name for its genus). Re-run.

Do at most these two extra passes. Record every MATCH string you tried for the output header. If all passes come back empty or irrelevant, go to step 6.

### 3. Group results by researcher (author)

Collapse the returned rows **by `author`**. Within each author, sort their posts newest-first by `date` (`NULL` dates last). Across authors, order by the strength of the best match (the top-ranked post's bm25) or simply by number of on-topic hits — put the researcher with the most relevant work first.

Deduplicate: if the same post appears twice, keep it once. Cap at roughly the top **3–5 posts per author** so the answer stays readable; note if more exist.

### 4. Relevance check (don't stretch a keyword match)

Before including a post, confirm the snippet/title actually concerns the user's question — that the matched term is used in the relevant sense, not an incidental mention. A post that merely contains the word "stress" in an unrelated aside is **not** a hit for a heat-stress question. Discard incidental matches. This is the same discipline `literature-connector` applies to abstracts.

### 5. Flag shadowed posts

For any included post with `shadowed = 1`, add an explicit inline caveat next to its link, e.g.:

> ⚠️ *shadowed URL — this permalink is shared by another post in the same notebook, so it may not resolve to this exact post on the live site; verify against the source before treating it as a clean live link.*

This is the collision issue found in Grace's notebook (Jekyll's `permalink: /:title/` collapses same-slug posts from different years onto one URL). Never present a shadowed post's URL as if it were a guaranteed clean live link.

### 6. If nothing relevant is found

If after the broadening/reformulation passes there are still no genuinely relevant posts, **say so plainly**:

> No posts in the lab archive appear to address [topic]. (Searched: `<each MATCH string tried>`.)

Do **not** stretch a loose keyword match into a false positive, and do not invent or infer an answer from the labs' general area of work. Absence of a result is a valid, useful answer.

### 7. Assemble the output

Format the answer as:

```markdown
# Lab Archive — [restated question]

**Searched:** `<final MATCH string>` [· plus fallbacks: `<...>`, `<...>` if used]
**Matched:** [N] post(s) across [M] researcher(s)

---

## [Researcher name] — [source label]

- **[Post title]** · [YYYY-MM-DD]
  > … matching snippet with the hit **highlighted** …
  [permalink URL]
  [⚠️ shadowed-URL caveat, only if shadowed=1]

- **[Next post]** · [date]
  > … snippet …
  [permalink]

## [Next researcher] — [source]

...

---

## Summary

[2–3 sentences: who in the lab has touched this, and how much. Every specific claim
here must point to one of the cited posts above — no finding stated without its link.]
```

Source labels: `tumbling-oysters` → Tumbling Oysters, `grace` → Grace's notebook, `ariana` → Ariana's notebook, `sams` → Sam's notebook, `megan` → Megan's notebook, `wordpress` → genefish WordPress. Note that WordPress and Tumbling Oysters have many authors, so the same source may appear under several researchers.

## Citation discipline (hard rule)

Every post you reference must be cited with its actual `url` (the `derive_permalink` output stored in the `posts` table). **Never paraphrase, summarize, or assert a finding without linking to the specific source post it came from** — this mirrors `literature-connector`'s citation rule. Do not merge findings from several posts into one uncited claim. If you cannot point to a specific archived post for a statement, do not make the statement. Do not fabricate titles, dates, authors, or URLs — report only what the query returned.

## If the archive is missing

If `.cache/archive.db` does not exist (or has no `posts` table), do not build it and do not guess an answer. Tell the user the archive has not been built yet and that `scripts/build_archive.py` needs to be run first, then stop.
