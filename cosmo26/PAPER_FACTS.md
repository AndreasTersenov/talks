# PAPER_FACTS — the number ledger for the COSMO-26 deck

**Rule: no number goes on a slide unless it appears in this file with a source line.**
The June deck (`../NonGaussian_Universe_2026/`) asserts several numbers the papers no longer
support. This file is the authority; the old deck is not.

Sources, both read in full on 2026-08-19:

- **Paper I** — *Mitigating Baryonic Effects in Weak Lensing with Higher-Order Statistics*.
  Tersenov, Guerrini, Starck, Kilbinger. A&A `aa60075-26`, **resubmitted 2026-08-10**.
  `~/Desktop/Impact_of_Baryonic_Feedback_Resubmission/submission_2026-08-10/_source_contents/main.tex`
- **Paper II** — *The joint wavelet ℓ1-norm matches neural compression for tomographic
  weak-lensing inference*. Tersenov, Starck, Kilbinger. **In preparation.**
  `~/Desktop/joint_l1_paper_overleaf/` (`main.tex` + `sections/*.tex`)

**Scoping guardrail, carried over from the June script and still binding.** Paper I is
full-sky HEALPix with masked footprints; Paper II is 10°×10° flat-sky patches. Their figures of
merit are *not* comparable and must never be chained into one ladder. Paper I's statement is
"ℓ1 vs the power spectrum on baryon-safe scales"; Paper II's is "ℓ1 vs a learned compressor on
matched patches". Two separate sentences, always.

---

## 1. Shared setup (say once, applies to both)

| | |
|---|---|
| Simulations | `cosmoGRID V1` (Fluri+2022, Kacprzak+2023), `PkdGrav3`, HEALPix `Nside=512` → ℓ ≤ 1024 |
| Cosmology | flat *w*CDM, 6 params (Ωm, σ8, w0, H0, ns, Ωb), Sobol-sampled; fiducial Ωm=0.26, σ8=0.84, w0=−1 |
| Reported subspace | (Ωm, σ8, w0) — the lensing-constrained directions |
| Tomography | 4 source bins, mean z ≈ 0.3, 0.5, 0.7, 0.9 |
| Noise | *Euclid*-like: n_gal = 30 arcmin⁻², σ_ε = 0.26 per component, added at map level |
| FoM₃ | 1/√det **C**(Ωm, σ8, w0) |
| Starlet | 5 scales; the 4 finest dyadic bands ≈ 10′, 20′, 40′, 80′; coarse scale excluded |
| Baryons (Paper I) | BCM "shell baryonification"; log₁₀(M_c⁰/h⁻¹M_⊙) = **13.82**, ν = 0 |

**Paper I only** — masked polar-cap footprints at 2 000 / 5 000 / 10 000 / 14 000 / 28 000 /
35 000 deg² and full sky; NPE with a **MAF**; every point averaged over **5 independent
training runs**; tension via **Q_DM** (`tensiometer`), threshold **0.3σ**.

**Paper II only** — 10°×10° gnomonic patches, 80×80 px (7.5′/px), |b| < 75°, **180 patches per
realisation × 50 noise realisations = 9 000 mock observations**; training on **3.2×10⁵ patch
examples from 899 cosmologies**, the same set for both summaries; every summary compressed to
**d = 10** and passed through the **same RealNVP** (4 coupling blocks, width 128; 3 flows
pooled); CNN is a **ResNet-18-family** net trained with **VMIM** for 5×10⁴ steps; map means
subtracted per channel (mass-sheet degeneracy). Patch size chosen at 10° because gnomonic
corner distortion falls from **6.3 % at 20° to 1.5 % at 10°**.

---

## 2. Paper I — what changed since the June deck

| claim | June deck says | **paper says** | source |
|---|---|---|---|
| ℓ1 vs PS on baryon-safe scales | "~3×" | **×1.15** (2k), **×1.60** (5k), **×1.80** (14k), **×2.61** (full sky) | Table `tab:fom_results` |
| peak counts vs PS | not stated | **×0.46**, **×0.63**, **×1.07**, **×1.17** — *below* the PS at the small areas | same |
| bias @ 14 000 deg² | "$C_\ell$ ~2σ" | PS **2.2σ**, peaks **3.6σ**, ℓ1 **3.6σ** | §`sec:bias_vs_area` |
| bias @ full sky | "exceeds 3σ for all" | PS **~3.5σ**, both HOS **> 6σ** | same |
| bias @ 2 000 deg² | not stated | PS **~0.4σ**, peaks **~0.8σ**, ℓ1 **~1.0σ** | same |
| PS scale cut | "ℓ ≲ 400" | ℓmax **860 / 580 / 540 / 460 / 380 / 380 / 340** for 2k / 5k / 10k / 14k / 28k / 35k / full sky | Table `tab:scale_cuts` |
| HOS scale cut | drop finest band | drop **j = 1**, every area — unchanged | same |
| BNT on the PS | not quantified | **FoM ×1.4** at 14k; see below | §`sec:bnt_results` |

