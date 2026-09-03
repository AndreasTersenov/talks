"""Flip a dark-background figure for a light one by inverting CIELAB lightness.

L* -> 100 - L* reverses the luminance ramp, so what was bright-on-black becomes
dark-on-paper, while a* and b* are untouched -- hue and chroma survive, which a
naive 255-RGB inversion would destroy (orange would come back blue).

Out-of-gamut is expected and fine here: a bright yellow at L*~95 has no
high-chroma counterpart at L*~5, so littlecms clips it toward a dark warm tone.
For a visualisation thumbnail that is the right trade.
"""
from PIL import Image, ImageCms
import sys

def lab_invert(src, dst):
    im = Image.open(src).convert('RGBA')
    alpha = im.getchannel('A')
    srgb_p, lab_p = ImageCms.createProfile('sRGB'), ImageCms.createProfile('LAB')
    to_lab = ImageCms.buildTransformFromOpenProfiles(srgb_p, lab_p, 'RGB', 'LAB')
    to_rgb = ImageCms.buildTransformFromOpenProfiles(lab_p, srgb_p, 'LAB', 'RGB')
    L, A, B = ImageCms.applyTransform(im.convert('RGB'), to_lab).split()
    L = L.point(lambda v: 255 - v)
    out = ImageCms.applyTransform(Image.merge('LAB', (L, A, B)), to_rgb).convert('RGBA')
    out.putalpha(alpha)
    # transparent pixels carry RGB(0,0,0), which inverts to white and can bleed
    # into anti-aliased edges on a non-premultiplied resize. Neutralise them.
    out.paste((90, 70, 60, 0), mask=alpha.point(lambda v: 255 if v == 0 else 0))
    out.save(dst)
    return out

lab_invert(sys.argv[1], sys.argv[2])

# Usage:  python3 tools/darkfig-lab-invert.py in.png out.png
#
# Use this, NOT tools/darkfig-to-light.py, when the DATA COLOURS themselves were
# chosen for a dark background — i.e. the colormap's bright end carries the
# strong signal. darkfig-to-light.py only inverts near-neutral pixels, so it
# fixes white axes and labels but leaves the data ramp running the wrong way for
# paper (and it once turned Kaiser-Squires' grey contour coding into black
# halos). This script inverts L* for every pixel, which reverses the ramp.
