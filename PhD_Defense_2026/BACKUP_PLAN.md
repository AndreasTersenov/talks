# The backup section — applied 2026-09-12

Was: 61 frames in one flat right-arrow run, with five divider slides that implied a grouping
nobody had built. Now: **five vertical columns**, the same idiom the main line uses for the
four papers, so Right walks categories and Down walks within one.

| h | column | frames | title card |
|---|---|---|---|
| 25 | Cosmology, ΛCDM and the tensions | 8 | *Earlier intro versions* (existing) |
| 26 | Mass mapping methods | 13 | **new** |
| 27 | Statistics: wavelets, peaks, ℓ1 | 8 | *Method detail* (existing) |
| 28 | Part 3 — learned vs analytical summaries | 13 | *Learned vs analytical…* (existing) |
| 29 | Part 4 — baryons, BNT and scale cuts | 20 | *Do baryons break HOS?* (existing) |

62 backup frames (61 + the new card). Main line untouched: frames 1–51 verified identical.

## How the ambiguous ones were settled

Ten slides read as either Part 3 or Part 4 from their titles. The asset prefixes decide it —
on the main line, `p2_*` figures appear only on Part 3 slides and `p1_*` only on Part 4:

| slide | evidence | column |
|---|---|---|
| *Q1 The joint ℓ1-norm reaches the FoM of the optimal compressor* | `p2_` | Part 3 |
| *Q1 At equal constraining power, the analytical statistic is cheaper* | analytical vs learned | Part 3 |
| *backup We are all optimizing statistics…* | framing for the learned-vs-analytical debate | Part 3 |
| *§3 Cross-bin information: κᵢ×κⱼ gives +24%* | `p2_ablation`, §3 tag | Part 3 |
| *backup Where the ℓ1-norm's constraining power comes from* | `p2_fisher` | Part 3 |
| *backup The ℓ1-norm across cosmologies* | `p2_l1_hist_vs_s8` | Part 3 |
| *backup The data: flat-sky tomographic patches* | `p2_methods_flatsky` | Part 3 |
| *backup The tie per mock observation* | `p2_cp_fom3_bars` | Part 3 |
| *Q2 Without any feedback model…* | feedback = baryons | Part 4 |
| *§4 The channel-mixing CNN is unaffected by the transform* | §4 tag beats the `p2_` asset — the subject is BNT | Part 4 |

## Structural notes

**`PnPMass on residuals` was un-nested.** It was the only *visible* backup section that was
already a vertical stack, and reveal supports two levels only — inside a column its children
would have been depth 3. Its two slides are now siblings in the mass-mapping column.

**The LAM-era lensing pedagogy stays flat and hidden**, at the foot of the file. Two of those
five are themselves vertical stacks, they are all `data-visibility="hidden"`, and they render
as nothing either way, so columning them would have bought nothing and cost the same depth
problem.

## Renumbering

Backup frames all moved; the main line did not. Updated:

| old → new | beat |
|---|---|
| 53 → 54 | A0.4v the two tensions |
| 105 → 65 | A1.8 mass mapping as Bayesian inference |
| 111 → 71 | A2.5 the residual variant |
| 112 → 72 | A2.6 the uncertainty, in full |
| 98 → 78 | A3.5 the phases |
| 64 → 98 | A4.6 nulling, and what goes wrong |
| 65 → 99 | A4.7 the information is recovered by a joint reading |
| 63 → 88 | the Q&A pointer at SPEAKER_SCRIPT.md:1205 |

Done in one pass, since 98 is both an old and a new value. `PROSE_PASS.md`,
`REHEARSAL_FEEDBACK.md` and `# Decisions and history` were left alone — dated records.

## Verified

- 114 rendered frames (113 + the new card); divider at 52; columns 8/13/8/13/20
- frames 1–51 byte-identical to before, checked frame by frame
- `<img>`, `<aside>`, `figcaption`, hidden count, `<script>`, `Reveal.initialize` all unchanged;
  `<section>` tags balanced
- all-fragments height sweep: no main-line frame over 720px; backup frame 58 at 736 is the old
  frame 91, unchanged and pre-existing
- `check-asset-links.py` clean; `measure-script.py` 44:46, cue audit unchanged at four

## One thing left

