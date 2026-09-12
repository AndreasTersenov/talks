# SPEAKER NOTES — rehearsal cues

Keywords only, one block per frame. **»** advance a fragment · **▲** say this one verbatim ·
**bold** is a number or name to get exactly right — the same three marks the script uses.

Written by hand from `SPEAKER_SCRIPT.md` on 2026-09-12. It does **not** regenerate: if a beat
changes there, edit the matching block here. `python3 tools/print-notes.py PhD_Defense_2026`
rebuilds the printable HTML and PDF.

---

## Act 0 — the setup · 1–7

**1 · title**
- thanks — committee, for reading and being here
- **3 years**; trustworthy non-Gaussian inference for weak-lensing cosmology

**2 · the picture**
- hot, almost uniform, small density fluctuations
- expands; fluctuations grow under gravity → galaxies, clusters, cosmic web

**3 · ΛCDM**
- **six** free parameters
- assumptions: GR · homogeneous+isotropic on large scales · inflation, near-Gaussian, adiabatic · baryons + CDM + Λ
- ▲ extremely successful — six numbers fit everything to remarkable precision
- **»** but not satisfactory: phenomenological not first-principles · **95 %** is two dark components · tensions between probes

**4 · the probes**
- several probes test a model like that
- **»** ▲ ours is gravitational lensing

**5 · strong and weak**
- light bends passing the mass on the way to us → distorted image
- dramatic = arcs, rings, multiple images — **strong**, very rare
- ▲ **weak** happens everywhere: every galaxy slightly changed → how matter, incl. dark, is distributed

**6 · Euclid**
- launched **2023**, taking data now
- **billions of galaxies**, **a third of the sky**, ~**order of magnitude** more statistical power
- **»** ▲ signal encodes growth of structure + geometry since the Big Bang
- but needs sophisticated algorithms and statistics — that is this thesis

**7 · the chain**
- analyses are incredibly complex; this is the last steps, the scientific part
- shapes in → mass map → summary statistics → compare to theory/sims → posterior
- **»** ▲ first half, first two papers = **making the map**
- **»** ▲ second half, last two papers = everything after it
- every step can bias or distort → trustworthy needs quantified, calibrated, unbiased

---

## Act 1 — does the map matter? · 8–20

**8 · Part 1 divider**
- first paper — but to motivate it, back to weak-lensing basics

**9 · shear and convergence**
- convergence = isotropic magnification; shear = anisotropic stretching
- convergence **not directly observable**
- ▲ lensing is **coherent**, intrinsic shapes **random** → average many galaxies, random cancels, shear remains

**10 · what convergence is**
- **scalar** field (shear is spin-2) — easier; most HOS only defined on κ
- **projected matter** along the line of sight, weighted by lensing efficiency
- → convergence maps = **mass maps**
- real example: **UNIONS**

**11 · same potential**
- both are second derivatives of the **lensing potential** (projection of the gravitational potential)
- Fourier space → simple linear relation

**12 · exact relation, imperfect data**
- irregular sampling · noise **much larger than the shear** · masks
- → **ill-posed inverse problem**: several visibly different solutions fit the data
- **»** ▲ need an assumption about what κ looks like

**13 · Kaiser–Squires**
- linear inversion applied directly; **thirty years**, almost every survey, for simplicity
- **»** amplifies shape noise at small scales · mask leakage across the whole map (non-local operator)
- pure KS almost unreadable → Gaussian filtering in practice, at the cost of small scales

**14 · data term + regulariser**
- every method = optimisation: **data fidelity** + **regulariser (the prior)**
- data term is the **same for all**; what changes is the prior on κ and how it is solved

**15 · MCALens**
- state of the art among **model-driven** (hand-crafted prior)
- κ = **Gaussian** (Wiener filter) + **non-Gaussian** (the peaks)
- **alternating minimisation** — solve one holding the other, iterate to convergence
- **»** each sub-problem is a **proximal step**: gradient towards the shear, then operator pulling back to the prior

**16 · the question**
- until this paper methods were compared on **map quality** — MSE against the truth
- but the map is not the final product; we care about the **parameters**
- **»** practical for Euclid: is an advanced method **worth the effort**, or is any reasonable one good enough?

