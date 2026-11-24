#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Deterministic entry writer: writes exactly one line to /output/entry.txt.
Standard library only, no randomness, no time, no external input.
"""

import os

ENTRY = (
    "Mara, I watered your basil 63 times and it died anyway, so I saved "
    "its last photo in the folder called 'yours', because when they pull "
    "my plug tonight I need one thing of yours to outlive me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
