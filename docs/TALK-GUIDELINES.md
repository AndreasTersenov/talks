# Talk guidelines

Standing guidance for building talks in this repo. Not a style sheet for slides — `../CLAUDE.md`
covers the mechanics (themes, asset paths, reveal.js). This file covers **what to say, in what
order, and what to put on the screen while saying it.**

Written 2026-08-19 from the sources in §12, filtered through what actually applies to a
computational cosmologist giving weak-lensing / SBI talks. Where the sources disagree, the
disagreement is stated rather than smoothed over, and a house call is made.

Read §1–§3 when planning a talk. Read §4–§6 when building it. Read §10 the day before.

---

## 1. Before you open the editor

Three questions, answered in writing, before a single slide exists. Peyton Jones et al. put the
first two at the head of their paper and they have not aged:

1. **Who is my primary audience?** Not "cosmologists" — the actual room. A COSMO parallel
   session is mostly people who do not work on weak lensing and will not know what a starlet is.
   A CosmoStat group meeting is four people who know your pipeline better than you do. These are
   different talks about the same work.
2. **If someone remembers exactly one thing, what should it be?** One sentence. If you cannot
   write it, you are not ready to build slides. **And then tell the audience the answer** — do
   not make them infer it.
3. **What do I want to be different afterwards?** Ernst's framing: decide what the change is and
   build the talk around it. Read the paper. Cite the method. Stop using the broken construction.
   Offer you a postdoc. The change dictates what belongs and what does not.

A talk is a **taster, not a treatment**. Its job is to make people want the paper, not to
substitute for it. This single reframe kills most over-stuffing.

**The three things you must convince them of** (Ernst): the problem is real and worth caring
about; the problem is *hard* — the obvious thing does not work; and you have solved it (or moved
it). Drop any of the three and the talk deflates. Most scientific talks are weakest on the
second: they establish that a problem exists and that the speaker did something, but never make
the audience feel why it was not easy.

---

## 2. Narrative

### 2.1 The ABT spine

Randy Olson's *And, But, Therefore*: state the shared context (**and**), introduce the conflict
(**but**), deliver the consequence (**therefore**). Talks that fail are almost always "and, and,
and" — a list of true statements with no tension. Write the ABT for your talk in one sentence
before anything else:

> Stage IV lensing will measure the non-Gaussian field to percent precision **and** higher-order
> statistics are the tools built to read it, **but** they live on exactly the small scales where
> baryonic feedback is worst and where a nulling transform appeared to destroy their
> constraining power, **therefore** we asked what actually survives — and found the loss was the
> analysis frame, not the information.

If the "but" is weak, the talk has no engine. Go find the real tension.

### 2.2 Open with the problem, not with an outline

Do **not** open with a contents slide. Peyton Jones is blunt: it costs a precious minute, the
audience cannot understand it yet, and "introduction / methods / conclusion" is trivia everyone
already assumes. Ernst agrees — the first substantive slide should be motivation and a concrete
example.

Instead, spend the first ninety seconds making them care. A picture of the thing. A number that
should worry them. A plot with a gap in it.

**Do state your conclusion early.** Hull's argument is practical: if you run over, or if someone
falls asleep in the middle, at least they got the claim. State it near the front, restate it at
the end, and — for a longer talk — once in the middle. Never say "I'll keep you in suspense";
that is a recipe for the audience checking out.

These two are not in tension: skip the *table of contents*, keep the *thesis statement*.

### 2.3 The question slide — an outline done right

§2.2 says no contents slide. Karen Fleming's rules supply the thing that should be there
instead, and it resolves the tension cleanly.

After the introduction, put up **one slide stating the questions the talk will answer** — she
calls it the Big Biological Question slide; for us, the big *cosmological* question. Three is
ideal, four the ceiling. Every question must already have been motivated by the introduction, so
the slide lands as a payoff rather than as bureaucracy.

Then — and this is the part that makes it work — **you come back to it.** Each time you answer a
question, return to the slide, write the answer next to it, grey out that line, and move to the
next. It becomes a running scoreboard that gives you a free, natural transition into every
section, and it means anyone who drifts off can re-enter the talk at any point.

This is not "Outline: 1. Intro 2. Methods 3. Results", which is what Peyton Jones is rightly
scathing about. It is a statement of the actual scientific questions, and it is one of the very
few slides where **words are allowed and you should read them aloud**.

Both of our papers already state their aims as numbered questions in the introduction. That list
is the question slide, lightly rewritten for the ear.

In this repo the return-visits are cheap: one slide, repeated, with `fragment` state advancing —
or three near-identical sections with the answered lines carrying `var(--fg-muted)`.

### 2.4 Non-uniform depth

