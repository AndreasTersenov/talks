"""Drive the deck through the chosen build states and dump, per state, the walker's items plus
isolated transparent snapshots of everything that has to go in as a picture.

usage: harvest.py DECK STATES.json OUTDIR [h.v.f ...]   (no h.v.f given = every state in the list)

DECK is the talk directory name (e.g. PhD_Defense_2026); the repo root must be served on PORT
(default 8765: `python3 -m http.server 8765` at the repo root).
"""
import json
import os
import sys

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
DECK, STATES, OUT = sys.argv[1:4]
only = sys.argv[4:]
PORT = os.environ.get('PORT', '8765')
os.makedirs(OUT, exist_ok=True)
EXTRACT = open(os.path.join(HERE, 'extract.js')).read()
PREPARE = open(os.path.join(HERE, 'prepare.js')).read()
states = json.load(open(STATES))
if only:
    wanted = set(only)
    states = [s for s in states if f"{s['h']}.{s['v']}.{s['f']}" in wanted]

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 720}, device_scale_factor=2)
    page.goto(f'http://127.0.0.1:{PORT}/{DECK}/')
    page.wait_for_function('window.Reveal && Reveal.isReady()')
    page.evaluate("Reveal.configure({controls:false, progress:false, slideNumber:false, transition:'none', "
                  "backgroundTransition:'none', autoAnimate:false})")
    page.evaluate('document.fonts.ready')
    page.wait_for_timeout(2500)
    print('pseudo-elements materialised:', page.evaluate(PREPARE), flush=True)

    for st in states:
        key = f"{st['h']:02d}_{st['v']:02d}_{st['f'] + 1:02d}"
        page.evaluate(f"Reveal.slide({st['h']},{st['v']},{st['f']})")
        page.wait_for_timeout(2500 if st.get('canvas') else 1200)
        page.screenshot(path=f'{OUT}/{key}_ref.png')
        data = page.evaluate(EXTRACT)

        # the slide background alone (colour, image, or particle iframe)
        page.evaluate("window.__isolate(null, false)")
        page.screenshot(path=f'{OUT}/{key}_bg.png')
        page.evaluate("window.__restore()")

        for it in data['items']:
            if it['type'] != 'snap':
                continue
            r = it['rect']
            page.evaluate("""([id, self]) => {
                window.__isolate(document.querySelector(`[data-snap="${id}"]`), self);
                document.documentElement.classList.add('snapmode'); }""", [it['id'], bool(it.get('selfOnly'))])
            pad = 2
            clip = {'x': max(0, r['x'] - pad), 'y': max(0, r['y'] - pad),
                    'width': min(1280, r['x'] + r['w'] + pad) - max(0, r['x'] - pad),
                    'height': min(720, r['y'] + r['h'] + pad) - max(0, r['y'] - pad)}
            it['file'] = f"{key}_snap{it['id']}.png"
            it['rect'] = {'x': clip['x'], 'y': clip['y'], 'w': clip['width'], 'h': clip['height']}
            page.screenshot(path=f"{OUT}/{it['file']}", clip=clip, omit_background=True)
            page.evaluate("window.__restore(); document.documentElement.classList.remove('snapmode')")

        data['key'] = key
        data['state'] = st
        json.dump(data, open(f'{OUT}/{key}.json', 'w'))
        n = {}
        for it in data['items']:
            n[it['type']] = n.get(it['type'], 0) + 1
        print(key, n, flush=True)
    browser.close()
