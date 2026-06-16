# Speaker script: "Do Baryons Break Higher-Order Statistics?"
The Non-Gaussian Universe, FORTH Heraklion, Tue 16 Jun 2026, ~25 min.

This is what to say, slide by slide, in the deck's actual order. It is written to be spoken, not read.
Square brackets are stage directions (clicks, pointing, the animations). Numbers and framing match the
slides. Target ~25 min; the per-slide budgets sum to ~24, leaving slack.

## Delivery notes (read once)
- Pace: roughly 1 min per static slide, 1.5–2 min per animated one. If you run long, the first cuts are
  the BNT "2-point rule" animation (block 3) and the wavelet-peaks detail slide (S5b).
- Honesty guardrails to keep in the spoken words: the CNN beats the l1-norm by **~7%** (not 15), and
  **both are calibrated**; the "baryon-robust CNN+BNT" line is a **next step, not a finished result**;
  keep Paper I (full-sky, l1 ~3x the power spectrum) and Paper II (flat-sky, l1 ~ optimal CNN) as two
  separate statements, never one number.
- The BNT animation's recovery ladder (auto 0.15x, +cross 0.22x, CNN 0.93x, whiten 1.06x) is the
  raw intuition build; your headline numbers are the matched-NDE **0.26x / 0.96x** from the slide just
  before it, and whitening **1.06x**. Narrate the ladder qualitatively; quote the 0.26x/0.96x/1.06x.
- One person to name out loud: **Simone Vinciguerra** at the hinge ("I'll come back to this"), and pay
  it off at the conclusion. Tee up Wednesday's round table at the cost/benefit slide and the close.

---

## S1: Title  ("Can we trust higher-order weak lensing?")
[~45 s]

Good afternoon, and thanks for having me. The title on my abstract is "Do baryons break higher-order
statistics?", but let me put the real question on the table first, the one I think this whole meeting is
circling: **can we actually trust higher-order weak lensing?** Trust it enough to put it at the heart of
a flagship analysis. That is the thread through both halves of this talk. Part one is about baryonic
feedback, joint work with Sacha Guerrini, Martin Kilbinger and Jean-Luc Starck. Part two is about
learned versus analytical summaries, and whether we can believe either one's contours.

---

## S2: §0, the skeptic + the trust checklist
[~1.5 min]

Here is the situation. Everyone in this room is optimizing statistics: going to higher order, squeezing
more out of the field than the power spectrum can give. And yet, [gesture at the skeptic] the two-point
community is, let us say, not fully convinced.

[beat for the bubble: "I don't believe any of your contours."]

And honestly, they have a point. The flagship Stage-III and Stage-IV analyses are still run with
standard two-point statistics. Our beautiful higher-order results are still, for the most part, treated
as proofs of concept. So the question is not "can we compute another statistic." It is: **what would it
take to make higher-order statistics trustworthy enough to lead a flagship analysis?**

It is not one thing. It is a whole checklist that this community keeps raising. [gesture across the list]
Blinding. Robust covariance. Emulators. Systematics. Analytical cross-checks. The non-Gaussian
likelihood. Knowing the limits of each method. Null and validation tests. And simplicity.

I will not solve all of these today. But this talk takes several of them head-on, systematics, the
limits of each method, a validation standard, and simplicity, and, because everything I do is
simulation-based, two of these come for free: I never form a covariance, and I never assume a Gaussian
likelihood. You will notice this checklist is essentially the agenda for tomorrow's round table. Keep
that in mind; I will come back to it.

---

## S3: Part 1 divider  ("Do baryons break HOS?")
[~15 s]

So, part one. Baryonic feedback, the wavelet l1-norm, and a transform called BNT. Let me start with the
systematic that forces the whole issue.

---

## S4: §1, Stage IV is systematics-limited
[~1.5 min]

The headline of the last decade is that Stage-IV surveys are **no longer statistics-limited**. We will
have so many galaxies that the error bars are tiny. The bottleneck has moved: it is now **systematics**.

