# PhD Defense — University of Crete, 14 September 2026

Andreas Tersenov. **45 min presentation (mostly uninterrupted) → ~5–15 min general-audience
questions → closed examination by the seven-member committee, 1–3 h.**

Forked from `../cosmo26/` on 2026-08-25 for its mechanics, theme and reusable slides.
Per TALK-GUIDELINES §2.7: **the chrome is inherited, the argument is re-derived.**

## Read these first

| file | what it is |
|---|---|
| **`STRUCTURE.md`** | The running order, the 2×2 spine, the budget, the cut lines, the backup plan, the committee analysis. Signed off before slide surgery. |
| **`PAPER_FACTS.md`** | The number ledger, all four thesis chapters. **No number goes on a slide unless it is in here with a source line.** Derived numbers are marked `[derived]` with the arithmetic. |

Two things in `PAPER_FACTS.md` govern every result slide:

- **Ratios only.** No absolute figure of merit reaches a slide. Each act draws a baseline at 1.0
  and names what its 1.0 means (§0, §7 of `STRUCTURE.md`).
- **The ratios are not all the same quantity.** Ch2's FoM is a fourth root over four parameters;
  Ch4/Ch5's is a square root over three. `PAPER_FACTS.md` §0 and §8.2 carry the prepared answer.

## Status

**2026-09-01 — the light section starts, at shear and convergence.**

Two slides added after Euclid, **0.6a** (shear and convergence) and **0.6b** (what the convergence
is), rebuilt from `../LAM_2026/` §5 and §6 into the preprint components. **They are the first light
slides in the talk** — the dark run ends at Euclid and the change of ground marks the move from the
picture of the Universe to the quantities the thesis operates on.

Two figures were re-cut rather than restyled, because both carried an opaque white page that read as
a bright card on the warm paper: `assets/diagrams/WL_distortions_trim.png` and
`assets/figures/maps/WL_mass_map_trim.png` are ink-and-plot on transparency, cropped to their
content. **The originals are untouched** — nine other decks reference them.

Two things this opened, both written up in `STRUCTURE.md` §5 under the Act 0 table:

- **⚠ The talk is about 2:30 over.** Re-measured beat by beat on 2026-09-03: Act 0 **11:25**,
  Act 1 **11:29**, Act 2 **3:57** — **26:51 scripted**, plus roughly 20:12 still estimated for
  Acts 3–4 and the conclusions, against a 45:00 slot. Every one of the 25 beats now agrees with its
  own heading to within 3 seconds. The cut ladders are the first place to go. See
  `SPEAKER_SCRIPT.md`'s budget note and `STRUCTURE.md` §5.
