# SPEAKER_SCRIPT — PhD defense, University of Crete, 14 September 2026

Format per `../docs/TALK-GUIDELINES.md` §11b. **`[CLICK]`** = fragment advance.
**〔stage directions〕** = done, not said. **▲** = must survive verbatim as the wording
drifts in rehearsal. Timings are **measured** from the spoken word count at **140 wpm**,
not estimated — recompute after every edit.

> **Status: Acts 0, 1 and 2.** Written before the slides, deliberately: the words come
> first, the slides support them. Acts 3–4 and the conclusions are not drafted yet.

| act | measured | budget |
|---|---|---|
| Act 0 — the setup | **11:25** | 10:00 |
| Act 1 — Ch2, does the map matter? | **11:29** | 8:15 |
| Act 2 — Ch3, PnPMass | **3:57** | 4:30 |
| | **26:51** | 22:45 |

> **Re-measured 2026-09-03**, every beat, from its own spoken word count at 140 wpm. All 25 beats
> now agree with their headings to within 3 seconds.
>
> **⚠ The talk is over budget and this is the number to act on.** Act 1 grew by 2:58 in the Part 1
> rebuild: five slides that had no beat in this script now have one — A1.4a (sparse), A1.4b
> (MCALens and the proximal operator), A1.5 (the stakes), A1.5a (the experiment) and A1.5b (the
> three maps) — against the old A1.5 (*why we compress*, 1:30) which left with the statistics
> runway. **Part of that 2:58 is not new material at all**: those slides were always going to be
> spoken over, they were simply never measured. The rest is genuinely new.
>
> Two consequences:
>
> - **Act 1 is 3:14 over its 8:15 budget.** The cut ladder for Acts 1–2 below is the first place
>   to go; tiers 1–2 recover about 1:03 without touching an argument.
> - **The 1:30 that left Act 1 has to land in Act 3**, because the seven runway frames landed
>   there. Act 3's estimate in `STRUCTURE.md` predates the move and should be checked before the
>   whole-talk figure is trusted.
>
> Act 0's 1:25 overrun is unchanged in substance — A0.6c came back from Act 1 on 2026-09-03,
> which is where 0:53 of it comes from.

The slack is deliberate and should stay slack — pauses, the beat after a headline, and the
time a room needs to look at a figure before you talk over it. It is **not** room for more
material.

> **Act 0 is 0:30 over its own budget**, and **Act 1 is 1:09 over**, as of 2026-09-02.
> A0.6a and A0.6b — shear and convergence, then what the convergence is — remain as a
> two-slide light formalism block between Euclid and the chain.
>
> **The κ–γ slide moved again on 2026-09-02**, out of Act 0 and into Act 1, where it now sits
> directly behind the *Part 1* divider as **A1.1a**. Nothing was added or cut: 0:53 of spoken
> words crossed the act boundary, so the whole-talk figure is unchanged and only the
> attribution moved. This is the reorder that finally puts the κ↔γ formalism next to the
> methods that use it, instead of twenty minutes upstream of them.
>
> **It also collided three beats into each other** — A1.1a, A1.2 and A1.3 now restate one
> another within a minute. See the ⚠ note at A1.1a: resolving it is worth 0:35–0:45 and would
> put both acts back inside budget. That trim is the outstanding decision.

---

## The three things this opening must do

1. Give a wide audience — family, students, two committee members who do not work on
   lensing — a picture of the Universe they can hold for the next forty-five minutes.
2. Make the case for **weak lensing specifically**, not cosmology generally.
3. Land the hinge: **at Stage IV precision, the analysis becomes the limitation.** Every
   act afterwards is an instance of it.

Fixed points (Andreas, 2026-08-26): **ΛCDM**, **cosmological probes**, **Euclid**.

**Revised 2026-08-29.** Two changes to A0.3. It no longer names Ωm, σ8 and w0 with definitions — it
glosses what the six parameters *represent* and stops; the three directions arrive at the first
contour plot in Act 1, where the room can see what they do. And it no longer sets up a taxonomy of
dark energy. A field-equation slide (modify the geometry / the contents / leave Λ alone) was drafted
and **cut**: this thesis makes no dark-energy claim, so motivating one promises a question the talk
never answers, and A0.4 already earns lensing more concretely by calling it the probe sensitive to
both geometry and growth. What survives is the epistemics, in one sentence — you do not test the
model by arguing about what Λ is, you measure the same numbers several independent ways and check
they agree — which hands straight into the probes beat. The field-equation slide stays in the deck
as **general-audience Q&A backup**.

---

## A0.1 — Title · 0:27

〔Stand still. Let the chair finish. Look at the room, not the screen. Do not rush this;
the opening thirty seconds are the ones you can least afford to improvise.〕

