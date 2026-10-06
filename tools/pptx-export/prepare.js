// Runs once after load. Turns every ::before / ::after that draws something into a real <span>
// carrying the pseudo-element's computed style, so the walker sees bullets, bars and arrowheads
// as ordinary elements. Adds the style rules the snapshot mode needs.
(() => {
  const css = document.createElement('style');
  css.textContent = `
    [data-pzb]::before { content: none !important; }
    [data-pza]::after  { content: none !important; }
    .reveal .slides button { visibility: hidden !important; }
    html.snapmode, html.snapmode body, html.snapmode .reveal, html.snapmode .reveal-viewport,
    html.snapmode .reveal .slides { background: transparent !important; background-image: none !important; }
    html.snapmode .reveal .backgrounds { display: none !important; }
    html.isolating .reveal .slides, html.isolating .reveal .slides * { transition: none !important; }
  `;
  document.head.appendChild(css);

  // Isolation by inline !important styles, which beat any stylesheet rule (some deck rules force
  // visibility with !important themselves). target = null hides the whole slide content (background
  // capture); otherwise only the target paints, and with selfOnly only its own box, not its children.
  const saved = [];
  window.__isolate = (target, selfOnly) => {
    const hide = el => { saved.push([el, el.style.getPropertyValue('visibility'), el.style.getPropertyPriority('visibility'),
      el.style.getPropertyValue('color'), el.style.getPropertyPriority('color')]); el.style.setProperty('visibility', 'hidden', 'important'); };
    document.documentElement.classList.add('isolating');
    const slidesRoot = document.querySelector('.reveal .slides');
    for (const el of [slidesRoot, ...slidesRoot.querySelectorAll('*')]) {
      if (target && el === target) {
        hide(el);
        el.style.setProperty('visibility', 'visible', 'important');
        if (selfOnly) el.style.setProperty('color', 'transparent', 'important');
      } else if (target && target.contains(el)) {
        if (selfOnly) hide(el);
      } else hide(el);
    }
  };
  window.__restore = () => {
    for (const [el, v, vp, c, cp] of saved.reverse()) {
      if (v) el.style.setProperty('visibility', v, vp); else el.style.removeProperty('visibility');
      if (c) el.style.setProperty('color', c, cp); else el.style.removeProperty('color');
    }
    saved.length = 0;
    document.documentElement.classList.remove('isolating');
  };

  const unquote = c => {
    const parts = c.match(/"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'/g);
    if (!parts) return '';
    return parts.map(p => p.slice(1, -1).replace(/\\([0-9a-fA-F]{1,6}) ?/g, (_, h) => String.fromCodePoint(parseInt(h, 16)))
      .replace(/\\(.)/g, '$1')).join('');
  };
  // idempotent: JS-driven slides re-render their markup, so this runs again at every extraction
  window.__materialize = root => {
    const todo = [];
    for (const el of root.querySelectorAll('*')) {
      if (el.closest('.katex, svg') || el.dataset.pseudo) continue;
      for (const pse of ['::before', '::after']) {
        if ((pse === '::before' && el.dataset.pzb) || (pse === '::after' && el.dataset.pza)) continue;
        const s = getComputedStyle(el, pse);
        if (!s.content || s.content === 'none' || s.content === 'normal') continue;
        todo.push([el, pse, s]);
      }
    }
    for (const [el, pse, s] of todo) {
      const span = document.createElement('span');
      for (let i = 0; i < s.length; i++) {
        const prop = s[i];
        if (prop === 'content') continue;
        span.style.setProperty(prop, s.getPropertyValue(prop));
      }
      span.textContent = unquote(s.content);
      span.dataset.pseudo = pse;
      if (pse === '::before') { el.insertBefore(span, el.firstChild); el.dataset.pzb = '1'; }
      else { el.appendChild(span); el.dataset.pza = '1'; }
    }
    return todo.length;
  };
  return window.__materialize(document.querySelector('.reveal .slides'));
})()
