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
    # A comment sitting on its own line must take its NEWLINE with it. Otherwise the
    # blank it leaves behind reads as a paragraph break and splits the sentence that
    # wrapped around it -- "...measured shear" / "; and a regulariser..." was two
    # paragraphs, mid-clause, on the printed page.
    txt = "\n".join(body)
    txt = re.sub(r"(?m)^[ \t]*<!--.*?-->[ \t]*\n", "", txt, flags=re.S)
    txt = re.sub(r"<!--.*?-->", "", txt, flags=re.S)                # anything inline
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
    txt = re.sub(r"\s+([;,.])", r"\1", txt)      # the join can leave " ;" behind
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
            out += ["", "**%s**" % it["title"], ""]   # the only bold in the file
            continue
        w = spoken_words("\n".join(it["body"]))
        mins = w / WPM
        elapsed += mins
        fm = FRAMEREF.search(it["title"])
        frame = fm.group(1) if fm else "?"
        name = it["title"].split("·")[0].strip()
        # two trailing spaces = a hard break, so the words start on the next line
        # without a paragraph gap; and no rule, because the frame line already
        # separates one beat from the next. Both are page count.
        out += ["*frame %s · %s · %s · %s · ≈ %s in*  " % (
                    frame, name, it["id"], mmss(mins), mmss(elapsed)),
                clean(it["body"]), ""]

    dest = os.path.join(root, d, "SPEAKER_SCRIPT_PRINT.md")
    io.open(dest, "w", encoding="utf-8").write("\n".join(out).rstrip() + "\n")
    print("wrote %s — %d beats, %s spoken" % (dest, len(beats), mmss(total)))
    html = os.path.join(root, d, "SPEAKER_SCRIPT_PRINT.html")
    write_html(html, title, total, beats, items)
    write_pdf(html, os.path.join(root, d, "SPEAKER_SCRIPT_PRINT.pdf"))


def write_pdf(html, dest):
    """Headless Chrome is the only renderer here that honours @page and columns.

    pandoc/wkhtmltopdf would need extra install and neither does CSS columns
    properly. If no Chrome is found we say so and leave the HTML, which prints
    correctly from any browser anyway.
    """
    import shutil, subprocess
    cands = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ] + [c for c in (shutil.which("google-chrome"), shutil.which("chromium"),
                     shutil.which("chromium-browser")) if c]
    exe = next((c for c in cands if os.path.exists(c)), None)
    if not exe:
        print("no Chrome found — print %s from a browser instead" % os.path.basename(html))
        return
    subprocess.run([exe, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=" + dest, "file://" + os.path.abspath(html)],
                   check=True, capture_output=True)
    import re as _re
    pages = len(_re.findall(rb"/Type\s*/Page[^s]", io.open(dest, "rb").read()))
    print("wrote %s — %d pages" % (dest, pages))


# ------------------------------------------------------------------- for paper
def inline(md):
    """The subset of markdown this script actually uses."""
    import html as H
    t = H.escape(md)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t, flags=re.S)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t, flags=re.S)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t, flags=re.S)
    t = t.replace("[CLICK]", '<span class="click">[CLICK]</span>')
    t = t.replace("▲", '<span class="tri">▲</span>')
    t = re.sub(r"〔(.+?)〕", r'<span class="stage">〔\1〕</span>', t, flags=re.S)
    return t


def write_html(dest, title, total, beats, items):
    """A print stylesheet is the only way to set the type; markdown cannot.

    Two columns at 9.6pt on A4 is about a third of the pages of a default
    markdown-to-PDF render, and a beat never breaks across a column.
    """
    css = """
@page { size: A4; margin: 11mm 10mm 12mm; }
html { font-size: 9.6pt; }
body { font-family: "Source Serif 4", Georgia, serif; line-height: 1.30;
       margin: 0; color: #111; column-count: 2; column-gap: 7mm;
       column-rule: 0.4pt solid #ddd; text-align: left; hyphens: auto; }
h1 { font-size: 1.15rem; font-weight: 600; margin: 0 0 1mm; column-span: all; }
.meta { color: #555; font-size: 0.82rem; margin: 0 0 3mm; column-span: all;
        border-bottom: 0.5pt solid #bbb; padding-bottom: 1.5mm; }
.act { font-weight: 600; font-size: 0.95rem; margin: 3mm 0 1.5mm;
       border-top: 1pt solid #333; padding-top: 1.2mm; break-after: avoid; }
.beat { break-inside: avoid; margin: 0 0 2.6mm; }
.fl { font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 0.76rem;
      color: #444; letter-spacing: -0.01em; margin: 0 0 0.6mm; }
.fl b { color: #000; font-weight: 600; }
p { margin: 0 0 1.1mm; orphans: 2; widows: 2; }
b { font-weight: 600; }
.click { font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 0.78rem;
         font-weight: 600; color: #b03000; }
.tri { color: #b03000; }
.stage { color: #666; font-style: italic; }
code { font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 0.86em; }
"""
    body = ['<h1>%s</h1>' % title,
            '<p class="meta">%s spoken · %d beats · %g wpm · generated by tools/print-script.py</p>'
            % (mmss(total), len(beats), WPM)]
    elapsed = 0.0
    for it in items:
        if it["kind"] == "act":
            body.append('<div class="act">%s</div>' % inline(it["title"]))
            continue
        w = spoken_words("\n".join(it["body"]))
        mins = w / WPM
        elapsed += mins
        fm = FRAMEREF.search(it["title"])
        frame = fm.group(1) if fm else "?"
        name = it["title"].split("·")[0].strip()
        paras = [p for p in re.split(r"\n\s*\n", clean(it["body"])) if p.strip()]
        body.append('<div class="beat"><p class="fl"><b>frame %s</b> · %s · %s · %s · %s in</p>%s</div>'
                    % (frame, inline(name), it["id"], mmss(mins), mmss(elapsed),
                       "".join("<p>%s</p>" % inline(p.replace("\n", " ")) for p in paras)))
    io.open(dest, "w", encoding="utf-8").write(
        "<!doctype html><meta charset=utf-8><title>%s</title><style>%s</style>\n%s\n"
        % (title, css, "\n".join(body)))
    print("wrote %s — print stylesheet, two columns" % dest)


if __name__ == "__main__":          # importable: print-notes.py reuses write_pdf/inline
    main()
