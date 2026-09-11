#!/usr/bin/env python3
"""Strip a SPEAKER_SCRIPT.md down to the words actually said, for printing.

`SPEAKER_SCRIPT.md` is a working document: budget tables, a cut ladder, Q&A
tiers, a register note, a number ledger, a decisions log, and every parked beat
kept against the day it comes back. None of that helps at the lectern, and on
paper it buries the thing you are reading from.

This keeps only:
  - the act headers, as dividers
  - one heading per spoken beat: frame number, title, and its measured length
  - the words, with [CLICK] cues and 〔stage directions〕 intact

and drops HTML comments (parked wording), blockquote notes, markdown tables,
and every beat marked SKIP.

It also stamps a RUNNING TOTAL on each beat -- "≈ 12:40 in" -- which the source
document cannot carry, because it is the one number that tells you mid-talk
whether you are ahead or behind.

    tools/print-script.py PhD_Defense_2026            # -> SPEAKER_SCRIPT_PRINT.md
    tools/print-script.py PhD_Defense_2026 --wpm 121
    tools/print-script.py PhD_Defense_2026 --qa       # append the Q&A tiers

Regenerate it after editing the script; it is derived, never edited by hand.
"""
import io, os, re, sys

WPM = 121.0
HEAD = re.compile(r"^##\s+(?P<id>[A-Z][\w.]*)\s+—\s+(?P<title>.*?)\s*$")
FRAMEREF = re.compile(r"·\s*frames?\s+(\d+)(?:\s*[–-]\s*(\d+))?", re.I)


def spoken_words(text):
    """Same counting rule as measure-script.py, so the two agree."""
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    keep = [l for l in text.split("\n")
            if not l.lstrip().startswith((">", "#", "|", "<!--"))]
    t = "\n".join(keep)
    t = re.sub(r"〔[^〕]*〕", " ", t, flags=re.S)
    t = re.sub(r"\[CLICK[^\]]*\]", " ", t)
    t = re.sub(r"\*\*▲\*\*|▲", " ", t)
    t = re.sub(r"`[^`]*`", " ", t)
    t = re.sub(r"[*_]{1,2}", "", t)
    return len(re.findall(r"[A-Za-z0-9][\w'’\-–]*", t))


def clean(body):
    """The body as it should read on paper."""
    txt = re.sub(r"<!--.*?-->", "", "\n".join(body), flags=re.S)   # parked wording
    out = []
    for line in txt.split("\n"):
        s = line.lstrip()
        if s.startswith(">") or s.startswith("|"):                 # notes, tables
            continue
        out.append(line.rstrip())
    txt = "\n".join(out)
    # the source separates beats with "---", and stacks two of them before an act
    # header; on paper a doubled rule reads as a mistake
    txt = re.sub(r"(?m)^-{3,}\s*$", "---", txt)
    txt = re.sub(r"(?:^|\n)---\s*(?:\n---\s*)+", "\n---\n", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    txt = re.sub(r"(?:\n---\s*)+$", "", txt)          # no rule at the end of a beat
    return txt.strip()


def mmss(minutes):
    t = int(round(minutes * 60))
    return "%d:%02d" % (t // 60, t % 60)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    d = sys.argv[1].rstrip("/")
    global WPM
    if "--wpm" in sys.argv:
        WPM = float(sys.argv[sys.argv.index("--wpm") + 1])
    root = os.path.dirname(os.path.abspath(__file__)) + "/.."
    src = io.open(os.path.join(root, d, "SPEAKER_SCRIPT.md"),
                  encoding="utf-8").read().split("\n")

    # ---- collect acts and beats, in order, ignoring every other section
    # Act 0 has no "# Act 0" header -- the beats simply follow the document title --
    # so the title line must not be mistaken for the start of the working material.
    items, cur, in_tail, seen_title = [], None, False, False
    for line in src:
        m = HEAD.match(line)
        if m:
            cur = {"kind": "beat", "id": m.group("id"),
                   "title": m.group("title"), "body": []}
            # a beat is only a beat if it names a frame and is not parked
            if not FRAMEREF.search(cur["title"]) or " SKIP" in cur["title"].upper():
                cur = None
            elif in_tail:
                cur = None
            else:
                items.append(cur)
            continue
        if line.startswith("# "):
            cur = None
            head = line[2:].strip()
            if not seen_title:
                seen_title = True          # the document title, not a section
            elif head.startswith("Act "):
                items.append({"kind": "act", "title": head})
                in_tail = False
            else:
                # everything from the parked beats onward is working material
                in_tail = True
            continue
        if line.startswith("#"):
            cur = None
            continue
        if cur is not None:
            cur["body"].append(line)

    beats = [i for i in items if i["kind"] == "beat"]
    total = sum(spoken_words("\n".join(b["body"])) for b in beats) / WPM

    # Headings are deliberately NOT markdown headings. On paper an `##` renders large
    # and bold in every converter, and 51 of them shout over the words they introduce.
    # A monospace line is findable at a glance -- which is all it has to be, mid-talk --
    # without competing. One line per beat instead of three, which also saves paper.
    title = src[0].lstrip("# ").strip() if src and src[0].startswith("#") else d
    out = ["# %s" % title, "",
           "%s spoken, %d beats, at %g wpm. Derived from `SPEAKER_SCRIPT.md` by "
           "`tools/print-script.py` — do not edit this file." % (mmss(total), len(beats), WPM),
           ""]

    elapsed = 0.0
    for it in items:
        if it["kind"] == "act":
            out += ["", "*%s*" % it["title"], ""]   # each beat already ends in a rule
            continue
        w = spoken_words("\n".join(it["body"]))
        mins = w / WPM
        elapsed += mins
        fm = FRAMEREF.search(it["title"])
        frame = fm.group(1) if fm else "?"
        name = it["title"].split("·")[0].strip()
        out += ["`frame %s · %s · %s · %s · ≈ %s in`" % (
                    frame, name, it["id"], mmss(mins), mmss(elapsed)), "",
                clean(it["body"]), "", "---", ""]

    dest = os.path.join(root, d, "SPEAKER_SCRIPT_PRINT.md")
    io.open(dest, "w", encoding="utf-8").write("\n".join(out).rstrip() + "\n")
    print("wrote %s — %d beats, %s spoken" % (dest, len(beats), mmss(total)))


main()
