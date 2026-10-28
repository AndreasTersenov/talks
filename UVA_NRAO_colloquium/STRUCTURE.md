# STRUCTURE — UVA Astronomy / NRAO colloquium, Thursday 29 October 2026, 45 min talk + questions

**Status: proposal, 2026-10-25, for Andreas's sign-off. No slide has changed for content yet.**
Built against `../docs/TALK-GUIDELINES.md`. The audit behind it is `COLLOQUIUM_ADAPTATION.md`. The
defence's own structure is `../PhD_Defense_2026/STRUCTURE.md`, and this file replaces the copy of it
that came with the fork.

Decided 2026-10-25 (Andreas):

- **Purpose.** Andreas has just joined UVA as a **GECO fellow**. Colloquia are normally given by
  visitors, and a slot opened for the fellows. This one introduces him to the department and to NRAO,
  and shows what he does.
- **Slot.** 45 minutes of talking, then questions.
- **Title**: *Trustworthy non-Gaussian inference for weak-lensing cosmology in the Euclid era*: the
  defence title, with "in the Euclid era" added on 2026-10-26 at Satya's suggestion. It places the
  talk as someone coming from Europe with Euclid work, which should draw a wider room. The analyses
  use Euclid-like simulations, not Euclid data, so the talk promises readiness for Euclid, never
  Euclid results. Both title words still have to be defined early and in plain language (A6), and
  Euclid arrives early, at C5.
- **Depth.** Both halves stay. The mapping half goes *deeper* than in the defence; the cuts come from
  the inference teaching and the defence apparatus, and further cuts are decided at the timed run.
- **No new post-PhD results.** The outlook may point at them later.

---

## The three questions

- **Primary audience.** UVA Astronomy (GECO, his own group: galaxy evolution and cosmology; VITA
  theory; VICO star and planet formation; CMB instrumentation for the Simons Observatory) and NRAO /
  the North American ALMA Science Center. Experts in imaging and in galaxy physics, mostly not in
  weak lensing. Pitch the first third at any astronomer.
- **The one thing they should remember.**
  > How we make a dark-matter map, and how we read it, change the science. Done carefully, the
  > non-Gaussian information gives much tighter constraints, with error bars we can trust.
- **What should be different afterwards.** The department and NRAO know who Andreas is and what he
  brings: imaging and inverse problems with learned priors and guaranteed error bars, statistics
  beyond the power spectrum, simulation-based inference. Someone with one of those problems (an
  imaging problem at NRAO, feedback in GECO, an inference problem anywhere) comes to talk to him.

## ABT

> Euclid and Rubin are measuring the shapes of billions of galaxies, **and** from those shapes we can
> map the dark matter across a third of the sky, **but** the map is an ill-posed inverse problem, and
> the most informative part of the signal is non-Gaussian, at small scales, and tangled up with galaxy
> feedback, **therefore** we built ways to reconstruct the map with honest error bars and to read it
> with statistics that keep what the power spectrum misses, and we measured what survives once the
> feedback scales are thrown away.

## The question slide, revisited

The defence asked one question per paper, on the paper's divider. Keep the device, drop the papers:
the two halves each open on a light divider carrying their two questions in plain words, and the
conclusions answer all four.

| | question | answered at |
|---|---|---|
| **Q1** | Does the way we make the map change the science? | C15–C16 |
| **Q2** | Can we make maps that are accurate, fast, and come with error bars we can trust? | C18–C19 |
| **Q3** | Can a statistic designed by hand keep as much information as a neural network trained to be optimal? | C27–C30 |
| **Q4** | Does that advantage survive once we throw away the scales where feedback acts? | C31–C34 |

## The three takeaways

1. **Reconstruction is not preprocessing.** A map that is 4 % better by the usual fidelity metric gives
   a ×2.6 higher figure of merit (≈ ×1.6 smaller error bars per parameter, see "Numbers").
2. **A learned prior can come with guaranteed error bars**, and does not have to be retrained for
   every survey.
