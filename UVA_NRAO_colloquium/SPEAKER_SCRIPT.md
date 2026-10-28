# SPEAKER_SCRIPT — UVA Astronomy / NRAO colloquium, Thursday 29 October 2026

**`[CLICK]`** advance a fragment (⟨click⟩ inside a short path) · **▲** say verbatim · **bold** the
anchor to glance at · *italic* the word to lean on. Written 2026-10-28 for this deck, from the defence
script (`PhD_Defense_2026/SPEAKER_SCRIPT.md`), then revised the same day for register (Andreas: no
rhetorical set-ups, no cheesy phrases, scientific wording throughout).

## The budget

Measured at **121 wpm**, the rate of the defence rehearsal (2026-09-10). `tools/measure-script.py
UVA_NRAO_colloquium --wpm 121 --target 36:00` counts the spoken words, stamps each heading and checks
every `[CLICK]` against the deck. The printable version, with the Q&A sections and the scales cheat
sheet appended: `tools/print-script.py UVA_NRAO_colloquium --wpm 121 --qa`.

| part | frames | at 121 wpm |
|---|---|---|
| Introduction | 1–8 | 4:28 |
| Making the map | 9–25 | 11:42 |
| Reading the map | 26–45 | 10:21 |
| Feedback | 46–51 | 4:01 |
| Close | 52 | 1:41 |
| | | **32:13**, against a 36:00 target |

> **Read-through against delivery.** The defence ran 8 to 20 % over its read-through when delivered
> from memory. A 36:00 read-through lands at about 39 to 43 minutes, inside the 45-minute slot. The
> slack is deliberate.

---
---

# Act 1 — Introduction · frames 1–8

---

## I.1 — title · frame 1 · 0:29

Thank you for the introduction, and thank you all for coming.

I joined UVA a few weeks ago as a **GECO fellow**. Before that I did my PhD between Crete and CEA
Paris-Saclay, in the CosmoStat group. Today I will talk about methods for **trustworthy non-Gaussian
inference** in weak-lensing cosmology, for the surveys that are now taking data.

---

## I.2 — the picture · frame 2 · 0:18

In the standard picture, the Universe starts in a hot, nearly uniform state, with small density
fluctuations. As it expands, those fluctuations grow under gravity into the structure we observe
today: galaxies, clusters, and the cosmic web.

---

## I.3 — what ΛCDM is, and where it stops · frame 3 · 0:39

The model that describes this is ΛCDM: six free parameters, on top of a set of assumptions about
gravity, the geometry, the contents of the Universe and its initial conditions.

**▲** It fits a wide range of observations with remarkable precision.

[CLICK] **▲** But it is phenomenological rather than derived from first principles. About ninety-five
per cent of its energy content is in two **dark components** whose nature is unknown. And independent
probes of the same parameters now show **tensions** between them.

---

## I.4 — the probes · frame 4 · 0:12

Several probes test the model, through the geometry of the Universe and the growth of structure.

[CLICK] **▲** The one I work with is **weak gravitational lensing**.

---

## I.5 — strong and weak lensing · frame 5 · 0:33

Light from a distant galaxy is **deflected** by the mass along its path, so its image is distorted.
Near massive clusters this produces arcs and multiple images: the **strong** regime, which is rare.

**▲** Everywhere else the effect is **weak**: the shapes of background galaxies are distorted
coherently, by about a per cent. Measured over millions of galaxies, this distortion traces the total
matter distribution, dark matter included.

---

## I.6 — Euclid · frame 6 · 0:23

**Euclid** is an ESA mission, launched in 2023, that measures weak lensing and galaxy clustering
together: lensing from the visible imager, clustering from the near-infrared. It will cover about
**fourteen thousand square degrees**, a third of the sky, and measure the shapes of **billions of
galaxies**.

---

## I.7 — Euclid now · frame 7 · 0:54

The survey started in February 2024 and runs for six years. The first quick release, Q1, came out in
March 2025: sixty-three square degrees of deep fields, with twenty-six million galaxies. **Next
month** comes DR1-Foundation: about nineteen hundred square degrees of images, catalogues and spectra.
The weak-lensing and clustering products follow in **mid-2027**; these are the data the methods in
this talk are designed for. DR2 follows in 2029, and DR3, the full survey, in 2031.

[CLICK] On a common scale: Q1, DR1, DR2 and the full survey.

[CLICK] **▲** Euclid is one of three Stage IV lensing surveys now operating: Rubin's ten-year LSST
began in June, and Roman launched in August.

> Months only: ESA's dates are tentative, and DR1's exact day is not public. *If asked why the
> lensing products come a year after DR1:* the shapes are validated and calibrated first, and the
> cosmological analysis is run blind.

---

## I.8 — the analysis chain · frame 8 · 0:59

A survey analysis has many stages. This is the chain reduced to its final, scientific steps. We
start from the **galaxy shapes**, reconstruct a **map of the matter distribution**, compress the map
into a few **summary statistics**, and compare those with predictions or simulations to obtain the
posterior distribution of the cosmological parameters.

[CLICK] **▲** The first half of the talk is about **making the map**.

[CLICK] **▲** The second half is about **reading it**: extracting the cosmological information and
inferring the parameters.

Each of these steps can bias the result or misestimate the uncertainties. In the title,
**trustworthy** means unbiased, with calibrated uncertainties. **Non-Gaussian** refers to the
information beyond the two-point statistics of the standard analysis; I will come back to it.

---
---

# Act 2 — Making the map · frames 9–25

---

## M.1 — the first half · frame 9 · 0:17

The first half goes from the measured shear to a map of the matter. This is an ill-posed inverse
problem, so it depends on the prior we use, and the result needs an uncertainty.

---

## M.2 — shear and convergence · frame 10 · 0:36

