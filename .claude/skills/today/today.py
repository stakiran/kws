"""Create today's daily page under wiki/ and open it in VSCode.

Usage:
    python .claude/skills/today/today.py

Behavior:
    - Compute today's date in yyyy-mm-dd (local time).
    - Target file: <repo-root>/wiki/<yyyy-mm-dd>.scb
    - If the file does not exist:
        - Create it as an empty file.
        - Prepend " [<yyyy-mm-dd>]" right after the "daily pages:" line in wiki/index.scb.
    - If the file already exists:
        - Do nothing to the filesystem (no edit, no overwrite).
    - Finally, open the target file in VSCode via `code <path>`.
    - Print one line of status: CREATED / EXISTS, plus the target path.

Notes:
    - Repo root is resolved as the script's parent at depth 3
      (.claude/skills/today/ -> repo root).
    - index.scb is expected to contain a line exactly matching "daily pages:".
      If not found, the script aborts with a non-zero exit and prints an error.
"""

import datetime
import pathlib
import subprocess
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
WIKI_DIR = REPO_ROOT / "wiki"
INDEX_PATH = WIKI_DIR / "index.scb"
DAILY_PAGES_MARKER = "daily pages:"


def prepend_link_to_index(date_str: str) -> None:
    if not INDEX_PATH.exists():
        print(f"ERROR: {INDEX_PATH} not found", file=sys.stderr)
        sys.exit(1)

    text = INDEX_PATH.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    marker_idx = None
    for i, line in enumerate(lines):
        if line.rstrip("\r\n") == DAILY_PAGES_MARKER:
            marker_idx = i
            break

    if marker_idx is None:
        print(f"ERROR: '{DAILY_PAGES_MARKER}' line not found in {INDEX_PATH}", file=sys.stderr)
        sys.exit(1)

    newline = "\r\n" if lines[marker_idx].endswith("\r\n") else "\n"
    new_link_line = f" [{date_str}]{newline}"

    lines.insert(marker_idx + 1, new_link_line)
    INDEX_PATH.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    today = datetime.date.today().strftime("%Y-%m-%d")
    target = WIKI_DIR / f"{today}.scb"

    if target.exists():
        status = "EXISTS"
    else:
        target.touch()
        prepend_link_to_index(today)
        status = "CREATED"

    subprocess.run(["code", str(target)], shell=True, check=False)
    print(f"{status}: {target}")


if __name__ == "__main__":
    main()
