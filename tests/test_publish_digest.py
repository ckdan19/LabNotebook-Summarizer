"""Tests for scripts/publish_digest.py — HTML sanitizer, title extraction, and dry-run."""

import sys
import os
import io
import json
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from types import SimpleNamespace
from unittest.mock import patch
from urllib.error import HTTPError

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import publish_digest


class TestSanitizer(unittest.TestCase):
    """Verify that the HTML allowlist blocks unsafe content at every attack surface."""

    def test_script_tag_and_content_dropped(self):
        raw = '<p>Before</p><script>alert("xss")</script><p>After</p>'
        result = publish_digest.sanitize(raw)
        self.assertNotIn("script", result)
        self.assertNotIn("alert", result)
        self.assertIn("<p>Before</p>", result)
        self.assertIn("<p>After</p>", result)

    def test_iframe_tag_and_content_dropped(self):
        raw = '<p>Text</p><iframe src="https://evil.com">Fallback content</iframe><p>More</p>'
        result = publish_digest.sanitize(raw)
        self.assertNotIn("iframe", result)
        # Content inside DROP_WITH_CONTENT tags is also suppressed
        self.assertNotIn("Fallback content", result)
        self.assertIn("<p>Text</p>", result)
        self.assertIn("<p>More</p>", result)

    def test_nested_script_content_dropped(self):
        raw = "<div><script>evil()</script>Visible text</div>"
        result = publish_digest.sanitize(raw)
        self.assertNotIn("evil", result)
        self.assertIn("Visible text", result)

    def test_object_tag_and_content_dropped(self):
        raw = '<object data="evil.swf">Fallback</object>'
        result = publish_digest.sanitize(raw)
        self.assertNotIn("object", result)
        self.assertNotIn("Fallback", result)

    def test_inline_onclick_stripped(self):
        raw = '<p onclick="evil()">Paragraph text</p>'
        result = publish_digest.sanitize(raw)
        self.assertNotIn("onclick", result)
        self.assertNotIn("evil", result)
        self.assertIn("<p>", result)
        self.assertIn("Paragraph text", result)

    def test_onerror_stripped_from_img(self):
        raw = '<img src="https://example.com/img.png" onerror="evil()" alt="photo">'
        result = publish_digest.sanitize(raw)
        self.assertNotIn("onerror", result)
        # Allowed attributes on img are preserved
        self.assertIn('src="https://example.com/img.png"', result)
        self.assertIn('alt="photo"', result)

    def test_javascript_url_stripped_from_href(self):
        raw = '<a href="javascript:alert(1)">Click me</a>'
        result = publish_digest.sanitize(raw)
        self.assertNotIn("javascript:", result)
        # Tag and text survive — only the dangerous href is dropped
        self.assertIn("Click me", result)

    def test_javascript_url_case_insensitive(self):
        raw = '<a href="JAVASCRIPT:alert(1)">Click</a>'
        result = publish_digest.sanitize(raw)
        self.assertNotIn("javascript:", result.lower())

    def test_valid_https_href_preserved(self):
        raw = '<a href="https://example.com" title="Example">Link text</a>'
        result = publish_digest.sanitize(raw)
        self.assertIn('href="https://example.com"', result)
        self.assertIn('title="Example"', result)

    def test_http_href_preserved(self):
        raw = '<a href="http://example.com">Old link</a>'
        result = publish_digest.sanitize(raw)
        self.assertIn('href="http://example.com"', result)

    def test_mailto_href_preserved(self):
        raw = '<a href="mailto:lab@uw.edu">Email us</a>'
        result = publish_digest.sanitize(raw)
        self.assertIn('href="mailto:lab@uw.edu"', result)

    def test_allowed_inline_tags_preserved(self):
        raw = "<p>A <strong>bold</strong> and <em>italic</em> word.</p>"
        result = publish_digest.sanitize(raw)
        self.assertIn("<strong>bold</strong>", result)
        self.assertIn("<em>italic</em>", result)

    def test_unknown_tag_dropped_content_kept(self):
        # div and span are not in ALLOWED_TAGS — tags dropped, text survives
        raw = "<div><span>Some text</span></div>"
        result = publish_digest.sanitize(raw)
        self.assertNotIn("<div>", result)
        self.assertNotIn("<span>", result)
        self.assertIn("Some text", result)

    def test_img_src_must_be_allowed_scheme(self):
        raw = '<img src="javascript:void(0)" alt="bad">'
        result = publish_digest.sanitize(raw)
        self.assertNotIn("javascript:", result)

    def test_special_chars_in_text_escaped(self):
        raw = "<p>5 > 3 and 2 < 4</p>"
        result = publish_digest.sanitize(raw)
        self.assertNotIn(">", result.replace("<p>", "").replace("</p>", ""))
        self.assertIn("&gt;", result)
        self.assertIn("&lt;", result)


