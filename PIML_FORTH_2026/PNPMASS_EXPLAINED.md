# PnPMass and PnPMass3D, explained

A plain account of the two methods you talk about in frames 10 to 19, for you, not for the room.
It follows the published paper (Leterme, Tersenov, Fadili & Starck 2026, A&A 710, A292; you
co-developed the method and the uncertainty quantification) and the September 2026 draft of the
tomographic paper (Leterme, Tersenov & Starck, in preparation). Every number is in `PAPER_FACTS.md`.
Notation is the deck's: the operator is **P**, the mask **M**, the noise covariance **Σ**.

---

## 1. The problem in one line

$$\gamma = M P \kappa + n$$

- $\kappa$ is the convergence map, real, $N \times N$ pixels, flattened to a vector.
- $P$ is the Kaiser–Squires operator: in Fourier space, $\hat\gamma_1 = \hat P_1 \hat\kappa$ and
  $\hat\gamma_2 = \hat P_2 \hat\kappa$ with $\hat P_1 = (k_1^2 - k_2^2)/k^2$ and
  $\hat P_2 = 2 k_1 k_2 / k^2$. The two kernels have $|\hat P_1|^2 + |\hat P_2|^2 = 1$, so $P$ has
  unit norm and $P^\top P = I$ up to the $k = 0$ mode.
- $M$ is a binary mask: a pixel with no galaxy in it, or outside the footprint, is zero.
- $n$ is shape noise, Gaussian, independent per pixel, with variance
  $\sigma_\epsilon^2 / N_{\rm gal}(k)$ in pixel $k$: fewer galaxies, more noise. $\Sigma$ is that
  diagonal matrix. In the paper $\sigma_\epsilon = 0.39$ and there are about 32 galaxies per
  arcmin², which is Euclid-like.

Why it is ill-posed, in three items you already say on frame 7. The noise is larger than the
signal and the inverse amplifies it at small scales. The mask removes data and $P$ is non-local,
so a hole leaves whole Fourier modes unconstrained. And $P$ kills a constant: adding a constant
to $\kappa$ does not change $\gamma$ (the mass-sheet degeneracy), so every method looks for a
**zero-mean** map.

The paper works with real vectors: it stacks the real and imaginary parts of $\gamma$, which
doubles the length of the data vector and turns $P$ into a real $2N^2 \times N^2$ matrix. Nothing
conceptual changes, so I keep the short notation here.

---

## 2. The classical way, and the iteration everything is built on

Every regularised method solves

$$\hat\kappa = \arg\min_\kappa \; \tfrac12 \| \gamma - M P \kappa \|^2_{\Sigma^{-1}} + g(\kappa),$$

a data term plus a regulariser $g$ that encodes the prior. The standard solver for this shape of
problem is **forward–backward splitting** (FBS, Combettes & Wajs 2005). Each iteration has two
steps:

1. **forward**, a gradient step on the data term:
   $\kappa_0 = \kappa^{(i)} + \tau\, P^\top M^\top \Sigma^{-1} (\gamma - M P \kappa^{(i)})$;
2. **backward**, the proximal operator of the regulariser:
   $\kappa^{(i+1)} = \mathrm{prox}_{\tau g}(\kappa_0) = \arg\min_x \tfrac12\|x - \kappa_0\|^2 + \tau g(x)$.

The prox is a denoiser in disguise: it takes a noisy map and returns the nearest map the prior
likes. For an ℓ1 penalty in a wavelet basis the prox is soft-thresholding, and FBS is ISTA. For a
Gaussian prior it is a Wiener step, and FBS is the iterative Wiener filter. MCALens alternates
both. This is the sentence on frame 9: the data term is the same for everyone, and the methods
differ by the second term.

---

## 3. The plug-and-play idea

Keep the loop, replace the prox by a **learned denoiser** $F_\Theta$:

$$\kappa_0 = \kappa^{(i)} + \tau\, B\, (\gamma - M P \kappa^{(i)}), \qquad \kappa^{(i+1)} = F_\Theta(\kappa_0, \tau).$$

Two things change in how you should think about it.

**It is no longer an optimisation.** A network is not the prox of any function in general, so the
loop does not minimise anything. It is a **fixed-point iteration**: you apply the same map
$T = F_\Theta \circ (\text{forward step})$ again and again, and you want it to settle. The paper is
explicit that $\hat\kappa$ is not a MAP estimate. It is "the map the loop converges to".

**Convergence is a contraction argument** (Banach). The loop converges to a unique zero-mean fixed
point if

