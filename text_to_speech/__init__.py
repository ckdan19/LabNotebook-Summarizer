"""Generate narrated WAV files from LabNotebook-Summarizer digests."""

from .digest import digest_to_narration
from .engine import generate_audio

__all__ = ["digest_to_narration", "generate_audio"]

