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
# Scripts of published editions are archived here and committed with episodes.json, so a
# later retry (e.g. `podcast spanish`) never depends on an expiring CI artifact.
SCRIPT_DIR = episodes.REPO_ROOT / "podcast" / "scripts"
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


SPANISH_ERRORS = (PipelineError, ScriptError, OSError, ValueError, RuntimeError)


def make_audio(script: Dict[str, Any], *, title: str, stem: str, language: str,
               episode: int, args) -> Dict[str, Any]:
    """Voice ``script`` with Kokoro and encode it to MP3. Returns title, mp3, minutes."""
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
    return {"title": title, "mp3": str(mp3), "minutes": round(minutes, 1),
            "_minutes": minutes}


def upload_audio(audio: Dict[str, Any]) -> None:
    """Upload the MP3 to the WordPress media library; adds ``audio_url``."""
    upload = _run_json([sys.executable, str(SCRIPTS_DIR / "upload_media.py"), audio["mp3"],
                        "--title", audio["title"]])
    audio["audio_url"] = upload["url"]


def publish_post(script: Dict[str, Any], audio: Dict[str, Any], *, stem: str, language: str,
                 date_range: str, args, other_edition_url: str = "") -> None:
    """Create the WordPress post for an uploaded edition; adds status/post_url/post_id."""
    post_md = OUTPUT_DIR / (stem + "-post.md")
    post_md.write_text(
        build_post_markdown(audio["title"], script, audio["audio_url"], audio["_minutes"],
                            date_range, language=language,
                            other_edition_url=other_edition_url),
        encoding="utf-8",
    )
    try:
        post = _run_json([sys.executable, str(SCRIPTS_DIR / "publish_digest.py"), str(post_md),
                          "--category", CATEGORIES[language], "--status", args.status])
    except PipelineError as exc:
        raise PipelineError("{} (the MP3 was already uploaded: {})".format(
            exc, audio["audio_url"]))
    _save_script(script, SCRIPT_DIR / (stem + ".json"))
    audio.update({
        "status": post.get("post_status", args.status),
        "post_url": post.get("url", ""),
        "post_id": post.get("post_id", ""),
    })


def _public(result: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in result.items() if not k.startswith("_")}


def spanish_script(english: Dict[str, Any], *, season: int, episode: int, args):
    """Adapt (or reuse) the Spanish script. Returns (script, script_file)."""
    label = episodes.episode_label(season, episode)
    if getattr(args, "spanish_script_file", None):
        return _load_script(args.spanish_script_file), args.spanish_script_file
    spanish = adapt_to_spanish(english, label, hosts=tuple(args.hosts), model=args.model)
    script_file = str(OUTPUT_DIR / "TWIF-{}-es.json".format(label))
    _save_script(spanish, Path(script_file))
    return spanish, script_file


def spanish_edition(english: Dict[str, Any], *, season: int, episode: int, date_range: str,
                    args, english_post_url: str = "") -> Dict[str, Any]:
    """Make the Spanish edition on its own: script, audio, upload, post."""
    label = episodes.episode_label(season, episode)
    stem = "TWIF-{}-es".format(label)
    spanish, script_file = spanish_script(english, season=season, episode=episode, args=args)
    title = episodes.post_title(season, episode, spanish["episode_title"], language="es")
    if args.dry_run:
        return {"title": title, "script_file": script_file, "words": word_count(spanish),
                "description": spanish.get("description", ""),
                "status": "script written (dry run)"}
    audio = make_audio(spanish, title=title, stem=stem, language="es", episode=episode,
                       args=args)
    audio["script_file"] = script_file
    if args.no_publish:
        audio["status"] = "audio generated (not uploaded)"
        return _public(audio)
    upload_audio(audio)
    publish_post(spanish, audio, stem=stem, language="es", date_range=date_range, args=args,
                 other_edition_url=english_post_url)
    return _public(audio)


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
    """Both editions. Order: scripts -> both MP3s uploaded -> English post (linking the
    Spanish audio) -> Spanish post (linking the English post). A Spanish failure at any
    step leaves the English episode intact and makes the run exit 2."""
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

    # --- scripts --------------------------------------------------------------
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

    spanish: Dict[str, Any] = {}
    es_script = None
    if not args.no_spanish:
        try:
            es_script, es_file = spanish_script(script, season=season, episode=number,
                                                   args=args)
            spanish = {"title": episodes.post_title(season, number, es_script["episode_title"],
                                                    language="es"),
                       "script_file": es_file, "words": word_count(es_script)}
        except SPANISH_ERRORS as exc:
            spanish = {"error": str(exc)}

    def finish() -> int:
        if not args.no_spanish:
            report["spanish"] = _public(spanish)
        _emit(report)
        return 2 if "error" in spanish else 0

    if args.dry_run:
        report["status"] = "script written (dry run: no audio, no upload, no post)"
        report["description"] = script.get("description", "")
        if es_script is not None:
            spanish["description"] = es_script.get("description", "")
            spanish["status"] = "script written (dry run)"
        return finish()

    # --- audio (and upload) for both editions ---------------------------------
    english = make_audio(script, title=title, stem="TWIF-{}".format(label), language="en",
                         episode=number, args=args)
    if not args.no_publish:
        upload_audio(english)
    if es_script is not None:
        try:
            spanish.update(make_audio(es_script, title=spanish["title"],
                                      stem="TWIF-{}-es".format(label), language="es",
                                      episode=number, args=args))
            if not args.no_publish:
                upload_audio(spanish)
        except SPANISH_ERRORS as exc:
            spanish["error"] = str(exc)

    if args.no_publish:
        english["status"] = "audio generated (not uploaded)"
        if "mp3" in spanish and "error" not in spanish:
            spanish["status"] = "audio generated (not uploaded)"
        report.update(_public(english))
        return finish()

    # --- posts: English first, linking the Spanish audio ----------------------
    spanish_audio_url = spanish.get("audio_url", "") if "error" not in spanish else ""
    publish_post(script, english, stem="TWIF-{}".format(label), language="en",
                 date_range=date_range, args=args, other_edition_url=spanish_audio_url)
    report.update(_public(english))
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

    if "audio_url" in spanish and "error" not in spanish:
        try:
            publish_post(es_script, spanish, stem="TWIF-{}-es".format(label), language="es",
                         date_range=date_range, args=args,
                         other_edition_url=english["post_url"])
            _record_spanish(season, number, spanish)
        except SPANISH_ERRORS as exc:
            spanish["error"] = str(exc)
    return finish()


def cmd_spanish(args) -> int:
    """Make (or remake) the Spanish edition of an already-published English episode."""
    state = episodes.load_state()
    entry = episodes.find_episode(state, args.episode)
    season, number = entry.get("season", state["season"]), entry["episode"]
    label = episodes.episode_label(season, number)
    name = "TWIF-{}.json".format(label)
    candidates = [Path(args.script_file)] if args.script_file else [SCRIPT_DIR / name,
                                                                     OUTPUT_DIR / name]
    english_path = next((str(c) for c in candidates if c.exists()), None)
    if english_path is None:
        raise PipelineError(
            "English script for {} not found (looked in {}). Pass --script-file; it is in "
            "the run's twif-episode artifact.".format(label, ", ".join(map(str, candidates))))
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
    es.add_argument("--script-file",
                    help="English script JSON (default: podcast/scripts/, then podcast/output/)")
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