The Part 3 and Part 4 cards say *"Part 2 of 2"* and *"Part 1 of 2"* — the **papers'** numbering,
which runs opposite to the talk's. In talk order Part 3 comes first, so the columns are right
but the cards read backwards. Retitling them is a one-line change if it bothers you on the day.

---

# Amendment — 2026-09-13

## Four explainer cards added

Andreas asked for backup slides on notions the talk names without explaining, to be built one at a
time as he finds them going through the deck. Four so far, all in the mass-mapping half:

| slide | column | sources |
|---|---|---|
| *Inpainting fills the mask before the inversion, with a sparsity prior in the DCT* | mass mapping methods | Pires et al. 2009 §4.2–4.4 |
| *The denoiser is trained once, on white noise…* | PnPMass | Leterme+ 2026 (A&A 710, A292) |
| *A transformer lets every patch look at every other patch* | PnPMass | thesis `figures/intro/N4_attention.pdf` |
| *Conformal calibration fixes the size of the error bar…* | PnPMass | Romano+ 2019; Leterme+ 2026 §5.2 |

Every fact on them was read out of the primary source rather than reconstructed; the provenance is
in an HTML comment above each section. Two thesis figures were copied into the shared assets
(`attention_vs_convolution`, `unet_encoder_decoder`) and one was drawn for the CQR slide
(`tools/make-cqr-schematic.py`).

## Column 2 split in two

Was: one *Mass mapping methods* column carrying both papers. Now two, so the two papers of the
first half have a column each, matching what the other columns already do for Parts 3 and 4:

| h | column | frames | holds |
|---|---|---|---|
| 26 | Mass mapping methods | 11 | the inverse problem, KS, inpainting, the Bayesian view, Wiener, sparse recovery, MCALens |
| 27 | **PnPMass** (new card) | 7 | the denoiser, the transformer, the residual variant, the uncertainties, CQR, implementation |

The shared mass-mapping vocabulary (KS, Wiener, sparse recovery, MCALens) stays with the first
paper, since that paper is the comparison of exactly those methods.

**119 rendered frames** (was 113 before 2026-09-13). Columns now 8/11/7/8/13/20.

## The script's backup pointers moved

Six insertions shifted every backup frame from 64 on. `SPEAKER_SCRIPT.md` was **not** edited:

| beat | line | says | should say |
|---|---|---|---|
| A1.8 mass mapping as Bayesian inference | 947 | frame 65 | **66** |
| A2.5 the residual variant | 971 | frame 71 | **75** |
| A2.6 the uncertainty, in full | 986 | frame 72 | **76** |
| A3.5 the phases | 1018 | frame 78 | **83** |
| A4.6 nulling, and what goes wrong | 1031 | frame 98 | **103** |
| A4.7 the information is recovered | 1070 | frame 99 | **104** |
| Q&A coverage pointer | 1205 | frame 88 | **93** |

A0.4v (frame 54) is unaffected — it sits before the first insertion.

**Separately stale, and older than this:** line 1276 points the BNT thread at *"backup frames 66–68
and 73–76"*. Those numbers predate the 2026-09-12 column rebuild; the BNT figures are now 103–111.

---

# Amendment — 2026-09-13 (second pass)

## Six cards brought over from `PhD_Day_2025/index_Vilasini.html`

Andreas sent seven screenshots from that deck as candidates. Five were rebuilt, two of those
merged into one; two more were rebuilt from scratch because their content did not survive
checking. All of them keep the explainer-card brief: a notion the talk uses without explaining.

| new card | column | built from |
|---|---|---|
| *Why filter at all, and why the starlet* | statistics | **merges** "Why filter at all?" + "Fourier vs Gaussian vs Starlet" |
| *Gravity makes a one-sided field…* | statistics | "Asymmetry of δ and its imprint on wavelet ℓ1" |
| *Why ℓ1 and not ℓ2 on the wavelet coefficients* | statistics | "Why ℓ1 instead of ℓ2 on wavelet coefficients?" |
| *The PDF and the ℓ1-norm measure the same kind of thing…* | statistics | "PDF vs wavelet ℓ1: differentiability matters" |
| *Does the choice of filter bias the inference?* | statistics | "Does filtering bias inference?", **rebuilt** |
| *Learning the summary instead of fixing it* | learned vs analytical | "Learning optimal filters vs fixed multiscale starlet", **rebuilt** |