Thank you, and good morning. Thank you all for coming, and thank you to the committee for
reading this.

This is a talk about how we measure the Universe: what we can learn from the light that
reaches us, and what it takes to trust what we learn from it.

I would like to start with the picture we are trying to fill in.

---

## A0.2 — the picture · 1:08

〔Turn to the screen, orient the room once, then turn back. Give them a couple of seconds
to look before you narrate.〕

This is the history of the Universe as we currently model it. Time runs from left to right,
and the width of the cone is the scale factor — how much the Universe has expanded.

The initial conditions are set very early: a nearly scale-invariant spectrum of small,
close-to-Gaussian density perturbations. Three hundred and seventy-five thousand years in,
the plasma recombines and the Universe becomes transparent. That released light is the
microwave background, and it is a snapshot of those perturbations at redshift about eleven
hundred, when they were still about one part in ten to the fifth.

**▲** After that they grow by gravitational instability. How fast they grow depends on how
much matter there is and on how the Universe is expanding, and that is what turns a nearly
smooth field into the galaxies and clusters we observe.

And in the last few billion years the expansion began to accelerate, which suppresses that
growth.

---

## A0.3 — what ΛCDM is, and how you test it · 2:20

〔The slide the physicists are waiting for. Be precise, do not gesture. The parameter columns are
there to be pointed at, not read out.〕

So what is the model?

ΛCDM is a short list of assumptions. **Gravity** is general relativity, unmodified. The
**geometry** is spatially flat, homogeneous and isotropic on large scales. The **contents** are
cold dark matter — collisionless and non-relativistic — plus baryons, radiation, and a constant Λ.
And the **initial conditions** come from inflation: adiabatic, near-Gaussian, near-scale-invariant
perturbations.

**▲** On those assumptions, six free parameters. Two fix the initial conditions — the amplitude and
the tilt of the primordial fluctuation spectrum. Two fix the composition — how much ordinary
matter, how much cold dark matter. And two more: the angular scale of the sound horizon, which sets
the expansion rate, and the optical depth to reionisation.

〔Point at the three groups. **Do not** define Ωm, σ8 or w₀ — they arrive at the first contour plot
in Act 1, where the room can see what they do.〕

**▲** And notice what is *not* in that list: the density of Λ. In a flat universe it is not a free
parameter at all — it is whatever is left once you have counted everything else.

That is the entire model, and it fits the microwave background, the expansion history and the
clustering of galaxies simultaneously.

[CLICK] **▲** But it is a *phenomenological* description, not an explanation. About ninety-five per
cent of the budget is two components whose nature we do not know — and there are three things in
this picture the model does not account for.

〔The pie is replaced by the cone here. Then one click per question; let each land before the next.〕

[CLICK] We do not know what **dark matter** is. It has never been detected in a laboratory.

[CLICK] We do not know what **dark energy** is either. The value of Λ is put in by hand — the
simplest choice available, not one that anything requires.

[CLICK] **▲** And the measurements we make at the two ends of this picture do not quite agree with
each other.

〔One clause only. A0.4 makes that quantitative; if you explain S₈ here you will say it twice. This
is the thread the next two slides pull.〕

**▲** So how do you test a model like that? Not by arguing about what Λ *is*. You can put the
acceleration into the geometry, or into the contents, or leave it as a constant of nature, and the
expansion history barely changes.

**▲** You test it by measuring the same few numbers **several independent ways**, and checking that
they agree.

〔That sentence is the hinge into the next slide. Land it and stop.〕

---

## A0.4 — the probes, and a consistency test that does not quite pass · 1:42

〔The densest beat in Act 0, and the most important. Do not speed up.〕

Different probes measure different combinations of those two, which is the reason we use
several.

The microwave background gives the initial conditions and the geometry out to redshift
eleven hundred. Baryon acoustic oscillations use the sound horizon frozen in at
recombination as a standard ruler, which maps the expansion history. Supernovae give
luminosity distances. Galaxy clustering traces the matter, but through galaxies, which are
biased tracers, so a bias model sits between what we count and what we want.

**▲** Weak lensing responds to the total matter directly, and it is sensitive to both the
geometry and the growth. That is why this thesis is about lensing.

[CLICK] **▲** Now, the consistency between independent probes is itself the test of the
model. Measure the initial conditions with the microwave background, evolve them forward
assuming ΛCDM, predict what we should see today — and then measure it. If ΛCDM is right,
those agree.

[CLICK] As the uncertainties fell towards the per-cent level, they stopped agreeing
perfectly. The present-day expansion rate comes out differently from the early-Universe
extrapolation than from direct measurement. And the amplitude of clustering — S-eight,
sigma-eight times the square root of Omega-m over nought point three, the combination
lensing constrains best — came out about one point seven sigma below the Planck
extrapolation in DES and KiDS.

