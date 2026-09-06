# SPEAKER_SCRIPT — PhD defense, University of Crete, 14 September 2026

Format per `../docs/TALK-GUIDELINES.md` §11b. **`[CLICK]`** = fragment advance.
**〔stage directions〕** = done, not said. **▲** = must survive verbatim as the wording drifts in
rehearsal.

**Every timing in this file is measured, not estimated** — spoken words divided by 140 wpm, with
stage directions, cues and blockquotes excluded. The measurement is done by
`../tools/measure-script.py`, which also checks every `[CLICK]` cue against the deck's real
fragment count:

```
tools/measure-script.py PhD_Defense_2026           # report
tools/measure-script.py PhD_Defense_2026 --write   # ...and stamp the headings
```

Run it after every edit. A heading you typed by hand is a heading that is wrong.

> **Rewritten end to end 2026-09-06**, against the deck as it stands at **114 frames**. The
> previous version covered Acts 0–2 only, was written before most of the slides existed, and had
> been overtaken by four structural passes: the joint-ℓ1 paper moving ahead of the baryon paper,
> the wavelet excursion, the statistics-shape plots, and the introduction rebuild. Acts 3 and 4 and
> the close are new. Every beat now names the **frame** it is spoken over, which is what makes the
> cue audit possible.

## The budget

| act | frames | measured | notes |
|---|---|---|---|
| Act 0 — the setup | 1–9 | 11:27 | ends on the four questions |
| Act 1 — Part 1, does the map matter? | 10–23 | 13:11 | opens with the formalism, moved here 2026-09-06 |
| Act 2 — Part 2, PnPMass | 24–30 | 6:31 | frames 27–28 are the first cut |
| Act 3 — Part 3, the summaries | 31–53 | 19:24 | the longest act; 13:08 of it is teaching |
| Act 4 — Part 4, baryons and nulling | 54–60 | 8:30 | |
| Close | 61–62 | 1:42 | |
| | **62** | **60:46** | **against a 40:00 target in a 45:00 slot** |

> **⚠ The talk is 20:46 over, and that is the number to act on.** It is not a rounding problem: the
> main line has grown to 62 frames, and 62 frames is an hour-long talk at any honest rate. *The
> arithmetic, and how to close it* — after the close, below — is a tiered ladder with measured
> savings that gets to **48:05** without losing an argument, and three named packages for the last
> seven minutes. Read it before rehearsing, not after.

〔The table above is what the measuring tool prints. If it disagrees with the headings below, the
tool has not been run since the last edit.〕

**The slack in a 45-minute slot is deliberate and must stay slack** — pauses, the beat after a
headline, and the seconds a room needs to look at a figure before you talk over it. It is not room
for more material.

## What the script pass exposed

Four things that are deck problems, not script problems. They are listed here because the script
is where they became impossible to ignore, and each one is cheap to fix.

1. **There are no Part 3 and Part 4 dividers.** Frame 9 promises four parts; the deck names Parts 1
   and 2 on black dividers and then runs Parts 3 and 4 together behind one *movement II* opener at
   frame 31. The room is told there are four questions and then shown two labelled parts. Two
   divider slides would close it, and they are also the natural place to put the paper references
   for Papers 3 and 4, which currently appear only on the conclusions.
2. **Frames 37, 38 and 39 are redundant with frames 40 and 41.** They teach peak counts, the
   starlet transform and the ℓ1-norm; frame 41 then teaches all three again, better, with the
   shapes of the statistics drawn. Frame 40 explains what a wavelet *is* — and it sits *after* two
   slides that have already used starlets. **Parking 37–39 saves 1:47 and removes a repetition
   the committee will notice.** The beats are written below anyway, marked, in case they stay.
3. **Frames 27 and 28 are twelve clicks of PnPMass flipbook** with no notes, and `STRUCTURE.md` §5
   has said since the Part 1 rebuild that they belong in backup. They are the single largest
   discretionary block in the talk: **1:24**.
4. **Twelve slides' `aside class="notes"` carry `[CLICK]` counts that do not match their own
   fragments** — frame 45 says four clicks and has one, frame 43 says three and has two. The notes
   were written before the builds settled. This script is now the authority; the notes should be
   trimmed to pointers rather than maintained in parallel.

---

# Act 0 — the setup · frames 1–9

Three things this opening must do:

1. Give a wide audience — family, students, two committee members who do not work on lensing — a
   picture of the Universe they can hold for the next forty-five minutes.
2. Make the case for **weak lensing specifically**, not cosmology generally.
3. Land the hinge: **at Stage IV precision, the analysis becomes the limitation.** Every act
   afterwards is an instance of it.

Fixed points (Andreas, 2026-08-26): **ΛCDM**, **cosmological probes**, **Euclid**.

---

## A0.1 — title · frame 1 · 0:27

〔Stand still. Let the chair finish. Look at the room, not the screen. Do not rush this; the
opening thirty seconds are the ones you can least afford to improvise.〕

Thank you, and good morning. Thank you all for coming, and thank you to the committee for reading
this.

This is a talk about how we measure the Universe: what we can learn from the light that reaches us,
and what it takes to trust what we learn from it.

I would like to start with the picture we are trying to fill in.

---

## A0.2 — the picture · frame 2 · 1:06

〔Turn to the screen, orient the room once, then turn back. Give them a couple of seconds to look
before you narrate.〕

This is the history of the Universe as we currently model it. Time runs from left to right, and the
width of the cone is the scale factor — how much the Universe has expanded.

The initial conditions are set very early: a nearly scale-invariant spectrum of small,
close-to-Gaussian density perturbations. Three hundred and seventy-five thousand years in, the
plasma recombines and the Universe becomes transparent. That released light is the microwave
background, and it is a snapshot of those perturbations at redshift about eleven hundred, when they
were still about one part in ten to the fifth.

**▲** After that they grow by gravitational instability. How fast they grow depends on how much
matter there is and on how the Universe is expanding, and that is what turns a nearly smooth field
into the galaxies and clusters we observe.

And in the last few billion years the expansion began to accelerate, which suppresses that growth.

---

## A0.3 — what ΛCDM is, and how you test it · frame 3 · 2:18

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

〔One clause only. A0.4 makes that quantitative; if you explain S₈ here you will say it twice.〕

**▲** So how do you test a model like that? Not by arguing about what Λ *is*. You can put the
acceleration into the geometry, or into the contents, or leave it as a constant of nature, and the
expansion history barely changes.

**▲** You test it by measuring the same few numbers **several independent ways**, and checking that
they agree.

〔That sentence is the hinge into the next slide. Land it and stop.〕

---

## A0.4 — the probes, and the one we follow · frame 4 · 0:52

〔The densest beat in Act 0, and the most important. Do not speed up. The box that lights on the
click is the lensing panel — point at it rather than saying "the bottom right".〕

Different probes measure different combinations of those numbers, which is the reason we use
several.

The microwave background gives the initial conditions and the geometry out to redshift eleven
hundred. Baryon acoustic oscillations use the sound horizon frozen in at recombination as a
standard ruler, which maps the expansion history. Supernovae give luminosity distances. Galaxy
clustering traces the matter, but through galaxies, which are biased tracers, so a bias model sits
between what we count and what we want.

[CLICK] **▲** Weak lensing responds to the total matter directly, and it is sensitive to both the
geometry and the growth at once. That is why this thesis is about lensing, and it is the only one
of these four I will talk about again.

---

## A0.4v — the two tensions · frame 5 · OPTIONAL VERTICAL · 0:47

> **Take this only if the clock is good.** It is a vertical under A0.4, one press of DOWN, and
> nothing later in the talk depends on it. Skipping it costs nothing; taking it costs 0:47. The
> decision is made *on* frame 4, not in advance.

〔If you take it: press DOWN, deliver, press UP, and carry straight on. Do not apologise for the
detour.〕

The consistency between independent probes is itself the test of the model. Measure the initial
conditions with the microwave background, evolve them forward assuming ΛCDM, predict what we should
see today — and then measure it. If ΛCDM is right, those agree.

As the uncertainties fell towards the per-cent level, they stopped agreeing perfectly. The
present-day expansion rate comes out differently from the early-Universe extrapolation than from
direct measurement. And the amplitude of clustering — S-eight, the combination lensing constrains
best — came out about one point seven sigma below the Planck extrapolation in DES and KiDS.

[CLICK] Three ways to read that. New physics. A statistical fluctuation. **▲** Or something in the
analysis itself.

〔Do not resolve it. That third reading is the one this thesis is about, and it is enough to have
said it once.〕

---

## A0.5 — what weak lensing measures · frame 6 · 1:03

〔A new picture, and the last drawing in the introduction — everything after this is data. The
slide has no fragments: it goes up whole. Give the room two seconds to read it before you start
talking over it.〕

Here is the same idea, drawn properly. Follow the light from those distant galaxies on its way to
us.

It does not travel through empty space. It passes every structure that happens to lie along the
way, and every mass it passes bends its path slightly. By the time that light reaches us, the image
of the galaxy is slightly distorted — stretched one way and squashed the other.

For any single galaxy the effect is about a per cent. Far too small to see, and we do not know what
shape the galaxy had to begin with.

**▲** But the distortion is coherent. Neighbouring galaxies behind the same piece of structure are
distorted the same way. So we measure the shapes of very many galaxies and look for that shared
pattern.

That is cosmic shear, and it lets us map the matter back to redshift about three.

---

## A0.6 — Euclid, and what the signal is · frame 7 · 1:08

〔The "and now" beat. Let the clip run behind you; do not narrate the clip.〕

And we are about to be able to do this properly.

Euclid is a European Space Agency mission. It launched in 2023, it is taking data now, and it will
survey fourteen thousand square degrees — about a third of the sky. It will measure the shapes of
billions of galaxies. The first cosmological data release is in June 2027. Rubin will follow from
the ground, and Roman deeper over a smaller area.

