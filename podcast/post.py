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


def build_post_markdown(
    title: str,
    script: Dict[str, Any],
    audio_url: str,
    minutes: float,
    date_range: str,
) -> str:
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
        lines += ["## In this episode", ""]
        lines += ["- {}".format(_one_line(note)) for note in notes]
        lines.append("")
    lines += [
        "**Running time:** about {} minutes. **Download:** <{}>".format(round(minutes), audio_url),
        "",
    ]
    if date_range:
        lines += [
            "Covers lab notebook activity from {}, as compiled in that week's "
            "Full Lab Digest.".format(date_range),
            "",
        ]
    lines += [
        "_Script written with Claude from the weekly lab digest; voices generated with "
        "the Kokoro text-to-speech engine._",
        "",
    ]
    return "\n".join(lines)
