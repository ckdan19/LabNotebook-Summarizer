"""Kokoro-82M adapter."""

from ..audio import AudioSegment, samples_to_segment
from .base import ProviderUnavailable, SpeechProvider


class KokoroProvider(SpeechProvider):
    """Generate speech with hexgrad's official ``kokoro`` inference package."""

    SAMPLE_RATE = 24000
    REPO_ID = "hexgrad/Kokoro-82M"

    def __init__(self, voice: str = "af_heart", language: str = "a", speed: float = 1.0):
        if speed <= 0:
            raise ValueError("Kokoro speed must be positive.")
        try:
            from kokoro import KPipeline
        except ImportError as exc:
            raise ProviderUnavailable(
                "Kokoro is not installed. Create a Python 3.10+ environment and run "
                "'pip install -r text_to_speech/requirements-kokoro.txt'."
            ) from exc

        self.voice = voice
        self.speed = speed
        try:
            self.pipeline = KPipeline(lang_code=language, repo_id=self.REPO_ID)
        except Exception as exc:
            raise ProviderUnavailable("Kokoro could not load: {}".format(exc)) from exc

    def synthesize(self, text: str) -> AudioSegment:
        parts = []
        try:
            generated = self.pipeline(
                text,
                voice=self.voice,
                speed=self.speed,
                split_pattern=r"\n+",
            )
            for _graphemes, _phonemes, samples in generated:
                parts.append(samples_to_segment(samples, self.SAMPLE_RATE).pcm16)
        except Exception as exc:
            raise RuntimeError("Kokoro synthesis failed: {}".format(exc)) from exc
        if not parts:
            raise RuntimeError("Kokoro synthesis produced no audio.")
        return AudioSegment(b"".join(parts), self.SAMPLE_RATE)

