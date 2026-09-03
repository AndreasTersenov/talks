# PAPER_FACTS — the number ledger for the defense deck

**Rule: no number goes on a slide unless it appears in this file with a source line.**
Where a number is *derived* here rather than quoted from a paper, it is marked **[derived]** and
the arithmetic is shown. Derived numbers are held to the same rule: ledger first, slide second.

Written 2026-08-25 from the thesis, which is the authority — the papers are reproduced inside it,
so a claim that disagrees with `~/Desktop/PhD_thesis/` is wrong regardless of which draft it came
from. `../cosmo26/PAPER_FACTS.md` covers Ch4 and Ch5 only and is superseded by this file; one of
its stated justifications is corrected in §8.1.

| thesis ch. | paper | status | source read |
|---|---|---|---|
| **Ch2** | Tersenov, Baumont, Starck, Kilbinger — *Impact of weak-lensing mass-mapping algorithms on cosmology inference* | **Published**, A&A 698, A25 (2025) | `papers/paper1_mass_mapping/paper1_body.tex`; also `~/Desktop/AA53707-25/` |
| **Ch3** | Leterme, **Tersenov**, Fadili, Starck — *A plug-and-play approach with fast UQ for weak lensing mass mapping* | **Published**, A&A 710, A292 (2026) | `papers/paper3_pnpmass/thesis_version/paper3_body_thesis.tex` (condensed 2nd-author version) |
| **Ch4** | Tersenov, Guerrini, Starck, Kilbinger — *Mitigating baryonic effects in weak lensing with HOS* | **Submitted** to A&A (`aa60075-26`, resubmitted 2026-08-10) | `papers/paper2_baryonic_feedback/paper2_body.tex`; also `~/Desktop/Impact_of_Baryonic_Feedback_Resubmission/submission_2026-08-10/` |
| **Ch5** | Tersenov, Starck, Kilbinger — *The joint wavelet ℓ1-norm matches neural compression* | **Submitted** to A&A | `papers/paper4_l1_vs_cnn/sections/*.tex`; also `~/Desktop/joint_l1_paper_overleaf/` |

Ch3 authorship line for the talk: **led by H. Leterme; A.T. co-developed the method and the
uncertainty quantification.**

---

## 0. The ratio policy

`STRUCTURE.md` §7: **no absolute figure of merit reaches a slide.** Absolutes are recorded here
for the examination and the speaker notes. Slides carry ratios against a baseline drawn as a line
at 1.0.

**But the ratios are not all the same quantity.** This is the trap §7's "one visual grammar"
framing could hide, and it is the sharpest question in the deck:

| chapter | FoM | scales as | a ratio of 2.0 means |
|---|---|---|---|
| **Ch2** | (det F̃)^(1/n), n = 4 | (det **C**)^(−1/4) | a **per-dimension** factor, like a σ ratio |
| **Ch4, Ch5** | FoM₃ = 1/√det **C** | (det **C**)^(−1/2) | an **inverse-volume** factor on the 1σ ellipsoid |

Ch2's exponent is a fourth root over four parameters; Ch4/Ch5's is a square root over three. So
Ch2's **×2.57 is a linear-scale improvement**, and expressed the way Ch4 and Ch5 express theirs it
would be ×2.57⁴ ≈ **43.6 in inverse posterior volume** **[derived]**. That is a startling number
and it is *not* the published claim — do not put it on a slide, do not lead with it.

**What this means in practice.** Keep the paper's own number and say what it is:

> *"a 157 per cent improvement in the four-parameter figure of merit"* — Ch2, verbatim in substance
> *"a factor 1.8 in the figure of merit"* — Ch4

Each act names its quantity once, out loud. The visual grammar (baseline at 1.0) survives intact;
what does not survive is a sentence that reads ×2.6 and ×1.8 as the same kind of thing. Prepared
answer for *"×2.6 in what?"* is in §8.2.

---

## 1. The three setups — never chained