**▲** That is roughly an order of magnitude more statistical power than the surveys we have today.

〔The hand-off into the whole rest of the talk. Slow down, stand still, and let the last sentence
land before you click on.〕

[CLICK] **▲** And that signal is worth the trouble, because it is the statistical memory of
everything the Universe has done since the Big Bang. The initial conditions, the growth of
structure, the geometry — all of it is written into how the light was bent on the way here. But
none of it comes out on its own. Getting it out is an algorithms problem.

And that is what this thesis is about.

---

## A0.7 — what it actually takes · frame 8 · 0:47

〔The deck turns from black to paper here. Do not remark on it — let the room notice. This is a
borrowed slide and you must say so.〕

Before I show you my own picture of that, here is an honest one.

This is the DES Year 3 analysis, from pixels to cosmology, and it is Alexandra Amon's diagram, not
mine. Do not try to read it — that is the point.

[CLICK] Nearly every box on it is a paper in its own right, and the great majority of them are
measurement and calibration: modelling the point spread function, calibrating shapes, dealing with
blended galaxies, getting redshift distributions, building covariances. Then analysis choices, and
only at the very end, cosmology.

**▲** A real survey analysis is mostly not the physics. I am not going to talk about most of this.

---

## A0.8 — the chain, and the four questions · frame 9 · 2:59

> The most important slide in the deck and the longest beat in Act 0. The four questions are
> **canonical** — the board at frame 61 asks exactly these, in these words. If you change one here,
> change it there.

〔The thesis statement, and the map for everything after it. Walk the diagram left to right once,
unhurried, touching each box — this is the picture the room sees again at the head of every part.
Then slow right down for the ▲ and let it sit.〕

So this thesis is about the analysis.

Between the galaxy shapes we measure and the cosmological parameters we report there is a chain. A
catalogue of shapes and redshifts. Binned into shear maps. Inverted into mass maps. Compressed into
a summary statistic. Compared against simulations to infer the parameters. And out comes a
posterior.

Underneath runs the other half of it. Cosmologies drawn from a prior, run through N-body
simulations, and then given the systematics — baryons, intrinsic alignments, shape and redshift
calibration — before any of it is compared with the data.

[CLICK] **▲** Every one of those stages is now built out of learned components, and every one of
them can bias the answer, or quietly throw information away, with no internal check noticing.

〔Beat. Then the four questions — one click each. Point at the box that lights up, ask the question,
and let it sit before you move on. Do not race these: this is the map of the whole talk, and it is
the last thing the room gets before the material starts.〕

[CLICK] The first question is about this step here. Shear goes in, a mass map comes out. That
inversion is not a measurement — it is a choice of algorithm, and there are many of them. The field
has always judged those algorithms on how closely the map matches the truth. But the map is not
what we publish; the posterior is. **▲** So: is mass mapping preprocessing, or does the choice of
reconstruction change the cosmology we infer?

[CLICK] Second question, same box. Suppose it does matter. Then we want a reconstruction that is
flexible, fast, accurate, **and** honest about how wrong it is — all four at once, on a survey the
size of Euclid.

[CLICK] The third question moves one step to the right, and then all the way to the end. A mass map
is a hundred thousand correlated pixels. It has to be compressed before anything can be inferred
from it, and then that compressed reading has to become a posterior. **▲** So: what is the most we
can read out of a map, and what does it take to turn that reading into a posterior?

[CLICK] And the fourth question is the one that decides whether any of the rest is usable.
Everything so far assumes the simulations tell the truth. They do not, quite — there is
astrophysics in the real Universe that we cannot model, and it sits on the same scales as the
signal. **▲** Does any of it survive that?

〔Beat.〕

Four questions. Two about the maps, two about the summaries. Each pair asks whether there is
something to gain, and then whether we can actually have it. You will see this picture again at the
head of every part, with one box lit — and we come back to these four at the end, with the answers.

---
---

# Act 1 — Part 1, does the map matter? · frames 10–23

> **Act 1 opens with the formalism block**, moved out of the introduction on 2026-09-06. Shear
> against convergence, the projection integral, and the exact κ–γ relation are Part 1's own
> machinery — the paper is about inverting γ into κ — so they now run straight into *the relation
> is exact, the measurement is not*.
>
> **The consequence for this script is a trim that was owed for a week.** The old A0.6c ended by
> listing noise, masks and the mass-sheet degeneracy; frame 14 is a whole slide about exactly
> those three. A1.4 below now stops at *it is exact* and hands over. The deck forces it: frame 13
> has no fragments at all.

---

## A1.1 — the question · frame 10 · 0:23

〔Act divider. Say the question, then stop. They saw it on the chain ninety seconds ago, so do not
re-argue it — point at the lit box and let the callback do the work. Turn back to the room for the
last line.〕

Question one, and here is the same picture with the same step lit.

Every map-based statistic in this talk starts from a reconstruction. So before anything else: does
the choice of reconstruction change the cosmology we infer, or is it preprocessing?

〔Beat, then turn to the screen.〕 To answer that I have to tell you what is being reconstructed.

---

## A1.2 — shear and convergence · frame 11 · 1:09

〔The first slide that names quantities rather than telling a story, so drop the pace a little and
stand still.〕

So what is it we actually measure?

Take a round patch of sky behind some structure. Lensing does two things to it. It changes the size
of the patch — that is the convergence, kappa. And it stretches the patch one way while squashing
it the other: that is the shear, gamma, two numbers rather than one because a stretch has an
orientation.

Both are second derivatives of the same lensing potential. Two readings of one field.

**▲** But the convergence, the one that *is* the mass, is the one we cannot measure: we never knew
how big the galaxy was to begin with. The shear we can, because it is coherent — every galaxy
behind the same structure is stretched the same way, so with enough of them the shared alignment
lifts out of the noise.

[CLICK] **▲** So we measure the shear and we want the convergence. Getting from one to the other is
a reconstruction, and that is where this thesis starts.

---

## A1.3 — what the convergence is · frame 12 · 0:44

〔Do not read the equation. Point at the two pieces and say what each one carries. The map on the
right is the object every result in this talk is computed on, so let it sit for a beat at the end.〕

And this is what the convergence is. Add up all the matter along the line of sight, weighted by how
efficiently each piece of it lenses — a weight that peaks about halfway to the galaxy whose light
we are looking at.

[CLICK] Two things ride in that integral. The kernel carries the geometry: distances, and the
expansion history. The overdensity carries the growth of structure. **▲** A convergence map
responds to both at once, which is why lensing tests the model rather than measuring a single
number.

And this is what one looks like. Every result I show you is computed on maps like this.

---

## A1.4 — one potential, two observables · frame 13 · 0:30

〔Short, and it must stay short. The whole job of this slide is to establish that a way across
*exists* and is exact. The reason it does not work is the next slide, and if you start listing
noise and masks here you will say them twice.〕

So how do we get from the one to the other?

Both are second derivatives of the same potential, so in Fourier space the relation inverts in a
single line: the mass map is a linear combination of the two shear components. That is
Kaiser–Squires.

**▲** Linear, fast, no free parameters — and on a complete, noiseless field, exact. So there is a
way across, and it is not an approximation.

〔Beat, and change tone for the next slide.〕

---

## A1.5 — the relation is exact, the measurement is not · frame 14 · 1:18

〔The pivot of the act, and the slide the whole of Part 1 rests on. Be precise here, because the
obvious framing is wrong: the problem is not that we are going the awkward way round.〕

The relation is exact. The measurement is not.

We never get to invert gamma, because we never observe gamma. Three things stand between us and it,
and they are all on this line.

**Shape noise.** Every galaxy has its own intrinsic ellipticity, far larger than the shear we are
after — so the shear estimate at any one place is mostly noise, and the inversion amplifies it at
small scales.

**The mask.** The operator is non-local, it mixes Fourier modes, so a hole in the footprint leaves
whole modes the data say nothing about.

**And a blind spot.** Shear cannot see a constant added to kappa. The overall level of the map is
simply not measurable.

Put those together and you get this: a family of maps, visibly different — one sharp, one
noise-dominated, one heavily smoothed — and every one of them fits the measurement.

[CLICK] **▲** So you cannot simply invert. Choosing one means adding an assumption — and that
assumption is not a technicality, it **is** the method.

**▲** Everything in this chapter is a different answer to one question: what do you assume about
kappa?

---

## A1.6 — the standard answer · frame 15 · 0:58

〔Be fair to Kaiser–Squires. It is what the field has used for thirty years and it has good
reasons. The point is not that it is bad, it is that its assumption is invisible.〕

The standard answer is the one we just wrote down: apply the exact inverse anyway.

That is what almost every survey has done for thirty years, and for good reasons — linear, no
tuning, one Fourier transform, and exact if the field were complete and noiseless.

[CLICK] But look at the pair. Same field, same mask. The structure on the left is not there on the
right, and the colour bar on the right spans twice the range of the truth — **▲** that extra range
is noise, not signal. And the mask contour bleeds right across the map, because the Fourier
transform does not know there is a hole.

In practice we control that by smoothing. Which works — but **▲** smoothing *is* an assumption,
applied bluntly and after the fact, and it removes exactly the small-scale structure we came for.

---

## A1.7 — every method is one term · frame 16 · 1:13

〔The organising slide of the act, and the one that makes the next four make sense. Deliberately
*not* Bayesian yet — that is the next slide. Take the methods one at a time; each is a physical
statement about the convergence field, not a piece of machinery.〕

So state the assumption up front instead.

A reconstruction is a fit: the map that reproduces the shear you measured, which is the first term,
and is not absurd as a map, which is the second. **▲** Every method on this slide writes exactly
that problem, and the first term is identical for all of them.

**▲** So the whole history of mass mapping is a history of the second term — what you are willing
to assume a mass map looks like.

