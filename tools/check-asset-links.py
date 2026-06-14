#!/usr/bin/env python3
"""Check that every local resource referenced by a talk deck actually resolves.

Simulates how a browser would resolve references when the repo is served from
its root (document at /<TalkDir>/<file>.html):

  - relative refs (`assets/x.png`, `../assets/x.png`, `reveal.js/dist/...`)
    resolve against the HTML file's own directory;
  - absolute refs (`/assets/x.png`) resolve against the repo root (the site root);
  - external (http/https/protocol-relative/data/mailto/tel/js) and pure
    anchors (`#/3`) are skipped.

Run from the repo root:

    python3 tools/check-asset-links.py            # summary + unresolved list
    python3 tools/check-asset-links.py --quiet    # summary only

Exit code is the number of unresolved references (capped at 1), so it doubles
as a CI gate. The stable, sorted `MISSING ...` output is meant to be diffed
before/after a change.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parent.parent

# src=/href=/data-*=/poster=  "value"  (single or double quoted)  +  url(value)
ATTR_RE = re.compile(
    r"""(?:src|href|poster|data-src|data-background
        |data-background-image|data-background-video|data-background-iframe)
        \s*=\s*(["'])(.*?)\1""",
    re.IGNORECASE | re.VERBOSE,
)
URL_RE = re.compile(r"""url\(\s*(['"]?)(.*?)\1\s*\)""", re.IGNORECASE)

SKIP_PREFIXES = ("http://", "https://", "//", "data:", "mailto:", "tel:", "javascript:", "#")


def iter_html() -> list[Path]:
    out = []
    for p in REPO.rglob("*.html"):
        parts = set(p.parts)
        if "reveal.js" in parts or "node_modules" in parts:
            continue
        out.append(p)
    return sorted(out)


def refs_in(html: Path) -> list[str]:
    text = html.read_text(errors="ignore")
    found = [m.group(2) for m in ATTR_RE.finditer(text)]
    found += [m.group(2) for m in URL_RE.finditer(text)]
    return found


def resolve(html: Path, ref: str) -> Path | None:
    """Return the filesystem path a browser (served from repo root) would hit,
    or None if the ref is external/anchor and should be skipped."""
    ref = ref.strip()
    if not ref or ref.lower().startswith(SKIP_PREFIXES):
        return None
    ref = ref.split("#", 1)[0].split("?", 1)[0]
    if not ref:
        return None
    ref = unquote(ref)
    if ref.startswith("/"):
        return (REPO / ref.lstrip("/")).resolve()
    return (html.parent / ref).resolve()


def main() -> int:
    quiet = "--quiet" in sys.argv
    missing: list[tuple[str, str]] = []
    checked = 0
    for html in iter_html():
        for ref in refs_in(html):
            target = resolve(html, ref)
            if target is None:
                continue
            checked += 1
            if not target.exists():
                missing.append((str(html.relative_to(REPO)), ref))

    missing.sort()
    if not quiet:
        for html_rel, ref in missing:
            print(f"MISSING  {html_rel}  ->  {ref}")
        print("-" * 60)
    print(f"decks scanned: {len(iter_html())}   refs checked: {checked}   "
          f"unresolved: {len(missing)}")
    return 0 if not missing else 1


if __name__ == "__main__":
    sys.exit(main())
