# talks

Repository of public talks. Each top-level directory is a standalone
[reveal.js](https://revealjs.com) deck, published to GitHub Pages at
`https://andreastersenov.github.io/talks/<TalkDir>/`. All decks share **one
`assets/` folder at the repo root**, referenced from each deck as `../assets/…`.

## Previewing locally

Served from the repo root (so the shared `../assets/` paths resolve):

```bash
npm install            # first time only — installs live-server
npm start              # http://localhost:8000 with live-reload
```

Then open `http://localhost:8000/<TalkDir>/` (e.g. `/LAM_2026/`). Export a PDF
from `/<TalkDir>/?print-pdf`.

No-dependency fallback (manual refresh): `python3 -m http.server 8000` at the
repo root.

After cloning: `git submodule update --init --recursive`.

## Creating a new presentation

  - Make a copy of a recent talk directory (it already wires up the current
    reveal.js fork and theme). **Delete the copied `assets/` folder** — assets
    live at the repo root now.
  - Point the reveal.js submodule:

    ```
    $ git submodule add https://github.com/EiffL/reveal.js.git <TalkDir>/reveal.js
    $ cd <TalkDir>/reveal.js && git submodule update --init --recursive
    ```

  - Reference figures as `../assets/<category>/…` (the root `assets/` folder is
    split into `logos/`, `backgrounds/`, `diagrams/`, `figures/`, `photos/`,
    `videos/`, `misc/`); drop new images into the matching subfolder.
  - Preview from the repo root (`npm start`, open `/<TalkDir>/`).

## Checking asset links

```bash
python3 tools/check-asset-links.py
```

Resolves every deck's local references as a browser served from the repo root
would, and lists any that don't exist.
