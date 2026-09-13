#!/usr/bin/env python3
"""A three-panel schematic of conformalised quantile regression, for the CQR
backup slide.

The deck states that the moment network's variance is not calibrated and that
CQR fixes it, but nothing in the deck SHOWS the mechanism, and the mechanism is
three steps that are each obvious once drawn:

  (a)  on held-out examples where the truth is known, draw the network's
       interval and the truth. Some truths fall outside, and more of them than
       the target rate allows.
  (b)  score every example by how far outside it fell - the paper's conformity
       score, max(lo - kappa, kappa - hi), which is negative when the truth is
       inside and then measures the slack. Take the (1 - alpha) quantile q.
  (c)  widen every interval by q on each side. The miscovered fraction is now
       alpha by construction, and q < 0 would shrink them instead.

The numbers here are SYNTHETIC and the panels are labelled schematic: the
figure illustrates the procedure, it is not a measurement. The real before and
after miscoverage rates for PnPMass are in assets/figures/statistics/cqr1.png.

Reference: Romano, Patterson & Candes 2019; the mass-mapping adaptation is
Leterme, Tersenov, Fadili & Starck 2026 (A&A 710, A292), Sect. 5.2.

Run with a python that has numpy and matplotlib:

    /usr/local/bin/python3 tools/make-cqr-schematic.py

Writes assets/diagrams/cqr_schematic.png.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK    = "#1c1c22"
MUTED  = "#6a6760"
EDGE   = "#c9c6c0"
ACCENT = "#2f49c0"
WARN   = "#c2521f"

rng = np.random.default_rng(7)

# One pixel, across the calibration set: the quantile in CQR is taken per pixel
# over the held-out examples, so this is the axis the procedure actually runs on.
N = 14
truth  = rng.normal(0.0, 1.0, N)
centre = truth + rng.normal(0.0, 0.62, N)        # the reconstruction's error
half   = 0.34 + 0.16 * rng.random(N)             # the network's half-interval,
                                                 # too tight, which is the case
                                                 # the paper reports
lo, hi = centre - half, centre + half

# the paper's conformity score: positive when the truth fell outside the
# interval, negative when it fell inside, and then it measures the slack
score = np.maximum(lo - truth, truth - hi)

# alpha is inflated from the paper's 4.55% so that a miss is visible at N = 14
ALPHA = 0.20
q = np.quantile(score, 1 - ALPHA)

fig, ax = plt.subplots(1, 3, figsize=(13.4, 3.5))


def strip(a):
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        a.spines[s].set_color(EDGE)
    a.tick_params(colors=MUTED, labelsize=12, length=3)
    a.set_facecolor("none")


def bars(a, half_i, title):
    x = np.arange(N)
    inside = (truth >= centre - half_i) & (truth <= centre + half_i)
    a.vlines(x, centre - half_i, centre + half_i, color=ACCENT, lw=3.6,
             alpha=0.28, zorder=1)
    a.hlines(centre - half_i, x - 0.26, x + 0.26, color=ACCENT, lw=1.5, zorder=2)
    a.hlines(centre + half_i, x - 0.26, x + 0.26, color=ACCENT, lw=1.5, zorder=2)
    a.scatter(x[inside], truth[inside], s=28, color=INK, zorder=3)
    a.scatter(x[~inside], truth[~inside], s=62, color=WARN, zorder=4,
              marker="X", linewidths=0)
    a.set_xlim(-0.9, N - 0.1)
    a.set_ylim(-3.6, 3.6)
    a.set_xticks([])
    a.set_yticks([-2, 0, 2])
    a.set_title(title, color=INK, fontsize=15, pad=9)
    return int((~inside).sum())


def caption(a, text):
    a.text(0.5, -0.085, text, transform=a.transAxes, ha="center", va="top",
           color=MUTED, fontsize=13)


m0 = bars(ax[0], half, "1.  the network's interval")
caption(ax[0], "%d of %d truths land outside" % (m0, N))
ax[0].set_ylabel(r"$\kappa$ at one pixel", color=MUTED, fontsize=13)

srt = np.sort(score)
ax[1].scatter(np.arange(N), srt, s=36, color=INK, zorder=3)
ax[1].axhline(0.0, color=EDGE, lw=1.2, zorder=1)
# stop the line short of the label, or the glyph is drawn on top of it
ax[1].plot([-0.9, N - 0.15], [q, q], color=WARN, lw=1.8, ls="--", zorder=2)
ax[1].text(N + 0.25, q, "$q$", color=WARN, fontsize=16, va="center", ha="left")
ax[1].text(0.07, 0.94, "outside", transform=ax[1].transAxes, color=MUTED,
           fontsize=12, va="top")
ax[1].text(0.07, 0.08, "inside", transform=ax[1].transAxes, color=MUTED,
           fontsize=12, va="bottom")
ax[1].set_xlim(-0.9, N + 1.9)
ax[1].set_xticks([])
ax[1].set_title("2.  score each one, take the quantile", color=INK, fontsize=15, pad=9)
caption(ax[1], r"$s=\max(\hat\kappa^- - \kappa,\; \kappa - \hat\kappa^+)$, sorted")
ax[1].set_ylabel("conformity score", color=MUTED, fontsize=13)

m1 = bars(ax[2], half + q, "3.  widen every interval by $q$")
caption(ax[2], "%d of %d outside: the rate you asked for" % (m1, N))

for a in ax:
    strip(a)
ax[0].text(0.0, 1.17, "schematic", transform=ax[0].transAxes, ha="left",
           va="bottom", color=MUTED, fontsize=12, style="italic")

fig.subplots_adjust(left=0.052, right=0.995, top=0.83, bottom=0.16, wspace=0.19)
fig.savefig("assets/diagrams/cqr_schematic.png", dpi=200, transparent=True)
print("wrote assets/diagrams/cqr_schematic.png  (%d -> %d miscovered of %d, q = %+.2f)"
      % (m0, m1, N, q))