- **Slides 14–35 converted to the light theme** (2026-09-02). 19 frames took `data-theme="light"`,
  their explicit black `data-background` was stripped (it would beat the theme background), and
  **34 hardcoded inline colours were retokenised** by the `talks-inline-styling` recipe: the dark
  card fills (`#1c1c1c`, `rgba(20,20,20,.85)`, …) → `var(--surface)`, the dark-background accents
  (`#ffaa7f`, `#6bdcff`) → `var(--accent)`, light text (`#ddd`, `#e7e7e7`) → `var(--fg)`, greys →
  `var(--fg-muted)`, hairlines → `var(--edge)`. Zero hardcoded hex left in the range.
  **9 figures were repointed to `_light` siblings that already existed** — every one preserves the
  original aspect ratio, so no layout moved. Those siblings were the *recoloured fallbacks* from
  `tools/darkfig-to-light.py`.

  **Three of them are no longer fallbacks** (2026-09-03). The two result figures on frames 28–29 —
  `countours_all_methods_MSPC_6scales_light`, `countours_ks_different_scales_light` and
  `countours_mca_different_scales_light` — are now rendered from the **published paper PDFs**
  (`AA53707-25/figures/*.pdf`) at 250 dpi, with the opaque white page removed so the warm paper
  shows through. The recoloured versions had a real defect: inverting the near-neutral pixels turned
  Kaiser–Squires' **grey** contour coding into thick black halos, and muddied the fills. The
  conversion rule (`tools/`-style, near-white band only: `min(r,g,b) ≥ 252` → transparent,
  `≤ 236` → opaque) deliberately never touches mid-grey, so the grey method coding survives.
  All three PDFs are 576×576 pt and the outputs 2000×2000, identical to what they replaced, so no
  layout moved. Ink covers 90.7 % of frame against the fallbacks' 93.3 % — under 3 % smaller, and
  left uncropped so the slide matches the paper's own framing.

  **Four more replaced from Andreas's own re-exports** (2026-09-03): `Relation_btw_kappa_and_gamma_light`
  (frame 9 — the old one carried a black box behind the lensing potential), `cosmology_with_maps_light`
  (41), `starlet_transform_light` (42) and `wavelet_l1_norm_light` (43). Same 250 dpi + de-page
  treatment. Three were aspect-neutral to within 2 %; `cosmology_with_maps` came out 7.5 % wider in
  aspect, i.e. shorter, so it cannot overflow. **Frame 43 got a NEW file rather than an overwrite**:
  it had been pointing at `wavelet_l1_norm.png`, which `NonGaussian_Universe_2026` also uses, so the
  deck was repointed to `wavelet_l1_norm_light.png` and the shared original left alone.

  **The shear thumbnail was converted, not just darkened** (2026-09-03). It was drawn for a black
  background, so its colormap put the *strong* signal at the bright end — which on cream is the end
  that disappears. `tools/darkfig-lab-invert.py` inverts CIELAB L\* for every pixel, reversing the
  ramp so strong whiskers are dark on paper, while a\*/b\* keep the hue a naive 255−RGB inversion
  would have flipped. One file covers the chain slide, both act dividers and the inverse-problem slide.

  **One recoloured fallback is left on a live slide:** `mass_maps_(ks_iks_mca)_transparent_light`
  (frame 27). `mass_maps.pdf` in the paper folder is its counterpart; the difference is a **colour
  cast** — the fallback is brighter and warmer than the published figure — not the halo defect, so
  it is left for Andreas to rule on.

  **Two pre-existing markup bugs on frame 43**, LAM-verbatim and untouched by this pass:
  `class="block; fragment fande-in"` — the stray semicolon means the class is `block;`, so the
  callout never matches `.block` and renders unstyled, and `fande-in` is a typo for `fade-in`, so
  that step appears with no animation. Both are visible in the deck. Left for the joint LAM restyle.
  **The Part 1 act divider was deliberately left dark** — dividers are punctuation between
  movements (see the theme map). One attribute if that call is wrong.
- **Bayes is taught once, at A1.4** (2026-09-02), not twice. The reconstruction slide is now an
  *anatomy* of posterior ∝ likelihood × prior with the prior term marked and fanning into the four
  methods that can fill it; it absorbed the old *Overview of mass mapping methods*, and the MAP /
  proximal machinery is a vertical beneath. The MAP-vs-full-posterior distinction is deferred to
  Part 2 with a FLAG in the script. Reasoning in `STRUCTURE.md`, "Where Bayes gets taught".
- **Part 1 was rebuilt for continuity** (2026-09-03). It ran as a sequence of slides rather than an
  argument, so it now goes: divider → *why the problem is hard* → Kaiser–Squires → the Bayesian
  view → sparse → MCALens → *the stakes* → the experiment → the three maps → the answer → where the
  gain comes from. **The back half came from the parked *Restyled Acts 1–2* block**, which had been
  sitting hidden and undecided since it was built and already implemented the design this pass
  needed; the four LAM originals it replaces are hidden behind a new *LAM originals, Part 1*
  divider, not deleted. **Two slides were built from scratch** — the forward/inverse teaching slide
  (specified in `STRUCTURE.md` since the Acts 1–2 plan, scripted, never built) and the stakes slide.
  **MCALens was rebuilt** around what it assumes, how it alternates, and what a proximal operator is
  — the step PnPMass later replaces — with its algebra demoted to a vertical and its long-swapped
  `\underbrace` labels corrected. **The four-panel slide lost the RMSE table** and gained a key of
  what each method assumes, badged *Euclid baseline* / *state of the art*. **Seven statistics frames
  moved to the head of Act 3**, where they collide with one existing slide — flagged, not merged.
  **The four-question scoreboard moved to just before the conclusions.** Full reasoning in
  `STRUCTURE.md` §5b.