### Written in the original author's form

First drafts rewrote these in this deck's prose register and Andreas rejected them twice: too long,
then still not hers. The cards now keep her structure and voice — a bordered block, a bold label, a
colon, an arrow to the consequence, and a closing accent line where she had one. Her titles are kept
verbatim. **Only claims that are demonstrably wrong were changed**, and each change is listed here.

| her text | what it now says | why |
|---|---|---|
| "the ℓ1-norm … is dominated by rare collapsed peaks, **not by the underdense regions**" | "…dominated by rare collapsed peaks; unlike peak counts it still reads the underdense side, in its negative SNR bins" | as written it contradicts the ℓ1 slide two frames earlier, whose selling point is peaks *and* voids |
| "**Noise behaviour**: shape noise is small-amplitude; ℓ2 amplifies it quadratically" | replaced by "**Binning does the work**: ℓ1 is summed per band *and* per SNR bin" | shape noise is not small-amplitude in lensing, it dominates |
| "Use **theory-tracked summaries** … with a modelled covariance" / "null tests on Gaussian mocks" | covariance from a finite set of realizations, simulation-based inference, TARP-DRP + SBC | there is no analytic model for the ℓ1 covariance here, and the tests actually run are TARP and SBC |
| "Peter & McQuinn (2016) … MNRAS 475, 894" / "D'Isanto & Polsterer (2018) … A&A 620, A87" | Gupta+ 2018 (PRD 97, 103515), Fluri+ 2018 (PRD 98, 123518), Ribli+ 2019 (Nat. Astron. 3, 93), Jeffrey, Alsing & Lanusse 2021 (MNRAS 501, 954) | the first does not exist; the second is A&A **609**, A111 and is a photometric-redshift paper |

"Reduces mode mixing" was cut from the filtering bullet at one point and restored on Andreas's
call: a wavelet basis does separate the scales well, and *reduces* is the honest verb. The caveat,
that the bands are band-passes and adjacent ones overlap in multipole, sits in the footnote instead.

Also: the stray `©` before "training-dataset dependent" is gone, and *Why filter at all?* and *Fourier
vs Gaussian vs Starlet* are merged into one two-column card, keeping both of her block titles.

### One thing tried and dropped

An intermediate version of the ℓ1-vs-ℓ2 card led on Parseval: the total ℓ2 over a band is exactly
that band's power, so an unbinned ℓ2 returns only C_ℓ. The identity is real — `w_j = ψ_j * I` is a
linear convolution, so it holds per realisation, and it was checked numerically against the à trous
transform on a skewed field, agreeing to twelve digits. Dropped on Andreas's call: nobody in this
lineage motivates ℓ1 that way, and the slide compared an unbinned ℓ2 against an SNR-binned ℓ1,
which is not like-for-like. The card cites Ajani, Starck & Pettorino 2021 instead. Parked here in
case it is ever wanted.

**125 rendered frames** (was 119). Backup columns now 8/11/7/13/14/20.

## The script's backup pointers moved again — this table supersedes the one above

| beat | line | says | should say |
|---|---|---|---|
| A1.8 mass mapping as Bayesian inference | 947 | frame 65 | **66** *(unchanged)* |
| A2.5 the residual variant | 971 | frame 71 | **75** *(unchanged)* |
| A2.6 the uncertainty, in full | 986 | frame 72 | **76** *(unchanged)* |
| A3.5 the phases | 1018 | frame 78 | **84** |
| A4.6 nulling, and what goes wrong | 1031 | frame 98 | **109** |
| A4.7 the information is recovered | 1070 | frame 99 | **110** |
| Q&A coverage pointer | 1205 | frame 88 | **99** |

Line 1276's BNT thread, *"backup frames 66–68 and 73–76"*, now points at **109–117**.

`SPEAKER_SCRIPT.md` was not edited.

## Noticed, not changed

The column-4 divider card is titled *Method detail* and its lead describes Kaiser–Squires, the
Bayesian stack, sparse recovery, MCALens and the PnPMass implementation. That is the content of
columns 2 and 3. Column 4 holds the statistics: wavelets, peaks, the ℓ1-norm, and now the five
cards above. The card needs a new title and lead.
