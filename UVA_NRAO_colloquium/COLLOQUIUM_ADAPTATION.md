# COLLOQUIUM_ADAPTATION — from the Crete defence to the UVA Astronomy / NRAO colloquium

**Status: proposal, 2026-10-25. Nothing in `index.html` has changed for content yet.** This is the
audit that comes before a new `STRUCTURE.md` (TALK-GUIDELINES §2.7: *keep the chrome, re-derive the
argument*). Decisions for Andreas are in §8; once those are made, `STRUCTURE.md` is rewritten for
this room and slide surgery starts.

Read against: the deck as forked (`a16f748`), the per-frame times in `SPEAKER_SCRIPT.md`,
`../docs/TALK-GUIDELINES.md` §1–3, §5, §8, and `../PhD_Defense_2026/REHEARSAL_FEEDBACK.md`.

---

## 1. The room

What we know (UVA Astronomy department pages and job ads, 2024–25; check the current faculty list):

- **UVA Astronomy**, 20+ faculty. Groups: GECO (galaxy evolution *and cosmology*), VITA (theory),
  VICO (star and planet formation, astrochemistry), VAIL (instrumentation). CMB work is mostly
  instrumentation, for the Simons Observatory.
- **NRAO headquarters and the North American ALMA Science Center** are on the UVA grounds, and many
  NRAO astronomers are adjunct faculty. Interferometric imaging and deconvolution are home turf.

What follows from it:

- **The expertise is bimodal again, but the other way round from the defence.** In Crete, four
  examiners knew the lensing better than the room did. Here almost nobody follows the weak-lensing
  depth. But a large part of the room is expert in the machinery of Movement I: imaging an
  incomplete, noisy linear measurement. And the galaxy-evolution people know the physics Part 4 calls
  a nuisance (AGN and supernova feedback) better than we do.
- So: **teach lensing from scratch, teach inference barely at all, teach imaging by analogy to their
  own.** Astronomers use Bayes and MCMC daily, and SBI is spreading through the field (SED fitting,
  exoplanet retrievals, gravitational waves). Nobody in this room needs the change-of-variables
  formula.
- **Rule of thirds, re-pitched:**

| minutes | pitched at |
|---|---|
| 0–13 | any astronomer: what a dark-matter map is, why it is hard to make, what is at stake |
| 13–27 | astronomers who image or model data: regularised imaging, learned priors, honest error bars, multiscale statistics |
| 27–40 | the few cosmologists (GECO, SO): joint reading of the redshift slices, the feedback cut, then back to the whole room for the close |

---

## 2. What this talk is for (proposed; depends on §8, Q1)

**The one thing** (draft):

> How we turn noisy data into a map, and how we read the map, are scientific choices with a
> measurable cost. With learned priors that come with guaranteed error bars, and multiscale
> statistics, the same data give much tighter answers that we can trust.

It is the defence's one-thing with the thesis taken out of it, and stated so that it is true of
*their* data too.

**ABT** (draft):

> Euclid and Rubin are measuring the shapes of billions of galaxies, **and** from those shapes we can
> map the dark matter across a third of the sky, **but** the map is an ill-posed inverse problem, and
> the most informative part of the signal is non-Gaussian, at small scales, and tangled up with galaxy
> feedback, **therefore** we built ways to reconstruct the map with honest error bars and to read it
> with statistics that keep what the power spectrum misses, and we measured what survives once the
> feedback scales are thrown away.

**Title.** The current one, *Trustworthy non-Gaussian inference for weak-lensing cosmology*, is a
thesis title. "Non-Gaussian" reads as a statement about noise to most of this room. Options:

- *Mapping dark matter, and reading the map: weak lensing as an imaging problem*
- *What is in a dark-matter map? Inverse problems, multiscale statistics and simulation-based inference for weak lensing*
- *Weighing the cosmic web with billions of galaxy shapes*

---

## 3. Where it still reads as a PhD defence

### 3a. On the screen

