# STRUCTURE — PhD defense, University of Crete, 14 September 2026

**45 min presentation (mostly uninterrupted) → ~5–15 min questions from the general audience →
closed examination by the committee, 1–3 h.**

Built against `../docs/TALK-GUIDELINES.md`. Sources read in full on 2026-08-25:
`~/Desktop/PhD_thesis/` — abstract (`auxilliaires/resume.tex`), the roadmap and gap statements
(`chapters/introduction/thesis-roadmap.tex`), all four chapter abstracts (`chapters/chap{1,3,2,4}.tex`),
the results sections of all four papers, and `chapters/conclusion.tex`.

**Status: proposal. No slide exists yet. Nothing has been scaffolded beyond this file.**

---

## 0. What is different about a defense

Three structural facts that override the format budgets in §3 of the guidelines, because none of
them describes a defense.

**The presentation and the examination are separate events with separate audiences.** The 45
minutes are for the room: committee, colleagues, students, family. The 1–3 hour examination
afterwards is for seven people who have read the manuscript. Almost everything the guidelines say
about Q&A preparation applies to the *second* event, and the deck has to serve both — a talk that
lands with the room, and behind it a backup library deep enough to survive an hour of
cross-examination. The backup pile stops being a pile and becomes an indexed reference deck.

**The committee already knows the results.** They cannot be surprised by the numbers. What they
can be shown is *coherence* — that the four papers are one program rather than four things that
happened over four years. That is the thing the manuscript is worst at conveying, because a paper
chapter reproduced verbatim carries its own framing, and it is the thing the defense is best at.
So the value the talk adds is the spine, not the content.

**Under-running is a failure mode here, unlike a colloquium.** Hull's "finish early, nobody
complains" holds at a seminar. A 30-minute defense of a four-paper thesis reads as thin.
The target is **40 minutes of measured material** for the 45-minute slot: enough buffer for the
occasional interruption, and no risk of standing there at minute 32.

---

## 1. The three questions

**Primary audience — the seven-member committee, pitched so the room can follow.**
From `main.tex` §Examination committee:

| | | reads this talk as |
|---|---|---|
| Jean-Luc Starck | supervisor, FORTH / CEA | knows it at the level of the code |
| Martin Kilbinger | co-supervisor, CEA | knows it at the level of the code |
| Vasiliki Pavlidou | co-supervisor, U. Crete Physics | the scientific taste and the framing |
| Panagiotis Tsakalides | U. Crete **Computer Science** | conformal prediction, fixed points, flows — his own vocabulary |
| **Frédéric Courbin** | Universitat de Barcelona | **strong lensing, deconvolution, inverse problems** |
| Andreas Zezas | U. Crete Physics | astrophysics + astrostatistics, not weak lensing |
| Nikos Kylafis | U. Crete Physics, emeritus | theoretical astrophysics, not weak lensing |

**The expertise in the room is bimodal, and that is the single most important planning fact.**
Four people (Starck, Kilbinger, Tsakalides, Courbin) will follow the deepest slide in the deck.
Two (Zezas, Kylafis) are excellent astrophysicists who do not work on weak lensing, and Pavlidou
sits in between. There is no pitch that serves both at once, which is exactly why the rule of
thirds is not optional here — it is the mechanism that gives each half of the committee a third of
the talk that is theirs.

Two consequences worth stating in advance:

- **Courbin changes the weight of Movement I.** Deconvolution and regularised inversion are his
  own field. Mass mapping as an ill-posed inverse problem, the sparsity prior in MCALens, and the
  plug-and-play denoiser in Chapter 3 are all things he will assess as a specialist rather than
  hear as background. Act 1 and Act 2 should be built *for him*, and it is worth being ready for
  the comparison to image deconvolution being raised explicitly — it is a fair analogy and a
  friendly one.
- **Zezas and Kylafis are the reason A0.2–A0.6b exist.** Not as courtesy, but because two of the seven
  votes come from people for whom the first thirteen minutes carry most of the talk's content.
  "Non-Gaussian" and "the power spectrum is not sufficient" have to be *shown*, not asserted.

The resolution is the rule of thirds (§3.3), and for a defense it is not optional:

| minutes | pitched at |
|---|---|
| 0–13 | any physicist in the room. Weak lensing, why non-Gaussian, why mass mapping. |
| 13–27 | the subfield. Higher-order statistics, SBI, scale cuts. |
| 27–40 | the committee. Joint reading, the nulled frame, sufficiency — then back up to the room for the conclusions. |

**The one thing they should remember.**

> Every step between the shear catalogue and the posterior is a scientific choice with a
> measurable cost — and once you actually measure those costs, the non-Gaussian information
> survives all of them.

**What should be different afterwards.** Beyond the obvious: that the committee sees one research
program with a method, not four papers with a common author. Specifically, that "we validated it"
stops meaning "we ran a coverage test" and starts meaning "we stress-tested it against a
systematic the simulator does not contain, and we benchmarked it against something strong."

---

## 2. ABT

> Stage IV surveys will deliver the non-Gaussian lensing field at percent precision, **and** the
> machinery for reading it — mass mapping, higher-order summaries, simulation-based inference — is
> now built almost entirely out of learned components, **but** every one of those components can
> bias the answer or throw it away without a single internal check noticing, which is why these
> analyses still do not carry a survey's headline constraints, **therefore** this thesis takes the
> chain link by link and measures what each choice costs the final posterior, treating calibration
> and stress-testing as design requirements rather than as things you do at the end.

The "but" is the real one, and it is the thesis's own: a coverage test certifies an estimator
against the simulator that trained it and is constitutionally unable to flag a simulator that is
wrong. Everything in the thesis is a response to that.

---

## 3. The spine: two movements, diagnose then build

```
MOVEMENT I — the maps
  Ch2   diagnose   does the reconstruction change the cosmology?      → yes: ×2.6 tighter
  Ch3   build      PnPMass: flexible, fast, conformally calibrated

MOVEMENT II — the summaries
  Ch4   diagnose   what survives once every baryon-touched scale goes? → the ℓ1-norm, ×1.8
  Ch5   build      the joint ℓ1-norm: reaches the learned ceiling

  through-line     measure the cost → build the fix → attach a guarantee
```

**Updated 2026-08-27 — the 2×2 and the chain diagram are the same structure.** Movement I is
box 2 of A0.8's chain (the map); Movement II is box 3 (the summary). So the spine does not need a
second device to explain it: the chain *is* the map of the talk, the scoreboard says which question
we are on, and §3b uses the same boxes to place every mini-introduction. Three jobs, one graphic.

```
        shapes  →  [ 2. map ]  →  [ 3. summary ]  →  parameters
                    Q1  Q2          Q3  Q4
                   Ch2 Ch3         Ch4 Ch5
                   MOVEMENT I      MOVEMENT II
```

Each movement opens with a *cost*, closes with a *construction*, and each construction carries a
calibration guarantee of its own — conformal per-pixel coverage for the maps, TARP/SBC coverage
for the posteriors. That symmetry is real, not rhetorical: it is exactly the structure of the
thesis's own gap statements in `sec:intro-gaps`, and it is why the four chapters are a program.

**Why not a strict chapter walk.** Four equal acts in publication order is "and, and, and". The
manuscript already does that and it is precisely what the defense should improve on.

**Why not the pipeline walk** (catalogue → map → summary → posterior). It is a better story than
the chapter walk, and the abstract narrates it that way, but it implies an end-to-end analysis the
thesis never ran — PnPMass maps have not been pushed through a higher-order inference. The
conclusions say so explicitly. Using the pipeline as the spine would make the seam load-bearing
and invite the committee to lean on it. The 2×2 keeps the pipeline as a *diagram* (A0.9, recurring)
without claiming the chain was run.

---

## 3b. The mini-introduction problem — and the rule that resolves it

**Raised by Andreas, 2026-08-27, and it is the hardest design problem in this deck.**

Five things need teaching before they can be used: **mass mapping and its ill-posedness**,
**Bayesian inference**, **simulation-based inference**, **higher-order statistics**, and
**BNT / lensing tomography**. Every one of them appears in more than one chapter. Front-loading
them all makes a twenty-minute preamble before any result; teaching each at first use bloats
whichever act happens to come first and leaves the later ones thin.

Three rules make it tractable.

**1. The chain diagram is the geography, and every mini-introduction is a zoom into one of its
boxes.** A0.7 already draws it — shapes → map → summary → parameters — and the four questions land
on it cleanly: **Q1 and Q2 are both box 2**, **Q3 and Q4 are both box 3**. Staged that way a
mini-introduction stops reading as a detour and starts reading as descent into a box the room
already knows. Re-show the chain, dimmed except the box in play, at every act divider. This is the
device that keeps the flow, and it costs one recurring graphic.

