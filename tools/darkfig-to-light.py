#!/usr/bin/env python3
"""Rasterise a figure and, if it was made for a dark slide, recolour it for a light one.

Why this exists
---------------
Two problems bite every deck lifted out of `LAM_2026`, `ENS_seminar_2026` or
`PhD_Day_2025` into a `talks.css` deck:

1. **Chrome does not render a PDF inside an `<img>` tag.** Those decks carry ~20
   PDF-as-`<img>` refs each, so they only ever looked right in Safari. cosmo26 and
   the defense deck carry none, which is why the problem stayed invisible.
2. **Their result figures were exported for a dark background** -- transparent
   canvas, *white* axes, labels, frames and legend boxes. On the preprint theme's
   warm paper (`#f7f5f0`) the labels vanish and the legend becomes a black blob.

Rasterising fixes (1). For (2) the recolour is deliberately conservative: invert
the luminance of **near-neutral pixels only**, leaving anything saturated alone.
White ink flips to black; the Wong method coding (KS grey, iKS vermillion,
MCALens blue) and every colormap pass through untouched. Mid-grey is a fixed
point under the transform, which is exactly what KS's grey encoding wants.

**What it must not be pointed at.** Figures containing an `imshow` panel -- convergence
maps, correlation matrices -- have a colormap whose dark end is near-neutral, so the
recolour flips it to white speckle and ruins the field. Those stay dark-slide figures;
the tool detects them by painted area and rasterises only. The contact sheet is still
the real check -- look at it before putting anything on a slide.

This is a recolour, not a re-plot. If the source notebook is to hand, re-exporting
with a light style is still the better answer -- see `docs/TALK-GUIDELINES.md` §5.

Usage
-----
    python3 tools/darkfig-to-light.py assets/figures/posteriors/foo_dark.pdf
    python3 tools/darkfig-to-light.py --sheet /tmp/check.png assets/**/*_dark.pdf
    python3 tools/darkfig-to-light.py --force-invert assets/diagrams/bar.pdf

Naming: `*_dark.pdf` -> `*_light.png`; anything else -> `*.png`, or `*_light.png`
if it needed inverting. Sources are never modified and nothing is overwritten
unless `--overwrite` is passed.
"""
import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter, ImageOps

# A pixel counts as "neutral" (ink or frame rather than data) below this
# max-minus-min spread across RGB. 32/255 keeps anti-aliased grey text in and
# leaves even softly-tinted data out.
SATURATION_CUTOFF = 32
# Above this painted fraction the figure has filled panels -- an imshow map, or a
# plot drawn on a white axes patch over a dark canvas. Recolouring those flips the
# panel to black and speckles any colormap, so the tool refuses. Measured across the
# repo's figures: everything below 0.20 recoloured cleanly, everything above 0.40
# was damaged, and nothing sits in between.
RASTER_PANEL = 0.35
# Erosion reach, in pixels, that separates a glyph stroke from a filled panel at
# the default 2000px raster. Must be odd.
PANEL_REACH = 11
# Below this, an alpha value is treated as fully transparent background.
ALPHA_FLOOR = 8


def is_tracked(path: Path) -> bool:
    """Is this file committed to git? Overwriting one changes every deck using it."""
    try:
        return subprocess.run(["git", "ls-files", "--error-unmatch", str(path)],
                              capture_output=True).returncode == 0
    except OSError:
        return False


def decks_referencing(path: Path) -> str:
    try:
        out = subprocess.run(["grep", "-rl", path.name, "--include=index.html", "."],
                             capture_output=True, text=True).stdout.split()
        return ", ".join(sorted({d.split("/")[1] for d in out if "/" in d}))
    except OSError:
        return ""


def rasterise(pdf: Path, out_png: Path, long_side: int) -> None:
    """PDF -> PNG, keeping the transparent background.

    `-transp` is not optional: without it pdftocairo flattens the transparent
    canvas to white, which produces a white-backed plot for a dark slide.
    """
    with tempfile.TemporaryDirectory() as td:
        stem = Path(td) / "page"
        subprocess.run(
            ["pdftocairo", "-png", "-transp", "-singlefile",
             "-scale-to", str(long_side), str(pdf), str(stem)],
            check=True, capture_output=True,
        )
        shutil.move(str(stem.with_suffix(".png")), out_png)