And before we trust any summary statistic, beyond-two-point especially, we have to quantify how each
systematic affects it, and crucially, at the **contour level**, on the actual inferred parameters, not
just on the data vector.

The sharpest small-scale systematic is **baryonic feedback**. [gesture at the Illustris movie] AGN and
supernovae push gas around and suppress matter on small scales, which is exactly where the constraining
power lives, and exactly where the feedback models disagree most with each other. So it both mimics a
cosmological signal and biases our inference.

That sets up the two questions for part one: first, how badly does unmodeled feedback **bias** our
non-Gaussian statistics? And second, if we make a safe scale cut to protect ourselves, do higher-order
statistics **still beat the power spectrum**? To answer them I use CosmoGrid simulations, four
tomographic bins, with paired dark-matter-only and "baryonified" maps, Euclid-like noise, and
simulation-based inference.

---

## S5: §1, higher-order statistic I: wavelet peak counts
[~50 s]

Let me introduce the two statistics I will use, quickly, because you all know them. The first is **peak
counts**. [point] You smooth the convergence map, define a signal-to-noise field, and count its local
maxima in bins of signal-to-noise. The high peaks trace the massive structures. It is simple and very
well established. Its one limitation: it only uses the high signal-to-noise peaks.

---

## S5b: §1, wavelet peaks via the starlet transform
[~40 s, droppable if long]

In practice we do this multi-scale, with the **starlet transform**: you write the map as a sum of
wavelet bands plus a coarse map, and count peaks scale by scale. A nice side effect is that each band
covers a different frequency range, so the peak-count covariance is nearly diagonal.

---

## S6: §1, higher-order statistic II: the starlet l1-norm
[~1 min]

The second statistic is the one I will lean on, the **starlet l1-norm**. [point at the formula] At each
scale and each signal-to-noise bin, you simply sum the absolute values of the wavelet coefficients.

The reason I like it: the l1-norm generalizes peak counts. Instead of keeping only the peaks, it uses
**every pixel**, the peaks and the voids, the whole convergence PDF, with no need to define a discrete
feature at all. It is, if you like, the analytical hero of this talk. And, foreshadowing, that "uses the
whole distribution" property is exactly why it will beat peaks in a moment.

---

## S7: §1, the inference pipeline (SBI animation)
[~1.5 min; let it animate, narrate over it]

How do we get from a statistic to a posterior? [start the animation] We take the CosmoGrid convergence
maps, add Euclid-like noise, apply the wavelet transform, and compute the summary statistic. Then,
because none of these statistics has a tractable likelihood, we do not write one down. We learn the
posterior directly: a normalizing flow, a conditional masked autoregressive flow, is conditioned on the
summary and trained to map a simple Gaussian into the posterior over cosmology, by minimizing the
negative log-probability of the true parameters. [let it finish] This is neural posterior estimation,
all in JAX. This same machine carries both halves of the talk.

---

## S8: §1, mitigation: scale cuts
[~1.25 min]

Now the systematics test. The criterion is simple: a mitigation is good enough if it brings the
baryonic bias below **0.3 sigma**. [click through the points]

For the power spectrum, you need an aggressive cut, down to multipoles below about 400, and that throws
away most of your signal. For the starlet l1-norm, something much nicer happens: the contamination is
**isolated in a single scale**, the finest wavelet band. So you just drop that one band, and you are
clean, across every survey area we tried. [point at the curve] And we do this as a function of survey
area on purpose, because more area means smaller error bars, which means you are more sensitive to any
residual bias.

---

## S9: §1, baryonic bias scales with survey area
[~1.25 min]

