#!/usr/bin/env python3
"""The shapes of the two wavelet statistics, drawn smoothly for the slide.

Slide 40 says peak counts and the starlet l1-norm are one-point statistics on
the same decomposition, and then shows a peak map and a formula. What it never
shows is what the statistics LOOK like - which is the thing that makes the pair
concrete, and the thing that separates them: peak counts live on the positive
side of the field and fall by decades from the finest scale to the coarsest,
while the l1-norm is bimodal about zero, reading voids as well as peaks, with
comparable amplitude at every scale because it uses every pixel.

The measured versions of both are noisy single-realisation curves, and the ones
in the papers are laid out as method or cosmology comparisons that do not fit a
block on a slide. These are therefore SMOOTH, SYNTHETIC curves with the correct
qualitative behaviour, drawn from the same analytic family the real ones follow,
and the slide labels them schematic. They illustrate the shape of a statistic;
they are not a measurement, and no number is read off them.

  peaks  a skew-normal in S/N, amplitude falling by a factor of about four per
         scale - coarser bands have far fewer independent resolution elements,
         hence far fewer maxima. Reference: assets/.../starlet_peaks_thumb.png.
  l1     |nu| times a skewed coefficient distribution, which is what produces
         the dip at zero (small coefficients contribute nothing to a sum of
         absolute values) and a hump either side of it. Coarser scales are
         broader and flatter. Reference: the measured curve Andreas supplied.

Run with a python that has numpy and matplotlib:

    /usr/local/bin/python3 tools/make-hos-shapes.py

Writes assets/diagrams/hos_peaks_shape.png and assets/diagrams/hos_l1_shape.png.
"""
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PAPER  = "#f7f5f0"
INK    = "#1c1c22"
MUTED  = "#6a6760"
EDGE   = "#c9c6c0"

# one ramp, shared by both figures, so a colour means the same scale in each
SCALE_COLS = ["#2f49c0", "#5a6fd0", "#8f7fb5", "#c07a86", "#d96a1f"]
NS = 5


def phi(x):
    return np.exp(-0.5 * x ** 2) / math.sqrt(2 * math.pi)


def Phi(x):
    return np.array([0.5 * (1.0 + math.erf(v / math.sqrt(2.0))) for v in np.ravel(x)]
                    ).reshape(np.shape(x))


def skewnorm(x, mu, sigma, alpha):
    z = (x - mu) / sigma
    return 2.0 / sigma * phi(z) * Phi(alpha * z)


def style(ax, xlabel, ylabel):
    # transparent: the figure sits inside a block whose surface is not the page
    # paper, and an opaque canvas shows up as a lighter rectangle inside it.
    ax.set_facecolor("none")
    ax.set_xlabel(xlabel, color=MUTED, fontsize=12.5, labelpad=4)
    ax.set_ylabel(ylabel, color=MUTED, fontsize=12.5, labelpad=4)
    ax.tick_params(colors=MUTED, labelsize=11, length=3)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(EDGE)
    leg = ax.legend(frameon=False, fontsize=11, labelspacing=0.32,
                    handlelength=1.5, borderpad=0.1)
    for txt in leg.get_texts():
        txt.set_color(MUTED)
    ax.text(0.995, 1.02, "schematic", transform=ax.transAxes, ha="right",
            va="bottom", color=MUTED, fontsize=10, style="italic")


# ------------------------------- peak counts --------------------------------
nu = np.linspace(-1.6, 6.4, 800)
figA, axA = plt.subplots(figsize=(5.6, 3.8))
for j in range(NS):
    amp = 3000.0 / (4.0 ** j)
    mu = 0.62 + 0.10 * j
    sig = 1.35 - 0.11 * j
    y = amp * skewnorm(nu, mu, sig, 2.2) / skewnorm(np.array([mu + 0.5 * sig]),
                                                    mu, sig, 2.2)[0]
    axA.plot(nu, y, color=SCALE_COLS[j], lw=2.1, label="scale %d" % (j + 1))
axA.set_yscale("log")
axA.set_xlim(-1.6, 6.4)
axA.set_ylim(0.7, 8e3)
style(axA, "S/N", "peak counts")
figA.subplots_adjust(left=0.135, right=0.985, top=0.92, bottom=0.145)
figA.savefig("assets/diagrams/hos_peaks_shape.png", dpi=200, transparent=True)
print("wrote assets/diagrams/hos_peaks_shape.png")

# -------------------------------- l1-norm -----------------------------------
nu = np.linspace(-6.0, 6.0, 1200)
figB, axB = plt.subplots(figsize=(5.6, 3.8))
# a single common normalisation, so the curves keep their relative heights:
# a broader coefficient distribution spreads the same total over more bins, so
# the coarse scales come out lower and wider on their own.
SIG = [1.05, 1.15, 1.28, 1.45, 1.75]
curves = [np.abs(nu) * skewnorm(nu, 0.05, SIG[j], 0.18) for j in range(NS)]
top = max(c.max() for c in curves)
for j, y in enumerate(curves):
    axB.plot(nu, y / top, color=SCALE_COLS[j], lw=2.1,
             label="scale %d" % (j + 1))
axB.set_xlim(-6, 6)
axB.set_ylim(0, 1.12)
axB.set_yticks([])
style(axB, "S/N", r"$\ell_1$ per bin")
figB.subplots_adjust(left=0.075, right=0.985, top=0.92, bottom=0.145)
figB.savefig("assets/diagrams/hos_l1_shape.png", dpi=200, transparent=True)
print("wrote assets/diagrams/hos_l1_shape.png")