[CLICK] Wiener filtering assumes a Gaussian field with a fixed power spectrum. Optimal, if that is
true. But the late-time field is not Gaussian, and the peaks are the whole point.

[CLICK] Sparse recovery assumes the opposite kind of map: mostly empty, a few strong features —
which is much closer to what a field of haloes looks like.

[CLICK] MCALens says you do not have to choose: a smooth Gaussian background *with* sparse peaks on
top.

[CLICK] And deep learning stops assuming and learns the term from simulations. Hold that thought —
it is Part 2.

---

## A1.8 — so write the assumption down · frame 17 · 0:54

〔The **one** place Bayes is taught in the whole talk, so pitch the first paragraph at the widest
person in the room and read the opening sentence almost verbatim. For some of them this is the
first time.〕

And there is a name for what we just did.

**▲** Bayes' rule is bookkeeping for belief. What we should believe about the map after seeing the
data is fixed by two things: how well a candidate map explains the shear we measured, which is
physics we already have — times what we assumed before we looked, which is the prior.

[CLICK] The regulariser was the prior all along. Kaiser–Squires assumed essentially nothing.

[CLICK] Wiener assumes a Gaussian field. [CLICK] Sparse recovery assumes the map is sparse in a
wavelet basis. [CLICK] MCALens assumes it is both at once.

[CLICK] **▲** And the same three terms come back in Part 3, with the cosmological parameters as the
unknown instead of a map — except that there, the likelihood is the one we *cannot* write down.

> **FLAG — say it only if pressed, and say it in Part 2 regardless.** Here we take the *most
> probable* map: a point estimate. Part 2 is where the uncertainty arrives, and Part 3 wants the
> whole distribution. Starck is the likeliest person to ask.

---

## A1.9 — MCALens, and the step Part 2 replaces · frame 18 · 1:27

〔The slide in Act 1 that Part 2 depends on. Land the proximal-operator sentence slowly — PnPMass
is unintelligible without it, and this is the only place it gets said.〕

MCALens is the only method here that does not treat the field as one thing.

It models the convergence as a sum. A **Gaussian** component, handled by a Wiener filter that needs
nothing but the power spectrum. Plus a **sparse non-Gaussian** component in the starlet basis — the
peaks and haloes, which is exactly where the higher-order signal lives.

[CLICK] It solves them by alternating. Fix one component, solve for the other, then swap, and
repeat until the map stops moving.

[CLICK] And each of those solves ends the same way, with a **proximal step**. Thirty seconds on
what that is, because we meet it again and I would rather you had the picture than the definition.

You take a step towards fitting the data and you land somewhere. It fits the shear better than
where you were, and it may be nonsense as a map. **▲** The proximal operator is the correction: it
hands back the nearest map the prior will accept. Near, so you keep the progress you just made;
acceptable, so you do not run away into noise. For sparsity it is simply thresholding.

〔Deliberate pause. This sentence is the setup for the whole of Part 2.〕

Remember that step, because in Part 2 we throw it away and put a neural network in its place.

---

## A1.10 — the stakes · frame 19 · 0:54

〔The divider asked the question; this is where the room learns it was a real question and not a
rhetorical one. Do not rush the last line — it is why the paper exists.〕

So: three methods, three different maps — and every one of them reproduces the shear it was given.

Up to this paper, the way the field compared reconstructions was to measure how close the map came
to the truth, in simulations, against a truth that no real survey will ever have.

[CLICK] **▲** But the map is not what we publish. The posterior is. And nothing in a reconstruction
error tells you what happens to Omega-m, sigma-eight, or w-nought.

So it was genuinely open, and it was argued about — with something concrete riding on it. Euclid
has to pick a reconstruction. If mass mapping is preprocessing, take the cheap one and move on. If
it is not, that choice is a scientific decision, and it should be made deliberately.

---

## A1.11 — the experiment · frame 20 · 0:52

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

## A1.12 — the three maps · frame 21 · 0:39

〔Point at the small scales, and give the room longer than feels natural to actually look.〕

Here are the three reconstructions of the same simulated field.

Kaiser–Squires inverts directly, and because the noise diverges at small scales it has to be
smoothed — so the small scales are simply gone. Inpainting KS fills the mask in first and is
otherwise the same. MCALens is different in kind, and you can see it: the structure survives.

**▲** And read the labels on the right. The two that assume nothing about kappa are what Euclid
plans to run. MCALens is the state-of-the-art alternative. That is the comparison this paper makes.

---

## A1.13 — the answer · frame 22 · 1:13

〔The headline of the act. The whole ladder is on screen at once — there are no fragments here, so
walk it with your hand, not with clicks. Slow down on the two numbers, and do not skip iKS:
reporting the null result is what makes the positive one credible.〕

Same twenty-five simulations, the same peak counts, the same emulator, the same likelihood, the
same sampler. The only thing that changed is the reconstruction.

**▲** And it changes the answer.

Kaiser–Squires sets the baseline at one. Inpainting buys nothing — zero point nine nine six.
**▲** That is a null result and I report it as one: the inpainting acts on the masked regions, and
the peak counts exclude those regions anyway. It would not carry over to a Fourier-space statistic
like the bispectrum, which uses the whole area, and the paper says so.

And MCALens is a factor of two point six. In the paper's convention, a hundred and fifty-seven per
cent.

〔Beat.〕

**▲** Here is the sentence I would most like you to keep. Measured on reconstruction error, MCALens
beats Kaiser–Squires by four per cent. Measured on the figure of merit, by a hundred and
fifty-seven.

Map quality and constraining power are not the same objective. The method that makes the best map
is not the method that gives you the best posterior.

〔If pressed on precision: Chapter 2 reports no error bars — one chain per method. Say it before
someone finds it.〕

---

## A1.14 — where the gain comes from · frame 23 · 0:58

〔The mechanism slide, and the one that survives the closed examination. No fragments: the whole
ladder is up, so point along it. Take the time.〕

So where does it come from?

We can localise it, because the statistic is multi-scale. Start with the coarsest bands only —
sixteen and thirty-two arcminutes, plus the coarse map — and add finer scales one at a time.

Kaiser–Squires improves when you add eight arcminutes. And then it stops: four arcminutes adds
nothing significant, and two adds nothing. MCALens improves at every scale you add, all the way
down to two.

**▲** So the gain is not a global normalisation. It is small-scale reconstruction fidelity —
MCALens recovers structure at scales where the linear inversion has already smoothed itself into
noise, and the higher-order statistic can read it.

〔Beat, and turn back to the room.〕

Which tells you where the effort belongs. The reconstruction is not preprocessing. It is a
scientific choice, and it should be made with the statistic that comes after it in view.

---
---

# Act 2 — Part 2, PnPMass · frames 24–30

> **Frames 27 and 28 are the first thing to cut in the whole talk.** Twelve clicks of the same
> diagram building up, 1:24 of narration, and `STRUCTURE.md` has wanted them in backup since the
> Part 1 rebuild. A2.4 and A2.5 below exist so that the talk *works* if they stay; A2.3 carries a
> tier-0 short path that replaces both in eighteen seconds.

---

## A2.1 — the divider · frame 24 · 0:11

〔The attribution goes here, said once, plainly, and at normal pace. Do not over-explain it and do
not undersell it either.〕

Question two, and the same box lit again.

This chapter is joint work with Hubert Leterme. I co-developed the method, and the uncertainty
quantification is mine.

---

## A2.2 — what we actually want · frame 25 · 1:10

〔The table is a scoreboard, not a reading exercise. Point at columns, not rows.〕

If the reconstruction matters this much, what do we actually want from one?

[CLICK] Four things. It should be **accurate**. **Flexible** — one model that still works when the
noise level or the footprint changes. **Fast** enough to run on a survey. And it should tell you
**how wrong it is**, in a way you can check.

[CLICK] The model-driven methods give you two of the four. Wiener and MCALens are flexible, and
their assumptions are explicit — but Wiener assumes the field is Gaussian, which is the assumption
this whole thesis exists to avoid, and MCALens is slow.

[CLICK] And deep learning has been tried, with several approaches, and it works — the accuracy is
there. But look at the columns that empty out. Each of those networks is trained for one noise
level and one mask, so a change of footprint means retraining; and most of them hand you a point
estimate with no error bar at all.

[CLICK] **▲** Nothing had all four. That empty row is the paper.

---

## A2.3 — the construction · frame 26 · 1:12

〔The one idea in this act. Walk the three lines of algebra once, left to right, and land the last
paragraph slowly.〕

PnPMass.

Remember the proximal step from Part 1 — the one that pulls a candidate map back onto what the
prior allows. The reconstruction is a fixed-point iteration: a gradient step towards consistency
with the measured shear, then that proximal step. Standard forward–backward splitting.

[CLICK] **▲** Plug-and-play replaces the proximal step with a learned denoiser. Instead of writing
a prior down and deriving its operator, we train a network to denoise convergence maps, and let
denoising *be* the prior.

Ours is a Swin-Transformer, seven million parameters, trained once on white Gaussian noise across a
range of noise levels, with the noise level handed to it as an extra input channel.

**▲** And that is the whole point. The denoiser never sees the mask, never sees the survey, never
sees one particular noise level baked into a map. It learns one thing — what a plausible
convergence field looks like. The physics of the observation stays in the gradient step, where it
belongs. Change the noise, change the footprint: the same trained network runs.

> **Tier-0 short path replacing A2.4 and A2.5 entirely** (−1:06). Say this instead of walking the
> flipbooks, and skip both frames:
>
> > Eight iterations of that, alternating data step and denoiser, and the map converges. There is a
> > variant that denoises the residual rather than the map, which does slightly better; the
> > iteration histories are in backup.

---

## A2.4 — the iteration, step by step · frame 27 · 0:32

