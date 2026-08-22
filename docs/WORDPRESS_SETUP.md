# Getting a WordPress.com Access Token

The publishing tools in this repo — the **`wordpress-publisher`**, **`full-lab-digest`**,
**`daily-literature-post`**, and **`digest-audio-publish`** skills — all authenticate to
WordPress.com with a single OAuth2 access token stored at:

```
~/.config/LabNotebook-Summarizer/wp_token
```

The scripts (`scripts/publish_digest.py`, `scripts/upload_media.py`) read this file
themselves, send the token only as an `Authorization: Bearer` request header, and redact it
from anything they print. You never need to paste the token into a command or into the
conversation. This guide walks through obtaining that token.

You only need to do this **once**. The token is long-lived; redo these steps only if you
revoke it or it stops working.

> **Draft-only by default.** Having a token stored here enables **draft** publishing.
> Live (immediately visible) publishing is a separate, deliberate authorization — see the
> note at the end of this document and `AUTHORIZATION.md`.

---

## 1. Register an application

1. Go to **https://developer.wordpress.com/apps/** and sign in with the WordPress.com
   account that owns the notebook site (`genefish.wordpress.com`).
2. Click **Create New Application** and fill in the form:
   - **Name / Description:** anything recognizable, e.g. `LabNotebook-Summarizer`.
   - **Website URL:** any URL you control (e.g. the notebook site) — not important for
     this flow.
   - **Redirect URLs:** set a value you can read a `code` back from. A simple choice is
     `http://localhost` (you will copy the `code` out of the redirected URL by hand). It
     must match **exactly** what you use in the authorize URL later.
   - **Type:** choose **Web** — **not** *Native*.

   > ⚠️ **The type must be "Web."** Applications registered as **Native** are *not* issued a
   > **client secret**, and the token-exchange step below requires the client secret. If you
   > pick Native you will be stuck with no way to complete the OAuth2 flow. If you already
   > created a Native app, create a new Web one (or edit the type if the dashboard allows it).

3. Save. The application page now shows three values you need:
   - **Client ID** (a number)
   - **Client Secret** (a long string) — treat this like a password
   - **Redirect URL** (what you entered above)

---

## 2. Authorize (get a `code`)

Build the authorize URL, substituting your **Client ID** and the exact **Redirect URL** you
registered:

```
https://public-api.wordpress.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&response_type=code&scope=global
```

Open that URL in a browser. WordPress.com will ask you to approve the application, then
redirect to your redirect URL with a `?code=...` query parameter appended, e.g.:

```
http://localhost/?code=abcd1234efgh5678...
```

Copy the value of the `code` parameter (everything after `code=`, up to any `&`).

> ⏱ **The `code` is short-lived — it expires within a couple of minutes.** Have the
> exchange command in step 3 ready to paste *before* you generate the code, and run it
> immediately. If you get an `invalid_grant` / expired-code error, just repeat step 2 to
> mint a fresh code and try again.

---

## 3. Exchange the `code` for an access token

Immediately run the following, substituting your Client ID, Client Secret, Redirect URL,
and the `code` you just copied. This is the one place the client secret and code appear on a
command line — run it **only in your local terminal** (see the security note below):

```bash
curl -sS https://public-api.wordpress.com/oauth2/token \
  -d client_id=YOUR_CLIENT_ID \
  -d client_secret=YOUR_CLIENT_SECRET \
  -d redirect_uri=YOUR_REDIRECT_URI \
  -d grant_type=authorization_code \
  -d code=YOUR_CODE
```

On success this returns JSON like:

```json
{"access_token":"XXXXXXXXXXXXXXXX","token_type":"bearer","blog_id":"...","blog_url":"https://genefish.wordpress.com","scope":"global"}
```

The value of `access_token` is your token. Copy it (without the surrounding quotes).

