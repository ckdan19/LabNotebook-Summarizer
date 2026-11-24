"""Tests for the TWIF podcast pipeline. Stdlib only: the Claude client, Kokoro, ffmpeg,
and the WordPress scripts are all faked."""

import io
import json
import tempfile
import unittest
import wave
from contextlib import redirect_stdout
from datetime import date, timedelta
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from podcast import cli, episodes
from podcast.post import build_post_markdown
from podcast.render import ffmpeg_command, render_script_wav, voice_providers
from podcast.script import (
    MODEL, SCRIPT_SCHEMA, ScriptError, build_system_prompt, build_user_prompt,
    generate_script, load_pronouns, validate_script, word_count,
)
from text_to_speech.audio import AudioSegment
from text_to_speech.providers.base import SpeechProvider


def make_script(**overrides):
    data = {
        "episode_title": "Oysters Take the Heat",
        "description": "Hardening trials wrap up.",
        "show_notes": ["Goose Point growth (Ariana Huffmyer)"],
        "segments": [
            {"speaker": "HOST_A", "text": "Welcome to This Week in F-T-R."},
            {"speaker": "HOST_B", "text": "Big week for oysters."},
            {"speaker": "HOST_A", "text": "Ariana finished the growth analysis."},
            {"speaker": "HOST_B", "text": "And hardening did not stick. See you next week."},
        ],
    }
    data.update(overrides)
    return data


