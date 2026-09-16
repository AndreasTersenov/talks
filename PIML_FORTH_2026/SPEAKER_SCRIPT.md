# SPEAKER_SCRIPT — PIML Workshop, FORTH, 16 September 2026, 12:00

**`[CLICK]`** advance a fragment · **▲** say verbatim · **bold** the anchor to glance at ·
*italic* the word to lean on. Bold and italic mark delivery only.

## The budget

Measured at **121 wpm**, the rate of the defense rehearsals. The slot is **25 + 5**. Delivered from
memory expect two to three minutes more than the script says: slower per word, plus the pauses a
read-through skips.

| act | frames | at 121 wpm |
|---|---|---|
| Act 0 — the setup | 1–5 | 4:30 |
| Part 1 — making the map | 6–19 | 14:56 |
| Part 2 — reading the map | 20–27 | 7:42 |
| Close | 28 | 0:48 |
| | **28 frames** | **27:56** |

> **Over the slot.** The cut ladder at the end says what to drop and what each cut buys. The planned
> exit is the end of Part 1, at about 19:30 on the clock; behind that, take tiers 1 and 2 live.

---

## A0.1 — title · frame 1 · 0:25

Thank you, and good afternoon.

I defended my PhD on this work two days ago, so today you get the short version, adapted for this
room: a weak-lensing pipeline seen as an **inverse problem**, a **feature extractor** and an
**inference** step, and, at each step, where the machine learning should go.

---

## A0.2 — lensing in one picture · frame 2 · 0:42

One picture of the physics.

Light from distant galaxies travels to us through all the matter along the way, most of it dark
matter. Gravity bends its path, so the image arrives distorted. Sometimes that is dramatic: arcs,
multiple images. **▲** But what happens *everywhere* is the **weak** regime: every galaxy behind any
structure has its shape changed, by about a per cent. If we measure the shapes of enough galaxies,
the pattern of distortions tells us how the matter is distributed, dark matter included.

---

## A0.3 — the measurement, and the image we want · frame 3 · 1:04

So here is the problem, in your vocabulary.

The **measurement** is the shear: a distortion field with two components per position. It is
sampled only where there are galaxies, and it is dominated by noise, because every galaxy has its
own intrinsic shape, much larger than the distortion we are after. The lensing is coherent and the
intrinsic shapes are random, so averaging over many neighbouring galaxies cancels the random part
and leaves the shear.

**▲** The **image we want** is the convergence: a scalar map of the projected matter along the line
of sight. We call it the mass map.

And the data are coming: Euclid is measuring the shapes of billions of galaxies over a third of
the sky, and extracting the signal from them is an algorithms problem.

---

## A0.3b — one potential, one operator · frame 4 · 0:47

The two quantities are not independent. Both are second derivatives of the **lensing potential**,
which is a projection of the gravitational potential along the line of sight. So in Fourier space,
one linear operator takes the map to the shear. I call it **P**. It has two components, the two
kernels you see here, and they have unit modulus, so the relation inverts in one line: kappa equals
P one gamma one plus P two gamma two.

**▲** Linear, and exact, for a complete, noiseless field. This P is the operator in every equation
that follows.

---

## A0.5 — the chain, and the two questions · frame 5 · 1:32

Here is the pipeline, reduced to the steps that matter. It is also the map of the talk.

Galaxy shapes go in. From the shapes we make the mass map: that is a **linear inverse problem**.
From the map we extract a feature vector, because a hundred thousand correlated pixels cannot be
compared with theory directly. And from the features we infer a handful of parameters of the
physical model, with a simulator in place of a likelihood.

Every one of these steps can bias the answer or distort the error bars without anything
downstream noticing. And every step is now a place where a network could go.

[CLICK] **▲** Question one, the first half of the talk: in the inverse problem, learn *only the
prior*. Is the reconstruction as accurate as a network trained end to end? Does it work for any
configuration? And can we certify its error bars?

[CLICK] **▲** Question two, the second half: the features. A learned encoder, or hand-crafted
features? Which one extracts more about the parameters, and why? And in both cases, how do we
know: we **benchmark**, we **calibrate**, we **test**.

---
---

# Part 1 — making the map · frames 6–19

---

## A1.0 — the Part 1 card · frame 6 · 0:16

Part 1, making the map. Two papers: one on what the choice of prior does to the science, and one,
led by **Hubert Leterme**, on a learned prior with certified error bars.

