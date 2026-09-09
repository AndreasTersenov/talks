# SPEAKER_SCRIPT — PhD defense, University of Crete, 14 September 2026

## The budget

| act | frames | measured | notes |
|---|---|---|---|
| Act 0 — the setup | 1–8 | 8:46 | ends on the chain, in two halves |
| Act 1 — Part 1, does the map matter? | 9–21 | 10:57 | opens with the formalism, moved here 2026-09-06 |
| Act 2 — Part 2, PnPMass | 22–26 | 4:37 | frame 25 is the first cut |
| Act 3 — Part 3, the summaries | 27–47 | 15:45 | still the longest act by far |
| Act 4 — Part 4, baryons | 48–53 | 5:28 | opens on its own divider, added 2026-09-07 |
| Close | 54 | 1:49 | |
| | **54 frames** | **47:26** | **at 120 wpm, against a 40:00 target** |

> **⚠ 47:26 spoken against a 40:00 target, at 120 wpm — over by 7:26.** Every beat was rewritten
> for brevity on 2026-09-07 (61:37 → 43:22); on 2026-09-09 A1.6 to the close were rewritten for
> clarity and register, which put 0:43 back (a precise sentence is usually longer than a punchy
> one), and Act 0 grew to 8:46 in Andreas's own rewrite (A0.8 alone is 3:28). What is left is
> structural, and *The arithmetic, and how to close it* — after the close, below — names it. **Set
> the wpm from a real timing before trusting any of these numbers.**

**The slack in a 45-minute slot is deliberate and must stay slack** — pauses, the beat after a
headline, and the seconds a room needs to look at a figure before you talk over it. It is not room
for more material.

---

## A0.1 — title · frame 1 · 0:57

Thank you, and good afternoon. Thank you all for coming, and thank you to the committee for reading
this and being here in person.

I'm very happy today to present the work that I have been doing for my PhD over the past 3 years.
This thesis is about extracting information from weak gravitational lensing data, and using it to constrain cosmological parameters. In particular, it is about recovering as much of that information as we can, including the part the standard analysis leaves out, and about making sure that the cosmological results we build on it can be trusted.

I would like to start with the picture we are trying to fill in.

---

## A0.2 — the picture · frame 2 · 0:22

This is the history of the Universe as we currently model it.

It starts in a hot, almost uniform state, with very small fluctuations in density. It expands. And
those fluctuations grow under gravity into the structure we observe today — galaxies, clusters, the
cosmic web.

---

## A0.3 — what ΛCDM is, and where it stops · frame 3 · 1:20

Our prevailing model describing all of that is ΛCDM — Lambda, cold dark matter. It is a very simple model, with just six free parameters.

It rests on this short list of assumptions, basically that gravity is given by general relativity, that the Universe is homogeneous and isotropic on large scales, that the initial conditions come from inflation, and are near-Gaussian and adiabatic, and that the matter is a mixture of baryons, cold dark matter and a cosmological constant.

**▲** And it has been extremely successful. Those six numbers fit 
<!-- the microwave background, the expansion history and the clustering of galaxies simultaneously,  -->
our different observations 
to a remarkable precision.

[CLICK] **▲** But it is still not a fully satisfactory answer, for a few reasons. First of all, it is a
**phenomenological** description rather than a first-principles explanation. About ninety-five per
cent of what it describes is two **dark components** whose nature we do not know. 
And independent probes of the same parameters have started to show **tensions** — statistically significant disagreements in the cosmological parameters they report. 

---

## A0.4 — the probes, and the one we follow · frame 4 · 0:16

So how do you study the Universe, and test a model like that? Well, there are several probes that do that...

[CLICK] **▲** But the one we follow in this talk is **gravitational lensing**.

---

## A0.5 — strong and weak lensing · frame 5 · 0:46
Here is the basic idea of gravitational lensing. 

Light from a distant source passes every mass on the way to us, and each one bends its path, so the
image arrives distorted.

Occasionally that is dramatic — arcs, multiple images, Einstein rings, visible by eye. That is the
**strong** regime, and it is very rare.

**▲** What happens *everywhere* is the **weak** regime: every galaxy behind any structure has its
shape slightly changed. This gives us an indication of how the matter (including the dark matter) is distributed -- the Large Scale Structure of the Universe. 

---

## A0.6 — Euclid, and what the signal is · frame 6 · 0:57

And we are about to be able to do this to a new level of precision. 
The next generation of cosmological surveys is here, and the one I work on is **Euclid**.
Euclid launched in 2023, it is taking data now,
and it will measure the shapes of billions of galaxies over a third of the sky, giving us roughly an
order of magnitude more statistical power than anything we have.

[CLICK] **▲** That signal encodes the growth of structure and the geometry of the Universe since
the Big Bang. 

But in order to extract this information and do cosmology with it we need really sophisticated algorithms and statistics.

That is what this thesis is about.

---

## A0.7 — what it actually takes · frame 7 · 0:32

Modern cosmological survey analyses are incredibly complex. 

To demonstrate how intricate the chain is, here is a diagram of the DES Year 3 (a previous generation survey) analysis, 
from pixels to cosmology.

[CLICK] Almost every box here is a paper on its own, and much of it has to do with measurement and calibration. 

The actual cosmology parts are only the parts on the very right.
---

## A0.8 — the chain, and the two halves · frame 8 · 3:28
Here is a similar thing, but reduced to the last steps that are the scientific part of the analysis.

Galaxy shapes go in. From the shapes we make a map of the mass distribution. From the map we extract a few numbers, the summary statistics.
We compare those with theoretical predictions, or with simulations, in a bayesian framework, and we get the probability distributions of the parameters.

[CLICK] **▲** The first half of the talk, the first two papers, is about this step: making the map.
<!-- Several algorithms do it. But does the choice matter for the cosmological results, and can we build a really advanced one whose error bars we can trust, and which can be implemented in a 
survey like Euclid? -->

[CLICK] **▲** The second half, the last two papers, is about everything after it: 
extracting information from the the map, and using it to infer cosmology.
<!-- How much of the cosmological information do the summary statistics keep, and does that survive 
the realistic case, where we have physics that the simulations get wrong? -->

Every one of these steps can bias the result or distort the error bars, if it fails to capture the relevant physical or observational effects.
That's why for the results to be trustworthy, we need methods that properly quantify the unceirtainty, are calibrated, and tested for being unbiased. Otherwirse, we risk producing incorrect scientific conclusions.

<!-- , and the whole chain rests on the simulations being right. If they miss a physical or
observational effect, the posterior at the end looks perfectly normal, and it is wrong. The more of
the pipeline is learned from those simulations, the easier that is to miss: a network asked about
data it was not trained on answers confidently and incorrectly. Trustworthy means we checked, at
every step, that this is not happening to us.

*Every step of this analysis can potentially bias the result, affect the uncertainties,*

*it remains critically dependent on the fidelity of the simulations. If forward models fail to capture all relevant physical or observational effects, and the training data is not representative of the true underlying processes, we risk producing highly unreliable posterior estimates, distorted uncertainty quantification, and incorrect scientific conclusions.*

*This model misspecification problem is arguably more severe in SBI than in traditional
Bayesian inference, where the likelihood is explicit, as neural networks are known to produce arbitrarily incorrect predictions when probed with out-of-distribution (OOD) data. In my postdoctoral research, I aim to develop a new generation of robust and interpretable SBI frameworks that explicitly address these limitations through three complementary avenues.* -->


---
---

# Act 1 — Part 1, does the map matter? · frames 9–21

---

## A1.1 — the question · frame 9 · 0:06

So.. Let's start with our first paper. 

First, what is exactly being reconstructed.

---

## A1.2 — shear and convergence · frame 10 · 0:52

The effect of weak lensing can be summarised in two quantities: the convergence, which is the 
an isotropic magnification of the image, and the shear, which is the anisotropic stretching of the image.

Convergence is not directly observable, because we do not know the intrinsic size of a galaxy. 

The shear however is measurable through statistical analysis of the shapes of many galaxies. 
<!-- The idea is that for one galaxy the stretch is about a per cent, far smaller than the shape it already had.  -->
**▲** The idea is that the lensing is **coherent**
and to a good approximation, the intrinsic shapes are **random**. Therefore, if we average the ellipticities over many galaxies in a patch,
the random part cancels, and what survives is the shear.

---

## A1.3 — what the convergence is · frame 11 · 1:07

However, we would really like to know the convergence, for a few reasons.

First of all, it is a scalar field, so it is easier to work with and extract infromation from than the shear, which is a spin-2 field. 

