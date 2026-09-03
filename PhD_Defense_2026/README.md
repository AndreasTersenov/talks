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

  **Still recoloured fallbacks on live slides:** `Relation_btw_kappa_and_gamma_light` (frame 9),
  `mass_maps_(ks_iks_mca)_transparent_light` (frame 27), `cosmology_with_maps_light` (42) and
  `starlet_transform_light` (43). Only frame 27 has a counterpart in the paper folder
  (`mass_maps.pdf`); the difference there is a **colour cast** — the fallback is brighter and warmer
  than the published figure — not the halo defect, so it was left for Andreas to rule on. The other
  three are schematics with no published original.
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

## Not yet done

- Listed on the repo landing page (`../index.html`) as the top 2026 entry.
- `SPEAKER_SCRIPT.md` does not exist. Spec in TALK-GUIDELINES §11b; `../cosmo26/SPEAKER_SCRIPT.md`
  is the worked example. It needs **two** Q&A tiers — the general-audience questions and the
  closed examination are different rooms.