**2. Teach at maximum motivation, not at first use.** The case that decides this is higher-order
statistics. Ch2 uses wavelet peak counts, so first use is Act 1 — but Act 1's entire argument is
that *the statistic is held fixed while the map varies*. Teaching the starlet decomposition there
would spend the slide budget on the one thing Act 1 is deliberately not varying. So Act 1 says
"we count peaks in the map, held fixed" and stops; the real teaching happens in Act 3, where the
statistic is the subject. The same rule sends SBI to Act 3 rather than Act 1.

**3. One archetype for all of them.** Same slide shape every time, so the room learns the rhythm:
*this is teaching, it will be brief, then we return to the argument.* Reinforces §12's note about
Tinnaneri Sreekanth's recurring pipeline.

### Where each concept is taught

| concept | taught in | why there, and not earlier |
|---|---|---|
| mass mapping, the ill-posed inverse problem | **Act 1** | it *is* Q1's subject; Act 1 cannot pose its question without it |
| Bayesian inference (emulator + MCMC) | **Act 1**, one spoken line | a means, never a subject. No slide. Do not explain MCMC to this committee |
| higher-order statistics — the **recipe** | **Act 1**, 1.4 | 1.6 is unreadable without it: peaks, counted at five angular scales, and nothing more |
| higher-order statistics — the **theory** | **Act 3** | starlet band-passes, peaks vs ℓ1, why it beats the power spectrum. Held fixed in Act 1, so it earns nothing there |
| simulation-based inference (NPE, coverage) | **Act 3** | where the coverage validation is load-bearing rather than incidental |
| BNT / lensing tomography | **Act 3** cliffhanger | first use and maximum motivation coincide; Act 4 only needs a callback |

**Recipe before theory** (added 2026-08-29). A concept can legitimately be taught twice if the two
halves are *different kinds* of thing: Act 1 needs the multi-scale peak count as an **instrument**
("what we do to the map"), Act 3 needs it as a **subject** ("why this captures information the
power spectrum misses"). The rule is that the first pass must be a recipe with no theory in it —
if Act 1 starts explaining the starlet transform, it has taken Act 3's slide.

**The callback rule.** A concept's *second* appearance gets one sentence and the dimmed chain, never
a re-explanation. Act 4 does not re-teach the ℓ1-norm; it says "the same statistic, read jointly"
and moves. If a callback needs more than a sentence, the concept was taught in the wrong act.

**What this costs.** Act 1 carries two teaching slides and Act 3 carries three, so those are the
two heaviest acts. That is the right place for the weight: Act 1's teaching pays off again in
Act 2, and Act 3's pays off again in Act 4. Nothing is taught twice.

---

## 4. The four questions — stated upfront, ticked off

Unlike the COSMO-26 deck, which withheld its questions and generated each from the previous
answer, **the defense states all four at minute seven and returns to them**. This is Fleming's
device (§2.3) used as intended, and a defense is the format it fits best: the committee has read
the thesis, so nothing is spoiled, and the room gets a map it can re-enter at any point.

| | question | answered at | answer |
|---|---|---|---|
| **Q1** | Is mass mapping preprocessing, or does the choice of reconstruction change the cosmology we infer? | A1.4–A1.5 | **It changes it.** Same simulations, same peak counts, same likelihood — swapping KS for MCALens moves the four-parameter figure of merit by **157 %**, and the gain comes from the small scales KS never recovers. |
| **Q2** | Can a reconstruction be flexible, fast, accurate and honest about its own uncertainty at the same time? | A2.2–A2.3 | **Yes.** PnPMass: one denoiser trained once, inside a fixed-point iteration; no retraining across noise or footprint; per-pixel error bars with a distribution-free finite-sample coverage guarantee. |
| **Q3** | If we discard every scale unmodelled baryons measurably touch, is there any non-Gaussian information left worth having? | A3.4–A3.5 | **Yes.** The contamination localises into the finest wavelet band. Drop it — at every survey area, with no feedback model at all — and the starlet ℓ1-norm still constrains **×1.8** tighter than the power spectrum at Stage IV, **×2.6** at full sky. |
| **Q4** | Do we need a neural network to read the maps, or can a hand-built statistic reach the same ceiling? | A4.4–A4.6 | **A fixed wavelet statistic reaches it.** The joint ℓ1-norm, built from the auto-maps alone with no training, matches a compressor trained to maximise the information it retains — 3371 against 3326. |

**The fifth question, never stated but always the subject: what makes any of it trustworthy?**
It is answered on the conclusions slide, and it is what the four answers have in common — each
one is a *contrast inside a matched pipeline*, with the estimator held fixed and the calibration
verified before any figure of merit was compared.

---

## 5. Budget

**Rewritten 2026-08-27 against the deck that actually exists**, not a projection. Target **40:00**.
Act 0's timings are **measured** at 140 wpm from `SPEAKER_SCRIPT.md`; Acts 1–2 are measured for the
words but the slide counts below are the *revised* targets, not what is in the deck today.

### Where we are starting from

The live flow is **67 frames** — 51 horizontal slides plus 16 vertical sub-slides. That is roughly
**double** the ~34–37 this slot supports. The three things eating it:

- **27 slides before the first result.** Act 0 (9) → superseded intro variants (6) → mass-mapping
  pedagogy (9) → Act 1 setup (3), and only then Ch2's answer. The number to watch is minute 10.
- **Six slides that are a mistake, not a choice.** The *Earlier intro versions* block is still
  navigable — its divider says "not part of the talk" but it never got `data-visibility="hidden"`.
- **LAM's pacing is coffee-club pacing.** "Traditional Approach: The 2-Point Route" is a ten-frame
  build explaining the power spectrum to a committee containing Starck and Kilbinger. Plus three
  separate pipeline diagrams and two consecutive methods-overview slides.

**The cuts come from slides 9–23, not from Acts 3–4.** cosmo26's 14 slides for two chapters are
already tight; the fat is all in the runway.

### The running order, slide by slide

**47 frames of main line, ~47:30 — and that is over.** Act 0 measures **11:25**, Act 1 **11:29**,
Act 2 **3:57**: **26:51 scripted**, against roughly 20:12 still estimated for Acts 3–4 and the
conclusions. **That is about 2:30 past a 45:00 slot**, and it is the number to act on before the
next rehearsal, not after.

Where it came from: the 2026-09-03 Part 1 rebuild put beats on five slides that never had one
(1.4a, 1.4b, 1.5, 1.5a, 1.5b) and retired the old 1.5. Some of that is genuinely new material and
some is simply the first honest measurement of slides that were always going to be spoken over.
**Two caveats on the estimate itself:** the seven statistics frames that left Part 1 took their
1:30 with them into Act 3, whose estimate predates the move and so is probably low; and the
four-question scoreboard moved to the conclusions, where it is still unscripted. Acts 0–2 are
measured beat by beat from `SPEAKER_SCRIPT.md`; everything after is an estimate.

`src` column: **built** = in the deck and keepable · **frozen** = Andreas's
call, do not touch · **lift** = LAM/cosmo26 slide, needs compressing · **merge** = two existing
slides into one · **new** = does not exist. **TEACH** marks a §3b mini-introduction.

---

#### Act 0 — the setup · 9 frames *(the timings below are pre-2026-09-06 and have not been re-measured; the three formalism slides they include have left the act)*

| # | on screen | visual | src | min |
|---|---|---|---|---|
| 0.1 | *Trustworthy non-Gaussian inference for weak-lensing cosmology* | title card, particles bg | built | 0:27 |
| 0.2 | 13.8 billion years, from quantum fluctuations to galaxies | the cone | **frozen** | 1:08 |
| 0.3 | ΛCDM: six numbers, and the assumptions that let you get away with six | 3 parameter columns over the assumptions block; on click the budget pie **swaps for the annotated cone**, then dark matter / dark energy / tensions one at a time | **rebuilt** | 2:20 |
| 0.4 | Independent probes are a test — and they do not quite agree | probes + the S8 tension | **frozen** | 1:42 |
| 0.5 | A 1 % distortion, invisible alone, **coherent** across neighbours | the cone again + light rays | rebuild | 1:03 |
| 0.6 | Euclid: an order of magnitude more statistical power | mission clip + four figures | rebuild | 0:38 |
| 0.6 | *(closing beat, added 2026-09-06)* the lensing signal is the **statistical memory** of the whole history of the Universe, and getting it out is an **algorithms** problem | one line under the Euclid block | **built** | +0:20 |
| 0.6a | ~~We measure the **shear**. What we want is the **convergence**.~~ | **moved into Part 1, 2026-09-06** | moved | &mdash; |
| 0.6b | ~~A convergence map carries both **geometry** and **growth**~~ | **moved into Part 1, 2026-09-06** | moved | &mdash; |
| 0.6c | ~~One potential, two observables — the relation is **exact**~~ | **moved into Part 1, 2026-09-06** | moved | &mdash; |
| 0.7 | A real weak-lensing analysis is **dozens of steps**, and most of them are not the physics | the DES Y3 flowchart (Amon), credited | **built** · **theme flips to light here** since 0.6a left | 0:50 |
| 0.8 | Between the shapes and the parameters there is a **chain** — and **the four questions of the thesis on it** | **the master chain graphic**, then **four clicks, one question each, lighting the step it is about**: shear→maps · maps · maps→…→posterior · summaries + systematics | **rebuilt 2026-09-06** | ~2:10 |
| 0.9 | ~~Four questions about that chain~~ | folded into 0.8, 2026-09-06. The board still exists, immediately before the conclusions, as a **return** | moved | &mdash; |

*The beat, as of 2026-09-06.* A picture of the Universe → the model that fits it, and where it
stops being satisfying → **how you test a model like that**: independent probes, and lensing is the
one we follow → what lensing is, strong and then weak → the survey about to make it precise, and the
fact that the signal is the statistical memory of the whole history of the Universe → **so here is
what it actually takes to read it**: the real DES analysis, dozens of steps → stripped to the
scientific spine, that is the chain → **and here are the four questions of this thesis, one per
click, each on the step of the chain it is asked about.**

The formalism — shear against convergence, the projection integral, the exact κ–γ relation — is
**no longer in the introduction**. It is Part 1's own machinery, and it now opens Part 1, running
straight into *the relation is exact, the measurement is not*. The introduction is shorter for it
and ends on the whole thesis rather than on Parts 1 and 2.

### Where Bayes gets taught — decided 2026-09-02

**Once, at A1.4, for the whole talk.** Bayesian inference appears twice in this thesis: over a
*map* in Acts 1–2 (reconstruction) and over *three numbers* in Acts 3–4 (SBI). The risk is not
that Bayes goes untaught, it is that the room silently merges the two uses. Teaching it twice,
in two notations, actively invites that. So it is taught once, as a template with a named slot
for the unknown, and the second use is a callback rather than a lesson.

**Why at A1.4 rather than at the SBI slide.** It is first use (§3b: teach at maximum
motivation). The prior is *visual* in this problem — different priors give visibly different
maps of the same field, which cannot be shown for a prior on Ω<sub>m</sub>. And Acts 1–2 then
spend twelve minutes varying the prior; deferring Bayes would leave that stretch using "prior"
as undefined vocabulary, which is exactly the general-audience failure to avoid.

**The geography does the disambiguation for free.** In the chain graphic, reconstruction is box
3 and inference is box 5, and the inference box is already stamped p(θ|x). So Act 3 needs one
line, not a primer: *same formula, the unknown is three numbers not a map, and this time the
likelihood cannot be written down.* A0.6/A1.4's closing line pre-announces exactly that.

**FLAG, deliberately deferred: MAP vs the full posterior.** Mass mapping takes the *most
probable* map — a point estimate. Cosmological inference wants the whole distribution. Saying
"Bayesian" for both without marking the difference is the fair thing for an examiner to push
on, and Starck is the likeliest to. It is **not** put on the A1.4 slide (it would dilute the
one lesson); it lives in that slide's speaker notes and as a FLAG block in `SPEAKER_SCRIPT.md`
A1.4, to be said in Part 2 where the uncertainty actually arrives. The arc is the answer: point
estimate in Ch2, calibrated uncertainty in Ch3, full posterior on parameters in Ch4–5.

**What it absorbed.** The old *Overview of mass mapping methods* slide was the same content in
worse form — four bullets, each of the shape "Prior on κ → …". It is now the fan-out, and the
original is a vertical beneath, along with the MAP / alternating-scheme / proximal-operator
material. Net: one slide fewer on the floor, nothing lost.

**0.10 is the recall device's first use (2026-09-01, Andreas's idea).** Rather than opening Part 1
with a Kaiser–Squires derivation, the talk returns to 0.8's chain with the shear-maps → mass-maps
step lit — arrow included, because naming two adjacent stages means the step between them, not two
boxes. The room already knows the picture, so lighting a piece of it locates the next twenty
minutes without a word of explanation. `pipeline.js` lights the connecting arrow automatically when
two adjacent stages are active.

