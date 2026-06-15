# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A collection of public talks (cosmology / weak lensing / SBI), each one a
standalone [reveal.js](https://revealjs.com) HTML slide deck in its own
top-level directory (e.g. `LAM_2026/`, `ENS_seminar_2026/`, `TITAN_Saclay_2025/`).
All decks share a **single `assets/` folder at the repo root** and reference it
with a relative `../assets/…` path. Each talk is published to GitHub Pages at
`https://andreastersenov.github.io/talks/<TalkDir>/`.

## Working on a talk (local preview)

The dev server is served from the **repo root** (not from inside a talk dir —
that would root the server below `assets/` and break the `../assets/` paths).

```bash
npm install                 # first time only, at the repo root (installs live-server)
npm start                   # live-server on http://localhost:8000 with live-reload
# then open http://localhost:8000/<TalkDir>/   e.g. /LAM_2026/
```

Zero-dependency fallback (no live-reload, manual refresh):

```bash
python3 -m http.server 8000   # at the repo root, then open /<TalkDir>/
```

**PDF export**: open `http://localhost:8000/<TalkDir>/?print-pdf` and use the
browser's print-to-PDF.

After cloning, hydrate the reveal.js submodules: `git submodule update --init --recursive`.

## Asset references — the load-bearing convention

Shared assets live in the root `assets/`, split into type subfolders —
`logos/`, `backgrounds/`, `diagrams/`, `figures/`, `photos/`, `videos/`,
`misc/` — and `figures/` is split further into `maps/`, `posteriors/`,
`statistics/`, `matrices/`. Decks reference them with a **relative parent path
including the subfolder(s)**:

```html
<img src="../assets/figures/maps/kappa.png">  <!-- NOT "assets/…", NOT "/assets/…" -->
```

This resolves correctly both locally (served from root → `/assets/…`) and on
GitHub Pages (`/talks/assets/…`). Do **not** reintroduce a per-talk `assets/`
folder, an absolute `/assets/…` path, or a symlink — **GitHub Pages does not
publish symlinks**, which is the bug that originally forced per-talk copies.
New images go into the matching `assets/<category>/` subfolder; `docs/asset-map.tsv`
records the current filename→category assignment.

Verify after editing refs:

```bash
python3 tools/check-asset-links.py    # resolves every deck's local refs; lists any missing
```

## Per-talk anatomy

Each talk directory holds:

- `index.html` — the deck. Slides are **hand-written HTML**; each top-level
  `<section>` is a slide, nested `<section>`s are vertical sub-slides.
- `reveal.js/` — a **git submodule** pinned to the `EiffL/reveal.js` fork (see
  `.gitmodules`), carrying the custom `darkenergy`/`brightenergy` themes and
  extra plugins (math, d3, chart).
- `background.html` + `particles.*` — animated particles.js title background,
  loaded via `data-background-iframe="background.html"`.
- `gulpfile.js` + `package.json` — **vestigial.** Left over from when each talk
  was served on its own; decks load the prebuilt `reveal.js/dist/…`, so nothing
  needs building to view, and serving is now done from the repo root. Don't rely
  on the per-talk `npm start`.
- Sometimes variant decks (`index_eval_committee.html`) or an archived snapshot
  (`index_snapshot_v1.html`), and a reference `main.tex` of the related paper.

## Deck-editing conventions

- Custom theme `darkenergy` (`reveal.js/dist/theme/darkenergy.css`, built from
  `reveal.js/css/theme/source/darkenergy.scss`).
- Layout grid classes: `container` wrapping `col`; `plain` for borderless images.
- `alert` = theme accent color on inline text; `fragment` (e.g. `fragment
  fade-in`) for incremental reveals.
- `data-visibility="hidden"` on a `<section>` parks a draft slide (kept in the
  file, skipped in the deck).
- Math / Markdown / Highlight plugins are enabled in the `Reveal.initialize`
  block, so `$…$` math and ```` ```lang ```` code fences work in slides.

## The "Preprint" theme (new — opt-in, for new talks)

A refreshed light+dark theme lives in **`assets/themes/talks.css`** (+
`assets/themes/theme-switch.js`), loaded as an overlay *after* the submodule's
`darkenergy.css`. It's a paper/preprint aesthetic: cobalt accent (`#7d92ff` dark
/ `#2f49c0` light), **Source Serif 4** headings, **IBM Plex Sans** body, **IBM
Plex Mono** labels, ruled `.block` callouts, hairlines. It is **opt-in** — only
decks that link it use it; existing decks keep `darkenergy`. **`PREPRINT_TEMPLATE/`
is the reference deck** (a migrated copy of `LAM_2026`, dark + light, exercising
every component — and representative of the real slide/plot types).

