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
- **Title kept**: *Trustworthy non-Gaussian inference for weak-lensing cosmology*. So both title words
  have to be defined early and in plain language (A6).
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
| C6 | From galaxy shapes to parameters: make the map, then read it | 7 | 1:00 | rework: no paper labels. Define the title's two words here: *non-Gaussian* = the information the power spectrum misses; *trustworthy* = unbiased, error bars that mean what they say |

### Movement I — making the map · ~13:00 · deeper than in the defence

| # | slide | from | min | change |
|---|---|---|---|---|
| C7 | Making the map: Q1, Q2 | 8 | 0:20 | rework: plain divider, no paper title |
| C8 | We measure the shear, but we want the mass map | 9–11 | 1:15 | merge: no derivative equations; one line on *why* κ (peaks and voids need a scalar field) |
| C9 | Mass mapping is an imaging problem with missing and noisy data, like interferometry | 12 | 1:30 | rework: γ = MPκ + n beside V = SFI + n; the mass-sheet degeneracy as the missing zero spacing |
| C10 | The direct inversion is the dirty image of lensing | 13 | 0:50 | rework |
| C11 | Every method is regularised imaging: a data term plus a prior | 14 | 1:00 | keep the one equation; a short walk through the priors (Gaussian, sparse, both, learned), from the parked A1.7 text |
| C12 | MCALens: a smooth Gaussian part plus sparse peaks | 15 | 0:45 | rework: no prox formula. "A gradient step, then a denoising step", in words, because C18 needs it |
| C13 | Does the choice change the science? Hold everything else fixed and find out | 16, 17 | 1:00 | merge |
| C14 | MCALens recovers small-scale structure that the direct inversion smooths away | 18 | 0:50 | keep; "with gap-filling" for iKS |
| C15 | A map that is 4 % better gives a ×2.6 higher figure of merit | 19 | 1:40 | rework: the first corner plot, explained; the parameters in words; "fidelity is not science yield" |
| C16 | The gain comes from the small scales | 20 | 0:35 | keep, shorter: "remember this; it comes back in the last part" |
| C17 | Learned methods are accurate, but must be retrained, and give no error bars | 22 | 0:45 | rework: no table |
| C18 | Plug-and-play: replace the denoising step by a network trained once | 23 | 1:40 | rework: the loop as a picture, no iteration equations. Credit Hubert Leterme here. The radio parallel (AIRI), if verified |
| C19 | PnPMass is as accurate as the specialised networks, with the smallest error bars that keep their coverage | 24 | 1:40 | rework: "guaranteed coverage", never "calibrated"; conformal in one sentence |

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
| C35 | What I want to do here | 110 | 1:30 | rework: real data (UNIONS, Euclid, Rubin), closing the loop between the halves, feedback as a signal (GECO), learned priors with guarantees for other inverse problems (radio, 21-cm). Collaborators credited here. UVA-specific plans: Andreas, later |
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

Never cut: C2, C9, C15, C19, C30, C34, C36.

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

- **C9–C11, C18–C19: interferometry.** Visibilities ↔ shear; no zero spacing ↔ the mass-sheet
  degeneracy; dirty image ↔ Kaiser–Squires; RML imaging ↔ data term + regulariser; learned
  denoisers in forward–backward (AIRI, R2D2) ↔ PnPMass; CLEAN images without per-pixel errors ↔
  conformal error bars. **Verify the radio references** before any of them is on a slide; AIRI above
  all, because it is the likeliest question.
- **C15: fidelity is not science yield.** 4 % in RMSE, ×2.6 in the figure of merit.
- **C31: feedback is GECO's physics.** Acknowledge it, and offer lensing-as-a-feedback-probe as a
  forward-looking idea in C35, never as a result.
- **C22, C24: the ISM.** Same power spectrum, different fields; the ℓ1-norm as a PDF in the wavelet
  domain.

## Vocabulary rules (from `COLLOQUIUM_ADAPTATION.md` §4)

**calibrated** → guaranteed coverage · **convergence** → the mass map (κ named once); the iteration
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
| **Mon 26** | pass 1, mechanical: title slide, dividers, § markers, chain labels, the on-slide vocabulary and numbers; park the cuts. Pass 2: merges and new slides (C2, C9, C35, C36). Ledger entries for UNIONS and C4 |
| **Tue 27** | script rewritten for every changed beat; measure with `tools/measure-script.py`; untimed run-through in the evening |
| **Wed 28** | timed run-through; cut along the planned exits; PDF export; screenshots |
| **Thu 29** | silent click-through a few hours before; talk |

## Open items for Andreas

- **Remind Andreas at the end of the pass:** the on-screen ratio notation, 157 % → ×2.6 (C15, C36)
  and 36 % → ×1.36 (C27). Deferred by him on 2026-10-25, undecided.
- The **×2.6 interpretation** (Numbers).
- **UNIONS map** facts for C2.
- A **UVA / GECO logo** for C1 (not in `assets/logos/` yet).
- **C35**: what you are working on here. Later, as decided.