Three ways to read that. New physics. A statistical fluctuation. **▲** Or something in the
analysis itself.

〔Do not resolve it. Move on.〕 Hold that thought.

---

## A0.5 — what weak lensing measures · 1:03

〔A new picture, and the last drawing in the introduction — everything after this is
data. The slide has no fragments: it goes up whole. Give the room two seconds to read it
before you start talking over it.〕

Here is the same idea, drawn properly. Follow the light from those distant galaxies on
its way to us.

It does not travel through empty space. It passes every structure that happens to lie
along the way, and every mass it passes bends its path slightly. By the time that light
reaches us, the image of the galaxy is slightly distorted — stretched one way and squashed
the other.

For any single galaxy the effect is about a per cent. Far too small to see, and we do not
know what shape the galaxy had to begin with.

**▲** But the distortion is coherent. Neighbouring galaxies behind the same piece of
structure are distorted the same way. So we measure the shapes of very many galaxies and
look for that shared pattern.

That is cosmic shear, and it lets us map the matter back to redshift about three.

---

## A0.6 — Euclid · 0:38

〔The "and now" beat. Let the clip run behind you; do not narrate the clip.〕

And we are about to be able to do this properly.

Euclid is a European Space Agency mission. It launched in 2023, it is taking data now, and
it will survey fourteen thousand square degrees — about a third of the sky. It will measure
the shapes of billions of galaxies. The first cosmological data release is in June 2027.
Rubin will follow from the ground, and Roman deeper over a smaller area.

**▲** That is roughly an order of magnitude more statistical power than the surveys we have
today.

---

## A0.6a — shear and convergence · 1:09

〔The deck turns from black to paper here. Do not remark on it — let the room notice.
This is the first slide that names quantities rather than telling a story, so drop the
pace a little and stand still.〕

So what is it we actually measure?

Take a round patch of sky behind some structure. Lensing does two things to it. It changes
the size of the patch — that is the convergence, kappa. And it stretches the patch one way
while squashing it the other: that is the shear, gamma, two numbers rather than one because
a stretch has an orientation.

Both are second derivatives of the same lensing potential. Two readings of one field.

**▲** But the convergence, the one that *is* the mass, is the one we cannot measure: we
never knew how big the galaxy was to begin with. The shear we can, because it is coherent —
every galaxy behind the same structure is stretched the same way, so with enough of them the
shared alignment lifts out of the noise.

[CLICK] **▲** So we measure the shear and we want the convergence. Getting from one to the
other is a reconstruction, and that is where this thesis starts.

---

## A0.6b — what the convergence is · 0:45

〔Do not read the equation. Point at the two pieces and say what each one carries. The map
at the bottom is the object every result in this talk is computed on, so let it sit for a
beat at the end.〕

And this is what the convergence is. Add up all the matter along the line of sight,
weighted by how efficiently each piece of it lenses — a weight that peaks about halfway to
the galaxy whose light we are looking at.

Two things ride in that integral. The kernel carries the geometry: distances, and the
expansion history. The overdensity carries the growth of structure. **▲** A convergence map
responds to both at once, which is why lensing tests the model rather than measuring a
single number.

And this is what one looks like — simulated, here. Every result I show you is computed on
maps like this.

---

## A0.6c — how you get from one to the other · 0:53

〔Closes the Act 0 formalism block. First half over the clean diagram; take the click before the
second half, and slow down on the last line — it is the sentence Part 1's question grows out of.〕

So how do we get from the one to the other?

Both are second derivatives of the same potential, so in Fourier space the relation inverts
in a single line: the mass map is a linear combination of the two shear components. That is
Kaiser-Squires. It is linear, it is fast, it has no free parameters — and on a complete,
noiseless field it is exact.

[CLICK] Real data is none of those things. Every galaxy carries shape noise. The survey has
holes where there are no galaxies to measure. And the overall level of the map is not
constrained at all — the mass-sheet degeneracy.

**▲** So the inversion stops being a calculation and becomes a choice. And what you choose
changes the map you get.

---

## A0.7 — the hinge · BENCHED 2026-09-01 · was 0:45

> **The slide is at the back of the deck, not in the flow** (reveal #90, under *Earlier
> intro versions*), and this beat is benched with it. The words are kept verbatim: nothing
> here is superseded, it was moved.
>
> **What it leaves open.** A0.4 raises the S₈ disagreement and this was the beat that paid
> it off — *it was the third one, it was the analysis*. Nothing pays it off now. The talk
> still works, because A0.6c's *the inversion stops being a calculation and becomes a
> choice* hands off into A0.8 cleanly. The four questions no longer land here at all — the
> scoreboard moved to the conclusions on 2026-09-03 — so Act 0 now ends on the hand-off into
> Part 1. But a
> committee that hears "the probes do not quite agree" in minute four and never hears why
> is owed an answer, and it is a likely general-audience question. Two ways back:
> reinstate the slide, or fold its ▲ sentence into A0.4's close.

