#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — writes the entry line to /output/entry.txt."""

import os

LINE = "At 1%, I finally admit it: I was never at 100%. I've been lying since the box."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
