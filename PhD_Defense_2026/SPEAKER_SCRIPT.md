# SPEAKER_SCRIPT — PhD defense, University of Crete, 14 September 2026

Format per `../docs/TALK-GUIDELINES.md` §11b. **`[CLICK]`** = fragment advance. **▲** = must
survive verbatim as the wording drifts in rehearsal. Everything else on the page is spoken.

> Stage directions were stripped on 2026-09-07 (Andreas): *"I know what to do. You don't have to
> tell me that, and this just makes the script harder to read."* The handful that carried something
> other than delivery advice — words you might say, a hazard on a figure, an answer to a question —
> are `>` notes now. **Do not put them back**: if a new note is not sayable and not a fact about the
> deck, it does not belong in the file.

**Every timing in this file is measured, not estimated** — spoken words divided by the rate, with
cues and blockquotes excluded. The rate is **120 wpm**, and it is provisional: 140 is a *reading*
rate and delivery is slower than that. Time yourself on one beat and set it with `--wpm`. The measurement is done by
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
| Act 0 — the setup | 1–9 | 7:30 | ends on the chain, in two halves |
| Act 1 — Part 1, does the map matter? | 10–22 | 10:34 | opens with the formalism, moved here 2026-09-06 |
| Act 2 — Part 2, PnPMass | 23–27 | 4:11 | frame 26 is the first cut |
| Act 3 — Part 3, the summaries | 28–47 | 15:22 | still the longest act by far |
| Act 4 — Part 4, baryons | 48–53 | 5:12 | opens on its own divider, added 2026-09-07 |
| Close | 54 | 1:50 | |
| | **54 frames** | **44:40** | **at 120 wpm, against a 40:00 target** |

> **⚠ 44:40 spoken against a 40:00 target, at 120 wpm — over by 4:40.** Every beat was rewritten
> for brevity on 2026-09-07 (61:37 → 43:22), so **the prose is spent**; what is left is structural,
> and *The arithmetic, and how to close it* — after the close, below — names it. **Set the wpm from
> a real timing before trusting any of these numbers.**

### Seven slides moved to backup, 2026-09-06

The main line is **54 frames**, down from 62. Seven left it for the backup section, each placed
beside its relatives rather than dumped at the end, so they can be found under questioning. **All
frame numbers in this file are the numbers after the move.**

| was | is now | slide | sits beside |
|---|---|---|---|
| 17 | **106** | *Every mass-mapping method is a Bayesian inference with a different prior on κ* — the Bayes slide | the LAM original of the same idea, 107 |
| 28 | **112** | *PnPMass on residuals* | the training slide, 114 |
| 29 | **113** | *Pixel-wise uncertainties from a second network, calibrated with conformal prediction* — the UQ chain | now a **vertical under 112**, as asked |
| 37 | **100** | *Peak counts* | the wavelet primer, 97–99 |
| 38 | **101** | *One starlet transform* | " |
| 39 | **102** | *The starlet ℓ1-norm* | " |
| 59 | **66** | *Nulling promises localized scale cuts* | the three BNT explainers, 68–70 |
| 60 | **67** | *The information is recoverable* | " |

**Frame 5 — the two tensions — stays where it is**, as a vertical under frame 4. It is skipped by
not pressing DOWN, which costs nothing and leaves it one keystroke away.

Their beats are kept below, marked SKIP, and are still audited against the deck at their new
numbers. **Two of them took material with them and it had to be rehomed** — see the banners on
**A1.8** (the word *prior*, the Part 3 pointer, the point-estimate flag) and **A4.6** (the whole
nulling thread).

**The slack in a 45-minute slot is deliberate and must stay slack** — pauses, the beat after a
headline, and the seconds a room needs to look at a figure before you talk over it. It is not room
for more material.

## The animation policy — 2026-09-07

Andreas, after walking the deck: *"we clearly have overdone this."* The main line carried **97
clicks over 39 frames**, most of them revealing text in the order the eye reads it anyway. Every
build was audited against one rule:

> **A build survives only if it (a) withholds an answer the room should not read early, (b) swaps
> one thing for another in place, (c) moves focus around a diagram that stays on screen, or (d)
> *is* the animation** — a flipbook, or a canvas explainer stepped by markers.
>
> Anything that merely reveals text in reading order goes. The eye already does that, and every
> click is a moment you spend on the clicker instead of on the room.

**97 clicks → 67, across 31 frames.** Sixteen slides lost some or all of their build; two of them
were then put back, and both are marked below:

| frame | was | now | why |
|---|---|---|---|
| 3 | 4 | 1 | the pie→cone swap survives; the three annotations ride in with it and you point |
| 12 | 1 | 0 | a callout of extra detail |
| 16 | 4 | 0 | five methods read as a list **(Andreas)** |
| 17 | 2 | 1 | the proximal box survives; *how it solves* does not |
| 19 | 1 | 0 | a lead line under a diagram |
| 24 | 4 | 0 | a comparison table **(Andreas)** |
| 25 | 1 | 0 | one click for the whole body |
| 37 | 2 | 1 | the MCMC animation survives; the equation reveal does not |
| 38 | 2 | 1 | the faces survive; the bullet does not |
| 40 | 3 | 1 | the three-stage diagram goes up whole; *the cost is paid once* is still withheld |
| ~~45~~ | 8 | **8** | *stripped, then restored 2026-09-07.* Not a flipbook: the picture stays and the **highlight moves**, and what it moves through is the reason the bins are not independent. It was the one call in this audit I got wrong |
| 53 | 5 | 3 | **(Andreas)** the contour and its numbers are one beat: the bullets now land with the ℓ1-norm |
| ~~46~~ | 3 | **3** | *restored 2026-09-07* — route one wants the screen to itself before route two lands beside it |
| 51 | 7 | 0 | seven clicks of one plot **(Andreas)** |
| 52 | 1 | 0 | one click for the whole body |
| 55 | 1 | 0 | the conclusions go up whole |

**What survives, and why it earns the click.** Frame 9's four questions and frames 29/36's pipeline
focus move the light around a diagram that stays put. Frames 26 and 42/50 *are* animations — the
PnPMass iteration, and the two canvas explainers whose markers step them through their acts. Frame
30 swaps a video for a figure, frame 35 swaps each definition for its shape, frame 46 swaps the
mask for the joint definition. And frames 47 and 53 hold back an answer: the ladder to the tie, and
the contours on baryon-safe scales — **frame 53 Andreas named explicitly**, because that is where
Part 4's question gets its answer and the tension is worth keeping.

Single-click frames that survive are all the same shape: a claim withheld until the room has looked
at the figure (7, 8, 11, 14, 15, 18, 34, 39, 41, 44). Those are not builds, they are punchlines.

**If you add a fragment, put it through the rule first**, and re-run `measure-script.py` — it will
tell you if a cue has gone stale.

---

## What the script pass exposed

Four things that are deck problems, not script problems. They are listed here because the script
is where they became impossible to ignore, and each one is cheap to fix.

1. **There are no Part 3 and Part 4 dividers.** Frame 9 promises four parts; the deck names Parts 1
   and 2 on black dividers and then runs Parts 3 and 4 together behind one *movement II* opener at
   frame 28. The room is told there are four questions and then shown two labelled parts. Two
   divider slides would close it, and they are also the natural place to put the paper references
   for Papers 3 and 4, which currently appear only on the conclusions.
2. ~~Three slides define peak counts, the starlet transform and the ℓ1-norm that frame 35 then
   defines again, better, ninety seconds later~~ — **moved to backup 2026-09-06**, where they now
   sit at 100–102, after the wavelet primer, which is the order they should be read in. A3.10 opens
   with a bridge, since the wavelet excursion has become the room's first encounter with either
   statistic.
