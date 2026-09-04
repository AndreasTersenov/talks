#!/usr/bin/env python3
"""Draw the wavelet primer figure for the defense deck's backup section.

Nothing in `assets/` explains what a wavelet *is* — the deck's starlet figures all
start from a decomposition already taken. This draws the two pictures a question
about wavelets actually needs, in the deck's light palette:

  left   the comparison everyone can anchor on: Fourier's basis is a set of sines,
         each perfectly sharp in frequency and spread over the whole domain; a
         wavelet is one compact shape, dilated — sharp in scale AND in place.
  right  the transform. A 1-D signal carrying a narrow spike, a medium bump and a
         broad swell, and the starlet bands it decomposes into — each feature
         landing in the band whose width matches it, and the sum of the bands plus
         the coarse map reproducing the signal exactly.

Run with a python that has numpy and matplotlib:

    /usr/local/bin/python3 tools/make-wavelet-primer.py

Writes two files, because the deck asks the two questions on separate slides:
assets/diagrams/wavelet_vs_fourier.png (what a wavelet is, against Fourier) and
assets/diagrams/wavelet_bands.png (what the transform does).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PAPER  = "#f7f5f0"
INK    = "#1c1c22"
MUTED  = "#6a6760"
ACCENT = "#2f49c0"
EDGE   = "#c9c6c0"

H = np.array([1.0, 4.0, 6.0, 4.0, 1.0]) / 16.0   # B3-spline filter


def atrous(sig, nscales):
    """Starlet (a-trous) transform: bands w_j and the coarse residual c_J."""
    c = sig.astype(float)
    bands = []
    for j in range(nscales):
        step = 2 ** j
        k = np.zeros((len(H) - 1) * step + 1)
        k[::step] = H
        pad = len(k) // 2
        cp = np.pad(c, pad, mode="reflect")
        cn = np.convolve(cp, k, mode="valid")
        bands.append(c - cn)
        c = cn
    return bands, c


def starlet_wavelet(n=512, step=0):
    """One row of the starlet wavelet: the impulse response of c_j - c_{j+1}.

    The a-trous filter works in samples, so the abscissa is the sample index —
    dilating by 2^j widens the response by exactly that factor.
    """
    x = np.arange(n) - n // 2
    d = np.zeros(n); d[n // 2] = 1.0
    bands, _ = atrous(d, step + 1)
    return x, bands[step]


# ================= figure 1 — the Fourier basis against the wavelet =========
figA, (axF, axW) = plt.subplots(1, 2, figsize=(12.4, 4.4))
figA.patch.set_facecolor(PAPER)
shades = [ACCENT, "#6d80d8", "#a3aee8"]

# --- Fourier: sines, each one frequency, all of them everywhere
axF.set_facecolor(PAPER)
xf = np.linspace(-46, 46, 4000)
for k, lam in enumerate([46.0, 23.0, 11.5]):
    axF.plot(xf, 0.34 * np.cos(2 * np.pi * xf / lam) + 0.62 - 0.62 * k,
             color=shades[k], lw=2.0 - 0.3 * k)
axF.set_xlim(-46, 46)
axF.set_ylim(-1.12, 1.14)
axF.set_yticks([])
axF.set_xlabel("position", color=MUTED, fontsize=11)
axF.set_title("Fourier: sines", color=INK, fontsize=13, pad=12)
axF.text(0, -1.02, "each one frequency, all of them everywhere",
         ha="center", fontsize=10.5, color=MUTED)

# --- wavelets: one shape, dilated, and localised
axW.set_facecolor(PAPER)
for k, step in enumerate([1, 2, 3]):
    x, psi = starlet_wavelet(step=step)
    psi = psi / psi.max()
    axW.plot(x, psi, color=shades[k], lw=2.2 - 0.35 * k,
             label=rf"$\psi(x/2^{{{k+1}}})$", zorder=3 - k)
axW.axhline(0, color=EDGE, lw=0.9, zorder=0)
axW.set_xlim(-46, 46)
axW.set_ylim(-0.62, 1.14)
axW.set_yticks([])
axW.set_xlabel("position", color=MUTED, fontsize=11)
axW.set_title("wavelets: one shape, dilated", color=INK, fontsize=13, pad=12)
axW.legend(frameon=False, fontsize=10.5, loc="upper right",
           labelcolor=INK, handlelength=1.6)
axW.annotate("compact — it dies away",
             xy=(28, 0.005), xytext=(31, 0.46), fontsize=10, color=MUTED,
             ha="center", arrowprops=dict(arrowstyle="-", color=EDGE, lw=1))
axW.text(0, -0.55, "each one scale, and one place",
         ha="center", fontsize=10.5, color=MUTED)

for a in (axF, axW):
    for sp in a.spines.values():
        sp.set_visible(False)
    a.tick_params(colors=MUTED, labelsize=10, length=3)
figA.tight_layout(w_pad=3.0)
figA.savefig("assets/diagrams/wavelet_vs_fourier.png", dpi=200, facecolor=PAPER)
print("wrote assets/diagrams/wavelet_vs_fourier.png")

# ======================= figure 2 — what the transform does =================
figB, ax = plt.subplots(figsize=(9.8, 5.6))
figB.patch.set_facecolor(PAPER)
ax.set_facecolor(PAPER)
n = 1024
t = np.arange(n)
# Three wave packets, an octave and a half apart.  A Gaussian bump is not
# localised in scale — its wavelet response spreads over several bands — whereas
# a packet of wavelength lambda answers in the band that matches lambda, which is
# the thing this figure is trying to show.
def packet(centre, lam, amp=1.0):
    env = np.exp(-0.5 * ((t - centre) / (1.1 * lam)) ** 2)
    return amp * env * np.cos(2 * np.pi * (t - centre) / lam)

sig = packet(200, 7.0) + packet(510, 28.0, 0.95) + packet(830, 110.0, 0.9)
NS = 5
bands, coarse = atrous(sig, NS)

# The five wavelet bands share ONE scale, so their heights can be compared and
# the claim in the title is actually testable on the figure.  Normalising each
# band to its own maximum would put the narrow spike at full height in every
# band, which is the opposite of the point.  The signal and the coarse map are
# each drawn to their own maximum; they are not part of that comparison.
band_scale = max(np.abs(b).max() for b in bands)
rows = [("signal", sig, INK, np.abs(sig).max())] + \
       [(rf"$w_{j+1}$", bands[j], ACCENT, band_scale) for j in range(NS)] + \
       [(rf"$c_{NS}$  coarse", coarse, MUTED, np.abs(coarse).max())]
gap = 1.05
for i, (lab, y, col, sc) in enumerate(rows):
    off = -i * gap
    ax.axhline(off, color=EDGE, lw=0.7, zorder=0)
    ax.plot(t, y / sc * 0.46 + off,
            color=col, lw=1.7 if i == 0 else 1.4, zorder=3)
    ax.text(-40, off, lab, ha="right", va="center", fontsize=11,
            color=INK if i == 0 else MUTED)

for x0, txt in [(200, "small"), (510, "medium"), (830, "large")]:
    ax.annotate(txt, xy=(x0, -(NS + 1) * gap + 0.35), xytext=(x0, 0.86),
                fontsize=10, color=MUTED, ha="center",
                arrowprops=dict(arrowstyle="-", color=EDGE, lw=1, ls=(0, (3, 3))))

ax.set_xlim(-150, n + 10)
ax.set_ylim(-(NS + 1) * gap - 1.15, 1.25)
ax.set_yticks([]); ax.set_xticks([])
ax.set_title("each feature lands in the band that matches its size",
             color=INK, fontsize=13, pad=12)
ax.text(n / 2, -(NS + 1) * gap - 0.86,
        r"signal $=\ w_1 + w_2 + w_3 + w_4 + w_5 + c_5$   — nothing is lost"
        "\n" r"the five bands share one vertical scale",
        ha="center", fontsize=10.5, color=MUTED)

for sp in ax.spines.values():
    sp.set_visible(False)
ax.tick_params(colors=MUTED, labelsize=10, length=3)
figB.tight_layout()
figB.savefig("assets/diagrams/wavelet_bands.png", dpi=200, facecolor=PAPER)
print("wrote assets/diagrams/wavelet_bands.png")