---

## A1.1 — the inverse problem · frame 7 · 0:55

The forward model is one line: a known linear operator, a mask, and additive noise.

The relation is exact, but the data are not. The noise is much larger than the signal, and the
direct inversion amplifies it at small scales. The mask removes data, and because the operator is
non-local, a hole leaves whole Fourier modes unconstrained. And a constant added to the map does not
change the data at all.

So the problem is ill-posed in the usual sense. Here are **three visibly different maps**, all
consistent with the same measurement. [CLICK] **▲** To pick one, we need a prior. And the choice of
prior is what distinguishes the methods.

---

## A1.2 — the direct linear inverse · frame 8 · 0:49

The standard method, for thirty years, is the direct linear inverse, **Kaiser–Squires**: apply the
inverse operator in Fourier space. One FFT, no regulariser, no free parameters.

[CLICK] Same field, same mask, left and right. The structure you see on the left is buried on the
right, and the colour bar spans *twice* the range: that extra range is noise. And the mask leaks
across the whole map, because the Fourier transform does not know there is a hole. In practice,
people smooth the result with a Gaussian kernel. That tames the noise, at the cost of the small
scales.

---

## A1.3 — data term plus regulariser · frame 9 · 1:23

Every method after that is a regularised least-squares problem, which you will recognise. A
**data-fidelity term**: the residual against the measured shear, weighted by the noise covariance.
Plus a **regulariser**, which says what a plausible map looks like.

The data term is the same for every method. What changes is the second term. Kaiser–Squires has
none, only the smoothing. Wiener filtering is an **ℓ2 prior**: a Gaussian field with a known power
spectrum. Sparse recovery is an **ℓ1 prior**, in a wavelet basis. MCALens, the state of the art
among hand-crafted priors, models the map as a Gaussian component plus a sparse one, and solves it
with proximal steps. **▲** And deep learning stops assuming, and *learns* the regulariser from
simulations.

This choice is not cosmetic. In our 2025 paper we held everything else fixed and only swapped the
reconstruction method. The sparse solver's map was **four per cent** better than the linear inverse.
The constraining power on the parameters was **a hundred and fifty-seven per cent** better.

---

## A1.6 — four ways to put a network in an inverse problem · frame 10 · 1:25

So the prior matters, and a learned prior is the obvious next step. There are four ways to put a
network in a linear inverse problem, and this room knows all four. Grey is a physics step, blue is a
network, and the dashed box is what gets trained together.

**End to end**: data in, image out, and the physics is only in the training pairs. A new mask or
noise level means retraining. **Unrolled**: physics steps and networks on one rail, trained through
together. It transfers as far as the training covered. **Plug-and-play**: a fixed loop, a data step
and a denoiser, and the dashed box is around the denoiser alone. It is trained once, on its own.
And **posterior sampling** puts the same learned prior inside a sampler: you get the full posterior,
at thousands of passes.

**▲** The two on the right survive a new mask or noise level, because the prior never saw the
operator. Plug-and-play is the cheap one: eight passes. What we add is the error bars.

---

## A1.7 — plug-and-play · frame 11 · 1:47

Here is the iteration. The first line is one step of **forward–backward splitting**, the standard
solver for a data term plus a regulariser, and the solver behind the sparse methods from two slides
ago: a gradient step on the data term, towards the measured shear, then the proximal operator of
the regulariser, which enforces the hand-crafted prior. Plug-and-play keeps the gradient step and
replaces the proximal operator with a **denoiser** trained on simulated maps. The iteration
converges to a fixed point, under the usual non-expansiveness conditions. And the denoiser has
learned a much richer model of a mass map than anything we can write down.

**▲** It is flexible because of *where the physics sits*. The denoiser is a Swin transformer with
seven million parameters. It is trained once, on white Gaussian noise over a range of levels, and it
never sees the operator, the mask or the noise covariance. Those enter only in the gradient step, at
inference time. Nothing is trained through the iteration, so one network serves every
configuration.

Here it is running. The shear comes in, the map is initialised at zero, the **forward step** gives a
noisy map, and the **backward step**, the denoiser, pulls it back onto realistic maps. [CLICK] The
output is fed back, and after eight iterations it has converged.

