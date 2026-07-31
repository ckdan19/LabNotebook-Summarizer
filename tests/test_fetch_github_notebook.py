"""Tests for scripts/fetch_github_notebook.py — cosmetic/substantive boundary and clip()."""

import sys
import os
import io
import json
import unittest
from contextlib import redirect_stdout
from datetime import datetime, timezone
from unittest.mock import patch
from urllib.error import HTTPError

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import fetch_github_notebook

COSMETIC_LINES = fetch_github_notebook.DEFAULT_COSMETIC_LINES  # 6


def _entry(additions, deletions, status="modified", filename="posts/2026-07-28-test.qmd"):
    return {
        "filename": filename,
        "status": status,
        "additions": additions,
        "deletions": deletions,
        "patch": "@@ -1,2 +1,2 @@\n-old line\n+new line",
    }


class TestCosmeticBoundary(unittest.TestCase):
    """build_post classifies a modified file as cosmetic iff additions+deletions <= cosmetic_lines."""

    def test_exactly_6_lines_is_cosmetic(self):
        post = fetch_github_notebook.build_post("owner/repo", _entry(3, 3), "abc", COSMETIC_LINES)
        self.assertEqual(post["change_class"], "cosmetic")

    def test_7_lines_is_substantive(self):
        post = fetch_github_notebook.build_post("owner/repo", _entry(4, 3), "abc", COSMETIC_LINES)
        self.assertEqual(post["change_class"], "substantive")

    def test_0_lines_is_cosmetic(self):
        post = fetch_github_notebook.build_post("owner/repo", _entry(0, 0), "abc", COSMETIC_LINES)
        self.assertEqual(post["change_class"], "cosmetic")

    def test_1_addition_is_cosmetic(self):
        post = fetch_github_notebook.build_post("owner/repo", _entry(1, 0), "abc", COSMETIC_LINES)
        self.assertEqual(post["change_class"], "cosmetic")

    def test_5_lines_is_cosmetic(self):
        post = fetch_github_notebook.build_post("owner/repo", _entry(3, 2), "abc", COSMETIC_LINES)
        self.assertEqual(post["change_class"], "cosmetic")

    def test_added_file_is_substantive_regardless_of_line_count(self):
        # A newly added file is always substantive — status != "modified"
        post = fetch_github_notebook.build_post(
            "owner/repo", _entry(2, 0, status="added"), "abc", COSMETIC_LINES
        )
        self.assertEqual(post["change_class"], "substantive")

    def test_renamed_file_is_substantive(self):
        entry = _entry(0, 0, status="renamed")
        post = fetch_github_notebook.build_post("owner/repo", entry, "abc", COSMETIC_LINES)
        self.assertEqual(post["change_class"], "substantive")

    def test_cosmetic_post_includes_patch_field(self):
        post = fetch_github_notebook.build_post("owner/repo", _entry(1, 1), "abc", COSMETIC_LINES)
        self.assertIn("patch", post)

    def test_substantive_post_omits_patch_field(self):
        post = fetch_github_notebook.build_post("owner/repo", _entry(10, 5), "abc", COSMETIC_LINES)
        self.assertNotIn("patch", post)

    def test_custom_threshold_respected(self):
        # 10 additions is substantive at default threshold (6), cosmetic at threshold 15.
        entry = _entry(10, 0)
        at_default = fetch_github_notebook.build_post("owner/repo", entry, "abc", COSMETIC_LINES)
        at_generous = fetch_github_notebook.build_post("owner/repo", entry, "abc", 15)
        self.assertEqual(at_default["change_class"], "substantive")
        self.assertEqual(at_generous["change_class"], "cosmetic")

    def test_blob_url_contains_sha_and_path(self):
        entry = _entry(1, 0, filename="posts/my-post.qmd")
        post = fetch_github_notebook.build_post("owner/repo", entry, "deadbeef", COSMETIC_LINES)
        self.assertIn("deadbeef", post["blob_url"])
        self.assertIn("posts/my-post.qmd", post["blob_url"])

    def test_previous_filename_included_when_present(self):
        entry = _entry(0, 0, status="renamed")
        entry["previous_filename"] = "posts/old-name.qmd"
        post = fetch_github_notebook.build_post("owner/repo", entry, "abc", COSMETIC_LINES)
        self.assertEqual(post["previous_filename"], "posts/old-name.qmd")