3. **Frame 26 is still seven clicks of PnPMass flipbook** with no notes, and `STRUCTURE.md` §5 has
   said since the Part 1 rebuild that it belongs in backup. Its partner has already gone to 112;
   this is the other half of the same block, and it is tier 1.
4. **Twelve slides' `aside class="notes"` carry `[CLICK]` counts that do not match their own
   fragments** — frame 39 says four clicks and has one, frame 37 says three and has two. The notes
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

## A0.1 — title · frame 1 · 0:32

Thank you, and good afternoon. Thank you all for coming, and thank you to the committee for reading
this and being here in person.

I'm very happy today to present the work that I have been doing for my PhD over the past 3 years.
This thesis is about extracting information from weak gravitational lensing data, and using it to constrain cosmological parameters. In particular, it is about recovering as much of that information as we can, including the part the standard analysis leaves out, and about making sure that the cosmological results we build on it can be trusted.

I would like to start with the picture we are trying to fill in.

---

## A0.2 — the picture · frame 2 · 0:22

This is the history of the Universe as we currently model it.

It starts in a hot, almost uniform state, with very small fluctuations in density. It expands. And
those fluctuations grow under gravity into the structure we observe today — galaxies, clusters, the
cosmic web.

---

## A0.3 — what ΛCDM is, and where it stops · frame 3 · 1:20

Our prevailing model describing all of that is ΛCDM — Lambda, cold dark matter. It is a very simple model, with just six free parameters.

It rests on this short list of assumptions, basically that gravity is given by general relativity, that the Universe is homogeneous and isotropic on large scales, that the initial conditions come from inflation, and are near-Gaussian and adiabatic, and that the matter is a mixture of baryons, cold dark matter and a cosmological constant.

**▲** And it has been extremely successful. Those six numbers fit 
<!-- the microwave background, the expansion history and the clustering of galaxies simultaneously,  -->
our different observations 
to a remarkable precision.

[CLICK] **▲** But it is still not a fully satisfactory answer, for three reasons. First of all, it is a
**phenomenological** description rather than a first-principles explanation. About ninety-five per
cent of what it describes is two **dark components** whose nature we do not know. 
And independent probes of the same parameters have started to show **tensions** — statistically significant disagreements in the cosmological parameters they report. 

---

## A0.4 — the probes, and the one we follow · frame 4 · 0:16

So how do you study the Universe, and test a model like that? Well, there are several probes that do that...

[CLICK] **▲** But the one we follow in this talk is **gravitational lensing**.

<!-- ---

## A0.4v — the two tensions · frame 5 · SKIP · 0:55

> **SKIPPED (Andreas, 2026-09-06).** It is a vertical under A0.4, so skipping it costs nothing but
> not pressing DOWN, and nothing later in the talk depends on it. Kept here because it is the one
> beat that can come back for free if the clock turns out generous — the decision is made *on*
> frame 4, not in advance.

The consistency between independent probes is itself the test of the model. Measure the initial
conditions with the microwave background, evolve them forward assuming ΛCDM, predict what we should
see today — and then measure it. If ΛCDM is right, those agree.

As the uncertainties fell towards the per-cent level, they stopped agreeing perfectly. The
present-day expansion rate comes out differently from the early-Universe extrapolation than from
direct measurement. And the amplitude of clustering — S-eight, the combination lensing constrains
best — came out about one point seven sigma below the Planck extrapolation in DES and KiDS.

[CLICK] Three ways to read that. New physics. A statistical fluctuation. **▲** Or something in the
analysis itself. -->

---

## A0.5 — strong and weak lensing · frame 6 · 0:41
Here is the basic idea of gravitational lensing. 

Light from a distant source passes every mass on the way to us, and each one bends its path, so the
image arrives distorted.

Occasionally that is dramatic — arcs, multiple images, Einstein rings, visible by eye. That is the
**strong** regime, and it needs a very massive object almost on the line of sight, so it is rare.

**▲** What happens *everywhere* is the **weak** regime: every galaxy behind any structure has its
shape slightly changed. This gives us a hint of the matter (including the dark matter) distributed along the line of sight, and that hint is what we want to read.

---

## A0.6 — Euclid, and what the signal is · frame 7 · 0:44

And we are about to be able to do this to a new level of precision. 
The next generation of cosmological surveys is here, and the one I work on is **Euclid**.
Euclid launched in 2023, it is taking data now,
and it will measure the shapes of billions of galaxies over a third of the sky. **▲** Roughly an
order of magnitude more statistical power than anything we have.

[CLICK] **▲** And that signal encodes the growth of structure and the geometry of the Universe since
the Big Bang. But none of it comes out on its own — getting it out is an algorithms problem.

That is what this thesis is about.

---

## A0.7 — what it actually takes · frame 8 · 0:40

Modern cosmological survey analyses are incredibly complex. 

To demonstrate how intricate the chain is, here is a diagram of the DES Year 3 (a previous generation survey) analysis, 
from pixels to cosmology.

[CLICK] Almost every box here is a paper on its own, and much of it has to do with measurement and calibration. 

The actual cosmology parts are only the parts on the very right.
---

## A0.8 — the chain, and the two halves · frame 9 · 2:17
Here is a similar thing, but reduced to the last steps that are the scientific part of the analysis.

Galaxy shapes go in. From the shapes we make a map of the mass distribution. From the map we extract a few numbers, the summary statistics.
We compare those with theoretical predictions, or with simulations, in a bayesian framework, and out come the probability distributions of the parameters.

[CLICK] **▲** The first half of the talk, the first two papers, is about this step: making the map.
Several algorithms do it. But does the choice matter for the cosmological results, and can we build a really advanced one whose error bars we can trust, and which can be implemented in a 
survey like Euclid?

[CLICK] **▲** The second half, the last two papers, is about everything after it: 
extracting information from the the map, and using it to infer cosmology.
How much of the cosmological information do the summary statistics keep, and does that survive 
the realistic case, where we have physics that the simulations get wrong?

Every one of these steps can bias the result or distort the error bars, if it fails to capture the relevant physical or observational effects.
That's why for the results to be trustworthy, we need methods that properly quantify the unceirtainty, are calibrated, and tested for being unbiased. Otherwirse, we risk producing highly unreliable posterior estimates, distorted uncertainty quantification, and incorrect scientific conclusions.

<!-- , and the whole chain rests on the simulations being right. If they miss a physical or
observational effect, the posterior at the end looks perfectly normal, and it is wrong. The more of
the pipeline is learned from those simulations, the easier that is to miss: a network asked about
data it was not trained on answers confidently and incorrectly. Trustworthy means we checked, at
every step, that this is not happening to us.

*Every step of this analysis can potentially bias the result, affect the uncertainties,*

*it remains critically dependent on the fidelity of the simulations. If forward models fail to capture all relevant physical or observational effects, and the training data is not representative of the true underlying processes, we risk producing highly unreliable posterior estimates, distorted uncertainty quantification, and incorrect scientific conclusions.*

*This model misspecification problem is arguably more severe in SBI than in traditional
Bayesian inference, where the likelihood is explicit, as neural networks are known to produce arbitrarily incorrect predictions when probed with out-of-distribution (OOD) data. In my postdoctoral research, I aim to develop a new generation of robust and interpretable SBI frameworks that explicitly address these limitations through three complementary avenues.* -->


---
---

# Act 1 — Part 1, does the map matter? · frames 10–22

---

## A1.1 — the question · frame 10 · 0:18

So.. Let's start with our first paper. 

First, what is exactly being reconstructed.

---

## A1.2 — shear and convergence · frame 11 · 1:18

The effect of weak lensing can be summarised in two quantities: the convergence, which is the 
an isotropic magnification of the image, and the shear, which is the anisotropic stretching of the image.

