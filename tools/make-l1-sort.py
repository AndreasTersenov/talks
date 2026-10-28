#!/usr/bin/env python3
"""The starlet l1-norm without its formula: "sort every pixel, then weigh it by its strength".

For the UVA / NRAO colloquium (2026-10-27): Andreas feared the l1-norm card of the wavelet-
statistics slide (C24, a formula) would lose the room. The plan already said "no l1 formula".
This builds the replacement for that slide's bottom row, in the spirit of Wassim Kabalan's
defence animations (a figure made for one slide, frames that line up, a PDF still per click),
but drawn by CSS, not pre-rendered, so it needs no video and exports to PDF click by click.

One band of a starlet transform, pixel by pixel, then four clicks after it appears; the
slide types the l1-norm's formula a part at a time alongside (Andreas, 2026-10-27):

    0  the band: each pixel a coefficient (red above its local mean, blue below, grey ~ 0)
    1  peak counts: the local maxima are ringed and drop into a histogram, by height
    2  sort: every pixel flies to its value and stacks: the histogram of the band
                                                         ("pixels in the bin")
    3  weigh: each block, where it stands, grows or shrinks to |value|        ("|value|")
    4  add up: each bin's blocks restack as one bar, each pixel a slice as thick as its |value|.
       The middle collapses, a hump each side remains (voids left, peaks right); each bar's
       height is that bin's sum of |w|, the l1-norm of the band, drawn literally ("l1 = sum")

The field is an ILLUSTRATION, not a simulation from the papers: a lognormal field (a Gaussian
random field with P(k) ~ k^-2.4, exponentiated, then pixelised), so it has the peaks and the
shallow, wide voids of the real convergence. The transform is a real starlet (a trous, B3-spline,
periodic), and the band is w2. Values are in units of the band's standard deviation, the way
the papers bin in signal-to-noise; the bins are 0.25 wide.

Writes UVA_NRAO_colloquium/l1_sort.js, which drops the SVG into every [data-l1sort] element
when the page loads, before reveal lays out the PDF pages. Every block carries its position in
each state as CSS custom properties; colloquium.css moves them, keyed to the slide's marker
fragments (.l1-mk1..3), so the build needs no JS of its own and the PDF shows each click's
end state.

    venv/bin/python tools/make-l1-sort.py

Needs numpy, scipy and Pillow.
"""
import base64
import io
import json

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

OUT = "UVA_NRAO_colloquium/l1_sort.js"

N, SEED, BAND = 32, 31, 1            # 32 x 32 pixels; band index 1 = w2
SLOPE, SIG, UP = -2.4, 0.6, 4        # chosen for a broad band histogram with clear blobs
BIN = 0.25                           # bin width, in units of the band's std
LO, HI = -2.25, 5.5                  # the bin range; this seed's band spans -2.1 to 5.3

# the stage, in SVG units (1 unit = 1 px on the 1200 x 720 canvas)
W, H = 1100, 286
M = 8                                # a map pixel
MAP_X, MAP_Y = 14, 14                # the map is N*M = 256 square
HX0, HX1 = 340, 1086                 # the histogram's horizontal extent
BASE, TOP = 238, 22                  # its baseline and the highest a stack may reach
GAP = 3                              # between bins
PEAK_BLOCK = 13                      # peaks are few: their blocks are drawn larger

INK, MUTED, ACCENT = "#1c1c22", "#6a6760", "#2f49c0"
# diverging, two hues and a grey middle (a white middle would vanish on the white slide)
STOPS = [(-3.0, (44, 90, 160)), (-1.2, (128, 165, 214)), (0.0, (205, 201, 194)),
         (1.5, (232, 150, 128)), (4.0, (184, 41, 47))]


def lognormal_field(n, seed):
    rng = np.random.default_rng(seed)
    big = n * UP
    kx = np.fft.fftfreq(big)[:, None]
    ky = np.fft.fftfreq(big)[None, :]
    k = np.hypot(kx, ky)
    k[0, 0] = 1
    amp = k ** (SLOPE / 2)
    amp[0, 0] = 0
    g = np.real(np.fft.ifft2(np.fft.fft2(rng.standard_normal((big, big))) * amp))
    g = g / g.std() * SIG
    kappa = np.exp(g - SIG ** 2 / 2) - 1
    return kappa.reshape(n, UP, n, UP).mean(axis=(1, 3))


def starlet(img, nscales):
    """Isotropic undecimated (a trous) starlet transform, B3-spline, periodic."""
    h = np.array([1, 4, 6, 4, 1]) / 16.0
    c = img.copy()
    bands = []
    for j in range(nscales):
        kern = np.zeros(4 * 2 ** j + 1)
        kern[::2 ** j] = h
        smooth = ndi.convolve1d(ndi.convolve1d(c, kern, axis=0, mode="wrap"), kern, axis=1, mode="wrap")
        bands.append(c - smooth)
        c = smooth
    return bands, c


