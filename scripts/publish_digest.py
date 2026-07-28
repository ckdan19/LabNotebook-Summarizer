#!/usr/bin/env python3
"""Convert a Markdown digest to sanitized HTML and post it to WordPress.com as a draft.

The token is read from disk by this process and passed only in a request header, so it
never appears in a shell command line, in argv, or in this script's output. Digest text
is never interpolated into a shell command — it is read and JSON-encoded in-process.
"""

import argparse
import html
import json
import os
import re
import stat
import subprocess
import sys
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_SITE = "genefish.wordpress.com"
DEFAULT_TOKEN_FILE = "~/.config/LabNotebook-Summarizer/wp_token"
API_BASE = "https://public-api.wordpress.com/rest/v1.1/sites/{site}/posts/new/"
TIMEOUT = 30

# Digest bodies are built from third-party notebook posts, so the HTML that reaches
# WordPress is sanitized against an allowlist: unknown tags are dropped, all text is
# escaped, and only these attributes survive.
ALLOWED_TAGS = {
    "p", "br", "hr", "h1", "h2", "h3", "h4", "h5", "h6", "strong", "em", "b", "i",
    "code", "pre", "blockquote", "ul", "ol", "li", "a", "img", "del", "sup", "sub",
    "table", "thead", "tbody", "tr", "th", "td",
}
VOID_TAGS = {"br", "hr", "img"}
DROP_WITH_CONTENT = {"script", "style", "iframe", "object", "embed", "form"}
ALLOWED_ATTRS = {"a": {"href", "title"}, "img": {"src", "alt", "title"}}
ALLOWED_SCHEMES = ("http://", "https://", "mailto:")


class Sanitizer(HTMLParser):
    """Rebuild HTML from an allowlist. Anything not explicitly permitted is escaped."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in DROP_WITH_CONTENT:
            self.skip_depth += 1
            return
        if self.skip_depth or tag not in ALLOWED_TAGS:
            return  # drop the tag itself, keep any text inside it
        kept = ""
        for name, value in attrs:
            if name not in ALLOWED_ATTRS.get(tag, set()) or value is None:
                continue
            if name in ("href", "src") and not value.lower().startswith(ALLOWED_SCHEMES):
                continue
            kept += f' {name}="{html.escape(value, quote=True)}"'
        self.parts.append(f"<{tag}{kept}{' /' if tag in VOID_TAGS else ''}>")

    def handle_endtag(self, tag):
        if tag in DROP_WITH_CONTENT:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth or tag not in ALLOWED_TAGS or tag in VOID_TAGS:
            return
        self.parts.append(f"</{tag}>")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_data(self, data):
        if not self.skip_depth:
            self.parts.append(html.escape(data, quote=False))

    def result(self):
        self.close()
        return "".join(self.parts)


def sanitize(raw_html: str) -> str:
    parser = Sanitizer()
    parser.feed(raw_html)
    return parser.result()


def plain_text(raw: str) -> str:
    """Flatten a heading to plain text — the post title must not carry markup."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", raw))).strip()


def read_token(path: str):
    """Return (token, warnings). Never log or return the token in any other channel."""
    resolved = os.path.expanduser(path)
    if not os.path.isfile(resolved):
        raise FileNotFoundError(
            f"WordPress token not found. Create {path} containing your WordPress.com "
            "API access token (generate one at https://developer.wordpress.com/apps/)."
        )
    warnings = []
    mode = stat.S_IMODE(os.stat(resolved).st_mode)
    if mode & 0o077:
        warnings.append(
            f"Token file {path} is readable by other users (mode {mode:04o}); "
            f"run: chmod 600 {path}"
        )
    with open(resolved, encoding="utf-8") as handle:
        token = handle.read().strip()
    if not token:
        raise ValueError(f"WordPress token file {path} is empty.")
    return token, warnings


def split_digest(path: str):
    """Return (title, body). The first line must be the Markdown H1 used as the title."""
    with open(path, encoding="utf-8") as handle:
        lines = handle.readlines()
    if not lines:
        raise ValueError(f"Digest file {path} is empty.")
    first = lines[0].strip()
    if not first.startswith("# "):
        raise ValueError(
            f"Digest file {path} does not start with a Markdown '# ' heading "
            f"(found: {first[:60]!r}); cannot derive a post title."
        )
    # The heading becomes the WordPress post title, so it is dropped from the body to
    # avoid showing up twice.
    return plain_text(first[2:]), "".join(lines[1:]).lstrip("\n")


