# PAPER_FACTS — the numbers this deck uses

**The authority is `../PhD_Defense_2026/PAPER_FACTS.md`** (written 2026-08-25 from the thesis,
which reproduces the four papers). Nothing here is new; this file lists only what reaches a slide
or the script in `PIML_FORTH_2026`, with the section of the defense ledger it comes from. The two
rules carry over: **ratios only** on slides (no absolute figure of merit), and the ratios of Part 1
and Part 2 are **not the same quantity** (defense ledger §0).

| where | what is said | value | source |
|---|---|---|---|
| frame 9, A1.3 (spoken) | the sparse solver's map error against the linear inverse | ratio **0.959**, "4 % better" | §2, RMSE table |
| frame 9, A1.3 (spoken) | its constraining power against the linear inverse | ratio **2.57**, "157 %" | §2, 4-parameter FoM, wavelet peak counts |
| frame 9, A1.3 (spoken) | inpainting the mask changes nothing | ratio 0.996 | §2, iKS null result |
| frame 11, A1.7 | denoiser size, iterations | SUNet, **7.2 M** parameters; **8** iterations; step size in (0, 0.176) | §3 |
| frame 15, A1.9 | PnPMass accuracy against DeepMass | RMSE ratio **1.013**, "within about 1 %" | §3 |
| frame 12, A1.7b | the residual variant against DeepMass | RMSE ratio **1.006**, "within half a per cent"; beats the map variant by 6.04–6.88 × 10⁻³ at 95 % | §3 |
| frame 12, A1.7b (spoken) | iterations | budget **8**; at τ = 0.176 the residual variant is flat from iteration 2, the map variant settles by 3 | §3, the paper's per-iteration figure (`PnP_iterations1.png`, not shown) |
| frame 15, A1.9 | smallest calibrated error bars | on all **512** test maps | §3 |
| frame 15, A1.9 | target error rate | α ≈ **4.55 %**, from 1 024 calibration maps | §3 |
| frame 25, A2.6 | the learned encoder ahead of the per-channel ℓ1 | **36 %** (3326 / 2448) | §5 |
| frame 27, A2.9 | the tie | joint ℓ1 **3371 ± 96** against CNN **3326 ± 30**, ratio 1.01 ± 0.03, said as "a tie" | §5 |
| frame 24, A2.4 | training set | **3.2 × 10⁵** patches, **899** cosmologies, d = 10, RealNVP | §5 |
| Q&A 5 | the architecture ladder | RealNVP +36 %, resnet-18 +6 % | script, defense Q&A tier 2 |
| Q&A 6 | the baryon result (backup only) | bias 2.2σ (PS) / 3.6σ (HOS) at 14 000 deg²; ℓ1 **×1.8** on safe scales, ±0.6 | §4 |

**Deliberately not said**: the absolute figures of merit of Part 1 (758 / 755 / 1947); the
inverse-volume conversion ×2.57⁴; the PnPMass timing table (the claim is *trained once*, not *fast
per map*).

## The tomographic block (frames 17–19, added 2026-09-15)

**Source**: the draft `main.tex` of *Plug-and-play mass mapping with joint reconstruction across
several redshift bins* (Leterme, Tersenov & Starck, in preparation, September 2026), read on
2026-09-15. A draft: the test set is 32 crops with a to-do to make it 512, and the introduction
quotes a "20 %" RMSE gain (marked red) that the results table does not reproduce. **The table and
Fig. 4 are the authority; the 20 % is not said.**

