#!/usr/bin/env python3
"""The SBI pipeline as ONE diagram — a redraw of thesis figure F6b_stages.

Split into three separate panels the procedure stops reading as a procedure: the
(theta, x) pairs produced on the left have to visibly travel into the network in
the middle, and the trained network has to visibly produce the posterior on the
right. So this is a single figure, with the three stages marked underneath by
brackets rather than cut apart.

Adapted for the slide in two ways beyond the palette:

  * the three stages sit on tinted panels — warm for the simulator, which is the
    physics half, cobalt for the learning and inference halves — so the eye can
    take the figure in as three regions before reading any of it;
  * it is emitted THREE times, cumulatively, on an identical canvas, so the slide
    can build it up while it is being narrated. Same extent, same crop: they are
    designed to be stacked and revealed, not cropped to content.

    /usr/local/bin/python3 tools/make-sbi-pipeline.py

Writes assets/diagrams/sbi_build_1.png, _2.png, _3.png.

NOT sbi_pipeline.png: assets/ is case-insensitive on macOS and SBI_pipeline.png
already exists there, referenced by eight other decks. Writing the lowercase name
silently overwrites it.
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
WARM   = "#c2521f"
rng = np.random.default_rng(5)

PANELS = [
    (1.0, 26.0, "#c2521f", 0.055),     # the simulator: physics
    (27.5, 70.5, ACCENT,   0.055),     # the flow: learning
    (72.0, 99.0, ACCENT,   0.030),     # inference
]


def draw(upto):
    fig, ax = plt.subplots(figsize=(13.6, 5.6), dpi=200)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(0, 100); ax.set_ylim(-10, 50)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect("equal")
    for sp in ax.spines.values():
        sp.set_visible(False)

    def arrow(x0, y0, x1, y1, color=MUTED, lw=1.4, ls="-"):
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                     mutation_scale=13, lw=lw, color=color,
                                     linestyle=ls, shrinkA=0, shrinkB=0,
                                     joinstyle="miter"))

    def blob(cx, cy):
        """A posterior drawn as contours of an actual mixture, not as one outline
        scaled three times — nested copies of a single shape are the tell that a
        blob was drawn rather than computed, and real credible regions change
        shape as they tighten."""
        gx, gy = np.meshgrid(np.linspace(cx - 13, cx + 13, 420),
                             np.linspace(cy - 11, cy + 11, 420))
        K = 1.4                                   # overall size of the credible region
        comps = [((-1.9,  0.9), (3.4, 1.5), -0.62, 1.00),
                 (( 1.2, -0.3), (2.1, 2.2),  0.35, 0.86),
                 (( 2.8,  1.6), (1.6, 1.0),  1.15, 0.42),
                 ((-0.6, -1.6), (1.4, 0.9), -0.20, 0.34)]
        comps = [((mx * K, my * K), (sa * K, sb * K), ang, w)
                 for (mx, my), (sa, sb), ang, w in comps]
        d = np.zeros_like(gx)
        for (mx, my), (sa, sb), ang, w in comps:
            ca, sa_ = np.cos(ang), np.sin(ang)
            dx, dy = gx - (cx + mx), gy - (cy + my)
            u = ca * dx + sa_ * dy
            v = -sa_ * dx + ca * dy
            d += w * np.exp(-0.5 * ((u / sa) ** 2 + (v / sb) ** 2))
        d /= d.max()
        # contourf cannot take per-level alpha, so each band is filled separately,
        # outermost first — a single call with alpha would paint one flat shape.
        for lo, a in ((0.10, 0.18), (0.30, 0.34), (0.60, 0.85)):
            ax.contourf(gx, gy, d, levels=[lo, 1.001], colors=[ACCENT],
                        alpha=a, zorder=2)

    # the tinted regions, one per stage revealed so far
    for k, (x0, x1, col, alpha) in enumerate(PANELS[:upto], start=1):
        ax.add_patch(FancyBboxPatch((x0, -8.4), x1 - x0, 57.6,
                                    boxstyle="round,pad=0.6,rounding_size=1.6",
                                    facecolor=col, alpha=alpha, edgecolor="none",
                                    zorder=0))

    rng = np.random.default_rng(5)

    # ======================================================== 1. simulation
    ax.text(13, 47.5, r"prior  $\pi(\theta)$", ha="center", fontsize=12.5, color=INK)
    for w, a in ((9.0, 0.18), (6.0, 0.34), (3.2, 0.85)):
        ax.add_patch(Ellipse((13, 41), w, 0.62 * w, angle=25, facecolor=ACCENT,
                             alpha=a, edgecolor="none"))
    th = rng.multivariate_normal([13, 41], [[2.4, 1.2], [1.2, 1.2]], 10)
    ax.scatter(th[:, 0], th[:, 1], s=11, color=INK, zorder=5, linewidths=0)

    arrow(13, 36.5, 13, 31.5)
    ax.text(14.4, 34, r"$\theta$", fontsize=12, color=MUTED)

    ax.add_patch(FancyBboxPatch((7.5, 25.0), 11, 6, boxstyle="round,pad=0.4",
                                facecolor=PAPER, edgecolor=INK, lw=1.5))
    ax.text(13, 28.0, "simulator", ha="center", va="center", fontsize=12, color=INK)

    arrow(13, 24.0, 13, 19.5)
    xs = rng.normal(size=(600, 2))
    px = 13 + 3.1 * xs[:, 0]
    py = 13.5 + 1.5 * (xs[:, 1] + 0.7 * xs[:, 0] ** 2 - 0.9)
    keep = (px > 4) & (px < 22) & (py > 7.5) & (py < 19)
    ax.scatter(px[keep], py[keep], s=3.2, color=ACCENT, alpha=0.55, linewidths=0)
    ax.text(13, 5.0, r"simulated data   $x \sim p(x \mid \theta)$",
            ha="center", fontsize=12, color=INK)

    # ========================================================== 2. learning
    if upto >= 2:
        ax.text(37, 40.5, r"base  $\mathcal{N}$", ha="center", fontsize=12.5,
                color=INK)
        for w, a in ((8.0, 0.18), (5.2, 0.34), (2.8, 0.85)):
            ax.add_patch(Ellipse((37, 30), w, w * 0.62 * 1.6, facecolor=ACCENT,
                                 alpha=a, edgecolor="none"))
        arrow(42.5, 30, 48.5, 30)

        cols = [(52, 3), (56.5, 4), (61, 4), (65.5, 2)]
        prev = None
        for cx, k in cols:
            ys = np.linspace(30 - 2.6 * (k - 1) / 2, 30 + 2.6 * (k - 1) / 2, k)
            if prev is not None:
                for y0 in prev[1]:
                    for y1 in ys:
                        ax.plot([prev[0], cx], [y0, y1], color=SOFT, lw=0.5, zorder=1)
            ax.scatter([cx] * k, ys, s=70, facecolor=PAPER, edgecolor=ACCENT,
                       lw=1.3, zorder=3)
            prev = (cx, ys)
        ax.text(58.7, 40.5, r"conditional flow   $q_\phi(\theta \mid x)$",
                ha="center", fontsize=12.5, color=ACCENT)

        ax.plot([21, 58.7], [13.5, 13.5], color=INK, lw=1.3, solid_capstyle="butt")
        arrow(58.7, 13.5, 58.7, 25.5, color=INK)
        ax.text(40, 15.4, r"the pairs  $(\theta,\, x)$", ha="center", fontsize=12,
                color=INK)
        ax.text(40, 10.6, "trained by maximum likelihood", ha="center",
                fontsize=10.5, color=MUTED)

    # ========================================================= 3. inference
    if upto >= 3:
        ax.add_patch(FancyBboxPatch((73.5, 42.5), 21, 5.6, boxstyle="round,pad=0.4",
                                    facecolor=PAPER, edgecolor=INK, lw=1.5))
        ax.text(84, 45.3, r"observed  $x_{\rm obs}$", ha="center", va="center",
                fontsize=12, color=INK)
        arrow(84, 41.6, 84, 36.5)
        arrow(68.5, 30, 74.0, 30, color=WARM)
        ax.text(71.3, 32.2, "trained", ha="center", fontsize=10.5, color=WARM)
        blob(84.5, 29.0)
        ax.text(84, 14.5, "posterior estimate", ha="center", fontsize=12, color=INK)
        ax.text(84, 10.3, r"$q_\phi(\theta \mid x_{\rm obs})$", ha="center",
                fontsize=13, color=ACCENT)

    # ============================================================= captions
    STAGES = [(3.5, 22.5, "1.  Simulation", "draw $\\theta$, simulate,\nkeep the $(\\theta,\\, x)$ pairs"),
              (29.5, 68.5, "2.  Learning",  "fit the conditional flow\non those pairs"),
              (74.0, 97.0, "3.  Inference", "evaluate at $x_{\\rm obs}$;\ncheap to repeat")]
    for k, (x0, x1, name, sub) in enumerate(STAGES[:upto], start=1):
        col = "#c2521f" if k == 1 else ACCENT
        ax.text((x0 + x1) / 2, -3.2, name, ha="center", va="top", fontsize=13,
                color=col)
        ax.text((x0 + x1) / 2, -5.1, sub, ha="center", va="top", fontsize=10.5,
                color=MUTED, linespacing=1.4)

    fig.subplots_adjust(0, 0, 1, 1)
    out = f"assets/diagrams/sbi_build_{upto}.png"
    fig.savefig(out, facecolor=PAPER)      # NO bbox_inches: the three must align
    plt.close(fig)
    print("wrote", out)


for k in (1, 2, 3):
    draw(k)
