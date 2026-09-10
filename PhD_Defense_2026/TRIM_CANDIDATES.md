# Where the time is, and what can come out — 2026-09-10

> **Updated later the same day.** The phases slide left the main line for backup 100, the
> posterior gloss went into A0.8, and A3.4 took over the list of higher-order statistics. Every
> frame number below is the numbering after that move; beat ids are unchanged.

> **Superseded in part, 2026-09-10 (evening).** The CosmoStat rehearsal ran the talk in **48:00**
> reading from the script — 6,041 spoken words, so **126 wpm**, not the 110 this document was
> planned at. The measurement below still ranks the items correctly; its absolute times are
> **14 % pessimistic**. Since it was written, the DES-pipeline frame has been parked (**every frame
> from the old 8 up is now one lower**, and the numbers below have been shifted accordingly),
> frame 33's classical-inference beat has been cut from 1:20 to 0:52, and all three `[CLICK]`
> mismatches are fixed. What the rehearsal room asked for is in `REHEARSAL_FEEDBACK.md`, and some
> of it *added* time deliberately. Current state: **49:32 at 126 wpm**.

A read of every spoken beat in `SPEAKER_SCRIPT.md` against the slide it is spoken over, looking for
repetition, overexplaining, and material that can be passed over quickly. **Nothing here has been
applied.** Each item names the beat, what would go, and what it saves.

## The measurement it is based on

`tools/measure-script.py PhD_Defense_2026 --wpm 110` on the script as of 2026-09-10, after the
conclusions rewrite, the posterior gloss in A0.8, and the phases slide leaving the main line. Cues, blockquote notes and HTML comments are excluded, so
these are spoken words only.

| rate | spoken |
|---|---|
| 100 wpm | 60:55 |
| 110 wpm | **55:22** |
| 120 wpm | 50:46 |

**110 wpm is the planning number**, and even that counts only words. It does not count the pause
after a headline, the seconds the room needs on a new figure, or turning to the screen and back.
Over 53 frames that is another three to five minutes, so the delivered length as the script stands
is **58 to 61 minutes**, against a 45-minute slot and a 40-minute target.

| act | frames | at 110 wpm | share |
|---|---|---|---|
| Act 0 | 1–7 | 9:18 | 17 % |
| Act 1 | 8–20 | 11:46 | 21 % |
| Act 2 | 21–25 | 5:27 | 10 % |
| Act 3 | 26–45 | 19:57 | 36 % |
| Act 4 | 46–51 | 7:24 | 13 % |
| Close | 52 | 1:31 | 3 % |

## The one structural fact

Act 3 is 19:57 of the 55:22, and five of its frames are machinery that carries none of the results:

| frame | beat | at 110 wpm |
|---|---|---|
| 31 | wavelets | 1:40 |
| 34 | classical inference | ~~1:21~~ **done, now 0:52** |
| 35 | generative modelling | 1:04 |
| 36 | normalizing flows | 1:11 |
| 37 | simulation-based inference | 1:08 |
| | **total** | **6:24** |

Eleven per cent of the talk is spent teaching, to a room where Tsakalides has this vocabulary
professionally, three of the committee know it at the level of the code, and the two astrophysicists
need one sentence, which is the sentence A3.16 already opens with. Every other item in this document
is smaller than this one decision.

---

## Group A — repetition, where the same point is made twice

No claim is lost by any of these. **Total 2:07.**