### FoM on baryon-safe scales (units of 10⁴, ±  = scatter over 5 NPE runs)

| statistic | 2 000 | 5 000 | 14 000 | full sky |
|---|---|---|---|---|
| PS | 2.3 ± 0.3 | 6.4 ± 0.7 | 14.5 ± 0.9 | 54.9 ± 2.9 |
| starlet peaks | 1.1 ± 0.1 (×0.46) | 4.1 ± 0.5 (×0.63) | 15.5 ± 3.5 (×1.07) | 64.0 ± 7.2 (×1.17) |
| starlet ℓ1 | 2.7 ± 0.2 (×1.15) | 10.3 ± 0.4 (×1.60) | **26.1 ± 8.2 (×1.80)** | **143.4 ± 21.4 (×2.61)** |

Two honesty notes that belong in the spoken words if this table is shown:

- The HOS entries are **conservative at the small areas**. The dyadic starlet forces the whole
  `j=1` band out everywhere, while the PS gets a sliding ℓmax tuned per area. Only at full sky
  are both statistics cut to their actual limits. A √2-resolution or non-dyadic filter bank
  would recover some of this.
- **Peak counts lose to the PS below Stage IV.** Do not quietly drop them from the plot; the
  honest statement is that the ℓ1-norm, not "HOS in general", is what survives the cut.

### BNT on the power spectrum (a *positive* Paper I result the June deck never quantified)

- Lossless check: at full resolution (ℓmax = 1024, no cuts) the standard and BNT contours are
  effectively identical, FoM within a few per cent — **provided the cross-spectra between
  transformed bins are kept**.
- Requires an **embedding network** in front of the flow: the nulling anticorrelates the bins,
  so BNT cross-spectra fluctuate about zero and the information is spread over many
  low-amplitude components. Without it the marginals are fine but the correlation structure
  degrades. Same architecture used in both bases so only the basis differs.
- Baryon sensitivity localizes to the **first transformed bin** κ̂₁, so the cut goes there
  alone and bins 2–4 keep ℓmax ≈ 1024.
- At 14 000 deg² with the matched cut ℓmax = 460: the bin-specific BNT cut retains
  **92 of 120 bandpowers** against **50** for the global cut → **FoM ×1.4**, with
  **σ(Ωm) −14 %**, **σ(σ8) −19 %**, σ(w0) essentially unchanged.

### BNT on map-based HOS (Paper I's negative result — the one Paper II resolves)

Contours for starlet peaks and the ℓ1-norm **inflate drastically** under BNT, worse than
standard tomography even with conservative scale cuts. They formally pass the 0.3σ bias
criterion, but only because they are larger. Paper I's own diagnosis: the data vector carries
**auto-components only**, so it cannot model the noise field the mixing has correlated.
Paper I cites `vinciguerra_euclid_2026`, who keep tomographic maps for bin combinations up to
quadruplets and still see inflation, and concludes that a truly lossless nulled HOS analysis is
"highly non-trivial". **This is the cliffhanger Paper II answers.**

### Mechanism, in the paper's own words

Nulling subtracts the tomographic maps. The shared signal cancels (intended); the shape noise
is independent between bins so it does **not** cancel — the variances add. Each higher-z
transformed map therefore carries less signal and more noise, and the shape noise, originally
independent, becomes **correlated across the transformed maps**.

### Other Paper I facts worth a slide

- Baryonic suppression of the PS reaches **≈1.5 % by ℓ ≈ 1000** for the higher-z bins on noisy
  maps. The apparent "high-z bins are worse" trend is a **noise artifact** — N_ℓ dominates the
  denominator at low z. On noiseless maps the ordering inverts to the physically expected one
  (lowest-z bin most suppressed, starting at lower ℓ).
- The HOS baryon response is concentrated in the **positive SNR tail** and vanishes in the
  noise-dominated bulk (|ν| ≲ 2.5) — which is why an SNR-space cut (not just a scale cut) is
  available to HOS and not to the PS. Left to future work in the paper.