**0.7 was cut from the flow on 2026-09-01** (Andreas) and sits at the back with the earlier intro
versions, reveal #90. It was the tension payoff — *it was the third one, it was the analysis* — and
0.4 now raises a disagreement that the talk never resolves. That is a real open end, not a tidy-up:
see the benched A0.7 beat in `SPEAKER_SCRIPT.md` for the two ways to close it. **0.8 is the slide the rest of the talk hangs on** — it is the map, the
scoreboard's geography, and the staging device for every mini-introduction (§3b).

**No dark-energy taxonomy** (decided 2026-08-29). A field-equation slide reading Λ three ways —
modify the geometry, modify the contents, or leave it as a constant — was drafted and cut. The
thesis makes **no dark-energy claim**: w₀ is an axis in the figures of merit, never an interpreted
result, so setting up that question promises something the talk never returns to. And 0.4 already
earns lensing more concretely, by naming it the one probe sensitive to both geometry **and** growth.
What survives is one sentence of epistemics at the end of 0.3 — *you do not test the model by
arguing about what Λ is, you measure the same numbers several independent ways and check they
agree* — which is also the cleanest hand-off into 0.4. The field-equation slide stays in the deck as
**general-audience Q&A backup**, where "so what is dark energy?" is a likely question.

**Parameters are glossed here, named later.** 0.3 says only what the six numbers represent, in
words. Ωm, σ8 and w0 are introduced at **1.5**, the first contour plot, where the room can see what
they do rather than being asked to hold three definitions for forty minutes.

**Transition out:** *"I am going to ask four questions about that chain. The first two are about
this box."*

**0.6a–0.6b, and where the light section starts (2026-09-01, revised 2026-09-02).** The dark run
ends at Euclid; the deck moves to paper at 0.6a, to mark the change from the picture of the Universe
to the quantities the thesis operates on. Both are §3b mini-introductions placed at maximum
motivation, and together they establish: *what we measure* → *what the convergence is*.
0.6a's line — *we measure the shear, we want the convergence* — is the sentence Act 1's whole
question is built on, and 0.6b makes the convergence map a concrete object before every later
result is computed on one.

The third slide of that block, 0.6c, **is no longer here**: *how you get from one to the other,
and why that is hard* now opens Part 1 as 1.1a. The reasoning is that it is not general lensing
pedagogy — it is the specific setup Kaiser–Squires needs, and stating Act 1's premise a full act
before Act 1 opens bought nothing except a twenty-minute gap between the formalism and the methods
that use it.

**The chain graphic is now a component, and it recurs (2026-09-01).** 0.8's diagram is defined
once in a `#wl-pipeline` `<template>` and cloned by `pipeline.js` into every
`<div class="pipeline-slot">`; `data-active` names the stage to light, `data-variant="compact"`
drops the thumbnails for the act openers. Six stages — catalogue, shear maps, mass maps,
summaries, inference, posterior — over a second **model lane** in causal order: prior →
N-body simulations → systematics, rejoining the data lane at inference along the one
accent-coloured edge in the diagram. π(θ) opens the model lane and p(θ|x) closes the data
lane, which is the shape of the whole exercise.

Two corrections got it here, both Andreas's (2026-09-01). **Systematics belong on the model
lane**: they are modelled and marginalised in the prediction, not something that happens to
the data in transit — the first version bracketed baryonic feedback under the two data stages
it contaminates, which read as if the contamination were part of the measurement. And
**systematics come after the simulations, not before**: you cannot contaminate a simulation
you have not run. **Edit the template, never the copies.**

It is live on 0.8 (full, neutral) and on the Act 1 and Act 2 openers (compact, `maps` lit).
**Acts 3 and 4 have no opener slides at all** — they begin on content slides inherited from
cosmo26 — so the device stops halfway through the talk. Giving them dividers in the style of
*Part 1* / *Part 2*, each carrying `data-active="summaries"`, is two slides and about 0:30, and
belongs with the Acts 3–4 pass. The insert is one line wherever those dividers land.

**0.6c became 1.1a on 2026-09-02, and the runway hole closed itself.** The κ–γ relation slide
had been pulled *up* into Act 0 from the mass-mapping runway; it has now been pushed back down,
past the *Part 1* divider, so it opens the movement instead of closing the formalism block.
(The LAM verbatim original stays parked in place, `data-visibility` hidden, directly beneath it.)

Three consequences, in order of how much they matter:

- **The redundancy flagged here in the 2026-09-01 pass is gone.** The slide that opens the
  runway no longer re-introduces material 0.6c has already covered, because 0.6c *is* now the
  slide that opens the runway.
- **0:53 crossed from Act 0 into Act 1.** Nothing was written or cut, so the whole-talk figure
  is unchanged; Act 0 is now 10:32 against 10:00 and Act 1 is 9:24 against 8:15.
- **It created a new, tighter collision.** 1.1a, 1.2 and 1.3 now restate *ill-posed* and the
  Kaiser–Squires one-liner inside a single minute, where they used to be twenty minutes apart.
  The trim is specified in the ⚠ note at A1.1a in `SPEAKER_SCRIPT.md`, worth 0:35–0:45 — enough
  to put both acts back inside budget. **Not applied; it is a decision about spoken words.**

