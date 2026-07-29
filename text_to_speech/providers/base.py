"""Provider contract for an isolated speech engine."""

from abc import ABC, abstractmethod

from ..audio import AudioSegment


class ProviderUnavailable(RuntimeError):
    """Raised when an optional engine is not installed or cannot load."""


class SpeechProvider(ABC):
    """A loaded engine capable of synthesizing one narration chunk."""

    @abstractmethod
    def synthesize(self, text: str) -> AudioSegment:
        """Return mono PCM16 audio for ``text``."""