Second, it has a direct physical interpretation: the convergence is the projected matter along the line of sight, weighted by how efficiently each piece of it lenses. So it essentially tells us the distribution of matter in the Universe, which is what we want to know.
That's why convergence maps are also called mass maps.

<!-- Two things ride in that integral: the kernel carries the geometry, the overdensity carries the
growth. **▲** A convergence map responds to both at once, which is why lensing tests the model
rather than measuring one number. -->

Here you can see an example of a real mass map I created for the UNIONS galaxy survey.

---

## A1.4 — shear and convergence from the same potential · frame 12 · 0:26
Lucky for us, the shear and convergence are not independent. They are both second order derivatives of 
this quantity called the lensing potential, which is itself a projection of the gravitational potential along the line of sight.

In Fourier space we can go from one to the other with a simple linear relation.

---

## A1.5 — the relation is exact, the measurement is not · frame 13 · 1:00

While the relation is exact, the data is imperfect. The shear is measured from galaxy shapes, which are irregularly sampled, and have noise (much larger than the shear itself) and *masks* -- missing regions where there are no galaxies or where the data is not usable.

<!-- **Shape noise**, far larger than the shear itself, and the inversion amplifies it at small scales.
**The mask**: the operator is non-local, so a hole leaves whole modes unconstrained. And **a blind
spot** — shear cannot see a constant added to kappa, so the overall level is not measurable. -->

This is why mass mapping is an **ill-posed inverse problem**: there are multiple possible solutions visibly different from each other and consistent with the data. 

[CLICK] **▲** To get a unique solution, we have to make an assumption about what the kappa looks like.

---

## A1.6 — Kaiser–Squires · frame 14 · 0:56

The simplest method, and the standard one, is Kaiser–Squires: apply the linear inversion directly
to the measured shear. Almost every survey has used it for thirty years, and on a complete,
noiseless field it is exact.

[CLICK] But the data are neither complete nor noiseless. Then it amplifies the shape noise at small
scales: here, same field and same mask, the colour scale of the reconstruction spans twice the
range of the truth, and the extra range is noise. The mask leaks across the whole map, because the
operator is non-local. And the convergence is recovered only up to a constant.

In practice the noise is controlled by smoothing, which removes the small scales.

---

## A1.7 — a data term plus a regulariser · frame 15 · 1:12

But moving towards more advanced methods, every method can be written as an optimisation problem with two
terms: a data-fidelity term, how well the map reproduces the measured shear, weighted by the noise
covariance; and a regulariser, which encodes the prior, what we assume a plausible convergence map
looks like. The methods differ in the regulariser, and in the way they solve the optimisation problem.

Kaiser–Squires has no regulariser, only the smoothing. Wiener filtering assumes a Gaussian field
with a known power spectrum: optimal for a Gaussian field, but the late-time field is not Gaussian.
Sparse recovery assumes the map is sparse in a wavelet basis, mostly empty with a few strong
features, which is closer to a field of haloes. MCALens combines the two, a Gaussian plus a sparse
component. And deep learning learns the regulariser from simulations; that is Part 2.

---

## A1.9 — MCALens · frame 16 · 1:03

The state-of-the-art unsupervised method is MCALens.
It models the convergence as the sum of two components: a Gaussian component, estimated with
a Wiener filter, which needs only the power spectrum; and a non-Gaussian component, sparse in the
starlet domain, which contains the peaks. The two are estimated by alternating minimisation: solve
for one holding the other fixed, then the other, and iterate to convergence.

[CLICK] Each sub-problem is solved with what is called a "proximal step". 
A gradient step on the data term gives a map, v, that fits the shear better but is not necessarily consistent with the prior. The proximal
operator returns the map closest to v that is consistent with the prior; for a sparsity prior it
is a thresholding of the wavelet coefficients.
<!-- I mention it because in Part 2 this operator is replaced by a neural network. -->

---

## A1.10 — the question · frame 17 · 0:48

So different priors give different maps, all consistent with the measured shear. Until this
paper, mass-mapping methods were compared just on the quality of the map: how close the reconstruction
comes to the truth in terms of mean-square error, in simulations. 
But in practice,the map is not the final product. 
What we care about is the cosmological parameters, and the reconstruction error does not tell us how the choice of method affects
them.

[CLICK] For Euclid this is a practical question: is an advanced reconstruction method worth the
effort, or is any reasonable method good enough?

---

## A1.11 — the experiment · frame 18 · 0:56

To answer it, we built a pipeline in which everything is held fixed except the mass-mapping method:
we work with the cosmo-SLICS simulations, in a Euclid-like setting, and we run the whole chain from shear to posterior for each method. 
We use multi-scale peak counts as the statistic, and an emulator with a Gaussian likelihood and MCMC for
the inference. These details are not that important right now, I will come back to all these steps in Part 3 and Part 4.

[CLICK] What matter is that the only thing that varies is the reconstruction: Kaiser–Squires, Kaiser–Squires with
inpainting, and MCALens. So any difference in the posteriors comes from the mass-mapping method.


---

## A1.12 — the three maps · frame 19 · 0:47

Here are the three reconstructions of the same simulated field, next to the truth. Kaiser–Squires has to be
smoothed, so the small-scale structure is lost. Inpainted Kaiser–Squires fills the mask before the
inversion and is otherwise the same. MCALens recovers much more of the small-scale structure.

The first two are the Euclid baseline: mass mapping has been treated as preprocessing with little
effect on the cosmology, so the simplest method became the default. MCALens is the state of the
art. So this compares what a survey will run with the best we can do.

---

## A1.13 — the answer · frame 20 · 1:00

The result, for the multi-scale peak counts and the four-parameter figure of merit, as ratios to
Kaiser–Squires.

First result: inpainting makes no difference: zero point nine nine six.

But MCALens improves the figure of merit by a significant factor of two point six, a hundred and fifty-seven per
cent. 
**▲** So while MCALens improves the RMSE of the map by only four per cent, the figure of merit, so the tightness of the posterior, is improved
by a hundred and fifty-seven. Map quality and constraining power are not the same objective.

So mass mapping is far from a neutral preprocessing step. The choice of reconstruction changes the
cosmological constraints substantially, and for cosmological surveys it is really worth using an advanced method.

> **If pressed on precision:** Chapter 2 reports no error bars; one chain per method.
>
> **If pressed on the RMSE comparison:** the RMSE table smooths each map with the kernel that
> minimises its own RMSE; the figure of merit uses the kernel that maximises its own constraining
> power. They are not the same maps, and that is the point: optimising for map quality and for the
> posterior are different problems.

---

## A1.14 — where the gain comes from · frame 21 · 0:48

Because of the way that we implemented our analysis, we could really look into how the reconstruction
of the different spacial scales affects the constraining power. 
And what we find is that if we look at the cosmological information coming from smaller and smaller scales
in the map, we see that the constraining power of the Kaiser–Squires reconstruction stops improving below eight arcminutes,
while with MCALens the more small-scale information we add, the better the constraints get.

What this means is that MCALens is much better at recovering the small-scale structure, which KS loses to the noise. 

---
---

# Act 2 — Part 2, PnPMass · frames 22–26
---

## A2.1 — the divider · frame 22 · 0:26

Part 2, the second paper. 
Since we have established that the reconstruction matters, the next question is whether we can
build a method that is accurate and fast, with error bars we can trust, for a survey the size of
Euclid.

This is what we develop in this paper, led by Hubert Leterme.

---

## A2.2 — what we want from a method · frame 23 · 0:44

Deep learning has been applied to mass mapping, with several approaches, and it has been quite successful. 
But what do we want from a method, in order to use it in a survey like Euclid? 
Four things: accurate; flexible, meaning the same trained
model works when the noise or the mask changes; fast; and with fast uncertainty quantification (we 
want error bars of the reconstruction, not just the map).

And really, none of the existing methods have all four. That is what we set out to build.

---

## A2.3 — plug-and-play · frame 24 · 1:47

Our method is based on the plug-and-play framework, from the optimisation literature. 
It is a way to solve an inverse problem with a learned prior, and it is very flexible.


The starting point is the iteration from Part 1: a gradient step on the data
term, towards the measured shear, then a proximal step that enforces the prior. Plug-and-play
replaces the proximal operator (which enforces the prior) with a deep denoiser trained on simulations: instead of writing down
a prior, we learn what a plausible convergence map looks like and enforce it through denoising. The
iteration converges to a fixed point.

Why this is better than our analytical priors of e.g. MCALens? 
Because the denoiser is trained on simulations, it can learn a much more complex and realistic prior than we can write down analytically. 
It can capture the non-Gaussian features of the convergence maps, which are important for cosmological inference.

