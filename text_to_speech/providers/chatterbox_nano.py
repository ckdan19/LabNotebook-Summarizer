"""Chatterbox-Nano adapter."""

from pathlib import Path
from typing import Optional

from ..audio import AudioSegment, samples_to_segment
from .base import ProviderUnavailable, SpeechProvider


def _select_device(torch_module: object, requested: str) -> str:
    if requested != "auto":
        return requested
    if torch_module.cuda.is_available():
        return "cuda"
    mps = getattr(torch_module.backends, "mps", None)
    if mps is not None and mps.is_available():
        return "mps"
    return "cpu"


class ChatterboxNanoProvider(SpeechProvider):
    """Generate English speech with Resemble AI's 110M Nano model."""

    def __init__(self, device: str = "auto", voice_sample: Optional[str] = None):
        if voice_sample and not Path(voice_sample).is_file():
            raise ValueError("Voice sample does not exist: {}".format(voice_sample))
        try:
            import torch
            from chatterbox.tts_turbo import ChatterboxTurboTTS
        except ImportError as exc:
            raise ProviderUnavailable(
                "Chatterbox-Nano is not installed. Create a Python 3.10+ environment "
                "and run 'pip install -r "
                "text_to_speech/requirements-chatterbox-nano.txt'."
            ) from exc

        self.torch = torch
        self.device = _select_device(torch, device)
        self.voice_sample = voice_sample
        try:
            self.model = ChatterboxTurboTTS.from_pretrained(
                device=self.device,
                nano=True,
            )
        except Exception as exc:
            raise ProviderUnavailable(
                "Chatterbox-Nano could not load on {}: {}".format(self.device, exc)
            ) from exc

    def synthesize(self, text: str) -> AudioSegment:
        options = {}
        if self.voice_sample:
            options["audio_prompt_path"] = self.voice_sample
        try:
            with self.torch.inference_mode():
                waveform = self.model.generate(text, **options)
            if hasattr(waveform, "detach"):
                waveform = waveform.detach().cpu().float().numpy()
            return samples_to_segment(waveform, int(self.model.sr))
        except Exception as exc:
            raise RuntimeError(
                "Chatterbox-Nano synthesis failed on {}: {}".format(self.device, exc)
            ) from exc

