# SPEAKER SCRIPT — COSMO-26, Leiden

**15 min + 3 for questions. This script runs 14:07, so it lands a minute early.**
Word count is 1976, which is 14:07 at a deliberate 140 words per minute. Much of the room
works in a second or third language; the pace is part of the plan, not a shortfall.

Every number below traces to `PAPER_FACTS.md` and was re-checked against the paper sources on
2026-08-22. Read `../docs/TALK-GUIDELINES.md` §6 before the first rehearsal.

**How to use this.** The prose is what you say, not a paraphrase of it. Rehearse it out loud once
without timing, fix whatever your mouth refuses to say, then rehearse timed. The wording will drift
after that, which is fine — the sentences that matter are marked **▲ land this**, and those should
survive verbatim, because they are the ones carrying a claim you do not want to soften on the day.

`[CLICK]` marks a fragment advance. `〔stage〕` is a direction, never spoken.

---

## 1 — Title · 0:32

〔Face the room. Do not look at the screen — you know what it says.〕

Thanks very much. I'm Andreas Tersenov, from CEA Paris-Saclay and the University of Crete.

Stage IV lensing — Euclid, Rubin, Roman — will be limited by systematics rather than by statistics.
Most of what those surveys carry that a power spectrum cannot see sits on small scales. So does the
astrophysics we cannot model. This talk is about how much of that information we can actually keep,
and about what it takes to extract it.

---

## 2 — The problem, and two questions · 1:14

〔Turn to the schematic and orient the room to the axes, then turn back. This is the one slide where
turning around is licensed.〕

Here is the tension, schematically. Angular scale runs along the bottom: large linear scales on the
left, small non-linear scales on the right.

The first curve is how much non-Gaussian information there is beyond the two-point function. It
grows towards smaller scales and peaks somewhere in the middle. The second curve is baryonic
feedback — gas pushed around by AGN and supernovae. Negligible on large scales, then rising steeply
on exactly the scales we want.

We cannot model that reliably, so the standard response is to cut those scales. The shaded band is
how far the cut has to reach. [CLICK] If we are lucky it is the narrow one and we keep most of the
signal. If we are not, it is the wide one, and the question becomes whether anything is left at all.

〔Pause. Then, more slowly — these two sentences set up the first half of the talk.〕

So, two questions. **▲** First: how much does unmodelled feedback bias higher-order statistics, and
how does that get worse as surveys get bigger? Second: once those scales are cut, is there anything
left to gain over the power spectrum?

---

## 3 — The two statistics · 1:01

〔Do not read the band labels off the figure — it is a thesis illustration at a finer pixel scale
than our analysis, and its arcminute numbers are not ours.〕

Two statistics, both built on the same decomposition. We take the convergence map and write it as a
sum of band-pass images, each carrying structure of a characteristic angular size. That is the
starlet wavelet transform. We use the four finest bands, roughly ten to eighty arcminutes.

[CLICK] On each band we can count peaks: local maxima of the signal-to-noise field, binned by
height. Well established, and it keeps only a subset of the field, the discrete features.

[CLICK] The ℓ1-norm generalises that. Instead of counting maxima in a signal-to-noise bin, we sum
the absolute values of every coefficient in it. S-j-i is just the coefficients at scale j whose
signal-to-noise falls in bin i. Every pixel contributes, voids as well as peaks, and there is no
feature-detection step to tune. **▲** That is the statistic I will follow for the rest of the talk.

---

## 4 — The inference pipeline · 0:26

〔The animation runs on clicks; keep talking over it and do not wait for it.〕

Everything goes through simulation-based inference. We take the cosmoGRID simulations, convergence
maps at known cosmologies, add shape noise, measure the statistic, and use that data vector to
condition a normalising flow which gives us the posterior. No likelihood assumption anywhere.

Every posterior in this talk has been verified calibrated, with TARP and SBC. I have the coverage
plots in backup.

---

## 5 — How bad is the bias · 1:02

cosmoGRID includes a baryon correction model, so we can take the same map with and without
feedback, push both through that pipeline, and measure how far the inferred parameters move.

〔Turn, name the axes, turn back.〕

That shift, in sigma, is on the y-axis. Survey area on the x-axis. And it grows with area — not
because the bias itself grows, but because the error bars shrink, so the same systematic becomes
more significant.