Lensing changes the image of a galaxy in two ways: the **convergence**, an isotropic magnification,
and the **shear**, an anisotropic stretch. The convergence is **not directly observable**, since we
do not know the intrinsic size of a galaxy.

**▲** The shear is measurable. Intrinsic ellipticities are, to a good approximation, randomly
oriented, while the lensing distortion is **coherent** over neighbouring galaxies. Averaged over many
galaxies, the intrinsic part averages out, and the shear remains.

---

## M.3 — what the convergence is · frame 11 · 0:33

The convergence is the quantity we want. It is a **scalar field**, whereas the shear is spin-2, and
most of the statistics I will show later are defined on it. It is also directly physical: the
**projected matter density** along the line of sight, weighted by the lensing efficiency. Convergence
maps are therefore called **mass maps**.

This is a mass map I reconstructed from the **UNIONS** survey.

---

## M.4 — the same potential · frame 12 · 0:11

Shear and convergence are both second derivatives of the **lensing potential**, so in Fourier space
one is a **linear function** of the other.

---

## M.5 — the relation is exact, the measurement is not · frame 13 · 0:37

The relation is exact, but the data are not. The shear is estimated from galaxy shapes, which sample
the sky irregularly, carry shape noise much larger than the signal, and are missing in **masked**
regions, for example around bright stars.

Mass mapping is therefore an **ill-posed inverse problem**: many different maps are consistent with
the same data.

[CLICK] **▲** Selecting one requires a **prior** on the map, and the choice of prior is what
distinguishes the methods.

---

## M.6 — Kaiser–Squires · frame 14 · 0:34

The standard method, used for thirty years, is **Kaiser–Squires**: the linear inversion applied
directly to the measured shear. It has no free parameters, takes one FFT, and is exact for complete,
noiseless data.

[CLICK] On real data it **amplifies the shape noise** at small scales, and the mask **leaks** into the
whole map, since the operator is non-local. In practice the map is smoothed, which removes the
*small scales*.

---

## M.7 — interferometric imaging · frame 15 · 1:03

This is the same problem as **interferometric imaging**. In both cases the data are a linear
instrument response to the image we want, plus noise.

For an interferometer, the visibilities are the Fourier transform of the sky, sampled on the uv
coverage, plus thermal noise.

[CLICK] For lensing, the shear is the mass map through the shear operator and the mask, plus shape
noise much larger than the signal. These panels are a simulation with a real survey mask.

[CLICK] **▲** The direct inverse gives the **dirty image**, with its sidelobes; for us, the
Kaiser–Squires map, with its noise and its leakage at the mask edges. In both cases the solution is
regularised with a **prior**: CLEAN, maximum entropy or sparsity in radio; the Wiener filter,
sparsity or MCALens in lensing.

> *If asked where the analogy stops:* the radio gaps are in Fourier space, ours in real space, and
> every one of our pixels is noise-dominated. Our operator alone loses no information: a complete,
> noiseless field inverts exactly, up to its mean. The mean is unconstrained by the shear, the
> mass-sheet degeneracy, which corresponds to the missing zero spacing.

> **Tier-0 short path** (about −0:38). *This is the same problem as interferometric imaging: the data
> are a linear instrument response to the image, plus noise. ⟨click⟩ Here is ours, with the mask and
> the shape noise. ⟨click⟩ The direct inverse gives the dirty image, or our Kaiser–Squires map, and in
> both cases the solution is regularised with a prior.*

---

## M.8 — a data term plus a regulariser · frame 16 · 0:25

Every method can be written as an optimisation with two terms: a **data-fidelity term**, which
measures how well the map reproduces the shear, and a **regulariser**, which encodes the prior. The
data term is common to all methods; they differ in the prior and in how the problem is solved.

---

## M.9 — MCALens · frame 17 · 0:44

Among the methods with an explicit, hand-crafted prior, the state of the art is **MCALens**. It
models the convergence as the sum of **a Gaussian component**, estimated with a Wiener filter, and **a
sparse non-Gaussian component** that captures the peaks. The two are estimated by alternating
minimisation.

[CLICK] Each sub-problem is solved with a **proximal step**: a gradient step towards the measured
shear, followed by an operator that projects the result onto what the prior allows. In the method I
present next, this operator is replaced by a neural network.

---

## M.10 — the question · frame 18 · 0:32

Different priors give different maps, all consistent with the data. Until our study, mass-mapping
methods were compared on the **quality of the map**, its error against the truth in simulations. But
the map is an intermediate product; what we want are the **cosmological parameters**.

[CLICK] For Euclid this is a practical question: does an advanced reconstruction method **improve the
constraints** enough to justify its cost?

---

## M.11 — the experiment · frame 19 · 0:24

To answer it, we built a pipeline in which everything is **held fixed** except the mass-mapping
method: Euclid-like simulations, processed through the whole chain from shear to posterior, once per
method. I describe the later steps in the second half.

[CLICK] The **only thing that varies** is the reconstruction.

---

## M.12 — the maps · frame 20 · 0:28

These are reconstructions of the same simulated field, next to the truth. **Kaiser–Squires** is the
baseline planned for Euclid: mass mapping has been treated as a preprocessing step with little effect
on the cosmology, so the simplest method became the default. **MCALens** is the state of the art; it
recovers small-scale structure that Kaiser–Squires smooths out.

> *If asked about inpainting:* the paper also tests Kaiser–Squires with the mask inpainted first, the
> other Euclid baseline. It gives the same posterior as Kaiser–Squires, so it is left out here.

---

## M.13 — the answer · frame 21 · 1:01

This is the first corner plot, so briefly: each contour is the joint posterior of a *pair* of
parameters, each curve on the diagonal the marginal of one parameter, and the two shades enclose
**sixty-eight and ninety-five per cent** of the probability. Grey is Kaiser–Squires, blue is MCALens,
and **MCALens is tighter** on every parameter.