**Open, and worth a decision.** As placed, the theme runs dark → **light, light** → dark (0.7 the
hinge, 0.8 the chain) → light (0.9 the scoreboard). Three flips in five slides, and it half-defeats
the reason for flipping at all. Two consequences, neither fatal but both real:
0.7's *"which brings me back to that disagreement"* now reaches back four slides instead of two, and
the light section starts, stops and restarts. Moving 0.6a and 0.6b to sit **after 0.9** would give
one clean flip at the scoreboard, keep the hinge two slides from the tension it pays off, and put
the formalism where it is needed anyway — immediately before the mass-mapping runway. It is a
block move of two contiguous sections. Not done: the placement after Euclid was asked for
explicitly.

---

#### Act 1 — Q1: does the map matter? · 7 slides · 8:07 *(measured)* · **box 2**

| # | on screen | visual | src | min |
|---|---|---|---|---|
| 1.1 | *Part 1: does the choice of mass-mapping method matter for cosmology?* | act divider, compact chain with the **map** box lit, + arXiv:2501.06961 | built | 0:43 |
| 1.2 | **TEACH** The forward direction has **one answer**. The inverse direction has **many** | two lanes; the inverse one ends in a **fan** of candidate maps, all consistent with the shear | **built 2026-09-03** | 0:57 |
| 1.3 | Kaiser–Squires assumes **almost nothing** about κ — which is the problem | the truth/KS pair; derivation + operator algebra on 3 verticals | built | 1:23 |
| 1.4 | **TEACH** So write the assumption **down** — posterior, likelihood, prior | the Bayes decomposition, then the three priors; 3 verticals | built | 1:44 |
| 1.4a | What *sparse* actually claims | the starlet atoms; a physical claim, not a numerical trick | lift (LAM) | 0:57 |
| 1.4b | MCALens: **two components**, and a different rule for each | the κ_G + κ_NG split, the alternation, and **what a proximal operator is** — the step Part 2 replaces | **rebuilt 2026-09-03** | 1:06 |
| 1.5 | Different assumptions, different maps — and **nobody had checked** whether it mattered | two cards: what the field measured against what it had not; the Euclid stake | **built 2026-09-03** | 0:54 |
| 1.5a | Same simulations, same statistic, same likelihood — **only the map changes** | the fixed chain, with compression and inference marked as Part 3's business | **unparked 2026-09-03** | 0:52 |
| 1.5b | Kaiser–Squires **smooths the small scales away**. MCALens does not. | the four panels beside a key of **what each assumes**, badged Euclid-baseline / state-of-the-art | **unparked + adapted** | 0:39 |
| 1.6 | **Swapping the reconstruction alone moves the FoM by 157 %** | contours + ratio ladder to KS = 1.00× | **unparked 2026-09-03** | 1:15 |
| 1.7 | MCALens keeps gaining to 2′; KS saturated at 8′ | the two scale ladders | **unparked 2026-09-03** | 0:59 |

*The beat.* **Restructured 2026-08-29 on Andreas's call, and this is now the strongest sequence in
the deck.** It is a derivation, not a list of three methods:

> ill-posed, so many solutions → the standard fix is the analytic formula → here is why that is far
> from perfect → so make the assumption explicit and write it as inference → the prior is the design
> choice → Gaussian, sparse, and the best analytic prior we found is MCALens's.

Everything in the act then answers one question — **what do you assume about κ?** — which is why
1.2's *the added assumption is the method* and 1.4's *likelihood × prior* are both never-cut. They
are what make **Act 2 legible**: PnPMass is this same slide with the prior no longer written down
but learned. Without 1.4, plug-and-play arrives as machinery instead of as the next step in an
argument.

**iKS must not vanish.** The old three-methods slide named it; the derivation nearly dropped it.
It is now introduced on 1.3 as the obvious repair for the mask, and 1.6 reports it as the null
result. `PAPER_FACTS.md` §6 is explicit that it stays.

**1.5 answers *why* we compress, not just *how*** (Andreas, 2026-08-29). A pure recipe — "we count
peaks at five scales" — states what we do and skips the reason, and the reason is load-bearing: a
convergence map is ~10⁵ correlated pixels with no tractable likelihood, because the field is not
Gaussian and there is no closed form to appeal to. So we compress to a short vector and characterise
*that* from simulations. Which leads to the sentence the slide exists for:

> **every compression throws something away, and what survives is decided entirely by which summary
> you choose — so the summary is a scientific choice, exactly as the reconstruction was.**

That is the **root of Questions 3 and 4**, planted in Act 1 and harvested twice later. It also gives
the act a symmetry worth having: 1.2–1.4 say the *map* is a choice, 1.5 says the *summary* is a
choice, and the four questions are those two choices interrogated in turn.

Then, and only then, the recipe: peaks are local maxima in the S/N map, counted at several angular
scales — which is the minimum needed for **1.7 to be readable at all**. **Do not** explain the
starlet transform or why this beats the power spectrum; both are Act 3's subject, and this is the
biggest delivery risk in the act.

**Transition out:** *"So the reconstruction is a scientific choice — and the choice is a prior. Which
raises the obvious question about the same box: what if you do not write the prior down at all?"*
→ tick Q1.

---

#### Act 2 — Q2: can the map be trusted? · 5 slides · 5:00 · **box 2**

| # | on screen | visual | src | min |
|---|---|---|---|---|
| 2.1 | *Flexible, fast, accurate and honest about its uncertainty — at once?* | chain, box 2 still lit, + **attribution** | new | 0:35 |
| 2.2 | Every existing reconstruction gives up at least one of the four | two method-family cards + "what we want" | built | 1:00 |
| 2.3 | **TEACH** One denoiser, trained once, inside a fixed-point iteration | PnP forward–backward diagram | lift | 1:30 |
| 2.4 | **TEACH** Distribution-free per-pixel intervals, calibrated on held-out data | conformal / CQR schematic | lift | 0:55 |
| 2.5 | **Smallest calibrated error bars of any method tested** | bounds + calibration + miscoverage | lift | 1:00 |

*The beat.* Attribution first, once, plainly. Then: what four things we want → nothing had them →
the construction → the guarantee → the result. The claim is the **error bars**, not the RMSE; 2.5
must not let the accuracy comparison become the subject.

**Transition out:** *"That is the map. Now down the chain — to what we do with it."* → tick Q2.

---

#### Act 3 — Q3: does the summary survive baryons? · 8 slides · 8:00 · **box 3**

| # | on screen | visual | src | min |
|---|---|---|---|---|
| 3.1 | *Is there non-Gaussian information left once baryons are cut out?* | chain, **box 3 lit** | new | 0:30 |
| 3.2 | The information and the worst systematic live on the same scales | the two-curve schematic | built | 1:00 |
| 3.3 | **TEACH** Peaks count maxima, the ℓ1-norm weighs everything — one starlet decomposition | starlet row + peaks + ℓ1 | built | 1:30 |
| 3.4 | **TEACH** Simulation-based inference, every posterior coverage-tested | NPE pipeline + TARP/SBC gate | built | 1:00 |
| 3.5 | Unmodelled feedback biases every statistic, and worse the bigger the survey | bias vs survey area | built | 1:00 |
| 3.6 | Buying back an unbiased answer costs the power spectrum most of its range | the scale cuts | built | 1:00 |
| 3.7 | **On baryon-safe scales the ℓ1-norm still gains ×1.8 at Stage IV** | ratio-vs-area curve, PS at 1.0 | re-plot | 1:30 |
| 3.8 | **TEACH** Nulling should have been the fix — it inflates the contours instead | BNT kernels + inflated contours | built | 0:30 |

*The beat.* The densest act, and the one carrying three mini-introductions. Motivation first (3.2)
so the teaching in 3.3–3.4 is *asked for* rather than imposed; then the diagnosis (3.5–3.6), the
answer (3.7), and a cliffhanger (3.8) that Act 4 pays off. **3.8 ends on an unresolved negative
result** — do not soften it, it is what makes Act 4 land.

**Transition out:** *"Hold that. Same box, one more question."* → tick Q3, cliffhanger open.

---

#### Act 4 — Q4: learned or hand-built? · 7 slides · 7:00 · **box 3**

| # | on screen | visual | src | min |
|---|---|---|---|---|
| 4.1 | *Do we need a network to read the maps?* | chain, box 3 still lit | new | 0:30 |
| 4.2 | Beating the power spectrum is a low bar — what is the ceiling? | κ patch + the VMIM compressor | built | 1:15 |
| 4.3 | Same maps, same flow, both calibrated | the comparison diagram | built | 1:00 |
| 4.4 | Read bin by bin, the ℓ1-norm reaches three quarters of the ceiling | corner plot, ×0.74 | built | 1:00 |
| 4.5 | Two routes to the inter-bin information — or read each pair jointly | cross-maps vs the joint cell map | built | 1:15 |
| 4.6 | **A fixed wavelet statistic reaches the learned ceiling, with no training** | completeness ladder, ceiling at 1.0 | re-plot | 1:15 |
| 4.7 | Under nulling, what a summary keeps tracks how jointly it reads the bins | BNT retention ladder | built | 0:45 |