def classify(im: Image.Image) -> str:
    """Is this figure drawn for a light slide or a dark one?

    Trusting the `_dark` filename suffix is not enough -- some are opaque white
    exports that merely live next to dark ones. Decide from the pixels: an opaque
    canvas is judged by its corners, a transparent one by whether its neutral ink
    is closer to black or to white.
    """
    im = im.convert("RGBA")
    small = im.copy()
    small.thumbnail((360, 360))
    px = small.load()
    w, h = small.size
    corners = [px[1, 1], px[w - 2, 1], px[1, h - 2], px[w - 2, h - 2]]

    if sum(1 for c in corners if c[3] < 40) < 3:
        lum = sum(0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2] for c in corners) / 4
        return "light" if lum > 200 else "dark" if lum < 80 else "unknown"

    dark = light = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a < 200 or max(r, g, b) - min(r, g, b) > SATURATION_CUTOFF:
                continue
            lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
            if lum < 110:
                dark += 1
            elif lum > 200:
                light += 1
    return "light" if dark > light else "dark"


def panel_mask(alpha: Image.Image, reach: int = PANEL_REACH) -> Image.Image:
    """White where a pixel sits *inside* a large opaque region, black elsewhere.

    This is the distinction that matters. These figures draw two different kinds
    of white: axis labels and titles, which are thin glyph strokes on the
    transparent canvas and must be flipped to black; and filled panels -- a white
    axes patch, an imshow map -- which are already correct and must be left alone.

    A min-filter erodes the alpha channel by `reach`: a 3px glyph stroke
    disappears, a 400px panel keeps its interior. Then a max-filter grows the
    survivors back so panel *edges* are protected too, otherwise the recolour
    leaves a black rim around every panel.
    """
    solid = alpha.point(lambda v: 255 if v > 200 else 0)
    eroded = solid.filter(ImageFilter.MinFilter(reach))
    return eroded.filter(ImageFilter.MaxFilter(reach))


def invert_neutrals(im: Image.Image, protect_panels: bool = True) -> Image.Image:
    """Invert near-neutral pixels; leave saturated ones, and optionally filled
    panels, exactly as they are.

    Done with whole-band operations rather than a per-pixel loop -- a 2000px
    figure is four million pixels and the loop version takes tens of seconds.
    """
    im = im.convert("RGBA")
    r, g, b, a = im.split()
    rgb = Image.merge("RGB", (r, g, b))

    hi = ImageChops.lighter(ImageChops.lighter(r, g), b)
    lo = ImageChops.darker(ImageChops.darker(r, g), b)
    saturation = ImageChops.subtract(hi, lo)
    flip = saturation.point(lambda v: 255 if v < SATURATION_CUTOFF else 0)

    if protect_panels:
        keep = panel_mask(a)
        flip = ImageChops.subtract(flip, keep)

    out = Image.composite(ImageOps.invert(rgb), rgb, flip)
    out.putalpha(a)
    return out


def contact_sheet(pairs, dest: Path, tile: int = 460) -> None:
    """Rasterised source on the dark ground, result on the paper, side by side.

    Composited on the real theme colours so the check is the check that matters:
    can you read the axis labels on the slide this is going on?
    """
    DARK, PAPER = (21, 22, 27, 255), (247, 245, 240, 255)
    tiles = []
    for before, after in pairs:
        for path, ground in ((before, DARK), (after, PAPER)):
            im = Image.open(path).convert("RGBA")
            im.thumbnail((tile, tile))
            card = Image.new("RGBA", im.size, ground)
            card.alpha_composite(im)
            tiles.append(card)

    per_row = 4
    rows = [tiles[i:i + per_row] for i in range(0, len(tiles), per_row)]
    width = max(sum(t.width for t in row) for row in rows)
    height = sum(max(t.height for t in row) for row in rows)
    sheet = Image.new("RGB", (width, height), (110, 110, 110))
    y = 0
    for row in rows:
        x = 0
        for t in row:
            sheet.paste(t, (x, y))
            x += t.width
        y += max(t.height for t in row)
    sheet.save(dest)


DARK_SUFFIX = re.compile(r"_dark(\d*)$")