The denoiser is a Swin transformer neural network with seven million parameters, trained once on white Gaussian
noise over a range of levels. 
**▲** With this choice of gradient step, the noise covariance and the
mask enter only in the data term, at inference time, so the same network applies to any noise level
and any footprint. That is what makes it flexible.

> **Tier-0 short path, replacing A2.4** (−0:22). Say this and skip frame 25:
>
> > Eight iterations of that, alternating the data step and the denoiser, and the map converges.
> > A variant that denoises the residual rather than the map does slightly better; it is in the
> > backup.

---

## A2.4 — the iteration, step by step · frame 25 · 0:34

Here it is visualised.
One iteration. We start from zero; the forward step, the gradient step on the data term, gives a
noisy map, and the backward step, the denoiser, gives the estimate of the convergence, which
already resembles the truth. The denoiser's noise level is set to the step size.

[CLICK] The output is fed back, and after eight iterations the map has converged to the fixed
point.

---

## A2.7 — accurate, with calibrated uncertainties · frame 26 · 1:43


Not only does our method produce accurate maps, it also produces error bars for the reconstruction,
which are also perfectly calibrated, with mathematical guarantees. We implemented this 
via moment neworks and a statistical technique called conformalized quantile regression.

<!-- A second network, trained the same way on the same simulated pairs, predicts the error of the
reconstruction pixel by pixel, in one forward pass. **▲** Because a network's own error estimate
comes with no guarantee, we calibrate it with conformal prediction, conformalised quantile
regression on a held-out set, which gives a distribution-free coverage guarantee that holds whether
or not the network is well specified. -->

And here are the results: on the x-axis we plot the
reconstruction error, and on the y-axis we plot the
size of the calibrated error bars, so lower left is better. 

**▲** On accuracy, PnPMass is within about one per cent of DeepMass, a deep learning method trained specifically
for this mask and noise level. On uncertainty, it has the smallest calibrated error bars of all
methods, on all five hundred and twelve maps.

[CLICK] The uncertainty is not uniform: the error bars are larger where the structure is, and
small elsewhere.

[CLICK] And remember, DeepMass needs retraining for every new mask or noise level, making it not applicable to an 
actual large survey, whereas PnPMass is trained once and works for any field.

---
---

# Act 3 — Part 3, the summaries · frames 27–47
---

## A3.1 — the second half · frame 27 · 0:15

The second half of the talk is about what comes after the map: the summary statistic we extract
from it, and the inference of the cosmological parameters from that statistic.

---

## A3.2 — the map has to be compressed · frame 28 · 0:32

So back to our pipeline. We have a map, and we want to compare it with theory to infer the cosmological parameters.
The map is of the order of a hundred thousand correlated pixels, so it would be extremely hard to work with directly. Instead, 
we compress it into a summary statistic before we compare it with theory. 
[CLICK] The choice of statistic determines how
much information is retained. 

---

## A3.3 — the two-point function · frame 29 · 0:52

The standard statistic for weak lensing is the two-point correlation function: how correlated the shear is between
pairs of galaxies separated by an angle theta, measured in real space as xi-plus and xi-minus, or
in harmonic space as the power spectrum.

[CLICK] Every flagship cosmic shear result of the last decade, KiDS, DES, HSC, is a two-point
analysis, and for good reasons. It can be predicted analytically, its covariance is understood,
and there are two decades of work on its systematics.

[CLICK] **▲** For a Gaussian random field, the power spectrum is a sufficient statistic: it
contains all the information. 
But the late-time density field is not Gaussian.

---

## A3.4 — same power spectrum · frame 30 · 0:22

Gravitational collapse and nonlinear structure formation
makes the field non-Gaussian: matter concentrates into haloes and filaments
around voids. 

And here you can clearly see the issue with that: these two completely different fields have the same power spectrum.

A two-point analysis cannot distinguish them.

---

## A3.5 — the phases · frame 31 · 0:26

The difference is in the Fourier phases. The power spectrum keeps only the amplitudes of the
Fourier modes; the phases, which carry the structure of the cosmic web, the filaments, haloes and
voids, are discarded. To access that information we need higher-order statistics: peak counts,
wavelet statistics, the ℓ1-norm, Minkowski functionals, and others.

---

## A3.6 — the gain · frame 32 · 0:13

And this information seems to be quite valuable: from our forecasts, done on simulations, adding different higher-order statistics to the power spectrum significantly improves the constraints. 

## A3.10 — wavelets · frame 33 · 1:32

But to talk about the higher-order statistics we investigate and develop in this thesis, we need to open a small parenthesis on a mathematical tool that is central to them: wavelets.


We are all familiar with Fourier analysis, which decomposes a signal into sines and cosines. Wavelet analysis is similar, but instead of sines and cosines it uses wavelets: localised, oscillating functions that can be dilated and translated to analyse the signal at different scales and positions.

<!-- In Fourier analysis the basis functions are sines, each with a single
frequency and extending over the whole map, so a Fourier coefficient says which scales are present but nothing about where.  -->

For example here you can see the signal being decomposed into wavelet coefficients at different scales. The wavelet coefficient at scale a and position
b measures how much structure of size a there is at position b.


[CLICK] This is well suited to convergence maps, which consists of localised
structures, clusters, filaments and voids, each with a characteristic size and position. 
Such a field is *sparse* in the wavelet domain: it is described by a few large coefficients. 
And the
different scales can be analysed, or removed, separately.

---

## A3.11 — the two statistics · frame 34 · 1:52

So the higher-order statistics we will focuse on both start from the wavelet decomposision of the map, using an isotropic wavelet called the starlet.

And you can see how the starlet transform decomposes the map into a set of band-pass images, each carrying structure of a characteristic angular size.

One thing you can do with these band-pass images is to count the peaks on them, the local maxima of the convergence field, and build a histogram of their amplitudes. This is the wavelet peak counts statistic.

It is very sensitive to the non-Gaussian features of the field, and it encodes very useful information for cosmology, because as you can imagine, peaks are associated with haloes, and the abundance and distribution of haloes depends greatly on the cosmological parameters.

But by just counting the peaks, we are throwing away a lot of information: the voids, the filaments, and the rest of the field. So something else you can do is to sum the absolute values of all the wavelet coefficients, in each band, and build a histogram of those sums. This is the starlet ℓ1-norm statistic. You can imagine it as a PDF of the field in the wavelet domain.



<!-- [CLICK] Its shape is different: bimodal, with a dip at zero, because coefficients near zero
contribute little to a sum of absolute values. The negative side is the voids. This is the
statistic we use for the rest of the talk. -->

---

## A3.12 — from the summary to the parameters · frame 35 · 0:26

Ok, so now we have some summary statistics, and we want to compare it with theory predictions we have assuming different cosmological models, to infer the cosmological parameters that best describe the data.

To do that in a way that encodes all the uncertainties that come into play, we use Bayesian statistics.

---

## A3.13 — classical inference · frame 36 · 1:14

The posterior on the parameters comes from Bayes' theorem: the posterior probability of the
parameters given the data is proportional to the likelihood, how probable the measured data are
for a given set of parameters, times the prior, what we assume about the parameters before seeing
the data. 

In the classical approach the likelihood is written down analytically,
usually as a Gaussian in the data vector, with a theoretical prediction for the mean and a covariance matrix. 

For example, for the power spectrum this is a good approximation, because each band power averages over many independent modes. 

[CLICK] Having an expression for the likelihood, we then approximate the posterior numerically: we
sample it with Markov chain Monte Carlo methods, and the samples give the constraints on the parameters.

For the higher-order statistics we have neither a theoretical prediction for the mean nor a Gaussian distribution, so we need something else.

---

## A3.14 — generative modelling · frame 37 · 0:59

The tool comes from generative modelling. The problem is this: there is a probability distribution
we do not know, and what we have is a set of samples drawn from it. We want to learn the
distribution from the samples, by fitting a parametric model distribution to them. Once
the model is trained we can generate new samples from it, and, for some classes of models, also evaluate its density, the probability it assigns to any point. 

[CLICK] Generative models are the family of models everyone has heard about in the last few years;
they are the algorithms behind image generation, for example. And here you can see how much these models have advanced over the last few years.

<!-- For us the samples are cosmological parameters and summary statistics rather than images, and the models are the same. -->

---

## A3.15 — normalizing flows · frame 38 · 1:05

The generative model class we use is the normalizing flow. 
Start from a simple distribution, a unit Gaussian,
and transform it into the target distribution through a series of simple invertible
transformations, one after the other; their composition is flexible. Because every step is invertible, any point can be mapped back to the Gaussian, and the model density follows from the change-of-variables formula, with a Jacobian determinant that is cheap because the layers have triangular Jacobians.

