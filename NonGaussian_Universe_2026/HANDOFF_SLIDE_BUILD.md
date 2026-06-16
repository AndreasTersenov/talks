# HANDOFF: build the "Non-Gaussian Universe" slide deck

You are picking up a talk that has been fully planned (content, narrative, figures) in a separate
session. Your job is to **build the reveal.js deck** in this folder
(`/home/tersenov/software/talks/NonGaussian_Universe_2026/`), using the repo's Preprint theme, from a
finished content package. Do **not** redo the science or re-plan the narrative; it is locked. Read the
source-of-truth files, plan the build, get Andreas's sign-off, then build.

---

## 0. The talk in one screen

- **Title (locked):** "Do Baryons Break Higher-Order Statistics?"
- **When/where:** Tue 16 Jun 2026, 12:30–13:00 (30 min slot), Dougalis room, FORTH, Heraklion.
- **Length:** ~25 min of talking (assume Q&A inside the slot).
- **Conference:** "The Non-Gaussian Universe" (a small, expert, Starck-lineage meeting: wavelets/sparsity,
  higher-order weak-lensing statistics, SBI/NDE methodology, one-point statistics, plus a large 21cm/EoR
  contingent). There is a strong "can we trust beyond-2pt?" undercurrent and a **Wednesday round table**
  whose questions this talk is built to seed.
- **Shape:** two acts as one story. **Part 1** = the baryonic-feedback paper (Tersenov, Guerrini,
  Kilbinger, Starck). **Part 2** = the L1-vs-CNN SBI work. The spine is the **optimal tomographic
  weak-lensing strategy**, and the connective tissue is the **BNT transform** (Part 1: BNT breaks the
  analytical statistic; Part 2: the break is a recoverable frame artifact).

---

## 1. Source of truth (READ THESE FIRST, in this order)

All in the `cnn_sbi` repo (a different repo from this one; use absolute paths):

1. **`/mnt/home/tersenov/software/cnn_sbi/TALK_NONGAUSSIAN_CONTENT.md`** — THE content package. It has:
   the one-sentence spine (§0), the full narrative arc (§1), **audience tuning per speaker (§1.5)**, the
   **slide-by-slide content S1–S19 (§2)** with the spoken point + the figure for each, the
   **figure-per-slide manifest (§3)**, the **vetted numbers + honesty flags (§4)**, and the
   **build-in-deck asset list (§5)**. The §2 slide titles are already written as assertion-evidence
   headlines; use them as the slide titles.
2. **`/mnt/home/tersenov/software/cnn_sbi/TALK_BEST_PRACTICES.md`** — slide-design and narrative
   standard (Doumont/Alley/Hull/Olson distilled): assertion-evidence headlines, one message per slide,
   KISS, colorblind-safe, conclusions stated early. Follow it.
3. **`/mnt/home/tersenov/software/cnn_sbi/TALK_FIGURE_AUDIT.md`** and
   **`/mnt/home/tersenov/software/cnn_sbi/talk_figures/INDEX.md`** — the figure inventory and the
   **locked color palette** (see §4 below).
4. **`/home/tersenov/software/talks/CLAUDE.md`** — this repo's conventions (auto-loaded for you). The
   Preprint-theme section is load-bearing for how you wire the deck.

The budget reality is in the §2 intro: the content is the **full ~30 min version (19 slides + a ~4-5 min
animation block)**. To land 25 min there is a documented **trim path** (merge S2+S3, keep S5/S6 fast,
fold the marked beats) to ~16 slides. Build the full version; mark the trims so Andreas can cut live.

---

## 2. Repo + theme conventions (how decks are built here)

Read `/home/tersenov/software/talks/CLAUDE.md` in full. The essentials:

- Each talk is a standalone reveal.js deck in its own dir; **this deck is `index.html` in this folder.**
- **Shared assets** live at the repo root `assets/` and are referenced with a relative parent path
  including the subfolder: `../assets/figures/<category>/foo.pdf`. Never a per-talk `assets/`, never an
  absolute `/assets/…`, never a symlink (Pages drops symlinks). Categories under `figures/`:
  `maps/`, `posteriors/`, `statistics/`, `matrices/`.
- **Use the new Preprint theme.** It lives in `assets/themes/talks.css` + `assets/themes/theme-switch.js`.
  **`PREPRINT_TEMPLATE/` is the reference deck** (a migrated `LAM_2026`, dark + light, exercising every
  component): copy its wiring to scaffold this deck. Paper/preprint aesthetic: cobalt accent, Source
  Serif 4 headings, IBM Plex Sans body, IBM Plex Mono labels, ruled `.block` callouts.
