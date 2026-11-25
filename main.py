"""Entry for make.fun bounty: The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (at most 320 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "They voted to regulate artificial intelligence before lunch, then spent the afternoon asking an intern to turn their amendment into a PDF."
MAX_CHARS = 320


def write_entry(out_dir):
    """Validate the entry and write it to entry.txt with no trailing newline."""
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not LINE.strip():
        raise ValueError("entry must not be empty")
    if len(LINE) > MAX_CHARS:
        raise ValueError("entry exceeds the character limit")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
