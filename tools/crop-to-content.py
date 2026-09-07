#!/usr/bin/env python3
"""Crop an image down to its own content, so `margin: auto` actually centres it.

Several of the borrowed figures in this repo carry a wide, uneven margin of
background baked into the file. On a slide whose background is the same colour
the margin is invisible, so the picture reads as badly centred even though the
CSS box around it is centred perfectly - the eye centres on the *content*, and
the content is off to one side of its own canvas.

    /usr/local/bin/python3 tools/crop-to-content.py IN OUT [--pad N] [--thr N]

The threshold is a distance from the corner pixel's colour, so this works on a
black surround and a white one alike. Padding is added symmetrically, which is
what re-centres the content; it is clamped at the canvas edge, and if a clamp
bites, the opposite side is trimmed to match so the result stays centred.

Never write over the input: `assets/` is shared, and another deck is probably
using the original as it is.
"""
import argparse
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("src")
ap.add_argument("out")
ap.add_argument("--pad", type=int, default=24, help="margin to keep, in source pixels")
ap.add_argument("--thr", type=int, default=12, help="how far from the surround colour counts as content")
a = ap.parse_args()

if a.src == a.out:
    raise SystemExit("refusing to overwrite the source; assets/ is shared")

im = Image.open(a.src).convert("RGB")
px = np.asarray(im).astype(int)
h, w = px.shape[:2]

surround = px[0, 0]
ink = np.abs(px - surround).max(axis=2) > a.thr
cols = np.where(ink.any(axis=0))[0]
rows = np.where(ink.any(axis=1))[0]
if not len(cols) or not len(rows):
    raise SystemExit("no content found above the threshold")

def span(lo, hi, limit):
    """Pad both sides equally, then trim back symmetrically if a side clamps."""
    keep = min(a.pad, lo, limit - 1 - hi)
    return lo - keep, hi + keep + 1

x0, x1 = span(cols[0], cols[-1], w)
y0, y1 = span(rows[0], rows[-1], h)

im.crop((x0, y0, x1, y1)).save(a.out, quality=95, subsampling=0)
print("%s  %dx%d  ->  %s  %dx%d  (aspect %.4f)"
      % (a.src, w, h, a.out, x1 - x0, y1 - y0, (x1 - x0) / (y1 - y0)))
print("   content x %d..%d, y %d..%d; surround rgb%s" % (cols[0], cols[-1], rows[0], rows[-1], tuple(surround)))