Here is why area matters so much. [point] As the survey grows, the bias in units of sigma grows with it.
At a Stage-IV area, around fourteen thousand square degrees, even the power spectrum already shows about
a two-sigma bias. At full sky, the tension exceeds three sigma for **every** statistic. And notice the
higher-order statistics are actually **more** biased than the power spectrum, which makes sense, they
live on exactly the small, baryon-contaminated scales. [gesture at the shifted contours] So this is not
a corner case. Unmodeled baryons will move your contours.

---

## S10: §1, are HOS still useful?  (the 3x result)
[~1.25 min]

So we make the cut. The natural worry is that once you protect yourself from baryons, you have thrown
away the non-Gaussian information and there is no point. That is **not** what happens. [point at the
contours] On the baryon-safe scales, the starlet l1-norm still gives constraints about **three times
tighter** than the power spectrum, in the full-sky limit.

That is the first real message of the talk: higher-order statistics are not just probes of the deep
non-linear regime. There is robust, usable non-Gaussian information at intermediate, quasi-linear
scales that feedback barely touches. And it is cheap to protect: one scale cut, no feedback model
required. [optional nod] This is also, by the way, one answer to the round table's model-versus-scale-
cuts question: the cut is robust and it is cheap.

---

## S11(Part1): §1, tomography (Zeghal flipbook)
[~1 min; click through the frames]

But could we do **better** than a single number per bin? This is where tomography comes in, and where I
want to plant an idea that the field has under-explored. [click through the flipbook] We slice the
source galaxies in redshift, and each slice gives us its own convergence map. [final frame] So we do not
have one map, we have a tomographic stack.

Here is the key point: the lensing kernels are **broad and they overlap**. A low-redshift structure
contributes to every higher bin. So the bins are not independent, they **share information**. The
community has worked very hard on which statistic to compute. It has spent much less effort on how to
optimally use these overlapping bins. That, the **optimal tomographic strategy**, is really what the
rest of this talk is about. And the natural tool for re-organizing the bins is the BNT transform.

---

## S12(Part1): §1, the BNT transform
[~1.5 min]

BNT, after Bernardeau, Nishimichi and Taruya, is a linear, **invertible** re-mixing of the tomographic
bins. [point at the kernels] On the left are the standard kernels: broad and overlapping, which means a
fixed angular scale mixes many physical scales and many redshifts together. On the right are the BNT
kernels: it subtracts weighted combinations of the lower bins to **null the low-redshift lensing
efficiency**, so each transformed field is localized to a thin slice in lens redshift.

Why do we care? Because that localization sharpens the mapping between angular scale and physical scale.
And for us specifically, it lets us isolate the low-redshift, small-scale systematics, the baryonic
feedback, into specific bins, and cut scales only where we need to, instead of throwing away data
everywhere. For the power spectrum this is essentially lossless. It sounds like exactly the tool we
want.

---

## S13(Part1): §1, THE HINGE: BNT inflates the HOS contours
[~1.5 min; this is the pivot, slow down]

And then you apply it to map-based higher-order statistics, and it backfires. [point at the gray
contours] The per-bin l1-norm contours **inflate dramatically**. The reason is that the same linear
mixing that nulls the signal also takes the originally independent shape noise in each bin and
**correlates** it, raising the noise floor.

Now here is the puzzle, and this is really the hinge of the whole talk. BNT is **invertible**. By
construction, no information can actually be lost. And yet a recent Euclid forecast, **Vinciguerra and
collaborators**, Simone, who speaks on Wednesday, found this same inflation persists for higher-order
statistics, even when you explicitly model the cross-bin components, and they concluded that recovering
the lost signal-to-noise is "highly non-trivial."

So which is it? Is the BNT information really lost for higher-order statistics, or are we just
**analyzing it wrong**? Hold that thought. Simone, I promise I will come back to it.

---

## S14: Part 2 divider
[~15 s]

That question takes us into part two: learned versus analytical summaries, whether we can trust them,
and the resolution of the BNT puzzle.

---

## S15: §2, Part 2 intro: learned summaries + the cliffhanger
[~1 min]

