# Digest Audio Publish Skill

Trigger this skill when the user asks to **publish audio for the latest digest**,
**post the audio version of the full lab digest**, **narrate and publish the latest
digest's audio**, or any similar phrasing that means: generate the spoken narrations
for the most recent full lab digest and publish them to WordPress as their **own**
post.

This skill is **standalone** and separate from `full-lab-digest`, `digest-audio`, and
`wordpress-publisher`. It orchestrates the audio + upload + publish flow end to end.
It does **not** generate a new digest and it does **not** edit the existing digest
post — it creates a **new, separate** WordPress post that links to the audio and back
to the original digest.

Paths below are relative to the repository root, which is the working directory Claude
Code starts in.

## Prerequisites (verify before running)

- **`.venv-tts`** exists and has a TTS engine installed (Kokoro by default). Narration
  runs with `.venv-tts/bin/python`, **not** the system `python3` — the engines and
  their heavy dependencies (Torch, model weights) live only in that isolated
  environment. If `.venv-tts/bin/python` is missing, stop and point the user at the
  setup section of `text_to_speech/README.md`; do not install anything automatically.
- **`scripts/upload_media.py`** exists (uploads a local file to the WordPress media
  library and returns its public URL). If it is missing, stop and report that — this
  skill cannot upload audio without it.
- **WordPress token** at `~/.config/LabNotebook-Summarizer/wp_token`. The upload and
  publish scripts read it themselves; never read, echo, or pass it on a command line.
- **The original digest post's WordPress URL.** The new audio post links back to it.
  If the user has not provided it and it cannot be found, ask for it before publishing.

## Steps

### 1. Find the most recently published full lab digest

```bash
ls -t digests/full-lab-digest-*.md | head -1
```

Print the resolved path to the user and confirm it is the intended digest. Read its
first line (the `# ` heading) to get the human date range, e.g.:

```
# Full Lab Digest — 2026-08-11 to 2026-08-17 (7 days)
```

Extract the **date range** (`2026-08-11 to 2026-08-17`) — it is used in the audio
post's title. The digest filename encodes the end date and window
(`full-lab-digest-2026-08-17-7d.md`); a date alone can match a 7-day and a 14-day
digest, so if the user names only a date and it is ambiguous, list the matches and ask.

### 2. Generate both WAV narrations (conversational)

Both narrations use the **conversational** style. They differ only in scope:

- **Summaries edition** — notebook post summaries only (default scope).
- **Full / analysis edition** — the entire digest including the cross-notebook and
  literature sections (`--include-analysis`).

Both editions use the same style, so their **default** output filenames would collide
(the default name is derived from digest stem + provider + style only, *not* from
`--include-analysis`). You **must** pass an explicit, distinct `--output` for each.

First preview each with `--dry-run` (no model load) to confirm the narration reads post
titles and key findings and skips URLs, figure paths, and generated-at metadata:

```bash
.venv-tts/bin/python -m text_to_speech DIGEST.md --style conversational --dry-run
.venv-tts/bin/python -m text_to_speech DIGEST.md --style conversational --include-analysis --dry-run
```

Then generate the WAVs (use the default `kokoro` provider unless the user asked for
Chatterbox-Nano). Write both into `text_to_speech/output/` (gitignored):

```bash
.venv-tts/bin/python -m text_to_speech DIGEST.md \
  --style conversational \
  --output text_to_speech/output/STEM-summaries.wav

.venv-tts/bin/python -m text_to_speech DIGEST.md \
  --style conversational --include-analysis \
  --output text_to_speech/output/STEM-analysis.wav
```

Replace `STEM` with the digest filename stem (e.g. `full-lab-digest-2026-08-17-7d`).
Each command prints a single JSON object on stdout; a `"status": "audio generated"`
object means the WAV was written. A `{"error": ...}` object with a non-zero exit means
it failed — **stop, keep any files already written, and report** (see step 6). A full
digest takes several minutes per edition; that is expected.

### 3. Upload both WAVs to the WordPress media library

Upload each file with `scripts/upload_media.py`. This uses the system `python3`
(standard library only — no TTS deps needed). Only the **file path** is ever a
command-line argument; the file is binary, so no digest text passes through a shell.

```bash
python3 scripts/upload_media.py text_to_speech/output/STEM-summaries.wav
python3 scripts/upload_media.py text_to_speech/output/STEM-analysis.wav
```

Each call prints JSON including the uploaded media's public `url`. Capture both URLs —
the summaries-edition URL and the analysis-edition URL. If either upload fails (non-zero
exit / `error` field), **stop, keep all local WAVs, and report** (step 6). Do not delete
anything and do not publish a post that links to an upload that did not succeed.

> **Token handling:** `upload_media.py` reads the token from
> `~/.config/LabNotebook-Summarizer/wp_token` itself and sends it only as a request
> header. Never `cat`, echo, or pass the token on a command line. To check only that it
> exists: `[ -s ~/.config/LabNotebook-Summarizer/wp_token ] && echo present || echo missing`.

### 4. Publish a new, separate audio post

