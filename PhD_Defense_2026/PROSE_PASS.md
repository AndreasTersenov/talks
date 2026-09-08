# Prose pass, 2026-09-07: the anti-AI edit of the slide text

Andreas asked for the slides to stop reading as machine-written. This is the ledger: every
change to the **visible** text of `index.html`, before and after, with the tell it was fixing,
so each one can be checked and any of them reverted. Scope, method and the things deliberately
left alone are at the bottom.

**Not touched:** speaker notes (`<aside class="notes">`), HTML comments, `SPEAKER_SCRIPT.md`,
`STRUCTURE.md`, every number (no value on any slide changed; the one that looks changed, Q1 on
the conclusions slide, went from the word "four" to "4 %", which is what the ledger in
`PAPER_FACTS.md` says it is).

## What was wrong, in order of how much of it there was

1. **Em dashes as a mid-sentence pivot.** 150 of them in the visible text of the visible slides,
   most of them the "clause — and the turn" or "clause — which is the point" shape, in titles
   and body alike. Now 23, and those are label separators (`question 1 — the maps`,
   `route 1 — change the input`, `first — predict the error`, bylines), which are typography,
   not prose.
2. **"X, not Y" antitheses and two-beat titles.** "The relation is exact. The measurement is
   not." / "Kaiser–Squires smooths the small scales away. MCALens does not." / "The gain is not a
   global normalisation. It is…" / "So the question is not whether… It is whether…" and the
   four conclusion verdicts ("Not preprocessing." "Yes — PnPMass." "No network needed." "It
   survives."). Each is now one plain sentence that says the positive thing.
3. **Significance-marking tails.** "— which is what makes it runnable…", "That is what makes
   this simulation-based inference.", "— which is exactly what makes a scale cut cheap",
   "— and it is what makes coverage testing affordable", "Which matters next." Deleted or turned
   into an ordinary clause.
4. **Small tics.** "honest about its own uncertainty" (three places), "Honest limits", "an honest
   report", "make it honest"; "quietly throw information away"; "Bayes' rule is bookkeeping for
   belief" (bolded aphorism, twice); "first rung all along"; "the error bars know where the
   peaks are"; "Dovetails with"; one Title Case heading; one duplicated line on the whitening
   backup slide.

Counts: 137 replacements over 60 slides; em dashes in visible text 150 → 23; the tic list above
0 remaining on visible slides.

## The changes, slide by slide

Slide numbers are the leaf-slide index from the file (the order sections appear in
`index.html`, hidden ones included), not reveal's hash. Text is shown as rendered, tags stripped.

### slide 3

| before | after | what it was |
|---|---|---|
| Gravity — general relativity, unmodified | Gravity: general relativity, unmodified | dash as gloss separator |
| Geometry — spatially flat, homogeneous and isotropic on large scales | Geometry: spatially flat, homogeneous and isotropic on large scales | dash as gloss separator |
| Contents — cold dark matter (collisionless, non-relativistic), baryons, | Contents: cold dark matter (collisionless, non-relativistic), baryons, | dash as gloss separator |
| Initial conditions — adiabatic, near-Gaussian and near-scale-invariant, | Initial conditions: adiabatic, near-Gaussian and near-scale-invariant, | dash as gloss separator |

### slide 6

| before | after | what it was |
|---|---|---|
| Getting it out of the data is an algorithms problem — and that is the thesis. | Getting it out of the data is an algorithms problem, and that is what this thesis is about. | dash pivot into a flourish |

### slide 7

| before | after | what it was |
|---|---|---|
| most of them are measurement — PSF modelling, | most of them are measurement: PSF modelling, | dash before a list |

### slide 8 (+ hidden copy, slide 9)

| before | after | what it was |
|---|---|---|
| can bias the answer, or quietly throw information away, with no internal check noticing. | can bias the answer or throw information away, and nothing inside the pipeline would notice. | 'quietly' (soft adverb tic) + participial tail |

### slide 8 (+ hidden copy, slide 71)

| before | after | what it was |
|---|---|---|
| Can one reconstruction be flexible, fast, accurate and honest about its own uncertainty — on a survey the size of Euclid? | Can one reconstruction be flexible, fast, accurate, and tell you how wrong it is, on a survey the size of Euclid? | 'honest' tic + dash pivot |
| Does any of that survive the real Universe — the astrophysics we cannot model? | Does any of that survive the real Universe, where there is astrophysics we cannot model? | dash pivot |

### slide 12

| before | after | what it was |
|---|---|---|
| not observable — true size unknown | not observable: the true size is unknown | dash as gloss separator |
| measurable — from many galaxy shapes | measurable, from many galaxy shapes | dash as gloss separator |

### slide 13

| before | after | what it was |
|---|---|---|
| $W$ — geometry: distances, expansion history | $W$ carries the geometry: distances, expansion history | dash as gloss separator |
| $\delta$ — growth of structure | $\delta$ carries the growth of structure | dash as gloss separator |
| both at once — a test of the model, not a number | both at once, so a map tests the model rather than measuring one number | dash + 'X, not Y' antithesis |
| UNIONS, reconstructed with MCALens — the real thing, mask and all | UNIONS, reconstructed with MCALens. Real data, mask and all | dash pivot |
| $\kappa$ is a scalar — one number per pixel. | $\kappa$ is a scalar, one number per pixel. | dash pivot |

### slide 14

| before | after | what it was |
|---|---|---|
| One potential, two observables — and the relation between them is exact | One potential, two observables, and an exact relation between them | title: '— and' pivot |
| $\gamma_i = \hat{P}_i\,\kappa$ — mass to shear | mass to shear: $\gamma_i = \hat{P}_i\,\kappa$ | dash as gloss separator |
| $\kappa = \hat{P}_1\gamma_1 + \hat{P}_2\gamma_2$ — shear back to mass | shear back to mass: $\kappa = \hat{P}_1\gamma_1 + \hat{P}_2\gamma_2$ | dash as gloss separator |

### slide 16

| before | after | what it was |
|---|---|---|
| The relation is exact. The measurement is not. | The relation is exact, but we never observe γ itself | title: 'X is A. Y is not.' antithesis |
| $\mathbf{n}$ — noise: a galaxy’s own shape is far bigger than the shear | $\mathbf{n}$ is the noise: a galaxy’s own shape is far bigger than the shear | dash as gloss separator |
| $\mathbf{M}$ — gaps: the survey has holes, and no data means no constraint | $\mathbf{M}$ marks the gaps: the survey has holes, and no data means no constraint | dash as gloss separator |
| $\mathbf{P}$ — a blind spot: shear cannot see a constant added to $\kappa$ | $\mathbf{P}$ has a blind spot: shear cannot see a constant added to $\kappa$ | dash as gloss separator |
| Choosing one map means adding an assumption — and that assumption is the method. | Choosing one map means adding an assumption, and that assumption is the method. | dash pivot |

### slide 17

| before | after | what it was |
|---|---|---|
| about κ — which is the problem | about κ, so the noise comes through with the signal | title: '— which is the problem' pivot |
| Note the colour scales:the reconstruction | Note the colour scales: the reconstruction | typo (missing space) |
| one FFT — fast on any survey | one FFT, fast on any survey | dash as gloss separator |

### slide 18

| before | after | what it was |
|---|---|---|
| Every method solves the same optimisation — they differ in one term | Every method solves the same optimisation and differs in one term | title: dash pivot |
| $\mathbf{N}$ — per‑pixel noise covariance | $\mathbf{N}$ is the per‑pixel noise covariance | dash as gloss separator |
| $\lambda$ — data against prior | $\lambda$ weighs data against prior | dash as gloss separator |
| first term identical for all — the difference is $\mathcal{R}$ | the first term is identical for every method, only $\mathcal{R}$ differs | dash pivot |
| $\mathcal{R}$ — what each method assumes a mass map looks like | $\mathcal{R}$ is what each method assumes a mass map looks like | dash as gloss separator |
| no $\mathcal{R}$ — invert, then smooth | no $\mathcal{R}$: invert, then smooth | dash as gloss separator |
| mostly empty — a few strong wavelet coefficients | mostly empty, with a few strong wavelet coefficients | dash as gloss separator |
| both — smooth background, sparse peaks on top | both: a smooth background with sparse peaks on top | dash as gloss separator |

### slide 19

| before | after | what it was |
|---|---|---|
| sparse in starlets — the peaks and haloes that carry the higher-order signal. | sparse in starlets: the peaks and haloes that carry the higher-order signal. | dash pivot |
| Repeat until the map stops moving. Each half ends the same way — with a proximal step. | Repeat until the map stops moving. Each half ends with a proximal step. | dash pivot + padding |
| a data step lands at $v$ — better fit, not a plausible map | a data step lands at $v$: a better fit, but not yet a plausible map | dash + antithesis |

### slide 20

| before | after | what it was |
|---|---|---|
| Different assumptions, different maps — and nobody had checked whether it mattered | Different assumptions give different maps, and nobody had checked whether it mattered | title: '— and' pivot |
| How close the reconstruction lands to the truth — a reconstruction error, computed in simulations, against a map no real survey ever has. | How close the reconstruction lands to the truth: a reconstruction error, computed in simulations against a map no real survey has. | dash pivot |
| happens to $\Omega_m$, $\sigma_8$ or $w_0$ — and the posterior is what we actually publish. | happens to $\Omega_m$, $\sigma_8$ or $w_0$, and the posterior is what we publish. | dash pivot + 'actually' |
| reconstruction worth building for a survey like Euclid — or is mass mapping just preprocessing that any method does well enough? | reconstruction worth building for a survey like Euclid, or is mass mapping just preprocessing that any method does well enough? | dash pivot |

### slide 21

| before | after | what it was |
|---|---|---|
| Same simulations, same statistic, same likelihood — only the map changes | Same simulations, same statistic, same likelihood. Only the map changes | title: dash pivot |
| Whatever moves in the posterior is the reconstruction — not the simulations, not the statistic, not the sampler. | Whatever moves in the posterior is the reconstruction. | 'not X, not Y, not Z' triad |
| it — and that compression is a choice of its own. Part 3 is about which statistic to compress with. Here it is deliberately held fixed, so it cannot be the explanation for anything that moves. | it, and the compression is a choice of its own. Part 3 is about which statistic to compress with. Here it is held fixed on purpose, so it cannot explain anything that moves. | dash pivot + wordiness |

### slide 22

| before | after | what it was |
|---|---|---|
| Kaiser–Squires smooths the small scales away. MCALens does not. | MCALens keeps the small scales that Kaiser–Squires smooths away | title: 'X does. Y does not.' antithesis |
| what we are trying to recover — and what no real survey has | what we are trying to recover, and what no real survey has | dash pivot |
| nothing — but fill the mask in first, by inpainting | nothing, but the mask is inpainted first | dash pivot |
| Only MCALens is non-linear — only MCALens treats the structures carrying the higher-order signal differently from the Gaussian background. | MCALens is the only non-linear method here, and the only one that treats the structures carrying the higher-order signal differently from the Gaussian background. | anaphora ('Only MCALens… only MCALens') + dash |

### slide 23

| before | after | what it was |
|---|---|---|
| MCALens reconstructs the field 4 % better in RMSE — and gives a 157 % better figure of merit. | MCALens reconstructs the field 4 % better in RMSE and gives a 157 % better figure of merit. | dash pivot |
| Chapter 2 quotes no error bars — one chain per method. | Chapter 2 quotes no error bars: one chain per method. | dash pivot |

### slide 24

| before | after | what it was |
|---|---|---|
| The gain is not a global normalisation. It is small‑scale reconstruction fidelity — MCALens recovers structure | The gain is small‑scale reconstruction fidelity, not a global normalisation. MCALens recovers structure | 'It is not X. It is Y —' antithesis + dash |

### slide 31

| before | after | what it was |
|---|---|---|
| with the smallest calibrated bars — and no retraining | with the smallest calibrated bars, and no retraining | title: '— and' pivot |
| down and to the left is better — and after calibration everyone is on target | down and to the left is better, and after calibration everyone is on target | dash pivot |
| deployability: any mask, any noise — at inference, not in training | deployability: any mask, any noise, set at inference rather than in training | dash + antithesis |
| the error bars know where the peaks are | the error bars rise where the peaks are | personification |
| PnPMass is trained once — which is what makes it runnable on a survey like Euclid. | PnPMass is trained once, which is why it can run on a survey like Euclid. | '— which is what makes' significance tail |
| Honest limits: coverage is marginal, not conditional — what escapes concentrates at the peaks — and κTNG is a single cosmology. | Two limits: coverage is marginal, not conditional (what escapes concentrates at the peaks), and κTNG is a single cosmology. | 'honest' tic + double dash |

### slide 46

| before | after | what it was |
|---|---|---|
| touch it — and which statistic you compress with decides how much of the information survives. | touch it, and which statistic you compress with decides how much of the information survives. | dash pivot |

### slide 47.1

| before | after | what it was |
|---|---|---|
| The two‑point function is the field's baseline — and for a Gaussian field it is everything | The two‑point function is the field's baseline, and for a Gaussian field it is everything | title: '— and' pivot |
| DES Y3 cosmic shear, two‑point functions only — harmonic ($C_\ell$) and real space ($\xi_\pm$) | DES Y3 cosmic shear, two‑point functions only: harmonic ($C_\ell$) and real space ($\xi_\pm$) | dash before a list |
| every flagship result — KiDS‑1000, DES Y3, HSC Y3 — is a two‑point analysis | every flagship result (KiDS‑1000, DES Y3, HSC Y3) is a two‑point analysis | paired dashes |
| A Gaussian random field is its power spectrum — nothing else to know. So the question is not whether the two‑point function is good. It is whether the late‑time field is Gaussian. | A Gaussian random field is its power spectrum, and there is nothing else to know. So the question is whether the late‑time field is Gaussian. | dash + 'the question is not X. It is Y.' antithesis |

### slide 47.4

| before | after | what it was |
|---|---|---|
| everything that makes the web a web — filaments, haloes, voids — lives there | everything that makes the web a web, the filaments, haloes and voids, lives there | paired dashes |

### slide 47.5

| before | after | what it was |
|---|---|---|
| On the same maps, peaks beat the power spectrum — and multi‑scale peaks beat single‑scale | On the same maps, peaks beat the power spectrum, and multi‑scale peaks beat single‑scale | title: '— and' pivot |
| Forecasts from the same convergence maps — power spectrum, peaks after one filter, and peaks read at every scale. | Forecasts from the same convergence maps: power spectrum, peaks after one filter, and peaks read at every scale. | dash before a list |

### slide 52

| before | after | what it was |
|---|---|---|
| zero mean — $\int \psi\,\mathrm{d}x = 0$ | zero mean, $\int \psi\,\mathrm{d}x = 0$ | dash as gloss separator |
| one shape, a whole family — stretch by $a$, shift to $b$: | one shape, a whole family: stretch by $a$, shift to $b$, | dash pivot |
| $W(a,b) = \int f\,\psi_{a,b}\,\mathrm{d}x$ — structure of size $a$, at place $b$ | $W(a,b) = \int f\,\psi_{a,b}\,\mathrm{d}x$ measures structure of size $a$, at place $b$ | dash as gloss separator |
| the cosmic web is made of localised objects — clusters, filaments, voids — each with a size and a place | the cosmic web is made of localised objects (clusters, filaments, voids), each with a size and a place | paired dashes |
| and the scales can then be read — or set aside — one at a time | and the scales can then be read, or set aside, one at a time | paired dashes |

### slide 53

| before | after | what it was |
|---|---|---|
| $\mathcal{S}_{j,i}$ — the coefficients of scale $j$ whose SNR falls in bin $i$ | $\mathcal{S}_{j,i}$ are the coefficients of scale $j$ whose SNR falls in bin $i$ | dash as gloss separator |

### slide 54

| before | after | what it was |
|---|---|---|
| For peaks, for the ℓ1‑norm, for anything a network computes, there is not. | For peaks, the ℓ1‑norm, or anything a network computes, there is none. | anaphoric triad |
| So the comparison runs against simulations — the whole bottom row of the chain. That is what makes this simulation‑based inference. | So the comparison runs against simulations, the whole bottom row of the chain. This is simulation‑based inference. | dash + 'That is what makes this' significance marker |

### slide 55

| before | after | what it was |
|---|---|---|
| Bayes’ rule is bookkeeping for belief. What we should believe about the cosmology | What we should believe about the cosmology | aphoristic bolded opener |
| the posterior — the contours we publish | the posterior: the contours we publish | dash as gloss separator |
| the prior — ranges on the parameters | the prior: ranges on the parameters | dash as gloss separator |
| Then sample it — MCMC walks the parameter space and returns the posterior. | Then sample it: MCMC walks the parameter space and returns the posterior. | dash pivot |

### slide 56

| before | after | what it was |
|---|---|---|
| Learn the distribution a training set was drawn from — when all you ever see is the samples. | Learn the distribution a training set was drawn from, when all you ever see is the samples. | dash pivot |
| once trained, you can sample from $\mathbb{P}_\theta$ — and, for some models, evaluate the density $p_\theta(x)$ | once trained, you can sample from $\mathbb{P}_\theta$, and for some models evaluate the density $p_\theta(x)$ | dash pivot |
| is why the same machinery is behind the models everyone has been hearing about — faces, images, video, molecules | is why the same machinery is behind the models everyone has been hearing about: faces, images, video, molecules | dash before a list |
| The same idea — learn $\mathbb{P}_\theta$, then sample it. | The same idea: learn $\mathbb{P}_\theta$, then sample it. | dash pivot |

### slide 57

| before | after | what it was |
|---|---|---|
| diagonal — cheap enough to train on | diagonal, cheap enough to train on | dash pivot |
| its density — all three at once | its density, all three at once | dash pivot |
| and it becomes $q_\phi(\theta \mid x)$ — a posterior you can fit, by maximum likelihood. | and it becomes $q_\phi(\theta \mid x)$: a posterior you can fit by maximum likelihood. | dash pivot |

### slide 58

| before | after | what it was |
|---|---|---|
| We cannot write $p(x \mid \theta)$ down — but we can draw from it. So stop evaluating a likelihood and learn the posterior instead. | We cannot write $p(x \mid \theta)$ down, but we can draw from it. So instead of evaluating a likelihood, learn the posterior. | dash pivot + imperative flourish |
| That is what amortised means — and it is what makes coverage testing affordable. | That is what amortised means, and it is why coverage testing is affordable. | '— and it is what makes' significance tail |

### slide 59

| before | after | what it was |
|---|---|---|
| Beating the power spectrum is a low bar — how much is actually there to get? | Beating the power spectrum is a low bar. How much is actually there to get? | dash pivot |

### slide 62

| before | after | what it was |
|---|---|---|
| same maps, same flow, both calibrated — only the summary changes | same maps, same flow, both calibrated. Only the summary changes | dash pivot |

### slide 64

| before | after | what it was |
|---|---|---|
| multiply the two bins pixel by pixel — bright only where both have structure. | multiply the two bins pixel by pixel: bright only where both have structure. | dash pivot |

### slide 66

| before | after | what it was |
|---|---|---|
| (schematic — not to scale) | (schematic, not to scale) | dash in a parenthetical |

### slide 67

| before | after | what it was |
|---|---|---|
| The same pipeline — and the wavelet keeps the scales separate | The same pipeline, and the wavelet keeps the scales separate | title: '— and' pivot |

### slide 68

| before | after | what it was |
|---|---|---|
| Baryonic Bias Scales with Survey Area | Baryonic bias grows with survey area | Title Case heading |

### slide 70

| before | after | what it was |
|---|---|---|
| the signal survives on quasi‑linear scales — these are not only deep‑non‑linear probes | the signal survives on quasi‑linear scales, so HOS are not just probes of the deep non‑linear regime | dash + 'not only' construction |

### slide 72

| before | after | what it was |
|---|---|---|
| Not preprocessing. Swap the reconstruction and nothing else, and the figure of merit moves by 157 % — while the reconstruction error moves by four. Map quality and constraining power are not the same objective. | It changes the cosmology. Swap the reconstruction and nothing else, and the figure of merit moves by 157 %, while the reconstruction error moves by 4 %. Map quality and constraining power are different objectives. | two-word verdict + dash pivot + 'not the same' antithesis; 'four' was ambiguous (4 %) |
| Can one reconstruction be flexible, fast, accurate and honest about its own uncertainty? | Can one reconstruction be flexible, fast, accurate, and tell you how wrong it is? | 'honest' tic (matches slide 8) |
| Yes — PnPMass. Within 1 % of a network fine‑tuned to the observation, the smallest calibrated error bars of any method tested, and trained once rather than per footprint. | Yes, PnPMass does. It is within 1 % of a network fine‑tuned to the observation, has the smallest calibrated error bars of any method tested, and is trained once rather than per footprint. | verdict-dash-name pattern; verbless fragment made a sentence |
| What is the most we can read out of a map — and does it take a neural network? | What is the most we can read out of a map, and does it take a neural network? | dash pivot |
| No network needed. Build joint reading into the statistic and a fixed wavelet ℓ1‑norm matches an information‑optimal learned compressor, with no training at all. | No, it does not take a network. Read the bins jointly and a fixed wavelet ℓ1‑norm matches an information‑optimal learned compressor, with no training at all. | two-word verdict; answer now matches the question's grammar |
| Does any of that survive the real Universe — the astrophysics we cannot model? | Does any of that survive the real Universe, where there is astrophysics we cannot model? | dash pivot (matches slide 8) |
| It survives. Cut every scale unmodelled baryons measurably touch and the ℓ1‑norm is still ×1.8 tighter than $C_\ell$ at Stage IV, ×2.6 at full sky — and our cut is the crudest one available, so that is a floor. | Yes. Cut every scale that unmodelled baryons measurably touch, and the ℓ1‑norm is still ×1.8 tighter than $C_\ell$ at Stage IV and ×2.6 at full sky. Our cut is the crudest one available, so those numbers are a lower bound. | dramatic two-word verdict + dash pivot + 'floor' metaphor (4th use) |

### slide 76

| before | after | what it was |
|---|---|---|
| a tie on every parameter, over 9,000 mock observations — not a figure-of-merit artefact | a tie on every parameter over 9,000 mock observations, so not an artefact of the figure of merit | dash + 'not X' tail |

### slide 77

| before | after | what it was |
|---|---|---|
| it reads the bins jointly for free. Which matters next. | it reads the bins jointly for free. That matters in the nulled frame. | 'Which matters next.' tease fragment |

### slide 86

| before | after | what it was |
|---|---|---|
| And the power spectrum was this ladder's first rung all along. | The power spectrum was the first rung of this same ladder. | 'all along' reveal flourish |

### slide 90

| before | after | what it was |
|---|---|---|
| The analytical statistic ties it — and it is the safer instrument | The analytical statistic ties it, and it is the safer instrument | title: '— and' pivot |
| So the question is not whether the network wins, but what the cost and the risk are buying | So the question is what the cost and the risk are buying | 'the question is not X but Y' |

### slide 91

| before | after | what it was |
|---|---|---|
| matches the optimal learned summary — 3371 against 3326, a tie, both calibrated. | matches the optimal learned summary: 3371 against 3326, a tie, both calibrated. | dash pivot |
| what survives tracks how jointly the summary reads the bins — 0.16, 0.24, 0.72, 0.96. | what survives tracks how jointly the summary reads the bins: 0.16, 0.24, 0.72, 0.96. | dash before a list |

### slide 95

| before | after | what it was |
|---|---|---|
| Confirms the intuition block; closes the Vinciguerra loop | Confirms the intuition block | duplicate of the caveat line below it |

### slide 100

| before | after | what it was |
|---|---|---|
| ordering is a noise artefact — the noise power dominates the denominator at low z. | ordering is a noise artefact: the noise power dominates the denominator at low z. | dash pivot |

### slide 101

| before | after | what it was |
|---|---|---|
| bulk ($\|\nu\| \lesssim 2.5$) — which is why an SNR-space cut is available to higher-order statistics and not to the power spectrum. | bulk ($\|\nu\| \lesssim 2.5$). That is why an SNR-space cut is available to higher-order statistics and not to the power spectrum. | '— which is why' tail |

### slide 102

| before | after | what it was |
|---|---|---|
| The collapse is calibrated. The wide contours are an honest report of a real loss in that representation, not over-confidence — which is what makes the retention ladder a statement about information rather than about a broken fit. | The collapse is calibrated: the wide contours report a real loss in that representation, not over-confidence. So the retention ladder measures information, not the quality of a fit. | 'honest' tic + '— which is what makes' significance tail |

### slide 103

| before | after | what it was |
|---|---|---|
| signal-to-noise ($\|\nu\| \approx 1$–2) — mildly non-linear structure, not the rare extreme peaks. Dovetails with Paper I: | signal-to-noise ($\|\nu\| \approx 1$–2): mildly non-linear structure rather than the rare extreme peaks. Consistent with Paper I: | dash + antithesis + 'dovetails' |

### slide 104

| before | after | what it was |
|---|---|---|
| across the prior — no training, no emulator, and the dependence is visible by eye. | across the prior: no training, no emulator, and the dependence is visible by eye. | dash pivot |

### slide 106

| before | after | what it was |
|---|---|---|
| FoM3 across 9,000 mocks — medians 3045, 3371, 3326 | FoM3 across 9,000 mocks: medians 3045, 3371, 3326 | dash before a list |

### slide 107

| before | after | what it was |
|---|---|---|
| is one configuration of the first layer — available before any non-linearity, at no capacity cost. The 4% shortfall is an optimisation residual, not lost information. | is one configuration of the first layer, available before any non-linearity at no capacity cost. The 4% shortfall is an optimisation residual rather than lost information. | dash + 'X, not Y' tail |

### slide 121

| before | after | what it was |
|---|---|---|
| $\int\psi\,\mathrm{d}x = 0$ — those two properties are the whole definition | $\int\psi\,\mathrm{d}x = 0$. Those two properties are the whole definition | dash pivot |
| for a field made of localised objects — peaks, filaments, voids — that is the right trade. | for a field made of localised objects (peaks, filaments, voids) that is the right trade. | paired dashes |

### slide 122

| before | after | what it was |
|---|---|---|
| slide the dilated wavelet across the data at each scale — the result is one band‑pass image per scale, plus a coarse residual holding what is left | slide the dilated wavelet across the data at each scale: the result is one band‑pass image per scale, plus a coarse residual holding what is left | dash pivot |
| a feature of a given angular size lands in one band — which is exactly what makes a scale cut cheap, and what Part 3 relies on | a feature of a given angular size lands in one band, and that is what makes the scale cut in Part 3 cheap | '— which is exactly what makes' tail |

### slide 123

| before | after | what it was |
|---|---|---|
| almost all of an image sits in a few large coefficients — keep those, discard the rest. | almost all of an image sits in a few large coefficients: keep those, discard the rest. | dash pivot |
| the same move with a different rule — threshold the small coefficients. | the same move with a different rule: threshold the small coefficients. | dash pivot |

### slide 124

| before | after | what it was |
|---|---|---|
| — the map smoothed by a filter, in units of the noise. | , the map smoothed by a filter, in units of the noise. | dash pivot |

### slide 126

| before | after | what it was |
|---|---|---|
| peaks and voids are included automatically — no threshold to choose, no definition of a peak to defend | peaks and voids are included automatically: no threshold to choose, no definition of a peak to defend | dash pivot |

### slide 130

| before | after | what it was |
|---|---|---|
| Bayes’ rule is bookkeeping for belief. What we should believe after seeing the data is fixed by two things:how well | What we should believe after seeing the data is fixed by two things: how well | aphoristic bolded opener + typo |
| the posterior — the map we report | the posterior: the map we report | dash as gloss separator |
| the likelihood — physics we already have | the likelihood: physics we already have | dash as gloss separator |
| stop choosing — learn it from simulations | stop choosing: learn it from simulations | dash pivot |

### slide 130+131

| before | after | what it was |
|---|---|---|
| The same three terms come back in Part 3 — with the cosmological parameters as the unknown, and a likelihood we can no longer write down. | The same three terms come back in Part 3, with the cosmological parameters as the unknown and a likelihood we can no longer write down. | dash pivot (same line on both slides) |

### slide 131

| before | after | what it was |
|---|---|---|
| physics we already have — the operator from two slides ago | physics we already have: the operator from two slides ago | dash as gloss separator |
| the choice — and the only term that changes | the choice, and the only term that changes | '— and' pivot |

### slide 136

| before | after | what it was |
|---|---|---|
| forward pass — with a coverage guarantee on top | forward pass, with a coverage guarantee on top | title: dash pivot |
| then — make it honest | then — calibrate it | 'honest' tic |
| Not “the network says $\pm\sigma$” — a stated coverage level that holds whether or not the network is well specified. | Instead of “the network says $\pm\sigma$”: a stated coverage level that holds whether or not the network is well specified. | 'Not X — Y' antithesis |

### follow-ups after the screenshot pass

| slide | before | after | what it was |
|---|---|---|---|
| 17 | about κ, so the noise comes through with the signal | about κ, so the noise comes straight through | title filled the full slide width; shortened |
| 4.2 | the clustering amplitude — late-time probes sit low | the clustering amplitude: late-time probes sit low | dash as gloss separator |
| 4.2 | the expansion rate — the early-Universe extrapolation | the expansion rate: the early-Universe extrapolation | dash as gloss separator |

## Flagged and left alone (your call)

- **The speaker script and the notes still carry the old phrasings** where the slide changed:
  the script says "quietly throw information away" (line 292), "honest about how wrong it is"
  (line 300), "Bayes' rule is bookkeeping for belief" (line 455), "It survives" is not in the
  script but "Mass mapping is not preprocessing" is (line 1237). Spoken, these are fine; the tells
  are a reading problem, not a listening one. If you want the script to mirror the slides
  exactly, say so and I will make the same pass there.
- **Q3 on the conclusions slide is not "the same words" as Q3 on the chain board.** The board
  (slide 8) asks "…and what does it take to turn that reading into a posterior?"; the conclusions
  (slide 72) ask "…and does it take a neural network?". The notes on slide 72 say the questions
  are repeated verbatim. I did not reconcile them; both readings are defensible and it is a
  content decision.
- **Slide 6's hand-off line** ("That signal is the statistical memory of everything the Universe
  has done since the Big Bang") is grand, but it is the script's own beat and the room hears it,
  so I only removed the dash pivot after it.
- **"floor" / "ceiling"**: reduced (the conclusions slide now says "lower bound"), not purged; the
  backup ladder slides still use both, and they are the paper's own words.
- **Slide 90's "CNNs are powerful but treacherous"** and the "thumb on the scale" label are the
  conference deck's voice; left.
- **Label separators** with em dashes (kickers, `qtab`s, bylines, part dividers) were left as
  typography. If you would rather they went too, it is a five-minute scripted change.
- **Not in scope:** hidden and parked slides (`data-visibility="hidden"`), the "not part of the
  talk" archive sections (superseded LAM originals, earlier intro versions, the old
  three-answer conclusions), and the LAM-lifted method backups (Kaiser–Squires derivation,
  Wiener, sparse recovery, MCALens algebra, implementation), which do not read as AI and carry
  their own older typos ("funtions", "Disctrete"). The two hidden copies of the four-question
  board were changed along with the live one so they stay consistent if ever unparked.

