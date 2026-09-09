# Script pass, 2026-09-09: A1.6 to the close, for clarity and register

Andreas edited A0.1 to A1.5 himself and asked for the rest of `SPEAKER_SCRIPT.md` to be brought to
the same standard: clear first, precise and scientific second, and not verbose. This is the
record: what was wrong, the rules taken from his own beats, what changed in each beat, and what
was left for him to decide. The before-version is in git (`SPEAKER_SCRIPT.md` at `d74ec50` plus
his uncommitted edits); `git diff` gives every sentence.

**Not touched:** the bodies of A0.1 to A1.5 (only frame numbers in their headings, and one `[CLICK]`
cue in A1.5 where the deck reveals the prior line on a click); the Q&A tiers; the register notes;
the number ledger at the end; the deck.

## 1. Diagnosis

Read against the deck, slide by slide, the old beats had seven problems. Examples are verbatim.

1. **Sentences that perform instead of explain.** *"But look at the pair."* *"Here is the sentence
   I would most like you to keep."* *"That is the comparison."* *"It cannot be anything else."*
   *"That last row is the paper."* *"Those three rarely come together."* *"On top of it. Not above
   it."* *"And here is the difficulty that shapes everything after."* Each is a punchline. None
   carries content the slide does not already show, and each reads as written prose rather than a
   sentence a person says to a room.
2. **Antithesis as a tic.** *"the gain is not a global normalisation — it is small-scale
   reconstruction fidelity"*, *"What that buys is not convenience"*, *"So the question is never
   whether… It is whether…"*, *"not a diagnosis"*, *"not just another statistic"*, *"not a
   network's guess in one pass"*, *"they pay in different currencies"*. Replaced by the positive
   statement.
3. **The speaker narrating his own script.** *"which is worth twenty seconds because we meet it
   again"*, *"So, thirty seconds."*, *"Remember it, because…"*, *"hold this one too"*, *"Be precise
   about the peak counts"*, *"Two things to leave you with"*, *"the objection I would raise
   myself"*. The sentence announces what the next sentence will do instead of saying it.
4. **Imprecision where the slide is precise.** *"the same three pieces"* on a slide with two terms;
   *"fits the shear better and may be nonsense as a map"* for *not necessarily consistent with the
   prior*; *"never sees the mask, never sees the survey"* for *the mask and noise covariance enter
   only in the data term, at inference*; *"reliable uncertainties"* for the table's *fast UQ*;
   *"most hand you a point estimate"* against a table where DeepMass has fast UQ; *"unsupervised
   methods"* for the slide's *model-driven*; *"smoothed itself into noise"*; the Part 4 bias
   described without saying what it is measured against; *"five slices"* for a four-bin analysis
   illustrated with a five-bin figure.
5. **Vocabulary the room does not use.** *currencies, buys, nailed down, hero, rides, the hinge,
   the light, hair, instrument, machinery, runs away into noise, backfires.*
6. **Saying things twice.** The proximal operator taught in A1.9 and again in A2.3; the
   *no-likelihood* motivation on A3.12, A3.13 and A3.16; *held fixed* on A1.11, A3.1 and A3.2;
   *everything so far was on clean simulations* opening both A4.0 and A4.1; *who covers with the
   tightest bars* in two forms on A2.7.
7. **Stale mechanics.** Every main-line frame number from the old 6 onward was one too high (the
   two-tensions vertical went to backup 55 and the script was not renumbered); the 157 % slide had
   a `[CLICK]` and no fragment; the tool reported 30 cue mismatches. Now 0.

## 2. The rules, taken from A0.1 to A1.5

- Say the thing, then stop. No sentence whose job is to point at another sentence.
- Define the object in its own terms first (*spin-2 field*, *ill-posed inverse problem*,
  *irregularly sampled*, *mask*), then why it matters, in one clause.
- Plain connectives are fine (*So*, *However*, *In particular*, *Lucky for us*); rhetorical ones
  are not (*And here is…*, *Which tells you…*, *That is the comparison*).
- Complete sentences. Fragments read as slide bullets.
- **▲** only on what must survive verbatim: a concession, a result, a definition the argument
  rests on.
- `>` notes only for facts: a number on a borrowed figure, an answer to hold, a short path.
- Numbers in words, as the register notes already say.
- Each act ends by answering its question in one sentence, since the four questions are the
  spine and the close returns to them.

## 3. What changed, beat by beat

