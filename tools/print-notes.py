#!/usr/bin/env python3
"""Render SPEAKER_NOTES.md to a printable HTML + PDF.

The notes are cue cards, not a script: they are glanced at mid-sentence, so the
type is set larger than print-script.py's 9.6pt and the click markers are given
a colour of their own so the eye finds the next advance without reading.

    python3 tools/print-notes.py PhD_Defense_2026

Writes SPEAKER_NOTES_PRINT.html and .pdf next to the source. Chrome renders the
PDF — see print-script.write_pdf for why nothing else will do.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
# print-script.py is not an importable module name (the hyphen), so load it by path
import importlib.util
_spec = importlib.util.spec_from_file_location("printscript", os.path.join(HERE, "print-script.py"))
printscript = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(printscript)

CSS = """
@page { size: A4; margin: 11mm 10mm 9mm; }
html { font-size: 10.4pt; }
body { font-family: "IBM Plex Sans", -apple-system, system-ui, sans-serif;
       line-height: 1.32; color: #16161a; margin: 0;
       column-count: 2; column-gap: 7mm; }
h1 { font-size: 1.2rem; font-weight: 600; margin: 0 0 1mm; column-span: all; }
.meta { color: #55555f; font-size: 0.8rem; margin: 0 0 3mm; column-span: all;
        border-bottom: 0.5pt solid #c9c9d2; padding-bottom: 1.5mm; }
.act { font-weight: 600; font-size: 1rem; margin: 4mm 0 2mm; column-span: all;
       border-bottom: 0.5pt solid #c9c9d2; padding-bottom: 1mm; color: #2f49c0; }
.act:first-of-type { margin-top: 0; }
.beat { margin: 0 0 2.6mm; break-inside: avoid; }
.fl { font-family: "IBM Plex Mono", ui-monospace, monospace; font-weight: 600;
      font-size: 0.92rem; color: #2f49c0; }
.ti { font-weight: 600; }
.note { color: #8a4b16; font-style: italic; font-size: 0.88rem; }
ul { margin: 0.7mm 0 0; padding-left: 4.2mm; }
li { margin: 0 0 0.5mm; }
b { font-weight: 600; }
i { color: #44444c; }
.click { color: #c2521f; font-weight: 700; }
.tri  { color: #6a6760; font-weight: 400; font-size: 0.8rem; }
"""


def inline(md):
    t = printscript.inline(md)
    t = t.replace("»", '<span class="click">&raquo;</span>')
    return t


def parse(md):
    """-> [('act', text) | ('beat', frame, title, note, [bullets])]"""
    out, cur = [], None
    for raw in md.split("\n"):
        line = raw.rstrip()
        if line.startswith("## "):
            cur = None
            out.append(("act", line[3:].strip()))
        elif re.match(r"^\*\*\d+ ", line):
            m = re.match(r"^\*\*(\d+) · (.+?)\*\*(.*)$", line)
            if not m:
                continue
            note = m.group(3).strip().lstrip("←").strip()
            cur = ("beat", m.group(1), m.group(2), note, [])
            out.append(cur)
        elif line.startswith("- ") and cur:
            cur[4].append(line[2:])
    return out


def main():
    deck = sys.argv[1] if len(sys.argv) > 1 else "PhD_Defense_2026"
    root = os.path.join(HERE, "..", deck)
    src = os.path.join(root, "SPEAKER_NOTES.md")
    md = open(src, encoding="utf-8").read()
    items = parse(md)
    nbeats = sum(1 for i in items if i[0] == "beat")

    body = []
    for it in items:
        if it[0] == "act":
            body.append('<div class="act">%s</div>' % inline(it[1]))
        else:
            _, fno, title, note, bullets = it
            head = '<span class="fl">%s</span> <span class="ti">%s</span>' % (fno, inline(title))
            if note:
                head += ' <span class="note">%s</span>' % inline(note)
            lis = "".join("<li>%s</li>" % inline(b) for b in bullets)
            body.append('<div class="beat">%s<ul>%s</ul></div>' % (head, lis))

    html = ("<!doctype html><html><head><meta charset='utf-8'>"
            "<title>Speaker notes</title><style>%s</style></head><body>"
            "<h1>Speaker notes &mdash; rehearsal cues</h1>"
            "<p class='meta'>%d frames &middot; <span class='click'>&raquo;</span> advance a "
            "fragment &middot; <span class='tri'>&#9650;</span> say this one verbatim &middot; "
            "<b>bold</b> is a number or name to get exactly right</p>"
            "%s</body></html>" % (CSS, nbeats, "".join(body)))

    dest_html = os.path.join(root, "SPEAKER_NOTES_PRINT.html")
    open(dest_html, "w", encoding="utf-8").write(html)
    print("wrote %s — %d frames" % (dest_html, nbeats))
    printscript.write_pdf(dest_html, os.path.join(root, "SPEAKER_NOTES_PRINT.pdf"))


if __name__ == "__main__":
    main()