class TestClip(unittest.TestCase):
    """clip() keeps the head and tail of a post so front matter and conclusions survive."""

    def test_short_text_returned_unchanged(self):
        text = "Short post content."
        result, dropped = fetch_github_notebook.clip(text, limit=1000)
        self.assertEqual(result, text)
        self.assertEqual(dropped, 0)

    def test_text_exactly_at_limit_not_clipped(self):
        text = "x" * 100
        result, dropped = fetch_github_notebook.clip(text, limit=100)
        self.assertEqual(result, text)
        self.assertEqual(dropped, 0)

    def test_text_one_over_limit_is_clipped(self):
        text = "x" * 101
        result, dropped = fetch_github_notebook.clip(text, limit=100)
        self.assertGreater(dropped, 0)

    def test_front_matter_survives_clipping(self):
        front_matter = "---\ntitle: Important Post\ndate: 2026-07-28\nauthor: Lab\n---\n"
        body = "B" * 10000
        conclusion = "\n## Conclusions\nResults were significant.\n"
        full_text = front_matter + body + conclusion

        limit = 500
        result, dropped = fetch_github_notebook.clip(full_text, limit)

        self.assertGreater(dropped, 0)
        # Head (70% of limit = 350 chars) must contain the front matter (~60 chars)
        self.assertTrue(
            result.startswith(front_matter[:40]),
            f"Front matter not at start of clipped result: {result[:80]!r}",
        )

    def test_conclusion_survives_clipping(self):
        front_matter = "---\ntitle: My Post\n---\n"
        body = "C" * 10000
        conclusion = "Final conclusion: this experiment showed positive results."
        full_text = front_matter + body + conclusion

        limit = 500
        result, dropped = fetch_github_notebook.clip(full_text, limit)

        self.assertGreater(dropped, 0)
        # Tail (30% of limit = 150 chars) must contain the conclusion (~57 chars)
        self.assertTrue(
            result.endswith(conclusion[-40:]),
            f"Conclusion not at end of clipped result: {result[-80:]!r}",
        )

    def test_omission_marker_present_when_clipped(self):
        text = "A" * 10000
        result, dropped = fetch_github_notebook.clip(text, limit=100)
        self.assertIn("characters omitted from the middle", result)
        self.assertIn(str(dropped), result)

    def test_dropped_count_accurate(self):
        text = "x" * 1000
        limit = 100
        _, dropped = fetch_github_notebook.clip(text, limit)
        self.assertEqual(dropped, 900)

    def test_70_30_head_tail_split(self):
        # First 100 chars are A, second 100 chars are B; limit=100.
        # head = int(100 * 0.7) = 70 chars of A, tail = 30 chars of B.
        text = "A" * 100 + "B" * 100
        result, dropped = fetch_github_notebook.clip(text, limit=100)
        self.assertTrue(result.startswith("A" * 70))
        self.assertTrue(result.endswith("B" * 30))


