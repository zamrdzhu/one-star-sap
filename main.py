"""A one-line 1-star review from a houseplant about its human owner.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The 279-character gate is checked on every run so an over-long edit
can never slip through silently. The grievance is the plant's own:
watered never, apologised to anyway, dying politely by the window.
"""

import os
import sys

LINE = (
    "One star. My owner waters me when he remembers I exist, which "
    "is never, then apologises to a plant that cannot leave. I have "
    "been dying politely by this window since March."
)


def main() -> int:
    if not 1 <= len(LINE) <= 279:
        print(f"error: line is {len(LINE)} chars, must be 1-279",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
