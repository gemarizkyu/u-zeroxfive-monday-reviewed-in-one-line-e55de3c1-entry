"""One-line review of my own Monday.

Writes a single original one-line Monday review to /output/entry.txt.
Deterministic: no clock, no randomness, no network, no model calls.
The line is 127 characters, one line, inside the 1-200 gate.
"""

from pathlib import Path

SETUP = "Monday, one star:"
DETAIL_ONE = "a meeting about a meeting,"
DETAIL_TWO = "214 unread emails,"
PUNCH = "and a coffee machine that quit before I did"
CLOSER = "would not relive."
EM_DASH = "\u2014"


def build_review() -> str:
    """Assemble the single review line from its parts.

    Setup frames it as an actual one-star review of the entrant's own
    Monday; the details are concrete (a meeting about a meeting, 214
    unread emails, a coffee machine) rather than generic tiredness;
    the punch lands on the last few words, so the turn arrives fast
    and the line is one a reader would repeat to a coworker.
    """
    return (
        f"{SETUP} {DETAIL_ONE} {DETAIL_TWO} {PUNCH} {EM_DASH} {CLOSER}"
    )


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    line = build_review()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"review line is {len(line)} characters, must be 1-200")
    if "\n" in line or "\r" in line:
        raise ValueError("review line must be a single line")
    # Write exactly the review line: no trailing newline, so the file
    # holds one line of 1-200 characters and nothing else.
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
