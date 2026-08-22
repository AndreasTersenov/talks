# SPEAKER SCRIPT — COSMO-26, Leiden

**15 min + 3 for questions.** The script is 2,186 words. That is **15:37 at 140 words per minute**
and **14:34 at 150**, so where it lands depends on a rate you will not know until you have rehearsed
it once. Much of the room works in a second or third language, so 140 is the rate worth aiming for
— which means **plan on making the first tier of cuts below**. Do not decide that from reading; run
it timed, then cut.

Every number below traces to `PAPER_FACTS.md` and was re-checked against the paper sources on
2026-08-22. Read `../docs/TALK-GUIDELINES.md` §6 before the first rehearsal.

**How to use this.** The prose is what you say, not a paraphrase of it. Rehearse it out loud once
without timing, fix whatever your mouth refuses to say, then rehearse timed. The wording will drift
after that, which is fine — the sentences that matter are marked **▲ land this**, and those should
survive verbatim, because they are the ones carrying a claim you do not want to soften on the day.

`[CLICK]` marks a fragment advance. `〔stage〕` is a direction, never spoken.

---

## 1 — Title · 0:49

〔Face the room. Do not look at the screen — you know what it says.〕

Thanks very much. I'm Andreas Tersenov, a PhD student at FORTH in Crete and the CosmoStat lab at
CEA Paris-Saclay. This is work with Sacha Guerrini, Jean-Luc Starck and Martin Kilbinger, across two
papers, and both should be on arXiv in September.

Stage IV surveys, Euclid first among them, will measure the lensing field with unprecedented
precision. Exploiting that fully takes statistics that go beyond two-point functions and Gaussian
likelihoods. And it takes them in a regime that is systematics-limited rather than
statistics-limited, where the work is controlling astrophysical and instrumental effects subtle
enough to bias the answer without anyone noticing.

**▲** Those two things pull against each other, and that is where this talk starts.

---

## 2 — The problem, and two questions · 1:28

〔Turn to the schematic and orient the room to the axes, then turn back. This is the one slide where
turning around is licensed.〕

In order to be able to trust our HOS results, we need to carefully investigate how they are affected by systematics, on the contour level.

And here is the tension. Angular scale runs along the bottom: large linear scales left, small non-linear scales right.

The first curve is the non-Gaussian information beyond the two-point function. It grows towards
smaller scales and peaks somewhere in the middle. The second is roughly how our small-scale
systematics behave, baryonic feedback above all: gas pushed around by AGN and supernovae. Negligible
on large scales, then rising steeply on exactly the scales we want.

Modelling them is an active area, but not yet reliable enough to trust, so the standard response is
to cut those scales. The shaded band is how far the cut has to reach. [CLICK] If we are lucky it is the narrow one and we keep most of the
signal. If we are not, it is the wide one, and the question becomes whether anything is left at all.

〔Pause. Then, more slowly — these two sentences set up the first half of the talk.〕

So, two questions. **▲** First: how much does unmodelled feedback bias higher-order statistics, and
how does that get worse as surveys get bigger? Second: once those scales are cut, is there anything
left to gain over the power spectrum?

---

## 3 — The two statistics · 0:56

〔Do not read the band labels off the figure — it is a thesis illustration at a finer pixel scale
than our analysis, and its arcminute numbers are not ours.〕

In this work, we focus on two families of statistics, both built on the same multi-scale decomposition. We take the convergence map and using the
starlet wavelet transform write it as a
sum of band-pass images, each carrying structure of a characteristic angular size. 
<!-- We use the four finest bands, roughly ten to eighty arcminutes. -->

[CLICK] On each band we can count peaks: local maxima of the signal-to-noise field, binned by
height. It's been shown to be very sensitive, but it keeps only a subset of the field, the discrete features.

[CLICK] The ℓ1-norm generalises that. Instead of counting maxima in a signal-to-noise bin, we sum
the absolute values of every coefficient in it. S-j-i is just the coefficients at scale j whose
signal-to-noise falls in bin i. Every pixel contributes, voids as well as peaks, and there is no
feature-detection step to tune. 

