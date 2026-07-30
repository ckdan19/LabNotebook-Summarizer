# Digest Text to Speech

This directory is a self-contained, optional audio layer for LabNotebook-Summarizer.
It reads a completed Markdown digest and writes a mono WAV file. The fetchers,
summarization workflows, digest state, and WordPress publisher do not import it.

Two local engines are supported behind the same provider interface:

- `kokoro` (default): Kokoro-82M with a selectable built-in voice and speed.
- `chatterbox-nano`: Resemble AI's English Nano model, with an optional reference
  recording for an authorized voice.

Generated files go to `text_to_speech/output/` by default and are ignored by Git.

## Setup

Both current engine packages require Python 3.10 or newer. Chatterbox is developed
and tested upstream with Python 3.11, so Python 3.11 is the simplest shared choice.
Keep the environment separate from the repository's standard-library fetch scripts:

```bash
python3.11 -m venv .venv-tts
source .venv-tts/bin/activate
python -m pip install --upgrade pip
```

Install one engine:

```bash
pip install -r text_to_speech/requirements-kokoro.txt
```

or:

```bash
pip install -r text_to_speech/requirements-chatterbox-nano.txt
```

Kokoro uses `espeak-ng` for English fallback and some languages. On macOS:

```bash
brew install espeak-ng
```

The first real generation downloads model weights from the provider's model host.

## Generate a digest recording

Preview exactly what will be spoken without installing or loading a model:

```bash
python -m text_to_speech digests/full-lab-digest-2026-07-28-7d.md --dry-run
```

The default `direct` style stays close to the written digest. For a smoother
spoken version with transitions, friendlier field phrasing, and a closing line,
select the `conversational` style:

```bash
python -m text_to_speech digests/full-lab-digest-2026-07-28-7d.md \
  --style conversational \
  --dry-run
```

Generate with Kokoro:

```bash
python -m text_to_speech digests/full-lab-digest-2026-07-28-7d.md \
  --provider kokoro \
  --voice af_heart
```

Generate with Chatterbox-Nano:

```bash
python -m text_to_speech digests/full-lab-digest-2026-07-28-7d.md \
  --provider chatterbox-nano \
  --device auto
```

An authorized reference clip can condition Chatterbox-Nano:

```bash
python -m text_to_speech DIGEST.md \
  --provider chatterbox-nano \
  --voice-sample /absolute/path/to/reference.wav
```

Use a person's voice only with their permission. Chatterbox-generated speech
contains the provider's built-in perceptual watermark.

By default, narration includes notebook post summaries and omits the
cross-notebook/literature sections. Add `--include-analysis` to narrate the entire
digest. Use `--style direct` (the default) or `--style conversational` to choose
the spoken presentation. Conversational output gets a `-conversational` filename
suffix so it does not overwrite a direct recording. Use
`--output path/to/file.wav` to override the output location.

## Reading the output

A full digest takes several minutes to synthesize. When run in a terminal, the
chunk counter (`Synthesizing chunk 12/135...`) is written to stderr so a long run
is visibly alive; stdout stays a single JSON object, and the counter is suppressed
when stderr is redirected. Torch's `dropout`/`weight_norm` notices come from the
engine packages themselves and are harmless. A failed run prints
`{"error": ...}` and exits non-zero, so a `"status": "audio generated"` object
means the WAV was written.

## Design boundary

`digest.py` is the Markdown-to-speech preparation layer. `providers/` contains the
only engine-specific imports. `engine.py` chunks narration and combines provider
results, while `audio.py` owns the provider-neutral WAV format. Optional packages
are imported lazily, so importing or testing the rest of the repository never loads
Torch or downloads a model.
