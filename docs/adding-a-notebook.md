# Adding a new GitHub-hosted notebook

This walks through everything that has to change to add a fifth (or sixth) GitHub-hosted
lab notebook to the pipeline, in the order that lets you verify each step before moving
to the next. It covers **eleven files**. Most of the machinery is already generic — the
fetcher is config-driven, the subagents share one formatting contract, the archive
builder takes a source list — so the work is small, but it is spread out, and nothing
fails loudly if you miss a step in the second half.

Grace's notebook is used as the worked example throughout. It is the most instructive of
the four: the only Jekyll site among three Quarto sites, and the only one that needs
per-file commit dates.

**Scope.** This is the procedure for a **GitHub-hosted** notebook (Quarto or Jekyll,
posts as `.qmd`/`.md` files in a repo). Adding a second **WordPress** site is a different
and shorter path — see [What this does not cover](#what-this-does-not-cover) at the end.

---

## 0. Collect these facts first

Everything below is mechanical once you have these seven answers. Get them by browsing
the repo and opening one published post side by side with its source file.

| What you need | How to find it | Grace's notebook |
|---|---|---|
| Repo slug | The GitHub URL | `grace-ac/grace-ac.github.io` |
| Post directory | Where post files actually live | `_posts/` |
| File layout | One file per post, or a folder per post with an `index.*` inside? | flat files |
| File extension | `.qmd` (Quarto) or `.md` (Jekyll/plain) | `.md` |
| Front-matter fields | Open a post's source; note which of `title`, `author`, `date`, `categories` are present | `title`, `date`, `categories` — **no `author`** |
| Published URL scheme | Open one post on the live site and compare its URL to its file path | `_posts/YYYY-MM-DD-slug.md` → `https://grace-ac.github.io/slug/` |
| Author name | The person the notebook belongs to (needed as a fallback when front matter has no `author`) | Grace Crandall |

You do **not** need the default branch. The fetcher reads post bodies at a commit SHA and
the archive builder resolves `default_branch` from the repo metadata, so `main` vs
`master` never comes up.

Pick a short lowercase **source key** (`grace`, `ariana`, `sams`, `tumbling-oysters`).
It is used as the `--notebook` value, the archive `source` column, the agent filename,
and the digest filename prefix — so choose it once and reuse it verbatim everywhere.

---

## Step 1 — Register the notebook in the fetcher

**File:** [`scripts/fetch_github_notebook.py`](../scripts/fetch_github_notebook.py) —
the `NOTEBOOKS` dict.

```python
NOTEBOOKS = {
    ...
    "<source-key>": {
        "repo": "<owner>/<repo>",
        "prefix": "<post-directory>/",   # matched with str.startswith on the full repo path
        "suffix": "<extension-or-/index.qmd>",  # matched with str.endswith
        # "file_dates": True,            # only if the agent compares dates — see below
    },
}
```

Two things to get right:

- **`suffix` is matched against the full path, not just the filename.** That is what lets
  `"/index.qmd"` pin a folder-per-post layout to the folder's index file (Sam's notebook),
  while a bare `".qmd"` accepts both flat and nested post files (Ariana's, tumbling-oysters).
  If posts are folder-per-post, use `/index.qmd` — otherwise every other `.qmd` in a post
  folder is treated as its own post.
- **`file_dates: True` costs one extra API call per post.** Set it only when the agent
  actually needs per-file commit history. Today that is only Grace's notebook, whose agent
  flags front-matter dates that disagree with when the file was committed. The flag can
  also be passed per-run as `--file-dates`.

You do **not** need to touch `argparse`: `--notebook` takes its choices from
`sorted(NOTEBOOKS)`, so the new key appears automatically.

### Verify

```bash
python3 scripts/fetch_github_notebook.py --notebook <source-key> --days 60
```

Expect JSON with `repo`, `week_start`, `today`, `commits_scanned`, `posts`, `warnings`.

- `commits_scanned: 0` → the repo genuinely had no commits in the window; widen `--days`.
- `commits_scanned` > 0 but `posts: []` → **`prefix` or `suffix` is wrong.** Compare them
  against real paths in the repo; this is the single most common mistake.
- A `403` mentioning the rate limit → set `GITHUB_TOKEN` (or `GH_TOKEN`) in the
  environment to raise the limit from 60 to 5,000 requests/hour.

---

## Step 2 — Teach the archive how to build the published URL

**File:** [`scripts/notebook_parsing.py`](../scripts/notebook_parsing.py) —
`derive_permalink()`.

This is the one step with **no generic fallback**. The function ends in
`raise ValueError(f"unknown notebook source: {source!r}")`, so if you skip it the archive
build fails loudly for the new source rather than quietly storing posts nobody can cite.
That is deliberate — `lab-archive` cites every claim with the `url` this function
produced, so a wrong URL is worse than no URL.

Add a branch before the `raise`, following whichever existing pattern matches the live
site:

| Layout | Rule | Example |
|---|---|---|
| Quarto, folder per post | strip the trailing `index.qmd`, keep the trailing slash (`_strip_index`) | `posts/84-trout-meth/index.qmd` → `…/posts/84-trout-meth/` |
| Quarto, flat file | swap the `.qmd` extension for `.html` | `posts/2026-07-06-seed-hardening.qmd` → `…/posts/2026-07-06-seed-hardening.html` |
| Jekyll | take the basename, drop the `.md`, strip the leading `YYYY-MM-DD-` (`_DATE_PREFIX`), add a trailing slash | `_posts/2026-07-15-enrichment-prelim.md` → `https://grace-ac.github.io/enrichment-prelim/` |

Note that `path` is `lstrip("/")`-ed at the top of the function, so a leading slash in the
input is already handled — don't re-handle it in your branch.

Then add a case to the permalink tests in
[`tests/test_notebook_parsing.py`](../tests/test_notebook_parsing.py) (the class that
already covers all four notebooks) and extend the docstring's list of schemes.

### Verify

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); import notebook_parsing as n; print(n.derive_permalink('<source-key>','<a-real-post-path>'))"
```

Paste the printed URL into a browser. It must load the actual post — not the site's home
page, not a 404. Then run the suite:

```bash
python3 -m unittest discover -s tests
```

---

## Step 3 — Add the source to the archive builder

**File:** [`scripts/build_archive.py`](../scripts/build_archive.py) — two constants.

1. **`GITHUB_SOURCES`** — add the key. The list is ordered *ascending by notebook size*
   on purpose: a build that stops on an exhausted rate limit has then made progress on the
   cheap notebooks first. Insert the new one by roughly how many posts it has, not at the
   end.
2. **`DEFAULT_AUTHORS`** — map the key to the author's display name. This is the fallback
   used when a post's front matter has no `author` (Grace's notebook omits it entirely, and
   a few posts elsewhere leave it blank). `lab-archive` groups results by `author`, so a
   missing entry means the new notebook's posts group under `None`.

`ALL_SOURCES` and the `--sources` choices derive from `GITHUB_SOURCES`, so there is
nothing else to edit.

### Verify

```bash
python3 scripts/build_archive.py --sources <source-key>
```

This needs the `gh` CLI authenticated — the archive builder gets its token from
`gh auth token` and exits with instructions if that fails. The run prints a per-source
`total / added / skipped` line. Then check what actually landed:

```bash
python3 -c "import sqlite3; c=sqlite3.connect('.cache/archive.db'); print(c.execute(\"SELECT COUNT(*), SUM(shadowed) FROM posts WHERE source='<source-key>'\").fetchone()); print(*c.execute(\"SELECT date, author, url FROM posts WHERE source='<source-key>' ORDER BY date DESC LIMIT 3\"), sep='\n')"
```

Sanity-check three things: the count is in the ballpark of the repo's post count, `author`
is populated, and the `shadowed` sum is 0 or small. A large `shadowed` count means many
posts collapse onto the same published URL — expected for a Jekyll site using
`permalink: /:title/` with repeated slugs across years, suspicious anywhere else (it
usually means the Step 2 branch drops something that distinguishes posts).

---

## Step 4 — Write the subagent

**New file:** `.claude/agents/<source-key>-notebook-agent.md`.
**Also edit:** [`.claude/shared/notebook-digest-format.md`](../.claude/shared/notebook-digest-format.md).

Copy the closest existing agent (`grace-notebook-agent.md` for Jekyll,
`ariana-notebook-agent.md` for flat Quarto, `sams-notebook-agent.md` for folder-per-post
Quarto) and replace only the notebook-specific half. The shared contract at
`.claude/shared/notebook-digest-format.md` owns the fetch/classify/format steps — the
agent must open by reading it, and must not restate or fork it. That deduplication is
the whole point (roadmap item 2); an agent that re-describes the output format will drift
from the other four.

The agent carries exactly these notebook-specific pieces, and nothing else:

1. **Fetch config** — the `python3 scripts/fetch_github_notebook.py --notebook <key>` line.
2. **Repo structure** — one or two sentences on the post layout, so the agent knows what a
   path means.
3. **Front-matter fields to extract** — and explicitly call out any *missing* field, e.g.
   "there is no `author` field — this is a single-author personal site."
4. **Per-post extras** — which optional JSON fields this notebook produces
   (`content_truncated` on the Quarto notebooks, `commit_dates` when `file_dates` is set)
   and what to do with them.
5. **Published permalink convention** — how to build the URL for the **URL** block line.
6. **No-activity message** — the exact sentence to return when `posts` is empty.
7. **Header** — the `#` title and the `>` source attribution line.
8. **Block fields** — which of the contract's block lines to include, which to omit
   (no **Author** line for a single-author site), and any extra line this notebook adds
   (Grace's date-mismatch warning).

Two things not to add unless they apply: the contract already says to return the summary
rather than write a file, so only add a file-write clause if this notebook needs one
(tumbling-oysters has the inverse — an explicit note to *skip* its file write when
`full-lab-digest` invokes it). And the front-matter `date`-vs-`commit_dates` mismatch
check only makes sense with `file_dates` enabled.

Finally, add the new agent to the roster sentence at the top of
`notebook-digest-format.md`, which names the GitHub agents the contract governs.

### Verify

Ask Claude a question the agent's `description` should catch — "what's new in
`<researcher>`'s notebook this week" — and confirm it launches *that* agent and returns a
summary in the contract's shape (a `#` header, one `###` block per post, `---` between
blocks). If it launches the wrong agent or none, the `description` field needs the
researcher's name and the repo slug in it, phrased like the existing four.

