# WordPress Publisher Skill

Trigger this skill when the user asks to **publish the weekly digest to WordPress**, **post the digest to WordPress**, **create a WordPress draft**, or any similar phrasing that involves sending a lab digest to genefish.wordpress.com.

## What this skill does

Reads the most recently generated full lab digest (or a user-specified digest file), converts it from Markdown to HTML, reads a WordPress API token from a config file, and POSTs the content to the WordPress.com REST API as a **draft** (not published) so the user can review before it goes live.

## Steps

### 1. Identify the digest file

If the user specified a file path or date, use that. Otherwise, find the most recently modified full lab digest:

```bash
ls -t ~/LabNotebook-Summarizer/digests/full-lab-digest-*.md | head -1
```

Print the resolved file path to the user so they can confirm it is the right one.

### 2. Read the WordPress API token

```bash
cat ~/.config/LabNotebook-Summarizer/wp_token
```

**If this command fails** (file does not exist, permission denied, or returns empty output):
- Stop immediately.
- Report to the user: `WordPress token not found. Please create the file ~/.config/LabNotebook-Summarizer/wp_token containing your WordPress.com API access token. You can generate one at https://developer.wordpress.com/apps/`
- Do **not** proceed to any further steps.

Store the token in a shell variable; **never** print it to the conversation or write it to any file.

### 3. Extract the post title

The first line of the digest file will be a Markdown `#` heading such as:
`# Full Lab Digest — 2026-07-14 to 2026-07-20`

Strip the leading `# ` to get the post title. Example result: `Full Lab Digest — 2026-07-14 to 2026-07-20`

```bash
head -1 PATH_TO_DIGEST | sed 's/^# //'
```

### 4. Convert Markdown to HTML

Use Python's `markdown` library if available, otherwise fall back to `pandoc`:

```bash
# Try Python markdown first
python3 -c "
import sys, markdown
content = open('PATH_TO_DIGEST').read()
print(markdown.markdown(content, extensions=['tables', 'fenced_code', 'nl2br']))
" 2>/dev/null
```

If that fails (Python markdown not installed), fall back to:

```bash
pandoc -f markdown -t html PATH_TO_DIGEST
```

If neither is available, report: `Could not convert Markdown to HTML — please install python3-markdown (pip install markdown) or pandoc.` and stop.

Store the HTML output in a temporary file in the scratchpad directory (never in the project directory or `/tmp`).

### 5. POST to the WordPress API

Run the following curl command. Substitute:
- `TOKEN` with the value read in Step 2 (passed as a shell variable, not printed)
- `TITLE` with the title from Step 3
- `HTML_FILE` with the path to the temporary HTML file from Step 4

```bash
WP_TOKEN=$(cat ~/.config/LabNotebook-Summarizer/wp_token)
TITLE="[title from step 3]"
HTML_CONTENT=$(cat [html_file_from_step_4])

curl -s -w "\n%{http_code}" \
  -X POST \
  -H "Authorization: Bearer ${WP_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "$(python3 -c "
import json, sys
title = sys.argv[1]
content = open(sys.argv[2]).read()
print(json.dumps({'title': title, 'content': content, 'status': 'draft'}))
" "${TITLE}" "[html_file_from_step_4]")" \
  "https://public-api.wordpress.com/rest/v1.1/sites/genefish.wordpress.com/posts/new/"
```

**Important implementation note:** Build the JSON body using Python's `json.dumps` (as shown above) rather than shell string interpolation — the HTML content contains characters that would break a shell-quoted JSON string.

Capture both the response body and the HTTP status code (the `-w "\n%{http_code}"` flag appends the status on a final line).

### 6. Handle the API response

Split the curl output: the last line is the HTTP status code; everything before it is the JSON response body.

**HTTP 200 or 201 — success:**
- Parse the JSON response and extract the `URL` field (the draft's edit/preview URL).
- Report to the user:
  ```
  Draft created successfully.
  Title: [title]
  WordPress draft URL: [URL from response]
  Status: draft (not yet published — review at the URL above before publishing)
  ```

**HTTP 400 — bad request:**
- Print the response body for the user to inspect.
- Report: `WordPress API returned 400 Bad Request. The response body above may explain why.`

**HTTP 401 or 403 — authentication error:**
- Do **not** print the token or hint at its value.
- Report: `WordPress API returned [status code] — authentication failed. Check that the token in ~/.config/LabNotebook-Summarizer/wp_token is valid and has permission to post to genefish.wordpress.com. You may need to regenerate the token at https://developer.wordpress.com/apps/`

**HTTP 404:**
- Report: `WordPress API returned 404 — the site genefish.wordpress.com was not found or is not accessible with this token.`

**Any other non-2xx status:**
- Print the status code and response body.
- Report: `WordPress API returned an unexpected status [code]. See the response above.`

**curl itself fails (exit code non-zero, no HTTP status captured):**
- Report: `curl failed to reach the WordPress API. Check your internet connection and try again.`

### 7. Clean up

Delete the temporary HTML file created in Step 4 from the scratchpad directory.

## Security rules (always enforced)

- The token is read from `~/.config/LabNotebook-Summarizer/wp_token` every time — it is **never** stored in memory between sessions, hardcoded in any file, or echoed to the conversation.
- The status is always set to `draft` — this skill never publishes directly.
- If authentication fails at any point, stop and report clearly rather than retrying or falling back.