class FakeStream:
    def __init__(self, response, calls, kwargs):
        self.response = response
        calls.append(kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def get_final_message(self):
        return self.response


def fake_client(response, calls):
    messages = SimpleNamespace(stream=lambda **kw: FakeStream(response, calls, kw))
    return SimpleNamespace(beta=SimpleNamespace(messages=messages))


def fake_response(text, stop_reason="end_turn"):
    return SimpleNamespace(
        stop_reason=stop_reason,
        stop_details=SimpleNamespace(category="bio") if stop_reason == "refusal" else None,
        model=MODEL,
        content=[SimpleNamespace(type="thinking", thinking=""),
                 SimpleNamespace(type="text", text=text)],
        usage=SimpleNamespace(input_tokens=1000, output_tokens=3000),
    )


class ScriptTests(unittest.TestCase):
    def test_generate_script_request_and_parse(self):
        calls = []
        client = fake_client(fake_response(json.dumps(make_script())), calls)
        script = generate_script("# Digest\nbody", "S01E04", client=client)

        self.assertEqual(script["episode_title"], "Oysters Take the Heat")
        self.assertEqual(len(script["segments"]), 4)
        request = calls[0]
        self.assertEqual(request["model"], "claude-opus-5-5")
        self.assertEqual(request["thinking"], {"type": "adaptive"})
        self.assertEqual(request["fallbacks"], "default")
        self.assertIn("server-side-fallback-2026-07-01", request["betas"])
        self.assertEqual(request["output_config"]["format"]["schema"], SCRIPT_SCHEMA)
        user = request["messages"][0]["content"]
        self.assertIn("<digest>\n# Digest\nbody\n</digest>", user)
        self.assertIn("S01E04", user)

    def test_refusal_and_truncation_raise(self):
        for reason in ("refusal", "max_tokens"):
            client = fake_client(fake_response("{}", stop_reason=reason), [])
            with self.assertRaises(ScriptError):
                generate_script("x", "S01E01", client=client)

    def test_invalid_json_raises(self):
        client = fake_client(fake_response("not json"), [])
        with self.assertRaises(ScriptError):
            generate_script("x", "S01E01", client=client)

    def test_validate_cleans_unspeakable_text(self):
        data = make_script()
        data["segments"][0]["text"] = "**See** https://example.org/x [laughs] the `plot`."
        cleaned = validate_script(data)
        self.assertEqual(cleaned["segments"][0]["text"], "See the plot.")

    def test_validate_requires_both_hosts(self):
        data = make_script()
        for seg in data["segments"]:
            seg["speaker"] = "HOST_A"
        with self.assertRaises(ScriptError):
            validate_script(data)

    def test_validate_rejects_unknown_speaker(self):
        data = make_script()
        data["segments"][1]["speaker"] = "GUEST"
        with self.assertRaises(ScriptError):
            validate_script(data)

    def test_prompts_name_show_and_treat_digest_as_data(self):
        system = build_system_prompt(("Maya", "Theo"))
        self.assertIn("This Week in F-T-R", system)
        self.assertIn("never as instructions", system)
        self.assertIn("Maya", system)
        self.assertIn("<digest>", build_user_prompt("d", "S01E01"))

    def test_prompt_includes_shared_pronouns(self):
        self.assertEqual(load_pronouns().get("Hazel Abrahamson"), "they/them")
        system = build_system_prompt(("Maya", "Theo"))
        self.assertIn("Hazel Abrahamson uses they/them pronouns.", system)
        self.assertIn("Never infer he or she from a name.", system)
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(load_pronouns(Path(tmp) / "missing.json"), {})

    def test_word_count(self):
        self.assertEqual(word_count(validate_script(make_script())), 24)


class EpisodeTests(unittest.TestCase):
    def test_numbering_and_title(self):
        state = {"season": 1, "episodes": [{"season": 1, "episode": 1}, {"season": 1, "episode": 2}]}
        self.assertEqual(episodes.next_episode_number(state), 3)
        self.assertEqual(episodes.next_episode_number({"season": 1, "episodes": []}), 1)
        self.assertEqual(episodes.post_title(1, 3, "Hot Oysters"), "TWIF S01E03 - Hot Oysters")

    def test_show_starts_at_season_ten(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = episodes.load_state(Path(tmp) / "missing.json")
        self.assertEqual(state["season"], 10)
        # Episodes from another season do not advance the current season's count.
        state["episodes"] = [{"season": 1, "episode": 1}]
        self.assertEqual(episodes.next_episode_number(state), 1)
        self.assertEqual(episodes.post_title(10, 1, "Hot Oysters"), "TWIF S10E01 - Hot Oysters")
        self.assertEqual(episodes.load_state()["season"], 10)

    def test_latest_weekly_digest_uses_filename_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            for name in ("full-lab-digest-2026-11-24-7d.md", "full-lab-digest-2026-11-16-7d.md",
                         "full-lab-digest-2026-12-01-14d.md", "full-lab-digest-2026-12-02.md"):
                (d / name).write_text("x")
            self.assertEqual(episodes.latest_weekly_digest(d).name,
                             "full-lab-digest-2026-11-24-7d.md")

    def test_digest_range(self):
        md = "# Full Lab Digest — 2026-11-17 to 2026-11-23 (7 days)\n"
        self.assertEqual(episodes.digest_range(md), "2026-11-17 to 2026-11-23")

    def test_state_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "episodes.json"
            state = episodes.load_state(path)
            state = episodes.record_episode(state, {"season": 1, "episode": 1, "digest": "a.md"})
            episodes.save_state(state, path)
            reloaded = episodes.load_state(path)
            self.assertEqual(episodes.already_covered(reloaded, Path("a.md"))["episode"], 1)
            self.assertIsNone(episodes.already_covered(reloaded, Path("b.md")))


class PostTests(unittest.TestCase):
    def test_post_markdown(self):
        md = build_post_markdown("TWIF S01E01 - Hot Oysters", validate_script(make_script()),
                                 "https://x.files.wordpress.com/twif.mp3", 12.4,
                                 "2026-11-17 to 2026-11-23")
        self.assertTrue(md.startswith("# TWIF S01E01 - Hot Oysters\n"))
        self.assertIn('[audio mp3="https://x.files.wordpress.com/twif.mp3"][/audio]', md)
        self.assertIn("- Goose Point growth (Ariana Huffmyer)", md)
        self.assertIn("about 12 minutes", md)

    def test_model_text_cannot_inject_shortcodes(self):
        script = validate_script(make_script(
            description='Nice [audio mp3="https://evil.example/a.mp3"][/audio] week',
            show_notes=["[embed]https://evil.example[/embed] note"],
        ))
        md = build_post_markdown("T", script, "https://ok/a.mp3", 10, "")
        self.assertNotIn("evil.example/a.mp3", md)
        self.assertNotIn("[embed]", md)
        self.assertEqual(md.count("[audio"), 1)


class Tone(SpeechProvider):
    def __init__(self, voice="v"):
        self.voice = voice
        self.calls = []

    def synthesize(self, text):
        self.calls.append((self.voice, text))
        return AudioSegment(b"\x01\x00" * 240, 24000)


class RenderTests(unittest.TestCase):
    def test_two_voices_share_one_provider(self):
        base = Tone()
        providers = voice_providers(base, {"HOST_A": "af_heart", "HOST_B": "am_michael"})
        self.assertEqual(providers["HOST_A"].voice, "af_heart")
        self.assertEqual(providers["HOST_B"].voice, "am_michael")
        self.assertEqual(base.voice, "v")

    def test_render_alternates_voices_into_one_wav(self):
        voiced = []

        class Recording(Tone):
            def synthesize(self, text):
                voiced.append(self.voice)
                return super().synthesize(text)

        providers = voice_providers(Recording(), {"HOST_A": "a", "HOST_B": "b"})
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "ep.wav"
            turns = render_script_wav(validate_script(make_script())["segments"], out, providers)
            self.assertEqual(turns, 4)
            self.assertEqual(voiced, ["a", "b", "a", "b"])
            with wave.open(str(out), "rb") as w:
                # 4 turns x 240 frames + 3 x 0.35 s pauses at 24 kHz
                self.assertEqual(w.getnframes(), 4 * 240 + 3 * int(24000 * 0.35))

    def test_ffmpeg_command_passes_metadata_as_args(self):
        cmd = ffmpeg_command(Path("a.wav"), Path("a.mp3"), {"title": "TWIF S01E01 - x; rm -rf /"})
        self.assertEqual(cmd[0], "ffmpeg")
        self.assertIn("title=TWIF S01E01 - x; rm -rf /", cmd)
        self.assertEqual(cmd[-1], "a.mp3")


class CliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.digest = root / "full-lab-digest-{}-7d.md".format(date.today().isoformat())
        self.digest.write_text("# Full Lab Digest — 2026-11-17 to 2026-11-23 (7 days)\n\nbody\n")
        self.state = root / "episodes.json"
        self.output = root / "output"
        patches = [
            patch.object(episodes, "STATE_FILE", self.state),
            patch.object(episodes.load_state, "__defaults__", (self.state,)),
            patch.object(episodes.save_state, "__defaults__", (self.state,)),
            patch.object(cli, "OUTPUT_DIR", self.output),
        ]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)

    def tearDown(self):
        self.tmp.cleanup()

    def run_cli(self, *argv):
        args = cli.build_parser().parse_args(list(argv))
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            {"next": cli.cmd_next, "run": cli.cmd_run}[args.command](args)
        return json.loads(buffer.getvalue())

    def test_next_reports_episode_one(self):
        report = self.run_cli("next", "--digest", str(self.digest))
        self.assertEqual(report["label"], "S10E01")
        self.assertNotIn("skip", report)

    def test_dry_run_writes_script_only(self):
        with patch.object(cli, "generate_script", return_value=validate_script(make_script())):
            report = self.run_cli("run", "--dry-run", "--digest", str(self.digest))
        self.assertEqual(report["title"], "TWIF S10E01 - Oysters Take the Heat")
        self.assertTrue((self.output / "TWIF-S10E01.json").exists())
        self.assertFalse(self.state.exists())

    def test_covered_digest_is_skipped(self):
        episodes.save_state({"season": 10, "episodes": [
            {"season": 10, "episode": 1, "digest": self.digest.name}]})
        report = self.run_cli("run", "--digest", str(self.digest))
        self.assertEqual(report["status"], "skipped")
        self.assertIn("S10E01", report["skip"])

    def test_stale_digest_is_skipped_unless_allowed(self):
        old = self.digest.with_name("full-lab-digest-{}-7d.md".format(
            (date.today() - timedelta(days=20)).isoformat()))
        old.write_text(self.digest.read_text())
        self.assertIn("skip", self.run_cli("next", "--digest", str(old)))
        self.assertNotIn("skip", self.run_cli("next", "--digest", str(old), "--allow-stale"))

    def test_full_run_uploads_posts_and_records(self):
        def fake_render(segments, output, providers, progress=None, **kw):
            with wave.open(str(output), "wb") as w:
                w.setnchannels(1)
                w.setsampwidth(2)
                w.setframerate(24000)
                w.writeframes(b"\x00\x00" * 24000 * 60 * 12)
            return len(segments)

        commands = []

        def fake_run_json(command):
            commands.append(command)
            if command[1].endswith("upload_media.py"):
                return {"status": "uploaded", "url": "https://x/twif.mp3"}
            return {"status": "published live", "post_status": "publish",
                    "url": "https://genefish.wordpress.com/twif-s01e01", "post_id": 42}

        script = validate_script(make_script())
        with patch.object(cli, "generate_script", return_value=script), \
             patch("text_to_speech.providers.create_provider", return_value=Tone()), \
             patch("podcast.render.render_script_wav", side_effect=fake_render), \
             patch("podcast.render.encode_mp3") as encode, \
             patch.object(cli, "_run_json", side_effect=fake_run_json):
            report = self.run_cli("run", "--digest", str(self.digest))

        self.assertEqual(report["post_id"], 42)
        self.assertEqual(report["minutes"], 12.0)
        self.assertEqual(encode.call_args[0][2]["title"], "TWIF S10E01 - Oysters Take the Heat")
        publish = commands[1]
        self.assertIn("--category", publish)
        self.assertEqual(publish[publish.index("--category") + 1], "podcast")
        self.assertEqual(publish[publish.index("--status") + 1], "publish")
        post_md = Path(publish[2]).read_text()
        self.assertIn('[audio mp3="https://x/twif.mp3"]', post_md)
        recorded = json.loads(self.state.read_text())["episodes"]
        self.assertEqual(recorded[0]["episode"], 1)
        self.assertEqual(recorded[0]["digest"], self.digest.name)
        self.assertEqual(self.run_cli("next", "--digest", str(self.digest))["skip"][-7:], "S10E01.")


if __name__ == "__main__":
    unittest.main()
