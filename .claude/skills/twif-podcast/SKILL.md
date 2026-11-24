# TWIF Podcast Skill

Trigger this skill when the user asks to **make, run, preview, or publish this week's
TWIF episode**, the **"This Week in FTR" podcast**, or similar phrasing about the weekly
lab podcast.

TWIF is a two-host podcast built from the newest weekly full lab digest
(`digests/full-lab-digest-YYYY-MM-DD-7d.md`). The `podcast` package does all of the work.
This skill only runs it and reports the result. It normally runs every Wednesday from
`.github/workflows/twif-podcast.yml`. Use this skill for a manual or local run.

Paths are relative to the repository root.

## Prerequisites

- `.venv-tts/bin/python` exists, with Kokoro and the podcast dependencies installed:
  `.venv-tts/bin/python -m pip install -r text_to_speech/requirements-kokoro.txt -r podcast/requirements.txt`.
  If it is missing, stop and give the user that command. Do not install anything yourself.
- `ffmpeg` is on PATH (`brew install ffmpeg` on macOS). It is needed for anything past `--dry-run`.
- `ANTHROPIC_API_KEY` is set in the environment.
- The WordPress token is at `~/.config/LabNotebook-Summarizer/wp_token`. The scripts read it
  themselves. Never read it, echo it, or pass it on a command line.
- The `podcast` category already exists on genefish.wordpress.com. The token cannot create
  categories, and an unknown category is silently dropped.

## Steps

1. Show the plan:

   ```bash
   .venv-tts/bin/python -m podcast next
   ```

   Report the digest, the episode label (for example `S01E03`), and any `skip` reason.

2. Write the script only. This makes one Claude API call and nothing else:

   ```bash
   .venv-tts/bin/python -m podcast run --dry-run
   ```

   Show the user the title, the word count (about 1,500-2,200 words is 10-15 minutes) and
   the description. Offer to show the script JSON from `podcast/output/`.

3. With the user's go-ahead, make the full episode, reusing the reviewed script so Claude
   is not called a second time:

   ```bash
   .venv-tts/bin/python -m podcast run --script-file podcast/output/TWIF-S01EXX.json
   ```

   This publishes **live** by default. Add `--status draft` if the user wants a draft, or
   `--no-publish` to stop once the MP3 exists.

4. Report `title`, `minutes`, `audio_url`, `post_url` and `post_id`. If the command prints
   `{"error": ...}`, report it verbatim and stop. Do not retry the upload or the post by
   hand. The error message says whether the MP3 had already been uploaded.

5. A successful publish appends the episode to `podcast/episodes.json`. Tell the user this
   file needs committing so the next episode number is right.

## Notes

- The episode number is one more than the highest episode recorded in
  `podcast/episodes.json`. A digest that already has an episode is skipped.
- A weekly digest more than 10 days old is skipped unless `--allow-stale` is passed.
- `--digest PATH`, `--hosts A B`, `--voice-a` and `--voice-b` change the source digest,
  the host names and the Kokoro voices.
