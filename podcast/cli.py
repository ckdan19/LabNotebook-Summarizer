"""TWIF (This Week in FTR) episode pipeline.

    python -m podcast next                 # which digest / episode number would run
    python -m podcast run --dry-run        # write the script only; no audio, no upload
    python -m podcast run                  # script -> MP3 -> upload -> live post

Every step prints one JSON object on stdout; failures print {"error": ...} and exit 1.
The WordPress token is never read here: uploading and posting are delegated to
scripts/upload_media.py and scripts/publish_digest.py, which read it themselves.
"""

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any, Dict, List

from . import episodes
from .post import build_post_markdown
from .script import (DEFAULT_HOSTS, MODEL, ScriptError, generate_script, validate_script,
                     word_count)

OUTPUT_DIR = episodes.REPO_ROOT / "podcast" / "output"
SCRIPTS_DIR = episodes.REPO_ROOT / "scripts"
CATEGORY = "podcast"
MAX_DIGEST_AGE_DAYS = 10


class PipelineError(RuntimeError):
    pass


def _emit(payload: Dict[str, Any]) -> None:
    print(json.dumps(payload, indent=2))


def _progress(index: int, total: int) -> None:
    if sys.stderr.isatty():
        print("\rVoicing turn {}/{}...".format(index, total), end="", file=sys.stderr, flush=True)


def _run_json(command: List[str]) -> Dict[str, Any]:
    """Run one of the stdlib publishing scripts and return its JSON report."""
    completed = subprocess.run(command, capture_output=True, text=True)
    try:
        report = json.loads(completed.stdout)
    except json.JSONDecodeError:
        raise PipelineError(
            "{} printed no JSON (exit {}): {}".format(
                Path(command[1]).name, completed.returncode,
                (completed.stderr or completed.stdout).strip()[:500],
            )
        )
    if completed.returncode != 0 or "error" in report:
        raise PipelineError("{} failed: {}".format(Path(command[1]).name, report.get("error", report)))
    return report


def select_digest(args, state) -> Path:
    digest = Path(args.digest) if args.digest else episodes.latest_weekly_digest()
    if digest is None or not digest.exists():
        raise PipelineError("No weekly full-lab-digest-*-7d.md digest was found.")
    return digest


def plan(args) -> Dict[str, Any]:
    state = episodes.load_state()
    digest = select_digest(args, state)
    season = state["season"]
    number = episodes.next_episode_number(state)
    info: Dict[str, Any] = {
        "digest": str(digest),
        "season": season,
        "episode": number,
        "label": episodes.episode_label(season, number),
    }
    covered = episodes.already_covered(state, digest)
    if covered:
        info["skip"] = "Digest {} was already used for {}.".format(
            digest.name, episodes.episode_label(covered.get("season", season), covered["episode"])
        )
        return info
    made = episodes.digest_date(digest)
    if made and not args.allow_stale and (date.today() - made).days > MAX_DIGEST_AGE_DAYS:
        info["skip"] = (
            "Newest weekly digest ({}) is more than {} days old; the Monday digest may "
            "have failed. Pass --allow-stale to use it anyway.".format(made, MAX_DIGEST_AGE_DAYS)
        )
    return info


def cmd_next(args) -> None:
    _emit(plan(args))


