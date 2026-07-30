"""Command-line interface for digest narration."""

import argparse
import json
import sys
from pathlib import Path

from .digest import chunk_narration, digest_to_narration
from .engine import generate_audio
from .providers import create_provider


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate narrated WAV audio from a LabNotebook Markdown digest."
    )
    parser.add_argument("digest", type=Path, help="Markdown digest to narrate")
    parser.add_argument(
        "--provider",
        choices=("kokoro", "chatterbox-nano"),
        default="kokoro",
        help="local speech engine (default: kokoro)",
    )
    parser.add_argument("--output", type=Path, help="output WAV path")
    parser.add_argument(
        "--include-analysis",
        action="store_true",
        help="also narrate cross-notebook and literature sections",
    )
    parser.add_argument(
        "--style",
        choices=("direct", "conversational"),
        default="direct",
        help="narration style (default: direct)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the prepared narration without loading a speech model",
    )
    parser.add_argument("--chunk-chars", type=int, default=500)
    parser.add_argument("--pause", type=float, default=0.2, help="seconds between chunks")

    kokoro = parser.add_argument_group("Kokoro options")
    kokoro.add_argument("--voice", default="af_heart")
    kokoro.add_argument("--language", default="a", help="Kokoro language code")
    kokoro.add_argument("--speed", type=float, default=1.0)

    chatterbox = parser.add_argument_group("Chatterbox-Nano options")
    chatterbox.add_argument(
        "--device",
        choices=("auto", "cpu", "mps", "cuda"),
        default="auto",
    )
    chatterbox.add_argument(
        "--voice-sample",
        help="optional reference WAV for voice cloning; use only with permission",
    )
    return parser


def _progress_reporter():
    """Return a stderr progress callback, or None when output is not a terminal."""
    if not sys.stderr.isatty():
        return None

    def report(index: int, total: int) -> None:
        print(
            "\rSynthesizing chunk {}/{}...".format(index, total),
            end="",
            file=sys.stderr,
            flush=True,
        )

    return report


def _default_output(digest: Path, provider: str, style: str = "direct") -> Path:
    suffix = "-conversational" if style == "conversational" else ""
    filename = "{}-{}{}.wav".format(digest.stem, provider, suffix)
    return Path(__file__).resolve().parent / "output" / filename


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        markdown = args.digest.read_text(encoding="utf-8")
        narration = digest_to_narration(
            markdown,
            include_analysis=args.include_analysis,
            style=args.style,
        )
        chunks = chunk_narration(narration, max_chars=args.chunk_chars)
        output = args.output or _default_output(args.digest, args.provider, args.style)

        if args.dry_run:
            print(json.dumps(
                {
                    "dry_run": True,
                    "digest": str(args.digest),
                    "provider": args.provider,
                    "style": args.style,
                    "output": str(output),
                    "characters": len(narration),
                    "chunks": len(chunks),
                    "narration": narration,
                },
                indent=2,
            ))
            return

        provider = create_provider(
            args.provider,
            device=args.device,
            voice=args.voice,
            language=args.language,
            speed=args.speed,
            voice_sample=args.voice_sample,
        )
        progress = _progress_reporter()
        generated_chunks = generate_audio(
            narration,
            output,
            provider,
            chunk_chars=args.chunk_chars,
            pause_seconds=args.pause,
            progress=progress,
        )
        if progress is not None:
            print("\r\033[KSynthesized {} chunks.".format(generated_chunks), file=sys.stderr)
        print(json.dumps(
            {
                "status": "audio generated",
                "digest": str(args.digest),
                "provider": args.provider,
                "style": args.style,
                "output": str(output),
                "chunks": generated_chunks,
            },
            indent=2,
        ))
    except (OSError, ValueError, RuntimeError) as exc:
        print(json.dumps({"error": str(exc)}, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