class TestSplitDigest(unittest.TestCase):

    def _write_temp(self, content):
        fd, path = tempfile.mkstemp(suffix=".md")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    def test_extracts_title_from_h1(self):
        path = self._write_temp("# Weekly Lab Digest\n\nSome body content.\n")
        try:
            title, body = publish_digest.split_digest(path)
            self.assertEqual(title, "Weekly Lab Digest")
            self.assertIn("Some body content.", body)
        finally:
            os.unlink(path)

    def test_title_strips_inline_html(self):
        path = self._write_temp("# Weekly <em>Lab</em> Digest\n\nBody.\n")
        try:
            title, body = publish_digest.split_digest(path)
            self.assertEqual(title, "Weekly Lab Digest")
        finally:
            os.unlink(path)

    def test_title_unescapes_html_entities(self):
        path = self._write_temp("# Fish &amp; Chips Summary\n\nContent.\n")
        try:
            title, body = publish_digest.split_digest(path)
            self.assertEqual(title, "Fish & Chips Summary")
        finally:
            os.unlink(path)

    def test_h1_heading_not_in_body(self):
        path = self._write_temp("# My Title\n\nReal body here.\n")
        try:
            title, body = publish_digest.split_digest(path)
            self.assertNotIn("# My Title", body)
            self.assertIn("Real body here.", body)
        finally:
            os.unlink(path)

    def test_multiline_body_preserved(self):
        content = "# Digest\n\n## Section A\n\nText A.\n\n## Section B\n\nText B.\n"
        path = self._write_temp(content)
        try:
            title, body = publish_digest.split_digest(path)
            self.assertEqual(title, "Digest")
            self.assertIn("Section A", body)
            self.assertIn("Section B", body)
        finally:
            os.unlink(path)

    def test_empty_file_raises_value_error(self):
        fd, path = tempfile.mkstemp(suffix=".md")
        os.close(fd)
        try:
            with self.assertRaises(ValueError):
                publish_digest.split_digest(path)
        finally:
            os.unlink(path)

    def test_no_h1_raises_value_error(self):
        path = self._write_temp("This file does not start with a heading.\n")
        try:
            with self.assertRaises(ValueError):
                publish_digest.split_digest(path)
        finally:
            os.unlink(path)

    def test_h2_heading_raises_value_error(self):
        path = self._write_temp("## Not an H1\n\nBody.\n")
        try:
            with self.assertRaises(ValueError):
                publish_digest.split_digest(path)
        finally:
            os.unlink(path)

    def test_title_with_date_suffix(self):
        # Realistic digest title that includes a date
        path = self._write_temp("# Lab Digest — Week of 2026-07-28\n\nBody.\n")
        try:
            title, body = publish_digest.split_digest(path)
            self.assertEqual(title, "Lab Digest — Week of 2026-07-28")
        finally:
            os.unlink(path)


class TestReadToken(unittest.TestCase):
    """The token is a live credential: absence, emptiness, and loose modes all matter."""

    def _write_token(self, content, mode=0o600):
        fd, path = tempfile.mkstemp(suffix=".token")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
        os.chmod(path, mode)
        return path

    def test_missing_file_raises_with_setup_guidance(self):
        with self.assertRaises(FileNotFoundError) as ctx:
            publish_digest.read_token("/nonexistent/path/wp_token")
        self.assertIn("developer.wordpress.com", str(ctx.exception))

    def test_empty_file_raises_value_error(self):
        path = self._write_token("")
        try:
            with self.assertRaises(ValueError):
                publish_digest.read_token(path)
        finally:
            os.unlink(path)

    def test_whitespace_only_file_raises_value_error(self):
        path = self._write_token("   \n\t\n")
        try:
            with self.assertRaises(ValueError):
                publish_digest.read_token(path)
        finally:
            os.unlink(path)

    def test_token_is_stripped_of_surrounding_whitespace(self):
        path = self._write_token("  abc123\n")
        try:
            token, _ = publish_digest.read_token(path)
            self.assertEqual(token, "abc123")
        finally:
            os.unlink(path)

    def test_private_mode_produces_no_warning(self):
        path = self._write_token("abc123", mode=0o600)
        try:
            _, warnings = publish_digest.read_token(path)
            self.assertEqual(warnings, [])
        finally:
            os.unlink(path)

    def test_world_readable_mode_warns_with_chmod_hint(self):
        path = self._write_token("abc123", mode=0o644)
        try:
            _, warnings = publish_digest.read_token(path)
            self.assertEqual(len(warnings), 1)
            self.assertIn("chmod 600", warnings[0])
        finally:
            os.unlink(path)

    def test_group_readable_mode_warns(self):
        path = self._write_token("abc123", mode=0o640)
        try:
            _, warnings = publish_digest.read_token(path)
            self.assertEqual(len(warnings), 1)
        finally:
            os.unlink(path)


