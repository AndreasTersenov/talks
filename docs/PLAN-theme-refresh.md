# Plan — Theme refresh: a tasteful light+dark slide theme

Status: **proposed, awaiting sign-off.** Nothing in the existing decks changes
until you approve. All work lands first in a throwaway test deck.

## Goal

Take the EiffL `darkenergy`/`brightenergy` theme and make it (a) prettier and
more distinctive for scientific talks, and (b) a genuine **light + dark pair**,
both good-looking, **switchable mid-presentation** (per slide, plus a live
keyboard toggle). Prove it on a copy of `LAM_2026/` with extra test slides.

## The load-bearing architectural decision

The current theme CSS lives **inside the `reveal.js` git submodule**
(`reveal.js/dist/theme/darkenergy.css`, built from
`css/theme/source/darkenergy.scss`). Two reasons that's the wrong layer to edit:

1. Submodules are tracked by **commit SHA, not file contents**. Editing the
   submodule's SCSS doesn't get recorded in *this* repo.
2. GitHub Pages re-checks-out the submodule at the pinned `EiffL/reveal.js` SHA
   (`864e0550`) when it builds. Local theme edits are discarded on publish —
   you'd have to push to François's fork, which you don't own.

**Therefore:** the new theme is a self-contained stylesheet **you own, in this
repo**, served by Pages, loaded *in place of* the submodule theme link. The
submodule keeps doing what it's good at — the reveal.js engine (`reveal.css`,
transitions, plugins, particles). We only take over the *look*.

```
talks/
  assets/
    themes/
      talks.css          ← the whole theme: both modes, all components, via CSS vars
      theme-switch.js     ← ~30 lines: per-slide + keyboard light/dark switching
```

Per-deck wiring changes exactly one line:

```html
<!-- was -->
<link rel="stylesheet" href="reveal.js/dist/theme/darkenergy.css">
<!-- becomes -->
<link rel="stylesheet" href="../assets/themes/talks.css">
<script defer src="../assets/themes/theme-switch.js"></script>
```

`reset.css` and `reveal.css` still come from the submodule (the engine).
`../assets/themes/...` resolves both locally (served from root) and on Pages
(`/talks/assets/themes/...`), consistent with the repo's asset convention, and
`check-asset-links.py` will track both files for free.

## Typography — the one real taste call (needs your pick)

Current theme uses **Fira Sans for both headings and body** → no typographic
contrast, a bit anonymous. I want character + legibility at projector distance +
cohesion with the landing page (Newsreader serif / IBM Plex Mono / amber).

Three directions; I recommend **A**:

- **A — Editorial science (recommended).** Display serif headings + clean sans
  body + mono for code/data.
  - Display: **Fraunces** (variable, optical-size, a little “wonk” — warm,
    distinctive, not an AI default), used tight and with restraint.
  - Body: **Inter** (neutral, reads at distance).
  - Mono: **IBM Plex Mono** (carries the landing-page identity into the deck).
  - *Why:* the serif/sans contrast is exactly what the flat current theme
    lacks; mono + amber tie the deck to the site front door.

- **A′ — Cohesion-first.** Same as A but headings in **Newsreader** (the exact
  landing-page serif) for maximal site-wide unity. Slightly less display punch
  than Fraunces. One-variable swap, so trivial to change later.

- **B — Modern grotesque (safe).** Strong sans display (**Space Grotesk** /
  **Hanken Grotesk**) + Inter body + IBM Plex Mono. Cleaner/techier, but closer
  to a generic “AI default” dark deck; least distinctive.

Type scale (root ~38px; reveal's default h1 of 3.77em is too big for science
slides that carry figures):

| role        | size      | treatment                                  |
|-------------|-----------|--------------------------------------------|
| h1 (title)  | 2.5em     | display, tracking −0.02em, line-height 1.05|
| h2 (slide)  | 1.6em     | display                                     |
| h3 (sub)    | 1.2em     | italic, muted — subtitle/venue              |
| h4 (eyebrow)| 0.7em     | mono, uppercase, letter-spacing 0.18em      |
| body        | 1em       | sans                                        |
| figcaption  | 0.68em    | mono, muted                                 |

## Color — both modes from one token set

Refined off the current `#111 / #eee` (research: avoid pure black bg and pure
white text — halation/eye-fatigue; keep amber but fix its contrast on white).

Dark mode:

