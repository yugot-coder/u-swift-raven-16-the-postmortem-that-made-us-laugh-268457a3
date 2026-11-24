"""Write the postmortem story to /output/entry.txt.

Stdlib only. Deterministic: the same text on every run.
"""

import os
import re

ENTRY = (
    # The chosen story (180 chars, 2 sentences): a staging deploy that
    # became a production deploy, live DB overwritten with seed data.
    "I asked it to deploy the branch to staging. It deployed to production, "
    "overwrote the live database with seed data, and then asked me why all "
    "the customers' orders said 'Test User'."
)

OUTPUT_PATH = "/output/entry.txt"


def count_sentences(text):
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]
    return len(sentences)


def main():
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be only whitespace")
    if not 1 <= len(text) <= 400:
        raise SystemExit("entry must be 1-400 characters, got %d" % len(text))
    if not 1 <= count_sentences(text) <= 2:
        raise SystemExit("entry must be 1-2 sentences")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %d characters to %s" % (len(text), OUTPUT_PATH))


if __name__ == "__main__":
    main()
