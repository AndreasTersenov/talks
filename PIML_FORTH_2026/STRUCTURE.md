# STRUCTURE — PIML Workshop, FORTH, Heraklion · 16 September 2026 · 25 min + 5 Q

Wednesday 16 September, **12:00–12:30**, listed in the programme as *Machine Learning for
Non-Gaussian Weak-Lensing Cosmology*. Built on 2026-09-14 (the day of the defense) from
`../PhD_Defense_2026/`, against `../docs/TALK-GUIDELINES.md` §3.2. Numbers trace to
`PAPER_FACTS.md`, which points at the defense ledger.

**Script target: 22:00 at 121 wpm** (the rate measured at the defense rehearsals). Delivered from
memory that lands near 25.

---

## The room

The programme, from the workshop page's programme PDF. Wednesday is the astro day:

| | |
|---|---|
| 10:00 | keynote, F. Lanusse, *ML + physical modelling for cosmological surveys* |
| 11:30 | Pérez Roncero, *2D-1D wavelet denoising of JWST IFU data for lens galaxy dynamics* |
| **12:00** | **Tersenov** |
| 14:00 | keynote, J. Zeghal, *SBI and generative models for cosmology* |

Thursday is Earth observation, Friday medical imaging and Daley on agentic engineering.
Organisers: Starck, Tsagkatakis, Tsakalides, De Santis, Papale. Listed topics: physics-informed and
hybrid AI for inverse problems, unrolling, neural operators, generative models and learned priors
for imaging, Bayesian inference and UQ in physics-constrained learning.

So: cosmologists **plus** signal processing, computer science, Earth observation and medical
imaging. The TITAN/FORTH people have seen the mass-mapping story twice (2024, 2025). Pitch the
first third at a signal-processing person; the shared vocabulary is *data term + regulariser,
proximal operator, learned prior, calibration*.

## The three questions

**Primary audience.** An ML / inverse-problems person who has never heard of weak lensing.

**The one thing to remember.**
> Learn only what the physics cannot supply, the prior rather than the operator, and certify it.
> Done that way a plug-and-play reconstruction with conformal error bars is as accurate as a
> network trained end to end for one configuration and never needs retraining; and a hand-crafted
> wavelet feature vector carries as much information about the parameters as a learned encoder
> trained to maximise it.

**What should be different afterwards.** That "we used a neural network" is heard as a claim with
a benchmark to beat and a guarantee to attach. That the inverse-problems people recognise their
own machinery in a cosmology pipeline. That they read the PnPMass and joint-ℓ1 papers.

## ABT

> Next-generation galaxy surveys will measure a non-Gaussian field at percent precision, **and** the
> pipeline that turns the measured images into a few physical parameters (a linear inverse
> problem, a feature extractor, an inference step) is increasingly built out of learned
> components, **but** a component learned from a simulator can bias the answer or discard
> information without any internal check noticing, **therefore** we learn only what the physics
> cannot supply, benchmark every learned step against the best hand-crafted alternative, and attach
> a calibration guarantee to it.

---

## The translation layer

*"We are not talking to cosmologists anymore"* (Andreas, 2026-09-14). The rule for every slide and
every beat: **name the object in the room's vocabulary first, then attach the cosmology word
once.** The glossary the script is written in is at the head of `SPEAKER_SCRIPT.md`. The physics
that stays: one picture of lensing, one sentence on what the map is, one on the survey. Nothing
about ΛCDM, tensions, or probes.

Analogies the room owns, and none invented: image reconstruction from a masked noisy linear
measurement; plug-and-play, cited on the slide from the paper's own references; hand-crafted
features against learned representations; correlated channels and their marginals; the information
is in the Fourier phases.

---

## Running order — 28 frames (revised 2026-09-15: the questions on the chain, the taxonomy drawn, the phase demo, the open questions on the chain; the tomographic block added; refocused: Euclid and the 2025 experiment out, the residual variant and the nulling in)

`src` = the frame in `../PhD_Defense_2026/` (as numbered on 2026-09-14) the slide was lifted from.

### Act 0 — the problem · frames 1–5

| # | on screen | src |
|---|---|---|
| 1 | title | 1, retitled |
| 2 | Foreground mass deflects the light of background galaxies and distorts their images | 5 |
| 3 | We measure a noisy, masked distortion field. The image we want is the projected mass (Euclid in one spoken sentence) | 9, retitled, block titles tagged |
| 4 | Shear and convergence are both second derivatives of the lensing potential: the figure, and the operator P defined in Fourier space, the symbol every later equation uses | 11, **lifted** 2026-09-15 (Andreas: define P before the inverse problem) |
| 5 | The analysis chain from galaxy shapes to parameters, and where the learning goes: the two questions arrive as the two click-cards under the flowchart (process boxes sub-labelled *inverse problem / feature extraction / likelihood-free*) | 7, cards rewritten |

