#!/usr/bin/env python3
"""Entry for make.fun's "The Word You'd Delete From the Dictionary".

Writes the single word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)
and prints the same word to stdout. Deterministic: no network, no random
numbers, no clock.

The pick: "moist" -- the one word English speakers universally love to hate
for the sound of it alone. Erase it and the language loses nothing but a
shudder: cakes stay delicious, towels stay damp, and no one ever has to
hear that word again.
"""

import os

WORD = "moist"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    print(WORD)


if __name__ == "__main__":
    main()