| beat | what repeats | saves |
|---|---|---|
| **A1.12** | The Euclid-baseline paragraph restates A1.10's *mass mapping was treated as preprocessing* and pre-empts A1.13's own closing line. The same claim lands three times in four minutes. Keep it on A1.13, where it is the answer. | 0:25 |
| **A4.2** | The four-click walk through the pipeline. A3.16 taught the same pipeline eight minutes earlier. Only the separation of scales is load-bearing, and it is the point the beat ends on. | 0:28 |
| **A1.9 / A2.3** | The proximal step is explained in full in A1.9, then the whole iteration is walked again in A2.3. One of the two should be a callback rather than a second explanation. A2.3 is the one that needs it, so shorten A1.9. | 0:20 |
| **A4.1** | Three sentences saying systematics have to be assessed at the contour level. Frame 48's lead line says exactly that, on screen. | 0:16 |
| **A2.7** | *DeepMass needs retraining for every new mask or noise level* is the third statement of flexibility, after A2.2's definition and A2.3's mechanism. Make it a clause. | 0:12 |
| **A3.15** | *trained to maximise the likelihood of the training samples* and *the training objective is just the maximum likelihood* are the same sentence twice, four lines apart. | 0:10 |
| **A1.7** | MCALens is described in the five-method list and then again in full on the next slide. Drop it from the list. | 0:08 |
| **A3.16** | Opens on *we have no analytical likelihood*, which is the sentence A3.13 has just closed on. | 0:08 |

## Group B — reading aloud what the slide already shows

**Total 1:10.**

| beat | what | saves |
|---|---|---|
| **A4.1** | The two questions at the end are the two cards on screen, printed in full. Point at them and say "so, two questions". | 0:30 |
| **A2.2** | The four columns are read down; the table is the slide. | 0:15 |
| **A3.23** | Each arm is named as it appears, but the build names them. | 0:15 |
| **A4.4** | The multipole ladder, 860 down to 340, is printed on the slide. | 0:10 |

## Group C — overexplaining, where the level sits below the room

**Total about 1:30.**

- **A1.2 to A1.5** spend **3:43** on shear, convergence, the lensing potential and the ill-posed
  problem before the first result appears. This is the formalism section and it is generous for this
  committee.
- **A1.3** gives two numbered reasons for wanting the convergence where one sentence would do.
- **A3.11** spends about thirty-five words explaining why peaks are cosmologically informative.
- **A2.3** gives the denoiser's architecture, parameter count and training noise range, inside the
  longest beat in Act 2. The *why this beats an analytical prior* paragraph is the valuable half.
- **A3.13** justifies the Gaussian likelihood through band-power averaging, which is a nicety.

## Group D — the structural cuts, in the order to take them

| cut | saves | what it costs |
|---|---|---|
| Frames **35, 36, 37** — generative modelling, normalizing flows, simulation-based inference | 3:36 | Nothing the room needs. A3.16 opens with the one sentence that replaces them. This is the cut ladder's existing tier 2. |
| Frame **18** — the three maps | 0:51 | Frame 17's chain shows them in miniature. |
| Frame **24** — the PnPMass iteration | 0:37 | A2.3 has already described it. Tier 1 in the ladder. |
| Frame **31** — the wavelet excursion | 1:40 | A real loss. It is what stops the ℓ1-norm sounding arbitrary, and Part 4's scale cuts lean on scales being separable. **Take this one last.** |

---

## Where it lands

| after | total at 110 wpm |
|---|---|
| now | 55:22 |
| + group A, repetition | 53:15 |
| + group B, slide-reading | 52:05 |
| + group C, overexplaining | 50:35 |
| + frames 35–37 (flows, SBI, generative modelling) | 46:59 |
| + frames 18 and 24 | 45:31 |
| + frame 31 | 43:51 |

**Two conclusions.**

Everything short of group D buys about five minutes, taking the talk from 55 to 51. Fifty-one is
still six minutes past the slot, so the prose alone does not close it.

**40:00 is not reachable** without dropping something you would miss: with every item in this
document applied you land at 43:51. If the real constraint is the 45-minute slot rather than the
40-minute target, then groups A and B plus frames 35 to 37, 18 and 24 get you there, and nothing in
that set is a claim the room will notice missing.

## Also worth knowing

- The cut ladder inside `SPEAKER_SCRIPT.md` is **stale** — sized when the script measured 47:26 at
  120 wpm, against a script that is now 52 frames and measured at 126. Its *ordering* is still
  right; its landing times are not. Re-size it before trusting it on the day.
- ~~Three `[CLICK]` cues are out of sync with the deck.~~ **Fixed 2026-09-10.** A3.2 (frame 27),
  A3.11 (frame 32) and A3.22 (frame 44) now match; `measure-script.py` reports a clean audit.
