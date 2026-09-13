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

**126 rendered frames** (was 119). Backup columns now 8/11/7/14/14/20.

## The script's backup pointers moved again — this table supersedes the one above

| beat | line | says | should say |
|---|---|---|---|
| A1.8 mass mapping as Bayesian inference | 947 | frame 65 | **66** *(unchanged)* |
| A2.5 the residual variant | 971 | frame 71 | **75** *(unchanged)* |
| A2.6 the uncertainty, in full | 986 | frame 72 | **76** *(unchanged)* |
| A3.5 the phases | 1018 | frame 78 | **84** |
| A4.6 nulling, and what goes wrong | 1031 | frame 98 | **110** |
| A4.7 the information is recovered | 1070 | frame 99 | **111** |
| Q&A coverage pointer | 1205 | frame 88 | **100** |

Line 1276's BNT thread, *"backup frames 66–68 and 73–76"*, now points at **110–118**.

`SPEAKER_SCRIPT.md` was not edited.

## Noticed, not changed

The column-4 divider card is titled *Method detail* and its lead describes Kaiser–Squires, the
Bayesian stack, sparse recovery, MCALens and the PnPMass implementation. That is the content of
columns 2 and 3. Column 4 holds the statistics: wavelets, peaks, the ℓ1-norm, and now the five
cards above. The card needs a new title and lead.


---

# Amendment — 2026-09-13 (third pass)

## A physical-scale reference card

Frame 92, at the end of the statistics column: *What an arcminute is worth, in megaparsecs*. Andreas
asked for it so a question about physical scales has an answer with numbers on it, then asked for it
simpler: no per-band breakdown, no wavenumbers, just one table of angular scale against comoving
size with the familiar structures on the same ruler.

| row | where it comes from |
|---|---|
| 1′, 10′, 20′, 1° at z = 0.1 / 0.3 / 0.6 | `tools/make-scale-table.py`, cosmoGRID fiducial Ωm = 0.26, h = 0.6736 |
| galaxy halo, cluster R₂₀₀, σ8 sphere, linear regime, BAO | standard values, not measurements from this thesis |

Two things Andreas caught on reading it, both now fixed:

- **The conversion is redshift-dependent**, and a single dash-range hid that behind what looked like
  a fixed factor. The angular rows are broken out by lens redshift instead, which is also the
  honest way to show the factor-5 spread.
- **The BAO row said 105 h⁻¹Mpc.** That figure comes from papers assuming h ≈ 0.71; with this
  card's h = 0.6736 the sound horizon r_d = 147.09 Mpc is **99 h⁻¹Mpc**.
- **The units were stated three ways** — nowhere in the top half, in the second header for the
  structures, and a second unit inline on the BAO row. The table now declares `comoving size
  [h⁻¹Mpc]` once, in a band spanning the numeric columns, and every number below is in it. The
  147 Mpc lives in the footnote, where it doubles as the worked conversion for any row.

`tools/make-scale-table.py` re-derives the angular rows, so they can be checked rather than trusted.
It also prints the single-source-plane lensing-kernel peaks (z = 0.15, 0.26, 0.36, 0.47 for the four
bins), which is what fixes z_lens = 0.1–0.6 as the interval worth quoting, and the per-band table
from the earlier version of the card, in case the detail is ever wanted back.

The card carries one line of text besides the table: the spread is the lensing geometry, one angular
scale being a factor ~5 in physical size. That is the BNT motivation from the baryonic-feedback
paper's own introduction. The rest sits in the speaker note, including the payoff that feedback
bites below about 1 h⁻¹Mpc, which is the finest band and nothing else, and is why dropping one band
is the whole scale cut.


---

# Amendment — 2026-09-14

## A card explaining TARP and SBC

Frame 101, immediately after the card that shows their results, so the explainer sits next to the
thing it explains. Two columns, one test each.

| claim on the card | source |
|---|---|
| SBC: rank of the truth among posterior samples, uniform if calibrated | Talts, Betancourt, Simpson, Vehtari & Gelman 2018, arXiv:1804.06788 |
| TARP: coverage from the distance to a random reference point, joint, samples only, **necessary and sufficient** | Lemos, Coogan, Hezaveh & Perreault-Levasseur 2023, ICML (PMLR 202), arXiv:2302.03026 |
| rank-histogram shapes: U → too narrow, hump → too wide, sloped → biased | standard SBC diagnostics |
| above the diagonal is conservative | matches this deck's own coverage figure, which plots expected coverage against credibility level |