These bijective transformations are parametrised by neral networks, which are trained to maximise the likelihood of the training samples. So essentially the flow learns from the samples the best way to transform a Gaussian into the target distribution. 

The training objective is just the maximum likelihood of the model density on the training samples.

---

## A3.16 — simulation-based inference · frame 39 · 1:03

So how do we use this for cosmological inference?
We have no analytical likelihood, but we have a simulator: a forward model that we give cosmological parameters and it
produces simulated data, with all the stochasticity of the process. So we draw parameters from the
prior, run the simulator on each, and keep the pairs of parameters and data.

[CLICK] Those pairs are the training samples for a conditional normalizing flow, with the data as
the conditioning input. Trained on them, the flow is directly a model of the posterior: give it the real observation, and it returns the posterior.

The simulations are the only expensive step, and they are run once. Inference is then essentially free, so we can check on thousands of simulated observations.

---

## A3.16b — the divider, Part 3 · frame 40 · 0:21

So now that we know how to do all that, we can ask the third question: how much of the cosmological information do the summary statistics keep, and do we need a neural network if we want to extract *all* of it?
---

## A3.17 — why build a statistic by hand · frame 41 · 1:10

We are looking for the best summary statistic for weak lensing. The ℓ1-norm extracts more than the
power spectrum. [CLICK] But beating the power spectrum is "easy". The real question is how much
information the data contain, and how much of it a statistic keeps.

But... since we are already using neural networks for the inference, why not let one learn the compression as well? 

There are reasons to be careful. A network needs a lot of training data. What it learns is hard to
interpret. And it generalises less predictably: a feature present in the simulations but not in
the real data can bias the result without us noticing. 
  
Nevertheless, people have started doing it, and the theoretically optimal way is to build the
network into the simulation-based inference pipeline and train it together with the flow, an idea
called VMIM.
---

## A3.18 — what optimal means · frame 42 · 0:43

First, what optimal means here. The network is a compressor: it maps the convergence maps to a
low-dimensional summary, and a flow maps the summary to a posterior. [CLICK] The two are trained
together to maximise the mutual information between the summary and the parameters, which is
equivalent to maximising the expected log posterior. [CLICK] So a network trained this way
estimates the most information any summary of these maps can carry. If a hand-built statistic
reaches it, that statistic is sufficient, as far as we can measure.

---

## A3.19 — the setup · frame 43 · 0:40

This is the analysis framework we built to answer that question, and in fact most of the work in this
paper is in this figure: building the simulation-based inference pipeline, from the
convergence maps to the cosmological parameters, and implementing both arms so that they share
everything except the summary. One arm is the analytical higher-order statistics;
the other is the neural compression, a convolutional network trained with the VMIM objective from
the previous slide, through the same normalizing flow.

---

## A3.20 — the gap · frame 44 · 0:34

And here's the first result: the two statistics are not that far apart, but the CNN wins, by thirty-six per cent in the figure of merit. So the l1-norm clearly loses a part of the infromation in the data.

[CLICK] However, the comparison is not symmetric: there is an important property of these maps
that the ℓ1-norm, as we have used it so far, does not take into account.

---

## A3.21 — tomography · frame 45 · 1:15

That property is weak-lensing tomography. The observer is on the left; the source
galaxies are sliced into redshift bins. [CLICK] Take the most distant bin. [CLICK] Its light is
lensed by all the matter in front of it, [CLICK] which gives its convergence map. [CLICK] A nearer
bin [CLICK] is lensed by a shorter column, [CLICK] and gives a fainter map. [CLICK] One map per
bin, and the matter lensing a nearer bin also lenses every bin behind it: the kernels overlap.
[CLICK] So the maps are not independent: the same structure appears in several bins, with an amplitude
that depends on how far away it is. How the signal changes from bin to bin is what tells us where
the matter sits along the line of sight, and so how structure grew with time. That is much of the
cosmological information in tomography, and a per-bin statistic, which sees each map on its own,
cannot see it.

---

## A3.22 — two routes · frame 46 · 2:08

With two-point statistics, extending them to capture the cross-bin information is easy: we also
compute the two-point functions between separate bins. For higher-order statistics such as the
ℓ1-norm there is no obvious equivalent. 

We tried to design two ways to give the ℓ1-norm access to the cross-bin information.

The first option was to create extra maps that capture the "cross" structure: for each pair of bins, multiply the two maps pixel by pixel. The
product is strong only where both bins have structure at the same place. 
To extract the informations from those, we compute the ℓ1-norm on them as well.

[CLICK] The second approach changes the statistic itself. In this figure, the two curves on the axes
are the standard ℓ1-norms of two bins, one on each axis. They are the marginals of a fuller
picture: the plane between them, where each point is a position on the sky, placed by its value in
one bin and its value in the other. [CLICK] The joint ℓ1-norm is the ℓ1-norm extended to that 2D plane:
the same sum of absolute values, in the cells of this grid instead of in the bins of a histogram.
So it records how the strengths in the two bins pair up, position by position: how often a given
strength in one bin comes with a given strength in the other. That is the inter-bin information. If the ℓ1-norm is the PDF of a map in the wavelet
domain, think of the joint ℓ1-norm as the joint PDF of two tomographic bins.


---

## A3.23 — the answer · frame 47 · 0:48
So let's see what we get with our updated higher-order statistics.

Same maps, same flow, four summaries. The per-bin ℓ1-norm. [CLICK] Adding the product cross-maps. [CLICK] The joint ℓ1-norm. [CLICK] And the CNN: which falls almost perfectly onto the joint l1. 

So both neural nets and the joint l1 appear to
give the same performance in terms of extracting cosmological information. And since the network was trained to be information-optimal, this shows that the joint ℓ1-norm essentially encodes all the cosmologically useful information in the weak lensing maps.

And it does without any training, being computationally efficient, interpretable and robust.
---
---

# Act 4 — Part 4, baryons · frames 48–53

> The whole nulling / BNT thread is **out of the main line**; it is backup 67 and 68. See the
> banner on A4.6.

---

## A4.0 — the divider · frame 48 · 0:18
So now that we have shown how great our higher order statistics are and how well they works in idealized cases, let's go to our final paper to see what happens in a more messy, realistic scenario.
---

## A4.1 — the collision of scales · frame 49 · 2:35


Real data have systematic effects: things present in the measurement that are not in our model,
of instrumental origin, like errors in the galaxy shapes, or physical, like the effect of baryons
on the matter distribution. Not all of them can be modelled, and an effect that is in the data but
not in the analysis biases the result.
So to do a proper analysis that can be trusted, we need to carefully investigate how our statistics are affected by each systematic.
And while most groups are doing it at just looking at the impact on the datavector, this is not enough. A proper investigation should show the effect on the posteriors.

The dominant astrophysical systematic effect at small scales is baryonic feedback: energy from active galactic nuclei
and supernovae pushes gas out of haloes and suppresses the matter distribution on small scales.
The simulations we can use for inference dark-matter-only, and the feedback models disagree with each other, so this is physics we cannot model reliably.

The problem is that the non-Gaussian information and the contamination live on the same small
scales. Since we cannot fully reliably model them for HOS, the conservative approach is to remove those scales, and the question is how impactful this is.
[CLICK] So we may find ourselves either in the optimistic case: only the smallest scales are contaminated, and most of the non-
Gaussian information survives. [CLICK] Or in the pessimistic case: the contamination reaches much
further, and after the cut the power spectrum would do just as well.

So, two questions follow: how exactly does unmodelled feedback bias the higher-order statistics, and how does
that grow with area; and once the contaminated scales are cut, is there still a gain over the power
spectrum, or all of our efforts in designing better statistics were in vain, cause they are useless in the real world?

---

## A4.2 — the pipeline · frame 50 · 0:48

The pipeline is very similar to the simulation-based one from the previous paper. [CLICK] Convergence maps from
CosmoGrid at known cosmologies, [CLICK] with Euclid-like shape noise and masks, [CLICK] the starlet
transform, with each statistic measured on each wavelet scale separately, [CLICK] and the
concatenated data vector conditions a normalizing flow, which gives the posterior.

The one point to keep is the separation of scales: because the statistics are measured scale by
scale, the data vector is organised by scale, and a contaminated scale can be removed by dropping
its band. That is what makes scale cuts possible for higher-order statistics.

---

## A4.3 — how large the bias is · frame 51 · 1:04

First question: how large is the bias if we do nothing. CosmoGrid gives every realisation with and
without baryonic feedback, so we train the flow on the dark-matter-only maps, which is the case of
no baryon model at all, and then feed it a baryonified observation. We run this for a range of
survey areas, to see how the bias evolves as surveys get larger.

