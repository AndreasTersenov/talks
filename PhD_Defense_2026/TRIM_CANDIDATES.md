# Where the time is, and what can come out — 2026-09-10

A read of every spoken beat in `SPEAKER_SCRIPT.md` against the slide it is spoken over, looking for
repetition, overexplaining, and material that can be passed over quickly. **Nothing here has been
applied.** Each item names the beat, what would go, and what it saves.

## The measurement it is based on

`tools/measure-script.py PhD_Defense_2026 --wpm 110` on the script as of 2026-09-10, with the
conclusions rewritten and A0.8 shortened. Cues, blockquote notes and HTML comments are excluded, so
these are spoken words only.

| rate | spoken |
|---|---|
| 100 wpm | 61:25 |
| 110 wpm | **55:49** |
| 120 wpm | 51:10 |

**110 wpm is the planning number**, and even that counts only words. It does not count the pause
after a headline, the seconds the room needs on a new figure, or turning to the screen and back.
Over 54 frames that is another three to five minutes, so the delivered length as the script stands
is **58 to 62 minutes**, against a 45-minute slot and a 40-minute target.

| act | frames | at 110 wpm | share |
|---|---|---|---|
| Act 0 | 1–8 | 8:56 | 16 % |
| Act 1 | 9–21 | 12:02 | 22 % |
| Act 2 | 22–26 | 5:43 | 10 % |
| Act 3 | 27–47 | 20:15 | 36 % |
| Act 4 | 48–53 | 7:24 | 13 % |
| Close | 54 | 1:31 | 3 % |

## The one structural fact

Act 3 is 20:15 of the 55:49, and five of its frames are machinery that carries none of the results:

| frame | beat | at 110 wpm |
|---|---|---|
| 33 | wavelets | 1:40 |
| 36 | classical inference | 1:21 |
| 37 | generative modelling | 1:04 |
| 38 | normalizing flows | 1:11 |
| 39 | simulation-based inference | 1:08 |
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
| **A4.1** | Three sentences saying systematics have to be assessed at the contour level. Frame 49's lead line says exactly that, on screen. | 0:16 |
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
| Frames **36, 37, 38** — classical inference, generative modelling, normalizing flows | 3:36 | Nothing the room needs. A3.16 opens with the one sentence that replaces them. This is the cut ladder's existing tier 2. |
| Frame **19** — the three maps | 0:51 | Frame 18's chain shows them in miniature. |
| Frame **25** — the PnPMass iteration | 0:37 | A2.3 has already described it. Tier 1 in the ladder. |
| Frame **33** — the wavelet excursion | 1:40 | A real loss. It is what stops the ℓ1-norm sounding arbitrary, and Part 4's scale cuts lean on scales being separable. **Take this one last.** |

---

## Where it lands

| after | total at 110 wpm |
|---|---|
| now | 55:49 |
| + group A, repetition | 53:42 |
| + group B, slide-reading | 52:32 |
| + group C, overexplaining | 51:00 |
| + frames 36–38 | 47:24 |
| + frames 19 and 25 | 45:56 |
| + frame 33 | 44:16 |

**Two conclusions.**

Everything short of group D buys about five minutes, taking the talk from 56 to 51. Fifty-one is
still six minutes past the slot, so the prose alone does not close it.

**40:00 is not reachable** without dropping something you would miss: with every item in this
document applied you land at 44:16. If the real constraint is the 45-minute slot rather than the
40-minute target, then groups A and B plus frames 36 to 38, 19 and 25 get you there, and nothing in
that set is a claim the room will notice missing.

## Also worth knowing

- The cut ladder inside `SPEAKER_SCRIPT.md` is **stale**. It was sized when the script measured
  47:26 and still claims its tiers land at 44:03. Re-size it against these numbers before trusting
  it on the day.
- Three `[CLICK]` cues are out of sync with the deck: A3.2 on frame 28 (one cue, two fragments),
  A3.11 on frame 34 (one cue, four fragments), A3.22 on frame 46 (two cues, three fragments).
  `measure-script.py` prints them on every run.
