#!/usr/bin/env python3
"""The radio row of the radio-interferometry / weak-lensing bridge, as four simulated panels.

For the UVA / NRAO colloquium (2026-10): the bridge slide after "mass mapping is an ill-posed
inverse problem" writes d = A s + n once and puts one instrument per row under it:

    radio     visibilities  =  uv coverage  x  the sky  + thermal noise   ->  dirty image

The lensing row is the PnPMass paper's own panels (tools/make-pnp-build.py). The toy lensing
panels and the plug-in-loop tiles this script used to write went with the slides that used them
(2026-10-27); they are in git history.

Everything here is an ILLUSTRATION made for the slide (a toy radio sky, a toy VLA-like array),
not data; the slide says so.

    venv/bin/python tools/make-imaging-parallel.py      # writes assets/diagrams/imaging_parallel/*.png

Needs numpy and matplotlib. Fixed seed, so it is reproducible.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm, Normalize

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

    # the data themselves, for the equation slide: the visibilities on the uv tracks, coloured by
    # amplitude (no new random draws, so the panels above are unchanged)
    amp = np.log10(np.abs((F + noise)[iv, iu]))
    order = np.argsort(amp)

    def draw_vis(ax):
        ax.scatter(uv[order, 0] + N / 2, uv[order, 1] + N / 2, s=3.2, c=amp[order], cmap=CMAP, lw=0)
    save(draw_vis, "radio_vis.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    radio_panels(np.random.default_rng(7))
