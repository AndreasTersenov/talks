# SPEAKER SCRIPT — COSMO-26, Leiden

**15 min + 3 for questions.** 

---

## 1 — Title 

Thanks very much. I'm Andreas Tersenov, a PhD student at FORTH in Crete and the CosmoStat lab at CEA Paris-Saclay. This is work with Sacha Guerrini, Jean-Luc Starck and Martin Kilbinger, across two papers, and both should be on arXiv in September.

<!-- So to set up the scene: we all know Stage IV surveys, Euclid first among them, will measure the lensing field with unprecedented precision. Exploiting that **fully** needs statistics that go beyond two-point functions (so HOS) and beyond Gaussian likelihoods. 
We're also moving from a regime that is 
statistics-limited into one that is systematics-limited, where the work is controlling astrophysical and instrumental effects that can bias the inference. -->

<!-- **▲** Those two things pull against each other, and that is where this talk starts. -->

---

## 2 — The problem, and two questions 

So to set up the scene:
As we all know, in WL fields a big part of the information is not gaussian, and therefore not captured by 2pt statistics. So in the community we proliferate HOS and show amazing results with them, in terms of information gain. However...

In order to be able to trust any of our HOS results, we need to know exactly how they are affected by systematics, at the level of the cosmological contours.

And here on this schematic figure you can see the issue. 

The blue curve is the non-Gaussian information beyond the two-point function. It grows towards smaller scales, as the field becomes more non-Gaussian. 
The gray curve is roughly how our small-scale systematics behave, for example, baryonic feedback: gas pushed around by AGN and supernovae. On large scales it's negligible, but then it rises steeply on exactly the scales we want to use with HOS.

Modelling baryons is an active area, but not yet reliable enough to trust, especially for HOS (with many significantly different alternative models), so the standard response is to cut those scales. The question is how far that cut has to reach.

So we kinda have two scenaria. 
[CLICK] If we are lucky, only the smallest scales are affected. We cut them and most of the non-Gaussian information is still there. [CLICK] But what if the contamination reaches much further, and once it is cut there is nothing beyond-Gaussian left worth having?

So, two questions. **▲** First: how does unmodelled feedback bias higher-order statistics;
and once those scales are cut, is there anything left to gain over the power spectrum?

---

## 3 — The two statistics 

In this work, we focus on two families of statistics, both built on the same multi-scale decomposition. 
The basic idea is that we take the weak lensing map and using the starlet wavelet transform decompose it into a sum of band-pass images, each carrying structure of a characteristic angular size. 
<!-- We use the four finest bands, roughly ten to eighty arcminutes. -->

[CLICK] On each band we can count peaks: local maxima of the convergence field, binned by height. It's been shown to be very sensitive to cosmology...
<!-- , but it keeps only a subset of the field, the discrete features. -->

[CLICK] The wavelet ℓ1-norm is a statistic that generalises that. Instead of counting maxima in an SNR bin, we sum the absolute values of every wavelet coefficient in it. 
<!-- S-j-i is just the coefficients at scale j whose signal-to-noise falls in bin i.  -->
This way the information from every part of the field is retained, not just the peaks. 

You can think about it as a sort of PDF in the wavelet space, at each scale, capturing both the field's Gaussian core and non-Gaussian tails. 

---

## 4 — The inference pipeline 

To answer those two questions we asked, we need a way from maps to posteriors that assumes no likelihood, and works the same way for every statistic. So, simulation-based inference. We take the cosmoGRID convergence
maps at known cosmologies, add shape noise and masks, apply the starlet transform, and measure each statistic on each wavelet scale. Then concatenate, and that data vector conditions a normalising flow, which gives us the posterior.

Every posterior in this talk has been verified calibrated, with TARP and SBC.

---

## 5 — How bad is the bias 

[CLICK] cosmoGRID gives us each realisation with and without baryonic feedback, so we train the flow on the dark-matter-only maps (which is the case of having no baryon model at all) and then feed it a baryonified, "realistic" "observation". 

We measure the bias of the posteriors, in sigma, for different survey areas: from small surveys to Stage IV and extending all the way to full sky.

