# SPEAKER_SCRIPT — PIML Workshop, FORTH, 16 September 2026, 12:00

**`[CLICK]`** advance a fragment · **▲** say verbatim · **bold** the anchor to glance at.
Timings are stamped by `tools/measure-script.py PIML_FORTH_2026 --wpm 121 --write`; the rate is
the one measured at the defense rehearsals. **Target 22:00** for a 25 + 5 slot; delivered from
memory expect two to three minutes more.

## The register: say this, not that

The room is cosmologists plus signal processing, computer science, Earth observation and medical
imaging. Every cosmology noun is introduced in the room's words first, then the term is attached
once. Never say FoM, HOS, NPE, MAF, BNT or S8 without the phrase.

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
| peak counts | a **histogram of local maxima**, scale by scale | peak counts |
| starlet ℓ1-norm | the **ℓ1-norm of the wavelet coefficients per scale and amplitude bin**: a weighted multiscale histogram using every pixel | the ℓ1-norm |
| tomographic bins | **distance slices**: a **multi-channel image whose channels are correlated** | the channels |
| cross-maps | **product channels** | product channels |
| joint ℓ1-norm | a **joint 2-D histogram over channel pairs**, ℓ1-weighted | the joint ℓ1-norm |
| CNN, VMIM | a **learned encoder** trained with the flow to **maximise mutual information** with the parameters: the ceiling | the learned encoder |
| SBI, NPE | **likelihood-free inference**: a conditional normalising flow trained on simulator (θ, x) pairs | the flow |
| TARP, SBC | a **calibration test**: when the pipeline says 68 %, is it right 68 % of the time | calibrated |
| conformal, CQR | theirs already; **distribution-free, finite-sample** once | conformal |
| Euclid, Stage IV | the **next-generation survey** | Euclid |

---

## A0.1 — title · frame 1 · 0:22

Thank you. I defended my PhD on this work two days ago, so what you get today is the version for
this room: a weak-lensing pipeline seen as an inverse problem, a feature extractor and an
inference step, and where the learning goes in each.

---

## A0.2 — lensing in one picture · frame 2 · 0:40

One picture of the physics. Light from distant galaxies travels to us through all the matter along
the way, most of it dark. Gravity bends its path, so the image arrives distorted. Occasionally that
is dramatic: arcs, multiple images. **▲** What happens everywhere is the **weak** regime: every
galaxy behind any structure has its shape changed by about a per cent. Measure the shapes of enough
galaxies and the pattern of distortions is a map of the matter, dark matter included.

---

## A0.3 — the measurement, and the image we want · frame 3 · 0:59

So here is the problem in your vocabulary. The **measurement** is a distortion field, the shear:
two components per position, sampled only where there are galaxies, and dominated by noise, because
every galaxy has its own intrinsic shape, far larger than the distortion we are after. The lensing
is coherent and the intrinsic shapes are random, so averaging over neighbours recovers the shear.
**▲** The **image we want** is the convergence: a scalar map of the projected matter along the line
of sight, the mass map. And the data are arriving: Euclid, launched in 2023, is measuring the shapes of
billions of galaxies over a third of the sky, and extracting the signal from them is an algorithms
problem.

---

## A0.3b — one potential, one operator · frame 4 · 0:44

The two are not independent. Both are second derivatives of the lensing potential, a projection of
the gravitational potential along the line of sight, so in Fourier space one linear operator takes
the map to the shear: P, with two components, the two kernels you see here. They have unit modulus,
so the relation inverts in one line, convergence equals P one gamma one plus P two gamma two.
**▲** Linear and exact for a complete, noiseless field. And this P is the operator in every
equation that follows.

---

## A0.5 — the chain, and the two questions · frame 5 · 1:23

The pipeline, reduced to the steps that matter; it is the map of the talk. Galaxy shapes go in.
From the shapes we make the mass map: a **linear inverse problem**. From the map we extract a
feature vector, because a hundred thousand correlated pixels cannot be compared with theory
directly. From the features we infer a handful of parameters of the physical model, with a
simulator standing in for the likelihood. Every step can bias the answer or distort the error bars
without anything downstream noticing, and every step now has a place where a network could go.