---

## Step 5 — Wire it into the skills and the docs

Nothing here fails loudly; it just leaves instructions that quietly contradict reality.

| File | What to change |
|---|---|
| [`full-lab-digest/SKILL.md`](../.claude/skills/full-lab-digest/SKILL.md) | Add the agent to the step-2 launch list; add a `## <Source label>` section (with its paste placeholder) to the step-6 template; add the source to the step-9 Data & Figures group order; update every hardcoded count (see below) |
| [`lab-archive/SKILL.md`](../.claude/skills/lab-archive/SKILL.md) | Add the key to the `source` column's list of allowed values, and to the source-label map at the bottom |
| [`digest-index/SKILL.md`](../.claude/skills/digest-index/SKILL.md) | Add the `<source-key>-` filename-prefix → type rule, and the short label used in the "sources with activity" column |
| [`README.md`](../README.md) | Add a row to the Data Sources table; update the `--notebook` choices in the `fetch_github_notebook.py` example and its Options line; update the Repository Structure comments ("one subagent per notebook source", "shared by the four GitHub agents") |
| `.claude/settings.local.json` | Add `Bash(python3 scripts/fetch_github_notebook.py --notebook <key>)` (and the `--days N` variants you expect) so unattended runs don't stop on a permission prompt |

**The hardcoded counts.** The number *five* is written into prose in about a dozen places —
"all five subagents", "wait for **all five**", "the five compiled summaries", "`[N] of 5
sources had activity`", "every post the five notebooks have ever published". A skill told
to wait for five returns while six subagents are running is a real bug, not a cosmetic
one. Find them all with:

```bash
grep -rn "five\|all four\|four GitHub\| of 5 " .claude README.md
```

Roadmap item 13 recommends replacing these with count-free phrasing ("all notebook
subagents", "every source listed in step 2") so the next addition is a shorter diff. If
you are already in here, that is the better fix.

---

## Step 6 — Run it end to end

```bash
python3 -m unittest discover -s tests
```

Then ask Claude for a full lab digest and check three things in the output: the new
`## <Source label>` section is present, its content came from the new agent (not a
placeholder), and the `> [N] of [total] sources had activity` line counts the new source.