| | **Ch2** | **Ch4** | **Ch5** |
|---|---|---|---|
| simulations | cosmo-SLICS (Harnois-Déraps+2021) | cosmoGRID V1 | cosmoGRID V1 |
| geometry | DES-Y1 footprint, **19 tiles × 100 deg²**, 1′ px, 600×600 | full-sky HEALPix `Nside=512`, masked polar caps | **10°×10°** gnomonic patches, 80×80 px (7.5′/px) |
| areas | one (DES-Y1-like) | 2 000 / 5 000 / 10 000 / 14 000 / 28 000 / 35 000 deg² + full sky | one |
| parameters | Ωm, σ8, **h**, w0 | Ωm, σ8, w0 | Ωm, σ8, w0 |
| inference | GP emulator + MCMC | NPE, **MAF** | NPE, **RealNVP** |
| statistic | peak counts, wavelet peak counts | PS, starlet peaks, starlet ℓ1 | ℓ1 variants vs CNN |
| covariance | SLICS, 124 sims × 10 noise realisations | — (SBI) | — (SBI) |

**Ch3 is not in this table** because it reports no figure of merit at all — it is scored on
reconstruction RMSE and error-bar size, which are a different axis again.

The one spoken sentence that covers it: *"these are three different simulation suites and three
different survey geometries, so read the relative values, not the absolute ones."*

---

## 2. Ch2 — mass mapping propagates to the cosmology

### Setup facts

- Three methods: **Kaiser–Squires**, **inpainting KS** (DCT inpainting of the mask),
  **MCALens** (Starck+2021; sparse + Gaussian two-component model).
- **25 cosmologies** in cosmo-SLICS; peaks binned into **20 linear bins over −2 < S/N < 6**.
- Wavelet peak counts: starlet, **five scales [2′, 4′, 8′, 16′, 32′] plus the coarse map**.
- Shear pre-smoothing σ = **0.4′**; optimal post-filter kernel **2′ for KS/iKS, 1′ for MCALens**
  (chosen to maximise constraining power, *not* to minimise RMSE — see below).
- Mock data vector = the **GP emulator's prediction at the fiducial cosmology**, so contours are
  centred by construction and only constraining power is compared. Cross-checked against a
  simulation-derived data vector in the appendix.

### The headline — 4-parameter FoM, wavelet peak counts

| method | FoM (Ωm, h, w0, σ8) | **ratio to KS [derived]** |
|---|---|---|
| KS | 758 | 1.00 |
| iKS | 755 | **0.996** — indistinguishable |
| MCALens | 1947 | **2.57**, i.e. the paper's **+157 %** |