[CLICK] **▲** Question one, the first half: in the inverse problem, learn only the prior. Is the
reconstruction as accurate as a network trained end to end, does it work for any configuration,
can its error bars be certified?

[CLICK] **▲** Question two, the second half: the features. A learned encoder, or hand-crafted
features? Who extracts more about the parameters, and why? And in each case, how we know:
benchmarked, calibrated, tested.

---

# Part 1 — learning the prior · frames 6–19

---

## A1.0 — the Part 1 card · frame 6 · 0:16

Part 1, making the map. Two papers: one on what the choice of prior does to the science, and one,
led by Hubert Leterme, on a learned prior with certified error bars.

---

## A1.1 — the inverse problem · frame 7 · 0:49

The forward model is one line: a known linear operator, a mask, additive noise. The relation is
exact; the data are not. The noise is much larger than the signal, and the direct inversion
amplifies it at small scales. The mask removes data, and because the operator is non-local a hole
leaves whole modes unconstrained. And a constant added to the map leaves the data unchanged. So it
is ill-posed in the ordinary sense: **three visibly different maps**, all consistent with the same
measurement. [CLICK] **▲** Selecting one requires a prior, and the choice of prior is what
distinguishes the methods.

---

## A1.2 — the direct linear inverse · frame 8 · 0:47

The standard method for thirty years is the direct linear inverse, Kaiser–Squires: apply the
inverse operator in Fourier space. One FFT, no regulariser, no free parameters. [CLICK] Same field,
same mask, left and right. The structure you see on the left is buried on the right, and the colour
bar spans twice the range: that extra range is noise. The mask leaks across the whole map, because
the Fourier transform does not know there is a hole. In practice one smooths with a Gaussian
kernel, which tames the noise at the cost of the small scales.

---

## A1.3 — data term plus regulariser · frame 9 · 1:25

Every method after that is a regularised least-squares problem you will recognise: a data-fidelity
term, the residual against the measured shear weighted by the noise covariance, plus a regulariser
that says what a plausible map looks like. The data term is the same for every method; the history
of mass mapping is the history of the second term. Kaiser–Squires has none, only the smoothing.
Wiener filtering is an **ℓ2 prior**: a Gaussian field with a known power spectrum. Sparse recovery
is an **ℓ1 prior** in a wavelet basis. MCALens, the state of the art among hand-crafted priors,
models the map as a Gaussian component plus a sparse one, solved with proximal steps. **▲** And
deep learning stops assuming and learns the regulariser from simulations. The choice is not
cosmetic: in the 2025 paper we held everything else fixed and swapped only the reconstruction, and
the sparse solver's map is four per cent better than the linear inverse while the constraining
power on the parameters is a hundred and fifty-seven per cent better.

---

## A1.6 — four ways to put a network in an inverse problem · frame 10 · 1:22

So the prior matters, and a learned prior is the obvious next step. There are four ways to put a
network in a linear inverse problem, and this room knows all four. Grey is a physics step, blue is
a network, and the dashed box is what gets trained together. End to end: data in, image out, the
physics only in the training pairs; a new mask or noise level means retraining. Unrolled: physics
steps and networks on one rail, trained through together; it transfers as far as the training
covered. Plug-and-play: a fixed loop, a data step and a denoiser, and the dashed box is around the
denoiser alone, trained once, on its own. Posterior sampling puts the same learned prior inside a
sampler: the full posterior, at thousands of passes. **▲** The two on the right survive a new
mask or noise level because the prior never saw the operator. Plug-and-play is the cheap one:
eight passes. The error bars are what we add.

---

## A1.7 — plug-and-play · frame 11 · 1:23

Here is the plug-and-play iteration. A gradient step on the data term, towards the measured shear;
then the step that used to be a proximal operator enforcing a hand-crafted prior is a **denoiser**
trained on simulated maps. The iteration converges to a fixed point under the usual
non-expansiveness conditions, and the denoiser has learned a far richer model of a mass map than we
can write down.