And as we can see,  it becomes very strong pretty quickly with survey area — because the error bars shrink. You can see it here on the contours: as the survey area grows, the posteriors tighten and the bias becomes more and more statistically significant.

And, as expected, the higher-order statistics are more biased than the power spectrum, since they are very sensitive to the contaminated small scales.


---

## 6 — What the cut costs 

To bring the bias under 0.3 sigma (which is our threshold), we have an iterative scheme to determine the optimal cuts, as you see here. We derive the posteriors, removing more and more small-scale information until the bias is below the threshold.

For the power spectrum we just remove multipole modes and find the appropriate ℓmax for every area. 

For the wavelets the scale cuts are applied by removing the smaller wavelet bands. We find that we need only their finest band dropped, at every area.


*But keep in mind that whole-band removal is the only cut we have, so it is the blunter instrument, and we are certainly throwing away clean information with it, and in principle we can improve on that.*

---

## 7 — First answer 

So, we saw how HOS posteriors are biased by unmodelled baryonic feedback, and how to cut to de-bias them.

Which brings us to the second question: whether anything is left to gain over the power spectrum once the cuts are applied. These are the Stage IV posteriors, baryon-safe scales only. Power spectrum first. [CLICK] Peak counts. [CLICK] And the ℓ1-norm.

**▲** On those scales the ℓ1-norm reaches a figure of merit 1.8 times the power spectrum's. At full sky (because of the better-adjusted wavelet cut), 2.6.
<!-- 
[CLICK] Peak counts are not as good, but they still carry plenty of complementary information to PS: their degeneracy directions in the w0 planes differ from the power spectrum's. -->

[CLICK] So higher-order statistics are not only deep-non-linear probes. The signal survives on quasi-linear scales with no baryon model at all. 

In principle we can do even better than that: our cut is not optimised, and as feedback modelling improves the analysis moves back into the non-linear regime, where the gain is larger.

---

## 8 — The second question 

So the ℓ1-norm survives the cut, and on baryon-safe scales it comfortably beats the power spectrum. And it seems like a really strong statistic. 

But the question is *how far from optimal is it*? How much of the information in these maps are we leaving on the table?

For a non-Gaussian field there is no analytic answer to that. But there is a practical one: train a neural network to compress the maps, with an objective that
makes the summary "optimal" by construction. This gives us a ceiling we can measure against.

And that is the same question the field has been asking from the other side: if a learned summary is going to do better than any analytic statistic, why hand-build a statistic at all? 

These claims have however mostly been made comparing to the power spectrum. Not against a strong higher-order statistic. So we made it.

---

## 9 — The benchmark 

The compressor we test against is a convolutional network trained with VMIM, inside the same SBI pipeline. It reads the four tomographic maps and returns a low-dimensional summary. The compressor network and the flow are trained *together*, and the pair is rewarded whenever the flow puts high probability on the true parameters.

That objective is a variational lower bound on the mutual information between the summary and the parameters. So in principle this compressor extracts everything the maps make accessible with respect to cosmology, which is exactly why it is essentially a ceiling.

---

## 10 — Making it a fair fight 

The comparison has to be fair, so: we take the same maps (which for every realization is a set of 4 flat-sky, 10 deg tomographic maps corresponding to the same patch), the same flow, the same compressed dimensionality, both arms verified calibrated. *The only thing that changes is the summary.*

---

## 11 — The gap 

And here is the first result. In grey, the ℓ1-norm measured on the four tomographic maps. [CLICK] In blue, the network. You can see that they are not that far apart, however the network is ahead, by thirty-six percent in the figure of merit.

However, the comparison is a bit unfair, because the two are not reading the same thing. The network takes all four maps together from its first convolutional layer; the ℓ1-norm is measured one bin at a time. And as we know, the bins do carry correlated inter-bin information which a per-channel statistic never sees.

**▲** So let's try to close the asymmetry and find out.

---

## 12 — Two routes 