> Room cue: if François showed score-based mass mapping this morning (Remy et al. 2023), one
> sentence here: *the same kind of learned prior as the sampler you saw this morning, used here as a
> fixed-point reconstruction, with the uncertainty handled next.*

> **Tier-0 short path** (−0:20). Drop the walk-through. After *one network serves every
> configuration*, say only: *Eight iterations of this, a data step and a denoiser, and the map has
> converged.* Then click once.

---

## A1.7b — PnPMass on residuals · frame 12 · 0:45

There is a variant that puts more physics in. The map is a Gaussian component plus a non-Gaussian
one, and the Gaussian part has a closed-form optimum, the **Wiener filter**. So let the Wiener filter
do that part. [CLICK] Subtract its prediction from the data, and run the loop on the residual, with
a denoiser trained on non-Gaussian residuals only. Then add the two back together.

[CLICK] **▲** This variant is within **half a per cent** of the network trained end to end for this
configuration, and it has converged after two iterations.

---

## A1.8 — the second network, and its objective · frame 13 · 1:02

The map is only half of the result. The other half is the error bar.

So the data fan out to two networks. The denoiser, in the loop, gives the map. A **second network**,
trained on the same simulated pairs, gives the error map. Its target is the squared residual of the
reconstruction: the square of the difference between the truth and the map. The minimiser of that
loss is the **posterior variance**, pixel by pixel. One forward pass each, no sampling.

The spread it has to cover comes from two places: the noise and the mask, which is the fan of maps
from the first slide, and the learned prior, which picked one of them. **▲** But a network's own
variance estimate comes with *no guarantee*.

---

## A1.8b — conformal calibration · frame 14 · 1:14

So we calibrate it, on held-out maps where the truth is known. Three steps, and you can watch them.

Take one pixel across the held-out maps, and draw the network's interval for each of them. Half of
the truths land outside, which is far more than the rate we asked for. [CLICK] Score each truth by
how far outside it fell, negative if it was inside. Sort the scores, and take the quantile. [CLICK]
Widen every interval by that amount. The old bar is the dark core inside the new one. Now twenty per
cent land outside, which is the rate we asked for.

[CLICK] **▲** That is **conformalised quantile regression**, and this is the guarantee: the miss
rate sits between alpha minus one over n plus one, and alpha, for any network and any data
distribution, with n held-out maps. Distribution-free, finite-sample. It holds whether or not the
network is well specified.

---

## A1.9 — accurate, with the smallest calibrated error bars · frame 15 · 1:22

Here is the whole result in one plot. Across, the reconstruction error. Up, the size of the
calibrated error bar. **Lower left is better.**

The colour is the miscoverage rate. Before calibration the circles sit above the target; after
calibration every diamond is on it. So the comparison is not about who covers. Everyone covers,
that is the guarantee doing its job. It is about who covers with the *tightest* bars.

**▲** On accuracy, PnPMass is within **one per cent** of DeepMass, which is a U-Net trained end to
end for this exact mask and noise level. On uncertainty, it has the **smallest calibrated error
bars** of every method tested, on all five hundred and twelve test maps. [CLICK] And the uncertainty
is larger where the structure is.

[CLICK] **▲** Remember that DeepMass has to be retrained whenever the footprint or the noise
changes. PnPMass is trained *once*. Two honest limits: the guarantee is marginal, not conditional,
and it is weakest at the peaks. And this is a single cosmology.

---

## A1.10 — six correlated channels · frame 16 · 1:03

One more step, from a paper in preparation with Hubert Leterme.

Slice the source galaxies by distance, and you get one map per slice: **six channels**. Here are the
six maps of one field, reconstructed the way I will show in two slides. The same structures appear
in every channel, and they get stronger with distance, because each slice is lensed by all the
matter in front of it. So the channels are strongly correlated.

[CLICK] And here is what we actually measure. Each channel gets a sixth of the galaxies, so the
noise per channel is much worse than in the single-map problem, and many pixels have no galaxy at
all. **▲** Six ill-posed problems, each worse than the one we just solved, and they *share their
answer*.

---

## A1.10b — the nulling · frame 17 · 0:55

Why do we want the channels at all? Channel k sees everything in front of it. And the apparent size
of a structure mixes its physical size with its distance, so a multiscale analysis on one channel
mixes scales. **Nulling** fixes that.