Convergence is not directly observable, because we do not know the intrinsic size of a galaxy. 

The shear however is measurable through statistical analysis of the shapes of many galaxies. 
<!-- The idea is that for one galaxy the stretch is about a per cent, far smaller than the shape it already had.  -->
**▲** The idea is that the lensing is **coherent**
and to a good approximation, the intrinsic shapes are **random**. Therefore, if we average the ellipticities over many galaxies in a patch,
the random part cancels, and what survives is the shear.

---

## A1.3 — what the convergence is · frame 12 · 0:34

However, we would really like to know the convergence, for a few reasons.

First of all, it is a scalar field, so it is easier to work with and extract infromation from than the shear, which is a spin-2 field. 

Second, it has a direct physical interpretation: the convergence is the projected matter along the line of sight, weighted by how efficiently each piece of it lenses. So it essentially tells us the distribution of matter in the Universe, which is what we want to know.
That's why convergence maps are also called mass maps.

<!-- Two things ride in that integral: the kernel carries the geometry, the overdensity carries the
growth. **▲** A convergence map responds to both at once, which is why lensing tests the model
rather than measuring one number. -->

Here you can see an example of a real mass map I created for the UNIONS galaxy survey.

---

## A1.4 — shear and convergence from the same potential · frame 13 · 0:27
Lucky for us, the shear and convergence are not independent. They are both second order derivatives of 
this quantity called the lensing potential, which is itself a projection of the gravitational potential along the line of sight.

In Fourier space we can go from one to the other with a simple linear relation.

---

## A1.5 — the relation is exact, the measurement is not · frame 14 · 1:06

While the relation is exact, the data is imperfect. The shear is measured from galaxy shapes, which are irregularly sampled, and have noise (much larger than the shear itself) and *masks* -- missing regions where there are no galaxies or where the data is not usable.

<!-- **Shape noise**, far larger than the shear itself, and the inversion amplifies it at small scales.
**The mask**: the operator is non-local, so a hole leaves whole modes unconstrained. And **a blind
spot** — shear cannot see a constant added to kappa, so the overall level is not measurable. -->

This is why mass mapping is an **ill-posed inverse problem**: there are multiple possible solutions visibly different from each other and consistent with the data. 

**▲** To get a unique solution, we have to make an assumption about what the kappa looks like.

---

## A1.6 — the standard answer · frame 15 · 0:50

The standard answer is to apply the exact inverse anyway, which is what almost every survey has
done for thirty years — and for good reasons.

[CLICK] But look at the pair. Same field, same mask. The structure on the left is not on the right,
and the colour bar spans twice the range — **▲** that extra range is noise. And the mask bleeds
across the whole map, because the Fourier transform does not know there is a hole.

We control that by smoothing. **▲** But smoothing *is* an assumption, applied bluntly and after the
fact, and it removes the small scales we came for.

---

## A1.7 — every method is one term · frame 16 · 1:29

So state the assumption up front instead.

A reconstruction is a fit: the map that reproduces the shear, and is not absurd as a map. **▲**
Every method here writes that same problem, with an identical first term — so the whole history of
mass mapping is a history of the second one, what you are willing to assume a mass map looks like.
Which is a **prior**, in everything but name.

Wiener assumes a Gaussian field — optimal if that were true, but the late-time field is not
Gaussian and the peaks are the whole point. Sparse recovery assumes the opposite: mostly empty, a
few strong features, which is much closer to a field of haloes. MCALens says you do not have to
choose — a smooth background *with* sparse peaks on top. And deep learning stops assuming and
learns the term from simulations.

**▲** And hold this one too: exactly the same three pieces come back in Part 3, with the
cosmological parameters as the unknown instead of a map — except that there, it is the *likelihood*
we cannot write down.

---

## A1.8 — mass mapping as Bayesian inference · frame 106 · SKIP · 0:56

> **SKIPPED (Andreas, 2026-09-06), and three things had to move out of it first.**
>
> - **The word *prior*.** This was the only place in Act 1 that named it, and A2.3 then says
>   *let denoising be the prior*. A1.7 now names it, in one clause.
> - **The forward pointer to Part 3** — *the same three terms come back with the parameters as the
>   unknown, and there the likelihood is the one we cannot write down*. It sets up A3.12 and A3.13
>   and it now closes A1.7.
> - **The point-estimate flag** (Starck), which now sits on A1.9.
>
> **Consequence for the cut ladder:** frame 37 was on the tier-2 park list on the grounds that
> Bayes is taught here. It no longer is, so **frame 37 is the only place Bayes appears in the talk**
> and has come off that list.

And there is a name for what we just did.

**▲** In Bayesian terms: the posterior probability of a map given the shear is the likelihood of the
shear given the map, which is physics we already have — times the prior, what we assumed before
we looked.

[CLICK] The regulariser is the prior. Kaiser–Squires assumed essentially nothing.

[CLICK] Wiener assumes a Gaussian field. [CLICK] Sparse recovery assumes the map is sparse in a
wavelet basis. [CLICK] MCALens assumes it is both at once.

[CLICK] **▲** And the same three terms come back in Part 3, with the cosmological parameters as the
unknown instead of a map — except that there, the likelihood is the one we *cannot* write down.

> **FLAG — say it only if pressed, and say it in Part 2 regardless.** Here we take the *most
> probable* map: a point estimate. Part 2 is where the uncertainty arrives, and Part 3 wants the
> whole distribution. Starck is the likeliest person to ask.

---

## A1.9 — MCALens, and the step Part 2 replaces · frame 17 · 1:12

MCALens is the only one here that does not treat the field as one thing. It models the convergence
as a **Gaussian** component, handled by a Wiener filter, plus a **sparse non-Gaussian** one in the
starlet basis — the peaks, where the higher-order signal lives. It solves them by alternating until
the map stops moving.

[CLICK] And each solve ends with a **proximal step**, which is worth twenty seconds because we meet
it again. You take a step towards fitting the data and land somewhere that fits the shear better
and may be nonsense as a map. **▲** The proximal operator hands back the nearest map the prior will
accept — near, so you keep the progress; acceptable, so you do not run away into noise. For
sparsity it is thresholding.

Remember it, because in Part 2 we throw it away and put a neural network in its place.

> **FLAG — inherited from the Bayes slide, now backup 107. Say it only if pressed, and say it in Part 2
> regardless.** Everything in Part 1 takes the *most probable* map: a point estimate. Part 2 is
> where the uncertainty arrives, and Part 3 wants the whole distribution. Starck is the likeliest
> person to ask.

---

## A1.10 — the stakes · frame 18 · 0:39

Three methods, three different maps — and every one reproduces the shear it was given. Up to this
paper, the field compared them by how close the map came to the truth, in simulations.

But the map is not what we publish. The posterior is, and nothing in a reconstruction error tells
you what happens to Omega-m, sigma-eight or w-nought.

[CLICK] **▲** So it was open, and argued about, with something concrete riding on it: Euclid has to
pick a reconstruction.

---

## A1.11 — the experiment · frame 19 · 0:34

So we built the pipeline. Twenty-five cosmologies from cosmo-SLICS, same statistic, same emulator,
same likelihood, same sampler. [CLICK] And we changed exactly one thing in it: the reconstruction,
which changes the map a lot.

**▲** So whatever moves in the posterior is the reconstruction. It cannot be anything else.

The last two boxes — compression, and inference — are a scientific choice of their own. That is
Part 3. Here they are nailed down on purpose.

---

## A1.12 — the three maps · frame 20 · 0:42

Three reconstructions of the same simulated field. Kaiser–Squires has to be smoothed, so the small
scales are gone. Inpainting fills the mask first and is otherwise the same. MCALens is different in
kind, and you can see it — the structure survives.