Since we don't have "cross spectra" for HOS, one way to capture the inter-bin information is to build/approximate the missing channel. E.g. for each pair of tomographic bins, multiply the two maps pixel by pixel: the product lights up only where both have structure in the same place. This gives six pairs, six new channels, on which we can also compute the ℓ1-norm, and append to the data vector. 
A complementary operation is to make *convolution-based* cross maps.

The other route changes the statistic instead of the maps. And the idea is similar to how a joint probability distribution over the two tomographic maps encodes information compared to just the two marginal distributions. 

Look at the figure. The two curves on the edges are the per-tomographic-bin ℓ1-norms, one histogram for each of the two bins. Everything in the middle is what they miss — whether the two bins are bright in the same places.

**▲** So we measure the middle. That is the joint ℓ1-norm. Think of it as an object that encodes the joint probability distribution over the two redshift bins, rather than a product of marginals. It is a bit more complicated, but that's the idea.

*Of course, optimally, we would like to be able to do this in the full 4-d tomographic space (not just for pairs of tomographic maps), however simply because of the curse of dimensionallity, pairwise is the best we can do.*

---

## 13 — The tie 

Here is what that buys. Auto-only ℓ1-norm. [CLICK] Add the product cross-maps. [CLICK] The joint ℓ1-norm. [CLICK] And the CNN, which lands on top of it.

So essentially the joint l1 matches the neural statistic. What that means is that it appears to saturate the information these maps make accessible, without any training, and with a data vector you can inspect.

[CLICK] It holds on every parameter, over nine thousand mock observations.


---

## 14 — The third question 

There's a third question we looked at, on nulling transforms and BNT — those two slides — which I don't have time for. The answer is on the conclusions slide, and I'd be glad to go through it in the break.

<!-- One more question, and it comes back from the baryon half of the talk.

Scale cuts are partly so expensive because lensing projects a whole range of physical scales onto
each angular scale, so an angular cut is not a cut in physical scale. Nulling approaches like BNT
repair that: linear combinations of the tomographic bins, chosen so the kernels become narrow and
localised in redshift. Then a cut can go only where the systematic is.

On the power spectrum it works. We demonstrate that we can gain about a factor 1.4 in figure of merit at Stage IV in our setup, by
cutting only the bin that needs it.

[CLICK] But applied to higher-order statistics, by us and by others, it does this instead. The blue
contours are the ℓ1-norm in the nulled basis. They balloon.

〔Let that sit for a beat before you explain why it is strange.〕

**▲** And that should be impossible. BNT is a fixed, invertible transform. No information can have been lost.
And yet the per-bin ℓ1-norm keeps sixteen percent of its figure of merit.

---

## 15 — What comes back · 1:09

So we ran the same four summaries through the nulled frame.

Here you can see how much the contours for each probe inflate if we derive them in the BNT frame.

[CLICK] Per-bin ℓ1-norm: only sixteen percent of the original if derived in BNT space. [CLICK] Add one derived field per pair, the product
cross-maps: twenty-four. [CLICK] The joint ℓ1-norm, the statistic we built two slides ago:
seventy-two. [CLICK] And the network, which reads all four channels natively, is lossless within
the errors.

And this is due to the simple fact that in the BNT frame much more of the cosmological information moves from the auto-maps into the inter-bin structure. So what a summary retains under the nulling tracks how jointly it reads the bins. 

This happens because the transform correlates the shape noise across the maps, so the constraint stops sitting in any individual channel and starts sitting in the structure across them. 
(Which runs against intuition: nulling is
designed to de-correlate the bins, and joint reading matters more there, not less.)

[CLICK] **▲** So nulling can be kept as a mitigation at no cost in constraining power, provided some
stage of the pipeline reads the bins jointly. And notice the power spectrum was the first rung of
this same ladder all along: it survives the transform only if you keep the cross-spectra between
transformed bins. -->

---

## 16 — Conclusions 

Two questions, two answers.

Does baryonic feedback put the non-Gaussian information out of reach? No. Cut every contaminated
scale and the ℓ1-norm is still 1.8 times tighter at Stage IV, 2.6 at full sky.

Do we need deep learning to extract it? No. Read the bins jointly and a fixed wavelet statistic matches a compressor trained to be optimal, while being robust, interpretable and inspectable, and not requiring any training.