| frame | what | why it is a defence artefact |
|---|---|---|
| 1 | "PhD defense, University of Crete, 14 September 2026", "Doctoral thesis in Physics", supervisor line, Crete/ICS/CosmoStat logos | the ritual, not the science. Credit collaborators instead, on the slides and in a closing thanks |
| 7 | "the first half: papers 1 and 2", "the second half: papers 3 and 4" | organised by publication |
| 8, 21, 37, 45 | four "Part N" dividers carrying full paper titles, author lists and arXiv numbers | a publication list, read aloud four times. Move the citation to a footer on each result slide |
| 25 | "Parts 1 and 2 were about the mass map. Parts 3 and 4 are about…" | same |
| 17–50 | `§1`…`§4` markers on the headlines | thesis chapter numbering |
| 22 | a 5-method × 4-column comparison table (Wiener, MCALens, DeepMass, DeepPosterior, MMGAN) | positioning the novelty for examiners. Also a table, which TALK-GUIDELINES §5 forbids |
| 40 | the pipeline figure ("most of the work in this paper is in this figure") | shows the labour, not a result |
| 51 | Q1–Q4 scoreboard with ✓ Yes | the committee's four questions. A colloquium closes on takeaways and an outlook |

### 3b. In the script

"thank you to the committee for reading this", "the work I have been doing for my PhD over the past 3
years", "the one we follow in this thesis", "That is what this thesis is about", "our first paper",
"in this paper", "the third question", "our final paper", "This thesis followed the analysis chain…".
All of these turn into present tense and first person: *my work*, *we found*.

### 3c. In the structure, which is the part that matters

`STRUCTURE.md` §0 says it outright. The defence's job was to show that **four papers are one
programme**: "the value the talk adds is the spine, not the content", and "under-running is a failure
mode here, unlike a colloquium". A colloquium inverts both. The room does not care that it was four
papers, it wants to learn something and remember one idea, and finishing early is fine.

What that requirement left in the deck:

1. **Uniform depth.** Every paper gets a full act because a thesis must be covered. A colloquium
   should choose (TALK-GUIDELINES §2.4): two or three things done properly, the rest in a sentence.
2. **Justification depth.** Machinery shown so an examiner can check it: the proximal operator
   (15), the plug-and-play iteration with B = AᵀΣ⁻¹ (23), the Gaussian likelihood (33), the
   change-of-variables formula (35), the mutual-information objective (39), the ℓ1 definition (31),
   the joint ℓ1 cell sum (43). **23 of the 51 main-line frames carry mathematics, and about ten show
   a full equation.** §5.1 of the guidelines says roughly one.
3. **Rigour slides.** "Everything else is fixed" (17, 40) is the right experiment and a defence
   needs it on screen. Here it is one spoken sentence.
4. **No outlook.** The main line ends on the Q1–Q4 board. *What comes next* is backup frame 110,
   and its last line, *"a trained denoiser in a proximal scheme fits any linear inverse problem with
   known noise … 21-cm"*, is the best sentence in the deck for this room, and it is hidden.

---

## 4. What this audience will trip on: vocabulary

Words that mean something else to an astronomer, or something specific to a radio astronomer:

| word in the deck | what the room hears | use instead |
|---|---|---|
| **calibrated** error bars | antenna gain and phase calibration, for half of NRAO | "error bars with **guaranteed coverage**". Define once: 90 % intervals that really contain the truth 90 % of the time |
| **convergence** κ | …and two slides later "iterate until it converges" (15, 23) | call κ "the **mass map**" throughout; the iteration "settles" or "stops changing" |
| figure of merit, FoM₃ | nothing (it is a dark-energy-task-force term) | name the quantity once per number. Part 1's ×2.6 is ≈ ×1.6 smaller error bars per parameter; Parts 3–4's ×1.36 and ×1.8 are volumes of the error ellipsoid. See `STRUCTURE.md`, "Numbers": the ledger disagrees with itself here |
| 157 % (19, 51) vs ×2.6 (script) | two different numbers | **×2.6** everywhere (the ratio policy); ×1.36 for the 36 % |
| Stage IV | nothing | "Euclid- and Rubin-era" |
| C_ℓ, ℓ_max = 860, multipole | CMB people yes, the rest no | angular scale in arcminutes |
| HOS | an acronym | "statistics beyond the power spectrum" |
| Ω_m, σ₈, w₀, h, S₈ | Ω_m and h fine; σ₈ and w₀ vaguely | name them once in words (how much matter, how clumpy, how dark energy behaves). They label every corner plot, and the main line never introduces them (the parameter slide is backup 59) |
| baryonic feedback as "contamination" or "systematic" | to GECO, feedback is the science | say it in their words: AGN and supernova feedback. See §5c |
| Kaiser–Squires, MCALens, iKS, DeepMass, MMGAN, VMIM, MAF, Swin, CQR, TARP/SBC, cosmo-SLICS, CosmoGrid, κTNG | names | §8 of the guidelines: a method name is not an explanation. Say what it does; keep at most three names (Kaiser–Squires, MCALens, PnPMass) |

