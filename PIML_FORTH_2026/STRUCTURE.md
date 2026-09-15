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

## Running order — 26 frames (revised 2026-09-15: the questions on the chain, the taxonomy drawn, the phase demo, the open questions on the chain)

`src` = the frame in `../PhD_Defense_2026/` (as numbered on 2026-09-14) the slide was lifted from.

### Act 0 — the problem · frames 1–5

| # | on screen | src |
|---|---|---|
| 1 | title | 1, retitled |
| 2 | Foreground mass deflects the light of background galaxies and distorts their images | 5 |
| 3 | We measure a noisy, masked distortion field. The image we want is the projected mass | 9, retitled, block titles tagged |
| 4 | Euclid: mapping the dark Universe (billions of galaxies, a third of the sky, an algorithms problem) | 6 |
| 5 | The analysis chain from galaxy shapes to parameters, and where the learning goes: the two questions arrive as the two click-cards under the flowchart (process boxes sub-labelled *inverse problem / feature extraction / likelihood-free*) | 7, cards rewritten |

### Part 1 — learning the prior · frames 6–16 · one vertical column

| # | on screen | src |
|---|---|---|
| 6 | Part 1 card, *Learning the prior*: both papers, pipeline lit at maps | 8 + 21, merged |
| 7 | In practice, mass mapping is an ill-posed inverse problem | 12 |
| 8 | Kaiser–Squires inversion is exact for complete, noiseless data, but amplifies the noise | 13 |
| 9 | Every mass-mapping method minimises a data term plus a regulariser that encodes the prior (card row restored: no prior / ℓ2 / ℓ1 / both / learned) | 14 |
| 10 | The simulations, statistic and likelihood are fixed, and only the mass-mapping method varies | 17 |
| 11 | The sparse solver reconstructs the map 4 % better, and constrains the parameters 157 % better | 19, retitled |
| 12 | Four ways to put a network in a linear inverse problem, **drawn**: four block diagrams in one vocabulary (grey physics step, blue network, dashed box around what is trained together, a loop where there is one) | **new**, replaces 22 |
| 13 | Plug-and-play: a learned denoiser replaces the proximal step (+ lineage source line) | 23 |
| 14 | A second network predicts the error, pixel by pixel, from the same simulated pairs: the drawn strip (data → denoiser loop → the map; data → variance network → the σ map), and the objective under it | backup `uq`, **redrawn** |
| 15 | Conformal calibration makes the error bar honest: the three steps drawn as one SVG in the deck's vocabulary, arriving one click at a time (the interval, the sorted scores with the quantile, the widened intervals with the old bar as a dark core), then the guarantee inequality | **new**, split from 14 |
| 16 | PnPMass is as accurate as the fine-tuned networks, with the smallest calibrated error bars | 24 |

### Part 2 — learning the features, or not · frames 17–24 · one vertical column

| # | on screen | src |
|---|---|---|
| 17 | Part 2 card, *Learning the features, or not*, pipeline lit at summaries | 37 |
| 18 | Two very different fields can have the same power spectrum; one click swaps to the phase-only / amplitude-only demo | 28 + `2pt-phase-amp_light.png` |
| 19 | Peak counts and the ℓ1-norm are one-point statistics of the wavelet coefficients, scale by scale | 31 |
| 20 | Likelihood-free inference: the posterior is learned from simulator samples, and calibration-tested | 36 |
| 21 | A learned encoder trained to be information-optimal | 39 |
| 22 | The learned encoder is 36 % ahead of the hand-crafted features | 41 |
| 23 | Two routes to the cross-channel information: product channels, or a joint 2-D histogram | 43 |
| 24 | Read the channels jointly, and the hand-crafted ℓ1-norm matches the optimal encoder | 44 |

