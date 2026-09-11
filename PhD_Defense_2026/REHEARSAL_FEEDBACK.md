# The CosmoStat rehearsal — comments, and what to do about them

**Rehearsal: 2026-09-10, 11:30. Delivered in 48:00, reading from the script.**
Four sets of comments: three from the rehearsal room (transcribed in
`defence_prep_comments.txt`), plus Martin's, sent afterwards and explicitly *"in view of reducing
material"*.

This file is the evaluation. What each comment says, whether it holds, and what was done. It is a
companion to `TRIM_CANDIDATES.md`, which measures where the time is; this one records what the room
actually noticed.

> **Frame numbers in the comments are the numbers the room saw**, i.e. the deck as rehearsed.
> Parking the DES-pipeline slide has since moved everything from the old 8 up one lower, so the
> talk is now **52 main-line frames** and 114 in the file. The *Applied* section at the end uses
> the new numbering; everything above it uses the room's.

---

## What 48 minutes means

> **Corrected 2026-09-11.** The 6,041-word count below was inflated: `measure-script.py` counted
> HTML comments as spoken. The rehearsed script holds **5,799** real spoken words, so the measured
> rate is **121 wpm**, not 126. Both the tool and the rate were fixed on 2026-09-11. The talk now
> measures **44:14**, and the gap against a 45-minute slot is three to eight minutes delivered,
> not ten. Everything in this file that quotes a time was computed before that fix.

The script measures **5,799 spoken words**. Delivered in 48:00, that is **121 wpm** — well above the
110 wpm this file and `TRIM_CANDIDATES.md` have been planning against, which predicted 52:43. The
model was pessimistic on rate and roughly right on total, because a read-through skips most of the
pause overhead it was budgeting for.

The number to plan against now is **not** 48:00. A read-through is the fast end of the range:

| | |
|---|---|
| read from the script, measured | **48:00** |
| from memory, slower per word (≈110 wpm) | ≈52:30 |
| + the pauses a read-through skips — a new figure, turning to the screen, the beat after a headline, over 53 frames | +2 to 4 min |
| **realistic delivered** | **52 – 57 min** |

Against a 45-minute slot that is a gap of about **ten minutes**, not five. Every earlier estimate in
this repo understated the rate and overstated the total; the conclusion is unchanged and slightly
sharper. Martin's comments are the only set aimed squarely at that gap, which is why they rank
first below.

---

## Where the reviewers converge

Independent agreement is the signal worth weighting. Sorted by how many people arrived at it alone:

| | R1 | R2 | R3 | Martin |
|---|---|---|---|---|
| text too small | ● (5 slides) | | ● | |
| too much teaching / recover minutes | ● | (implied) | | ● |
| concepts arrive after they are used | ● (32) | ● (8→35) | ● | |
| 115 slides / backup numbering | ● | | ● | |
| frame 35 is too long | ● | ● | | ● |
| frame 51 is confusing | ● | | | ● |

R1 is the reviewer with the handwritten notes and the long summary — the same person; they say so.
R2 is "I have Two points". R3 is the lowercase set.

---

## Martin's comments — the reduction list

Ranked by what they buy against the ten-minute gap.

### 1. Frame 7, the DES pipeline — remove it. **Agreed, take it.**

Martin: *"You have your own pipeline in the next slide, that should be sufficient, no? The DES slide
has a lot of distracting DES-specific text, like paper authors and Amon's personal contribution
that is a bit confusing."*

Right on all three counts. It is a borrowed figure whose caption credits a person the room does not
need, its detail is unreadable at the size it renders, and frame 8 immediately draws the same chain
in the deck's own visual language and then uses that chain four more times as the talk's recurring
geography. Frame 7 exists to say *real analyses are complicated*, and A0.8's own first sentence
already says it. **Saves 0:35.**

### 2. Frame 35, likelihood-based inference — shorten. **Agreed, and this is the big one.**

Martin: *"just say that there is this traditional Bayesian sampling method, but that you are going
beyond this with ILI and SBI."* R1 says the same thing from the other end (*"you introduce deeply
many things at various stages (VMIM, NPE, …) — I think you can gain the three minutes"*), and R2's
Bayes-at-8-formalised-at-35 observation is the third face of it.

Three people, three routes, one conclusion. Frames 35–38 are **6:24 at 110 wpm, eleven per cent of
the talk**, and none of them carries a result. This is the same finding as `TRIM_CANDIDATES.md`
Group D, now with witnesses.