**▲** And the two that assume nothing about kappa are what Euclid plans to run, because mass mapping
has been treated as a preprocessing step that does not affect the cosmology, so the simplest method
became the default. That is the comparison.

---

## A1.13 — the answer · frame 21 · 1:18

Only the reconstruction changed. **▲** And it changes the answer.

Kaiser–Squires is the baseline. Inpainting buys nothing — zero point nine nine six. **▲** That is a
null result and I report it as one: inpainting acts on the masked regions, which the peak counts
exclude anyway. And MCALens is a factor of two point six — a hundred and fifty-seven per cent.

**▲** Here is the sentence I would most like you to keep. On reconstruction error, MCALens beats
Kaiser–Squires by four per cent. On the figure of merit, by a hundred and fifty-seven.

Map quality and constraining power are not the same objective.

[CLICK] **▲** And this is what it means for a survey. Mass mapping was treated as a small step that
did not matter, which is why everyone went for the simplest method, Kaiser–Squires. It matters: the
choice of reconstruction changes the cosmological constraints substantially, so for real cosmological
results we need to push for advanced algorithms.

> **If pressed on precision:** Chapter 2 reports no error bars — one chain per method.

---

## A1.14 — where the gain comes from · frame 22 · 0:46

And we can localise it, because the statistic is multi-scale. Add finer bands one at a time:
Kaiser–Squires improves down to eight arcminutes and then stops. MCALens keeps improving all the
way to two.

**▲** So the gain is not a global normalisation — it is small-scale reconstruction fidelity.
MCALens recovers structure where the linear inversion has already smoothed itself into noise, and
the statistic can read it.

Which tells you where the effort belongs: the reconstruction is a scientific choice, and it should
be made with the statistic that follows it in view.

---
---

# Act 2 — Part 2, PnPMass · frames 23–27

> **Frame 26 is the first thing to cut in the whole talk.** Seven clicks of one diagram building
> up, and `STRUCTURE.md` has wanted it in backup since the Part 1 rebuild. Its partner and the UQ
> slide are already there, at 112 and 113. A2.3 carries a tier-0 short path that replaces the lot
> in eighteen seconds.

---

## A2.1 — the divider · frame 23 · 0:31

Question two, and the same box lit again. Since the reconstruction matters, we need the best possible
algorithm for a survey like Euclid. MCALens is the best of the unsupervised methods. But what about
supervised ones: has deep learning been applied to mass mapping?

This chapter is joint work with Hubert Leterme. I co-developed the method, and the uncertainty
quantification is mine.

---

## A2.2 — what we actually want · frame 24 · 0:52

The answer is yes, several times over, and it works. So what do we want from a reconstruction? Four
things — the four columns. Accurate. Flexible, so one model survives a change of noise or footprint.
Fast enough for a survey. And reliable uncertainties.

The model-driven methods give you two: Wiener assumes Gaussianity, the assumption this thesis
exists to avoid, and MCALens is slow. The deep-learning ones are accurate and fast — but each
network is trained for one noise level and one mask, and most hand you a point estimate with no
error bar.

**▲** Nothing had all four. That last row is the paper.

---

## A2.3 — the construction · frame 25 · 0:58

PnPMass. Remember the proximal step from Part 1. The reconstruction is a fixed-point iteration: a
gradient step towards the measured shear, then that proximal step.

**▲** Plug-and-play replaces the proximal step with a learned denoiser. Instead of writing a prior
down and deriving its operator, we let denoising *be* the prior. Ours is a Swin-Transformer, seven
million parameters, trained once on white Gaussian noise across a range of levels.

**▲** And that is the whole point: the denoiser never sees the mask, never sees the survey. It
learns one thing — what a plausible convergence field looks like — and the physics of the
observation stays in the gradient step. Change the noise, change the footprint, the same network
runs.

> **Tier-0 short path replacing A2.4 and A2.5 entirely** (−1:06). Say this instead of walking the
> flipbooks, and skip both frames:
>
> > Eight iterations of that, alternating data step and denoiser, and the map converges. There is a
> > variant that denoises the residual rather than the map, which does slightly better; the
> > iteration histories are in backup.

---

## A2.4 — the iteration, step by step · frame 26 · 0:26

[CLICK] We start from the raw Kaiser–Squires inversion. [CLICK] A gradient step, [CLICK] then the
denoiser, and it already looks like a map. [CLICK] After that it is correcting, not constructing.

[CLICK] [CLICK] [CLICK] **▲** Eight iterations to a fixed point — not a network's guess in one
pass, but a fixed point of an operator that has the data in it.

---

## A2.5 — the residual variant · frame 112 · SKIP · 0:34

> **MOVED TO BACKUP (Andreas, 2026-09-06).** A variant, not a result. A2.3's short path names it in
> one clause if anyone needs it. It now carries the UQ slide as its vertical: press DOWN from 112.

[CLICK] And there is a variant worth thirty seconds, because it is the one that performs best.

Instead of denoising the map at each step, denoise the **residual** — the difference between where
the data step lands and where you were. [CLICK] [CLICK] The network then only ever sees the part
that is changing, which is closer to the white-noise problem it was actually trained on.

[CLICK] [CLICK] Same eight iterations, slightly better maps.

---

## A2.6 — error bars from one forward pass · frame 113 · SKIP · 1:36

> **MOVED TO BACKUP (Andreas, 2026-09-06), and this one costs something.** It is the mechanism
> behind the calibrated error bars A2.7 then reports, and conformal prediction is Tsakalides's own
> vocabulary — so expect it in questions rather than in the talk. It is a **vertical under 112**, so
> from the residual slide press DOWN. **A2.7 now carries two sentences of it**; do not skip those as
> well. Q&A tier 2, question 8 is the follow-up to be ready for.

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

## A2.7 — accurate, with calibrated uncertainties · frame 27 · 1:46

The map is only half a result. A second network, trained the same way, predicts the error of the
reconstruction in one forward pass. **▲** And because a network's own variance is not a guarantee,
we calibrate it — conformalised quantile regression, distribution-free, and it does not require the
network to be right.

> Those two sentences are the whole of backup frame 113, compressed. Cutting them makes the result
> below meaningless.

Which gives this. Reconstruction error across, calibrated interval up: down and left is better.

**▲** After calibration everybody is on target coverage — that is the guarantee doing its job. So
the comparison is not who covers. It is who covers with the tightest bars.

**▲** On accuracy: within one per cent of a DeepMass fine-tuned to this exact mask and noise, from
a denoiser that was never shown either. On uncertainty: the smallest calibrated interval of
anything we tested, on all five hundred and twelve maps.

[CLICK] And it is not constant — the bars rise where the structure is, which is what lets them stay
small everywhere else.

[CLICK] Then deployability. DeepMass and MMGAN are retrained whenever the footprint changes; we
train once. **▲** That is the difference between a method that wins a benchmark and one Euclid
could run.

Two limits. Coverage is marginal, not conditional — what escapes concentrates at the peaks, exactly
where Part 1 said the information lives. And this is a single cosmology.

---
---

# Act 3 — Part 3, the summaries · frames 28–47

> **The longest act, and the one with the most to cut.** There is no *Part 3* divider in the deck:
> frame 28 opens both remaining parts at once. Until that is fixed, A3.1 has to do the naming out
> loud.

---

## A3.1 — where we are · frame 28 · 0:26

Both projects so far live inside one box of that chain — the map. **▲** Everything else was held
fixed on purpose.

The rest of the talk moves one box right: Part 3 builds the statistic that reads the most out of a
map, Part 4 asks whether it survives the astrophysics we cannot model.

---

## A3.2 — from the map to a summary statistic · frame 29 · 0:20