class TestChangedFiles(unittest.TestCase):
    """The compare call must span the whole window and flag incomplete results."""

    @staticmethod
    def _commit(sha, parents=None):
        return {"sha": sha, "parents": parents if parents is not None else []}

    def _run(self, commits, response):
        seen = {}

        def fake_get_json(url, timeout):
            seen["url"] = url
            return response

        with patch("fetch_github_notebook.get_json", side_effect=fake_get_json):
            files, warnings = fetch_github_notebook.changed_files("owner/repo", commits, 20)
        return files, warnings, seen["url"]

    def test_base_is_first_parent_of_oldest_commit(self):
        # commits are newest-first, so the range must run parent-of-oldest -> newest.
        commits = [self._commit("newsha"), self._commit("oldsha", [{"sha": "parentsha"}])]
        _, warnings, url = self._run(commits, {"status": "ahead", "files": []})
        self.assertIn("compare/parentsha...newsha", url)
        self.assertEqual(warnings, [])

    def test_root_commit_without_parents_compares_against_itself(self):
        commits = [self._commit("onlysha", [])]
        _, warnings, url = self._run(commits, {"status": "identical", "files": []})
        self.assertIn("compare/onlysha...onlysha", url)
        self.assertEqual(warnings, [])

    def test_identical_status_produces_no_warning(self):
        commits = [self._commit("a"), self._commit("b", [{"sha": "c"}])]
        _, warnings, _ = self._run(commits, {"status": "identical", "files": []})
        self.assertEqual(warnings, [])

    def test_missing_status_produces_no_warning(self):
        commits = [self._commit("a"), self._commit("b", [{"sha": "c"}])]
        _, warnings, _ = self._run(commits, {"files": []})
        self.assertEqual(warnings, [])

    def test_diverged_status_warns_about_rewritten_history(self):
        commits = [self._commit("a"), self._commit("b", [{"sha": "c"}])]
        _, warnings, _ = self._run(commits, {"status": "diverged", "files": []})
        self.assertEqual(len(warnings), 1)
        self.assertIn("rewritten", warnings[0])

    def test_300_file_cap_warns(self):
        commits = [self._commit("a"), self._commit("b", [{"sha": "c"}])]
        files = [{"filename": "posts/p%d.qmd" % i} for i in range(300)]
        returned, warnings, _ = self._run(commits, {"status": "ahead", "files": files})
        self.assertEqual(len(returned), 300)
        self.assertEqual(len(warnings), 1)
        self.assertIn("300 files", warnings[0])

    def test_299_files_does_not_warn(self):
        commits = [self._commit("a"), self._commit("b", [{"sha": "c"}])]
        files = [{"filename": "posts/p%d.qmd" % i} for i in range(299)]
        _, warnings, _ = self._run(commits, {"status": "ahead", "files": files})
        self.assertEqual(warnings, [])

    def test_missing_files_key_returns_empty_list(self):
        commits = [self._commit("a"), self._commit("b", [{"sha": "c"}])]
        files, warnings, _ = self._run(commits, {"status": "ahead"})
        self.assertEqual(files, [])


class TestRateLimitMessage(unittest.TestCase):

    @staticmethod
    def _error(code, remaining=None, reset=None):
        headers = {}
        if remaining is not None:
            headers["X-RateLimit-Remaining"] = remaining
        if reset is not None:
            headers["X-RateLimit-Reset"] = reset
        return HTTPError("https://api.github.com/x", code, "Forbidden", headers, None)

    def test_non_rate_limit_status_returns_empty(self):
        self.assertEqual(fetch_github_notebook.rate_limit_message(self._error(404)), "")

    def test_403_with_requests_remaining_returns_empty(self):
        # A 403 with budget left is a permissions problem, not a rate limit.
        err = self._error(403, remaining="42")
        self.assertEqual(fetch_github_notebook.rate_limit_message(err), "")

    def test_403_exhausted_returns_message(self):
        err = self._error(403, remaining="0")
        with patch.dict(os.environ, {}, clear=True):
            message = fetch_github_notebook.rate_limit_message(err)
        self.assertIn("rate limit", message.lower())

    def test_429_exhausted_returns_message(self):
        err = self._error(429, remaining="0")
        with patch.dict(os.environ, {}, clear=True):
            message = fetch_github_notebook.rate_limit_message(err)
        self.assertIn("rate limit", message.lower())

    def test_unauthenticated_hint_mentions_github_token(self):
        err = self._error(403, remaining="0")
        with patch.dict(os.environ, {}, clear=True):
            message = fetch_github_notebook.rate_limit_message(err)
        self.assertIn("GITHUB_TOKEN", message)

    def test_authenticated_hint_says_limit_exhausted(self):
        err = self._error(403, remaining="0")
        with patch.dict(os.environ, {"GITHUB_TOKEN": "tok"}, clear=True):
            message = fetch_github_notebook.rate_limit_message(err)
        self.assertIn("5,000/hour is exhausted", message)
        self.assertNotIn("set GITHUB_TOKEN", message)

    def test_reset_timestamp_rendered_as_utc_clock_time(self):
        # 2026-07-30T18:30:00Z
        reset = str(int(datetime(2026, 7, 30, 18, 30, tzinfo=timezone.utc).timestamp()))
        err = self._error(403, remaining="0", reset=reset)
        with patch.dict(os.environ, {}, clear=True):
            message = fetch_github_notebook.rate_limit_message(err)
        self.assertIn("resets 18:30 UTC", message)

    def test_non_numeric_reset_omits_clock_time(self):
        err = self._error(403, remaining="0", reset="soon")
        with patch.dict(os.environ, {}, clear=True):
            message = fetch_github_notebook.rate_limit_message(err)
        self.assertNotIn("resets", message)