---

## 4 — The inference pipeline · 0:45

〔The animation runs on clicks; keep talking over it and do not wait for it.〕

To answer those two questions we need a way from maps to posteriors that assumes no likelihood, and
the same way for every statistic. So, simulation-based inference. We take the cosmoGRID convergence
maps at known cosmologies, add shape noise and masks, apply the wavelet transform, and measure each
statistic. That data vector conditions a normalising flow, which gives us the posterior.

The implementation is our own, in JAX: neural posterior estimation with a conditional masked
autoregressive flow, trained to maximise the log-probability of the true parameters.

Every posterior in this talk has been verified calibrated, with TARP and SBC. I have the coverage
plots in backup.

---

## 5 — How bad is the bias · 1:16

cosmoGRID gives us each realisation twice, with and without baryonic feedback. So we train the flow
on the dark-matter-only maps, which is the case of having no baryon model at all, then feed it a
baryonified map and watch how far the posterior moves.

〔Turn, name the axes, turn back.〕

That shift, in sigma, is on the y-axis, survey area on the x. And it grows with area, not because
the bias grows but because the error bars shrink, so the same systematic becomes more significant.

[CLICK] At Stage IV, fourteen thousand square degrees, the power spectrum is off by 2.2 sigma, and
both wavelet statistics by 3.6. [CLICK] At full sky the power spectrum passes three and a half, and the higher-order statistics go beyond six.

[CLICK] Two things. The higher-order statistics are the more biased, as you would expect, since
they live on the contaminated small scales. And all of this is at full map resolution. No cuts yet.

[CLICK] And on the right, what that looks like in the contours: the power-spectrum posterior
tightening and marching away from the truth as the area grows.

---

## 6 — What the cut costs · 1:06

So we cut, deriving the cut separately at each survey area, with the criterion that the bias comes
below 0.3 sigma.

[CLICK] For the power spectrum that means a sliding ℓmax: 860 at two thousand square degrees,
falling to 340 at full sky. At Stage IV and beyond, more than half the multipole range goes.

[CLICK] For the wavelets, the contamination concentrates in the single finest band, so dropping
j equals one is enough at every area. 

〔Slow down here. This is the honest-broker moment and it buys you credibility for the rest of the
talk.〕

**▲** But one important point. The two cuts are not the same kind of object. The power spectrum's
can be tuned to keep exactly what is safe at each area. Our wavelet bands are dyadic, so whole-band
removal is the only cut available to us, and at smaller footprints that is overkill: we are
certainly discarding clean information. The wavelet cut is the coarser instrument here. That is
fixable, and fairly easily, we just did not do it in this study.

---

## 7 — First answer · 0:59

Which brings us to the second question: whether anything is left to gain over the power spectrum
once the cuts are applied. These are the Stage IV posteriors, baryon-safe scales only. Power
spectrum first. [CLICK] Peak counts. [CLICK] And the ℓ1-norm.

**▲** On those scales the ℓ1-norm reaches a figure of merit 1.8 times the power spectrum's. At full sky (because of the better-adjusted wavelet cut), 2.6.

[CLICK] Peak counts are not as good, but they still carry plenty of complementary information: their
degeneracy directions in the w0 planes differ from the power spectrum's.

[CLICK] So higher-order statistics are not only deep-non-linear probes. The signal survives on
quasi-linear scales with no baryon model at all. And this is a floor: our cut is not
optimised, and as feedback modelling improves the analysis moves back into the non-linear regime,
where the gain is larger.

---

## 8 — The second question · 1:10

〔Do not put this question on the room cold. The two sentences that set it up are doing the work;
give them time.〕

So the ℓ1-norm survives the cut, and on baryon-safe scales it comfortably beats the power spectrum.
But beating the power spectrum is a low bar for a non-Gaussian statistic. **▲** The question I
actually care about is how much of the information in these maps we are getting at all: whether the
ℓ1-norm is close to everything that is there, or leaving a lot behind.

