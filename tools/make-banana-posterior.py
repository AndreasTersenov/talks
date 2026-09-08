#!/usr/bin/env python3
"""A clean two-parameter posterior with the usual curved (banana) degeneracy.

Drawn for the chain diagram on the defense's slide 8, in the deck's light palette:
two filled credible regions (68 and 95 per cent), thin edges, a light frame, small
axis labels, nothing else.  The shape is synthetic on purpose; it stands for "a
posterior", not for any result in the thesis.  numpy + matplotlib only.

    python3 tools/make-banana-posterior.py

Writes assets/figures/posteriors/banana_clean.png (square, transparent margins).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PAPER = "#f7f5f0"
INK = "#1c1c22"
MUTED = "#6a6760"
ACCENT = "#2f49c0"

rng = np.random.default_rng(7)
n = 400_000
t = rng.normal(0.0, 1.0, n)
# a curved ridge: x runs along the banana, y bends with it, both with scatter
x = 0.31 + 0.050 * t + rng.normal(0, 0.013, n)
y = 0.80 - 0.065 * t + 0.022 * t**2 + rng.normal(0, 0.024, n)

xs = np.linspace(0.13, 0.49, 241)
ys = np.linspace(0.64, 1.09, 241)
H, xe, ye = np.histogram2d(x, y, bins=[xs, ys])
# separable Gaussian smoothing, numpy only
def gauss1d(sigma):
    r = int(3 * sigma); k = np.exp(-0.5 * (np.arange(-r, r + 1) / sigma) ** 2); return k / k.sum()
k = gauss1d(3.5)
Z = np.apply_along_axis(lambda v: np.convolve(v, k, mode="same"), 0, H)
Z = np.apply_along_axis(lambda v: np.convolve(v, k, mode="same"), 1, Z).T  # (y, x)
X, Y = np.meshgrid(0.5 * (xe[1:] + xe[:-1]), 0.5 * (ye[1:] + ye[:-1]))

# levels enclosing 68 and 95 per cent of the mass
z = np.sort(Z.ravel())[::-1]
cz = np.cumsum(z) / z.sum()
lev95 = z[np.searchsorted(cz, 0.95)]
lev68 = z[np.searchsorted(cz, 0.68)]

fig, ax = plt.subplots(figsize=(3.2, 3.2), dpi=220)
fig.patch.set_alpha(0)
ax.set_facecolor(PAPER)
ax.contourf(X, Y, Z, levels=[lev95, Z.max()], colors=[ACCENT], alpha=0.26)
ax.contourf(X, Y, Z, levels=[lev68, Z.max()], colors=[ACCENT], alpha=0.5)
ax.contour(X, Y, Z, levels=[lev95, lev68], colors=[ACCENT], linewidths=[1.0, 1.2])
ax.set_xlim(xs[0], xs[-1]); ax.set_ylim(ys[0], ys[-1])
ax.set_xticks([]); ax.set_yticks([])
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color(MUTED); ax.spines[side].set_linewidth(0.8)
ax.set_xlabel(r"$\Omega_\mathrm{m}$", color=INK, fontsize=11, labelpad=4)
ax.set_ylabel(r"$S_8$", color=INK, fontsize=11, labelpad=6, rotation=0, va="center")
# symmetric margins: the frame sits centred in the square image, so the picture
# lines up under whatever is above it on a slide
fig.subplots_adjust(left=0.16, right=0.84, top=0.90, bottom=0.16)
out = "assets/figures/posteriors/banana_clean.png"
fig.savefig(out, dpi=220, transparent=True)
print("wrote", out)
