"""Provider-independent narration orchestration."""

import tempfile
from pathlib import Path

from .audio import write_wav
from .digest import chunk_narration
from .providers.base import SpeechProvider


def generate_audio(
    narration: str,
    output: Path,
    provider: SpeechProvider,
    *,
    chunk_chars: int = 500,
    pause_seconds: float = 0.2,
) -> int:
    """Synthesize narration and return the number of engine calls made."""
    chunks = chunk_narration(narration, max_chars=chunk_chars)
    segments = (provider.synthesize(chunk) for chunk in chunks)
    output.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        prefix=".digest-audio-",
        suffix=".wav",
        dir=str(output.parent),
        delete=False,
    )
    temporary = Path(handle.name)
    handle.close()
    try:
        write_wav(temporary, segments, pause_seconds=pause_seconds)
        temporary.replace(output)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return len(chunks)
