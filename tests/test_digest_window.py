"""Tests for the shared digest window, backdated-post flag, and automated-post filter."""

import os
import sys
import unittest
from datetime import date, datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import fetch_lab_posts
from notebook_parsing import digest_window, is_backdated


class TestDigestWindow(unittest.TestCase):

    def test_pacific_evening_run_uses_pacific_date(self):
        # The 2026-11-24 digest ran at 02:07 UTC = 18:07 PST on Monday Nov 23.
        # The old code labelled it Nov 18–24; the lab's week was Nov 17–23.
        now = datetime(2026, 11, 24, 2, 7, tzinfo=timezone.utc)
        start, today, cutoff = digest_window(7, now)
        self.assertEqual(today, date(2026, 11, 23))
        self.assertEqual(start, date(2026, 11, 17))
        # Local midnight Nov 17 PST is 08:00 UTC.
        self.assertEqual(cutoff, datetime(2026, 11, 17, 8, 0, tzinfo=timezone.utc))

    def test_window_spans_exactly_days_calendar_dates(self):
        now = datetime(2026, 7, 13, 15, 0, tzinfo=timezone.utc)  # Monday 08:00 PDT
        start, today, cutoff = digest_window(7, now)
        self.assertEqual((today - start).days, 6)
        # Local midnight in summer (PDT) is 07:00 UTC.
        self.assertEqual(cutoff, datetime(2026, 7, 7, 7, 0, tzinfo=timezone.utc))

    def test_post_in_header_range_is_never_before_cutoff(self):
        # Grace's 2026-11-17 commit at 22:47 UTC must fall inside the window
        # whose header starts on Nov 17, and before a window starting Nov 18.
        commit = datetime(2026, 11, 17, 22, 47, tzinfo=timezone.utc)
        _, _, cutoff = digest_window(7, datetime(2026, 11, 24, 2, 7, tzinfo=timezone.utc))
        self.assertGreaterEqual(commit, cutoff)
        _, _, later = digest_window(7, datetime(2026, 11, 25, 2, 7, tzinfo=timezone.utc))
        self.assertLess(commit, later)

    def test_naive_now_treated_as_utc(self):
        a = digest_window(7, datetime(2026, 11, 24, 2, 7))
        b = digest_window(7, datetime(2026, 11, 24, 2, 7, tzinfo=timezone.utc))
        self.assertEqual(a, b)

    def test_days_must_be_positive(self):
        with self.assertRaises(ValueError):
            digest_window(0)


class TestIsBackdated(unittest.TestCase):
    START = date(2026, 11, 17)

    def test_added_post_dated_before_window(self):
        self.assertTrue(is_backdated("added", "2026-11-04", self.START))

    def test_added_post_dated_in_window(self):
        self.assertFalse(is_backdated("added", "2026-11-17", self.START))

    def test_modified_old_post_is_an_edit_not_backdated(self):
        self.assertFalse(is_backdated("modified", "2026-11-04", self.START))

    def test_missing_or_unparseable_date(self):
        self.assertFalse(is_backdated("added", None, self.START))
        self.assertFalse(is_backdated("added", "last-modified", self.START))


class TestIsAutomated(unittest.TestCase):

    def test_daily_literature_title(self):
        self.assertTrue(fetch_lab_posts.is_automated(
            {"title": "Daily Literature Connections — 2026-11-18", "categories": []}))

    def test_full_lab_digest_title(self):
        self.assertTrue(fetch_lab_posts.is_automated(
            {"title": "Full Lab Digest — 2026-11-10 to 2026-11-16 (7 days)"}))

    def test_category_alone_is_enough(self):
        self.assertTrue(fetch_lab_posts.is_automated(
            {"title": "Something else", "categories": ["auto-literature-connections"]}))

    def test_twif_podcast_title(self):
        self.assertTrue(fetch_lab_posts.is_automated(
            {"title": "TWIF S01E03 - Gene Bodies and Green Water", "categories": []}))

    def test_podcast_category_any_case(self):
        self.assertTrue(fetch_lab_posts.is_automated(
            {"title": "This week in the lab", "categories": ["Podcast"]}))

    def test_title_starting_with_twif_word_only(self):
        # "Twifold" is not a TWIF episode; the prefix needs the trailing space.
        self.assertFalse(fetch_lab_posts.is_automated(
            {"title": "Twifold symmetry in larval shells", "categories": []}))

    def test_ordinary_lab_post_kept(self):
        self.assertFalse(fetch_lab_posts.is_automated(
            {"title": "11.18: first exposure for sublethal/lethal experiment",
             "categories": ["Uncategorized"]}))

    def test_title_mentioning_literature_not_at_start_kept(self):
        self.assertFalse(fetch_lab_posts.is_automated(
            {"title": "Notes on daily literature connections workflow"}))


if __name__ == "__main__":
    unittest.main()
