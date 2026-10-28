#!/usr/bin/env python3
"""The joint l1-norm, built: one point per pixel in the plane of two bins, then the cells.

For the UVA / NRAO colloquium (2026-10-27): route 2 of the cross-bin slide (C29) showed the
paper's joint-histogram figure and the cell-sum formula, two abstractions at once. This builds it
in the visual language of the l1 build two slides earlier (tools/make-l1-sort.py: same starlet,
same colours), one step per click:

    0  one wavelet band in two redshift bins, i and j, beside an empty plane
       (x: the value in bin i, y: the value in bin j)
    1  pair: one pixel, ringed in both maps, becomes one point in the plane
    2  joint distribution: every pixel does; the same matter lenses both bins, so it is
       correlated, along the diagonal
    3  marginals: the per-bin l1 curves of the two bins (|u|-weighted marginals), on the plane's
       top and right edges -- all a per-bin statistic sees of the joint distribution
    4  shuffle: bin j's pixels permuted. Each point keeps its x and moves in y only, the joint
       distribution loses its correlation, and both marginals stay EXACTLY the same (permuting
       one map changes neither per-bin l1): the per-bin statistic cannot tell the two apart
    5  cells: the real joint distribution back, a 10 x 10 grid on the plane (K = 10, as in the paper)
    6  weigh and add up: each point grows with 1/2 (|u_i| + |u_j|), the paper's l1 weight, and
       each cell fills with the sum of its points' weights -- the joint l1-norm of the pair

The fields are an ILLUSTRATION: two lognormal fields built from correlated Gaussian fields
(correlation RHO, the overlap of two adjacent bins' lensing kernels in spirit, not in value),
starlet band w2, values in units of each band's standard deviation as the paper's SNR.

Writes UVA_NRAO_colloquium/joint_l1.js, which drops the SVG into every [data-jl1] element when
the page loads (the two-slide and the one-slide versions share it); the motion is CSS keyed to
the slides' marker fragments (.jm1..6), as for the l1 build, so the PDF shows each click.

    venv/bin/python tools/make-joint-l1.py

Needs numpy, scipy and Pillow.
"""
import base64
import importlib.util
import io
import json
import os

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("l1sort", os.path.join(HERE, "make-l1-sort.py"))
l1sort = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(l1sort)                 # the same starlet and the same colours

OUT = "UVA_NRAO_colloquium/joint_l1.js"

N, SEED, BAND = 32, 3, 1                         # 32 x 32 pixels; band index 1 = w2
SLOPE, SIG, UP, RHO = -2.4, 0.6, 4, 0.82
LO, HI, K = -2.6, 5.4, 10                        # the plane's range; a K x K grid of cells
MARG_BINS = 20                                 # finer bins for the two per-bin l1 curves

# the stage, in SVG units
W, H = 1100, 492                                 # the axis label sits inside
M = 6                                            # a map pixel; each map is N*M = 192 square
MAPI_X, MAPI_Y = 60, 30
MAPJ_X, MAPJ_Y = 60, 262
PX, PY, PS = 560, 104, 330                       # the plane: left, top, side
SH = 66                                          # depth of the marginal strips
DOT_R = 2.4


