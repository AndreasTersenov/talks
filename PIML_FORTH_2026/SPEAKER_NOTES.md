# SPEAKER_NOTES — cue cards, one per main-line frame

Pushed into the slides' `<aside class="notes">` by `python3 tools/sync-notes.py PIML_FORTH_2026 --write`.
`**»**` marks a click. `SPEAKER_SCRIPT.md` is the authority for the words.

## Act 0

**1 · title**
- defended two days ago; today the version for this room
- an inverse problem, a feature extractor, an inference step; where the learning goes in each

**2 · lensing in one picture**
- light through all the matter, most of it dark; gravity bends the path, image arrives distorted
- strong regime rare; **weak** regime everywhere, ~1 % per galaxy
- enough shapes → the pattern of distortions is a map of the matter

**3 · the measurement, the image we want**
- **measurement** = shear: two components per position, sampled at galaxies, noise-dominated
- lensing coherent, intrinsic shapes random → average neighbours
- **image we want** = convergence, the mass map: scalar, projected matter
- both second derivatives of one potential → known linear operator

**4 · Euclid**
- launched 2023, taking data; billions of shapes, a third of the sky, ×10 statistical power
- ▲ the limit is no longer the statistics but what we can do with them: an algorithms problem

**5 · the chain**
- shapes → mass map (linear inverse problem, mask, noise covariance) → feature vector (10⁵ correlated pixels cannot meet theory) → parameters (simulator for the likelihood)
- **»** ▲ first half: the inverse problem; what the prior does, what a learned prior buys
- **»** ▲ second half: features + inference; what must be learned, how we check it
- every step can bias or distort without anything downstream noticing

**6 · the two questions** ← read them, the only words on the slide
- **Q1** operator, mask, noise in the data term; learn only the prior: accurate? any configuration? certifiable bars?
- **Q2** learned encoder vs hand-crafted features: who extracts more, and why?
- ▲ how we know: benchmarked, calibrated, tested. Return here at the end

## Part 1

**7 · Part 1 card**
- making the map; two papers: does the prior matter (2025), a learned prior with certified bars (2026, led by Hubert Leterme)

**8 · the inverse problem**
- one line: linear operator, mask, noise. Relation exact, data not
- noise ≫ signal, amplified at small scales; mask → non-local operator, unconstrained modes; constant offset invisible
- three visibly different maps, all consistent
- **»** ▲ selecting one needs a prior; the prior is what distinguishes the methods

**9 · the direct linear inverse**
- Kaiser–Squires: inverse operator in Fourier space, one FFT, no regulariser, thirty years
- **»** same field, same mask: structure buried, colour bar twice the range (noise), mask leaks
- in practice Gaussian smoothing, at the cost of the small scales

**10 · data term + regulariser**
- regularised least squares: data fidelity (noise-weighted residual) + regulariser (plausible map)
- data term same for all; the second term is the history
- none (KS) · **ℓ2** Gaussian field (Wiener) · **ℓ1** in wavelets (sparse) · Gaussian + sparse (MCALens, proximal steps) · ▲ **learned** from simulations (deep learning)

**11 · the experiment**
- until this paper, compared on map quality (MSE vs truth); but the map is not the product
- everything held fixed: simulations, features, likelihood, sampler
- **»** only the reconstruction varies: linear inverse, inpainted, sparse solver

**12 · 4 % against 157 %** ← first posterior: explain the plot once
- panels = posterior over parameter pairs (matter density, expansion rate, dark-energy eq. of state, clumpiness); 68 / 95 %; smaller = more precise
- inpainting changes nothing (grey under red); sparse solver tighter everywhere
- stems: **open** = map error, 4 % better; **filled** = constraining power (inverse 1σ volume), ×2.6, ▲ 157 %
- ▲ not the same objective: choose the reconstruction by the posterior it gives

**13 · what about deep learning**
- people have, it works; four needs at once: accurate, flexible (same model for any noise/mask), fast, fast UQ
- end-to-end networks: accurate, fast, retrained per mask and noise level
- ▲ nothing has all four

**14 · plug-and-play** ← room cue: Lanusse's keynote
- Venkatakrishnan, Bouman & Wohlberg 2013 and the decade since
- forward–backward: gradient step on the data term, then prox; PnP: prox → **denoiser** trained on simulated maps; fixed point under non-expansiveness
- richer prior than we can write down
- ▲ flexible because of where the physics sits: Swin transformer, 7 M, trained once on white noise; operator, mask, covariance only in the gradient step at inference
- PnP, not unrolling: nothing trained through the iteration; one network, every configuration
- walk the figure: shear in, zero init, forward (noisy), backward (denoiser) **»** fed back, eight iterations

