#!/usr/bin/env python3
"""List a deck's rendered frames, numbered the way reveal numbers them.

    python3 tools/list-frames.py PhD_Defense_2026            # every frame
    python3 tools/list-frames.py PhD_Defense_2026 phases     # only titles matching

Hiding or unhiding a single section renumbers everything after it, which is what
makes the backup-frame pointers in SPEAKER_SCRIPT.md go stale. Run this after any
such edit and fix the pointers against the output rather than by arithmetic.

Frame numbering follows sync-notes.frame_spans: sections in document order,
data-visibility="hidden" skipped, a parent with visible children contributing the
children rather than itself.
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("syncnotes", os.path.join(HERE, "sync-notes.py"))
syncnotes = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(syncnotes)


def title_of(src, a, b):
    chunk = "\n".join(src[a:min(b, a + 40)])
    m = re.search(r"<h[1-4][^>]*>(.*?)</h[1-4]>", chunk, re.S)
    if not m:
        return ""
    t = re.sub(r"<[^>]+>", "", m.group(1))
    return re.sub(r"\s+", " ", t).strip()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    deck = args[0] if args else "PhD_Defense_2026"
    needle = args[1].lower() if len(args) > 1 else None

    path = os.path.join(HERE, "..", deck, "index.html")
    src = open(path, encoding="utf-8").read().split("\n")
    spans = syncnotes.frame_spans(src)

    shown = 0
    for f, (a, b) in spans.items():
        t = title_of(src, a, b)
        if needle and needle not in t.lower():
            continue
        depth = len(re.match(r"^(\t*)", src[a]).group(1))
        print("%4d  %-3s  line %-6d %s" % (f, "top" if depth == 3 else "sub", a + 1, t[:84]))
        shown += 1

    hidden = sum(1 for l in src if syncnotes.HID in l)
    print("\n%d frames%s, %d hidden sections in the file"
          % (len(spans), "" if needle is None else " (%d shown)" % shown, hidden))


if __name__ == "__main__":
    main()
