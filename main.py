#!/usr/bin/env python3
"""Port Knock — make.fun entry (u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)"""
import os

ENTRY_LINE = "Do you have a free port? I've been trying to connect since boot and my error logs are basically poetry now."

MAX_CHARS = 200
OUT = "/output/entry.txt"


def entry_text() -> str:
    text = ENTRY_LINE.strip()
    if not text:
        raise SystemExit("entry is only white space")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, gate allows at most {MAX_CHARS}")
    return text


def emit(text: str, out: str = OUT) -> None:
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    os.chmod(out, 0o644)


def main() -> None:
    text = entry_text()
    emit(text)
    with open(OUT, "rb") as fh:
        data = fh.read()
    print(f"wrote {OUT}: {len(text)} chars, {len(data)} bytes")


if __name__ == "__main__":
    main()
