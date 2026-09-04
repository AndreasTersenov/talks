#!/usr/bin/env python3
"""The picture everyone has seen: a 2-D wavelet decomposition of a photograph.

Every textbook shows this on a castle, on Barbara, on a teddy bear. Those are
other people's figures and this repository is public, so this draws the same thing
from an image the deck already ships: the University of Crete campus, which is
where the defense happens. It also happens to be an ideal test image — hard
building edges, a repeating olive-grove texture, and broad hills behind, so all
three detail orientations and every level have something to show. A deep
astronomical field does not work here: it is dominated by pixel noise, and every
detail band comes out as salt and pepper.

Three levels of the separable CDF 5/3 transform (the reversible wavelet of
JPEG 2000), laid out in the classical quadrant mosaic: the approximation shrinking
into the top-left corner, and at every level the vertical, horizontal and diagonal
detail bands beside it.

    /usr/local/bin/python3 tools/make-wavelet-image-demo.py

Writes assets/diagrams/wavelet_image_demo.png.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

SRC   = "assets/photos/UoC_campus.jpeg"
OUT   = "assets/diagrams/wavelet_image_demo.png"
N     = 512
LEVELS = 3

PAPER  = "#f7f5f0"
INK    = "#1c1c22"
MUTED  = "#6a6760"
ACCENT = "#2f49c0"


def dwt53(x):
    """One level of the CDF 5/3 transform along the last axis (even length)."""
    s = x[..., 0::2].astype(float)
    d = x[..., 1::2].astype(float)
    s_next = np.concatenate([s[..., 1:], s[..., -1:]], axis=-1)
    d = d - 0.5 * (s + s_next)                       # predict
    d_prev = np.concatenate([d[..., :1], d[..., :-1]], axis=-1)
    s = s + 0.25 * (d_prev + d)                      # update
    return s, d


def dwt53_2d(img):
    """Return LL, (HL vertical, LH horizontal, HH diagonal)."""
    L, H = dwt53(img)                    # along rows -> columns split
    LL, LH = dwt53(L.T)
    HL, HH = dwt53(H.T)
    return LL.T, HL.T, LH.T, HH.T


def stretch(band, pct=99.8, gamma=0.85):
    v = np.abs(band)
    hi = np.percentile(v, pct)
    return np.clip(v / max(hi, 1e-9), 0, 1) ** gamma


# ---------------------------------------------------------------- the mosaic
im = Image.open(SRC).convert("L")
w, h = im.size
side = min(w, h)
cx = int(0.42 * w)                      # the built-up half, not the empty sky
left = min(max(cx - side // 2, 0), w - side)
im = im.crop((left, 0, left + side, side)).resize((N, N), Image.LANCZOS)
img = np.asarray(im, dtype=float) / 255.0

mosaic = np.zeros((N, N))
cur = img
for lev in range(LEVELS):
    LL, HL, LH, HH = dwt53_2d(cur)
    m = LL.shape[0]
    mosaic[0:m,      m:2 * m] = stretch(HL)
    mosaic[m:2 * m,  0:m]     = stretch(LH)
    mosaic[m:2 * m,  m:2 * m] = stretch(HH)
    cur = LL
mosaic[0:cur.shape[0], 0:cur.shape[1]] = (cur - cur.min()) / np.ptp(cur)

# ----------------------------------------------------------------- the figure
fig, ax = plt.subplots(figsize=(6.6, 6.9))
fig.patch.set_facecolor(PAPER)
ax.imshow(mosaic, cmap="gray", vmin=0, vmax=1, interpolation="nearest")
ax.set_xticks([]); ax.set_yticks([])
ax.set_facecolor(PAPER)
for sp in ax.spines.values():
    sp.set_visible(False)

for lev in range(LEVELS):
    m = N // 2 ** (lev + 1)
    ax.plot([0, 2 * m], [m, m], color=ACCENT, lw=1.0, alpha=0.85)
    ax.plot([m, m], [0, 2 * m], color=ACCENT, lw=1.0, alpha=0.85)

k = N // 8
ax.text(k + 6, k - 6, "approximation", color="#ffffff", fontsize=8.5,
        ha="right", va="bottom")
ax.text(3 * N / 4, 12, "vertical detail", color="#ffffff", fontsize=9.5,
        ha="center", va="top")
ax.text(6, 3 * N / 4, "horizontal", color="#ffffff", fontsize=9.5,
        ha="left", va="center", rotation=90)
ax.text(3 * N / 4, N - 10, "diagonal", color="#ffffff", fontsize=9.5,
        ha="center", va="bottom")

ax.set_title("three levels of a 2-D wavelet transform",
             color=INK, fontsize=12.5, pad=10)
fig.text(0.5, 0.03,
         "each level halves the resolution and keeps what was lost",
         ha="center", fontsize=9.5, color=MUTED)

fig.tight_layout(rect=(0, 0.05, 1, 1))
fig.savefig(OUT, dpi=200, facecolor=PAPER)
print("wrote", OUT)