Four drafts, and the useful record is what Andreas cut each time:

- **Metaphor standing in for a quantity** ("a cloud of possible answers"). Say the quantity.
- **Gesturing at a mechanism without giving it** ("tracks where the truth lands among the posterior
  samples", "the answer comes as a shape"). Either state the mechanism or leave it to the note.
- **Terms of art used as if they were plain** ("compares the coverage achieved with the coverage
  claimed"). The card now never says *coverage*; it says *when the pipeline says 68%, is it right
  68% of the time*.
- **Bullets that carry no information** ("reads one parameter at a time", "tells you that something
  is wrong, not what"). Cut. The first became a block title, where it does work.
- **Cute parallel headings** ("what kind of wrong?" / "wrong at all?"). Read as AI. The headings are
  now *SBC, one parameter at a time* and *TARP, all of them at once*, which state the actual
  difference between the two tests.

What survived is three bullets for SBC (count the samples below the truth; a correct posterior makes
that count equally likely to be anything; pile-ups at the extremes mean the error bars are too
small, in the middle too large) and two for TARP (the same check jointly, via distances to a random
point; and the proof that passing it means the posterior is correct, which the per-parameter test
cannot give). The full mechanics live in the speaker note.

The footnote carries the caveat that both are averages over simulations rather than statements about
the one dataset in hand, which is the same limitation the conformal bounds have. The speaker note
names L-C2ST as the local version, which is already mentioned in the results card's note.

**127 rendered frames.** Backup columns 8/11/7/14/15/20.

## The script's backup pointers, current as of this amendment

| beat | line | says | should say |
|---|---|---|---|
| A1.8 mass mapping as Bayesian inference | 947 | frame 65 | **66** |
| A2.5 the residual variant | 971 | frame 71 | **75** |
| A2.6 the uncertainty, in full | 986 | frame 72 | **76** |
| A3.5 the phases | 1018 | frame 78 | **84** |
| A4.6 nulling, and what goes wrong | 1031 | frame 98 | **111** |
| A4.7 the information is recovered | 1070 | frame 99 | **112** |
| Q&A coverage pointer | 1205 | frame 88 | **100** |

Line 1276's BNT thread now points at **111–119**.


## A cosmological-parameter reference card

Frame 61, at the end of the cosmology column, next to the tensions material. Seven rows: symbol,
a plain gloss, and how much lensing constrains it. Ωm, σ8 and S8 are marked in the verdict column;
w0, h, ns and Ωb are not.

The lead and the footnote carry the *why*, which is the part a question actually wants: κ is a
projection of the matter field, its amplitude goes roughly as σ8 Ωm^0.5, so that combination is
pinned and the two separately are not. S8 ≡ σ8 √(Ωm/0.3) is written the way frame 58 already writes
it. Shape parameters are left to the CMB.

The sensitivity column is the standard picture rather than a measurement from this thesis, and the
card is phrased so. The speaker note carries the follow-ups: why the contour is a banana, that dark
energy enters through both distances and growth, that h/ns/Ωb are priored, and that massive
neutrinos suppress small-scale power so higher-order statistics carry more of that signal than the
power spectrum does.

**128 rendered frames.** Backup columns 9/11/7/14/15/20.

Every pointer in the table above shifts by one again, since the insert is in column 1: A1.8 → 67,
A2.5 → 76, A2.6 → 77, A3.5 → 85, A4.6 → 112, A4.7 → 113, the Q&A coverage pointer → 101, and the
BNT thread → 112–120.


## A card on the systematics beyond baryonic feedback

Frame 129, at the end of the Part 4 column, which is the systematics column. Six rows: name, what
it is, how it is handled. Intrinsic alignments and masks are marked, being the two this thesis
touches.

Taken from the thesis introduction rather than reconstructed:

| row | source |
|---|---|
| intrinsic alignments, photo-z, masks, covariance | `weak-lensing.systematics.draft.tex` and `statistical-framework.systematics-{astro,obs}.draft.tex` |
| shape measurement | `sec:intro-shear-measurement` |
| source clustering | `weak-lensing.tex` l.679, where it is one of the approximations entering the Limber C_κ, stated to hold to sub-percent for Stage IV (Kilbinger 2015) |

**Source clustering is the one to watch.** The thesis lists it as an assumption behind the Limber
projection and does not develop what it does to map-based statistics, so the card claims nothing
about the HOS side. If that matters for the defense it needs a real source, not an extrapolation.

The closing line is the thesis's own argument: all of these act hardest on the small non-linear
scales, which is where higher-order statistics draw their advantage, and every one of them is
better understood for the two-point function. The speaker note carries the II/GI split, why IA is
the open one for HOS (the alignment signal is itself non-Gaussian, so a nuisance amplitude fitted
to the 2-point function says nothing about how it propagates into peaks or the ℓ1-norm), and a
plain answer to "which worries you most".

**129 rendered frames.** Backup columns 9/11/7/14/15/21.


## An outlook card

Last frame of the Part 4 column, after the systematics card: *What comes next*. Six items from the
thesis Perspectives (`chapters/conclusion.tex`, `sec:conclusion-limitations-perspectives`), chosen
as the ones that answer "what would you do next" rather than "what are the caveats":

| near term | further out |
|---|---|
| to data: UNIONS and *Euclid*, each systematic built into the forward model at map level | PnPMass next versions: spherical, tomographic, BNT-aware |
| **close the loop**: PnPMass maps and their pixel uncertainties feeding a higher-order inference, end to end | conditional rather than marginal conformal coverage, so the guarantee holds at the peaks |
| learned maps through the same cosmological pipeline, and what they keep away from their training point | the systematics left out: alignments, source clustering, photo-z, then stress-test peaks, the ℓ1-norm and the compressor |

Written as label + fragment rather than sentences, on Andreas's note that the first version read
as prose. "Conditional, not marginal" went too: it is the X-not-Y pattern he reads as an AI tell,
and the row now just says **Conditional coverage**.

"Close the loop" is marked because the thesis calls it, in those words, *the most direct
continuation of this work*. The footnote is the thesis's closing move: the template is not specific
to lensing, and 21-cm is the interesting case because foreground removal occupies the same slot in
the chain that mass mapping does here.

Left in the thesis and off the card: validating the scale cut against FLAMINGO and marginalising the
BCM parameters, a finer filter bank for area-dependent cuts, the large-deviation-theory cross-check
of the PDF and the ℓ1-norm, and field-level inference as an absolute reference for sufficiency.

## The pointer tables above are superseded by a tool

Andreas is hiding unused backup slides, and every hide renumbers everything after it, so a frame
number written down here is stale within the hour. `tools/list-frames.py` prints the current
numbering instead:

```
python3 tools/list-frames.py PhD_Defense_2026            # every frame
python3 tools/list-frames.py PhD_Defense_2026 phases     # only titles matching
```

It reuses `sync-notes.frame_spans`, so it counts frames exactly the way reveal does, and it reports
how many hidden sections the file holds. Fix the `SPEAKER_SCRIPT.md` backup pointers against its
output once the hiding pass is finished, not against the tables above.


### Cross-correlations with other probes are not in the thesis

Checked, because Andreas thought they were. Every "cross" in the conclusion is cross-**bin** or
cross-**map** — the tomographic channels, not other experiments. The only other-probe material is
the closing paragraph of the Perspectives, where the *methodology* transfers: galaxy clustering
first, 21-cm intensity mapping as the interesting case because foreground removal occupies the same
slot in the analysis chain that mass mapping does here. That is already the card's footnote. The
single hit for "combining probes" is generic framing in `objectifs.tex`, not a proposal.

So a cross-probe item would be a new claim rather than something drawn from the thesis. Worth adding
if he wants it as a defense answer — it is a reasonable next step — but it should be added knowingly.


## Born, Limber, ray tracing

End of the cosmology column, after the parameter card. Three rows, because these get treated as
three points on one axis and they are not: **Born and ray tracing are two ways to turn a simulation
into a map; Limber is an approximation in an analytic prediction.** The lead says exactly that.

| row | source |
|---|---|
| Born: potential read on the unperturbed ray, first order in Φ | `weak-lensing.tex` l.98 (Bartelmann & Schneider 2001) |
| ray tracing: rays deflected plane by plane along the true path, lens–lens couplings kept; post-Born terms on κ well below current errors | `inference.simulations.draft.tex` l.44–51 (Hilbert+ 2009, Kilbinger 2015) |
| Limber: transverse modes only, k = ℓ/f_K(χ), sub-percent at Stage IV scales | `weak-lensing.tex` l.663–682 (Kilbinger 2015) |

The footnote places our own work: CosmoGridV1 sums lens planes along the straight ray, so the maps
are Born — checked against the UFalcon documentation and the CosmoGridV1 paper, since neither of our
papers states it in those words. Limber enters the thesis only where an analytic P_κ is needed, in
the Wiener prior (`weak-lensing.tex` l.1007); every statistic in the talk is measured on maps.