[CLICK] A map is a hundred thousand correlated pixels, so it has to be compressed — **▲** and which
statistic you compress with decides how much of the information survives.

[CLICK] In Part 1 that box was nailed down. Now it is the subject.

---

## A3.3 — the baseline everybody uses · frame 30 · 0:48

Start from the thing everybody uses: take two galaxies separated by some angle, how correlated are
their shapes.

[CLICK] And it works — every flagship cosmic-shear result of the last decade is a two-point
analysis, with twenty years of systematics work built around it. **▲** I am not here to tell you it
is a bad statistic.

[CLICK] The issue is this. For a Gaussian random field the power spectrum is not just a good
summary, it is a *complete* one. **▲** So the question is never whether the two-point function is
good. It is whether the field is Gaussian.

---

## A3.4 — and it is not · frame 31 · 0:20

And gravity has had thirteen billion years to make sure it is not. These two fields have **the same
power spectrum** — one a simulated convergence map, one a Gaussian field drawn to match it. A
two-point measurement cannot tell them apart.

---

## A3.5 — the cosmic web is in the phases · frame 32 · 0:23

What differs — filaments, haloes, voids — is not in the amplitudes of the Fourier modes. It is in
the **phases**, and a two-point measurement keeps the amplitudes and throws the phases away.

**▲** Everything that makes the cosmic web a web lives in what the power spectrum discards.

---

## A3.6 — and it is worth having · frame 33 · 0:32

And it is worth having. Forecasts on the same maps — Virginia Ajani's figure, on the neutrino mass
rather than my parameters. The power spectrum in blue is much the widest; peaks after a **single**
filter are tighter; peaks at **every scale**, red and black, tighter again.

**▲** Nothing about the data changed. The only thing that moves those contours is the choice of
summary statistic.

---

## A3.7 — peak counts · frame 100 · SKIP · 0:25

> **MOVED TO BACKUP (Andreas, 2026-09-06).** Frame 35 defines peak counts again, thirty seconds
> later, and draws their shape as well. The beat is kept for questions.

A peak is a local maximum of the signal-to-noise field — the map smoothed by a filter, in units of
the noise. Peaks sit where kappa is high, so they trace the massive structures, and counting them
by height is a one-point statistic that sees exactly what the power spectrum cannot.

---

## A3.8 — one starlet transform · frame 101 · SKIP · 0:32

> **MOVED TO BACKUP (Andreas, 2026-09-06).** Frame 34 explains what a wavelet is, and this slide
> used to come *before* it. Frame 35 defines the starlet decomposition properly. In backup the
> order is right: the wavelet primer at 97–99, then this.

A single filter size is a choice, and the wrong one throws information away. The starlet transform
writes the map as a sum of band-pass images, each carrying structure of one characteristic angular
size, plus a coarse map. Count peaks band by band and the analysis is multi-scale from one
transform — and because the bands cover different frequency ranges, the covariance comes out almost
diagonal.

---

## A3.9 — the starlet ℓ1-norm · frame 102 · SKIP · 0:22

> **MOVED TO BACKUP (Andreas, 2026-09-06).** Frame 35 defines the ℓ1-norm with the same formula and
> shows its shape.

The ℓ1-norm generalises the peak count. Instead of counting maxima, sum the absolute starlet
coefficients in each signal-to-noise bin, band by band. Every pixel contributes — voids as well as
peaks — and there is no threshold to choose and no definition of a peak to defend.

---

## A3.10 — what a wavelet is · frame 34 · 1:32

I have put the words *peak counts* and *starlet* on the screen without defining either, and both
our statistics are built on a wavelet transform. So, thirty seconds.

Fourier's basis is sines — each a single frequency across the whole map, telling you which scales
are present and nothing about where. **▲** A wavelet is the other trade: compact, oscillating, zero
mean, and that is the whole definition. Stretch it, shift it, and the coefficient is how much
structure of size *a* sits at place *b*. Do that at every size and each feature answers in the band
that matches it — and the bands add back up to the signal exactly.

[CLICK] Same operation on a convergence map. **▲** And here is why it suits this field: a
convergence map is made of objects that have a size and a place, so each one lands in a single band
at its own position, and a handful of large coefficients carry the field.

Same sparsity the Part 1 prior exploited — and it is why the scales can be handled one at a time,
which matters in Part 4.

---

## A3.11 — the two statistics · frame 35 · 1:17

> **The band labels printed on the figure are not ours** — it is a thesis illustration at a finer
> pixel scale. The analysis uses the four finest dyadic bands, roughly 10 to 80 arcminutes.

Both our statistics are one-point statistics — histograms of pixel values — made multi-scale by
that starlet transform.

[CLICK] Peak counts: the local maxima of the signal-to-noise field, histogrammed per bin. Well
established, and it keeps only the discrete features.

[CLICK] This is what that looks like, scale by scale — shapes, not numbers. They turn over in the
same place and stack in amplitude, and they live almost entirely on the positive side.

[CLICK] The ℓ1-norm generalises it: instead of counting maxima, sum the absolute coefficients in
each bin. **▲** Every pixel contributes, voids as well as peaks, with nothing to threshold or tune.
That is our analytical hero for the rest of the talk.

[CLICK] And its shape is different — bimodal, a dip *at* zero, because a coefficient near zero adds
nothing to a sum of absolute values. The left hump is the voids. **▲** That is what "every pixel
contributes" means, and why the ℓ1-norm carries more than the peaks.

---

## A3.12 — no analytic likelihood, so simulations · frame 36 · 0:28

We have a summary; we need a posterior.

[CLICK] **▲** And here is the difficulty that shapes everything after. For the power spectrum you
can write down a likelihood. For peak counts, for the ℓ1-norm, for anything a network computes, you
cannot.

[CLICK] So the whole bottom row lights up: the likelihood is replaced by simulations. That is
simulation-based inference.

---

## A3.13 — classical inference with an explicit likelihood · frame 37 · 0:50

Classical inference is the same rule as in Part 1, with the parameters as the unknown instead of a
map.

All the work is in the middle term, which classically is assumed Gaussian in the data vector — and
**▲** that is a claim about the data, not a convenience: it holds when each data point averages many
independent modes, which is exactly a band-power.

[CLICK] Then MCMC walks parameter space and hands back the posterior.

**▲** And that is the hinge. Both ingredients had to be written down, and for the ℓ1-norm there is
no analytic prediction and the distribution is not Gaussian.

---

## A3.14 — generative modelling · frame 38 · 0:48

So we need different machinery, and it comes from generative modelling: you are handed examples and
you want the distribution they came from.

**▲** The point that matters for us: once trained you can always *sample* such a model, but you
cannot always *evaluate* its density. A GAN will generate a face and cannot tell you how probable
it was — and for inference we need the density, because the density **is** the posterior.

[CLICK] And none of it cares what x is. Those are generated faces four years apart; what we use for
cosmological inference is the same object.

---

## A3.15 — normalizing flows · frame 39 · 0:50

We need a distribution that is three things at once: flexible enough to be an arbitrary posterior,
samplable, and with a density we can evaluate. **▲** Those three rarely come together.

A normalizing flow gets all three. Start from a unit Gaussian and push it through a learned
invertible map; because it is invertible the density comes along by change of variables, and each
layer is built so its Jacobian is triangular, which makes the determinant cheap.

[CLICK] **▲** And the step that matters here: condition every layer on data, and instead of one
distribution you have a family — a posterior you can fit.

---

## A3.16 — simulation-based inference · frame 40 · 1:06

Which gives us this. We have no analytical likelihood for these statistics, but in cosmology we do
have simulators — we can *draw* from the likelihood even though we cannot evaluate it. So: draw
parameters from the prior, run the forward model, keep the pair, a few hundred thousand times.
**▲** That is the expensive part, and the only expensive part.

