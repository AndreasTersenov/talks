#!/usr/bin/env python3
"""The two figure-of-merit comparisons, drawn as stem plots instead of HTML bars.

Slides 21 and 56 each ranked a handful of methods with a `.ladder` of CSS bars.
They read as a web widget rather than as a figure, and they sat next to real
matplotlib panels on the same slide, so the contrast was the problem. These draw
the same numbers in the idiom of the panels beside them: a stem with a diamond
head per method, a full box frame, serif type with STIX math.

Colours are taken FROM the figure each plot has to live beside, so a colour means
the same method on both halves of a slide:

  slide 21  the getdist corner plot `countours_all_methods_MSPC_6scales_light.png`
            -> KS grey #808080, iKS red #e03424, MCALens blue #006fed
  slide 56  the violin panel `p2_cp_fom3_bars/step3.png`
            -> l1+product #d55e00, joint l1 #009e73, CNN #0072b2 (Wong)
            auto-maps has no counterpart there and takes a warm grey, which is
            also the right reading: it is the weakest baseline.

Numbers are the PAPER_FACTS ledger, unchanged:

  slide 21  FoM(Om, h, w0, s8) KS 758 / iKS 755 / MCALens 1947 -> 1.00 / 1.00 / 2.6
            No error bars: Ch2 runs one chain per method, and the slide says so.
  slide 56  FoM3 auto 2448 +/- 27 · +product 3045 +/- 183 · joint 3371 +/- 96 ·
            CNN 3326 +/- 30.  The bars ARE drawn here - the tie claim rests on
            3371 +/- 96 against 3326 +/- 30, and the CSS ladder could not show it.

Run with a python that has numpy and matplotlib:

    /usr/local/bin/python3 tools/make-fom-stems.py

Writes assets/figures/statistics/fom_massmapping_stems.png
   and assets/figures/statistics/fom_summaries_stems.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

PAPER = "#f7f5f0"
INK   = "#1c1c22"
MUTED = "#6a6760"
EDGE  = "#b9b5ae"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["STIX Two Text", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "axes.linewidth": 1.1,
    "xtick.direction": "out",
    "ytick.direction": "out",
})


def trim(path, pad=14):
    """Crop the uniform paper margin.

    The x-axis sub-labels are drawn with clip_on=False, so tight_layout cannot
    see them and the reserved strip is always a little too generous. Rather than
    tune the reserve per figure, save generously and cut back to the ink.
    """
    im = Image.open(path).convert("RGB")
    a = np.asarray(im)
    bg = a[0, 0]
    ink = np.any(np.abs(a.astype(int) - bg.astype(int)) > 6, axis=2)
    rows = np.where(ink.any(axis=1))[0]
    cols = np.where(ink.any(axis=0))[0]
    box = (max(cols[0] - pad, 0), max(rows[0] - pad, 0),
           min(cols[-1] + pad + 1, a.shape[1]), min(rows[-1] + pad + 1, a.shape[0]))
    im.crop(box).save(path)


def frame(ax):
    """The box-and-ticks look of the panels these sit beside."""
    for sp in ax.spines.values():
        sp.set_color(INK)
    ax.set_facecolor(PAPER)
    ax.tick_params(colors=INK, labelcolor=INK, length=4, width=1.0)
    ax.set_axisbelow(True)


def stems(ax, xs, vals, cols, lw=3.4, ms=13):
    for x, v, c in zip(xs, vals, cols):
        ax.vlines(x, 0, v, color=c, lw=lw, zorder=2)
        ax.plot([x], [v], marker="D", ms=ms, color=c,
                markeredgecolor=PAPER, markeredgewidth=1.2, zorder=3)


# ------------------------------------------------------- slide 21: mass mapping
def massmapping():
    names = ["Kaiser–Squires", "inpainting KS", "MCALens"]
    subs  = ["the baseline", "no change", "sparse + Gaussian"]
    vals  = [1.00, 1.00, 2.57]
    tags  = ["1.00×", "1.00×", "2.6×"]
    cols  = ["#808080", "#e03424", "#006fed"]
    xs    = [0, 1, 2]

    fig, ax = plt.subplots(figsize=(5.5, 3.95))
    fig.patch.set_facecolor(PAPER)
    frame(ax)

    ax.axhline(1.0, color=EDGE, lw=1.1, ls=(0, (5, 4)), zorder=1)
    stems(ax, xs, vals, cols)

    for x, v, t, c in zip(xs, vals, tags, cols):
        ax.text(x, v + 0.13, t, ha="center", va="bottom",
                fontsize=15, color=c)

    ax.set_xlim(-0.62, 2.62)
    ax.set_ylim(0, 3.15)
    ax.set_yticks([0, 1, 2, 3])
    ax.set_yticklabels(["0", "1", "2", "3"], fontsize=13)
    ax.set_ylabel("figure of merit, relative to KS",
                  fontsize=13, color=INK, labelpad=6)
    ax.set_xticks(xs)
    ax.set_xticklabels(names, fontsize=13.5, color=INK)
    for x, s in zip(xs, subs):
        ax.text(x, -0.30, s, ha="center", va="top", fontsize=11,
                color=MUTED, style="italic", transform=ax.transData,
                clip_on=False)

    fig.tight_layout(rect=(0, 0.045, 1, 1))
    out = "assets/figures/statistics/fom_massmapping_stems.png"
    fig.savefig(out, dpi=220, facecolor=PAPER)
    trim(out)
    print("wrote", out, Image.open(out).size)


# --------------------------------------------------------- slide 56: summaries
def summaries():
    names = [r"$\ell_1$, auto-maps", r"$\ell_1$ + product",
             r"joint $\ell_1$-norm", "CNN, VMIM"]
    subs  = ["one bin\nat a time", "+ a derived field\nper pair",
             "each pair's full\n2-D distribution", "all four\nchannels at once"]
    vals  = [2448, 3045, 3371, 3326]
    errs  = [27, 183, 96, 30]
    cols  = ["#8a8580", "#d55e00", "#009e73", "#0072b2"]
    xs    = [0, 1, 2, 3]

    fig, ax = plt.subplots(figsize=(7.6, 3.55))
    fig.patch.set_facecolor(PAPER)
    frame(ax)

    ax.axhline(vals[3], color=EDGE, lw=1.1, ls=(0, (5, 4)), zorder=1)
    ax.text(-0.48, vals[3] + 90, "the optimal compressor", ha="left", va="bottom",
            fontsize=11, color=MUTED, style="italic")

    stems(ax, xs, vals, cols, lw=3.2, ms=12)
    for x, v, e, c in zip(xs, vals, errs, cols):
        ax.errorbar([x], [v], yerr=[e], fmt="none", ecolor=c,
                    elinewidth=1.6, capsize=5, capthick=1.6, zorder=4)

    for x, v, e, c in zip(xs, vals, errs, cols):
        ax.text(x, v + e + 120, f"{v}", ha="center", va="bottom",
                fontsize=14.5, color=c)

    ax.set_xlim(-0.55, 3.55)
    ax.set_ylim(0, 4100)
    ax.set_yticks([0, 1000, 2000, 3000, 4000])
    ax.set_yticklabels(["0", "1000", "2000", "3000", "4000"], fontsize=11.5)
    ax.set_ylabel(r"FoM$_3$", fontsize=13.5, color=INK, labelpad=6)
    ax.set_xticks(xs)
    ax.set_xticklabels(names, fontsize=13, color=INK)
    for x, s in zip(xs, subs):
        ax.text(x, -830, s, ha="center", va="top", fontsize=10.5,
                color=MUTED, style="italic", linespacing=1.25, clip_on=False)

    fig.tight_layout(rect=(0, 0.10, 1, 1))
    out = "assets/figures/statistics/fom_summaries_stems.png"
    fig.savefig(out, dpi=220, facecolor=PAPER)
    trim(out)
    print("wrote", out, Image.open(out).size)


massmapping()
summaries()
