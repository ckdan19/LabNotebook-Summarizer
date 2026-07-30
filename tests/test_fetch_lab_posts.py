"""Tests for scripts/fetch_lab_posts.py — strip_html, parse_date, and paging logic."""

import sys
import os
import unittest
from datetime import datetime, timezone, timedelta
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import fetch_lab_posts


class TestStripHtml(unittest.TestCase):

    def test_script_tag_body_removed(self):
        raw = '<p>Before</p><script>alert("xss")</script><p>After</p>'
        result = fetch_lab_posts.strip_html(raw)
        self.assertNotIn("alert", result)
        self.assertNotIn("xss", result)
        self.assertIn("Before", result)
        self.assertIn("After", result)

    def test_style_tag_body_removed(self):
        raw = "<p>Text</p><style>body { color: red; display: none }</style>"
        result = fetch_lab_posts.strip_html(raw)
        self.assertNotIn("color", result)
        self.assertNotIn("display", result)
        self.assertIn("Text", result)

    def test_multiline_script_removed(self):
        raw = '<script type="text/javascript">\nvar x = 1;\nvar y = 2;\n</script><p>Content</p>'
        result = fetch_lab_posts.strip_html(raw)
        self.assertNotIn("var x", result)
        self.assertIn("Content", result)

    def test_html_entity_amp_unescaped(self):
        raw = "<p>Fish &amp; Chips</p>"
        result = fetch_lab_posts.strip_html(raw)
        self.assertIn("Fish & Chips", result)

    def test_lt_gt_entities_unescaped(self):
        # &lt;div&gt; is literal text, not an HTML tag — should survive as <div>
        raw = "<p>&lt;div&gt; is an HTML element</p>"
        result = fetch_lab_posts.strip_html(raw)
        self.assertIn("<div>", result)
        self.assertIn("HTML element", result)

    def test_numeric_entity_unescaped(self):
        raw = "<p>Quoted: &#34;hello&#34;</p>"
        result = fetch_lab_posts.strip_html(raw)
        self.assertIn('"hello"', result)

    def test_regular_tags_stripped_content_kept(self):
        raw = "<p><strong>bold</strong> and <em>italic</em></p>"
        result = fetch_lab_posts.strip_html(raw)
        self.assertIn("bold", result)
        self.assertIn("italic", result)
        # No HTML tags should remain
        self.assertNotIn("<", result)

    def test_entity_unescaping_happens_after_tag_removal(self):
        # &lt;br&gt; in plain text should become <br> after unescaping,
        # not get stripped as though it were a real tag.
        raw = "The tag &lt;br&gt; forces a line break."
        result = fetch_lab_posts.strip_html(raw)
        self.assertIn("<br>", result)

    def test_empty_string_returns_empty(self):
        self.assertEqual(fetch_lab_posts.strip_html(""), "")

    def test_none_returns_empty(self):
        self.assertEqual(fetch_lab_posts.strip_html(None), "")

    def test_whitespace_normalized(self):
        raw = "<p>One  \n  Two</p>"
        result = fetch_lab_posts.strip_html(raw)
        self.assertNotIn("\n", result)
        self.assertIn("One", result)
        self.assertIn("Two", result)