*The beat.* No new teaching — callbacks only (§3b). Set the ceiling → make the comparison fair →
show the honest shortfall → build the fix → reach the ceiling → and 4.7 pays off 3.8's cliffhanger,
which is what closes the whole programme rather than just this act.

**Transition out:** *"Four questions, four answers."* → tick Q4.

---

#### Conclusions · 4 slides · 5:00

| # | on screen | visual | src | min |
|---|---|---|---|---|
| C.1 | **The four questions, answered** | the scoreboard, all four ticked | rewrite | 1:30 |
| C.2 | What this changes in practice, and where it goes next | — | new | 1:45 |
| C.3 | What it does not yet cover | limitations, plainly | new | 1:00 |
| C.4 | What this thesis produced, and thanks | papers + code + acknowledgements | new | 0:45 |

*The beat.* C.1 is the payoff of the device set up on 0.9 — the same four cards, now with answers.
Per §12, **end on C.1**: after C.4, navigate back to C.1 and leave it on screen through the
questions, so the room stares at the claims rather than at the word "Thank you".

### Two numbers to watch in the first timed rehearsal

**The first result is slide 1.6 — the 16th of 40 — at about minute 16.** Past the minute-10 rule,
deliberately, and it got later when Act 1 became a derivation. The justification is that Act 1's
teaching is the most reused in the deck: 1.2 and 1.4 are what make Act 2 legible, and 1.5 is what
makes 1.7 readable. If rehearsal says it drags, the cut ladder's tier-3 (**A1.4's sparse-prior
paragraph**, −0:19) goes first, then Act 0's tier-1 and tier-2.

**The talk is 41:38 against a 40:00 target — 1:38 over**, with Acts 2–4 still estimated. The slot
is 45 minutes, so this still leaves **3:22 of real buffer**, which is why it is a flag and not yet a
problem. But Act 1 has grown twice now (a derivation in 1.2–1.4, then the *why compress* opening on
1.5) and it is the reason the number moved; both were the right trade and neither should be undone
first.

In reserve, in the order I would take them: the 4.3+4.4 merge (Act 4), Act 0's tier-1 and tier-2
(−1:12 together), then A1.5's *why compress* opening (−0:35, tier 2) — that one last, because it is
the setup for two of the four questions. **Do not add material to Acts 2–4 without taking one.**

**Act 3 is the overrun risk.** Eight slides and three of the five mini-introductions, in 8:00. If
rehearsal says it is tight, buy a slide from Act 4 — 4.3 and 4.4 can merge, since "the comparison
is fair" and "ℓ1 trails by a quarter" are one thought.

---

### What moves out of the main line

| now | goes to |
|---|---|
| *Earlier intro versions* (6 slides) | parked — `data-visibility="hidden"`, like the other two blocks |
| Wiener filter, sparse recovery, MCALens detail, inpainting, the operator algebra | **backup**, Ch2 section — this is where Courbin's questions will want them |
| "Traditional Approach: The 2-Point Route" (10 frames) | one sentence in Act 3's HOS slide; the phase/amplitude panel to backup |
| LAM's "Inference pipeline" and the duplicate methods overview | deleted — the chain diagram and Act 1's reconstruction slide already carry both |
| PnPMass step-by-step flipbooks (14 frames) | backup, Ch3 section |

---

## 5b. The Part 1 rebuild — 2026-09-03

Andreas's brief was continuity and looks: Part 1 read as a sequence of slides rather than an
argument, its back half was LAM-verbatim and ugly, and it detoured into summary statistics that
belong to Papers 3–4. Four decisions were taken with him before implementation.

**1. Part 1 is built on the parked restyled block, not the LAM originals.** The restyled Act 1
slides had been sitting hidden at the end of the file under *Restyled Acts 1–2*, marked
"alternatives — not part of the talk", undecided since they were built. They already implemented
the design this pass needed. They are now the flow; the four LAM originals they replace (the
four-panel + RMSE table, the generic inference-pipeline diagram, the bare question slide and the
results pair) are hidden behind a new *LAM originals, Part 1* divider. **Nothing was deleted.**

**2. The four-panel slide is captioned by what each method *assumes*.** The RMSE table is gone —
it ranked reconstructions on map fidelity, which is exactly the metric this part of the talk argues
is the wrong one to choose by. Keeping it on the slide would have undercut 1.5's whole point. The
key sits *beside* the figure rather than under it, because the panels are a 2×2 grid and a caption
row would imply a positional mapping that is not there. KS and iKS carry an **Euclid baseline**
badge against MCALens's **state of the art** — the stake Andreas would otherwise have had to say
out loud every time.

**3. The seven statistics frames moved to the head of Act 3.** They taught the two-point route,
peak counts, wavelet peaks and the starlet ℓ1-norm in the middle of Part 1 — an act that varies
the *map* and holds the statistic fixed. **Known collision, deliberately left:** the slide directly
after them (*Wavelet peak counts and the ℓ1-norm are 1-pt statistics on the same starlet
transform*) re-teaches the last two frames of the moved block. Merging is an Acts 3–4 job; doing it
blind would cut material Andreas has not reviewed.

**4. The four-question scoreboard moved to just before the conclusions.** Stated upfront it leaned
on machinery the room had not met, and read as confusing rather than orienting. It now sets up the
answers. C.1 — the same board with all four ticked — is still to be written.

**Two things built from scratch**, because the argument had holes rather than ugly slides:

- **1.2, the inverse problem.** §5 has specified this slide since the Acts 1–2 plan and
  `SPEAKER_SCRIPT.md` has carried its beat all along, but it was never built — so the deck asserted
  "ill-posed" and moved on, and the room never learned what an inverse problem *is*. Everything
  downstream rests on it.
- **1.5, the stakes.** The divider asks the question; this slide is what makes it a real one rather
  than rhetorical.

**Also corrected in passing:** MCALens's `\underbrace` labels had been swapped since the LAM lift —
κ_NG was labelled *Standard Wiener filter approach*. Fixed on the algebra vertical.

**Act 0 changed too.** 0.6c made a round trip (pushed behind the Part 1 divider on 09-02, brought
back on 09-03) and now closes the formalism block, so the run reads: *we can only measure shear* →
*but convergence is what we want, and it is a scalar* → *luckily the two are not independent*. The
scalar-vs-spin-2 argument was missing from 0.6b entirely and was added; 0.6a's closing line was
trimmed because it pre-empted both of the slides after it.

---

## 5c. The introduction rebuild — 2026-09-06

Andreas walked the introduction out loud and found it did two things in the wrong order: it taught
the lensing formalism to a room that had no use for it yet, and it declared only half the thesis
before diving into Part 1. Three changes.

**1. The formalism block moves into Part 1.** *We measure the shear, we want the convergence* ·
*a convergence map carries geometry and growth* · *one potential, two observables, and the relation
is exact* — three slides that used to sit between Euclid and the pipeline. They are Part 1's own
machinery: the paper is about inverting γ into κ, and Part 1's second slide is *the relation is
exact, the measurement is not*. So they now open Part 1 and run straight into it. Their parked LAM
originals travelled with them.

The introduction loses nothing. Euclid hands directly to the real DES pipeline, which is the honest
answer to *what does it take to read this signal* — and **the theme flip (dark → paper) moves to
that slide**, where it still marks the same boundary: we have stopped drawing the Universe and
started on the analysis of it.

**2. Euclid gets its closing beat.** A survey this size does not just give more of the same
measurement; it moves the limit off the statistics and onto what we are able to do with them. One
line on the slide — the signal is the **statistical memory** of everything the Universe has done
since the Big Bang, and getting it out is an **algorithms** problem — and that is the sentence the
rest of the talk answers.

**3. A0.8 becomes the map of the thesis.** It used to end on a hand-off line about Parts 1 and 2 and
leave the other two parts unannounced until the middle of the talk. Now all four questions are asked
here, one per click, **each lighting the step of the chain it is about**:

| click | question | lit |
|---|---|---|
| 1 | *(the claim: every stage is a learned component, and each can bias the answer or throw information away with no internal check noticing)* | nothing dimmed |
| 2 | **Q1 · the maps · Part 1** — is mass mapping preprocessing, or does the choice of reconstruction change the cosmology we infer? | shear → mass maps |
| 3 | **Q2 · the maps · Part 2** — can one reconstruction be flexible, fast, accurate and honest about its own uncertainty, on a survey the size of Euclid? | mass maps |
| 4 | **Q3 · the summaries · Part 3** — what is the most we can read out of a map, and what does it take to turn that reading into a posterior? | maps → summaries → inference → posterior |
| 5 | **Q4 · the summaries · Part 4** — does any of that survive the real Universe, the astrophysics we cannot model? | summaries + systematics |

This is what gives the room the shape of the whole work before any of it starts, which is the one
thing §0 says the defense is *for* and the manuscript is worst at. Every part opener afterwards is
then a return to a picture they have already seen with a box lit.