[CLICK] It is a fixed, invertible, triangular re-mixing of the channels, three at a time, with
weights set by the geometry alone, such that each new channel sees only the matter near its own
distance. **▲** The price is that it is a *difference of noisy maps*. The noise adds up, and an
error in one channel leaks into the next. That is the test the reconstruction has to pass.

---

## A1.11 — one denoiser, six channels · frame 18 · 1:08

The obvious way is to run the loop six times, with one denoiser per channel, and ignore that they
share the answer.

[CLICK] The alternative changes one thing. The measurements are stacked into one six-channel image.
The data step is block-diagonal, so each channel still has its own mask and its own noise. And the
denoiser is **one network**, with six channels in and six channels out, trained on six-channel
simulations. So the correlation across channels lives in the prior.

[CLICK] **▲** Nothing else moves: the operator, the masks and the noise levels still enter only in
the data step. And the theory follows: convergence with masked data, and an error bound that ties
the error of the loop to the error of the denoiser alone. As a by-product, the bound justifies the
step size we had been choosing by hand.

---

## A1.12 — the tomographic result · frame 19 · 1:10

Before any re-mixing, the joint reconstruction has a lower error in every channel. Over the test
set, zero point eight nine against zero point nine five, relative to the zero map.

[CLICK] Now we null the foreground, the re-mixing from two slides ago. These are differences of
noisy maps, so the errors add up. [CLICK] **▲** After the nulling, the per-channel reconstruction is
*worse than the zero map* from the third channel on: one point four eight on average. It has
invented structure. The joint reconstruction never crosses one. The honest limit: in the far
channels it sits close to one, so they are recovered, but barely.

[CLICK] And here it is in a map, the nearest channel of one field. The per-channel reconstruction
sees nothing. The joint one reads the peak from the other five channels, and the peak is there in
the truth.

> **Tier-0 short path** (−0:25). Say the two numbers, then click three times through to the map:
> *Before the nulling, zero point eight nine against zero point nine five. After it, the per-channel
> loop is worse than the zero map, one point four eight; the joint one never crosses one. And in the
> map: per channel sees nothing, joint reads the peak from the other five, and it is in the truth.*

---
---

# Part 2 — reading the map · frames 20–27

---

## A2.0 — the Part 2 card · frame 20 · 0:13

Part 2, reading the map. The map has to become a feature vector before the inference, and the
question is whether that step needs a network.

---

## A2.1 — same power spectrum · frame 21 · 0:52

The standard feature vector in our field is second order: the two-point function, or the power
spectrum, the Fourier amplitudes. **▲** For a Gaussian random field it is complete. But the
late-time matter field is *not* Gaussian: gravity collapses it into haloes and filaments around
voids. Here are two fields with the **same power spectrum**, and a two-point analysis cannot tell
them apart.

[CLICK] You know this picture. Keep only the phases, and the web is still there. Keep only the
amplitudes, and nothing is. The information is in the phases. To reach it we need statistics beyond
second order: peak counts, wavelet statistics, Minkowski functionals.

---

## A2.2 — the hand-crafted feature · frame 22 · 0:59

You have just seen a starlet in the previous talk, so I can be brief. Ours is the same isotropic
undecimated wavelet transform: the map becomes a sum of band-pass images, each with structure of a
characteristic size, plus a coarse residual. Our hand-crafted feature lives on those bands.

[CLICK] It is the **ℓ1-norm**: in each band, bin the coefficients by amplitude, and sum their
absolute values, bin by bin. Every pixel contributes: the peaks, the voids, and the filaments in
between. [CLICK] Plotted against the amplitude, it looks like this. One curve per scale, two lobes.
A weighted histogram of the field in the wavelet domain. That is the whole feature vector. No
training, and every entry has a name.

---

## A2.3 — likelihood-free inference · frame 23 · 1:04

For these features there is no analytic likelihood. What we have is a **simulator**. So we draw
parameters from the prior, run the simulator, and keep the pairs. [CLICK] Those pairs train a
conditional normalising flow, and the trained flow is directly a model of the posterior: give it the
observation, and it returns the posterior. Justine will go much deeper into this at two o'clock.

Two things matter for what follows. **▲** Every posterior in this talk is **calibration-tested**: on
thousands of simulated cases, when the pipeline says sixty-eight per cent, it is right sixty-eight
per cent of the time. And such a test certifies the estimator against the simulator that trained
it. What happens when the simulator's physics is wrong is a separate study, and it is in the backup.