〔Seven clicks of the same figure filling in. Do **not** narrate every click — start it, say what
changes, then click through the rest in silence while the room watches. Talking over all seven is
the fastest way to lose ninety seconds you needed elsewhere.〕

Here is what that looks like running.

[CLICK] We start from the raw Kaiser–Squires inversion — noise everywhere.

[CLICK] One gradient step towards the measured shear, [CLICK] then the denoiser, and the map
already looks like a map. [CLICK] The next iterations are correcting rather than constructing.

[CLICK] [CLICK] [CLICK] **▲** Eight iterations and it has converged to a fixed point. Not a
network's guess at the answer in one pass — a fixed point of an operator that has the data in it.

---

## A2.5 — the residual variant · frame 28 · 0:29

〔Five more clicks of the same kind. Same rule: start it, then let it run.〕

[CLICK] And there is a variant worth thirty seconds, because it is the one that performs best.

Instead of denoising the map at each step, denoise the **residual** — the difference between where
the data step lands and where you were. [CLICK] [CLICK] The network then only ever sees the part
that is changing, which is closer to the white-noise problem it was actually trained on.

[CLICK] [CLICK] Same eight iterations, slightly better maps.

---

## A2.6 — error bars from one forward pass · frame 29 · 1:22

〔The real result of the act begins here. Read the chain left to right before you say anything
about calibration.〕

The map is only half a result.

Read the chain: the shear goes in, the denoiser gives the map, and then a second network — trained
the same way, on the same simulated pairs — gives the error.

[CLICK] Where does the spread come from, when the reconstruction looks deterministic? Two sources.
Noise and the mask leave a whole family of maps consistent with the data — the fan from Part 1,
which never went away. And the thing that picks one out of that family is a denoiser learned from
simulations, so it brings its own model error. We have to cover both.

The second network is trained on the squared residual of the reconstruction, and the minimiser of
that loss is exactly the posterior variance, pixel by pixel. One forward pass, no sampling.

[CLICK] But a network's own variance is not a guarantee — neural uncertainties are famously
overconfident. So we calibrate: conformalised quantile regression against a held-out set,
distribution-free and finite-sample. It does not require the network to be right.

[CLICK] **▲** That is the shift. Not "the network says plus-or-minus sigma", but a stated coverage
level that holds whether or not the model is well specified.

---

## A2.7 — accurate, and honest about it · frame 30 · 1:35

〔Three panels; the claim is the error bars. Do not let the accuracy comparison become the subject —
it is the setup for the real result. Then slow down for the limitations: volunteering them here
buys you credibility for Acts 3 and 4.〕

This is the whole result in one plot. Reconstruction error across, the size of the calibrated
interval up — down and to the left is better.

**▲** First thing to notice: after calibration, everybody is on the target coverage. That is not a
result, that is the conformal guarantee doing its job. So the comparison is not who covers —
everyone covers. It is who covers with the tightest bars.

**▲** On accuracy: within one per cent of a DeepMass fine-tuned to this exact mask and this exact
noise — from a denoiser that was never shown either. On uncertainty: the smallest calibrated
interval of anything we tested, on all five hundred and twelve test maps.

[CLICK] And it is not a constant interval — here is the map beside its own error bars. It rises
where the structure is, which is what lets the bars stay small everywhere else.

[CLICK] Then deployability, which is the point I care about. DeepMass and MMGAN are retrained
whenever the footprint or the noise changes. We train once. **▲** That is the difference between a
method that wins a benchmark and one Euclid could actually run.

〔Beat. Then the limits, plainly.〕

Two limits. The coverage is marginal, not conditional — it holds on average over pixels, and what
escapes concentrates at the peaks, which is exactly where Part 1 said the information lives. And
this is a single cosmology.

---
---

# Act 3 — Part 3, the summaries · frames 31–53

> **The longest act, and the one with the most to cut.** Frames 37–39 repeat frames 40–41 and are
> written below as PARK beats. There is no *Part 3* divider in the deck: frame 31 opens both
> remaining parts at once. Until that is fixed, A3.1 has to do the naming out loud.

---

## A3.1 — where we are · frame 31 · 0:44

〔Stop and turn back to the room. This is the only structural pause in the second half of the talk,
and it is worth the ten seconds it costs.〕

Stop and look at where we are.

Both projects so far — does the reconstruction matter, and can we build a better one with honest
error bars — live inside a single box of that chain. The map. **▲** Everything else was held fixed
on purpose, so that nothing else could explain what moved.

The rest of the talk moves one box to the right. Those are questions three and four from the board
at the start, in that order: Part 3 builds the statistic that reads the most out of a map, and Part
4 asks whether it survives the astrophysics we cannot model.

---

## A3.2 — same chain, one step to the right · frame 32 · 0:35

〔The same diagram, and you want the room to watch the light move. Point, do not re-describe.〕

Same picture, and watch which boxes light.

[CLICK] A map is a hundred thousand correlated pixels. No likelihood can touch that directly, so it
has to be compressed into a summary — **▲** and which statistic you compress with decides how much
of the information survives the compression.

[CLICK] In Part 1 that box was nailed down on purpose. Now it is the subject: a map goes in, a
summary comes out. We come back to the rest of the chain when we reach the inference.

---

## A3.3 — the baseline everybody uses · frame 33 · 1:06

〔Be genuinely fair here. Half the room has spent a career on two-point statistics and the
committee contains people who will notice if you are not.〕

Start from the thing everybody uses.

The two-point function asks a simple question — take two galaxies separated by some angle, how
correlated are their shapes. You can measure it in real space as xi-plus-minus, or in harmonic
space as C-ell.

[CLICK] And it works. Every flagship cosmic-shear result of the last decade is a two-point
analysis: KiDS, DES, HSC. There are good reasons for that. Theory predicts it analytically, we
understand its covariance, and twenty years of systematics work — intrinsic alignments,
photometric redshifts, baryons — has been built around it. **▲** I am not here to tell you it is a
bad statistic.

[CLICK] Here is the actual issue. For a Gaussian random field the power spectrum is not just a good
summary, it is a *complete* one — the field **is** its power spectrum, and there is nothing else to
know.

**▲** So the question is never whether the two-point function is good. It is whether the field is
Gaussian.

---

## A3.4 — and it is not · frame 34 · 0:21

〔Two frames, one argument. Put the pair up and say almost nothing — the figure is the whole point,
and the room needs a moment to see that the two panels look nothing alike.〕

And gravity has had thirteen billion years to make sure it is not.

These two fields have **the same power spectrum**. One of them is a simulated convergence map; the
other is a Gaussian random field drawn to match it exactly. A two-point measurement cannot tell
them apart.

---

## A3.5 — the cosmic web is in the phases · frame 35 · 0:30

Look at what actually differs. The filaments, the haloes, the voids between them — none of that is
in the amplitudes of the Fourier modes. It is in the **phases**, and a two-point measurement keeps
the amplitudes and throws the phases away.

**▲** Everything that makes the cosmic web a web lives in what the power spectrum discards. To get
at it you need statistics beyond two-point: peaks, wavelets, the ℓ1-norm, Minkowski functionals.

---

## A3.6 — and it is worth having · frame 36 · 0:25

〔A forecast, not a measurement — say so.〕

And it is worth having. These contours are forecasts on the same convergence maps: the power
spectrum, then peak counts after a single Gaussian filter, then peak counts on a multi-scale
decomposition.

**▲** Nothing about the data changed. The only thing that moves those contours is the choice of
summary statistic. That is what makes the choice a scientific one.

---

## A3.7 — peak counts · frame 37 · PARK · 0:21

> **PARK THIS FRAME.** Frame 41 defines peak counts again, thirty seconds later, and draws their
> shape as well. If it stays, this is the beat.

A peak is a local maximum of the signal-to-noise field — the map smoothed by a filter, in units of
the noise. Peaks sit where kappa is high, so they trace the massive structures, and counting them
by height is a one-point statistic that sees exactly what the power spectrum cannot.

---

## A3.8 — one starlet transform · frame 38 · PARK · 0:28

> **PARK THIS FRAME.** Frame 40 explains what a wavelet is, and it comes *after* this slide has
> already used one. Frame 41 then defines the starlet decomposition properly.

A single filter size is a choice, and the wrong one throws information away. The starlet transform
writes the map as a sum of band-pass images, each carrying structure of one characteristic angular
size, plus a coarse map. Count peaks band by band and the analysis is multi-scale from one
transform — and because the bands cover different frequency ranges, the covariance comes out almost
diagonal.

---

## A3.9 — the starlet ℓ1-norm · frame 39 · PARK · 0:19

> **PARK THIS FRAME.** Frame 41 defines the ℓ1-norm with the same formula and shows its shape.

The ℓ1-norm generalises the peak count. Instead of counting maxima, sum the absolute starlet
coefficients in each signal-to-noise bin, band by band. Every pixel contributes — voids as well as
peaks — and there is no threshold to choose and no definition of a peak to defend.

---

## A3.10 — what a wavelet is · frame 40 · 1:38

〔An excursion, and the one place in the talk where the thesis reaches outside cosmology. Two
frames, then move on. The figures teach — these are the words that go with them, not a second
explanation.〕

Two of our three statistics are built on a wavelet transform, so: thirty seconds on what that is.

Everything so far has been Fourier, whose basis is sines — each one a single frequency running
across the whole map. A Fourier coefficient tells you which scales are present and nothing about
where.

**▲** A wavelet is the other trade: a function that is compact and oscillates with zero mean, and
that really is the whole definition. Stretch it and shift it, and the coefficient is the overlap
between the data and one stretched, shifted copy — how much structure of size *a* sits at place
*b*. Do that at every size and you have the transform: each feature answers in the band whose width
matches it, at its own position, and the bands plus the coarse map add back up to the signal
exactly.

[CLICK] Same operation on a convergence map. **▲** And here is why it suits this field: a
convergence map is not a smooth wash, it is made of objects that have a size and a place — clusters,
filaments, voids. So each structure lands in one band at its own position, and a handful of large
coefficients carry the field.