On the right, both quantities are given relative to Kaiser–Squires. The open diamonds are the map
error: MCALens improves it by **four per cent**. The filled diamonds are the figure of merit: it
increases by a factor of **two point six**, a hundred and fifty-seven per cent.

**▲** Map quality and constraining power are *different objectives*, and surveys should use advanced
reconstruction methods to make full use of their data.

---

## M.14 — where the gain comes from · frame 22 · 0:23

The gain comes from the small scales. As smaller scales are added, the Kaiser–Squires constraints
stop improving below **eight arcminutes**, while the MCALens constraints keep improving: MCALens
recovers the **small-scale structure** that Kaiser–Squires loses to noise. These scales come back in
the last part of the talk.

---

## M.15 — what a method needs · frame 23 · 1:02

Since the reconstruction affects the constraints, the next step was to develop a better method for a
survey like Euclid. This work was led by **Hubert Leterme**.

Such a method has **four requirements**. It has to be **accurate**, down to the small scales where
the gain comes from. **Flexible**: the mask and the noise vary between surveys and within one, so it
cannot require retraining for each configuration. **Fast**: the same reconstruction is applied to the
data and to every simulation used in the inference. And it has to provide **calibrated error bars**,
pixel by pixel.

[CLICK] **▲** No existing method meets all four. The model-based methods are flexible but less
accurate, or slow; deep networks are accurate, but must be retrained for every mask and noise level.

---

## M.16 — plug-and-play · frame 24 · 1:57

Our method, **PnPMass**, uses the **plug-and-play** framework. It is an iteration between two steps,
starting from an empty map.

[CLICK] **▲** The first is a gradient step towards the data. This step contains the **physical
model**: the shear operator, the mask, and the noise covariance. The result is a noisy map.

[CLICK] The second is a **denoiser**: a neural network trained once on simulations, which replaces
the proximal operator of the prior. It can represent a much more detailed prior than an analytical
one. The result is a clean map.

[CLICK] We iterate until the map converges to a **fixed point**, shown here next to the true map.
Because the mask and the noise enter only through the data step, the same trained network applies to
any survey configuration.

[CLICK] **▲** Without error bars, the map is of limited use: we cannot assess the significance of
individual peaks, or propagate its uncertainty into a downstream analysis. After convergence, a
**second network** predicts the error of each pixel in a single pass, without sampling.

[CLICK] **▲** A network's own error estimate carries no guarantee, so we calibrate it with
**conformal prediction**, on held-out simulations. These panels show the calibrated lower and upper
bounds minus the true map: the lower bound lies below the truth almost everywhere, and the upper
bound above it, at the nominal ninety-five per cent rate. I will not go into the details here, but I
am happy to discuss them afterwards.

> *If asked:* the second network is an order-2 moment network, trained once on the squared
> residuals, like the denoiser, on white noise; strictly, it takes one more data step from the
> converged map. The calibration is conformalised quantile regression. *If asked about radio:* the
> same plug-and-play approach is used for radio imaging (AIRI, Terris et al. 2023), with denoisers
> trained on optical, and even MRI, images.

> **Tier-0 short path** (about −1:36). *The method alternates two steps: ⟨click⟩ a gradient step
> towards the data, which contains the physical model, ⟨click⟩ and a denoiser trained once on
> simulations; ⟨click⟩ iterated to a fixed point. ⟨click⟩ A second network predicts the error of each
> pixel, ⟨click⟩ and conformal calibration guarantees their coverage.*

---

## M.17 — accurate, with the smallest calibrated error bars · frame 25 · 0:54

Both axes are relative to **DeepMass**, a network retrained for exactly this mask and noise; it sits
at the origin, and lower left is better.

[CLICK] In map error, PnPMass is within about **one per cent** of DeepMass.

[CLICK] These are the networks' own error bars, before calibration: the truth falls outside them too
often.

[CLICK] After calibration, every method's two-sigma intervals reach ninety-five per cent coverage, so
the methods are compared on the **width** of their intervals.

[CLICK] **▲** PnPMass has the **smallest calibrated error bars** of all. The other deep-learning
methods have to be retrained for every new mask and noise level; PnPMass is trained **once** and
applies to any configuration.

> *If asked, the limits:* the guarantee is marginal, not conditional, so the misses concentrate at
> the peaks; and κTNG is a single cosmology.

---
---

# Act 3 — Reading the map · frames 26–45

---

## R.1 — the second half · frame 26 · 0:14

The second half goes from the map to the cosmological parameters: statistics that capture more than
the power spectrum, simulation-based inference, and the small-scale systematics that limit both.

---

## R.2 — the map has to be compressed · frame 27 · 0:18

A map has of the order of a **hundred thousand correlated pixels**, too many to compare with theory
directly. [CLICK] We compress it into a **low-dimensional summary statistic**. [CLICK] The choice of
statistic *determines how much information is retained*.

---

## R.3 — the two-point function · frame 28 · 0:38

The standard statistic is the **two-point function**: the correlation of the shear between pairs of
galaxies as a function of separation, or, in harmonic space, the power spectrum.

[CLICK] All wide lensing surveys measure it, KiDS, DES, HSC, UNIONS, because it can be predicted
analytically, its covariance is well understood, and its systematics have been studied for two
decades.

[CLICK] **▲** For a Gaussian field, the power spectrum contains **all the information**. The late-time
density field is *not Gaussian*.

---

## R.4 — same power spectrum · frame 29 · 0:19

Gravitational collapse concentrates matter into haloes and filaments around voids. These two fields
have **the same power spectrum** but are clearly different, and a two-point analysis *cannot
distinguish them*. The information it misses is accessible to **higher-order statistics**.

---

## R.5 — the gain · frame 30 · 0:13

In forecasts, adding higher-order statistics to the power spectrum **significantly tightens the
constraints**. In Euclid, a dedicated group prepares these statistics for the first data release.

