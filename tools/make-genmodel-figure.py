#!/usr/bin/env python3
"""The generative-modelling triptych: true density, the samples we actually see,
and the model fitted to them.

Drawn rather than lifted from another deck's slides. The target is two moons
rather than a Gaussian blob: a Gaussian would make the middle panel look like a
solved problem, and the whole point is that the distribution is something no
closed form is going to hand you.

The model panel is a real kernel density estimate of the finite sample with a
slightly generous bandwidth, so it is close to the truth without being identical
— which is what a fitted model actually looks like.

    /usr/local/bin/python3 tools/make-genmodel-figure.py

Writes assets/diagrams/generative_modelling.png.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PAPER  = "#f7f5f0"
INK    = "#1c1c22"
ACCENT = "#2f49c0"

rng = np.random.default_rng(11)
LIM = (-1.6, 2.6, -1.1, 1.7)
gx, gy = np.meshgrid(np.linspace(LIM[0], LIM[1], 340),
                     np.linspace(LIM[2], LIM[3], 340))


def moons(n, noise=0.075):
    """The classic two-moons: two facing half-circles."""
    k = n // 2
    t = np.pi * rng.random(k)
    a = np.stack([np.cos(t), np.sin(t)], axis=1)
    t = np.pi * rng.random(n - k)
    b = np.stack([1 - np.cos(t), 0.5 - np.sin(t)], axis=1)
    return np.vstack([a, b]) + rng.normal(scale=noise, size=(n, 2))


def kde(pts, bw):
    d = np.zeros_like(gx)
    for px, py in pts:
        d += np.exp(-0.5 * ((gx - px) ** 2 + (gy - py) ** 2) / bw ** 2)
    return d / d.max()


true = kde(moons(4000, 0.055), 0.055)      # the truth: dense and sharp
pts = moons(300)                            # what we are given
model = kde(pts, 0.115)                     # what a model fits to it

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.0))
fig.patch.set_facecolor(PAPER)

panels = [
    (true,  r"true  $\mathbb{P}$",             "img"),
    (pts,   r"samples  $x_i \sim \mathbb{P}$", "pts"),
    (model, r"model  $\mathbb{P}_\theta$",     "img"),
]
for ax, (data, title, kind) in zip(axes, panels):
    ax.set_facecolor(PAPER)
    if kind == "img":
        ax.imshow(data ** 0.55, extent=LIM, origin="lower",
                  cmap="viridis", interpolation="bilinear")
    else:
        ax.scatter(pts[:, 0], pts[:, 1], s=11, color=ACCENT, alpha=0.85,
                   linewidths=0)
    ax.set_xlim(LIM[0], LIM[1]); ax.set_ylim(LIM[2], LIM[3])
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_aspect("equal")
    ax.set_title(title, color=INK, fontsize=15, pad=12)
    for sp in ax.spines.values():
        sp.set_color("#00000022")

fig.subplots_adjust(left=0.02, right=0.98, top=0.86, bottom=0.04, wspace=0.16)
fig.savefig("assets/diagrams/generative_modelling.png", dpi=200, facecolor=PAPER)
print("wrote assets/diagrams/generative_modelling.png")
