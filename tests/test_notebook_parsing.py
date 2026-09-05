"""Tests for scripts/notebook_parsing.py — front-matter parsing and permalink derivation."""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import notebook_parsing


class TestNormalizeDate(unittest.TestCase):
    """normalize_date coerces every date shape the five notebooks actually write."""

    def test_iso_passthrough(self):
        self.assertEqual(notebook_parsing.normalize_date("2026-07-28"), "2026-07-28")

    def test_iso_with_time_and_zone_is_truncated(self):
        # Sam's notebook: `2026-08-01 10:00:00+00:00` sorts AFTER a bare
        # `2026-08-01` end bound, so it must lose the time to stay in-window.
        self.assertEqual(notebook_parsing.normalize_date("2026-08-01 10:00:00+00:00"), "2026-08-01")
        self.assertEqual(notebook_parsing.normalize_date("'2026-08-01 10:00'"), "2026-08-01")
        self.assertEqual(notebook_parsing.normalize_date("2026-07-28T09:00:00Z"), "2026-07-28")

    def test_us_month_first_four_digit_year(self):
        # tumbling-oysters and Megan's notebook: the majority of their posts.
        self.assertEqual(notebook_parsing.normalize_date("12-01-2025"), "2025-12-01")
        self.assertEqual(notebook_parsing.normalize_date('"12-01-2025"'), "2025-12-01")
        self.assertEqual(notebook_parsing.normalize_date("12-1-2025"), "2025-12-01")

    def test_us_month_first_two_digit_year(self):
        self.assertEqual(notebook_parsing.normalize_date("05-14-24"), "2024-05-14")

    def test_month_name(self):
        self.assertEqual(notebook_parsing.normalize_date('"May 31, 2023"'), "2023-05-31")
        self.assertEqual(notebook_parsing.normalize_date("31 May 2023"), "2023-05-31")

    def test_unpadded_iso(self):
        self.assertEqual(notebook_parsing.normalize_date("2026-8-1"), "2026-08-01")

    def test_template_placeholder_is_none(self):
        self.assertIsNone(notebook_parsing.normalize_date("YYYY-MM-DD"))

    def test_impossible_dates_are_none(self):
        self.assertIsNone(notebook_parsing.normalize_date("13-01-2025"))
        self.assertIsNone(notebook_parsing.normalize_date("2026-02-30"))

    def test_empty_and_none(self):
        self.assertIsNone(notebook_parsing.normalize_date(""))
        self.assertIsNone(notebook_parsing.normalize_date("   "))
        self.assertIsNone(notebook_parsing.normalize_date(None))


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

    def test_us_date_in_front_matter_is_normalised(self):
        text = "---\ntitle: GBM plots\ndate: 12-1-2025\n---\n"
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["date"], "2025-12-01")

    def test_placeholder_date_in_front_matter_is_none(self):
        text = "---\ntitle: Template\ndate: YYYY-MM-DD\n---\n"
        fm = notebook_parsing.parse_front_matter(text)
        self.assertIsNone(fm["date"])

    def test_missing_categories_is_empty_list(self):
        text = "---\ntitle: No cats\ndate: 2026-07-15\n---\n"
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["categories"], [])

    def test_inline_categories_with_trailing_template_comment(self):
        # Newer tumbling-oysters posts leave the template's `#choose ...` scaffold
        # comment on the categories line; only the values before `#` are real.
        text = (
            "---\n"
            "title: Sea star wasting\n"
            'categories: ["Transcriptomics", "Genomics"] #choose "Aquaculture", "Computing"\n'
            "---\n"
        )
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["categories"], ["Transcriptomics", "Genomics"])

    def test_scalar_value_trailing_comment_stripped(self):
        text = "---\ntitle: Real title # placeholder\ndate: 2026-07-15\n---\n"
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["title"], "Real title")

    def test_hash_inside_quotes_preserved(self):
        text = '---\ntitle: "Issue #42 writeup"\n---\n'
        fm = notebook_parsing.parse_front_matter(text)
        self.assertEqual(fm["title"], "Issue #42 writeup")

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

    def test_megan_nested_qmd_becomes_html(self):
        # Megan's Quarto site has no fixed folder convention; a dated-month
        # folder holds a named .qmd that renders to a sibling .html.
        url = notebook_parsing.derive_permalink(
            "megan", "posts/2026-08/fieldretrieval1.qmd"
        )
        self.assertEqual(
            url,
            "https://meganewing.github.io/mewing-notebook/posts/2026-08/fieldretrieval1.html",
        )

    def test_megan_projects_folder_qmd_becomes_html(self):
        # A different subfolder (projects/) resolves the same way.
        url = notebook_parsing.derive_permalink(
            "megan", "posts/projects/clamtrials.qmd"
        )
        self.assertEqual(
            url,
            "https://meganewing.github.io/mewing-notebook/posts/projects/clamtrials.html",
        )

    def test_megan_index_qmd_becomes_folder(self):
        # An index.qmd renders to its folder, not a .html file.
        url = notebook_parsing.derive_permalink("megan", "posts/welcome/index.qmd")
        self.assertEqual(
            url, "https://meganewing.github.io/mewing-notebook/posts/welcome/"
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
