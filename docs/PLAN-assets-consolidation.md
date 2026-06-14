# Plan — consolidate per-talk `assets/` into one shared folder

**Date:** 2026-06-14
**Branch:** `reorg/shared-assets` (do not work on `main`)
**Status:** awaiting sign-off

## Goal

Replace the 13 near-duplicate per-talk `assets/` folders with a single shared
`assets/` at the repo root, referenced from each deck via a relative `../assets/`
path. Keep every deck rendering correctly both locally and on GitHub Pages.

## Why this shape (and not something tidier)

To have **one committed copy** of each asset *and* have GitHub Pages serve it,
the deck HTML must reach up to the repo root with a relative path. The
alternatives are dead ends:

- A real per-talk `assets/` folder → that's the duplication we're removing.
- A per-talk `assets` **symlink** → works locally, but **GitHub Pages does not
  publish symlinks** (this is almost certainly the original bug that pushed you
  to copy folders into every talk).
- An **absolute** `/assets/…` or `/talks/assets/…` path → resolves on Pages but
  not under a local static server rooted at the repo.

A relative `../assets/…` reference is the only form that is simultaneously
deduplicated-in-git and correct in both environments.

## Findings (measured, 2026-06-14)

- 1009 asset files across talks; **198 unique by content** → ~80% redundancy.
- Deduplicated set ≈ **284 MB**, vs ~1.2 GB of per-talk copies → working tree
  shrinks ~0.95 GB. (Git *history* keeps the old blobs — see Non-goals.)
- All in-deck references are clean relative paths (`src="assets/…"`); zero
  `../`, and only **one** absolute path (the broken `porqueres_hbm.png`).
- Reference syntaxes to rewrite (delimiter-anchored): `="assets/` (934),
  `'assets/` (98), `('assets/` (7).
- **One basename collision**, `logo-FORTH-IoA.png` (two versions) — but it is
  **referenced by no deck**, so it's harmless. Keep the newer version
  (`e5b86f4e…`, used by the 5 recent talks).
- **Old snapshot to preserve (not delete):** `ENS_seminar_2026/assets/index.html`
  and `LAM_2026/assets/index.html` are **byte-identical** copies of an earlier
  ENS-deck snapshot (the LAM one is even titled "ENS scattering club" — it rode
  along when the LAM folder was copied from ENS). Referenced by nothing.
  Decision: move one copy to `ENS_seminar_2026/index_snapshot_v1.html`; drop the
  identical LAM duplicate.
- **Pre-existing broken refs (baseline = 60), not caused by this change:**
  - `AstroML_JC_Mar24/index.html` → `/talks/assets/porqueres_hbm.png` (file
    absent from repo).
  - `CCA_Predoc_2025` → `assets/lognormal_comparision.png` (1, absent).
  - `PhD_Day_2025/index_Vilasini.html` → 57 absent assets (guest deck).
  - `UNIONS_Paris_2024` → `assets/KiDS_DES_weird_constraints.png` (1, absent).

## Target layout

```
talks/
  assets/                 # the ONE shared folder (union of unique assets)
  .nojekyll               # new: disable Jekyll, never skip files on Pages
  package.json            # new: root dev server (npm start → live-server)
  tools/check-asset-links.py   # new: the verifier (back pressure)
  LAM_2026/
    index.html            # refs rewritten assets/… → ../assets/…
    background.html       # same
    index_eval_committee.html
    reveal.js/  gulpfile.js  package.json   # untouched this round
  …(other talks, no assets/ folder)…
```

## Local preview after the change

`npm start` from inside a talk dir no longer works (it would root the server
inside the talk, so `../assets/` escapes the root). Instead:

- **Default:** add a root `package.json` with
  `"start": "live-server --port=8000"` (live-server as a devDep). Run `npm
  install` once at the root, then `npm start`, open
  `http://localhost:8000/<TalkDir>/`. Live-reload preserved; one command for
  every talk.
- **Zero-dep fallback:** `python3 -m http.server 8000` at the repo root, open
  the same URL (manual refresh).

## Execution steps

0. **Branch + baseline.** `git switch -c reorg/shared-assets`. Run the verifier
   to record the baseline broken set (expect 60). Commit the verifier first so
   it's available for before/after.
1. **Rescue the snapshot.** Move `ENS_seminar_2026/assets/index.html` →
   `ENS_seminar_2026/index_snapshot_v1.html`; remove the byte-identical
   `LAM_2026/assets/index.html`. Confirm no references first.