class TestParseDate(unittest.TestCase):

    def test_z_suffix_parses_as_utc(self):
        result = fetch_lab_posts.parse_date("2026-07-06T17:57:23Z")
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, timezone.utc)
        self.assertEqual(result.year, 2026)
        self.assertEqual(result.hour, 17)

    def test_lowercase_z_suffix(self):
        result = fetch_lab_posts.parse_date("2026-07-06T17:57:23z")
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, timezone.utc)

    def test_negative_offset_preserved(self):
        result = fetch_lab_posts.parse_date("2026-07-06T17:57:23-07:00")
        self.assertIsNotNone(result)
        import datetime as dt
        expected_offset = dt.timezone(dt.timedelta(hours=-7))
        self.assertEqual(result.utcoffset(), expected_offset.utcoffset(None))

    def test_naive_datetime_gets_utc_tzinfo(self):
        # WordPress sometimes emits dates without a timezone — treat as UTC.
        result = fetch_lab_posts.parse_date("2026-07-06T17:57:23")
        self.assertIsNotNone(result)
        self.assertEqual(result.tzinfo, timezone.utc)

    def test_unparseable_returns_none(self):
        self.assertIsNone(fetch_lab_posts.parse_date("not a date"))

    def test_empty_string_returns_none(self):
        self.assertIsNone(fetch_lab_posts.parse_date(""))

    def test_none_input_returns_none(self):
        self.assertIsNone(fetch_lab_posts.parse_date(None))

    def test_invalid_iso_values_return_none(self):
        self.assertIsNone(fetch_lab_posts.parse_date("2026-99-99T25:99:99Z"))

    def test_z_suffix_correct_time_value(self):
        # Verify the Z-rewrite doesn't shift the clock value.
        result = fetch_lab_posts.parse_date("2026-01-15T08:30:00Z")
        self.assertEqual(result.hour, 8)
        self.assertEqual(result.minute, 30)