def correlated_lognormals(n, seed):
    rng = np.random.default_rng(seed)
    big = n * UP
    kx = np.fft.fftfreq(big)[:, None]
    ky = np.fft.fftfreq(big)[None, :]
    k = np.hypot(kx, ky)
    k[0, 0] = 1
    amp = k ** (SLOPE / 2)
    amp[0, 0] = 0

    def grf():
        g = np.real(np.fft.ifft2(np.fft.fft2(rng.standard_normal((big, big))) * amp))
        return g / g.std()

    a, b = grf(), grf()
    out = []
    for g in (a, RHO * a + np.sqrt(1 - RHO ** 2) * b):
        g = g * SIG
        kappa = np.exp(g - SIG ** 2 / 2) - 1
        out.append(kappa.reshape(n, UP, n, UP).mean(axis=(1, 3)))
    return out


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def map_png(u):
    img = np.zeros((N, N, 3), np.uint8)
    for (r, c), v in np.ndenumerate(u):
        img[r, c] = l1sort.colour(v)
    buf = io.BytesIO()
    Image.fromarray(img).resize((N * M, N * M), Image.NEAREST).save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def main():
    ki, kj = correlated_lognormals(N, SEED)
    ui = l1sort.starlet(ki, 3)[0][BAND]
    uj = l1sort.starlet(kj, 3)[0][BAND]
    ui, uj = ui / ui.std(), uj / uj.std()
    for u in (ui, uj):
        assert LO < u.min() and u.max() < HI, (u.min(), u.max())
    corr = np.corrcoef(ui.ravel(), uj.ravel())[0, 1]

    X = lambda v: PX + (v - LO) / (HI - LO) * PS
    Y = lambda v: PY + PS - (v - LO) / (HI - LO) * PS
    rng = np.random.default_rng(3)
    perm = rng.permutation(N * N)                       # the shuffle: bin j's pixels permuted
    uif, ujf = ui.ravel(), uj.ravel()
    wgt = 0.5 * (np.abs(uif) + np.abs(ujf))             # the paper's l1 weight per pixel

    # the cells: sum of the weights of the points that fall in each
    edges = np.linspace(LO, HI, K + 1)
    ci = np.clip(np.digitize(uif, edges) - 1, 0, K - 1)
    cj = np.clip(np.digitize(ujf, edges) - 1, 0, K - 1)
    cell = np.zeros((K, K))
    np.add.at(cell, (ci, cj), wgt)
    alpha = 0.92 * (cell / cell.max()) ** 0.6          # a monotone ramp, faint cells still seen

    # the two marginals: each bin's own l1 curve, sum of |u| per bin, as on the l1 slide
    sedges = np.linspace(LO, HI, MARG_BINS + 1)
    scent = (sedges[:-1] + sedges[1:]) / 2
    l1i = np.bincount(np.digitize(uif, sedges) - 1, weights=np.abs(uif), minlength=MARG_BINS)
    l1j = np.bincount(np.digitize(ujf, sedges) - 1, weights=np.abs(ujf), minlength=MARG_BINS)
    l1j_scr = np.bincount(np.digitize(ujf[perm], sedges) - 1, weights=np.abs(ujf[perm]),
                          minlength=MARG_BINS)
    assert np.allclose(l1j, l1j_scr)                    # the shuffle leaves the marginal alone
    smax = max(l1i.max(), l1j.max())

    # the example: a strong shared peak (top 3 to 8 per cent), not the extreme one, so it lands well
    # inside the plane, and the one of those nearest the maps' centre, so its rings are whole
    tot = uif + ujf
    lo_, hi_ = np.quantile(tot, [0.92, 0.97])
    cand = np.where((tot >= lo_) & (tot <= hi_))[0]
    rr, cc = np.divmod(cand, N)
    ex = int(cand[np.argmin((rr - N / 2) ** 2 + (cc - N / 2) ** 2)])
    ex_r, ex_c = divmod(ex, N)

    p = [f'<svg class="jl1-svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
         'aria-label="one wavelet scale in two tomographic bins; each pixel becomes a point in '
         'the plane of its two coefficients; their joint distribution is correlated; the per-bin '
         'l1 curves are its two marginals; shuffling one bin leaves the marginals unchanged but '
         'removes the correlation; the joint l1-norm sums the l1 weight of the points in each cell '
         'of a 10 by 10 grid">']
    css = "".join(f".jl1-svg .c{i}{{fill:{l1sort.hexc(l1sort.colour(c))}}}" for i, c in enumerate(scent))
    p.append(f"<style>{css}</style>")

    # the maps
    for (mx, my), u, lab in (((MAPI_X, MAPI_Y), ui, "redshift bin i"), ((MAPJ_X, MAPJ_Y), uj, "redshift bin j")):
        p.append(f'<image x="{mx}" y="{my}" width="{N * M}" height="{N * M}" href="{map_png(u)}"/>')
        p.append(f'<rect class="j-frame" x="{mx}" y="{my}" width="{N * M}" height="{N * M}"/>')
        p.append(f'<text class="j-maplab" x="{mx + N * M / 2}" y="{my + N * M + 22}">{lab}</text>')

    # the plane: cells (under everything), frame, zero lines, grid, labels
    cw = PS / K
    for a in range(K):
        for b in range(K):
            if cell[a, b] <= 0:
                continue
            p.append(f'<rect class="j-cell" x="{f(PX + a * cw)}" y="{f(PY + PS - (b + 1) * cw)}" '
                     f'width="{f(cw)}" height="{f(cw)}" style="--a:{alpha[a, b]:.3f}"/>')
    p.append(f'<line class="j-zero" x1="{f(X(0))}" y1="{PY}" x2="{f(X(0))}" y2="{PY + PS}"/>')
    p.append(f'<line class="j-zero" x1="{PX}" y1="{f(Y(0))}" x2="{PX + PS}" y2="{f(Y(0))}"/>')
    for t in range(1, K):
        p.append(f'<line class="j-grid" x1="{f(PX + t * cw)}" y1="{PY}" x2="{f(PX + t * cw)}" y2="{PY + PS}"/>')
        p.append(f'<line class="j-grid" x1="{PX}" y1="{f(PY + t * cw)}" x2="{PX + PS}" y2="{f(PY + t * cw)}"/>')
    p.append(f'<rect class="j-frame" x="{PX}" y="{PY}" width="{PS}" height="{PS}"/>')
    p.append(f'<text class="j-tick" x="{f(X(0))}" y="{PY + PS + 20}">0</text>')
    p.append(f'<text class="j-tick" x="{PX - 12}" y="{f(Y(0) + 5)}">0</text>')
    p.append(f'<text class="j-axlab" x="{PX + PS / 2}" y="{PY + PS + 44}">value in bin i &#8594;</text>')
    p.append(f'<text class="j-axlab" transform="rotate(-90 {PX - 34} {PY + PS / 2})" '
             f'x="{PX - 34}" y="{PY + PS / 2}">value in bin j &#8594;</text>')

    # the marginals: bin i's l1 curve on the top edge, bin j's on the right edge
    bw = PS / MARG_BINS
    for s_ in range(MARG_BINS):
        hi_ = l1i[s_] / smax * SH
        if hi_ > 0.3:
            p.append(f'<rect class="j-sh j-shx c{s_}" x="{f(PX + s_ * bw + 1)}" y="{f(PY - 6 - hi_)}" '
                     f'width="{f(bw - 2)}" height="{f(hi_)}"/>')
        hj = l1j[s_] / smax * SH
        if hj > 0.3:
            p.append(f'<rect class="j-sh j-shy c{s_}" x="{PX + PS + 6}" y="{f(PY + PS - (s_ + 1) * bw + 1)}" '
                     f'width="{f(hj)}" height="{f(bw - 2)}"/>')
    p.append(f'<text class="j-shlab" x="{PX + PS + 8}" y="{PY - 12}">'
             'per-bin &#8467;<tspan class="j-sub" dy="4">1</tspan></text>')

    # the example position: ringed in both maps, guide lines to both axes
    for mx, my in ((MAPI_X, MAPI_Y), (MAPJ_X, MAPJ_Y)):
        p.append(f'<circle class="j-ring" cx="{mx + ex_c * M + M / 2}" cy="{my + ex_r * M + M / 2}" r="{M * 1.3}"/>')
    exx, exy = X(uif[ex]), Y(ujf[ex])
    p.append(f'<line class="j-guide" x1="{f(exx)}" y1="{f(exy)}" x2="{f(exx)}" y2="{PY + PS}"/>')
    p.append(f'<line class="j-guide" x1="{f(exx)}" y1="{f(exy)}" x2="{PX}" y2="{f(exy)}"/>')

    # the dots: one per position, starting on its pixel of bin i
    for idx in range(N * N):
        r, c = divmod(idx, N)
        sx, sy = MAPI_X + c * M + M / 2, MAPI_Y + r * M + M / 2
        tx, ty = X(uif[idx]), Y(ujf[idx])
        ty4 = Y(ujf[perm[idx]])
        kk = min(0.3 + wgt[idx] / 1.1, 3.2)
        d = 0.5 * r / N + 0.2 * rng.random()
        d4 = 0.35 * rng.random()
        p.append(f'<circle class="j-dot" cx="{f(sx)}" cy="{f(sy)}" r="{DOT_R}" '
                 f'style="--x:{f(tx - sx)}px;--y:{f(ty - sy)}px;--y4:{f(ty4 - sy)}px;--k:{kk:.2f};'
                 f'--d:{d:.2f}s;--d4:{d4:.2f}s"/>')
    sx, sy = MAPI_X + ex_c * M + M / 2, MAPI_Y + ex_r * M + M / 2
    p.append(f'<circle class="j-ex" cx="{f(sx)}" cy="{f(sy)}" r="{DOT_R * 2.2}" '
             f'style="--x:{f(exx - sx)}px;--y:{f(exy - sy)}px"/>')
    p.append("</svg>")
    svg = "".join(p)

    js = ("/* GENERATED by tools/make-joint-l1.py, do not edit. The joint-l1 build of the cross-bin\n"
          " * slides: drops the SVG into every [data-jl1] element, synchronously, so it is in place\n"
          " * before reveal lays out the PDF pages. The motion is in colloquium.css. */\n"
          "(function () {\n"
          f"  var svg = {json.dumps(svg)};\n"
          "  var hosts = document.querySelectorAll('[data-jl1]');\n"
          "  for (var i = 0; i < hosts.length; i++) hosts[i].innerHTML = svg;\n"
          "})();\n")
    with open(OUT, "w") as fh:
        fh.write(js)
    print(f"wrote {OUT}: {len(js) // 1024} KB; correlation {corr:.2f}; u_i {ui.min():.1f}..{ui.max():.1f}, "
          f"u_j {uj.min():.1f}..{uj.max():.1f}; {int((cell > 0).sum())} cells filled")


if __name__ == "__main__":
    main()