---

## R.6 — wavelets · frame 31 · 0:41

The statistics I use are built on **wavelets**. Where Fourier analysis decomposes a signal into
sines and cosines, a wavelet decomposition uses **localised, oscillating functions**, dilated and
translated, so each coefficient measures the structure of a given size at a given position.

[CLICK] This suits a mass map, which consists of localised structures with characteristic sizes.
Convolving the map with a small wavelet extracts its small-scale structure, and with a large one its
large-scale structure, so the map can be analysed **scale by scale**.

---

## R.7 — the two statistics · frame 32 · 1:12

We use an isotropic wavelet transform, the **starlet**, which decomposes the map into band-pass
images, each containing structure of one characteristic size.

[CLICK] This is one band, pixel by pixel: red above the local mean at that scale, blue below.

[CLICK] The first statistic keeps the **local maxima** and counts them as a function of height: the
**wavelet peak counts**. Peaks trace dark-matter haloes, whose abundance depends strongly on the
cosmology.

[CLICK] Peak counts discard the voids and filaments. The second statistic uses **every pixel**,
sorted by value: the histogram of the band.

[CLICK] Each pixel is weighted by its absolute value, so large coefficients dominate, and those near
zero contribute little.

[CLICK] **▲** Summing within each bin gives the **starlet ℓ1-norm**: the voids on the left, the peaks
on the right, one curve per band. It is a summary of the one-point distribution of the field in the
wavelet domain.

> *If asked (radio):* this is related to P(D) analysis: the distribution of all pixel values carries
> information below the detection threshold, beyond what the counts of detected sources give.

> **Tier-0 short path** (about −0:57). *⟨click⟩ One band. ⟨click⟩ Peak counts keep the local maxima.
> ⟨click⟩ ⟨click⟩ ⟨click⟩ The ℓ1-norm keeps every pixel, weighted by its absolute value, and sums
> them bin by bin, so it captures both voids and peaks.*

---

## R.8 — from the summary to the parameters · frame 33 · 0:08

To infer the parameters from these statistics, with all the uncertainties propagated, we use
**Bayesian inference**.

---

## R.9 — classical inference · frame 34 · 0:36

The posterior is proportional to the **likelihood times the prior**. The classical analysis assumes a
likelihood, usually Gaussian in the data vector, which requires a model for the mean and a covariance
matrix. For the power spectrum this is standard.

[CLICK] The posterior is then sampled with MCMC. For peak counts or the ℓ1-norm we have *neither* an
analytical model for the mean *nor* a justified Gaussian likelihood, so we need a different approach.

---

## R.10 — generative modelling · frame 35 · 0:22

That approach comes from **generative modelling**: learning an unknown distribution from samples
drawn from it, by fitting a parametric model. Once trained, the model can generate new samples and
**evaluate the density** at any point.

[CLICK] The same class of models underlies modern image generation.

---

## R.11 — normalizing flows · frame 36 · 0:23

We use **normalizing flows**: a sequence of **invertible** transformations, each parametrised by a
neural network, that maps a standard Gaussian onto the target distribution. Because each step is
invertible, the density follows from the change-of-variables formula, and the flow is trained by
maximum likelihood on the samples.

---

## R.12 — simulation-based inference · frame 37 · 0:33

For our statistics the likelihood cannot be written down, but **we can simulate**: given the
parameters, the simulator produces mock data, including their stochasticity. We draw parameters from
the prior, simulate, and keep the **pairs**.

[CLICK] These pairs train a **conditional flow**, which then models the posterior directly: given
the observed data, it returns the posterior. In Euclid, the weak-lensing group is preparing
simulation-based analyses of this kind.

---

## R.13 — how much can a summary keep · frame 38 · 0:42

We want the most informative summary. The ℓ1-norm outperforms the power spectrum.
[CLICK] But beating the power spectrum is "easy". **▲** The question is **how close to all of the
information** in the map a summary can get.

Since networks already perform the inference, a network can also learn the compression. That has
costs: it needs a large training set, it is hard to interpret, and a feature present in the
simulations but absent from the data can bias it unnoticed. But it provides the reference.

---

## R.14 — what optimal means · frame 39 · 0:29

A network **compresses** each map into a low-dimensional summary, and a flow maps the summary to a
posterior. [CLICK] The two are trained **jointly**, to maximise the **mutual information** between
the summary and the parameters. [CLICK] In principle, the network then retains *the maximum
information any summary of these maps can carry*, and that is the reference we compare against.

---

## R.15 — the setup · frame 40 · 0:15

This is the framework we built: the simulation-based pipeline from the maps to the parameters, the
analytical statistics, and the neural compressor. The two approaches share everything except the
summary.

---

## R.16 — the gap · frame 41 · 0:19

The first result: the network's figure of merit is **thirty-six per cent** higher, so the ℓ1-norm
loses part of the information.

[CLICK] But the comparison is *not symmetric*: the ℓ1-norm, as used so far, ignores a property of
these maps.

---

## R.17 — tomography · frame 42 · 0:49

That property is **tomography**. [CLICK] The source galaxies are divided into **redshift bins**.
[CLICK] The most distant bin [CLICK] is lensed by all the matter in front of it, [CLICK] which gives
its convergence map. [CLICK] A nearer bin [CLICK] is lensed by a shorter column of matter, [CLICK] and
gives another map.

[CLICK] **▲** There is one map per bin, but the maps are *not independent*: the same structures
appear in several of them. How the signal changes from bin to bin locates the matter along the line
of sight, and so constrains the growth of structure. A statistic computed on each map separately
cannot capture this.

---

## R.18 — route 1 · frame 43 · 0:34