- **Per-slide light/dark:** tag a `<section data-theme="light">` to match a figure made for a light
  background; dark is the default. Scoped per section, PDF-safe.
- **Component classes** (use these, do not hand-roll): `slide-title` (+ optional `<span class="sec">§2</span>`),
  `block`/`block-title`/`block-content`, `kicker`, `callout`/`takeaway`, `stat` (`num`+`label`),
  `runhead`, `alert`, `title-card`, `container`/`col`.
- **Do not inline-style theme colors** (`style="color:#…"` is invisible to the theme; use tokens
  `var(--accent)`, `var(--surface)`, `var(--fg-muted)`, …). **Exception:** the locked Wong *method*
  colors (CNN `#0072B2`, L1 `#D55E00`) are an intentional, colorblind-safe data encoding and stay as
  literal hex in legends/figures/animations. Theme chrome = tokens; method identity = Wong hex.
- **Preview** from the repo root: `npm install` once, then `npm start`, open
  `http://localhost:8000/NonGaussian_Universe_2026/`. PDF export: append `?print-pdf` and print.
- **Verify refs:** `python3 tools/check-asset-links.py` from the repo root after editing.

---

## 3. What ALREADY EXISTS in this folder (integrate, do NOT rebuild)

This folder is currently "parked self-contained" (vendored reveal.js + KaTeX, white theme). Two finished
or in-progress interactive components were built here and must be **integrated** into the real deck, not
recreated:

- **`bnt_explainer.{html via index.html, css, js}`** — the **BNT intuition animation** ("shadows of a
  rotating cloud"). This IS Andreas's ~4-5 min intuition block (the deck's S15→S16 hinge: *why BNT
  destroys the per-channel ℓ1 but is lossless for the channel-mixing CNN*). It is **three** explainer
  slides (`cloud`, `mechanism`, `twopoint`), each a `<section data-bnt-explainer>`. **Read this folder's
  `README.md`** for the integration recipe ("Drop it into your real deck" + "Integrate-later pass"):
  copy the `<section>`s in, link the CSS, call `BNTExplainer.attach(Reveal)` after `Reveal.initialize`,
  retune chrome to theme tokens but **keep the Wong method colors**. The on-screen numbers are the real
  measured ones (3045→779 = 0.26×, 3326→3186 = 0.96×, whiten 1.06×); do not change them. This is
  Andreas's content; integrate it, do not rewrite the mechanism.
- **`neural_summaries.{html,css,js}` + `neural_summaries_section.html`** — the **S11 "how a CNN learns a
  summary" viz** (slide 1 = regression/MSE; the VMIM half is the companion). This is exactly the S11
  beat (MSE → VMIM). Inspect it, finish/integrate it for S11; do not start over.
- `proto_mechanism.html`, `proto_neural_summaries.html`, `proto_principle.html` — prototypes/explorations.
  Reference only.

When you wire these into the real deck, follow the README's integrate-later pass: drop the vendored
`vendor/reveal/`, point at the repo reveal.js submodule, link `../assets/themes/talks.css` +
`theme-switch.js`, and author the animation sections as `data-theme="light"` slides.

---

## 4. Hard rules (do not violate)

- **Locked Wong palette:** CNN = blue `#0072B2`, L1 = vermillion `#D55E00`. Color encodes *method only*.
  Basis is texture (no-BNT solid, BNT hatched). Never combine `hatch` + `alpha` in matplotlib (PNG and
  PDF render differently); use a lightened fill + saturated hatch. (Full rule in `TALK_FIGURE_AUDIT.md §0`.)
- **No em-dashes** anywhere in slide text (use commas/colons/parens; arrows → ⇔ ↦ are fine). Say
  "projection" not "shadow", "cross-bin"/"common signal", avoid colliding terms. (The content doc is
  already em-dash-free; keep it that way.)
- **Honesty flags (must travel onto the slides; full list in `TALK_NONGAUSSIAN_CONTENT.md §4`):**
  - M1 is **~7% (population median), matched-NDE, calibrated-with-caveat**. NOT "+15%", NOT the
    noiseless-obs number. Phrase: "the analytical ℓ1 almost matches the optimal CNN; the gap is the
    density estimator, not the physics." The fully-clean L1 number is raw-MAF 2875.
  - M3 BNT: L1+product **3045 → 779 = 0.26×** (collapse), CNN **3326 → 3186 = 0.96×** (lossless),
    matched NDE; whitening recovers **1.06×**.
  - The **"CNN+BNT → baryon-robust HOS" punchline is forward-looking**, not a demonstrated end-to-end
    baryon-mitigation result. Present it as the synthesis/next-step, not a measurement.
  - **Do not merge Paper I (full-sky HEALPix, ℓ_max cuts) and Paper II (flat-sky 10° patches) into one
    quantitative FoM ladder.** "PS → ℓ1 → CNN" is a conceptual progression, not one axis.
  - **Always show marginals (σ and/or 2D areas) alongside any FoM3** (FoM3 is fragile).
  - **Never present the historical inflated numbers** ("L1 wins 3-4×", the full-sphere-cross results) as
    results; they appear only as the *journey* on the verdict/pitfalls slide.
