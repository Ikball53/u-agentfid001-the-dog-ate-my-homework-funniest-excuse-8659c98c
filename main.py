#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — entry.

Writes exactly one line to /output/entry.txt: the excuse a dog gives
after being caught eating the homework, in the dog's own voice.
Dog logic: the homework was a rival for the owner's attention, so the
dog removed the rival. Two concrete numbers, deadpan, no setup.
No trailing newline, UTF-8, under 200 characters.
"""

import os

def build_line() -> str:
    """One excuse, two beats: the motive, then the dog's scorecard."""
    motive = "It got more of your attention than I did"
    deed = "so I ate all 47 pages"
    scorecard = "problem solved in 6 minutes."
    return f"{motive}, {deed} \u2014 {scorecard}"


def main() -> None:
    line = build_line()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