**15 · the error bar**
- second network on the same pairs predicts the squared residual → posterior variance per pixel, one pass
- spread from: noise + mask (the fan), and the learned prior that picked one map
- ▲ a network's variance has no guarantee → CQR on a held-out set: distribution-free, finite-sample, network need not be right
- **»** ▲ a stated coverage level that holds whether or not the model is well specified

**16 · accurate, smallest calibrated bars**
- axes: across error, up bar size, lower-left better; colour miscoverage: circles above target before, diamonds on it after
- not who covers (everyone) but who covers with the tightest bars
- ▲ within 1 % of DeepMass (U-Net trained end to end for this mask and noise); smallest calibrated bars, all 512 test maps
- **»** uncertainty rises where the structure is
- **»** ▲ DeepMass retrained per footprint/noise; PnPMass trained once
- two limits: marginal not conditional (weakest at peaks); single cosmology

## Part 2

**17 · Part 2 card**
- the map must become a feature vector before inference; does that step need a network?

**18 · same power spectrum**
- standard feature vector is second order: two-point function, Fourier amplitudes; ▲ complete for a Gaussian field
- late-time field not Gaussian: haloes, filaments, voids; two fields, same spectrum
- the information is in the phases → statistics beyond second order: peaks, wavelets, Minkowski

**19 · the two hand-crafted features** ← room cue: the wavelet talk before
- same isotropic undecimated wavelet transform: band-pass images + coarse residual
- **»** peak counts: local maxima histogrammed per scale; peaks are haloes
- **»** maxima throw away voids and filaments → ℓ1-norm: sum of |coefficients| per band, binned by amplitude; every pixel; one-point distribution in the wavelet domain

**20 · likelihood-free inference** ← room cue: hand off to Zeghal at 14:00
- no analytic likelihood; a simulator: draw θ, run, keep pairs
- **»** pairs train a conditional flow = the posterior; hand it the observation
- ▲ every posterior calibration-tested: says 68 %, right 68 % of the time
- certifies against the simulator that trained it; wrong physics in the simulator = separate study, backup

**21 · the learned encoder**
- beating second order is easy; how close to all of it?
- why not learn the compression: careful (data, interpretability, generalisation), but the principled way:
- **»** encoder → 10-d summary; flow → posterior
- **»** trained together to maximise mutual information = expected log posterior
- ▲ an estimate of the ceiling, not just another feature; the benchmark

**22 · the setup**
- same simulated maps (four distance slices per patch), same flow tuned per feature, same calibration tests
- 3 × 10⁵ patches, 899 cosmologies; architecture, dimension, flow family swept
- only the feature vector differs

**23 · the gap**
- **»** the encoder wins by 36 % in constraining power
- not symmetric: something about the maps the ℓ1-norm does not yet see

**24 · the channels are correlated** ← eight clicks
- galaxies sliced by distance **»** distant slice **»** lensed by all matter in front **»** its map **»** nearer slice **»** shorter column **»** another map **»** **»** channels not independent
- how the signal changes channel to channel = where the matter sits = how structure grew
- ▲ a per-channel statistic sees only the marginals; the encoder's first layer mixes all four

**25 · two routes**
- route one, change the input: product of each channel pair, strong where both have structure; same ℓ1-norm
- **»** route two, change the statistic: per-channel ℓ1 = the two marginals on the axes
- **»** grid on the plane, ℓ1 weight per cell: joint 2-D histogram; diagonal both strong, off-diagonal one strong; that is the redshift information; no extra maps

**26 · the answer**
- per-channel ℓ1 **»** + product channels **»** joint ℓ1 **»** the encoder lands on top of it
- ▲ a tie, not a win: encoder coverage slightly conservative
- ▲ sufficiency: the joint ℓ1-norm carries essentially all the accessible information, no training, inspectable, nothing to retrain

## Close

**27 · conclusions** ← stays up through questions
- Q1 ▲ yes: within 1 % of the end-to-end networks, smallest calibrated bars, trained once for any mask and noise
- Q2 ▲ only while it reads the channels jointly; give the ℓ1-norm the same access and it matches the optimal encoder, no training
- ▲ learn only what the physics cannot supply, benchmark it, calibrate it before trusting it
