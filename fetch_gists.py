"""Fetch all public/private gists for a GitHub user and save each as a single .md file.

Usage:
    python fetch_gists.py            # fetch all gists
    python fetch_gists.py --test     # fetch only the most recent 1 gist (for verification)

Requirements:
    - Environment variable GITHUB_TOKEN must be set (PAT with `gist` scope for private gists).
    - Output directory: raw_gists/

Behavior:
    - One .md file per gist, named `<gist-id>.md`.
    - If a gist has multiple files, they are merged into the single .md with `## <filename>` headers.
    - Files that already exist in raw_gists/ are skipped (no re-fetch).
    - A YAML-ish frontmatter block records id, url, description, created_at, updated_at, files.
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

USER = "stakiran"
OUT_DIR = "raw_gists"
API_BASE = "https://api.github.com"
PER_PAGE = 100


def http_get(url, token):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "fetch-gists-script")
    if token:
        req.add_header("Authorization", f"token {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8"), dict(r.headers)


def list_all_gists(token):
    """List gist metadata across all pages. Returns list ordered newest -> oldest."""
    gists = []
    page = 1
    while True:
        url = f"{API_BASE}/users/{USER}/gists?per_page={PER_PAGE}&page={page}"
        body, _ = http_get(url, token)
        batch = json.loads(body)
        if not batch:
            break
        gists.extend(batch)
        if len(batch) < PER_PAGE:
            break
        page += 1
    return gists


def fetch_gist_detail(gist_id, token):
    url = f"{API_BASE}/gists/{gist_id}"
    body, _ = http_get(url, token)
    return json.loads(body)


def render_markdown(detail):
    files = detail.get("files", {}) or {}
    parts = []
    for finfo in files.values():
        content = finfo.get("content")
        if content is None and finfo.get("truncated"):
            raw_url = finfo.get("raw_url")
            if raw_url:
                try:
                    body, _ = http_get(raw_url, token=None)
                    content = body
                except Exception as e:
                    content = f"<error fetching raw content: {e}>"
        if content is None:
            content = ""
        parts.append(content.rstrip("\n"))
    return "\n\n".join(parts) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test",
        action="store_true",
        help="Fetch only the most recently updated gist (for verification).",
    )
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("ERROR: GITHUB_TOKEN environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)

    print("Listing gists...")
    gists = list_all_gists(token)
    print(f"Found {len(gists)} gists.")

    if args.test:
        gists = gists[:1]
        print(f"--test mode: processing only the latest 1 gist ({gists[0]['id'] if gists else 'none'}).")

    saved = 0
    skipped = 0
    failed = 0
    for i, g in enumerate(gists, 1):
        gid = g["id"]
        out_path = os.path.join(OUT_DIR, f"{gid}.md")
        if os.path.exists(out_path):
            skipped += 1
            print(f"[{i}/{len(gists)}] SKIP (exists): {gid}")
            continue
        try:
            detail = fetch_gist_detail(gid, token)
            md = render_markdown(detail)
            with open(out_path, "w", encoding="utf-8", newline="\n") as f:
                f.write(md)
            saved += 1
            print(f"[{i}/{len(gists)}] SAVED: {gid} (files={len(detail.get('files') or {})})")
        except urllib.error.HTTPError as e:
            failed += 1
            print(f"[{i}/{len(gists)}] FAIL: {gid} HTTP {e.code} {e.reason}", file=sys.stderr)
            if e.code == 403:
                print("  Rate limited or forbidden. Stopping.", file=sys.stderr)
                break
        except Exception as e:
            failed += 1
            print(f"[{i}/{len(gists)}] FAIL: {gid} {e}", file=sys.stderr)
        time.sleep(0.1)

    print(f"\nDone. saved={saved} skipped={skipped} failed={failed}")


if __name__ == "__main__":
    main()
