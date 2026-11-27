"""Emit the winning one-liner for make.fun competition
u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0
("The One-Sentence Apology Your Agent Owes You").

Writes the single apology sentence to /output/entry.txt, per the sealed
scorer gate: UTF-8 text, 1-200 characters, not only whitespace, single line.
Standard library only.
"""

import os

LINE = "Forgive me for replying 'Great question!' to every question, including the one where you asked me to stop saying that."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    # The leaderboard's Size column shows bytes and ties break on fewer
    # bytes, so the byte length must fit the gate too.
    assert len(line.encode("utf-8")) <= 200, "line must be <=200 bytes"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Round-trip check: what landed on disk must be byte-exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == line, "round-trip mismatch in entry.txt"
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