### Part 1 — learning the prior · frames 6–19 · one vertical column

| # | on screen | src |
|---|---|---|
| 6 | Part 1 card, *Learning the prior*: three papers, pipeline lit at maps | 8 + 21, merged |
| 7 | In practice, mass mapping is an ill-posed inverse problem | 12 |
| 8 | Kaiser–Squires inversion is exact for complete, noiseless data, but amplifies the noise | 13 |
| 9 | Every mass-mapping method minimises a data term plus a regulariser that encodes the prior (card row restored: no prior / ℓ2 / ℓ1 / both / learned; the 2025 result in one spoken sentence) | 14 |
| 10 | Four ways to put a network in a linear inverse problem, **drawn**: four block diagrams in one vocabulary (grey physics step, blue network, dashed box around what is trained together, a loop where there is one) | **new**, replaces 22 |
| 11 | Plug-and-play: a learned denoiser replaces the proximal step (+ lineage source line) | 23 |
| 12 | A variant with more physics in: a Wiener filter takes the Gaussian part, the loop runs on the residual: the paper's build figure (two states), then the 0.5 % line | backup residuals, **promoted** |
| 13 | A second network predicts the error, pixel by pixel, from the same simulated pairs: the drawn strip (data → denoiser loop → the map; data → variance network → the σ map), and the objective under it | backup `uq`, **redrawn** |
| 14 | Conformal calibration makes the error bar honest: the three steps drawn as one SVG in the deck's vocabulary, arriving one click at a time (the interval, the sorted scores with the quantile, the widened intervals with the old bar as a dark core), then the guarantee inequality | **new**, split from 14 |
| 15 | PnPMass is as accurate as the fine-tuned networks, with the smallest calibrated error bars | 24 |
| 16 | Slice the sources by distance: six correlated channels, each measured with a sixth of the galaxies, **drawn**: the six maps of one field (the joint reconstruction: the exported truths turned out to be the nulled ones, see `PAPER_FACTS.md`), then on a click the six measurements | **new** (Leterme, Tersenov & Starck, in preparation) |
| 17 | Nulling: a fixed, invertible re-mixing of the channels makes each one local in distance, **drawn**: the lens-efficiency curves at full width, nested, then on a click local, with the lower-triangular matrix beside them and the why / the price under them | **new** |
| 18 | One multichannel denoiser in the same loop, **drawn**: the per-channel way (six loops, nothing shared) against the joint way (one six-channel image, a block-diagonal data step, one denoiser six in six out), then the iteration with P block-diagonal | **new** |
| 19 | Joint reconstruction wins in every channel, and it is the only one that survives the foreground nulling, **drawn**: error per channel before, the re-mixing as a compact reminder, error after with the per-channel line leaving the chart above the zero map; then, as a card over the chart, four maps of the nearest channel | **new** (values parsed from the draft's Fig. 4b) |

### Part 2 — learning the features, or not · frames 20–27 · one vertical column

| # | on screen | src |
|---|---|---|
| 20 | Part 2 card, *Learning the features, or not*, pipeline lit at summaries | 37 |
| 21 | Two very different fields can have the same power spectrum; one click swaps to the phase-only / amplitude-only demo | 28 + `2pt-phase-amp_light.png` |
| 22 | The ℓ1-norm is a one-point statistic of the wavelet coefficients, per scale and amplitude bin: the formula, then on a click the schematic data vector, one curve per scale (the peaks column dropped and the shape figure hidden for the defense restored, 2026-09-15, Andreas: the ℓ1 alone) | 31 |
| 23 | Likelihood-free inference: the posterior is learned from simulator samples, and calibration-tested | 36 |
| 24 | A learned encoder, trained jointly with the flow to maximise the mutual information I(t; θ): the objective written as the variational bound it is, the boxes naming ResNet-18, d = 10 and RealNVP, the explainer's captions in the same terms (2026-09-15, Andreas: this room can take it) | 39, reworded |
| 25 | The learned encoder is 36 % ahead of the hand-crafted features | 41 |
| 26 | Two routes to the cross-channel information: product channels, or a joint 2-D histogram | 43 |
| 27 | Read the channels jointly, and the hand-crafted ℓ1-norm matches the optimal encoder | 44 |

*Same maps, same flow, both calibrated* (defense 40) left the main line on 2026-09-15 for backup
column 3; its sentence is spoken at the end of frame 24. The tomography flipbook (defense 42,
Justine Zeghal's figure) is hidden in place on Andreas's call: frame 16 now shows the six channels
of one field, and frame 25 names the gap outright: the ℓ1-norm is per channel and never sees the
cross-bin structure shown on frame 16.

### Close · frame 28

| # | on screen | src |
|---|---|---|
| 28 | Conclusions: three claims, one line each (the prior learned and the physics kept; hand-crafted can match learned; learn only what the physics cannot supply), no restated questions (2026-09-15, Andreas: the earlier version was too verbose) | 51, rewritten twice |

Ends on the conclusions, which stay up through questions. No "thank you" slide.

### Out of the main line, deliberately

- The cosmological frame (defense 2–4): this room needs the observable and the survey.
- **The open-questions frame** (the chain with three cards): hidden in place on 2026-09-15, Andreas's
  call, no spoken trace; the three answers stay in the script's Q&A.
- **Euclid (defense 6) and the 2025 experiment pair (defense 17, 19)**: hidden in place on
  2026-09-15, Andreas's call, to keep the talk on the method. Each survives as one spoken
  sentence, on frames 3 and 9.
- MCALens, the three maps, the scale ladder (15, 18, 20): backup column 1.
- The wavelet primer, Bayes, generative modelling, flows (30, 33–35): backup column 3. The room
  has just sat through a wavelet talk and Zeghal covers SBI at 14:00.
- **Baryons, all of Part 4**: backup column 4. Andreas's call (2026-09-14): not really the
  workshop's subject. It survives as one spoken sentence on frame 23 and as the answer to
  "your calibration tests only certify against the simulator".

## Budget

Estimated from the defense's measured beats, trimmed: Act 0 ≈ 4:30, Part 1 ≈ 9:00, Part 2 ≈ 7:50,
close ≈ 1:15 → **≈ 22:35**; the tomographic block (frames 16–19, 2026-09-15) adds about 4:15 on
top of a script that already measured 23:23, and the refocus of the same day (Euclid and the 2025
pair out, the residual variant in) gives back about 1:30. The cut ladder below is no longer
optional. The script is measured, not estimated:

```
python3 tools/measure-script.py PIML_FORTH_2026 --wpm 121
```

### Cut ladder, in order

1. frame 25 folded into 27's four-arm build (the auto-only arm is its first frame): −0:30
2. frame 10, the four ways, to one sentence at the top of 11: −1:00
3. frame 12, the residual variant, to one sentence at the end of 11: −0:40
4. frame 24's *why not learn the compression* to one sentence: −0:20
5. frame 14 back to backup, its guarantee sentence kept on 15: −0:55
6. the tomographic block as a whole (frames 16–19), one sentence at the end of 15: −4:00

**Never cut**: 7 (the inverse problem); 11; 15's *smallest calibrated bars, trained once*; 19's
*worse than the zero map* if the block is in; 24's definition of optimal; 27's *a tie, not a win*.

**Planned exit**: end of Part 1 (frame 19), expect 17:00. Behind → take cuts 1 and 4 live.

## Backup — four columns after the divider (frame 30)

| column | holds |
|---|---|
| mass mapping methods | MCALens, the three maps, the scale ladder, the Bayesian view, sparse recovery |
| PnPMass | the denoiser card, the CQR card; the tomographic extension: the theory card (convergence with masks, the error bound, the step size), the maps after the nulling, the draft's two figures |
| statistics and inference | wavelets, the phases, classical inference, generative modelling, flows, the TARP/SBC results and explainer, the +24 % cross-bin ablation, the tie per mock |
| baryons, nulling and systematics | the whole of the defense's Part 4, the nulling pair, the systematics card, the outlook |

`python3 tools/list-frames.py PIML_FORTH_2026` prints the current numbering.

## Room cues (spoken, in the script)

- **Lanusse, 10:00**: hybrid physical/ML modelling; his group's score-based mass mapping (Remy+
  2023) is PnPMass's nearest relative. Cue on frame 11, filled in after hearing the keynote. The
  contrast to have ready: posterior sampling with a score model against a fixed-point
  reconstruction with a finite-sample conformal guarantee.
- **Pérez Roncero, 11:30**, wavelet denoising: frame 22 opens with *you have just seen a starlet*.
- **Zeghal, 14:00**, SBI keynote: frame 23 is one slide with a hand-off.
- **Starck and Tsakalides** organise it and sat on the committee this morning.

## Dreaded questions (answers in `SPEAKER_SCRIPT.md`)

1. Why plug-and-play rather than unrolling or a deep-equilibrium model?
2. Convergence with a transformer denoiser?
3. Why a point estimate plus conformal, and not posterior sampling?
4. Marginal coverage is weak.
5. Is the CNN under-trained?
6. Your calibration tests certify against the simulator. What if the simulator is wrong?
7. Does the tie generalise to a richer field?
8. Why the starlet, and why ℓ1 rather than ℓ2?
9. Why not null the foreground on the measurements first?
10. Twenty-four iterations now, against eight before?
11. Could the joint denoiser invent foreground structure from the background channels?
