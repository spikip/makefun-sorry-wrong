"""Entry for the make.fun bounty "Sorry, I Heard That Wrong".

The program writes a single line to /output/entry.txt: an apology
for a mishearing. The joke is the swap — "bring snacks" heard as
"bring facts" — which is funny because the two words are nothing
alike, yet the mistake is entirely believable in a loud room. The
payoff is the result: the speaker arrived empty-handed and
overprepared, which is the exact opposite of what the party
needed and the exact opposite of what the speaker intended. The
apology does not grovel; it reports the damage with the confidence
of someone who brought a lecture to a potluck. The gate allows 1
to 140 characters of UTF-8 text, so the line is checked against
that cap before it is written.
"""

import os

# The mishearing is the whole joke: snacks became facts, so the
# speaker arrived empty-handed and overprepared — wrong in both
# directions at once. Confidence after the mistake is the charm.
ENTRY = (
    "Sorry, I heard 'bring snacks' as 'bring facts', so I arrived "
    "empty-handed and overprepared."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # One line, no trailing newline: the gate counts characters, so
    # the entry is written exactly as judged.
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