def colour(u):
    us = [s[0] for s in STOPS]
    u = min(max(u, us[0]), us[-1])
    for (u0, c0), (u1, c1) in zip(STOPS[:-1], STOPS[1:]):
        if u <= u1:
            t = (u - u0) / (u1 - u0)
            return tuple(round(a + (b - a) * t) for a, b in zip(c0, c1))
    return STOPS[-1][1]


def hexc(c):
    return "#%02x%02x%02x" % c


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def main():
    w = starlet(lognormal_field(N, SEED), 3)[0][BAND]
    u = w / w.std()
    assert LO <= u.min() and u.max() < HI, (u.min(), u.max())   # no pixel clipped into an end bin
    edges = np.arange(LO, HI + 1e-9, BIN)
    nb = len(edges) - 1
    b_of = np.digitize(u, edges) - 1
    centres = (edges[:-1] + edges[1:]) / 2
    is_peak = (u == ndi.maximum_filter(u, size=3, mode="wrap"))

    pitch = (HX1 - HX0) / nb
    counts = np.bincount(b_of.ravel(), minlength=nb)
    # sub-columns per bin: the fewest that keep the tallest stack under the ceiling
    for k in range(3, 20):
        blk = (pitch - GAP) / k
        if np.ceil(counts.max() / k) * blk <= BASE - TOP:
            break
    blk = (pitch - GAP) / k
    s2 = blk / M

    rng = np.random.default_rng(7)
    order = np.argsort(-np.abs(u.ravel()), kind="stable")    # strongest at the bottom of a stack
    col_of, row_of = {}, {}
    fill = np.zeros((nb, k), int)
    for idx in order:
        bi = b_of.ravel()[idx]
        c = int(np.argmin(fill[bi]))                         # the shortest sub-column
        col_of[idx], row_of[idx] = c, fill[bi, c]
        fill[bi, c] += 1

    absu = np.abs(u.ravel())

    # click 3: weigh. Each block stays in its sub-column and takes a height proportional to |u|
    hsub = np.zeros((nb, k))
    for idx in order:
        hsub[b_of.ravel()[idx], col_of[idx]] += absu[idx]
    alpha_w = (BASE - TOP - 6) / hsub.max()
    y3_of, cum3 = {}, np.zeros((nb, k))
    for idx in order:
        bi, c = b_of.ravel()[idx], col_of[idx]
        hgt = absu[idx] * alpha_w
        cum3[bi, c] += hgt
        y3_of[idx] = (BASE - cum3[bi, c], hgt)

    # click 4: add up. Each bin restacks as ONE bar, each pixel a slice as thick as |u|, so a
    # bar's height is the bin's sum of |u| -- the l1-norm -- scaled so the tallest bar fits
    l1 = np.bincount(b_of.ravel(), weights=absu, minlength=nb)
    alpha = (BASE - TOP - 28) / l1.max()                     # px per unit of |u|
    y4_of, cum = {}, np.zeros(nb)
    for idx in order:
        bi = b_of.ravel()[idx]
        hgt = absu[idx] * alpha
        cum[bi] += hgt
        y4_of[idx] = (BASE - cum[bi], hgt)

    # click 1: the peaks alone, one column per bin, larger blocks
    peak_rows = np.zeros(nb, int)
    pk_pos = {}
    for idx in np.argsort(u.ravel()):
        if not is_peak.ravel()[idx]:
            continue
        bi = b_of.ravel()[idx]
        x = HX0 + bi * pitch + (pitch - GAP - PEAK_BLOCK) / 2
        y = BASE - (peak_rows[bi] + 1) * PEAK_BLOCK
        peak_rows[bi] += 1
        pk_pos[idx] = (x, y)

    # ---------------------------------------------------------------- the SVG
    css = "".join(f".l1s-svg .c{i}{{fill:{hexc(colour(c))}}}" for i, c in enumerate(centres))
    parts = [f'<svg class="l1s-svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
             f'style="--s1:{PEAK_BLOCK / M:.4f};--s2:{s2:.4f};--s4:{(pitch - GAP) / M:.4f}" '
             'aria-label="one wavelet band, pixel by pixel; the peaks, then every pixel, sorted '
             'into a histogram by value; then each pixel weighed by its absolute value, leaving '
             'two humps, voids and peaks: the l1-norm">',
             f"<style>{css}</style>"]

    # the band itself stays put: an image of the same pixels, in the same colours
    img = np.zeros((N, N, 3), np.uint8)
    for (r, c), v in np.ndenumerate(b_of):
        img[r, c] = colour(centres[v])
    buf = io.BytesIO()
    Image.fromarray(img).resize((N * M, N * M), Image.NEAREST).save(buf, "PNG", optimize=True)
    uri = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
    parts.append(f'<image class="l1s-map" x="{MAP_X}" y="{MAP_Y}" width="{N * M}" height="{N * M}" '
                 f'href="{uri}"/>')
    parts.append(f'<rect class="l1s-frame" x="{MAP_X}" y="{MAP_Y}" width="{N * M}" height="{N * M}"/>')

    # the axis
    x0 = HX0 + (0 - LO) / BIN * pitch - GAP / 2
    parts.append(f'<line class="l1s-axis" x1="{HX0 - 4}" y1="{BASE + 0.5}" x2="{HX1}" y2="{BASE + 0.5}"/>')
    parts.append(f'<line class="l1s-axis" x1="{f(x0)}" y1="{BASE}" x2="{f(x0)}" y2="{BASE + 7}"/>')
    parts.append(f'<text class="l1s-tick" x="{f(x0)}" y="{BASE + 24}">0</text>')
    parts.append(f'<text class="l1s-end" x="{HX0}" y="{BASE + 24}">&#8722;</text>')
    parts.append(f'<text class="l1s-end" x="{HX1 - 8}" y="{BASE + 24}">+</text>')
    parts.append(f'<text class="l1s-axlab" x="{f((HX0 + HX1) / 2 + 60)}" y="{BASE + 44}">'
                 'value of the pixel (the wavelet coefficient)</text>')

    # the blocks: one per pixel, with its place in each state
    for idx in range(N * N):
        r, c = divmod(idx, N)
        x, y = MAP_X + c * M, MAP_Y + r * M
        bi = b_of.ravel()[idx]
        hx = HX0 + bi * pitch + col_of[idx] * blk
        bx = HX0 + bi * pitch
        y2 = BASE - (row_of[idx] + 1) * blk
        y3, h3 = y3_of[idx]
        y4, h4 = y4_of[idx]
        d = 0.55 * r / N + 0.18 * rng.random()          # pours from the top of the map down
        style = (f"--dx2:{f(hx - x)}px;--dy2:{f(y2 - y)}px;"
                 f"--dy3:{f(y3 - y)}px;--t3:{h3 / M:.3f};"
                 f"--dx4:{f(bx - x)}px;--dy4:{f(y4 - y)}px;--t4:{h4 / M:.3f};--d:{d:.2f}s")
        cls = f"px c{bi}"
        if idx in pk_pos:
            px_, py_ = pk_pos[idx]
            style += f";--dx1:{f(px_ - x)}px;--dy1:{f(py_ - y)}px"
            cls += " pk"
        parts.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{M}" height="{M}" style="{style}"/>')

    # rings round the peaks, on the map
    for idx in pk_pos:
        r, c = divmod(idx, N)
        parts.append(f'<circle class="l1s-ring" cx="{MAP_X + c * M + M / 2}" cy="{MAP_Y + r * M + M / 2}" r="{M * 0.95}"/>')

    # click 4: the curve through the bar tops, and the two humps named
    tops = [(HX0 + i * pitch + (pitch - GAP) / 2, BASE - l1[i] * alpha) for i in range(nb)]
    path = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in tops)
    parts.append(f'<path class="l1s-curve" d="{path}"/>')
    neg = [i for i in range(nb) if centres[i] < 0]
    pos = [i for i in range(nb) if centres[i] > 0.6]
    i_v = max(neg, key=lambda i: l1[i])
    i_p = max(pos, key=lambda i: l1[i])
    parts.append(f'<text class="l1s-hump" x="{f(tops[i_v][0])}" y="{f(tops[i_v][1] - 12)}">voids</text>')
    parts.append(f'<text class="l1s-hump" x="{f(tops[i_p][0])}" y="{f(tops[i_p][1] - 12)}">peaks</text>')
    parts.append("</svg>")
    svg = "".join(parts)

    js = ("/* GENERATED by tools/make-l1-sort.py, do not edit. The l1-norm build of the wavelet-\n"
          " * statistics slide: drops the SVG into every [data-l1sort] element, synchronously, so it is\n"
          " * in place before reveal lays out the PDF pages. The motion is in colloquium.css. */\n"
          "(function () {\n"
          f"  var svg = {json.dumps(svg)};\n"
          "  var hosts = document.querySelectorAll('[data-l1sort]');\n"
          "  for (var i = 0; i < hosts.length; i++) hosts[i].innerHTML = svg;\n"
          "})();\n")
    with open(OUT, "w") as fh:
        fh.write(js)
    print(f"wrote {OUT}: {len(js) // 1024} KB; {nb} bins x {k} sub-columns, block {blk:.1f} px, "
          f"{int(is_peak.sum())} peaks, tallest bin {counts.max()}")


if __name__ == "__main__":
    main()
