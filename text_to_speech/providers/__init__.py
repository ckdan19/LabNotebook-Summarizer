"""Lazy provider selection keeps heavyweight engines optional."""

from typing import Optional

from .base import SpeechProvider


def create_provider(
    name: str,
    *,
    device: str = "auto",
    voice: str = "af_heart",
    language: str = "a",
    speed: float = 1.0,
    voice_sample: Optional[str] = None,
) -> SpeechProvider:
    if name == "kokoro":
        from .kokoro import KokoroProvider

        return KokoroProvider(voice=voice, language=language, speed=speed)
    if name == "chatterbox-nano":
        from .chatterbox_nano import ChatterboxNanoProvider

        return ChatterboxNanoProvider(device=device, voice_sample=voice_sample)
    raise ValueError("Unknown TTS provider: {!r}".format(name))


__all__ = ["SpeechProvider", "create_provider"]