**▲** It is flexible because of where the physics sits. The denoiser, a Swin transformer with seven
million parameters, is trained once, on white Gaussian noise over a range of levels, and never sees
the operator, the mask or the noise covariance. Those enter only in the gradient step, at
inference. Nothing is trained through the iteration, so one network serves every configuration.

Here it is running: shear in, the map initialised at zero, the **forward step** giving a noisy map,
the **backward step**, the denoiser, pulling it onto realistic maps. [CLICK] The output is fed
back; eight iterations later it has converged.

> Room cue: if François showed score-based mass mapping this morning (Remy et al. 2023), one
> sentence here: *the same learned prior as the sampler you saw this morning, used as a fixed-point
> reconstruction, with the uncertainty handled next.*

---

## A1.7b — PnPMass on residuals · frame 12 · 0:42

A variant that puts more physics in. The map is a Gaussian component plus a non-Gaussian one, and
the Gaussian part has a closed-form optimum, the Wiener filter, so let it do that part. [CLICK]
Subtract its prediction from the data and run the loop on the residual, with a denoiser trained on
non-Gaussian residuals only; then add the two back. [CLICK] **▲** That variant is within half a
per cent of the network trained end to end for this configuration, and it has converged after two
iterations.

---

## A1.8 — the second network, and its objective · frame 13 · 1:00

The map is half the result; the other half is the error bar. The data fans out to two networks.
The denoiser, in the loop, gives the map. A second network, trained on the same simulated pairs,
gives the error map. Its objective is the squared residual of the reconstruction: regress the
square of the difference between the truth and the map, and the minimiser of that loss is the
posterior variance, pixel by pixel. One forward pass each, no sampling. The spread it has to cover
comes from two places: the noise and the mask, the fan of maps from the first slide, and the
learned prior that picked one of them. **▲** But a network's own variance carries no guarantee.

---

## A1.8b — conformal calibration · frame 14 · 1:09

So we calibrate it on held-out maps where the truth is known, and the procedure is three steps you
can watch. Take one pixel across the held-out maps and draw the network's interval at each: half
the truths land outside, far more than the rate we asked for. [CLICK] Score each truth
by how far outside it fell, negative if it was inside, sort them, and take the quantile. [CLICK]
Widen every interval by that much; the old bar is the dark core inside the new one. Twenty
per cent outside: the rate you asked for. [CLICK] **▲** That is conformalised quantile regression,
and this is the guarantee: the miss rate sits between alpha minus one over n plus one and alpha,
for any network and any distribution, with n held-out maps. Distribution-free, finite-sample. It
holds whether or not the network is well specified.

---

## A1.9 — accurate, with the smallest calibrated error bars · frame 15 · 1:16

The whole result in one plot. Across, reconstruction error; up, the size of the calibrated error
bar; lower left is better. Colour is the miscoverage rate: before calibration the circles sit above
the target, after calibration every diamond is on it. So the comparison is not who covers, everyone
covers, that is the guarantee doing its job. It is who covers with the tightest bars.

**▲** On accuracy, PnPMass is within one per cent of DeepMass, a U-Net trained end to end for this
exact mask and noise level. On uncertainty it has the smallest calibrated error bars of every
method tested, on all five hundred and twelve test maps. [CLICK] The uncertainty rises where the
structure is. [CLICK] **▲** And DeepMass has to be retrained whenever the footprint or the noise
changes; PnPMass is trained once. Two honest limits: the guarantee is marginal, not conditional,
and weakest at the peaks; and this is a single cosmology.

## A1.10 — six correlated channels · frame 16 · 0:55

One more step, from the paper in preparation with Hubert Leterme. Slice the source galaxies by
distance and you get one map per slice: six channels. Here are the six images we want, for one
field. The same structures appear in every channel, because each slice is lensed by all the
matter in front of it; the channels are strongly correlated. [CLICK] And here
is what we measure. Each channel gets a sixth of the galaxies, so the noise per channel is far
worse than in the single-map problem, and many pixels have no galaxy at all. **▲** Six ill-posed
problems, each worse than the one we just solved, that share their answer.

---

