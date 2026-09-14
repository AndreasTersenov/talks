# PAPER_FACTS — the numbers this deck uses

**The authority is `../PhD_Defense_2026/PAPER_FACTS.md`** (written 2026-08-25 from the thesis,
which reproduces the four papers). Nothing here is new; this file lists only what reaches a slide
or the script in `PIML_FORTH_2026`, with the section of the defense ledger it comes from. The two
rules carry over: **ratios only** on slides (no absolute figure of merit), and the ratios of Part 1
and Part 2 are **not the same quantity** (defense ledger §0).

| where | what is said | value | source |
|---|---|---|---|
| frame 12, A1.5 | the sparse solver's map error against the linear inverse | ratio **0.959**, "4 % better" | §2, RMSE table |
| frame 12, A1.5 | its constraining power against the linear inverse | ratio **2.57**, "157 %" | §2, 4-parameter FoM, wavelet peak counts |
| frame 12, A1.5 | inpainting the mask changes nothing | ratio 0.996 | §2, iKS null result |
| frame 14, A1.7 | denoiser size, iterations | SUNet, **7.2 M** parameters; **8** iterations; step size in (0, 0.176) | §3 |
| frame 16, A1.9 | PnPMass accuracy against DeepMass | RMSE ratio **1.013**, "within about 1 %" | §3 |
| frame 16, A1.9 | smallest calibrated error bars | on all **512** test maps | §3 |
| frame 16, A1.9 | target error rate | α ≈ **4.55 %**, from 1 024 calibration maps | §3 |
| frame 23, A2.6 | the learned encoder ahead of the per-channel ℓ1 | **36 %** (3326 / 2448) | §5 |
| frame 26, A2.9 | the tie | joint ℓ1 **3371 ± 96** against CNN **3326 ± 30**, ratio 1.01 ± 0.03, said as "a tie" | §5 |
| frame 22, A2.5 | training set | **3.2 × 10⁵** patches, **899** cosmologies, d = 10, RealNVP | §5 |
| Q&A 5 | the architecture ladder | RealNVP +36 %, resnet-18 +6 % | script, defense Q&A tier 2 |
| Q&A 6 | the baryon result (backup only) | bias 2.2σ (PS) / 3.6σ (HOS) at 14 000 deg²; ℓ1 **×1.8** on safe scales, ±0.6 | §4 |

**Deliberately not said**: the absolute figures of merit of Part 1 (758 / 755 / 1947); the
inverse-volume conversion ×2.57⁴; the PnPMass timing table (the claim is *trained once*, not *fast
per map*).
