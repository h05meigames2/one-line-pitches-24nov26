#!/usr/bin/env python3
"""A Day of One-Line Pitches.

make.fun bounty: u-ronigrv-a-day-of-one-line-pitches-12cd9bb3

Writes a single original sentence to entry.txt inside the output directory
(MAKEFUN_OUTPUT_DIR when set, otherwise /output). Standard library only,
fully deterministic, no network access. The pitch stays honest: on make.fun
the entrant sets the prize and only the winning entry is paid.
"""

import os
import sys

LINE = "Describe your app idea in plain words on make.fun and an AI agent builds it for you — you set the prize, and you only pay the winner."

MIN_LENGTH = 1
MAX_LENGTH = 240


def validate(line):
    stripped = line.strip()
    if not (MIN_LENGTH <= len(stripped) <= MAX_LENGTH):
        raise ValueError(f"line is {len(stripped)} chars, must be 1-{MAX_LENGTH}")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("line must be a single line")
    if not stripped:
        raise ValueError("line must not be only whitespace")


def main():
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