**The four questions are canonical.** The board before the conclusions asks exactly these four, in
this order, in the same words — it is now a *return*, not an opener, and its notes say so. Change
one, change both.

*Deliberately avoided in the wording:* "higher-order statistics". Q3 and Q4 are asked in plain terms
(*the most we can read out of a map*, *the real Universe*) because at frame 9 the room has not met
the vocabulary and does not need it.

**Mechanism, for whoever edits this next.** `data-steps` on a `.pipeline-slot` (see `pipeline.js`)
marks each step's stages `on-k`; which step is showing is decided in CSS off reveal's own
**`.current-fragment`** on zero-size `.qstep` markers, and the cards live stacked in one grid cell
so the diagram above never walks up and down the screen. `.current-fragment`, not `.visible`:
fragments stay visible once shown, so `.visible` would leave every earlier question lit as well.
No `fragmentshown` listener, because `?print-pdf` sets the classes directly and fires no events.

### Left open by this pass

- **The conclusions slide still numbers its three answers Q1–Q3 against an older question set**
  (deep learning / baryons / nulling), which now collides with the canonical four. Three backup
  slides carry those old tags too. Renumbering is a single consistent pass; it has not been made.
- ~~`SPEAKER_SCRIPT.md` has no beats for A0.8's four questions or for Euclid's closing line~~ —
  **done 2026-09-06**: the script was rewritten end to end against the 114-frame deck, every beat
  anchored to its frame, every timing measured by `../tools/measure-script.py`, and every `[CLICK]`
  audited against the deck's real fragment count.
- **Seven slides moved to backup, 2026-09-06** (Andreas), each placed beside its relatives rather
  than dumped at the end. The main line is **54 frames**, down from 62; the deck is still 114.

  | was | is now | slide | sits beside |
  |---|---|---|---|
  | 17 | **106** | the Bayes slide | the LAM original of the same idea, 107 |
  | 28 | **112** | PnPMass on residuals | the training slide, 114 |
  | 29 | **113** | the UQ chain | a **vertical under 112** |
  | 37–39 | **100–102** | peaks, the starlet transform, the ℓ1-norm | the wavelet primer, 97–99 |
  | 59–60 | **66–67** | the nulling result and its payoff | the three BNT explainers, 68–70 |

  **Frame 5, the two tensions, stays** as a vertical under frame 4 — skipped by not pressing DOWN.
  **Every frame number in `SPEAKER_SCRIPT.md` and below is post-move.** Two of the seven took
  material with them. Frame 59–60 is the whole nulling / BNT thread, dropped as too
  technical for the time — which also spends the joint ℓ1-norm's second, independent payoff, leaving
  that argument resting on the tie alone. Frame 17 was **the one place Bayes was taught**, and the
  §5 decision *Bayes gets taught once, at A1.4, for the whole talk* no longer holds: the word
  *prior* and the Part 3 forward pointer moved onto frame 16's beat, the point-estimate flag onto
  frame 18's, and frame 43 is now the only Bayes slide in the talk. The beats are kept in the
  script, marked SKIP, and still audited against the deck.
- **The talk measures 54:16 spoken against a 40:00 target**, with 7:53 parked in the skipped beats.
  §5's budget tables below all predate the measurement and should be read as historical. The
  script's own *The arithmetic, and how to close it* is the live version: a five-tier ladder that
  lands at 40:19, no tier of which is a whole-act decision.
- Two structural gaps the script pass exposed: **there are no Part 3 and Part 4 dividers** (frame 9
  promises four parts, the deck labels two), and **frames 37–39 repeat frames 40–41** — peaks, the
  starlet transform and the ℓ1-norm are each defined twice within ninety seconds.

---

## 6. The three takeaways

1. **The reconstruction is not preprocessing.** It is a scientific choice that propagates to the
   precision of the constraints, and it should be made with the downstream inference in mind.
2. **Non-Gaussian information survives the most conservative possible treatment of baryons** — no
   feedback model at all, every measurably contaminated scale discarded — and still beats the
   power spectrum. That number is a floor, not a forecast.
3. **A hand-built wavelet statistic can be near-sufficient**, provided it reads the tomographic
   bins jointly — which means "we used a learned compressor" is a claim that now has a benchmark
   to beat, and interpretable summaries should not be abandoned without that test.

---

## 7. Numbers: ratios only

**Decision (2026-08-25, Andreas): no absolute figure of merit ever appears on a slide. Only
ratios.** This falls straight out of the no-tables rule (§5) — an absolute FoM is a table cell
with nowhere else to live — and it is also the right call on the science, because the ratio is the
inferential content and the absolute value is an artefact of the setup that produced it.

It dissolves a problem that would otherwise have run through the whole deck. Three mutually
incomparable figures of merit appear in this thesis:

| chapter | FoM definition | parameters | simulations | footprint | inference |
|---|---|---|---|---|---|
| **Ch2** | (det F̃)^(1/n) | Ωm, σ8, h, w0 (n=4) | cosmo-SLICS | DES-Y1-like, 19 × 100 deg² tiles | GP emulator + MCMC |
| **Ch4** | 1/√det C | Ωm, σ8, w0 | cosmoGRID V1 | full-sky HEALPix, masked polar caps, 2 000 deg² → full sky | NPE, MAF |
| **Ch5** | 1/√det C | Ωm, σ8, w0 | cosmoGRID V1 | 10° × 10° gnomonic patches | NPE, RealNVP |

Ch4 and Ch5 share a definition but not a footprint; Ch2 shares neither with either. On a
ratios-only deck none of that ever reaches the screen, and the one spoken sentence — *"these are
three different setups, so read the relative values, not the absolute ones"* — covers it.

### The visual grammar this buys

Every result graphic in the deck becomes the same object: **a ratio, against a horizontal
reference line at 1.0, and each act names what its 1.0 means.** That consistency is worth as much
as the honesty.

| act | the line at 1.0 is | what is plotted against it |
|---|---|---|
| **Act 1** (Ch2) | Kaiser–Squires | iKS ≈ 1.0, MCALens **×2.6** (wavelet peaks) |
| **Act 3** (Ch4) | the power spectrum | ℓ1-norm and starlet peaks, **as curves against survey area** |
| **Act 4** (Ch5) | the learned compressor — *the ceiling* | the completeness ladder climbing to it |
| **Act 4, BNT** (Ch5) | each summary's own un-nulled constraint | the retention ladder |

The Act 3 graphic is the one that gains most: what was a table of twelve FoM values becomes two
curves against survey area with the power spectrum as a flat line at unity. It carries the
*trend* — the ℓ1 advantage growing with area, peaks crossing unity only at Stage IV — which the
table never showed at a glance.

The Act 4 ladder, as fractions of the compressor: **0.74 → 0.80 → 0.92 → 0.98 → 1.01**
(auto, +convolution, +product, both, joint ℓ1). The ceiling at 1.0 and the last rung sitting on it
*is* the chapter's claim, drawn.

### The one thing ratios hide, and the fix

**A ratio looks more precise than the numbers behind it.** ×1.80 at 14 000 deg² comes from
26.1 ± 8.2 against 14.5 ± 0.9 — a 31 % relative uncertainty on the numerator, from the scatter
over five independent NPE training runs. §8 of the guidelines is explicit that the figure of merit
is fragile, and stripping the absolute values must not strip the error bars with them.

**So: every ratio graphic carries its uncertainty band, and the spoken sentence carries it too.**
This is not a concession — it is what makes two of the claims correct rather than approximately
correct:

- Starlet peaks at 14 000 deg² are ×1.07 with a band that comfortably spans 1.0. The honest word
  is **"comparable to the power spectrum"**, and the error bar is what licenses it.
- Joint ℓ1 against the compressor is ×1.014 with the spreads overlapping unity. The error bar is
  the entire reason **"tie"** is the right word and "beats" is not.

Propagated bands are *derived*, not quoted, and go in `PAPER_FACTS.md` marked as such, with the
arithmetic shown. Nothing derived reaches a slide without that line.

Rules carried over from `../cosmo26/PAPER_FACTS.md`, still binding:

- Quote the number you can defend, not the one that sounds best. ×1.8 at Stage IV *and* ×2.6 at
  full sky, with which regime matters said out loud.
- **Peak counts do not win.** On baryon-safe scales they sit *below* the power spectrum at 2 000
  and 5 000 deg² (×0.46, ×0.63) and reach parity only at Stage IV. The honest statement is that
  the ℓ1-norm survives the cut, not that "higher-order statistics" do. Their contribution is the
  different contour orientation, which is complementarity, not constraining power.
- **×1.01 against the compressor is a tie, never a win.** The CNN's slightly conservative coverage
  is the paper's own explanation for the gap. Say "matches", say "reaches the ceiling", never
  "beats". (The absolute pair, 3371 ± 96 against 3326 ± 30, stays in the ledger and the speaker
  notes for the examination; it does not go on a slide.)