---

## A2.4 — the learned encoder · frame 24 · 1:36

Beating second-order statistics is easy. The real question is how close a feature vector gets to
**all** of the information in the map. And since the inference is already a network, why not learn
the compression too? There are reasons to be careful: training data, interpretability,
generalisation. But the principled way to do it is **variational mutual-information maximisation**.

[CLICK] A convolutional encoder maps each four-channel map to a ten-dimensional summary, and a
conditional normalising flow, RealNVP, maps the summary to a posterior. [CLICK] The two are trained
jointly, on the expected log posterior under the flow. That objective is a variational lower bound
on the mutual information between the summary and the parameters, up to the entropy of the prior.
It is tight when the flow matches the posterior. So maximising it over the encoder maximises the
information the summary carries, and at the optimum the summary is a sufficient statistic.

**▲** So this network is not just another feature. It is an estimate of the **ceiling**: the most
any summary of these maps can carry. And the comparison is matched: same simulated maps, same flow,
same calibration tests on every posterior. Only the feature vector differs.

---

## A2.6 — the gap · frame 25 · 0:52

First result. The two are not far apart, but [CLICK] the learned encoder wins, by **thirty-six per
cent** in constraining power. So the hand-crafted feature loses part of the information.

But the comparison is not symmetric. The ℓ1-norm is computed *channel by channel*, and you saw in
Part 1 what that leaves out. The channels are correlated, each slice is lensed by the matter in
front of it, and much of the information is in how the signal changes from one channel to the next.
**▲** A per-channel statistic never sees that cross-bin structure. It only sees the marginals. The
encoder's first layer mixes all four channels.

---

## A2.8 — two routes · frame 26 · 1:10

So we designed two ways to give the hand-crafted feature the same access.

**Route one**, change the input: for every pair of channels, multiply the two maps pixel by pixel.
The product is strong only where both maps have structure, and we run the same ℓ1-norm on it.

[CLICK] **Route two**, change the statistic. At a given scale, every pixel has a wavelet coefficient
in each of the two channels. The per-channel ℓ1-norm is the histogram along each axis: the two
marginals. [CLICK] Instead, we lay a grid on the plane and sum the ℓ1 weight in each cell. That is a
**joint two-dimensional histogram** over the channel pair. The diagonal is where both channels are
strong. Off the diagonal, one is strong and the other weak. That is the redshift information. We
call this the joint ℓ1-norm, and it needs no extra maps.

---

## A2.9 — the answer · frame 27 · 0:55

Same maps, same flow, four feature vectors. The per-channel ℓ1-norm. [CLICK] Plus the product
channels. [CLICK] The joint ℓ1-norm. [CLICK] And the learned encoder, which lands right on top of
the joint ℓ1-norm.

**▲** That is a tie, and I want to call it a tie, *not a win*. The encoder's coverage is slightly
conservative, which plausibly accounts for the hair between them. And since the encoder was trained
to be information-optimal, a hand-crafted feature that reaches it is a sufficiency result: **▲** the
joint ℓ1-norm carries essentially all the information about the parameters that these maps make
accessible. With no training, a data vector you can inspect, and nothing to retrain when the survey
changes.

---
---

## C — conclusions · frame 28 · 0:48

So, two things to take away.

**Learn the prior and keep the physics.** A plug-and-play reconstruction with a learned denoiser is
as accurate as the networks trained end to end for one configuration, its error bars are
calibrated, and it is trained once: for any mask, any noise level, and for six correlated channels at
once.

**Hand-crafted features can match a learned encoder.** Read the channels jointly, and the wavelet
ℓ1-norm ties the information-optimal encoder, with no training.

**▲** Learn only what the physics cannot supply, benchmark it, and calibrate it before you trust it.

Thank you.

---
---

# Slides hidden in place

Four frames sit in the file with `data-visibility="hidden"` and no frame number. None has a beat.

| slide | why it left | what survives |
|---|---|---|
| Euclid (defense 6) | the talk is about the method | one sentence at the end of A0.3 |
| the 2025 experiment pair (defense 17, 19) | same | the two numbers at the end of A1.3 |
| the tomography flipbook (defense 42) | frame 16 shows the channels themselves | the correlation sentence in A2.6 |
| three open questions on the chain | Andreas, 2026-09-15: no open stuff | the three answers are Q&A 2, 4 and 6 |

