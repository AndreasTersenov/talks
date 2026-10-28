#!/usr/bin/env python3
"""The mass-mapping figures without inpainting KS (iKS): the corner plot and the maps.

For the UVA / NRAO colloquium (2026-10-28, Andreas: iKS only confuses a colloquium room). Two
figures of the mass-mapping part show it, and neither is redrawn.

THE MAPS (the comparison slide). mass_maps_(ks_iks_mca)_transparent_light.png is a 2 x 2 of
panels (truth, Kaiser-Squires, iterative Kaiser-Squires, MCALens), each with its own title,
ticks and colour bar. Three are cut out, at one size and with the axes at the same offset in
each, into assets/figures/maps/mass_maps_noiks/{truth,ks,mcalens}.png, for a row of three.

THE CORNER PLOT (the figure-of-merit slide) compares Kaiser-Squires, iKS and MCALens. Its source,
assets/figures/posteriors/countours_all_methods_MSPC_6scales_dark.pdf, is matplotlib (getdist)
vector output, where every iKS element is its own path in iKS's two reds. So nothing is redrawn:
this deletes exactly those paths and leaves every other operator of the page as it was.

    - the iKS contour fills, contour edges and 1-D curves: every path painted in
      (0.878, 0.204, 0.141) or its light shade (0.951, 0.682, 0.656), fill or stroke;
    - the iKS legend entry: its swatch (painted in the same red) and its "(iKS) TJ" label;
    - then the MCALens legend row moves up into the gap, and the legend frame's bottom edge
      comes up by the same step, so the legend reads KS, MCALens with nothing missing.

Writes countours_all_methods_noiks_MSPC_6scales_dark.pdf next to the source, and the light
version straight from the vector, countours_all_methods_noiks_MSPC_6scales_light.png (2000 px,
transparent, like the original's light PNG). The light version swaps the pure neutrals only
(white ink to black, the black legend fill to white) and leaves the greys alone, which is what
tools/darkfig-to-light.py does to pixels; that tool was not used here because with the red
contours gone, KS's large grey contours read to it as filled panels it must not recolour, and it
left the legend black and the truth lines white inside them.

    venv/bin/python tools/make-noiks-figures.py

Needs PyMuPDF and Pillow. The counts it prints (paths dropped per colour) are the check that nothing else
went: 6 fills in each red, 10 strokes in dark red, and the legend swatch.
"""
import os
import re
import fitz
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
POST = os.path.join(HERE, "..", "assets", "figures", "posteriors")
SRC = os.path.join(POST, "countours_all_methods_MSPC_6scales_dark.pdf")
OUT = os.path.join(POST, "countours_all_methods_noiks_MSPC_6scales_dark.pdf")
PNG = os.path.join(POST, "countours_all_methods_noiks_MSPC_6scales_light.png")

MAPS = os.path.join(HERE, "..", "assets", "figures", "maps")
GRID = os.path.join(MAPS, "mass_maps_(ks_iks_mca)_transparent_light.png")
# each panel's box in the 2000 x 1637 grid: the quadrant's ink (found as fully transparent
# rows and columns between the quadrants) plus a 10 px margin, all 964 x 782
PANELS = {"truth": (9, 9, 973, 791), "ks": (1026, 9, 1990, 791), "mcalens": (1026, 835, 1990, 1617)}

REDS = {(0.878, 0.204, 0.141), (0.951, 0.682, 0.656)}
PAINT = {"f", "F", "f*", "S", "s", "B", "B*", "b", "b*"}
CONSTRUCT = {"m", "l", "c", "v", "y", "h", "re"}
TOKEN = re.compile(rb"""
    (?P<str>\((?:\\.|[^\\()])*\))          # a literal string (no nesting in this file)
  | (?P<arr>\[[^\]]*\])                    # an array, kept whole
  | (?P<name>/[^\s/\[\]()<>{}%]+)
  | (?P<num>[+-]?(?:\d+\.?\d*|\.\d+))
  | (?P<op>[A-Za-z'"*]+[*]?)
""", re.X)


def ops(stream):
    """Split a content stream into (operands, operator) pairs, keeping each one's raw bytes."""
    out, operands, start = [], [], None
    for m in TOKEN.finditer(stream):
        if start is None:
            start = m.start()
        if m.lastgroup == "op":
            out.append({"args": operands, "op": m.group().decode(), "raw": stream[start:m.end()]})
            operands, start = [], None
        else:
            operands.append(m.group())
    return out


def rgb(args):
    return tuple(round(float(a), 3) for a in args)


def maps():
    grid = Image.open(GRID)
    out = os.path.join(MAPS, "mass_maps_noiks")
    os.makedirs(out, exist_ok=True)
    for name, box in PANELS.items():
        path = os.path.join(out, name + ".png")
        grid.crop(box).save(path, optimize=True)
        print("wrote", os.path.normpath(path))


