#!/usr/bin/env python3
"""The normalizing-flow figure: a Gaussian pushed step by step into a target.

Drawn rather than borrowed, in the deck's light palette. The maps are chosen to be
honest about the two claims the slide makes:

  * every step is invertible, so the density can be carried along with the samples;
  * every step has a TRIANGULAR Jacobian — each output coordinate depends only on
    itself and the ones before it — which is exactly why the determinant is cheap.

    /usr/local/bin/python3 tools/make-flow-figure.py

Writes assets/diagrams/normalizing_flow.png.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, PowerNorm

PAPER  = "#f7f5f0"
INK    = "#1c1c22"
MUTED  = "#6a6760"
ACCENT = "#2f49c0"

CMAP = LinearSegmentedColormap.from_list("paper_accent", [PAPER, "#b9c2ee", ACCENT])

rng = np.random.default_rng(3)
z = rng.normal(size=(160000, 2))


def f1(p):                       # bend: x2 depends on x1
    x = p.copy()
    x[:, 1] = p[:, 1] + 0.55 * p[:, 0] ** 2 - 0.9
    return x


def f2(p):                       # stretch each axis on its own
    x = p.copy()
    x[:, 0] = 1.55 * p[:, 0]
    x[:, 1] = 0.62 * p[:, 1]
    return x


def f3(p):                       # a second bend, the other way
    x = p.copy()
    x[:, 1] = p[:, 1] + 0.85 * np.sin(1.15 * p[:, 0])
    return x


stages = [("base", z), ("", f1(z)), ("", f2(f1(z))), ("target", f3(f2(f1(z))))]
labels = [r"$z \sim \mathcal{N}(0,\,\mathbf{1})$", None, None, r"$x = f(z)$"]

fig, axes = plt.subplots(1, 4, figsize=(13.6, 3.7))
fig.patch.set_facecolor(PAPER)

for k, (ax, (name, p)) in enumerate(zip(axes, stages)):
    ax.set_facecolor(PAPER)
    # a square window centred on the cloud, so equal aspect is kept and the
    # shape still fills the panel instead of floating in white space
    lo = np.percentile(p, 0.2, axis=0)
    hi = np.percentile(p, 99.8, axis=0)
    ctr = 0.5 * (lo + hi)
    half = 0.56 * max(hi - lo)
    ext = (ctr[0] - half, ctr[0] + half, ctr[1] - half, ctr[1] + half)
    # a power norm rather than a hard clip: the core keeps an internal gradient
    # instead of flattening into one blue blob
    ax.hexbin(p[:, 0], p[:, 1], gridsize=58, cmap=CMAP, linewidths=0,
              mincnt=1, extent=ext, norm=PowerNorm(0.55))
    ax.set_xlim(ext[0], ext[1]); ax.set_ylim(ext[2], ext[3])
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_aspect("equal", adjustable="box")
    for sp in ax.spines.values():
        sp.set_color("#00000018")
    if labels[k]:
        ax.set_title(labels[k], color=INK, fontsize=12, pad=8)
    else:
        ax.set_title(" ", fontsize=12, pad=8)

# the maps, drawn between the panels
for k, txt in enumerate([r"$f_1$", r"$f_2$", r"$f_3$"]):
    a, b = axes[k].get_position(), axes[k + 1].get_position()
    xm = 0.5 * (a.x1 + b.x0)
    ym = 0.5 * (a.y0 + a.y1)
    fig.text(xm, ym, "→", ha="center", va="center", fontsize=17, color=MUTED)
    fig.text(xm, ym + 0.085, txt, ha="center", va="center", fontsize=12, color=ACCENT)

fig.text(0.5, 0.045,
         "each step is invertible, and each one changes the density by exactly "
         "the volume it stretches or squeezes",
         ha="center", fontsize=10.5, color=MUTED)

fig.subplots_adjust(left=0.02, right=0.98, top=0.88, bottom=0.14, wspace=0.30)
fig.savefig("assets/diagrams/normalizing_flow.png", dpi=200, facecolor=PAPER)
print("wrote assets/diagrams/normalizing_flow.png")
