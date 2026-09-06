#!/usr/bin/env python3
"""What a wavelet transform actually DOES, drawn on a convergence field.

The first version of the excursion slide showed a wavelet shape and a set of
1-D bands, and it did not land: you could see the pieces without ever seeing
the operation, and nothing on the slide looked like the data the talk is about.
This draws the operation itself, twice, on a 2-D field:

    kappa  (*)  psi at a small size   =  one map of the small structure
    kappa  (*)  psi at a large size   =  one map of the large structure

Convolution is the right verb for this audience: slide the shape over the map
and record the overlap everywhere. Doing it at every size is the transform, and
the output being a MAP at each size - not a curve - is the whole reason a
one-point statistic per scale exists at all, which is the next slide.

The field is synthetic: a Gaussian random field with a power-law spectrum plus
a handful of compact haloes, so that there is real structure at two well
separated sizes and the two band images visibly differ. It illustrates the
operation; it is not data, and the slide does not claim it is.

Run with a python that has numpy and matplotlib:

    /usr/local/bin/python3 tools/make-wavelet-what.py

Writes assets/diagrams/wavelet_what.png.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PAPER  = "#f7f5f0"
INK    = "#1c1c22"
MUTED  = "#6a6760"
ACCENT = "#2f49c0"

H1 = np.array([1.0, 4.0, 6.0, 4.0, 1.0]) / 16.0


def atrous2d(img, nscales):
    """2-D isotropic starlet: bands w_j and the coarse residual c_J."""
    c = np.asarray(img, float)
    bands = []
    for j in range(nscales):
        step = 2 ** j
        k = np.zeros((len(H1) - 1) * step + 1)
        k[::step] = H1
        sm = np.apply_along_axis(
            lambda r: np.convolve(np.pad(r, len(k) // 2, mode="reflect"), k, "valid"),
            0, c)
        sm = np.apply_along_axis(
            lambda r: np.convolve(np.pad(r, len(k) // 2, mode="reflect"), k, "valid"),
            1, sm)
        bands.append(c - sm)
        c = sm
    return bands, c


def kernel(n, step):
    """The 2-D starlet wavelet at one dilation: the band a delta lands in."""
    d = np.zeros((n, n))
    d[n // 2, n // 2] = 1.0
    bands, _ = atrous2d(d, step + 1)
    return bands[step]


# ------------------------------------------------------------------ the field
N = 256
rng = np.random.default_rng(11)
kx = np.fft.fftfreq(N)[:, None]
ky = np.fft.fftfreq(N)[None, :]
k = np.sqrt(kx ** 2 + ky ** 2)
P = np.zeros_like(k)
P[k > 0] = k[k > 0] ** -3.0
field = np.real(np.fft.ifft2(np.fft.fft2(rng.standard_normal((N, N))) * np.sqrt(P)))
field /= field.std()

yy, xx = np.mgrid[0:N, 0:N]


def halo(cx, cy, s, a):
    return a * np.exp(-0.5 * ((xx - cx) ** 2 + (yy - cy) ** 2) / s ** 2)


# compact haloes, sized to land squarely in the fine band, and broad ones for
# the coarse band. Without them a power-law field gives the fine band a uniform
# hash, which shows nothing.
for cx, cy, s, a in [(58, 70, 3.4, 4.0), (150, 48, 3.0, 3.6), (196, 158, 3.6, 3.8),
                     (92, 190, 2.9, 3.2), (210, 96, 3.2, 3.0), (120, 128, 3.1, 3.4)]:
    field += halo(cx, cy, s, a)
for cx, cy, s, a in [(80, 96, 16.0, 2.6), (178, 176, 19.0, 2.4), (60, 190, 13.0, 2.0)]:
    field += halo(cx, cy, s, a)

SMALL, LARGE = 2, 5
bands, _coarse = atrous2d(field, LARGE + 1)


def show(ax, img, cmap="RdBu_r", q=99.0):
    v = np.percentile(np.abs(img), q)
    ax.imshow(img, cmap=cmap, vmin=-v, vmax=v, interpolation="bilinear")
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color("#c9c6c0"); s.set_linewidth(0.8)


fig = plt.figure(figsize=(9.7, 5.6))
fig.patch.set_facecolor(PAPER)
gs = fig.add_gridspec(2, 5, width_ratios=[1.0, 0.20, 1.0, 0.20, 1.0],
                      hspace=0.26, wspace=0.02,
                      left=0.055, right=0.945, top=0.87, bottom=0.07)

KN = 96
for row, (step, lab) in enumerate([(SMALL, "small"), (LARGE, "large")]):
    axk = fig.add_subplot(gs[row, 0])
    show(axk, field)
    if row == 0:
        axk.set_title("a convergence map", color=INK, fontsize=13, pad=8)
        # the other two columns get their headings once, on the top row

    axo = fig.add_subplot(gs[row, 1])
    axo.axis("off")
    axo.text(0.5, 0.5, "$\\circledast$", ha="center", va="center",
             fontsize=21, color=MUTED, transform=axo.transAxes)

    axp = fig.add_subplot(gs[row, 2])
    ker = kernel(KN * 2, step)
    c = KN
    half = 40
    show(axp, ker[c - half:c + half, c - half:c + half], q=99.9)
    axp.set_xlabel("the shape, %s" % lab, color=MUTED, fontsize=11, labelpad=5)

    axe = fig.add_subplot(gs[row, 3])
    axe.axis("off")
    axe.text(0.5, 0.5, "$=$", ha="center", va="center",
             fontsize=19, color=MUTED, transform=axe.transAxes)

    axb = fig.add_subplot(gs[row, 4])
    show(axb, bands[step])
    if row == 0:
        axp.set_title("one shape, at one size", color=INK, fontsize=13, pad=8)
        axb.set_title("a map of that size of structure", color=INK, fontsize=13, pad=8)
    axb.set_xlabel("%s structure, and where it is" % lab,
                   color=MUTED, fontsize=11, labelpad=5)

fig.text(0.50, 0.955,
         "slide the shape over the map and record the overlap everywhere",
         ha="center", color=MUTED, fontsize=12.5)

fig.savefig("assets/diagrams/wavelet_what.png", dpi=200, facecolor=PAPER)
print("wrote assets/diagrams/wavelet_what.png")
