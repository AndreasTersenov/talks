#!/usr/bin/env python3
"""Measure a SPEAKER_SCRIPT.md against its deck, and stamp the timings back into it.

`docs/TALK-GUIDELINES.md` §11b asks for two things a human cannot keep true by hand:

  1. **Timings measured, not estimated.** Spoken words / 140 wpm, recomputed after every
     edit. An estimated timing is worse than none, because it is believed.
  2. **`[CLICK]` cues that have not gone stale.** A cue pointing at a fragment that no
     longer exists is discovered mid-rehearsal, at the worst possible moment.

So this reads the script and the deck together:

    tools/measure-script.py PhD_Defense_2026            # report only
    tools/measure-script.py PhD_Defense_2026 --write    # ...and stamp the headings

A beat is a `## <id> — <title> · frame <N> · <M:SS>` heading. Everything under it counts
as spoken except stage directions 〔…〕, blockquote notes, headings, tables and HTML
comments. `frame <N>` (or `frames <N>-<M>`) ties the beat to the deck; the [CLICK] count is
then checked against the number of fragment STEPS on those frames — distinct
data-fragment-index values, or the raw fragment count where they are unindexed.

Beats with no `frame` reference (cut ladders, Q&A, register notes) are skipped by both
checks, which is what makes it safe to keep them in the same file.
"""
import io, os, re, sys
from html.parser import HTMLParser

WPM = 140.0


# ----------------------------------------------------------------- the deck
class Deck(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.d = 0; self.in_slides = False
        self.stack = []; self.root = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs); cls = (a.get("class") or "").split()
        if tag == "div" and "slides" in cls:
            self.in_slides = True
        if self.in_slides:
            if tag == "section":
                n = {"a": a, "kids": [], "frags": [], "title": None}
                (self.stack[-1]["kids"] if self.stack else self.root).append(n)
                self.stack.append(n)
            elif self.stack and "fragment" in cls:
                self.stack[-1]["frags"].append(a.get("data-fragment-index"))
            elif self.stack and tag in ("h1", "h2", "h3") and self.stack[-1]["title"] is None:
                self.stack[-1]["title"] = ""
        self.d += 1

    def handle_endtag(self, tag):
        self.d -= 1
        if tag == "section" and self.stack:
            self.stack.pop()

    def handle_data(self, txt):
        if self.stack and self.stack[-1]["title"] == "":
            pass


def frames_of(path):
    """Visible reveal frames, in order, with their fragment-step count."""
    p = Deck(); p.feed(io.open(path, encoding="utf-8").read())
    out = []

    def hidden(n):
        return n["a"].get("data-visibility") == "hidden"

    for n in p.root:
        if hidden(n):
            continue
        kids = [k for k in n["kids"] if not hidden(k)]
        for f in (kids or [n]):
            idx = f["frags"]
            if not idx:
                steps = 0
            elif all(i is None for i in idx):
                steps = len(idx)
            else:
                steps = len({i for i in idx if i is not None})
            out.append({"steps": steps, "cls": f["a"].get("class", "")})
    return out


# --------------------------------------------------------------- the script
HEAD = re.compile(r"^##\s+(?P<id>[A-Z][\w.]*)\s+—\s+(?P<title>.*?)\s*$")
FRAMEREF = re.compile(r"·\s*frames?\s+(\d+)(?:\s*[–-]\s*(\d+))?", re.I)
TIMEREF = re.compile(r"·\s*(\d+):([0-5]\d)\s*$")


def spoken(lines):
    """Words actually said: drop stage directions, notes, headings, tables, comments."""
    text = "\n".join(l for l in lines
                     if not l.lstrip().startswith(">")
                     and not l.lstrip().startswith("#")
                     and not l.lstrip().startswith("|")
                     and not l.lstrip().startswith("<!--"))
    text = re.sub(r"〔[^〕]*〕", " ", text, flags=re.S)      # stage directions
    text = re.sub(r"\[CLICK[^\]]*\]", " ", text)             # cues
    text = re.sub(r"\*\*▲\*\*|▲", " ", text)                 # verbatim marks
    text = re.sub(r"`[^`]*`", " ", text)                     # inline code
    text = re.sub(r"[*_]{1,2}", "", text)                    # emphasis marks
    return len(re.findall(r"[A-Za-z0-9][\w'’\-–]*", text))


