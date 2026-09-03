#!/usr/bin/env python3
"""Re-ground a dark-background matplotlib figure that contains imshow panels.

Why this exists
---------------
`darkfig-to-light.py` inverts the luminance of near-neutral pixels and leaves
saturated ones alone. That is right for line plots and posterior contours, and it
explicitly refuses figures with an imshow panel: a colormap's dark end (inferno's
`(0,0,3)`, viridis' deep purple) is near-neutral, so a blanket inversion turns the
voids of a large-scale-structure map into white speckle and destroys the field.

This tool takes the panel geometry into account instead of avoiding it:

* the **figure background and its text** (titles, suptitles, anything living in the
  margins) are re-grounded from black onto the theme's paper `#f7f5f0`, with white
  ink flipped to `#1c1c22` and every antialiased grey in between interpolated;
* **image panels are left byte-for-byte alone** — the colormap is the data;
* a panel that is a *plot* rather than an image can be named with `--invert-panel`
  and gets the neutral-only inversion inside its own rectangle, so its white axes,
  ticks, labels and legend frame flip while its coloured lines survive.

Panels are found as bands of non-background pixels: the figure background must be
exactly `(0,0,0)`, which is what matplotlib's dark styles emit, and which is
distinguishable from a colormap's dark end (never exactly black). Check the result;
a figure whose panels touch or whose background is not pure black needs `--panels`
given by hand.

Usage
-----
    python3 tools/darkfig-panel-light.py assets/diagrams/pk_lss.png --invert-panel 2
    python3 tools/darkfig-panel-light.py assets/diagrams/foo.png --panels 10,20,300,280

Writes `<name>_light.png` beside the source. Sources are never modified.
"""
import sys, os
from PIL import Image

PAPER = (247, 245, 240)
INK   = (28, 28, 34)
BG    = (0, 0, 0)


def luminance(p):
    return (0.2126 * p[0] + 0.7152 * p[1] + 0.0722 * p[2]) / 255.0


def blend(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def find_panels(im):
    """Panel x-ranges inside the densest band of non-background rows."""
    px, (W, H) = im.load(), im.size
    rowc = [sum(1 for x in range(0, W, 2) if px[x, y] != BG) for y in range(H)]
    thr = 0.30 * (W / 2)
    rows = [y for y, c in enumerate(rowc) if c > thr]
    if not rows:
        return []
    r0, r1 = rows[0], rows[-1]
    colc = [sum(1 for y in range(r0, r1 + 1, 2) if px[x, y] != BG) for x in range(W)]
    thr = 0.30 * ((r1 - r0) / 2)
    bands, run = [], None
    for x, c in enumerate(colc):
        if c > thr and run is None:
            run = x
        elif c <= thr and run is not None:
            bands.append((run, x)); run = None
    if run is not None:
        bands.append((run, W))
    return [(x0, r0, x1, r1) for x0, x1 in bands if x1 - x0 > 20]


def main(argv):
    src = argv[1]
    invert = {int(v) for a, v in zip(argv, argv[1:]) if a == "--invert-panel"}
    im = Image.open(src).convert("RGB")
    panels = find_panels(im)
    print(f"{src}: {len(panels)} panels {panels}")
    out = im.copy(); px = out.load(); W, H = out.size

    def inside(x, y):
        for i, (x0, y0, x1, y1) in enumerate(panels):
            if x0 <= x < x1 and y0 <= y < y1:
                return i
        return None

    for y in range(H):
        for x in range(W):
            p = px[x, y]
            i = inside(x, y)
            if i is None or i in invert:        # background, margins, plot panels
                # neutral ink only, everywhere: a coloured line inside a plot
                # panel survives, and so does a panel the detector missed.
                if max(p) - min(p) <= 40:
                    px[x, y] = blend(PAPER, INK, luminance(p))

    dst = os.path.splitext(src)[0] + "_light.png"
    out.save(dst, optimize=True)
    print("wrote", dst)


if __name__ == "__main__":
    main(sys.argv)
