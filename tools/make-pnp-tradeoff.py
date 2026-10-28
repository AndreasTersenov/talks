#!/usr/bin/env python3
"""The PnPMass result redrawn as a build: accuracy, then calibration, then the smallest bars.

For the UVA / NRAO colloquium (2026-10-28): the PnPMass result slide (C19) carried the paper's
summary figure at journal size, with a miscoverage colour bar. This redraws it at slide size with
both axes relative to DeepMass (the network retrained for this exact mask and noise), so lower left
is better and DeepMass sits at the origin, and builds it in four clicks:

    1  accuracy: each method on the map-error axis (the error-bar axis is not shown yet, so the
       line of methods reads as a number line, not as a value of the error bars)
    2  the networks' own error bars (order-2 moment networks), before calibration: open circles.
       Wiener and MCALens have none (the paper initialises theirs to zero)
    3  calibration (conformalised quantile regression): every method moves to its calibrated size,
       at the target coverage; the trails show the move. DeepMass's bars shrink, PnPMass's grow
       slightly (the paper, Sect. "Effect of the calibration on the confidence intervals")
    4  PnPMass: the smallest calibrated bars

Numbers: x is the RMSE ratio to DeepMass, from PAPER_FACTS section 3 (Table rmse of the paper).
The error-bar sizes are read off the paper's vector figure (img/summary.pdf in the arXiv source of
2603.22006) on 2026-10-28, calibrated on its own tick marks; the same read gives the RMSE values of
the ledger to the third digit, which is the check. Sizes are the paper's normalised mean interval
length, divided here by DeepMass's calibrated one.

Writes UVA_NRAO_colloquium/pnp_tradeoff.js, which drops the SVG into every [data-pnptr] element
when the page loads; the motion is CSS keyed to the slide's marker fragments (.tm1..4).

    python3 tools/make-pnp-tradeoff.py
"""
import json

OUT = "UVA_NRAO_colloquium/pnp_tradeoff.js"

# name, RMSE ratio to DeepMass (ledger), normalised interval length before and after calibration
# (paper figure; None: no error bars before calibration), class
METHODS = [
    ("Wiener",             1.039, None,   3.2514, "cl"),
    ("MCALens",            1.025, None,   3.2398, "cl"),
    ("DeepMass",           1.000, 3.1999, 3.1357, "nn"),
    ("PnPMass (residual)", 1.006, 3.0252, 3.1002, "nn pnp"),
    ("PnPMass",            1.013, 2.9743, 3.0041, "nn pnp pnp0"),
]
REF = 3.1357                                   # DeepMass, calibrated

W, H = 760, 440
PX0, PX1, PY0, PY1 = 104, 735, 18, 372         # the plot
XLO, XHI = 0.994, 1.046
YLO, YHI = 0.932, 1.052
STRIP = PY1 - 76                               # click 1: the methods on a line, by accuracy,
                                               # high enough that a label below clears "better"
# label placement on the strip (dx, dy, anchor) and in the plane (dx, dy, anchor)
STRIP_LAB = {"Wiener": (0, -14, "middle"), "MCALens": (0, -14, "middle"), "DeepMass": (0, -14, "middle"),
             "PnPMass (residual)": (0, 26, "middle"), "PnPMass": (0, -14, "middle")}
PLANE_LAB = {"Wiener": (-12, -12, "end"), "MCALens": (-12, -12, "end"), "DeepMass": (12, -10, "start"),
             "PnPMass (residual)": (12, -8, "start"), "PnPMass": (12, 6, "start")}


def X(v):
    return PX0 + (v - XLO) / (XHI - XLO) * (PX1 - PX0)


def Y(v):
    return PY1 - (v - YLO) / (YHI - YLO) * (PY1 - PY0)


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def pct(v):
    return "0" if abs(v) < 1e-9 else f"{v * 100:+.0f} %".replace("-", "&#8722;")


