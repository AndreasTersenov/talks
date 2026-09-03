"""Headless render check for the BNT explainer slide.
Loads index.html, steps through the 5 acts, screenshots each, and reports any
console errors / page exceptions. Verification-only (not part of the deliverable).
"""
import pathlib, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent.resolve()
URL = (HERE / "index.html").as_uri()
OUT = HERE / "_verify_shots"
OUT.mkdir(exist_ok=True)

errors = []

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 800},
                            device_scale_factor=2)
    page.on("console", lambda m: errors.append(f"[{m.type}] {m.text}")
            if m.type in ("error", "warning") else None)
    page.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))

    page.goto(URL)
    page.wait_for_timeout(1200)   # let reveal init + first frame settle

    for act in range(1, 6):
        if act > 1:
            page.keyboard.press("ArrowRight")
        page.wait_for_timeout(1400)   # let the tween settle
        # report what the engine thinks the act is + meter text
        info = page.evaluate("""() => {
            const s = document.querySelector('[data-bnt-explainer]');
            const e = s && s._bntEngine;
            return {
              act: e ? e.act : null,
              ratio: s.querySelector('.bnt-bar--l1 .bnt-bar-ratio')?.textContent,
              cnnRatio: s.querySelector('.bnt-bar--cnn .bnt-bar-ratio')?.textContent,
              cnnOpacity: s.querySelector('.bnt-bar--cnn')?.style.opacity,
              abs: s.querySelector('.bnt-meter-abs')?.textContent,
              caption: (s.querySelector('.bnt-caption')?.textContent || '').slice(0, 70),
              kern: s.querySelector('.bnt-kernels-caption')?.textContent
            };
        }""")
        print(f"ACT {act}: engine.act={info['act']}  "
              f"l1={info['ratio']}  cnn={info['cnnRatio']}(op={info['cnnOpacity']})  "
              f"abs='{info['abs']}'  kern='{info['kern']}'")
        print(f"        cap: {info['caption']}")
        page.screenshot(path=str(OUT / f"act{act}.png"))

    browser.close()

print("\n=== console errors/warnings ===")
if errors:
    for e in errors:
        print(" ", e)
    sys.exit(1)
else:
    print("  none")
