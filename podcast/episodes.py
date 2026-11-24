"""Episode numbering, digest selection, and the committed episode log."""

import json
import re
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = REPO_ROOT / "podcast" / "episodes.json"
DIGEST_DIR = REPO_ROOT / "digests"
SEASON = 10  # the show started at season 10

DIGEST_NAME_RE = re.compile(r"^full-lab-digest-(\d{4}-\d{2}-\d{2})-7d\.md$")


def load_state(path: Path = STATE_FILE) -> Dict[str, Any]:
    if not path.exists():
        return {"season": SEASON, "episodes": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("season", SEASON)
    data.setdefault("episodes", [])
    return data


def save_state(state: Dict[str, Any], path: Path = STATE_FILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def next_episode_number(state: Dict[str, Any]) -> int:
    season = state.get("season", SEASON)
    numbers = [e["episode"] for e in state["episodes"] if e.get("season", season) == season]
    return max(numbers, default=0) + 1


def episode_label(season: int, episode: int) -> str:
    return "S{:02d}E{:02d}".format(season, episode)


def post_title(season: int, episode: int, catchy: str, language: str = "en") -> str:
    marker = " (Español)" if language == "es" else ""
    return "TWIF {}{} - {}".format(episode_label(season, episode), marker, catchy)


def find_episode(state: Dict[str, Any], episode: Optional[int] = None) -> Dict[str, Any]:
    """The entry for ``episode`` in the current season, or the latest one."""
    season = state.get("season", SEASON)
    entries = [e for e in state["episodes"] if e.get("season", season) == season]
    if episode is not None:
        entries = [e for e in entries if e.get("episode") == episode]
    if not entries:
        raise ValueError("No recorded episode {}in season {}.".format(
            "{} ".format(episode) if episode is not None else "", season))
    return max(entries, key=lambda e: e["episode"])


def update_episode(state: Dict[str, Any], season: int, episode: int,
                   changes: Dict[str, Any]) -> Dict[str, Any]:
    episodes = [
        {**e, **changes} if e.get("season") == season and e.get("episode") == episode else e
        for e in state["episodes"]
    ]
    return {**state, "episodes": episodes}


def digest_date(path: Path) -> Optional[date]:
    match = DIGEST_NAME_RE.match(path.name)
    return date.fromisoformat(match.group(1)) if match else None


def latest_weekly_digest(directory: Path = DIGEST_DIR) -> Optional[Path]:
    """Newest 7-day full lab digest, by the date in its filename."""
    dated = [(digest_date(p), p) for p in directory.glob("full-lab-digest-*-7d.md")]
    dated = [(d, p) for d, p in dated if d is not None]
    return max(dated)[1] if dated else None


def already_covered(state: Dict[str, Any], digest: Path) -> Optional[Dict[str, Any]]:
    for entry in state["episodes"]:
        if entry.get("digest") == digest.name:
            return entry
    return None


def digest_range(markdown: str) -> str:
    """Return the human date range from the digest's H1, or '' if absent."""
    first = markdown.lstrip().splitlines()[0] if markdown.strip() else ""
    match = re.search(r"(\d{4}-\d{2}-\d{2}\s+to\s+\d{4}-\d{2}-\d{2})", first)
    return match.group(1) if match else ""


def record_episode(state: Dict[str, Any], entry: Dict[str, Any]) -> Dict[str, Any]:
    episodes: List[Dict[str, Any]] = list(state["episodes"])
    episodes.append(entry)
    return {**state, "episodes": episodes}