def main():
    p = [f'<svg class="tr-svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
         'aria-label="map error against calibrated error-bar size, both relative to DeepMass; '
         'after calibration every method reaches the target coverage, and PnPMass has the '
         'smallest error bars, within about one per cent of DeepMass in map error">']
    # grid, reference lines through DeepMass, frame, ticks
    for t in (0.0, 0.01, 0.02, 0.03, 0.04):
        x = X(1 + t)
        p.append(f'<line class="tr-grid" x1="{f(x)}" y1="{PY0}" x2="{f(x)}" y2="{PY1}"/>')
        p.append(f'<text class="tr-tick" x="{f(x)}" y="{PY1 + 22}">{pct(t)}</text>')
    for t in (-0.06, -0.04, -0.02, 0.0, 0.02, 0.04):
        y = Y(1 + t)
        p.append(f'<line class="tr-grid tr-yax" x1="{PX0}" y1="{f(y)}" x2="{PX1}" y2="{f(y)}"/>')
        p.append(f'<text class="tr-tick tr-ytick tr-yax" x="{PX0 - 10}" y="{f(y + 5)}">{pct(t)}</text>')
    p.append(f'<line class="tr-ref" x1="{f(X(1))}" y1="{PY0}" x2="{f(X(1))}" y2="{PY1}"/>')
    p.append(f'<line class="tr-ref tr-refy tr-yax" x1="{PX0}" y1="{f(Y(1))}" x2="{PX1}" y2="{f(Y(1))}"/>')
    p.append(f'<line class="tr-axis" x1="{PX0}" y1="{PY1}" x2="{PX1}" y2="{PY1}"/>')
    p.append(f'<line class="tr-axis" x1="{PX0}" y1="{PY0}" x2="{PX0}" y2="{PY1}"/>')
    p.append(f'<text class="tr-axlab" x="{(PX0 + PX1) / 2}" y="{PY1 + 50}">map error, relative to DeepMass</text>')
    p.append(f'<text class="tr-axlab tr-ylab tr-yax" transform="rotate(-90 {PX0 - 66} {(PY0 + PY1) / 2})" '
             f'x="{PX0 - 66}" y="{(PY0 + PY1) / 2}">error-bar size, relative to DeepMass</text>')
    p.append(f'<text class="tr-better tr-yax" x="{PX0 + 14}" y="{PY1 - 12}">&#8601; better</text>')

    # the calibration trails, under the points
    for name, x, before, after, cls in METHODS:
        if before is None:
            continue
        p.append(f'<line class="tr-trail {cls}" x1="{f(X(x))}" y1="{f(Y(before / REF))}" '
                 f'x2="{f(X(x))}" y2="{f(Y(after / REF))}"/>')

    # the points: one group per method, moved by CSS between the states
    for name, x, before, after, cls in METHODS:
        gx, y1 = X(x), STRIP
        y2 = Y(before / REF) if before is not None else STRIP
        y3 = Y(after / REF)
        sdx, sdy, sa = STRIP_LAB[name]
        pdx, pdy, pa = PLANE_LAB[name]
        p.append(f'<g class="tr-pt {cls}" style="--x:{f(gx)}px;--y1:{f(y1)}px;--y2:{f(y2)}px;--y3:{f(y3)}px">'
                 f'<circle class="tr-dot" r="7"/>'
                 f'<text class="tr-lab tr-lab1" x="{sdx}" y="{sdy}" text-anchor="{sa}">{name}</text>'
                 f'<text class="tr-lab tr-lab2" x="{pdx}" y="{pdy}" text-anchor="{pa}">{name}</text></g>')
    p.append("</svg>")
    svg = "".join(p)

    js = ("/* GENERATED by tools/make-pnp-tradeoff.py, do not edit. The PnPMass result as a build:\n"
          " * drops the SVG into every [data-pnptr] element, synchronously, so it is in place before\n"
          " * reveal lays out the PDF pages. The motion is in colloquium.css. */\n"
          "(function () {\n"
          f"  var svg = {json.dumps(svg)};\n"
          "  var hosts = document.querySelectorAll('[data-pnptr]');\n"
          "  for (var i = 0; i < hosts.length; i++) hosts[i].innerHTML = svg;\n"
          "})();\n")
    with open(OUT, "w") as fh:
        fh.write(js)
    for name, x, before, after, cls in METHODS:
        b = f"{before / REF:.3f}" if before else "  -  "
        print(f"{name:20s} map error {x:.3f}   bars before {b}   after {after / REF:.3f}")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