def mmss(minutes):
    total = int(round(minutes * 60))
    return "%d:%02d" % (total // 60, total % 60)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    d = sys.argv[1].rstrip("/")
    write = "--write" in sys.argv
    root = os.path.dirname(os.path.abspath(__file__)) + "/.."
    spath = os.path.join(root, d, "SPEAKER_SCRIPT.md")
    dpath = os.path.join(root, d, "index.html")
    src = io.open(spath, encoding="utf-8").read().split("\n")
    frames = frames_of(dpath)

    beats, cur = [], None
    for i, line in enumerate(src):
        m = HEAD.match(line)
        if m:
            cur = {"line": i, "id": m.group("id"), "title": m.group("title"), "body": []}
            beats.append(cur)
        elif line.startswith("#"):
            # any other heading ends the beat: the ladders, the Q&A tiers and the
            # ledger live in the same file and are not spoken.
            cur = None
        elif cur is not None:
            cur["body"].append(line)

    problems, total = [], 0.0
    for b in beats:
        b["words"] = spoken(b["body"])
        b["mins"] = b["words"] / WPM
        fm = FRAMEREF.search(b["title"])
        b["frames"] = None
        if fm:
            lo = int(fm.group(1)); hi = int(fm.group(2) or fm.group(1))
            b["frames"] = (lo, hi)
            total += b["mins"]
            if hi > len(frames):
                problems.append("%s: names frame %d, deck has %d" % (b["id"], hi, len(frames)))
            else:
                want = sum(frames[k - 1]["steps"] for k in range(lo, hi + 1))
                got = len(re.findall(r"\[CLICK", "\n".join(b["body"])))
                b["want"], b["got"] = want, got
                if want != got:
                    problems.append("%s (frame%s %s): %d [CLICK] cues, deck has %d fragment steps"
                                    % (b["id"], "s" if hi > lo else "",
                                       "%d-%d" % (lo, hi) if hi > lo else str(lo), got, want))

    print("%-10s %-52s %6s %6s  %s" % ("beat", "title", "words", "time", "clicks"))
    print("-" * 92)
    for b in beats:
        if b["frames"] is None:
            continue
        clicks = "%d/%d%s" % (b["got"], b["want"], "" if b["got"] == b["want"] else "  <-- MISMATCH") \
            if "want" in b else "-"
        print("%-10s %-52s %6d %6s  %s" % (b["id"], b["title"][:52], b["words"], mmss(b["mins"]), clicks))
    print("-" * 92)
    acts = {}
    for b in beats:
        if b["frames"] is None:
            continue
        act = re.match(r"([A-Z]\d*|C)", b["id"]).group(1)
        a = acts.setdefault(act, {"m": 0.0, "lo": 10 ** 9, "hi": 0})
        a["m"] += b["mins"]
        a["lo"] = min(a["lo"], b["frames"][0]); a["hi"] = max(a["hi"], b["frames"][1])
    for act in sorted(acts, key=lambda k: acts[k]["lo"]):
        a = acts[act]
        print("%-10s %-52s %6s %6s" % (act, "frames %d-%d" % (a["lo"], a["hi"]), "", mmss(a["m"])))
    print("-" * 92)
    print("%-10s %-52s %6s %6s   (target 40:00)" % ("TOTAL", "", "", mmss(total)))

    if problems:
        print("\n%d CLICK/frame problem(s):" % len(problems))
        for p in problems:
            print("  - " + p)
    else:
        print("\nevery [CLICK] cue matches the deck.")

    if write:
        for b in beats:
            if b["frames"] is None:
                continue
            t = TIMEREF.sub("", b["title"]).rstrip()
            src[b["line"]] = "## %s — %s · %s" % (b["id"], t, mmss(b["mins"]))
        io.open(spath, "w", encoding="utf-8").write("\n".join(src))
        print("\nstamped %d headings in %s" % (sum(1 for b in beats if b["frames"]), spath))


if __name__ == "__main__":
    main()