Mono-scale peak counts, same parameters: KS 492, iKS 444, MCALens 578 → MCALens **×1.17**
(the paper's **+17 %**) **[derived from Table `sspc_fom_tab`]**.

MCALens + wavelet peaks against KS + mono-scale peaks: 1947/492 = **×3.96**, the paper's **+296 %**.

### The single most useful fact in this chapter

**Map quality and constraining power are not the same objective, and the gap is enormous.**

| | RMSE (×10⁻⁵, mean over 25 cosmologies) | **ratio to KS [derived]** |
|---|---|---|
| KS (γ smoothed) | 1018 ± 2 | 1.00 |
| iKS (γ smoothed) | 1023 ± 2 | 1.005 |
| MCALens (γ smoothed) | 976 ± 2 | **0.959** |

MCALens reconstructs the field **4 % better in RMSE** and yields a **157 % better figure of
merit**. That contrast is the chapter's thesis in one line and it belongs on S11 or S12.

**Caveat that must be spoken with it.** The two comparisons optimise different things: the RMSE
table smooths each map with the kernel that *minimises its own RMSE*, while the FoM analysis uses
the kernel that *maximises its own constraining power* (2′ vs 1′). They are therefore not the
same maps. This does not weaken the point — it is the point: optimising for map quality and
optimising for the posterior are different problems.

### The mechanism (S12)

Incremental scale inclusion, starting from [16′, 32′, coarse] and adding 8′, then 4′, then 2′:

- **KS** improves significantly on adding 8′; **4′ and 2′ add nothing significant.**
- **MCALens** improves significantly at **every** added scale, down to 2′.

Source: §Wavelet peak counts, Figs. `ms_pc_constraints_ks_scales` / `..._mca_scales`. This is the
evidence that the gain is small-scale reconstruction fidelity, not a global normalisation effect.

### Honesty items

- **iKS ≈ KS is a null result and should be reported as one**, not skipped. The paper's reasons:
  inpainting affects the masked regions, which are excluded from the peak counts anyway; and the
  Gaussian-smoothing optimum may not have been fully reached. It explicitly says the conclusion
  **would not generalise to a Fourier-space statistic such as the bispectrum**, which uses the
  full area including masked regions.
- **MCALens does not win every pair.** In the mono-scale analysis it is *worse* than KS for
  (Ωm, h) — 450 vs 476 — and for (h, σ8) — 293 vs 336 **[derived from Table `sspc_fom_tab`]**.
  The multi-scale analysis is where it wins across the board.
- MCALens produces a **narrower peak histogram with a higher mode**, because its denoising
  suppresses both noise and part of the signal while the S/N map is normalised by the *input
  shear* noise. Not a bug; worth knowing before someone asks why the histograms differ.

---

## 3. Ch3 — PnPMass

No figure of merit. Scored on **reconstruction accuracy** and **calibrated error-bar size**.

### Setup facts

- Data: **κTNG** (Osato+2021) hydrodynamic mock convergence maps, **5°×5°**, **0.29′/px**,
  sources to z = 2.6, a **single** cosmology (Ωm = 0.3089, σ8 = 0.8159, H0 = 67.74).
- Noise covariance from the **S10 COSMOS shear catalogue** (Schrabback+2010), σ_ε = **0.39**,
  ≈ **32 galaxies arcmin⁻²** — Euclid-like by design.
- Training 70 560 images / validation 1 440 / **calibration 1 024** / **test 512**.
- Denoiser: **SUNet** (Swin-Transformer), **7.2 M parameters**, noise-level-aware via an extra
  input channel; trained on white Gaussian noise with σ ~ U(0, 0.2); 100 epochs, Adam.
- PnPMass run for **8 iterations**; step-size admissible interval (0, 0.176).
- Target error rate **α ≈ 4.55 %** ("2σ confidence"). With 1 024 calibration examples the
  post-calibration miscoverage is bounded in **[4.45 %, 4.55 %]**.
- Implementation: **DeepInverse** + PyTorch. Code: `github.com/hubert-leterme/weaklensing_uq`.

### Reconstruction accuracy (normalised RMSE, ×10⁻¹, κTNG test set)

| method | RMSE | **ratio to DeepMass [derived]** |
|---|---|---|
| Wiener | 8.86 ± 0.34 | 1.039 |
| MCALens | 8.74 ± 0.44 | 1.025 |
| **DeepMass** (retrained for this mask + noise) | **8.53 ± 0.48** | **1.00** |
| PnPMass | 8.64 ± 0.50 | **1.013** |
| PnPMass (non-Gaussian residuals) | 8.58 ± 0.49 | **1.006** |

**The ± is the standard deviation across the 512 test images, not the error on the mean.** It is
therefore *not* an error bar on the difference between methods, and quoting it as one would
understate the results. The paper's significance claims come from paired/bootstrap comparisons:
the residual variant beats standard PnPMass by **6.04–6.88 × 10⁻³ at 95 % confidence**, and
PnPMass's error bars are smaller than DeepMass's **on all 512 test images**.

Slide-safe statement: **PnPMass is within about 1 % of a network fine-tuned to the specific
observation, and the residual variant within about 0.5 %** — while needing no retraining.

### The claim that actually matters

**PnPMass produces the smallest calibrated error bars of every method tested**, including
DeepMass, despite being slightly less accurate. Observed on all 512 test images. The paper's
conjecture: DeepMass detects more peaks (better RMSE) but also hallucinates more (worse
confidence), so accuracy and error-bar size trade against each other.

After calibration **all** methods hit the same miscoverage rate — that is what CQR guarantees.
The comparison is therefore purely about **which method achieves it with the tightest bars**,
which is the correct axis and worth saying explicitly.

### Timing (κTNG)

| | training (order 1) | training (order 2) | calibration | inference |
|---|---|---|---|---|
| DeepMass | 7 h 27 | 46 h 33 | 18 s | 7 s |
| PnPMass | 31 h 41 | 47 h 20 | 1 min 42 | 50 s |

PnPMass inference is **slower per map** than DeepMass. The argument is not speed-per-map, it is
that **training happens once**: DeepMass must repeat its ~54 h whenever the noise or footprint
changes, and PnPMass does not. Say it that way — "fast at inference" alone invites the table.

### Honesty items

- **Single cosmology.** κTNG is one parameter set. Robustness across cosmologies is named in the
  paper as the first open direction.
- **Marginal, not conditional, coverage.** The guarantee holds on average over pixels; miscoverage
  concentrates at the **peaks** of the convergence field, which is exactly where Ch2 says the
  cosmological information is. Conditional conformal prediction (Gibbs+2025) is the named fix.
- The COSMOS reconstruction (vs MMGAN, DeepMass) is a **qualitative** figure. No metric attached.

---

## 4. Ch4 — baryons

### Setup facts

- `cosmoGRID V1` (Fluri+2022, Kacprzak+2023), `PkdGrav3`, HEALPix `Nside=512` → ℓ ≤ 1024.
- Flat *w*CDM, 6 sampled params; **fiducial Ωm = 0.26, σ8 = 0.84, w0 = −1**; reported subspace
  **(Ωm, σ8, w0)**.
- **4 tomographic bins**, mean z ≈ 0.3, 0.5, 0.7, 0.9. Euclid-like noise: n_gal = 30 arcmin⁻²,
  σ_ε = 0.26 per component, at map level.
- Baryons: BCM **"shell baryonification"**, **log₁₀(M_c⁰/h⁻¹M_⊙) = 13.82, ν = 0**. ~1 000× faster
  than 3D particle displacement, which is what made 2 500 cosmologies affordable.
- Starlet: 5 scales, the **4 finest dyadic bands ≈ 10′, 20′, 40′, 80′**; coarse excluded.
- NPE with a **MAF**; every point averaged over **5 independent training runs** (the ± throughout).
- Tension via **Q_DM** (`tensiometer`) → Gaussian-equivalent σ. Threshold **0.3σ**.
- Coverage: **TARP** (Lemos+2023) on every posterior.

### Bias at full resolution (ℓmax = 1024, no cuts)

| area | PS | starlet peaks | starlet ℓ1 |
|---|---|---|---|
| 2 000 deg² | ~0.4σ | ~0.8σ | ~1.0σ |
| 14 000 deg² | **2.2σ** | **3.6σ** | **3.6σ** |
| full sky | ~3.5σ | **> 6σ** | **> 6σ** |

At every area the HOS are the *more* affected statistic. The reason is not that they are more
baryon-sensitive per se but that their contours are tighter *and* their displacement direction
differs: both wavelet statistics push σ8 and w0 low with little movement in Ωm, while the PS
slides along its Ωm–σ8 degeneracy toward low Ωm and absorbs the rest in w0.

### The cuts

- **PS — a sliding ℓmax**, tuned per area: **860 / 580 / 540 / 460 / 380 / 380 / 340** for
  2k / 5k / 10k / 14k / 28k / 35k / full sky.
- **HOS — drop the finest band (j = 1), at every area.** The surviving bands dominate ℓ ≲ 336.

### What survives — the Act 3 ratio curve

Ratios are the paper's own (parentheses in Table `tab:fom_results`); the **bands are derived**
by propagating the 5-run scatter, σ_r/r = √((σ_A/A)² + (σ_B/B)²), treating the two as independent:

| area | starlet peaks / PS | starlet ℓ1 / PS |
|---|---|---|
| 2 000 deg² | ×0.46 ± 0.08 | **×1.15 ± 0.18** |
| 5 000 deg² | ×0.63 ± 0.11 | ×1.60 ± 0.19 |
| 14 000 deg² | ×1.07 ± 0.25 | ×1.80 ± 0.58 |
| full sky | ×1.17 ± 0.15 | ×2.61 ± 0.41 |

**Rounding note.** Recomputing the ratios from the rounded FoM values above does *not* reproduce
the paper's printed ratios at the two smallest areas — the table gives ℓ1/PS = 2.7/2.3 = 1.17
against the printed **×1.15**, peaks 1.1/2.3 = 0.48 against **×0.46**, and peaks 4.1/6.4 = 0.64
against **×0.63**. The paper computed its ratios from unrounded values, which is correct. **Use
the paper's printed ratios**, not a recomputation from the table, and do not "fix" them.

Absolutes behind them, **ledger only** (FoM₃ in units of 10⁴): PS 2.3 ± 0.3, 6.4 ± 0.7,
14.5 ± 0.9, 54.9 ± 2.9 · peaks 1.1 ± 0.1, 4.1 ± 0.5, 15.5 ± 3.5, 64.0 ± 7.2 · ℓ1 2.7 ± 0.2,
10.3 ± 0.4, 26.1 ± 8.2, 143.4 ± 21.4.

**Three things the bands change, and all three must be spoken:**

1. **At 2 000 deg² the ℓ1 advantage is not significant** — 1.15 ± 0.17 touches unity. The claim
   "the ℓ1-norm beats the power spectrum at every area" is *not* supported at the smallest
   footprint. Correct statement: the advantage **grows with area and is significant from
   5 000 deg² upward**.
2. **Peaks at 14 000 deg² are consistent with parity** — 1.07 ± 0.25. "Comparable to the power
   spectrum" is the right phrase; the band is why.
3. **×1.80 at 14 000 deg² carries a ±0.58 band**, driven by a 31 % scatter on the ℓ1 FoM across
   the five NPE runs. Quote it as "about a factor of two", not as 1.80.

**Only four survey areas have FoM entries** (2k / 5k / 14k / full sky), against seven in the
scale-cut table. The ratio-vs-area curve therefore has **four points, not seven** — do not draw a
smooth seven-point trend the paper does not have.

### BNT on the power spectrum — the positive result

- Lossless check at ℓmax = 1024, no cuts: standard and BNT contours effectively identical, FoM
  within a few per cent — **provided the cross-spectra between transformed bins are kept**.
- Needs an **embedding network** before the flow: nulling anticorrelates the bins, so BNT
  cross-spectra fluctuate about zero and the signal spreads over many low-amplitude components.
  Same architecture in both bases, so only the basis differs.
- Baryon sensitivity **localises to the first transformed bin κ̂₁**; bins 2–4 keep ℓmax ≈ 1024.
- At 14 000 deg²: bin-specific cut retains **92 of 120 bandpowers** vs **50** for the global cut →
  **FoM ×1.4**, with **σ(Ωm) −14 %**, **σ(σ8) −19 %**, σ(w0) essentially unchanged.

### BNT on map-based HOS — the negative result Ch5 resolves

Contours for starlet peaks and the ℓ1-norm **inflate drastically**. They formally pass the 0.3σ
criterion, but **only because they are larger** — the paper says so explicitly, and so must the
talk. Ch4's own diagnosis: the data vector carries **auto-components only**, so it cannot model
the noise field the mixing has correlated.

Mechanism, in the paper's words: nulling subtracts tomographic maps. The shared signal cancels
(intended); the shape noise is independent between bins so it does **not** cancel — variances add.
Each higher-z transformed map carries less signal and more noise, and the noise becomes
**correlated across the transformed maps**.

### Other Ch4 facts worth having

- PS baryonic suppression reaches **≈1.5 % by ℓ ≈ 1000** for the higher-z bins **on noisy maps**.
  The apparent "high-z bins are worse" ordering is a **noise artefact** — N_ℓ dominates the
  denominator at low z. On noiseless maps the ordering inverts to the physically expected one.
  Good question to be ready for; it is in the appendix.
- The HOS baryon response concentrates in the **positive SNR tail** and vanishes in the
  noise-dominated bulk (|ν| ≲ 2.5). That makes an **SNR-space cut** available to HOS and not to
  the PS — left to future work, so flag it as a direction, not a result.
- Closing frame: this is the **floor**. No feedback model at all, every measurably contaminated
  scale discarded.

---

## 5. Ch5 — the joint ℓ1-norm

### Setup facts

- Same `cosmoGRID V1`, but **10°×10° gnomonic patches**, 80×80 px, |b| < 75°, **180 patches ×
  50 noise realisations = 9 000 mock observations**.
- Training on **3.2 × 10⁵ patch examples from 899 cosmologies**, the same set for both summaries.
- Every summary compressed to **d = 10**, passed through the **same RealNVP** (4 coupling blocks,
  width 128; 3 flows pooled), tuned **separately for each summary**.
- CNN: **ResNet-18 family**, trained with **VMIM** for 5 × 10⁴ steps.
- Map means subtracted per channel (mass-sheet degeneracy).
- Patch size 10° because gnomonic corner distortion falls from **6.3 % at 20° to 1.5 % at 10°**.
- Every posterior verified with **TARP + SBC**.

### The completeness ladder — the Act 4 graphic

Baseline is the **CNN**, because VMIM makes it an estimate of the *ceiling*, not a rival.
Ratios and bands **[derived]**, same propagation as §4:

| summary | ratio to CNN | band |
|---|---|---|
| ℓ1 auto-only | **0.74** | ± 0.010 |
| + convolution cross-maps | 0.80 | (no ± published) |
| + product cross-maps | **0.92** | ± 0.056 |
| both cross-map types | 0.98 | (no ± published) |
| **joint ℓ1** | **1.01** | ± 0.030 |
| CNN (VMIM) | 1.00 | — |

Absolutes, **ledger only** (FoM₃): auto 2448 ± 27 · +conv 2671 · +prod 3045 ± 183 · both 3255 ·
joint 3371 ± 96 · CNN 3326 ± 30. Marginals for the headline four: σ(Ωm) 0.053 / 0.048 / 0.044 /
0.045, σ(σ8) 0.085 / 0.077 / 0.072 / 0.072, σ(w0) 0.245 / 0.229 / 0.223 / 0.231 for
auto / +product / joint / CNN.

**joint ℓ1 = 1.01 ± 0.030 includes unity.** That is what licenses "tie", and it is the whole
reason "beats" is wrong. The ± is the spread over **three independently trained compressors** —
the dominant source of run-to-run variability. Flow-training stochasticity moves medians by ≲1 %;
the sampling error of the median over 9 000 mocks is < 0.5 %.

The CNN gains **nothing systematic** from explicit cross-maps: it already reads the four bins
jointly. The paper's expected explanation for joint ℓ1 sitting a hair above it is the CNN's mildly
conservative coverage.

### The BNT retention ladder

Each summary against **its own** un-nulled constraint. Ratios published; bands **[derived]**:

| summary | retention | band |
|---|---|---|
| ℓ1 auto-only | **0.16** | ± 0.018 |
| ℓ1 + product | **0.24** | ± 0.017 |
| joint ℓ1 | **0.72** | ± 0.065 |
| CNN | **0.96** | ± 0.018 |

Absolutes, **ledger only**: 388 ± 43 / 2448 ± 27 · 718 ± 29 / 3045 ± 183 · 2424 ± 208 / 3371 ± 96 ·
3186 ± 52 / 3326 ± 30. For ℓ1+product under BNT: σ(σ8) 0.077 → 0.133, σ(w0) 0.229 → 0.300.

**One law instead of four results:** *what a summary retains under the nulling tracks how jointly
it reads the bins.* 1-D marginals → 0.16. One derived field per pair → 0.24. Full pairwise
distributions → 0.72. All four channels at once → 0.96. Counter-intuitive, since the nulling is
designed precisely to **de**-correlate the bins.

All BNT posteriors pass the same TARP + SBC battery. **The collapse is calibrated** — the wide
contours are an honest report of a real loss in that representation, not over-confidence.

### The joint ℓ1-norm, defined

Per scale and bin pair (i, j), lay a fixed **K×K grid (K = 10)** over the joint (u_i, u_j) plane of
SNR-normalised wavelet coefficients and sum the ℓ1 weight **½(|u_i| + |u_j|)** in each cell.
**Six bin pairs**, concatenated over scales. Built from the **four auto-maps alone — no explicit
cross-map channel.**

Summing |·| rather than counting pixels is what makes it the 2-D analogue of the ℓ1-norm rather
than a joint PDF estimate. **Pairwise is the ceiling**: with K⁴ cells against 80×80 pixels a 4-D
histogram is almost everywhere empty. The residual gap to the CNN is exactly the genuinely 3- and
4-bin structure.

### The closure criterion (Appendix `app:bnttheory`)

A fixed summary is BNT-invariant exactly when its induced action T(x) ↦ T(Bx) is **invertible**.

- Full auto **+ cross** second-moment vector **passes**: BNT acts as the congruence
  **Ĉ ↦ B Ĉ Bᵀ**, invertible. Hence the exact invariance of a 2-point analysis under nulling.
- **Auto-spectra alone fail on completeness** — they keep only the diagonal of B Ĉ Bᵀ, four
  numbers that depend on all ten originals but cannot be inverted without the off-diagonals.
  Repairable by restoring the cross-spectra.
- The **per-channel ℓ1 fails structurally**: under B it becomes "mix the channels, then take a
  single-channel marginal histogram", and marginalising after mixing is irreversible. **No later
  processing of the single-channel histograms can restore it.**
- The **CNN is immune for free**: feeding it Bx gives the same first layer with kernels KB, so
  f ↦ f∘B is a bijection of the network class onto itself. "Undo the nulling" is one configuration
  of the first layer, available before any non-linearity at no capacity cost.

### Other Ch5 facts

- **Cramér–Wold on survey practice.** Merging two bins' catalogues and measuring on the combined
  map supplies only **linear** cross channels. Cumulants expand multilinearly, so pairwise
  equal-weight combinations are **complete at second order, incomplete at third and beyond**.
  This is *why* the standard construction does not cure BNT inflation.
- **Why the tie is not surprising.** Noisy κ maps at these depths are close to a Gaussian random
  field plus quasi-circular peaks, and the starlet basis is built for exactly that. Corollary
  worth saying out loud: **where the field is morphologically richer, the balance should tip back
  toward the network.**
- **Fisher map** (Appendix `app:fisher`): the ℓ1's constraining power concentrates at
  **intermediate scales (j = 2–3, tens of arcmin) and moderate SNR (|ν| ≈ 1–2)** — mildly
  non-linear structure, not rare extreme peaks. Dovetails with Ch4's "drop j = 1 and keep most".
- Full-sphere leakage: cross channels carry **12–20 %** of their variance at ℓ < 18 vs **0.4–1 %**
  for the autos; cross power piles up at median ℓ ≈ 60–90 against ℓ_eff ≈ 600 for the autos.

---

## 6. Framing rules — phrasings that must not drift

Carried from `../cosmo26/PAPER_FACTS.md` §3b, still binding, all three verified against the thesis.

**The two scale cuts are not like for like.** The PS gets a **sliding** ℓmax tuned per area; the
starlet gets a **quantised** cut, because whole-band removal is the only option a dyadic
decomposition offers. Dropping j = 1 suffices everywhere, but at smaller footprints it *"likely
discards more uncontaminated, quasi-linear information than strictly necessary."* So the wavelet
cut is **coarser and therefore conservative, not cleverer**. The genuine wavelet property is that
the contamination *concentrates* in one band.

**Peak counts do not "lose".** They reach **approximate parity** at Stage IV and slightly exceed
the PS at full sky; at smaller areas they trail, and largely *because of the cut*, not the
statistic. And their degeneracy directions differ from the PS in the (Ωm, w0) and (σ8, w0) planes,
so **comparable FoM is not redundancy** — they add information.

**Starlet bands overlap.** They are band-passes that **overlap substantially**, labelled by a
characteristic angular size. They do not "isolate a single angular scale".

**Ch2's iKS result is a null result**, and the paper says it does not generalise to Fourier-space
statistics. Do not silently drop iKS from the Act 1 figure.

---

## 7. Numbers that must not survive a copy-paste from an older deck

From `../NonGaussian_Universe_2026/` and the June-era slides, via `../cosmo26/PAPER_FACTS.md` §4.4:

`~3×` → **×1.8 (14k) / ×2.6 (full sky)** · `~7 %` → **a tie** · `0.26×` → **0.24×** ·
`+20 %` → **+24 %** · `"convolution adds nothing"` → **+9 %** · `"~2σ at 14k"` → **2.2σ (PS),
3.6σ (HOS)** · `0.15/0.22/0.93/1.06` → **0.16/0.24/0.72/0.96**.

**`../cosmo26/bnt_explainer.js` still hardcodes the superseded ladder.** If that component is
reused it must be re-pointed before it goes in the deck.

**The whitening result (`Q = (BBᵀ)^(−1/2)B` recovers the per-channel ℓ1 "1.06×") is not in the
paper** and was retired from the COSMO-26 deck on 2026-08-20. It stays retired.

---

## 8. Corrections and open calls

### 8.1 The "~1×" CNN rung — right decision, wrong stated reason

`../cosmo26/PAPER_FACTS.md` renders the CNN's BNT retention as a full bar labelled **~1×**, on the
grounds that *"0.96 is within its error of unity"*. **Propagation does not support that
justification.** 3186 ± 52 against 3326 ± 30 gives **0.958 ± 0.018 [derived]**, which sits about
2.3σ below unity.

The decision to draw it as ~1× is still right, but the defensible reason is **theoretical, not
statistical**: the closure criterion proves f ↦ f∘B is a bijection of the CNN class onto itself,
so the true retention is exactly 1 and the measured shortfall is an **optimisation residual**. The
paper says exactly this — *"the departure from unit retention is then an optimisation residual,
not a loss of information"* (`Abnt-theory.tex`).

Two consequences:

- On the slide, ~1× is fine. In the **words**, the justification is the closure argument, never
  "it's within the error bar."
- The independence assumption in the propagation is itself questionable — the two figures of merit
  come from the same mocks and the same summary, so they are correlated and the true band on the
  ratio is narrower than ±0.018. That is an argument *for* ~1×, but it is one I have not
  quantified and should not assert. **If asked, the honest answer is the closure argument.**

This is the kind of question Tsakalides or Courbin would ask, so it is worth having straight.

### 8.2 Prepared answer for "×2.6 in what?"

> *"Chapter 2's figure of merit is the fourth root of the determinant of the Fisher matrix over
> four parameters, so a factor 2.6 is a per-dimension improvement — comparable to a ratio of
> uncertainties. Chapters 4 and 5 use one over the square root of the determinant of the
> covariance over three parameters, which is an inverse volume. The two are not the same power, so
> I quote each chapter's ratio in its own convention rather than chaining them. The setups differ
> as well: different simulation suites, different geometries."*

### 8.3 Numbers I could not verify and that are therefore not slide-eligible

- The **±** on the `+convolution` and `both cross-map types` rungs of the Ch5 completeness ladder
  is not published. Draw those rungs without bands, or omit them from the graphic.
- The **+9 %** convolution-cross-map gain is flagged in the paper as **sensitive to the training
  realisation**. If it goes on a slide it goes with that clause attached.
- Ch2 reports **no error bars on the FoM** — the values come from single MCMC chains per method.
  So the Act 1 ratio bar has **no band to draw**, unlike Acts 3 and 4. Do not invent one, and do
  not let the missing band read as higher precision than Acts 3–4. Worth one spoken clause.

### 8.5 A0.2's pie chart is wrong, and it must not ship as it stands

`assets/diagrams/dedm_pie_chart.001.jpeg`, lifted from `../PhD_Day_2025` §3, breaks the matter
slice into **"Dark Matter ~73 %" and "Visible Universe ~27 %"**. Against the thesis's own
Section 1.1.5 and Planck 2018 that is wrong:

| | of the **total** budget | of the **matter** slice |
|---|---|---|
| dark energy | ~68 % (thesis) | — |
| cold dark matter | ~27 % (thesis) | **84.3 %** [derived] |
| baryons | <5 % (thesis) | **15.7 %** [derived] |

Derived from Planck 2018: Ωb h² = 0.02237, Ωc h² = 0.1200, h = 0.674 → Ωb = 0.0492,
Ωc = 0.2642, Ωm = 0.3134.

The figure's **27 % is the CDM-of-total number wearing the label "Visible Universe."** Ordinary
matter is overstated by a factor of about five as a share of the total, or about 1.7 as a share of
matter, depending on which reading the viewer takes. The left-hand pie (dark energy ~70 %, total
matter ~30 %) is fine and consistent with the thesis.

Starck, Kilbinger and Pavlidou will all read this instantly, on slide two.

**Options, in order of preference:** replace with a corrected figure; or crop to the left-hand pie
alone, which is correct and still makes the "most of it is dark" point; or drop the figure and let
the three parameter cards carry A0.2. **Do not ship the current version.**

### 8.4 Open call — the Ch2 volume conversion

§0 records ×2.57⁴ ≈ 43.6 as the inverse-volume equivalent of Ch2's headline. It is arithmetically
correct and rhetorically tempting. **Recommendation: keep it out of the talk entirely.** It is not
the published claim, it will read as inflation to anyone who checks, and the 157 % figure is
already strong. Recorded here only so that the answer exists if someone derives it themselves.

---

## 9. External facts used in Act 0

Not thesis results, so they need their own source lines. All traced to the thesis introduction
(`chapters/introduction/cosmology-basics.tex` §1.1.7) so the talk and the manuscript agree.

| fact | value | source |
|---|---|---|
| Euclid survey area | **~14,000 deg²** of extragalactic sky | `cosmology-basics.tex` L360, citing `euclid_2024` |
| …as a fraction of the sky | **~34 %**, "about a third" [derived] | 14,000 / 41,253 deg² |
| Euclid launch | **2023** | same line |
| Euclid DR1 | **June 2027**, first cosmological data release | same line |
| Euclid probes | weak lensing from visible imaging, clustering from NIR | same line |
| Rubin/LSST area | **~18,000 deg²**, southern sky, ground-based | `cosmology-basics.tex` L359 |
| Stage IV galaxy counts | **"billions of galaxies"** | `cosmology-basics.tex` L357, L359; `conclusion.tex` L7 |
| ΛCDM budget | dark energy ~68 %, CDM ~27 %, baryons <5 % of total | `cosmology-basics.tex` §Composition, citing `Planck2020params` |

**"1.5 billion galaxies" is deliberately not used.** It appears on the `../PhD_Day_2025` slide and
is a real Euclid figure in the mission literature, but it is **not in the thesis**, so it fails the
ledger rule. "Billions of galaxy shapes" is supported and lands just as hard.