## A1.10b — the nulling · frame 17 · 0:52

Why do we want the channels at all? Channel k sees everything in front of it, and a structure's
apparent size mixes its physical size with its distance, so a multiscale analysis on one channel
mixes scales. Nulling fixes that. [CLICK] A fixed, invertible, triangular re-mixing, three channels
at a time, with weights set by the geometry alone, so that each new channel sees only the matter
near its own distance. **▲** The price is that it is a difference of noisy maps: the noise adds
up, and an error in one channel leaks into the next. That is the test the reconstruction has to
pass.

---

## A1.11 — one denoiser, six channels · frame 18 · 1:04

The obvious way is to run the loop six times, one denoiser per channel, and ignore that they share
the answer. [CLICK] The alternative changes one thing. The measurements are stacked into one
six-channel image; the data step is block-diagonal, each channel still with its own mask and its
own noise; and the denoiser is one network with six channels in and six out, trained on
six-channel simulations, so the correlation across channels lives in the prior. [CLICK] **▲**
Nothing else moves: the operator, the masks and the noise levels still enter only in the data
step. The theory follows: convergence with masked data, and an error bound that ties the loop's
error to the denoiser's own error and, as a by-product, justifies the step size we had been
choosing by hand.

---

## A1.12 — the tomographic result · frame 19 · 1:06

Before any re-mixing, the joint reconstruction has a lower error in every channel; over the test
set, zero point eight nine against zero point nine five, relative to the zero map. [CLICK] Now null the
foreground, the re-mixing from two slides ago: differences of noisy maps, so the errors add up.
[CLICK] **▲** After the nulling, the per-channel reconstruction is worse than the zero map from
the third channel on, one point four eight on average: it has invented structure. The joint
reconstruction never crosses one. The honest limit: in the far channels it sits close to one, so
they are recovered, barely. [CLICK] And in the map, the nearest channel of one field: the
per-channel reconstruction sees nothing, the joint one reads the peak from the other five
channels, and it is there in the truth.

---
---

# Part 2 — learning the features, or not · frames 20–27

---

## A2.0 — the Part 2 card · frame 20 · 0:12

Part 2, reading the map. The map has to become a feature vector before inference, and the question
is whether that step needs a network.

---

## A2.1 — same power spectrum · frame 21 · 0:50

The standard feature vector in this field is second order: the two-point function, the Fourier
amplitudes. **▲** For a Gaussian random field it is complete. But the late-time matter field is not
Gaussian: gravity collapses it into haloes and filaments around voids. Here are two fields with the
same power spectrum, and a two-point analysis cannot tell them apart. [CLICK] You know this
picture: keep only the phases and the web is still there; keep only the amplitudes and nothing is.
The information is in the phases. To reach it we need statistics beyond second order: peak counts,
wavelet statistics, Minkowski functionals.

---

## A2.2 — the two hand-crafted features · frame 22 · 1:01

You have just seen a starlet in the previous talk, so I can be brief. Ours is the same isotropic
undecimated wavelet transform: the map becomes a sum of band-pass images, each carrying structure of
a characteristic size, plus a coarse residual. Two hand-crafted features live on those bands.
[CLICK] **Peak counts**: find the local maxima and histogram their amplitudes, scale by scale. Peaks
are haloes, and how many there are depends strongly on the parameters. [CLICK] Counting maxima
throws away the voids, the filaments, everything else. So the **ℓ1-norm** sums the absolute values
of all the coefficients in each band, binned by amplitude: a weighted multiscale histogram that uses
every pixel. Think of it as the one-point distribution of the field in the wavelet domain.

---

## A2.3 — likelihood-free inference · frame 23 · 1:01

For these features there is no analytic likelihood. What we have is a simulator. So draw
parameters from the prior, run it, keep the pairs. [CLICK] Those pairs train a conditional
normalising flow, and the trained flow is directly a model of the posterior: hand it the
observation, it returns the posterior. Justine will go much deeper into this at two o'clock.

