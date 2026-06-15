# BNT explainer — "shadows of a rotating cloud"

A self-contained **reveal.js** slide that makes ONE effect intuitive for the
*Non-Gaussian Universe* talk:

> Why does the BNT transform collapse the wavelet ℓ1-norm's figure of merit
> (even with cross-maps) while leaving the CNN essentially lossless?

It depicts the **proven** mechanism (not a new one) from the `cnn_sbi` repo:
`scripts/sbi/results/exploratory/flatsky_cross_2026_06/BNT_THEORY_DEEP_DIVE.md` §1,
`FLATSKY_BNT_RESULT.md`, and `HANDOFF_BNT_VIZ_TALK.md`.

## Status in this repo (parked, self-contained)

This dir is **parked self-contained**: it keeps its own vendored reveal.js
(`vendor/reveal/`) and its own styling rather than using the repo's reveal.js
submodule + Preprint theme. It works immediately/offline, but it does **not yet**
follow the repo conventions (shared `../assets/`, `assets/themes/talks.css`).

**Integrate-later pass** (when wiring it into the actual Non-Gaussian deck): drop
`vendor/reveal/`, point the deck at a `reveal.js/` submodule, link
`../assets/themes/talks.css` + `theme-switch.js`, author the explainer `<section>`
as a `data-theme="light"` slide, and retune the chrome in `bnt_explainer.css` to
theme tokens (`var(--surface)`, `var(--fg)`, `var(--fg-muted)`, `var(--edge)`) —
**keeping the locked Wong method colors** (CNN `#0072B2`, L1 `#D55E00`). The
animation logic in `bnt_explainer.js` is reveal-agnostic (it only calls
`window.Reveal` via `BNTExplainer.attach`), so no JS change is needed.

## Preview it

Open `index.html` in any browser (no server needed — it's all relative, offline-safe):

```
xdg-open index.html      # or just double-click it
```

Step with **→ / Space / click** (advance an act), **← / Shift-Tab** (step back),
**R** or the *↻ replay* button (auto-replay the whole sequence on the current slide).

## The five acts (advance on click)

| Act | What happens | FoM₃ meter |
|-----|--------------|-----------|
| 1 | Maps → a fixed **cloud** of pixels; the ℓ1 is its **shadow** on each axis. The cloud is elongated along a **deep common mode** → both shadows rich. | ℓ1 **1.00×** (3045) |
| 2 | **BNT re-orients the measuring axes** off the deep mode onto thin, signal-poor slices (+ amplified noise) → shadows go blank. *The cloud never moves.* | ℓ1 **0.26×** (779) |
| 3 | Where did it go? Into the cloud's **shape** — the relations *between* maps. No single-map histogram sees it in this frame. | ℓ1 0.26× |
| 4 | The **CNN mixes channels first** → draws its own axis back along the cloud (undo B for free) → rich again. **Basis-robust, not "smarter."** | CNN **0.96×** (3186) |
| 5 | **Whitening** rotates to a *different clean frame* → shadows back → recovers **1.06×**. Nothing was lost; the collapse was the **frame**. | ℓ1 **1.06×** |

The lensing-kernel inset morphs (Act 2) from 4 broad overlapping kernels n(z)
into 1 broad map + 3 thin slices — *why* the cloud is elongated and the nulled
axes are signal-poor.

## Drop it into your real deck

The slide is a single `<section>` (in `slide_section.html`, identical to the one
in `index.html` between the `BEGIN/END DROP-IN SECTION` comments). To merge:

1. Copy the `<section class="bnt-slide" data-bnt-explainer> … </section>` into
   your deck's `.slides` container.
2. In `<head>`: `<link rel="stylesheet" href="bnt_explainer.css">`
3. Before `</body>`: `<script src="bnt_explainer.js"></script>`
4. **After** your `Reveal.initialize({...})` call:
   ```js
   BNTExplainer.attach(Reveal);
   ```

That's it. The CSS is scoped under `.bnt-slide`, so it won't fight your deck's
theme. The animation reads reveal's fragment state, so it works with your deck's
own navigation, autoslide, speaker notes, PDF export, etc.

### Notes
- **Offline-safe.** reveal.js 5.1.0 is vendored under `vendor/reveal/` (the
  theme's web-font `@import` was stripped). Nothing loads from a CDN at runtime.
- **No build step, no dependencies.** Pure `<canvas>` + a little DOM.
- The toy cloud is **hand-tuned** (stylised 2-D), generated from a fixed seed so
  it's identical every reload. It is *not* fit to data — it is tuned to match the
  *proven behaviour* (collapse on BNT axes, recovery on a whitened frame). The
  on-screen numbers ARE the real measured ones (matched best-NDE; see below).
- **Palette is locked** to the deck convention (Wong, colourblind-safe):
  CNN = blue `#0072B2`, L1 = vermillion `#D55E00`; colour encodes *method* only.

## The numbers (HANDOFF §4 — real, measured)

- ℓ1+product (matched best-NDE): FoM₃ **3045 → 779 = 0.26×** (σ(σ8) +65%); calibrated.
- CNN ResNet18: FoM₃ **3326 → 3186 = 0.96×** (lossless within seed scatter).
- Whitening recovery (L1-auto): **1.06×** (full recovery).

The meter is **ratio-led** (FoM₃ is fragile; ratios are the arm-comparable
headline); absolute pairs are shown for the matched ℓ1+product / CNN arms.

## Correctness guardrails (HANDOFF §2 — what the visual must NOT imply)

This build was checked against all four traps:

1. **Info is never destroyed.** The cloud is *identical, fixed pixels* in every
   act; only the measuring axes move. A standing caption says so.
2. **Not "irreducibly joint."** Act 5 recovers fully in a *different* clean frame
   → the visual says "any sane frame feeds the ℓ1," not "you need joint stats."
3. **The CNN is basis-robust, not stronger.** Act 4 says exactly that.
4. **Not "noise washes out peaks."** The lead cause shown is the axes pointing
   *across* the cloud (geometry); amplified noise is a secondary broadening.

One honest stylisation: BNT is an invertible **shear**, not a literal rotation
(the genuine rotation is the whitening Q). The animation shows the two BNT axes
becoming **non-orthogonal** (a shear) as they swing off the deep mode — faithful
to that — while keeping the load-bearing invariant: *cloud fixed, axes move,
shadows collapse.*

## Files

```
index.html            standalone preview (contains the drop-in <section>)
slide_section.html    just the <section>, for pasting into your deck
bnt_explainer.css     scoped styling (Wong palette, big fonts)
bnt_explainer.js      the canvas engine + reveal wiring (BNTExplainer.attach)
vendor/reveal/        vendored reveal.js 5.1.0 (offline)
```