---
---

# The arithmetic, and how to close it

**27:56 spoken against a 25-minute slot**, at 121 wpm, before the pauses. Stamped by
`tools/measure-script.py PIML_FORTH_2026 --wpm 121 --write`; re-run it after every edit, and do not
trust a row below you have not re-measured.

| act | frames | measured | share |
|---|---|---|---|
| Act 0 | 1–5 | 4:30 | 16 % |
| Part 1 | 6–19 | 14:56 | 53 % |
| Part 2 | 20–27 | 7:42 | 28 % |
| Close | 28 | 0:48 | 3 % |

Part 1 carries the tomographic block, which is what makes the talk long. The ladder is ordered so
that the block is the last thing to go.

## Tier 0 — short paths, written out

Two beats carry a complete shorter version in a `>` note under them: **A1.7** (drop the
walk-through, −0:20) and **A1.12** (the two numbers, then click to the map, −0:25). Take these
first; they cost no slide.

## Tier 1 — the teaching frames

| | what | saves |
|---|---|---|
| 1 | **A1.6, the four ways, to one sentence at the top of A1.7**: *end to end, unrolled, plug-and-play, posterior sampling; this is the third*. The drawing stays in the file, skipped. | −1:00 |
| 2 | **A1.8b, the conformal steps, back to backup**; its guarantee sentence is kept at the end of A1.9. | −0:55 |

## Tier 2 — the variants and the framing

| | what | saves |
|---|---|---|
| 3 | **A1.7b, the residual variant, to one sentence at the end of A1.7**: *a variant that lets a Wiener filter take the Gaussian part and runs the loop on the residual is within half a per cent of the end-to-end network*. | −0:40 |
| 4 | **A2.6 folded into A2.9's build**: the per-channel arm is the first frame of frame 27, so the gap can be said there. | −0:30 |
| 5 | **A2.4's *why not learn the compression* to one sentence.** | −0:20 |

## Tier 3 — the block

**The tomographic block (A1.10, A1.10b, A1.11, A1.12) costs about 4:00.** If it has to go, it goes
as a block: A1.9 closes with *and the same loop, with one six-channel denoiser, carries the
correlated channels of a tomographic analysis; paper in preparation*, and frames 16–19 are skipped.

## Never cut

- A1.1, the inverse problem, and A1.3's *four per cent against a hundred and fifty-seven*.
- A1.7's *one network serves every configuration*.
- A1.9's *smallest calibrated bars, trained once*, and its two honest limits.
- A1.12's *worse than the zero map*, if the block is in.
- A2.4's definition of the ceiling.
- A2.9's *a tie, and I want to call it a tie*.

## Planned exit

End of Part 1, frame 19, at about **19:30** on the clock if nothing was cut. With tiers 0 to 2
taken in advance (−3:30) it is about 16:30, and the talk lands near 24:30. Part 2 is 7:42 and has
no fat left below tier 2.

---
---

# Room cues

- **Lanusse, 10:00**, keynote on ML and physical modelling for surveys. Fill in the A1.7 cue after
  hearing it. The contrast to have ready: a score-based model samples the posterior over maps; a
  fixed-point reconstruction with conformal calibration gives a point estimate with a finite-sample
  guarantee, at a fraction of the cost per map.
- **Pérez Roncero, 11:30**, wavelet denoising of IFU cubes, directly before you. A2.2 opens with
  *you have just seen a starlet*.
- **Zeghal, 14:00**, SBI keynote. A2.3 hands off to her.
- **Starck and Tsakalides** organise the workshop and sat on the committee. Nothing needs
  re-arguing for them.

---
---

# Q&A, ranked

Short answers. Do not reach for the backup deck unless the answer needs a figure.

**1. "Why plug-and-play rather than unrolling, or a deep-equilibrium model?"**
Flexibility. Unrolling trains through a fixed number of iterations for one forward operator, so a
new mask or noise level means retraining. A deep-equilibrium model is the same fixed point trained
end to end, with the same dependence. Here the denoiser never sees the operator, so one network
serves every configuration. The price is that convergence relies on the denoiser being close to
non-expansive. That is why it is trained on white Gaussian noise across a range of levels, and not
on the actual observation.