For two-point statistics the extension is straightforward: one also correlates different bins. For
higher-order statistics there is no direct equivalent, and we tried two approaches. The first builds,
for each pair of bins, a new map that encodes their cross-bin structure, for example the
**pixel-wise product**, which is large only where both maps have structure at the same position. The
ℓ1-norm is then computed on these maps as well.

---

## R.19 — route 2, the joint ℓ1-norm · frame 44 · 1:06

The second approach changes the statistic itself. This is one wavelet scale, in two redshift bins of
the same field.

[CLICK] Each pixel has a coefficient in both bins: **one point in the plane**.

[CLICK] All pixels together form the **joint distribution**, correlated because the same matter
lenses both bins.

[CLICK] The two per-bin ℓ1-norms depend only on its **marginals**.

[CLICK] **▲** If we shuffle the pixels of one bin, the marginals are unchanged, but the joint
distribution is not. A per-bin statistic *cannot detect* the cross-bin structure.

[CLICK] We therefore bin the joint distribution on a grid,

[CLICK] and sum the ℓ1 weights of the pixels in each cell. This is the **joint ℓ1-norm**. The diagonal
cells correspond to pixels where both maps have similar amplitude; the off-diagonal cells, to pixels
where one is large and the other small.

> *If asked:* pairwise is the limit. A four-dimensional histogram over these pixels is almost
> everywhere empty, so genuine three- and four-bin structure remains with the network.

> **Tier-0 short path** (about −0:47). *⟨click⟩ Each pixel is a point in the plane, ⟨click⟩ all of
> them a joint distribution, ⟨click⟩ and the per-bin ℓ1-norms see only its marginals. ⟨click⟩
> Shuffling one bin leaves them unchanged. ⟨click⟩ ⟨click⟩ So we bin the joint distribution itself:
> the joint ℓ1-norm.*

---

## R.20 — the answer · frame 45 · 0:30

Same maps, same flow, four summaries. The per-bin ℓ1-norm. [CLICK] With the product maps added.
[CLICK] The joint ℓ1-norm. [CLICK] And the network, which falls almost exactly on the joint ℓ1-norm.

**▲** Since the network is trained to be information-optimal, the joint ℓ1-norm retains essentially
**all the cosmological information** in these maps. It requires no training, and each of its terms
has a direct interpretation.

---
---

# Act 4 — Feedback · frames 46–51

---

## F.1 — the scales of the signal and of the systematics · frame 46 · 0:51

So far the analysis was idealised. Real data contain **systematic effects**: physical or
observational effects that are not in the model, and that bias the result if they are not accounted
for.

**▲** The non-Gaussian information and most of these systematics are on **the same small scales**.
Where a systematic cannot be modelled reliably, the conservative option is to remove those scales.

[CLICK] In the *optimistic* case, only the smallest scales are affected, and most of the
non-Gaussian information survives. [CLICK] In the *pessimistic* case, the contamination extends to
larger scales, and after the cut the power spectrum performs as well as the higher-order statistics.

---

## F.2 — galaxy feedback · frame 47 · 0:58

The dominant astrophysical systematic on small scales is **baryonic feedback**: energy from active
galactic nuclei and supernovae expels gas from haloes and redistributes the matter on small scales.
This is the Illustris simulation: the dark matter, and the gas heated by feedback.

**▲** For galaxy evolution, feedback is a central subject of study. For this analysis it is a
systematic we cannot model reliably: the simulations we can afford for inference are dark-matter
only, and the feedback models disagree with one another.

[CLICK] This raises two questions. How much does unmodelled feedback bias the higher-order
statistics, as survey areas reach Stage IV? [CLICK] And once the affected scales are removed, do they
still add information beyond the power spectrum?

---

## F.3 — the pipeline · frame 48 · 0:21

The pipeline is the simulation-based one described before. [CLICK] Simulated maps at many
cosmologies, [CLICK] with Euclid-like noise and masks, [CLICK] the starlet transform, [CLICK] and a
flow that returns the posterior. Because the statistics are computed scale by scale, an affected
scale can be removed.

---

## F.4 — how large the bias is · frame 49 · 0:49

First, the bias without any mitigation. We train the flow on **dark-matter-only** maps, with no
baryon model, and apply it to an observation **that includes feedback**, for a range of survey areas.

For a survey of the previous generation, the bias is not significant. But the statistical errors
decrease with area while the systematic shift does not, so at Euclid's fourteen thousand square
degrees the bias reaches two point two sigma for the power spectrum, and three point six sigma for the
higher-order statistics, which are more sensitive to small scales.

[CLICK] **▲** With great statistical power comes great systematics responsibility.

---

## F.5 — the cuts · frame 50 · 0:23

We therefore remove small scales until the bias is below **zero point three sigma**. For the power
spectrum, this means keeping multipoles up to four hundred and sixty at Euclid's area. For the
wavelet statistics, the same approach, but removing the finest wavelet bands instead of multipoles.

---

## F.6 — after the cuts · frame 51 · 0:40

These are the Stage IV posteriors on the remaining scales. [CLICK] The power spectrum. [CLICK] Peak
counts. [CLICK] And the ℓ1-norm.

**▲** On these scales the ℓ1-norm still reaches a figure of merit **one point eight times** that of
the power spectrum, and **two point six** at full sky. The peak counts provide complementary
information, with different degeneracy directions.

**▲** The non-Gaussian information therefore persists on *quasi-linear* scales, without any baryon
model. With better feedback modelling, smaller scales could be included, where the gain is larger.

> The ×1.8 at Stage IV carries a ±0.6 band (`PAPER_FACTS.md` §4); if pressed, "about a factor of
> two". Peaks: ×1.07 at Stage IV, ×1.17 at full sky.

---
---

# Act 5 — Close · frame 52

---

## C.1 — conclusions · frame 52 · 1:41

