#!/usr/bin/env python3
"""Why a wavelet basis is the useful one: almost everything is in almost nothing.

The excursion slide's pop-over needs to show POWER, not layout. A quadrant
mosaic of detail bands is a picture of a file format; this is a picture of the
property the whole talk leans on. Take a photograph, transform it, keep only
the largest few per cent of the coefficients, throw the rest away, and
transform back. The picture survives.

That is the sparsity argument in one image, and it is the same property three
different parts of this thesis rely on: thresholding small coefficients is
denoising (the proximal step in MCALens), and a field whose information sits in
a few localised coefficients per scale is a field a one-point wavelet statistic
can read efficiently.

The transform is the separable CDF 5/3 - the reversible wavelet of JPEG 2000 -
so the claim on the slide ("that is JPEG 2000") is literally what is drawn. The
kept fraction is measured, not asserted: whatever KEEP is set to, the figure
prints what was actually retained.

Run with a python that has numpy, matplotlib and PIL:

    /usr/local/bin/python3 tools/make-wavelet-sparsity.py

Writes assets/diagrams/wavelet_sparsity.png.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

SRC    = "assets/photos/UoC_campus.jpeg"
OUT    = "assets/diagrams/wavelet_sparsity.png"
N      = 512
LEVELS = 5
KEEP   = 0.05          # fraction of coefficients retained

PAPER  = "#f7f5f0"
INK    = "#1c1c22"
MUTED  = "#6a6760"
ACCENT = "#2f49c0"


def fwd(x):
    """One level of CDF 5/3 along the last axis (even length)."""
    s = x[..., 0::2].astype(float)
    d = x[..., 1::2].astype(float)
    d = d - 0.5 * (s + np.concatenate([s[..., 1:], s[..., -1:]], axis=-1))
    s = s + 0.25 * (np.concatenate([d[..., :1], d[..., :-1]], axis=-1) + d)
    return s, d


def inv(s, d):
    """Exact inverse of fwd, undoing update then predict."""
    s = s - 0.25 * (np.concatenate([d[..., :1], d[..., :-1]], axis=-1) + d)
    d = d + 0.5 * (s + np.concatenate([s[..., 1:], s[..., -1:]], axis=-1))
    x = np.empty(s.shape[:-1] + (s.shape[-1] * 2,))
    x[..., 0::2] = s
    x[..., 1::2] = d
    return x


def fwd2(img):
    L, H = fwd(img)                       # split along x
    LL, LH = fwd(L.T)                     # then along y
    HL, HH = fwd(H.T)
    return LL.T, LH.T, HL.T, HH.T


def inv2(LL, LH, HL, HH):
    L = inv(LL.T, LH.T).T
    H = inv(HL.T, HH.T).T
    return inv(L, H)


def analyse(img, levels):
    coeffs, c = [], img.astype(float)
    for _ in range(levels):
        c, LH, HL, HH = fwd2(c)
        coeffs.append((LH, HL, HH))
    return c, coeffs


def synthesise(c, coeffs):
    for LH, HL, HH in reversed(coeffs):
        c = inv2(c, LH, HL, HH)
    return c


im = Image.open(SRC).convert("L")
w, h = im.size
side = min(w, h)
left = min(max(int(0.42 * w) - side // 2, 0), w - side)
img = np.asarray(im.crop((left, 0, left + side, side)).resize((N, N), Image.LANCZOS),
                 dtype=float)

coarse, coeffs = analyse(img, LEVELS)

# the threshold is set on the detail coefficients only: the coarse image is the
# DC of the picture and dropping it would be a different (and dishonest) demo.
allc = np.concatenate([b.ravel() for lvl in coeffs for b in lvl])
ndet = allc.size
keep_n = int(round(KEEP * (ndet + coarse.size)))
keep_n = max(keep_n - coarse.size, 1)
thr = np.partition(np.abs(allc), -keep_n)[-keep_n]

kept = 0
sparse = []
for LH, HL, HH in coeffs:
    trio = []
    for b in (LH, HL, HH):
        m = np.abs(b) >= thr
        kept += int(m.sum())
        trio.append(np.where(m, b, 0.0))
    sparse.append(tuple(trio))

rec = synthesise(coarse.copy(), sparse)
frac = (kept + coarse.size) / (ndet + coarse.size)
print("kept %d of %d coefficients = %.2f%%" % (kept + coarse.size,
                                               ndet + coarse.size, 100 * frac))

fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.75))
fig.patch.set_facecolor(PAPER)
for ax, pic, lab in [(axes[0], img, "the photograph"),
                     (axes[1], rec, "kept the largest %.0f%% of the\nwavelet coefficients"
                      % (100 * frac))]:
    ax.imshow(np.clip(pic, 0, 255), cmap="gray", vmin=0, vmax=255,
              interpolation="bilinear")
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color("#c9c6c0"); s.set_linewidth(0.8)
    ax.set_xlabel(lab, color=MUTED, fontsize=12, labelpad=7)
fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.14, wspace=0.06)
fig.savefig(OUT, dpi=200, facecolor=PAPER)
print("wrote", OUT)
