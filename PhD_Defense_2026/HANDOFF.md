# HANDOFF — PhD defense deck, 2026-09-10 evening

Written at the end of a long session so the next one can pick up without re-deriving anything.
Defense is **14 September 2026**. Everything below is committed and pushed except where noted.

---

## Where it stands

| | |
|---|---|
| main line | **51 frames** (113 in the file; the rest is backup) |
| spoken length | **44:14 at 121 wpm** (was reported as 47:44/126 — both were wrong, see below) |
| the rate to plan at | **121 wpm** — measured, not assumed (see below) |
| `[CLICK]` audit | **4 mismatches**: frames 6, 24, 42, 43 |
| `check-asset-links.py` | clean for this deck |
| type floor | 17 px on the 1200×720 canvas, two-tier |
| last commit | `b875ca7` |

**Uncommitted on purpose:** `SPEAKER_SCRIPT.md` carries Andreas's own in-flight edits (he was
rewording Act 0 and switching "this talk" → "this thesis"). Do not commit it without asking.
`SPEAKER_SCRIPT.html` / `.pdf` are his exports; untracked, leave them.

### The one number that matters

The CosmoStat rehearsal on 2026-09-10 ran the script in **48:00**, reading.

**Corrected 2026-09-11.** That was first read as 6,041 words → 126 wpm, but `measure-script.py`
counted HTML comments as spoken: it dropped only lines *starting* with `<!--`, so multi-line and
mid-line comments leaked. The rehearsed script holds **5,799** real spoken words, so the rate is
**121 wpm**. Both errors were in the same direction and cancelled, which is why nobody noticed —
but they stop cancelling the moment anything is cut, because this script is edited by *parking*
sentences in comments. On 2026-09-11 a trim to A1.7 that saved 0:14 was reported as a 0:36
increase. Fixed in `spoken()` and in the `[CLICK]` audit.

The talk is **44:14** read from the script. Delivered from memory expect **48–53 min** against a
**45-minute slot**, so the gap is **three to eight minutes**, not the ten this file used to claim.

---

## What happened this session

Four sets of rehearsal comments (`defence_prep_comments.txt`) were evaluated in
**`REHEARSAL_FEEDBACK.md`**, then worked through. In commit order from `bdcd70f`:

- **Typography.** 260 of 574 main-line text elements rendered below 17 px; 84 below 13 px. A
  two-tier floor now applies (17 px for anything read, 13 px for credits/sources), across 170 rules
  in five stylesheets. Italics went from **28 % of elements to 1 %** — the theme's `--label-style`
  put every caption and tag in small italic serif, and slide-title accents were `<em>`.
- **Deck.** DES-Y3 pipeline parked (Martin) → main line 52; slide numbers count the main line and go
  silent in backup; UNIONS added to the survey line; frame 39 retitled away from "perfect"; UNIONS
  shape-catalogue citation added; title slide credits enlarged, CEA dropped, slides link restyled;
  generative-model strip extended to a present-day panel with the credit corrected (the paper is
  **Shirvani**, not "Boesel & Marks").
- **Script.** Transitions restored at the Part 1→2 and 2→3 joins; glosses for wavelets and peak
  counts at first use; the miscoverage colorbar explained; A3.13 cut 1:20 → 0:52; a new tier-2 Q&A
  for the Part 3 × Part 4 interaction; three stale `[CLICK]` cues fixed; Group A trims applied.
- **Slides 23+24 merged** into one Plug-and-Play slide, then laid out over five iterations. Final
  form: **no card**, text aligned to the title's text edge, figure centred at 66 % and dropped low.

---

## What is left, in priority order

### 1. The inference runway — frames 34–37 (~3:20)
Classical inference, generative modelling, normalizing flows, SBI. **Three reviewers plus Martin**
named this as the place to save minutes. Not touched because Andreas rewrote those beats to his own
instructions on 2026-09-09. **Ask before cutting.** My view: keep frame 35 (generative modelling —
the one a non-specialist follows) and compress 36 and 37 around it.

### 2. Other structural cuts
- frame **18**, the three maps (~0:45) — frame 17's chain shows them in miniature
- frame **31**, the wavelet excursion (~1:25) — take this one **last**; it is what stops the
  ℓ1-norm sounding arbitrary
- A2.3 already carries a **tier-0 short path** worth −0:20, decided live

### 3. Housekeeping
- The **cut ladder** inside `SPEAKER_SCRIPT.md` is stale — sized at 47:26/120 wpm against 54 frames.
  Ordering still right, landing times fiction.
- `REHEARSAL_FEEDBACK.md`'s *Applied* section stops at the first batch; everything after `ba1ff7e`
  is unrecorded there.
- `TRIM_CANDIDATES.md` still advertises Group B as 1:10, which Andreas has since rejected.

### 4. Blocked on Andreas
| item | needs |
|---|---|
| frame 43, lensing efficiencies (Martin) | re-export `p1_kernels_standard.png` on a transparent ground, white labels, **four** bins. He said he'd do it later. |
| frame 48, SBI (Martin) | Martin flagged it "can be removed or reduced" and doesn't remember why — ask him |
| frame 44, κᵢ×κⱼ product maps | Martin undecided; Andreas said **keep for now** |
| the cat panel's credit | Andreas said **don't worry, no credit needed** |

---

## Rules learned the hard way

**Trust nothing in `TRIM_CANDIDATES.md` without re-checking it.** Group A promised 2:07 and
delivered **0:45** — two of its eight items had been overtaken by rewrites. Group B promised 1:10,
was really 0:15, and was rejected. **Verify every item against the current text before proposing
it.**

**Andreas edits files while you work.** Check `git status` before and after; re-read before editing.
He rewords beats and slides mid-session.