class TestCollectPostsPaging(unittest.TestCase):

    def _wp_post(self, post_id, date_str, title="Test Post"):
        return {
            "ID": post_id,
            "date": date_str,
            "title": title,
            "URL": f"https://example.com/{post_id}",
            "content": "<p>Some content.</p>",
            "author": {"name": "Lab Member"},
        }

    def test_cutoff_stops_paging_and_excludes_old_post(self):
        cutoff = datetime(2026, 7, 21, 0, 0, 0, tzinfo=timezone.utc)
        recent = "2026-07-25T12:00:00Z"
        old = "2026-07-19T12:00:00Z"
        page = [self._wp_post(1, recent, "Recent"), self._wp_post(2, old, "Old")]

        with patch("fetch_lab_posts.fetch_page", return_value={"posts": page}):
            posts, warnings = fetch_lab_posts.collect_posts(
                "example.com", cutoff, per_page=100, max_pages=10, timeout=15
            )

        titles = [p["title"] for p in posts]
        self.assertIn("Recent", titles)
        self.assertNotIn("Old", titles)
        self.assertEqual(warnings, [])

    def test_max_pages_warning_issued_when_limit_hit(self):
        # All posts are recent; the loop never reaches the cutoff and must hit max_pages.
        cutoff = datetime(2020, 1, 1, tzinfo=timezone.utc)
        always_recent = "2026-07-15T12:00:00Z"
        single_post_page = [self._wp_post(1, always_recent, "New Post")]

        with patch("fetch_lab_posts.fetch_page", return_value={"posts": single_post_page}):
            posts, warnings = fetch_lab_posts.collect_posts(
                "example.com", cutoff, per_page=1, max_pages=2, timeout=15
            )

        self.assertEqual(len(warnings), 1)
        self.assertIn("2 pages", warnings[0])
        self.assertIn("cutoff", warnings[0].lower())

    def test_no_warning_when_cutoff_reached_within_limit(self):
        cutoff = datetime(2026, 7, 21, 0, 0, 0, tzinfo=timezone.utc)
        old = "2026-07-15T12:00:00Z"
        page = [self._wp_post(99, old, "Very Old")]

        with patch("fetch_lab_posts.fetch_page", return_value={"posts": page}):
            posts, warnings = fetch_lab_posts.collect_posts(
                "example.com", cutoff, per_page=100, max_pages=10, timeout=15
            )

        self.assertEqual(posts, [])
        self.assertEqual(warnings, [])

    def test_empty_batch_terminates_without_warning(self):
        cutoff = datetime(2020, 1, 1, tzinfo=timezone.utc)

        with patch("fetch_lab_posts.fetch_page", return_value={"posts": []}):
            posts, warnings = fetch_lab_posts.collect_posts(
                "example.com", cutoff, per_page=100, max_pages=10, timeout=15
            )

        self.assertEqual(posts, [])
        self.assertEqual(warnings, [])

    def test_max_pages_warning_mentions_page_count(self):
        cutoff = datetime(2020, 1, 1, tzinfo=timezone.utc)
        recent = "2026-07-15T12:00:00Z"
        page = [self._wp_post(1, recent)]

        with patch("fetch_lab_posts.fetch_page", return_value={"posts": page}):
            _, warnings = fetch_lab_posts.collect_posts(
                "example.com", cutoff, per_page=1, max_pages=5, timeout=15
            )

        self.assertEqual(len(warnings), 1)
        self.assertIn("5 pages", warnings[0])

    def test_unreadable_date_warns_and_skips_only_that_post(self):
        cutoff = datetime(2020, 1, 1, tzinfo=timezone.utc)
        broken = self._wp_post(7, "not a date", "Broken Date")
        good = self._wp_post(8, "2026-07-25T12:00:00Z", "Good Date")

        with patch("fetch_lab_posts.fetch_page",
                   side_effect=[{"posts": [broken, good]}, {"posts": []}]):
            posts, warnings = fetch_lab_posts.collect_posts(
                "example.com", cutoff, per_page=100, max_pages=2, timeout=15
            )

        titles = [p["title"] for p in posts]
        self.assertNotIn("Broken Date", titles)
        self.assertIn("Good Date", titles)
        self.assertEqual(len(warnings), 1)
        self.assertIn("7", warnings[0])
        self.assertIn("unreadable date", warnings[0])

    def test_excerpt_used_when_content_absent(self):
        cutoff = datetime(2020, 1, 1, tzinfo=timezone.utc)
        post = self._wp_post(5, "2026-07-25T12:00:00Z")
        del post["content"]
        post["excerpt"] = "<p>Excerpt text.</p>"

        with patch("fetch_lab_posts.fetch_page",
                   side_effect=[{"posts": [post]}, {"posts": []}]):
            posts, _ = fetch_lab_posts.collect_posts(
                "example.com", cutoff, per_page=100, max_pages=2, timeout=15
            )

        self.assertEqual(posts[0]["content"], "Excerpt text.")

    def test_empty_content_falls_back_to_excerpt(self):
        cutoff = datetime(2020, 1, 1, tzinfo=timezone.utc)
        post = self._wp_post(6, "2026-07-25T12:00:00Z")
        post["content"] = ""
        post["excerpt"] = "<p>Fallback body.</p>"

        with patch("fetch_lab_posts.fetch_page",
                   side_effect=[{"posts": [post]}, {"posts": []}]):
            posts, _ = fetch_lab_posts.collect_posts(
                "example.com", cutoff, per_page=100, max_pages=2, timeout=15
            )

        self.assertEqual(posts[0]["content"], "Fallback body.")

    def test_missing_author_falls_back_to_unknown(self):
        cutoff = datetime(2020, 1, 1, tzinfo=timezone.utc)
        post = self._wp_post(9, "2026-07-25T12:00:00Z")
        post["author"] = None

        with patch("fetch_lab_posts.fetch_page",
                   side_effect=[{"posts": [post]}, {"posts": []}]):
            posts, _ = fetch_lab_posts.collect_posts(
                "example.com", cutoff, per_page=100, max_pages=2, timeout=15
            )

        self.assertEqual(posts[0]["author"], "Unknown")

    def test_post_fields_mapped_correctly(self):
        cutoff = datetime(2020, 1, 1, tzinfo=timezone.utc)
        recent = "2026-07-25T09:00:00Z"
        post_data = [self._wp_post(42, recent, "Mapped Title")]

        # Return the post on page 1, then an empty batch so paging terminates
        # naturally without duplicating the same post across multiple pages.
        with patch("fetch_lab_posts.fetch_page",
                   side_effect=[{"posts": post_data}, {"posts": []}]):
            posts, _ = fetch_lab_posts.collect_posts(
                "example.com", cutoff, per_page=100, max_pages=2, timeout=15
            )

        self.assertEqual(len(posts), 1)
        p = posts[0]
        self.assertEqual(p["title"], "Mapped Title")
        self.assertEqual(p["author"], "Lab Member")
        self.assertEqual(p["date"], "2026-07-25")
        self.assertIn("example.com/42", p["url"])


if __name__ == "__main__":
    unittest.main()