def opaque_fraction(im: Image.Image) -> float:
    """How much of the canvas is painted. Line plots on a transparent canvas run
    0.03-0.17; anything with filled panels runs 0.4-0.8."""
    small = im.convert("RGBA")
    small.thumbnail((500, 500))
    px = small.getchannel("A").load()
    w, h = small.size
    return sum(1 for y in range(h) for x in range(w) if px[x, y] > 200) / (w * h)


def output_path(src: Path, inverted: bool) -> Path:
    """`foo_dark.pdf` -> `foo_light.png` when recoloured, `foo_dark.png` when not.

    A rasterise-only pass keeps the original stem on purpose: the figure is still
    a dark-slide figure, it just needed to stop being a PDF.
    """
    if not inverted:
        return src.with_suffix(".png")
    stem, n = DARK_SUFFIX.subn(lambda m: "_light" + m.group(1), src.stem)
    if not n:
        stem += "_light"
    return src.with_name(stem + ".png")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sources", nargs="+", type=Path, help="PDF or PNG figures")
    ap.add_argument("--long-side", type=int, default=2000,
                    help="target pixels on the long side when rasterising (default 2000)")
    ap.add_argument("--sheet", type=Path,
                    help="write a before/after contact sheet here for the eyeball check")
    ap.add_argument("--force-invert", action="store_true",
                    help="invert regardless of what the classifier decides")
    ap.add_argument("--flat", action="store_true",
                    help="recolour every neutral pixel, including inside filled panels "
                         "-- for pure line art with no axes patch")
    ap.add_argument("--no-invert", action="store_true",
                    help="rasterise only, keeping the original name -- for figures the "
                         "recolour damages (anything with an imshow panel)")
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    pairs, failures, warnings = [], [], []
    print(f"{'source':58s} {'verdict':10s} {'action':9s} output")
    for src in args.sources:
        if not src.exists():
            failures.append(f"{src}: not found")
            continue
        try:
            with tempfile.TemporaryDirectory() as td:
                if src.suffix.lower() == ".pdf":
                    raster = Path(td) / "r.png"
                    rasterise(src, raster, args.long_side)
                else:
                    raster = src

                im = Image.open(raster)
                if args.force_invert:
                    verdict = "forced"
                elif DARK_SUFFIX.search(src.stem):
                    # The `_dark` suffix is this repo's own convention and it is
                    # authoritative. The pixel test below is only for figures that
                    # do not carry it -- it has been fooled twice by figures whose
                    # legend box is a black rectangle, which reads as dark ink.
                    verdict = "dark:name"
                else:
                    verdict = classify(im)
                inverted = args.force_invert or verdict.startswith("dark")
                if args.no_invert:
                    inverted = False
                dest = output_path(src, inverted)

                if dest.exists() and args.overwrite and is_tracked(dest):
                    users = decks_referencing(dest)
                    warnings.append(
                        f"{dest.name}: overwrote a shared asset that is committed to git"
                        + (f" and referenced by {users}" if users else "")
                        + ". `assets/` is mutable -- replacing a figure changes every deck "
                          "that uses it. Prefer a new name.")
                if dest.exists() and not args.overwrite and not args.dry_run:
                    print(f"{str(src)[:58]:58s} {verdict:10s} {'exists':9s} {dest.name}")
                    continue

                action = "invert" if inverted else "rasterise"
                print(f"{str(src)[:58]:58s} {verdict:10s} {action:9s} {dest.name}")
                if args.dry_run:
                    continue

                out = (invert_neutrals(im, protect_panels=not args.flat)
                       if inverted else im.convert("RGBA"))
                out.save(dest)
                if args.sheet:
                    keep = dest.with_name(dest.stem + ".__before.png")
                    Image.open(raster).convert("RGBA").save(keep)
                    pairs.append((keep, dest))
        except subprocess.CalledProcessError as exc:
            failures.append(f"{src}: pdftocairo failed -- {exc.stderr.decode()[:200]}")
        except Exception as exc:  # noqa: BLE001 -- report and keep going
            failures.append(f"{src}: {type(exc).__name__}: {exc}")

    if args.sheet and pairs:
        contact_sheet(pairs, args.sheet)
        print(f"\ncontact sheet -> {args.sheet}")
    for keep, _ in pairs:
        keep.unlink(missing_ok=True)

    for w in warnings:
        print(f"\nCHECK   {w}", file=sys.stderr)
    for f in failures:
        print(f"FAILED  {f}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