Build a small Markdown file for the **new** post (write it to the scratchpad directory,
not into `digests/`). Its first line must be the `# ` heading — `publish_digest.py`
turns that into the post title and drops it from the body. Use a title like:

```
# 🎧 Audio: Full Lab Digest — 2026-08-11 to 2026-08-17
```

First, get each edition's approximate duration (in minutes) from its WAV — the block
quotes a running time per edition. The narrations are mono WAVs, so the stdlib `wave`
module is enough:

```bash
python3 -c "import wave,sys; w=wave.open(sys.argv[1],'rb'); print(round(w.getnframes()/w.getframerate()/60,1))" text_to_speech/output/STEM-summaries.wav
python3 -c "import wave,sys; w=wave.open(sys.argv[1],'rb'); print(round(w.getnframes()/w.getframerate()/60,1))" text_to_speech/output/STEM-analysis.wav
```

Do this **before** the WAVs are deleted in step 5.

Body content — this is the exact "Listen to this digest" block from the live 2026-08-17
digest post (post ID 9480 on genefish.wordpress.com), reproduced in Markdown that
`publish_digest.py` renders to the same HTML. The block uses **bare angle-bracket
autolinks** (`<url>`) so the link text is the URL itself, and each edition carries an
approximate running time. Fill in the two captured media URLs, the two durations, and
the original digest post URL — do not restyle the wording:

```markdown
# 🎧 Audio: Full Lab Digest — 2026-08-11 to 2026-08-17

Audio narrations of the [full lab digest for 2026-08-11 to 2026-08-17](ORIGINAL_DIGEST_POST_URL).

## 🎧 Listen to this digest

Audio narration generated with the Kokoro text-to-speech engine (conversational style).

- **Summaries edition (~SUMMARIES_MIN min)** — the per-source notebook updates: <SUMMARIES_URL>
- **Full edition (~ANALYSIS_MIN min)** — summaries plus the cross-notebook patterns, historical connections, and literature connections: <ANALYSIS_URL>

Read the full written digest here: [Full Lab Digest — 2026-08-11 to 2026-08-17](ORIGINAL_DIGEST_POST_URL).
```

The `# ` first line is the post title (`publish_digest.py` strips it from the body); the
`## 🎧 Listen to this digest` heading, the intro sentence, and the two bullet lines are
verbatim from post 9480. If the user narrated with a provider other than Kokoro, change
the engine name in the intro sentence to match; otherwise leave the wording as-is.

Preview the conversion first (does not read the token or contact the API):

```bash
python3 scripts/publish_digest.py SCRATCH/audio-post.md --dry-run
```

Show the user the resolved **title** and the first lines of `content_preview`, and
confirm the two audio links resolved. Then publish it as a **new live post**
(`--status publish` is an explicit override; `publish_digest.py` defaults to `draft`):

```bash
python3 scripts/publish_digest.py SCRATCH/audio-post.md --status publish
```

`publish_digest.py` always POSTs to `posts/new/`, so this is always a brand-new post,
never an edit of the existing digest post. On success it prints `status`
(`published live`), `url`, and `post_id` — report all three. On any HTTP/auth/network
error it exits non-zero with an `error` field: **report it verbatim and stop.** Do not
retry, fall back to `curl`, or try another token path.

### 5. Delete the local WAVs after a successful upload

Once **both** uploads in step 3 succeeded (and, ideally, the post in step 4 published),
delete the two local WAV files:

```bash
rm text_to_speech/output/STEM-summaries.wav text_to_speech/output/STEM-analysis.wav
```

Only delete files whose upload returned a success + URL. These are regenerable from the
digest, so removing them after a confirmed upload is safe and keeps the working tree
clean (`text_to_speech/output/` is gitignored regardless).

### 6. Report the result

On full success, report:

```
Audio published.
Digest: [resolved digest path] — [date range]
Summaries edition: [summaries media URL]
Full/analysis edition: [analysis media URL]
New audio post: [WordPress post URL] (post_id [id], published live)
Local WAVs deleted.
```

On **any** failure at any step, stop at that step and report clearly:
- which step failed and the exact `error` message from the failing command,
- which WAVs were generated and where they still are on disk (do **not** delete them),
- which uploads (if any) succeeded, and
- whether a post was published.

Never delete a WAV whose upload did not succeed, and never publish a post linking to an
upload that failed.

## Notes / boundaries

- This skill **generates** audio; it does not install TTS engines. Missing engine deps
  are a stop-and-report condition, with the fix from `text_to_speech/README.md`.
- Digest text is derived from third-party notebook posts. It only ever reaches WordPress
  through `publish_digest.py`, which sanitizes it against a tag allowlist; content never
  passes through a shell here — only file paths do.
- The token is read from disk by the scripts on each run — never printed, never written
  elsewhere, never placed on a command line.
- This skill publishes a **new** post **live** (`--status publish` in step 4) because
  the user asked to publish the audio. `publish_digest.py` always POSTs to `posts/new/`,
  so this only ever creates a new post and never edits the existing digest post. To
  create a private draft for review instead, drop `--status publish` from the step 4
  command (`publish_digest.py` defaults to `draft`).