- **The intro block moved to the back** (2026-09-01): the hinge plus the five earlier intro
  versions now sit at reveal #89–95. Act 0 runs title → formalism → chain → four questions with no
  detour. **0.4's S₈ tension is now unresolved** — see `STRUCTURE.md` §5.
- **The theme now flips three times in five slides** — dark, light ×2, dark ×2 (the hinge and the
  chain), light (the scoreboard). Moving 0.6a/0.6b after the scoreboard would make it one flip and
  keep the hinge two slides from the tension it pays off. Left as placed, which was the instruction.

`SPEAKER_SCRIPT.md` A0.5 was rewritten at the same time: it still opened *"This is the same diagram
again"*, which stopped being true when A0.5 became the Stonebraker lensing figure rather than the
cone. The stale register note and the tier-0 short path that repeated the claim are fixed too.

**2026-08-27 — Acts 1 and 2 are in the deck, lifted verbatim.**

102 top-level sections: **75 in the live flow**, 27 parked. The deck now runs Act 0 → Acts 1–2
(Ch2, Ch3) → Acts 3–4 (Ch4, Ch5, inherited from cosmo26) → conclusions → backup.

- **Acts 1–2 are `../LAM_2026/` §24–57, copied unchanged.** Deliberate: the restyle into the
  preprint components is a later, joint pass. LAM's vertical stacks and fragment builds are intact,
  so several slides are legitimately blank until the first click (`Performance` is all fragments).
- **`SPEAKER_SCRIPT.md` now covers Acts 0, 1 and 2** — 16:07 measured against a 20:00 budget.
  Written before the slides, as with Act 0.
- **The four-question scoreboard (A0.10) exists**, closing Act 0. `STRUCTURE.md` §4 specified it and
  nothing implemented it.
- **Section markers renumbered** to the defense's four acts. They were cosmo26's three: §1→§3,
  §2→§4, cosmo26's §3 split between Act 3 (the nulling cliffhanger) and Act 4 (the recovery), and
  its §0 demoted to `backup`.
- **Every PDF-in-`<img>` is gone** (0 refs), and `check-asset-links.py` reports **0 problems**.

### Structural repair — 2026-08-27

**105 of the deck's 129 sections were sitting after `</html>`.** The browser closed the document
and put them in `<body>` outside `.reveal`, so reveal owned only 24 slides while the rest rendered
as ordinary page flow beneath its chrome. Spliced back inside `div.slides`; **nothing was lost**.

Now: **84 navigable slides**, 24 vertical sub-slides, 21 parked (reveal strips those at init),
0 KaTeX errors, 0 asset problems.

The reason this survived so long is that every text-level check passes on a file in that state —
asset links, tag balance, file-order heading listings, even screenshots. Only a DOM count of
`div.slides > section` catches it. Written up as `../docs/REVEAL-GOTCHAS.md` §8b; run it after any
scripted insertion.

### The mass-mapping inverse problem — promoted 2026-08-27

Nine slides moved from the parked block into the live flow at **15–23**, immediately before the
Act 1 divider, in LAM's own order: the κ–γ relation → mass mapping as an inverse problem → KS and
why it is ill-posed → the operator form → KS's practical difficulties → Bayesian reconstruction →
sparse recovery → MCALens → the methods overview. This is the setup Act 1 assumes.

Per-method detail stays parked as examination backup: inpainting, the two Wiener-filter slides,
`from galaxies to mass maps`, and the weak-lensing intro that Act 0 already covers.

**Two bugs surfaced doing it, both inherited from `../LAM_2026/`:**