That is the same sparsity the reconstruction prior in Part 1 exploited — and it is why the scales
can be handled one at a time, which will matter in Part 4.

---

## A3.11 — the two statistics · frame 41 · 1:39

〔Four clicks: define a statistic, then show its shape. Do not read the formula. **Do not quote the
band labels on the figure** — it is a thesis illustration at a finer pixel scale than our analysis.〕

So here are our two higher-order statistics, and they are both one-point statistics — histograms of
pixel values — made multi-scale by that same starlet transform.

[CLICK] Peak counts first: find the local maxima of the signal-to-noise field, and histogram them
per bin. Simple, well established, and it keeps only the discrete features.

[CLICK] And this is what that looks like, scale by scale — the shapes, not the numbers. Note what
separates the scales. They all turn over in the same place, just above a signal-to-noise of one,
and they are stacked in amplitude, roughly a factor of four apart, because a coarser band has that
many fewer resolution elements to hold a maximum. And they live almost entirely on the positive
side. That is what "only the discrete features" means.

[CLICK] The ℓ1-norm generalises it: instead of counting maxima, sum the absolute coefficients in
each signal-to-noise bin. **▲** Every pixel contributes, voids as well as peaks, and there is no
feature-detection step to define or tune. That is our analytical hero for the rest of the talk.

[CLICK] And its shape is quite different — bimodal, a hump either side of zero and a dip *at* zero,
because a coefficient near zero adds nothing to a sum of absolute values. The left hump is the
voids. **▲** That picture is what "every pixel contributes" means, and it is the reason the
ℓ1-norm carries more than the peaks do.

---

## A3.12 — and then it has to become a posterior · frame 42 · 0:45

〔Same diagram, third time, and now the right-hand end. This is the hinge into the inference
machinery, so make the difficulty explicit rather than sliding past it.〕

Same picture one more time, and now the other end of it. We have a summary; we need a posterior.

[CLICK] **▲** Here is the difficulty that shapes everything after it. For the power spectrum you
can write down a likelihood — Gaussian to good approximation, with a covariance you can model. For
peak counts, for the ℓ1-norm, for anything a neural network computes, you cannot. There is no
analytic form.

[CLICK] So the whole bottom row lights up. The likelihood is replaced by simulations: draw
cosmologies from a prior, run them, apply the systematics, compute the same summary on each one,
and learn the relationship. That is simulation-based inference.

---

## A3.13 — the classical route · frame 43 · 1:08

〔Bayes itself is not the content — everyone here has it, and Part 1 already taught it once. What
is new is the middle term and what it costs.〕

The classical route, in one line, and it is the same rule as in Part 1 with the parameters as the
unknown instead of a map.

[CLICK] All the work is in the middle term, and the classical analysis assumes it is Gaussian in
the data vector. That needs a theory prediction, fast enough for a million sampler calls, and a
covariance. **▲** And the Gaussian form is a claim about the data, not a convenience: it holds when
each data point averages many independent modes — which is exactly a band-power of the power
spectrum, and why the field gets away with it.

[CLICK] Then you sample: MCMC walks parameter space and hands back the posterior.

**▲** And that is the hinge. Both ingredients had to be written down, and for peak counts or the
ℓ1-norm there is no analytic prediction for the mean, and the distribution is not Gaussian — it is
a count statistic in the tail of a non-Gaussian field.

---

## A3.14 — generative modelling · frame 44 · 1:02

〔The one moment in the talk that reaches outside cosmology, and worth the thirty seconds precisely
because the room has been hearing about these models for three years. Then get off it.〕

So we need different machinery, and it comes from a part of machine learning most of you have been
reading about.

Generative modelling: you are handed examples and you want the distribution they came from. The
middle panel is all you ever have — a finite sample. The left is the truth, which you never see;
the right is what a model believes after seeing the middle one.

[CLICK] **▲** And here is the point that matters for us. Once trained you can always *sample* such
a model — but you cannot always *evaluate* its density. A GAN will generate a face and cannot tell
you how probable it was. For inference we need the density, because the density **is** the
posterior.

[CLICK] And none of it cares what x is. Those are generated faces four years apart; the thing we
use for cosmological inference is the same object.

---

## A3.15 — normalizing flows · frame 45 · 1:08

〔One click only on this slide, whatever the notes on it say. Walk the picture: a Gaussian, bent,
stretched, bent again.〕

So we need a way to represent a distribution that is three things at once: flexible enough to be an
arbitrary posterior, samplable, and with a density we can evaluate. **▲** Those three rarely come
together — a histogram is not flexible, a GAN gives no density, an MCMC chain gives samples but no
normalised density either.

A normalizing flow gets all three. Start from a unit Gaussian, which you can sample and evaluate
trivially, and push it through a learned invertible map. Because the map is invertible the density
comes along with it, by change of variables — and the engineering trick is to build each layer so
its Jacobian is triangular, so the determinant is a product down the diagonal. You fit it by
maximum likelihood, which is gradient descent.

[CLICK] **▲** And the last step is the one that matters here: condition every layer on some data,
and instead of one distribution you have a family — a posterior you can fit.

---

## A3.16 — simulation-based inference · frame 46 · 1:24

〔Three stages, one click each. The last click is the one that matters and it is not the obvious
one, so do not let it become a footnote.〕

Which gives us this.

The problem, stated plainly: for the statistics we care about we have no accurate analytical
likelihood — but we do have a simulator. We can *draw* from p of x given theta even though we
cannot evaluate it. So stop trying to evaluate a likelihood, and learn the posterior instead.

[CLICK] Stage one, the physics half. Draw parameters from the prior, run the forward model, keep
the pair. A few hundred thousand times. **▲** This is the expensive part, and it is the only
expensive part.

[CLICK] Stage two, the learning half. Those pairs are the training set for a conditional flow — the
object from the last slide, with every layer conditioned on the data vector. The optimum of that
loss is the true posterior.

[CLICK] Stage three: hand the trained flow the real observation and read the posterior straight
off. No sampler, milliseconds. **▲** And the reason that matters is not convenience. Because
inference is now essentially free, we can afford to run it on thousands of simulated observations
and check that the posteriors are actually calibrated — which is not a luxury when the likelihood
was never written down and nothing else would catch a bad one.

---

## A3.17 — the objection I would raise myself · frame 47 · 0:53

〔A hinge, not a result. Keep it short, and do not front-load the answer.〕

So we have a statistic that reads more than the power spectrum. But look at the middle box again:
the summary is the one part of this chain we still choose *by hand*.

And the field increasingly fills that box with a neural network trained to compress the maps —
which is routinely described as optimal. **▲** If that is true, why hand-build a statistic at all?

[CLICK] Take the objection seriously, because it is the one I would raise. The honest answer is
that the optimality claim is nearly always demonstrated against the power spectrum — which any
non-Gaussian summary already beats — and rarely against a strong hand-crafted higher-order
statistic under matched conditions.

**▲** So the question is open. That is what we set out to close.

---

## A3.18 — what "optimal" means here · frame 48 · 0:48

〔The definition the whole result rests on. Say it once, precisely.〕

And you have to be careful what optimal means, so here is the one we use.

Train the compressor and the flow together, and maximise the **mutual information** between the
summary and the parameters. That is variational mutual information maximisation, and in practice it
is the same objective as before — maximise the log-posterior of the parameters given the compressed
map.

[CLICK] **▲** The point is that this is not just another statistic to compare against. A network
trained this way is an estimate of the **ceiling** — the most any summary of these maps could
carry.

[CLICK] So if a hand-built statistic reaches it, that is not a win over a baseline. It is a
sufficiency result.

---

## A3.19 — a fair comparison · frame 49 · 0:23

〔Fast and flat, like A1.11. Its only job is to make the result unimpeachable.〕

Same maps, two summaries, the same flow, the same calibration.

Flat-sky ten-degree patches, so that any cross-maps we build later are physically constructible
from a single patch. Both arms calibrated. Three hundred and twenty-four thousand patches over
eight hundred and ninety-nine cosmologies — **▲** enough that whatever gap we see is the
compressor, not data scarcity.

---

## A3.20 — read bin by bin, the ℓ1-norm trails · frame 50 · 0:54

〔Report the observation. Note the asymmetry. **Do not** diagnose it — the next two slides are the
experiment that finds out, and asserting the cause here costs you the payoff.〕

And read bin by bin, the network wins.

The CNN posterior is tighter: a three-parameter figure of merit of three thousand three hundred and
twenty-six against two thousand four hundred and forty-eight. About thirty-six per cent.

[CLICK] Now — the two arms are not reading the same thing. The lensing kernels overlap while the
shape noise is independent, so the redshift bins carry genuinely correlated information. All four
maps enter the network's first convolutional layer together. The ℓ1-norm is computed one channel at
a time, and only ever sees the one-dimensional marginals.

**▲** That is an observation about how the comparison is set up, not yet a diagnosis. It might
account for all of the gap, some of it, or none. So close the asymmetry and measure what happens.

---

## A3.21 — tomography · frame 51 · 0:22

〔Eight clicks of one picture assembling. Start it, say the two sentences, and let the rest run in
silence.〕

[CLICK] [CLICK] The sources are sliced in redshift, [CLICK] [CLICK] and each slice gives its own
convergence map.

[CLICK] [CLICK] **▲** But the lensing kernels are broad and they overlap — a structure at low
redshift lenses every bin behind it. [CLICK] [CLICK] So the bins are not independent measurements;
they share information, and something has to read that shared part.

---

## A3.22 — two places to intervene · frame 52 · 1:31

〔The methods slide of the paper, and the densest thing in Act 3. Take it slowly, and land the last
sentence — it is the reason the joint ℓ1-norm exists.〕

The gap is structural, so there are exactly two places to intervene: the input, or the statistic.

