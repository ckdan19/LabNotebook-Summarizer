# GitHub Notebook Digest — Shared Output Contract

This file is the single source of truth for how the five GitHub notebook subagents
(`ariana-notebook-agent`, `sams-notebook-agent`, `grace-notebook-agent`,
`tumbling-oysters-agent`, `megan-notebook-agent`) fetch, classify, and format post
activity. Each agent
`Read`s this file first, then applies the notebook-specific details from its own
definition (repo, `--notebook` value, URL convention, front-matter fields,
no-activity message, header, and which block fields to include). The output shape
below is exactly what the `full-lab-digest` skill expects to paste in verbatim.

Follow these steps exactly and return **only** the structured summary — do not dump
raw fetched content into the conversation.

## Step 1 — Fetch the changed posts

Run the helper script from the repository root (the working directory Claude Code
starts in), substituting this notebook's config name:

```bash
python3 scripts/fetch_github_notebook.py --notebook <notebook-name>
```

This makes two GitHub API calls to find every post changed in the last 7 days, then
fetches those post bodies — do **not** call the GitHub API yourself, and do not use
`gh` (it is not installed on this machine). Pass `--days N` if a window other than 7
days is requested.

The script prints JSON with `repo`, `week_start`, `today`, `commits_scanned`,
`posts`, and `warnings`. Each entry in `posts` has:

- `path` — the post's path in the repo
- `content` — the post source, read at the commit that changed it
- `change_class` — `substantive` (new post or a real edit) or `cosmetic` (a modified
  post whose diff is ≤6 lines: a link fix, typo, or formatting change)
- `patch` — the diff, present only on `cosmetic` posts
- `status`, `additions`, `deletions`, `blob_url`

Some notebooks add extra per-post fields — see your agent file (e.g.
`content_truncated` on the Quarto notebooks, `commit_dates` on Grace's).
`commits_scanned` is useful context when reporting no activity: it distinguishes a
repo that was quiet entirely from one that merely had no post changes.

## Step 2 — Handle empty results, errors, and warnings

- If `posts` is empty, return the notebook's **no-activity message** (given in your
  agent file) and nothing else.
- If the JSON contains an `error` key, the script exited non-zero — return that error
  message rather than a summary, and do not fall back to calling the API by hand. A
  rate-limit error means `GITHUB_TOKEN` should be set in the environment.
- If `warnings` is non-empty, append each one as a bullet under a `**Warnings**` line
  at the end of your summary.

## Step 3 — Summarize each post

For posts with `change_class: substantive`, parse `content` and extract:

- **Front matter** (between the opening `---` and closing `---`): the fields listed
  in your agent file.
- **Key finding**: 2–3 sentences capturing the main question, method, and result or
  conclusion. Focus on results/conclusion sections, or the final paragraphs if none
  exist. Do not quote verbatim — paraphrase. If the post is logistical (meeting
  notes, sample prep, equipment setup, software install, data received), summarize
  what was done and any decisions or outcomes noted.
- **Figure links**: scan `content` for both syntaxes and capture each URL:
  - Markdown: `![alt](url)`
  - HTML: `<img src="url"`

  Classify each as `local` (relative path, no `http`) or `external` (starts with
  `http`).

For posts with `change_class: cosmetic`, the post is not new work — it was only
lightly edited this week. Still report its front-matter fields, but replace the
**Key finding** line with a **Change this week** line describing what the `patch`
actually did (e.g. "corrected a broken repo link, no new science content"). Do not
present a cosmetically edited post as this week's science, and do not list its
figures.

## Step 4 — Return the structured summary

Use the header from your agent file, then one block per post, separated by `---`, in
this format:

```
### [title]
- **Date**: [date]
- **URL**: [published URL]
- **Author**: [author]
- **Categories**: [comma-separated categories]
- **Key finding**: [2-3 sentence synthesis]      ← or **Change this week** for cosmetic edits
- **Figures**:
  - local: [relative path] (if any)
  - external: [full URL] (if any)
```

Include exactly the block fields your agent file specifies — omit any line that
doesn't apply to this notebook (e.g. no `Author` for a single-author site, no `URL`
for a notebook without a published-permalink convention), and add any notebook-
specific lines it calls for. Group posts chronologically by date (oldest first).

Unless your agent file says otherwise, return the summary directly to the main
conversation — do not write a file.