- the denoiser is non-expansive (Lipschitz constant $\le 1$),
- the denoiser outputs zero-mean maps (a mean-centring layer at its output does this),
- $B M P$ is positive semidefinite,
- the step size satisfies $0 < \tau < 2 / \|B M P\|$.

Non-expansiveness is the one condition that is not enforced. It could be, by regularising the
spectral norm of the Jacobian during training (Pesquet et al. 2021), but that is expensive. The
paper assumes it and checks convergence empirically. In practice **eight iterations** suffice.
That is Q&A 2.

---

## 4. The trick that makes it flexible: the choice of B

This is the centre of the method, and it is what "the physics enters only in the data step" means.

The paper takes

$$B = P^\top M^\top \Sigma^{-1/2},$$

a **noise-whitening** operator. (The slide writes $B = P^\top \Sigma^{-1}$ for brevity. The
$-1/2$ is the point, and it is also why the data term is not the Gaussian log-likelihood: that
would have $\Sigma^{-1}$.)

Now look at what the denoiser sees at the fixed point. If the reconstruction is close to the truth,
$\hat\kappa \approx \kappa$, then the forward step applied to $\hat\kappa$ gives

$$\kappa_0 \approx \kappa + \tau\, B\, n .$$

With this $B$, the noise term $\tau B n$ has covariance $\tau^2\, P^\top M^\top M P$, and because
$P^\top P \approx I$ that is approximately $\tau^2 I$ away from the mask. **So the denoiser only ever
has to remove white Gaussian noise of standard deviation $\tau$.** It never needs to know $\Sigma$ or
$M$; both have been absorbed into the forward step. The survey's noise level and footprint enter
at inference, in the data step, and the denoiser is the same network for every survey.

Two consequences follow:

- **What the denoiser is trained on.** Simulated maps plus white Gaussian noise, and nothing else.
  No shear, no mask, no covariance in the training set.
- **What the step size is.** The upper bound $2 / \|B M P\|$ works out to roughly
  $2 \min_k \sigma_k$, twice the noise level of the *least* noisy pixel. In the paper the admissible
  interval is $(0, 0.176)$. Since $\tau$ is also the noise level the denoiser has to handle, and you
  want to choose $\tau$ per survey without retraining, the denoiser is trained over a **range** of
  noise levels, $\sigma \sim U(0, 0.2)$, with the noise level given to it as an extra input channel.

---

## 5. The denoiser

- **SUNet**, a Swin-transformer denoiser, 7.2 M parameters, made noise-level-aware by an extra
  input channel (the DRUNet trick), with a mean-centring layer at the output.
- Trained on **κTNG** (Osato et al. 2021): hydrodynamic mock convergence maps, 5°×5°, 0.29′ per
  pixel, sources to $z = 2.6$, **one cosmology** ($\Omega_m = 0.3089$, $\sigma_8 = 0.8159$,
  $H_0 = 67.74$). 70 560 training crops, 1 440 validation, 1 024 calibration, 512 test.
- MSE loss. A denoiser trained with an MSE loss on (noisy, clean) pairs approximates the
  **posterior mean** of the clean map given the noisy one. That is what the uncertainty part below
  builds on.

The honest caveat you say on frame 15: a single cosmology in training. Robustness across
cosmologies is the first open direction in the paper.

---

## 6. The residual variant (frame 12)

Write the map as a Gaussian part plus a non-Gaussian part, $\kappa = \kappa_g + \kappa_{ng}$. The
Gaussian part has a closed-form optimal estimator, the Wiener filter, so let it do that part:

1. $\kappa_g = \text{Wiener}(\gamma)$;
2. subtract its prediction from the data: $\gamma_{ng} = \gamma - M P \kappa_g$;
3. run PnPMass on $\gamma_{ng}$, with a denoiser trained on **non-Gaussian residuals**
   ($\kappa - \kappa_g$ of the simulations plus white noise);
4. $\hat\kappa = \kappa_g + \hat\kappa_{ng}$.

The residual is sparser and closer to what the denoiser was trained on, so the loop is better
behaved: within **0.5 %** of DeepMass (RMSE ratio 1.006, against 1.013 for the plain variant), and
converged after two iterations at $\tau = 0.176$. The 6.0 to 6.9 × 10⁻³ improvement over plain
PnPMass is significant at 95 % on paired comparisons.

---

## 7. The error bars, part one: a second network

The map is the posterior mean, so the natural error bar is the posterior variance. **Moment
networks** (Jeffrey et al. 2020) estimate it with a second network trained on the same inputs:

- target: the squared residual of the first network, $\left(\kappa - F_\Theta(\kappa_0)\right)^2$,
  pixel by pixel;
- a network trained with an MSE loss on that target approximates
  $\mathrm{Var}[\kappa \mid \kappa_0]$, the posterior variance.

In the PnP loop this costs **one extra iteration**: once the fixed point $\hat\kappa$ is reached,
run the forward step once more and apply the variance network instead of the denoiser. Same
architecture, same white-noise training, final layer a ReLU instead of mean-centring so the
output is non-negative. Output: a variance map $\hat\sigma^2$.

Error bars from it, assuming Gaussian marginals: $\hat\kappa \pm z\,\hat\sigma$ with $z = 2$, i.e.
a target miss rate of $\alpha \approx 4.55\,\%$ ("2σ confidence"). This is a **heuristic**: it
rests on the denoiser being the exact posterior mean, on the fixed point being close to the truth
(which fails near the mask), and on the Gaussian assumption. So the miss rate is not guaranteed.
That is frame 13's last line.

---

## 8. The error bars, part two: conformal calibration (frame 14)

**Conformalised quantile regression** (CQR, Romano et al. 2019) fixes the bars after the fact,
with a guarantee that does not depend on any of the assumptions above.

- Take a **calibration set** of $n = 1\,024$ maps with known truth, disjoint from training.
- For each map and each pixel, compute the **conformity score**
  $s = \max(\text{low} - \kappa,\; \kappa - \text{high})$: how far outside the interval the truth
  fell, negative if inside.
- Per pixel, take the $(1-\alpha)(1 + 1/n)$ empirical quantile of the scores, $q$.
- Widen: $[\text{low} - q,\; \text{high} + q]$.

The guarantee, for exchangeable (e.g. i.i.d.) calibration and test data, at each pixel:

$$\alpha - \frac{1}{n+1} \;\le\; \Pr\{\kappa \notin [\text{low}', \text{high}']\} \;\le\; \alpha .$$

Three words you use on frame 14 and what they mean here:

- **distribution-free**: no assumption on the data distribution or on the network being right;
- **finite-sample**: the bound holds at $n = 1\,024$, not only asymptotically; with 1 024 maps the
  miss rate lands in $[4.45\,\%, 4.55\,\%]$;
- **marginal**: the probability is averaged over pixels, over inputs and over calibration sets.
  Some inputs miss more than others, and the misses concentrate at the **peaks**. That is the
  limit you concede on frame 15 and in Q&A 4; conditional conformal methods are the named fix.

The lower bound matters as much as the upper: CQR is not over-conservative, which is why it was
chosen over risk-controlling prediction sets. Every method in the comparison is calibrated the
same way, so after calibration they all miss at the same rate, and the only question left is who
gets there with the tightest bars.

---

## 9. What the results say (frame 15)

RMSE on the 512 κTNG test maps, as ratios to DeepMass (a U-Net trained end to end for this exact
mask and noise level):

| method | RMSE ratio |
|---|---|
| Wiener | 1.039 |
| MCALens | 1.025 |
| DeepMass (retrained for this mask and noise) | 1.000 |
| **PnPMass** | **1.013** |
| **PnPMass, residual variant** | **1.006** |

Two things to say, in this order:

1. **Accuracy**: within about 1 % of DeepMass, half a per cent for the residual variant, with
   no retraining.
2. **Uncertainty**: after calibration, PnPMass has the **smallest error bars** of every method,
   DeepMass included, on all 512 test maps. The paper's reading: DeepMass finds more peaks (better
   RMSE) but also hallucinates more, so it needs wider bars to cover.

The timing argument, if it comes up: PnPMass is *slower per map* than DeepMass (about 50 s against
7 s). The claim is not speed. It is that DeepMass must repeat its two days of training whenever
the mask or the noise changes, and PnPMass does not. Say "trained once", never "fast".

---

## 10. PnPMass3D: the tomographic version (frames 16 to 19)

### 10.1 What tomography adds

Slice the source galaxies into redshift bins. The convergence of bin $j$ is a line-of-sight
integral of the matter density with a **lens efficiency** $q_j(\chi)$ that is non-zero for all
matter *in front* of the bin:

$$\kappa_j \propto \int_0^{\chi_j} \frac{q_j(\chi)}{a(\chi)}\, \delta(\chi)\, d\chi .$$