**2. "Does it converge, with a transformer as the denoiser?"**
In practice, eight iterations, and the residual variant is better behaved than the map variant.
The classical guarantee needs a non-expansive denoiser and a step size in the admissible interval,
zero to zero point one seven six here. Non-expansiveness can be encouraged in training by
regularising the spectral norm of the Jacobian (Pesquet et al. 2021), which is costly. We did not,
and we verify convergence empirically.

**3. "Why a point estimate plus conformal calibration, and not posterior sampling?"**
Cost per map at Euclid's scale, and the kind of guarantee. Sampling a learned posterior gives a
distribution whose calibration depends on the model being right. Conformal calibration gives a
finite-sample, distribution-free coverage statement that does not. The two are complementary, and
the score-based samplers are the nearest relatives of this method.

**4. "Marginal coverage is weak."**
Agreed, and it is the limitation I would attack. The guarantee holds on average over pixels. The
miscoverage concentrates at the peaks, which is where Part 1 argued the information lives.
Conditional conformal methods exist, and they are the named next step.

**5. "Is the encoder under-trained? That is why it ties."**
Architecture, summary dimension, training budget and flow family were each swept. Getting the
encoder to its number took an expressive flow, RealNVP, worth thirty-six per cent, and a better
architecture, a ResNet-18, worth another six. Deeper networks overfit at nine hundred cosmologies.
The converse is honest: with a much larger simulation suite the encoder would likely pull ahead
again. The tie is a statement about the data volume a survey analysis actually has.

**6. "Your calibration tests certify against the simulator. What if the simulator is wrong?"**
Exactly, and we measured it. Baryonic feedback is astrophysics the simulator lacks at small scales.
Train the flow on maps without it, feed it an observation with it, and at Euclid's area the
hand-crafted features are biased by three point six sigma, the second-order statistic by two point
two. The contamination localises in the finest wavelet band. Drop that band, and the ℓ1-norm still
constrains one point eight times tighter than the power spectrum on the scales that remain. It is
in the backup, column four.

**7. "Would the tie hold on a richer field?"**
Noisy mass maps at these depths are close to a Gaussian field plus quasi-circular peaks, which is
exactly what the wavelet basis is built for. Where the field is morphologically richer, the balance
should tip back toward the learned encoder. And the pairwise joint statistic has a ceiling of its
own: genuine three- and four-channel structure stays with the network.

**8. "Why the starlet, and why ℓ1 rather than ℓ2?"**
Isotropic atoms match the roughly round things in the map, and undecimated means the result does not
depend on where a structure sits on the grid. Summing absolute values keeps the negative side, the
voids, which a count of maxima discards. Binning by amplitude is what makes it more than a band
power. Backup column three has the cards.

**9. "Why not null the foreground on the measurements first, and reconstruct in the nulled space?"**
The re-mixing is linear and invertible, so it is the same problem in another basis, and the data
step would carry the re-mixed operator. What changes is the prior: the denoiser would be trained on
nulled maps, which have lower signal-to-noise and are closer to Gaussian. We have not tested it. The
joint reconstruction in the natural basis, nulled afterwards, is the comparison the paper makes.

**10. "Twenty-four iterations now, against eight before?"**
The step size is larger in the tomographic problem, so the contraction rate is closer to one, and
the convergence proposition says exactly that. It is the price of the lower signal-to-noise per
channel. The error curve is flat by about fifteen iterations.

**11. "Could the joint denoiser be inventing foreground structure from the background channels?"**
That is what the nulling tests. The nulled channels contain only local matter, so a reconstruction
that leaks foreground shows up there as invented structure. That is what the per-channel maps do,
and the joint maps do not. The honest limit is the other way: in the far channels the joint
reconstruction stays close to the zero map, so they are recovered, barely.

---
---

# Register notes

- **The room is not cosmologists only.** Signal processing, computer science, Earth observation
  and medical imaging are in it. Say the object in their words first, then attach the cosmology
  word once. Never say FoM, HOS, NPE, MAF, BNT or S8 without the phrase.
- **Numbers out loud, in words**, as written here. "One point four eight", not "one point four
  eight ex". A spoken decimal that has to be decoded is lost.
- **Concede first.** A1.9's two limits, A1.12's *recovered, barely*, A2.9's *a tie, not a win*, and
  the honest converse in Q&A 5 are volunteered before anyone can raise them. That is what buys the
  rest of the talk its credibility.