- **Fixed.** `\kappa_\rm G` — a brace-less `\rm` subscript on the MCALens slide. MathJax (which
  LAM loads) tolerates it; the vendored **KaTeX** in this deck does not, so the whole boxed
  equation rendered as red error text. Now `\kappa_{\rm G}`. Deck-wide KaTeX errors: **0**.
  Worth knowing generally: anything lifted from a MathJax deck needs a KaTeX pass.
- **NOT fixed, needs your call.** On that same MCALens slide the two `\underbrace` labels are
  **swapped**: κ<sub>NG</sub> is labelled *"Standard Wiener filter approach"* and κ<sub>G</sub>
  *"Modified wavelet approach"*. It is the other way round — the Gaussian component is the Wiener
  part, the non-Gaussian is the sparse/wavelet part, which is what the alternating-minimisation
  lines further down the same slide correctly imply. Left alone because it is a verbatim lift,
  but it is a factual error about your own method with Starck on the committee.

### Parked, not deleted

| block | what | why |
|---|---|---|
| *Earlier intro versions* | the Act 0 iterations | kept for comparison |
| *Restyled Acts 1–2* | 9 slides rebuilt in the preprint components | superseded by the verbatim lift, pending the joint restyle |
| *Lensing pedagogy and mass-mapping methods* | `../LAM_2026/` §3–23, 21 slides | raw material for A0.5 and the Ch2 backup library — promote what is wanted |

### The figure problem, and where it stands

Two things bite every deck lifted out of `LAM_2026` / `ENS_seminar_2026` / `PhD_Day_2025`:

1. **Chrome renders nothing from a PDF inside an `<img>`.** Those decks carry 25 / 24 / 19 such
   refs; cosmo26 carries none, which is why it stayed invisible. Every figure the defense deck uses
   is now rasterised to `.png` with `tools/darkfig-to-light.py --no-invert` — same appearance, a
   format that draws.
2. **Their result figures were exported for a dark background** (transparent canvas, white axes and
   labels), so they cannot go on a light slide as they are.

**Andreas has light-background originals of these plots** (2026-08-27). Those are the right answer
and they supersede the recolouring below — **do not spend more time converting dark figures.**

`tools/darkfig-to-light.py` recolours as a fallback: it inverts near-neutral pixels only, and
protects filled panels by eroding the alpha channel so glyph strokes flip while an `imshow` map or
a white axes patch does not. It works, but not perfectly — the converted figures still read a little
oddly, which is why the originals win. The tool stays for the rasterising, which is not optional.

## The reuse map

This is the actual state of play. cosmo26 was built from thesis Ch4 and Ch5, so **Movement II
arrives in this fork almost complete**; Movement I is built in other decks in this repo and has to
be lifted in (below).

### Movement II — inherited, mostly ready

| forked § | our slide | action |
|---|---|---|
| 2 — scales schematic | **A3.1** Q3 opener | reuse |
| 3 — starlet → peaks and ℓ1 | **A3.2** | reuse |
| 4 — SBI pipeline, NPE | **A3.3** | reuse, add the on-simulations flag |
| 5 — baryonic bias vs survey area | **A3.4** | **merged** with §6 into one beat |
| 6 — what the cuts cost | **A3.4** | **merged** with §5 |
| 7 — are HOS still useful? | **A3.5** | **re-plot** as the ratio-vs-area curve, PS at 1.0, bands drawn |
| 14 — nulling inflates the contours | **A3.6** cliffhanger | reuse |
| 8 — beating the PS is a low bar | **A4.1** Q4 opener | reuse |
| 9 — a compressor trained to be information-optimal | **A4.1–A4.2** | reuse |
| 10 — same maps, same flow, both calibrated | **A4.2** | reuse; this is the methodological claim |
| 11 — read bin by bin, ℓ1 trails | **A4.3** | reuse, restate as ×0.74 of the ceiling |
| 12 — two routes to the inter-bin information | **A4.4** | reuse |
| 13 — read jointly, ℓ1 reaches the CNN | **A4.5** | **re-plot** ladder as fractions of the ceiling |
| 15 — the information is recoverable | **A4.6** | reuse; retention ladder is already ratios |
| 16 — conclusions | **C.1** | rewrite as the four-question scoreboard |