The kernels are nested: the matter that lenses bin 2 also lenses bins 3, 4, 5, 6. So the six maps
are strongly correlated, and a structure at low redshift shows up in every channel. The draft uses
six bins with edges $z = 0, 0.57, 0.80, 1.05, 1.36, 1.79, 2.60$ (Euclid's bins, merged in pairs).

Each bin now has its own mask $M_j$ and noise $\Sigma_j$, and both are much worse than in the
single-map problem: a sixth of the galaxies per bin, so at 0.29′ pixels most pixels of a given bin
are empty. The draft's motivation is that ordinary 2D methods applied bin by bin fail here,
especially after the nulling.

### 10.2 Nulling (the BNT transform, frame 17)

Nulling re-mixes the bins so that each new map sees only the matter near its own distance. It is
a fixed linear combination of three consecutive bins,

$$\kappa_j^{\rm BNT} = w_j^{(1)} \kappa_{j-2} + w_j^{(2)} \kappa_{j-1} + \kappa_j ,$$

with weights chosen so that the combined lens efficiency vanishes both beyond bin $j$ (automatic)
and in front of bin $j-2$ (two conditions, two unknowns: the weights sum to zero, and their ratios
to the bins' harmonic-mean distances sum to zero). The first two rows are $\kappa_1$ and
$\kappa_2 - \kappa_1$. Put together it is a **lower-triangular, invertible** $6 \times 6$ matrix
whose entries depend only on the geometry (distances), not on the data. This is the version of
Barthelemy et al. 2022 for binned sources; the original is Bernardeau, Nishimichi & Taruya 2014.

Why one wants it: with nested kernels, one angular scale in one bin mixes small physical scales
nearby with large physical scales far away. After nulling, a scale cut in a nulled bin is a cut at
a known distance. The price: the nulled maps are **differences of noisy maps**. The noise of three
bins adds up, and an error in the reconstruction of one bin leaks into the next. That is why it is
the test the reconstruction has to pass.

### 10.3 The joint problem (frame 18)

Stack the six problems into one:

$$\gamma = M P \kappa + n, \qquad \kappa = \begin{pmatrix}\kappa_1\\ \vdots\\ \kappa_6\end{pmatrix},\;
P = \mathrm{diag}(P_0, \dots, P_0),\; M = \mathrm{diag}(M_1, \dots, M_6),\; \Sigma = \mathrm{diag}(\Sigma_1, \dots, \Sigma_6).$$

Then run **exactly the same loop** as in 2D, with the same $B = P^\top M^\top \Sigma^{-1/2}$. The
data step is block-diagonal, so each channel still has its own mask and noise. The one change is
the denoiser: **one SUNet with six input and six output channels** (7.3 M parameters), trained on
six-channel simulated maps plus white noise, with a per-channel mean-centring layer. So the
cross-bin correlation lives entirely in the prior, which is the only place it could live.

The baseline (the "per channel" curves on frame 19) is the naive alternative: six independent 2D
PnPMass runs, six denoisers, each with its own step size.

### 10.4 What the theory adds

The draft proves two things, both adapted to the many-empty-pixels situation.

**Convergence** (Proposition 1). The conditions of Section 3 are restated on the subspace of
zero-mean maps (which the mean-centring layer enforces), and the loop converges **linearly** to a
unique fixed point with rate $L_\tau\, \rho_\tau$, where $L_\tau \le 1$ is the denoiser's Lipschitz
constant and

$$\rho_\tau = \begin{cases} \tau \lambda_{\max} - 1 & \text{if } \tau \ge 2/(\lambda_{\min} + \lambda_{\max}) \\ 1 - \tau \lambda_{\min} & \text{otherwise,}\end{cases}$$

with $\lambda_{\min}, \lambda_{\max}$ the eigenvalues of $B M P$ on that subspace.

**Accuracy** (Proposition 2). The PnP error is bounded by the denoiser's own error on white noise
of level $\tau$:

$$\mathbb{E}\|\hat\kappa - \kappa\|^2 \;\le\; \frac{1}{(1 - L_\tau \rho_\tau)^2}\; \mathbb{E}\|F_\Theta(\kappa + \tau B n, \tau) - \kappa\|^2 .$$

Read it as: *the loop cannot do better than its denoiser, and it does worse by a factor set by how
fast it converges*. This is what you say on frame 18 as "an error bound that ties the loop's error
to the denoiser's error". It also settles the step size. The denoiser's error grows with $\tau$
(more noise to remove), while the prefactor blows up as $\tau \to 0$ (slow convergence). With a
mask, $\lambda_{\min} = 0$, and the safe choice is the largest step for which the forward step is
still non-expansive,

$$\tau = 2/\lambda_{\max} = 2/7.66 = 0.261 ,$$

which is what had been chosen empirically in 2D. Hence "as a by-product, justifies the step size
we had been choosing by hand".

The step is larger than in 2D and $\lambda_{\min} = 0$, so the contraction rate is closer to one
and the loop needs **24 iterations** instead of eight. The draft reads this as the price of the
lower signal-to-noise per channel. That is Q&A 10.

Training this time: white noise with $\sigma \sim U(0, 0.3)$, MSE loss, 50 epochs, 70 560 crops of
384×384, the κTNG cosmology.

### 10.5 What the results say (frame 19)

NRMSE over the test set, normalised so that predicting zero scores exactly 1 (so "worse than the
zero map" is a literal reading of 1.48):

| | before nulling, joint | before, per channel | after nulling, joint | after, per channel |
|---|---|---|---|---|
| denoising alone, $\sigma = 0.2$ | 0.729 | 0.818 | 0.862 | 2.297 |
| **PnP, 24 iterations** | **0.891** | 0.953 | **0.944** | 1.479 |

Per channel, before nulling, the joint loop is better in every bin (0.86 to 0.91 against 0.94 to
1.00). After nulling, the per-channel loop crosses 1 from the third bin on and leaves the axis; the
joint loop rises gently from 0.90 to 1.00 and never crosses. The honest reading you give on frame
19: the far nulled channels are recovered, but barely.

Why the per-channel loop fails after nulling: the nulled bin $j$ is a combination of three
reconstructed bins, so any bin-by-bin error that is not consistent across bins survives the
subtraction and appears as invented structure. The joint denoiser makes the six reconstructions
consistent with each other, so the subtraction cancels what it should.

### 10.6 Draft caveats, in case they come up

- It is a **draft**. The test set is 32 crops, with a to-do to make it 512. The introduction
  quotes a 20 % gain that the table does not show; the table is the authority and the 20 % is not
  said.
- **No uncertainty quantification** in the 3D paper yet. The moment network and CQR carry over in
  principle (the loop is the same), but it has not been done. Say so if asked.
- Still a **single cosmology**, still κTNG, still simulated noise and mask from the COSMOS
  catalogue. A run on real COSMOS data is on the to-do list.
- No comparison against MCALens or Kaiser–Squires in the tomographic setting yet; the only
  baseline is per-bin PnPMass.

---

## 11. The four sentences that hold it together

If you lose the thread, these are the four claims, in order:

1. **The physics stays in the data step.** Operator, mask and noise covariance enter only through
   $B$ and the forward step, at inference.
2. **The denoiser only ever removes white noise of level τ.** That is what the choice
   $B = P^\top M^\top \Sigma^{-1/2}$ buys, and it is why one network serves every configuration.
3. **The error bar is a second network, then calibrated.** The variance network gives a heuristic
   bar; conformal calibration makes its miss rate exactly α, for any network, on n held-out maps.
4. **In tomography, the correlation lives in the prior.** Same loop, block-diagonal data step, one
   six-channel denoiser. Nulling is the test, because it turns inconsistent errors into invented
   structure.

---

## 12. Numbers at a glance

| | PnPMass (2D) | PnPMass3D (draft) |
|---|---|---|
| denoiser | SUNet, 7.2 M, noise-aware | SUNet 6 in / 6 out, 7.3 M, noise-aware |
| training noise | white, $\sigma \sim U(0, 0.2)$ | white, $\sigma \sim U(0, 0.3)$ |
| step size | in $(0, 0.176)$ | $0.261 = 2/\lambda_{\max}$, $\lambda_{\max} = 7.66$ |
| iterations | 8 (residual variant: 2) | 24 |
| accuracy | RMSE ratio to DeepMass 1.013; residual 1.006 | NRMSE joint 0.891 / per channel 0.953; after nulling 0.944 / 1.479 |
| error bars | moment network + CQR, α ≈ 4.55 %, 1 024 calibration maps; smallest calibrated bars on all 512 test maps | none yet |
| data | κTNG, 5°×5°, 0.29′/px, one cosmology; COSMOS bright catalogue for mask and noise | same, six bins, edges 0, 0.57, 0.80, 1.05, 1.36, 1.79, 2.60 |
| code | DeepInverse + PyTorch, `github.com/hubert-leterme/weaklensing_uq` | DeepInverse + PyTorch |
