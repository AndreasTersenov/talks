#!/usr/bin/env python3
"""A small Metropolis-Hastings animation for the classical-inference slide.

Why generated rather than borrowed: the obvious candidates online are watermarked
third-party work and run to ~14 MB apiece. This repository is public and served on
GitHub Pages, so it draws its own — in the deck's light palette, at a size that
belongs in a corner of a slide (a few hundred kB).

The target is a correlated 2-D Gaussian, which is the honest illustration for this
slide: it is the shape a Gaussian likelihood with a fixed covariance actually
produces, and the anticorrelation is the degeneracy the room expects to see in an
Omega_m - sigma_8 plane.

    /usr/local/bin/python3 tools/make-mcmc-gif.py

Writes assets/misc/mcmc_sampling.gif.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

PAPER  = "#f7f5f0"
INK    = "#1c1c22"
MUTED  = "#6a6760"
ACCENT = "#2f49c0"

OUT     = "assets/misc/mcmc_sampling.gif"
FRAMES  = 70
PER     = 55          # chain steps revealed per frame
STEP    = 0.42        # proposal width
rng     = np.random.default_rng(7)

MU  = np.array([0.30, 0.81])
COV = np.array([[0.0016, -0.0021], [-0.0021, 0.0049]])
INV = np.linalg.inv(COV)


def logp(x):
    d = x - MU
    return -0.5 * d @ INV @ d


# ------------------------------------------------------------------ the chain
n = FRAMES * PER
chain = np.empty((n, 2))
x = np.array([0.24, 0.94])
lp = logp(x)
sd = np.sqrt(np.diag(COV))
for i in range(n):
    prop = x + rng.normal(scale=STEP * sd, size=2)
    lpp = logp(prop)
    if np.log(rng.random()) < lpp - lp:
        x, lp = prop, lpp
    chain[i] = x

# ----------------------------------------------------------------- the frames
gx, gy = np.meshgrid(np.linspace(0.20, 0.40, 200), np.linspace(0.66, 0.96, 200))
pts = np.stack([gx.ravel(), gy.ravel()], axis=1) - MU
dens = np.exp(-0.5 * np.einsum("ij,jk,ik->i", pts, INV, pts)).reshape(gx.shape)

frames = []
for f in range(FRAMES):
    k = (f + 1) * PER
    fig, ax = plt.subplots(figsize=(3.6, 2.7), dpi=100)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    ax.contour(gx, gy, dens, levels=[0.11, 0.37, 0.78], colors=MUTED,
               linewidths=0.8, alpha=0.75)
    ax.plot(chain[:k, 0], chain[:k, 1], color=ACCENT, lw=0.35, alpha=0.28)
    ax.scatter(chain[:k, 0], chain[:k, 1], s=3.2, color=ACCENT, alpha=0.30,
               linewidths=0)
    ax.scatter(*chain[k - 1], s=26, color="#c2521f", zorder=5, linewidths=0)
    ax.set_xlim(0.20, 0.40); ax.set_ylim(0.66, 0.96)
    ax.set_xlabel(r"$\Omega_m$", color=MUTED, fontsize=9, labelpad=1)
    ax.set_ylabel(r"$\sigma_8$", color=MUTED, fontsize=9, labelpad=1)
    ax.tick_params(colors=MUTED, labelsize=7, length=2)
    for sp in ax.spines.values():
        sp.set_color("#00000022")
    fig.tight_layout(pad=0.4)
    fig.canvas.draw()
    frames.append(Image.frombuffer(
        "RGBA", fig.canvas.get_width_height(),
        fig.canvas.buffer_rgba(), "raw", "RGBA", 0, 1).convert("RGB"))
    plt.close(fig)

frames = [im.convert("P", palette=Image.ADAPTIVE, colors=32) for im in frames]
frames[0].save(OUT, save_all=True, append_images=frames[1:],
               duration=70, loop=0, optimize=True)
print("wrote", OUT, frames[0].size)