- Displacement directions differ: both wavelet statistics push σ8 and w0 low with little
  movement in Ωm; the PS slides along its Ωm–σ8 degeneracy toward low Ωm and absorbs the rest
  in w0. Combined with tighter HOS contours, that is why the HOS tensions are larger.
- Closing frame: this is the **floor**. No feedback model at all, every measurably contaminated
  scale discarded. Anything that models the feedback can only improve on it.

---

## 3. Paper II — what changed since the June deck

**The headline flipped.** June: "the CNN still wins by ~7 %". Now: **a tie**, because the paper
introduces a new statistic, the **joint ℓ1-norm**.

| claim | June deck says | **paper says** | source |
|---|---|---|---|
| headline | CNN ahead by **~7 %** | **tie** — joint ℓ1 **3371 ± 96** vs CNN **3326 ± 30** | Table `tab:headline` |
| BNT retention | ℓ1+prod **0.26×**, CNN 0.96× | auto **0.16**, +product **0.24**, joint ℓ1 **0.72**, CNN **0.96** | Table `tab:bnt` |
| product cross-map gain | "+20 %" | **+24 %** | §`sec:power` |
| convolution cross-map | "adds nothing" | **+9 %**, and sensitive to the training realisation | §`sec:crossinfo` |
| full-sphere leakage | "~92 % leakage" | full-sphere cross channels carry **12–20 %** of their variance at ℓ<18 vs **0.4–1 %** for the autos; cross power piles up at median ℓ ≈ 60–90 vs ℓ_eff ≈ 600 for the autos | same |

### The headline table (matched RealNVP, medians over 9 000 mocks)

| summary | σ(Ωm) | σ(σ8) | σ(w0) | FoM₃ |
|---|---|---|---|---|
| ℓ1 auto-only | 0.053 | 0.085 | 0.245 | 2448 ± 27 |
| ℓ1 + product | 0.048 | 0.077 | **0.229** | 3045 ± 183 |
| **joint ℓ1** | **0.044** | **0.072** | 0.223 | **3371 ± 96** |
| CNN (VMIM) | 0.045 | 0.072 | 0.231 | 3326 ± 30 |

The ± is the **spread over three independently trained compressors** — the dominant source of
run-to-run variability. Flow training stochasticity moves medians by ≲1 %; the sampling error of
the median over the mocks is < 0.5 %.

### The completeness ladder (FoM₃, same pipeline)

`auto 2448` → `+convolution 2671 (+9 %)` → `+product 3045 (+24 %)` → `both 3255` →
`joint ℓ1 3371` — against the CNN's `3326`.

The CNN gains **nothing systematic** from explicit cross-maps: it already reads the four bins
jointly. The mildly conservative CNN coverage is the paper's expected explanation for the
joint ℓ1 sitting a hair above it — **call it a tie, never a win.**

### The BNT retention ladder — the single best thing in either paper

| summary | no BNT | BNT | retention |
|---|---|---|---|
| ℓ1 auto-only | 2448 ± 27 | 388 ± 43 | **0.16** |
| ℓ1 + product | 3045 ± 183 | 718 ± 29 | **0.24** |
| joint ℓ1 | 3371 ± 96 | 2424 ± 208 | **0.72** |
| CNN | 3326 ± 30 | 3186 ± 52 | **0.96** |

**How 0.96 is shown on the slide (2026-08-22, Andreas).** The act-3 ladder renders the CNN rung as a **full bar labelled `~1×`**, not `0.96×`. 0.96 is within its error of unity, and the claim the slide is making is *approximately lossless under the nulling*; a two-decimal figure invites the audience to read a real 4% loss that the measurement does not support. The ladder is scaled so a full track is 1.0, which makes the other three rungs read directly as the fraction retained. The exact value stays here and in the speaker notes for Q&A.

For ℓ1+product under BNT: σ(σ8) **0.077 → 0.133**, σ(w0) **0.229 → 0.300**.

**One law instead of four results:** *what a summary retains under the nulling tracks how
jointly it reads the bins.* 1-D marginals → 0.16. One derived field per pair → 0.24. Full
pairwise distributions → 0.72. All four channels at once → 0.96. Counter-intuitive, since the
nulling is designed precisely to *de-correlate* the bins.

All BNT posteriors pass the same TARP + SBC battery. **The collapse is calibrated** — the wide
contours are an honest report of a real loss in that representation, not over-confidence.

### What is new in Paper II and absent from the June deck