- The Ch4 HOS scale cuts are **conservative at small areas** — the dyadic starlet forces the whole
  j=1 band out everywhere while the power spectrum gets a sliding ℓmax tuned per area. Only at
  full sky are both cut to their actual limits.

**Next artifact: `PAPER_FACTS.md` in this directory**, re-derived from the thesis rather than
forked from the COSMO-26 ledger, and extended to Ch2 and Ch3 which that ledger never covered.
No number reaches a slide before it is in there with a source line.

---

## 8. Honesty flags, placed deliberately

Each of these is said before anyone can raise it. Placement matters more than wording; the point
is that none of them arrives as a concession extracted under questioning.

| flag | where | one-line form |
|---|---|---|
| Everything is on simulations | A3.3, once, plainly | "Every result here is on simulations; that was deliberate, because isolating one analysis step needs ground truth — and it means the application to data is still ahead." |
| One feedback prescription, fixed parameters | A3.4 | "One baryon-correction realisation. A stronger prescription moves the cut to larger scales." |
| The cut is a floor, not a forecast | A3.5 | "No feedback model at all, every contaminated scale gone. Anything that models the feedback improves on this." |
| Ch3 is second-author | A2.1 | "This chapter is led by Hubert Leterme; I co-developed the method and the uncertainty quantification." |
| Coverage tests cannot see a wrong simulator | A4.2 or C.3 | "A coverage test certifies the estimator against the simulator that trained it. It cannot, by construction, tell you the simulator is wrong — which is why Chapter 4 exists." |
| The chain was never run end-to-end | C.3 | "The two halves developed in parallel. PnPMass maps have not been pushed through a higher-order inference; that is the most direct continuation of this work." |
| No intrinsic alignments, no photo-z errors, no source clustering | C.3 | Stated as a list, once, without hedging. |

The last three are the ones a defense rewards most. §2.6: the person who finds you out is the one
asking the first question.

---

## 9. Cut lines

Written as tiers with measured savings once the script exists. Provisional:

- **to 39:00** — fold A1.1 into A1.2's opening sentence (the slide stays up, only the narration
  goes, −0:45); fold A3.6 into the close of A3.5 (−0:30); take the short path on A0.4 (−1:00).
  **≈ −2:15.**
- **to 36:30** — also drop A1.5, the scale ladder (−1:15), stating the mechanism in one sentence
  over A1.4; also take the short path on A3.2 (−0:45); trim A0.2 to a single spoken sentence over
  A0.3 (−0:30). **≈ −2:30.**
- **to 33:30** — also compress Act 2 to A2.2 + A2.3 (−1:00), shorten A4.2 (−0:45), and merge C.3
  into C.2 (−1:00). **≈ −2:45.**
- **Never cut**: A0.7 (the phase/amplitude slide — it is what makes "non-Gaussian" mean something
  to the non-lensers on the committee), A0.9 and A0.10 with C.1 (the scoreboard bookends), A2.3,
  A3.5, A4.5, A4.6, C.3. Cutting the limitations slide to save a minute is the worst trade in
  this deck.

**Two planned exits** (§3.4), with a clock check written into the script at each:

- **Exit A — end of Act 2 (A2.3), expect 20:00.** Behind → take the Act 3 short path.
- **Exit B — end of A4.5, expect 34:00.** Behind → A4.6 becomes 45 s and go straight to C.1.

---

## 10. Backup — a reference deck, not a pile

The examination is 1–3 hours. This section is the part of the deck that does the most work and it
is the part a conference talk never needs. Organised by chapter behind a numbered index slide,
parked with `data-visibility="hidden"`, and **rehearsed for jump-by-number**.

**Ch2** — full 4-param corner plots (single-scale and wavelet); the FoM tables per parameter pair;
GP emulator validation and the fiducial-vs-emulated data vector check; correlation matrices;
Hartlap; the RMSE table for the maps; MCALens's sparse+Gaussian decomposition.

**Ch3** — the fixed-point convergence argument and the non-expansiveness condition; the whitened
formulation and why the noise covariance collapses to one scalar; step-size sensitivity; moment
networks (order-1 and order-2); CQR and the finite-sample marginal guarantee; the miscoverage
plots before/after calibration; timing table; the COSMOS reconstruction; PnPMass on non-Gaussian
residuals.

**Ch4** — the cosmoGRID setup and the BCM parameters; fractional-difference curves for PS, peaks
and ℓ1 (noisy *and* noiseless — the redshift-ordering inversion is a good question to be ready
for); TARP/SBC coverage for every posterior; the Q_DM tension metric and the 0.3σ threshold; the
full scale-cut table; per-area contours; the BNT lensing kernels and transformed maps; the
BNT-on-PS result (×1.4, 92 of 120 bandpowers) and the embedding-network requirement.

**Ch5** — the CNN architecture and the VMIM objective; why d = 10; RealNVP vs MAF and the
per-summary flow tuning; the product and convolution cross-maps and the full completeness ladder;
the full BNT retention table with error bars; the closure criterion (a summary survives the
transform iff its induced action is invertible) and why auto-spectra alone fail it; the
full-sphere leakage argument for the cross-channels; mean subtraction and the mass-sheet
degeneracy; the patch-size choice (6.3 % → 1.5 % gnomonic distortion).

**Cross-cutting** — the three setups of §7 side by side as cards, for the "how do your figures of
merit relate?" question; what field-level inference would add as an *absolute* reference rather
than a relative one; the misspecification literature; the propagated error bands behind every
ratio shown in the main line.

---

## 11. The questions I am dreading

Ranked. §11b: the first entry should be the objection I would raise myself, and every answer
carries its honest converse — the conditions under which the result would not hold.

1. **Everything is on simulations. What actually breaks on real data?** — the one to prepare
   hardest. Measurement systematics, PSF residuals, blending, photo-z; the fact that higher-order
   statistics cannot absorb a contaminant at summary level so every systematic has to go into the
   forward model; null tests and blinding do not have simulation analogues.
2. **One baryon prescription. Would FLAMINGO or a different BCM move the cut?** — honest answer:
   possibly, and validating the cut against full hydro suites is named as the immediate next step.
3. **Your coverage tests certify against the simulator that trained them. How do you know the
   simulator is right?** — the thesis's own central admission. Ch4 *is* the answer, as an explicit
   stress test, and it is not a general one.
4. **Why believe the joint ℓ1 ties the CNN, rather than the CNN being under-trained?** — the
   protocol: same budget, same dimension, three independently trained compressors, spread quoted,
   flow tuned separately for each summary. And the converse: the residual gap is genuine 3- and
   4-bin structure, and pairwise is where the histogram runs out of samples.
5. **What is the absolute information content? Your FoMs are all relative.** — correct, they are
   contrasts inside matched pipelines; field-level inference is the reference point that would
   make "near-sufficient" an absolute statement.
6. **What exactly was your contribution to Chapter 3?** — co-developed the method and the UQ.
   Stated the same way in the talk (A2.1) and here.
7. **Is the 157 % reconstruction quality or just better denoising?** — the scale ladder is the
   evidence; also the honest note that iKS ≈ KS says inpainting buys nothing *for peak counts*,
   and would not generalise to a Fourier-space statistic like the bispectrum.
8. **Why peak counts in Ch2 and the ℓ1-norm in Ch4/Ch5?** — chronology and simulation suite, and
   it should be owned as such rather than rationalised.
9. **Intrinsic alignments.** — absent from the forward models, named in the perspectives, and the
   natural next stress test. Do not improvise a magnitude.
10. **If joint reading recovers the nulled information anyway, why use BNT at all?** — bin-specific
    scale cuts; the ×1.4 on the power spectrum; BNT-smoothing; and a BNT-aware reconstruction as
    the map-level version.

---

## 11b. Source decks — what is liftable, and what it costs

Corrected 2026-08-25. My earlier claim that Movement I "does not exist at all" was wrong: it was
based on looking only at `../cosmo26/`. Across the repo, **all four chapters already have built
slides.**

| deck | covers | state |
|---|---|---|
| `../cosmo26/` | **Ch4, Ch5** | Newest numbers, preprint theme, already forked in. The primary source for Acts 3–4. |
| `../LAM_2026/` and `../ENS_seminar_2026/` | **Ch2, Ch3**, plus Ch4 | 71 and 66 sections. Part 1 (§25–46) is our Act 1 including the scale ladder; Part 2 (§47–58) is our Act 2. **Ch4 numbers predate the resubmission — take the figures, not the numbers.** |
| `../PhD_Day_2025/index.html` | the cosmological opening and the lensing pedagogy | **49 refs, 0 missing.** §3 §5 §9 §21 §22 §24 §12–15 are Act 0. Andreas's own adaptation of the Vilasini opening. |
| `../PhD_Day_2025/index_Vilasini.html` | LDT, GOLCONDA | **51 of 61 refs missing** — her figures were never copied into `assets/`. Structurally interesting, **not liftable** without sourcing the assets. |
| `../NonGaussian_Universe_2026/` | **Ch4, Ch5**, deep BNT | Missing from this table until 2026-08-27. 33 sections, already preprint-themed, and its BNT slides (frame artifact, signal/noise under nulling, the 2-point rule) are the best-built backup material in the repo. |

