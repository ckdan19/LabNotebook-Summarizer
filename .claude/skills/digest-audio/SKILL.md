# Digest Audio Skill

Trigger this skill when the user asks to narrate a lab digest, create an audio
version of notebook summaries, or generate speech with Kokoro or Chatterbox-Nano.

## Steps

1. Identify the Markdown digest to narrate. If the user refers to "the latest
   digest", select the newest `digests/full-lab-digest-*.md` by the date encoded in
   the filename. Do not generate a new digest unless the user also asks for one.
2. Use `kokoro` unless the user explicitly requests Chatterbox-Nano. Do not install
   an engine automatically; if its optional dependency is missing, return the
   command from `text_to_speech/README.md` that installs that provider in the
   isolated Python 3.11 environment.
3. First run the preparation-only check:

   ```bash
   python -m text_to_speech DIGEST.md --provider PROVIDER --style STYLE --dry-run
   ```

   Check that the narration includes post titles and key findings and does not read
   URLs, figure paths, or generated-at metadata. Use `direct` unless the user asks
   for a more natural or conversational version; in that case use
   `--style conversational`.
4. Generate the WAV:

   ```bash
   python -m text_to_speech DIGEST.md --provider PROVIDER --style STYLE
   ```

   Pass any user-requested voice, speed, device, output, or `--include-analysis`
   options. A `--voice-sample` must be a recording the user is authorized to use.
5. Return the absolute output path and render the WAV in the conversation when the
   client supports local audio playback.