| where | what is said | value | source |
|---|---|---|---|
| frame 17, A1.10 | six distance slices | edges z = 0, 0.57, 0.80, 1.05, 1.36, 1.79, 2.60 (Euclid bins, pairs merged) | Sect. 4.1, Fig. 2 |
| frame 17, A1.10 | a sixth of the galaxies, many empty pixels | 32 gal/arcmin² over all bins (COSMOS bright); at 0.29′ pixels "the number of missing pixels … is very large" | Sect. 2.3, 4.2 |
| frame 18, A1.11 | the denoiser | SUNet, 6 in / 6 out, noise-level channel, per-channel centring, **7.3 M** parameters | Sect. 4.5 |
| frame 18, A1.11 | step size fixed by the bound | τ = 2/λmax = **0.261**, λmax = 7.66; **24** iterations | Sect. 3.4, 4.4, eq. (stepsize) |
| frame 19, A1.12 | error over all channels, before the nulling | joint **0.891**, per channel **0.953** (NRMSE ×10⁻¹: 8.91 / 9.53) | Table 1, PnP row |
| frame 19, A1.12 | after the nulling | joint **0.944**, per channel **1.479** | Table 1, PnP row |
| frame 19 drawing | per-channel values, before, joint | 0.896, 0.864, 0.864, 0.875, 0.888, 0.910 | Fig. 4b, parsed from the SVG |
| frame 19 drawing | before, per channel | 0.995, 0.969, 0.955, 0.944, 0.957, 0.952 | Fig. 4b |
| frame 19 drawing | after, joint | 0.896, 0.887, 0.949, 0.983, 0.994, 0.999 | Fig. 4b |
| frame 19 drawing | after, per channel | 0.995, 0.984, 1.098, then above the axis (1.2) | Fig. 4b |
| backup | denoising alone at σ = 0.2 | joint 0.729 / per channel 0.818 before; 0.862 / 2.297 after | Table 1 |
| backup | the bound | E‖κ̂ − κ‖² ≤ (1 − L_τ ρ_τ)⁻² E‖F_Θ(κ + n_τ) − κ‖² | Proposition 2 |

"Relative to the zero map": the NRMSE is normalised so that predicting zero scores exactly one,
which is what makes "worse than the zero map" a literal reading of 1.48. The lens-efficiency
curves on frame 19 are computed in the build script from the draft's cosmology (H0 = 67.74,
Ωm = 0.3089) with one source distance per slice, at the slice's mid-distance; they are a schematic
of Fig. 1, not Fig. 1.

**Frame 16, the nulling** (added with the refocus of 2026-09-15): the transform is the one the
draft uses, Barthelemy et al. 2022's version for binned sources of Bernardeau, Nishimichi & Taruya
2014, a lower-triangular matrix with three non-zero entries per row whose weights depend only on
the (harmonic-mean) distances of the slices (draft Sect. 2.2). The curves are the same schematic as
frame 18's middle panel, at full width.

The frame numbers in the table above are as of the tomographic build; after the refocus of the
same day (Euclid and the 2025 pair hidden, the residual variant and the nulling in) they read:
frames 12 → 8 (spoken only), 14 → 10, 16 → 14, 23 → 24, 26 → 26, 22 → 23, and the tomographic
block 17–19 → 15, 17, 18.

With the operator slide lifted in after frame 3 (2026-09-15), every main-line frame from 4 on is
one higher again; `tools/list-frames.py PIML_FORTH_2026` is the authority. The Fourier kernels on
that slide, P̂₁ = (k₁² − k₂²)/k² and P̂₂ = 2k₁k₂/k², are Kaiser & Squires 1993.

**The `target_zbin_k` exports are the nulled truths, not the plain ones** (found 2026-09-15,
Andreas's hunch, checked on the rasters): inverting the viridis colours, the joint reconstructions
of neighbouring channels correlate at 0.98 or better, the targets at 0.3 to 0.4 beyond channel 2;
the target of channel k correlates with the plain joint reconstruction of channel k at 0.86 (k = 1),
0.56 (k = 2) and at most 0.05 from k = 3 on, blurred or not. That is a nulled truth: channel 1
untouched, channel 2 a difference, channels 3 to 6 emptied. Frame 16 therefore shows the **joint
reconstruction** in its top row, captioned "the maps, per slice", not the truth; the channel-1 map
on frame 19's card is unaffected (the nulling leaves channel 1 as it is). To confirm with Hubert
Leterme, and to replace with the plain truths if he exports them.

**Frame 24, reworded 2026-09-15.** ResNet-18 encoder, d = 10, RealNVP flow, four channels: defense ledger §5 and its Q&A tier 2 (the architecture ladder). The objective as written, E log q_ψ(θ | f_φ(x)) ≤ I(t; θ) − H(θ), is the Barber & Agakov 2003 bound that VMIM (Jeffrey, Alsing & Lanusse 2021) maximises.