Note the one thing that argues the other way: the room on 14 September is not the CosmoStat room.
Tsakalides has this vocabulary professionally and three of the committee know it at code level, but
Pavlidou does not work on lensing. The resolution is to keep the frame that is legible to a
non-specialist — **36, generative modelling** — and compress 35, 37 and 38 around it, rather than
delete the run wholesale.

### 3. Frame 51, the scale cuts. **Agreed, and there is already a figure for it.**

Martin: *"you talk about scale cuts in the C_ell and l_1, but then only show the power spectrum,
which I found slightly confusing."* Correct — the slide's title names both, its third bullet says
the starlet drops j = 1, and the only panel on screen is the power-spectrum bias-versus-ℓmax figure.

`assets/figures/statistics/p1_hos_frac_diff_l1/` already holds the ℓ1 counterpart, scale by scale;
it is on backup frame 82. Putting one panel of it beside the power spectrum makes the slide say what
its title claims, and it defuses R1's *"we really give away so many scales :("* in the same move —
see below.

### 4. Frame 44, the lensing efficiencies. **Agreed, and that figure also already exists.**

Martin: *"it would be good to show a plot of the tomographic lensing efficiencies, that illustrated
this fact."* The beat's punchline is literally *"the kernels overlap"* and there is no kernel on the
screen — nine animation steps of the tomography cartoon, then an assertion.

`assets/figures/statistics/p1_kernels_standard.png` is exactly it: four overlapping efficiency
curves, all rising through the same low-redshift structure. It is currently on backup frame 66.

### 5. Frame 45, drop the κᵢ × κⱼ product maps. **Martin is undecided. So am I, and it is Andreas's call.**

For: it is a third concept on a slide that already has to distinguish tomographic bins from
histogram bins, it is confusable with the joint ℓ1-norm, and it performs worse (3045 against 3371).
Against: it is the evidence that a variety of combinations was tried, which is what makes the joint
statistic look like a result rather than a lucky guess — and R1's *"can you discuss the difficulties
of such comparisons"* suggests this committee rewards showing the search.

**My read:** keep it in the *figure*, cut it from the *mouth*. One clause — "the obvious route,
explicit cross maps, buys some of it back" — instead of the current explanation. The plot keeps the
evidence, the beat stops teaching a concept that loses. Saves roughly 0:25 without removing anything
from the record.

### 6. Frame 49, SBI — *"I don't remember why."* **No action.**

A flag without a reason is not actionable, and frame 49 is the one slide that shows where in *this
paper's* pipeline the statistics are computed per wavelet band, which is what makes the scale cut on
51 mean anything. Leaving it. Worth asking Martin directly if it matters.

---

## The rehearsal room's comments

### Holds, no argument

**The font sizes.** R1 flagged five slides, R3 flagged the deck. Measurable and correct. The canvas
is 1200 × 720 with a 24 px base; captions run 0.42–0.5 em, which is **10–12 px, or 1.4–1.7 % of frame
height**. Both reviewers independently named frames 11 and 31 — the two slides where the caption
carries information rather than a source line.

| where | was | element |
|---|---|---|
| frame 29 | 0.42 em | `.twopt figcaption` |
| frame 37 | 0.44 em | `.ft-gif figcaption` |
| frame 11 | 0.46 em | `.kappadef .kmap figcaption` — R3's exact flag |
| frame 31 | 0.46 em | `.hosgain figcaption` — R1's exact flag |
| frame 26 | 0.46 em | `.pnpres figcaption` |
| frames 8, 27 | 11 px, 14.5 px | chain flowchart labels |

The fix is a floor, not a per-slide fiddle: **nothing that must be read below 0.6 em (≈14 px)**, source
and attribution lines no lower than 0.55 em. Testing in the room is good advice, but it should not be
a condition — the fix costs nothing and the room is unknown.

**Frame 37, the change-of-variables formula.** A cascade bug rather than a judgement call:
`.floweq .katex` is 0.9 em but sits inside `.fl-left p` at 0.72 em, so it renders at **0.65 em ≈ 15.5 px**,
with the ∂f⁻¹/∂x fraction inside it near 11 px. The smallest equation in the deck, and the only
equation on its slide.

**Frame 13, the underbrace.** KaTeX sets `\underbrace{}_{\text{…}}` labels at scriptstyle, 0.7× the
equation, so "the mask" and "shear operator" land near 17 px. Same mechanism on frame 35's
likelihood. Correct.

**Frame 26, the colorbar.** The sharpest of the small comments. The markers *are* coloured by
miscoverage, but every point sits between 0.045 and 0.07 on a 0–0.07 scale, so two-thirds of the
colour axis is empty and the encoding is invisible — and the beat never mentions colour.