### Movement I — not in this fork, but built elsewhere

**Correction (2026-08-25).** An earlier version of this file said Movement I "does not exist at
all." That was wrong — it was based on looking only at cosmo26. `../LAM_2026/` and
`../ENS_seminar_2026/` already contain the Ch2 and Ch3 story, and `../PhD_Day_2025/index.html`
contains the cosmological opening and the lensing pedagogy. See `STRUCTURE.md` §11b for the full
source table and what lifting costs.

| our slides | what | source |
|---|---|---|
| **A0.2–A0.7** | the cosmological frame and the lensing pedagogy | `../PhD_Day_2025/index.html` §3 §5 §9 §21 §22 §24 §12–15 |
| **A0.8** | information and systematics share a scale range | cosmo26 §2, base state |
| **A0.9–A0.10** | the chain diagram, the four-question scoreboard | **new** |
| **A1.1–A1.5** | Ch2, mass mapping | `../LAM_2026/` §25–46 |
| **A2.1–A2.3** | Ch3, PnPMass | `../LAM_2026/` §47–58 |
| **C.1–C.5** | conclusions, limitations, perspectives, output, thanks | **new**, C.1 from cosmo26 §16 |

The catch: those decks load `darkenergy.css` **without** the `talks.css` preprint overlay, so every
lifted slide needs a real restyle into this deck's components. The figures and the argument
transfer; the markup does not.

### Chores the fork carries

- **Section markers are stale.** The forked deck's `<span class="sec">§1/§2/§3</span>` refer to
  cosmo26's three acts. They must be renumbered to the defense's four.
- **`bnt_explainer.js` hardcodes the superseded recovery ladder** `0.15/0.22/0.93/1.06`. Ours is
  `0.16/0.24/0.72/0.96`. See `PAPER_FACTS.md` §7. Re-point before reuse.
- **The `Backup` divider (§17) and the 32 slides after it** need re-indexing against
  `STRUCTURE.md` §10, which asks for a *chapter-organised* library covering all four chapters.
  What is inherited covers Ch4 and Ch5 only.
- Four graphics named in `STRUCTURE.md` §13.5 do not exist and carry the ratio grammar.
- Act 0 is planned and sourced (`STRUCTURE.md` §5) but **not built**.

## Preview

From the **repo root**, never from here:

```bash
npm start                    # then open http://localhost:8000/PhD_Defense_2026/
python3 tools/check-asset-links.py
```

PDF export: `http://localhost:8000/PhD_Defense_2026/?print-pdf`, then print-to-PDF. Export it
early — `../docs/REVEAL-GOTCHAS.md` §5–§7 covers what breaks and how to compress the result.

## Anatomy

Standard repo conventions (`../CLAUDE.md`): `darkenergy` plus the `../assets/themes/talks.css`
preprint overlay, then `custom.css` and `new_slides.css`. Four interactive canvas components
carried over from cosmo26, each scoped CSS plus a reveal-agnostic JS engine:

| component | files | standalone preview |
|---|---|---|
| BNT explainer | `bnt_explainer.{css,js}` | `index_parked_bnt_preview.html` |
| Neural summaries (MSE vs VMIM) | `neural_summaries.{css,js}` | `neural_summaries.html` |
| SBI pipeline | `sbi_pipeline.{css,js}` | `sbi_pipeline.html` |
| Tomography flipbook | `tomography.css` | `tomography.html` |
| **The analysis chain** | `pipeline.js` + the `#wl-pipeline` `<template>` in `index.html` | &mdash; |

`*_section.html` are the paste-in `<section>` snippets. `vendor/katex/` renders the deck's math;
`vendor/reveal/` backs the standalone previews only.

Canvas components **do not paint under headless Chrome** (`REVEAL-GOTCHAS.md` §6) — a blank canvas
in a screenshot is a `requestAnimationFrame` artifact, not a bug, and a headless PDF has empty
panels on those slides. Print from a real browser.

## The typography pass — 2026-09-04