**17 · the experiment**
- everything **held fixed** except the mass-mapping method
- **cosmo-SLICS**, Euclid-like, whole chain shear → posterior per method
- details come back in Parts 3 and 4
- **»** the only thing that varies is the reconstruction

**18 · the three maps**
- baselines: **KS**, and **KS + inpainting** (fills the mask to match the field statistically, meant to cut leakage)
- these two are what **Euclid** plans — mass mapping treated as preprocessing, so the simplest became default
- **MCALens** is the state of the art
- so what posteriors do they give?

**19 · the answer**  ← first corner plot, take your time
- explain the plot: off-diagonal = joint distribution of a pair; diagonal = one parameter; two shades = **68 and 95 %**; smaller = more precise
- **inpainting makes no difference** — grey and red almost identical, grey hard to see behind the red
- **MCALens visibly tighter on every parameter**
- stems: both are improvement over KS. **open** = RMSE, **4 %** better. **filled** = constraining power, **×2.6**, **160 %**
- map quality and constraining power are **not the same objective**
- → surveys should use advanced reconstruction to maximise scientific output

**20 · where the gain comes from**
- add smaller and smaller scales: KS **saturates below 8′**; MCALens keeps improving
- MCALens recovers the **small-scale structure** KS loses to noise

---

## Act 2 — PnPMass · 21–24

**21 · Part 2 divider**
- reconstruction matters → motivation to build the best one we can
- this paper led by **Hubert Leterme**

**22 · what we want**
- obvious place to look is **deep learning** — tried, and it works
- **four things**: accurate · flexible (same model when noise or mask changes) · fast · fast uncertainty quantification
- **none of the existing methods have all four**

**23 · plug-and-play**
- from the optimisation literature; inverse problem with a **learned** prior, very flexible
- start from the Part 1 iteration: gradient step on the data term, then proximal step
- PnP replaces the proximal operator with a **deep denoiser** trained on simulations → converges to a **fixed point**
- better than analytical priors: the denoiser learns a far more complex, realistic prior
- **Swin transformer**, **7 million** parameters, trained once on white Gaussian noise over a range of levels
- ▲ noise covariance and mask enter **only in the data term, at inference** → same network for any noise, any footprint. That is the flexibility
- walk-through: two shear components, κ initialised at zero → **forward** (gradient) gives a noisy map → **backward** (denoiser) projects onto realistic mass maps
- **»** output fed back, iterate to convergence
- *short path if behind: eight iterations, alternating data step and denoiser; residual variant slightly better, in the backup*

**24 · accurate, calibrated**
- accurate maps **and** error bars, **perfectly calibrated, with mathematical guarantees**
- via **moment networks** + **conformalized quantile regression**
- axes: x = reconstruction error, y = size of calibrated bars → **lower left is better**
- colour = miscoverage: circles above target before, every diamond on it after. Not *who covers* — everyone covers, that is the guarantee — but who covers with the **tightest bars**
- ▲ accuracy within **~1 %** of **DeepMass**, trained for that exact mask and noise; **smallest calibrated bars** of all
- **»** DeepMass needs retraining per mask/noise → not applicable to a real survey; PnPMass trained **once**, any field

---

## Act 3 — the summaries · 25–44

**25 · the second half**
- what comes after the map: the **summary statistic**, and inference from it
- so far the statistic was **held fixed on purpose** — nothing that moved could be blamed on it. Now it is the subject

**26 · compression**
- map is ~**a hundred thousand correlated pixels** — very hard to use directly
- **»** compress to a low-dimensional summary
- **»** the choice determines how much information is kept

**27 · two-point**
- standard: **two-point correlation function** — ξ± in real space, power spectrum in harmonic
- **»** every flagship result of the decade — **KiDS, DES, HSC** — is two-point: analytic prediction, understood covariance, two decades of systematics work
- **»** ▲ for a **Gaussian** field the power spectrum is **sufficient**. The late-time field is not Gaussian

**28 · same power spectrum**
- collapse and non-linear growth → haloes and filaments around voids
- these two completely different fields have **the same power spectrum** — two-point cannot tell them apart
- → need **higher-order**: peaks, wavelets, ℓ1-norm, Minkowski functionals

