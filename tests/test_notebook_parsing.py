"""Tests for scripts/notebook_parsing.py — front-matter parsing and permalink derivation."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import notebook_parsing


class TestParseFrontMatter(unittest.TestCase):
    """parse_front_matter pulls title/author/date/categories out of the --- block."""

    def test_tumbling_quoted_title_and_inline_categories(self):
        text = (
            "---\n"
            'title: "Trout methylation"\n'
            "author: Steven Roberts\n"
            "date: 2026-07-28\n"
            "categories: [methylation, trout]\n"
            "---\n"
            "Body text here.\n"
        )
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["title"], "Trout methylation")
        self.assertEqual(fm["author"], "Steven Roberts")
        self.assertEqual(fm["date"], "2026-07-28")
        self.assertEqual(fm["categories"], ["methylation", "trout"])

    def test_ariana_scalar_category_and_quoted_date(self):
        # A single bare-scalar category normalizes to a one-element list.
        text = (
            "---\n"
            "layout: post\n"
            "title: Point Whitney seed hardening\n"
            "author: Ariana Huffmyer\n"
            "date: '2026-07-06'\n"
            "categories: Point_Whitney\n"
            "---\n"
        )
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["title"], "Point Whitney seed hardening")
        self.assertEqual(fm["author"], "Ariana Huffmyer")
        self.assertEqual(fm["date"], "2026-07-06")
        self.assertEqual(fm["categories"], ["Point_Whitney"])

    def test_sams_block_list_categories(self):
        text = (
            "---\n"
            'title: "Glycogen Assay"\n'
            "author: Sam White\n"
            "date: 2026-07-30\n"
            "categories:\n"
            "  - assay\n"
            "  - glycogen\n"
            "---\n"
        )
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["title"], "Glycogen Assay")
        self.assertEqual(fm["author"], "Sam White")
        self.assertEqual(fm["categories"], ["assay", "glycogen"])

    def test_grace_missing_author_uses_default(self):
        # Grace's notebook front matter has no author field.
        text = (
            "---\n"
            "layout: post\n"
            "title: Enrichment prelim\n"
            "date: 2026-07-15\n"
            "categories: [qpcr, enrichment]\n"
            "---\n"
        )
        fm = notebook_parsing.parse_front_matter(text, default_author="Grace Crandall")
        self.assertEqual(fm["title"], "Enrichment prelim")
        self.assertEqual(fm["author"], "Grace Crandall")
        self.assertEqual(fm["categories"], ["qpcr", "enrichment"])

    def test_missing_author_without_default_is_none(self):
        text = "---\ntitle: A post\ndate: 2026-07-15\n---\n"
        fm = notebook_parsing.parse_front_matter(text)
        self.assertIsNone(fm["author"])

    def test_empty_author_value_falls_back_to_default(self):
        text = "---\ntitle: A post\nauthor:\ndate: 2026-07-15\n---\n"
        fm = notebook_parsing.parse_front_matter(text, default_author="Fallback")
        self.assertEqual(fm["author"], "Fallback")

    def test_no_front_matter_block_returns_defaults(self):
        fm = notebook_parsing.parse_front_matter("Just a body, no front matter.\n",
                                                 default_author="Someone")
        self.assertIsNone(fm["title"])
        self.assertIsNone(fm["date"])
        self.assertEqual(fm["categories"], [])
        self.assertEqual(fm["author"], "Someone")

    def test_leading_blank_lines_before_block_tolerated(self):
        text = "\n\n---\ntitle: Later start\n---\n"
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["title"], "Later start")

    def test_missing_categories_is_empty_list(self):
        text = "---\ntitle: No cats\ndate: 2026-07-15\n---\n"
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["categories"], [])

    def test_colon_in_quoted_title_preserved(self):
        text = '---\ntitle: "Analysis: part 1"\n---\n'
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["title"], "Analysis: part 1")

    def test_body_key_value_lines_ignored(self):
        # A `key: value` line in the body must not leak into the parsed fields.
        text = "---\ntitle: Real title\n---\nnote: this is body text\n"
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["title"], "Real title")


class TestDerivePermalink(unittest.TestCase):
    """derive_permalink maps a repo path to the notebook's published URL."""

    def test_tumbling_oysters_folder_index(self):
        url = notebook_parsing.derive_permalink(
            "tumbling-oysters", "posts/84-trout-meth/index.qmd"
        )
        self.assertEqual(
            url, "https://sr320.github.io/tumbling-oysters/posts/84-trout-meth/"
        )

    def test_ariana_flat_qmd_becomes_html(self):
        url = notebook_parsing.derive_permalink(
            "ariana", "posts/2026-07-06-point-whitney-seed-hardening.qmd"
        )
        self.assertEqual(
            url,
            "https://ahuffmyer.github.io/posts/2026-07-06-point-whitney-seed-hardening.html",
        )

    def test_grace_strips_date_prefix_and_extension(self):
        url = notebook_parsing.derive_permalink(
            "grace", "_posts/2026-07-15-enrichment-prelim.md"
        )
        self.assertEqual(url, "https://grace-ac.github.io/enrichment-prelim/")

    def test_sams_keeps_year_and_date_slug_folder(self):
        url = notebook_parsing.derive_permalink(
            "sams", "posts/2026/2026-07-30-Glycogen-Assay/index.qmd"
        )
        self.assertEqual(
            url,
            "https://robertslab.github.io/sams-notebook/posts/2026/2026-07-30-Glycogen-Assay/",
        )

    def test_leading_slash_in_path_tolerated(self):
        url = notebook_parsing.derive_permalink(
            "ariana", "/posts/2026-07-01-goals.qmd"
        )
        self.assertEqual(url, "https://ahuffmyer.github.io/posts/2026-07-01-goals.html")

    def test_grace_filename_without_date_prefix_unchanged(self):
        # A non-standard filename with no YYYY-MM-DD- prefix keeps its slug as-is.
        url = notebook_parsing.derive_permalink("grace", "_posts/2026filter-qpcr.md")
        self.assertEqual(url, "https://grace-ac.github.io/2026filter-qpcr/")

    def test_unknown_source_raises(self):
        with self.assertRaises(ValueError):
            notebook_parsing.derive_permalink("wordpress", "posts/x.qmd")


if __name__ == "__main__":
    unittest.main()