2. **Build the shared folder.** Union all per-talk `assets/` into root `assets/`
   by basename, newest-wins on the lone `logo-FORTH-IoA.png` collision, skipping
   `.DS_Store`. Preserve `PhD_Day_2025/assets/science-lss.MP4` (note: uppercase
   `.MP4` — keep the reference's case exact for case-sensitive Pages). Reconcile
   against the 49 pre-existing root `assets/` files; **diff-report** any basename
   where the root copy differs from the talk copies before overwriting.
3. **Rewrite references** in every non-reveal deck HTML
   (`index.html`, `background.html`, `index_eval_committee.html`,
   `index_Vilasini.html`): delimiter-anchored replace
   `"assets/`→`"../assets/`, `'assets/`→`'../assets/`, `(assets/`→`(../assets/`.
   This leaves `examples/assets/` (reveal demo leftovers) and the absolute
   `/talks/assets/` path untouched by design.
4. **Fix the one absolute path** for consistency:
   `/talks/assets/porqueres_hbm.png` → `../assets/porqueres_hbm.png` in
   `AstroML_JC_Mar24/index.html`. (Image is still missing — flagged, not
   invented.)
5. **Delete per-talk `assets/`** folders with `git rm -r`.
6. **Add infra:** root `.nojekyll`, root `package.json` (live-server),
   `tools/check-asset-links.py`.
7. **Update docs:** `README.md` and `CLAUDE.md` — new shared-assets layout and
   the root-serve / python-fallback workflow.

## Verification (back pressure)

- **`tools/check-asset-links.py`** simulates "served from repo root, document at
  `/<talk>/<file>`," resolves every `src`/`href`/`url(…)`/`data-background*`
  reference, and reports unresolved ones. Success criterion: the post-migration
  unresolved set is a **subset of the baseline 60** — i.e. every ref that
  resolved before still resolves. No new breakage allowed.
- **Visual spot-check:** serve from root and load 3 decks across eras
  (`TITAN_Saclay_2024`, `PhD_Day_2025`, `LAM_2026`); confirm title-slide
  particle background + logos + figures render.
- **Size check:** `du -sh assets` ≈ 284 MB; working tree ~0.95 GB smaller.

## Rollback

Everything is on a branch and under git. Abort at any point with
`git restore` / `git reset --hard`, or just don't merge the branch.

## Non-goals (explicitly out of scope this round)

- **Git history rewrite.** Deleting duplicates shrinks the working tree, not
  `.git`. Reclaiming clone size needs `git filter-repo`/BFG + force-push, which
  rewrites every commit SHA and breaks existing clones/links. Not worth it for a
  public talks repo; revisit only if clone size becomes a real pain.
- **De-duplicating build tooling.** Once serving from root, the per-talk
  `gulpfile.js`/`package.json` become vestigial (decks load the prebuilt
  `reveal.js/dist/…`, no build needed to view). Removing them — and possibly
  collapsing 13 reveal.js submodules into one shared copy — is the natural next
  step, but it's a separate change.
- **Repo-root clutter** (`logo-FORTH-IoA.png`, `logo-FORTH-IoA 2.png`,
  `white_test/`, etc.) — note for later, not touched here.
- **The 60 pre-existing broken refs** — surfaced, not fixed (their image files
  are simply absent; fixing means finding/recreating them, a separate task).

## Decisions (signed off 2026-06-14)

- **Snapshot files:** preserve one as `ENS_seminar_2026/index_snapshot_v1.html`,
  drop the identical LAM duplicate.
- **`PhD_Day_2025/index_Vilasini.html`:** **path-only rewrite** like every other
  deck. It has 70 asset refs — 13 currently resolve, 57 already broken; the
  rewrite changes zero slide content and keeps the 13 working images loading.
- **Branch:** `reorg/shared-assets`, not `main`.
- **Working-tree sequencing:** commit the pending work as a clean checkpoint
  first, then do the reorg as separate commits.

## Working-tree handling (pre-reorg checkpoint)

The tree is dirty. Checkpoint these, then reorg on top:

- **Stage & commit (user's pending work):** edited decks (`COLOURS_Saclay_2025`,
  `JournalClub_Montreal_2026`, `LAM_2026` `index.html`), new images
  (`CCA_Predoc_2025/assets/dark_matter_art.jpeg`,
  `COLOURS_Saclay_2025/assets/QR_mass_mapping_impact.png`), the new
  `ENS_seminar_2026/index_eval_committee.html`, and the new
  `CosmoStat_group_meeting_2025/` talk (handle its reveal.js/node_modules
  correctly — inspect before committing). CosmoStat + the ENS variant are
  **included** in the consolidation.
- **Commit separately (session artifacts):** `CLAUDE.md`, `docs/`,
  `tools/check-asset-links.py`.
- **Do NOT touch:** `.DS_Store` churn (suggest gitignoring later) and the two
  submodule-pointer wobbles (`TITAN_Eval_2024/reveal.js`, `test/reveal.js`).