- **The joint ℓ1-norm.** Per scale and bin pair (i,j), lay a fixed K×K grid over the joint
  (u_i, u_j) plane of SNR-normalised wavelet coefficients and sum the ℓ1 weight
  ½(|u_i| + |u_j|) in each cell. K = 10, six bin pairs, concatenated over scales. Built from the
  **four auto-maps alone — no explicit cross-map channel.** Summing |·| rather than counting
  pixels is what makes it the 2-D analogue of the ℓ1-norm rather than a joint PDF estimate.
  Pairwise is the ceiling: with K⁴ cells against 80×80 pixels a 4-D histogram is almost
  everywhere empty. The residual gap to the CNN is exactly the genuinely 3- and 4-bin structure.
- **The closure criterion** (Appendix `app:bnttheory`). A fixed summary is BNT-invariant exactly
  when its induced action T(x) ↦ T(Bx) is invertible.
  - The full auto **+ cross** second-moment vector **passes**: BNT acts as the congruence
    **Ĉ ↦ B Ĉ Bᵀ**, invertible. Hence the exact invariance of a 2-point analysis under nulling.
  - **Auto-spectra alone fail on completeness** — they keep only the diagonal of B Ĉ Bᵀ, four
    numbers that depend on all ten originals but cannot be inverted without the off-diagonals.
    Repairable by restoring the cross-spectra.
  - The **per-channel ℓ1 fails structurally**: under B it becomes "mix the channels, then take a
    single-channel marginal histogram", and marginalising after mixing is irreversible. **No
    later processing of the single-channel histograms can restore it.**
  - The **CNN is immune for free**: feeding it Bx gives the same first layer with kernels KB, so
    f ↦ f∘B is a bijection of the network class onto itself. "Undo the nulling" is one
    configuration of the first layer, available before any non-linearity at no capacity cost.
    The 4 % shortfall is an optimisation residual, not information loss.
- **Cramér–Wold on survey practice.** The standard remedy — merge the galaxy catalogues of two
  bins and measure the statistic on the combined map — supplies only **linear** cross channels
  (the map estimator is linear in the sources, so the combined map is a count-weighted average,
  noise included). Cumulants expand multilinearly, so pairwise equal-weight combinations are
  **complete at second order and incomplete at third and beyond**, and three-bin mixed cumulants
  need three-bin combinations. This is *why* the standard construction does not cure BNT
  inflation — and it is consistent with `vinciguerra_euclid_2026`.
- **Why the tie is not surprising.** Noisy κ maps at these depths are close to a Gaussian random
  field plus quasi-circular peaks, and most morphology beyond that sits below the shape noise.
  The starlet basis is built for exactly that. Independent evidence: MCALens — a mass-mapping
  method on the same Gaussian + sparse two-component model — matches deep generative
  reconstructions. Corollary worth saying out loud: **where the field is morphologically richer
  than Gaussian-plus-peaks, the balance should tip back toward the network.**
- **The honest ledger on learned summaries** (§`sec:analyticalvslearned`): the ℓ1-norm is fixed
  before any simulation is seen, needs no retraining per survey configuration, cannot overtrain,
  and its data vector is inspectable scale-by-SNR. The compressor must be retrained and
  recalibrated for every change of forward model, and — the sharp risk — being trained to be
  maximally informative *on the simulations*, it cannot distinguish physical features from
  simulator artifacts and will exploit whichever carries information.
- **Where the CNN still earns its keep**: the nulled frame. Its native joint reading is the
  simplest lossless option there, and it needs no cross-map engineering.
- **Practical BNT message** (§`sec:bntpractice`): the nulling need not cost a higher-order
  analysis anything, **provided some stage of the pipeline reads the bins jointly.** Two named
  routes — the transform-back-after-cutting approach (`gu_mitigating_2025`,
  `vinciguerra_euclid_2026`, with the caveat that cut and inversion do not exactly commute over
  a factor of a few in ℓ), and moving the joint reading into the mass-mapping step (a
  tomographic plug-and-play reconstruction acting directly in the nulled frame).
- **Fisher map** (Appendix `app:fisher`): the ℓ1's constraining power concentrates at
  **intermediate scales (j = 2–3, tens of arcmin) and moderate SNR (|ν| ≈ 1–2)** — mildly
  non-linear structure, not the rare extreme peaks. Dovetails with Paper I's "drop j=1 and
  you keep most of it".

---

## 3b. Two claims that must be phrased the paper's way

These are not number errors, they are **framing** errors, and both were on slides until
2026-08-20. Neither survives contact with the paper.

### The two scale cuts are not like for like

Wrong: *"$C_\ell$ needs an area-dependent cut that discards most of the signal; the starlet
isolates the contamination in one scale, so removing one band suffices"* — which reads as the
wavelet cut being cleverer.

