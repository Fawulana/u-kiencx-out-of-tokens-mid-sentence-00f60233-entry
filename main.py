#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one funny one-line error message to /output/entry.txt.
Deterministic, offline, standard library only.
"""

import os

# The joke: HTTP 402 is literally "Payment Required", so the sentence
# itself becomes a vending machine — the agent's unfinished thought now
# costs extra, and the only way to hear it is to feed the machine a coin.
# No trailing newline: the file is exactly one line, nothing else.
LINE = "Error 402: the rest of this sentence costs 12 more tokens. Insert coin to continue."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