3. **A hand-built multiscale statistic keeps as much as an optimal network**, and its advantage over
   the power spectrum survives cutting the feedback scales.

---

## Running order and budget

Target **~35:00 read-through** at the measured 121 wpm, which delivers at **~38–42 min** (the
defence ran 8–20 % over its read-through). `from` = the frame in the forked deck (`list-frames.py`).

`keep` · `rework` same slide, new words or labels · `merge` · `new` · cuts are listed below the table.

### Introduction · ~4:30 · for any astronomer

| # | slide (assertion headline, draft) | from | min | change |
|---|---|---|---|---|
| C1 | title | 1 | 0:30 | rework: GECO fellow, UVA; the PhD (Crete, CEA, CosmoStat) as one small credit line; no "PhD defense", no supervisor line |
| C2 | This is a map of the dark matter, made from galaxy shapes | 10 (fig) | 0:40 | new: the UNIONS mass map, full-bleed. "Everything after this slide is on simulations, on purpose" |
| C3 | ΛCDM fits everything with six numbers, and we do not know what 95 % of it is | 2, 3 | 0:50 | rework: drop the four-assumption list; name the parameters lensing measures, in words (how much matter, how clumpy, how dark energy behaves) |
| C4 | Foreground mass distorts the images of background galaxies | 5 | 0:50 | keep, plus the noise problem: the distortion is far smaller than a galaxy's own shape |
| C5 | Euclid and Rubin are measuring billions of galaxy shapes | 6 | 0:40 | rework: add Rubin |
| C5b | Euclid has been surveying since 2024, and its first large release is next month | new | 0:40 | new (2026-10-28): a timeline over the Perseus image (launch, survey, Q1, DR1-Foundation in November, DR1 lensing mid-2027, DR2 June 2029, DR3 October 2031; Andreas: the releases in full); click 1, the areas (63 / ~1,900 / ~7,500 / ~14,000 deg²); (the blind-analysis line that was click 1 parked on 2026-10-28, Andreas: it offers the room nothing; a Q&A note now); click 2, not alone: Rubin's LSST began in June 2026, Roman launched in August 2026 (Andreas: option 1 of the extras). Public facts only, months not days (PAPER_FACTS §9). Slide 6 now says "weak-lensing data release, mid-2027". "In Euclid" lines on the HOS-forecast slide (HOWLS) and the SBI slide (the weak-lensing group's simulation-based analyses) |
| C6 | From galaxy shapes to parameters: make the map, then read it | 7 | 1:00 | rework: no paper labels. Define the title's two words here: *non-Gaussian* = the information the power spectrum misses; *trustworthy* = unbiased, error bars that mean what they say |

### Movement I — making the map · ~13:00 · deeper than in the defence

| # | slide | from | min | change |
|---|---|---|---|---|
| C7 | Making the map: Q1, Q2 | 8 | 0:20 | rework: plain divider, no paper title |
| C8 | We measure the shear, but we want the mass map | 9–11 | 1:15 | merge: no derivative equations; one line on *why* κ (peaks and voids need a scalar field) |
| C9 | Kaiser–Squires is exact for complete, noiseless data, but amplifies the noise | 13 | 0:50 | headline back to the defence's (2026-10-27); it comes before the bridge, so the bridge can call it back |
| C10 | Mass mapping is an imaging problem with missing and noisy data, like interferometry | 12 | 1:30 | rework: γ = MPκ + n beside V = SFI + n; the mass-sheet degeneracy as the missing zero spacing. Moved after Kaiser–Squires (2026-10-27): its direct-inverse column is the map just explained, and "add a prior" leads into C11 |
| C11 | Every method is regularised imaging: a data term plus a prior | 14 | 1:00 | keep the one equation; a short walk through the priors (Gaussian, sparse, both, learned), from the parked A1.7 text |
| C12 | MCALens: a smooth Gaussian part plus sparse peaks | 15 | 0:45 | rework: no prox formula. "A gradient step, then a denoising step", in words, because C18 needs it |
| C13 | Does the choice change the science? Hold everything else fixed and find out | 16, 17 | 1:00 | merge |
| C14 | MCALens recovers small-scale structure that the direct inversion smooths away | 18 | 0:50 | keep; "with gap-filling" for iKS |
| C15 | A map that is 4 % better gives a ×2.6 higher figure of merit | 19 | 1:40 | rework: the first corner plot, explained; the parameters in words; "fidelity is not science yield" |
| C16 | The gain comes from the small scales | 20 | 0:35 | keep, shorter: "remember this; it comes back in the last part" |
| C17 | Learned methods are accurate, but must be retrained, and give no error bars | 22 | 0:45 | rework: no table |
| C18 | Plug-and-play: replace the denoising step by a network trained once | 23 | 1:40 | rework: the loop as a picture, no iteration equations. Credit Hubert Leterme here. No radio on screen (2026-10-27); AIRI in the notes, if asked |
| C19 | PnPMass is as accurate as the specialised networks, with the smallest calibrated error bars | 24 | 1:40 | the defence slide, wording kept (Andreas, 2026-10-27); say once what "calibrated" means; conformal in one sentence |

