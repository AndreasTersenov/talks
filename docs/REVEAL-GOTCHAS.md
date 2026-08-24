# reveal.js gotchas

Traps in this deck stack that cost real debugging time, with the fix and how to verify it.
Written from the COSMO-26 build (2026-08). Read before doing surgery on builds, overlays, or
anything that must survive PDF export.

---

## 1. Fragment ordering: never mix indexed and unindexed fragments on one slide

**The trap.** reveal does *not* order fragments by DOM position when indices are present. It buckets
every fragment carrying `data-fragment-index` by that number, then appends **all unindexed
fragments after those buckets**. So an unindexed `fragment` wrapper containing indexed children is
ordered *after its own contents*.

**What it looks like.** Several clicks that appear to do nothing (they are advancing through
build-up frames inside a still-hidden container), then the container arrives with every frame
already switched on — the figure appears complete in one step instead of building.

**The fix.** On any slide with fragments, either **all** of them carry an explicit
`data-fragment-index`, or **none** do. Never both.

**Verify** — this scan should print zero:

```bash
python3 - <<'EOF'
import re
s = open('cosmo26/index.html').read()
body = s[s.index('<div class="slides">'):]
for i, sec in enumerate(re.split(r'\n\t\t\t<section', body)[1:]):
    tags = re.findall(r'<[a-z0-9]+[^>]*\bclass="[^"]*\bfragment\b[^"]*"[^>]*>', sec)
    if not tags: continue
    idx = [int(m.group(1)) if (m := re.search(r'data-fragment-index="(\d+)"', t)) else None
           for t in tags]
    if any(v is not None for v in idx) and any(v is None for v in idx):
        print('MIXED on slide', i + 1, idx)
EOF
```

**Corollary.** To make several elements appear *together*, give them the **same** explicit index.
Leaving them all unindexed does the opposite — they get sequential ordinals and arrive one at a time.

---

## 2. Elements that appear and then disappear: `fade-in-then-out`

`fade-out` starts visible; `fade-in` stays visible. For something that should show *only* during its
own step (two alternative scenarios where the second replaces the first), use
`class="fragment fade-in-then-out"`.

It keys off reveal's `current-fragment` class, not `visible` — a different code path from every
other fragment, so verify it explicitly, including in PDF (§5).

---

## 3. reveal caps every slide image at 95%

**The trap.** reveal's own stylesheet sets `max-width: 95%; max-height: 95%` on slide images. If you
position an overlay in per-cent of a wrapper and the image inside renders at 95% of that wrapper,
the overlay is measured against a box that is not the image, and it lands wrong by ~5% — plus
whatever the auto-sizing adds.

**The fix**, when an overlay must align to an image:

```css
.wrapper {                         /* pin it; do not let layout size it */
  position: relative; display: block;
  width: 316px; aspect-ratio: <W> / <H>;   /* the asset's own ratio */
}
.wrapper img {
  display: block; width: 100%; height: 100%; margin: 0;
  max-width: none; max-height: none;       /* lift reveal's cap */
}
.wrapper .overlay {
  position: absolute; left: …%; top: …%; width: …%; height: …%;
  box-sizing: border-box;          /* or side padding is added to the width */
}
```

Both `max-*: none` and `box-sizing: border-box` are required. Missing either produces an overlay
that is subtly, confusingly wrong.

**Measure the per-cents off the asset**, do not guess: find the panel's pixel box with PIL and divide
by the image dimensions.

---

## 4. Getting geometry ground truth

Eyeballing a screenshot is how you waste an hour. Two reliable methods:

- **Colour probe.** Temporarily set the element's background to `#ff00ff`, screenshot, and find the
  bounding box of magenta pixels with PIL. Exact, and it works for anything that paints.
- **DOM probe.** Add a temporary `<script>` that runs after `Reveal.on('ready')`, writes
  `getBoundingClientRect()` and `getComputedStyle()` values into a `data-` attribute, then read it
  with `chrome --headless --dump-dom | grep -o 'data-probe="[^"]*"'`. This is what distinguishes
  "my CSS is not applying" from "my CSS is applying to a box that is not what I think it is".

Note `getComputedStyle().width` is the **content** box while `getBoundingClientRect().width` is the
**border** box — a discrepancy between them is a `box-sizing` bug.

---

## 5. Verify builds in the PDF too, not just the browser

`?print-pdf` renders one page per fragment state. Confirm the classes rather than trusting it:

```bash
chrome --headless=new --disable-gpu --virtual-time-budget=12000 \
  --dump-dom "http://127.0.0.1:8000/<TalkDir>/?print-pdf" > /tmp/pdfdom.html
```

then grep for the element and check which pages carry `visible` and `current-fragment`. This is the
only cheap way to know a `fade-in-then-out` exports correctly.

---

## 6. Canvas explainers do not paint under headless Chrome

The interactive components draw inside `requestAnimationFrame`, which `--virtual-time-budget`
starves. The `<canvas>` comes out blank while everything around it renders normally. Raising the
budget does not help.

Consequences: a blank canvas in a headless screenshot is **not** evidence of a bug; and a PDF
exported this way has empty panels on those slides. For a usable PDF of an animated deck, print from
a real browser.

---

## 7. Exporting a PDF

```bash
chrome --headless=new --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=90000 --print-to-pdf=out.pdf \
  "http://127.0.0.1:8000/<TalkDir>/?print-pdf"
```

Raw output is large (36 MB for this deck). Ghostscript at 150 dpi gets it to ~9 MB with text still
vector and plots legible:

```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH -dDetectDuplicateImages=true \
   -sOutputFile=small.pdf out.pdf
```

To cut the backup slides, find the divider page with `pdftotext -f N -l N`, then
`pdfseparate` + `pdfunite`.

---

## 8. Editing `index.html` safely

Scripted edits to a 1000-line deck have destroyed it once. Rules that have held since:

- **Always absolute paths** in edit scripts. The working directory does not persist between
  `Bash` calls, and a relative path has silently targeted the repo-root landing page instead of the
  deck more than once.
- **Assert before writing.** `assert s.count(old) == 1` on every replacement, and write the file
  only after all replacements have matched. A failed assert then leaves the file untouched rather
  than half-edited.
- Whitespace in the file drifts (hand edits, editor reformatting), so a replacement string copied
  from an earlier read may no longer match. Re-read the region before a scripted edit rather than
  trusting a transcript.

---

## 9. Build-up frames are usually cumulative

Before staging an `r-stack`, check whether frame *N* already contains frames 1…*N*−1. In this repo
they generally do. If so, showing the final state is one `<img>` rather than a stack, and dropping
the build costs nothing. Check by counting colour populations per frame with PIL rather than
assuming.