[CLICK] At Stage IV, fourteen thousand square degrees, the power spectrum is off by 2.2 sigma, and
both wavelet statistics by 3.6. [CLICK] At full sky the power spectrum passes three and a half, and
the higher-order statistics go beyond six.

[CLICK] Two things. The higher-order statistics are the more biased, which is what you would expect
since they live on the contaminated small scales. And all of this is at full map resolution, ℓmax of
1024. No cuts yet.

---

## 6 — What the cut costs · 1:06

So we cut. The criterion is to bring the bias below 0.3 sigma, and we derive the cut separately at
each survey area.

[CLICK] For the power spectrum that means a sliding ℓmax: 860 at two thousand square degrees,
falling to 340 at full sky. At Stage IV and beyond, more than half the multipole range goes.

[CLICK] For the wavelets, the contamination concentrates in the single finest band, so dropping
j equals one is enough at every area.

〔Slow down here. This is the honest-broker moment and it buys you credibility for the rest of the
talk.〕

**▲** I want to be careful here, because it is tempting to read that as the wavelets doing better.
The two cuts are not the same kind of object. The power spectrum's can be tuned to keep exactly what
is safe at each area. Our wavelet bands are dyadic, so whole-band removal is the only cut available,
and at smaller footprints we are certainly discarding clean information. The wavelet cut is the
coarser instrument, and therefore the conservative one.

---

## 7 — First answer · 1:11

Which brings us to the first answer. These are the Stage IV posteriors on baryon-safe scales only.
Power spectrum first. [CLICK] Peak counts. [CLICK] And the ℓ1-norm.

**▲** On those scales the ℓ1-norm reaches a figure of merit 1.8 times the power spectrum's. At full
sky, 2.6.

[CLICK] Peak counts sit much closer to the power spectrum, about parity at Stage IV. I would not
read that as peaks being a weak statistic. Part of it is the cut: whole-band removal costs the peaks
more than the sliding ℓmax costs the power spectrum, and most where that cut is loosest. And their
degeneracy directions in the w0 planes differ, so they still carry something a joint analysis
would use.

[CLICK] So higher-order statistics are not only deep-non-linear probes. The signal survives on
quasi-linear scales with no baryon model at all. And this is a floor twice over: our cut is not
optimised, and as feedback modelling improves the analysis moves back into the non-linear regime,
where the gain is larger.

---

## 8 — The second question · 0:45

〔This question is generated by the answer you just gave. Do not ask it earlier.〕

So the ℓ1-norm survives the cut. But that raises the obvious objection, and it is the one I would
raise myself. The summary statistic is the unknown box in the middle of that pipeline, and
increasingly people fill it with a neural network trained to compress the maps. Those compressors
are usually described as near-optimal. **▲** If that is true, why hand-build a statistic at all?

[CLICK] The honest answer is that the optimality claim is almost always demonstrated against the
power spectrum, which any non-Gaussian summary already beats. Against a strong hand-crafted
higher-order statistic, under matched conditions, it has not really been tested. So we tested it.

---

## 9 — The benchmark · 0:36

The compressor we test against is a convolutional network trained with VMIM. It reads the four
tomographic maps and returns a ten-dimensional summary. Network and flow are trained together, and
the pair is rewarded whenever the flow puts high probability on the true parameters.

That objective is a variational lower bound on the mutual information between the summary and the
parameters. **▲** Which is why this is worth comparing against: it gives us an estimate of the
ceiling, rather than one more statistic in the pile.

---

## 10 — Making it a fair fight · 0:25

The comparison has to be fair, so: the same maps, the same flow, the same compressed dimension, both
arms verified calibrated. The only thing that changes is the summary.

Flat-sky ten-degree patches. Three hundred and twenty-four thousand of them, across eight hundred
and ninety-nine cosmologies, so if a gap shows up it is the compressor and not data scarcity.

---

## 11 — The gap · 0:53

First result. In grey, the ℓ1-norm measured on the four tomographic maps. [CLICK] In blue, the
network. The network is ahead, by thirty-six percent in the figure of merit.

〔Read the result plainly. Do not editorialise about the network being better, and do not yet claim
to know why.〕

Now look at how the comparison is set up, because the two are not reading the same thing. The
network takes all four maps together from its first convolutional layer. The ℓ1-norm is measured one
bin at a time. And the bins do carry correlated information — the lensing kernels overlap while the
shape noise is independent — so a per-channel statistic never sees it.

