#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — entrypoint.

Writes the final one-line warning label to /output/entry.txt.
Deterministic, no network, no environment secrets, no dependencies.

The label (65 chars): the paradox is the joke itself — the warning you are
reading is the very warning your younger self ignored, and "then, too"
closes the loop on the reader. Phrased as a genuine safety notice so the
joke cuts against official calm.
"""

import os

LABEL = "WARNING: Do not warn your younger self. He ignored you then, too."


def main() -> None:
    text = LABEL.strip()
    assert 1 <= len(text) <= 120, "label must be 1-120 characters"
    assert "\n" not in text, "label must be a single line"
    assert text.startswith("WARNING: "), "label must read as a safety notice"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
