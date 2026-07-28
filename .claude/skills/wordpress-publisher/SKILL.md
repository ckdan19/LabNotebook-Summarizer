# WordPress Publisher Skill

Trigger this skill when the user asks to **publish the weekly digest to WordPress**, **post the digest to WordPress**, **create a WordPress draft**, or any similar phrasing that involves sending a lab digest to genefish.wordpress.com.

## What this skill does

Reads the most recently generated full lab digest (or a user-specified digest file) and hands it to `scripts/publish_digest.py`, which converts the Markdown to sanitized HTML and POSTs it to the WordPress.com REST API as a **draft** (never published) so the user can review before it goes live.

All the credential handling, HTML escaping, and JSON encoding happen inside that script. **Do not reimplement any of it in shell.** Digest text is derived from third-party notebook posts, so pasting it into a shell command is a command-injection path: a post title containing `$(...)` or a backtick would execute. The script takes a file path and never lets content reach a shell.

Paths below are relative to the repository root, which is the working directory Claude Code starts in.

## Steps

### 1. Identify the digest file

If the user specified a file path or date, use that. Otherwise, find the most recently modified full lab digest:

```bash
ls -t digests/full-lab-digest-*.md | head -1
```

Print the resolved file path to the user so they can confirm it is the right one.

Full-digest filenames end in the window length (`full-lab-digest-2026-07-27-14d.md`), so a date alone can match more than one file — say, a 7-day and a 14-day digest ending on the same day. If the user gave only a date and it matches several, list the matches and ask which to publish.

### 2. Preview the converted post

Run the publisher in dry-run mode. This reads and converts the digest but does **not** read the token or contact the API:

```bash
python3 scripts/publish_digest.py digests/full-lab-digest-2026-07-21.md --dry-run
```

The output is JSON with `title`, `converter`, `tags_removed_approx` (an approximate count of HTML tags the sanitizer stripped), `content_bytes`, and `content_preview`.

Show the user the **title** and the **first few lines of `content_preview`**. If `tags_removed_approx` is greater than 0, mention it — the digest contained raw HTML that was stripped, which is expected for sanitization but worth noting.

If the output contains an `error` key, report it and stop. Common cases:
- The digest does not begin with a `# ` heading — the script cannot derive a post title. Ask the user for a title or fix the digest.
- Neither `python-markdown` nor `pandoc` is installed. Report the message verbatim; the fix is `pip install markdown`.

### 3. Ask the user to confirm

Publishing sends lab content to an externally hosted site. **Wait for the user to explicitly confirm** before running step 4, even though the post is created as a draft. Do not skip this because the user asked for "publish" earlier in the conversation — confirm the specific resolved file and title.

### 4. Create the draft

```bash
python3 scripts/publish_digest.py digests/full-lab-digest-2026-07-21.md
```

The script reads the token from `~/.config/LabNotebook-Summarizer/wp_token` itself, sends it only as a request header, and redacts it from anything it prints. It always sets `status: draft`.

**Never** `cat` the token file, echo it, pass it as a command-line argument, or interpolate it into a `curl` command. `cat`-ing it would copy the credential into the conversation transcript, and passing it in argv would expose it to any local process via `ps`. If you need to check whether the token exists without reading it:

```bash
[ -s ~/.config/LabNotebook-Summarizer/wp_token ] && echo present || echo missing
```

### 5. Report the result

On success the script prints JSON with `status: "draft created"`, `url`, `post_id`, and `http_status`. Report to the user:

```
Draft created successfully.
Title: [title]
WordPress draft URL: [url]
Status: draft (not yet published — review at the URL above before publishing)
```

If `warnings` is non-empty, relay each warning. The most common one is that the token file is readable by other users, with the `chmod 600` command to fix it.

On failure the script exits non-zero and prints an `error` field explaining the HTTP status: authentication failure (401/403), site not found (404), an unexpected status with the response body, or a network failure. **Report the `error` message as-is and stop.** Do not retry, do not fall back to `curl`, and do not attempt a different site or token path.

If the token file is missing or empty, the error explains how to create it; relay that and stop:

> `WordPress token not found. Create ~/.config/LabNotebook-Summarizer/wp_token containing your WordPress.com API access token (generate one at https://developer.wordpress.com/apps/).`

## Security rules (always enforced)

- The token is read from `~/.config/LabNotebook-Summarizer/wp_token` by the script on each run — never printed to the conversation, never written to another file, never placed in a command line, and never stored between sessions.
- Digest content never passes through a shell. Only the file *path* is ever a command-line argument.
- The digest body is sanitized against a tag allowlist before it is sent: `<script>`, `<style>`, `<iframe>`, inline event handlers such as `onerror`, and `javascript:` URLs are removed. Lab digests summarize third-party posts, so treat their content as untrusted when it is about to reach a public site.
- The status is always `draft` — this skill never publishes directly.
- If authentication fails at any point, stop and report rather than retrying or falling back.