> If you get `{"error":"invalid_grant", ...}` the code expired or was already used — return
> to step 2 for a fresh one. If you get an error about the client secret being missing, your
> app is registered as **Native** — recreate it as **Web** (step 1).

---

## 4. Store the token

Create the config directory and write the token using a **heredoc**, not `echo`:

```bash
mkdir -p ~/.config/LabNotebook-Summarizer
cat > ~/.config/LabNotebook-Summarizer/wp_token <<'EOF'
PASTE_YOUR_ACCESS_TOKEN_HERE
EOF
chmod 600 ~/.config/LabNotebook-Summarizer/wp_token
```

> **Why a heredoc and not `echo`?** Access tokens can contain shell-special characters such
> as `&`, `#`, `!`, `$`, and quotes. With `echo "$TOKEN"` the shell may interpret those
> (history expansion on `!`, variable expansion on `$`, command chaining on `&`), silently
> corrupting or truncating the stored token. A **quoted** heredoc (`<<'EOF'`, note the single
> quotes) writes the text through verbatim with no expansion. Paste the token on its own line
> between the two `EOF` markers.

`chmod 600` restricts the file to your user; the publishing scripts warn if the token is
readable by others.

### Verify it saved

Check the file exists and is non-empty **without printing its contents** (printing it would
copy the credential into your terminal scrollback / the conversation transcript):

```bash
[ -s ~/.config/LabNotebook-Summarizer/wp_token ] && echo present || echo missing
```

You can also confirm the length looks right without revealing the token:

```bash
wc -c < ~/.config/LabNotebook-Summarizer/wp_token
```

Do **not** `cat` the file to eyeball it.

---

## 5. Test before publishing for real

First run a **`--dry-run`**, which converts and sanitizes the digest *without reading the
token or contacting the API* — it verifies your Markdown and the tooling before any network
call:

```bash
python3 scripts/publish_digest.py path/to/some-digest.md --dry-run
```

If that succeeds, do a real **draft** publish (the default `--status` is `draft`):

```bash
python3 scripts/publish_digest.py path/to/some-digest.md
```

On success the script prints JSON with `status: "draft created"` and a `url`. Open that URL
in the WordPress.com dashboard to confirm the draft is there and looks right. Nothing is
public until you (or an authorized live-publish path) deliberately publish it.

If you get a 401/403 authentication error, the token is wrong, expired, or was corrupted on
save — redo steps 2–4 (and double-check you used a quoted heredoc).

---

## Security notes

- **Never paste the client secret, the access token, or the OAuth `code` anywhere except
  your own local terminal.** Do not paste them into the chat, a commit, a shared doc, a
  chat/DM, an issue, or a URL you send to anyone. The `wp_token` file lives outside the
  repository and must never be committed.
- The scripts are designed so the token stays local: they read `wp_token` directly and send
  it only as a request header. You should never need to `cat`, `echo`, or interpolate the
  token into a `curl` command yourself.
- **If a secret or token is ever exposed** (pasted somewhere it shouldn't be, committed,
  logged, shared), revoke it promptly: go to **WordPress.com → Account → Security →
  Connected Applications**, find this application, and **Disconnect / Remove** it. That
  invalidates the token immediately. Then repeat this guide to issue a fresh one, and update
  `~/.config/LabNotebook-Summarizer/wp_token`. If the **client secret** leaked, also reset
  it (or delete and recreate the app) at https://developer.wordpress.com/apps/.

---

## Draft vs. live publishing

Storing a token here only enables **draft** publishing — every tool that uses it creates
unpublished drafts by default (`scripts/publish_digest.py` defaults to `--status draft`).

**Live (immediately visible) publishing is a separate, deliberate authorization** and is
*not* granted just by having a token. It is controlled by **`AUTHORIZATION.md`** in the repo
root, which is the single durable switch that lets the `daily-literature-post` skill publish
its daily post live. Any other live publishing is a manual, confirmed action. See
`AUTHORIZATION.md` for the exact marker and how to pause it.
