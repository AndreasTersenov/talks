// Walks the current reveal slide and returns a flat, paint-ordered list of items:
//   box   — a background fill and/or border (becomes a native shape)
//   line  — one visible side of a box whose sides differ (a rule, a left bar)
//   text  — one paragraph-ish run of inline content (becomes a native text box)
//   img   — an <img> whose file can go in as-is (full resolution, cropped by overflow clips)
//   snap  — anything drawn by the browser that has no native equivalent (canvas, inline SVG,
//           display math, iframes, images that CSS transforms); Python screenshots it alone
//   video — a <video>; Python embeds the file with a poster frame
// All geometry is in viewport CSS px (1280x720), which maps 1:1 onto a 13.333in slide.
(() => {
  const sec = Reveal.getCurrentSlide();
  const items = [];
  let snapId = 0;
  window.__materialize(sec);
  // markers left by the previous build state of the same slide
  document.querySelectorAll('[data-bulleted], [data-snap]').forEach(e => { delete e.dataset.bulleted; delete e.dataset.snap; });

  const cs = el => getComputedStyle(el);
  const R = el => { const r = el.getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height }; };

  function parseColor(c) {
    if (!c) return null;
    let m = c.match(/rgba?\(([^)]+)\)/);
    if (m) {
      const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(parseFloat);
      return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1];
    }
    m = c.match(/color\(srgb ([^)]+)\)/);
    if (m) {
      const p = m[1].split(/[ \/]+/).filter(Boolean).map(parseFloat);
      return [p[0] * 255, p[1] * 255, p[2] * 255, p.length > 3 ? p[3] : 1];
    }
    if (/^(transparent|none)$/.test(c.trim())) return [0, 0, 0, 0];
    try {
      const g = (window.__pix = window.__pix || document.createElement('canvas').getContext('2d', { willReadFrequently: true }));
      g.clearRect(0, 0, 1, 1); g.fillStyle = '#000'; g.fillStyle = c; g.fillRect(0, 0, 1, 1);
      const d = g.getImageData(0, 0, 1, 1).data;
      return d[3] ? [d[0], d[1], d[2], d[3] / 255] : [0, 0, 0, 0];
    } catch (err) { return null; }
  }

  function effOpacity(el) {
    let o = 1;
    for (let x = el; x && x !== document.documentElement; x = x.parentElement) o *= parseFloat(cs(x).opacity);
    return o;
  }

  // the part of el's rect that survives every ancestor with overflow clipping
  function clipRect(el, rect) {
    let r = rect || R(el);
    let x0 = r.x, y0 = r.y, x1 = r.x + r.w, y1 = r.y + r.h;
    for (let a = el.parentElement; a && a !== document.body; a = a.parentElement) {
      const s = cs(a);
      if (s.overflowX !== 'visible' || s.overflowY !== 'visible' || (s.clipPath && s.clipPath !== 'none')) {
        const q = R(a);
        x0 = Math.max(x0, q.x); y0 = Math.max(y0, q.y);
        x1 = Math.min(x1, q.x + q.w); y1 = Math.min(y1, q.y + q.h);
      }
    }
    x0 = Math.max(x0, 0); y0 = Math.max(y0, 0); x1 = Math.min(x1, 1280); y1 = Math.min(y1, 720);
    return { x: x0, y: y0, w: Math.max(0, x1 - x0), h: Math.max(0, y1 - y0) };
  }

  function inkRect(el) {
    let r = R(el);
    let x0 = r.x, y0 = r.y, x1 = r.x + r.w, y1 = r.y + r.h;
    for (const d of el.querySelectorAll('*')) {
      const q = d.getBoundingClientRect();
      if (q.width < 0.5 || q.height < 0.5) continue;
      x0 = Math.min(x0, q.left); y0 = Math.min(y0, q.top); x1 = Math.max(x1, q.right); y1 = Math.max(y1, q.bottom);
    }
    return clipRect(el, { x: x0, y: y0, w: x1 - x0, h: y1 - y0 });
  }

  // turned or vertical text has no faithful text-box equivalent: it goes in as a picture
  function isRotated(el) {
    const s = cs(el);
    if (/vertical|sideways/.test(s.writingMode)) return true;
    const m = s.transform && s.transform.match(/^matrix\(([^)]+)\)/);
    if (!m) return false;
    const [a, b, c] = m[1].split(',').map(parseFloat);
    return Math.abs(b) > 0.01 || Math.abs(c) > 0.01;
  }

  const isKatexInline = el => el.classList && el.classList.contains('katex') && !el.closest('.katex-display');
  const isTransformed = el => { const t = cs(el).transform; return t && t !== 'none' && !/^matrix\(1, 0, 0, 1,/.test(t) && !/^matrix\(([\d.]+), 0, 0, \1,/.test(t); };

  function isAtomic(el) {
    const t = el.tagName;
    if (t === 'IMG' || t === 'VIDEO' || t === 'CANVAS' || t === 'IFRAME' || t === 'OBJECT' || t === 'EMBED') return true;
    if (t.toLowerCase() === 'svg' && !el.closest('.katex')) return true;
    if (el.classList.contains('katex-display') || t === 'MJX-CONTAINER') return true;
    return false;
  }

  const BLOCK = new Set(['block', 'flex', 'grid', 'list-item', 'table', 'table-row', 'table-cell',
    'table-row-group', 'table-header-group', 'table-footer-group', 'flow-root', 'inline-flex', 'inline-grid', 'table-caption']);

  const blockCache = new Map();
  function isBlockish(el) {
    if (blockCache.has(el)) return blockCache.get(el);
    let v;
    if (isKatexInline(el)) v = false;
    else if (isAtomic(el)) v = true;
    else {
      const s = cs(el);
      v = BLOCK.has(s.display) || s.position === 'absolute' || s.position === 'fixed' || s.float !== 'none';
      // an inline element that wraps blocks, images or a box of its own is laid out like a block
      if (!v && s.display === 'inline-block') {
        const bg = parseColor(s.backgroundColor);
        v = (bg && bg[3] > 0.02) || parseFloat(s.borderTopWidth) > 0 || parseFloat(s.borderLeftWidth) > 0;
      }
      if (!v) for (const c of el.children) { if (isBlockish(c) && cs(c).display !== 'none') { v = true; break; } }
    }
    blockCache.set(el, v);
    return v;
  }

  function emitBox(el, s, op) {
    const r = R(el);
    if (r.w < 0.3 || r.h < 0.3) return;
    const bg = parseColor(s.backgroundColor);
    const hasBg = bg && bg[3] > 0.02;
    const bgImg = s.backgroundImage && s.backgroundImage !== 'none' ? s.backgroundImage : null;
    const raw = ['Top', 'Right', 'Bottom', 'Left'].map(k => ({
      w: parseFloat(s['border' + k + 'Width']) || 0,
      c: parseColor(s['border' + k + 'Color']),
      st: s['border' + k + 'Style'],
    }));
    const sides = raw.map(b => (b.w > 0 && b.c && b.c[3] > 0.02 && b.st !== 'none' && b.st !== 'hidden') ? b : null);
    // a CSS triangle (arrowheads, bubble tails): zero-size content, borders of which some are transparent
    const thick = raw.filter(b => b.w > 0 && b.st !== 'none');
    if ((el.clientWidth < 1 || el.clientHeight < 1) && thick.length >= 2 && thick.some(b => b.c && b.c[3] > 0.02) && thick.some(b => !b.c || b.c[3] <= 0.02)) {
      el.dataset.snap = ++snapId;
      items.push({ type: 'snap', id: snapId, selfOnly: true, rect: clipRect(el), op });
      return;
    }
    const anySide = sides.some(Boolean);
    const rings = [], insetRules = [];
    let dropShadow = null;
    if (s.boxShadow && s.boxShadow !== 'none') {
      for (const sh of s.boxShadow.split(/,(?![^(]*\))/)) {
        const col = parseColor(sh);
        const nums = sh.replace(/rgba?\([^)]*\)|color\([^)]*\)/, '').trim().split(/\s+/).map(parseFloat);
        const [dx, dy, blur, spread] = [nums[0] || 0, nums[1] || 0, nums[2] || 0, nums[3] || 0];
        if (!col || col[3] <= 0.05) continue;
        if (!/inset/.test(sh) && dx === 0 && dy === 0 && spread > 0 && blur <= 2) rings.push({ spread, col });
        else if (!/inset/.test(sh) && blur > 2 && !dropShadow) dropShadow = { dx, dy, blur, col };
        else if (/inset/.test(sh) && blur <= 1 && !spread && (dx || dy)) insetRules.push({ dx, dy, col });
      }
    }
    const scaleNow = el.offsetWidth ? r.w / el.offsetWidth : 1;
    if (s.outlineStyle && s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) > 0) {
      const oc = parseColor(s.outlineColor);
      if (oc && oc[3] > 0.05) rings.push({ spread: parseFloat(s.outlineWidth) + 2 * (parseFloat(s.outlineOffset) || 0), col: oc, outline: true });
    }
    for (const g of rings) {
      const sp = g.spread * scaleNow;
      items.push({ type: 'box', rect: { x: r.x - sp / 2, y: r.y - sp / 2, w: r.w + sp, h: r.h + sp }, op,
        radius: (parseFloat(s.borderTopLeftRadius) || 0) * scaleNow + sp / 2, fill: null, border: { w: sp, c: g.col, dash: false }, shadow: null });
    }
    for (const g of insetRules) {
      const w = Math.abs(g.dx || g.dy) * scaleNow;
      if (g.dy < 0) items.push({ type: 'line', x1: r.x, y1: r.y + r.h - w / 2, x2: r.x + r.w, y2: r.y + r.h - w / 2, w, c: g.col, op, dash: false });
      else if (g.dy > 0) items.push({ type: 'line', x1: r.x, y1: r.y + w / 2, x2: r.x + r.w, y2: r.y + w / 2, w, c: g.col, op, dash: false });
      else if (g.dx > 0) items.push({ type: 'line', x1: r.x + w / 2, y1: r.y, x2: r.x + w / 2, y2: r.y + r.h, w, c: g.col, op, dash: false });
      else items.push({ type: 'line', x1: r.x + r.w - w / 2, y1: r.y, x2: r.x + r.w - w / 2, y2: r.y + r.h, w, c: g.col, op, dash: false });
    }
    if (!hasBg && !anySide && !bgImg) return;
    const rad = s.borderTopLeftRadius || '0';
    const ellipse = /%/.test(rad) ? parseFloat(rad) >= 50 : false;
    const radius = /%/.test(rad) ? parseFloat(rad) / 100 * Math.min(r.w, r.h) : (parseFloat(rad) || 0) * scaleNow;
    if (bgImg) {
      // gradients and textures: let the browser paint the box itself, without its children
      el.dataset.snap = ++snapId;
      items.push({ type: 'snap', id: snapId, selfOnly: true, rect: r, op });
      return;
    }
    const uniform = sides.every(b => b && sides[0] && b.w === sides[0].w && b.c.join() === sides[0].c.join());
    items.push({
      type: 'box', rect: r, op, radius,
      fill: hasBg ? bg : null,
      border: uniform ? { w: sides[0].w, c: sides[0].c, dash: sides[0].st === 'dashed' || sides[0].st === 'dotted' } : null,
      ellipse, shadow: dropShadow ? { dx: dropShadow.dx * scaleNow, dy: dropShadow.dy * scaleNow, blur: dropShadow.blur * scaleNow, c: dropShadow.col } : null,
    });
    if (!uniform) {
      const [t, rt, b, l] = sides;
      const seg = (x1, y1, x2, y2, side) => items.push({ type: 'line', x1, y1, x2, y2, w: side.w, c: side.c, op,
        dash: side.st === 'dashed' || side.st === 'dotted' });
      if (t) seg(r.x, r.y + t.w / 2, r.x + r.w, r.y + t.w / 2, t);
      if (b) seg(r.x, r.y + r.h - b.w / 2, r.x + r.w, r.y + r.h - b.w / 2, b);
      if (l) seg(r.x + l.w / 2, r.y, r.x + l.w / 2, r.y + r.h, l);
      if (rt) seg(r.x + r.w - rt.w / 2, r.y, r.x + r.w - rt.w / 2, r.y + r.h, rt);
    }
  }

  // ---------- math: KaTeX's MathML → styled runs ----------
  const ACCENT = { '^': '̂', 'ˆ': '̂', '~': '̃', '˜': '̃', '¯': '̄', '‾': '̅',
    '˙': '̇', '¨': '̈', '→': '⃗', '⃗': '⃗' };
  const MATHALPHA = (alphabet, ch) => {
    const c = ch.codePointAt(0);
    const upper = c >= 65 && c <= 90, lower = c >= 97 && c <= 122;
    if (!upper && !lower) return ch;
    const holes = {
      script: { B: 0x212C, E: 0x2130, F: 0x2131, H: 0x210B, I: 0x2110, L: 0x2112, M: 0x2133, R: 0x211B, e: 0x212F, g: 0x210A, o: 0x2134 },
      double: { C: 0x2102, H: 0x210D, N: 0x2115, P: 0x2119, Q: 0x211A, R: 0x211D, Z: 0x2124 },
      fraktur: { C: 0x212D, H: 0x210C, I: 0x2111, R: 0x211C, Z: 0x2128 },
    }[alphabet];
    if (holes[ch]) return String.fromCodePoint(holes[ch]);
    const base = { script: 0x1D49C, double: 0x1D538, fraktur: 0x1D504 }[alphabet];
    return String.fromCodePoint(base + (upper ? c - 65 : 26 + c - 97));
  };
  const SPACED = new Set(['=', '≈', '∼', '≃', '≡', '<', '>', '≤', '≥', '→', '←', '⇒', '∝', '+', '−', '×', '∈', '⊂', '≪', '≫', '↦', '∣', '|']);
  const BIGOP = n => /^[∑∫∏⋃⋂∮]$/.test((n.textContent || '').trim());
  // structures a line of text cannot carry: a math-only block containing one of these goes in as a picture
  const COMPLEX = 'mfrac, msqrt, mroot, munderover, mtable, mover';
  function mathRuns(node, base, shift) {
    const out = [];
    const run = (t, italic, extra) => out.push({ ...base, t, italic: italic, shift, math: true, ...(extra || {}) });
    const kids = [...node.children];
    const tag = node.tagName.toLowerCase();
    const sub = (n, d) => mathRuns(n, base, (shift || 0) + d);
    switch (tag) {
      case 'mi': case 'mn': case 'mtext': case 'ms': {
        const t = node.textContent;
        const variant = node.getAttribute('mathvariant') || '';
        const letter = tag === 'mi';
        const italic = variant ? /italic/.test(variant) && !/script|double|fraktur/.test(variant) : (letter && [...t].length === 1);
        const alphabet = /script/.test(variant) ? 'script' : /double-struck/.test(variant) ? 'double' : /fraktur/.test(variant) ? 'fraktur' : null;
        if (alphabet) run([...t].map(ch => MATHALPHA(alphabet, ch)).join(''), false, { font: 'Cambria Math' });
        else run(t, italic, /bold/.test(variant) ? { bold: true, weight: 700 } : null);
        if (letter && [...t].length > 1 && !variant.includes('bold')) run(' ', false);   // log, max, arg: a space before the argument
        break;
      }
      case 'mo': {
        const t = node.textContent.trim();
        if (t === '⁡' || t === '⁢' || t === '') break;       // invisible function application / times
        if (BIGOP(node)) { run(t, false); break; }
        if (SPACED.has(t) && node.getAttribute('stretchy') !== 'true') run(' ' + t + ' ', false);
        else if (t === ',') run(', ', false);
        else run(t, false);
        break;
      }
      case 'mspace': { const w = parseFloat(node.getAttribute('width')) || 0; if (w > 0.15) run(' ', false); break; }
      case 'msub': out.push(...mathRuns(kids[0], base, shift), ...sub(kids[1], -1)); if (BIGOP(kids[0])) run(' ', false); break;
      case 'msup': out.push(...mathRuns(kids[0], base, shift), ...sub(kids[1], 1)); break;
      case 'msubsup': out.push(...mathRuns(kids[0], base, shift), ...sub(kids[1], -1), ...sub(kids[2], 1)); if (BIGOP(kids[0])) run(' ', false); break;
      case 'munder': out.push(...mathRuns(kids[0], base, shift), ...sub(kids[1], -1)); run(' ', false); break;
      case 'munderover': out.push(...mathRuns(kids[0], base, shift), ...sub(kids[1], -1), ...sub(kids[2], 1)); run(' ', false); break;
      case 'mover': {
        const acc = kids[1] && ACCENT[kids[1].textContent.trim()];
        const b = mathRuns(kids[0], base, shift);
        if (acc && b.length) { b[b.length - 1].t += acc; out.push(...b); }
        else out.push(...b, ...sub(kids[1], 1));
        break;
      }
      case 'mfrac': {
        const simple = n => n.textContent.trim().length <= 2;
        const [n, d] = kids;
        if (!simple(n)) run('(', false);
        out.push(...mathRuns(n, base, shift));
        if (!simple(n)) run(')', false);
        run('/', false);
        if (!simple(d)) run('(', false);
        out.push(...mathRuns(d, base, shift));
        if (!simple(d)) run(')', false);
        break;
      }
      case 'msqrt': run('√(', false); kids.forEach(k => out.push(...mathRuns(k, base, shift))); run(')', false); break;
      case 'mroot': run('√(', false); out.push(...mathRuns(kids[0], base, shift)); run(')', false); break;
      case 'mphantom': case 'annotation': case 'annotation-xml': break;
      case 'semantics': if (kids[0]) out.push(...mathRuns(kids[0], base, shift)); break;
      case 'mtable': kids.forEach((k, i) => { if (i) run('; ', false); out.push(...mathRuns(k, base, shift)); }); break;
      default: kids.forEach(k => out.push(...mathRuns(k, base, shift)));
    }
    return out;
  }

  // ---------- inline content → runs ----------
  function styleOf(el, op, shift) {
    const s = cs(el);
    const fam = s.fontFamily.split(',')[0].replace(/["']/g, '').trim();
    const w = parseInt(s.fontWeight, 10);
    const col = parseColor(s.color) || [0, 0, 0, 1];
    const va = s.verticalAlign;
    let sh = shift || 0;
    if (va === 'sub') sh -= 1; else if (va === 'super') sh += 1;
    return {
      font: fam, px: parseFloat(s.fontSize), weight: w, bold: w >= 600, italic: s.fontStyle === 'italic',
      color: [col[0], col[1], col[2], col[3] * op], underline: /underline/.test(s.textDecorationLine),
      strike: /line-through/.test(s.textDecorationLine), shift: sh, ws: s.whiteSpace,
      caps: s.textTransform, spacing: parseFloat(s.letterSpacing) || 0,
    };
  }

  function collectRuns(node, parentStyle, out, opBase) {
    if (node.nodeType === 3) {
      if (node.nodeValue && parentStyle.color[3] > 0.05) out.push({ ...parentStyle, t: node.nodeValue });
      return;
    }
    if (node.nodeType !== 1) return;
    const el = node;
    const s = cs(el);
    if (s.display === 'none' || s.visibility === 'hidden') return;
    if (el.tagName === 'BR') { out.push({ br: true }); return; }
    const op = effOpacity(el);
    if (op < 0.05) return;
    if (isKatexInline(el)) {
      const math = el.querySelector('math');
      const st = styleOf(el, op, parentStyle.shift);
      if (math) {
        const base = { ...st, font: 'Times New Roman', bold: st.bold };
        out.push(...mathRuns(math, base, parentStyle.shift));
      }
      return;
    }
    if (el.tagName === 'IMG' || el.tagName.toLowerCase() === 'svg') return;   // inline icons: dropped
    const st = styleOf(el, op, parentStyle.shift);
    const gapL = parseFloat(s.marginLeft) + parseFloat(s.paddingLeft), gapR = parseFloat(s.marginRight) + parseFloat(s.paddingRight);
    if (gapL > 4) out.push({ ...parentStyle, t: '\u2002', keep: true });
    if (el.tagName === 'SUB') st.shift = (parentStyle.shift || 0) - 1;
    if (el.tagName === 'SUP') st.shift = (parentStyle.shift || 0) + 1;
    for (const c of el.childNodes) collectRuns(c, st, out, op);
    if (gapR > 4) out.push({ ...parentStyle, t: '\u2002', keep: true });
  }

  function normalise(runs) {
    // CSS white-space collapsing across run boundaries
    const out = [];
    let lastSpace = true;
    for (const r of runs) {
      if (r.br) { if (out.length && !out[out.length - 1].br) out[out.length - 1].t = out[out.length - 1].t.replace(/ +$/, ''); out.push(r); lastSpace = true; continue; }
      if (r.keep) { if (out.length) out.push({ ...r }); lastSpace = true; continue; }
      let t = r.t;
      if (!/pre/.test(r.ws || '')) t = t.replace(/[\s ]+/g, m => (m.includes(' ') && !/[\s]/.test(m.replace(/ /g, '')) ? m : ' '));
      if (r.caps === 'uppercase') t = t.toUpperCase();
      if (lastSpace) t = t.replace(/^ +/, '');
      if (!t) continue;
      lastSpace = / $/.test(t);
      out.push({ ...r, t });
    }
    while (out.length && (out[out.length - 1].br || !out[out.length - 1].t.trim())) {
      const last = out[out.length - 1];
      if (last.br || !last.t.trim()) out.pop(); else break;
    }
    if (out.length && !out[out.length - 1].br) out[out.length - 1].t = out[out.length - 1].t.replace(/ +$/, '');
    return out;
  }

  // getComputedStyle does not report ::marker colours, so read the matching stylesheet rules
  let markerRules = null;
  function markerColor(li) {
    if (!markerRules) {
      markerRules = [];
      const visit = rules => { for (const r of rules) {
        if (r.cssRules && !r.selectorText) { try { visit(r.cssRules); } catch (err) {} continue; }
        if (r.selectorText && /::marker/.test(r.selectorText) && r.style && r.style.color) markerRules.push(r);
      } };
      for (const sh of document.styleSheets) { try { visit(sh.cssRules); } catch (err) {} }
    }
    let colour = null;
    for (const r of markerRules) {
      for (const sel of r.selectorText.split(',')) {
        if (!/::marker/.test(sel)) continue;
        try { if (li.matches(sel.replace(/::marker/g, '').trim())) colour = r.style.color; } catch (err) {}
      }
    }
    if (!colour) return null;
    const v = colour.match(/var\((--[^,)]+)/);
    if (v) colour = cs(li).getPropertyValue(v[1]).trim() || colour;
    return parseColor(colour);
  }

  function emitText(el, nodes) {
    const range = document.createRange();
    range.setStartBefore(nodes[0]);
    range.setEndAfter(nodes[nodes.length - 1]);
    const rects = [...range.getClientRects()].filter(q => q.width > 0.5 && q.height > 0.5);
    if (!rects.length) return;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const q of rects) { x0 = Math.min(x0, q.left); y0 = Math.min(y0, q.top); x1 = Math.max(x1, q.right); y1 = Math.max(y1, q.bottom); }
    const op = effOpacity(el);
    if (op < 0.05) return;
    // a block that is nothing but one piece of structured math: picture it, LaTeX in the alt text
    const solid = nodes.filter(n => !(n.nodeType === 3 && !n.nodeValue.trim()));
    if (solid.length === 1 && solid[0].nodeType === 1) {
      const k = isKatexInline(solid[0]) ? solid[0] : solid[0].querySelector && solid[0].querySelector('.katex');
      if (k && solid[0].textContent.trim() === k.textContent.trim() && k.querySelector(COMPLEX)) {
        k.dataset.snap = ++snapId;
        const tex = k.querySelector('annotation[encoding="application/x-tex"]');
        items.push({ type: 'snap', id: snapId, rect: inkRect(k), op, alt: tex ? tex.textContent : '' });
        return;
      }
    }
    // inline highlights (a background on a span inside the text) sit under the text box
    for (const n of nodes) {
      if (n.nodeType !== 1) continue;
      for (const h of [n, ...n.querySelectorAll('*')]) {
        if (h.closest('.katex')) continue;
        const hs = cs(h);
        const hb = parseColor(hs.backgroundColor);
        const himg = hs.backgroundImage && hs.backgroundImage !== 'none';
        if (!(hb && hb[3] > 0.02) && !himg) continue;
        const hop = effOpacity(h);
        if (himg) { h.dataset.snap = ++snapId; items.push({ type: 'snap', id: snapId, selfOnly: true, rect: clipRect(h), op: hop }); continue; }
        for (const q of h.getClientRects()) {
          if (q.width < 1 || q.height < 1) continue;
          items.push({ type: 'box', rect: { x: q.left, y: q.top, w: q.width, h: q.height }, op: hop,
            radius: parseFloat(hs.borderTopLeftRadius) || 0, fill: hb, border: null, ellipse: false, shadow: null });
        }
      }
    }
    const base = styleOf(el, op, 0);
    const runs = [];
    for (const n of nodes) collectRuns(n, base, runs, op);
    const clean = normalise(runs);
    if (!clean.some(r => r.t && r.t.trim())) return;
    const s = cs(el);
    // rendered scale of this element (reveal's fit-to-window plus any CSS transform)
    const scale = el.offsetWidth ? el.getBoundingClientRect().width / el.offsetWidth : Reveal.getScale();
    const lh = s.lineHeight === 'normal' ? null : parseFloat(s.lineHeight);
    // the box the text is allowed to wrap in: the element's content box, not the ink
    const er = R(el);
    const padL = parseFloat(s.paddingLeft) * scale, padR = parseFloat(s.paddingRight) * scale;
    const bl = parseFloat(s.borderLeftWidth) * scale, br = parseFloat(s.borderRightWidth) * scale;
    const content = { x: er.x + padL + bl, w: er.w - padL - padR - bl - br };
    let bullet = null;
    const li = el.tagName === 'LI' ? el : null;
    if (li && !li.dataset.bulleted) {       // the marker belongs to the li's first run of text only
      li.dataset.bulleted = '1';
      const ls = s.listStyleType;
      if (ls && ls !== 'none') {
        const mc = markerColor(li) || base.color;
        bullet = { char: ls === 'square' ? '▪' : ls === 'circle' ? '◦' : ls === 'decimal' ? null : '•',
          num: ls === 'decimal' ? [...li.parentElement.children].indexOf(li) + 1 : null, color: mc };
      }
    }
    const firstIndent = Math.max(0, rects[0].left - content.x);
    items.push({
      type: 'text', rect: { x: x0, y: y0, w: x1 - x0, h: y1 - y0 }, content, scale, firstIndent,
      align: s.textAlign, lh: lh ? lh * scale : null, lines: rects.length ? Math.round((y1 - y0) / ((lh || base.px * 1.2) * scale)) : 1,
      runs: clean.map(r => r.br ? r : { t: r.t, font: r.font, pt: r.px * scale * 0.75, cssPx: r.px, spacingPt: (r.spacing || 0) * scale * 0.75, bold: r.bold, weight: r.weight, italic: r.italic,
        color: r.color, underline: r.underline, strike: r.strike, shift: r.shift, math: !!r.math }),
      bullet,
    });
  }

  function walk(el) {
    const s = cs(el);
    if (s.display === 'none' || s.visibility === 'hidden') return;
    const op = effOpacity(el);
    if (op < 0.05) return;
    const r = clipRect(el);
    if (r.w < 0.5 || r.h < 0.5) return;
    if (el !== sec && isRotated(el) && el.textContent.trim()) {
      el.dataset.snap = ++snapId;
      items.push({ type: 'snap', id: snapId, rect: inkRect(el), op });
      return;
    }
    if (el !== sec) emitBox(el, s, op);
    if (isAtomic(el)) {
      const full = R(el);
      if (el.tagName === 'VIDEO') {
        items.push({ type: 'video', src: el.currentSrc || (el.querySelector('source') || {}).src, rect: full, op });
        return;
      }
      if (el.tagName === 'IMG') {
        const src = el.currentSrc || el.src;
        const nat = el.naturalWidth / el.naturalHeight, box = full.w / full.h;
        const fit = s.objectFit;
        const plain = /\.(png|jpe?g|gif|webp)(\?|$)/i.test(src) && (fit === 'fill' || Math.abs(nat / box - 1) < 0.03)
          && (!s.filter || s.filter === 'none') && !isTransformed(el);
        if (plain) { items.push({ type: 'img', src, rect: full, clip: r, op, alt: el.alt || '' }); return; }
      }
      if (el.tagName === 'CANVAS') {
        try {
          items.push({ type: 'canvas', data: el.toDataURL('image/png'), rect: full, clip: r, op });
          return;
        } catch (err) { /* tainted: fall through to a snapshot */ }
      }
      el.dataset.snap = ++snapId;
      const latex = el.querySelector && el.querySelector('annotation[encoding="application/x-tex"]');
      items.push({ type: 'snap', id: snapId, rect: el.tagName.toLowerCase() === 'svg' || el.classList.contains('katex-display') ? inkRect(el) : r, op, alt: latex ? latex.textContent : (el.getAttribute('alt') || el.getAttribute('aria-label') || '') });
      return;
    }
    let seq = [];
    const flush = () => { if (seq.length) { emitText(el, seq); seq = []; } };
    for (const n of el.childNodes) {
      if (n.nodeType === 3) { seq.push(n); continue; }
      if (n.nodeType !== 1) continue;
      if (isBlockish(n)) { flush(); walk(n); } else seq.push(n);
    }
    flush();
  }

  walk(sec);
  return { items, scale: Reveal.getScale() };
})()
