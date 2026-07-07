# Weekly Lab Digest Skill

Trigger this skill when the user asks for a **weekly summary**, **weekly digest**, or **weekly lab notebook summary** of the genefish lab notebook.

## What this skill does

Fetches posts from the [genefish WordPress lab notebook](https://genefish.wordpress.com) published in the last 7 days and produces a structured digest, grouped by author.

## Steps

1. **Fetch recent posts** by running the helper script:

   ```bash
   python3 ~/LabNotebook-Summarizer/scripts/fetch_lab_posts.py
   ```

   The script queries `https://public-api.wordpress.com/rest/v1.1/sites/genefish.wordpress.com/posts/?number=20`, filters to posts from the last 7 days, strips HTML, and outputs JSON with fields: `author`, `date`, `title`, `url`, `content`.

2. **If no posts are returned**, report: "No new posts in the genefish lab notebook in the last 7 days."

3. **For each post**, write a 2-3 sentence summary covering:
   - Who posted and when
   - The key activity, experiment, measurement, or finding
   - Any notable result, anomaly, or next step mentioned

4. **Group by author** when more than one author is present. Use a `## Author Name` heading per author, with their posts listed beneath in chronological order.

5. **Output format**:

```
# Weekly Lab Digest — [week_start] to [today]

## [Author Name]

**[Post Title]** · [YYYY-MM-DD] · [URL]
[2-3 sentence summary]

## [Author Name 2]

**[Post Title]** · [YYYY-MM-DD] · [URL]
[2-3 sentence summary]
```

If all posts are from a single author, omit the author grouping headers and just list posts chronologically.
