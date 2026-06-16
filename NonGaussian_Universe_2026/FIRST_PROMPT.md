We are building my conference talk deck "Do Baryons Break Higher-Order Statistics?" for the
"Non-Gaussian Universe" meeting (Tue 16 Jun 2026, ~25 min). The science, narrative, and figures are
already fully planned in a previous session; your job is to BUILD the reveal.js deck, not re-plan it.

Working dir: /home/tersenov/software/talks/  (deck goes in NonGaussian_Universe_2026/index.html).

Read these first, in order, before doing anything:
1. /home/tersenov/software/talks/NonGaussian_Universe_2026/HANDOFF_SLIDE_BUILD.md  (your full brief)
2. /mnt/home/tersenov/software/cnn_sbi/TALK_NONGAUSSIAN_CONTENT.md  (the locked content, slides S1–S19)
3. /mnt/home/tersenov/software/cnn_sbi/TALK_BEST_PRACTICES.md  (slide-design standard)
4. /home/tersenov/software/talks/CLAUDE.md  (repo + Preprint-theme conventions)
5. /home/tersenov/software/talks/NonGaussian_Universe_2026/README.md  (the existing BNT animation)

Key things the handoff will tell you, so you are not surprised:
- Use the repo's opt-in **Preprint theme** (scaffold from PREPRINT_TEMPLATE/); shared assets at the repo
  root referenced as ../assets/figures/<category>/…; preview from the repo root (npm start, open
  /NonGaussian_Universe_2026/); verify with tools/check-asset-links.py. I would like to use the light version of the Preprint theme.
- Two interactive components are ALREADY built in this folder and must be INTEGRATED, not rebuilt: the
  BNT intuition animation (bnt_explainer.*, = my ~4-5 min block) and the neural-summaries MSE→VMIM viz
  (neural_summaries.*, = slide S11). However, maybe you will need to slightly adapt them to fit the deck's Preprint theme and the slide layout.
- Hard rules: NO em-dashes in slide text; carry the honesty flags from the content doc §4 (M1 is ~7% matched-NDE not
  +15%; the CNN+BNT→baryon-robustness line is forward-looking; do not merge Paper I and II into one FoM
  ladder; always show marginals with FoM3; never present the historical inflated numbers as results).
- The content is the full ~30 min version (19 slides + the animation block); there is a documented trim
  path to ~25 min. Build the full version and mark the trims.

Do NOT start building yet. First read everything above, then write me a short build plan: the deck
scaffold approach, the figure-transfer list (the p1_*/p2_* figures live in the cnn_sbi repo's
talk_figures/ and need to come into ../assets/), the slide-by-slide asset mapping, and where the two
existing components slot in. Wait for my sign-off on the plan before you build.