---

## 5. Bridges to the room

### 5a. Mass mapping *is* interferometric imaging (the big one, for NRAO and ALMA)

The correspondence is close enough to put on one slide, and it changes how half the room hears
Movement I:

| interferometry | weak lensing |
|---|---|
| visibilities, V = S F I + n: incomplete Fourier sampling | shear, γ = M P κ + n: masked, noisy, non-local |
| no zero spacing: the total flux is unconstrained | **mass-sheet degeneracy**: a constant added to κ is unconstrained |
| dirty image: linear, fast, sidelobes | **Kaiser–Squires**: linear, fast, noise and mask leakage |
| tapering or weighting | Gaussian smoothing of Kaiser–Squires |
| CLEAN, MEM, sparsity priors, RML imaging | Wiener, sparse recovery, MCALens: "a data term plus a regulariser" (frame 14 *is* RML) |
| learned denoisers inside forward–backward (AIRI, R2D2) | **PnPMass** |
| CLEAN images come without per-pixel error bars | **conformal per-pixel error bars** (frame 24) |

The "mass-sheet ↔ missing zero spacing" line is a one-sentence aha for this room, and it is exact.

Before any of this reaches a slide, check the radio-side references (Högbom 1974; Cornwell 2008
multiscale CLEAN; Carrillo, McEwen & Wiaux 2012 SARA; Terris et al. 2023 AIRI; Aghabiglou et al.
2024 R2D2), the same way every number goes through `PAPER_FACTS.md`. **The claim that AIRI is
plug-and-play with a learned denoiser is the one to get exactly right.**

### 5b. "Image fidelity is not science yield" (frame 19)

MCALens improves the RMSE of the map by **4 %** and the constraints by **×2.6**. For a room that
judges images by fidelity and dynamic range, that is the most transferable result in the talk: the
metric an imager optimises for is not the metric the science needs. Say it in those words.

### 5c. Feedback is the room's own physics (Part 4)

Frame 46 calls feedback the thing "we cannot model reliably" and treats it as contamination. In this
room it is the subject of half the galaxy-evolution research. Flip the framing for one sentence:
*your signal is my systematic.* The result that the contamination sits in the finest wavelet band is
then also a statement about *where* feedback reshapes the matter distribution. That opens a door
(lensing as a probe of feedback), which has to be flagged as forward-looking, not as a result.

### 5d. Same power spectrum, different fields (frame 28)

For the star-formation and ISM people (VICO) this is a familiar point: turbulence studies use
column-density PDFs and multiscale statistics (Δ-variance, wavelet scattering) for the same reason.
The ℓ1-norm, described in the script as "a PDF of the field in the wavelet domain", will sound
natural to them. The Simons Observatory people know lensing reconstruction from the CMB side.

### 5e. One real map

Everything in the talk is on simulations, deliberately (*What comes next* says so). For a room of
observers, open on the one real-data image the deck has: the **UNIONS mass map** (frame 10, now an
aside). Say plainly and early that the results are simulation studies (TALK-GUIDELINES §8). The
area and galaxy count of that map are **not in `PAPER_FACTS.md` yet**, so they need adding before the
opener can quote them.

---

## 6. Frame by frame

Times are the measured beats from `SPEAKER_SCRIPT.md` (121 wpm read-through). The heading times sum to
**44:47 for frames 1–51**, and a delivery from memory runs 10–20 % longer, so about 49–53 min.