Body copy across the rebuilt slides was set at 0.5-0.6em in `--fg-muted`. That is the theme's
**caption voice** — small *and* grey — and it was carrying the argument on slides that were half
empty. Two rules now hold, and are recorded in `custom.css`:

- **Main content is `var(--fg)` at 0.66-0.95em.** `--fg-muted` at 0.42-0.48em is for captions,
  source lines and footnotes only. The one deliberate exception is the left column of the stakes
  slide, where the quieter grey *is* the contrast being drawn.
- **Size to the space, not to a scale.** If a slide is half empty the type is too small by
  definition; the scale exists to keep captions below the body, not to cap the body.

The same pass rebuilt the four LAM-verbatim Act 3 teaching slides (HOS constraints, peak counts,
wavelet peaks, the starlet l1-norm) out of bordered blocks and into figure-plus-three-lines, and
converted their dark figures with `tools/darkfig-panel-light.py` — the panel-aware companion to
`darkfig-to-light.py`, for figures whose imshow panels a blanket inversion would destroy.

**Not covered by it:** Act 2's PnPMass slides (still dark, still carrying inline hex), and the
already-restyled result slides of Acts 3-4, which were left alone because they are dense with
figures and were not the offenders.

## The introduction rebuild — 2026-09-06

Andreas walked the opening out loud and found two faults in its order. It taught the lensing
formalism — shear against convergence, the projection integral, the exact κ–γ relation — to a room
that had no use for it yet; and it declared only half the thesis before diving into Part 1, leaving
Parts 3 and 4 unannounced until the middle of the talk.

**The formalism block moved into Part 1.** Those three slides are Part 1's own machinery: the paper
is about inverting γ into κ, and Part 1's second slide is *the relation is exact, the measurement is
not*. They now sit immediately behind the Part 1 divider and run straight into it. Their parked LAM
originals travelled with them. Euclid hands directly to the real DES pipeline instead — and **the
theme flip from black to paper moved onto that slide**, where it marks the same boundary it always
did.

**Euclid gained a closing beat**: the lensing signal is the statistical memory of everything the
Universe has done since the Big Bang, and getting it out is an algorithms problem. That is the
sentence the rest of the talk answers.

**The chain slide became the map of the thesis.** All four questions are now asked on it, one per
click, each lighting the step of the chain it is about — the maps twice, then the summaries twice.
The four are **canonical**: the board before the conclusions asks exactly these, in the same words,
and is now a *return* rather than an opener. The wording deliberately avoids "higher-order
statistics", which the room has not met at that point.

New mechanism for it, in `pipeline.js`: `data-steps` on a `.pipeline-slot` marks each step's stages
`on-k`, and which step is showing is decided in CSS off reveal's own **`.current-fragment`** on
zero-size `.qstep` markers. Not `.visible` — fragments stay visible once shown, so `.visible` would
leave every earlier question lit as well. Not a `fragmentshown` listener either, because
`?print-pdf` sets the classes directly and fires no events. The cards live stacked in one grid cell
(`.qbay`) so the diagram above never walks up and down the screen as the questions turn over.

Cost on the clock, measured at 140 wpm: **+2:06 to the talk**, almost all of it on the chain slide.
`SPEAKER_SCRIPT.md` carries the arithmetic and the three cheapest ways to buy it back.

**Left open:** the conclusions slide still numbers its three answers Q1–Q3 against an older question
set (deep learning / baryons / nulling), which now collides with the canonical four; three backup
slides carry those old tags too.

## Not yet done

- Listed on the repo landing page (`../index.html`) as the top 2026 entry.
- ~~`SPEAKER_SCRIPT.md` is written through Act 2 only~~ — **rewritten end to end 2026-09-06.**
  All 62 main-line frames have a beat, both Q&A tiers are written, every timing is measured by
  `../tools/measure-script.py` and every `[CLICK]` is audited against the deck. Seven slides moved
  to backup on 2026-09-06, so the main line is **54 frames** and the script **measures 54:30 spoken
  against a 40:00 target**; the five-tier ladder in it lands at 40:15 and is the live plan. The
  script's *Seven slides moved to backup* table is the before/after numbering.
