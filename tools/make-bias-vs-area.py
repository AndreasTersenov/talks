#!/usr/bin/env python3
"""Baryonic bias against survey area, redrawn for a slide, with the survey classes as regions.

The paper figure (Tersenov, Guerrini, Starck & Kilbinger 2026, arXiv:2609.09131, Fig.
`fig:nsigma_vs_area`) is a journal half-column: at slide size its ticks, legend and axis labels
are unreadable. This draws the same points at slide size, in the idiom of the panels the slide
sets it beside (box frame, serif type with STIX math, as tools/make-fom-stems.py), and splits
the area axis into the survey classes (suggested to Andreas, 2026-10-27):

    small surveys    < 3 000 deg2
    Stage III        3 000 - 7 500 deg2     DES (the paper: "Stage III-like ... DES or KiDS")
    Stage IV         7 500 - 20 000 deg2    Euclid ~14 000, Rubin ~18 000 (PAPER_FACTS section 9)
    beyond           20 000 deg2 to the full sky (41 253 deg2)

The class edges are a convention, not a measurement: each sits between the paper's own anchor
areas (2 000 "early data releases", 5 000 Stage III-like, 14 000 Stage IV-like, the full sky),
so every class holds at least one point. The area axis is logarithmic: on the paper's linear
axis the two smaller classes share the left fifth of the plot and their labels collide.

Numbers: read off the paper's vector figure (figures/bias_vs_area_three_stats.pdf in the arXiv
source) on 2026-10-27, calibrated on its own tick marks; the means are the line vertices, the
errors half the error-bar lengths (the standard deviation over five NPE training runs). They
agree with the ledger (PAPER_FACTS: 2.2 / 3.6 / 3.6 sigma at 14 000 deg2; ~0.4 / 0.8 / 1.0 at
2 000). The paper plots no point at the full sky; its largest area is 35 000 deg2.

Run with a python that has numpy and matplotlib:

    venv/bin/python tools/make-bias-vs-area.py

Writes assets/figures/statistics/bias_vs_area_regions.png
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["STIX Two Text", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "axes.linewidth": 1.1,
    "xtick.direction": "out",
    "ytick.direction": "out",
})

PAPER = "#ffffff"          # the slide's background is white, not the warm paper
INK   = "#1c1c22"
MUTED = "#6a6760"

FULL_SKY = 41253
AREA = np.array([2000, 5000, 10000, 14000, 28000, 35000])

# name: (mean n_sigma, std over 5 NPE runs, colour, marker, line style). Colours and markers are
# the paper's (Okabe-Ito blue / vermillion / green; circle / square / triangle).
STATS = {
    "power spectrum": ([0.433, 1.253, 2.096, 2.208, 3.083, 3.567],
                       [0.054, 0.118, 0.216, 0.222, 0.347, 0.478], "#0072B2", "o", "-"),
    "peak counts":    ([0.753, 2.002, 3.082, 3.661, 5.612, 6.236],
                       [0.113, 0.316, 0.431, 0.399, 0.375, 0.512], "#D55E00", "s", (0, (5, 2.2))),
    r"$\ell_1$-norm": ([0.962, 2.408, 3.443, 3.599, 5.669, 6.083],
                       [0.325, 0.159, 0.318, 0.287, 0.437, 0.332], "#009E73", "^",
                       (0, (8, 2.2, 1.6, 2.2))),
}

# (from, to, name, examples): one hue, light to dark, as the classes grow
LEFT = 1000
CLASSES = [
    (LEFT,  3000,     "small\nsurveys", ""),
    (3000,  7500,     "Stage III",      "DES"),
    (7500,  20000,    "Stage IV",       "Euclid, Rubin"),
    (20000, FULL_SKY, "beyond",         ""),
]
TINT = ["#eeeaf8", "#e0d9f2", "#d2c8eb", "#c4b6e4"]


def main():
    fig, ax = plt.subplots(figsize=(6.0, 4.1))
    fig.patch.set_facecolor(PAPER)
    for sp in ax.spines.values():
        sp.set_color(INK)
    ax.tick_params(colors=INK, labelcolor=INK, length=4, width=1.0)
    ax.set_xscale("log")
    ax.set_xlim(LEFT, FULL_SKY)
    ax.set_ylim(0, 8.3)

    for (a0, a1, name, eg), tint in zip(CLASSES, TINT):
        ax.axvspan(a0, a1, color=tint, lw=0, zorder=0)
        mid = np.sqrt(a0 * a1)                              # the middle, on a log axis
        ax.text(mid, 8.05, name, ha="center", va="top", fontsize=14, color=INK, linespacing=1.0)
        if eg:
            ax.text(mid, 7.4, eg, ha="center", va="top", fontsize=12, color=MUTED, style="italic")
    for _, a1, _, _ in CLASSES[:-1]:                        # a hairline of background between classes
        ax.axvline(a1, color=PAPER, lw=2, zorder=0.5)

    for name, (mean, std, colour, marker, ls) in STATS.items():
        ax.errorbar(AREA, mean, yerr=std, color=colour, lw=2.2, ls=ls, marker=marker, ms=8.5,
                    mec=PAPER, mew=1.3, elinewidth=1.6, capsize=3.5, capthick=1.6, zorder=3,
                    label=name)

    ax.set_xticks([1000, 2000, 5000, 10000, 20000, FULL_SKY])
    ax.set_xticklabels(["1 000", "2 000", "5 000", "10 000", "20 000", "full\nsky"], fontsize=13.5)
    ax.minorticks_off()
    ax.set_yticks(range(8))
    ax.set_yticklabels([str(i) for i in range(8)], fontsize=13.5)
    ax.set_xlabel(r"survey area  [deg$^2$]", fontsize=15, color=INK)
    ax.set_ylabel(r"baryonic bias  [$\sigma$]", fontsize=15, color=INK)

    # the legend sits under the plot: inside, every corner holds data or a class label
    fig.legend(loc="lower center", ncol=3, frameon=False, fontsize=14, labelcolor=INK,
               handlelength=2.6, columnspacing=1.6, bbox_to_anchor=(0.53, 0.0))
    fig.tight_layout(rect=(0, 0.075, 1, 1))
    out = "assets/figures/statistics/bias_vs_area_regions.png"
    fig.savefig(out, dpi=220, facecolor=PAPER, bbox_inches="tight", pad_inches=0.06)
    print("wrote", out)


if __name__ == "__main__":
    main()