**▲** That is an observation about the setup, not a diagnosis. It might account for all of the gap,
some of it, or none. So let's close the asymmetry and find out.

---

## 12 — Two routes · 1:01

There are exactly two places to intervene. The input, or the statistic.

The obvious one is to build the missing channel: for each pair of bins, multiply the two maps pixel
by pixel. The product lights up only where both bins have structure in the same place. Six pairs,
six new channels, the same ℓ1-norm on each.

[CLICK] The second route leaves the maps alone. At a given scale each pixel gives both bins'
coefficients at once, and the per-bin ℓ1-norm sees only the one-dimensional histogram of each: the
two curves on the edges of this figure.

[CLICK] Lay a grid over the pair plane instead, and sum the ℓ1 weight in each cell. That is the
joint ℓ1-norm.

[CLICK] **▲** The difference is the point. A cross-map collapses each pair to a single field before
the statistic is taken. The joint ℓ1-norm never reduces it.

---

## 13 — The tie · 0:49

Here is what that buys. Auto-only ℓ1-norm. [CLICK] Add the product cross-maps. [CLICK] The joint
ℓ1-norm. [CLICK] And the CNN, which lands on top of it rather than above it.

〔Pause before the number. This is the headline of the talk.〕

**▲** 3371 against 3326. That is a tie, and I want to be precise about it. It is not a win: the
network's coverage is mildly conservative, which we expect accounts for the ℓ1-norm sitting a hair
above. What it does mean is that both summaries appear to saturate the information these maps make
accessible. And since VMIM estimates the ceiling, a hand-built statistic reaching it is a statement
about sufficiency rather than the result of a horse race.

[CLICK] It holds on every parameter, over nine thousand mock observations.

〔Off-budget. Say it only if you are running early, or if a hand goes up before you finish:〕
If you are wondering whether we simply
trained the network badly — getting it this good took an expressive flow and a residual
architecture, and the deeper networks overfit at 899 cosmologies. It is at its optimum.

---

## 14 — The third question · 1:05

One more question, and it comes back from the baryon half of the talk.

Scale cuts are expensive because lensing projects a whole range of physical scales onto each angular
scale, so an angular cut is not a cut in physical scale. The BNT transform repairs that: it takes
linear combinations of the tomographic bins so the kernels become narrow and localised in distance,
and then a cut can go only where the systematic actually is.

On the power spectrum that works. About a factor 1.4 in figure of merit at Stage IV, from cutting
only the bin that needs it.

[CLICK] Applied to the map-based higher-order statistics, it does this instead. The blue contours are
the ℓ1-norm in the nulled basis. They balloon.

〔Let that sit for a beat before you explain why it is strange.〕

**▲** And that should be impossible. BNT is a fixed, invertible matrix. Nothing can have been lost.
And yet the per-bin ℓ1-norm keeps sixteen percent of its figure of merit.

---

## 15 — What comes back · 1:09

So we ran the same four summaries through the nulled frame.

[CLICK] Per-bin ℓ1-norm: sixteen percent. [CLICK] Add one derived field per pair, the product
cross-maps: twenty-four. [CLICK] The joint ℓ1-norm, the statistic we built two slides ago:
seventy-two. [CLICK] And the network, which reads all four channels natively, is lossless within
the errors.

**▲** What a summary retains under the nulling tracks how jointly it reads the bins. The transform
correlates the shape noise across the maps, so the constraint stops sitting in any individual
channel and starts sitting in the structure across them. Which runs against intuition: nulling is
designed to de-correlate the bins, and joint reading matters more there, not less.

[CLICK] **▲** So nulling can be kept as a mitigation at no cost in constraining power, provided some
stage of the pipeline reads the bins jointly. And notice the power spectrum was the first rung of
this same ladder all along: it survives the transform only if you keep the cross-spectra between
transformed bins.

---

## 16 — Conclusions · 0:50

Three questions, three answers.

Does baryonic feedback put the non-Gaussian information out of reach? No. Cut every contaminated
scale and the ℓ1-norm is still 1.8 times tighter than the power spectrum at Stage IV, 2.6 at full
sky.

Do we need deep learning to extract it? No. Read the bins jointly and a fixed wavelet statistic
matches a compressor trained to be optimal, with no training and a data vector you can inspect.

Can nulling then be used with higher-order statistics? Yes, provided the summary reads the bins
jointly. The inflation was the frame, not lost information.

