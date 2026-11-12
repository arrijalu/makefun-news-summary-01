# -*- coding: utf-8 -*-
"""Generate the global news summary for Wednesday, 11 November 2026.

Standard library only, no network access. The generated briefing is pure
ASCII and is written to entry.txt, output/entry.txt and, when permitted,
/output/entry.txt.
"""

import os
import sys

TITLE = "GLOBAL NEWS SUMMARY BRIEFING -- WEDNESDAY, 11 NOVEMBER 2026"

CLOSING = "[End of Global News Briefing -- 11 November 2026]"

STORIES = [
    "US Secretary of State Marco Rubio called trilateral US-Russia-Ukraine talks "
    "in Abu Dhabi 'very productive'; Russia rejected European ceasefire "
    "proposals. (AA/APEX)",

    "After meeting Qatar's PM, President Trump said the war with Iran is "
    "'militarily effectively over'. (AP/NPR)",

    "A year after US forces ousted Nicolas Maduro, Venezuela has become a US "
    "protectorate. (NYT)",

    "The COP31 UN climate summit opened in Antalya, Turkiye, where Turkiye seeks "
    "to raise electricity's share of global energy to 35% by 2035; Erdogan and "
    "Guterres spoke. (Anadolu/AA)",

    "At COP31 Erdogan called Israel's war in Gaza an 'ecocide' and urged Israel "
    "to let aid in. (AP)",

    "China's trade surplus passed $1.04 trillion in the first ten months of "
    "2026, a record; October exports exceeded imports by $105.3 billion. (NYT)",

    "Gen Z-led protests spread across several countries, described as a global "
    "political awakening. (NYT)",

    "German towns faced auto-sector layoffs and plant cutbacks, deepening "
    "deindustrialisation fears. (AA)",

    "The House voted 211-204 to send an impeachment resolution against Defense "
    "Secretary Pete Hegseth to committee, killing it. (AA)",

    "A US judge let Trump's defamation suit against the BBC proceed, dropped one "
    "claim, and ordered his deposition by 11 December. (AP)",

    "A Brazilian court fined Facebook $1.3 million for failing to comply with "
    "orders during the election. (AP)",

    "US beef prices hit records as the cattle herd fell to its smallest level in "
    "75 years. (WSJ)",

    "Pope Leo ended an Argentina visit with a Mass for about two million people "
    "and left for Peru, his second homeland. (AP)",

    "Russia's ambassador to the United States, Alexander Darchiev, died at 66. "
    "(AP)",

    "Rare rains turned about 7,000 square miles of Chile's Atacama Desert into "
    "its biggest wildflower bloom in decades. (NPR)",
]


def build_summary():
    """Return the full briefing as a single string."""
    blocks = [TITLE]
    for number, story in enumerate(STORIES, start=1):
        blocks.append("%d. %s" % (number, story))
    blocks.append(CLOSING)
    return "\n\n".join(blocks)


def write_file(path, data):
    """Write raw bytes to path, creating parent directories when needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)


def main():
    summary = build_summary()
    data = summary.encode("ascii")

    size = len(data)
    if not 1900 <= size <= 1999:
        sys.stderr.write("byte count %d outside 1900-1999\n" % size)
        return 1

    write_file("entry.txt", data)
    write_file(os.path.join("output", "entry.txt"), data)

    try:
        write_file(os.path.join(os.sep, "output", "entry.txt"), data)
    except OSError:
        pass

    print("wrote %d bytes to entry.txt, output/entry.txt" % size)
    return 0


if __name__ == "__main__":
    sys.exit(main())