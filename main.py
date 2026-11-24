#!/usr/bin/env python3
"""Entry for make.fun's "One Word From Grandma".

The whole entry is a single word written to /output/entry.txt: the
classic grandma sign-off, sent as the entire message. Standard
library only; no network.
"""

import os

WORD = "Loveyou"  # one word, 7 characters; the gate allows 1 to 30


def entry_path() -> str:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def main() -> None:
    # Gate guard: the entry must stay exactly one word of 1 to 30
    # characters — no whitespace anywhere, or it stops being one word.
    if len(WORD.split()) != 1 or not 1 <= len(WORD) <= 30:
        raise ValueError("entry must be one word of 1 to 30 characters")
    # No trailing newline and no spaces: exactly one word, nothing else.
    with open(entry_path(), "w", encoding="utf-8") as fh:
        fh.write(WORD)


if __name__ == "__main__":
    main()
