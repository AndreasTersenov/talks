#!/usr/bin/env python3
"""The radio-interferometry / weak-lensing parallel, as six simulated panels.

For the UVA / NRAO colloquium (2026-10): the bridge slide after "mass mapping is an ill-posed
inverse problem". Two rows, the same three steps in each:

    radio     the sky          ->  uv coverage (what an interferometer samples)  ->  dirty image
    lensing   the mass map     ->  shear sticks, masked and noisy               ->  Kaiser-Squires

Everything here is an ILLUSTRATION made for the slide (a toy radio sky, a lognormal field, a toy
VLA-like array, a toy mask), not data and not a paper result; the slide says so.

    venv/bin/python tools/make-imaging-parallel.py      # writes assets/diagrams/imaging_parallel/*.png

Needs numpy, scipy and matplotlib. Fixed seeds, so it is reproducible.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm, Normalize
from scipy.ndimage import gaussian_filter

N = 256                     # grid
PX = 600                    # output panel size, pixels
CMAP = "inferno"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "diagrams", "imaging_parallel")
BG = "black"


def save(arr_or_fn, name, norm=None):
    fig = plt.figure(figsize=(PX / 100, PX / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG)
    fig.patch.set_facecolor(BG)
    if callable(arr_or_fn):
        arr_or_fn(ax)
    else:
        ax.imshow(arr_or_fn, cmap=CMAP, norm=norm, origin="lower", interpolation="bilinear")
    ax.set_xlim(-0.5, N - 0.5)
    ax.set_ylim(-0.5, N - 0.5)
    ax.axis("off")
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=100, facecolor=BG)
    plt.close(fig)
    print("wrote", os.path.normpath(path))


def gauss2d(x0, y0, sx, sy, theta=0.0, amp=1.0):
    y, x = np.mgrid[0:N, 0:N]
    c, s = np.cos(theta), np.sin(theta)
    xr = c * (x - x0) + s * (y - y0)
    yr = -s * (x - x0) + c * (y - y0)
    return amp * np.exp(-0.5 * ((xr / sx) ** 2 + (yr / sy) ** 2))


# ----------------------------------------------------------------------------- radio
def radio_sky(rng):
    sky = np.zeros((N, N))
    # a double-lobed radio galaxy: core, two jets, two lobes with hotspots
    cx, cy, th = 120.0, 136.0, np.deg2rad(28)
    d = np.array([np.cos(th), np.sin(th)])
    sky += gauss2d(cx, cy, 1.2, 1.2, amp=1.0)
    for sgn in (+1, -1):
        for t in np.linspace(6, 44, 28):
            px, py = np.array([cx, cy]) + sgn * t * d
            sky += gauss2d(px, py, 1.0, 1.0, amp=0.10)
        lx, ly = np.array([cx, cy]) + sgn * 52 * d
        sky += gauss2d(lx, ly, 11, 6.5, th, amp=0.32)
        hx, hy = np.array([cx, cy]) + sgn * 58 * d
        sky += gauss2d(hx, hy, 1.6, 1.6, amp=0.9)
    # compact sources
    for _ in range(9):
        x, y = rng.uniform(20, N - 20, 2)
        sky += gauss2d(x, y, 1.0, 1.0, amp=rng.uniform(0.25, 0.8))
    # one faint extended source
    sky += gauss2d(196, 62, 16, 12, 0.6, amp=0.10)
    return sky


def uv_tracks():
    """A toy VLA-like Y array (9 antennas per arm), a one-hour track: the six spokes of a snapshot,
    smeared into short arcs, so the coverage is visibly incomplete."""
    arms = np.deg2rad([5.0, 125.0, 245.0])
    r = (np.arange(1, 10) / 9.0) ** 1.716
    ants = np.array([[ri * np.sin(a), ri * np.cos(a)] for a in arms for ri in r])
    bl = np.array([ants[j] - ants[i] for i in range(len(ants)) for j in range(i + 1, len(ants))])
    dec = np.deg2rad(45.0)
    uv = []
    for h in np.linspace(-np.pi / 24, np.pi / 24, 14):         # +/- 30 min
        c, s = np.cos(h), np.sin(h)
        u = c * bl[:, 0] - s * bl[:, 1]
        v = (s * bl[:, 0] + c * bl[:, 1]) * np.sin(dec)
        uv.append(np.stack([u, v], 1))
    uv = np.concatenate(uv)
    uv = np.concatenate([uv, -uv])                              # conjugate points
    return uv / np.abs(uv).max() * 0.40 * N                      # in grid frequency units


def radio_panels(rng):
    sky = radio_sky(rng)
    uv = uv_tracks()
    S = np.zeros((N, N))
    iu = np.round(uv[:, 0]).astype(int) % N
    iv = np.round(uv[:, 1]).astype(int) % N
    S[iv, iu] = 1.0
    S[0, 0] = 0.0                                               # no zero spacing
    F = np.fft.fft2(sky)
    noise = (rng.normal(size=F.shape) + 1j * rng.normal(size=F.shape)) * 0.02 * np.abs(F).max() / 40
    dirty = np.real(np.fft.ifft2(S * (F + noise))) / S.sum() * N * N
    dirty /= np.abs(dirty).max()

    save(sky / sky.max(), "radio_sky.png", norm=PowerNorm(0.45, vmin=0, vmax=1))

    def draw_uv(ax):
        ax.scatter(uv[:, 0] + N / 2, uv[:, 1] + N / 2, s=1.6, c="#fcd462", lw=0, alpha=0.9)
        ax.plot([N / 2], [N / 2], marker="+", ms=9, mew=1.2, color="#8a8a96")
    save(draw_uv, "radio_uv.png")

    save(dirty, "radio_dirty.png", norm=Normalize(vmin=-0.12, vmax=0.7))


# ----------------------------------------------------------------------------- lensing
def lognormal_kappa(rng):
    k1 = np.fft.fftfreq(N)[None, :]
    k2 = np.fft.fftfreq(N)[:, None]
    k = np.sqrt(k1 ** 2 + k2 ** 2)
    k[0, 0] = 1.0
    pk = k ** -2.4 * np.exp(-(k / 0.18) ** 2)
    pk[0, 0] = 0.0
    g = np.real(np.fft.ifft2(np.fft.fft2(rng.normal(size=(N, N))) * np.sqrt(pk)))
    g = (g - g.mean()) / g.std()
    kap = np.exp(0.9 * g)
    return (kap - kap.mean()) / kap.std(), k1, k2


def mask_holes(rng):
    y, x = np.mgrid[0:N, 0:N]
    M = np.ones((N, N))
    for _ in range(7):                                          # bright-star holes
        cx, cy = rng.uniform(25, N - 25, 2)
        M[(x - cx) ** 2 + (y - cy) ** 2 < rng.uniform(7, 14) ** 2] = 0
    M[(x > 150) & (x < 168) & (y > 30)] = 0                      # a missing strip
    M[(x < 18) | (y > N - 14)] = 0                               # the survey edge
    return M


def lensing_panels(rng):
    kap, k1, k2 = lognormal_kappa(rng)
    ksq = k1 ** 2 + k2 ** 2
    ksq[0, 0] = 1.0
    P1, P2 = (k1 ** 2 - k2 ** 2) / ksq, 2 * k1 * k2 / ksq
    P1[0, 0] = P2[0, 0] = 0.0                                    # the mass sheet is invisible
    K = np.fft.fft2(kap)
    g1, g2 = np.real(np.fft.ifft2(P1 * K)), np.real(np.fft.ifft2(P2 * K))
    M = mask_holes(rng)
    sn = 3.0 * np.std(g1)                                         # shape noise per pixel
    n1, n2 = rng.normal(size=(N, N)) * sn, rng.normal(size=(N, N)) * sn
    o1, o2 = (g1 + n1) * M, (g2 + n2) * M
    ks = np.real(np.fft.ifft2(P1 * np.fft.fft2(o1) + P2 * np.fft.fft2(o2)))
    ks = gaussian_filter(ks, 1.3)

    lo, hi = np.percentile(kap, [1, 99.7])
    save(kap, "lens_kappa.png", norm=Normalize(vmin=lo, vmax=hi))

    def draw_shear(ax):
        ax.imshow(np.where(M > 0, np.nan, 1.0), cmap="Greys", vmin=0, vmax=1.35, origin="lower",
                  interpolation="nearest", alpha=0.45)            # masked = dark grey
        cell = N // 22
        for i in range(22):
            for j in range(22):
                sl = (slice(i * cell, (i + 1) * cell), slice(j * cell, (j + 1) * cell))
                if M[sl].mean() < 0.6:
                    continue
                a1, a2 = o1[sl][M[sl] > 0].mean(), o2[sl][M[sl] > 0].mean()
                e = np.hypot(a1, a2)
                phi = 0.5 * np.arctan2(a2, a1)
                L = min(e / (2.2 * np.std(g1)) * cell * 1.8, cell * 1.05)
                xc, yc = (j + 0.5) * cell, (i + 0.5) * cell
                dx, dy = 0.5 * L * np.cos(phi), 0.5 * L * np.sin(phi)
                ax.plot([xc - dx, xc + dx], [yc - dy, yc + dy], color="#f2f2f2", lw=1.6,
                        solid_capstyle="round")
    save(draw_shear, "lens_shear.png")

    def draw_ks(ax):
        klo, khi = np.percentile(ks[M > 0], [1, 99.7])
        ax.imshow(ks, cmap=CMAP, norm=Normalize(vmin=klo, vmax=khi), origin="lower",
                  interpolation="bilinear")
        ax.contour(M, levels=[0.5], colors="white", linewidths=0.9, origin="lower")
    save(draw_ks, "lens_ks.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    radio_panels(np.random.default_rng(7))
    lensing_panels(np.random.default_rng(11))