## Method

`scratchpad/deai_edit.py` (+ `deai_edit_2.py`): absolute path; every `old` string copied from the
file and required to match exactly once (whitespace runs matched loosely, everything else
literal); nothing written until every replacement matched; `<section` count asserted unchanged.
Verified by diffing the rendered text of every leaf slide before/after, and by headless-Chrome
screenshots of every slide whose title changed (14, 16, 17, 18, 20, 21, 22, 31, 47.1, 47.5, 67,
68, 72, 90, 136.2) plus 8, 13, 24, 55 and 58: no title wraps, no layout moved. Slide 17's new
title was shortened once because the first version filled the full width.

---

# Pass 2, same day: the titles and the register

Andreas, after reading pass 1: the em dashes were only part of it. The titles were "corny /
unscientific / impersonal" (wit, twist, storytelling voice), the "[general statement]: [detailed
explanation]" shape read as AI too, and the colon glosses pass 1 introduced ("n is the noise: …")
just moved the pattern. His own titles in the deck ("Are HOS still useful?", "Where does this
improvement come from?", "Shear & Convergence") are the register.

The assertion-evidence form stays (TALK-GUIDELINES §4.1 asks for full-sentence titles that carry
the slide's message). What changed is the voice: each title is now a plain descriptive sentence,
and body copy is technical fragments rather than teaching-voice glosses.

- **Titles.** Every title in the talk run and in the backups reachable for questions, e.g.
  "ΛCDM: six numbers, and the assumptions that let you get away with six" → "ΛCDM describes the
  Universe with six free parameters, plus a set of assumptions"; "Between the galaxy shapes and
  the parameters there is a chain" → "The analysis chain from galaxy shapes to parameters, and the
  four questions of this thesis"; "We measure the shear. What we want is the convergence." →
  "We measure the shear, but theory predicts the convergence"; "Kaiser–Squires assumes almost
  nothing about κ …" → "Kaiser–Squires inversion is exact for complete, noiseless data, but
  amplifies the noise".
- **The four questions**, on the board, its hidden copy and the conclusions, are reworded in the
  same plain form (Q1 is now Andreas's own earlier title, "Does the choice of mass-mapping method
  matter for the final constraints?"). Q3 on the conclusions slide now matches the board exactly,
  and its answer covers both halves of the question.
- **Glosses** → technical fragments: "n is the noise: a galaxy's own shape is far bigger than the
  shear" → "shape noise n, intrinsic ellipticities much larger than the shear"; "P has a blind
  spot: …" → "mass-sheet degeneracy, a constant added to κ leaves the shear unchanged".
- **Bayes slides**: the "what we believe, after / what we assume, before we look" teaching labels
  → "after the data / before the data"; the lede is now Bayes' theorem stated plainly.
- Metaphors out: "statistical memory of everything the Universe has done", "the error bars know
  where the peaks are", "the ceiling", "movement II", "the thumb on the scale", "one story".

255 replacements over 70 slides. Numbers unchanged.

## Pass 2 changes, slide by slide

### slide 2

| before | after | what it was |
|---|---|---|
| Thirteen point eight billion years, from quantum fluctuations to galaxies | The Universe evolved from quantum fluctuations to galaxies over 13.8 billion years | title: twist/wit -> plain statement |

### slide 3

| before | after | what it was |
|---|---|---|
| ΛCDM: six numbers, and the assumptions that let you get away with six | ΛCDM describes the Universe with six free parameters, plus a set of assumptions | title: twist/wit -> plain statement |
| how much ordinary matter, how much cold dark matter | baryon and cold dark matter densities | '[term]: [gloss]' teaching voice -> technical fragment |
| the sound-horizon angle, and when the Universe reionised | angular size of the sound horizon, optical depth to reionisation | '[term]: [gloss]' teaching voice -> technical fragment |
| A phenomenological description, not an explanation. About 95 % of the budget is two components whose nature we do not know, and the value of $\Lambda$ is put in by hand. | ΛCDM is a phenomenological model. About 95 % of the energy budget is in two components of unknown nature, and the value of $\Lambda$ is put in by hand. | 'X, not Y' opener |

### slide 4.1

| before | after | what it was |
|---|---|---|
| How we test it: independent probes of geometry and growth | Independent probes test the model through both geometry and growth | title: twist/wit -> plain statement |

### slide 4.2

| before | after | what it was |
|---|---|---|
| And two places where the measurements do not agree | The late-time S8 and the local H0 disagree with the CMB predictions | title: twist/wit -> plain statement |
| the clustering amplitude: late-time probes sit low against the CMB band | S8 from late-time probes lies below the CMB value | '[term]: [gloss]' teaching voice -> technical fragment |
| the expansion rate: the early-Universe extrapolation against the distance ladder | H0 from the early Universe against the local distance ladder | '[term]: [gloss]' teaching voice -> technical fragment |
| three readings new physics, a statistical fluctuation, or something in the analysis | possible explanations new physics, a statistical fluctuation, or a systematic in the analysis | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 5

| before | after | what it was |
|---|---|---|
| Mass between us and a galaxy bends the light, and distorts the image we see | Foreground mass deflects the light of background galaxies and distorts their images | title: twist/wit -> plain statement |

### slide 6

| before | after | what it was |
|---|---|---|
| That signal is the statistical memory of everything the Universe has done since the Big Bang. Getting it out of the data is an algorithms problem, and that is what this thesis is about. | The lensing signal encodes the growth of structure and the geometry of the Universe. Extracting it from the data is an algorithms problem, and that is the subject of this thesis. | grand metaphor -> plain claim |

### slide 7

| before | after | what it was |
|---|---|---|
| A real weak-lensing analysis is dozens of steps, and most of them are not the physics | Most of a real weak-lensing analysis is measurement and calibration | title: twist/wit -> plain statement |
| Nearly every box is its own paper, and most of them are measurement: PSF modelling, shape calibration, blending, redshift distributions, covariances. The cosmology is the last two boxes on the right. | Almost every box is a paper on its own, and most of the work is measurement and calibration (PSF modelling, shape calibration, blending, redshift distributions, covariances). The cosmological inference is the last two boxes. | wit/teaching voice -> plain statement |

### slide 8 (+ hidden 9)

| before | after | what it was |
|---|---|---|
| Between the galaxy shapes and the parameters there is a chain | The analysis chain from galaxy shapes to parameters, and the four questions of this thesis | title: twist/wit -> plain statement |

### slide 8

| before | after | what it was |
|---|---|---|
| Every one of those stages is now built out of learned components, and every one of them | Each of these steps now involves learned components. Each of them | narrative voice |

### slide 8 (+ hidden 9)

| before | after | what it was |
|---|---|---|
| can bias the answer or throw information away, and nothing inside the pipeline would notice. | can bias the result or discard information, and there is no internal check that would detect it. | personified pipeline |

### slide 8 (+ hidden 71)

| before | after | what it was |
|---|---|---|
| Is mass mapping preprocessing, or does the choice of reconstruction change the cosmology we infer? | Does the choice of mass-mapping method matter for the final constraints? | Q1, in Andreas's own earlier wording |
| Can one reconstruction be flexible, fast, accurate, and tell you how wrong it is, on a survey the size of Euclid? | Can one method be accurate, flexible and fast, with reliable uncertainties, at the scale of Euclid? | Q2 |
| What is the most we can read out of a map, and what does it take to turn that reading into a posterior? | How much cosmological information can a summary statistic extract from the maps, and how do we turn it into a posterior? | Q3 |
| Does any of that survive the real Universe, where there is astrophysics we cannot model? | Do these results hold up against astrophysical systematics we cannot model, such as baryonic feedback? | Q4 |

### slide 12

| before | after | what it was |
|---|---|---|
| We measure the shear. What we want is the convergence. | We measure the shear, but theory predicts the convergence | title: twist/wit -> plain statement |
| isotropic: a change of size | isotropic magnification | '[term]: [gloss]' teaching voice -> technical fragment |
| set by the projected mass | proportional to the projected mass | '[term]: [gloss]' teaching voice -> technical fragment |
| not observable: the true size is unknown | not directly observable (the unlensed size is unknown) | '[term]: [gloss]' teaching voice -> technical fragment |
| anisotropic: a stretch | anisotropic distortion | '[term]: [gloss]' teaching voice -> technical fragment |
| coherent behind the same structure | coherent across neighbouring galaxies | '[term]: [gloss]' teaching voice -> technical fragment |
| measurable, from many galaxy shapes | measurable from galaxy ellipticities | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 13

| before | after | what it was |
|---|---|---|
| A convergence map carries both geometry and growth | The convergence is a projection of the matter density, sensitive to geometry and growth | title: twist/wit -> plain statement |
| $W$ carries the geometry: distances, expansion history | $W(\chi)$ depends on the geometry (distances, expansion history) | '[term]: [gloss]' teaching voice -> technical fragment |
| $\delta$ carries the growth of structure | $\delta$ depends on the growth of structure | '[term]: [gloss]' teaching voice -> technical fragment |
| both at once, so a map tests the model rather than measuring one number | so $\kappa$ probes both at once | '[term]: [gloss]' teaching voice -> technical fragment |
| UNIONS, reconstructed with MCALens. Real data, mask and all | UNIONS convergence map, reconstructed with MCALens (real data; the survey mask in grey) | wit/teaching voice -> plain statement |
| and it is the easier object to work with | why reconstruct κ | wit/teaching voice -> plain statement |
| $\kappa$ is a scalar, one number per pixel. The shear is spin‑2: two components that turn with the coordinate frame. Theory predicts $\kappa$, and every statistic in this talk is measured on it. | $\kappa$ is a scalar field, while the shear is spin‑2 (two components that rotate with the coordinate frame). Theory predicts $\kappa$, and all the statistics in this talk are computed on $\kappa$ maps. | wit/teaching voice -> plain statement |

### slide 14

| before | after | what it was |
|---|---|---|
| One potential, two observables, and an exact relation between them | Shear and convergence are both second derivatives of the lensing potential | title: twist/wit -> plain statement |
| mass to shear: $\gamma_i = \hat{P}_i\,\kappa$ | from convergence to shear: $\gamma_i = \hat{P}_i\,\kappa$ | '[term]: [gloss]' teaching voice -> technical fragment |
| shear back to mass: $\kappa = \hat{P}_1\gamma_1 + \hat{P}_2\gamma_2$ | from shear to convergence: $\kappa = \hat{P}_1\gamma_1 + \hat{P}_2\gamma_2$ | '[term]: [gloss]' teaching voice -> technical fragment |
| linear, and exact on a complete noiseless field | linear and exact for a complete, noiseless field | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 16

| before | after | what it was |
|---|---|---|
| The relation is exact, but we never observe γ itself | In practice, mass mapping is an ill-posed inverse problem | title: twist/wit -> plain statement |
| what we measure | measured shear | '[term]: [gloss]' teaching voice -> technical fragment |
| all fit the measurement | all consistent with the data | '[term]: [gloss]' teaching voice -> technical fragment |
| $\mathbf{n}$ is the noise: a galaxy’s own shape is far bigger than the shear | shape noise $\mathbf{n}$, intrinsic ellipticities much larger than the shear | '[term]: [gloss]' teaching voice -> technical fragment |
| $\mathbf{M}$ marks the gaps: the survey has holes, and no data means no constraint | survey mask $\mathbf{M}$, missing data and a non-local inversion | '[term]: [gloss]' teaching voice -> technical fragment |
| $\mathbf{P}$ has a blind spot: shear cannot see a constant added to $\kappa$ | mass-sheet degeneracy, a constant added to $\kappa$ leaves the shear unchanged | '[term]: [gloss]' teaching voice -> technical fragment |
| Choosing one map means adding an assumption, and that assumption is the method. | Selecting one solution requires a prior on $\kappa$, and the choice of prior is what distinguishes the methods. | aphorism |

### slide 17

| before | after | what it was |
|---|---|---|
| Kaiser–Squires assumes almost nothing about κ, so the noise comes straight through | Kaiser–Squires inversion is exact for complete, noiseless data, but amplifies the noise | title: twist/wit -> plain statement |
| same field, same mask. Note the colour scales: the reconstruction spans twice the range of the truth. | Same field and mask. The colour scale of the reconstruction spans twice the range of the truth. | wit/teaching voice -> plain statement |
| Why it is the standard | Advantages | wit/teaching voice -> plain statement |
| What it costs | Limitations | wit/teaching voice -> plain statement |
| the mask leaks across the whole map | mask effects leak across the map (non-local operator) | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 18

| before | after | what it was |
|---|---|---|
| Every method solves the same optimisation and differs in one term | Every mass-mapping method minimises a data term plus a regulariser that encodes the prior | title: twist/wit -> plain statement |
| Find the $\kappa$ that stays consistent with the measured shear while remaining physically plausible. | Find the $\kappa$ that fits the measured shear and is plausible under a prior. | wit/teaching voice -> plain statement |
| $\mathbf{N}$ is the per‑pixel noise covariance | $\mathbf{N}$, noise covariance | '[term]: [gloss]' teaching voice -> technical fragment |
| $\lambda$ weighs data against prior | $\lambda$, regularisation strength | '[term]: [gloss]' teaching voice -> technical fragment |
| the first term is identical for every method, only $\mathcal{R}$ differs | the data term is the same for all methods; they differ in $\mathcal{R}$ | '[term]: [gloss]' teaching voice -> technical fragment |
| $\mathcal{R}$ is what each method assumes a mass map looks like | the regulariser $\mathcal{R}$ encodes the prior on $\kappa$ | '[term]: [gloss]' teaching voice -> technical fragment |
| no $\mathcal{R}$: invert, then smooth | no prior, smoothing only | '[term]: [gloss]' teaching voice -> technical fragment |
| mostly empty, with a few strong wavelet coefficients | sparse in a wavelet basis | '[term]: [gloss]' teaching voice -> technical fragment |
| both: a smooth background with sparse peaks on top | Gaussian plus sparse component | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 19

| before | after | what it was |
|---|---|---|
| MCALens: two components, and a different rule for each | MCALens models κ as a Gaussian plus a sparse component | title: twist/wit -> plain statement |
| the Gaussian part | Gaussian component | '[term]: [gloss]' teaching voice -> technical fragment |
| the smooth background. A Wiener filter, which needs only the power spectrum. | estimated with a Wiener filter, which needs only the power spectrum. | '[term]: [gloss]' teaching voice -> technical fragment |
| the non-Gaussian part | non-Gaussian component | '[term]: [gloss]' teaching voice -> technical fragment |
| sparse in starlets: the peaks and haloes that carry the higher-order signal. | sparse in the starlet domain (peaks and haloes). | '[term]: [gloss]' teaching voice -> technical fragment |
| How it solves: alternate | Alternating minimisation | '[term]: [gloss]' teaching voice -> technical fragment |
| Repeat until the map stops moving. Each half ends with a proximal step. | Iterate to convergence. Each sub-problem is solved with a proximal step. | '[term]: [gloss]' teaching voice -> technical fragment |
| what a proximal step does | the proximal operator | '[term]: [gloss]' teaching voice -> technical fragment |
| a data step lands at $v$: a better fit, but not yet a plausible map | a gradient step on the data term gives $v$ | '[term]: [gloss]' teaching voice -> technical fragment |
| prox returns the nearest map the prior accepts | prox returns the point closest to $v$ that is consistent with the prior | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 20

| before | after | what it was |
|---|---|---|
| Different assumptions give different maps, and nobody had checked whether it mattered | Different priors give different maps. Does the difference reach the constraints? | title: twist/wit -> plain statement |
| how the field compared them | how methods have been compared | wit/teaching voice -> plain statement |
| How close the reconstruction lands to the truth: a reconstruction error, computed in simulations against a map no real survey has. | By the reconstruction error with respect to the true map, in simulations. | '[term]: [gloss]' teaching voice -> technical fragment |
| Every method reproduces the shear it was handed. What they differ in is what they assume about everything the data leaves open. | All methods fit the observed shear; they differ in the prior. | wit/teaching voice -> plain statement |
| the question nobody had asked | the open question | narrative voice |
| Does that difference survive into the posterior? | Does the choice of method change the posterior? | wit/teaching voice -> plain statement |
| The map is an intermediate product. Nothing in a reconstruction error tells you what happens to $\Omega_m$, $\sigma_8$ or $w_0$, and the posterior is what we publish. | The map is an intermediate product. The reconstruction error says nothing about the constraints on $\Omega_m$, $\sigma_8$ or $w_0$. | wit/teaching voice -> plain statement |
| The question was open, and actively argued: is a state‑of‑the‑art reconstruction worth building for a survey like Euclid, or is mass mapping just preprocessing that any method does well enough? | A practical question for Euclid: is an advanced reconstruction method worth the effort, or is any reasonable method good enough? | wit/teaching voice -> plain statement |

### slide 21

| before | after | what it was |
|---|---|---|
| §1 Same simulations, same statistic, same likelihood. Only the map changes | §1 The simulations, statistic and likelihood are fixed, and only the mass-mapping method varies | title: twist/wit -> plain statement |
| One factor varies. Whatever moves in the posterior is the reconstruction. | Everything else is fixed, so any change in the posterior comes from the reconstruction. | wit/teaching voice -> plain statement |
| A map is $10^5$ correlated pixels, so it has to be compressed before any likelihood can touch it, and the compression is a choice of its own. Part 3 is about which statistic to compress with. Here it is held fixed on purpose, so it cannot explain anything that moves. | The map ($10^5$ correlated pixels) has to be compressed into a summary statistic before inference. Which statistic to use is the subject of Part 3; here it is held fixed. | wit/teaching voice -> plain statement |

### slide 22

| before | after | what it was |
|---|---|---|
| §1 MCALens keeps the small scales that Kaiser–Squires smooths away | §1 MCALens recovers small-scale structure that Kaiser–Squires smooths out | title: twist/wit -> plain statement |
| what each one assumes about $\kappa$ | prior on $\kappa$ | '[term]: [gloss]' teaching voice -> technical fragment |
| what we are trying to recover, and what no real survey has | the true map (simulations only) | '[term]: [gloss]' teaching voice -> technical fragment |
| nothing. Invert directly, then smooth to control the noise | none. Direct inversion, then smoothing | '[term]: [gloss]' teaching voice -> technical fragment |
| nothing, but the mask is inpainted first | none; the mask is inpainted (DCT) before inversion | '[term]: [gloss]' teaching voice -> technical fragment |
| MCALens is the only non-linear method here, and the only one that treats the structures carrying the higher-order signal differently from the Gaussian background. | MCALens is the only non-linear method of the three, and the only one that models the non-Gaussian structures separately from the Gaussian background. | wit/teaching voice -> plain statement |

### slide 23

| before | after | what it was |
|---|---|---|
| §1 Swapping the reconstruction alone moves the figure of merit by 157 % | §1 MCALens improves the figure of merit by 157 % over Kaiser–Squires | title: twist/wit -> plain statement |
| the baseline | baseline | wit/teaching voice -> plain statement |
| a null result | no change | wit/teaching voice -> plain statement |
| the paper’s +157 % | +157 % | wit/teaching voice -> plain statement |
| map quality is not constraining power | reconstruction error vs constraining power | wit/teaching voice -> plain statement |
| MCALens reconstructs the field 4 % better in RMSE and gives a 157 % better figure of merit. | MCALens improves the RMSE by only 4 %, but the figure of merit by 157 %. | wit/teaching voice -> plain statement |
| Inpainting changes nothing here because the peak counts already exclude the masked regions; the paper is explicit that this would not carry over to a Fourier‑space statistic. Chapter 2 quotes no error bars: one chain per method. | Inpainting has no effect here because peaks in the masked regions are excluded anyway; this would not hold for a Fourier‑space statistic. No error bars on the figure of merit (one chain per method). | wit/teaching voice -> plain statement |

### slide 24

| before | after | what it was |
|---|---|---|
| §1 MCALens keeps gaining down to 2′, where Kaiser–Squires has already saturated at 8′ | §1 The gain comes from scales below 8′, which only MCALens recovers | title: twist/wit -> plain statement |
| adding 4′ and 2′ changes nothing significant | adding the 4′ and 2′ scales does not change the contours | wit/teaching voice -> plain statement |
| the mechanism | interpretation | wit/teaching voice -> plain statement |
| The gain is small‑scale reconstruction fidelity, not a global normalisation. MCALens recovers structure where the linear inversion has already smoothed itself into noise, and the higher‑order statistic can read it. | MCALens recovers small‑scale structure that the linear inversion loses to noise, and the peak counts are sensitive to exactly those scales. | wit/teaching voice -> plain statement |

### slide 31

| before | after | what it was |
|---|---|---|
| §2 As accurate as the fine‑tuned networks, with the smallest calibrated bars, and no retraining | §2 PnPMass matches the accuracy of the fine‑tuned networks, with the smallest calibrated error bars | title: twist/wit -> plain statement |
| down and to the left is better, and after calibration everyone is on target | lower left is better; after calibration, all methods reach the target coverage | wit/teaching voice -> plain statement |
| accuracy: level with the deep‑learning methods | accuracy comparable to the deep‑learning methods | '[term]: [gloss]' teaching voice -> technical fragment |
| uncertainty: the smallest bars of any method, all 512 maps | smallest calibrated intervals of all methods, on all 512 test maps | '[term]: [gloss]' teaching voice -> technical fragment |
| deployability: any mask, any noise, set at inference rather than in training | mask and noise covariance enter at inference time, not in training | '[term]: [gloss]' teaching voice -> technical fragment |
| the error bars rise where the peaks are | the uncertainty map traces the structure | wit/teaching voice -> plain statement |
| DeepMass and MMGAN are retrained whenever the footprint or the noise changes. PnPMass is trained once, which is why it can run on a survey like Euclid. | DeepMass and MMGAN need retraining for every new mask or noise level; PnPMass is trained once and applies to any configuration. | wit/teaching voice -> plain statement |
| Two limits: coverage is marginal, not conditional (what escapes concentrates at the peaks), and κTNG is a single cosmology. | Limitations: the coverage guarantee is marginal, not conditional (miscoverage concentrates at the peaks), and κTNG is a single cosmology. | wit/teaching voice -> plain statement |

### slide 45

| before | after | what it was |
|---|---|---|
| movement II — the summaries | second half — the summaries | musical metaphor |
| Everything so far was one box of the chain | Parts 3 and 4 move from the map to the summary statistic | title: twist/wit -> plain statement |
| Parts 3 and 4 are about the next two: which statistic we compress the map with, and whether the answer survives the systematics. | Parts 1 and 2 were about the mass map. Parts 3 and 4 are about the summary statistic, and its robustness to systematics. | wit/teaching voice -> plain statement |

### slide 46

| before | after | what it was |
|---|---|---|
| Same chain, one step to the right | The map has to be compressed into a summary statistic before inference | title: twist/wit -> plain statement |
| A map is $10^5$ correlated pixels, so it has to be compressed before any likelihood can touch it, and which statistic you compress with decides how much of the information survives. | The map has to be compressed into a summary statistic before inference, and the choice of statistic determines how much information is retained. | wit/teaching voice -> plain statement |

### slide 47.1

| before | after | what it was |
|---|---|---|
| The two‑point function is the field's baseline, and for a Gaussian field it is everything | The two‑point function is the standard statistic, and is complete for a Gaussian field | title: twist/wit -> plain statement |
| two decades of systematics work built around it | two decades of work on its systematics | wit/teaching voice -> plain statement |
| A Gaussian random field is its power spectrum, and there is nothing else to know. So the question is whether the late‑time field is Gaussian. | For a Gaussian random field, the power spectrum contains all the information. The question is whether the late‑time density field is Gaussian. | wit/teaching voice -> plain statement |

### slide 47.3

| before | after | what it was |
|---|---|---|
| The power spectrum cannot tell these two apart | Two very different fields can have the same power spectrum | title: twist/wit -> plain statement |

### slide 47.4

| before | after | what it was |
|---|---|---|
| The cosmic web is written in the phases | The non-Gaussian information is in the phases | title: twist/wit -> plain statement |
| a two‑point measurement keeps the amplitudes and throws the phases away | the power spectrum keeps only the Fourier amplitudes | wit/teaching voice -> plain statement |
| everything that makes the web a web, the filaments, haloes and voids, lives there | the phases carry the structure of the cosmic web (filaments, haloes, voids) | wit/teaching voice -> plain statement |
| to reach it you need statistics beyond 2‑pt: peaks, wavelets, the ℓ1‑norm, Minkowski functionals | higher-order statistics are needed to access it: peak counts, wavelet statistics, the ℓ1‑norm, Minkowski functionals | wit/teaching voice -> plain statement |

### slide 47.5

| before | after | what it was |
|---|---|---|
| On the same maps, peaks beat the power spectrum, and multi‑scale peaks beat single‑scale | Peak counts constrain better than the power spectrum, and multi‑scale peaks better than single‑scale | title: twist/wit -> plain statement |
| Forecasts from the same convergence maps: power spectrum, peaks after one filter, and peaks read at every scale. | Forecasts from the same convergence maps: power spectrum, single-scale peaks, and multi-scale peaks. | wit/teaching voice -> plain statement |
| Nothing about the data changed. The only thing that moves these contours is the choice of summary statistic. | Same data; only the summary statistic changes. | punchline rhythm |

### slide 52

| before | after | what it was |
|---|---|---|
| a wavelet $\psi$ is compact, oscillating, zero mean, $\int \psi\,\mathrm{d}x = 0$ | a wavelet $\psi$ is a localised, oscillating function with zero mean, $\int \psi\,\mathrm{d}x = 0$ | '[term]: [gloss]' teaching voice -> technical fragment |
| one shape, a whole family: stretch by $a$, shift to $b$, $\psi_{a,b}(x) = \tfrac{1}{\sqrt{a}}\,\psi\!\big(\tfrac{x-b}{a}\big)$ | dilations and translations of $\psi$ form a family, $\psi_{a,b}(x) = \tfrac{1}{\sqrt{a}}\,\psi\!\big(\tfrac{x-b}{a}\big)$ | '[term]: [gloss]' teaching voice -> technical fragment |
| $W(a,b) = \int f\,\psi_{a,b}\,\mathrm{d}x$ measures structure of size $a$, at place $b$ | the coefficient $W(a,b) = \int f\,\psi_{a,b}\,\mathrm{d}x$ measures the structure at scale $a$ and position $b$ | '[term]: [gloss]' teaching voice -> technical fragment |
| why this suits a convergence map | why wavelets for convergence maps | wit/teaching voice -> plain statement |
| the cosmic web is made of localised objects (clusters, filaments, voids), each with a size and a place | the cosmic web consists of localised structures (clusters, filaments, voids) with a characteristic size and position | '[term]: [gloss]' teaching voice -> technical fragment |
| each one lands in one band, at its own position, so a few large coefficients carry the field | such a field is sparse in the wavelet domain: a few large coefficients | '[term]: [gloss]' teaching voice -> technical fragment |
| and the scales can then be read, or set aside, one at a time | scales can be analysed, or removed, separately | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 53

| before | after | what it was |
|---|---|---|
| Wavelet peak counts and the $\ell_1$-norm are 1-pt statistics on the same starlet decomposition | Wavelet peak counts and the starlet $\ell_1$-norm are both one-point statistics of the starlet coefficients | title: twist/wit -> plain statement |

### slide 54

| before | after | what it was |
|---|---|---|
| And then the summary has to become a posterior | Peak counts and the $\ell_1$-norm have no analytic likelihood, so the inference goes through simulations | title: twist/wit -> plain statement |
| For the power spectrum there is a likelihood you can write down. For peaks, the ℓ1‑norm, or anything a network computes, there is none. | The power spectrum has an analytic likelihood. Peak counts, the ℓ1‑norm and neural summaries do not. | wit/teaching voice -> plain statement |
| So the comparison runs against simulations, the whole bottom row of the chain. This is simulation‑based inference. | Instead, the comparison with the data goes through simulations, the bottom row of the chain (simulation‑based inference). | wit/teaching voice -> plain statement |

### slide 55

| before | after | what it was |
|---|---|---|
| The classical route rests on a likelihood you can write down | Classical inference needs an explicit likelihood, usually Gaussian in the data vector | title: twist/wit -> plain statement |
| What we should believe about the cosmology after seeing the data is fixed by how well a set of parameters explains what we measured, and by what we assumed before we looked. | Bayes' theorem: the probability of the parameters given the data is proportional to the probability of the data given the parameters, times the prior. | teaching voice |

### slide 55 (+130)

| before | after | what it was |
|---|---|---|
| what we believe, after | after the data | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 55

| before | after | what it was |
|---|---|---|
| how well those parameters explain the data we measured | how well the parameters explain the data | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 55 (+130)

| before | after | what it was |
|---|---|---|
| what we assume, before we look | before the data | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 55

| before | after | what it was |
|---|---|---|
| the posterior: the contours we publish | posterior | '[term]: [gloss]' teaching voice -> technical fragment |
| the likelihood | likelihood | '[term]: [gloss]' teaching voice -> technical fragment |
| the prior: ranges on the parameters | prior | '[term]: [gloss]' teaching voice -> technical fragment |
| All the work is in the middle term, and classically we assume it is Gaussian: | The likelihood is usually assumed Gaussian in the data vector: | wit/teaching voice -> plain statement |
| Then sample it: MCMC walks the parameter space and returns the posterior. | The posterior is then sampled with MCMC. | wit/teaching voice -> plain statement |

### slide 56

| before | after | what it was |
|---|---|---|
| Learn the distribution a training set was drawn from, when all you ever see is the samples. | Learn the distribution from which a set of samples was drawn. | wit/teaching voice -> plain statement |
| $\mathbb{P}$ is never handed to us. We get $X = \{x_0, x_1, \ldots, x_n\}$ and fit a parametric $\mathbb{P}_\theta$ meant to sit close to it | the true distribution $\mathbb{P}$ is unknown; we observe samples $X = \{x_0, x_1, \ldots, x_n\}$ and fit a parametric model $\mathbb{P}_\theta$ | wit/teaching voice -> plain statement |
| once trained, you can sample from $\mathbb{P}_\theta$, and for some models evaluate the density $p_\theta(x)$ | a trained model can generate new samples, and for some model classes evaluate the density $p_\theta(x)$ | wit/teaching voice -> plain statement |
| it is indifferent to what $x$ is, which is why the same machinery is behind the models everyone has been hearing about: faces, images, video, molecules | the framework does not depend on what $x$ is: the same machinery generates faces, images, video, molecules | wit/teaching voice -> plain statement |
| Generated faces, 2014 to 2017. The same idea: learn $\mathbb{P}_\theta$, then sample it. | Generated faces, 2014 to 2017: learn $\mathbb{P}_\theta$, then sample from it. | wit/teaching voice -> plain statement |

### slide 57

| before | after | what it was |
|---|---|---|
| A normalizing flow: a simple distribution pushed through an invertible map | A normalizing flow maps a simple distribution to a complex one through an invertible transform | title: twist/wit -> plain statement |
| Start from a unit Gaussian and learn an invertible map onto the distribution you want. The density comes along by change of variables: | Start from a unit Gaussian and learn an invertible map to the target distribution. The density follows from the change of variables formula: | wit/teaching voice -> plain statement |
| each layer has a triangular Jacobian, so the determinant is a product down the diagonal, cheap enough to train on | each layer has a triangular Jacobian, so the determinant is cheap to compute | wit/teaching voice -> plain statement |
| the result is flexible, you can sample it, and you can evaluate its density, all three at once | flexible, with tractable sampling and density evaluation | wit/teaching voice -> plain statement |
| the samples, carried along | samples transported by the flow | wit/teaching voice -> plain statement |
| Condition every layer on some data $x$ and it becomes $q_\phi(\theta \mid x)$: a posterior you can fit by maximum likelihood. | Conditioning the layers on data $x$ gives $q_\phi(\theta \mid x)$, a model of the posterior that is fit by maximum likelihood. | wit/teaching voice -> plain statement |

### slide 58

| before | after | what it was |
|---|---|---|
| Simulation‑based inference: replace the likelihood with the simulator | Simulation‑based inference learns the posterior directly from simulated data | title: twist/wit -> plain statement |
| We cannot write $p(x \mid \theta)$ down, but we can draw from it. So instead of evaluating a likelihood, learn the posterior. | The likelihood $p(x \mid \theta)$ cannot be written down, but the simulator samples from it. The posterior is learned directly from simulated $(\theta, x)$ pairs. | wit/teaching voice -> plain statement |
| The cost is all in stage 1, and it is paid once: the trained flow answers any new observation immediately. That is what amortised means, and it is why coverage testing is affordable. | The simulations are the only expensive step, and they are run once. The trained flow evaluates the posterior for any observation immediately (amortised inference), which makes coverage tests cheap. | wit/teaching voice -> plain statement |

### slide 59

| before | after | what it was |
|---|---|---|
| Beating the power spectrum is a low bar. How much is actually there to get? | Beating the power spectrum is easy. How much information is there to extract? | wit/teaching voice -> plain statement |

### slide 61

| before | after | what it was |
|---|---|---|
| §3 A fair comparison: same maps, same flow, both calibrated | §3 Both summaries are compared on the same maps, through the same flow, with both arms calibrated | title: twist/wit -> plain statement |

### slide 62

| before | after | what it was |
|---|---|---|
| §3 Read bin by bin, the ℓ1-norm trails the network | §3 The CNN beats the per-bin ℓ1-norm by 36% in FoM | title: twist/wit -> plain statement |
| same maps, same flow, both calibrated. Only the summary changes | same maps, same flow, both calibrated; only the summary differs | wit/teaching voice -> plain statement |
| But they are not reading the same thing: the $\ell_1$-norm one bin at a time, the network all four maps together | But the comparison is not symmetric: the $\ell_1$-norm sees one bin at a time, the network all four bins together | wit/teaching voice -> plain statement |
| So close that asymmetry, and see how much of the gap goes with it | Next: remove the asymmetry and see how much of the gap remains | wit/teaching voice -> plain statement |

### slide 64

| before | after | what it was |
|---|---|---|
| §3 Two routes to the inter-bin information: build cross maps, or read the pair jointly | §3 The cross-bin information can be reached through cross maps or through a joint statistic | title: twist/wit -> plain statement |
| multiply the two bins pixel by pixel: bright only where both have structure. Six such channels, one per bin pair, each read by the same ℓ1-norm. | the pixel-wise product of two bins is non-zero only where both have structure. Six such maps, one per bin pair, each analysed with the same ℓ1-norm. | wit/teaching voice -> plain statement |
| the per-bin ℓ1-normonly ever sees thetwo axis histograms | the per-bin ℓ1-normonly sees the twomarginal histograms | wit/teaching voice -> plain statement |
| each cell holds the ℓ1 weight of the pixels landing in it | each cell sums the ℓ1 weight of the pixels that fall in it | wit/teaching voice -> plain statement |
| A cross-map collapses each pair into one field before the statistic is taken. The joint ℓ1-norm keeps the whole plane, and needs no new map at all. | The cross-map reduces each bin pair to one field before computing the statistic. The joint ℓ1-norm uses the full 2-D distribution and needs no additional maps. | wit/teaching voice -> plain statement |

### slide 65

| before | after | what it was |
|---|---|---|
| §3 Read the bins jointly and the analytical ℓ1-norm reaches the optimal CNN | §3 With joint reading of the bins, the ℓ1-norm matches the optimal CNN | title: twist/wit -> plain statement |

### slide 66

| before | after | what it was |
|---|---|---|
| The non-Gaussian information and the worst small-scale systematic live on the same scales | Non-Gaussian information and baryonic feedback both live at small scales | title: twist/wit -> plain statement |

### slide 67

| before | after | what it was |
|---|---|---|
| The same pipeline, and the wavelet keeps the scales separate | In the SBI pipeline, the statistics are computed separately on each wavelet scale | title: twist/wit -> plain statement |

### slide 69

| before | after | what it was |
|---|---|---|
| §4 Buying back an unbiased inference costs $C_\ell$ most of its multipole range, and the starlet its finest band | §4 Removing the bias costs $C_\ell$ most of its multipole range, and the starlet only its finest band | title: twist/wit -> plain statement |
| $C_\ell$ takes a sliding cut, tuned to what is safe at each area: $\ell_{\rm max} = 860$ at 2,000 deg² falling to 340 at full sky | $C_\ell$: $\ell_{\rm max}$ tuned per survey area, from 860 at 2,000 deg² to 340 at full sky | wit/teaching voice -> plain statement |
| The starlet concentrates the contamination in its finest band, so dropping $j=1$ suffices at every area | starlet: the contamination is concentrated in the finest band, so dropping $j=1$ is enough at every area | wit/teaching voice -> plain statement |
| whole bands only, so we cut more than we need | whole bands only, a more conservative cut | wit/teaching voice -> plain statement |

### slide 70

| before | after | what it was |
|---|---|---|
| and this is a floor | and this is conservative | 'floor' metaphor |
| the signal survives on quasi‑linear scales, so HOS are not just probes of the deep non‑linear regime | the non-Gaussian signal survives on quasi‑linear scales | wit/teaching voice -> plain statement |
| our whole‑band cut is not optimised, and better baryon modelling pushes the analysis deeper, where the gain is larger | the whole‑band cut is not optimised, and better baryon modelling would allow smaller scales, where the gain is larger | wit/teaching voice -> plain statement |

### slide 72

| before | after | what it was |
|---|---|---|
| The four questions, answered | Answers to the four questions | title: twist/wit -> plain statement |
| Is mass mapping preprocessing, or does the choice of reconstruction change the cosmology we infer? | Does the choice of mass-mapping method matter for the final constraints? | Q1 |
| It changes the cosmology. Swap the reconstruction and nothing else, and the figure of merit moves by 157 %, while the reconstruction error moves by 4 %. Map quality and constraining power are different objectives. | Yes. Changing only the reconstruction method changes the figure of merit by 157 %, while the reconstruction error changes by 4 %. Reconstruction error is not a good proxy for constraining power. | A1 |
| Can one reconstruction be flexible, fast, accurate, and tell you how wrong it is? | Can one method be accurate, flexible and fast, with reliable uncertainties, at the scale of Euclid? | Q2 |
| Yes, PnPMass does. It is within 1 % of a network fine‑tuned to the observation, has the smallest calibrated error bars of any method tested, and is trained once rather than per footprint. | Yes. PnPMass is within 1 % in RMSE of a network fine‑tuned to the observation, has the smallest calibrated error bars of all methods tested, and is trained once for any mask and noise level. | A2 |
| What is the most we can read out of a map, and does it take a neural network? | How much cosmological information can a summary statistic extract from the maps, and how do we turn it into a posterior? | Q3, now identical to the board |
| No, it does not take a network. Read the bins jointly and a fixed wavelet ℓ1‑norm matches an information‑optimal learned compressor, with no training at all. | As much as an optimal neural compressor, and without a network. With joint reading of the tomographic bins, the wavelet ℓ1‑norm matches a VMIM‑trained CNN. Either summary goes through the same normalising flow to a calibrated posterior. | A3 |
| Does any of that survive the real Universe, where there is astrophysics we cannot model? | Do these results hold up against astrophysical systematics we cannot model, such as baryonic feedback? | Q4 |
| Yes. Cut every scale that unmodelled baryons measurably touch, and the ℓ1‑norm is still ×1.8 tighter than $C_\ell$ at Stage IV and ×2.6 at full sky. Our cut is the crudest one available, so those numbers are a lower bound. | Yes. After removing every scale affected by unmodelled baryons, the ℓ1‑norm still constrains ×1.8 tighter than $C_\ell$ at Stage IV and ×2.6 at full sky, with the most conservative scale cut available. | A4 |

### slide 75

| before | after | what it was |
|---|---|---|
| Q2 With no feedback model at all, cutting every contaminated scale still leaves the ℓ1-norm ahead of the power spectrum | Q2 Without any feedback model, the ℓ1-norm stays ahead of the power spectrum on baryon-safe scales | title: twist/wit -> plain statement |
| A floor: no feedback model, every contaminated scale discarded. | Conservative case: no feedback model, every contaminated scale removed. | wit/teaching voice -> plain statement |

### slide 76

| before | after | what it was |
|---|---|---|
| Q1 Build joint reading in, and a fixed wavelet statistic reaches the ceiling | Q1 The joint ℓ1-norm reaches the FoM of the optimal compressor | title: twist/wit -> plain statement |
| joint ℓ1-norm, new | joint ℓ1-norm (this work) | wit/teaching voice -> plain statement |
| ↑ the ceiling, a compressor trained to be optimal | ↑ reference: a compressor trained to be information-optimal | wit/teaching voice -> plain statement |

### slide 77

| before | after | what it was |
|---|---|---|
| Q1 Given the same constraining power, everything else decides | Q1 At equal constraining power, the analytical statistic is cheaper and safer to use | title: twist/wit -> plain statement |
| fixed — the ℓ1-norm | analytical — the ℓ1-norm | wit/teaching voice -> plain statement |
| The compressor keeps one advantage: it reads the bins jointly for free. That matters in the nulled frame. | One advantage of the compressor remains: it reads the bins jointly by construction. This matters in the nulled frame. | wit/teaching voice -> plain statement |

### slide 86

| before | after | what it was |
|---|---|---|
| §4 The information is recoverable by the summary that reads the bins jointly | §4 The information is recovered by a summary that reads the bins jointly | title: twist/wit -> plain statement |
| Same four summaries as before. In the standard frame they spanned 38%; here, a factor of six. | Same four summaries. In the standard frame they span 38% in FoM; in the nulled frame, a factor of six. | wit/teaching voice -> plain statement |
| So nulling can be kept as a mitigation at no cost in constraining power, provided some stage of the pipeline reads the bins jointly. The power spectrum was the first rung of this same ladder. | Nulling costs no constraining power provided some stage of the pipeline reads the bins jointly. The power spectrum with its cross-spectra is the simplest example. | wit/teaching voice -> plain statement |

### slide 90

| before | after | what it was |
|---|---|---|
| §3 The analytical statistic ties it, and it is the safer instrument | §3 The analytical statistic ties the CNN, at lower cost and risk | title: twist/wit -> plain statement |
| the thumb on the scale | in favour of the ℓ1-norm | wit/teaching voice -> plain statement |

### slide 92

| before | after | what it was |
|---|---|---|
| §4 You can see it in the maps: BNT trades deep signal for amplified, correlated noise | §4 BNT amplifies and correlates the shape noise in the maps | title: twist/wit -> plain statement |

### slide 93

| before | after | what it was |
|---|---|---|
| §4 The same maps, noiseless: BNT cleanly redistributes the signal | §4 Without noise, BNT redistributes the signal without loss | title: twist/wit -> plain statement |
| Without shape noise, BNT is a clean, invertible redistribution of the signal (the deep common mode becomes one shallow map plus thin slices). The contour inflation comes from the correlated noise it introduces, not from any lost signal. | Without shape noise, BNT is an invertible redistribution of the signal (the common mode becomes one shallow map plus thin slices). The contour inflation comes from the correlated noise, not from lost signal. | wit/teaching voice -> plain statement |

### slide 94

| before | after | what it was |
|---|---|---|
| §3 Where the cross-bin information lives: the κiκj product buys +24%, and reading each pair jointly buys the rest | §3 Cross-bin information: the κiκj product gives +24%, the joint ℓ1-norm the rest | title: twist/wit -> plain statement |
| add the cross-bin physics carefully | cross-map constructions | wit/teaching voice -> plain statement |

### slide 95

| before | after | what it was |
|---|---|---|
| §4 The clincher: a frame artifact, not lost information (one rotation recovers ℓ1, 1.06×) | §4 One whitening rotation recovers the full ℓ1-norm FoM (1.06×), so no information is lost | title: twist/wit -> plain statement |
| the information was never lost | the information is recovered | wit/teaching voice -> plain statement |

### slide 96

| before | after | what it was |
|---|---|---|
| backup One story: the optimal tomographic strategy (BNT becomes viable once the summary mixes bins) | backup Summary: BNT becomes viable once the summary statistic mixes the bins | title: twist/wit -> plain statement |
| one escalating story about cross-bin information | the common thread: cross-bin information | wit/teaching voice -> plain statement |
| Forward-looking: a route to baryon-robust, non-Gaussian SBI that keeps BNT's clean per-bin scale cuts without the contour-inflation tax. A next step, not a finished end-to-end measurement. | Outlook: a route to baryon-robust non-Gaussian SBI that keeps BNT's per-bin scale cuts without the contour inflation. A next step rather than a finished end-to-end measurement. | wit/teaching voice -> plain statement |

### slide 103

| before | after | what it was |
|---|---|---|
| Where the ℓ1-norm’s constraining power sits | Where the ℓ1-norm’s constraining power comes from | title: twist/wit -> plain statement |

### slide 106

| before | after | what it was |
|---|---|---|
| The tie, per mock rather than at the median | The tie per mock observation | title: twist/wit -> plain statement |

### slide 107

| before | after | what it was |
|---|---|---|
| §4 The channel-mixing CNN does not notice the transform at all (0.96×) | §4 The channel-mixing CNN is unaffected by the transform (0.96×) | title: twist/wit -> plain statement |

### slide 121

| before | after | what it was |
|---|---|---|
| Fourier tells you which scales are there. A wavelet tells you which, and where | Wavelets are localised in both scale and position | title: twist/wit -> plain statement |
| a wavelet is a function $\psi$ that is compact and oscillates with zero mean, $\int\psi\,\mathrm{d}x = 0$. Those two properties are the whole definition | a wavelet is a localised, oscillating function $\psi$ with zero mean, $\int\psi\,\mathrm{d}x = 0$ | '[term]: [gloss]' teaching voice -> technical fragment |
| one shape generates a family, $\psi_{a,b}(x) = \tfrac{1}{\sqrt{a}}\, \psi\!\left(\tfrac{x-b}{a}\right)$, and the coefficient $W(a,b) = \int f\,\psi_{a,b}$ asks how much structure of size $a$ sits at $b$ | dilations and translations form a family, $\psi_{a,b}(x) = \tfrac{1}{\sqrt{a}}\, \psi\!\left(\tfrac{x-b}{a}\right)$; the coefficient $W(a,b) = \int f\,\psi_{a,b}$ measures the structure at scale $a$ and position $b$ | '[term]: [gloss]' teaching voice -> technical fragment |
| a sine has infinite support: perfect resolution in frequency, none in position. A wavelet gives up a little of the first to buy the second | a sine has infinite support: full frequency resolution, no spatial resolution. A wavelet trades some of the former for the latter | '[term]: [gloss]' teaching voice -> technical fragment |
| for a field made of localised objects (peaks, filaments, voids) that is the right trade. The power spectrum is the Fourier answer; peaks and the ℓ1‑norm are the wavelet one | for a field of localised structures (peaks, filaments, voids) this is the right trade. The power spectrum is the Fourier statistic; peaks and the ℓ1‑norm are the wavelet ones | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 122

| before | after | what it was |
|---|---|---|
| The transform: the same data at every scale at once | The starlet transform splits the data into one band-pass image per scale plus a coarse residual | title: twist/wit -> plain statement |
| slide the dilated wavelet across the data at each scale: the result is one band‑pass image per scale, plus a coarse residual holding what is left | convolving the data with the dilated wavelet at each scale gives one band‑pass image per scale, plus a coarse residual | '[term]: [gloss]' teaching voice -> technical fragment |
| the starlet version used here is isotropic and undecimated: every band keeps the full pixel grid, so nothing is lost and the reconstruction is exact, $I = c_J + \sum_j w_j$ | the starlet is isotropic and undecimated: every band keeps the full pixel grid, and the reconstruction is exact, $I = c_J + \sum_j w_j$ | '[term]: [gloss]' teaching voice -> technical fragment |
| a feature of a given angular size lands in one band, and that is what makes the scale cut in Part 3 cheap | a structure of a given angular size appears in a single band, so a scale cut amounts to dropping one band | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 123

| before | after | what it was |
|---|---|---|
| Where most people meet wavelets: images | In image processing, the same transform is used for compression and denoising | title: twist/wit -> plain statement |
| compression: almost all of an image sits in a few large coefficients: keep those, discard the rest. That is JPEG 2000 | compression: most of the image is in a few large coefficients; keep those and discard the rest (JPEG 2000) | '[term]: [gloss]' teaching voice -> technical fragment |
| denoising: the same move with a different rule: threshold the small coefficients. That is the proximal step in Part 1 | denoising: threshold the small coefficients (the proximal step of Part 1) | '[term]: [gloss]' teaching voice -> technical fragment |
| ours is isotropic and undecimated instead: a convergence field has no grain and no preferred direction, and we want every scale on the full grid | the starlet is isotropic and undecimated: no preferred direction, and every scale on the full pixel grid | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 124

| before | after | what it was |
|---|---|---|
| , the map smoothed by a filter, in units of the noise. | , the signal-to-noise field of the filtered map. | '[term]: [gloss]' teaching voice -> technical fragment |
| peaks sit where $\kappa$ is high, so they trace massive structures | peaks trace regions of high $\kappa$, i.e. massive structures | '[term]: [gloss]' teaching voice -> technical fragment |
| counting them by height is a one‑point statistic that sees what the power spectrum cannot | the peak function (counts per SNR bin) is a one‑point statistic sensitive to non-Gaussian information | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 125

| before | after | what it was |
|---|---|---|
| One starlet transform, peaks at every scale | A single starlet transform gives peak counts at every scale | title: twist/wit -> plain statement |
| counting peaks band by band is a multi‑scale analysis, where a single filter size is not | counting peaks band by band gives a multi‑scale analysis | '[term]: [gloss]' teaching voice -> technical fragment |
| all the scales are processed at once, from one transform | all scales from a single transform | '[term]: [gloss]' teaching voice -> technical fragment |
| the bands cover different frequency ranges, so the peak‑count covariance comes out almost diagonal | the bands cover different frequency ranges, so the peak‑count covariance is almost diagonal | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 126

| before | after | what it was |
|---|---|---|
| The starlet $\ell_1$‑norm reads every pixel, not just the maxima | The starlet $\ell_1$‑norm uses every pixel | title: twist/wit -> plain statement |
| peaks and voids are included automatically: no threshold to choose, no definition of a peak to defend | peaks and voids are included automatically, with no threshold and no peak definition | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 130

| before | after | what it was |
|---|---|---|
| So write the assumption down | Every mass-mapping method is a Bayesian inference with a different prior on κ | title: twist/wit -> plain statement |
| What we should believe after seeing the data is fixed by two things: how well an answer explains what we saw, and what we assumed before we looked. | The posterior probability of a map given the shear is proportional to the likelihood of the shear given the map, times the prior on the map. | teaching voice |
| how well that explains the shear we measured | how well the map explains the shear | '[term]: [gloss]' teaching voice -> technical fragment |
| the posterior: the map we report | posterior | '[term]: [gloss]' teaching voice -> technical fragment |
| the likelihood: physics we already have | likelihood (forward model) | '[term]: [gloss]' teaching voice -> technical fragment |
| the prior | prior | '[term]: [gloss]' teaching voice -> technical fragment |
| stop choosing: learn it from simulations | prior learned from simulations | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 130+131

| before | after | what it was |
|---|---|---|
| The same three terms come back in Part 3, with the cosmological parameters as the unknown and a likelihood we can no longer write down. | The same structure returns in Part 3, with the cosmological parameters as the unknown and no explicit likelihood. |  |

### slide 131

| before | after | what it was |
|---|---|---|
| Writing it as inference makes the assumption explicit | The Bayesian view makes the prior explicit | title: twist/wit -> plain statement |
| the map we end up with, after seeing the data | the map, given the data | '[term]: [gloss]' teaching voice -> technical fragment |
| how well a given map explains the shear we measured | how well a map explains the measured shear | '[term]: [gloss]' teaching voice -> technical fragment |
| physics we already have: the operator from two slides ago | the forward model | '[term]: [gloss]' teaching voice -> technical fragment |
| what we take a mass map to look like, before we look | what we assume about the map | '[term]: [gloss]' teaching voice -> technical fragment |
| the choice, and the only term that changes | the only term that differs between methods | '[term]: [gloss]' teaching voice -> technical fragment |

### slide 136

| before | after | what it was |
|---|---|---|
| §2 Error bars from one extra forward pass, with a coverage guarantee on top | §2 Pixel-wise uncertainties from a second network, calibrated with conformal prediction | title: twist/wit -> plain statement |
| what this part of the talk adds | this work | wit/teaching voice -> plain statement |
| Noise and the mask leave the whole family of maps from Part 1, and the prior that picks one of them is learned from simulations. The variance has to cover both. | The posterior spread comes from the noise and the mask (Part 1), and from the learned prior that selects one map. The predicted variance has to account for both. | wit/teaching voice -> plain statement |
| A network's own variance is not a guarantee. | The variance predicted by a network is not calibrated. | wit/teaching voice -> plain statement |
| Conformal quantile regression rescales it pixel by pixel against a held‑out set, until the coverage is the coverage claimed. | Conformal quantile regression rescales it pixel by pixel on a held‑out calibration set, so that the intervals reach the target coverage. | wit/teaching voice -> plain statement |
| Instead of “the network says $\pm\sigma$”: a stated coverage level that holds whether or not the network is well specified. | The result is a coverage guarantee that holds whether or not the network is well specified. | wit/teaching voice -> plain statement |

---

# Pass 3, same day: the speaker notes and SPEAKER_SCRIPT.md

Mirrors the slide changes where the notes or the script quote slide text (the four questions,
the four answers, the DES Y3 beat, the Euclid hand-off, the Bayes beat), and sweeps the tics
("honest" ×14, "quietly", "genuinely" ×5, "bookkeeping for belief", "which is exactly", "that is
what makes", "all along"). Spoken em dashes are pause marks and were left alone. 18 note edits,
30 script edits. Beat headings and timings in the script are untouched except A2.7's title.

### speaker notes in index.html

| slide | before | after | what it was |
|---|---|---|---|
| 6 | carry the statistical memory of the whole history of the Universe | carry the imprint of the whole history of the Universe | metaphor |
| 7 | Before I show you my own picture, here is an honest one. | Before I show you my own picture, here is a real one. | 'honest' tic |
| 8 | can bias the answer or quietly throw information away with nothing inside the pipeline noticing. | can bias the result or discard information, with no internal check that would catch it. | 'quietly' + personified pipeline |
| 8 | flexible, fast, accurate, and honest about how wrong it is — all four at once, on a survey the size of Euclid. | accurate, flexible, fast, and with reliable uncertainties — all four at once, at the scale of Euclid. | 'honest' tic; matches the new Q2 |
| 10 (hidden) | Question two builds a reconstruction that is honest about its own uncertainty. | Question two builds a reconstruction with reliable uncertainties. | 'honest' tic |
| 31 | Two honest limits, and I would rather say them than be asked | Two limitations, and I would rather say them than be asked | 'honest' tic |
| 31 | which is exactly where Part 1 said the information lives | which is where Part 1 said the information lives | 'which is exactly' |
| 45 | can we build a better one with honest error bars | can we build a better one with calibrated error bars | 'honest' tic |
| 56 | The honest reason this slide exists: | The reason this slide exists: | 'honest' tic |
| 59 | The honest answer is that the optimality claim | The answer is that the optimality claim | 'honest' tic |
| 62 | so the bins carry genuinely correlated information | so the bins carry correlated information | 'genuinely' |
| 62 | which is the honest way to find out. | which is the only way to find out. | 'honest' tic |
| 67 | That is what makes a scale cut possible at all - a contaminated band can be dropped without touching the rest. | Without that, a scale cut would not be possible: a contaminated band can be dropped without touching the rest. | 'that is what makes' |
| 77 | the last line is the honest hand-off into the BNT act. | the last line is the hand-off into the BNT act. | 'honest' tic |
| 85 | That is a genuinely promising way to do scale cuts. | That is a promising way to do scale cuts. | 'genuinely' |
| 86 | The two-point case was the first rung of this same ladder all along. | The two-point case is the simplest instance of the same thing. | 'all along' reveal |
| 86 | HONEST RESIDUAL: the joint l1 keeps 0.72 | RESIDUAL: the joint l1 keeps 0.72 | 'honest' tic |
| 121 | Which is the honest one-line summary of this whole part of the talk: | Which is the one-line summary of this whole part of the talk: | 'honest' tic |

### SPEAKER_SCRIPT.md

| beat | before | after | what it was |
|---|---|---|---|
| A0.6 | And that signal is the statistical memory of everything the Universe has done since the Big Bang. | And that signal encodes the growth of structure and the geometry of the Universe since the Big Bang. | metaphor; matches slide 6 |
| A0.7 | Before my own picture of that, an honest one: the DES Year 3 analysis | Before my own picture of that, a real one: the DES Year 3 analysis | 'honest' tic |
| A0.7 | [CLICK] Nearly every box is its own paper, and most of them are measurement and calibration. | [CLICK] Almost every box is a paper on its own, and most of them are measurement and calibration. | mirror the slide |
| A0.7 | **▲** A real survey analysis is mostly not the physics, and I am not going to talk about most of it. | **▲** Most of a real survey analysis is measurement and calibration, and I am not going to talk about most of it. | 'not the physics' twist |
| A0.8 | Between the shapes we measure and the parameters we report there is a chain: a catalogue, binned | From the shapes we measure to the parameters we report, the analysis is a chain: a catalogue, binned | mirror the slide |
| A0.8 | [CLICK] **▲** Every one of those stages is now built out of learned components, and every one can bias the answer or quietly throw information away, with no internal check noticing. | [CLICK] **▲** Each of those steps now involves learned components, and each one can bias the result or discard information, with no internal check that would catch it. | 'quietly'; matches slide 8 |
| A0.8 | **▲** So: is mass mapping preprocessing, or does the choice of reconstruction change the cosmology? | **▲** So: does the choice of mass-mapping method matter for the final constraints? | Q1, matches the board |
| A0.8 | we want a reconstruction that is flexible, fast, accurate **and** honest about how wrong it is — all four, on a survey the size of Euclid. | we want a method that is accurate, flexible and fast, **and** gives reliable uncertainties — all four, at the scale of Euclid. | Q2, 'honest' tic |
| A0.8 | **▲** So: what is the most we can read out of a map, and what does it take? | **▲** So: how much information can a summary statistic extract from the maps, and how do we turn it into a posterior? | Q3, matches the board |
| A0.8 | **▲** Does any of it survive that? | **▲** Do the results hold up against that? | Q4 |
| A1.1 | so does that choice change the cosmology, or is it preprocessing? | so does the choice of method matter for the final constraints? | Q1 |
| A1.x Bayes | **▲** Bayes' rule is bookkeeping for belief. What we should believe about the map after seeing the data is fixed by two things: how well a candidate map explains the shear we measured, which is physics we already have — times what we assumed before we looked, which is the prior. | **▲** In Bayesian terms: the posterior probability of a map given the shear is the likelihood of the shear given the map, which is physics we already have — times the prior, what we assumed before we looked. | aphorism; teaching voice |
| A1.x Bayes | [CLICK] The regulariser was the prior all along. | [CLICK] The regulariser is the prior. | 'all along' |
| A2.2 | Fast enough for a survey. And honest about how wrong it is. | Fast enough for a survey. And reliable uncertainties. | 'honest' tic |
| A2.7 | ## A2.7 — accurate, and honest about it · frame 27 · 1:46 | ## A2.7 — accurate, with calibrated uncertainties · frame 27 · 1:46 | 'honest' tic |
| A3.x | [CLICK] It is the objection I would raise myself. The honest answer is that the optimality claim is | [CLICK] It is the objection I would raise myself. The answer is that the optimality claim is | 'honest' tic |
| A4.x | so the data vector is organised by scale. That is what makes a scale cut possible at all. | so the data vector is organised by scale. Without that, a scale cut would not be possible. | 'that is what makes' |
| A4.6 note | > the thesis that is genuinely counter-intuitive, and it is written out below. | > the thesis that is counter-intuitive, and it is written out below. | 'genuinely' |
| A4.6 | **▲** A genuinely promising way to do scale cuts | **▲** A promising way to do scale cuts | 'genuinely' |
| A4.6 | **▲** And the power spectrum was the first rung of this same ladder all along. Auto plus cross | **▲** And the power spectrum with its cross-spectra is the simplest case of the same thing. Auto plus cross | 'all along' reveal |
| Conclusions | **One.** Mass mapping is not preprocessing. Swap the reconstruction and nothing else, and the figure of merit moves by a hundred and fifty-seven per cent while the reconstruction error moves by four. **▲** Map quality and constraining power are different objectives. | **One.** Yes, the choice of mass-mapping method matters. Change the reconstruction and nothing else, and the figure of merit moves by a hundred and fifty-seven per cent while the reconstruction error moves by four per cent. **▲** Reconstruction error is not a good proxy for constraining power. | A1, matches slide 72 |
| Conclusions | and is trained once rather than per footprint. **▲** Which is what makes it a method a survey could run. | and is trained once for any mask and noise level. **▲** That is what a survey needs. | A2, 'which is what makes' |
| Conclusions | **Three.** No, we do not need a network to read the maps. Build joint reading into the statistic and a fixed wavelet ℓ1-norm matches an information-optimal learned compressor, with no training. | **Three.** As much as an optimal neural compressor, and we do not need the network. Read the bins jointly and a fixed wavelet ℓ1-norm matches a VMIM-trained CNN, with no training; either summary goes through the same flow to a calibrated posterior. | A3, matches slide 72 |
| Conclusions | **Four.** Baryons do not put it out of reach. Cut every contaminated scale and the ℓ1-norm is still one point eight times tighter at Stage IV, two point six at full sky. **▲** And that is a floor. | **Four.** Yes, they hold up. Cut every contaminated scale and the ℓ1-norm is still one point eight times tighter at Stage IV, two point six at full sky. **▲** And that is with the most conservative cut available. | A4, 'floor' |
| Q&A | answer is only as good as the simulations, which is exactly why Part 4 exists. | answer is only as good as the simulations, which is why Part 4 exists. | 'which is exactly' |
| Q&A note | **Do not improvise this one** — it is the genuinely > counter-intuitive result in the thesis | **Do not improvise this one** — it is the > counter-intuitive result in the thesis | 'genuinely' |
| Q&A | Time, and it is the honest answer. It is the one result | Time. It is the one result | 'honest' tic |
| Q&A | The honest form of the objection, and it deserves the working. | A fair objection, and it deserves the working. | 'honest' tic |
| Q&A | **The honest converse:** with a | **The converse:** with a | 'honest' tic |
| Q&A | by band — which is exactly what Part 4 needs — and a covariance | by band — which is what Part 4 needs — and a covariance | 'which is exactly' |

## Pass 4: five titles trimmed after the screenshot check

| slide | before | after | what it was |
|---|---|---|---|
| 31 | PnPMass matches the accuracy of the fine‑tuned networks, with the smallest calibrated error bars | PnPMass is as accurate as the fine‑tuned networks, with the smallest calibrated error bars | title wrapped; shortened |
| 47.5 | Peak counts constrain better than the power spectrum, and multi‑scale peaks better than single‑scale | Peak counts constrain better than the power spectrum, multi‑scale peaks better still | title wrapped; shortened |
| 53 | Wavelet peak counts and the starlet $\ell_1$-norm are both one-point statistics of the starlet coefficients | Wavelet peak counts and the $\ell_1$-norm are one-point statistics of the starlet coefficients | title wrapped; shortened |
| 54 | Peak counts and the $\ell_1$-norm have no analytic likelihood, so the inference goes through simulations | Peak counts and the $\ell_1$-norm have no analytic likelihood, so the inference uses simulations | title wrapped; shortened |
| 61 | §3 Both summaries are compared on the same maps, through the same flow, with both arms calibrated | §3 Both summaries are compared on the same maps, through the same flow, both calibrated | title wrapped; shortened |
| 75 | Q2 Without any feedback model, the ℓ1-norm stays ahead of the power spectrum on baryon-safe scales | Q2 Without any feedback model, the ℓ1-norm stays ahead of the power spectrum | title wrapped; shortened |

## Status of the pass-1 "flagged and left alone" list

- Script and notes: **done** in pass 3.
- Q3 wording on the board vs the conclusions: **reconciled** in pass 2 (both use the board's form).
- "statistical memory" hand-off line: **replaced** (slide 6, notes and script).
- "floor" / "ceiling" / "the thumb on the scale" / "movement II" / "one story": **replaced** in pass 2.
- "CNNs are powerful but treacherous" (slide 90): still there; conference voice, and Andreas's.
- Label-separator em dashes in kickers and bylines: still there (23), typography.
- Hidden, parked and LAM-lifted slides: still untouched, except the hidden copies of the
  four-question board, which follow the live one.

---

# Pass 5, same day: the conclusions slide, STRUCTURE.md and the script headings

- **Conclusions slide (frame 53):** cut to one line per question and one per answer. The
  questions are short forms of the board's; the answers keep only the number or the one claim.
  The slide's notes now say "in short form" instead of "in the same words".
- **STRUCTURE.md:** the four-question table (rewritten to the slides' wording and reordered to
  the deck's Q3 = summaries, Q4 = baryons), the running-order "on screen" cells for every
  retitled frame, the frame-9 click table, the three takeaways and the honesty-flag row.
  Decision narrative and dated history were left as written.
- **SPEAKER_SCRIPT.md:** six beat headings and two cross-reference labels that carried old
  titles, and the three spoken "floor" lines.

## Conclusions slide

| slide | before | after | what it was |
|---|---|---|---|
| 72 | Does the choice of mass-mapping method matter for the final constraints? | Does the choice of mass-mapping method matter? | conclusions cut to one line each |
| 72 | Yes. Changing only the reconstruction method changes the figure of merit by 157 %, while the reconstruction error changes by 4 %. Reconstruction error is not a good proxy for constraining power. | Yes. The figure of merit moves by 157 %, the reconstruction error by 4 %. | conclusions cut to one line each |
| 72 | Can one method be accurate, flexible and fast, with reliable uncertainties, at the scale of Euclid? | Can one method be accurate, flexible and fast, with reliable uncertainties? | conclusions cut to one line each |
| 72 | Yes. PnPMass is within 1 % in RMSE of a network fine‑tuned to the observation, has the smallest calibrated error bars of all methods tested, and is trained once for any mask and noise level. | Yes. PnPMass is within 1 % of the fine‑tuned networks, with the smallest calibrated error bars, trained once. | conclusions cut to one line each |
| 72 | How much cosmological information can a summary statistic extract from the maps, and how do we turn it into a posterior? | How much information can a summary statistic extract, and does it take a network? | conclusions cut to one line each |
| 72 | As much as an optimal neural compressor, and without a network. With joint reading of the tomographic bins, the wavelet ℓ1‑norm matches a VMIM‑trained CNN. Either summary goes through the same normalising flow to a calibrated posterior. | As much as an optimal CNN, and without one. The joint ℓ1‑norm ties the VMIM‑trained compressor. | conclusions cut to one line each |
| 72 | Do these results hold up against astrophysical systematics we cannot model, such as baryonic feedback? | Do the results hold up against unmodelled baryonic feedback? | conclusions cut to one line each |
| 72 | Yes. After removing every scale affected by unmodelled baryons, the ℓ1‑norm still constrains ×1.8 tighter than $C_\ell$ at Stage IV and ×2.6 at full sky, with the most conservative scale cut available. | Yes. On baryon‑safe scales the ℓ1‑norm is still ×1.8 tighter than $C_\ell$ at Stage IV, ×2.6 at full sky. | conclusions cut to one line each |

## STRUCTURE.md

| before | after |
|---|---|
| \| **Q1** \| Is mass mapping preprocessing, or does the choice of reconstruction change the cosmology we infer? \| A1.4–A1.5 \| **It changes it.** Same simulations, same peak counts, same likelihood — swapping KS for MCA | \| **Q1** \| Does the choice of mass-mapping method matter for the final constraints? \| A1.4–A1.5 \| **Yes.** Same simulations, same peak counts, same likelihood; swapping KS for MCALens moves the four-parameter figure  |
| \| 0.2 \| 13.8 billion years, from quantum fluctuations to galaxies \| | \| 0.2 \| The Universe evolved from quantum fluctuations to galaxies over 13.8 billion years \| |
| \| 0.3 \| ΛCDM: six numbers, and the assumptions that let you get away with six \| | \| 0.3 \| ΛCDM describes the Universe with six free parameters, plus a set of assumptions \| |
| \| 0.4 \| Independent probes are a test — and they do not quite agree \| | \| 0.4 \| Independent probes test the model through both geometry and growth; the late-time S8 and the local H0 disagree with the CMB predictions \| |
| \| 0.5 \| A 1 % distortion, invisible alone, **coherent** across neighbours \| | \| 0.5 \| Foreground mass deflects the light of background galaxies and distorts their images \| |
| the lensing signal is the **statistical memory** of the whole history of the Universe, and getting it out is an **algorithms** problem | the lensing signal encodes the growth of structure and the geometry of the Universe, and extracting it is an **algorithms** problem |
| \| 0.7 \| A real weak-lensing analysis is **dozens of steps**, and most of them are not the physics \| | \| 0.7 \| Most of a real weak-lensing analysis is **measurement and calibration** \| |
| \| 0.8 \| Between the shapes and the parameters there is a **chain** — and **the four questions of the thesis on it** \| | \| 0.8 \| The analysis chain from galaxy shapes to parameters, and **the four questions of this thesis** \| |
| \| 1.4 \| **TEACH** So write the assumption **down** — posterior, likelihood, prior \| | \| 1.4 \| **TEACH** Every mass-mapping method is a Bayesian inference with a different **prior** on κ \| |
| \| 1.4b \| MCALens: **two components**, and a different rule for each \| | \| 1.4b \| MCALens models κ as a **Gaussian plus a sparse** component \| |
| \| 1.5 \| Different assumptions, different maps — and **nobody had checked** whether it mattered \| | \| 1.5 \| Different priors give different maps. Does the difference reach the **constraints**? \| |
| \| 1.5a \| Same simulations, same statistic, same likelihood — **only the map changes** \| | \| 1.5a \| The simulations, statistic and likelihood are fixed, and only the **mass-mapping method** varies \| |
| \| 1.5b \| Kaiser–Squires **smooths the small scales away**. MCALens does not. \| | \| 1.5b \| MCALens recovers **small-scale structure** that Kaiser–Squires smooths out \| |
| \| 1.6 \| **Swapping the reconstruction alone moves the FoM by 157 %** \| | \| 1.6 \| **MCALens improves the FoM by 157 % over Kaiser–Squires** \| |
| \| 1.7 \| MCALens keeps gaining to 2′; KS saturated at 8′ \| | \| 1.7 \| The gain comes from scales below 8′, which only MCALens recovers \| |
| \| 2.1 \| *Flexible, fast, accurate and honest about its uncertainty — at once?* \| | \| 2.1 \| *Accurate, flexible and fast, with reliable uncertainties, at the scale of Euclid?* \| |
| \| 3.2 \| The information and the worst systematic live on the same scales \| | \| 3.2 \| Non-Gaussian information and baryonic feedback both live at small scales \| |
| \| 3.5 \| Unmodelled feedback biases every statistic, and worse the bigger the survey \| | \| 3.5 \| Baryonic bias grows with survey area \| |
| \| 3.6 \| Buying back an unbiased answer costs the power spectrum most of its range \| | \| 3.6 \| Removing the bias costs the power spectrum most of its multipole range, and the starlet only its finest band \| |
| \| 4.2 \| Beating the power spectrum is a low bar — what is the ceiling? \| | \| 4.2 \| Beating the power spectrum is easy; how much information is there to extract? \| |
| \| 4.4 \| Read bin by bin, the ℓ1-norm reaches three quarters of the ceiling \| | \| 4.4 \| The CNN beats the per-bin ℓ1-norm by 36 % in FoM \| |
| \| 4.5 \| Two routes to the inter-bin information — or read each pair jointly \| | \| 4.5 \| The cross-bin information can be reached through cross maps or through a joint statistic \| |
| \| 4.6 \| **A fixed wavelet statistic reaches the learned ceiling, with no training** \| | \| 4.6 \| **With joint reading of the bins, the ℓ1-norm matches the optimal CNN** \| |
| \| C.1 \| **The four questions, answered** \| | \| C.1 \| **Answers to the four questions** (one line per question, one per answer) \| |
| (*Wavelet peak counts and the ℓ1-norm are 1-pt statistics on the same starlet transform*) | (*Wavelet peak counts and the ℓ1-norm are one-point statistics of the starlet coefficients*) |
| *We measure the shear, we want the convergence* · *a convergence map carries geometry and growth* · *one potential, two observables, and the relation is exact* | *We measure the shear, but theory predicts the convergence* · *the convergence is a projection of the matter density, sensitive to geometry and growth* · *shear and convergence are both second derivatives of the lensing  |
| the signal is the **statistical memory** of everything the Universe has done since the Big Bang, and getting it out is an **algorithms** problem | the signal encodes the growth of structure and the geometry of the Universe, and extracting it is an **algorithms** problem |
| *(the claim: every stage is a learned component, and each can bias the answer or throw information away with no internal check noticing)* | *(the claim: each step now involves learned components, and each can bias the result or discard information with no internal check that would detect it)* |
| **Q1 · the maps · Part 1** — is mass mapping preprocessing, or does the choice of reconstruction change the cosmology we infer? | **Q1 · the maps · Part 1** — does the choice of mass-mapping method matter for the final constraints? |
| **Q2 · the maps · Part 2** — can one reconstruction be flexible, fast, accurate and honest about its own uncertainty, on a survey the size of Euclid? | **Q2 · the maps · Part 2** — can one method be accurate, flexible and fast, with reliable uncertainties, at the scale of Euclid? |
| **Q3 · the summaries · Part 3** — what is the most we can read out of a map, and what does it take to turn that reading into a posterior? | **Q3 · the summaries · Part 3** — how much cosmological information can a summary statistic extract from the maps, and how do we turn it into a posterior? |
| **Q4 · the summaries · Part 4** — does any of that survive the real Universe, the astrophysics we cannot model? | **Q4 · the summaries · Part 4** — do these results hold up against astrophysical systematics we cannot model, such as baryonic feedback? |
| Q3 and Q4 are asked in plain terms (*the most we can read out of a map*, *the real Universe*) | Q3 and Q4 are asked in plain terms (*how much information a summary statistic can extract*, *astrophysical systematics we cannot model*) |
| 1. **The reconstruction is not preprocessing.** It is a scientific choice | 1. **The choice of reconstruction matters.** It is a scientific choice |
| That number is a floor, not a forecast. | That number is a conservative estimate, not a forecast. |
| \| The cut is a floor, not a forecast \| A3.5 \| | \| The cut is a conservative estimate, not a forecast \| A3.5 \| |

## SPEAKER_SCRIPT.md

| before | after |
|---|---|
| \| 17 \| **106** \| *So write the assumption down* — the Bayes slide \| | \| 17 \| **106** \| *Every mass-mapping method is a Bayesian inference with a different prior on κ* — the Bayes slide \| |
| \| 29 \| **113** \| *Error bars from one extra forward pass* — the UQ chain \| | \| 29 \| **113** \| *Pixel-wise uncertainties from a second network, calibrated with conformal prediction* — the UQ chain \| |
| ## A1.4 — one potential, two observables · frame 13 · 0:27 | ## A1.4 — shear and convergence from the same potential · frame 13 · 0:27 |
| ## A1.8 — so write the assumption down · frame 105 · SKIP · 1:03 | ## A1.8 — mass mapping as Bayesian inference · frame 105 · SKIP · 1:03 |
| ## A3.2 — same chain, one step to the right · frame 29 · 0:20 | ## A3.2 — from the map to a summary statistic · frame 29 · 0:20 |
| ## A3.12 — and then it has to become a posterior · frame 36 · 0:28 | ## A3.12 — no analytic likelihood, so simulations · frame 36 · 0:28 |
| ## A3.13 — the classical route · frame 37 · 0:50 | ## A3.13 — classical inference with an explicit likelihood · frame 37 · 0:50 |
| The classical route is the same rule as in Part 1, with the parameters as the unknown instead of a map. | Classical inference is the same rule as in Part 1, with the parameters as the unknown instead of a map. |
| ## A3.19 — a fair comparison · frame 43 · 0:20 | ## A3.19 — same maps, same flow, both calibrated · frame 43 · 0:20 |
| \| 37 \| the classical route \| **−0:52** \| | \| 37 \| classical inference with an explicit likelihood \| **−0:52** \| |
| **▲** So the wavelet cut is not better. It is coarser, and therefore conservative. Everything on the next slide is a floor. | **▲** So the wavelet cut is not better. It is coarser, and therefore conservative. Everything on the next slide is a conservative estimate. |
| **▲** Two things to leave you with. The signal survives on *quasi-linear* scales — these are not only deep-non-linear probes. And it is a floor: our cut is not optimised, and a finer filter bank would recover more. | **▲** Two things to leave you with. The non-Gaussian signal survives on *quasi-linear* scales. And this is conservative: our cut is not optimised, and a finer filter bank would recover more. |
| the contamination could be removed where it sits rather than by removing a band. Future work, and everything in Part 4 is a floor because of it. | the contamination could be removed where it sits rather than by removing a band. Future work, and everything in Part 4 is conservative because of it. |