Wire it into a deck — in `<head>`, AFTER the darkenergy `<link>`:

```html
<link rel="stylesheet" href="../assets/themes/talks.css">
```

and at body end, **BEFORE** the `reveal.js/dist/reveal.js` script (it must run
before `Reveal.initialize`):

```html
<script src="../assets/themes/theme-switch.js"></script>
```

**Per-slide light/dark (authoring-time, PDF-safe).** Tag a section to match
whether its figure was made for a light or dark background:

```html
<section data-theme="light"> … </section>   <!-- cobalt on warm paper -->
<section> … </section>                        <!-- dark is the default -->
```

It's scoped per `<section>`, not a global toggle, so each slide self-themes and
PDF export stays correct. `class="light-slide"` is a legacy alias.

**Component classes** (token-driven, both modes): `slide-title` (serif title +
cobalt rule; optional `<span class="sec">§2</span>`), `block` + `block-title` +
`block-content` (ruled callout with a small-caps mono tab), `kicker` (mono
eyebrow), `callout` / `takeaway` (left-rule box with a `label`), `stat` (`num` +
`label` result rule), `runhead` (journal running head; `.r` = right side),
`alert` (accent text), `title-card` (title lockup). `container`/`col` still work.

**Do not inline-style colours.** A stylesheet can't override `style="color:#…"`,
so hardcoded hex in a `style=""` attribute is invisible to the theme. Use the
classes/tokens (`var(--accent)`, `var(--surface)`, `var(--fg-muted)`, …), not hex.

## Creating a new talk

Recent practice commits new talks straight to `main` (the README's older
branch-per-talk flow is no longer followed — see git history). To scaffold:

1. Copy a recent talk to a new `<TalkDir>/`. **For the new Preprint theme, copy
   `PREPRINT_TEMPLATE/`** (you inherit the theme wiring + representative slide
   archetypes); for the classic look copy a `darkenergy` deck (e.g.
   `ENS_seminar_2026/`). **Delete any `assets/` folder it brings along** — assets
   are shared at the root now.
2. Re-point the reveal.js submodule (`git submodule add
   https://github.com/EiffL/reveal.js.git <TalkDir>/reveal.js`, then
   `git submodule update --init --recursive`).
3. Reference figures as `../assets/<category>/…`; drop new images into the
   matching `assets/<category>/` subfolder.
4. Preview from the repo root (`npm start`, open `/<TalkDir>/`) and run
   `python3 tools/check-asset-links.py`.

## Gotchas

- `node_modules/` and `notes/` are gitignored. Run `npm install` **at the repo
  root** (for live-server); per-talk `node_modules` are no longer needed to serve.
- The shared `assets/` is **mutable**: re-cropping/replacing a figure changes
  every deck that uses it. To freeze a talk exactly as delivered, `git tag` it.
- reveal.js submodules are **pinned commits**; use `git submodule update` to sync.
- `.DS_Store` files are committed throughout and routinely show as modified —
  ignore that noise.
- `.nojekyll` at the root disables Jekyll on Pages (so no file is ever skipped);
  don't remove it.
- `template/`, `test/`, `white_test/` are scaffolding, not talks, and have
  pre-existing broken refs — `check-asset-links.py` flags them; ignore.