| beat | frame | what it now does |
|---|---|---|
| A1.6 | 14 | States Kaiser–Squires plainly, then the three limitations in the slide's order (noise amplification with the colour-scale evidence, mask leakage, the constant), then smoothing as the practical control. The *"look at the pair"* / *"the small scales we came for"* pair is gone. |
| A1.7 | 15 | The two-term optimisation, in the slide's words: data-fidelity term, regulariser encoding the prior; then each method as its regulariser. *"the whole history of mass mapping is a history of the second one"* and *"hold this one too"* gone. The forward pointer to Part 3 was dropped; A3.13 stands on its own. |
| A1.8 | 106, skip | Cleaned, banner shortened. |
| A1.9 | 16 | Two components, alternating minimisation, then the proximal step defined as on the slide (gradient step gives v; prox returns the closest map consistent with the prior; thresholding for sparsity). One sentence on why it is mentioned. |
| A1.10 | 17 | Different priors, different maps; methods compared on map quality until now; the parameters are the product; then the Euclid question as the slide asks it. *"argued about, with something concrete riding on it"* gone. |
| A1.11 | 18 | The held-fixed pipeline read off the boxes; the click on *the only thing that varies*; one sentence deferring the statistic and the inference to Parts 3 and 4. |
| A1.12 | 19 | The three maps described, the Euclid-baseline point in the slide's words. *"different in kind"*, *"That is the comparison"* gone. |
| A1.13 | 20 | The ratios, the iKS null result with its reason, the 4 % against 157 % contrast, the survey implication. Stale `[CLICK]` removed. Two `>` notes: precision, and the RMSE-versus-FoM kernel caveat from `PAPER_FACTS.md` §2. |
| A1.14 | 21 | The scale ladder as on the slide, the interpretation in the slide's words, and the answer to question one. |
| A2.1 | 22 | Part 2 named, question two asked in the divider's words, the authorship line. *"the same box lit again"* gone (the divider has no chain). |
| A2.2 | 23 | The four columns as the table defines them (*fast UQ*, not *reliable uncertainties*), each row read correctly, including DeepPosterior as the flexible-but-slow one. |
| A2.3 | 24 | The iteration, the plug-and-play substitution, the fixed point, the denoiser, and the reason it is flexible stated as the slide states it: noise covariance and mask enter only in the data term, at inference. Short path kept. |
| A2.4 | 25 | Two frames since 2026-09-09 (Andreas): iteration 1 shown at once, iteration 2 on one click. The beat now describes the picture and starts from zero, as the figure does; the old beat said Kaiser–Squires. |
| A2.5, A2.6 | 112, 113, skip | Cleaned; A2.6 kept in full for questions. |
| A2.7 | 26 | Three sentences on the UQ (second network, conformal calibration, distribution-free guarantee), then the plot read as the slide reads it, the two claims, the two clicks, the two limitations, the answer to question two. |
| A3.1 | 27 | The second half named, question three asked out loud (there is no Part 3 card). |
| A3.2 | 28 | Cue order follows the deck: click 1 reveals the sentence, click 2 lights the chain. |
| A3.3 | 29 | The two-point function defined, why it is the standard, then the Gaussian-completeness line as on the slide. *"I am not here to tell you it is a bad statistic"* gone. |
| A3.4 | 30 | What the two fields are (a simulated LSS map and a Gaussian field with the same power spectrum, per the figure's alt text). |
| A3.5 | 31 | Amplitudes kept, phases discarded, the list of higher-order statistics from the slide. |
| A3.6 | 32 | The Ajani forecast with the right colours (blue power spectrum, green single-scale peaks, red and black multi-scale) and the right parameters (Σmν, Ωm, As), checked against the figure. |
| A3.7–A3.9 | 100–102, skip | Cleaned. |
| A3.10 | 33 | The wavelet definition as on the slide, and the three reasons on the click. The *"I have put the words on the screen without defining either"* opener gone. |
| A3.11 | 34 | One-point statistics on the starlet transform; the four clicks in the deck's order (peaks, their shape, ℓ1, its shape). *"our analytical hero"* gone. Band-label caution kept. |
| A3.12 | 35 | Two clicks, the slide's two sentences. |
| A3.13 | 36 | Bayes' theorem read as a sentence, the Gaussian likelihood and why it holds for the power spectrum, MCMC, then why it fails for the higher-order statistics. |
| A3.14 | 37 | Generative modelling defined as on the slide; the density property named as the one we need. |
| A3.15 | 38 | The flow defined as on the slide; conditioning on the click. |
| A3.16 | 39 | Sample from the likelihood, train the conditional flow, amortised inference, coverage tests, and the fact that every posterior in Parts 3 and 4 passed one. |
| A3.17 | 40 | The objection stated, then the click line and the matched-comparison point. |
| A3.18 | 41 | What VMIM optimises, and what reaching it means. The *"not just another statistic"* antithesis gone. |
| A3.19 | 42 | The matched setup, now naming the four tomographic bins, which A3.20 needs. |
| A3.20 | 43 | The 36 % result, the asymmetry, and the refusal to diagnose before the experiment. |
| A3.21 | 44 | Eight clicks, no bin count spoken (the figure shows five, the analysis uses four). |
| A3.22 | 45 | The two routes as the slide names them; the joint ℓ1-norm defined as on the slide (grid, ½(|u_i|+|u_j|) per cell); the difference between the routes in the slide's words. |
| A3.23 | 46 | The four numbers as printed in the slide's inset, the tie called a tie, the sufficiency reading. Violins note points at backup 87. |
| A4.0 | 47 | Part 4 named, question four asked in the divider's words. |
| A4.1 | 48 | Baryonic feedback defined, the dark-matter-only training named, the optimistic and pessimistic cases on their clicks, the slide's two questions. No repeat of A4.0. |
| A4.2 | 49 | Four clicks, and the one load-bearing detail. |
| A4.3 | 50 | What the bias is (tension between the posteriors from a baryonified and a dark-matter-only mock, estimator trained on dark-matter-only, per the paper), the numbers, the growth with area, and the concession. |
| A4.4 | 51 | The criterion, the two cuts, the dyadic limitation and why the wavelet cut is conservative. |
| A4.5 | 52 | The three clicks, the ratios, the complementarity line from the slide, the peak-count position, the two closing points, the answer to question four. `>` note carries the ±0.6 band and the 2,000 deg² caveat from the ledger. |
| A4.6, A4.7 | 66, 67, skip | Cleaned, kept in full for questions. |
| C.2 | 53 | Four answers, each opened by naming its subject in a few words rather than re-reading the question, and a two-sentence close that ties *trustworthy* to the calibration checks. |

## 4. Frame renumbering

The two tensions left the main line (backup 55), so every main-line frame from the old 6 onward
was one too high. Beat headings, act headers, the budget table and the cut ladder now carry the
new numbers; the historical tables under *The animation policy* and *Seven slides moved to backup*
are dated records and were left as written, with a note above them. Backup numbers were already
right.

## 5. Timing

Measured at 120 wpm by `tools/measure-script.py`, cues excluded:

| | before (2026-09-07 script, Andreas's Act 0) | after |
|---|---|---|
| Act 0 | 8:46 | 8:46 |
| Acts 1–4 and close | 37:57 | 38:40 |
| total spoken | 46:43 | 47:26 |
| cue mismatches | 30 | 0 |

The rewrite is 0:43 longer over 45 frames than the version it replaces, after two trimming
passes. The old sentences were short because they were punchlines; the precise sentence is
usually longer. What remains is structural and is in the cut ladder: tier 1 (frames 25 and 49,
−0:57) and tier 2 (frames 36–38, −2:26) land at 44:03. Act 0 is Andreas's own and was not
touched; A0.8 alone measures 3:28.

## 6. Left for Andreas

- **A3.2's click order.** In the deck, click 1 reveals the sentence and click 2 lights the chain
  (`data-fragment-index` 1 and 2). It would read better the other way round. The script follows
  the deck as it is.
- **The tie slide prints absolute figures of merit** (2448 / 3045 / 3371 / 3326) in its inset,
  against `STRUCTURE.md` §7's ratios-only rule. The script speaks them because the slide shows
  them.
- **×1.8 at Stage IV carries a ±0.6 band.** The ledger asks for "about a factor of two" out loud;
  the slide and the conclusions say ×1.8, so the script says one point eight and carries the band
  as a note on A4.5.
- **The Q&A tiers** were not rewritten. They are in a different register (answers, not delivery)
  and read fine; a few tics remain (*"A fair objection, and it deserves the working"*, *"the
  limitation I would attack"*).

## 7. Addendum, later the same day

A Part 3 card went in at frame 40, after the SBI slide, opening the joint ℓ1 paper (Andreas). Question
three moved from A3.1 to the new beat A3.16b, and every frame from 40 onward in the table above is one
higher in the deck now (A3.17 is 41, the close is 54, the backup starts at 56). The Part 4 card carries
arXiv:2609.09131, and the two *in prep.* source lines for the joint ℓ1 paper now say *submitted*.

Frame 35 (A3.12) was then simplified to match Andreas's own rewrite of the beat: the slide now says only
that the summary statistic is compared with theoretical predictions in a Bayesian framework, with the
summary, inference and posterior steps lit from the start and no clicks. The no-likelihood point and the
simulations lane are made later, on the SBI slides.