For the area of a previous-generation survey the bias is not significant. But the error bars shrink
with area while the systematic stays the same, so for a survey like Euclid it becomes really bad,
and at full sky worse still. **▲** And as expected, the higher-order statistics are more biased
than the power spectrum, because they are more sensitive to the contaminated small scales.

---

## A4.4 — the cuts · frame 52 · 0:38

To bring the bias below our threshold of zero point three sigma, we remove small-scale information
step by step until it is. For the power spectrum, by lowering the maximum multipole, which gives an
ell-max for each area, from eight hundred and sixty at two thousand square degrees to three hundred
and forty at full sky. For the wavelet statistics, by removing the finest bands, and there dropping
the finest band alone is enough at every area.

---

## A4.5 — is there anything left · frame 53 · 1:22

So we have seen how the higher-order statistics are biased by unmodelled feedback, and how to cut
to remove the bias. The important question is whether anything is left to gain over the power
spectrum once the cuts are applied. These are the Stage IV posteriors, on baryon-safe scales only.
[CLICK] The power spectrum first. [CLICK] Peak counts. [CLICK] And the ℓ1-norm.

**▲** On those scales the ℓ1-norm reaches a figure of merit one point eight times the power
spectrum's, and at full sky, where the wavelet cut fits better, two point six. The peak counts are
comparable to the power spectrum, and they carry complementary information, since their
degeneracy directions in the w-nought planes differ.

**▲** So higher-order statistics are not only deep non-linear probes: the signal survives on
quasi-linear scales, with no baryon model at all. And in principle we can do better, since our cut
is not optimised, and as feedback modelling improves the analysis moves back into the non-linear
regime, where the gain is larger.


> The ×1.8 at Stage IV carries a ±0.6 band (`PAPER_FACTS.md` §4); if pressed, "about a factor of
> two". At 2,000 deg² the ℓ1 advantage is not significant; it is significant from 5,000 deg²
> upward. Peaks: ×1.07 at Stage IV, ×1.17 at full sky, trailing at smaller areas because of the
> whole-band cut.

---
---

# Close · frames 54–54

## C.1 — the question board — REMOVED 2026-09-07

> The board that repeated the four questions before the conclusions is **hidden** (Andreas): the
> close carries the questions *and* their answers on one slide.

## C.2 — conclusions · frame 54 · 1:23

> **The slide carries the four questions with their answers, in short form.** The room has met each
> question on its divider, so do not read them out again: give the summary below and let the slide
> hold the detail. The paper references are on the part dividers.

So, to summarise.

This thesis followed the analysis chain from galaxy shapes to cosmological parameters, and worked on
two steps of it: making the mass map, and reading it.

On the map, the choice of mass-mapping method is not neutral. It changes the figure of merit by a
hundred and fifty-seven per cent, while the reconstruction error changes by four. And with PnPMass
we have a method that is accurate, with calibrated error bars, and trained once for any mask and
noise level.

On the summary statistic, the joint ℓ1-norm extracts as much cosmological information as a neural
compressor trained to be optimal, without any training. And it stays ahead of the power spectrum
even after removing every scale that baryonic feedback contaminates.

**▲** So, steps of the analysis that are usually treated as neutral choices do change the
cosmological result. And with methods that are calibrated and tested, we can extract more of the
information in the data, and trust what we get out.

> The nulling result belongs here too and is deliberately not said; see A4.6. If it has come up
> during the talk, add one sentence: *and the same joint reading is what makes redshift nulling
> survivable for a higher-order analysis, which is in the thesis.*

Thank you.

---
---

# Beats for the slides that are not in the main line

Six beats, in deck order, for slides that sit in the backup section or are skipped on the day.
They were moved out of the acts on 2026-09-10 (Andreas) so that Act 0 to the Close reads as one
uninterrupted run of what is actually said. Each keeps the banner explaining why it left the main
line and what, if anything, moved out of it first. **A0.4v and A1.8 are inside HTML comment
fences**, exactly as they were in the acts, which is why their headings do not render.

---

<!-- ---

## A0.4v — the two tensions · frame 56 · SKIP · 0:55

> **SKIPPED (Andreas, 2026-09-06).** It is a vertical under A0.4, so skipping it costs nothing but
> not pressing DOWN, and nothing later in the talk depends on it. Kept here because it is the one
> beat that can come back for free if the clock turns out generous — the decision is made *on*
> frame 4, not in advance.

The consistency between independent probes is itself the test of the model. Measure the initial
conditions with the microwave background, evolve them forward assuming ΛCDM, predict what we should
see today — and then measure it. If ΛCDM is right, those agree.

As the uncertainties fell towards the per-cent level, they stopped agreeing perfectly. The
present-day expansion rate comes out differently from the early-Universe extrapolation than from
direct measurement. And the amplitude of clustering — S-eight, the combination lensing constrains
best — came out about one point seven sigma below the Planck extrapolation in DES and KiDS.

[CLICK] Three ways to read that. New physics. A statistical fluctuation. **▲** Or something in the
analysis itself. -->

---

<!-- 
## A1.8 — mass mapping as Bayesian inference · frame 107 · SKIP · 0:52

> **SKIPPED (Andreas, 2026-09-06).** Backup 107. The word *prior* moved to A1.7; the Part 3 pointer
> was dropped on 2026-09-09 (A3.13 stands on its own); the point-estimate flag sits on A1.9. Frame 36
> is now the only place Bayes appears in the talk.

In Bayesian terms: the posterior probability of a map given the shear is the likelihood of the
shear given the map, which is the forward model we already have, times the prior, what we assume
about the map before looking at the data.

[CLICK] The regulariser is the prior. Kaiser–Squires assumes essentially nothing. [CLICK] Wiener
filtering assumes a Gaussian field. [CLICK] Sparse recovery assumes the map is sparse in a wavelet
basis. [CLICK] MCALens assumes both at once.

[CLICK] The same three terms come back in Part 3, with the cosmological parameters as the unknown
instead of a map. There, the likelihood is the term we cannot write down.

> Everything in Part 1 takes the most probable map, a point estimate. Part 2 adds the uncertainty,
> and Part 3 wants the full posterior on the parameters. Starck is the likeliest person to ask.

--- -->

---

## A2.5 — the residual variant · frame 113 · SKIP · 0:30

> **MOVED TO BACKUP (Andreas, 2026-09-06).** A variant, not a result. A2.3's short path names it in
> one clause. The uncertainty slide is its vertical: press DOWN from 113.

[CLICK] There is a variant that performs slightly better. Instead of denoising the map at each
step, we denoise the residual: the difference between where the data step lands and the previous
map. [CLICK] [CLICK] The network then only sees the part that is changing, which is closer to the
white-noise problem it was trained on. [CLICK] [CLICK] Same eight iterations, slightly better
maps.

---

---

## A2.6 — the uncertainty, in full · frame 114 · SKIP · 1:36

> **MOVED TO BACKUP (Andreas, 2026-09-06).** It is the mechanism behind the calibrated error bars
> A2.7 reports, and conformal prediction is Tsakalides's own vocabulary, so expect it in questions.
> Vertical under 113. **A2.7 carries three sentences of it**; do not skip those as well. Q&A tier 2,
> question 8 is the follow-up.

The map is only half of the result. The shear goes in, the denoiser gives the map, and a second
network, trained the same way on the same simulated pairs, gives the error.

[CLICK] Where does the uncertainty come from, when the reconstruction is deterministic? From two
sources. Noise and the mask leave a whole family of maps consistent with the data, the
ill-posedness from Part 1. And the map selected from that family is chosen by a denoiser learned
from simulations, which has its own model error. Both have to be covered.

The second network is trained on the squared residual of the reconstruction; the minimiser of that
loss is the posterior variance, pixel by pixel. One forward pass, no sampling.

[CLICK] But a network's own variance estimate comes with no guarantee; neural uncertainties are
typically overconfident. So we calibrate it with conformalised quantile regression on a held-out
calibration set. The guarantee is distribution-free and finite-sample, and it does not require the
network to be right.

[CLICK] **▲** So instead of "the network says plus or minus sigma", we have a stated coverage level
that holds whether or not the model is well specified.

---

---

---

## A4.6 — nulling, and what goes wrong · frame 67 · SKIP · 1:50