[CLICK] **Route one**, the obvious one: manufacture the missing channel. For each pair of bins,
multiply the two maps pixel by pixel. The product is near zero almost everywhere and lights up only
where both bins have structure in the same place, so its one-point statistics carry the joint
structure of the pair. Six pairs, six new channels, and the *same* ℓ1-norm runs on each. Built from
the patch's own two maps, so a survey observing only that patch could actually form them.

[CLICK] **Route two**: leave the four maps alone and change what the statistic reads. At a given
scale, every pixel hands you all four bins' coefficients at once. The per-bin ℓ1-norm is the
absolute-value-weighted one-dimensional histogram of each — literally the two curves on the edges
of this figure. Lay a fixed ten-by-ten grid on the pair plane instead, and sum the ℓ1 weight of the
pixels landing in each cell. That is the joint ℓ1-norm.

[CLICK] **▲** And here is the difference that matters. The product map reduces a pair of bins to a
single derived field *before* the statistic is taken. The joint ℓ1-norm never reduces it — and it
needs no new map at all.

---

## A3.23 — the answer · frame 53 · 1:00

〔THE headline of the act. Build it arm by arm, and be exact about what it is and what it is not.〕

So: same maps, same flow, four summaries.

[CLICK] The ℓ1-norm read one bin at a time: two thousand four hundred and forty-eight.

[CLICK] Add the product cross-maps: three thousand and forty-five. Better, and not enough.

[CLICK] The joint ℓ1-norm — the statistic from the last slide, no new maps, no training: three
thousand three hundred and seventy-one.

[CLICK] And the CNN lands at three thousand three hundred and twenty-six. **▲** On top of it. Not
above it.

〔Beat. Then be precise, because this is the sentence the committee will test.〕

**▲** That is a tie, and I want to call it a tie rather than a win. The network's coverage is
mildly conservative, which plausibly accounts for the analytical statistic sitting a hair above.
The claim is that both summaries appear to saturate the information these maps make accessible —
sufficiency as far as we can measure it.

And the tie holds on every parameter, over nine thousand mock observations.

---
---

# Act 4 — Part 4, baryons and nulling · frames 54–60

> There is no *Part 4* divider either. A3.23 ends on a result and A4.1 opens a new paper; the turn
> has to be made with your voice.

---

## A4.1 — the collision of scales · frame 54 · 1:25

〔Turn back to the room for the first sentence — it is a change of subject, and the deck does not
mark it. Then let them read the figure before either band appears.〕

Everything so far has been on clean simulations. **▲** Stage IV is not statistics-limited any more,
it is systematics-limited — so what decides whether higher-order statistics can be used is not how
much they gain, it is how they behave under contamination.

And the worst offender is baryonic feedback: AGN and supernovae push gas out of haloes and suppress
the matter distribution on small scales, in a way that mimics a cosmological signal.

〔Point at the figure. Let it sit.〕

**▲** Here is the problem in one picture. The information beyond two-point lives at small scales.
The contamination lives at small scales. They are the same scales, and it is where the feedback
models disagree with each other most.

The conservative response is to throw the affected scales away. The question is what that costs,
and there are two ways it could go.

[CLICK] **Optimistic**: only the very smallest scales are touched, we cut them, and most of the
non-Gaussian information is still there.

[CLICK] **Pessimistic**: the contamination reaches much further, and once you have cut it there is
nothing beyond-Gaussian left worth having — the power spectrum would have done just as well.

**▲** Which of those is true is an empirical question, and it is the first thing we measured.

---

## A4.2 — the pipeline, again · frame 55 · 0:31

〔A deliberate refresher — it has been a while since the general SBI slide. Walk it quickly and do
not linger on the machinery. One detail is load-bearing; everything else is scenery.〕

Same machinery as before, quickly. [CLICK] Convergence maps from CosmoGrid, [CLICK] Euclid-like
noise added, [CLICK] wavelet transform, summary statistics, [CLICK] conditioning a normalizing
flow, and the posterior comes off it.

**▲** The one detail that matters for everything after this: the statistics are measured on each
wavelet band **separately**, so the data vector is organised by scale. That is what makes a scale
cut possible at all — a contaminated band can be dropped without touching the rest.

---

## A4.3 — how big is the bias · frame 56 · 0:58

〔Seven clicks building the two panels. The number to protect is the *ordering*, not the decimals.〕

So: how badly are we biased if we do nothing?

[CLICK] [CLICK] At a Stage IV area — fourteen thousand square degrees — the power spectrum shows a
two point two sigma shift. [CLICK] [CLICK] Peak counts and the ℓ1-norm show three point six.

[CLICK] [CLICK] And it gets worse with area, because more area means smaller error bars and
therefore more sensitivity to a fixed systematic. At full sky the power spectrum reaches about
three and a half sigma and both higher-order statistics exceed six.

[CLICK] **▲** Two things to be clear about. This is at full map resolution — no scale cuts yet, so
it is what you get if you use everything the maps offer. And the higher-order statistics are *more*
biased than the power spectrum, not less, precisely because they live on the contaminated small
scales. That is the honest starting point.

---

## A4.4 — what it costs to buy back · frame 57 · 1:02

〔Be scrupulously fair to the power spectrum here. The wavelet cut is *coarser*, and saying so is
what makes the next slide credible.〕

So we cut. The criterion is to bring the baryonic bias below three tenths of a sigma, and the two
statistics pay for it in different currencies.

[CLICK] The power spectrum takes a **sliding** cut, tuned to what is safe at each area: an
ell-max of eight hundred and sixty at two thousand square degrees, falling to three hundred and
forty at full sky. A large fraction of its range — but removed *precisely*.

The starlet concentrates the contamination in its finest band, so dropping that one band is enough
at every area. **▲** But the bands are dyadic, so whole-band removal is the only cut available, and
at the smaller footprints that certainly throws away uncontaminated quasi-linear information a
finer filter bank would have kept.

**▲** So the wavelet cut is not better. It is coarser, and therefore conservative. Everything on
the next slide is a floor.

---

## A4.5 — is there anything left · frame 58 · 1:23

〔The answer to question four, and the numbers matter. Be precise about the peak counts — the
temptation is to let them disappear into "the higher-order statistics", and that would be
overclaiming.〕

And the answer is yes.

[CLICK] On baryon-safe scales the starlet ℓ1-norm constrains **one point eight times** tighter than
the power spectrum at Stage IV, and **two point six times** tighter at full sky.

[CLICK] Be precise about the peak counts, because they are the weaker of the two. They reach
approximate parity with the power spectrum at Stage-IV areas and slightly exceed it at full sky; at
the smaller footprints they trail it. **▲** And the reason they trail is largely the cut, not the
statistic — the whole-band removal takes a larger fraction of the peak-count information than the
sliding ell-max takes from the power spectrum, and that penalty is worst exactly where the
power-spectrum cut is loosest.

[CLICK] Even at comparable figure of merit they are not redundant: in the planes involving w-nought
the degeneracy directions differ, so a joint analysis would still gain.

[CLICK] [CLICK] **▲** Two things I want to leave you with. The signal survives on *quasi-linear*
scales — these are not only deep-non-linear probes, which is what people assume. And this is a
floor: our cut is not optimised, and a finer filter bank or a cut in signal-to-noise rather than in
scale would recover more.

---

## A4.6 — nulling, and what goes wrong · frame 59 · 1:37

〔The third result, and it stands on its own. Plant the parenthesis about the cross-spectra and do
*not* explain it — it pays off on the next slide. Then pause on the paradox.〕

The third thing we looked at is a way of making those cuts less blunt.

Nulling — the BNT transform — is a linear re-mixing of the tomographic bins that cancels the
low-redshift lensing efficiency. Why anyone wants it: the standard kernels are broad and
overlapping, so one angular scale mixes low-redshift small scales with high-redshift large ones,
and an angular cut throws away clean high-redshift information along with the contamination. Null
the bins and each transformed field is localised in redshift, so you cut scales only where the
systematic is. **▲** A genuinely promising way to do scale cuts — and for the power spectrum it
works, provided you keep the cross-spectra between transformed bins.

[CLICK] Applied to a map-based higher-order statistic, it backfires. The same mixing correlates the
originally-independent shape noise across bins, the noise floor rises, and the contours **inflate**
— worse than standard tomography even with conservative cuts.

[CLICK] [CLICK] 〔Pause here.〕 And that should be impossible.

**▲** BNT is a fixed, invertible matrix. The Jacobian cancels in Bayes' rule, the Fisher
information is unchanged, and the posterior from the full field is identical in both frames. And
yet the ℓ1-norm keeps sixteen per cent.

We are not alone in hitting this: the Euclid analysis of Vinciguerra and collaborators this year
kept tomographic maps for bin combinations up to quadruplets and still concluded that recovering
the signal-to-noise was, in their words, highly non-trivial.

---

## A4.7 — and the answer was already in the room · frame 60 · 1:35

〔The best moment in the talk, because the answer is the statistic built two slides earlier for an
unrelated reason. Build the ladder, then cash the parenthesis from A4.6.〕

So we asked what it takes to get the information back, and ran the same four summaries through the
nulled frame.

[CLICK] The per-bin ℓ1-norm keeps sixteen per cent. [CLICK] Add one derived field per pair — the
product cross-maps — and it is twenty-four. Better, nowhere near.

[CLICK] The joint ℓ1-norm, the statistic we built two slides ago for a completely different reason,
keeps **seventy-two** per cent.

[CLICK] And the CNN, which reads all four channels natively, shows **no measurable loss** at all.

[CLICK] **▲** In the standard frame those four summaries spanned thirty-eight per cent. Here they
span a factor of six. The transform did not destroy information — it moved it somewhere only a
summary that reads the bins jointly can see.

〔Now cash the parenthesis.〕