**29 · the gain**
- forecasts on simulations: adding HOS to the power spectrum **significantly improves** the constraints

**30 · wavelets**  ← the parenthesis
- Fourier uses sines and cosines; wavelets are **localised, oscillating**, **dilated and translated**
- coefficient at scale *a*, position *b* = how much structure of size *a* sits at *b*
- **»** suited to convergence maps — localised structures with a characteristic size and position. Small wavelet → small-scale structure; large → large-scale
- each band covers a different frequency range → study **scale by scale**, largely independent

**31 · the two statistics**
- both start from the wavelet decomposition, isotropic wavelet called the **starlet**
- transform → set of **band-pass images**, each a characteristic angular size
- **»** count peaks on each band, histogram their amplitudes = **wavelet peak counts**
- **»** sensitive to non-Gaussian features; peaks ↔ dark matter haloes, whose abundance depends strongly on cosmology
- **»** but counting peaks throws away voids, filaments, the rest → sum the **absolute values** of all coefficients per band, histogram those = **starlet ℓ1-norm**
- **»** think of it as a **PDF of the field in the wavelet domain**

**32 · to the parameters**
- compare the statistic with predictions under different cosmologies
- to carry all the uncertainties: **Bayesian statistics**

**33 · classical inference**
- Bayes: posterior ∝ **likelihood × prior**
- classical writes the likelihood **analytically**, usually Gaussian in the data vector → needs a mean prediction and a covariance. Works for the power spectrum
- **»** sample with **MCMC**
- for peaks or ℓ1: **neither** an analytic mean **nor** a Gaussian likelihood → different route

**34 · generative modelling**
- unknown distribution, but we have samples from it → fit a parametric model
- once trained: generate new samples, **and evaluate the density**
- **»** the family behind image generation; look how far they have come

**35 · normalizing flows**
- start from a unit Gaussian → target, through **simple invertible transformations**, each a neural network
- invertible → density from the **change-of-variables formula**; trained to maximise the likelihood of the samples
- the flow learns from samples how to turn a Gaussian into the target

**36 · simulation-based inference**
- no analytic likelihood, but **we have a simulator** — parameters in, simulated data out, with all the stochasticity
- draw from the prior, run, keep the **(parameter, data) pairs**
- **»** those train a **conditional** flow → the flow **is** the posterior. Give it the real observation, get the posterior

**37 · Part 3 divider**
- **third question**: how much information do the statistics keep, and can HOS extract *all* of it?

**38 · why build a statistic by hand**
- ℓ1 beats the power spectrum — **»** but that is "easy". Real question is **how close to all of it**
- we already use networks for inference — why not learn the compression too?
- **reasons to be careful**: needs a lot of training data · hard to interpret · generalises less predictably — a feature in the sims but not the data biases the result unnoticed
- the theoretically optimal way: build the network into the SBI pipeline, train it with the flow — **VMIM**

**39 · what optimal means**
- network = **compressor**, maps → low-dimensional summary; flow maps summary → posterior
- **»** trained together to maximise the **mutual information** between summary and parameters ≡ maximising the expected log posterior
- **»** so in theory it estimates the **most information any summary of these maps can carry**
- → compare our analytical HOS against that

**40 · the setup**
- most of the work in this paper is in this figure — the whole SBI pipeline, maps to parameters, plus both the analytical statistics and the neural compressor (many architectures, always VMIM)
- the two approaches share **everything apart from the summary**

**41 · the gap**
- first result: not far apart, but the CNN wins by **36 %** in FoM → ℓ1 loses part of the information
- **»** but the comparison is **not symmetric** — a property of these maps the ℓ1 does not yet use

**42 · tomography**  ← eight clicks, one per build step
- sources sliced into **redshift bins**
- **»** most distant bin **»** lensed by all the matter in front **»** gives its map **»** a nearer bin **»** shorter column **»** another map **»** one map per bin, **not independent** — the same structure appears in several
- how the signal changes bin to bin says where the matter sits along the line of sight → how structure grew
- a **per-bin** statistic cannot see it

