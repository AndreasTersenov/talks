# BUILD PLAN — "Do Baryons Break Higher-Order Statistics?" (Non-Gaussian Universe, 16 Jun 2026)

Status: **awaiting Andreas's sign-off**. Built from HANDOFF_SLIDE_BUILD.md, TALK_NONGAUSSIAN_CONTENT.md
(§2 slide list is authoritative), TALK_BEST_PRACTICES.md, CLAUDE.md, README.md. No re-planning of science.

---

## A. Scaffold approach

- **reveal.js**: `git submodule add https://github.com/EiffL/reveal.js.git NonGaussian_Universe_2026/reveal.js`
  then `git submodule update --init --recursive`. (GitHub is reachable; confirmed.) This gives the
  `darkenergy` theme + math/markdown/highlight/notes/d3/chart plugins the Preprint overlay expects.
  After integration, **delete `vendor/` and the vendored `vendor/katex/`** (no longer needed).
- **Theme wiring** (copy from PREPRINT_TEMPLATE): in `<head>`, after darkenergy ->
  `<link rel="stylesheet" href="../assets/themes/talks.css">`; at body end, BEFORE `reveal.js/dist/reveal.js`,
  `<script src="../assets/themes/theme-switch.js"></script>`. Init block mirrors the template
  (Markdown/Highlight/Notes/Math plugins, width 1200 x 720).
- **Light deck**: tag every top-level `<section data-theme="light">` (your stated preference, and it
  matches the white-background Part-2 figures + the light `p1_*` figures). Title slide keeps the
  particles `background.html` (or a kappa-map backdrop, see decisions).
- `index.html` becomes the real deck. The current parked `index.html`, `proto_*.html`, `slide_section.html`,
  `_verify.py` stay on disk as reference but are not referenced by the deck.

## B. Where the two existing components slot in (INTEGRATE, not rebuild)

- **`neural_summaries.*` -> S11** (2 sub-sections: regression/MSE, then VMIM). Link `neural_summaries.css`;
  load `neural_summaries.js` before init; `NeuralSummaries.attach(Reveal)` after init. Move
  `assets/kappa_patch.png` -> `../assets/figures/maps/kappa_patch.png` and fix the 2 `<img>` srcs. Retune
  chrome (`.ns-*`) to talks.css tokens; keep the MSE/VMIM 2-colour encoding. Add LAM `NDE.gif` next to the
  VMIM "flow" box. Math: prefer the deck's reveal Math plugin (KaTeX) for `\(...\)`/`\[...\]`; if its config
  fights the section, fall back to the section's own vendored KaTeX. (Decided at build after submodule checkout.)
- **`bnt_explainer.*` -> the BNT-intuition block, between S15 and S16** (3 sub-sections: `cloud`,
  `mechanism`, `twopoint`). Link `bnt_explainer.css`; load `bnt_explainer.js`; `BNTExplainer.attach(Reveal)`
  after init. Retune chrome to talks.css tokens, **keep the Wong method colours** (CNN `#0072B2`,
  L1 `#D55E00`) and the measured numbers (3045->779=0.26x, 3326->3186=0.96x, whiten 1.06x). Authored as
  light slides. (Note: content §1 prose says "S13/S14"; §2 + HANDOFF say S15 -> block -> S16. Using the latter.)

## C. Figure transfer (cnn_sbi/talk_figures -> talks/assets/...)

Rule: **figures shown via `<img>` must be raster** (`<img src=*.pdf>` does not render in Chrome/Firefox).
Part-2 figures already ship `.png` twins -> use those. Part-1 figures are PDF-only -> **rasterize with
`gs -r200 -sDEVICE=png16m`** (only `gs` is available; no pdftoppm/convert/inkscape). Copy the source PDF too
(archival/PDF-export quality). Then run `python3 tools/check-asset-links.py` and update `docs/asset-map.tsv`.

