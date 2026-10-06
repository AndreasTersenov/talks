"""Choose which build states of a deck become slides, and write them as a JSON list for harvest.py.

usage: make_states.py DECK OUT.json [--all-steps h.v ...] [--add h.v.f ...]

Rule: every slide contributes its final state, plus any intermediate state whose content is gone in
the next one (a fade-out, a swap, an element covered or hidden), plus every state of a slide with a
<canvas>, since those are JS animations whose steps redraw. Covers drawn over earlier content are not
detected by the DOM, so check the comparison sheets and add such states by hand with --add
(h.v.f, f = -1 for the empty state). --all-steps keeps every build step of a slide.
The repo root must be served on PORT (default 8765).
"""
import json
import os
import sys

from playwright.sync_api import sync_playwright

DECK, OUT = sys.argv[1], sys.argv[2]
rest = sys.argv[3:]
all_steps, extra = set(), []
mode = None
for a in rest:
    if a in ('--all-steps', '--add'):
        mode = a
    elif mode == '--all-steps':
        all_steps.add(a)
    elif mode == '--add':
        extra.append(a)
PORT = os.environ.get('PORT', '8765')

VISIBLE = """(sec) => [...sec.querySelectorAll('.fragment, img, video, svg, canvas, figure, p, li, .block, .callout')].map(e => {
  const r = e.getBoundingClientRect(); if (r.width < 2 || r.height < 2) return 0;
  for (let x = e; x && x !== sec.parentElement; x = x.parentElement) {
    const s = getComputedStyle(x);
    if (parseFloat(s.opacity) < 0.6 || s.visibility === 'hidden' || s.display === 'none') return 0;
  }
  return 1; })"""

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 720})
    page.goto(f'http://127.0.0.1:{PORT}/{DECK}/')
    page.wait_for_function('window.Reveal && Reveal.isReady()')
    page.evaluate("Reveal.configure({transition:'none', backgroundTransition:'none'})")
    page.wait_for_timeout(2000)
    slides = page.evaluate("""Reveal.getSlides().map(s => { const i = Reveal.getIndices(s);
        return [i.h, i.v || 0, s.querySelectorAll('canvas').length]; })""")
    states = []
    for h, v, ncanvas in slides:
        page.evaluate(f'Reveal.slide({h},{v},-1)')
        page.wait_for_timeout(300)
        nsteps = page.evaluate("""new Set([...Reveal.getCurrentSlide().querySelectorAll('.fragment')]
            .map(f => f.getAttribute('data-fragment-index'))).size""")
        seen = []
        for f in range(-1, nsteps):
            page.evaluate(f'Reveal.slide({h},{v},{f})')
            page.wait_for_timeout(700)
            seen.append((f, page.evaluate(VISIBLE, page.evaluate_handle('Reveal.getCurrentSlide()'))))
        for k, (f, vis) in enumerate(seen):
            last = k == len(seen) - 1
            lost = not last and any(a and not b for a, b in zip(vis, seen[k + 1][1]))
            if last or lost or ncanvas or f'{h}.{v}' in all_steps or f'{h}.{v}.{f}' in extra:
                states.append({'h': h, 'v': v, 'f': f, 'canvas': ncanvas})
        print(f'{h}.{v}', [s['f'] for s in states if s['h'] == h and s['v'] == v], flush=True)
    browser.close()

json.dump(states, open(OUT, 'w'), indent=0)
print(len(states), 'states ->', OUT)