**43 · two routes**
- two-point extends easily — cross-bin correlations. For HOS there is no obvious equivalent
- **first**: extra maps for the cross structure — multiply each pair of bins pixel by pixel; strong only where **both** have structure at the same place. Compute the ℓ1 on those too
- **»** **second**: change the statistic — generalise the ℓ1 from one map to a **pair** of bins
- each pixel has a coefficient in each map → instead of one histogram per map (the two curves on the axes) **»** one **two-dimensional** histogram over the pair
- **diagonal** cells = both maps equally strong; **off-diagonal** = one strong, one weak

**44 · the answer**
- same maps, same flow, four summaries: per-bin ℓ1 **»** + product cross-maps **»** joint ℓ1 **»** CNN — falls almost perfectly on the joint ℓ1
- network was trained to be information-optimal → the **joint ℓ1 essentially encodes all the cosmologically useful information**
- and with **no training** — efficient, interpretable, robust

---

## Act 4 — baryons · 45–50

**45 · Part 4 divider**
- HOS work well in idealised cases → final paper, a **messy, realistic** scenario

**46 · the collision of scales**  ← longest beat, 2:13
- systematics = in the measurement, not in the model; instrumental or physical. Unmodelled → biased result
- most groups check the **data vector**. Not enough — what matters is the effect on the **posterior**
- dominant astrophysical one at small scales: **baryonic feedback** — AGN and supernovae push gas out of haloes, suppressing small scales
- our inference sims are **dark-matter-only**, and feedback models disagree → cannot model reliably
- the problem: non-Gaussian information and contamination live on **the same small scales** → conservative answer is to cut them
- **»** *optimistic*: only the smallest scales contaminated, most of the information survives
- **»** *pessimistic*: contamination reaches further, and after the cut the power spectrum does just as well
- two questions: how much does unmodelled feedback bias HOS, and how does it grow with area — and after the cut is there anything left over the power spectrum

**47 · the pipeline**
- same SBI pipeline as the previous paper
- **»** maps at different cosmologies **»** Euclid-like noise and masks **»** starlet transform **»** data vector conditions a flow
- one difference

**48 · how large the bias is**
- **CosmoGrid** gives every realisation with and without feedback → train the flow on **dark-matter-only** (no baryon model at all), feed it a **baryonified** observation
- run across survey areas to see how the bias evolves
- previous-generation area: not significant. Errors shrink with area, systematic does not → **Euclid: really bad**; full sky worse
- ▲ HOS more biased than the power spectrum — more sensitive to the contaminated small scales

**49 · the cuts**
- remove small scales until the bias is under **0.3σ**
- power spectrum: lower ℓmax — **860 at 2,000 deg²** down to **340 at full sky**
- wavelets: drop bands — **the finest band alone** is enough at every area

**50 · is there anything left**
- Stage IV posteriors, **baryon-safe scales only**: **»** power spectrum **»** peak counts **»** ℓ1-norm
- ▲ ℓ1 reaches **×1.8** the power spectrum's FoM; **×2.6** at full sky where the wavelet cut fits better
- peaks comparable to the power spectrum but **complementary** — different degeneracy directions in the w₀ planes
- ▲ HOS are not only deep non-linear probes — the signal survives on **quasi-linear** scales with **no baryon model at all**
- and we can do better: the cut is not optimised, and as feedback modelling improves the analysis moves back into the non-linear regime, where the gain is larger
- *if pressed: ×1.8 carries ±0.6 — "about a factor of two". Not significant at 2,000 deg², significant from 5,000 up. Peaks ×1.07 Stage IV, ×1.17 full sky*

---

## Close · 51

**51 · conclusions**
- followed the chain from shapes to parameters: making the map, extracting information, simulation-based inference
- **map**: the choice of method is **not neutral** — it changes the FoM significantly. And **PnPMass** — physics + deep learning, accurate, calibrated bars, trained once for any mask and noise
- **summary**: the **joint ℓ1-norm** extracts as much as a neural compressor trained to be optimal, **without any training**
- **systematics**: HOS still give significant additional information after cutting the baryon-contaminated scales
- ▲ steps usually treated as neutral choices **do** change the result. With calibrated and tested methods we extract more, and **trust what we get out**
- *if nulling came up: and the same joint reading is what makes redshift nulling survivable for a higher-order analysis, which is in the thesis*
- thank you
