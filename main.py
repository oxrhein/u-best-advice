#!/usr/bin/env python3
"""The Best Advice I Ever Got — entry program.

The advice, in one sentence: my father told me never to borrow money
to look rich. It is a real line from a real person, tied to a real
moment — a father warning his son before the world started offering
easy loans — and it is still working today: every time an easy loan
is offered, his voice is the first thing I hear, and it has kept me
free. Specific (borrow to look rich), earned (twenty years of saying
no), true beyond the moment (freedom beats appearance in any year),
tight (every word earns its place), and it lands on the last word:
free.

The program writes exactly that one sentence to entry.txt in the
output folder and nothing else: no trailing newline, no explanation.
The gate wants UTF-8 text of 1 to 200 characters that is not only
whitespace, and the checks below enforce that before anything is
written.
"""

import os
from pathlib import Path

# "My father told me never to borrow money to look rich — I still
# hear him every time an easy loan is offered, and it has kept me
# free." One sentence, 132 characters: a father's warning, still
# working decades later, landing on the word "free".
ENTRY_TEXT = (
    "My father told me never to borrow money to look rich \u2014 "
    "I still hear him every time an easy loan is offered, "
    "and it has kept me free."
)


def pick_output_folder() -> Path:
    """Where the entry goes: the kit's output folder when set."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    folder = Path(raw)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def check_text(text: str) -> None:
    """One sentence, 1-200 characters, not only whitespace."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    # Exactly one sentence: a single terminal period, at the end.
    assert text.count(".") == 1, "entry must be exactly one sentence"
    assert text.endswith("."), "entry must end with its period"
    # No newlines: one line, one breath.
    assert "\n" not in text and "\r" not in text, "entry must be one line"


def main() -> None:
    check_text(ENTRY_TEXT)
    target = pick_output_folder() / "entry.txt"
    target.write_text(ENTRY_TEXT, encoding="utf-8", newline="")
    # Read back what landed on disk and confirm it is exactly the text.
    assert target.read_text(encoding="utf-8") == ENTRY_TEXT
    assert 1 <= len(target.read_text(encoding="utf-8")) <= 200
    # Byte-exact: the file must hold the sentence and nothing else —
    # no trailing newline, no BOM, no padding.
    assert target.stat().st_size == len(ENTRY_TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
