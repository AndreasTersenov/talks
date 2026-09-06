#!/usr/bin/env python3
"""Draw the wavelet figure for the main talk's excursion slide.

The deck already argues that the power spectrum is blind to WHERE structure sits
(the phases slide). What it lacks is one picture of the instrument that is not,
short enough to sit on a slide that also carries a title, a lede and bullets.
The two backup primers are the long form: one answers "what is a wavelet"
against Fourier, the other walks the full six-band decomposition. This is the
compressed version of both, in one wide, short frame:

  left   the shape at three dilations - compact, oscillating, zero mean, and
         visibly the SAME shape each time. That is the whole definition.
  right  a signal carrying three wave packets of different wavelength at
         different places, and the COMPLETE transform underneath it: every
         band plus the coarse residual, so the reconstruction identity printed
         at the bottom is a claim the figure actually shows rather than one the
         reader has to take on trust.

Wave packets, not Gaussian bumps: a bump is localised in place but not in scale,
so its response smears across several bands, which is the opposite of the point.

The bands share one vertical scale so their heights can be compared and the
claim the figure makes is testable on the figure itself.

Run with a python that has numpy and matplotlib:

    /usr/local/bin/python3 tools/make-wavelet-excursion.py

Writes assets/diagrams/wavelet_excursion.png.
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
    c = np.asarray(sig, float)
    bands = []
    for j in range(nscales):
        step = 2 ** j
        k = np.zeros((len(H) - 1) * step + 1)
        k[::step] = H
        cj = np.convolve(np.pad(c, len(k) // 2, mode="reflect"), k, mode="valid")
        bands.append(c - cj)
        c = cj
    return bands, c


def starlet_profile(n, step):
    """The 1-D starlet wavelet at one dilation: the band a spike lands in."""
    spike = np.zeros(n)
    spike[n // 2] = 1.0
    bands, _ = atrous(spike, step + 1)
    return bands[step]


n = 768
t = np.arange(n)


def packet(centre, lam, amp=1.0):
    env = np.exp(-0.5 * ((t - centre) / (1.1 * lam)) ** 2)
    return amp * env * np.cos(2 * np.pi * (t - centre) / lam)


sig = packet(150, 5.0) + packet(390, 13.0, 0.95) + packet(630, 34.0, 0.9)
NS = 4                                # the whole transform fits on the slide
bands, coarse = atrous(sig, NS)
band_scale = max(np.abs(b).max() for b in bands)

fig = plt.figure(figsize=(12.4, 5.0))
fig.patch.set_facecolor(PAPER)
gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 3.15], wspace=0.10,
                      left=0.02, right=0.985, top=0.86, bottom=0.13)

# ---- left: one shape, three sizes -------------------------------------------
axw = fig.add_subplot(gs[0, 0])
axw.set_facecolor(PAPER)
WIN = 210
for step, off in [(4, 2.30), (5, 1.15), (6, 0.0)]:
    p = starlet_profile(2048, step)
    p = p / p.max() * 0.62
    xx = np.arange(len(p)) - len(p) // 2
    m = np.abs(xx) <= WIN
    axw.axhline(off, color=EDGE, lw=0.8, zorder=0)
    axw.plot(xx[m], p[m] + off, color=ACCENT, lw=2.2, solid_capstyle="round")
axw.set_xlim(-WIN, WIN)
axw.set_ylim(-0.95, 3.30)
axw.set_title("one shape, stretched", color=INK, fontsize=13.5, pad=10)
axw.text(0, -0.78, "compact, oscillating, zero mean",
         ha="center", va="center", color=MUTED, fontsize=11)
for s in axw.spines.values():
    s.set_visible(False)
axw.set_xticks([]); axw.set_yticks([])

# ---- right: slide it across the data ----------------------------------------
axb = fig.add_subplot(gs[0, 1])
axb.set_facecolor(PAPER)
rows = [("signal", sig, INK, np.abs(sig).max(), 1.8)] + \
       [(rf"$w_{j+1}$", bands[j], ACCENT, band_scale, 1.5) for j in range(NS)] + \
       [(rf"$c_{NS}$", coarse, MUTED, np.abs(coarse).max(), 1.5)]
gap = 0.86
for i, (lab, y, col, sc, lw) in enumerate(rows):
    off = -i * gap
    axb.axhline(off, color=EDGE, lw=0.7, zorder=0)
    axb.plot(t, y / sc * 0.45 + off, color=col, lw=lw, zorder=3)
    axb.text(-30, off, lab, ha="right", va="center", fontsize=11.5,
             color=INK if i == 0 else MUTED)

for x0, txt in [(150, "small"), (390, "medium"), (630, "large")]:
    axb.annotate(txt, xy=(x0, -len(rows) * gap + 0.55), xytext=(x0, 0.80),
                 fontsize=10.5, color=MUTED, ha="center",
                 arrowprops=dict(arrowstyle="-", color=EDGE, lw=1, ls=(0, (3, 3))))

axb.set_xlim(-110, n + 8)
axb.set_ylim(-len(rows) * gap - 1.18, 1.15)
axb.set_title("slide it across the data, at every size", color=INK,
              fontsize=13.5, pad=9)
axb.text(n / 2, -len(rows) * gap - 0.34,
         r"each feature answers in the band that matches its size"
         "\n"
         r"signal $=\ w_1 + w_2 + w_3 + w_4 + c_4$   — nothing is lost",
         ha="center", fontsize=10.5, color=MUTED)
for s in axb.spines.values():
    s.set_visible(False)
axb.set_xticks([]); axb.set_yticks([])

fig.savefig("assets/diagrams/wavelet_excursion.png", dpi=200, facecolor=PAPER)
print("wrote assets/diagrams/wavelet_excursion.png")
