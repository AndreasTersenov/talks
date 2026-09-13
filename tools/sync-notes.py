#!/usr/bin/env python3
"""Push SPEAKER_NOTES.md into the deck's <aside class="notes">, so reveal's
speaker view (press S) shows the cue cards.

    python3 tools/sync-notes.py PhD_Defense_2026            # dry run, reports only
    python3 tools/sync-notes.py PhD_Defense_2026 --write

Only the main line is touched. Whatever note a frame had is kept, parked in an
HTML comment beside the new one — comments do not render, so the speaker view
shows the bullets alone.

Frame numbers are derived the way reveal derives them: sections in document
order, hidden ones skipped, a parent with visible children contributing the
children rather than itself.
"""
import os
import re
import sys

HID = 'data-visibility="hidden"'


def frame_spans(src):
    """-> {frame number: (first line, last line + 1)} over the whole deck."""
    def tag(i):
        t, j = src[i], i
        while ">" not in t and j + 1 < len(src):
            j += 1
            t += " " + src[j]
        return t.split(">")[0]

    close = next(i for i, l in enumerate(src) if l == "\t\t</div>")
    bounds = [i for i, l in enumerate(src) if re.match(r"^\t{3}<section\b", l)] + [close]
    n, out = 0, {}
    for a, b in zip(bounds, bounds[1:]):
        if HID in tag(a):
            continue
        kids = [i for i in range(a, b) if re.match(r"^\t{4}<section\b", src[i])]
        if not kids:
            n += 1
            out[n] = (a, b)
        else:
            # bound each child by the NEXT child of any visibility. Bounding by the
            # next VISIBLE one swallows a hidden sibling, and the aside then lands
            # inside the hidden section, where reveal never renders it. Frames 22
            # and 23 are both followed by one.
            for k, e in zip(kids, kids[1:] + [b]):
                if HID in tag(k):
                    continue
                n += 1
                out[n] = (k, e)
    return out


def close_line(src, a):
    """The section's own </section>: the first one at its indent, not the last in
       the span, which for a last child is the parent's."""
    indent = re.match(r"^(\t*)", src[a]).group(1)
    want = indent + "</section>"
    for i in range(a + 1, len(src)):
        if src[i] == want:
            return i
    raise AssertionError("no closing tag for the section at line %d" % (a + 1))


def parse_notes(md):
    """-> {frame: (title, note, [bullets])}"""
    out, cur = {}, None
    for raw in md.split("\n"):
        line = raw.rstrip()
        m = re.match(r"^\*\*(\d+) · (.+?)\*\*(.*)$", line)
        if m:
            cur = int(m.group(1))
            out[cur] = (m.group(2), m.group(3).strip().lstrip("←").strip(), [])
        elif line.startswith("## "):
            cur = None
        elif line.startswith("- ") and cur:
            out[cur][2].append(line[2:])
    return out


def html(md):
    """The subset the notes use. Escaping first, so a stray < cannot inject."""
    import html as H
    t = H.escape(md)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t


def build(indent, title, note, bullets, parked):
    head = html(title) + ((" &mdash; <em>%s</em>" % html(note)) if note else "")
    L = ["%s<aside class=\"notes\">" % indent,
         "%s\t<p><strong>%s</strong></p>" % (indent, head),
         "%s\t<ul>" % indent]
    L += ["%s\t\t<li>%s</li>" % (indent, html(b)) for b in bullets]
    L.append("%s\t</ul>" % indent)
    if parked:
        # -- would close the comment early; the old notes are prose, so this is rare
        safe = re.sub(r"-{2,}", "- ", parked).strip()
        L.append("%s\t<!-- PARKED 2026-09-13, the note this replaced:" % indent)
        L += ["%s\t     %s" % (indent, l) for l in safe.split("\n") if l.strip()]
        L.append("%s\t-->" % indent)
    L.append("%s</aside>" % indent)
    return L


def main():
    deck = "PhD_Defense_2026"
    write = "--write" in sys.argv
    for a in sys.argv[1:]:
        if not a.startswith("-"):
            deck = a
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.join(here, "..", deck)

    notes = parse_notes(open(os.path.join(root, "SPEAKER_NOTES.md"), encoding="utf-8").read())
    path = os.path.join(root, "index.html")
    src = open(path, encoding="utf-8").read().split("\n")
    spans = frame_spans(src)

    main_line = sorted(f for f in notes if f in spans)
    missing = sorted(f for f in notes if f not in spans)
    if missing:
        print("notes for frames not in the deck: %s" % missing)

    edits, replaced, inserted = [], 0, 0
    for f in main_line:
        a, _ = spans[f]
        b = close_line(src, a) + 1
        chunk = "\n".join(src[a:b])
        indent = re.match(r"^(\t*)", src[a]).group(1) + "\t"
        title, note, bullets = notes[f]

        m = re.search(r"[ \t]*<aside class=\"notes\">(.*?)</aside>[ \t]*\n?", chunk, re.S)
        parked = ""
        if m:
            # skip an aside that lives inside a parked comment block
            before = chunk[:m.start()]
            if before.count("<!--") > before.count("-->"):
                m = None
            else:
                parked = re.sub(r"<[^>]+>", "", m.group(1))
                parked = re.sub(r"[ \t]+", " ", parked).strip()

        block = "\n".join(build(indent, title, note, bullets, parked)) + "\n"
        if m:
            new_chunk = chunk[:m.start()] + block + chunk[m.end():]
            replaced += 1
        else:
            rel = b - 1 - a                       # just before the closing tag
            lines = chunk.split("\n")
            lines[rel:rel] = block.rstrip("\n").split("\n")
            new_chunk = "\n".join(lines)
            inserted += 1
        edits.append((a, b, new_chunk))

    print("%d frames with notes: %d asides replaced, %d inserted" % (len(main_line), replaced, inserted))
    if not write:
        print("dry run — pass --write to apply")
        return

    for a, b, new_chunk in sorted(edits, reverse=True):
        src[a:b] = new_chunk.split("\n")
    open(path, "w", encoding="utf-8").write("\n".join(src))
    print("wrote %s" % path)


if __name__ == "__main__":
    main()
