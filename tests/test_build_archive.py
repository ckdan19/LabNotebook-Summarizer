"""Tests for scripts/build_archive.py — the stored-date renormalisation pass."""

import sys
import os
import sqlite3
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import build_archive


def _row(source, path, date, url=None):
    return {
        "source": source, "author": "A", "date": date, "url": url or f"https://x/{path}",
        "path": path, "title": "t", "categories": "[]", "body_text": "b",
        "blob_sha": "sha-" + path, "fetched_at": "2026-09-05T00:00:00+00:00",
    }


class TestRenormalizeDates(unittest.TestCase):
    """Rows archived before normalisation existed are fixed in place, once."""

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        build_archive.init_db(self.conn)

    def _dates(self):
        return dict(self.conn.execute("SELECT path, date FROM posts ORDER BY path").fetchall())

    def test_us_dates_rewritten_iso_left_alone(self):
        build_archive.upsert_post(self.conn, _row("tumbling-oysters", "posts/65-gbm-plots/index.qmd", "12-1-2025"))
        build_archive.upsert_post(self.conn, _row("megan", "posts/a.qmd", "03-15-2026"))
        build_archive.upsert_post(self.conn, _row("ariana", "posts/2026-07-06-b.qmd", "2026-07-06"))
        changed = build_archive.renormalize_dates(self.conn)
        self.assertEqual(changed, 2)
        self.assertEqual(self._dates(), {
            "posts/65-gbm-plots/index.qmd": "2025-12-01",
            "posts/a.qmd": "2026-03-15",
            "posts/2026-07-06-b.qmd": "2026-07-06",
        })

    def test_timestamped_date_truncated(self):
        build_archive.upsert_post(self.conn, _row("sams", "posts/2026/2026-08-01-x/index.qmd", "2026-08-01 10:00:00+00:00"))
        self.assertEqual(build_archive.renormalize_dates(self.conn), 1)
        self.assertEqual(self._dates()["posts/2026/2026-08-01-x/index.qmd"], "2026-08-01")

    def test_unreadable_date_falls_back_to_filename_stamp(self):
        build_archive.upsert_post(self.conn, _row("ariana", "posts/2026-07-06-c.qmd", "YYYY-MM-DD"))
        self.assertEqual(build_archive.renormalize_dates(self.conn), 1)
        self.assertEqual(self._dates()["posts/2026-07-06-c.qmd"], "2026-07-06")

    def test_unreadable_date_with_no_stamp_stays_null(self):
        build_archive.upsert_post(self.conn, _row("tumbling-oysters", "posts/welcome/index.qmd", "soon"))
        self.assertEqual(build_archive.renormalize_dates(self.conn), 1)
        self.assertIsNone(self._dates()["posts/welcome/index.qmd"])
        # NULL rows are re-examined each run but produce no further change.
        self.assertEqual(build_archive.renormalize_dates(self.conn), 0)

    def test_idempotent(self):
        build_archive.upsert_post(self.conn, _row("tumbling-oysters", "posts/1-a/index.qmd", "05-14-24"))
        self.assertEqual(build_archive.renormalize_dates(self.conn), 1)
        self.assertEqual(build_archive.renormalize_dates(self.conn), 0)


if __name__ == "__main__":
    unittest.main()
