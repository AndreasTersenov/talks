#!/usr/bin/env python3
"""Put a white-background figure onto the Preprint theme's paper ground.

Borrowed figures arrive on pure white. Dropped onto a `data-theme="light"` slide they
read as a brighter rectangle pasted on the page, because the theme's paper is #f7f5f0,
not #ffffff. The companion `darkfig-to-light.py` solves the opposite problem.

Keying out white and going transparent does not work here: the anti-aliased edges of
every line and glyph are *near* white, so a threshold leaves a bluish-white halo around
all of them. Instead every pixel is scaled by paper/255, which sends white exactly to
the paper colour, leaves black at black, and preserves every intermediate value — so
anti-aliasing survives and the coloured contours keep their relative weight.

    tools/whitefig-to-paper.py in.pdf assets/figures/posteriors/out.png [--width 1800]

A PDF source is rasterised first (Chrome renders nothing from a PDF in an <img> —
REVEAL-GOTCHAS). The surrounding white margin is cropped to a small, even padding.
"""
import os, subprocess, sys, tempfile
from PIL import Image

PAPER = (247, 245, 240)          # --surface / the theme's light ground


def main():
    a = sys.argv[1:]
    if len(a) < 2:
        sys.exit(__doc__)
    src, dst = a[0], a[1]
    width = int(a[a.index("--width") + 1]) if "--width" in a else 1800
    pad = int(a[a.index("--pad") + 1]) if "--pad" in a else 14

    if src.lower().endswith(".pdf"):
        tmp = tempfile.mkdtemp()
        stem = os.path.join(tmp, "page")
        subprocess.run(["pdftoppm", "-png", "-r", "600", "-scale-to", str(width * 2), src, stem],
                       check=True)
        pages = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
        assert len(pages) == 1, "expected a one-page figure, got %d" % len(pages)
        im = Image.open(os.path.join(tmp, pages[0])).convert("RGB")
    else:
        im = Image.open(src).convert("RGB")

    # crop the white margin: anything at all darker than near-white is content
    from PIL import ImageChops
    bg = Image.new("RGB", im.size, (255, 255, 255))
    box = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 6 else 0).getbbox()
    if box:
        l, t, r, b = box
        im = im.crop((max(l - pad, 0), max(t - pad, 0),
                      min(r + pad, im.width), min(b + pad, im.height)))

    if im.width != width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)

    im = Image.merge("RGB", [ch.point(lambda v, s=s: round(v * s / 255.0))
                             for ch, s in zip(im.split(), PAPER)])
    im.save(dst, optimize=True)
    print("wrote %s  %dx%d" % (dst, im.width, im.height))


if __name__ == "__main__":
    main()
