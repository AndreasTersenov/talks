#!/usr/bin/env python3
"""The generative-modelling triptych: true density, the samples we actually see,
and the model fitted to them.

Drawn rather than lifted from another deck's slides. Dark palette, because this
slide is deliberately a change of register — the machine-learning break in a talk
that is otherwise on paper.

    /usr/local/bin/python3 tools/make-genmodel-figure.py

Writes assets/diagrams/generative_modelling.png.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG    = "#15161b"
FG    = "#e8e6e1"
MUTED = "#989488"

rng = np.random.default_rng(11)
gx, gy = np.meshgrid(np.linspace(-3, 3, 300), np.linspace(-3, 3, 300))


def dens(mus, covs, ws):
    out = np.zeros_like(gx)
    for mu, cov, w in zip(mus, covs, ws):
        inv = np.linalg.inv(cov)
        dx, dy = gx - mu[0], gy - mu[1]
        q = inv[0, 0] * dx**2 + 2 * inv[0, 1] * dx * dy + inv[1, 1] * dy**2
        out += w * np.exp(-0.5 * q) / np.sqrt(np.linalg.det(cov))
    return out / out.max()


# the truth: a slightly lopsided, correlated blob
MUS  = [np.array([-0.15, 0.10]), np.array([0.75, -0.45])]
COVS = [np.array([[0.75, 0.30], [0.30, 0.65]]), np.array([[0.45, -0.10], [-0.10, 0.40]])]
WS   = [1.0, 0.55]
true = dens(MUS, COVS, WS)

# what we actually have: a finite draw
n = 260
which = rng.random(n) < WS[0] / sum(WS)
pts = np.where(
    which[:, None],
    rng.multivariate_normal(MUS[0], COVS[0], n),
    rng.multivariate_normal(MUS[1], COVS[1], n),
)

# the model: fitted to the sample, so close but not identical
mu_hat = pts.mean(axis=0)
cov_hat = np.cov(pts.T) * 1.06
model = dens([mu_hat], [cov_hat], [1.0])

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.3))
fig.patch.set_facecolor(BG)

panels = [
    (true,  r"true  $\mathbb{P}$",            "img"),
    (pts,   r"samples  $x_i \sim \mathbb{P}$", "pts"),
    (model, r"model  $\mathbb{P}_\theta$",     "img"),
]
for ax, (data, title, kind) in zip(axes, panels):
    ax.set_facecolor(BG)
    if kind == "img":
        ax.imshow(data, extent=(-3, 3, -3, 3), origin="lower",
                  cmap="viridis", interpolation="bilinear")
    else:
        ax.scatter(pts[:, 0], pts[:, 1], s=13, color="#7d92ff", alpha=0.85,
                   linewidths=0)
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_aspect("equal")
    ax.set_title(title, color=FG, fontsize=15, pad=12)
    for sp in ax.spines.values():
        sp.set_color("#ffffff22")

fig.subplots_adjust(left=0.02, right=0.98, top=0.86, bottom=0.04, wspace=0.16)
fig.savefig("assets/diagrams/generative_modelling.png", dpi=200, facecolor=BG)
print("wrote assets/diagrams/generative_modelling.png")