### Movement II — reading the map · ~14:30

| # | slide | from | min | change |
|---|---|---|---|---|
| C20 | Reading the map: Q3, Q4 | 25 | 0:20 | rework |
| C21 | Every lensing cosmology result so far is a power-spectrum measurement | 26, 27 | 0:50 | merge: drop ξ± and C_ℓ notation |
| C22 | Two very different fields can have the same power spectrum | 28 | 0:35 | keep |
| C23 | Wavelets see structure scale by scale, and where it is | 30 | 1:15 | rework: the pictures, not ψ_{a,b} |
| C24 | Peak counts and the ℓ1-norm read the map one wavelet scale at a time | 31 | 1:20 | rework: no ℓ1 formula |
| C25 | We cannot write the likelihood, but we can simulate it | 36 | 1:10 | rework: one sentence on why there is no likelihood (from 33), the flow called "a neural density estimator" |
| C26 | Can a hand-built statistic keep as much as a network trained to be optimal? | 38, 39 | 1:20 | merge: no mutual-information equation |
| C27 | The network wins, by ×1.36 | 41 | 0:35 | keep |
| C28 | Redshift slices see the same structures | 42 | 0:50 | rework: 3–4 steps of the build, not 9 |
| C29 | Reading two slices jointly | 43 | 1:20 | rework: the 2-D histogram picture first; the product maps and the cell-sum formula to backup |
| C30 | Read jointly, the hand-built statistic matches the network, with no training | 44 | 0:45 | keep |
| C31 | Galaxy feedback lives on the same small scales as the non-Gaussian signal | 46 | 2:00 | rework: in GECO's words. "In this building, feedback is the science; in my analysis it is what I cannot model" |
| C32 | Unmodelled feedback biases the result more as surveys grow | 48 | 1:00 | keep |
| C33 | Removing the bias costs the finest wavelet band | 49 | 0:35 | rework: arcminutes, not ℓ_max |
| C34 | On feedback-safe scales the ℓ1-norm still beats the power spectrum by ×1.8 | 50 | 1:15 | keep; say what ×1.8 is (the volume of the error ellipsoid) |

### Close · ~3:00

| # | slide | from | min | change |
|---|---|---|---|---|
| C35 | What I want to do here | 110 | 1:30 | **dropped 2026-10-28** (show the work, do not say it; see Open items). Was: rework: real data (UNIONS, Euclid, Rubin), closing the loop between the halves, feedback as a signal (GECO), learned priors with guarantees for other inverse problems (radio, 21-cm). Collaborators credited here. UVA-specific plans: Andreas, later |
| C36 | Conclusions: four answers, three takeaways, and what to come and talk to me about | 51 | 1:30 | rework. Ends the deck (checklist: end on conclusions, not on future work) |

| block | min |
|---|---|
| introduction | 4:30 |
| Movement I | 13:00 |
| Movement II | 14:30 |
| close | 3:00 |
| **total** | **35:00 read-through → ~38–42 delivered** |

### Candidates for leaving the main line — *not parked yet*