*Same maps, same flow, both calibrated* (defense 40) left the main line on 2026-09-15 for backup
column 3; its sentence is spoken at the end of frame 21. The tomography flipbook (defense 42,
Justine Zeghal's figure) is hidden in place on Andreas's call: one sentence on frame 22 says the
channels are distance slices that are not independent.

### Close · frames 25–26

| # | on screen | src |
|---|---|---|
| 25 | Three open questions, on the steps where they live: the chain flowchart again, three clicks lighting the map, the reconstruction, and systematics-into-features, one card each | **new**, the workshop hand-off into Q&A |
| 26 | Conclusions: the two questions answered, and the line that joins them | 51, rewritten |

Ends on the conclusions, which stay up through questions. No "thank you" slide.

### Out of the main line, deliberately

- The cosmological frame (defense 2–4): this room needs the observable and the survey.
- MCALens, the three maps, the scale ladder (15, 18, 20): backup column 1.
- The wavelet primer, Bayes, generative modelling, flows (30, 33–35): backup column 3. The room
  has just sat through a wavelet talk and Zeghal covers SBI at 14:00.
- **Baryons, all of Part 4**: backup column 4. Andreas's call (2026-09-14): not really the
  workshop's subject. It survives as one spoken sentence on frame 20 and as the answer to
  "your calibration tests only certify against the simulator".

## Budget

Estimated from the defense's measured beats, trimmed: Act 0 ≈ 4:30, Part 1 ≈ 9:00, Part 2 ≈ 7:50,
close ≈ 1:15 → **≈ 22:35**. The script is measured, not estimated:

```
python3 tools/measure-script.py PIML_FORTH_2026 --wpm 121
```

### Cut ladder, in order

1. frame 23 folded into 26's four-arm build (the auto-only arm is its first frame): −0:30
2. frame 13's table folded into 14's opening sentence: −0:40
3. frame 4 Euclid folded into 3's close: −0:35
4. frame 24's flipbook to three frames: −0:20
5. frame 15 back to backup, its two sentences kept on 16: −1:00

**Never cut**: 8 (the inverse problem); 12's *four per cent against 157*; 14; 16's *smallest
calibrated bars, trained once*; 21's definition of optimal; 26's *a tie, not a win*.

**Planned exit**: end of Part 1 (frame 16), expect 13:30. Behind → take cuts 1 and 4 live.

## Backup — four columns after the divider (frame 28)

| column | holds |
|---|---|
| mass mapping methods | MCALens, the three maps, the scale ladder, the Bayesian view, sparse recovery |
| PnPMass | the denoiser card, the residual variant, the CQR card |
| statistics and inference | wavelets, the phases, classical inference, generative modelling, flows, the TARP/SBC results and explainer, the +24 % cross-bin ablation, the tie per mock |
| baryons, nulling and systematics | the whole of the defense's Part 4, the nulling pair, the systematics card, the outlook |

`python3 tools/list-frames.py PIML_FORTH_2026` prints the current numbering.

## Room cues (spoken, in the script)

- **Lanusse, 10:00**: hybrid physical/ML modelling; his group's score-based mass mapping (Remy+
  2023) is PnPMass's nearest relative. Cue on frame 14, filled in after hearing the keynote. The
  contrast to have ready: posterior sampling with a score model against a fixed-point
  reconstruction with a finite-sample conformal guarantee.
- **Pérez Roncero, 11:30**, wavelet denoising: frame 19 opens with *you have just seen a starlet*.
- **Zeghal, 14:00**, SBI keynote: frame 20 is one slide with a hand-off.
- **Starck and Tsakalides** organise it and sat on the committee this morning.

## Dreaded questions (answers in `SPEAKER_SCRIPT.md`)

1. Why plug-and-play rather than unrolling or a deep-equilibrium model?
2. Convergence with a transformer denoiser?
3. Why a point estimate plus conformal, and not posterior sampling?
4. Marginal coverage is weak.
5. Is the CNN under-trained?
6. Your calibration tests certify against the simulator. What if the simulator is wrong?
7. Does the tie generalise to a richer field?