Part one gave us a strong **analytical** statistic, the l1-norm. The obvious next question, and one this
conference cares a lot about, is: how much better can a **learned**, supposedly optimal summary do?

By a learned summary I mean a neural network that compresses the convergence map directly into a handful
of numbers, instead of a hand-designed statistic. And we train it with VMIM, which I will unpack in a
second, so that it keeps as much cosmological information as possible. That is, in the technical sense,
the optimal learned compressor. So the two questions for part two are: is the learned summary actually
better, and, left over from part one, [beat] what on earth is going on with BNT?

---

## S16: §2, training a neural summary I: regression (MSE)
[~1 min; animation]

Let me show what "learned summary" means, because the choice of objective matters more than people
expect. The simplest idea is **regression**. [animate] You simulate parameters, render the map, push it
through a network, and ask the network to predict the parameters, minimizing mean-squared error.

The problem is what it learns. [point at the parameter-space plot] Mean-squared error pushes the
network's output to the **posterior mean**. And the moment the posterior is non-Gaussian or has a
degeneracy, the mean sits off the ridge, in a place no single cosmology actually predicts. You get a
point estimate, but a poor summary.

---

## S17: §2, training a neural summary II: VMIM
[~1 min; animation]

VMIM fixes this. [animate] Instead of predicting a number, you keep a low-dimensional **summary**, feed
it to a flow, and maximize the **mutual information** between the summary and the parameters, which in
practice means maximizing the expected log-posterior under that flow.

[point] Now the network is rewarded for preserving the **whole posterior shape**, the degeneracy
directions and all, with no Gaussian assumption. This is the objective that gives you the "optimal"
learned compressor, and it is what we put up against the l1-norm.

---

## S18: §2, the comparison, done fairly
[~1.25 min]

The comparison has to be fair, or it means nothing. [point at the schematic] So: the **same**
convergence maps go into either the l1-norm or the CNN. Both summaries then go through the **same** flow
density estimator, to a posterior. Same data, same inference machine, the only thing that changes is the
summary.

Two details that make this clean. We work on flat-sky ten-degree patches, which matters because it lets
us build cross-bin maps that are actually physical, not contaminated by full-sky leakage. And it is not
a question of undertraining: three hundred thousand patches, nine hundred cosmologies. The dataset is
ample, so if there is a gap, it is the summary's fault, not the data's. And both arms are calibrated,
which is the next slide.

---

## S19: §2, the headline (M1): l1 almost reaches the optimal CNN
[~2 min; the central Part-2 result]

Here is the central result of part two. [point at the contours] These are the posteriors from the
analytical l1-norm and from the optimal learned CNN, on the same data, through the same flow. They
**almost coincide**. [point at the FoM3 distribution] Across patches, the figures of merit are
near-identical: the CNN is ahead, but only by about **seven percent**.

Let me be precise, because this is the kind of claim that gets you in trouble. It is about seven
percent at the population level, and both summaries are calibrated. The reading is the strong one for
this room: a **hand-built, interpretable statistic essentially matches the optimal learned compressor**,
once you give them the same inference machine. The l1-norm, with a cross-bin term, is very nearly a
**sufficient** statistic for this problem.

[the referee aside, say it lightly] And before anyone thinks I just trained the network badly: getting
the CNN even to this point took real work, an expressive flow, the right architecture, and a large
dataset; a deeper network actually overfits at nine hundred cosmologies. So this is the CNN doing well.
The headline is still that the analytical statistic is right there with it.

[optional, to Heavens / the round table] This is one concrete data point for the round-table question of
optimal versus interpretable summaries: here, interpretable essentially **is** optimal.

---

## S20: §2, can we trust it? (calibration)
[~1.25 min]

But remember the whole framing: tight contours are worthless if they are wrong. So every arm has to
pass the same reliability battery. [point at the two panels] On the left, TARP coverage, varied over the
whole prior, sitting on the diagonal. On the right, simulation-based calibration, the rank histograms
flat within the band. Both the analytical and the learned summary pass the **same** tests.