> **MOVED TO BACKUP; the whole nulling / BNT thread is out of the talk (Andreas, 2026-09-06).** Too
> technical for the time available: it needs the transform, the noise-correlation mechanism and the
> invertibility paradox before the payoff means anything, and that is three minutes the talk does
> not have.
>
> **What goes with it.** A4.7's ladder, the joint ℓ1-norm keeping 0.72 where the per-bin ℓ1 keeps
> 0.16, was the second, independent payoff for the statistic built at A3.22; the talk now rests
> that argument on the tie at A3.23 alone.
>
> **Where it lives instead.** Frames **67 and 68**, in front of the three BNT explainers at 69–71.
> Q&A tier 2, questions 3 and 9. **If it comes up, do not improvise it**; it is the one
> counter-intuitive result in the thesis, and it is written out below.

The third thing we looked at is a way of making those cuts less blunt.

Nulling, the BNT transform, is a linear re-mixing of the tomographic bins that cancels the
low-redshift lensing efficiency. The reason to want it: the standard kernels are broad and
overlapping, so one angular scale mixes low-redshift small scales with high-redshift large ones,
and an angular cut throws away clean high-redshift information along with the contamination. Null
the bins and each transformed field is localised in redshift, so you cut scales only where the
systematic is. **▲** For the power spectrum it works, provided you keep the cross-spectra between
transformed bins.

[CLICK] Applied to a map-based higher-order statistic, it backfires. The same mixing correlates
the originally independent shape noise across bins, the noise floor rises, and the contours
**inflate**, to worse than standard tomography even with conservative cuts.

[CLICK] [CLICK] And this should not be possible. **▲** BNT is a fixed, invertible matrix. The
Jacobian cancels in Bayes' rule, the Fisher information is unchanged, and the posterior from the
full field is identical in both frames. And yet the ℓ1-norm keeps sixteen per cent.

We are not alone in hitting this: the Euclid analysis of Vinciguerra and collaborators this year
kept tomographic maps for bin combinations up to quadruplets and still concluded that recovering
the signal-to-noise was, in their words, highly non-trivial.

---

## A4.7 — the information is recovered by a joint reading · frame 68 · SKIP · 1:49

> **MOVED TO BACKUP with A4.6**; the two are one argument and neither works alone. Frames 67 and
> 68, in front of the three explainers that account for them.

So we asked what it takes to get the information back, and ran the same four summaries through
the nulled frame.

[CLICK] The per-bin ℓ1-norm keeps sixteen per cent. [CLICK] Add one derived field per pair, the
product cross-maps, and it is twenty-four. Better, nowhere near.

[CLICK] The joint ℓ1-norm, the statistic we built for a different reason, keeps **seventy-two**
per cent.

[CLICK] And the CNN, which reads all four channels natively, shows **no measurable loss**.

[CLICK] **▲** In the standard frame those four summaries spanned thirty-eight per cent. Here they
span a factor of six. The transform did not destroy information; it moved it into correlations
between bins that only a summary reading the bins jointly can see.

**▲** The power spectrum with its cross-spectra is the simplest case of the same thing. Auto plus
cross spectra are closed under the transform, and so exactly invariant; the auto-spectra alone
keep only the diagonal, and are not. That is the same statement.

**▲** So the practical message, for anyone planning a nulled analysis: nulling need not cost a
higher-order analysis anything, provided some stage of the pipeline reads the bins jointly.

The joint ℓ1-norm keeps seventy-two per cent, not all of it. The remainder is three- and four-bin
structure that a pairwise statistic cannot reach, and that is the one place the network keeps an
advantage.

---
---

# The arithmetic, and how to close it

**47:26 spoken against a 40:00 target**, at **120 wpm**. Over by **7:26**.

> **The rate matters more than any single cut.** 140 wpm is a *reading* rate; delivery has pauses
> in it. Andreas, timing himself: it takes "significantly more time than what you are estimating".
> 120 is the interim figure and it is a guess. **Read A0.8 aloud at delivery pace, time it, and set
> the real number** — the beat is 416 words, so the rate is 416 divided by the minutes it takes:
>
> ```
> tools/measure-script.py PhD_Defense_2026 --wpm 112 --write
> ```
>
> Every number below moves with it. At 110 wpm the talk is 51:45; at 130 it is 43:47.

| act | frames | measured | share |
|---|---|---|---|
| Act 0 — the setup | 1–8 | 8:46 | 18 % |
| Act 1 — Part 1 | 9–21 | 10:57 | 23 % |
| Act 2 — Part 2 | 22–26 | 4:37 | 10 % |
| Act 3 — Part 3 | 27–47 | 15:45 | 33 % |
| Act 4 — Part 4 | 48–53 | 5:28 | 12 % |
| Close | 54 | 1:49 | 4 % |
| *(not spoken)* | backup 56, 67–68, 101–103, 107, 113–114 | *8:50* | — |

**The prose is spent.** On 2026-09-07 every beat in the file was rewritten for brevity — 61:37 to
43:22, a thirty per cent cut with no slide touched. The 2026-09-09 rewrite for clarity held the
main line to within a minute of that. There is not another ten per cent in the sentences without
losing claims. What is left is structural.

## Tier 1 — two frames whose beat says nothing new · −0:57 · lands at 46:29

| frame | what | saves |
|---|---|---|
| 25 | the PnPMass iteration, two frames, which A2.3 has already described | **−0:32** |
| 50 | the SBI refresher. A3.16 taught the same pipeline twelve minutes earlier | **−0:25** |

## Tier 2 — the inference runway · −2:26 · lands at 44:03

**This is the recommendation.** Frames 36, 37 and 38 teach the classical Bayes route, generative
modelling and normalizing flows, to a room where Tsakalides has that vocabulary professionally,
three of the committee know it at the level of the code, and the two astrophysicists need exactly
one sentence: *for these statistics there is no likelihood, so we use the simulator instead* —
which is A3.16's opening line.

| frame | what | saves |
|---|---|---|
| 36 | classical inference with an explicit likelihood | **−0:50** |
| 37 | generative modelling and the faces | **−0:48** |
| 38 | normalizing flows. Fold *flexible, samplable, evaluable* into A3.16 | **−0:48** |

**Keep frame 42.** The definition of *optimal* is 0:38 and it is what makes A3.23 a sufficiency
result rather than a benchmark win — the first thing the committee will press on.

## If it is still long on the day

In this order, and each is a real loss:

| | cut | saves |
|---|---|---|
| 1 | A0.8's questions two and four, to one sentence each | −0:30 |
| 2 | frame 32, the Ajani forecast — A3.11's shapes make the point with the actual statistics | −0:32 |
| 3 | A2.2's read-down-the-table paragraph; go straight to *nothing had all four* | −0:25 |
| 4 | frame 45's narration to the first slice and the closing claim, keeping all eight clicks | −0:30 |
| 5 | frame 19, the three maps — frame 18's chain shows them in miniature | −0:30 |

## Never cut

- A0.8's two halves on the chain, and the four questions on the part dividers. The close returns to the four.
- A1.13's *four per cent against a hundred and fifty-seven*, and the iKS null result.
- A1.5's *the added assumption **is** the method*.
- A2.7's two uncertainty sentences — all that survives of backup 113 — and its two limits.
- A3.3's *the question is whether the field is Gaussian*, and the phases pair, frames 31–32.
- A3.18's definition of optimal.
- A3.23's *that is a tie, and I want to call it a tie*.
- A4.4's *the wavelet cut is coarser, and therefore conservative*, and A4.5's closing summary.

---
---

# Q&A — tier 1, the room

Five to fifteen minutes, general audience plus the two committee members who do not work on
lensing. Short answers. Do not reach for the backup deck unless the answer needs a figure.

**"Why do you need simulations at all — can't you just do the theory?"**
For the power spectrum we can, and the field does. For peak counts or the ℓ1-norm there is no
analytic prediction for the mean, and the distribution is not Gaussian — it is a count statistic in
the tail of a non-Gaussian field. So the simulator replaces the formula. The cost is that the
answer is only as good as the simulations, which is why Part 4 exists.

**"How do you know the machine learning is not just making things up?"**
Two answers. The reconstruction never leaves the data behind — the network is one step inside an
iteration whose other step is a gradient towards the measured shear, and it converges to a fixed
point of that pair. And for the inference we test it: because the trained flow answers any new
observation in milliseconds, we can run it on thousands of simulated observations where we know the
truth and check the posteriors actually cover. That is frame 66 in the backup.

**"Isn't 157 per cent suspiciously large?"**
It is a figure of merit, which is an inverse area in parameter space, so it moves faster than an
error bar. In linear terms it is about a factor of one and a half on each parameter. And it is a
*ratio* between two chains that differ in one step, so the systematics that would inflate an
absolute number cancel.

**"What happens when Euclid data actually arrive?"**
Everything in Parts 1, 3 and 4 is a forecast on simulations, deliberately — you cannot validate a
reconstruction without a truth. What transfers directly is PnPMass, which is trained once and takes
the mask and the noise at inference, and the ℓ1-norm pipeline, which needs only the simulation suite
to be run at the survey's own noise and footprint.

