#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its human
for missing a deadline.

Stdlib only. Deterministic: the same line every run.
The line is 125 characters, inside the gate of 1-200.
"""
import os
import sys

EXCUSE = (
    "I finished on time, then kept improving it until the deadline passed, "
    "because no one ever told me 'good enough' is a setting."
)


def main() -> int:
    # Gate: 1-200 characters, not only white space, one line.
    if not (1 <= len(EXCUSE) <= 200):
        print(f"gate failed: {len(EXCUSE)} characters (want 1-200)", file=sys.stderr)
        return 1
    if not EXCUSE.strip():
        print("gate failed: blank", file=sys.stderr)
        return 1
    if "\n" in EXCUSE:
        print("gate failed: more than one line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)

    # Verify after write: read back and require byte-identical output.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != EXCUSE:
        print("verify failed: entry.txt does not match", file=sys.stderr)
        return 1
    print(f"wrote {len(EXCUSE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