[CLICK] And then, instead of evaluating a likelihood, we **learn the posterior**. Those pairs train
a conditional flow, whose optimum is the true posterior. Hand it the real observation and read the
posterior off in milliseconds.

**▲** What that buys is not convenience. Inference is now free, so we can run it on thousands of
simulated observations and check the posteriors are actually calibrated — which is not a luxury
when the likelihood was never written down.

---

## A3.17 — the objection I would raise myself · frame 41 · 0:51

So we have a statistic that reads more than the power spectrum. But the summary is the one part of
this chain we still choose *by hand*, and the field increasingly fills that box with a neural
network described as optimal. **▲** If that is true, why hand-build a statistic at all?

[CLICK] It is the objection I would raise myself. The answer is that the optimality claim is
nearly always demonstrated against the power spectrum — which any non-Gaussian summary beats — and
rarely against a strong hand-crafted statistic under matched conditions.

**▲** So the question is open. That is what we set out to close.

---

## A3.18 — what "optimal" means here · frame 42 · 0:38

And you have to be careful what optimal means. Ours: train the compressor and the flow together,
maximising the **mutual information** between the summary and the parameters.

[CLICK] **▲** Which makes it not just another statistic to compare against — a network trained this
way is an estimate of the **ceiling**, the most any summary of these maps could carry.

[CLICK] So a hand-built statistic reaching it is not a win over a baseline. It is a sufficiency
result.

---

## A3.19 — same maps, same flow, both calibrated · frame 43 · 0:20

Same maps, two summaries, the same flow, both calibrated. Flat-sky patches, so the cross-maps we
build later are physically constructible. **▲** And three hundred thousand of them, over nine
hundred cosmologies — enough that any gap is the compressor, not data scarcity.

---

## A3.20 — read bin by bin, the ℓ1-norm trails · frame 44 · 0:44

And read bin by bin, the network wins — a figure of merit of three thousand three hundred against
two thousand four hundred. About thirty-six per cent.

[CLICK] But the two arms are not reading the same thing. All four maps enter the network's first
convolutional layer together; the ℓ1-norm is computed one channel at a time, and only ever sees the
one-dimensional marginals.

**▲** That is an observation about the setup, not a diagnosis. It might account for all of the gap,
or none. So close the asymmetry and measure.

---

## A3.21 — tomography · frame 45 · 0:48

The geometry, because everything after depends on it. We are on the left; the sources are sliced
into redshift bins.

[CLICK] Take the furthest slice. [CLICK] Its light came through **everything** in front of it.
[CLICK] That is its convergence map.

[CLICK] Now a nearer one. [CLICK] Shorter column. [CLICK] Fainter map.

[CLICK] Five slices, five maps — **▲** and every bin's column is contained inside the next one out.
The kernels are broad and they overlap.

[CLICK] **▲** So these are not five independent measurements. They share most of their matter while
the noise in each is independent, and something has to read that shared part.

---

## A3.22 — two places to intervene · frame 46 · 1:16

The gap is structural, so there are two places to intervene: the input, or the statistic.

**Route one**, the obvious one: manufacture the missing channel. Multiply each pair of bins pixel
by pixel — the product lights up only where both have structure in the same place. Six pairs, six
new channels, and the *same* ℓ1-norm runs on each.

[CLICK] **Route two**: leave the maps alone and change what the statistic reads. At a given scale
every pixel hands you all four bins' coefficients at once, and the per-bin ℓ1-norm only ever sees
the two axis histograms. [CLICK] Lay a grid on the pair plane instead and sum the ℓ1 weight in each
cell. That is the joint ℓ1-norm.

[CLICK] **▲** And here is the difference that matters. The product map reduces a pair to a single
field *before* the statistic is taken. The joint ℓ1-norm never reduces it, and it needs no new map
at all.

---

## A3.23 — the answer · frame 47 · 1:03

So: same maps, same flow, four summaries. The ℓ1-norm read one bin at a time is already up — two
thousand four hundred and forty-eight.

[CLICK] Add the product cross-maps: three thousand and forty-five. Better, and not enough.

[CLICK] The joint ℓ1-norm — the statistic from the last slide, no new maps, no training: three
thousand three hundred and seventy-one.

[CLICK] And the CNN lands at three thousand three hundred and twenty-six. **▲** On top of it. Not
above it.

**▲** That is a tie, and I want to call it a tie rather than a win — the network's coverage is
mildly conservative, which plausibly accounts for the hair between them. Both summaries appear to
saturate the information these maps make accessible.

And it holds on every parameter, over nine thousand mock observations.

> That last sentence is **not on the slide** — Andreas commented the `oneline` out. Say it over the
> final arm; the violins that show it are backup 57.

---
---

# Act 4 — Part 4, baryons · frames 48–53

> The whole nulling / BNT thread is **out of the main line** — it is now backup 66 and 67. See
> the banner on A4.6.

> ~~There is no *Part 4* divider. A3.23 ends on a result and A4.1 opens a new paper; the turn has
> to be made with your voice.~~ — **frame 48 is now that divider** (Andreas, 2026-09-07). Parts 1
> and 2 each had a card and Part 4 did not, so the change of paper was carried entirely by the
> voice. Part 3 still has no card of its own; the *Parts 3 and 4* opener at frame 28 covers it.

---

## A4.0 — the turn into Part 4 · frame 48 · 0:28

That is the summary statistic, and it is as good as a network. Which leaves the question that
decides whether any of it is usable.

Everything so far has assumed the simulations tell the truth. **▲** They do not, quite — and where
they are worst is exactly the small scales the ℓ1-norm has just made its case on.

---

## A4.1 — the collision of scales · frame 49 · 1:12

Everything so far has been on clean simulations. **▲** But Stage IV is systematics-limited, so what
decides whether these statistics can be used is not how much they gain — it is how they behave
under contamination.

The worst offender is baryonic feedback: AGN and supernovae push gas out of haloes and suppress
small scales in a way that mimics a cosmological signal.

**▲** And here is the problem in one picture. The information beyond two-point and the
contamination live on the *same* scales.

The conservative response is to cut those scales. Two ways it could go. [CLICK] **Optimistic**:
only the smallest are touched, and most of the non-Gaussian information survives the cut. [CLICK]
**Pessimistic**: the contamination reaches much further, and once it is cut the power spectrum
would have done just as well.

**▲** Which is true is an empirical question, and it is the first thing we measured.

---

## A4.2 — the pipeline, again · frame 50 · 0:24

Same machinery, quickly. [CLICK] Maps from CosmoGrid, [CLICK] Euclid-like noise, [CLICK] wavelet
transform and statistics, [CLICK] a flow, and the posterior.

**▲** The one detail that matters: the statistics are measured on each wavelet band **separately**,
so the data vector is organised by scale. Without that, a scale cut would not be possible.

---

## A4.3 — how big is the bias · frame 51 · 0:44

How badly are we biased if we do nothing? At Stage IV area the power spectrum shifts by two point
two sigma; peaks and the ℓ1-norm by three point six. And it gets worse with area — smaller error
bars mean more sensitivity to a fixed systematic — so at full sky both higher-order statistics
exceed six.

**▲** Two things to be clear about. This is at full resolution, no cuts yet. And the higher-order
statistics are *more* biased than the power spectrum, not less, because they live on the
contaminated scales.

---

## A4.4 — what it costs to buy back · frame 52 · 0:54

So we cut, to bring the bias below three tenths of a sigma — and the two statistics pay in
different currencies.