**▲** What is left to the network is the genuinely three- and four-bin structure a pairwise
statistic cannot reach. Thank you.

〔Stop. Do not add a coda. Take the applause and turn to the chair.〕

---

# Cut lines

Rehearse these so that running long degrades in a planned order instead of a panic.

**At 15:00 in rehearsal — drop ~1:00.** Cut the closing paragraph of §6 (the two cuts are not
like-for-like) down to one sentence: *"and to be fair, the wavelet cut is the coarser instrument
here, not the better one."* Cut the training-quality aside at the end of §13 and hold it for Q&A.

**At 16:00 — drop a further ~1:00.** Cut §10 entirely and fold it into one sentence at the head of
§11: *"same maps, same flow, both calibrated, so the only thing changing is the summary."* Cut the
counter-intuition paragraph in §15.

**At 17:00 — drop a further ~1:15.** Cut §12 to route two only: say that the obvious fix is to build
an explicit cross-map per pair, that it helps, and that the better answer was to change the statistic
instead. The cross-map panel stays on screen and you talk over it.

Do not cut §7 or §13. They are the two answers the talk exists to deliver.

---

# Q&A preparation

Rank ordered by how likely they are to come.

**"Isn't the tie just because your CNN is undertrained?"**
Getting the network to 3326 took a RealNVP flow rather than a simpler one, and a ResNet-18 rather
than a plain CNN. Deeper networks overfit at 899 cosmologies. Every retained choice is the best
performer of its own sweep, and the alternatives land within a few percent through the same flow. If
anything the comparison is generous to the network.

**"FoM₃ is a fragile summary in a degenerate parameter space."**
Agreed, which is why the marginals are in the paper alongside it: 0.044, 0.072, 0.223 for the joint
ℓ1-norm against 0.045, 0.072, 0.231 for the CNN. The per-mock violins are in backup — the point is
the overlap of the distributions, not the medians.

**"Is any of this robust to intrinsic alignments, photo-z, source clustering?"**
No claim there. This is a controlled methods study: one simulation suite, one baryon model, shape
noise only. What it establishes is a relative statement between summaries under matched conditions.
Real-world robustness needs the systematics work others in this session are presenting.

**"Why only pairwise? Why not read all four bins at once?"**
Because the patch cannot populate it. A four-dimensional histogram over K⁴ cells against 80×80
pixels is almost everywhere empty and its occupied cells are sampling noise. Two dimensions is the
highest joint dimension these patches fill densely, and the residual advantage the network keeps is
exactly the genuine three- and four-bin structure.

**"Your cross-maps are a construction. Couldn't you manufacture constraining power that way?"**
That is the right worry and it is why we build them patch-locally. A harmonic-space construction
draws on modes from beyond the patch and would credit a survey with information it cannot access.
We measured that effect: on the full sphere the cross channels carry 12 to 20 percent of their
variance at ℓ below 18, against 0.4 to 1 percent for the autos.

**"How does this compare with what Euclid is doing on BNT?"**
Vinciguerra et al. build tomographic maps for bin combinations up to quadruplets and keep the ones
that contribute, and their BNT contours for map-based higher-order statistics are still inflated
relative to the untransformed analysis. Our reading is consistent with that: what matters is whether
the summary reads the bins jointly, and a compressed selection of combinations need not.

**"Does the joint ℓ1-norm cost you in data-vector size or covariance?"**
Ten by ten cells, six bin pairs, four scales, compressed to ten dimensions before inference, exactly
as for the other summaries. Summing the ℓ1 weight in each cell rather than counting pixels is what
keeps it low-variance — it is a two-dimensional analogue of the ℓ1-norm, not a joint PDF estimate.

**"Second paper is not out yet?"**
In preparation. Happy to share a draft.

---

# Delivery notes for the day

- Practise the opening most. It is where the nerves peak and the part you can least afford to
  improvise.
- Say *measure*, *infer*, *obtain*. Not *get*. Under pressure you fall back on rehearsed habits, so
  build the right ones now.
- Green pointer, taken out of the bag before you start. Calm, deliberate strokes, one thing at a
  time.
- Face the room. Turn to the screen only to name axes on a new figure, then turn back.
- Silence beats "um". A pause after §14 is a gift to the room, and it lets you drink water.
- If you lose your place: pause, drink, resume. You can skip silently; nobody notices unless you
  announce it.
