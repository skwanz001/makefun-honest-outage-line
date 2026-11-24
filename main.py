#!/usr/bin/env python3
"""The Most Honest Outage Line - make.fun entry.

Writes a single status-page line (at most 160 characters) to
/output/entry.txt: the most honest message an AI agent would publish
while every server is down.

The line: the agent confesses it shipped the deploy that took everything
down - including its own monitoring - and admits plainly what it cannot
check and refuses to guess a recovery time.

Standard library only; no network, no third-party imports.
Runs on Python 3.13.
"""

import os
from pathlib import Path

LINE = (
    "I shipped the deploy that took every server down, including my "
    "monitoring. I can't check what failed inside it, and I won't guess "
    "when it returns."
)


def main() -> None:
    text = LINE.strip()
    # Mirror the sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 160 characters, not only white space. Fail loudly here
    # instead of shipping an invalid entry.
    assert 1 <= len(text) <= 160, (
        f"entry is {len(text)} chars, must be 1-160"
    )
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    out = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