For a non-Gaussian field there is no analytic answer to that. What we do have is where much of the
field has been moving anyway: train a neural network to compress the maps, with an objective that
makes the summary optimal by construction.

[CLICK] Which cuts both ways. It hands us something to measure against. **▲** And it raises a fair
question: if a learned summary is already optimal, why hand-build a statistic at all? Except that
the optimality claim is nearly always made against the power spectrum, and hardly ever against a
strong hand-crafted higher-order statistic. So we tested it.

---

## 9 — The benchmark · 0:42

The compressor we test against is a convolutional network trained with VMIM, inside the same SBI
pipeline. It reads the four tomographic maps and returns a ten-dimensional summary. Network and flow
are trained together, and the pair is rewarded whenever the flow puts high probability on the true
parameters.

That objective is a variational lower bound on the mutual information between the summary and the
parameters. **▲** So in principle this compressor extracts everything the maps make accessible,
which is exactly why it is worth measuring against: it is a ceiling, not one more statistic in
the pile.

---

## 10 — Making it a fair fight · 0:25

The comparison has to be fair, so: the same maps, the same flow, the same compressed dimensionality, both arms verified calibrated. The only thing that changes is the summary.

Flat-sky ten-degree patches. Three hundred and twenty-four thousand of them, across eight hundred
and ninety-nine cosmologies, so if a gap shows up it is the compressor and not data scarcity.

---

## 11 — The gap · 0:42

First result. In grey, the ℓ1-norm measured on the four tomographic maps. [CLICK] In blue, the
network. The network is ahead, by thirty-six percent in the figure of merit.

〔Read the result plainly. Do not editorialise about the network being better, and do not yet claim
to know why.〕

Now, the comparison is a bit unfair, because the two are not reading the same thing. The network
takes all four maps together from its first convolutional layer; the ℓ1-norm is measured one bin at
a time. And the bins do carry correlated information, since the lensing kernels overlap while the
shape noise is independent. A per-channel statistic never sees it.

**▲** So let's try to close the asymmetry and find out.

---

## 12 — Two routes · 1:37

One way to capture it is to build the missing channel. For each pair of bins, multiply the two maps
pixel by pixel: the product lights up only where both have structure in the same place. Six pairs,
six new channels, the same ℓ1-norm on each, appended to the data vector. A convolution gives a
second flavour.

[CLICK] The other route leaves the maps alone and changes what the statistic reads. Take one wavelet
scale. At every pixel you have four numbers, one per redshift bin, and the per-bin ℓ1-norm
histograms each of them separately. That is literally what the two curves on the edges of this
figure are.

〔This is the sentence the slide exists for. Slow down, and point at the two edge curves as you say
it.〕

**▲** But two separate histograms can never tell you whether the bins are large in the same places.
It is the same gap as between two auto-spectra and the cross-spectrum: knowing each field on its own
does not tell you how the two vary together. That lives in the plane, not in the margins.

[CLICK] So we use the plane. Lay a fixed grid over it, drop every pixel into the cell its pair of
coefficients points at, and add up the ℓ1 weight landing in each cell. That is the joint ℓ1-norm.

[CLICK] **▲** And that is what separates it from a cross-map, which collapses each pair into a
single field before the statistic is taken. The joint ℓ1-norm never collapses anything.

---

## 13 — The tie · 0:29

Here is what that buys. Auto-only ℓ1-norm. [CLICK] Add the product cross-maps. [CLICK] The joint
ℓ1-norm. [CLICK] And the CNN, which lands on top of it.

〔Pause before the number. This is the headline of the talk.〕

**▲** 3371 against 3326. What that means is that both summaries appear to saturate the information
these maps make accessible. And since VMIM estimates the ceiling, a hand-built statistic reaching it
is a statement about sufficiency.

[CLICK] It holds on every parameter, over nine thousand mock observations.