**"Why weak lensing rather than galaxy clustering?"**
Lensing responds to the total matter, so there is no galaxy-bias model between what we count and
what we want. And it is sensitive to the geometry and the growth at once, which is what makes it a
test of the model rather than a measurement of one number.

**"What is the single most important thing in the thesis?"**
That the analysis choices are not neutral. Two of the four results are the same shape: a step
everyone treats as preprocessing — which reconstruction, which frame the bins are in — turns out to
change the answer, and the fix is available if you look for it.

---

# Q&A — tier 2, the closed examination

One to three hours, seven people who have read the manuscript. These are ordered by how likely I
think the question is, and the first is the one I would ask myself.

> **The nulling / BNT thread is not in the talk, and it is in the manuscript.** So it will come up,
> and it will come up cold — the room will not have seen the transform, the noise-correlation
> mechanism or the ladder. Questions 3 and 9 below are the answers, and backup frames 69–71 and 74–77
> are the figures. **Lead with the thirty-second setup before the answer**, in these words:
>
> > Nulling — the BNT transform — re-mixes the tomographic bins so that each transformed field is
> > localised in redshift, which lets you cut scales only where the systematic actually is. It is a
> > fixed, invertible matrix, so it cannot destroy information. Applied to a map-based higher-order
> > statistic it nevertheless inflates the contours, and the resolution is that it moves the
> > information into correlations between bins that a per-bin statistic cannot see.
>
> Then take question 3 or 9 as asked. **Do not improvise this one** — it is the
> counter-intuitive result in the thesis, and the version that lands is the one written out here.

**0. "Why did you not present the nulling result?"**
Time. It is the one result in the thesis that needs three pieces of
machinery before the payoff means anything, and I would rather answer it properly here than rush it
on a slide. Then the setup above, then question 9.

**1. "You compare against a CNN. Did you try hard enough to make the CNN win?"**
A fair objection, and it deserves the working. Getting the network to 3326 took an
expressive flow — RealNVP, worth +36 % — and a better architecture, resnet18, worth a further 6 %.
Going deeper than that *overfits* at 899 cosmologies. So the network is not undertrained; it is at
the point where more capacity costs accuracy on this training set. **The converse:** with a
much larger simulation suite the network would very likely pull ahead again, and the tie is a
statement about the data volume a Stage-IV analysis actually has, not a theorem.

**2. "A tie is not a win. Why prefer the analytical statistic?"**
Given equal constraining power, everything else decides: no training, no architecture search, no
retraining when the footprint or the noise changes, an interpretable data vector you can cut band
by band — which is what Part 4 needs — and a covariance that is nearly diagonal by
construction. And the nulling result: the analytical statistic degrades gracefully in a transformed
frame and you can see *why*, where the network is a black box that happens to survive.

**3. "The joint ℓ1-norm keeps 0.72 under nulling, not 1. What is the missing 0.28?" (not in the talk)**
Genuine three- and four-bin structure. The joint statistic is pairwise by construction, and
pairwise is the ceiling a patch can actually populate — a four-dimensional histogram over K⁴ cells
against 80 × 80 pixels is almost everywhere empty. So the residual is real, it is where the network
keeps an advantage, and I would not claim otherwise.

**4. "Chapter 2 quotes no uncertainty on the 157 per cent."**
Correct, and it is a limitation. One chain per method, 25 cosmologies. The ordering is robust — the
scale ladder in frame 22 is an independent check that the gain is small-scale reconstruction
fidelity rather than a normalisation — but I would not defend the third significant figure.

**5. "Your wavelet scale cut is cruder than the power spectrum's. Is the comparison fair?"**
It is unfair *against* us, and I say so on the slide. The power spectrum gets a sliding ell-max
tuned to each area; the starlet can only drop whole dyadic bands, so at the smaller footprints we
certainly throw away uncontaminated quasi-linear information. A √2 or non-dyadic filter bank would
allow an area-tuned cut. And there is a better cut available in principle: the statistics are
binned in signal-to-noise as well as scale, and the baryonic response sits in the positive tail, so
the contamination could be removed where it sits rather than by removing a band. Future work, and
everything in Part 4 is conservative because of it.

**6. "You use one feedback model. What if the real Universe is worse?"**
Then the bias is larger and the cut is deeper — the *scaling* with area is the robust part, not the
absolute sigma. The mitigation strategy does not depend on which model is right, because it is
defined by a bias criterion, not by a feedback amplitude.

**7. "PnPMass: what does 'converges' actually mean here, and does it?"**
Fixed-point convergence of the forward–backward iteration with a learned operator in the backward
step. It is not free — the denoiser has to be non-expansive for the classical guarantees, which is
a real condition and the reason the training uses white Gaussian noise across a range of levels
rather than the actual observation. In practice eight iterations, and the residual variant is
better behaved than the map variant.

**8. "Marginal coverage is a weak guarantee."**
Agreed, and it is the limitation I would attack. It holds on average over pixels; the miscoverage
concentrates at the peaks, which is where Chapter 2 just argued the information lives. Conditional
coverage — per-pixel, or conditional on local signal-to-noise — is the obvious next step, and
conformal methods for it exist.

**9. "Why should nulling inflate anything if the transform is invertible?" (not in the talk)**
It should not, and that is the point of the result. The Jacobian cancels in Bayes' rule, the Fisher
information is unchanged, and the posterior from the *full field* is identical in both frames. What
changes is what a *given summary* can see: the transform correlates the originally-independent
shape noise across bins, and a summary that only reads one-dimensional marginals loses the part
that has moved into the correlations. The power spectrum is the two-point instance of exactly the
same statement — auto plus cross spectra are closed under the transform and exactly invariant, the
autos alone are not.

**10. "Is the ℓ1-norm actually new? Ajani et al. published it."**
The starlet ℓ1-norm is Ajani, Starck and Pettorino. What is new here is the joint reading — the
pairwise ℓ1 on the coefficient plane — and the demonstration that it closes the gap to an
information-optimal compressor, and that it is what makes nulling survivable.

**11. "Why cosmo-SLICS in Part 1 and CosmoGrid in Parts 3–4?"**
Different requirements. Part 1 needs many cosmologies with matched reconstructions and a truth map,
at DES-like depth. Parts 3 and 4 need a large training set for the flow and a baryonic
implementation. Nothing in either result depends on the suite; the comparisons are internal.

**12. "What would falsify the central claim?"**
A hand-built statistic reaching an information-optimal compressor is a claim about a regime. It
fails if the network can be trained to pull clearly ahead at matched calibration on a larger suite;
it fails if the tie does not survive a realistic mask and a realistic redshift distribution, both of
which are idealised here; and the sufficiency reading fails if VMIM is not actually estimating the
ceiling on these maps.

---
---

# Register notes

- Rehearse in the register you will deliver in. *Measure*, *infer*, *obtain* — not *get*. Under
  pressure you fall back on rehearsed habits, so build the right ones.
- **Numbers out loud, in words**, as written here. "One point eight times tighter", not "one point
  eight ex". A spoken decimal that has to be decoded is a spoken decimal that is lost.
- **Do not diagnose before the experiment.** A3.20 reports a gap and names an asymmetry; the
  diagnosis is A3.22 and A3.23. Asserting the cause early costs the payoff and overclaims.
- **Concede first.** A2.7's two limits, A4.3's *the higher-order statistics are more biased, not
  less*, A4.4's *our cut is coarser*, and A4.7's residual are all volunteered before anyone can
  raise them. That is what buys the rest of the talk its credibility, and it is the pattern the
  committee will be watching for.
- **The four questions are the spine.** If you lose your place, go back to *which of the four am I
  answering* — the room can follow you back the same way.
- Ground analogies in the papers rather than inventing them. *Two auto-spectra never tell you the
  cross-spectrum* is the one to reach for, and it is already the argument in A4.7.

---

# Numbers used, and where they are ledgered