| source (talk_figures/) | dest under assets/ | `<img>` uses | slide |
|---|---|---|---|
| p1_setup_nz_bins.pdf | figures/statistics/ | png (gs) | S3/S4 |
| p1_methods_tomo_maps.pdf | figures/maps/ | png (gs) | S4 |
| p1_baryon_impact_ps.pdf | figures/statistics/ | png (gs) | S4 (fold) |
| p1_baryon_impact_l1.pdf | figures/statistics/ | png (gs) | S8 support |
| p1_bias_vs_survey_area.pdf ★ | figures/statistics/ | png (gs) | S7 |
| p1_PSvsHOS_safe_scales.png ★ | figures/statistics/ | png (native) | S8 |
| p1_l1_constraints_vs_area.pdf | figures/statistics/ | png (gs) | S8 backup |
| p1_bnt_kernels.pdf | figures/statistics/ | png (gs) | S9 |
| p1_maps_before_noisy.pdf / _after_bnt_noisy.pdf | figures/maps/ | png (gs) | S9 |
| p1_BRIDGE_bnt_inflates_l1.pdf ★ | figures/posteriors/ | png (gs) | S9, S18 |
| p2_pipeline_schematic.{pdf,png} ★ | diagrams/ | png | S10 |
| p2_methods_flatsky_inputs.{pdf,png} | figures/maps/ | png | S1 backdrop / S10 |
| p2_methods_l1_vs_cosmology.{pdf,png} | figures/statistics/ | png | S6/S10 (fold) |
| p2_M1_matched_nde.{pdf,png} ★ | figures/statistics/ | png | S12 |
| p2_M1_corner_matched.{pdf,png} | figures/posteriors/ | png | S12 (opt) |
| p2_M1_nde_matrix.{pdf,png} | figures/matrices/ | png | S12 backup |
| p2_M1_calibration_tarp/sbc.{pdf,png} ★ | figures/statistics/ | png | S13 |
| p2_M2_cross_deleaking{,_nofullsphere}.{pdf,png} ★ | figures/statistics/ | png | S14 |
| p2_M3_bnt_inflation.{pdf,png} ★ | figures/statistics/ | png | S15 |
| p2_M3_corner_bnt_4way / _l1_collapse.{pdf,png} | figures/posteriors/ | png | S15 (opt) |
| p2_M3_calibration_tarp/sbc.{pdf,png} | figures/statistics/ | png | S15 calib |
| p2_M3_bnt_whitening.{pdf,png} ★ | figures/statistics/ | png | S16, S18 |
| backups: p2_M1_summary_embedding, p2_saliency_cnn, p2_M1_fom3_distribution, p2_M1_violin_fom3, p2_M1_stitched, p2_reliability_tarp_sbc | statistics/ posteriors/ maps/ | png | backup pile |

**Reuse in place (already in repo assets):** Illustris video `videos/illustris_movie_cube_sub_frame.mp4`
(S4); `figures/statistics/NDE.gif` (S11); LAM "Summary Statistics"/peaks/starlet assets (S5/S6);
LAM `_dark` Part-1 figures are NOT used (dark; this is a light deck).

## D. Slide-by-slide map (S1-S19 + block); ★ = carries the talk; (fold) = trim beat