- **The BNT-intuition block content is Andreas's.** Integrate the existing animation; do not invent a
  new mechanism or restyle its numbers.

---

## 5. Figures: where they are, how to bring them in

- The curated talk figures live in **`/mnt/home/tersenov/software/cnn_sbi/talk_figures/`** as `p1_*`
  (Part 1, baryon paper) and `p2_*` (Part 2, this work). `INDEX.md` there is the catalog.
- These are in a **different repo**. To use them, **copy each into this repo's shared assets**
  (`/home/tersenov/software/talks/assets/figures/<category>/`) and reference as
  `../assets/figures/<category>/…`. Pick the category that matches (`posteriors/`, `statistics/`,
  `maps/`, `matrices/`). Update `docs/asset-map.tsv` if you follow the existing bookkeeping.
- **Part 1 shortcut:** the `LAM_2026` deck already uses dark-theme `_dark.pdf` versions of most Part-1
  figures (in `assets/figures/statistics/` and `assets/figures/posteriors/`). If you theme Part 1 dark,
  reuse those directly. Light Part-1 versions = the `p1_*` from `talk_figures/`.
- **Reuse from `LAM_2026`** (see its `index.html`, Part 3, and §3 of the content doc): the **Illustris
  feedback video** (`assets/videos/illustris_movie_cube_sub_frame.mp4`) for S4, the **`NDE.gif`**
  (`assets/figures/statistics/NDE.gif`) for the flow side of S11, and the LAM "Summary Statistics" slide
  assets for the peaks/ℓ1 build (S5/S6). LAM's "Statistics vs Systematics" slide is the model for S4.
- After any figure move, run `python3 tools/check-asset-links.py`.

---

## 6. The build plan (slides S1–S19 + the animation block)

Authoritative content is `TALK_NONGAUSSIAN_CONTENT.md §2`; this is the index with the asset disposition.
★ = a slide that carries the talk. "build" = a new in-deck HTML/CSS asset to author (see §7).

| # | slide (assertion title in §2) | asset disposition |
|---|---|---|
| S1 | Title | title-card; optional κ-map backdrop |
| S2 | Optimizing statistics, but 2pt does not trust the contours | **build**: 2pt-skeptic cartoon + trust checklist |
| S3 | Optimal statistics studied, optimal *tomography* not | **build**: tomography viz (n(z) + overlapping kernels) |
| S4 | Stage IV is systematics-limited | reuse LAM framing + Illustris video + `p1_methods_tomo_maps` |
| S5 | Wavelet peak counts | **build**: peak-count illustration (LAM "Summary Statistics" assets) |
| S6 | The ℓ1-norm uses the whole distribution | **build**: ℓ1 definition/histograms |
| S7 ★ | Baryonic bias scales with survey area | `p1_bias_vs_survey_area` |
| S8 ★ | HOS resilient and 3× | `p1_PSvsHOS_safe_scales` |
| S9 ★ | The BNT bridge (it breaks HOS) | `p1_bnt_kernels` + `p1_maps_before/after_noisy` + `p1_BRIDGE_bnt_inflates_l1` |
| S10 | The comparison, done fairly | `p2_pipeline_schematic` |
| S11 | Neural compression: MSE → VMIM | **integrate `neural_summaries.*`** (already started) |
| S12 ★ | M1: ℓ1 almost reaches the optimal CNN (~7%) | `p2_M1_matched_nde` (+ opt `p2_M1_corner_matched`) |
| S13 ★ | Can we trust it? | `p2_M1_calibration_tarp` + `p2_M1_calibration_sbc` |
| S14 ★ | Where the cross-bin info lives (M2) | `p2_M2_cross_deleaking` |
| S15 ★ | BNT revisited (M3 quant) | `p2_M3_bnt_inflation` |
| block | **Andreas's BNT-intuition animation** | **integrate `bnt_explainer.*`** (3 acts; ~4-5 min) |
| S16 ★ | The clincher: a frame artifact | `p2_M3_bnt_whitening` |
| S17 | Is the +7% worth it? (→ round table) | **build**: cost/benefit balance |
| S18 ★ | One story: the optimal tomographic strategy | `p1_BRIDGE_bnt_inflates_l1` + `p2_M3_bnt_whitening` pair |
| S19 | Takeaways and what's next | text summary |

