#!/usr/bin/env python3
"""Upload a local file to a WordPress.com site's media library and return its URL.

Used by the `digest-audio-publish` skill to upload digest narration WAVs before it
publishes a post that links to them. Takes a file *path* only — the file's bytes are
sent as a multipart `media[]` field, never interpolated into a shell command.

The token is read from disk by this process and passed only in a request header, so it
never appears in a shell command line, in argv, or in this script's output. This mirrors
`scripts/publish_digest.py`; the token-reading and error-scrubbing logic are the same.
"""

import argparse
import json
import mimetypes
import os
import secrets
import stat
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_SITE = "genefish.wordpress.com"
DEFAULT_TOKEN_FILE = "~/.config/LabNotebook-Summarizer/wp_token"
API_BASE = "https://public-api.wordpress.com/rest/v1.1/sites/{site}/media/new/"
TIMEOUT = 120  # media files are larger than text posts; allow a generous upload window


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


def guess_mime(path: str) -> str:
    """Best-effort MIME type; WordPress needs one to accept the part."""
    mime, _ = mimetypes.guess_type(path)
    return mime or "application/octet-stream"


def build_multipart(file_path: str, mime: str, title: str = None):
    """Return (content_type_header, body_bytes) for a multipart/form-data upload.

    The file is sent as `media[]` (the field name the WordPress media endpoint expects
    for the file part). An optional title is sent as `attrs[0][title]`.
    """
    boundary = "----LabNotebookUpload" + secrets.token_hex(16)
    filename = os.path.basename(file_path)
    with open(file_path, "rb") as handle:
        file_bytes = handle.read()

    delimiter = f"--{boundary}\r\n".encode("utf-8")
    parts = []
    if title:
        parts.append(delimiter)
        parts.append(
            b'Content-Disposition: form-data; name="attrs[0][title]"\r\n\r\n'
        )
        parts.append(title.encode("utf-8"))
        parts.append(b"\r\n")

    parts.append(delimiter)
    # filename comes from os.path.basename of the caller-supplied path; quotes are
    # escaped so a crafted name cannot break out of the header.
    safe_name = filename.replace('"', "%22")
    parts.append(
        f'Content-Disposition: form-data; name="media[]"; filename="{safe_name}"\r\n'
        f"Content-Type: {mime}\r\n\r\n".encode("utf-8")
    )
    parts.append(file_bytes)
    parts.append(b"\r\n")
    parts.append(f"--{boundary}--\r\n".encode("utf-8"))

    body = b"".join(parts)
    return f"multipart/form-data; boundary={boundary}", body


def upload(site: str, token: str, file_path: str, mime: str, title: str = None):
    """POST the file to the media endpoint. Returns (http_status, parsed_body_or_text)."""
    content_type, body = build_multipart(file_path, mime, title)
    request = Request(
        API_BASE.format(site=site),
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": content_type,
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
    parser.add_argument("file", help="path to the media file to upload")
    parser.add_argument("--site", default=DEFAULT_SITE, help="WordPress.com site domain")
    parser.add_argument("--token-file", default=DEFAULT_TOKEN_FILE, help="path to the API token")
    parser.add_argument("--title", help="optional title for the media library item")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate the file and report what would be uploaded; do not read the "
        "token or contact the API",
    )
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        fail(f"File not found: {args.file}")
    size = os.path.getsize(args.file)
    if size == 0:
        fail(f"File is empty: {args.file}")
    mime = guess_mime(args.file)

    if args.dry_run:
        print(json.dumps(
            {
                "dry_run": True,
                "file": args.file,
                "filename": os.path.basename(args.file),
                "mime": mime,
                "size_bytes": size,
                "site": args.site,
                "title": args.title,
            },
            indent=2,
        ))
        return

    try:
        token, warnings = read_token(args.token_file)
    except (OSError, ValueError) as e:
        fail(str(e))

    try:
        status, payload = upload(args.site, token, args.file, mime, args.title)
    except (URLError, OSError) as e:
        fail(f"Could not reach the WordPress API: {e}. Check your network and retry.")
    finally:
        del token

    result = {
        "http_status": status,
        "file": args.file,
        "mime": mime,
        "size_bytes": size,
        "warnings": warnings,
    }

    if status in (200, 201):
        # The media endpoint returns a `media` list of uploaded items and an `errors`
        # list for parts it rejected. A 200 with an empty `media` list means the file
        # itself was not accepted, so treat that as a failure.
        media = payload.get("media") or []
        if not media:
            errors = payload.get("errors") or payload
            result["error"] = "Upload returned no media item; the file was rejected."
            result["response"] = errors
            print(json.dumps(result, indent=2))
            sys.exit(1)
        item = media[0]
        result.update({
            "status": "uploaded",
            "url": item.get("URL", ""),
            "media_id": item.get("ID", ""),
            "guid": item.get("guid", ""),
        })
        print(json.dumps(result, indent=2))
        return

    if status in (401, 403):
        result["error"] = (
            f"Authentication failed ({status}). Check that the token in "
            f"{args.token_file} is valid and may upload media to {args.site}; regenerate "
            "it at https://developer.wordpress.com/apps/ if needed."
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