But deletion is the wrong fix: that colour is the evidence for the slide's own bullet, *after
calibration all methods reach the target coverage*, and the black tick on the bar is the target. One
spoken clause recovers it.

**The slide count.** `slideNumber: 'c/t'` prints 34/115. The main line is **53 frames**; 62 of the 115
are backup. A `slideNumber` function that goes quiet past the Backup divider removes a bad first
impression in a few lines.

**The 2017 faces.** Slightly self-defeating: the beat's own justification is *the room has been
hearing about these models for three years*, and the newest image on screen is nine years old.
Needs a 2024+ replacement — a figure decision, flagged for Andreas.

**Frame 40, "the perfect summary statistic".** The most serious of the small comments. "Perfect" is
undefined at the moment it is said, and the definition arrives one slide later, operationally, as
max I(t; θ). Frame 40 is the setup for all of Part 3, so a vague word there costs the room the
thread — and there is a precise word available.

### Holds, but not the proposed fix

**"Have an introduction about all relevant notions earlier" (R1).** No. That front-loads a machinery
block before the first result, which is the thing R1 is simultaneously asking to cut three minutes
of. The facts behind the complaint are right — A1.7 says *"sparse in a wavelet basis"*, A1.9 says
*"sparse in the starlet domain"* and *"thresholding of the wavelet coefficients"*, A1.11 says *"we use
multi-scale peak counts as the statistic"*, three uses before frames 32–33 define either object — but
the cure is one clause at first use, not a new section. Ten seconds against three minutes.

**R3's version of the same point is better and worth taking.** Their knee-jerk was *"why all this work
to go to κ when we can measure cosmology from the shear field directly"*. Act 1 says how to make the
map at length and never says why. One sentence — the statistics we care about are one-point and
non-Gaussian and need a scalar field; you cannot count peaks on a spin-2 field — closes it, and does
R3's other job of motivating higher-order statistics early.

**R2's Bayes at 8, formalised at 35.** Holds as an observation. But formalising Bayes at frame 8
would be exactly the front-loading everyone else is complaining about. Cheaper: do not make the
promise. A0.8 says *"in a bayesian framework"*; three words out and the gap does not exist. The
posterior gloss already does the work the room needs there.

**R2's contours without setup.** Partly right, and the diagnosis matters more than the complaint.
The setup *is* spoken — A1.11 is 52 seconds of cosmo-SLICS, the statistic, the emulator, the Gaussian
likelihood, MCMC — and R2 concedes *"maybe you did but I missed it"*. So it is not missing, it failed
to land, which means speech is the wrong carrier. Frame 20's figcaption names the statistic and the
parameters but not the survey or the simulation, while its takeaway generalises to *"WL surveys
should use advanced reconstruction methods"*. A persistent context label fixes what a 52-second beat
did not.

**UNIONS.** The sentiment holds — Andreas is in the collaboration, shows a real UNIONS map on frame
11, and omitting it in front of this audience is an unforced error. But frame 29 does not carry a
survey list; it carries *"every flagship result (KiDS-1000, DES Y3, HSC Y3) is a two-point
analysis"*, and UNIONS has no published cosmic-shear cosmology, which R1 half-concedes. So reword the
claim rather than append to it.

On KiDS-1000 → KiDS-Legacy: yes, and the deck's own backup already cites the 2025 reanalysis. On
DES-Y3 → DES-Y6: **verify before changing.** The figure on that slide is Y3, so changing the text
alone would trade one inconsistency for another.

### Disputed

**"This talk" → "this defense" (R2).** The weakest item. It appears once in the script and zero times
on the slides. "This talk" is standard and neutral; "this defense" is stilted and points at the
ritual rather than the science. Ignoring it. "Today" is the graceful third option if it nags.

**"We really give away so many scales :(" (R1).** A reaction, not a request — and the talk answers it
on the very next frame, ×1.8 tighter than C_ℓ at Stage IV on baryon-safe scales. What it actually
reports is that *the dismay arrives one slide before the reassurance*. That is sequencing. The
defusing line already exists in the notes (the dyadic cut is coarse and therefore conservative) and
belongs on 51, not saved for 52. Martin's frame-51 comment and this one have the same fix.

**"Gaussian likelihood equation… centred?" (R1).** Take the size, leave the alignment. The left edge
is deliberate and there is a CSS comment explaining why: it lines up with the sentences above and
below it.