---

## Checklist

- [ ] `NOTEBOOKS` entry in `scripts/fetch_github_notebook.py`
- [ ] `derive_permalink()` branch in `scripts/notebook_parsing.py`
- [ ] permalink test case in `tests/test_notebook_parsing.py`
- [ ] `GITHUB_SOURCES` + `DEFAULT_AUTHORS` in `scripts/build_archive.py`
- [ ] `.claude/agents/<source-key>-notebook-agent.md`
- [ ] agent roster line in `.claude/shared/notebook-digest-format.md`
- [ ] `full-lab-digest/SKILL.md` — agent list, digest template section, Data & Figures order, counts
- [ ] `lab-archive/SKILL.md` — source list, source-label map
- [ ] `digest-index/SKILL.md` — filename prefix, short label
- [ ] `README.md` — Data Sources table, script options, structure comments
- [ ] `.claude/settings.local.json` — fetch permission entry
- [ ] tests pass; a full digest run shows the new section

---

## Gotchas

- **The published-URL line in a digest and `derive_permalink` are independent.** Ariana's
  agent omits the **URL** block line ("this notebook has no published-URL convention")
  while `derive_permalink` still produces an `ahuffmyer.github.io/…html` URL for the
  archive. If the live site's URLs are unstable, it is fine to omit the digest's URL line
  and still archive a derived URL — but do not skip Step 2 on those grounds, or the
  archive build will raise.