def markdown_to_html(body: str):
    """Return (html, converter_name). Raises RuntimeError if no converter is available."""
    try:
        import markdown
    except ImportError:
        pass
    else:
        extensions = ["tables", "fenced_code", "nl2br"]
        return markdown.markdown(body, extensions=extensions), "python-markdown"

    try:
        # markdown-raw_html keeps pandoc from passing embedded HTML straight through.
        completed = subprocess.run(
            ["pandoc", "--from", "markdown-raw_html", "--to", "html"],
            input=body, capture_output=True, text=True, check=True,
        )
    except FileNotFoundError:
        raise RuntimeError(
            "Could not convert Markdown to HTML — install python-markdown "
            "(pip install markdown) or pandoc."
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"pandoc failed: {e.stderr.strip()[:300]}")
    return completed.stdout, "pandoc"


def post_draft(site: str, token: str, title: str, content: str):
    """POST the draft. Returns (http_status, parsed_body_or_text)."""
    payload = json.dumps({"title": title, "content": content, "status": "draft"})
    request = Request(
        API_BASE.format(site=site),
        data=payload.encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    def scrub(value):
        # Error bodies get reported back to the user, so make sure a server that
        # reflects the credential cannot get it printed.
        return json.loads(json.dumps(value).replace(token, "[redacted]"))

    try:
        with urlopen(request, timeout=TIMEOUT) as resp:
            return resp.status, scrub(json.loads(resp.read().decode("utf-8")))
    except HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        try:
            return e.code, scrub(json.loads(raw))
        except json.JSONDecodeError:
            return e.code, scrub({"raw": raw[:1000]})


def fail(message: str, **extra):
    print(json.dumps({"error": message, **extra}, indent=2))
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("digest", help="path to the Markdown digest to publish")
    parser.add_argument("--site", default=DEFAULT_SITE, help="WordPress.com site domain")
    parser.add_argument("--token-file", default=DEFAULT_TOKEN_FILE, help="path to the API token")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="convert and sanitize only; do not read the token or contact the API",
    )
    args = parser.parse_args()

    try:
        title, body = split_digest(args.digest)
    except (OSError, ValueError) as e:
        fail(str(e))

    try:
        raw_html, converter = markdown_to_html(body)
    except RuntimeError as e:
        fail(str(e))

    content = sanitize(raw_html)
    removed = len(re.findall(r"<[a-zA-Z]", raw_html)) - len(re.findall(r"<[a-zA-Z]", content))

    if args.dry_run:
        print(json.dumps(
            {
                "dry_run": True,
                "digest": args.digest,
                "title": title,
                "converter": converter,
                "tags_removed_approx": max(0, removed),
                "content_bytes": len(content),
                "content_preview": content[:1500],
            },
            indent=2,
        ))
        return

    try:
        token, warnings = read_token(args.token_file)
    except (OSError, ValueError) as e:
        fail(str(e))

    try:
        status, payload = post_draft(args.site, token, title, content)
    except (URLError, OSError) as e:
        fail(f"Could not reach the WordPress API: {e}. Check your network and retry.")
    finally:
        del token

    result = {
        "http_status": status,
        "title": title,
        "converter": converter,
        "tags_removed_approx": max(0, removed),
        "warnings": warnings,
    }

    if status in (200, 201):
        result.update({
            "status": "draft created",
            "url": payload.get("URL", ""),
            "short_url": payload.get("short_URL", ""),
            "post_id": payload.get("ID", ""),
        })
        print(json.dumps(result, indent=2))
        return

    if status in (401, 403):
        result["error"] = (
            f"Authentication failed ({status}). Check that the token in "
            f"{args.token_file} is valid and may post to {args.site}; regenerate it at "
            "https://developer.wordpress.com/apps/ if needed."
        )
    elif status == 404:
        result["error"] = f"{args.site} was not found or is not accessible with this token (404)."
    else:
        result["error"] = f"WordPress API returned {status}."
        result["response"] = payload
    print(json.dumps(result, indent=2))
    sys.exit(1)


if __name__ == "__main__":
    main()
