"""Voice a two-host script with Kokoro and encode it to MP3 with ffmpeg."""

import copy
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Callable, Dict, Iterator, List, Optional

from text_to_speech.audio import AudioSegment, write_wav
from text_to_speech.digest import chunk_narration
from text_to_speech.providers.base import SpeechProvider

DEFAULT_VOICES = {"HOST_A": "af_heart", "HOST_B": "am_michael"}
TURN_PAUSE = 0.35  # seconds of silence between speakers
CHUNK_PAUSE = 0.12  # seconds between chunks of one long turn
MP3_BITRATE = "96k"


def voice_providers(base: SpeechProvider, voices: Dict[str, str]) -> Dict[str, SpeechProvider]:
    """One provider per host sharing a single loaded Kokoro pipeline.

    KokoroProvider reads ``self.voice`` on every call, so a shallow copy with a
    different voice reuses the model weights instead of loading them twice.
    """
    providers = {}
    for speaker, voice in voices.items():
        clone = copy.copy(base)
        clone.voice = voice
        providers[speaker] = clone
    return providers


def _silence(seconds: float, sample_rate: int) -> AudioSegment:
    return AudioSegment(b"\x00\x00" * max(1, int(sample_rate * seconds)), sample_rate)


def render_script_wav(
    segments: List[Dict[str, str]],
    output: Path,
    providers: Dict[str, SpeechProvider],
    *,
    chunk_chars: int = 400,
    progress: Optional[Callable[[int, int], None]] = None,
) -> int:
    """Synthesize every turn in order into one mono WAV. Returns turns voiced."""
    total = len(segments)

    def audio() -> Iterator[AudioSegment]:
        rate = None
        for index, segment in enumerate(segments, start=1):
            if progress is not None:
                progress(index, total)
            provider = providers[segment["speaker"]]
            for chunk_index, chunk in enumerate(chunk_narration(segment["text"], chunk_chars)):
                voiced = provider.synthesize(chunk)
                if rate is not None:
                    yield _silence(CHUNK_PAUSE if chunk_index else TURN_PAUSE, rate)
                rate = voiced.sample_rate
                yield voiced

    output.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        prefix=".twif-", suffix=".wav", dir=str(output.parent), delete=False
    )
    temporary = Path(handle.name)
    handle.close()
    try:
        write_wav(temporary, audio(), pause_seconds=0)
        temporary.replace(output)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return total


def ffmpeg_command(wav: Path, mp3: Path, metadata: Dict[str, str]) -> List[str]:
    command = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(wav),
        "-codec:a", "libmp3lame", "-b:a", MP3_BITRATE, "-ac", "1",
    ]
    for key, value in metadata.items():
        command += ["-metadata", "{}={}".format(key, value)]
    return command + [str(mp3)]


def encode_mp3(wav: Path, mp3: Path, metadata: Dict[str, str]) -> None:
    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "ffmpeg is not installed (macOS: 'brew install ffmpeg'; "
            "Ubuntu: 'sudo apt-get install ffmpeg')."
        )
    completed = subprocess.run(
        ffmpeg_command(wav, mp3, metadata), capture_output=True, text=True
    )
    if completed.returncode != 0:
        raise RuntimeError("ffmpeg failed: {}".format(completed.stderr.strip()[:500]))


def duration_minutes(wav: Path) -> float:
    import wave

    with wave.open(str(wav), "rb") as handle:
        return handle.getnframes() / handle.getframerate() / 60