So the constraining power I just showed you is **real**, not an artifact of an over-confident posterior.
And this is, again, a concrete proposal for the round table's question of what the minimum validation
standard should be: the same coverage and calibration battery, applied to every statistic, hand-built
or learned, no exceptions.

---

## S21: §2, BNT revisited (M3 quantitative)
[~1.5 min]

Now I can finally come back to the BNT puzzle, with both summaries, through that same fair inference
machine. [point at the corners] Same transform, opposite fates.

The per-channel l1-norm **collapses**: its figure of merit drops from about three thousand to under
eight hundred, a factor of about **0.26**, and the sigma-8 error roughly doubles. The channel-mixing
**CNN is essentially lossless**: 0.96, basically unchanged. And, importantly, that l1 collapse is itself
**calibrated**. The wide contours are not a bug, they are an honest report of a real information loss in
that representation.

So the gap here is **not** the inference machine, we are using the same one. The gap is the
**representation**: a per-channel statistic versus a summary that mixes the bins. Why does mixing the
bins make all the difference? That deserves a picture, not an equation.

---

## S22: BNT block 1: the rotating cloud (frame intuition)
[~1.5 min; click through the 5 acts]

[Act 1] Think of all the information in your maps as a fixed cloud of points. The l1-norm is a kind of
**shadow** of that cloud, its projection onto a measuring axis. The cloud is stretched along a deep,
common mode shared across the bins, with a non-Gaussian tail, so the shadow is rich.

[Act 2] Now apply BNT. BNT does **not** touch the cloud. It rotates the **measuring axes**, off that
deep common mode and onto thin, signal-poor slices. [point] The shadow goes nearly blank. The meter
collapses. But the cloud has not moved.

[Act 3] So where did the information go? Into the cloud's **shape**, the relations between the maps. No
single-map histogram, in this frame, can see it.

[Act 4] What does the CNN do differently? It **mixes the channels first**. It effectively draws its own
measuring axis back along the cloud, undoing BNT for free. So it is not smarter, it is **basis-robust**.

[Act 5] And to prove the information was never lost: one fixed **whitening** rotation takes you to a
different, clean frame, and the shadow comes right back, full recovery. The collapse was never about
lost information. It was about the **frame**.

---

## S23: BNT block 2: signal and noise (mechanism)
[~1.5 min; click through; narrate the ladder qualitatively]

The same story, now with the signal and the noise made explicit. [Act 1-2] The bins share one deep,
redundant common signal. BNT differences them, which scatters that common signal into thin slices, and
at the same time turns the independent noise into **amplified, correlated** noise. [point at the
covariance morphing] That is the double hit the per-map l1-norm suffers.

[the ladder] And you can watch the recovery climb. [point] The auto-only l1 collapses the most. Adding
the explicit cross channel only **half** helps, because a per-channel statistic can only read part of
the joint structure. The CNN, by un-mixing the bins, climbs almost all the way back. And the whitened
frame recovers it completely. [land it] The lesson: the information is sitting in the cross-bin
relations, and you only get it back if your summary can **mix the bins**.

---

## S24: BNT block 3: what survives BNT (the 2-point rule)
[~1 min; droppable if short on time]

One last piece, for the precise among you. [point] At the two-point level there is a clean rule. The
full auto-plus-cross spectrum matrix transforms as B C B-transpose, and because B is invertible, that is
**exactly** recoverable: the auto and cross power spectra together are invariant under BNT. But if you
keep only the **diagonal**, auto-only, you cannot invert back. That is the two-point shadow of the same
effect: keep the cross-information and BNT costs you nothing; throw it away and it does.

---

## S25: §2, is the +7% worth it? (the honest verdict)
[~2 min; the most memorable beat, do not rush]

