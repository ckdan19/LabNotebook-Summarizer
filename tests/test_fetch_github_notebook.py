"""Tests for scripts/fetch_github_notebook.py — cosmetic/substantive boundary and clip()."""

import sys
import os
import unittest

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

    def test_content_truncated_flag_set_when_clipping_occurs(self):
        # Simulate what fetch_body does with the return value of clip().
        long_text = "Line of content.\n" * 500  # ~8 500 chars
        limit = 1000
        clipped, dropped = fetch_github_notebook.clip(long_text, limit)

        post = {}
        if dropped:
            post["content_truncated"] = True
        post["content"] = clipped

        self.assertTrue(
            post.get("content_truncated"),
            "content_truncated should be True when clip() drops characters",
        )

    def test_content_truncated_not_set_for_short_post(self):
        # fetch_body only sets content_truncated when dropped > 0.
        short_text = "This is a short post.\n"
        limit = 60000
        _, dropped = fetch_github_notebook.clip(short_text, limit)

        post = {}
        if dropped:
            post["content_truncated"] = True

        self.assertFalse(
            post.get("content_truncated", False),
            "content_truncated must not be set for posts that fit within the limit",
        )


if __name__ == "__main__":
    unittest.main()