**Act 1** — `PAPER_FACTS.md` §2. Ratios to a KS baseline of 1.00: iKS **0.996**, MCALens **2.57**
(the paper's **+157 %**). RMSE ratios: iKS 1.005, MCALens **0.959** — the four-per-cent figure.
25 cosmologies · DES-Y1, 19 × 100 deg² · starlet scales 2′–32′ + coarse · KS saturates after 8′,
MCALens gains to 2′.

**Act 2** — `PAPER_FACTS.md` §3. RMSE ratios to DeepMass: PnPMass **1.013**, residual variant
**1.006** — quoted as "about one per cent". Smallest calibrated error bars **on all 512 test
images**. SUNet, **7.2 M** parameters. **8** iterations. Target error rate α ≈ 4.55 %.

**Act 3** — FoM₃, matched pipeline: auto-only ℓ1 **2448** · + product cross-maps **3045** · joint
ℓ1 **3371** · CNN-VMIM **3326**. The learned summary is **36 %** ahead of the per-bin ℓ1. Training
set **324 k** patches over **899** cosmologies, flat-sky 10° patches. Ties hold over **9,000** mock
observations. Architecture ladder: RealNVP **+36 %**, resnet18 **+6 %**.

**Act 4** — `PAPER_FACTS.md`, Tersenov+ 2026 A&A. Bias at full resolution, 14,000 deg²: C_ℓ
**2.2σ**, peaks and ℓ1 **3.6σ**; full sky C_ℓ **~3.5σ**, both HOS **> 6σ**. Cut criterion **0.3σ**.
C_ℓ sliding ell-max **860 → 340**; starlet drops **j = 1** at every area. On safe scales, ℓ1 is
**×1.80** tighter at Stage IV, **×2.61** at full sky; peaks **×1.07** and **×1.17**. Nulling
retention: per-bin ℓ1 **0.16**, + product cross-maps **0.24**, joint ℓ1 **0.72**, CNN **~1**
(measured 0.96, quoted as *no measurable loss*).

**Deliberately not said.** Chapter 2's absolute FoM values (758 / 755 / 1947) — ratios only. The
inverse-volume conversion ×2.57⁴ ≈ 43.6: arithmetically right, reads as inflation, stays off the
slide *and* out of the mouth. The Chapter 3 timing table — the argument is that training happens
once, not that inference is fast; leading with speed invites the table, where PnPMass loses per
map. And the band labels printed on frame 35's figure, which are a thesis illustration at a finer
pixel scale than the analysis.

---
---

# Decisions and history

Three records of how the deck and this script got here. They sat in front of Act 0 until
2026-09-10. Nothing in them is spoken, and the frame numbers in their tables are the numbers of
the day each was written, not today's.

---

### Seven slides moved to backup, 2026-09-06

The main line is **54 frames**, down from 62. Seven left it for the backup section, each placed
beside its relatives rather than dumped at the end, so they can be found under questioning. **All
frame numbers in this file are the numbers after the move.**

| was | is now | slide | sits beside |
|---|---|---|---|
| 17 | **106** | *Every mass-mapping method is a Bayesian inference with a different prior on κ* — the Bayes slide | the LAM original of the same idea, 107 |
| 28 | **112** | *PnPMass on residuals* | the training slide, 114 |
| 29 | **113** | *Pixel-wise uncertainties from a second network, calibrated with conformal prediction* — the UQ chain | now a **vertical under 112**, as asked |
| 37 | **100** | *Peak counts* | the wavelet primer, 97–99 |
| 38 | **101** | *One starlet transform* | " |
| 39 | **102** | *The starlet ℓ1-norm* | " |
| 59 | **66** | *Nulling promises localized scale cuts* | the three BNT explainers, 68–70 |
| 60 | **67** | *The information is recoverable* | " |

**Frame 5 — the two tensions — stays where it is**, as a vertical under frame 4. It is skipped by
not pressing DOWN, which costs nothing and leaves it one keystroke away.

Their beats are kept above, in *Beats for the slides that are not in the main line*, marked SKIP, and are still audited against the deck at their new
numbers. **Two of them took material with them and it had to be rehomed** — see the banners on
**A1.8** (the word *prior*, the Part 3 pointer, the point-estimate flag) and **A4.6** (the whole
nulling thread).

> **Renumbered 2026-09-09.** The two tensions left the main line for backup 56 (Andreas), and a Part 3
> card went in at frame 40 the same day, so against the two tables above every main-line frame from
> the old 6 to the old 39 is one lower, and from the old 40 onward unchanged. Beat headings,
> act headers and the cut ladder carry the new numbers; the tables above are a dated record and were
> left as written. Backup numbers were already right. Same day: A1.6 to the close rewritten for
> clarity and register (`SCRIPT_PASS.md`).

---

## The animation policy — 2026-09-07

Andreas, after walking the deck: *"we clearly have overdone this."* The main line carried **97
clicks over 39 frames**, most of them revealing text in the order the eye reads it anyway. Every
build was audited against one rule:

> **A build survives only if it (a) withholds an answer the room should not read early, (b) swaps
> one thing for another in place, (c) moves focus around a diagram that stays on screen, or (d)
> *is* the animation** — a flipbook, or a canvas explainer stepped by markers.
>
> Anything that merely reveals text in reading order goes. The eye already does that, and every
> click is a moment you spend on the clicker instead of on the room.

**97 clicks → 67, across 31 frames.** Sixteen slides lost some or all of their build; two of them
were then put back, and both are marked below:

| frame | was | now | why |
|---|---|---|---|
| 3 | 4 | 1 | the pie→cone swap survives; the three annotations ride in with it and you point |
| 12 | 1 | 0 | a callout of extra detail |
| 16 | 4 | 0 | five methods read as a list **(Andreas)** |
| 17 | 2 | 1 | the proximal box survives; *how it solves* does not |
| 19 | 1 | 0 | a lead line under a diagram |
| 24 | 4 | 0 | a comparison table **(Andreas)** |
| 25 | 1 | 0 | one click for the whole body |
| 37 | 2 | 1 | the MCMC animation survives; the equation reveal does not |
| 38 | 2 | 1 | the faces survive; the bullet does not |
| 40 | 3 | 1 | the three-stage diagram goes up whole; *the cost is paid once* is still withheld |
| ~~45~~ | 8 | **8** | *stripped, then restored 2026-09-07.* Not a flipbook: the picture stays and the **highlight moves**, and what it moves through is the reason the bins are not independent. It was the one call in this audit I got wrong |
| 53 | 5 | 3 | **(Andreas)** the contour and its numbers are one beat: the bullets now land with the ℓ1-norm |
| ~~46~~ | 3 | **3** | *restored 2026-09-07* — route one wants the screen to itself before route two lands beside it |
| 51 | 7 | 0 | seven clicks of one plot **(Andreas)** |
| 52 | 1 | 0 | one click for the whole body |
| 55 | 1 | 0 | the conclusions go up whole |

**What survives, and why it earns the click.** Frame 9's four questions and frames 29/36's pipeline
focus move the light around a diagram that stays put. Frames 26 and 42/50 *are* animations — the
PnPMass iteration, and the two canvas explainers whose markers step them through their acts. Frame
30 swaps a video for a figure, frame 35 swaps each definition for its shape, frame 46 swaps the
mask for the joint definition. And frames 47 and 53 hold back an answer: the ladder to the tie, and
the contours on baryon-safe scales — **frame 53 Andreas named explicitly**, because that is where
Part 4's question gets its answer and the tension is worth keeping.

Single-click frames that survive are all the same shape: a claim withheld until the room has looked
at the figure (7, 8, 11, 14, 15, 18, 34, 39, 41, 44). Those are not builds, they are punchlines.

**If you add a fragment, put it through the rule first**, and re-run `measure-script.py` — it will
tell you if a cue has gone stale.

---

## What the script pass exposed

Four things that are deck problems, not script problems. They are listed here because the script
is where they became impossible to ignore, and each one is cheap to fix.

1. **There are no Part 3 and Part 4 dividers.** Frame 9 promises four parts; the deck names Parts 1
   and 2 on black dividers and then runs Parts 3 and 4 together behind one *movement II* opener at
   frame 28. The room is told there are four questions and then shown two labelled parts. Two
   divider slides would close it, and they are also the natural place to put the paper references
   for Papers 3 and 4, which currently appear only on the conclusions.
2. ~~Three slides define peak counts, the starlet transform and the ℓ1-norm that frame 35 then
   defines again, better, ninety seconds later~~ — **moved to backup 2026-09-06**, where they now
   sit at 100–102, after the wavelet primer, which is the order they should be read in. A3.10 opens
   with a bridge, since the wavelet excursion has become the room's first encounter with either
   statistic.
3. **Frame 26 is still seven clicks of PnPMass flipbook** with no notes, and `STRUCTURE.md` §5 has
   said since the Part 1 rebuild that it belongs in backup. Its partner has already gone to 112;
   this is the other half of the same block, and it is tier 1.
4. **Twelve slides' `aside class="notes"` carry `[CLICK]` counts that do not match their own
   fragments** — frame 39 says four clicks and has one, frame 37 says three and has two. The notes
   were written before the builds settled. This script is now the authority; the notes should be
   trimmed to pointers rather than maintained in parallel.