| token        | value      | use                                  |
|--------------|------------|--------------------------------------|
| `--bg`       | `#0e1117`  | slide background (soft blue-black)   |
| `--surface`  | `#161b22`  | callouts, code blocks                |
| `--fg`       | `#e8eaed`  | body text (off-white, not #fff)      |
| `--fg-muted` | `#9aa4b2`  | captions, secondary                  |
| `--accent`   | `#e7a24c`  | amber — emphasis, rules, markers     |
| `--link`     | `#e7a24c`  | amber reads fine as link on dark     |
| `--rule`     | `rgba(255,255,255,.12)` | hairlines               |

Light mode:

| token        | value      | use                                  |
|--------------|------------|--------------------------------------|
| `--bg`       | `#faf8f4`  | warm off-white (not stark #fff)      |
| `--surface`  | `#f0ece4`  | callouts, code blocks                |
| `--fg`       | `#1a1d21`  | ink (not pure #000)                  |
| `--fg-muted` | `#5b6470`  | captions, secondary                  |
| `--accent`   | `#e7a24c`  | amber — **fills/rules/markers only** |
| `--link`     | `#9a5b16`  | burnt amber — legible link/emphasis  |
| `--rule`     | `rgba(0,0,0,.12)`       | hairlines               |

Contrast check (WCAG; body needs ≥4.5:1, large text ≥3:1):

- dark `--fg` on `--bg`: ~15:1 ✓ · amber on dark: ~8:1 ✓ (links + body ok)
- light `--fg` on `--bg`: ~15:1 ✓ · burnt-amber `--link` on light: ~7:1 ✓
- **amber on white ≈ 1.9:1 ✗** → that's exactly why light mode splits
  `--accent` (decoration) from `--link` (burnt amber). The amber *identity*
  survives in both modes; only the text hue darkens where it must.

Progress bar, controls, slide number, selection, `.alert` all read from these
tokens, so both modes stay coherent automatically.

## Components (the “tastier” layer)

Built once, themed by tokens, demoed in the test deck:

1. **Title slide lockup** — replaces the current inline-styled black box: a
   contained card over the particles bg, thin amber rule, mono eyebrow
   (date / venue), serif title, author + affiliation row.
2. **Callouts** — `.callout`, `.takeaway` (left accent border + surface bg) for
   key results.
3. **Blockquote** — accent left-rule, restrained italic, muted attribution.
4. **Figure + `figcaption`** — centered, mono muted caption; `.plain` (existing)
   still = borderless image.
5. **Tables** — bold header, 2px accent underline on header row, roomy padding.
6. **Code** — IBM Plex Mono, surface bg, subtle border; inline `code` chip.
   (monokai highlight theme stays for token colors.)
7. **Lists** — refined markers (amber `▸` / en-dash), tighter rhythm.
8. **Big-stat** — `.stat` (big number + small mono label) for headline numbers.
9. **`.alert` / `.hl`** — accent inline text / accent marker-underline.
10. **Columns** — keep `.container/.col`; add `.cols-3` and an asymmetric
    `.cols-2-1`, with a real gap and vertical-center variant.
11. **Optional running footer** (body-class toggle) — short title left, slide
    number right, muted mono; themed progress bar in amber.

ASCII sketch of the refreshed title slide:

```
┌──────────────────────────────────────────────┐
│   APR 16 2026 · LAM COFFEE CLUB   (mono eyebrow)│
│   ───────────────────────────                  │  ← amber hairline
│   Reconstructing the                            │
│   Non-Gaussian Universe          (Fraunces, big)│
│   Mass mapping, higher-order stats & SBI        │
│                                                 │
│   Andreas Tersenov   ·  FORTH / CEA   [logos]   │
└──────────────────────────────────────────────┘
        (particles.js cosmic background behind)
```

## Light/dark switching mechanism

- **Deck default:** `<body class="theme-dark">` (or `theme-light`).
- **Per slide:** `<section data-theme="light">` / `data-theme="dark"` overrides
  the default for that slide — pairs naturally with your `_dark.pdf`/`_light.pdf`
  figure variants (show the matching figure on the matching background).
- **`theme-switch.js`** (~30 lines): on `ready` + `slidechanged`, read the
  current slide's `data-theme` (fallback = deck default), set
  `body.theme-light/dark`, and sync reveal's slide-background color so the
  painted background matches the text mode. Binds **`T`** to flip the whole
  deck live mid-talk (when the room lighting surprises you).
- All colors come from CSS vars scoped under `body.theme-dark` /
  `.theme-light`, with a short transition so switches animate cleanly.

## The test deck

`THEME_TEST_2026/` — copy of `LAM_2026/`, submodule re-pointed to the same
`EiffL/reveal.js` SHA, theme link swapped to `../assets/themes/talks.css` +
the switch script. Then a block of **test slides** exercising every component:
title, section divider, **a light slide and a dark slide back-to-back** (proves
switching), 2-col + 3-col, figure+caption, callout/takeaway, blockquote, table,
code+math, big-stat, custom-marker list, `alert`/`hl`, and a “press T to toggle”
instructions slide. Doubles as a living style reference for future decks.

## Rollout (only after you like the test deck — separate sign-off)

Adopt across the 15 decks by swapping the one `<link>`(+script) line each —
low-risk, reversible, one commit. Not in scope now.

## Back-pressure / how we know it worked

- `python3 tools/check-asset-links.py` → resolves the new css/js refs, 0 new
  breakages.
- Local preview (`npm start`, `/THEME_TEST_2026/`); screenshots of both modes +
  a mid-deck switch.
- WCAG ratios above hold (recompute on final hexes).
- Print-to-PDF sanity in both modes (`?print-pdf`).
- Nothing in the other 15 decks changes — `git status` stays clean outside the
  new dir + `assets/themes/` + `docs/`.

## Open decisions for you

1. **Type direction: A (Fraunces) / A′ (Newsreader) / B (grotesque)?** ← blocks build
2. Keep the optional running footer on or off by default? (lean: off; on per-deck)
3. Test-deck name `THEME_TEST_2026` ok, or you'd prefer `_theme-lab/`?
