"""TWIF (This Week in FTR) episode pipeline.

    python -m podcast next                 # which digest / episode number would run
    python -m podcast run --dry-run        # write the script only; no audio, no upload
    python -m podcast run                  # script -> MP3 -> upload -> live post
    python -m podcast spanish              # (re)make the Spanish edition of the latest episode

Each episode is published twice: in English (category "podcast") and as a Chilean Spanish
adaptation (category "podcast-es"). A Spanish failure never undoes the English episode.

Every step prints one JSON object on stdout; failures print {"error": ...} and exit 1.
A run whose English episode succeeded but whose Spanish edition failed exits 2.
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
from .script import (DEFAULT_HOSTS, MODEL, ScriptError, adapt_to_spanish, generate_script,
                     validate_script, word_count)

OUTPUT_DIR = episodes.REPO_ROOT / "podcast" / "output"
SCRIPTS_DIR = episodes.REPO_ROOT / "scripts"
CATEGORIES = {"en": "podcast", "es": "podcast-es"}
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


def _load_script(path: str) -> Dict[str, Any]:
    return validate_script(json.loads(Path(path).read_text(encoding="utf-8")))


def _save_script(script: Dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(script, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def produce(script: Dict[str, Any], *, title: str, stem: str, language: str, episode: int,
            date_range: str, args, other_edition_url: str = "") -> Dict[str, Any]:
    """Voice ``script``, encode MP3, and (unless --no-publish) upload and post it."""
    from text_to_speech.providers import create_provider
    from .render import LANGUAGES, duration_minutes, encode_mp3, render_script_wav, voice_providers

    config = LANGUAGES[language]
    voices = dict(config["voices"])
    if language == "en":
        voices["HOST_A"] = args.voice_a or voices["HOST_A"]
        voices["HOST_B"] = args.voice_b or voices["HOST_B"]
    base = create_provider("kokoro", voice=voices["HOST_A"], language=config["kokoro_lang"],
                           speed=args.speed)
    wav = OUTPUT_DIR / (stem + ".wav")
    mp3 = OUTPUT_DIR / (stem + ".mp3")
    render_script_wav(script["segments"], wav, voice_providers(base, voices), progress=_progress)
    if sys.stderr.isatty():
        print("", file=sys.stderr)
    minutes = duration_minutes(wav)
    encode_mp3(wav, mp3, {
        "title": title,
        "album": config["album"],
        "artist": "Roberts Lab",
        "track": str(episode),
        "genre": "Podcast",
        "language": config["id3_lang"],
    })
    wav.unlink()
    result: Dict[str, Any] = {"title": title, "mp3": str(mp3), "minutes": round(minutes, 1)}
    if args.no_publish:
        result["status"] = "audio generated (not uploaded)"
        return result

    upload = _run_json([sys.executable, str(SCRIPTS_DIR / "upload_media.py"), str(mp3),
                        "--title", title])
    audio_url = upload["url"]
    post_md = OUTPUT_DIR / (stem + "-post.md")
    post_md.write_text(
        build_post_markdown(title, script, audio_url, minutes, date_range,
                            language=language, other_edition_url=other_edition_url),
        encoding="utf-8",
    )
    try:
        post = _run_json([sys.executable, str(SCRIPTS_DIR / "publish_digest.py"), str(post_md),
                          "--category", CATEGORIES[language], "--status", args.status])
    except PipelineError as exc:
        raise PipelineError("{} (the MP3 was already uploaded: {})".format(exc, audio_url))
    result.update({
        "status": post.get("post_status", args.status),
        "post_url": post.get("url", ""),
        "post_id": post.get("post_id", ""),
        "audio_url": audio_url,
    })
    return result


def spanish_edition(english: Dict[str, Any], *, season: int, episode: int, date_range: str,
                    args, english_post_url: str = "") -> Dict[str, Any]:
    """Adapt (or reuse) the Spanish script, then voice and publish it."""
    label = episodes.episode_label(season, episode)
    stem = "TWIF-{}-es".format(label)
    if getattr(args, "spanish_script_file", None):
        spanish = _load_script(args.spanish_script_file)
        script_file = args.spanish_script_file
    else:
        spanish = adapt_to_spanish(english, label, hosts=tuple(args.hosts), model=args.model)
        script_file = str(OUTPUT_DIR / (stem + ".json"))
        _save_script(spanish, Path(script_file))
    title = episodes.post_title(season, episode, spanish["episode_title"], language="es")
    if args.dry_run:
        return {"title": title, "script_file": script_file, "words": word_count(spanish),
                "description": spanish.get("description", ""),
                "status": "script written (dry run)"}
    result = produce(spanish, title=title, stem=stem, language="es", episode=episode,
                     date_range=date_range, args=args, other_edition_url=english_post_url)
    result["script_file"] = script_file
    return result


def _record_spanish(season: int, episode: int, result: Dict[str, Any]) -> None:
    if "post_url" not in result:
        return
    spanish = {
        "title": result["title"],
        "status": result["status"],
        "post_url": result["post_url"],
        "post_id": result["post_id"],
        "audio_url": result["audio_url"],
        "minutes": result["minutes"],
    }
    state = episodes.load_state()
    episodes.save_state(episodes.update_episode(state, season, episode, {"spanish": spanish}))


def cmd_run(args) -> int:
    info = plan(args)
    if "skip" in info:
        _emit({"status": "skipped", **info})
        return 0

    digest = Path(info["digest"])
    markdown = digest.read_text(encoding="utf-8")
    date_range = episodes.digest_range(markdown)
    season, number, label = info["season"], info["episode"], info["label"]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    script_path = OUTPUT_DIR / "TWIF-{}.json".format(label)

    if args.script_file:
        script = _load_script(args.script_file)
    else:
        script = generate_script(markdown, label, hosts=tuple(args.hosts), model=args.model)
        _save_script(script, script_path)

    title = episodes.post_title(season, number, script["episode_title"])
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
    else:
        english = produce(script, title=title, stem="TWIF-{}".format(label), language="en",
                          episode=number, date_range=date_range, args=args)
        report.update(english)
        if "post_url" in english:
            entry = {
                "season": season,
                "episode": number,
                "title": title,
                "digest": digest.name,
                "published": date.today().isoformat(),
                "status": english["status"],
                "post_url": english["post_url"],
                "post_id": english["post_id"],
                "audio_url": english["audio_url"],
                "minutes": english["minutes"],
            }
            episodes.save_state(episodes.record_episode(episodes.load_state(), entry))

    if args.no_spanish:
        _emit(report)
        return 0
    try:
        spanish = spanish_edition(script, season=season, episode=number, date_range=date_range,
                                  args=args, english_post_url=report.get("post_url", ""))
    except (PipelineError, ScriptError, OSError, ValueError, RuntimeError) as exc:
        report["spanish"] = {"error": str(exc)}
        _emit(report)
        return 2
    report["spanish"] = spanish
    if not args.dry_run:
        _record_spanish(season, number, spanish)
    _emit(report)
    return 0


def cmd_spanish(args) -> int:
    """Make (or remake) the Spanish edition of an already-published English episode."""
    state = episodes.load_state()
    entry = episodes.find_episode(state, args.episode)
    season, number = entry.get("season", state["season"]), entry["episode"]
    label = episodes.episode_label(season, number)
    english_path = args.script_file or str(OUTPUT_DIR / "TWIF-{}.json".format(label))
    if not Path(english_path).exists():
        raise PipelineError(
            "English script not found at {}. Pass --script-file (it is in the run's "
            "twif-episode artifact).".format(english_path))
    english = _load_script(english_path)
    digest = episodes.DIGEST_DIR / entry.get("digest", "")
    date_range = episodes.digest_range(digest.read_text(encoding="utf-8")) if digest.is_file() else ""
    result = spanish_edition(english, season=season, episode=number, date_range=date_range,
                             args=args, english_post_url=entry.get("post_url", ""))
    if not args.dry_run:
        _record_spanish(season, number, result)
    _emit({"season": season, "episode": number, "label": label, "spanish": result})
    return 0


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
    run.add_argument("--no-spanish", action="store_true", help="skip the Spanish edition")
    run.add_argument("--spanish-script-file",
                     help="reuse a saved Spanish script JSON instead of calling Claude")

    es = sub.add_parser("spanish", help="make the Spanish edition of a recorded episode")
    es.add_argument("--episode", type=int, help="episode number (default: latest)")
    es.add_argument("--script-file", help="English script JSON (default: podcast/output/)")
    es.add_argument("--spanish-script-file", help="reuse a saved Spanish script JSON")
    es.add_argument("--dry-run", action="store_true", help="write the Spanish script only")
    es.add_argument("--no-publish", action="store_true", help="stop after making the MP3")
    es.add_argument("--status", choices=["publish", "draft"], default="publish")
    es.add_argument("--model", default=MODEL)
    es.add_argument("--hosts", nargs=2, default=list(DEFAULT_HOSTS), metavar=("A", "B"))
    es.add_argument("--speed", type=float, default=1.0)
    es.set_defaults(voice_a=None, voice_b=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        code = {"next": cmd_next, "run": cmd_run, "spanish": cmd_spanish}[args.command](args)
    except (PipelineError, ScriptError, OSError, ValueError, RuntimeError) as exc:
        _emit({"error": str(exc)})
        sys.exit(1)
    sys.exit(code or 0)


if __name__ == "__main__":
    main()