- **Two different GitHub credentials.** The windowed fetcher reads `GITHUB_TOKEN` /
  `GH_TOKEN` from the environment and works unauthenticated at 60 requests/hour. The
  archive builder shells out to `gh auth token` and requires it. Subagents must not call
  `gh` or the API directly — the shared contract says so explicitly, and `gh` is not
  available in that environment.
- **Deleted and renamed posts.** A post deleted inside the window is skipped with a
  warning rather than summarized; a rename carries `previous_filename`. In the archive,
  row identity is `(source, path)`, so a renamed post adds a row rather than replacing
  one — the old row lingers until someone prunes it.
- **Cosmetic-edit classification is global, not per notebook.** A modified post whose diff
  is ≤6 lines is reported as `cosmetic` with its patch and a hard-trimmed body. If the new
  notebook's posts are routinely edited in small real increments, `--cosmetic-lines` is
  the knob; don't special-case it in the agent.

## What this does not cover

- **A second WordPress site.** That path has no `NOTEBOOKS` entry and no
  `derive_permalink` branch — WordPress posts carry their own canonical URL. It touches
  `scripts/fetch_lab_posts.py` (`DEFAULT_SITE`), `process_wordpress_source` in the archive
  builder, and a new agent modeled on `wordpress-agent`.
- **`daily-literature-post` and `weekly-lab-digest`.** Both read only
  `fetch_lab_posts.py` (WordPress), so adding a GitHub notebook needs no change to either.