def cmd_run(args) -> None:
    info = plan(args)
    if "skip" in info:
        _emit({"status": "skipped", **info})
        return

    digest = Path(info["digest"])
    markdown = digest.read_text(encoding="utf-8")
    label = info["label"]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    script_path = OUTPUT_DIR / "TWIF-{}.json".format(label)

    if args.script_file:
        script = validate_script(json.loads(Path(args.script_file).read_text(encoding="utf-8")))
    else:
        script = generate_script(markdown, label, hosts=tuple(args.hosts), model=args.model)
        script_path.write_text(json.dumps(script, indent=2) + "\n", encoding="utf-8")

    title = episodes.post_title(info["season"], info["episode"], script["episode_title"])
    report: Dict[str, Any] = {
        **info,
        "title": title,
        "script_file": str(args.script_file or script_path),
        "words": word_count(script),
        "turns": len(script["segments"]),
    }
    if args.dry_run:
        report["status"] = "script written (dry run: no audio, no upload, no post)"
        report["description"] = script.get("description", "")
        _emit(report)
        return

    # --- audio ---------------------------------------------------------------
    from text_to_speech.providers import create_provider
    from .render import DEFAULT_VOICES, duration_minutes, encode_mp3, render_script_wav, voice_providers

    voices = {"HOST_A": args.voice_a or DEFAULT_VOICES["HOST_A"],
              "HOST_B": args.voice_b or DEFAULT_VOICES["HOST_B"]}
    base = create_provider("kokoro", voice=voices["HOST_A"], speed=args.speed)
    stem = "TWIF-{}".format(label)
    wav = OUTPUT_DIR / (stem + ".wav")
    mp3 = OUTPUT_DIR / (stem + ".mp3")
    render_script_wav(script["segments"], wav, voice_providers(base, voices), progress=_progress)
    if sys.stderr.isatty():
        print("", file=sys.stderr)
    minutes = duration_minutes(wav)
    encode_mp3(wav, mp3, {
        "title": title,
        "album": "This Week in FTR",
        "artist": "Roberts Lab",
        "track": str(info["episode"]),
        "genre": "Podcast",
    })
    wav.unlink()
    report.update({"mp3": str(mp3), "minutes": round(minutes, 1)})

    if args.no_publish:
        report["status"] = "audio generated (not uploaded)"
        _emit(report)
        return

    # --- upload + post -------------------------------------------------------
    upload = _run_json([sys.executable, str(SCRIPTS_DIR / "upload_media.py"), str(mp3),
                        "--title", title])
    audio_url = upload["url"]
    post_md = OUTPUT_DIR / (stem + "-post.md")
    post_md.write_text(
        build_post_markdown(title, script, audio_url, minutes, episodes.digest_range(markdown)),
        encoding="utf-8",
    )
    try:
        post = _run_json([sys.executable, str(SCRIPTS_DIR / "publish_digest.py"), str(post_md),
                          "--category", CATEGORY, "--status", args.status])
    except PipelineError as exc:
        raise PipelineError("{} (the MP3 was already uploaded: {})".format(exc, audio_url))

    entry = {
        "season": info["season"],
        "episode": info["episode"],
        "title": title,
        "digest": digest.name,
        "published": date.today().isoformat(),
        "status": post.get("post_status", args.status),
        "post_url": post.get("url", ""),
        "post_id": post.get("post_id", ""),
        "audio_url": audio_url,
        "minutes": round(minutes, 1),
    }
    episodes.save_state(episodes.record_episode(episodes.load_state(), entry))
    report.update({"status": post.get("status"), "post_url": entry["post_url"],
                   "post_id": entry["post_id"], "audio_url": audio_url})
    _emit(report)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m podcast", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    def common(p):
        p.add_argument("--digest", help="digest to use (default: newest weekly 7d digest)")
        p.add_argument("--allow-stale", action="store_true",
                       help="use the newest digest even if it is more than 10 days old")

    common(sub.add_parser("next", help="show which digest and episode number would run"))
    run = sub.add_parser("run", help="write, voice, upload, and post the next episode")
    common(run)
    run.add_argument("--dry-run", action="store_true", help="write the script only")
    run.add_argument("--no-publish", action="store_true", help="stop after making the MP3")
    run.add_argument("--script-file", help="reuse a saved script JSON instead of calling Claude")
    run.add_argument("--status", choices=["publish", "draft"], default="publish",
                     help="WordPress post status (default: publish)")
    run.add_argument("--model", default=MODEL)
    run.add_argument("--hosts", nargs=2, default=list(DEFAULT_HOSTS), metavar=("A", "B"))
    run.add_argument("--voice-a", help="Kokoro voice for host A (default af_heart)")
    run.add_argument("--voice-b", help="Kokoro voice for host B (default am_michael)")
    run.add_argument("--speed", type=float, default=1.0)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        {"next": cmd_next, "run": cmd_run}[args.command](args)
    except (PipelineError, ScriptError, OSError, ValueError, RuntimeError) as exc:
        _emit({"error": str(exc)})
        sys.exit(1)


if __name__ == "__main__":
    main()