**The bolding (R3).** Right about the slides, and it is a handful of slides rather than the deck.
Emphasis tags run **6.3 % of visible words** across the main line — but the **conclusions** slide was
at 12.0 % (16 tags in 133 words, which really is every other phrase), the **wavelets** slide at
11.5 %, the **probes** slide at 14.9 %, and the deep-learning table, the flows slide and the SBI
slide all near 10 %.

Not every one of those is a fault. On the probes slide and in the deep-learning table the bold is a
**list marker** — it names the four probes and the column headings — and removing it would cost
structure, not decoration. The ones that were real are the conclusions slide, where the four
questions were bolded as well as the four answers, and the wavelets slide, where three accent words
sat in a row.

The script markup is a separate thing and is not the problem: 195 marked phrases in 6,041 spoken
words, about three per beat.

---

## The comment worth more than all the others

R1's *"potential question"* is not a criticism, it is a correct prediction, and there was no answer
to it anywhere — thirteen tier-2 Q&A entries and this was not one of them.

> *How do your Part 3 and Part 4 interact? You say the ℓ1-norm is optimal — does it still hold after
> you remove the small scales?*

The facts. Part 3's tie (joint ℓ1 **3371**, CNN **3326**) is measured with all starlet bands and no
baryons. Part 4 drops j = 1, uses the **per-bin** ℓ1, and never involves the CNN at all. So three
things are untested at once: the joint ℓ1 under baryons, the CNN under baryons, and either one after
the cut.

Both papers run on **CosmoGrid with four tomographic bins and Euclid-like noise**, so this is a
runnable experiment, not an incompatible-setups excuse — and saying so is better than reaching for
R1's own escape hatch.

There is also an answer that turns the question around. A scale cut is an operation on the *data
vector*: the ℓ1-norm has bands you can drop, the CNN's summary has no band structure at all, so
mitigating baryons on the learned side means retraining and re-deriving its optimality from scratch.
After mitigation the comparison is not apples-to-apples, and the asymmetry runs in Andreas's favour.
That is already the shape of tier-2 Q2; it needed to become its own entry with the numbers attached.

---

## Two things nobody flagged

Found while checking the above.

**A1.11 says "in a Euclid-like setting".** `PAPER_FACTS.md` and frame 19's own notes say **DES-Y1
footprint, 19 tiles of 100 deg²**; only the galaxy density is Euclid-like. This is very likely the
thing R2 tripped on, and it costs two words to fix.

**Frame 28's speaker note has Parts 3 and 4 inverted** — *"Part 3 asks whether that summary survives
baryonic feedback. Part 4 builds the one that does."* Frame 27's note, one slide earlier, has it
right. A stale deck note; the script beat never contained it.

---

## The synthesis

R1's two large comments look opposed and are not. *Take three minutes out of the teaching* and *spend
time on the transitions* are the same recommendation from opposite ends, and they fund each other.
Frames 35–38 are 6:24; two proper transitions cost about forty seconds.

And the transition complaint is partly self-inflicted. The bridge material still exists — A2.1 opens
with *"since we have established that the reconstruction matters"*, frame 27's note has *"everything
else was held fixed on purpose"* — but it sits in the divider beat, after the cut, rather than at the
end of the result, and A3.1 was trimmed to sixteen seconds in the time pass, which stripped the
Part 2 → Part 3 join to a bare announcement. A1.14 currently ends on a win; the limitation that
actually motivates Part 2 — MCALens is slow and hands you a map with no error bars — is true, is
Andreas's own, and was unsaid.

---

## Decisions left to Andreas

1. **Frame 36's 2014–2017 faces** need a 2024+ replacement image. Figure decision.
2. **Frame 45's κᵢ × κⱼ product maps** — Martin undecided. Recommendation above: keep the figure, cut
   the explanation to a clause.
3. **DES-Y3 → DES-Y6** on frame 29 — verify the Y6 cosmic-shear release before touching it.
4. **Frame 49** — ask Martin what he meant, or leave it.
5. **How deep to cut frames 35, 37 and 38.** Three reviewers say cut; how far is a judgement about
   Pavlidou and Tsakalides, not about the material.


---

## Applied, 2026-09-10 (evening)

Frame numbers here are the **new** ones. `measure-script.py` reports a clean `[CLICK]` audit for the
first time, and `check-asset-links.py` passes.

### Deck