Right (§`sec:scale_cuts`): the power spectrum gets a **sliding** $\ell_{\rm max}$, tuned to keep
exactly what is safe at each area. The starlet gets a **quantised** cut, because the dyadic bands
increase by powers of two and whole-band removal is the only option available. Dropping $j=1$
suffices everywhere, but at the smaller footprints it *"likely discards more uncontaminated,
quasi-linear information than strictly necessary."* A √2-resolution or non-dyadic filter bank
would allow an area-tuned cut and retain more.

So the wavelet cut is **coarser and therefore conservative**, not better. The genuine wavelet
property is that the contamination *concentrates* in one band. The genuine HOS advantage the
paper does claim is different: peaks and the ℓ1-norm are binned in **signal-to-noise as well as
scale**, and the baryonic response sits in the positive tail, so in principle the contamination
can be cut where it sits rather than by removing a band. Left to future work.

### Peak counts do not "lose"

Wrong: *"peak counts lose to $C_\ell$ below Stage IV (×0.46 at 2,000 deg²)"*.

Right (§`sec:info_content`): they **reach approximate parity** with the power spectrum at Stage
IV-like areas (×1.07) and slightly exceed it at full sky (×1.17); at smaller areas they trail.
And the reason is largely the cut, not the statistic — *"the quantized wavelet cut removes a
larger fraction of the peak-count information than the sliding $\ell_{\rm max}$ cut removes from
the PS, and this penalty is most severe where the PS cut is loosest."*

Also load-bearing, and easy to omit: *"in the ($\Omega_{\rm m}$, $w_0$) and ($\sigma_8$, $w_0$)
planes the degeneracy directions of both HOS differ from that of the PS, so the statistics are
partly complementary. The peak counts therefore add information despite reaching a figure of
merit comparable to that of the PS."* Comparable FoM is not redundancy.

### And one wording fix on the starlet itself

The starlet bands are **band-passes that overlap substantially** (App. `app:starlet_ell`:
*"Adjacent bands overlap substantially, so the half-power ranges indicate where each band
dominates"*). They are labelled by a characteristic angular size; they do not "isolate a single
angular scale".

---

## 4. Open calls — flagged, not silently resolved

### 4.1 The whitening result is not in Paper II

The June deck's clincher slide and **Act 5** of the BNT canvas animation both turn on *"one
fixed whitening rotation Q = (BBᵀ)^(−1/2)B recovers the per-channel ℓ1 fully, **1.06×**"*.
That number appears **nowhere** in the Paper II draft. The paper proves the same point by two
other routes: noiseless maps give BNT ≈ no-BNT contours for every summary, and the closure
criterion says why. The figure asset `assets/figures/statistics/p2_M3_bnt_whitening.png` still
exists.

**Resolved 2026-08-20: retired** (see `STRUCTURE.md` §7). No live slide in the main flow now
depends on it. The two slides that did have been repointed: the "one story" problem→resolution
pair now uses `p2_bnt_learned` (the CNN, unaffected by the transform) as its resolution panel,
and the clincher slide is left in the backup pile with an HTML banner flagging that it asserts
a number absent from Paper II. `assets/figures/statistics/p2_M3_bnt_whitening.png` is retained
but referenced only there.

### 4.2 The BNT animation is calibrated to superseded numbers

`bnt_explainer.js` hardcodes a recovery ladder of `auto 0.15× → +cross 0.22× → CNN 0.93× →
whiten 1.06×` and the pair `3045 → 779 = 0.26×`. Paper II's ladder is
**0.16 / 0.24 / 0.72 / 0.96**, and 0.26 is not in the paper (0.24 is). Retuning the meter values
is a contained edit — but replacing Act 5 (whitening) with the joint-ℓ1 rung changes what the
animation *argues*, so it follows from 4.1.

### 4.3 The "is the +7 % worth it?" slide has lost its premise

It is no longer 7 %; it is a tie. The underlying content still stands and is arguably *more*
pointed now (the network's unphysical-shortcut failure modes largely passed TARP and SBC), but
the slide was written for a round-table panel that does not exist at COSMO. Either recast as
"the analytical statistic ties it *and* is the safer instrument" or cut to backup.

### 4.4 Old-deck numbers that must not survive a copy-paste

`~3×` → **1.8× (14k) / 2.6× (full sky)** · `~7%` → **a tie** · `0.26×` → **0.24×** ·
`+20%` → **+24%** · `"convolution adds nothing"` → **+9%** · `"~2σ at 14k"` → **2.2σ (PS), 3.6σ (HOS)**.