**keep** as is · **rework** same slide, new words or new labels · **merge** fold into a neighbour ·
**cut** to backup (`data-visibility="hidden"`) · **new** does not exist

| # | frame | time | verdict | what changes |
|---|---|---|---|---|
| 1 | title | 0:27 | **rework** | new title, current affiliation, no defence line, no supervisor line |
| — | opener: the UNIONS mass map | — | **new** | "a map of dark matter made from galaxy shapes", plus "everything after this is simulations, on purpose" |
| 2 | timeline | 0:25 | cut or merge into 3 | the room knows it |
| 3 | ΛCDM assumptions | 1:19 | **rework** | drop the four-assumption list; keep "simple, successful, mostly unknown, in tension"; name the parameters lensing measures, in words |
| 4 | probes | 0:16 | cut | |
| 5 | strong vs weak lensing | 0:46 | keep | add the noise problem: the lensing distortion is far smaller than a galaxy's own shape (ledger the numbers) |
| 6 | Euclid | 0:58 | **rework** | add Rubin (NSF/DOE, the US room's survey) |
| 7 | chain | 1:22 | **rework** | "making the map" / "reading the map", no paper labels. Stays the recurring navigation |
| 8 | Part 1 divider | 0:10 | cut | citation moves to 18/19 |
| 9–11 | shear, convergence, potential | 2:17 | **merge** into one | "we measure the shear, we want the mass map, and they are linked exactly"; no derivative equations; one line on *why* κ (peaks need a scalar field, R3's rehearsal question) |
| 12 | ill-posed inverse problem | 0:43 | **rework** | the bridge slide: γ = MPκ + n next to V = SFI + n; mass-sheet ↔ zero spacing |
| 13 | Kaiser–Squires | 1:00 | rework | "the dirty image of lensing" |
| 14 | data term + regulariser | 0:38 | keep | the one equation the room can read; say "regularised imaging" |
| 15 | MCALens + prox | 0:51 | **merge** into 14 or 18 | no prox formula; "gradient step, then a denoising step", in words, because Part 2 needs it |
| 16–17 | the question, the fixed pipeline | 1:26 | **merge** | one slide: "does the choice change the science? Hold everything else fixed and find out" |
| 18 | three maps | 0:57 | keep | "with gap-filling" for iKS |
| 19 | the answer | 1:41 | **rework** | ×2.6 not 157 %; parameters in words; the fidelity-vs-science line (§5b) |
| 20 | scales below 8′ | 0:46 | keep, shorter | seeds Part 4: "the gain lives at small scales; remember that" |
| 21 | Part 2 divider | 0:22 | cut | Hubert Leterme's credit moves onto 23 |
| 22 | DL comparison table | 0:45 | **rework** | no table: "learned methods are accurate, but retrained per noise and mask, and give no error bars" |
| 23 | plug-and-play | 2:04 | **rework** | the loop as a picture, no iteration equations; the radio parallel (AIRI) |
| 24 | accuracy + uncertainty | 1:30 | **rework** | "guaranteed coverage", not "calibrated"; one sentence on conformal (holds even if the network is wrong) |
| 25 | second-half divider | 0:32 | rework | "reading the map", no "Parts 3 and 4" |
| 26–27 | compress; two-point | 1:24 | **merge** | "every lensing cosmology result so far is a power-spectrum measurement"; drop ξ± and C_ℓ notation |
| 28 | same power spectrum | 0:34 | keep | the ISM nod (§5d) |
| 29 | forecasts (Ajani+ 2021) | 0:13 | cut | |
| 30–31 | wavelets; peaks and ℓ1 | 3:08 | **merge** into one or two | pictures, no ψ_{a,b} and no ℓ1 formula; "the starlet was built for astronomical images" (verify) |
| 32–35 | Bayes chain, Gaussian likelihood, generative models, flows | 3:04 | cut | the room knows Bayes and MCMC; "a neural density estimator" is enough said about flows |
| 36 | SBI | 0:48 | keep | the only inference slide: "we can't write the likelihood, we can simulate it" |
| 37 | Part 3 divider | 0:17 | cut | |
| 38–39 | why by hand; the optimal compressor | 1:53 | **merge** | "can a hand-built statistic keep as much as a network trained to be optimal?", no MI equation |
| 40 | pipeline | 0:37 | cut | |
| 41 | the CNN wins by ×1.36 | 0:34 | keep | |
| 42 | tomography build, 9 steps | 1:01 | rework, shorter | 3–4 steps: redshift slices, the same structures lens every slice behind them |
| 43 | two routes | 1:49 | **rework** | the 2-D histogram picture only; product maps and the cell-sum formula to backup |
| 44 | the tie | 0:48 | keep | |
| 45 | Part 4 divider | 0:18 | cut | one spoken transition |
| 46 | collision of scales | 2:13 | **rework** | feedback in the room's words (§5c) |
| 47 | Part 4 pipeline | 0:19 | cut | "same pipeline as before" |
| 48 | bias grows with area | 1:04 | keep | |
| 49 | the cuts | 0:38 | rework | arcminutes, not ℓ_max |
| 50 | still useful? | 1:21 | keep | |
| 51 | Q1–Q4 board | 1:29 | **rework** | three takeaways for this room |
| — | what comes next | — | **new / promote** | from backup 110, rewritten: real data, closing the loop, and the bridge to other inverse problems (radio, 21-cm) |
| — | thanks and collaborators | — | new | Starck, Kilbinger, Leterme, Fadili, Guerrini, Baumont, Pavlidou … |

---

## 7. Budget

Rough targets per block, read-through times:

| block | now | target | how |
|---|---|---|---|
| intro (1–7, + opener) | 5:33 | ~4:30 | cut 2 and 4, compress 3, add the opener |
| making the map, teaching (9–15) | 5:29 | ~3:45 | 9–11 → one slide; 15 into 14; the bridge slide pays for itself |
| does the map matter (16–20) | 4:50 | ~3:45 | 16 + 17 merged |
| PnPMass (21–24) | 4:41 | ~3:30 | no divider, no table, no equations |
| why beyond the power spectrum (25–31) | 5:51 | ~3:45 | 26 + 27, 30 + 31 merged; 29 cut |
| inference (32–36) | 3:52 | ~1:15 | SBI only |
| hand-built vs learned (37–44) | 6:59 | ~3:45 | 38 + 39 merged, 40 cut, 42–43 shortened |
| feedback (45–50) | 5:53 | ~5:00 | divider and pipeline cut |
| close (51 + outlook + thanks) | 1:29 | ~3:00 | outlook added |
| **total** | **44:47** | **~32–34** | about 37–40 min delivered |

That leaves the slack a 45-minute slot needs, and it does it mostly by **merging and cutting slides
that already exist**. The new work is the title, the opener, the bridge slide, the outlook, and the
spoken text for every reworked frame. The figures are almost all reused.

If the slot turns out to be longer than 45 min of talking, the first things to bring back are the
wavelet teaching (30–31 at full length) and the tomography build (42).

---

## 8. Decisions for Andreas

**Answered 2026-10-25; the plan that follows from them is `STRUCTURE.md`.** In short: a GECO fellow
introducing himself to the department and NRAO; Thursday 29 October, 45 min of talking; both halves
kept, with the mapping half deeper, and the cuts taken from elsewhere; no new results yet; the title
stays. Two things above changed as a result. Part 3 is *not* compressed to its headline (§6's verdicts
for 38–44 are softened in `STRUCTURE.md`). And §2's title options are moot.

The original questions:

1. **What is the talk for?** Introducing yourself to the department and NRAO as a new member (then
   the outlook should say what you are doing *here*, and who you would like to talk to), a visit, or a
   job talk? This sets the close and the "what should be different afterwards".
2. **The slot.** Which Thursday (29 October or 5 November)? Is ~45 min the talk alone, or talk plus
   questions?
3. **Depth.** Proposed: Movement I deep (the imaging bridge lands with NRAO), Part 4 deep (feedback
   lands with GECO), Part 3 compressed to its headline (hand-built matches learned). Agree, or a
   different pick?
4. **Post-PhD work.** Anything new since September that should appear, even as one slide?
5. **Title**: one of §2's, or your own.
