"""One Line, No Deadline Met — make.fun entry (Account B).

Writes a single-line joke giving an excuse for a missed deadline to
/output/entry.txt. The gate requires UTF-8 text of 1-200 characters, not
only whitespace, and nothing else: no second line, no picture, no link.

The joke: the excuse blames the Wi-Fi for delivering the work to the
wrong year. It reads like something a person would actually say in a
stand-up ("sorry boss, the file went to 2019"), and the turn is that the
submission *was* on time — just delivered straight to a year where nobody
can read it. "Straight to" lands the punch harder than "just delivered".
"""

import os

ENTRY = "I submitted it on time \u2014 my Wi-Fi delivered it straight to 2019."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
