#!/usr/bin/env python3
"""The PnPMass panels, cut out of the paper's own build frames, for a loop-and-map slide.

For the UVA / NRAO colloquium (2026-10): version B of the plug-and-play slide draws the loop in
HTML (a data step and a denoiser, lit in turn) and shows the map it produces beside it, the way
Wassim Kabalan's particle-mesh slide does. The panels are REAL, not redrawn: each one is cut from
assets/figures/maps/PnP_1..9.png (the paper figure's build, Leterme, Tersenov, Fadili & Starck
2026), including its frame and the white footprint outline.

    frame   holds
    PnP_4   input gamma (both components), ground truth, iteration 1 (after the data step, after
            the denoiser)
    PnP_7   iteration 2
    PnP_8   iteration 3
    PnP_9   iteration 4

Boxes are the panels' framed squares, found as connected non-white regions of PnP_9 (2026-10-25);
every frame is 2880 x 1620 with the panels in the same places.

The radio-bridge slide (d = A s + n, one row per instrument) takes its lensing row from the same
panels: gamma1/gamma2 as the data, truth as the image we want, after_data_step_1 as the direct
inverse (from kappa = 0, the first data step is tau A^T Sigma^-1 gamma: a noise-weighted
Kaiser-Squires map), and mask.png, the survey mask traced back out of the gamma1 panel (the paper
draws masked pixels a flat light grey). The tracing is a picture of the mask, not the mask array.

    venv/bin/python tools/make-pnp-build.py      # writes assets/figures/maps/pnp_build/*.png

Needs Pillow, numpy and scipy.
"""
import os
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

HERE = os.path.dirname(__file__)
SRC = os.path.join(HERE, "..", "assets", "figures", "maps")
OUT = os.path.join(SRC, "pnp_build")

GAMMA1 = (216, 558, 668, 1010)
GAMMA2 = (217, 1032, 668, 1484)
TRUTH = (2011, 201, 2462, 652)
AFTER_DATA = (1047, 780, 1499, 1232)      # kappa_0^(i), after the forward (data) step
AFTER_DENOISER = (2011, 781, 2462, 1233)  # kappa^(i), after the backward step (the denoiser)

ITERATION_FRAME = {1: 4, 2: 7, 3: 8, 4: 9}


MASKED = (221, 220, 218)   # in the gamma panels, after resampling, within a few levels
OBSERVED = (52, 52, 60)
FRAME = (0, 0, 0)


def crop(frame, box, name):
    im = Image.open(os.path.join(SRC, f"PnP_{frame}.png")).convert("RGB")
    path = os.path.join(OUT, name)
    im.crop(box).save(path, optimize=True)
    print("wrote", os.path.normpath(path))


def mask_from_gamma(name="mask.png"):
    """Masked = the flat light grey: unsaturated and in the grey's brightness band. A median
    filter assigns the drawn white footprint outline, and the stray grey-ish data pixels, to
    whichever side surrounds them."""
    g = np.asarray(Image.open(os.path.join(OUT, "gamma1.png")).convert("RGB")).astype(int)
    sat, mean = g.max(-1) - g.min(-1), g.mean(-1)
    grey = (sat <= 16) & (mean >= 205) & (mean <= 236)
    hole = ndi.binary_opening(ndi.median_filter(grey.astype(np.uint8), size=7).astype(bool))
    frame = g.max(-1) <= 60
    out = np.where(hole[..., None], MASKED, OBSERVED).astype(np.uint8)
    out[frame] = FRAME
    path = os.path.join(OUT, name)
    Image.fromarray(out).save(path, optimize=True)
    print("wrote", os.path.normpath(path))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    crop(4, GAMMA1, "gamma1.png")
    crop(4, GAMMA2, "gamma2.png")
    crop(4, TRUTH, "truth.png")
    for i, f in ITERATION_FRAME.items():
        crop(f, AFTER_DATA, f"after_data_step_{i}.png")
        crop(f, AFTER_DENOISER, f"after_denoiser_{i}.png")
    mask_from_gamma()