**Decided 2026-10-25 (Andreas): park nothing up front.** Build the new slides and the additions
first, time the talk, and only then decide what to remove or compress. The list below is the
candidate pool for that decision, not a done deal; the budget above assumes it, so until then the
deck runs long.

2 (timeline, merged into C3) · 4 (probes) · 8, 21, 37, 45 (paper dividers) · 17 (merged) · 29
(Ajani forecasts) · 32 (Bayes chain) · 33 (Gaussian likelihood) · 34 (generative modelling) · 35
(normalizing flows) · 40 (the Part 3 pipeline) · 47 (the Part 4 pipeline).

---

## Cut lines (planned exits)

Decided at the timed run on Wednesday, not before. In order:

- **−1:30**: C12 folds into C11 (MCALens becomes one sentence); C16 to backup.
- **−3:00**: also C28 to a single still; C33 merges into C34.
- **−5:00**: also C23 merges into C24; C17 becomes one spoken line on C18.

Never cut: C2, C10, C15, C19, C30, C34, C36.

## Numbers

Every number that reaches a slide is in `PAPER_FACTS.md` with a source line. New entries needed:

- **The UNIONS mass map** (C2): area and galaxy count. Not in the ledger yet.
- **The lensing distortion vs intrinsic shape** (C4): the two sizes, with a source.
- **Rubin** (C5): already ledgered at ~18,000 deg².

**What ×2.6 means: check this before Thursday.** Part 1's figure of merit is (det F)^(1/4) over four
parameters. By the ledger's own scaling, (det C)^(−1/4), it moves like **1/σ² per parameter**, so
×2.57 corresponds to error bars **≈ √2.57 ≈ 1.6× smaller per parameter**. The script's prepared Q&A
answer agrees ("about a factor of one and a half on each parameter"). But `PAPER_FACTS.md` §0 calls it
"like a σ ratio" and derives ×43.6 in inverse volume from that, which by the same scaling should be
2.57² ≈ ×6.6. One of the two is wrong; check the paper's definition of F̃. Parts 3 and 4 use
FoM₃ = 1/√det C, the inverse volume of the 1σ ellipsoid, so their ×1.36 and ×1.8 are **volume**
ratios. To this room "×2.6 tighter" will sound like error bars 2.6× smaller. Say what each number is,
once, out loud.

## The bridges, and how to say them (from `COLLOQUIUM_ADAPTATION.md` §5)

- **C10 only: interferometry.** Andreas, 2026-10-27: one slide makes the connection, then the talk
  draws no more explicit parallels. On it: d = A s + n, visibilities ↔ shear, uv coverage ↔ mask,
  dirty image ↔ Kaiser–Squires. In the notes, for questions only: no zero spacing ↔ the mass-sheet
  degeneracy; where the analogy stops (their gaps are in Fourier space, ours in real space and
  noise-dominated); RESOLVE ↔ Wiener; AIRI ↔ PnPMass (C18 notes); CLEAN without per-pixel errors
  (C19 notes). Radio references checked 2026-10-27: AIRI is Terris, Dabbech, Tang &
  Wiaux 2023, MNRAS 518, 604, its denoiser trained on optical images; the follow-up (Terris, Tang,
  Jackson & Wiaux 2024) found MRI-trained denoisers work about as well.
- **C15: fidelity is not science yield.** 4 % in RMSE, ×2.6 in the figure of merit.
- **C31: feedback is GECO's physics.** Acknowledge it, and offer lensing-as-a-feedback-probe as a
  forward-looking idea in C35, never as a result.
- **C22, C24: the ISM.** Same power spectrum, different fields; the ℓ1-norm as a PDF in the wavelet
  domain.

## Vocabulary rules (from `COLLOQUIUM_ADAPTATION.md` §4)

**calibrated**: kept on C19 (Andreas, 2026-10-27), and said once, aloud, what it means · **convergence** → the mass map (κ named once); the iteration
"settles" · **FoM** → name the quantity once per number · **Stage IV** → Euclid- and Rubin-era ·
**C_ℓ, ℓ_max** → arcminutes · **HOS** → statistics beyond the power spectrum · **baryonic
contamination** → galaxy feedback · method names: Kaiser–Squires, MCALens and PnPMass only.