| what | frames | comment it answers |
|---|---|---|
| DES-Y3 pipeline **parked**; A0.8 took over the *analyses are complex* claim | old 7 | Martin |
| caption floor: nothing that must be read below **0.58 em** (was 0.42–0.5) | 10, 25, 28, 31, 36 + globals | R1, R3 |
| chain-flowchart labels 11 px → 13.5 px, 14.5 px → 17 px | 7, 27 | R1, R3 |
| `.runhead` 0.42 em → 0.55 em | theme-wide | R1, R3 |
| the ill-posed equation 1.05 em → **1.3 em**, so the underbrace labels are legible | 12 | R1 |
| the Gaussian likelihood 0.92 em → **1.08 em**; posterior/likelihood/prior 0.54 em → 0.66 em | 34 | R1 |
| **change-of-variables formula**: a 0.9 em KaTeX inside a 0.72 em paragraph rendered at 0.65 em; scoped off, now 0.95 em | 36 | R1 |
| slide numbers count the **main line only** and go quiet in the backup — `52` not `115` | all | R1, R3 |
| survey list → *every wide lensing survey measures cosmic shear this way: KiDS, DES, HSC, **UNIONS*** | 28 | R1 |
| retitled *How much of the map's information can a summary statistic keep?* | 39 | R1 |
| the **ℓ1 scale-cut panel** added beside the power spectrum; the `.cutpair` row it duplicated removed | 50 | Martin, R1 |
| emphasis thinned on the conclusions and wavelets slides | 31, 52 | R3 |
| speaker note with Parts 3 and 4 inverted, corrected | 27 | — |

### Script

| what | beat | comment |
|---|---|---|
| *in a bayesian framework* dropped, so the promise is never made | A0.8 | R2 |
| **why we want the map at all** — a scalar field, and you cannot count the peaks of a spin-2 field | A1.3 | R3 |
| *wavelet basis* glossed at first use, eight frames before it is defined | A1.7 | R1, R3 |
| **DES-Y1 footprint** with Euclid-like density, not "a Euclid-like setting"; peak counts glossed | A1.11 | R2, R3 |
| Part 1 now ends on the **limitation** — MCALens is slow and has no error bars — and Part 2 stops repeating it | A1.14, A2.1 | R1 |
| the **miscoverage colour** explained: the circles sit above the target, the diamonds on it | A2.7 | R1 |
| Part 2 → Part 3 join: *the summary statistic was held fixed on purpose. Now it is the subject* | A3.1 | R1 |
| classical inference **1:20 → 0:52** | A3.13 | Martin, R1, R2 |
| both cuts described, and *ours is the blunter instrument … everything on the next slide is a floor* | A4.4 | Martin, R1 |
| new tier-2 Q&A **3**, the Part 3 × Part 4 interaction; 3–12 renumbered to 4–13 | Q&A | R1 |
| three stale `[CLICK]` cues fixed (frames 27, 32, 44) | A3.2, A3.11, A3.22 | — |
| both budget tables re-sized at the **measured 126 wpm** | — | — |

### Where that leaves the clock

**49:32 at 126 wpm**, against 48:00 read at the rehearsal. Parking frame 7 and cutting A3.13 bought
about 1:10; the clarity fixes the room asked for spent about 3:00 of it. That is the honest trade —
most of these comments asked for the talk to be *clearer*, not shorter, and only Martin's list was
aimed at the clock.

The reduction still outstanding is the one three reviewers named: **frames 35, 36 and 37**
(generative modelling, normalizing flows, simulation-based inference), 2:50 together. Those three
beats were rewritten to Andreas's own instructions on 2026-09-09 — *explain that a flow is a series
of invertible transformations, say what the network is and what is learned, give SBI as the general
idea only* — so they have not been re-cut here without him. Cutting them to roughly 1:20 total, and
keeping frame 35 as the one that is legible to a non-specialist, is the single move that closes most
of the remaining gap.

### Not done, and why

- **Frame 43, the lensing efficiencies (Martin).** The only kernel figure in the repo,
  `p1_kernels_standard.png`, is a **light-background, four-bin** plot, and frame 43 is black and
  carries a **five-bin** cartoon. LAB-inverting it loses the axis labels — the deck's standing rule
  is not to recolour figures. Two minutes with the plotting code, exporting on a transparent ground
  with white labels and four bins, and it drops straight in.
- **Frame 35's 2014–2017 faces (R3).** Needs a 2024+ replacement image; a figure decision.
- **Frame 44's κᵢ × κⱼ product maps (Martin).** Martin is undecided; the recommendation above is to
  keep the figure and cut the explanation to a clause. Not applied.
- **DES-Y3 → DES-Y6 (R1).** Left alone — the version numbers are gone from the slide entirely now,
  which sidesteps it.
- **Frame 49, SBI (Martin).** A flag with no reason attached. Worth asking him.