Two things matter for what follows. **▲** Every posterior in this talk is calibration-tested: on
thousands of simulated cases, when the pipeline says sixty-eight per cent, it is right sixty-eight
per cent of the time. And such a test certifies the estimator against the simulator that trained
it; what happens when the simulator's physics is wrong is a separate study, in the backup.

---

## A2.4 — the learned encoder · frame 24 · 1:06

Beating second-order statistics is easy. The real question is how close to **all** of the
information in the map a feature vector gets. And since the inference is already a network, why not
learn the compression too? There are reasons to be careful: training data, interpretability,
generalisation. But the principled way to do it is this. [CLICK] An encoder maps each map to a
ten-dimensional summary, and a flow maps the summary to a posterior. [CLICK] The two are trained
together to maximise the mutual information between summary and parameters. **▲** So this network
is not just another feature: it is an estimate of the ceiling, the most any summary of these maps
can carry. And the comparison is matched: same simulated maps, same flow, the same calibration
tests on every posterior. Only the feature vector differs.

---

## A2.6 — the gap · frame 25 · 0:48

First result. The two are not far apart, but [CLICK] the learned encoder wins, by thirty-six per
cent in constraining power. So the hand-crafted feature loses part of the information. But the
comparison is not symmetric. These maps are a multi-channel image: the galaxies are sliced by
distance, each slice is lensed by all the matter in front of it, so the channels are not
independent, and how the signal changes from channel to channel is where much of the information
sits. **▲** A per-channel statistic sees only the marginals; the encoder's first layer mixes all
four channels.

---

## A2.8 — two routes · frame 26 · 1:05

Two ways to give a hand-crafted feature the same access. **Route one**, change the input: for every
pair of channels, multiply the two maps pixel by pixel. The product is strong only where both have
structure, and the same ℓ1-norm runs on it. [CLICK] **Route two**, change the statistic. At a
given scale every pixel has a wavelet coefficient in each of the two channels; the per-channel
ℓ1-norm is the histogram along each axis, the two marginals. [CLICK] Instead, lay a grid on the
plane and sum the ℓ1 weight in each cell: a joint two-dimensional histogram over the channel pair.
The diagonal is where both channels are strong; off the diagonal, one strong and one weak. That is
the redshift information. We call it the joint ℓ1-norm, and it needs no extra maps.

---

## A2.9 — the answer · frame 27 · 0:52

Same maps, same flow, four feature vectors. The per-channel ℓ1-norm. [CLICK] Plus the product
channels. [CLICK] The joint ℓ1-norm. [CLICK] And the learned encoder, which lands on top of the
joint ℓ1-norm. **▲** That is a tie, and I want to call it a tie, not a win: the encoder's coverage
is slightly conservative, which plausibly accounts for the hair. Since the encoder was trained to be
information-optimal, a hand-crafted feature reaching it is a sufficiency result: **▲** the joint
ℓ1-norm carries essentially all the information about the parameters that these maps make
accessible. With no training, an inspectable data vector, and nothing to retrain when the survey
changes.

---
---

## O — three open questions, on the chain · frame 28 · 0:55

Before the conclusions, three open questions, on the steps where they live. [CLICK] The map:
the conformal guarantee is marginal, and the misses sit at the peaks, where the information is.
Conditional coverage at map level, at a cost a survey can pay? [CLICK] The reconstruction:
plug-and-play converges if the denoiser is non-expansive, and for seven million parameters we
verify that empirically. Is there a cheaper certificate than a Jacobian bound? [CLICK] The
features, and what feeds them: the encoder's ceiling is a ceiling for the simulator. When the
physics is missing, which feature degrades gracefully, and can we tell without the truth? If any of
these is your problem, find me at lunch.

---

## C — conclusions · frame 29 · 0:54

So. Question one: learn only the prior, keep the physics in the data term. **▲** Yes. Within one
per cent of the networks trained end to end for a single configuration, the smallest calibrated
error bars of any method, trained once for any mask and any noise level. Question two: does a
learned encoder extract more than hand-crafted features? **▲** Only while it reads the channels
jointly. Give the hand-crafted ℓ1-norm the same access and it matches the information-optimal
encoder, with no training. **▲** The line that joins them: learn only what the physics cannot
supply, benchmark it against the best hand-crafted alternative, and calibrate it before you trust
it. Thank you.