[CLICK] And the third one, the one I skipped: can nulling then be used with higher-order statistics?
Yes, provided the summary reads the bins jointly. The inflation was the frame, not lost information.
**▲** Happy to go through that with anyone in the break.

Both papers are on the screen, and both go on arXiv in September. Thank you.

---

# Cut lines

Calibrated to this version of the script. Rehearse the tiers so that running long degrades in an
order you chose, rather than by panic on the day.

**Tier 0 — the short paths for §5 and §6, recovering about 1:26.** These are written out under each
of those sections rather than described here, because they are meant to be *rehearsed*, not
improvised mid-talk. Slides 5 and 6 are intermediate results: the room needs the numbers and the
one honest caveat, and nothing else. Take both short paths and the tiers below become optional.

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
- **§3, the "PDF in wavelet space" paragraph** (−0:20). Cut this last of the three: it is what stops
  the ℓ1-norm sounding arbitrary, and the "why should a hand-built statistic do this well" answer
  below leans on it.

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

**"Why a wavelet decomposition? Why not just smooth with a Gaussian at a few scales and cut there?"**
Four reasons, and the first two are the ones that matter.

*A Gaussian filter is a low-pass; a starlet band is a compensated band-pass.* Smooth a map at eight
arcminutes and it still contains every scale above eight arcminutes — the large-scale power is all
still in there, and it dominates the variance, so the one-point distribution of a smoothed map is
mostly telling you about scales far larger than the filter. The starlet wavelet integrates to zero,
so a band carries only the structure at that scale. The coefficient distribution is then *about*
that scale, which is the whole point of a scale-resolved statistic.

*Gaussian-smoothed maps at different scales are nested; wavelet bands are not.* Everything in the
four-arcminute map is also in the eight-arcminute map, so statistics measured across a ladder of
Gaussian filters are strongly correlated, and the covariance is close to singular — you need far
more simulations to estimate it, and you learn little from each extra scale. The starlet bands are
approximately decorrelated and the covariance comes out much closer to diagonal (Lin & Kilbinger
2018; Ajani et al. 2021).

*And specifically on the cut, which is what you are really asking.* The starlet gives an exact
decomposition: the map is the sum of the bands plus a coarse residual. Dropping j equals one removes
an entire, identifiable channel from the data vector. There is no equivalent move for a Gaussian
filter — its transfer function is exp(−k²σ²/2), which is never zero, so contaminated small-scale
power is present in every smoothed map at some level. You would have to over-smooth to be safe, and
that throws away clean information along with the contaminated. Our criterion is empirical anyway —
we measure the residual bias at under 0.3 sigma — precisely because adjacent starlet bands do
overlap and the cut is not a perfect excision in k.

*Two properties of this particular transform.* It is undecimated, so translation-invariant: peak
counts on a decimated orthogonal transform would depend on where the pixel grid happens to fall.
And it is isotropic, so no direction is privileged, which matches the quasi-circular structures a
convergence map is actually made of. A tensor-product wavelet basis would impose a preferred axis.

〔The honest counterpoint, if pressed: the dyadic ladder is why our cut is quantised and therefore
coarser than the power spectrum's sliding ℓmax. Concede it — it is the same point you already made
on slide 6, and a √2 or non-dyadic filter bank would let you tune it.〕

**"Why should a hand-built statistic do this well?"**
Because these maps are structurally simpler than the framing suggests. To a good approximation a
noisy convergence map is a Gaussian random field plus quasi-circular peaks from collapsed
structures, and most of the morphology beyond that sits below the shape noise. The starlet is
matched to exactly that: isotropic multiscale atoms that resemble the peaks they have to register,
and a statistic that reads the full coefficient amplitude distribution scale by scale. The same
picture shows up in mass mapping, where MCALens — a Gaussian field plus a sparse wavelet component —
is comparable to deep generative reconstructions. A learned compressor can only beat a fixed
statistic where the field holds structure the statistic does not encode, and here there is not much
of it. The honest converse: on a morphologically richer field the balance should tip back towards
the network.

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