To conclude. **Stage IV surveys are now operating**: Euclid and Rubin are taking data, and Roman has
launched. They will measure the shapes of billions of galaxies, and map the matter over a third of
the sky. At that statistical precision, the analysis methods and the systematics set the limit.

We need methods that make full use of the data: the choice of mass-mapping method alone changes the
figure of merit by a factor of more than two. **Learned priors combine well with the physical
model**: a network trained once, inside the physical model of the measurement, gives accurate maps for
any mask and noise level, with calibrated error bars.

**Non-Gaussian statistics** are needed to extract the full information of these surveys, and
interpretable wavelet statistics, read jointly across redshift bins, match an optimal neural network.
Small-scale astrophysics, above all baryonic feedback, has to be treated with care, but even on
scales unaffected by it the higher-order statistics add information beyond the power spectrum.

**▲** The methods are not specific to lensing: learned priors with calibrated uncertainties, and
inference beyond the power spectrum, apply to radio imaging, to 21-centimetre cosmology, and to other
inverse problems with a known instrument and noise model.

Thank you.

---
---

# Cut ladder

Measured by `tools/measure-script.py`; each saving is the words dropped at 121 wpm.

- **Tier 0, the short paths** written above. The slide stays; the narration shortens: M.7 −0:38, M.16
  −1:36, R.7 −0:57, R.19 −0:47; all four −3:57.
- **Tier 1**, fold a framing slide into the next one's first sentence: the potential (M.4) into M.3;
  the step to the parameters (R.8) into R.9; the setup (R.15) into R.16; the pipeline (F.3) into F.4.
  About −1:00 for all four.
- **Tier 2**, a slide in one sentence: the forecasts (R.5); normalizing flows (R.11), "a flow is a
  learned, invertible map from a Gaussian to the target distribution"; route 1 (R.18), "one approach
  combines pairs of bins into new maps, the other changes the statistic". About −0:55 for all three.
- **Never cut**: the radio analogy (M.7), the answer (M.13), the loop (M.16), the joint ℓ1 and its
  result (R.19, R.20), the result after the cuts (F.6), the conclusions.

---
---

# Q&A — the five to rehearse aloud

The questions this room is most likely to ask and least forgiving about. ⚠ marks an answer whose
honest core is a limitation: say it plainly, then the next step.

**"How is PnPMass different from AIRI or R2D2?"**
It is the same family: a learned denoiser inside a forward–backward iteration, as in AIRI. What is
specific to ours is the spin-2 lensing operator; a single denoiser trained once on white noise over
a range of levels, which works for any noise covariance and footprint because of how the gradient
step is preconditioned; and per-pixel error bars with a calibrated coverage. (Backup 69–70.)

**⚠ "Does the iteration provably converge?"**
Formally, it converges linearly to a unique fixed point if the step size is below a bound set by the
operator, here 0.176, and the denoiser is mean-preserving and non-expansive. The mean is enforced by
construction. Non-expansiveness is not enforced, because constraining the spectral norm of the
network's Jacobian during training is expensive, so the guarantee is formal. In practice it converges
in a few iterations.

**⚠ "Your coverage guarantee holds on simulations. What does it guarantee on real data?"**
Conformal calibration assumes the calibration maps and the data come from the same distribution. If
the simulations miss part of the physics, the guarantee does not transfer. That gap is exactly what
"trustworthy" has to address next: testing the simulations against the data, and calibration that
is robust to such shifts.

**⚠ "Which feedback model did you use, and would a stronger one change the conclusion?"**
One baryonification model, with fixed parameters. Stronger feedback would push the cuts to larger
scales and reduce the gain, so the result is conditional on that model. The next step is a range of
feedback strengths, or marginalising over the baryonic parameters instead of cutting.

**⚠ "Is the network really optimal? A better one might beat the joint ℓ1-norm."**
The training objective maximises a lower bound on the mutual information, so the network is the best
compression we could train, not an absolute bound. We tried several architectures, and a ResNet-18
was best. The maps were also fairly coarse, 7.5-arcminute pixels; at finer resolution a network may
gain more.

---

# Q&A — Euclid

Public facts only (`PAPER_FACTS.md` §9). Months, never days; nothing from Consortium meetings.

**"When can people use the data?"**
Q1, sixty-three square degrees of deep fields, has been public since March 2025. The next release,
DR1-Foundation, is due next month: about nineteen hundred square degrees of images, catalogues and
spectra. The weak-lensing and clustering products follow in mid-2027, DR2 in 2029 and DR3, the full
survey, in 2031. ESA describes these dates as tentative.

**"What does Euclid do that Rubin cannot, and the other way round?"**
From space the point-spread function is small and stable, about 0.16 arcseconds with 0.1-arcsecond
pixels, so galaxy shapes are measured with a PSF several times smaller than from the ground. Rubin
goes deeper over a larger area, about eighteen thousand square degrees, in six optical bands, which
helps the photometric redshifts. The two are complementary, and joint analyses are planned.

**"How do you get the redshifts?"**
Photometrically: Euclid's near-infrared photometry combined with ground-based optical imaging, UNIONS
in the north, and DES and later Rubin in the south. The galaxies are then divided into tomographic
bins.

**"How many galaxies?"**
The requirement is at least thirty per square arcminute for lensing; over fourteen thousand square
degrees, that is of order one and a half billion.

**"What limits Euclid's lensing analysis?"**
Systematics: the PSF model, the calibration of the shear measurement and of the photometric
redshifts, intrinsic alignments, blending, detector effects, and on small scales baryonic feedback,
the subject of the last part.

**"Will higher-order statistics be part of Euclid's cosmology?"**
Euclid has a group dedicated to them. A public forecast for a DR1-like setup (Euclid preparation,
Vinciguerra et al. 2026) found that each of five higher-order statistics, including the ℓ1-norm and
peak counts, tightens w0 by about a factor of 2.5 relative to the shear two-point functions. Which
statistics enter the official analysis is decided within the collaboration.

