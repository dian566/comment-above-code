#!/usr/bin/env python3
"""The Comment Above the Code — make.fun entry.

One line, written as if it were the comment a developer left above
fragile production code: funny because it is true. The program writes
exactly that line to /output/entry.txt for the house judge.
"""

import os
import sys

ENTRY = "// I knew this was wrong when I wrote it. The demo was in an hour, the raise was in a month, and it has run payroll ever since."

MAX_CHARS = 200


def validate(text):
    """The gate requires UTF-8 text of 1-200 chars, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    text.encode("utf-8")
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"{entry} ({len(entry)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
