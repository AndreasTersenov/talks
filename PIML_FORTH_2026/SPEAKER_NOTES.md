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
- and the data are arriving: Euclid, billions of shapes, a third of the sky; extracting the signal is an algorithms problem

**4 · one potential, one operator**
- both second derivatives of the lensing potential (a projection of the gravitational potential)
- Fourier space: one linear operator P, two components, the kernels on the slide; unit modulus → inverts in one line, κ = P₁γ₁ + P₂γ₂
- ▲ linear and exact on a complete noiseless field; this P is in every equation after this

**5 · the chain, and the two questions**
- shapes → mass map (linear inverse problem) → feature vector (10⁵ correlated pixels cannot meet theory) → parameters (simulator for the likelihood)
- every step can bias or distort unnoticed, and every step has a place for a network
- **»** ▲ Q1, first half: learn only the prior; as accurate as end to end, any configuration, certified bars?
- **»** ▲ Q2, second half: a learned encoder, or hand-crafted features? who extracts more, and why?
- how we know: benchmarked, calibrated, tested

## Part 1

**6 · Part 1 card**
- making the map; three papers: does the prior matter (2025), a learned prior with certified bars (2026, led by Hubert Leterme), the same loop on six correlated channels (in preparation)

**7 · the inverse problem**
- one line: linear operator, mask, noise. Relation exact, data not
- noise ≫ signal, amplified at small scales; mask → non-local operator, unconstrained modes; constant offset invisible
- three visibly different maps, all consistent
- **»** ▲ selecting one needs a prior; the prior is what distinguishes the methods

**8 · the direct linear inverse**
- Kaiser–Squires: inverse operator in Fourier space, one FFT, no regulariser, thirty years
- **»** same field, same mask: structure buried, colour bar twice the range (noise), mask leaks
- in practice Gaussian smoothing, at the cost of the small scales

**9 · data term + regulariser**
- regularised least squares: data fidelity (noise-weighted residual) + regulariser (plausible map)
- data term same for all; the second term is the history
- none (KS) · **ℓ2** Gaussian field (Wiener) · **ℓ1** in wavelets (sparse) · Gaussian + sparse (MCALens, proximal steps) · ▲ **learned** from simulations (deep learning)
- not cosmetic: 2025 paper, everything else fixed, only the reconstruction swapped: sparse solver 4 % better map, 157 % more constraining power

**10 · four ways, drawn** ← grey physics, blue network, dashed = trained together
- end to end: physics in the training pairs only; one pass; retrain per mask/noise (DeepMass, MMGAN)
- unrolled: steps and networks on one rail, trained through together; transfers as far as training covered
- plug-and-play: fixed loop, dashed box around the denoiser alone, trained once; eight passes; nothing to retrain
- posterior sampling: the same learned prior in a sampler (score-based, Remy 2023, François this morning); thousands of passes
- ▲ the two on the right survive a new configuration; PnP is the cheap one; the bars come next

**11 · plug-and-play** ← room cue: Lanusse's keynote
- Venkatakrishnan, Bouman & Wohlberg 2013 and the decade since
- forward–backward: gradient step on the data term, then prox; PnP: prox → **denoiser** trained on simulated maps; fixed point under non-expansiveness
- richer prior than we can write down
- ▲ flexible because of where the physics sits: Swin transformer, 7 M, trained once on white noise; operator, mask, covariance only in the gradient step at inference
- PnP, not unrolling: nothing trained through the iteration; one network, every configuration
- walk the figure: shear in, zero init, forward (noisy), backward (denoiser) **»** fed back, eight iterations

**12 · PnPMass on residuals** ← two clicks: the residual loop, the number
- more physics in: Gaussian + non-Gaussian; the Gaussian part has a closed form, the Wiener filter
- **»** subtract its prediction; loop on the residual with a denoiser trained on non-Gaussian residuals; add back
- **»** ▲ within 0.5 % of the end-to-end network (map variant 1 %); converged after two iterations

**13 · the second network, and its objective**
- the data fans out: denoiser in the loop → the map; variance network → the error map; same simulated pairs
- objective: regress the squared residual; minimiser = posterior variance, pixel by pixel; one pass each, no sampling
- spread from noise + mask (the fan) and the learned prior that picked one map
- ▲ a network's variance has no guarantee → next

**14 · conformal calibration** ← three clicks: scores, widened intervals, the guarantee
- one pixel across held-out maps: the network's interval misses half the truths
- **»** score by how far outside (negative inside), sort, take the quantile q
- **»** widen every interval by q; the old bar is the dark core; 20 % outside, the rate asked for
- **»** ▲ miss rate between α − 1/(n+1) and α, any network, any distribution; 1024 maps, α ≈ 4.55 %
- limit: marginal, weakest at the peaks (open question at the end)

**15 · accurate, smallest calibrated bars**
- axes: across error, up bar size, lower-left better; colour miscoverage: circles above target before, diamonds on it after
- not who covers (everyone) but who covers with the tightest bars
- ▲ within 1 % of DeepMass (U-Net trained end to end for this mask and noise); smallest calibrated bars, all 512 test maps
- **»** uncertainty rises where the structure is
- **»** ▲ DeepMass retrained per footprint/noise; PnPMass trained once
- two limits: marginal not conditional (weakest at peaks); single cosmology