class TestPostDraft(unittest.TestCase):
    """post_digest must send the token only in a header and never echo it back."""

    class _FakeResponse:
        def __init__(self, status, body):
            self.status = status
            self._body = body

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def read(self):
            return self._body

    def test_token_sent_as_bearer_header_and_status_is_draft(self):
        captured = {}

        def fake_urlopen(request, timeout=None):
            captured["auth"] = request.headers.get("Authorization")
            captured["payload"] = json.loads(request.data.decode("utf-8"))
            captured["url"] = request.full_url
            return self._FakeResponse(201, b'{"URL": "https://site/p/1", "ID": 1}')

        with patch("publish_digest.urlopen", side_effect=fake_urlopen):
            status, payload = publish_digest.post_digest(
                "example.wordpress.com", "sekrit", "My Title", "<p>Body</p>"
            )

        self.assertEqual(status, 201)
        self.assertEqual(captured["auth"], "Bearer sekrit")
        self.assertEqual(captured["payload"]["status"], "draft")
        self.assertEqual(captured["payload"]["title"], "My Title")
        # The token must never travel in the URL, where it would land in logs.
        self.assertNotIn("sekrit", captured["url"])
        self.assertEqual(payload["ID"], 1)

    def test_status_publish_is_sent_when_requested(self):
        captured = {}

        def fake_urlopen(request, timeout=None):
            captured["payload"] = json.loads(request.data.decode("utf-8"))
            return self._FakeResponse(201, b'{"URL": "https://site/p/1", "ID": 1}')

        with patch("publish_digest.urlopen", side_effect=fake_urlopen):
            publish_digest.post_digest(
                "example.wordpress.com", "sekrit", "T", "<p>c</p>", status="publish"
            )

        self.assertEqual(captured["payload"]["status"], "publish")

    def test_categories_sent_as_comma_separated_string(self):
        # The WordPress.com v1.1 API expects `categories` as a comma-separated
        # string of names, not a JSON array. Pin the exact wire format.
        captured = {}

        def fake_urlopen(request, timeout=None):
            captured["payload"] = json.loads(request.data.decode("utf-8"))
            return self._FakeResponse(201, b'{"URL": "https://site/p/1", "ID": 1}')

        with patch("publish_digest.urlopen", side_effect=fake_urlopen):
            publish_digest.post_digest(
                "example.wordpress.com", "sekrit", "T", "<p>c</p>",
                categories=["Alpha", "Beta Gamma"],
            )

        value = captured["payload"]["categories"]
        self.assertIsInstance(value, str)
        self.assertEqual(value, "Alpha,Beta Gamma")

    def test_categories_omitted_when_empty(self):
        # No categories means the key must not appear on the wire at all.
        captured = {}

        def fake_urlopen(request, timeout=None):
            captured["payload"] = json.loads(request.data.decode("utf-8"))
            return self._FakeResponse(201, b'{"URL": "https://site/p/1", "ID": 1}')

        with patch("publish_digest.urlopen", side_effect=fake_urlopen):
            publish_digest.post_digest(
                "example.wordpress.com", "sekrit", "T", "<p>c</p>", categories=[]
            )

        self.assertNotIn("categories", captured["payload"])

    def test_status_defaults_to_draft(self):
        captured = {}

        def fake_urlopen(request, timeout=None):
            captured["payload"] = json.loads(request.data.decode("utf-8"))
            return self._FakeResponse(201, b'{"URL": "https://site/p/1", "ID": 1}')

        with patch("publish_digest.urlopen", side_effect=fake_urlopen):
            publish_digest.post_digest("example.wordpress.com", "sekrit", "T", "<p>c</p>")

        self.assertEqual(captured["payload"]["status"], "draft")

    def test_reflected_token_in_error_body_is_redacted(self):
        token = "super-secret-token"
        body = json.dumps(
            {"error": "invalid_token", "message": "token %s was rejected" % token}
        ).encode("utf-8")
        error = HTTPError("https://api", 401, "Unauthorized", {}, io.BytesIO(body))

        with patch("publish_digest.urlopen", side_effect=error):
            status, payload = publish_digest.post_digest(
                "example.wordpress.com", token, "T", "<p>c</p>"
            )

        self.assertEqual(status, 401)
        rendered = json.dumps(payload)
        self.assertNotIn(token, rendered)
        self.assertIn("[redacted]", rendered)

    def test_reflected_token_in_non_json_error_body_is_redacted(self):
        token = "super-secret-token"
        body = ("<html>token %s rejected</html>" % token).encode("utf-8")
        error = HTTPError("https://api", 500, "Server Error", {}, io.BytesIO(body))

        with patch("publish_digest.urlopen", side_effect=error):
            status, payload = publish_digest.post_digest(
                "example.wordpress.com", token, "T", "<p>c</p>"
            )

        self.assertEqual(status, 500)
        self.assertIn("raw", payload)
        self.assertNotIn(token, json.dumps(payload))

    def test_non_json_error_body_is_truncated(self):
        error = HTTPError("https://api", 500, "Server Error", {}, io.BytesIO(b"x" * 5000))

        with patch("publish_digest.urlopen", side_effect=error):
            _, payload = publish_digest.post_digest(
                "example.wordpress.com", "tok", "T", "<p>c</p>"
            )

        self.assertLessEqual(len(payload["raw"]), 1000)