| # | assertion-title (from §2) | disposition | asset |
|---|---|---|---|
| S1 | Title: Do Baryons Break HOS? | title-card | kappa backdrop (opt) |
| S2 | Everyone optimizes statistics; 2pt camp distrusts the contours | **build** | skeptic cartoon + trust checklist |
| S3 | Optimal statistics studied; optimal *tomography* not | **build** | n(z)+overlapping-kernels SVG |
| S4 | Stage IV is systematics-limited | reuse | p1_methods_tomo_maps + Illustris video (+P(k) fold) |
| S5 | Wavelet peak counts | **build** | starlet decomposition + SNR peaks (LAM assets) |
| S6 | The l1-norm uses the whole distribution | **build** | l1 definition/histograms (+l1_vs_cosmology fold) |
| S7 ★ | Baryonic bias scales with survey area | figure | p1_bias_vs_survey_area |
| S8 ★ | HOS resilient AND ~3x on safe scales | figure | p1_PSvsHOS_safe_scales (+baryon_impact_l1) |
| S9 ★ | The BNT bridge: it breaks HOS (the hinge) | figure | p1_bnt_kernels + before/after maps + BRIDGE_bnt_inflates_l1; name Vinciguerra 2026 |
| S10 | The comparison, done fairly | figure | p2_pipeline_schematic |
| S11 | Neural compression: MSE -> VMIM | **integrate** | neural_summaries.* (+NDE.gif) |
| S12 ★ | l1 almost reaches the optimal CNN (~7%) | figure | p2_M1_matched_nde (+corner_matched fold; referee aside fold) |
| S13 ★ | Can we trust it? | figure | p2_M1_calibration_tarp + _sbc |
| S14 ★ | Where the cross-bin info lives (M2) | figure | p2_M2_cross_deleaking |
| S15 ★ | BNT revisited (M3 quant) | figure | p2_M3_bnt_inflation |
| block | BNT-intuition animation (~4-5 min) | **integrate** | bnt_explainer.* (cloud, mechanism, twopoint) |
| S16 ★ | The clincher: a frame artifact | figure | p2_M3_bnt_whitening; close Vinciguerra loop |
| S17 | Is the +7% worth it? (-> round table) | **build** | cost/benefit balance |
| S18 ★ | One story: the optimal tomographic strategy | figure | BRIDGE_bnt_inflates_l1 + p2_M3_bnt_whitening pair |
| S19 | Takeaways and what's next | text | summary; honesty/systematics-humility/21cm nods |

## E. Build-in-deck assets (HTML/CSS/SVG, Preprint tokens; Wong hex only for method identity)

S2 skeptic cartoon + 9-item trust checklist (highlight: systematics, limits, validation/null, simplicity;
mark covariance + Gaussian-likelihood as "SBI removes for free"). S3 n(z) bins + broad overlapping lensing
kernels (callback at S9). S5 starlet decomposition + peaks-per-SNR. S6 l1 = sum|coeff| in SNR bins
(peaks+voids). S17 balance scale (7% bar vs cost: arch search, 324k maps, TARP/SBC-escaping traps; BNT as the thumb).

## F. Conventions

- **Honesty flags travel onto slides** (§4): M1 = ~7% matched-NDE population (NOT +15%); M3 0.26x/0.96x,
  whiten 1.06x; CNN+BNT->baryon-robust is **forward-looking**; Paper I and II kept as separate scopes;
  marginals shown with every FoM3; historical inflated numbers appear only as "the journey" on S17.
- **No em-dashes** in slide text; arrows ok. **Wong** method colours literal; theme chrome via tokens.
- **Trim path**: full version built; `(fold)` beats wrapped in `<!-- TRIM-FOLD ... -->` comments;
  parked drafts use `data-visibility="hidden"`. Cuts to ~16 slides per §2 intro.
- **Back-pressure each step**: preview at `http://localhost:8000/NonGaussian_Universe_2026/`, confirm
  figures render in-browser AND in `?print-pdf`, run `check-asset-links.py`, grep for em-dashes.

## G. Decisions (LOCKED by Andreas, 2026-06-15)

1. **PDF-in-`<img>`: trusted.** Reference `.pdf` figures directly, no rasterization. (`gs` fallback held
   in reserve if a figure fails to render in preview; I verify in-browser as back-pressure.) This
   simplifies transfer to a plain copy of the figure files.
2. **Title backdrop: particles animation** (`background.html`, the standard deck look).
3. **S3 tomography viz: build fresh** as an SVG/CSS component, using `p1_setup_nz_bins` for the real n(z) shapes.
4. **Backups: main-line + `(fold)` figures now**, rest of the backup pile on request.