〔Off-budget. Say it only if you are running early, or if a hand goes up before you finish:〕
If you are wondering whether we simply
trained the network badly — getting it this good took an expressive flow and a residual
architecture, and the deeper networks overfit at 899 cosmologies. It is at its optimum.

---

## 14 — The third question · 1:08

One more question, and it comes back from the baryon half of the talk.

Scale cuts are partly so expensive because lensing projects a whole range of physical scales onto
each angular scale, so an angular cut is not a cut in physical scale. Nulling approaches like BNT
repair that: linear combinations of the tomographic bins, chosen so the kernels become narrow and
localised in distance. Then a cut can go only where the systematic is.

On the power spectrum it works. We gain about a factor 1.4 in figure of merit at Stage IV, by
cutting only the bin that needs it.

[CLICK] But applied to higher-order statistics, by us and by others, it does this instead. The blue
contours are the ℓ1-norm in the nulled basis. They balloon.

〔Let that sit for a beat before you explain why it is strange.〕

**▲** And that should be impossible. BNT is a fixed, invertible transform. No information can have been lost.
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

## 16 — Conclusions · 0:54

Three questions, three answers.

Does baryonic feedback put the non-Gaussian information out of reach? No. Cut every contaminated
scale and the ℓ1-norm is still 1.8 times tighter at Stage IV, 2.6 at full sky.

Do we need deep learning to extract it? No. Read the bins jointly and a fixed wavelet statistic
matches a compressor trained to be optimal, with no training and a data vector you can inspect.

Can nulling then be used with higher-order statistics? Yes, provided the summary reads the bins
jointly. The inflation was the frame, not lost information.

**▲** What is left to the network is the genuinely three- and four-bin structure a pairwise
statistic cannot reach.

[CLICK] Both papers are on the screen, and both go on arXiv in September. Thank you.

〔Stop. Do not add a coda. Take the applause and turn to the chair.〕

---

# Cut lines

Calibrated to this version of the script. Rehearse the tiers so that running long degrades in an
order you chose, rather than by panic on the day.

**Tier 1 — recovers about 1:00, and takes the script to 14:00.** Expect to need this.

- **§10 folds into §11** (−0:25). Drop the slide's own paragraph and open §11 with: *"Same maps, same
  flow, both calibrated, three hundred thousand patches across nine hundred cosmologies — the only
  thing changing is the summary."* The slide stays up while you say it.
- **§4, the implementation sentence** (−0:12). "The implementation is our own, in JAX…" is backup
  material; nobody has asked for it yet at minute four.
- **§5, the closing [CLICK]** (−0:11). The contour panel makes the same point the curve just made.
  Let the figure carry it silently.
- **§12, "A convolution gives a second flavour"** (−0:05). It is a footnote to a route you are
  about to argue against.
- **§7, the floor paragraph** (−0:10), trimmed to: *"and this is a floor — our cut is not optimised,
  and better baryon modelling moves the analysis deeper into the non-linear regime."*

**Tier 2 — a further 0:45, taking it to 13:15.** If tier 1 left you still over at the second timed
run.

- **§2, the two-question block** (−0:15). The questions are on the slide; point at them rather than
  reading them, and say only *"so, two questions"*.
- **§6, the honest-broker paragraph** (−0:20) down to one sentence: *"and to be fair, the wavelet
  cut is the coarser instrument here, not the better one — that is fixable, we just did not do it."*
- **§14, the 1.4 result** (−0:10). It is Paper I's positive BNT result, but the slide is about the
  negative one.

**Tier 3 — a further 1:00, taking it to 12:15.** Only if the session is running late and the chair
has asked.

- **§12 down to route two only** (−0:35). Say the obvious fix is an explicit cross-map per pair, that
  it helps, and that the better answer was to change the statistic. The cross-map panel stays on
  screen and you talk over it.
- **§15, the counter-intuition paragraph** (−0:12).
- **§3, the peak-count paragraph** (−0:13). Peaks then appear only on §7's figure, which is enough.

**Never cut** §7, §13 or the last two paragraphs of §15. They are the three answers the talk exists
to deliver.

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
