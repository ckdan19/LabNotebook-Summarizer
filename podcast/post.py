"""Build the Markdown for a TWIF WordPress post.

The post is converted and sanitized by scripts/publish_digest.py. The audio player is a
WordPress ``[audio]`` shortcode, which survives the sanitizer as plain text and gives the
podcast category feed an audio file to use as the episode enclosure.
"""

import re
from typing import Any, Dict

SHORTCODE_RE = re.compile(r"\[/?[A-Za-z][^\]]*\]")


def _one_line(text: str) -> str:
    # Model-written text is derived from third-party notebook posts, so drop anything
    # WordPress would treat as a shortcode; only the audio shortcode below is ours.
    return " ".join(SHORTCODE_RE.sub("", str(text)).split())


LABELS = {
    "en": {
        "in_episode": "In this episode",
        "running": "**Running time:** about {minutes} minutes. **Download:** <{url}>",
        "covers": "Covers lab notebook activity from {range}, as compiled in that week's "
                  "Full Lab Digest.",
        "other": "Spanish edition: <{url}>",
        "credit": "_Script written with Claude from the weekly lab digest; voices generated "
                  "with the Kokoro text-to-speech engine._",
    },
    "es": {
        "in_episode": "En este episodio",
        "running": "**Duración:** unos {minutes} minutos. **Descargar:** <{url}>",
        "covers": "Cubre la actividad de los cuadernos de laboratorio entre {range}, según "
                  "el resumen semanal del laboratorio (Full Lab Digest).",
        "other": "Episodio original en inglés: <{url}>",
        "credit": "_Guion adaptado al español de Chile con Claude a partir del episodio en "
                  "inglés; voces generadas con el motor de texto a voz Kokoro._",
    },
}


def build_post_markdown(
    title: str,
    script: Dict[str, Any],
    audio_url: str,
    minutes: float,
    date_range: str,
    language: str = "en",
    other_edition_url: str = "",
) -> str:
    labels = LABELS[language]
    lines = [
        "# {}".format(_one_line(title)),
        "",
        '[audio mp3="{}"][/audio]'.format(audio_url),
        "",
        _one_line(script.get("description", "")),
        "",
    ]
    notes = script.get("show_notes") or []
    if notes:
        lines += ["## {}".format(labels["in_episode"]), ""]
        lines += ["- {}".format(_one_line(note)) for note in notes]
        lines.append("")
    lines += [labels["running"].format(minutes=round(minutes), url=audio_url), ""]
    if date_range:
        if language == "es":
            date_range = date_range.replace(" to ", " y ")
        lines += [labels["covers"].format(range=date_range), ""]
    if other_edition_url:
        lines += [labels["other"].format(url=other_edition_url), ""]
    lines += [labels["credit"], ""]
    return "\n".join(lines)