> Andreas is a co-author of that forecast; mention only if asked (Andreas: a detail).

**"How does Euclid compare with current surveys?"**
Current lensing surveys cover hundreds to a few thousand square degrees: KiDS about a thousand, DES
Year 3 about four thousand, HSC a few hundred. Euclid covers about fourteen thousand, with space-based
shapes.

**"Euclid also measures clustering. How do the two combine?"**
Lensing comes from the visible imager; clustering from slitless near-infrared spectroscopy of
Hα-emitting galaxies, at redshifts of roughly one to two, and from the photometric sample. Combining
lensing, galaxy–galaxy lensing and clustering breaks degeneracies, for example between the growth
of structure and the geometry.

**"Is the UNIONS map on your slide Euclid data?"**
No. UNIONS is a ground-based survey of the northern sky, which also provides optical photometry for
Euclid's photometric redshifts. The map is from UNIONS's own shape catalogue.

---

# Q&A — physical scales, a cheat sheet

Approximate, at z ≈ 0.5, where the lensing of z ≈ 1 sources peaks; proper distances (`PAPER_FACTS.md`
§10 has the exact values).

**1′ ≈ 0.4 Mpc.**

**2′–4′ ≈ 1–1.5 Mpc:** cluster-sized haloes, where the first study's gain comes from.

**8′ ≈ 3 Mpc, k ≈ 1 h/Mpc:** below it, Kaiser–Squires gains nothing.

**ℓ ≈ 460 ≈ 20′ ≈ 9 Mpc, k ≈ 0.3 h/Mpc:** the power-spectrum cut at Euclid's area.

**Finest wavelet band ≈ 10′ ≈ 4 Mpc:** the one removed; the rest are ≈ 20′–80′, 8–30 Mpc.

**Feedback:** ~1 % suppression of the power spectrum from k ≈ 0.3 h/Mpc, 10–30 % at k ≈ 1–10.

**Averaging ellipticities:** ~700 galaxies to detect a 1 % shear, a ~5′ × 5′ patch, ~2 Mpc.

**Euclid's PSF ≈ 0.16″ ≈ 1 kpc.**

**ℓ ↔ angle:** θ ≈ π/ℓ, so ℓ = 1000 ≈ 10′.

---

# Q&A — radio and imaging (NRAO, ALMA)

**"Is there a regularisation weight to tune, like CLEAN's gain and threshold?"**
No. The step size is set by the spectrum of the operator, and the denoiser takes the corresponding
noise level as an input. The strength of the prior is set by the training distribution, not by a
hand-tuned weight.

**"What is the noise model? White, correlated?"**
Shape noise is independent between galaxies, so the covariance is diagonal: the ellipticity variance
over the number of galaxies in each pixel, and a very large variance in the masked pixels. The
gradient step is preconditioned so that the noise the denoiser sees is white, which is why one
network trained on white noise works for any covariance. For radio data, correlated image-plane
noise would enter through a data term in the visibility domain.

**"Does the denoiser invent structure, in the masked regions for example?"**
Inside the mask the data carry no information, so the map there comes from the prior; the predicted
error is correspondingly larger, and the downstream analyses exclude the masked areas. Elsewhere the
fixed point has to stay consistent with the measured shear. The calibration is marginal, so the
misses concentrate at the peaks.

**⚠ "Could conformal calibration work for interferometric images, without a ground truth?"**
It needs calibration examples with a known truth, so simulated skies passed through the instrument's
forward model: the uv coverage and the noise. The guarantee then holds to the extent that the
simulated skies are representative. In cosmology we have simulations built for that purpose; for
radio, the sky model is the harder part.

**"How do you fix the mean, your equivalent of the missing zero spacing?"**
The map is reconstructed with zero mean; the denoiser's output is mean-centred. The statistics are
computed on wavelet bands, which have zero mean, so a constant offset does not affect them.

**"What does it cost?"**
Training takes about a day and a half for the denoiser and two days for the error network, on one
GPU, once. A map with its error bars then takes under a minute, and the calibration about two
minutes. DeepMass is faster per map, seven seconds, but has to be retrained, about two days, for
every new mask and noise level.

**⚠ "Does it scale to Euclid's full sky?"**
The current version works on flat 5×5-degree fields. A spherical version is the next step.
(Backup 111.)

**"Why not reconstruct from the galaxy catalogue directly?"**
Binning the shapes into pixels is the analogue of gridding visibilities, and the pixel noise variance
follows from the number of galaxies in each pixel. A catalogue-level forward model is possible, at a
higher cost.

---

# Q&A — galaxy evolution and theory (GECO, VITA)

**"Instead of removing the feedback scales, could you measure feedback with them?"**
In principle, yes: with feedback parameters in the forward simulations, the same statistics would
constrain them. Baryonification is about a thousand times faster than particle-based methods, which
makes such simulation suites feasible. That is future work, not a result.

**⚠ "The mass-mapping prior was learned from simulations. Does it depend on their feedback model?"**
Yes, potentially. The PnPMass denoiser was trained on IllustrisTNG maps, so its prior includes TNG's
feedback. Testing it on simulations with a different feedback model, and at other cosmologies, is
needed before using it on data; the paper names robustness across cosmologies as the first open
direction.

**"Do the peaks correspond to haloes?"**
The high signal-to-noise peaks mostly do, to single massive haloes. Lower ones are often projections
of several structures along the line of sight, or noise. The statistic uses them as a population, so
all of them carry cosmological information without being identified individually.

**"Massive neutrinos also suppress small-scale power. Are they degenerate with feedback?"**
They are, partly. The forecast I showed included the neutrino mass, and higher-order statistics
tightened it. In the feedback study the neutrino mass was not varied.

