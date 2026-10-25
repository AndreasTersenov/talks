#!/usr/bin/env python3
"""Take a paper-ground figure back to pure white: the inverse of whitefig-to-paper.py.

The Preprint theme's light slides sit on warm paper (#f7f5f0), so its figures were
made on that ground — either scaled onto it by `whitefig-to-paper.py` (every pixel
times paper/255) or drawn on it directly by the `make-*.py` scripts (PAPER facecolor).
A deck on a plain white light theme shows each of them as a beige rectangle.

The fix divides every pixel by paper/255, which sends the paper exactly to white,
leaves black at black and keeps every intermediate value, so anti-aliasing survives.
For a `whitefig-to-paper.py` figure it recovers the white original up to rounding;
for a script-drawn one it lifts the colours by the same <7 %, which is the same tint
the paper put on them. Alpha is kept as is.

The original is left untouched (other decks still use it); the result is written
next to it as <name>_white.png.

    tools/paperfig-to-white.py assets/diagrams/wavelet_bands.png [more.png ...]
"""
import os, sys
from PIL import Image

PAPER = (247, 245, 240)          # the theme's light ground, as in whitefig-to-paper.py


def main():
    srcs = sys.argv[1:]
    if not srcs:
        sys.exit(__doc__)
    for src in srcs:
        im = Image.open(src)
        alpha = im.getchannel("A") if im.mode in ("RGBA", "LA") else None
        rgb = im.convert("RGB")
        rgb = Image.merge("RGB", [ch.point(lambda v, s=s: min(255, round(v * 255.0 / s)))
                                  for ch, s in zip(rgb.split(), PAPER)])
        if alpha is not None:
            rgb.putalpha(alpha)
        stem, ext = os.path.splitext(src)
        dst = stem + "_white" + ext
        rgb.save(dst, optimize=True)
        print("wrote %s  %dx%d" % (dst, rgb.width, rgb.height))


if __name__ == "__main__":
    main()