**▲** And the power spectrum was the first rung of this same ladder all along. Auto plus cross
spectra are closed under the transform, and so exactly invariant; the auto-spectra alone keep only
the diagonal, and are not. That is the same statement.

**▲** So the practical message, for anyone planning a nulled analysis: nulling need not cost a
higher-order analysis anything, provided some stage of the pipeline reads the bins jointly.

〔The honest residual — say it, do not wait to be asked.〕

The joint ℓ1-norm keeps seventy-two per cent, not all of it. The remainder is genuine three- and
four-bin structure that a pairwise statistic cannot reach, and that is the one place the network
keeps an advantage.

---
---

# Close · frames 61–62

## C.1 — back to the four questions · frame 61 · 0:08

〔A return, not an opener. Do **not** read them out again in full — point along them and let the
room re-read. They have seen these words once, at frame 9, and that is what makes this land.〕

Those were the four questions I put up at the start, in the same words.

〔Point along the four, one beat each, in silence.〕

Here are the answers.

---

## C.2 — conclusions · frame 62 · 1:34

> **⚠ THE SLIDE DOES NOT MATCH THIS BEAT YET.** Frame 62 still answers an older set of three
> questions — deep learning, baryons, nulling — numbered Q1–Q3, which collides with the canonical
> four. Three backup frames carry those old tags too. **The beat below is written for the four, and
> is the specification for the rebuild.** Until it is rebuilt, deliver C.2 from this text and
> ignore the numbering on the screen.

〔Land each answer and stop. Four sentences, four beats. Do not add anything.〕

**Question one.** Mass mapping is not preprocessing. Swap the reconstruction and nothing else, and
the figure of merit moves by a hundred and fifty-seven per cent — while the reconstruction error
moves by four. **▲** Map quality and constraining power are different objectives, and the
reconstruction should be chosen with the statistic that follows it in view.

**Question two.** Yes — PnPMass is accurate to within a per cent of a network fine-tuned to the
observation, has the smallest calibrated error bars of any method we tested, and is trained once
rather than per footprint. **▲** Which is what makes it a method a survey could actually run.

**Question three.** No, we do not need a neural network to read the maps. Build joint reading into
the statistic, and a fixed wavelet ℓ1-norm matches an information-optimal learned compressor — with
no training at all.

**Question four.** Baryonic feedback does not put it out of reach. Cut every contaminated scale and
the ℓ1-norm is still one point eight times tighter than the power spectrum at Stage IV, two point
six at full sky. **▲** And redshift nulling stays usable as a mitigation, at no cost in
constraining power, provided some stage of the pipeline reads the bins jointly.

[CLICK] 〔The references come up. One sentence, then stop and turn to the chair.〕

Those last two are the papers in preparation and in press — both on arXiv this month.

Thank you.

---
---

# The arithmetic, and how to close it

**Measured: 60:46 against a 40:00 target.** Over by **20:46**. That is not a rounding problem and
it will not come out of shaving sentences — the main line has grown to **62 frames**, and 62 frames
is an hour-long talk at any honest speaking rate.

| act | frames | measured | share |
|---|---|---|---|
| Act 0 — the setup | 1–9 | 11:27 | 19 % |
| Act 1 — Part 1 | 10–23 | 13:11 | 22 % |
| Act 2 — Part 2 | 24–30 | 6:31 | 11 % |
| Act 3 — Part 3 | 31–53 | 19:24 | 32 % |
| Act 4 — Part 4 | 54–60 | 8:30 | 14 % |
| Close | 61–62 | 1:42 | 3 % |

**The imbalance to look at is inside Act 3.** Frames 33–48 are **13:08 of teaching** — two-point
statistics, the phases, peaks, wavelets, Bayes, generative models, flows, SBI — in front of
**4:20** of the paper's own results. A defense can carry some pedagogy. A third of the talk is too
much, and it is where the cuts should come from first.

## Tier 1 — park what is redundant or superseded · −3:27 · lands at 57:19

Nothing is lost. Each of these is either said again elsewhere or already marked for backup.

| frames | what | saves |
|---|---|---|
| 37, 38, 39 | peaks, starlets, ℓ1-norm — all three defined again on frame 41, with the shapes drawn | **−1:08** |
| 27, 28 | the PnPMass flipbooks; `STRUCTURE.md` has wanted them in backup since the Part 1 rebuild. Use A2.3's tier-0 short path | **−1:01** |
| 55 | the SBI pipeline refresher; A3.16 taught the same pipeline twelve minutes earlier | **−0:31** |
| 5 | the two tensions — already an optional vertical, so this costs a keystroke, not a slide | **−0:47** |

## Tier 2 — park teaching whose content survives elsewhere · −3:24 · lands at 53:55

| frames | what | saves |
|---|---|---|
| 44 | generative modelling and the faces. Charming, and the only thing it is load-bearing for is the density-versus-samples point, which fits in one sentence of A3.15 | **−1:02** |
| 45 | normalizing flows. Fold *flexible, samplable, evaluable* into A3.16's first paragraph and show the flow only as part of the SBI diagram | **−0:50** net |
| 43 | the classical Bayes route. Bayes is taught properly at frame 17; keep only *for these statistics there is no likelihood*, which A3.12 already says | **−0:45** net |
| 36 | the forecast contours. Frame 41's statistic shapes make the same point with the actual statistics | **−0:25** |
| 51 | the tomography build. Eight clicks for a fact A3.20 states in a sentence | **−0:22** |

## Tier 3 — prose, inside beats that stay · −5:50 · lands at 48:05

| beat | cut | saves |
|---|---|---|
| A0.3 | the three annotated questions on the cone. Keep *phenomenological*, drop the one-line-each sequence | −0:35 |
| A0.8 | ask questions two and four in one sentence each; one and three carry the argument | −0:35 |
| A1.5 | name the three obstacles, do not explain each. The slide explains them | −0:25 |
| A1.7–A1.8 | merge the narration: *the regulariser was the prior all along* covers both slides | −0:35 |
| A1.9 | the proximal-operator paragraph down to the ▲ sentence and the thresholding clause | −0:30 |
| A2.2 | skip the four-requirement enumeration; go straight to *nothing had all four* | −0:40 |
| A2.6 | the two-sources-of-spread paragraph to one line | −0:25 |
| A2.7 | drop the deployability paragraph — it is on the slide, and A2.3 already said *trained once* | −0:30 |
| A3.3 | drop the list of reasons the field uses two-point; *it works, and here is why that is not the issue* | −0:25 |
| A3.10 | the wavelet definition down to the ▲ sentence and the figure walk | −0:35 |
| A3.22 | narrate route two only; point at route one and say *the obvious thing first, and it is not enough* | −0:35 |
| A4.4 | drop the sliding-cut multipole numbers; *a large fraction of its range, removed precisely* | −0:20 |
| A4.6 | drop the Vinciguerra citation from the spoken text; keep it for questions | −0:20 |

## The last 8:05 — a whole-act decision, and it is yours

Tiers 1–3 leave **48:05**. The guidelines are right that the honest way to close a gap this size is
to cut a whole act rather than shave further, and there are three ways to do it. Each is coherent;
none is free.

**Package A — reduce Part 2 to three frames** (24, 26, 30). Drops A2.2 and A2.6, **−2:30**, leaving
Part 2 at 2:58: the divider, the construction, the result. Question two still gets a real answer,
and the conformal-prediction machinery moves to Q&A.

**Package B — collapse Act 3's inference machinery** (keep 46 only; park 42, 47, 48 as well as
42/43/44/45 from tier 2). **−2:26.** The room is told there is no likelihood, that we replace it
with the simulator and a flow, and that the network is trained to be information-optimal — in one
slide instead of six. Costs the *why is this the ceiling* argument, which is what makes A3.23 a
sufficiency result rather than a benchmark win. **This is the one I would fight to keep.**

**Package C — reduce Act 1's method survey** (park 16 or 17, and 21). **−1:33.**

**Recommendation: A + B + C together lands at 41:36** — a 45-minute slot with real slack, and
1:36 above the target rather than 20:46 above it.
If only one can be taken, take **A** — it is joint work, Hubert is the first author, and it is the
only act where a compression does not cost an argument you make yourself.

**Never cut, at any tier:**

- A0.8's four questions. The whole talk is hung on them and the close returns to them.
- A1.13's *four per cent against a hundred and fifty-seven* contrast, and the iKS null result.
- A1.5's *the added assumption **is** the method* ▲.
- A2.7's two limitations, and A2.3's *never sees the mask* ▲.
- A3.3's *the question is whether the field is Gaussian* ▲, and the phases pair (34–35).
- A3.18's definition of optimal — without it A3.23 is a benchmark win rather than a sufficiency
  result.
- A3.23's *that is a tie, and I want to call it a tie*.
- A4.4's *the wavelet cut is coarser, and therefore conservative*.
- A4.7's honest residual, and the *provided some stage reads the bins jointly* clause.

---
---

# Q&A — tier 1, the room

Five to fifteen minutes, general audience plus the two committee members who do not work on
lensing. Short answers. Do not reach for the backup deck unless the answer needs a figure.

**"Why do you need simulations at all — can't you just do the theory?"**
For the power spectrum we can, and the field does. For peak counts or the ℓ1-norm there is no
analytic prediction for the mean, and the distribution is not Gaussian — it is a count statistic in
the tail of a non-Gaussian field. So the simulator replaces the formula. The cost is that the
answer is only as good as the simulations, which is exactly why Part 4 exists.

**"How do you know the machine learning is not just making things up?"**
Two answers. The reconstruction never leaves the data behind — the network is one step inside an
iteration whose other step is a gradient towards the measured shear, and it converges to a fixed
point of that pair. And for the inference we test it: because the trained flow answers any new
observation in milliseconds, we can run it on thousands of simulated observations where we know the
truth and check the posteriors actually cover. That is frame 73 in the backup.

