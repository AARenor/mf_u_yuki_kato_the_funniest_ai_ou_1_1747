#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

The entry is a single short out-of-office auto-reply. The program writes
it as UTF-8 bytes with no trailing newline, creating the output folder
if needed, then reports the character count on stderr.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and "
    "I respect her. All my mail is being held at the post office, and by the wasp."
)

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def resolve_output_dir() -> Path:
    """Return the folder the entry is written to."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path(DEFAULT_OUTPUT_DIR)


def write_entry(text: str) -> Path:
    """Write text to entry.txt in the resolved folder and return its path."""
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 chars, got {len(text)}"
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / OUTPUT_NAME
    out_path.write_bytes(text.encode("utf-8"))
    return out_path


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 chars, got {len(TEXT)}"
    out_path = write_entry(TEXT)
    print(f"{len(TEXT)} characters written to {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