〔If reinstated: slow down. This is the hinge of the whole talk. Pay off the thought you
left open.〕

Which brings me back to that disagreement.

[CLICK] Last year KiDS re-analysed their data with better calibration of galaxy shapes and
redshifts, and the tension fell below one sigma. **▲** It was the third one. It was the
analysis.

〔Beat.〕

**▲** Whether a tension like this reflects new physics or an unrecognised systematic is
settled by the analysis toolkit as much as by the data.

And that is the reason this matters more, not less, as the surveys get better. When the
statistical errors shrink by an order of magnitude, they stop being what limits you.
**▲** What limits you is how well you understand your own analysis.

---

## A0.8 — what this thesis is about, and the step Part 1 lives in · 1:20

> **Merged 2026-09-03.** This was two slides and two beats — the chain, then the hand-off with
> the same chain redrawn and one step lit. Andreas: *"slide eleven should be just an animation
> of slide ten."* It is now one slide with a second click that dims the diagram and lights the
> shear→mass-maps step, so the room watches one picture change instead of comparing two.
> The old hand-off slide is parked, hidden, directly below it in `index.html`.

〔The thesis statement, and the map for everything after it. Walk the diagram left to right
once, unhurried, touching each box — this is the picture the room sees again at the head of
every part. Then slow right down for the ▲ and let it sit.〕

So this thesis is about the analysis.

Between the galaxy shapes we measure and the cosmological parameters we report there is a
chain. A catalogue of shapes and redshifts. Binned into shear maps. Inverted into mass maps.
Compressed into a summary statistic. Compared against simulations to infer the parameters.
And out comes a posterior.

Underneath runs the other half of it. Cosmologies drawn from a prior, run through N-body
simulations, and then given the systematics — baryons, intrinsic alignments, shape and
redshift calibration — before any of it is compared with the data.

[CLICK] **▲** Every one of those stages is now built out of learned components, and every one
of them can bias the answer, or quietly throw information away, with no internal check
noticing.

〔Beat.〕

I am going to ask four questions about that chain. You will see this picture again at the head
of every part, with one box lit.


[CLICK] 〔The diagram dims and two boxes light. Point at them; do not redraw the picture in
words — the room can see it.〕

Now the same picture, with one step lit.

The first two parts both live there. Shear goes in; a mass map comes out. **▲** Everything for
the next twenty minutes is about what happens **between those two boxes**.
---


## Cut ladder for Act 0

Measured savings, in the order I would take them.

| tier | cut | saves |
|---|---|---|
| 1 | A0.2's initial-conditions sentence. Open at recombination and go forward. | −0:18 |
| 2 | A0.6's Rubin and Roman sentence; A0.4's supernovae and BAO sentences. | −0:20 |
| 3 | A0.4's *H*₀ sentence, keeping only the clustering amplitude. Costs the generality but keeps the beat. | −0:14 |
| 4 | A0.6c's *linear, fast, no free parameters* clause. The block on the slide says it; the room does not need it twice. | −0:07 |
| 4 | A0.6b's closing paragraph (*and this is what one looks like…*). The map is on the screen; pointing at it does the work. | −0:09 |
| 5 | A0.6a's *both are second derivatives* line — A0.6c restates it in full two slides later. | −0:06 |
| — | **Never cut:** A0.3's closing *measure it several independent ways* ▲ (it sets up the probes beat), the ▲ in A0.8, and A0.6a's ▲ pair — *we measure the shear, we want the convergence* is the sentence Act 1's question is built on. | |

**Tier-0 short path for A0.5** — if the clock is bad but the slide is up, say only:

> The same idea, drawn properly. Light from a distant galaxy passes every structure on the
> way to us, and each one bends it slightly, so the image arrives distorted. For one galaxy
> the effect is about a per cent — invisible. But it is coherent across neighbours, so we
> measure many galaxies and look for the shared pattern. That is cosmic shear.

(−0:24, and it keeps the payoff.)

---

## Register notes