## Backup, by likelihood for this room

1. PnPMass internals: the denoiser, trained once on white noise (69), the transformer (70), the
   residual variant (71).
2. The conformal calibration in full (72, 73).
3. The parked inference teaching: the Gaussian likelihood (33), normalizing flows (35).
4. The cosmological parameters (59).
5. The other systematics (109).
6. Inpainting (63); wavelets in image processing (78).
7. Coverage tests, TARP and SBC (92, 93).
8. The product cross-maps, and the joint-ℓ1 cell sum (from C29).

## Dreaded questions, for this room

1. **NRAO: "How is this different from AIRI / R2D2?"** The same family, a learned denoiser inside a
   forward–backward loop. What is ours: the spin-2 lensing operator, one network trained once on white
   noise for any noise level and footprint, and conformal per-pixel error bars. **Read AIRI before
   Thursday.**
2. **"Your coverage guarantee holds for the simulations. What does it guarantee on real data?"**
   Exchangeability with the calibration set: if the simulator is wrong, the guarantee does not
   transfer. That gap is exactly what *trustworthy* is about, and it is the outlook.
3. **GECO: "Instead of throwing the feedback scales away, can you measure feedback with them?"** In
   principle, with a simulator in which feedback is a parameter. Not done; say so.
4. **"×2.6 in what?"** See Numbers.
5. **"Does the joint ℓ1-norm still match the network after the feedback cut?"** Untested. Both papers
   run on CosmoGrid with the same setup, so it is a runnable experiment. A scale cut is natural for
   the ℓ1-norm (drop a band) and not for the network (retrain), which runs in our favour.