def main():
    maps()
    doc = fitz.open(SRC)
    page = doc[0]
    xref = page.get_contents()[0]
    seq = ops(doc.xref_stream(xref))

    fill = stroke = None
    keep, path, dropped = [], [], {}
    for o in seq:
        if o["op"] == "rg":
            fill = rgb(o["args"])
        elif o["op"] == "RG":
            stroke = rgb(o["args"])
        elif o["op"] == "g":
            fill = rgb(o["args"] * 3)
        elif o["op"] == "G":
            stroke = rgb(o["args"] * 3)
        if o["op"] in CONSTRUCT:
            path.append(o)
            continue
        if o["op"] in PAINT:
            uses_fill = o["op"] not in {"S", "s"}
            uses_stroke = o["op"] not in {"f", "F", "f*"}
            red = (uses_fill and fill in REDS) or (uses_stroke and stroke in REDS)
            if red:
                key = (o["op"], fill if uses_fill else stroke)
                dropped[key] = dropped.get(key, 0) + 1
                path = []
                continue
        keep.extend(path)
        path = []
        keep.append(o)
    keep.extend(path)

    # the iKS label: q, cm, BT, Tf, Td, [(iKS)] TJ, ET, Q
    i = next(k for k, o in enumerate(keep) if o["op"] == "TJ" and b"(iKS)" in o["args"][0])
    lo = max(k for k in range(i) if keep[k]["op"] == "q")
    hi = next(k for k in range(i, len(keep)) if keep[k]["op"] == "Q")
    label_y = float(keep[next(k for k in range(lo, i) if keep[k]["op"] == "cm")]["args"][5])
    del keep[lo:hi + 1]

    # the MCALens row: its label is the next q ... cm ... (MCALens) TJ ... Q, its swatch the path
    # painted just before that q. Move both up to the iKS row.
    j = next(k for k, o in enumerate(keep) if o["op"] == "TJ" and b"(MCALens)" in o["args"][0])
    q = max(k for k in range(j) if keep[k]["op"] == "q")
    cm = next(k for k in range(q, j) if keep[k]["op"] == "cm")
    dy = label_y - float(keep[cm]["args"][5])
    paint = max(k for k in range(q) if keep[k]["op"] in PAINT)
    first = paint
    while first > 0 and keep[first - 1]["op"] in CONSTRUCT:
        first -= 1

    def shift(o, ys):
        a = list(o["args"])
        for n in ys:
            a[n] = b"%.6f" % (float(a[n]) + dy)
        o["raw"] = b" ".join(a + [o["op"].encode()])

    for k in range(first, paint):
        o = keep[k]
        if o["op"] in {"m", "l"}:
            shift(o, [1])
        elif o["op"] == "re":
            shift(o, [1])
        elif o["op"] == "c":
            shift(o, [1, 3, 5])
    shift(keep[cm], [5])

    # the legend frame: the rounded rectangle painted with B that encloses the labels; its
    # lowest points come up by dy (PDF y runs upwards)
    frame = None
    for k, o in enumerate(keep):
        if o["op"] == "B":
            pts = [float(a) for p in keep[max(0, k - 12):k] if p["op"] in {"m", "l", "c"} for a in p["args"]]
            if len(pts) > 16:
                frame = k
                break
    start = frame
    while keep[start - 1]["op"] in CONSTRUCT:
        start -= 1
    ys = [float(a) for p in keep[start:frame] if p["op"] in {"m", "l", "c"} for a in p["args"][1::2]]
    bottom = min(ys)
    for k in range(start, frame):
        o = keep[k]
        if o["op"] in {"m", "l", "c"}:
            a = list(o["args"])
            for n in range(1, len(a), 2):
                if float(a[n]) < bottom + 4:
                    a[n] = b"%.6f" % (float(a[n]) + dy)
            o["raw"] = b" ".join(a + [o["op"].encode()])

    doc.update_stream(xref, b"\n".join(o["raw"] for o in keep))
    doc.save(OUT, garbage=3, deflate=True)

    # the light version: pure white and pure black swap, in every colour operator; greys stay
    def swap(o):
        if o["op"] in {"g", "G"} and float(o["args"][0]) in (0.0, 1.0):
            v = 1.0 - float(o["args"][0])
        elif o["op"] in {"rg", "RG"} and len({float(a) for a in o["args"]}) == 1 \
                and float(o["args"][0]) in (0.0, 1.0):
            v = 1.0 - float(o["args"][0])
        else:
            return o["raw"]
        n = 1 if o["op"] in {"g", "G"} else 3
        return b" ".join([b"%g" % v] * n + [o["op"].encode()])

    light = fitz.open(OUT)
    light.update_stream(light[0].get_contents()[0], b"\n".join(swap(o) for o in keep))
    print("dropped:", {f"{op} {c}": n for (op, c), n in sorted(dropped.items(), key=str)})
    print(f"legend: MCALens row moved by {dy:+.3f} pt, frame bottom {bottom:.3f} -> {bottom + dy:.3f}")

    out = light[0]
    zoom = 2000 / max(out.rect.width, out.rect.height)
    out.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=True).save(PNG)
    print("wrote", os.path.normpath(OUT), "and", os.path.normpath(PNG))


if __name__ == "__main__":
    main()
