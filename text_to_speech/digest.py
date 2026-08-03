"""Turn a Markdown digest into concise, speech-friendly narration."""

import html
import re
from datetime import date
from typing import List


ANALYSIS_SECTIONS = {
    "cross-notebook patterns & connections",
    "literature connections",
}
SKIPPED_FIELDS = {
    "categories",
    "figures",
    "url",
    "warnings",
}

IMAGE_RE = re.compile(r"!\[[^\]]*]\([^)]*\)")
LINK_RE = re.compile(r"\[([^\]]+)]\((?:[^()]|\([^)]*\))*\)")
RAW_URL_RE = re.compile(r"https?://[^\s)`>]+")
HTML_TAG_RE = re.compile(r"<[^>]+>")
FIELD_RE = re.compile(r"^[-*]\s+\*\*([^*]+)\*\*:\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
NARRATION_STYLES = {"direct", "conversational"}


def _spoken_date(value: str) -> str:
    """Make ISO dates less mechanical without changing other date formats."""
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        return value
    return "{} {}, {}".format(parsed.strftime("%B"), parsed.day, parsed.year)


def _conversational_heading(label: str, level: int, item_number: int) -> str:
    """Return a natural spoken introduction for a digest heading."""
    if level == 1:
        if item_number:
            # Combined digests can contain an embedded source digest with its own
            # H1. It is visual structure, not a second introduction.
            return ""
        return "Here's your lab notebook update. {}.".format(label.rstrip("."))
    if level == 2:
        if "digest" in label.lower():
            return ""
        return "{} {}.".format(
            "Let's start with" if item_number == 0 else "Now, let's turn to",
            label.rstrip("."),
        )
    if level == 3:
        lead_in = "First up" if item_number == 0 else "Next up"
        return "{}: {}.".format(lead_in, label.rstrip("."))
    return label + "."


def _conversational_field(name: str, value: str) -> str:
    """Turn a structured digest field into speech-friendly prose."""
    field = name.lower()
    value = value.rstrip(".")
    if field == "author":
        return "This update comes from {}.".format(value)
    if field == "date":
        return "It was posted on {}.".format(_spoken_date(value))
    if field == "key finding":
        return "Here's the main takeaway. {}.".format(value)
    if field == "change this week":
        return "Here's what changed this week. {}.".format(value)
    if field == "ai-use disclosure":
        return "A quick note on AI use: {}.".format(value)
    return "For {}, {}.".format(name.lower(), value)


def _plain_markdown(text: str) -> str:
    """Remove visual Markdown syntax while preserving its readable labels."""
    text = IMAGE_RE.sub("", text)
    text = LINK_RE.sub(r"\1", text)
    text = HTML_TAG_RE.sub("", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = RAW_URL_RE.sub("", text)
    text = re.sub(r"\(\s*\)", "", text)
    text = re.sub(r"(\*\*|__)(.*?)\1", r"\2", text)
    text = re.sub(r"(?<!\w)[*_](.*?)[*_](?!\w)", r"\1", text)
    text = text.replace("·", ",")
    text = re.sub(r"\s+", " ", html.unescape(text)).strip(" \t-*")
    return re.sub(r"\s+([,.;:!?])", r"\1", text)


def digest_to_narration(
    markdown: str,
    include_analysis: bool = False,
    style: str = "direct",
) -> str:
    """Extract notebook summaries and remove URLs/formatting that sound poor aloud.

    By default, the cross-notebook and literature sections are omitted so the
    recording stays focused on notebook-post summaries. Set ``include_analysis``
    to narrate those sections too. ``style="conversational"`` adds natural
    transitions and spoken versions of structured field labels; the default
    ``style="direct"`` preserves the digest's wording and order.
    """
    if style not in NARRATION_STYLES:
        raise ValueError(
            "style must be one of: {}.".format(", ".join(sorted(NARRATION_STYLES)))
        )

    conversational = style == "conversational"
    spoken: List[str] = []
    include_section = True
    in_fence = False
    skip_indented_fields = False
    skip_warning_block = False
    has_body_text = False
    title_number = 0
    section_number = 0
    post_number = 0

    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence or not line or line == "---":
            continue

        heading = HEADING_RE.match(line)
        if heading:
            level = len(heading.group(1))
            label = _plain_markdown(heading.group(2))
            if level == 2:
                include_section = include_analysis or label.lower() not in ANALYSIS_SECTIONS
                if include_section and "digest" not in label.lower():
                    post_number = 0
            if include_section and label:
                item_number = post_number
                if level == 1:
                    item_number = title_number
                elif level == 2:
                    item_number = section_number
                heading_text = label + "."
                if conversational:
                    heading_text = _conversational_heading(
                        label,
                        level,
                        item_number,
                    )
                if heading_text:
                    spoken.append(heading_text)
                if conversational and level == 1:
                    title_number += 1
                if conversational and level == 2 and "digest" not in label.lower():
                    section_number += 1
                if conversational and level == 3:
                    post_number += 1
            skip_indented_fields = False
            skip_warning_block = False
            continue

        if not include_section or skip_warning_block:
            continue
        if line.startswith(">"):
            # Activity counts and generated-at footers are useful on screen but
            # repetitive in a spoken summary.
            continue

        field = FIELD_RE.match(line)
        if field:
            name = _plain_markdown(field.group(1))
            value = _plain_markdown(field.group(2))
            skip_indented_fields = name.lower() in SKIPPED_FIELDS
            if not skip_indented_fields and value:
                spoken.append(
                    _conversational_field(name, value)
                    if conversational
                    else "{}: {}.".format(name, value.rstrip("."))
                )
                has_body_text = True
            continue

        if skip_indented_fields and raw_line[:1].isspace():
            continue
        skip_indented_fields = False

        if line.startswith("|") or re.fullmatch(r"[-:| ]+", line):
            continue
        text = _plain_markdown(re.sub(r"^[-*]\s+", "", line))
        if text.lower().rstrip(".") == "warnings":
            skip_warning_block = True
            continue
        if text and not re.fullmatch(r"https?://\S+", text):
            spoken.append(text if text.endswith((".", "!", "?")) else text + ".")
            has_body_text = True

    if conversational and has_body_text:
        spoken.append("That's the latest from the lab notebooks.")

    narration = "\n\n".join(spoken).strip()
    if not narration or not has_body_text:
        raise ValueError("The digest did not contain any narratable summary text.")
    return narration


def chunk_narration(text: str, max_chars: int = 500) -> List[str]:
    """Split narration at paragraphs and sentences without cutting words."""
    if max_chars < 80:
        raise ValueError("max_chars must be at least 80.")

    chunks: List[str] = []
    current = ""

    def add_piece(piece: str) -> None:
        nonlocal current
        piece = piece.strip()
        if not piece:
            return
        candidate = "{} {}".format(current, piece).strip()
        if len(candidate) <= max_chars:
            current = candidate
            return
        if current:
            chunks.append(current)
            current = ""
        while len(piece) > max_chars:
            split_at = piece.rfind(" ", 0, max_chars + 1)
            if split_at < 1:
                split_at = max_chars
            chunks.append(piece[:split_at].strip())
            piece = piece[split_at:].strip()
        current = piece

    for paragraph in re.split(r"\n\s*\n", text):
        sentences = re.split(r"(?<=[.!?])\s+", paragraph.strip())
        for sentence in sentences:
            add_piece(sentence)
        if current:
            chunks.append(current)
            current = ""

    if current:
        chunks.append(current)
    return chunks