**Show before applying.** Preview script edits as a dry run and slide edits as a screenshot. He
pushed back hard on a batch applied without review, and rejected Group B after seeing it. A
throwaway `_try.html` with an injected `<style>` override renders a variant without touching the
repo.

**Renumbering cascade.** Parking or merging a slide shifts every later frame. Update: beat headings,
act headers, **both** budget tables, Q&A pointers, and `TRIM_CANDIDATES.md`. **Do not** renumber the
`# Decisions and history` section — it is a dated record. Then run `measure-script.py … --write` to
restamp all beat headings.

**Gotchas that cost real time:**
- reveal caps every slide image at `max-width/max-height: 95%` — lift explicitly or your image
  silently refuses to fill its container.
- `position: absolute; bottom: …` does **not** reach the foot of a slide; sections are shrink-to-fit.
- reveal's `.r-stack` leaves images short of their container and off-centre inside it.
- a `slideNumber` function must return an **array**; reveal indexes `value[0..2]`, so a string is
  sliced into characters.
- a `<ul>` inside a `<p>` is auto-closed by the browser, so it does not inherit the paragraph's
  font-size. This is why a list can render larger than everything around it.
- an HTML-commented `[CLICK]` still counts in the cue audit.
- when cropping a figure to its ink, use a threshold that ignores near-white (`min(rgb) < 235`) and
  scan every pixel — a single `rgb(242,241,245)` stray added 260 px of phantom width and made a
  centred figure look shifted.
- **do not recolour figures** (`memory: talks-figure-conversion`) — LAB inversion loses axis labels.

---

## Verification, every time

```bash
cd ~/Software/talks
python3 tools/measure-script.py PhD_Defense_2026 --wpm 126      # timing + cue audit
python3 tools/measure-script.py PhD_Defense_2026 --wpm 126 --write   # restamp headings after edits
python3 tools/check-asset-links.py | grep PhD_Defense_2026      # silence is good
npm start                                                        # serve from the REPO ROOT
```

### Screenshotting a frame

Frame *n* → reveal hash. Sections with `data-visibility="hidden"` are removed from the DOM, so
count only visible ones; a section with nested `<section>`s contributes its visible children.

```python
# hashes.py — prints "#/h[/v]  fNNN" for the frame numbers given as argv
import re, sys
src = open("PhD_Defense_2026/index.html", encoding="utf-8").read().split("\n")
top = [i for i,l in enumerate(src) if re.match(r"^\t\t\t<section\b", l)] + [len(src)]
def tag(i):
    t = src[i]; j = i
    while ">" not in t and j+1 < len(src): j += 1; t += " " + src[j]
    return t.split(">")[0]
h = -1; n = 0; out = {}
for a, b in zip(top, top[1:]):
    if 'data-visibility="hidden"' in tag(a): continue
    h += 1
    kids = [i for i in range(a,b) if re.match(r"^\t\t\t\t<section\b", src[i])]
    vis  = [i for i in kids if 'data-visibility="hidden"' not in tag(i)]
    if not kids: n += 1; out[n] = f"#/{h}"
    else:
        for v,i in enumerate(vis): n += 1; out[n] = f"#/{h}/{v}"
for f in map(int, sys.argv[1:]): print(out[f], f"f{f:03d}")
```

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=1280,800 \
  --virtual-time-budget=8000 --screenshot=/tmp/f023.png \
  "http://127.0.0.1:8000/PhD_Defense_2026/#/22/0"
```

To see a later fragment, copy `index.html` to `_shot.html` with the `fragment` class stripped from
the element you want revealed, shoot that, then delete it.

### Auditing computed type size / overflow

Append this to a copy of `index.html`, load it headless with `--dump-dom`, and parse `#AUDITOUT`.
It reports every main-line text node's **computed** size and style — what the projector shows, not
what the CSS says. (It returns 0 height for vertical sub-slides; screenshot those instead.)

```js
window.addEventListener('load', function () { setTimeout(function () {
  var out = [], slides = Reveal.getSlides();
  var backup = slides.indexOf(document.getElementById('backup-divider'));
  slides.forEach(function (sec, i) {
    if (backup >= 0 && i >= backup) return;
    sec.querySelectorAll('*').forEach(function (el) {
      if (el.closest('aside.notes')) return;
      var own = Array.from(el.childNodes).filter(n => n.nodeType === 3 && n.textContent.trim().length > 1)
                     .map(n => n.textContent.trim()).join(' ');
      if (!own) return;
      var cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden') return;
      out.push([i+1, Math.round(parseFloat(cs.fontSize)*10)/10, cs.fontStyle,
                el.tagName.toLowerCase()+'.'+(el.className||'').toString().split(' ')[0],
                own.replace(/\s+/g,' ').slice(0,60)].join('\t'));
    });
  });
  var pre = document.createElement('pre'); pre.id = 'AUDITOUT';
  pre.textContent = out.join('\n'); document.body.appendChild(pre);
}, 4000); });
```

---

## Files

| file | what it is |
|---|---|
| `index.html` | the deck, 113 frames, 51 on the main line |
| `SPEAKER_SCRIPT.md` | the spoken script; beats, cues, budget tables, cut ladder, Q&A, history |
| `REHEARSAL_FEEDBACK.md` | the 2026-09-10 comments, evaluated, with what was applied |
| `TRIM_CANDIDATES.md` | where the time is — **numbers unreliable, see above** |
| `SCRIPT_PASS.md` | the 2026-09-09 rewrite record |
| `PAPER_FACTS.md` | the number ledger; no number reaches a slide unless it is here |
| `custom.css`, `new_slides.css` | deck-local styling, including the type floor and italic overrides |
