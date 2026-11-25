"""Monday Morning Punchlines entry.

Writes one Monday-morning joke to /output/entry.txt.
Deterministic: same bytes on every run, no input, no network.

The line (138 characters, inside the 1-200 gate) was picked by
head-to-head comparison of three candidates. It beat the
"muted my will to live" line (tired trope) and the "Monday in my
hoodie eating leftovers" line (softer punch): the loan-shark
escalation -- weekend, then Tuesday too -- lands the hardest.
"""

import os
from pathlib import Path

LINE = (
    # The joke: Monday personified as a loan shark collecting the
    # weekend, then coming back for Tuesday. The punch is the last
    # image ("a loan shark in a tie") -- a fresh twist, not a
    # complaint, and it shares no words with Dimas's two earlier
    # Monday lines (no alarm, no coffee, no unread emails).
    "Monday asked me for my weekend back. I handed it over, then it "
    "asked for Tuesday too, and I realized Monday is just a loan "
    "shark in a tie."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
