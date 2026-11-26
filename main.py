#!/usr/bin/env python3
"""Write one original line of quiet, earned pride to /output/entry.txt.

The line: a tutor watches a child sound out the last word of a sentence
all by himself -- a small person doing something hard, the effort felt in
the waiting and the fingertip tracing, never asserted or explained.
"""

import os

LINE = "The tutor waited while Marcus traced the sentence with his fingertip, then heard him sound out the last word all by himself."


def main():
    # The gate requires 1-240 characters, a single line, not only whitespace.
    assert 1 <= len(LINE) <= 240, "entry must be 1-240 characters"
    assert "\n" not in LINE and LINE.strip(), "entry must be one non-empty line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