**16 · six correlated channels** ← one click: the measurements
- paper in preparation with Hubert Leterme; slice the sources by distance, one map per slice, six channels
- the six maps of one field, our joint reconstruction shown as maps (the exported truths were the nulled ones): same structures in every channel, stronger with distance; each slice lensed by all the matter in front → correlated
- **»** the measurements: a sixth of the galaxies each, many pixels with none
- ▲ six ill-posed problems, each worse than the one just solved, that share their answer

**17 · the nulling** ← one click: the local channels and the matrix
- why the channels: k sees everything in front; apparent size mixes size and distance → a multiscale analysis on one channel mixes scales
- **»** fixed, invertible, triangular re-mixing, three channels at a time, weights from the distances alone (BNT); each new channel local in distance
- ▲ the price: a difference of noisy maps; noise adds up, an error in one channel leaks into the next; the test the reconstruction has to pass

**18 · one denoiser, six channels** ← two clicks: the joint loop, the equation
- the obvious way: six loops, six denoisers, nothing shared
- **»** one six-channel image; data step block-diagonal (own mask and noise per channel); one denoiser, 6 in 6 out, trained on six-channel simulations → correlation in the prior
- **»** ▲ nothing else moves: operator, masks, noise only in the data step
- theory follows: convergence with masked data; error bound → step size 2/λmax justified (backup)

**19 · the tomographic result** ← three clicks: the re-mixing, after, the maps
- before: joint lower in every channel, 0.89 against 0.95
- **»** why the channels: k sees everything in front → invertible triangular re-mixing nulls the foreground, three at a time (BNT); differences of noisy maps
- **»** ▲ after: per channel worse than the zero map from channel 3, 1.48 on average, invented structure; joint never crosses one; far channels recovered barely
- **»** the map, channel 1: per channel sees nothing, joint reads the peak from the other five, it is in the truth

## Part 2

**20 · Part 2 card**
- the map must become a feature vector before inference; does that step need a network?

**21 · same power spectrum**
- standard feature vector is second order: two-point function, Fourier amplitudes; ▲ complete for a Gaussian field
- late-time field not Gaussian: haloes, filaments, voids; two fields, same spectrum
- **»** phases only: the web is still there; amplitudes only: nothing. The information is in the phases
- → statistics beyond second order: peaks, wavelets, Minkowski

**22 · the two hand-crafted features** ← room cue: the wavelet talk before
- same isotropic undecimated wavelet transform: band-pass images + coarse residual
- **»** peak counts: local maxima histogrammed per scale; peaks are haloes
- **»** maxima throw away voids and filaments → ℓ1-norm: sum of |coefficients| per band, binned by amplitude; every pixel; one-point distribution in the wavelet domain

**23 · likelihood-free inference** ← room cue: hand off to Zeghal at 14:00
- no analytic likelihood; a simulator: draw θ, run, keep pairs
- **»** pairs train a conditional flow = the posterior; hand it the observation
- ▲ every posterior calibration-tested: says 68 %, right 68 % of the time
- certifies against the simulator that trained it; wrong physics in the simulator = separate study, backup

**24 · the learned encoder**
- beating second order is easy; how close to all of it?
- why not learn the compression: careful (data, interpretability, generalisation), but the principled way:
- **»** encoder → 10-d summary; flow → posterior
- **»** trained together to maximise mutual information = expected log posterior
- ▲ an estimate of the ceiling, not just another feature; the benchmark
- matched comparison: same maps, same flow, same calibration tests; only the feature vector differs (3 × 10⁵ patches, 899 cosmologies)

**25 · the gap**
- **»** the encoder wins by 36 % in constraining power
- not symmetric: the maps are a multi-channel image; slices by distance, each lensed by the matter in front → channels not independent; the change from channel to channel is the information
- ▲ a per-channel statistic sees only the marginals; the encoder's first layer mixes all four

**26 · two routes**
- route one, change the input: product of each channel pair, strong where both have structure; same ℓ1-norm
- **»** route two, change the statistic: per-channel ℓ1 = the two marginals on the axes
- **»** grid on the plane, ℓ1 weight per cell: joint 2-D histogram; diagonal both strong, off-diagonal one strong; that is the redshift information; no extra maps

**27 · the answer**
- per-channel ℓ1 **»** + product channels **»** joint ℓ1 **»** the encoder lands on top of it
- ▲ a tie, not a win: encoder coverage slightly conservative
- ▲ sufficiency: the joint ℓ1-norm carries essentially all the accessible information, no training, inspectable, nothing to retrain

**28 · three open questions, on the chain** ← three clicks
- **»** the map: marginal guarantee, misses at the peaks; conditional coverage at map level, at survey cost?
- **»** mass mapping: non-expansiveness of a 7 M transformer verified empirically; a cheaper certificate?
- **»** systematics → features: the ceiling is the simulator's; baryons (backup) fixed by one band, the encoder has no band; can we tell without the truth?
- find me at lunch

## Close

**29 · conclusions** ← stays up through questions
- Q1 ▲ yes: within 1 % of the end-to-end networks, smallest calibrated bars, trained once for any mask and noise; six correlated channels with one denoiser
- Q2 ▲ only while it reads the channels jointly; give the ℓ1-norm the same access and it matches the optimal encoder, no training
- ▲ learn only what the physics cannot supply, benchmark it, calibrate it before trusting it