**"Isn't 157 per cent suspiciously large?"**
It is a figure of merit, which is an inverse area in parameter space, so it moves faster than an
error bar. In linear terms it is about a factor of one and a half on each parameter. And it is a
*ratio* between two chains that differ in one step, so the systematics that would inflate an
absolute number cancel.

**"What happens when Euclid data actually arrive?"**
Everything in Parts 1, 3 and 4 is a forecast on simulations, deliberately — you cannot validate a
reconstruction without a truth. What transfers directly is PnPMass, which is trained once and takes
the mask and the noise at inference, and the ℓ1-norm pipeline, which needs only the simulation suite
to be run at the survey's own noise and footprint.

**"Why weak lensing rather than galaxy clustering?"**
Lensing responds to the total matter, so there is no galaxy-bias model between what we count and
what we want. And it is sensitive to the geometry and the growth at once, which is what makes it a
test of the model rather than a measurement of one number.

**"What is the single most important thing in the thesis?"**
That the analysis choices are not neutral. Two of the four results are the same shape: a step
everyone treats as preprocessing — which reconstruction, which frame the bins are in — turns out to
change the answer, and the fix is available if you look for it.

---

# Q&A — tier 2, the closed examination

One to three hours, seven people who have read the manuscript. These are ordered by how likely I
think the question is, and the first is the one I would ask myself.

**1. "You compare against a CNN. Did you try hard enough to make the CNN win?"**
The honest form of the objection, and it deserves the working. Getting the network to 3326 took an
expressive flow — RealNVP, worth +36 % — and a better architecture, resnet18, worth a further 6 %.
Going deeper than that *overfits* at 899 cosmologies. So the network is not undertrained; it is at
the point where more capacity costs accuracy on this training set. **The honest converse:** with a
much larger simulation suite the network would very likely pull ahead again, and the tie is a
statement about the data volume a Stage-IV analysis actually has, not a theorem.

**2. "A tie is not a win. Why prefer the analytical statistic?"**
Given equal constraining power, everything else decides: no training, no architecture search, no
retraining when the footprint or the noise changes, an interpretable data vector you can cut band
by band — which is exactly what Part 4 needs — and a covariance that is nearly diagonal by
construction. And the nulling result: the analytical statistic degrades gracefully in a transformed
frame and you can see *why*, where the network is a black box that happens to survive.

**3. "The joint ℓ1-norm keeps 0.72 under nulling, not 1. What is the missing 0.28?"**
Genuine three- and four-bin structure. The joint statistic is pairwise by construction, and
pairwise is the ceiling a patch can actually populate — a four-dimensional histogram over K⁴ cells
against 80 × 80 pixels is almost everywhere empty. So the residual is real, it is where the network
keeps an advantage, and I would not claim otherwise.

**4. "Chapter 2 quotes no uncertainty on the 157 per cent."**
Correct, and it is a limitation. One chain per method, 25 cosmologies. The ordering is robust — the
scale ladder in frame 23 is an independent check that the gain is small-scale reconstruction
fidelity rather than a normalisation — but I would not defend the third significant figure.

**5. "Your wavelet scale cut is cruder than the power spectrum's. Is the comparison fair?"**
It is unfair *against* us, and I say so on the slide. The power spectrum gets a sliding ell-max
tuned to each area; the starlet can only drop whole dyadic bands, so at the smaller footprints we
certainly throw away uncontaminated quasi-linear information. A √2 or non-dyadic filter bank would
allow an area-tuned cut. And there is a better cut available in principle: the statistics are
binned in signal-to-noise as well as scale, and the baryonic response sits in the positive tail, so
the contamination could be removed where it sits rather than by removing a band. Future work, and
everything in Part 4 is a floor because of it.

**6. "You use one feedback model. What if the real Universe is worse?"**
Then the bias is larger and the cut is deeper — the *scaling* with area is the robust part, not the
absolute sigma. The mitigation strategy does not depend on which model is right, because it is
defined by a bias criterion, not by a feedback amplitude.

**7. "PnPMass: what does 'converges' actually mean here, and does it?"**
Fixed-point convergence of the forward–backward iteration with a learned operator in the backward
step. It is not free — the denoiser has to be non-expansive for the classical guarantees, which is
a real condition and the reason the training uses white Gaussian noise across a range of levels
rather than the actual observation. In practice eight iterations, and the residual variant is
better behaved than the map variant.

**8. "Marginal coverage is a weak guarantee."**
Agreed, and it is the limitation I would attack. It holds on average over pixels; the miscoverage
concentrates at the peaks, which is where Chapter 2 just argued the information lives. Conditional
coverage — per-pixel, or conditional on local signal-to-noise — is the obvious next step, and
conformal methods for it exist.

**9. "Why should nulling inflate anything if the transform is invertible?"**
It should not, and that is the point of the result. The Jacobian cancels in Bayes' rule, the Fisher
information is unchanged, and the posterior from the *full field* is identical in both frames. What
changes is what a *given summary* can see: the transform correlates the originally-independent
shape noise across bins, and a summary that only reads one-dimensional marginals loses the part
that has moved into the correlations. The power spectrum is the two-point instance of exactly the
same statement — auto plus cross spectra are closed under the transform and exactly invariant, the
autos alone are not.

**10. "Is the ℓ1-norm actually new? Ajani et al. published it."**
The starlet ℓ1-norm is Ajani, Starck and Pettorino. What is new here is the joint reading — the
pairwise ℓ1 on the coefficient plane — and the demonstration that it closes the gap to an
information-optimal compressor, and that it is what makes nulling survivable.

**11. "Why cosmo-SLICS in Part 1 and CosmoGrid in Parts 3–4?"**
Different requirements. Part 1 needs many cosmologies with matched reconstructions and a truth map,
at DES-like depth. Parts 3 and 4 need a large training set for the flow and a baryonic
implementation. Nothing in either result depends on the suite; the comparisons are internal.

**12. "What would falsify the central claim?"**
A hand-built statistic reaching an information-optimal compressor is a claim about a regime. It
fails if the network can be trained to pull clearly ahead at matched calibration on a larger suite;
it fails if the tie does not survive a realistic mask and a realistic redshift distribution, both of
which are idealised here; and the sufficiency reading fails if VMIM is not actually estimating the
ceiling on these maps.

---
---

# Register notes

- Rehearse in the register you will deliver in. *Measure*, *infer*, *obtain* — not *get*. Under
  pressure you fall back on rehearsed habits, so build the right ones.
- **Numbers out loud, in words**, as written here. "One point eight times tighter", not "one point
  eight ex". A spoken decimal that has to be decoded is a spoken decimal that is lost.
- **Do not diagnose before the experiment.** A3.20 reports a gap and names an asymmetry; the
  diagnosis is A3.22 and A3.23. Asserting the cause early costs the payoff and overclaims.
- **Concede first.** A2.7's two limits, A4.3's *the higher-order statistics are more biased, not
  less*, A4.4's *our cut is coarser*, and A4.7's residual are all volunteered before anyone can
  raise them. That is what buys the rest of the talk its credibility, and it is the pattern the
  committee will be watching for.
- **The four questions are the spine.** If you lose your place, go back to *which of the four am I
  answering* — the room can follow you back the same way.
- Ground analogies in the papers rather than inventing them. *Two auto-spectra never tell you the
  cross-spectrum* is the one to reach for, and it is already the argument in A4.7.

---

# Numbers used, and where they are ledgered

**Act 1** — `PAPER_FACTS.md` §2. Ratios to a KS baseline of 1.00: iKS **0.996**, MCALens **2.57**
(the paper's **+157 %**). RMSE ratios: iKS 1.005, MCALens **0.959** — the four-per-cent figure.
25 cosmologies · DES-Y1, 19 × 100 deg² · starlet scales 2′–32′ + coarse · KS saturates after 8′,
MCALens gains to 2′.

**Act 2** — `PAPER_FACTS.md` §3. RMSE ratios to DeepMass: PnPMass **1.013**, residual variant
**1.006** — quoted as "about one per cent". Smallest calibrated error bars **on all 512 test
images**. SUNet, **7.2 M** parameters. **8** iterations. Target error rate α ≈ 4.55 %.

**Act 3** — FoM₃, matched pipeline: auto-only ℓ1 **2448** · + product cross-maps **3045** · joint
ℓ1 **3371** · CNN-VMIM **3326**. The learned summary is **36 %** ahead of the per-bin ℓ1. Training
set **324 k** patches over **899** cosmologies, flat-sky 10° patches. Ties hold over **9,000** mock
observations. Architecture ladder: RealNVP **+36 %**, resnet18 **+6 %**.

**Act 4** — `PAPER_FACTS.md`, Tersenov+ 2026 A&A. Bias at full resolution, 14,000 deg²: C_ℓ
**2.2σ**, peaks and ℓ1 **3.6σ**; full sky C_ℓ **~3.5σ**, both HOS **> 6σ**. Cut criterion **0.3σ**.
C_ℓ sliding ell-max **860 → 340**; starlet drops **j = 1** at every area. On safe scales, ℓ1 is
**×1.80** tighter at Stage IV, **×2.61** at full sky; peaks **×1.07** and **×1.17**. Nulling
retention: per-bin ℓ1 **0.16**, + product cross-maps **0.24**, joint ℓ1 **0.72**, CNN **~1**
(measured 0.96, quoted as *no measurable loss*).

**Deliberately not said.** Chapter 2's absolute FoM values (758 / 755 / 1947) — ratios only. The
inverse-volume conversion ×2.57⁴ ≈ 43.6: arithmetically right, reads as inflation, stays off the
slide *and* out of the mouth. The Chapter 3 timing table — the argument is that training happens
once, not that inference is fast; leading with speed invites the table, where PnPMass loses per
map. And the band labels printed on frame 41's figure, which are a thesis illustration at a finer
pixel scale than the analysis.