So let me be honest with you, because I think this is the most useful thing I can say before tomorrow's
panel. The CNN beats the analytical l1-norm by about **seven percent**, both calibrated. Is that worth
it? [let it sit]

Here is what that seven percent cost me. [point at the cost pan] An extensive architecture and
hyperparameter search. A very large dataset, and the strong VMIM compressor in particular needs that
scale or it **biases**. And worse, along the way the network kept finding **unphysical shortcuts**:
information in the geometry of how I cut the patches, in the **mean** of the maps, the mass-sheet mode,
and, with twenty-degree patches, projection features that depend on where the patch sits on the sky. All
of these tighten the contours, and **none of them would exist in real data**.

And here is the part that should worry everyone in this room: those failures **largely passed TARP and
SBC**. The contours looked beautifully calibrated, and they were still wrong. The l1-norm has none of
this. It is simple, it is interpretable, you can go back and look at the data vector and understand it.
The CNN is powerful, but it is treacherous.

So my honest answer for the panel: for that seven percent, on its own, I am not sure it is worth the
cost and the risk. Where the CNN clearly **does** earn its keep is BNT, the channel-mixing win, where it
recovers information a per-channel statistic structurally cannot. And the sharp version of the panel's
own question: if a neural statistic passes every validation test, should we trust it? My finding is that
some failure modes **pass every test and are still wrong**. So "passes the tests" cannot be the whole
bar.

---

## S26: §3, conclusion: do baryons break HOS? No.
[~1.5 min; land all three, then loop back]

So, back to the title. **Do baryons break higher-order statistics? No.** Three things to take away.

[Part 1] On baryon-safe scales the non-Gaussian information survives, and the l1-norm beats the power
spectrum by about three times, cleaned with a single scale cut.

[Part 2] The hand-built, interpretable l1-norm **nearly matches** the optimal learned summary, within
about seven percent, and both are calibrated. Interpretable is, essentially, optimal.

[the twist] And the apparent BNT "break" is a **frame artifact**: a channel-mixing compressor, or a
single fixed rotation, recovers everything. Simone, that is the answer to the puzzle, recovering the SNR
is not highly non-trivial, it is one rotation, as long as your summary uses the cross-bin information.

Where this points, and I will flag this clearly as a **next step**, not a finished measurement, is a
baryon-robust, non-Gaussian SBI that keeps BNT's clean per-bin scale cuts without paying the
contour-inflation tax. The to-do list is on the slide: a physical flat-sky cross for the CNN, an
end-to-end CNN-plus-BNT mitigation demo, and calibration at Stage-IV scale.

And to close where I opened: these are exactly tomorrow's round-table questions, optimal versus
interpretable, physics-based versus learned, what the validation standard should be. I have tried to
give you one honest data point on each. Thank you, to Sacha, Jean-Luc, Martin, to CosmoGrid, and to
Justine Zeghal's Learn2Map, and I am happy to take questions.

---

## Backup (for Q&A)
Have these ready; do not present them in the main flow.
- **Cross-maps / M2:** the kappa_i kappa_j product map (whose mean is the cross-correlation) adds about
  +20% to the l1-norm; a convolution adds nothing; and the old full-sphere 4x gain was ~92% full-sky
  leakage, so we use only the physical flat-sky arms. (Use if asked "did you try explicit cross-maps.")
- **The whitening clincher slide:** the explicit 1.06x recovery figure, if someone wants the number
  behind the animation.
- **The before/after BNT maps:** the visible SNR blow-up, if someone doubts the noise-mixing mechanism.
- **The one-story / problem-resolution pair:** if you want to restate the synthesis visually.
- **Likely questions:** systematics you did not model (IA, source clustering, photo-z) -> "controlled
  methods comparison; real-world robustness needs exactly the work several of you are presenting"; FoM3
  fragility -> "that is why I show the marginals and the full distribution, not a single number"; why
  the CNN at all if l1 matches -> "BNT, and the fact that on raw maps you do not know the sufficient
  statistic in advance."