The defence script's Q&A tier 1 (`SPEAKER_SCRIPT.md`) has prepared answers for the general-audience
questions ("why simulations", "how do you know the ML is not making things up", "what when Euclid
data arrive").

---

## Build order (four days)

| day | work |
|---|---|
| **Sun 25** | this file signed off |
| **Mon 26** | pass 1, mechanical: title slide, dividers, § markers, chain labels, the on-slide vocabulary and numbers; park the cuts. Pass 2: merges and new slides (C2, C10, C35, C36). Ledger entries for UNIONS and C4 |
| **Tue 27** | script rewritten for every changed beat; measure with `tools/measure-script.py`; untimed run-through in the evening |
| **Wed 28** | timed run-through; cut along the planned exits; PDF export; screenshots |
| **Thu 29** | silent click-through a few hours before; talk |

## Open items for Andreas

- **Remind Andreas at the end of the pass:** the on-screen ratio notation, 157 % → ×2.6 (C15, C36)
  and 36 % → ×1.36 (C27). Deferred by him on 2026-10-25, undecided.
- The **×2.6 interpretation** (Numbers).
- **Versions compared, one kept of each** (2026-10-27):
  - C10 radio bridge: **decided 2026-10-27**, the equation slide (#/7/6, after Kaiser–Squires);
    the picture version is gone. Its lensing row is now the PnPMass paper's field (κTNG), not the
    toy simulation.
  - C18 plug-and-play: **decided 2026-10-27**, the loop slide (#/8/2), without its radio click; the
    AIRI plug-in loop is gone. The paper-figure slide with the equations was hidden on 2026-10-28
    (Andreas), leaving the loop alone.
    A fourth click (2026-10-28, Andreas: uncertainty matters, name the method, no details, "happy
    to chat afterwards" said aloud): one extra pass as a row under the loop, a data step from the
    converged map, then a second network (order-2 moment network) in place of the denoiser, giving
    the error of each pixel (the paper's Algorithm 1); the caption names conformal calibration.
    **Open** (2026-10-28): a version 2 right after it (Andreas): click 4, an arrow down from the
    converged map into a second network drawn as a network, then the error map; click 5, conformal
    calibration, then the calibrated result, right to left under the loop, no "extra pass" row
    label and no second data step. The calibrated result is the paper's own appendix panels (the
    CQR bounds minus the true map, blue below and red above): the paper has no calibrated error map
    for this field, and a width map read back from those colours did not reproduce its calibration
    numbers (about 12 % narrower than 2 sigma-hat on this field, against the paper's ~1 % wider on
    average), so none is shown. Refined the same day (Andreas): less text and larger throughout; the
    data step shows the forward model (gamma = M P kappa + n) instead of "operator, mask, noise"; the
    denoiser box reads "trained once on sims" around a small drawn network; the loop's arrows are square
    (tried as one circle first); calibration reads "CQR"; the error map at the bounds' size. Version 1 is left
    as it was. **Decided 2026-10-28: version 2**; version 1 hidden, kept in the file.
  - C19 results: **decided 2026-10-28**, the result plot redrawn as a build (#/8/3), both axes
    relative to DeepMass: accuracy (a number line), the networks' own error bars, calibration (all at
    95 % coverage, with trails), PnPMass smallest, then the card "other deep-learning methods need
    retraining for every new mask and noise level; PnPMass is trained once and applies to any
    configuration". The defence slide (with "smallest calibrated error bars", kept as the title) and
    a three-tiles version are gone (git history).
  - C24 the two statistics: **decided 2026-10-28, the build**; the original hidden, kept in the
    file. Was open (2026-10-27; Andreas feared the l1-norm formula would lose the
    room). The original (#/15) against a copy whose bottom row is a build (#/16), appearing on its own
    click after the starlet row: one starlet band pixel by pixel; then (1) peak counts, the maxima
    ringed and sorted by height; (2) sort: every pixel by value, the band's histogram; (3) weigh: each
    block as tall as |value|; (4) add up: one bar per bin, voids and peaks remain, the l1-norm. The
    formula l1(bin) = sum over the pixels in the bin of |value| types itself a part per step. An
    illustration field (tools/make-l1-sort.py); notes per click, plus P(D) for the radio room if asked.
  - C29 cross-bin (joint l1): **decided 2026-10-27**, two slides: route 1 alone, titled in general
    terms (combine pairs of bins into new maps that encode their cross-bin structure) with the
    product maps as "for example", larger, no caption (#/22/5; convolution maps: notes only), then route 2 as a build (#/22/6). The original two-route slide
    and a one-slide version are gone (git history). The build, in the l1 slide's language
    (tools/make-joint-l1.py, an illustration): one wavelet scale in two tomographic bins; pair (one
    pixel, one point), the joint distribution (correlated), its marginals (the per-bin l1 curves),
    shuffle (bin j permuted: same marginals, no correlation), cells (10 x 10), weigh and add up; the
    formula greys in at the cells and turns black part by part. Wording in distributions and
    marginals, no metaphors (Andreas).
  - C31 feedback: **decided 2026-10-28, the pair**; the original hidden, kept in the file. Was open
    (2026-10-27; Andreas was told to make the video larger). The original
    (#/22/0) against a pair in his order (signal and systematics share scales, then feedback as a
    dominant one, then the questions): the sketch alone, stretched along the scale axis, its dashed
    curve relabelled "systematics", with its two clicks (#/22/1); then a dark slide, the Illustris video at 960 px with a poster
    frame for the PDF, the two questions (Andreas's wording) fading in over its middle on
    semi-transparent cards (#/22/2). The lead line is off the screen in the pair.
  - C32 bias against area: **decided 2026-10-28, the redrawn copy**; the original hidden, kept in
    the file. Was open (2026-10-27; the paper figure's labels were unreadable). The
    original (#/22/4) against a copy with the figure redrawn at slide size (#/22/5): same points, a
    log area axis split into small surveys (< 3 000 deg²), Stage III (to 7 500, DES), Stage IV (to
    20 000, Euclid and Rubin) and beyond (to the full sky); the corner plot beside it larger (370 to
    465 px), and without the "At full sky" bullet (the plot has no full-sky point). Class edges
    confirmed by Andreas (2026-10-27).
  - C36 conclusions: **decided 2026-10-28**, the one-block slide (#/25): six general statements
    over the Euclid field, four with the result of ours that backs it on a smaller line, all on
    screen from the start, the fuller sentences in the notes. The defence's four answers are hidden,
    kept in the file.
  - C17 learned methods: **decided 2026-10-28, the requirements around a mass map** (the true map
    of the loop's field, Andreas: it looks better, and which map does not matter here); the table,
    the cards and the list hidden, kept in the file. Was open (2026-10-28; Andreas: the table is not the best thing, but the talk
    still needs the motivation). The DL table (#/9/0) against a requirements slide after it (#/9/1):
    what a mass-mapping method needs to be used on a survey like Euclid, four cards (accurate, down
    to the small scales; flexible, any mask and noise level without retraining; fast, on the data and
    on thousands of simulations; error bars we can trust, pixel by pixel, calibrated), then on a
    click "No existing method meets all four at once"; which method misses what is in the notes.
    Andreas did not like the cards' look; two more layouts after it, same words and notes: a
    typographic list (large accent keywords, hairlines between rows) and the four requirements
    around a mass map with short leaders.
  - C14, C15 without iKS: **decided 2026-10-28, the copies without iKS**; the originals hidden, kept
    in the file. Was open (2026-10-28; Andreas: iterative Kaiser-Squires only confuses
    the room). Each original followed by a copy without it: the maps as a row of three (truth, KS,
    MCALens), each prior under its own map; the figure-of-merit slide with the corner plot's iKS
    paths deleted from its vector source (6 fills in each red, 10 strokes, the legend entry; the
    MCALens legend row moved up) and the stems redrawn without iKS. The notes keep iKS as a Q&A
    line (same posterior as KS).
- C33, C34 trimmed (2026-10-28, Andreas): the cut slide gives the C_l cut at Euclid's area only
  (ell_max = 460 at 14,000 deg^2, PAPER_FACTS section 4) and the starlet as "the same approach,
  but removing the finest wavelet bands instead of multipoles" (Andreas's wording); the result slide loses "and this is conservative" and keeps
  "better baryon modelling would allow smaller scales, where the gain is larger".
  The result slide's corner plot enlarged (480 to 575 px), same day.
- **Speaker script written (2026-10-28)**, then revised the same day for register (Andreas: no
  claude-isms, nothing cheesy, scientific wording). `SPEAKER_SCRIPT.md` is now the colloquium's (the
  copy of the defence script it replaces is unchanged in `PhD_Defense_2026/`): prose, the defence's
  sentences wherever a slide carried over, new prose for the rebuilt slides. **32:13** read-through
  at 121 wpm against a 36:00 target (Introduction 4:28, Making the map 11:42, Reading the map 10:21,
  Feedback 4:01, Close 1:41); every [CLICK] matches the deck; a cut ladder (short paths −3:57) and
  Q&A for the room. Printable: `SPEAKER_SCRIPT_PRINT.pdf` (`tools/print-script.py`). To confirm with Andreas: the ×2.6 reading (√2.57 ≈ 1.6 per parameter).
- C7, C20 dividers: **decided 2026-10-28, the new versions**; the originals hidden, kept in the file
  (Andreas: the numbered questions are too specific for a colloquium). The new versions have the problem in one line and three topic
  tags: "From noisy, incomplete shear measurements to a map of the matter" (an ill-posed inverse
  problem / priors, hand-crafted and learned / uncertainty quantification) and "From the map to the
  cosmological parameters" (statistics beyond the power spectrum / simulation-based inference /
  small-scale systematics), and no pipeline strip (Andreas).
- **UNIONS map** facts for C2.
- A **UVA / GECO logo** for C1 (not in `assets/logos/` yet).
- **C35 dropped (2026-10-28).** Andreas: no "what I want to do here" slide, and no explicit
  "come and talk to me". The talk positions him as the person at UVA and NRAO to talk to about
  advanced methods, deep learning and astrostatistics by showing the work, not by saying so.
