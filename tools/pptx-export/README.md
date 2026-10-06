# pptx-export: a reveal deck as an editable PowerPoint

Converts a deck into a `.pptx` of native objects: text boxes with the deck's fonts, colours and
weights; figures as the original image files (full resolution, cropped as on the slide); cards,
rules and arrows as shapes. What PowerPoint cannot draw goes in as a transparent picture: canvas,
inline SVG, display math (LaTeX in the alt text), rotated text, gradients. First used for
`PhD_Defense_2026` (2026-09-24, output in `PhD_Defense_2026/pptx_export/`).

## Run

Python deps (a venv is fine): `playwright python-pptx pillow numpy lxml`. Uses the system Chrome
(`channel='chrome'`), so no Playwright browser download is needed.

```bash
python3 -m http.server 8765                          # at the repo root, in another shell
cd tools/pptx-export
python make_states.py  <Deck> states.json            # which build states become slides
python harvest.py      <Deck> states.json work/      # walk each state: items + snapshots
python build.py        work/ <Deck>.pptx             # native objects
./keynote_render.sh    $PWD/<Deck>.pptx $PWD/kn/     # verify: Keynote re-renders every slide
python compare.py      work/ kn/ cmp                 # cmp_N.png: browser | Keynote, 3 slides per sheet
```

Read the `cmp_*.png` sheets. That comparison is the test. `states_PhD_Defense_2026.json` is the
hand-checked state list used for the defense deck.

## Before the supervisor, or anyone, opens it

The deck needs **Source Serif 4** (all optical-size cuts: Caption, SmText, Text, Subhead, Display),
**IBM Plex Sans** and **IBM Plex Mono** installed. Ship a `Fonts.zip` with the file. Keynote only
sees newly installed fonts after a relaunch.

## Known limits

- Keynote sets Source Serif about 4.5 % narrower than Chrome at the same size: titles end slightly
  early. This is Keynote's layout (it shows in its PDF export too). Nothing wraps worse for it.
- Inline math is converted from KaTeX's MathML to runs in Times New Roman. Fractions and roots inside
  a sentence become linear text. A block that is *only* structured math goes in as a picture.
- Animated GIFs stay GIFs, so they animate in slideshow. The Keynote export shows their first frame.
- Videos are embedded. The poster is the frame on the slide, or `work/posters/<name>.png` (e.g. from
  `qlmanage -t`) when Chrome cannot decode the file.

## Traps met while building it

See the memory note, or the comments in `extract.js` / `prepare.js`. The ones that matter if you change the code:

- Isolating an element for a snapshot has to use inline `!important` visibility and switch off
  transitions: reveal fragments transition `visibility`, and some deck rules force it with `!important`.
- Snapshots already include ancestor opacity, so no alpha goes on top of them in the pptx.
- Canvas content is read with `toDataURL` at extraction time. Isolating a canvas restarts its animation.
- Never write `b="0"`. Weights are chosen by legacy family names ("Source Serif 4 Subhead Semibold",
  "IBM Plex Sans SmBld"), and an explicit non-bold flag can override them.
- `keynote_render.sh` opens a uniquely named copy: `front document` can be a restored older window.
