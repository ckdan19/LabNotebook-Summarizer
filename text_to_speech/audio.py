"""Small WAV helpers shared by all optional TTS providers."""

import wave
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class AudioSegment:
    """Mono, signed 16-bit PCM audio."""

    pcm16: bytes
    sample_rate: int

    def __post_init__(self) -> None:
        if not self.pcm16:
            raise ValueError("A TTS provider returned an empty audio segment.")
        if len(self.pcm16) % 2:
            raise ValueError("16-bit PCM data must contain an even number of bytes.")
        if self.sample_rate <= 0:
            raise ValueError("sample_rate must be positive.")


def samples_to_segment(samples: object, sample_rate: int) -> AudioSegment:
    """Convert a NumPy-compatible floating waveform to clipped PCM16."""
    try:
        import numpy as np
    except ImportError as exc:
        raise RuntimeError(
            "The selected TTS provider did not install NumPy correctly."
        ) from exc

    audio = np.asarray(samples, dtype=np.float32)
    if audio.ndim > 1:
        audio = audio.reshape((-1, audio.shape[-1])).mean(axis=0)
    audio = np.clip(audio.reshape(-1), -1.0, 1.0)
    pcm = (audio * 32767.0).astype("<i2").tobytes()
    return AudioSegment(pcm, int(sample_rate))


def write_wav(
    path: Path,
    segments: Iterable[AudioSegment],
    pause_seconds: float = 0.2,
) -> None:
    """Write segments as one mono WAV, inserting a short pause between them."""
    if pause_seconds < 0:
        raise ValueError("pause_seconds cannot be negative.")

    iterator = iter(segments)
    try:
        first = next(iterator)
    except StopIteration:
        raise ValueError("No audio segments were generated.")

    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(first.sample_rate)
        output.writeframes(first.pcm16)
        silence = b"\x00\x00" * int(first.sample_rate * pause_seconds)
        for segment in iterator:
            if segment.sample_rate != first.sample_rate:
                raise ValueError(
                    "TTS provider changed sample rate from {} to {}.".format(
                        first.sample_rate, segment.sample_rate
                    )
                )
            output.writeframes(silence)
            output.writeframes(segment.pcm16)