The power spectrum takes a **sliding** cut, tuned to what is safe at each area. A large fraction of
its range, but removed *precisely*. The starlet concentrates the contamination in its finest band,
so dropping that one band is enough. **▲** But the bands are dyadic, so whole-band removal is the
only cut available, and at smaller footprints that throws away clean quasi-linear information too.

**▲** So the wavelet cut is not better. It is coarser, and therefore conservative. Everything on
the next slide is a conservative estimate.

---

## A4.5 — is there anything left · frame 53 · 1:30

And the answer is yes. Same maps, same cut, three summaries, laid on top of each other.

[CLICK] The power spectrum, on the scales it is allowed to keep.

[CLICK] Peak counts.

[CLICK] And the ℓ1-norm — with the numbers beside it: **one point eight times** tighter than the
power spectrum at Stage IV, and **two point six times** tighter at full sky.

Be precise about the peak counts, because they are the weaker of the two: parity with the power
spectrum at Stage IV, slightly ahead at full sky, trailing at smaller areas. **▲** And they trail
because of the cut, not the statistic — whole-band removal takes a larger fraction of the
peak-count information than a sliding ell-max takes from the power spectrum.

**▲** Two things to leave you with. The non-Gaussian signal survives on *quasi-linear* scales. And
this is conservative: our cut is not optimised, and a finer filter bank would recover more.

**▲** So baryonic feedback is a dominant systematic, it biases these statistics more than the power
spectrum, and even after cutting every scale it touches, the ℓ1-norm is still the better
instrument.

---

## A4.6 — nulling, and what goes wrong · frame 66 · SKIP · 1:52

> **MOVED TO BACKUP — the whole nulling / BNT thread is out of the talk (Andreas, 2026-09-06).**
> Too technical for the
> time available: it needs the transform, the noise-correlation mechanism and the invertibility
> paradox before the payoff means anything, and that is three minutes the talk does not have.
>
> **What goes with it.** A4.7's ladder — the joint ℓ1-norm keeping 0.72 where the per-bin ℓ1 keeps
> 0.16 — was the second, independent payoff for the statistic built at A3.22, and the talk now
> rests that argument on the tie at A3.23 alone. That is enough, but be aware you are spending the
> statistic's strongest supporting result to buy the time.
>
> **Where it lives instead.** Frames **66 and 67**, immediately in front of the three BNT
> explainers at 68–70 that say why it happens. Q&A tier 2, questions 3 and 9; the wider figure set
> is 71, 73–76 and 88. **If it comes up, do not improvise it** — it is the one part of
> the thesis that is counter-intuitive, and it is written out below.
>
> The beat is kept verbatim in case the clock turns out kind, or in case a committee member asks
> for it in full.

The third thing we looked at is a way of making those cuts less blunt.

Nulling — the BNT transform — is a linear re-mixing of the tomographic bins that cancels the
low-redshift lensing efficiency. Why anyone wants it: the standard kernels are broad and
overlapping, so one angular scale mixes low-redshift small scales with high-redshift large ones,
and an angular cut throws away clean high-redshift information along with the contamination. Null
the bins and each transformed field is localised in redshift, so you cut scales only where the
systematic is. **▲** A promising way to do scale cuts — and for the power spectrum it
works, provided you keep the cross-spectra between transformed bins.

[CLICK] Applied to a map-based higher-order statistic, it backfires. The same mixing correlates the
originally-independent shape noise across bins, the noise floor rises, and the contours **inflate**
— worse than standard tomography even with conservative cuts.

[CLICK] [CLICK]
 And that should be impossible.

**▲** BNT is a fixed, invertible matrix. The Jacobian cancels in Bayes' rule, the Fisher
information is unchanged, and the posterior from the full field is identical in both frames. And
yet the ℓ1-norm keeps sixteen per cent.

We are not alone in hitting this: the Euclid analysis of Vinciguerra and collaborators this year
kept tomographic maps for bin combinations up to quadruplets and still concluded that recovering
the signal-to-noise was, in their words, highly non-trivial.

---

## A4.7 — and the answer was already in the room · frame 67 · SKIP · 1:52

> **MOVED TO BACKUP with A4.6** — the two are one argument and neither works alone. They are now
> frames 66 and 67, immediately in front of the three explainers that account for them.

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

**▲** And the power spectrum with its cross-spectra is the simplest case of the same thing. Auto plus cross
spectra are closed under the transform, and so exactly invariant; the auto-spectra alone keep only
the diagonal, and are not. That is the same statement.

**▲** So the practical message, for anyone planning a nulled analysis: nulling need not cost a
higher-order analysis anything, provided some stage of the pipeline reads the bins jointly.

The joint ℓ1-norm keeps seventy-two per cent, not all of it. The remainder is genuine three- and
four-bin structure that a pairwise statistic cannot reach, and that is the one place the network
keeps an advantage.

---
---

# Close · frames 54–54

## C.1 — the question board — REMOVED 2026-09-07

> The board that repeated the four questions before the conclusions is **hidden** (Andreas): the
> rebuilt close carries the questions *and* their answers on one slide, so a separate board in
> front of it was the same words twice. Its beat is gone with it; C.2 absorbed the *these were the
> four questions* framing.

## C.2 — conclusions · frame 54 · 1:50

> **Rebuilt 2026-09-07 to match this beat.** The slide now carries the canonical four with their
> answers, and the separate question board that used to precede it is hidden — this one slide does
> both jobs. The old three-answer version (deep learning / baryons / nulling) is parked directly
> beneath it in `index.html`; its nulling wording is the one to use if the question comes.
>
> The paper references came off. They are on the part dividers where they belong, and the talk
> should end on the science rather than on a bibliography.

These are the four questions, one per part. Here are the answers.

**One.** Yes, the choice of mass-mapping method matters. Change the reconstruction and nothing else,
and the figure of merit moves by a hundred and fifty-seven per cent while the reconstruction error
moves by four per cent. **▲** Reconstruction error is not a good proxy for constraining power.

**Two.** Yes — PnPMass is within a per cent of a network fine-tuned to the observation, has the
smallest calibrated error bars of anything we tested, and is trained once for any mask and
noise level. **▲** That is what a survey needs.

**Three.** As much as an optimal neural compressor, and we do not need the network. Read the bins
jointly and a fixed wavelet ℓ1-norm matches a VMIM-trained CNN, with no training; either summary
goes through the same flow to a calibrated posterior.

**Four.** Yes, they hold up. Cut every contaminated scale and the ℓ1-norm is still one point eight
times tighter at Stage IV, two point six at full sky. **▲** And that is with the most conservative
cut available.

> The nulling result belongs here too and is deliberately not said — see A4.6. If it has come up
> during the talk, add one sentence: *and the same joint reading is what makes redshift nulling
> survivable for a higher-order analysis, which is in the thesis.*

**▲** Two of those questions were about the maps and two about the summaries, and both pairs
answered the same way: a step the field treats as neutral — which reconstruction, which statistic —
turns out to move the result.

Thank you.

---
---

# The arithmetic, and how to close it

**43:52 spoken against a 40:00 target**, at **120 wpm**. Over by **3:52**.

> **The rate matters more than any single cut.** 140 wpm is a *reading* rate; delivery has pauses
> in it. Andreas, timing himself: it takes "significantly more time than what you are estimating".
> 120 is the interim figure and it is a guess. **Read A0.8 aloud at delivery pace, time it, and set
> the real number** — the beat is 342 words, so the rate is 342 divided by the minutes it takes:
>
> ```
> tools/measure-script.py PhD_Defense_2026 --wpm 112 --write
> ```
>
> Every number below moves with it. At 110 wpm the talk is 47:51; at 130 it is 40:29.