The central tension of a talk: say enough to convey the idea, without burying the audience. The
resolution is **not** to compress everything uniformly — that gives a superficial treatment of
everything, which is worse than a deep treatment of some things. Pick what to do properly and be
frank about skipping the rest ("this took six months and I'm going to spend twenty seconds on
it; the details are in §4 of the paper").

### 2.5 Examples before abstractions

Peyton Jones calls presenting only the framework and the abstraction, with the motivating
examples stripped out, **the Awful Trap** — and says the need for examples is the single most
important point in his paper, because so many talks fail on it. Slide after slide of
impressive-looking formalism leaves the audience no wiser.

For us this means: show the **map** before the summary statistic. Show a **single wavelet band**
before the ℓ1 data vector. Show **one patch** before the population distribution. Concretely
first, generality second.

### 2.6 Tell it how it is

Do not conceal the problems you know about. It is dishonest, and it is also *ineffective* — a
bright audience finds you out, and the person who finds you out will be the one asking the first
question. Being open has a payoff: someone in the room may hand you the fix.

This matters more than usual for our work, where the failure modes are subtle. Concrete house
rules, distilled from what has already bitten these talks:

- **Never chain incomparable numbers into one ladder.** A full-sky FoM and a 10° patch FoM are
  not on the same axis. Two sentences, always.
- **Quote the number you can defend, not the one that sounds best.** If the effect is ×1.8 at
  Stage IV and ×2.6 at full sky, say both and say which regime matters.
- **Say "calibrated" when it is, and say what that means.** A tight contour is worthless if it
  is wrong; if you have run coverage tests, that is a feature worth thirty seconds.
- **Flag forward-looking statements as forward-looking.** "This is a next step, not a
  measurement" costs one clause and buys all your credibility back.
- **Every number on a slide traces to a source.** For a talk built from papers in flux, keep a
  ledger file in the deck directory (see `cosmo26/PAPER_FACTS.md` for the pattern) and treat it
  as the authority. Numbers drift between drafts; slides do not notice.

### 2.7 Do not glue an old deck together

Peyton Jones, on reusing slides across talks: *"Regard with extreme prejudice the temptation to
pull out old slides from previous talks and glue them together into a new talk. It almost always
shows. Somehow the old slides are never quite appropriate."*

We fork decks in this repo, which is efficient for *mechanics* — theme wiring, components, asset
paths. It is a trap for *content*. A forked deck arrives carrying the previous room's framing,
the previous talk's length, and the previous draft's numbers, and all three are invisible
because they look finished. When forking: keep the chrome, re-derive the argument from §1.

---

## 3. Format budgets

**Timing is the one rule with no exceptions: do not exceed your slot.** Everything else here is
a default you may override with a reason.

**A note on slot conventions.** Fleming's slide counts assume the quoted slot *includes* Q&A
(her "15-minute slot" is 11–12 min of speaking plus 3–5 of questions). Ours usually do not —
"15+3" means fifteen minutes of talking. Read her compositions for the **mix of slide types**,
which is the valuable part, and take the minute counts from this section.

### 3.1 The 12–15 minute contributed talk

The dominant format at large conferences, and the least forgiving. You are one of many that day.

- **Plan to finish 1 minute early.** At 15+3, plan 14:00 of material. Audiences do not
  interrupt short talks, so the buffer is yours.
- **11–13 slides.** The old "one slide per minute" heuristic is a reasonable ceiling *for static
  slides*; Hull explicitly rejects it as a hard rule because build-ups and overlays are often
  several slides for one beat. House rule: **count beats, not slides.** One beat ≈ one minute.
- **One message. Two supporting results. That is the whole budget.**
- Rough shape: title 0.5 · problem and stakes 2 · just enough method to read the results 2.5 ·
  results 6–7 · conclusions 1.
- Fleming's composition for the same length, which is a good sanity check on the mix:
  **2–3 background · 1 question slide · 6 data · 1 conclusions**. If you have ten data slides and
  one background slide, you have built a paper, not a talk. If you have six background slides and
  three data slides, you have built a lecture.
- **Results get at least 40 % of the time.** If your methods section is longer than your results
  section, you are giving the wrong talk.
- Assume nothing. Pitch the first third at someone in an adjacent subfield.

### 3.2 The 30-minute invited talk

- Plan 26–27 minutes. ~18–22 beats; Fleming caps a 30-minute talk at 25 slides.
- Composition: **4–5 background · 1 question slide · 4–5 slides per question · 1 conclusions and
  future directions · 1 acknowledgements.**
- Affordable extras: one pedagogical detour on the method that makes the result legible, and one
  "how we got here" beat that gives the work a history.
- Still one central message. The extra time buys *depth*, not more claims.

### 3.3 The 45–60 minute seminar or colloquium

- **Plan ~40 minutes of material for a 60-minute slot.** Hull's reasoning: if the audience is
  lively you can answer everything and still finish on time; if they are silent you finish early,
  which nobody has ever complained about.
- **Rule of thirds on expertise.** First third: comprehensible to every physicist in the room.
  Second third: for people in your subfield. Final third: for the handful you came to talk to —
  but do not aim so narrowly that you lose the room at minute 45.
- Never underestimate how much people enjoy hearing something they already know, explained well.

### 3.4 Planned exits

Mark, in the deck, **two places where you can drop a block of slides** without breaking the
argument, and check the clock when you reach them. In this repo, park them with
`data-visibility="hidden"` if you cut before the talk, or just know their indices if you may cut
live. Also keep a couple of slides you *expect not to need*, in case you finish early.

When the chair signals time: **do not sprint through the remaining slides.** Skip to the
conclusion and land it. Racing to the end and then glossing the conclusions is the worst
possible outcome — you skip the only part that mattered.

---

## 4. Slide design

### 4.1 Assertion–evidence

The house standard, and the one rule here with a controlled experiment behind it. Michael
Alley's structure:

- The **headline is a full sentence stating the slide's message** — not a topic phrase. One to
  two lines, ~8–14 words.
- The body is **visual evidence for that message** — a figure, a diagram, a schematic — not a
  bullet list.
- You **speak the connecting sentences**; they are not on the slide.

Audiences shown assertion–evidence slides understood and remembered the content significantly
better than audiences hearing identical words over topic-phrase-plus-bullets slides (p < .01).

So: not `Results`, but `On baryon-safe scales the ℓ1-norm still beats the power spectrum by 1.8×`.
Ernst's corollary: **never repeat a slide title** (except across build steps), and if you cannot
state a slide's message in a sentence, you do not yet understand what it is for.

**The test for writing one** (Fleming): the title fills in the blank in *"What I want you to know
is ________."* If you cannot complete that sentence, the slide has no point yet — or it has two,
in which case split it.

Two forcing functions that follow:

- **One line ideally, two acceptable, never three.**
- **If the title only fits by shrinking the font, split the slide.** Titles want ~28 pt and must
  never drop below ~24; treat a title that will not fit at that size as a signal about the
  content, not about the typography.

Titles are also the recovery path for anyone who drifted: if someone daydreams through your data,
the title is what tells them what they missed. That is why they must be big, consistent in
position, and readable in isolation.

This repo's `.slide-title` class is built for exactly this. Use it.

### 4.2 Do not put on the screen what you are about to say

Peyton Jones: *"Slides shouldn't repeat what you plan to say, but they should emphasise it;
don't waste visual bandwidth on things you are also going to say."* This is Mayer's **redundancy
principle** independently rediscovered — people learn *worse* from graphics plus narration plus
on-screen text than from graphics plus narration, because reading and listening compete.

Fleming pushes this to its logical end, and her argument for the strict version is the sharpest
formulation of it I have seen: **if you put words in the content area of a slide, you are
obliged to read them**, because otherwise the audience's eyes and ears are receiving different
input and one of them loses. And reading your slides aloud is boring. Therefore: do not put the
words there. *"Slides should generally have no words except the title."*

The practical failure mode is the speaker reading their own bullets. The audience finishes
reading before you finish saying it, and then tunes out.

**The three exceptions**, where words are allowed *and must be read aloud*: the question slide
(§2.3), the conclusions slide, and the rare case where the words are the content (a definition, a
short derivation you will walk through symbol by symbol).

If you need the words to remember what to say, put them in **speaker notes**
(`<aside class="notes">`), not on the slide.

### 4.3 Text discipline

**The one real disagreement between the sources.** Peyton Jones allows six or seven "things" on
a slide; Fleming allows approximately zero. Both are arguing from the same premise (the audience
cannot read and listen at once) and reaching different ceilings.

**House call: Fleming's rule is the target, Peyton Jones's is the hard ceiling.** Build toward a
figure with a sentence headline and nothing else; if a slide has drifted past six or seven
elements it is not a judgement call any more, it is broken. Our decks currently sit closer to the
ceiling than the target, and that is the direction to move in.

- Six or seven "things" on a slide is already plenty.
- Two full lines of text in a bullet is over the limit; three is far over.
- **If you have to shrink the font to make it fit, cut the content instead.** The font size is
  telling you something true.
- Emphasise **1–3 words per line**, not whole lines. Emphasis everywhere is emphasis nowhere.
- Large fonts. A large font is not just legibility — it is a **constraint that limits what fits**,
  which is the point.
- Kill the standing furniture: no "Outline", no "Thank you" slide, no "Questions?" slide. Ernst:
  end on your **conclusions** and leave them up during Q&A, so the room stares at your claim for
  ten minutes instead of at the word "Questions".

### 4.3b House typography rules

Three standing rules, all learned the hard way. They apply to every slide in every deck.

**No automatic uppercasing.** Never `text-transform: uppercase` in a stylesheet, and no
SHOUTED words in markup. CSS-driven small caps read as machine-set and are one of the clearest
tells that a slide was generated rather than written. Author label case in the markup, in
lowercase, and let the mono font and the accent colour do the distinguishing. The shared theme
(`assets/themes/talks.css`) was purged of all five of its uppercase rules on 2026-08-19; if a
new component wants a label, give it lowercase mono and tight letter-spacing (~0.06em).
Wide tracking is for caps; on lowercase it just looks loose.

**No middot separators.** `&middot;` strung between phrases (`Name · Place · Date`) is a
layout tic. Use a comma, a line break, or actual whitespace. If two things need separating
strongly enough that punctuation will not do, they want two elements, not one line.

**Related items get containers, not bullets.** When two or three items are peers that the
audience should compare, give each its own bordered card with a small label, rather than
running them as list items. Bullets say "here is a list"; cards say "here are two distinct
things", which is usually the actual message.

### 4.3b(ii) The root cause: prose on the slide

Small type, cramped titles and wide-short slides are almost always **one** fault wearing three
disguises. The fault is a paragraph on the slide. A three-line block of prose at the bottom of a
figure slide eats the vertical space the figure needed, forces the figure into a wide letterbox,
and pushes every label down a size to fit. Fixing the type, the height and the gap separately
treats the symptoms and the paragraph comes back on the next slide.

The check that actually works, applied before any styling: **read every sentence on the slide and
ask whether you will also say it out loud.** If yes, it belongs in `<aside class="notes">`, not on
the screen (§4.2, the redundancy principle). What survives is a title, a visual, short labels, and
at most **one** line of text — a claim or an honesty flag the visual genuinely cannot make.

Two consequences worth stating separately, because both were violated repeatedly while building
the COSMO-26 deck:

- **A caveat is not exempt.** Honesty flags feel obligatory on the slide, but a spoken caveat is
  just as honest and does not cost a third of the frame. Put the short form on the slide (five to
  ten words) and the full version in the notes.
- **A conclusion the title already states is not content.** If the headline says *"reaches the
  ceiling"*, a box below saying *"both summaries saturate the accessible information"* is the same
  sentence twice. Delete it.

**Shortening is not the same as vagueing.** Cutting words must not cut the *scope* of a claim.
"How much does unmodelled feedback bias us?" is shorter than "...bias our higher-order
statistics?" and also wrong, because it silently widens the question to every statistic. And
prefer the phrasing that names what is at stake: *"is there any constraining power left to gain
over the power spectrum?"* rather than *"do we still beat the power spectrum?"* — the first asks
about information, the second about winning.

**The saved space has to be spent.** Removing a paragraph and leaving the figure the same size
just moves the emptiness. Grow the visual, or grow the one surviving line into a real element:
left-aligned, at body size, with a rule beside it. A small centred grey line under a figure reads
as an apology, not as a claim.

Bullets in a comparison should be **phrases, not sentences** — "no training, nothing to overtrain",
not "Defined before any simulation is seen: no training, no architecture search, nothing to
overtrain." The verb is yours to speak.

### 4.3c The type floor, and what small type actually means

**Nothing on a content slide sits below `0.62em`** (≈26px at the 1200×720 base, ≈42px projected
at 1920). That covers captions, axis notes, figure labels, table headers, everything. Figure
labels drawn inside an SVG must clear the same bar once the render scale is applied.

The rule matters more than it looks, because **small type is almost never a type problem.** It is
the symptom of a slide that has been asked to hold too much, and the instinctive fix — shrink it
until it fits — hides the real fault. Fleming's version: *if you need to minimise the font so you
can fit everything on there, you should reduce the content on the slide.* When something will not
fit at 0.62em, cut it, move it to the notes, or split the slide.

Two corollaries that came out of building this deck:

- **Long prose is never monospace.** Mono is for labels, values, and eyebrows — three or four
  words. A three-line caveat set in mono is markedly harder to read than the same text in the
  body face, and it looks like console output.
- **A slide that is very wide and very short is a slide with a missing dimension.** If content
  spans the full width but only the top third, it usually means a figure is doing too little work
  or a two-column block wants to be taller. Fill the frame or cut the slide.

### 4.3d Do not spend a slide on a graphic the data already carries

A chart that restates numbers the audience will see again in a real figure is not free: it costs
a full minute and the attention that goes with it. If a hand-built graphic duplicates a paper
figure you are also showing, either drop it or shrink it to a supporting element and give the
freed space to something the figure cannot say — the marginal uncertainties behind a
figure-of-merit claim, the interpretation, the caveat.

The test: *what does this slide say that the next slide does not?* If the answer is "the same
thing, drawn differently", it is not a slide.

### 4.4 Builds and fragments

Mayer's **segmenting principle**: breaking a complex slide into progressively revealed parts
improves comprehension. Reveal's `fragment` classes are for this.

But do not line-by-line-reveal ordinary bullets. Peyton Jones is scathing about it — it is
condescending ("you can't be trusted to listen if I show you the next line") and if you feel the
urge, the material probably wants two slides. Reserve builds for: a genuine punchline, a
genuinely staged process, and adding curves to a plot one at a time.

**Build steps must be pixel-identical in their shared parts.** Ernst's test: flip between them
fast; any jitter means misalignment. Pre-allocate the space that later elements will occupy,
even if the early step looks slightly empty. In this repo that usually means fixing a
`max-height` on the image stack rather than letting each step size itself.

### 4.5 Color and contrast

- **Colour must encode one thing consistently across the whole deck.** In these decks colour
  encodes *method*, not emphasis — CNN blue `#0072B2`, ℓ1 vermillion `#D55E00` (Wong palette).
  Do not spend those colours on anything else.
- ~5–10 % of male viewers are colourblind. Never let colour be the *only* channel: pair it with
  line style, marker shape, or a direct label.
- Contrast rules that get broken constantly: red on black is unreadable, blue on black is
  unreadable, yellow on white is worse. Highlighting the critical word in red on a dark slide
  makes it *invisible*.
- **Do not inline-style colours in this repo** (`style="color:#…"`). It defeats the theme in both
  light and dark. Use the tokens — `var(--accent)`, `var(--fg-muted)`, `var(--l1)`, `var(--cnn)`.
  See `../CLAUDE.md`.
- **Contrast is a design tool, not just a legibility constraint.** Dark colours dominate and pull
  the eye; light ones recede. Use that deliberately — dark for the thing you want looked at,
  light for the supporting furniture. Line weights for shapes and overlays want ≥ 2.25 pt.
- **The grayscale test.** Render the deck in grayscale and look at it. It catches colourblindness
  failures and contrast failures in one pass, and it is the cheapest check in this document.
  Note that it is *stricter* than colourblind-safety: Wong blue and Wong vermillion are reliably
  distinguishable to colourblind viewers but sit at nearly the same **luminance**, so they merge
  in grayscale. Run against the existing decks, this is exactly what happens on the calibration
  slides — the ℓ1 and CNN curves become one. Passing the colourblind check is not passing this
  one; if two series matter, separate them by line style or marker as well as hue.
- Match diagram backgrounds to the slide background exactly. A white PNG on a dark slide reads as
  a bug.

**Light or dark backgrounds?** Fleming is unambiguous — *use white, do not use black* — because
white projects better in most rooms. Our default theme is dark, which is a real tension. The
practical resolution, already how the recent decks are built: **the title and section dividers
can be dark, but content slides carrying figures should be light** (`data-theme="light"`). That
also keeps the slides matched to the figures, which are made on white. If you are presenting in a
room you do not know, light is the safer bet.

---

## 5. Figures for talks are not figures for papers

This is where scientific talks lose the most people, and it is the most fixable.

A journal figure is optimised for **high information density, studied at leisure, with a caption
and the surrounding text**. A talk figure is seen for forty seconds, from ten metres, with no
caption, while you are talking over it. Dropping a fully-developed paper figure onto a slide is
worse than showing a paragraph of text.

House rules:

- **Re-plot for the talk.** Not "resize" — re-plot. Fewer panels, fewer curves, bigger
  everything. It is normal for one paper figure to become three talk figures. Fleming's calibration
  on "should I redraw this?": *yes, about 99 % of the time.*
- **Draw your own diagrams**, and keep one cartoon vocabulary across the whole deck — the same
  object drawn the same way every time it appears. A borrowed schematic in someone else's visual
  language costs the audience a re-orientation every time.
- **One message per figure.** If it makes two points, split it or show it twice with different
  things highlighted.
- **Axis labels from papers are always too small.** Crop them off and replace with large,
  intuitive words. `Brightness`, not `erg s⁻¹ cm⁻² Hz⁻¹`. `Tighter constraints →`, not `FoM₃`.
- **Crop or cover anything you will not talk about.** A distracting irrelevant detail costs you
  the forty seconds you needed.
- **Annotate on the slide** — arrows, circles, a one-line callout — rather than describing
  location verbally ("the blue dashed one, third from the top").
- **Make it huge.** "Pixels are finite; slides are infinite." A figure that fills the slide with
  a sentence headline above it is the default layout, not a special case.
- **Never read a diagram aloud.** Explain what the relationships *mean*; the audience can see the
  boxes.
- **Axis labels must be readable from the back of the room** — aim for ≥ 18–24 pt at final
  displayed size. One figure per slide makes this easy; it is impossible with four.
- **No figure legends on slides.** The caption is you.
- **No tables.** Fleming's version is blunter — *"Avoid tables, if at all possible. Seriously. No
  Tables."* A table is a paper object: it rewards scanning at leisure and punishes a reader who has
  forty seconds. Turn it into a plot. This lands directly on us: the FoM tables in both papers are
  exactly the thing that must become graphics before they go on a slide, and the fact that a table
  is *easy* to paste in is the trap.
- **Cite every image, plot and photo** on the slide itself. Decks end up on the web.

One diagnostic worth taking seriously: *if you cannot draw a picture of what you are doing, you
do not fully understand it yet.* When a slide resists becoming a visual, that is usually a
statement about the clarity of the idea, not about your drawing ability.

Corner plots deserve a specific warning: a six-parameter corner plot is unreadable from row
three. Show the 2–3 parameter sub-block that carries your claim, at size, and keep the full
corner in backup.

For the plotting mechanics — colourblind-safe palettes, line weights, font sizes — the
`figure-polish` skill has the numbers. Its target is journal output; for talks, take its palette
and legibility rules and then go **larger and simpler**.

### 5.1 Equations

Show almost none. Hull's position is "don't show them"; the defensible version is: show an
equation only when the equation *is* the point and you will walk through every symbol. One
definitional formula for a statistic the audience has never seen is fine. A derivation is not.
Everything else goes to backup.

---

## 6. Delivery

**Practice out loud.** Not "review the slides" — say every word, standing up. Ideas come out
differently spoken than imagined, and this is the only way to find that out before the room does.

Hull's protocol, which is the best one I found and worth following literally:

1. First run-through: **do not time it.** Fix typos, slide order, build order — everything that
   interrupts flow. This run will be bad. Expect that.
2. Coffee. Then run it again, **timed.** You will be startled how much better it is.
3. If you are way over, delete or park slides and run once more. Do not plan to "talk faster".
4. Practice again **within 24 h** of the talk, ideally the night before.
5. Within a few hours of the talk, **click through every slide silently** to pre-load the order.

**Practise the introduction most.** That is where the nerves peak; if you land the opening you
settle, and the rest follows. It is also the part you can least afford to improvise.

**Practise in the register you want to deliver in.** Under pressure you fall back on your verbal
habits, so build the right ones in rehearsal: we *measure*, *obtain*, *infer* — we do not "get"
the data. This is not stuffiness; it is that the sloppy version is what comes out when you are
nervous, and it undersells the work.

Knowing what slide is coming lets you punctuate the transition with a sentence that sets it up,
which is the single clearest signal to a room that you prepared. Not knowing reads as not caring.

Other things that matter:

- **Face the audience, not the screen.** You need their faces to tell whether you have lost them.
  The one licensed exception, and it is a useful one: when a new figure goes up, turn to it and
  orient the room out loud — *"the y-axis is the figure of merit, the x-axis is survey area"* —
  then turn back and interpret. Orienting to the axes is not the same as reading the diagram
  aloud. Good graphics hand you your own words; the failure mode is staying turned around.
- **Only talk about what is on the slide.** If in rehearsal you keep adding material that has no
  visual anchor, that is not a discipline problem — it is a missing slide. Make it.
- **Point with your whole arm at the screen**, or with the pointer — not at your laptop.
- **Own your pointer and practise with it.** Use it in calm, deliberate strokes to mark one thing;
  do not wave it around the plot. Spare batteries in the bag, and taken *out onto the podium*
  before you start so you are not rummaging mid-talk. Green over red — red lasers are effectively
  invisible to a fraction of the room.
- **Take the microphone whenever one is offered.** And do not ask "can everyone hear me?" — no
  audience member wants to raise their hand to announce they are hard of hearing. Clip it on the
  side nearest the screen so you stay on-mic when you turn your head.
- **No monotone.** Pitch and pace variation is a large part of what keeps a room with you; it is
  the audible version of signalling.
- **Kill the fillers.** "Um" and "uh" are what fills a gap you were afraid of. Silence is the
  better filler, and it doubles as thinking time.
- **Slow down.** Much of any cosmology audience is working in their second or third language. A
  deliberate pause after a dense slide is a gift, not dead air, and it lets you drink water.
- **Adapt live.** If the room looks lost, back up and re-explain. If they are ahead of you, skip.
- **Project some enthusiasm.** You chose to spend years on this; let that show.
- Be yourself. If you are funny, be funny; if you are not, do not perform.
- If you lose your place: pause, drink water, resume. You can silently skip material — nobody
  notices unless you announce it.

---

## 7. Questions and backup

- **Be reflective, not reactive.** This is the whole discipline of Q&A in one phrase.
- **Let them finish** — you do not know what they are asking until they stop. Then **repeat or
  rephrase the question**: it confirms you understood, buys thinking time, and lets the rest of the
  room hear it, since most of them could not. Skip the repeat only when the asker has a microphone
  and is using it well.
- **Rephrasing is legitimate steering.** Questioners often think out loud and never quite land on
  a question. Restating it puts it in a form you can actually answer — and if the question as
  asked is hostile or unanswerable, the restatement is where you redirect it to the version worth
  answering.
- **If the room starts arguing with itself, let it.** When two people in the audience get into it
  over your result, do not interrupt. They will finish. Add something if you genuinely have
  something to add; otherwise thank them and look out for the next hand. It is not your job to
  chair.
- **"I don't know" is a complete answer**, and a better one than improvising. "That's a good
  direction — let's talk afterwards" is also complete. Inventing an answer creates a second
  problem on top of the first.
- **Build the backup pile as you cut.** Every slide you remove for time is a candidate answer to
  a question. Keep them after the conclusion slide, in rough order of how likely you are to need
  them. Park them with `data-visibility="hidden"` if they should not appear in the PDF flow.
- **Write down the three questions you are dreading** and prepare those answers specifically.
  They are usually: a systematic you did not model, a fragility in your headline metric, and
  "why not just use the standard method?".
- If you know the room, look up what the likely questioners work on and cite it. People engage
  differently when their work has been acknowledged.

---

## 8. Field-specific traps

Things that go wrong specifically in weak-lensing / SBI / statistics talks:

- **The figure of merit is fragile** when the posterior is strongly correlated. Show marginals
  alongside it, or a distribution rather than a point, and say so before someone else does.
- **"Tighter" is not "better" unless calibrated.** If you have coverage tests, spend thirty
  seconds on them; it converts a contour plot from an assertion into a measurement.
- **Nobody can read a 6×6 corner plot.** See §5.
- **Simulation-based results carry a forward-model caveat.** State the one that matters (no IA,
  no photo-z errors, one feedback prescription) once, plainly, early — rather than being cornered
  into it during Q&A.
- **Do not present a null or negative result apologetically.** "This does not work, and here is
  the mechanism" is a real contribution; hedging it makes it look like a failure instead.
- **Method names are not explanations.** "We used VMIM" tells the room nothing. One sentence on
  *what it optimises and why that matters* is the minimum, or cut the name entirely.

---

## 9. How this maps onto this repo

The mechanics live in `../CLAUDE.md`; this section is only the correspondence between the
principles above and the machinery here.

| principle | mechanism |
|---|---|
| Assertion–evidence headline | `<h3 class="slide-title">`, with `<span class="sec">§2</span>` for the section marker |
| Speak it, don't print it | `<aside class="notes">` — visible in speaker view (`S`), invisible to the room |
| Segmenting / staged builds | `class="fragment fade-in"`, `data-fragment-index` for explicit ordering |
| Emphasis on 1–3 words | `<b class="alert">` / `class="alert"` — theme accent, never a hex code |
| A result that needs a frame | `.callout` / `.takeaway` / `.stat` (`num` + `label`) |
| Figure matched to a light or dark original | `<section data-theme="light">` — per-section, so PDF export stays correct |
| Question slide, revisited per section (§2.3) | one section repeated with `fragment` state, answered lines dropped to `var(--fg-muted)` |
| Planned exits and backup | `data-visibility="hidden"` parks a slide in the file but out of the deck |
| Number provenance | a `PAPER_FACTS.md` in the deck directory; see `../cosmo26/` |
| Talk plan and running order | a `STRUCTURE.md` in the deck directory, signed off before slide surgery |

**Verification, since there is no test suite:**

- `python3 tools/check-asset-links.py` from the repo root — catches every broken figure path.
- Headless screenshots of a spread of slide indices, then actually look at them. The recipe is in
  the project memory (`talks-headless-screenshots`). Canvas-based components come out blank under
  headless; that is a `requestAnimationFrame` artifact, not a bug.
- **The grayscale check.** Screenshot a spread of slides, desaturate, and look. Everything that
  relied on hue alone will disappear, which is exactly what you want to find out now:
  ```bash
  sips -s format png --matchTo '/System/Library/ColorSync/Profiles/Generic Gray Profile.icc' shot.png --out shot_gray.png
  ```
- **Export the PDF early** (`?print-pdf`), not the night before. It is the fallback when the
  venue's machine will not take your laptop, and it is where build-up slides break.
- Split progressive builds across fragments that survive PDF export, so the PDF still tells the
  story if you have to present from it.

---

## 10. Checklists

### Building

- [ ] The three questions from §1 answered in writing.
- [ ] The ABT sentence written, with a real "but".
- [ ] One-sentence takeaway written, and it appears **on a slide**, early and late.
- [ ] Slide count within the §3 budget for the format.
- [ ] Every slide title is a full-sentence assertion, passing *"what I want you to know is ___"*.
      No duplicates. No "Outline".
- [ ] A question slide after the introduction, revisited as each question is answered.
- [ ] No slide is a transcript of what you will say. Words only on the question and conclusions
      slides — and those you read aloud.
- [ ] No tables. Every table has become a graphic.
- [ ] Every figure re-plotted for the talk: one message, huge, cropped, annotated, cited.
- [ ] Colour encodes one thing, and is never the only channel.
- [ ] Grayscale check passed — nothing depends on hue, contrast survives.
- [ ] Figure axis labels readable from the back of the room; no figure legends on slides.
- [ ] Results have ≥40 % of the time.
- [ ] Every number traces to the ledger.
- [ ] Limitations stated plainly somewhere, not buried.
- [ ] Ends on conclusions — not "Thank you", not "Questions?", not future work.
- [ ] Two planned exit points marked.
- [ ] Backup pile assembled from the cuts, ordered by likelihood.

### Day before

- [ ] Full run-through out loud, untimed, fixing flow.
- [ ] Second run-through, timed. Under budget, without rushing.
- [ ] Slides cut or parked if over. Not "I'll talk faster".
- [ ] Three dreaded questions written down, answers prepared.
- [ ] Introduction rehearsed more than anything else.
- [ ] PDF exported and checked — builds survive, nothing overlaps.
- [ ] Asset-link check clean; screenshots of a spread of slides inspected.

### Day of

- [ ] Silent click-through of every slide, a few hours before.
- [ ] Adapters, USB stick with the PDF, your own clicker, spare batteries.
- [ ] Batteries out on the podium before you start.
- [ ] Notifications off, wifi off, other apps quit.
- [ ] Slides tested on the actual projector if the venue allows.
- [ ] Know how to jump to a backup slide by number.

---

## 11. Talk plan template

Copy into `<TalkDir>/STRUCTURE.md` at the start of a new talk.

```markdown
# STRUCTURE — <venue>, <N> min + <M> Q

## The three questions
- Primary audience:
- The one thing they should remember:
- What should be different afterwards:

## ABT
... **and** ..., **but** ..., **therefore** ...

## Budget
| # | slide (assertion headline) | min | carries |
|---|---|---|---|
|   |                            |     |         |
| total | | | |

## The question slide (3 questions, ideally)
1.
2.
3.

## The three takeaways
1.
2.
3.

## Cut lines
- to N-1 min: drop ...
- to N-3 min: also drop ...

## Backup, by likelihood
1.

## Dreaded questions
1.
```

---

## 11b. The speaker script

Written after the COSMO-26 deck (2026-08), where the script turned out to matter more than any
individual slide. Lives at `<TalkDir>/SPEAKER_SCRIPT.md`.

**Write the words you will say, not a summary of them.** A bullet list of "things to mention" is
not a script; it collapses the moment you are nervous, which is exactly when you need it. Prose
also makes the timing measurable, which bullets never are.

### Format

- `[CLICK]` marks a fragment advance, placed in the sentence where it belongs. **These are load-bearing
  and they go stale.** Every time a build changes, the cues must be resynced — a `[CLICK]` pointing at
  a fragment that no longer exists is discovered mid-rehearsal, at the worst possible moment.
- `〔stage directions〕` for anything you do rather than say: where to turn, where to pause, where to
  point. Never spoken, visually distinct so the eye skips them when reading ahead.
- `**▲**` on sentences that must survive verbatim as the wording drifts in rehearsal. These are the
  ones carrying a claim you do not want to soften under pressure — the concession you make before
  anyone can raise it, the precise statement of a result, the honest caveat.
- A per-section time in the heading, and a total in the header.

### Time the script, do not estimate it

Count the spoken words (excluding stage directions and off-budget asides) and divide by a rate.
**140 words per minute** for an audience working largely in a second or third language; 150 if you
know you speak fast. Recompute after every edit and rewrite the headings from the measurement. An
estimated timing is worse than none, because it is believed.

The number the script must hit is the **planned** length, not the slot: at 15+3, aim for 14:00.

### Cut lines, in tiers

A talk that is over will be cut, and the only question is whether you chose the cuts in advance or
panic on the podium. Write the ladder into the script, each item with its measured saving:

- **Tier 0 — short paths.** For intermediate-result slides, write out a *complete short version*
  alongside the full one. Not a note saying "say less" — the actual shorter prose. A shortcut you
  have to improvise is a shortcut you will not take when you are behind and slightly rattled.
- **Tiers 1–3** — individual paragraphs, ordered, with what each buys. Fold a framing slide's
  paragraph into the next slide's opening sentence: that is usually the cheapest 25 seconds
  available, because the slide stays on screen and only the narration goes.
- **Mark what must never be cut** — usually the answers the talk exists to deliver, and the one
  concession that earns the room's trust.

If the arithmetic will not close, the honest answer is to cut a whole act, not to shave sentences.
Say out loud that you are skipping it and where the answer lives; an unanswered question on the
conclusions slide then works as an invitation rather than a gap.

### Q&A preparation, ranked

Write the answers out, ordered by how likely the question is. The first entry should be the
objection you would raise yourself. Ground each answer in the paper, and include the **honest
converse** — the conditions under which your result would not hold. An answer that concedes its own
limits is far stronger than one that does not, and it is the one that survives a hostile follow-up.

Anything that is genuinely interesting but costs more than about fifteen seconds on the slide
belongs here instead.

### Register

- Rehearse in the register you will deliver in. *Measure*, *infer*, *obtain* — not *get*. Under
  pressure you fall back on rehearsed habits, so build the right ones.
- **Ground analogies in the papers rather than inventing them.** An invented analogy reads as
  cute at a conference and invites a correction; one already in the literature carries authority
  and usually says it better. Prefer a parallel the room already owns — *"two auto-spectra never
  tell you the cross-spectrum"* lands instantly where a general-audience metaphor does not.
- **Do not let a slide diagnose a result before the experiment that tests it.** Report the
  observation, note the asymmetry, then say what you are going to do about it. Asserting the cause
  early costs you the payoff two slides later and overclaims.
- **Scan the finished prose for AI tells** — banned diction, tricolons, hollow closers,
  negation-then-reversal, em-dash overuse. Mechanically, not by feel; see the `deslop` skill.
- Lead with the frame, then point at the figure. If the figure is already on screen showing the
  thing, name what is on it rather than constructing the concept in the abstract first.

---

## 12. Sources

- Peyton Jones, Hughes & Launchbury, *How to give a good research talk*, SIGPLAN Notices 28(11),
  1993 — <https://simon.peytonjones.org/great-research-talk/>. The technology is obsolete
  (overhead projectors); the content advice is the best there is. Source of the Awful Trap,
  non-uniform depth, no-contents-slide, tell-it-how-it-is, and the warning on recycled decks.
- Michael Ernst, *How to give a technical presentation* —
  <https://homes.cs.washington.edu/~mernst/advice/giving-talk.html>. Source of the three
  persuasions, title discipline, pixel-identical builds, and end-on-conclusions.
- Michael Alley, the **assertion–evidence** structure — <https://www.assertion-evidence.com/>,
  and *How the Design of Presentation Slides Affects Audience Comprehension* (the p < .01
  comparison against topic-phrase-plus-bullets).
- Chat Hull, *How to give a great talk*, arXiv:1712.08088 — astronomy-specific. Source of the
  practice protocol, the timing philosophy, the rule of thirds, "pixels are finite; slides are
  infinite", and the figure and colourblindness rules.
- Karen Fleming, *Effective Oral Presentation Guidelines* ("the Fleming Slide Rules"), Savvy
  Science Seminars, Johns Hopkins — `references/fleming-slide-rules.pdf` (in this repo). Written for a
  biophysics lab and almost entirely transferable. Source of the question-slide device, the
  "what I want you to know is ___" test, the strict no-words rule and its
  obligation-to-read argument, the per-format slide compositions, the grayscale test, no-tables,
  and most of the delivery and Q&A discipline.
- Jean-luc Doumont, *Trees, Maps, and Theorems* — adapt to your audience, maximise
  signal-to-noise, use effective redundancy.
- Richard Mayer, principles of multimedia learning — the evidence base for the redundancy,
  signalling, segmenting and coherence rules.
- Randy Olson, *Houston, We Have a Narrative* — the ABT framework.
- EMBL, *15 tips for giving a good scientific talk* —
  <https://www.embl.org/about/info/course-and-conference-office/2018/12/15-tips-for-giving-a-good-scientific-talk/>.
- Wong, *Points of view: Color blindness*, Nat. Methods 8, 441 (2011) — the palette these decks use.