class TestMarkdownToHtml(unittest.TestCase):

    def test_pandoc_used_when_python_markdown_missing(self):
        completed = SimpleNamespace(stdout="<p>hi</p>", stderr="")
        # sys.modules[name] = None makes "import name" raise ImportError.
        with patch.dict(sys.modules, {"markdown": None}):
            with patch("publish_digest.subprocess.run", return_value=completed) as run:
                html_out, converter = publish_digest.markdown_to_html("hi")

        self.assertEqual(converter, "pandoc")
        self.assertEqual(html_out, "<p>hi</p>")
        # raw_html must stay disabled so embedded HTML cannot bypass the sanitizer.
        self.assertIn("markdown-raw_html", run.call_args[0][0])

    def test_missing_both_converters_raises_runtime_error(self):
        with patch.dict(sys.modules, {"markdown": None}):
            with patch("publish_digest.subprocess.run", side_effect=FileNotFoundError()):
                with self.assertRaises(RuntimeError) as ctx:
                    publish_digest.markdown_to_html("hi")

        message = str(ctx.exception)
        self.assertIn("pandoc", message)
        self.assertIn("pip install markdown", message)

    def test_pandoc_failure_surfaces_stderr(self):
        failure = subprocess.CalledProcessError(1, ["pandoc"], stderr="pandoc exploded")
        with patch.dict(sys.modules, {"markdown": None}):
            with patch("publish_digest.subprocess.run", side_effect=failure):
                with self.assertRaises(RuntimeError) as ctx:
                    publish_digest.markdown_to_html("hi")

        self.assertIn("pandoc exploded", str(ctx.exception))


class TestDryRun(unittest.TestCase):
    """--dry-run must convert and sanitize only; it must never read the token file."""

    def test_dry_run_never_reads_token(self):
        fd, digest_path = tempfile.mkstemp(suffix=".md")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write("# Dry Run Test Digest\n\nContent for dry run test.\n")

        try:
            # Point --token-file at a path that does not exist on disk.
            # If read_token is called it raises AssertionError, failing the test.
            token_path = "/nonexistent/path/wp_token_must_not_be_read"

            captured = io.StringIO()
            with patch.object(sys, "argv", [
                "publish_digest.py", digest_path,
                "--dry-run", "--token-file", token_path,
            ]):
                with patch(
                    "publish_digest.markdown_to_html",
                    return_value=("<p>Content for dry run test.</p>", "test"),
                ):
                    with patch(
                        "publish_digest.read_token",
                        side_effect=AssertionError(
                            "read_token must not be called in --dry-run mode"
                        ),
                    ):
                        with redirect_stdout(captured):
                            publish_digest.main()

            output = json.loads(captured.getvalue())
            self.assertTrue(output.get("dry_run"))
            self.assertEqual(output.get("title"), "Dry Run Test Digest")
        finally:
            os.unlink(digest_path)

    def test_dry_run_output_has_expected_keys(self):
        fd, digest_path = tempfile.mkstemp(suffix=".md")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write("# Test\n\nBody.\n")

        try:
            captured = io.StringIO()
            with patch.object(sys, "argv", [
                "publish_digest.py", digest_path, "--dry-run",
            ]):
                with patch(
                    "publish_digest.markdown_to_html",
                    return_value=("<p>Body.</p>", "test"),
                ):
                    with patch("publish_digest.read_token",
                               side_effect=AssertionError("must not read token")):
                        with redirect_stdout(captured):
                            publish_digest.main()

            output = json.loads(captured.getvalue())
            for key in ("dry_run", "title", "converter", "content_bytes", "content_preview"):
                self.assertIn(key, output, f"Expected key {key!r} missing from dry-run output")
        finally:
            os.unlink(digest_path)


if __name__ == "__main__":
    unittest.main()
