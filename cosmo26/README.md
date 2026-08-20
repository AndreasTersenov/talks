# COSMO-26 — Leiden, 24–28 Aug 2026 (15 min + 3 Q)

Andreas Tersenov. Forked from `../NonGaussian_Universe_2026/` (FORTH Heraklion, 16 Jun 2026,
~25 min) on 2026-08-19 and being cut down and re-pointed at the current results.

## Read these first

| file | what it is |
|---|---|
| **`PAPER_FACTS.md`** | The number ledger. **No number goes on a slide unless it is in here with a source line.** Both papers are read into it, with an explicit delta against the June deck's now-stale claims. |
| **`STRUCTURE.md`** | The proposed 15-min running order, the time budget, the animation cut, and the open questions. A proposal to argue with — the slide list is **not** settled. |

## Status

- Scaffolded and wired: `reveal.js` submodule hydrated, shared `../assets/` convention enforced
  (the June deck's redundant local `assets/` is gone), shell retitled for COSMO-26.
- **New slides built (2026-08-19):** the backbone proposed in `STRUCTURE.md` §5 now exists as a
  contiguous block right after the title, marked `NEW SLIDES` in `index.html`, styled by
  `new_slides.css`. Charts are inline SVG/CSS — theme-aware and fragment-animatable, no new assets.
- **The June deck is untouched** and follows after the `ACT 0` banner, so the old and new can be
  compared. Nothing has been deleted or hidden yet; the cut pass is still to come, and the old
  slides still carry the stale numbers listed in `PAPER_FACTS.md` §4.4.
- The title slide carries a `TITLE PLACEHOLDER` marker.
- Not yet listed on the repo landing page (`../index.html`); that happens once the title is fixed.

## Preview

From the **repo root**, not from here:

```bash
npm start                    # then open http://localhost:8000/cosmo26/
python3 tools/check-asset-links.py
```

PDF export: `http://localhost:8000/cosmo26/?print-pdf`, then print-to-PDF.

## Anatomy

Standard repo conventions (`../CLAUDE.md`) plus three interactive canvas components carried over
from the June deck. Each is scoped CSS + a reveal-agnostic JS engine attached after
`Reveal.initialize`:

| component | files | standalone preview |
|---|---|---|
| BNT explainer (3 blocks: `cloud`, `mechanism`, `twopoint`) | `bnt_explainer.{css,js}` | `index_parked_bnt_preview.html` |
| Neural summaries (MSE vs VMIM) | `neural_summaries.{css,js}` | `neural_summaries.html` |
| SBI pipeline | `sbi_pipeline.{css,js}` | `sbi_pipeline.html` |
| Tomography flipbook | `tomography.css` | `tomography.html` |

`*_section.html` are the paste-in `<section>` snippets for each. `vendor/katex/` is the deck's
math renderer (used by `index.html`); `vendor/reveal/` backs the standalone previews only.

**Known stale:** `bnt_explainer.js` hardcodes the superseded recovery ladder
`0.15 / 0.22 / 0.93 / 1.06`. Paper II's is `0.16 / 0.24 / 0.72 / 0.96`. See `PAPER_FACTS.md` §4.2.