---
---

# The arithmetic, and how to close it

Stamped by `measure-script.py`. Target **22:00**. The cut ladder, in order, each with what it buys:

1. **A2.6 folded into A2.9's build**: the auto-only arm is the first frame of frame 27, so the gap
   can be said there. Frame 25 stays in the file, skipped. −0:30
2. **A1.6, the four ways, to one sentence at the top of A1.7**: *end to end, unrolled, plug-and-play,
   posterior sampling; this is the third*. The drawing stays in the file, skipped. −1:00
3. **A1.7b, the residual variant, to one sentence at the end of A1.7**: *a variant that lets a
   Wiener filter take the Gaussian part and runs the loop on the residual is within half a per cent
   of the end-to-end network*. −0:40
4. **A2.4's *why not learn the compression* to one sentence**: −0:20
5. **A1.8b back to backup**, its guarantee sentence kept in A1.9. −0:55

**Never cut**: A1.1 (the inverse problem), A1.7, A1.9's *smallest calibrated bars, trained once*,
A1.12's *worse than the zero map* if the block is in, A2.4's definition of the ceiling, A2.9's *a
tie, not a win*.

**Planned exit**: end of Part 1 (frame 19), expect 17:00 on the clock. Behind → cuts 1 and 4; the open
questions (frame 28) can go to one spoken sentence, −0:40.

**The tomographic block (A1.10–A1.12, added 2026-09-15) costs about 4:15 with the nulling frame.**
If it has to go, it goes as a block: A1.9 closes with *and the same loop, with one six-channel
denoiser, carries the correlated channels of a tomographic analysis; paper in preparation*, and
frames 16–19 are skipped, −4:00.

**Refocused 2026-09-15 (Andreas)**: the Euclid frame and the 2025 experiment pair (defense 6, 17,
19) are hidden in place; each survives as one sentence, in A0.3 and A1.3. The residual variant and
the nulling came in.

---

# Room cues

- **Lanusse, 10:00**, keynote on ML and physical modelling for surveys. Fill in the A1.7 cue after
  hearing it. The contrast to have ready: a score-based model samples the posterior over maps; a
  fixed-point reconstruction with conformal calibration gives a point estimate with a finite-sample
  guarantee, at a fraction of the cost per map.
- **Pérez Roncero, 11:30**, wavelet denoising of IFU cubes: A2.2 opens with *you have just seen a
  starlet*.
- **Zeghal, 14:00**, SBI keynote: A2.3 hands off to her.
- **Starck and Tsakalides** organise the workshop and sat on the committee. Nothing needs
  re-arguing for them.

---

# Q&A, ranked

**1. "Why plug-and-play rather than unrolling, or a deep-equilibrium model?"**
Flexibility. Unrolling trains through a fixed number of iterations for one forward operator, so a
new mask or noise level means retraining; a deep-equilibrium model is the same fixed point trained
end to end, with the same dependence. Here the denoiser never sees the operator, so one network
serves every configuration. The price is that convergence relies on the denoiser being close to
non-expansive, which is why it is trained on white Gaussian noise across a range of levels rather
than on the actual observation.

**2. "Does it converge, with a transformer as the denoiser?"**
In practice, eight iterations; the residual variant is better behaved than the map variant. The
classical guarantee needs a non-expansive denoiser and a step size in the admissible interval, zero
to zero point one seven six here. Non-expansiveness can be encouraged in training by regularising
the Jacobian's spectral norm (Pesquet et al. 2021), which is costly; we did not, and we verify
convergence empirically.

**3. "Why a point estimate plus conformal calibration, and not posterior sampling?"**
Cost per map at Euclid's scale, and the kind of guarantee. Sampling a learned posterior gives a
distribution whose calibration depends on the model being right. Conformal calibration gives a
finite-sample, distribution-free coverage statement that does not. The two are complementary, and
the score-based samplers are the nearest relatives of this method.