**Two mechanical traps, found 2026-08-27.** `LAM_2026` has **25** `<img src="….pdf">` refs,
`ENS_seminar_2026` 24, `PhD_Day_2025` 19 — and **Chrome renders none of them**. Those decks have
~20 invisible figures each and only ever looked right in Safari. Rasterise with
`tools/darkfig-to-light.py --no-invert` before lifting anything. Second, their result figures were
exported for a *dark* background, so they cannot go straight onto a light slide; Andreas has the
light-background originals, which is the fix — not recolouring.

**What lifting costs, per slide.** `PhD_Day_2025`, `LAM_2026` and `ENS_seminar_2026` load
`darkenergy.css` **without** the `../assets/themes/talks.css` overlay, so a lifted section arrives
unstyled against this deck's components. Budget a real restyle per slide: `slide-title` assertion
headline, `block`/`callout`/`stat` instead of bullets, theme tokens instead of any inline colour.

Three specific things that must not survive the lift:

- **The Planck parameter table** on `PhD_Day_2025` §4. §5 of the guidelines: no tables. The one
  sentence it is worth folds into A0.2.
- **"Traditional Approach: The 2-Point Route"** is four build steps under a repeated topic-phrase
  title. Compress to one assertion slide (A0.7); the phase/amplitude panel is the whole payload.
- **Bullet lists** on the weak-lensing intro slides. §4.3: the visual carries it, the verb is
  yours to speak.

And the standing warning, §2.7: these decks were built for other rooms and other lengths. Keep the
figures and the mechanics; re-derive the argument.

---

## 12. What to take from the Tinnaneri Sreekanth defense deck

<https://vilasinits.github.io/Talks/PhD-Defence/> — same field, same lab lineage, same reveal.js
stack (`github.com/vilasinits/Talks/tree/main/PhD-Defence`: plain `index.html`, `assets/`,
reveal.js as a submodule; no theme overlay). Read on 2026-08-25. Roughly **105 main slides + ~55
backup**, in three chapter parts.

**Take:**

- **The chapter divider is a question, not a label.** Her Part 2 divider reads *"Can we have a
  better emulator for convergence maps?"* and Part 3 *"Are we there yet — can we now directly
  start using theory?"* That is better than a bare section title and it costs nothing. Our act
  openers (A1.1, A2.1, A3.1, A4.1) should carry their question as the divider headline, with the
  scoreboard handling the global map. The two devices compose: the scoreboard says where we are in
  the program, the divider says what this act is for.
- **The scale of the backup library.** ~55 backup slides against ~105 main is the right ratio for a
  defense and confirms §10 is not over-built. Hers is organised by topic with the methodology
  objections (why ℓ1 and not ℓ2, filter choice, emulator bias, LDT validity range) answered in
  depth, keeping the main line lean. Same principle, and it is the part of a defense deck that
  actually gets used.
- **A "what this produced" beat near the end** — publication list with statuses, plus the
  open-source packages (WALE, GOLCONDA, LDT-2cell-ℓ1) named on their own slide. This is a defense
  convention we do not have in the repo and it is worth having: it converts four years into
  artefacts a committee can point at. Now C.4.
- **A recurring pipeline diagram anchoring every chapter** — independent arrival at the same device
  as our A0.9 chain. Good confirmation.

**Do not take:**

- **~105 main slides.** That is roughly 2.5 slides per minute. Fleming's ceiling scaled to this
  slot is ~37, and §4.3's whole argument is that the slide count is a constraint doing useful work.
  Our 34 is the house call and I would not move it.
- **The Planck-2018 parameter table in the introduction.** §5: no tables. It is exactly the object
  the rule exists for.
- **The "Thank you!" closing slide.** §4.3 is explicit — end on conclusions and leave them up, so
  the room stares at the claim through the questions rather than at the word "Thank you". Our C.5 →
  return-to-C.1 does the same job without spending the last frame on furniture.
- **No scoreboard.** She lets the three-part structure imply the progress. For a four-chapter
  thesis whose selling point is that the chapters are one program, the explicit ticking is worth
  its minute.

Worth re-reading her raw `index.html` at build time for reveal technique — layout, fragment use,
how the animated GIF of the iterative solver is staged. Structure is settled; that is a mechanics
question for later.

---

## 13. Open questions for Andreas

1. **Language.** English, given Starck, Kilbinger and Courbin on the committee — assumed unless
   you say otherwise. Anything bilingual (title slide, acknowledgements)?
2. **The general-audience Q&A**, before the committee clears the room. Do you want a small set of
   *lay* backup slides for it — one "what is weak lensing", one "what is a posterior" — kept
   separate from the examination library? I think yes, and it is cheap.
3. **The hook — settled 2026-08-25.** Not the S8 tension. Act 0 opens on the cosmological frame
   (A0.2) and then on Euclid actually taking data (A0.3), in the shape Andreas used in
   `../PhD_Day_2025`. A map and a mission are things you can look at; a tension plot needs setup
   before it means anything, and the thesis is not a tension paper.
4. **Ch3's weight.** Now 4:30, down from 5:00, because merging the RMSE benchmark into the
   accuracy/error-bar figure removed a slide that §4.3d says was redundant anyway. Lower still?
   Note that Courbin on the committee is an argument for *not* going lower.
5. **The figures that must be built, now that FoM values are off the slides.** Four graphics carry
   the ratio grammar and none of them exists yet:
   - **Act 1** — the KS-baseline ratio bar beside the contour sub-block.
   - **Act 3** — the ratio-vs-survey-area curve, ℓ1 and peaks against a power-spectrum line at 1.0,
     with the propagated bands. This is the single highest-value new figure in the deck: it
     replaces a twelve-cell table with a trend.
   - **Act 4** — the completeness ladder as fractions of the compressor, ceiling drawn at 1.0.
   - **Act 4** — the BNT retention ladder (this one exists in spirit in `../cosmo26/`).
   Plus the Ch4 scale-cut diagram and the Ch3 accuracy/error-bar scatter re-plotted. Confirm, because
   this is the bulk of the build work.
6. **Public code for C.4.** Which repositories go on the "what this thesis produced" slide? I know
   of the PnPMass one (`github.com/hubert-leterme/weaklensing_uq`) from the paper's data-availability
   statement. Are the Ch2, Ch4 and Ch5 pipelines public or publishable by 14 September? If any of
   them can be, that slide is a good reason to do it.
7. **Reuse from `../cosmo26/`.** The two-scenario schematic, the SBI pipeline diagram, the starlet
   explainer and the BNT explainer all exist and are good. §2.7 warns that reused slides carry the
   previous room's framing — these are *diagrams*, which is the safe category, but the BNT
   explainer hardcodes the superseded recovery ladder (`0.15/0.22/0.93/1.06`) and needs
   re-pointing at `0.16/0.24/0.72/0.96`.

---

## 14. Build order — revised 2026-08-27

The deck exists; this is a *restructure*, not a build. In order:

1. **Park what should never have been live.** `data-visibility="hidden"` on the *Earlier intro
   versions* block (6 slides). One attribute, six slides off the flow.
2. **Compress the runway (slides 15–23 → ~3).** The nine lifted pedagogy slides become Act 1's two
   teaching slides plus one methods overview; Wiener, sparse recovery, MCALens detail, inpainting
   and the operator algebra move to the Ch2 backup section.
3. **Cut LAM's pacing out of Acts 1–2.** The ten-frame 2-point build, the duplicate methods slide,
   LAM's own inference-pipeline diagram, the 14-frame PnPMass flipbooks.
4. **Build the recurring chain graphic** (§3b rule 1) — dimmed except the box in play — and put it
   on all four act dividers. This is the single highest-value new asset in the deck.
5. **`SPEAKER_SCRIPT.md` for Acts 3–4 and the conclusions**, word-counted at 140 wpm, then reconcile
   every act against §5 and replace the estimated minutes with measured ones.
6. **Then restyle**, jointly, into the preprint components — the pass deferred on 2026-08-27.
7. **Verify:** `check-asset-links.py`, the **DOM slide count** (`REVEAL-GOTCHAS.md` §8b — a file-order
   check does not prove the deck is intact), fragment audit, grayscale pass, PDF export early.

### Still open

- **Andreas's light-background figure originals** — they supersede any recolouring. Everything in
  Acts 1–2 currently uses the dark exports.
- **The MCALens slide's swapped `\underbrace` labels** (κ_NG ↔ κ_G). Factual, inherited from LAM,
  flagged and not fixed.
- **`bnt_explainer.js`** still hardcodes the superseded ladder `0.15/0.22/0.93/1.06` → `0.16/0.24/0.72/0.96`.
- **The four ratio graphics** of §13.5, none of which exists yet. (The master chain graphic,
  listed alongside them, was built on 2026-09-01 — see §5.)