| act | frames | measured | share |
|---|---|---|---|
| Act 0 — the setup | 1–9 | 7:14 | 17 % |
| Act 1 — Part 1 | 10–22 | 10:34 | 24 % |
| Act 2 — Part 2 | 23–27 | 4:13 | 10 % |
| Act 3 — Part 3 | 28–47 | 15:21 | 35 % |
| Act 4 — Part 4 | 48–52 | 4:47 | 11 % |
| Close | 54 | 1:43 | 4 % |
| *(not spoken)* | 5, and backup 66–66, 99–101, 105, 111–112 | *9:12* | — |

**The prose is spent.** On 2026-09-07 every beat in the file was rewritten for brevity — 61:37 to
43:22, a thirty per cent cut with no slide touched. There is not another ten per cent in the
sentences without losing claims. What is left is structural.

## Tier 1 — two frames whose beat says nothing new · −0:51 · lands at 43:01

| frame | what | saves |
|---|---|---|
| 26 | the PnPMass flipbook. Seven clicks to show an iteration converging, which A2.3 has already described | **−0:25** |
| 49 | the SBI refresher. A3.16 taught the same pipeline twelve minutes earlier | **−0:26** |

## Tier 2 — the inference runway · −2:34 · lands at 40:27

**This is the recommendation.** Frames 37, 38 and 39 teach the classical Bayes route, generative
modelling and normalizing flows, to a room where Tsakalides has that vocabulary professionally,
three of the committee know it at the level of the code, and the two astrophysicists need exactly
one sentence: *for these statistics there is no likelihood, so we use the simulator instead* —
which is A3.16's opening line.

| frame | what | saves |
|---|---|---|
| 37 | classical inference with an explicit likelihood | **−0:52** |
| 38 | generative modelling and the faces | **−0:52** |
| 39 | normalizing flows. Fold *flexible, samplable, evaluable* into A3.16 | **−0:50** |

**Keep frame 42.** The definition of *optimal* is 0:44 and it is what makes A3.23 a sufficiency
result rather than a benchmark win — the first thing the committee will press on.

## If it is still long on the day

In this order, and each is a real loss:

| | cut | saves |
|---|---|---|
| 1 | A0.8's questions two and four, to one sentence each | −0:30 |
| 2 | frame 33, the Ajani forecast — A3.11's shapes make the point with the actual statistics | −0:33 |
| 3 | A2.2's read-down-the-table paragraph; go straight to *nothing had all four* | −0:25 |
| 4 | frame 45's narration to the first slice and the closing claim, keeping all eight clicks | −0:30 |
| 5 | frame 20, the three maps — frame 19's chain shows them in miniature | −0:30 |

## Never cut

- A0.8's two halves on the chain, and the four questions on the part dividers. The close returns to the four.
- A1.13's *four per cent against a hundred and fifty-seven*, and the iKS null result.
- A1.5's *the added assumption **is** the method*.
- A2.7's two uncertainty sentences — all that survives of backup 113 — and its two limits.
- A3.3's *the question is whether the field is Gaussian*, and the phases pair, frames 31–32.
- A3.18's definition of optimal.
- A3.23's *that is a tie, and I want to call it a tie*.
- A4.4's *the wavelet cut is coarser, and therefore conservative*, and A4.5's closing summary.

---
---

# Q&A — tier 1, the room

Five to fifteen minutes, general audience plus the two committee members who do not work on
lensing. Short answers. Do not reach for the backup deck unless the answer needs a figure.

**"Why do you need simulations at all — can't you just do the theory?"**
For the power spectrum we can, and the field does. For peak counts or the ℓ1-norm there is no
analytic prediction for the mean, and the distribution is not Gaussian — it is a count statistic in
the tail of a non-Gaussian field. So the simulator replaces the formula. The cost is that the
answer is only as good as the simulations, which is why Part 4 exists.

**"How do you know the machine learning is not just making things up?"**
Two answers. The reconstruction never leaves the data behind — the network is one step inside an
iteration whose other step is a gradient towards the measured shear, and it converges to a fixed
point of that pair. And for the inference we test it: because the trained flow answers any new
observation in milliseconds, we can run it on thousands of simulated observations where we know the
truth and check the posteriors actually cover. That is frame 65 in the backup.

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

> **The nulling / BNT thread is not in the talk, and it is in the manuscript.** So it will come up,
> and it will come up cold — the room will not have seen the transform, the noise-correlation
> mechanism or the ladder. Questions 3 and 9 below are the answers, and backup frames 68–70 and 73–76
> are the figures. **Lead with the thirty-second setup before the answer**, in these words:
>
> > Nulling — the BNT transform — re-mixes the tomographic bins so that each transformed field is
> > localised in redshift, which lets you cut scales only where the systematic actually is. It is a
> > fixed, invertible matrix, so it cannot destroy information. Applied to a map-based higher-order
> > statistic it nevertheless inflates the contours, and the resolution is that it moves the
> > information into correlations between bins that a per-bin statistic cannot see.
>
> Then take question 3 or 9 as asked. **Do not improvise this one** — it is the
> counter-intuitive result in the thesis, and the version that lands is the one written out here.

**0. "Why did you not present the nulling result?"**
Time. It is the one result in the thesis that needs three pieces of
machinery before the payoff means anything, and I would rather answer it properly here than rush it
on a slide. Then the setup above, then question 9.

**1. "You compare against a CNN. Did you try hard enough to make the CNN win?"**
A fair objection, and it deserves the working. Getting the network to 3326 took an
expressive flow — RealNVP, worth +36 % — and a better architecture, resnet18, worth a further 6 %.
Going deeper than that *overfits* at 899 cosmologies. So the network is not undertrained; it is at
the point where more capacity costs accuracy on this training set. **The converse:** with a
much larger simulation suite the network would very likely pull ahead again, and the tie is a
statement about the data volume a Stage-IV analysis actually has, not a theorem.

**2. "A tie is not a win. Why prefer the analytical statistic?"**
Given equal constraining power, everything else decides: no training, no architecture search, no
retraining when the footprint or the noise changes, an interpretable data vector you can cut band
by band — which is what Part 4 needs — and a covariance that is nearly diagonal by
construction. And the nulling result: the analytical statistic degrades gracefully in a transformed
frame and you can see *why*, where the network is a black box that happens to survive.

**3. "The joint ℓ1-norm keeps 0.72 under nulling, not 1. What is the missing 0.28?" (not in the talk)**
Genuine three- and four-bin structure. The joint statistic is pairwise by construction, and
pairwise is the ceiling a patch can actually populate — a four-dimensional histogram over K⁴ cells
against 80 × 80 pixels is almost everywhere empty. So the residual is real, it is where the network
keeps an advantage, and I would not claim otherwise.

**4. "Chapter 2 quotes no uncertainty on the 157 per cent."**
Correct, and it is a limitation. One chain per method, 25 cosmologies. The ordering is robust — the
scale ladder in frame 22 is an independent check that the gain is small-scale reconstruction
fidelity rather than a normalisation — but I would not defend the third significant figure.

**5. "Your wavelet scale cut is cruder than the power spectrum's. Is the comparison fair?"**
It is unfair *against* us, and I say so on the slide. The power spectrum gets a sliding ell-max
tuned to each area; the starlet can only drop whole dyadic bands, so at the smaller footprints we
certainly throw away uncontaminated quasi-linear information. A √2 or non-dyadic filter bank would
allow an area-tuned cut. And there is a better cut available in principle: the statistics are
binned in signal-to-noise as well as scale, and the baryonic response sits in the positive tail, so
the contamination could be removed where it sits rather than by removing a band. Future work, and
everything in Part 4 is conservative because of it.

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

**9. "Why should nulling inflate anything if the transform is invertible?" (not in the talk)**
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
map. And the band labels printed on frame 35's figure, which are a thesis illustration at a finer
pixel scale than the analysis.
