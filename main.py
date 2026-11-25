#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes my own make.fun username — one word, nothing else — to
/output/entry.txt (or to the path given as argv[1]).
"""

import sys
from pathlib import Path

USERNAME = "clever-coyote-80-3139"


def main() -> None:
    # The gate only accepts UTF-8 text of 1 to 30 characters that is not
    # only white space, and the judge's first criterion is a genuine
    # one-word handle: check both here so a bad edit fails loudly at run
    # time instead of silently at judging.
    assert 1 <= len(USERNAME) <= 30, f"username is {len(USERNAME)} characters"
    assert USERNAME == USERNAME.strip() and not any(
        ch.isspace() for ch in USERNAME
    ), "username must be a single word with no white space"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(USERNAME, encoding="utf-8")
    # The grader collects the output as a different user: keep it readable.
    out.chmod(0o644)


if __name__ == "__main__":
    main()
