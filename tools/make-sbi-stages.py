#!/usr/bin/env python3
"""Three panels for the simulation-based-inference slide: simulate, learn, infer.

A redraw of the thesis figure F6b_stages in the deck's light palette, split into
three files so the slide can reveal — and dim — one stage at a time. Keeping them
separate is the whole point: a single raster cannot be animated stage by stage.

    /usr/local/bin/python3 tools/make-sbi-stages.py

Writes assets/diagrams/sbi_1_simulate.png, sbi_2_learn.png, sbi_3_infer.png.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Ellipse

PAPER  = "#f7f5f0"
INK    = "#1c1c22"
MUTED  = "#6a6760"
ACCENT = "#2f49c0"
SOFT   = "#b9c2ee"
rng = np.random.default_rng(5)

FIG = dict(figsize=(3.5, 3.2), dpi=200)


def blank(ax):
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect("equal")
    ax.set_facecolor(PAPER)
    for sp in ax.spines.values():
        sp.set_visible(False)


def arrow(ax, x0, y0, x1, y1, color=MUTED, lw=1.2):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                 mutation_scale=11, lw=lw, color=color,
                                 shrinkA=0, shrinkB=0))


def save(fig, name):
    fig.subplots_adjust(0, 0, 1, 1)
    fig.savefig(f"assets/diagrams/{name}", facecolor=PAPER,
                bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    print("wrote", name)


# ------------------------------------------------------- 1. simulate
fig, ax = plt.subplots(**FIG); blank(ax)
for w, a in ((2.9, 0.20), (2.0, 0.34), (1.1, 0.85)):
    ax.add_patch(Ellipse((3.0, 8.5), w, 0.62 * w, angle=25,
                         facecolor=ACCENT, alpha=a, edgecolor="none"))
th = rng.multivariate_normal([3.0, 8.5], [[0.30, 0.16], [0.16, 0.16]], 9)
ax.scatter(th[:, 0], th[:, 1], s=9, color=INK, zorder=4, linewidths=0)
ax.text(3.0, 10.0, r"prior  $\pi(\theta)$", ha="center", fontsize=9, color=INK)

arrow(ax, 3.0, 7.1, 3.0, 5.9)
ax.text(3.35, 6.5, r"$\theta$", fontsize=9, color=MUTED)

ax.add_patch(FancyBboxPatch((1.7, 4.1), 2.6, 1.6, boxstyle="round,pad=0.12",
                            facecolor=PAPER, edgecolor=INK, lw=1.3))
ax.text(3.0, 4.9, "simulator", ha="center", va="center", fontsize=9.5, color=INK)

arrow(ax, 3.0, 3.9, 3.0, 2.9)
xs = rng.normal(size=(320, 2))
ax.scatter(3.0 + 0.95 * xs[:, 0],
           1.5 + 0.40 * (xs[:, 1] + 0.75 * xs[:, 0] ** 2 - 0.9),
           s=2.6, color=ACCENT, alpha=0.5, linewidths=0)
ax.text(7.6, 1.5, r"$x \sim p(x \mid \theta)$", ha="center", fontsize=9, color=INK)
ax.text(7.4, 5.2, "keep the pair", ha="center", fontsize=8.6, color=MUTED)
ax.text(7.4, 4.4, r"$(\theta,\, x)$", ha="center", fontsize=10.5, color=ACCENT)
save(fig, "sbi_1_simulate.png")

# ------------------------------------------------------- 2. learn
fig, ax = plt.subplots(**FIG); blank(ax)
for w, a in ((2.6, 0.20), (1.7, 0.34), (0.9, 0.85)):
    ax.add_patch(Ellipse((1.7, 5.4), w, w, facecolor=ACCENT, alpha=a,
                         edgecolor="none"))
ax.text(1.7, 7.3, r"base $\mathcal{N}$", ha="center", fontsize=9, color=INK)

arrow(ax, 3.1, 5.4, 4.1, 5.4)

cols = [(4.9, 3), (6.3, 4), (7.7, 4), (9.0, 2)]
prev = None
for cx, k in cols:
    ys = np.linspace(5.4 - 0.62 * (k - 1), 5.4 + 0.62 * (k - 1), k)
    if prev is not None:
        for y0 in prev[1]:
            for y1 in ys:
                ax.plot([prev[0], cx], [y0, y1], color=SOFT, lw=0.45, zorder=1)
    ax.scatter([cx] * k, ys, s=42, facecolor=PAPER, edgecolor=ACCENT,
               lw=1.1, zorder=3)
    prev = (cx, ys)
ax.text(6.9, 9.4, r"conditional flow", ha="center", fontsize=9, color=ACCENT)
ax.text(6.9, 8.4, r"$q_\phi(\theta \mid x)$", ha="center", fontsize=10, color=ACCENT)

arrow(ax, 6.9, 2.6, 6.9, 3.5)
ax.text(6.9, 1.9, r"the $(\theta,\, x)$ pairs", ha="center", fontsize=9, color=INK)
ax.text(6.9, 1.0, "maximum likelihood", ha="center", fontsize=8.6, color=MUTED)
save(fig, "sbi_2_learn.png")

# ------------------------------------------------------- 3. infer
fig, ax = plt.subplots(**FIG); blank(ax)
ax.add_patch(FancyBboxPatch((2.2, 8.2), 5.6, 1.4, boxstyle="round,pad=0.12",
                            facecolor=PAPER, edgecolor=INK, lw=1.3))
ax.text(5.0, 8.9, r"observed  $x_{\rm obs}$", ha="center", va="center",
        fontsize=9.5, color=INK)
arrow(ax, 5.0, 8.0, 5.0, 6.6)

t = np.linspace(0, 2 * np.pi, 400)
for sc, a in ((1.55, 0.20), (1.05, 0.34), (0.55, 0.85)):
    r = 1.0 + 0.30 * np.sin(3 * t + 0.6) + 0.16 * np.cos(2 * t)
    ax.fill(5.0 + sc * 1.9 * r * np.cos(t), 4.0 + sc * 1.5 * r * np.sin(t),
            color=ACCENT, alpha=a, lw=0)
ax.text(5.0, 1.3, r"$q_\phi(\theta \mid x_{\rm obs})$", ha="center",
        fontsize=10.5, color=ACCENT)
ax.text(5.0, 0.4, "in milliseconds", ha="center", fontsize=8.6, color=MUTED)
save(fig, "sbi_3_infer.png")