class TestHeaders(unittest.TestCase):

    def test_no_token_omits_authorization(self):
        with patch.dict(os.environ, {}, clear=True):
            h = fetch_github_notebook.headers()
        self.assertNotIn("Authorization", h)
        self.assertIn("User-Agent", h)
        self.assertIn("Accept", h)

    def test_github_token_becomes_bearer(self):
        with patch.dict(os.environ, {"GITHUB_TOKEN": "abc"}, clear=True):
            h = fetch_github_notebook.headers()
        self.assertEqual(h["Authorization"], "Bearer abc")

    def test_gh_token_used_as_fallback(self):
        with patch.dict(os.environ, {"GH_TOKEN": "xyz"}, clear=True):
            h = fetch_github_notebook.headers()
        self.assertEqual(h["Authorization"], "Bearer xyz")

    def test_github_token_takes_precedence(self):
        with patch.dict(os.environ, {"GITHUB_TOKEN": "abc", "GH_TOKEN": "xyz"}, clear=True):
            h = fetch_github_notebook.headers()
        self.assertEqual(h["Authorization"], "Bearer abc")


class TestMainPostSelection(unittest.TestCase):
    """End-to-end over main(): path matching, body fetching, and truncation."""

    def _run_main(self, files, bodies, extra_args=(), notebook="tumbling-oysters"):
        commits = [{"sha": "headsha", "parents": [{"sha": "p"}]}]
        fetched = []

        def fake_get_text(url, timeout):
            fetched.append(url)
            for path, text in bodies.items():
                if url.endswith(path):
                    return text
            raise AssertionError("unexpected body fetch: %s" % url)

        argv = ["fetch_github_notebook.py", "--notebook", notebook] + list(extra_args)
        captured = io.StringIO()
        with patch.object(sys, "argv", argv), \
                patch("fetch_github_notebook.list_commits", return_value=commits), \
                patch("fetch_github_notebook.changed_files", return_value=(files, [])), \
                patch("fetch_github_notebook.get_text", side_effect=fake_get_text):
            with redirect_stdout(captured):
                fetch_github_notebook.main()

        return json.loads(captured.getvalue()), fetched

    def test_only_prefix_and_suffix_matches_become_posts(self):
        files = [
            _entry(10, 0, filename="posts/real-post.qmd"),
            _entry(10, 0, filename="README.md"),
            _entry(10, 0, filename="posts/notes.txt"),
            _entry(10, 0, filename="docs/other.qmd"),
        ]
        result, _ = self._run_main(files, {"posts/real-post.qmd": "Body text."})
        self.assertEqual([p["path"] for p in result["posts"]], ["posts/real-post.qmd"])

    def test_index_suffix_notebook_rejects_flat_post_files(self):
        # The "sams" notebook pins posts to a folder's index.qmd.
        files = [
            _entry(10, 0, filename="posts/2026-07-28-thing/index.qmd"),
            _entry(10, 0, filename="posts/flat.qmd"),
        ]
        result, _ = self._run_main(
            files,
            {"posts/2026-07-28-thing/index.qmd": "Body."},
            notebook="sams",
        )
        self.assertEqual(
            [p["path"] for p in result["posts"]], ["posts/2026-07-28-thing/index.qmd"]
        )

    def test_removed_post_is_skipped_with_warning_and_no_body_fetch(self):
        files = [
            _entry(0, 20, status="removed", filename="posts/gone.qmd"),
            _entry(10, 0, filename="posts/stays.qmd"),
        ]
        result, fetched = self._run_main(files, {"posts/stays.qmd": "Body."})

        self.assertEqual([p["path"] for p in result["posts"]], ["posts/stays.qmd"])
        self.assertTrue(any("gone.qmd" in w and "deleted" in w for w in result["warnings"]))
        # A deleted file has no body at the head SHA — fetching it would 404.
        self.assertFalse(any("gone.qmd" in url for url in fetched))

    def test_posts_sorted_by_path(self):
        files = [
            _entry(10, 0, filename="posts/zebra.qmd"),
            _entry(10, 0, filename="posts/alpha.qmd"),
        ]
        bodies = {"posts/zebra.qmd": "Z.", "posts/alpha.qmd": "A."}
        result, _ = self._run_main(files, bodies)
        self.assertEqual(
            [p["path"] for p in result["posts"]], ["posts/alpha.qmd", "posts/zebra.qmd"]
        )

    def test_body_is_read_at_head_sha(self):
        files = [_entry(10, 0, filename="posts/p.qmd")]
        _, fetched = self._run_main(files, {"posts/p.qmd": "Body."})
        self.assertEqual(len(fetched), 1)
        self.assertIn("/headsha/", fetched[0])

    def test_short_post_is_not_truncated(self):
        files = [_entry(10, 0, filename="posts/p.qmd")]
        result, _ = self._run_main(files, {"posts/p.qmd": "Short body."})
        post = result["posts"][0]
        self.assertEqual(post["content"], "Short body.")
        self.assertNotIn("content_truncated", post)
        self.assertEqual(result["warnings"], [])

    def test_long_substantive_post_is_clipped_and_warns(self):
        body = "HEAD-MARKER" + ("x" * 5000) + "TAIL-MARKER"
        files = [_entry(50, 0, filename="posts/p.qmd")]
        result, _ = self._run_main(
            files, {"posts/p.qmd": body}, extra_args=["--max-chars", "1000"]
        )

        post = result["posts"][0]
        self.assertTrue(post["content_truncated"])
        self.assertTrue(post["content"].startswith("HEAD-MARKER"))
        self.assertTrue(post["content"].endswith("TAIL-MARKER"))
        self.assertTrue(
            any("omitted from the middle" in w for w in result["warnings"]),
            result["warnings"],
        )

    def test_cosmetic_post_uses_tighter_cap_without_warning(self):
        # 5,000 chars fits the 60,000 substantive cap but not the 4,000 cosmetic one.
        body = "y" * 5000
        cosmetic = _entry(1, 0, filename="posts/tweak.qmd")
        result, _ = self._run_main([cosmetic], {"posts/tweak.qmd": body})

        post = result["posts"][0]
        self.assertEqual(post["change_class"], "cosmetic")
        self.assertTrue(post["content_truncated"])
        # Only substantive truncation is worth a warning — a trimmed link fix is not.
        self.assertEqual(result["warnings"], [])

    def test_substantive_post_of_same_size_is_not_truncated(self):
        body = "y" * 5000
        substantive = _entry(50, 0, filename="posts/real.qmd")
        result, _ = self._run_main([substantive], {"posts/real.qmd": body})

        post = result["posts"][0]
        self.assertEqual(post["change_class"], "substantive")
        self.assertNotIn("content_truncated", post)

    def test_no_commits_returns_empty_posts_without_fetching(self):
        captured = io.StringIO()
        argv = ["fetch_github_notebook.py", "--notebook", "tumbling-oysters"]
        with patch.object(sys, "argv", argv), \
                patch("fetch_github_notebook.list_commits", return_value=[]), \
                patch("fetch_github_notebook.get_text",
                      side_effect=AssertionError("must not fetch bodies")):
            with redirect_stdout(captured):
                fetch_github_notebook.main()

        result = json.loads(captured.getvalue())
        self.assertEqual(result["posts"], [])
        self.assertEqual(result["commits_scanned"], 0)

    def test_rate_limit_error_exits_with_actionable_message(self):
        error = HTTPError(
            "https://api.github.com/x", 403, "Forbidden",
            {"X-RateLimit-Remaining": "0"}, None,
        )
        captured = io.StringIO()
        argv = ["fetch_github_notebook.py", "--notebook", "tumbling-oysters"]
        with patch.object(sys, "argv", argv), \
                patch("fetch_github_notebook.list_commits", side_effect=error), \
                patch.dict(os.environ, {}, clear=True):
            with redirect_stdout(captured):
                with self.assertRaises(SystemExit) as ctx:
                    fetch_github_notebook.main()

        self.assertEqual(ctx.exception.code, 1)
        result = json.loads(captured.getvalue())
        self.assertIn("rate limit", result["error"].lower())


if __name__ == "__main__":
    unittest.main()