- **Do not diagnose before the experiment.** A2.6 reports a gap and names an asymmetry. The
  diagnosis is A2.8 and A2.9.
- **The two questions are the spine.** If you lose your place, go back to *which of the two am I
  answering*. The close returns to them.
- **Architecture names stay off the slides.** ResNet-18 is said only if asked (Q&A 5).

## Say this, not that

| cosmology word | first mention | thereafter |
|---|---|---|
| convergence κ | the **mass map**: a scalar image of the projected matter along the line of sight | the map |
| shear γ | the **measurement**: a two-component distortion field, sampled where there are galaxies, noise-dominated | the data |
| Kaiser–Squires | the **direct linear inverse**, one FFT, no regulariser | the linear inverse |
| MCALens | a **sparsity-regularised solver**: Gaussian plus ℓ1-in-wavelets component | the sparse solver |
| DeepMass, MMGAN | a **U-Net / a GAN trained end to end for one mask and noise level** | the end-to-end networks |
| figure of merit | **constraining power**: the inverse volume of the posterior's one-sigma region | constraining power |
| corner plot | the **posterior over the model parameters**, two at a time; smaller is more precise | the posterior |
| Ωm, σ8, h, w0 | the matter density, the clumpiness amplitude, the expansion rate, the dark-energy equation of state (once, on the first posterior) | the parameters |
| power spectrum | **second-order statistics**: the Fourier amplitudes; complete only for a Gaussian field | second-order statistics |
| higher-order statistics | **hand-crafted features beyond second order** | the hand-crafted features |
| starlet | an isotropic **undecimated wavelet transform** | the wavelet transform |
| starlet ℓ1-norm | the **ℓ1-norm of the wavelet coefficients per scale and amplitude bin**: a weighted multiscale histogram using every pixel | the ℓ1-norm |
| tomographic bins | **distance slices**: a **multi-channel image whose channels are correlated** | the channels |
| BNT | **nulling**: a fixed, invertible re-mixing of the channels that makes each one local in distance | the nulling |
| cross-maps | **product channels** | product channels |
| joint ℓ1-norm | a **joint 2-D histogram over channel pairs**, ℓ1-weighted | the joint ℓ1-norm |
| CNN, VMIM | a **learned encoder** trained with the flow to **maximise mutual information** with the parameters: the ceiling | the learned encoder |
| SBI, NPE | **likelihood-free inference**: a conditional normalising flow trained on simulator (θ, x) pairs | the flow |
| TARP, SBC | a **calibration test**: when the pipeline says 68 %, is it right 68 % of the time | calibrated |
| conformal, CQR | theirs already; **distribution-free, finite-sample** once | conformal |
| Euclid, Stage IV | the **next-generation survey** | Euclid |

---
---

# Numbers used, and where they are ledgered

`PAPER_FACTS.md` in this directory, which points at `../PhD_Defense_2026/PAPER_FACTS.md` as the
authority for the published papers.

**Part 1.** Map error ratio 0.959 (four per cent), constraining-power ratio 2.57 (a hundred and
fifty-seven per cent). PnPMass within about one per cent of DeepMass (RMSE ratio 1.013), the
residual variant within half a per cent (1.006). Smallest calibrated error bars on all 512 test
maps. SUNet, 7.2 M parameters. Eight iterations, step size in (0, 0.176). Target error rate
α ≈ 4.55 %, from 1 024 calibration maps.

**The tomographic block** (in preparation, draft of September 2026). Errors relative to the zero
map, over all channels: joint 0.891 against per-channel 0.953 before the nulling, 0.944 against
1.479 after. Step size 0.261 = 2/λmax with λmax = 7.66. 24 iterations. SUNet, six in, six out,
7.3 M parameters. The draft's introduction quotes a 20 % gain that its table does not reproduce; it
is not said.

**Part 2.** The learned encoder 36 % ahead of the per-channel ℓ1 (3326 against 2448). Joint ℓ1
3371 ± 96 against the encoder's 3326 ± 30, quoted as a tie. 3.2 × 10⁵ patches from 899
cosmologies, d = 10, RealNVP. Architecture ladder: RealNVP +36 %, ResNet-18 +6 %.

**Deliberately not said.** The absolute figures of merit of Part 1, the ×2.57⁴ inverse-volume
conversion, the PnPMass timing table (the claim is *trained once*, not *fast per map*), and the
ResNet-18 name.