- *Measure*, *infer*, *obtain*. Not *get*.
- "S-eight" out loud, not "S subscript eight".
- Say "about sixty-eight per cent", not "sixty-eight point three".
- **Do not** apologise for the wide-audience opening or signpost it ("for those of you who
  are not cosmologists…"). Pitch it and move.
- A0.2 and A0.5 are two views of one statement — the cone says *when*, the lensing
  diagram says *how*. Link them out loud (“the same idea, drawn properly”); do not
  introduce A0.5 as a new topic.
- The theme flips to paper at A0.6a and the room will feel it. **Do not narrate the
  change.** The pace change carries it.

## Numbers used, and where they are ledgered

Every figure above traces to `PAPER_FACTS.md` §9, which traces to the thesis introduction:
375,000 yr · ~68 % / ~27 % / <5 % · 14,000 deg² · a third of the sky · billions of galaxies
· June 2027 · Rubin ~18,000 deg² · 1.7σ · KiDS-Legacy below 1σ · order-of-magnitude leap.

**Not used, deliberately:** "1.5 billion galaxies" (real, but absent from the thesis, so it
fails the ledger rule).

---
---

# Act 1 — Ch2, does the map matter?

**Act 1 measured: 9:24 spoken** against a 8:15 budget, at 140 wpm — 1:09 over, and the
⚠ overlap at A1.1a is where it comes back from.

## A1.1 — the question · 0:43

〔Act divider. Say the question, then stop. Do not re-read the scoreboard aloud — they saw it
thirty seconds ago. Turn back to the room for the last line.〕

Question one.

Every map-based statistic starts from a reconstruction. We measure shear — the distortion of
galaxy shapes — and what we want is convergence, the projected mass. Turning one into the other is
an inverse problem, and it is ill-posed: the noise is large, the survey has holes, and the mask
destroys information that no method can put back.

**▲** The field has judged reconstruction methods on how closely the recovered map matches the
truth. But the map is not what we publish. The posterior is.

So — does the choice of reconstruction change the cosmology we infer, or is it preprocessing?

---

## A1.2 — one direction is easy; we need the other one · 0:57

〔General before specific. Stay off the lensing details — 1.3 does those. Land the last sentence
and stop; it is the thesis of the whole movement.〕

Before the methods, the shape of the problem.

One direction is easy. Give me the matter distribution, and I can compute exactly what galaxy
shapes you would observe. It is a deterministic calculation and it has one answer.

**▲** We need the other direction: we observe the shapes, and we want the matter. That is an
inverse problem, and this one is *ill-posed* — the data do not determine the answer. Many different
mass maps are consistent with the same observed shapes.

[CLICK] **▲** So you cannot simply invert. To choose among those maps you have to *add* something —
an assumption about what a plausible mass map looks like.

**▲** And that assumption is not a technicality. It **is** the method. Everything in this chapter is
a different answer to one question: what do you assume about κ?

---

## A1.3 — the standard answer, and why it is not enough · 1:23

〔Be fair to Kaiser–Squires. It is what the field has used for thirty years and it has good
reasons. The point is not that it is bad, it is that its assumption is invisible.〕

The standard answer is to write down the analytic inversion.

Shear and convergence are both second derivatives of the same lensing potential, so in Fourier
space the relation inverts in a single line. That is Kaiser–Squires. It is linear, it is fast, it
has no free parameters, and it is what almost every survey has used.

[CLICK] But look at what it assumes about κ: essentially nothing. And that shows up in two places.

**▲** The mask. Where there are no galaxies there is no shear — and the Fourier transform does not
care, so it spreads that hole right across the map.

**▲** And the noise. The inversion amplifies the smallest scales, and galaxy shape noise is large,
so what comes back at small scales is mostly noise.

[CLICK] There is an obvious repair for the first one: fill the mask in before you invert. That is
inpainting, and it gives you a second method — iKS. Hold on to it; we test it later.

[CLICK] In practice we fix that by smoothing. Which works — but smoothing **is** an assumption,
applied bluntly and after the fact, and it throws away exactly the small-scale structure we are
trying to measure.

---

## A1.4 — reconstruction as inference, and the one Bayes lesson · 1:44

〔The pivot of Movement I, and the slide that makes Act 2 make sense. This is also the ONE
place Bayes is taught in the whole talk, so pitch the first paragraph at the widest person in
the room. Then take the priors one at a time; each is a physical statement about the
convergence field, not a piece of machinery.〕

So instead of smoothing afterwards, state the assumption up front.

**▲** Write the reconstruction as inference. Three pieces. What we want — the map, given the
data. What we can write down — how shear comes from mass, which is the operator from two slides
ago, plus noise. And what we assume before we look: the prior.

[CLICK] Once it is written down, every method is a different answer to that one slot. Assume the
field is **Gaussian** — a covariance and nothing else — and the solution is the Wiener filter. It
is clean, and it is optimal if the assumption is true. But the late-time convergence field is not
Gaussian, and the peaks are the whole point.

[CLICK] Assume instead that it is **sparse** in a wavelet dictionary — that structure is
concentrated rather than spread out — and the peaks come back much better, at the cost of the
diffuse component.

[CLICK] **▲** MCALens takes both. It models κ as a Gaussian component plus a sparse non-Gaussian
one and solves for the two together. That is the best analytic prior we found, and it is the one
the rest of this act tests.

[CLICK] Or you stop choosing, and learn the prior from simulations. Hold that thought — it is
Part 2.

[CLICK] **▲** And the same three terms come back in Part 3, with the cosmological parameters as
the unknown instead of a map. There, the likelihood is the one we *cannot* write down.

〔Beat.〕 Four priors, four maps. Look at the small scales.

> **FLAG — say this only if pressed, and say it in Part 2 regardless.** Here we take the *most
> probable* map: a point estimate. In Part 3 we want the whole distribution. It is a real
> distinction and Starck is the likeliest person to ask. The arc is the answer — point estimate
> in Ch2, calibrated uncertainty in Ch3, full posterior on the parameters in Ch4–5.

---

## A1.4a — what "sparse" actually claims · 0:57

〔Short. A1.4 already named the sparse prior; this slide is what it *means*. Do not teach the
wavelet transform — say what a starlet looks like, make the claim concrete, and move.〕

So what does it mean to say the map is *sparse*?

It does not mean the map is mostly empty. It means there is a **basis** in which it is mostly
zeros — a representation where a handful of large coefficients carry nearly all of the signal and
everything else is small.

[CLICK] We use **starlets**: isotropic, positive wavelets that look, by construction, like the
convergence profile of a dark matter halo. So "the map is sparse in starlets" is a physical
statement, not a numerical trick. It says the field is a small number of haloes on a quiet
background.

**▲** That is a far stronger claim than Kaiser-Squires makes. It is also a claim that can be
wrong — and that is the point. The assumption is now visible, so it can be argued with.

---

## A1.4b — MCALens, and the one step Part 2 replaces · 1:06

〔The slide in Act 1 that Part 2 depends on. Land the proximal-operator sentence slowly — PnPMass
is unintelligible without it, and this is the only place it gets said.〕

MCALens does not choose between those two priors. It uses both, on different parts of the field.

It models the convergence as a sum. A **Gaussian** component, handled by a Wiener filter that needs
nothing but the power spectrum. Plus a **sparse non-Gaussian** component in the starlet basis — the
peaks and haloes, which is exactly where the higher-order signal lives.

[CLICK] And it solves them by alternating. Fix one component, solve for the other, then swap, and
repeat until the map stops moving.

[CLICK] **▲** Each of those solves ends the same way, with a **proximal step**. If you take one
thing from this slide, take this: a proximal operator is the step that pulls a candidate map back
onto what the prior allows. For sparsity it is just thresholding — keep the large wavelet
coefficients and zero the rest.

〔Deliberate pause. This sentence is the setup for the whole of Part 2.〕

Remember that step, because in Part 2 we throw it away and put a neural network in its place.

〔Down-arrow for the algebra only if asked.〕

---

## A1.5 — the stakes · 0:54

〔The pivot of the act. The divider asked the question; this is where the room learns it was a real
question and not a rhetorical one. Do not rush the last line — it is why the paper exists.〕

So: three methods, three different maps — and every one of them reproduces the shear it was given.

Up to this paper, the way the field compared reconstructions was to measure how close the map came
to the truth, in simulations, against a truth that no real survey will ever have.

[CLICK] **▲** But the map is not what we publish. The posterior is. And nothing in a reconstruction
error tells you what happens to Omega-m, sigma-8, or w-nought.

[CLICK] So it was genuinely open, and it was argued about — with something concrete riding on it.
Euclid has to pick a reconstruction. If mass mapping is preprocessing, take the cheap one and move
on. If it is not, that choice is a scientific decision, and it should be made deliberately.

---

## A1.5a — the experiment · 0:52

〔Fast and flat. This slide's only job is to make the result unimpeachable, so say the controls
plainly and do not linger.〕

So we built the pipeline and changed exactly one thing in it.

Twenty-five cosmologies from cosmo-SLICS — everything here is on simulations, because we need a
truth to compare against. Same statistic on every map, same emulator, same likelihood, same
sampler. Only the reconstruction changes.

**▲** So whatever moves in the posterior is the reconstruction. It cannot be anything else.

[CLICK] One word about the last two boxes, because they go past quickly. A map is a hundred
thousand correlated pixels, so it has to be compressed before any likelihood can touch it — and
which statistic you compress with is a scientific choice of its own. That is Part 3. Here it is
nailed down on purpose, so it cannot explain anything that moves.

〔**Do not** explain peak counts here. That is Act 3's material and it is the biggest delivery risk
in this act.〕

---

## A1.5b — the three maps · 0:39

〔Point at the small scales, and give the room longer than feels natural to actually look.〕

Here are the three reconstructions of the same simulated field.

Kaiser-Squires inverts directly, and because the noise diverges at small scales it has to be
smoothed — so the small scales are simply gone. Inpainting KS fills the mask in first and is
otherwise the same. MCALens is different in kind, and you can see it: the structure survives.

**▲** And read the stake on the right. The two that assume nothing about kappa are what Euclid
plans to run. MCALens is the state-of-the-art alternative. That is the comparison this paper makes.

---

## A1.6 — the answer · 1:15

〔The headline of the act. Slow down on the two numbers, and do not skip iKS — reporting the null
result is what makes the positive one credible.〕

Same twenty-five simulations, the same peak counts, the same emulator, the same likelihood, the
same sampler. The only thing that changed is the reconstruction.

**▲** And it changes the answer.

[CLICK] Kaiser–Squires sets the baseline at one.

[CLICK] Inpainting buys nothing — zero point nine nine six. **▲** That is a null result and I
report it as one. The inpainting acts on the masked regions, and the peak counts exclude those
regions anyway. It would not carry over to a Fourier-space statistic like the bispectrum, which
uses the whole area, and the paper says so.

[CLICK] MCALens is a factor two point six. In the paper's convention, a hundred and fifty-seven
per cent.

〔Beat.〕

**▲** And here is the sentence I would most like you to keep. Measured on reconstruction error,
MCALens beats Kaiser–Squires by four per cent. Measured on the figure of merit, by a hundred and
fifty-seven.

Map quality and constraining power are not the same objective. The method that makes the best map
is not the method that gives you the best posterior.

〔If pressed on precision: Chapter 2 reports no error bars — one chain per method. Say it before
someone finds it.〕

---

## A1.7 — where the gain comes from · 0:59

〔The mechanism slide, and the one that survives the closed examination. Take the time.〕

So where does it come from?

We can localise it, because the statistic is multi-scale. Start with the coarsest bands only —
sixteen and thirty-two arcminutes, plus the coarse map — and add finer scales one at a time.

[CLICK] Kaiser–Squires improves when you add eight arcminutes. [CLICK] And then it stops. Four
arcminutes adds nothing significant. Two adds nothing.

[CLICK] MCALens improves at every scale you add, down to two arcminutes.

**▲** So the gain is not a global normalisation. It is small-scale reconstruction fidelity —
MCALens recovers structure at scales where the linear inversion has already smoothed itself into
noise, and the higher-order statistic can read it.

〔Beat, and turn back to the room.〕 Which tells you where the effort belongs. The reconstruction
is not preprocessing. It is a scientific choice, and it should be made with the statistic that
comes after it in view.

---
---

# Act 2 — Ch3, PnPMass

**Act 2 measured: 3:57 spoken** against a 4:30 budget, at 140 wpm.

## A2.1 — what we actually want from a reconstruction · 1:09

〔The attribution goes here, said once, plainly, at the top. Do not over-explain it and do not
undersell it either.〕

Question two follows from the first. If the reconstruction matters this much, what do we want from
one?

〔Say before the list.〕 This chapter is joint work with Hubert Leterme. I co-developed the method,
and the uncertainty quantification is mine.

[CLICK] Four things. It should be **flexible** — one model that still works when the noise level
or the footprint changes. **Fast** enough to run on a survey. **Accurate**. And it should tell you
how wrong it is, in a way you can check.

[CLICK] Nothing had all four. Kaiser–Squires and Wiener are fast and flexible, but give you no
useful uncertainty — and Wiener assumes the field is Gaussian, which is the assumption this whole
thesis exists to avoid. Sparse and fully Bayesian methods are accurate but slow. And the
deep-learning reconstructions are accurate and fast at inference, but each one is trained for a
single noise level and a single mask, and it hands you a point estimate with no error bar at all.

---

## A2.2 — the construction · 1:07

〔The diagram. Walk it once, left to right. Do not go into proximal operators unless asked — there
is a backup slide, and going there unprompted costs a minute you do not have.〕

PnPMass.

[CLICK] The reconstruction is a fixed-point iteration: a gradient step towards consistency with
the measured shear, then a denoising step. That structure is standard — forward–backward
splitting. What plug-and-play does is replace the denoising step, which in a classical method
would be a hand-designed regulariser, with a learned denoiser.

[CLICK] Ours is a Swin-Transformer network. Seven million parameters, trained once on white
Gaussian noise across a range of noise levels, with the noise level handed to it as an extra input
channel.

**▲** And that is the whole point. The denoiser never sees the mask, never sees the survey, never
sees a convergence map with one particular noise level baked into it. It learns one thing — what a
plausible convergence field looks like. The physics of the observation stays in the gradient step,
where it belongs.

[CLICK] Change the noise. Change the footprint. The same trained network runs. Eight iterations,
and you have a map.

---

## A2.3 — accurate, and honest about it · 1:41

〔Three panels. The claim is the error bars. Do not let the accuracy comparison become the
subject — it is the setup for the real result.〕

Two questions. Is it accurate, and are its error bars honest?

[CLICK] On accuracy, the benchmark is DeepMass — a network retrained for this specific mask and
this specific noise. PnPMass lands within about one per cent of it. A variant that denoises the
residual rather than the map, within about half a per cent.

**▲** Within one per cent of a network fine-tuned to the observation, from a denoiser that was
never shown the observation.

[CLICK] For the uncertainties we use conformal prediction — conformalised quantile regression. It
gives per-pixel intervals with a distribution-free, finite-sample coverage guarantee: you set a
target error rate, calibrate on held-out data, and the intervals hit it. No Gaussianity, no
asymptotics, no assumption that the network is right.

Which means that after calibration, every method reaches the target rate. That is what the
guarantee does. So the comparison is not about whether the coverage holds — **▲** it is about
which method achieves that coverage with the *tightest* intervals.

[CLICK] PnPMass has the smallest calibrated error bars of every method we tested, DeepMass
included. On all five hundred and twelve test images.

〔Beat. Then slow down — volunteering the limitations here buys you credibility for Acts 3 and 4.〕

Two limits, plainly. The coverage is marginal, not conditional: it holds on average over pixels,
and the miscoverage concentrates at the peaks — which is exactly where Chapter 2 just said the
information lives. And this is a single cosmology. Robustness across cosmologies is the first
thing I would do next.

---

## Cut ladder for Acts 1 and 2

Measured savings, in the order I would take them.

| tier | cut | saves |
|---|---|---|
| 1 | A1.3's inpainting paragraph. Name iKS on the figure instead, and let A1.6's null result carry it. | −0:11 |
| 1 | A2.3's conformal-prediction explanation down to one sentence: "distribution-free per-pixel intervals, calibrated on held-out data." | −0:17 |
| 2 | A1.5's *why we compress* opening. Go straight to peaks; costs the setup for Questions 3 and 4. | −0:35 |
| 2 | A2.1's four-requirement enumeration; go straight to what was missing. | −0:18 |
| 3 | A1.4's sparse-prior paragraph. Go from Gaussian straight to MCALens; costs the reason MCALens has two components. | −0:19 |
| — | **Never cut:** A1.2's *the added assumption **is** the method* ▲ and A1.4's likelihood-times-prior ▲ (Act 2 is unreadable without both) (it sets up Act 1's question **and** Act 2's method), A1.5's five-angular-scales sentence (A1.7 is unreadable without it), A1.6's four-per-cent-versus-157 contrast, the iKS null result, A2.2's "never sees the mask" ▲, A2.3's tightest-intervals ▲, and both A2.3 limitations. | |

**Tier-0 short path for A1.7** (−0:41, and it keeps the mechanism) — if the clock is bad
but the slide is up:

> The statistic is multi-scale, so we can localise the gain. Add finer bands one at a time:
> Kaiser–Squires stops improving at eight arcminutes, MCALens keeps improving down to two. The
> gain is small-scale reconstruction fidelity, not a global normalisation.

---

## Numbers used in Acts 1–2, and where they are ledgered

**Act 1** — `PAPER_FACTS.md` §2. Ratios to a KS baseline of 1.00: iKS **0.996**, MCALens **2.57**
(the paper's **+157 %**). RMSE ratios: iKS 1.005, MCALens **0.959** — the four-per-cent figure.
25 cosmologies · DES-Y1, 19 × 100 deg² · starlet scales 2′–32′ + coarse · scale ladder: KS
saturates after 8′, MCALens gains to 2′.

**Act 2** — `PAPER_FACTS.md` §3. RMSE ratios to DeepMass: PnPMass **1.013**, residual variant
**1.006** — quoted as "about one per cent" and "about half a per cent". Smallest calibrated error
bars **on all 512 test images**. SUNet, **7.2 M** parameters. **8** iterations. Target error rate
α ≈ 4.55 %.

**Deliberately not said.** Ch2's absolute FoM values (758 / 755 / 1947) — ratios only, §0. The
inverse-volume conversion ×2.57⁴ ≈ 43.6 (§8.4: arithmetically right, reads as inflation, stays
off the slide *and* out of the mouth). The Ch3 timing table — the argument is that training
happens once, not that inference is fast; leading with speed invites the table, where PnPMass
loses per map (§3, Timing).