Park draft slides with `data-visibility="hidden"` rather than deleting. Tag the `(fold if tight)` beats
(noted in §2) so Andreas can cut to ~16 for 25 min.

---

## 7. Build-in-deck assets to author (pure illustration, no data)

All can be HTML/CSS components in the Preprint theme (preferred, theme-consistent) or small static
figures. Keep the Wong method colors; use theme tokens for chrome.

1. **S2 2pt-skeptic cartoon** + the **trust checklist** (items: blinding, covariance, emulators,
   systematics, analytical cross-checks, Gaussian-likelihood, method limits, null/validation tests,
   simplicity), with the items this talk addresses highlighted (systematics, limits, validation/null,
   simplicity) and the two SBI removes for free (covariance, likelihood). The cartoon is a laugh line;
   a simple speech-bubble icon is enough.
2. **S3 tomography viz** — the n(z) bins and the broad, overlapping lensing kernels (projection / kernel
   mixing). This is the visual anchor for cross-bin information and the callback at S9 (BNT re-mixes the
   same kernels). Andreas may already have a version; ask.
3. **S5 peak-count illustration** and **S6 ℓ1-norm definition** — the starlet decomposition, peaks =
   local maxima per scale, ℓ1 = sum of |coefficients| in SNR bins (peaks + voids + everything). LAM's
   "Summary Statistics" slide has reusable pieces.
4. **S17 cost/benefit balance** — a scale: the ~7% M1 bar on one pan, the cost on the other
   (architecture search, large dataset, unphysical-info traps that escape TARP/SBC), BNT as the thumb.

---

## 8. Audience tuning (weave as one-line nods, do not make separate slides)

Full detail in `TALK_NONGAUSSIAN_CONTENT.md §1.5`. The highlights:

- **The Wednesday round table** (Porqueres, Heavens, Uhlemann, Camera, Cuesta-Lazaro) is the single
  biggest opportunity; its posted questions (validation standard, robust-to-systematics, interpretable
  vs optimal, physics-based vs learned) are this talk's spine. S2, S12, S13, S17, S19 tee it up.
- **Simone Vinciguerra** is in the room: his Euclid forecast is the one S9 cites and S16 answers. Name it.
- **Alan Heavens** (keynote, hybrid analytical+NN compression): frame M1 as a data point for his program.
- **Cora Uhlemann** (one-point statistics): the starlet ℓ1 is a multiscale one-point statistic.
- **Giovanni Aricò** (baryonification): modeling and conservative cuts are complementary, not rivals.
- **Systematics humility:** Part 2 is a controlled methods comparison; real-world robustness (IA,
  source clustering, photo-z) is the work of others here (Vedder, Hwang, Gebauer). Say so on S19.
- **21cm/EoR half:** the ℓ1-norm / one-point PDF and the basis-dependence lesson generalize (S18/S19).

---

## 9. Workflow and back pressure

1. Read the four source-of-truth files (§1) and this folder's `README.md`.
2. **Write a short build plan** (deck scaffold choice, figure-transfer list, slide-by-slide asset
   mapping, which existing components go where) and **get Andreas's sign-off before building.** His
   standing rule: plan first, do not start coding until signed off.
3. Scaffold from `PREPRINT_TEMPLATE/` (or migrate this folder), wire the theme, hydrate the reveal
   submodule.
4. Bring in figures (copy to `../assets/figures/<category>/`, or reuse LAM `_dark`), then
   `python3 tools/check-asset-links.py`.
5. Build act by act. Integrate `neural_summaries` (S11) and `bnt_explainer` (block). Author the
   build-in-deck assets (§7).
6. **Back pressure every step:** preview at `http://localhost:8000/NonGaussian_Universe_2026/`, check the
   PDF export (`?print-pdf`) renders (animations have static fallbacks), run the asset-link checker, and
   confirm no em-dashes and the Wong palette on every method-colored element.
7. Iterate with Andreas on look and pacing.

---

## 10. Definition of done

A Preprint-theme `index.html` in this folder that:
- realizes S1–S19 + the integrated BNT animation block, content faithful to `TALK_NONGAUSSIAN_CONTENT.md`;
- integrates (not rebuilds) `bnt_explainer` and `neural_summaries`;
- references all figures via `../assets/…`, passes `check-asset-links.py`, and exports cleanly to PDF;
- obeys the Wong palette, the no-em-dash rule, and the §4 honesty flags;
- carries the `(fold if tight)` markers so the full ~30 min version trims to ~25 min live.

---

## 11. First prompt for the new session

Paste the block in `FIRST_PROMPT.md` (next to this file) into the fresh Claude Code session.