**⚠ "Intrinsic alignments are a small-scale effect too. Are they included?"**
No. They are not in these simulations; forward-modelling them at map level is on the list, with
photometric redshifts and source clustering. (Backup 110.)

**"Are dark-matter-only simulations adequate after the cut?"**
By construction, for this baryon model: we cut until the bias, measured on an observation with
feedback, is below 0.3 sigma at each survey area.

---

# Q&A — cosmology and the CMB (Simons Observatory)

**"What does this say about the S8 tension?"**
Nothing directly; there is no new measurement here. But one proposed explanation for the lower
lensing S8 is stronger feedback suppressing small-scale power, and those small scales are exactly
where cosmology and feedback are degenerate for these statistics. (Backup 55, 57.)

**"Could you apply this to CMB lensing, or cross-correlate with it?"**
The same statistics apply to CMB lensing convergence maps, and cross-correlations with galaxy lensing
help calibrate the shear and the redshifts. It is not part of this work.

**⚠ "In the first study you used a Gaussian likelihood for peak counts, but later you said it is not
justified."**
The first study used an emulator with a Gaussian likelihood and a simulated covariance, standard at
the time. All the methods shared it, so the relative comparison holds; the later studies use
simulation-based inference.

**"Does the choice of mass map matter for the power spectrum?"**
The power spectrum is measured from the shear directly, without a map. The mass-mapping choice
matters for map-based statistics; the first study used peak statistics.

**"Isn't 157 per cent suspiciously large?"**
The figure of merit here is the fourth root of the Fisher determinant over the four parameters, so a
factor of two point six corresponds to error bars about one point six times smaller per parameter,
on average. It is also a ratio between two chains that differ in a single step, so systematics that
would affect an absolute number cancel.

> **To confirm with Andreas** (STRUCTURE.md, open item "the ×2.6 interpretation"): FoM ∝
> (det C)^(−1/4) (PAPER_FACTS §0), so a uniform factor r on the four σ gives FoM ratio r², and
> ×2.57 ↔ r ≈ √2.57 ≈ 1.6. The ledger's "like a σ ratio" reads it as r = 2.57.

**"Can I compare the numbers across your three studies?"**
No: they use three different simulation suites and survey geometries. Compare relative values within
each study.

---

# Q&A — statistics, machine learning, the ISM

**"How do you check the posteriors?"**
Every posterior is tested for coverage on simulated observations with known parameters, with TARP and
simulation-based calibration. (Backup 93–94.)

**"Your per-pixel intervals: do they give the significance of a peak?"**
Not directly. They are marginal and pixel-wise, not a joint band over the map, and they do not encode
the correlations between pixels that a peak's significance needs.

**"Why normalizing flows, and not other density estimators?"**
They give exact densities and fast sampling, and neural posterior estimation with flows is
well-tested. Other estimators would also work.

**"How many simulations did you need?"**
For the comparison with the network, 899 cosmologies, about three hundred thousand patches. For the
feedback study, the full suite of two and a half thousand cosmologies.

**"How does the ℓ1-norm relate to the scattering transform?"**
The mean absolute wavelet coefficient in a band is the first-order scattering coefficient. The
ℓ1-norm resolves it by amplitude, so it keeps the shape of the distribution; scattering adds second-
order terms that couple scales, while the joint ℓ1-norm couples redshift bins.

**"Could the same statistics be used on dust, HI or molecular-cloud maps?"**
Yes. Multiscale statistics of this kind, and scattering transforms, are already used for the
interstellar medium and turbulence; the "same power spectrum, different fields" problem is the same
one. (Backup 81, on the phases.)

---

# Q&A — anyone

**"When will you apply this to Euclid data?"**
The weak-lensing products are planned for mid-2027. Everything I showed is on simulations, by design,
since validating a reconstruction requires the truth. What transfers directly is PnPMass, which is
trained once and takes the mask and noise only at inference, and the ℓ1-norm pipeline, which needs
the simulations run at the survey's noise level and footprint.

**"Will Euclid use these methods?"**
They are developed with Euclid in mind, and the collaboration has groups working on higher-order
statistics and on simulation-based inference. Which methods enter the official analysis is decided
within the collaboration.

**"How do you know the machine learning does not invent structure?"**
In the reconstruction, the network is one step of an iteration whose other step enforces consistency
with the measured shear. For the inference, the trained flow evaluates a new observation in
milliseconds, so we test it on thousands of simulated observations with known parameters and check
the coverage of the posteriors.

**"Why the ℓ1-norm, rather than the sum of squares?"**
The sum of squares in a band is a band power, which is two-point information. The ℓ1-norm, binned by
coefficient value, retains the shape of the distribution, including its tails, which is where the
non-Gaussian information is.

**"Why weak lensing rather than galaxy clustering?"**
Lensing responds to the total matter, so no galaxy-bias model is needed between the observable and
the matter field. It is also sensitive to both the geometry and the growth of structure.

**"What is the most important result?"**
That analysis choices treated as neutral are not: the reconstruction method and the summary statistic
both change the constraints, and with calibrated methods we can extract more of the information and
quantify how far to trust it.

---

# Numbers used, and where they are ledgered

Every number said above is in `PAPER_FACTS.md`: the Euclid dates and areas, Rubin and Roman (§9); the
157 %, ×2.6 and 4 % (§2); PnPMass within about 1 % of DeepMass, the 95 % coverage, the smallest
calibrated bars (§3); 36 % for the network (§5); 2.2σ and 3.6σ at 14,000 deg², the 0.3σ threshold,
ℓ_max = 460, ×1.8 and ×2.6 on the remaining scales (§4). In the Q&A: the PnPMass timings, κTNG and
the step-size bound (§3 and the paper), the baryonification model and the 2,500 cosmologies (§4), the
899 cosmologies and 7.5′ pixels of the network comparison (§5); the Euclid instrument facts
(§9) and the physical scales (§10).