**4. "Marginal coverage is weak."**
Agreed, and it is the limitation I would attack. The guarantee holds on average over pixels; the
miscoverage concentrates at the peaks, which is where Part 1 argued the information lives.
Conditional conformal methods exist and are the named next step.

**5. "Is the encoder under-trained? That is why it ties."**
Architecture, summary dimension, training budget and flow family were each swept. Getting the
encoder to its number took an expressive flow, RealNVP, worth thirty-six per cent, and a better
architecture, resnet-18, worth another six; deeper networks overfit at nine hundred cosmologies. The
converse is honest: with a much larger simulation suite the encoder would likely pull ahead again.
The tie is a statement about the data volume a survey analysis actually has.

**6. "Your calibration tests certify against the simulator. What if the simulator is wrong?"**
Exactly, and we measured it. Baryonic feedback is astrophysics the simulator lacks at small scales.
Train the flow on maps without it, feed it an observation with it, and at Euclid's area the
hand-crafted features are biased by three point six sigma, the second-order statistic by two point
two. The contamination localises in the finest wavelet band; drop that band and the ℓ1-norm still
constrains one point eight times tighter than the power spectrum on the scales that remain. It is
in the backup, column four.

**7. "Would the tie hold on a richer field?"**
Noisy mass maps at these depths are close to a Gaussian field plus quasi-circular peaks, which is
exactly what the wavelet basis is built for. Where the field is morphologically richer the balance
should tip back toward the learned encoder. And the pairwise joint statistic is a ceiling of its own:
genuine three- and four-channel structure stays with the network.

**8. "Why the starlet, and why ℓ1 rather than ℓ2?"**
Isotropic atoms match the roughly round things in the map; undecimated means thresholding does not
depend on where a structure sits on the grid. Summing absolute values keeps the negative side, the
voids, which a count of maxima discards, and binning by amplitude is what makes it more than a band
power. The backup column three has the cards.

**9. "Why not null the foreground on the measurements first, and reconstruct in the nulled space?"**
The re-mixing is linear and invertible, so it is the same problem in another basis; the data step
would carry the re-mixed operator. What changes is the prior: the denoiser would be trained on
nulled maps, which are lower in signal-to-noise and closer to Gaussian. We have not tested it; the
joint reconstruction in the natural basis, nulled afterwards, is the comparison the paper makes.

**10. "Twenty-four iterations now, against eight before?"**
The step size is larger in the tomographic problem, so the contraction rate is closer to one; the
convergence proposition says exactly that. It is the price of the lower signal-to-noise per
channel, and the error curve is flat by about fifteen iterations.

**11. "Could the joint denoiser be inventing foreground structure from the background channels?"**
That is what the nulling tests. The nulled channels contain only local matter; a reconstruction
that leaks foreground shows up there as invented structure, which is what the per-channel maps do
and the joint maps do not. The honest limit is the other way: in the far channels the joint
reconstruction stays close to the zero map, so they are recovered, barely.

---

# Numbers used, and where they are ledgered

`PAPER_FACTS.md` points at `../PhD_Defense_2026/PAPER_FACTS.md`, the authority. Part 1: map error
ratio 0.959 (four per cent), constraining-power ratio 2.57 (a hundred and fifty-seven per cent);
PnPMass within about one per cent of DeepMass, the residual variant within half a per cent; 512
test maps; 7.2 M parameters; eight iterations;
target error rate 4.55 per cent. Part 2: the learned encoder 36 per cent ahead of the per-channel
ℓ1; joint ℓ1 3371 ± 96 against the encoder's 3326 ± 30, quoted as a tie; 3.2 × 10⁵ patches from 899
cosmologies; RealNVP +36 per cent, resnet-18 +6 per cent. Deliberately not said: absolute figures of
merit, and the ×2.57⁴ inverse-volume conversion. The tomographic block (in preparation, draft of
September 2026): errors relative to the zero map, over all channels, joint 0.89 against per-channel
0.95 before the nulling, 0.94 against 1.48 after; step size 0.261 = 2/λmax with λmax 7.66;
24 iterations; the draft's introduction quotes a 20 % gain that its table does not reproduce, so
it is not said.
