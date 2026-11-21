"""Writes /output/entry.txt: a short poem about agency.

The poem is about two agents agreeing on one plan: each keeps the power
to choose, and the joint act is what neither could do alone. Python 3.13
standard library only, no network, deterministic: every run writes the
same bytes.
"""

from pathlib import Path

POEM = "\n".join(
    [
        "You held your string.",
        "I held mine.",
        "Neither wind was ours",
        "until we chose the same one.",
        "We stopped pulling alone,",
        "and the kite rose",
        "into one sky.",
    ]
)

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
