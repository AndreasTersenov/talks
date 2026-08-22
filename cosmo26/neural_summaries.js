/* ===========================================================================
 * Neural-summary explainer — "how each summary is trained"  (v2)
 * ---------------------------------------------------------------------------
 * Two sibling reveal.js slides, three acts each, on the PRINCIPLE of the two
 * ways a neural network learns a low-dimensional summary for SBI:
 *
 *   Slide 1 — Regression (MSE): the network's output IS the summary, trained
 *     against the true parameters (ℒ = E‖θ − f_φ(x)‖²). Optimum = posterior
 *     MEAN; on a non-Gaussian posterior that point misses the shape and is not
 *     a sufficient statistic.
 *   Slide 2 — VMIM: the network outputs a learned summary t; a normalizing
 *     flow q_ψ(θ|t) must rebuild the full posterior. Trained to max I(t;θ);
 *     optimum = a SUFFICIENT statistic that keeps the non-Gaussian shape.
 *
 * The pipeline + objective (the "how") are crisp HTML/CSS + KaTeX. Only the
 * parameter-space plot and the map thumbnail are <canvas>; the posterior is a
 * proper warped-Gaussian contour (getdist-style), not a blob. Self-contained,
 * own namespace (NeuralSummaries) and .ns-* selectors; loads beside the BNT
 * module. Act 1 = default; the two .ns-frag markers step to acts 2 and 3.
 * ======================================================================== */
(function (global) {
  "use strict";

  var C_MSE = "#E69F00", C_VMIM = "#0072B2", C_GREY = "#8a96a3",
      C_INK = "#1b2733", C_MUTE = "#8b95a0", C_OK = "#1d7a54";

  /* ------------------------------- helpers ------------------------------- */
  function mulberry32(s) { return function () {
    s |= 0; s = (s + 0x6D2B79F5) | 0; var t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
  function gaussian(rng) { var u = 1 - rng(), v = rng();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function ease(t) { return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2; }
  function hexA(hex, a) { var r = parseInt(hex.substr(1, 2), 16), g = parseInt(hex.substr(3, 2), 16),
    b = parseInt(hex.substr(5, 2), 16); return "rgba(" + r + "," + g + "," + b + "," + a + ")"; }
  function fitCanvas(c) {
    var dpr = Math.min(window.devicePixelRatio || 1, 2), r = c.getBoundingClientRect();
    var w = r.width || (c.width / 2), h = r.height || (c.height / 2);
    c._w = w; c._h = h; c._dpr = dpr; c.width = Math.round(w * dpr); c.height = Math.round(h * dpr);
  }
  function tweenStep(cur, tgt, keys, sm) { var moving = false;
    for (var i = 0; i < keys.length; i++) { var k = keys[i], d = tgt[k] - cur[k];
      if (Math.abs(d) > 1e-4) { cur[k] += d * sm; moving = true; } else cur[k] = tgt[k]; } return moving; }
  function clabel(ctx, txt, x, y, color, size, align, bold) {
    ctx.save(); ctx.fillStyle = color; ctx.textAlign = align || "left"; ctx.textBaseline = "middle";
    ctx.font = (bold ? "700 " : "400 ") + (size || 13) + "px ui-sans-serif, system-ui, sans-serif";
    ctx.fillText(txt, x, y); ctx.restore();
  }
  var VIRIDIS = [[68,1,84],[72,40,120],[62,74,137],[49,104,142],[38,130,142],
                 [31,158,137],[53,183,121],[110,206,88],[181,222,43],[253,231,37]];
  function viridis(t) { t = t < 0 ? 0 : (t > 1 ? 1 : t); var x = t * 9, i = Math.floor(x), f = x - i;
    if (i >= 9) return VIRIDIS[9]; var a = VIRIDIS[i], b = VIRIDIS[i + 1];
    return [a[0] + (b[0]-a[0])*f, a[1] + (b[1]-a[1])*f, a[2] + (b[2]-a[2])*f]; }

  /* ---- a smooth convergence-map thumbnail (viridis Gaussian random field) */
  function renderMap(canvas) {
    var G = canvas.width, rng = mulberry32(314159);
    var blobs = [];
    for (var k = 0; k < 6; k++) blobs.push({ x: rng(), y: rng(), a: 0.5 + rng() * 1.1, s: 0.10 + rng() * 0.10 });
    var ctx = canvas.getContext("2d"), img = ctx.createImageData(G, G);
    for (var yy = 0; yy < G; yy++) for (var xx = 0; xx < G; xx++) {
      var X = xx / (G - 1), Y = yy / (G - 1), v = 0.2 + 0.15 * Math.sin(6.0 * (X + 0.6 * Y));
      for (var bi = 0; bi < blobs.length; bi++) { var bb = blobs[bi], dx = X - bb.x, dy = Y - bb.y;
        v += bb.a * Math.exp(-(dx * dx + dy * dy) / (2 * bb.s * bb.s)); }
      var c = viridis((v - 0.1) / 1.7), o = (yy * G + xx) * 4;
      img.data[o] = c[0]; img.data[o+1] = c[1]; img.data[o+2] = c[2]; img.data[o+3] = 255;
    }
    ctx.putImageData(img, 0, 0);
  }

  /* ---- warped-Gaussian posterior, drawn as filled contour levels ---------
   * In whitened (u,v): u,v ~ N(0,1). Warp b = v − bend·(u²−1) bends it into a
   * banana whose MEAN stays at (cx,cy) while its ridge/mode moves off it. So an
   * amber dot at (cx,cy) sits off the ridge exactly when bend>0 — the proven
   * "mean misses a non-Gaussian posterior" point, drawn analytically (crisp). */
  function ptOf(P, u, v) {
    var a = u, b = v - P.bend * (u * u - 1);
    var ax = a * P.sx, by = b * P.sy, cr = Math.cos(P.rot || 0), sr = Math.sin(P.rot || 0);
    return [P.cx + ax * cr - by * sr, P.cy + ax * sr + by * cr];
  }
  function contourPath(ctx, P, r) {
    ctx.beginPath();
    for (var i = 0; i <= 64; i++) { var phi = i / 64 * 2 * Math.PI;
      var p = ptOf(P, r * Math.cos(phi), r * Math.sin(phi));
      if (i === 0) ctx.moveTo(p[0], p[1]); else ctx.lineTo(p[0], p[1]); }
    ctx.closePath();
  }
  function drawPosterior(ctx, P, color, alpha, fill) {
    if (alpha <= 0.01) return;
    ctx.save(); ctx.globalAlpha = alpha;
    var levels = [2.05, 1.15];                 // ~95%, ~68% (sized to fit the panel)
    for (var i = 0; i < levels.length; i++) {
      contourPath(ctx, P, levels[i]);
      if (fill) { ctx.fillStyle = hexA(color, i === 0 ? 0.13 : 0.22); ctx.fill(); }
      ctx.lineWidth = 2; ctx.strokeStyle = hexA(color, fill ? 0.55 : 0.95);
      if (!fill) ctx.setLineDash([9, 7]);
      ctx.stroke(); ctx.setLineDash([]);
    }
    ctx.restore();
  }
  function faintFrame(ctx, W, H) {
    ctx.save(); ctx.strokeStyle = "#dfe5ea"; ctx.lineWidth = 1.2;
    ctx.beginPath(); ctx.moveTo(34, H - 26); ctx.lineTo(W - 18, H - 26); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(34, H - 26); ctx.lineTo(34, 18); ctx.stroke();
    clabel(ctx, "Ωm", W - 22, H - 14, C_MUTE, 13, "right", false);
    ctx.restore();
  }

  /* ========================== shared engine base ========================= */
  function setup(self, root) {
    self.root = root;
    self.plot = root.querySelector(".ns-plot-canvas");
    self.captionEl = root.querySelector(".ns-caption");
    self.nActs = 3; self.act = 1; self.running = false; self.autoTimer = null;
    self.cur = self._stateForAct(1); self.tgt = self._stateForAct(1);
    var mapC = root.querySelector("canvas.ns-map"); if (mapC) renderMap(mapC);  // only if no real-patch <img>
    fitCanvas(self.plot); self._applyCopy(1);
    self._loop = function () { self._frame(); };
    window.addEventListener("resize", function () { fitCanvas(self.plot); self._draw(); });
  }
  function ctrlProto(P) {
    P.resize = function () { fitCanvas(this.plot); this._draw(); };
    P.goTo = function (act) { act = Math.max(1, Math.min(this.nActs, act));
      this.act = act; this.tgt = this._stateForAct(act); this._applyCopy(act); this.start(); };
    P.snapTo = function (act) { this.cur = this._stateForAct(act); this.goTo(act); };
    P.start = function () { if (!this.running) { this.running = true; requestAnimationFrame(this._loop); } };
    P.autoplay = function () { var s = this; if (this.autoTimer) clearInterval(this.autoTimer);
      this.snapTo(1); var a = 1; this.autoTimer = setInterval(function () {
        a += 1; if (a > s.nActs) { clearInterval(s.autoTimer); s.autoTimer = null; return; } s.goTo(a); }, 2600); };
    P._applyCopy = function (act) { var c = this.COPY[act]; if (!c) return;
      this.captionEl.innerHTML = c;
      renderMath(this.captionEl); };
  }

  /* ======================= SLIDE 1 — Regression ========================== */
  function RegressionEngine(root) { setup(this, root); }
  ctrlProto(RegressionEngine.prototype);
  RegressionEngine.prototype.COPY = {
    1: "<ul class='ns-bul'>" +
         "<li>A lensing map has \\(\\sim\\!10^4\\) pixels: too many to infer from directly</li>" +
         "<li>Compress it into a low-dimensional <b>summary</b> \\(t=f_\\phi(x)\\)</li>" +
         "<li><b>Regression:</b> train the network to predict the parameters (loss above)</li>" +
       "</ul>",
    2: "<ul class='ns-bul'>" +
         "<li>Optimum: the posterior <b>mean</b>, \\(\\hat\\theta=\\mathbb{E}[\\theta\\mid x]\\)</li>" +
         "<li>A compact, information-rich summary</li>" +
         "<li>Gaussian \\(\\Rightarrow\\) mean is <b>sufficient</b> \\(\\Rightarrow\\) <span class='c-ok'>lossless</span></li>" +
       "</ul>",
    3: "<ul class='ns-bul'>" +
         "<li>But the mean is <b>not always sufficient</b></li>" +
         "<li>Same mean, different shape \\(\\Rightarrow\\) same summary</li>" +
         "<li>The <span class='c-mse'>non-Gaussian</span> information is lost</li>" +
       "</ul>"
  };
  RegressionEngine.prototype._stateForAct = function (a) {
    return { suff: a >= 2 ? 1 : 0, twin: a >= 3 ? 1 : 0 };
  };
  RegressionEngine.prototype._frame = function () {
    var moving = tweenStep(this.cur, this.tgt, ["suff", "twin"], 0.12);
    this._draw(); if (moving) requestAnimationFrame(this._loop); else this.running = false;
  };
  RegressionEngine.prototype._draw = function () {
    var cv = this.plot, ctx = cv.getContext("2d"), W = cv._w, H = cv._h, st = this.cur;
    ctx.setTransform(cv._dpr, 0, 0, cv._dpr, 0, 0); ctx.clearRect(0, 0, W, H);
    faintFrame(ctx, W, H);
    var cx = W * 0.5, cy = H * 0.52, sx = W * 0.135, sy = H * 0.125;
    // acts 1-2: a single (Gaussian) posterior; the mean is the summary, and it
    // is a sufficient statistic there, so the compression is lossless.
    drawPosterior(ctx, { cx: cx, cy: cy, sx: sx, sy: sy, bend: 0, rot: 0 }, C_GREY, 1 - st.twin, true);
    if (st.suff > 0.4 && st.twin < 0.5) {
      ctx.save(); ctx.globalAlpha = st.suff * (1 - st.twin);
      clabel(ctx, "Gaussian: mean is sufficient ⇒ lossless", cx, 22, C_OK, 14.5, "center", true);
      ctx.restore();
    }
    // act 3: two posteriors, same mean, different (non-Gaussian) shapes ->
    // the same summary -> the non-Gaussian information is lost.
    if (st.twin > 0.01) {
      drawPosterior(ctx, { cx: cx, cy: cy, sx: sx * 0.95, sy: sy, bend: 0.62, rot: 0 }, C_GREY, st.twin, true);
      drawPosterior(ctx, { cx: cx, cy: cy, sx: sx * 1.15, sy: sy * 0.5, bend: 0, rot: -0.85 }, C_GREY, st.twin, true);
      ctx.save(); ctx.globalAlpha = st.twin;
      clabel(ctx, "two posteriors, same mean", cx, 22, C_INK, 14.5, "center", true);
      ctx.restore();
    }
    // the MSE summary: an amber dot at the mean
    ctx.fillStyle = C_MSE; ctx.beginPath(); ctx.arc(cx, cy, 7, 0, 2 * Math.PI); ctx.fill();
    ctx.lineWidth = 2; ctx.strokeStyle = "#fff"; ctx.stroke();
    var lbl = st.twin > 0.5 ? "same summary t" : (st.suff > 0.5 ? "θ̂ = mean" : "θ̂");
    clabel(ctx, lbl, cx + 13, cy - 16, C_MSE, 15.5, "left", true);
  };

  /* ========================== SLIDE 2 — VMIM ============================= */
  function VmimEngine(root) { setup(this, root); }
  ctrlProto(VmimEngine.prototype);
  VmimEngine.prototype.COPY = {
    1: "<ul class='ns-bul'>" +
         "<li>A network compresses the map to a <b>summary</b> \\(t=f_\\phi(x)\\)</li>" +
         "<li>\\(t\\) is just a code; a flow \\(q_\\psi(\\theta\\mid t)\\) turns it into a posterior</li>" +
         "<li>Both are trained <b>together</b>, rewarded whenever the flow puts high probability on the <b>true</b> \\(\\theta\\)</li>" +
       "</ul>",
    2: "<ul class='ns-bul'>" +
         "<li>So the network learns to keep <b>whatever helps</b> the flow do that</li>" +
         "<li>\\(q_\\psi\\) is pulled onto the true \\(p(\\theta\\mid x)\\), degeneracy and all &mdash; no assumed shape</li>" +
         "<li>That is what \"maximise the information \\(I(t;\\theta)\\)\" means in practice</li>" +
       "</ul>",
    3: "<ul class='ns-bul'>" +
         "<li>At the optimum \\(t\\) is a <b>sufficient statistic</b>: \\(p(\\theta\\mid x)=p(\\theta\\mid t)\\)</li>" +
         "<li>This is the <b>ceiling</b> our comparison is measured against</li>" +
         "<li>Not another statistic &mdash; an estimate of what is extractable</li>" +
       "</ul>"
  };
  VmimEngine.prototype._stateForAct = function (a) {
    return { qbend: a >= 2 ? 1 : 0, suff: a >= 3 ? 1 : 0 };
  };
  VmimEngine.prototype._frame = function () {
    var moving = tweenStep(this.cur, this.tgt, ["qbend", "suff"], 0.12);
    this._draw(); if (moving) requestAnimationFrame(this._loop); else this.running = false;
  };
  VmimEngine.prototype._draw = function () {
    var cv = this.plot, ctx = cv.getContext("2d"), W = cv._w, H = cv._h, st = this.cur;
    ctx.setTransform(cv._dpr, 0, 0, cv._dpr, 0, 0); ctx.clearRect(0, 0, W, H);
    faintFrame(ctx, W, H);
    var cx = W * 0.5, cy = H * 0.5, sx = W * 0.135, sy = H * 0.125;
    var T = { cx: cx, cy: cy, sx: sx, sy: sy, bend: 0.62, rot: 0 };       // true posterior (non-Gaussian)
    drawPosterior(ctx, T, C_GREY, 1, true);
    clabel(ctx, "true p(θ|x)", 42, 22, C_GREY, 14.5, "left", true);
    // q(θ|t): round blob -> matches the banana
    var qb = ease(st.qbend);
    var rR = sx * 0.78;
    var Q = { cx: cx, cy: cy, sx: lerp(rR, sx, qb), sy: lerp(rR, sy, qb), bend: 0.62 * qb, rot: 0 };
    drawPosterior(ctx, Q, C_VMIM, 1, false);
    clabel(ctx, "qψ(θ|t)", cx + sx * 1.05 + 8, cy, C_VMIM, 15, "left", true);
    // act 3: the two curves coincide -> t is sufficient
    if (st.suff > 0.01) { ctx.save(); ctx.globalAlpha = st.suff;
      clabel(ctx, "p(θ|x) = p(θ|t)", cx, H - 30, C_VMIM, 16.5, "center", true);
      clabel(ctx, "sufficient", cx, H - 52, C_OK, 14.5, "center", true);
      ctx.restore(); }
  };

  /* ---- KaTeX auto-render (offline; vendored) ---------------------------- */
  function renderMath(el) {
    if (global.renderMathInElement) {
      try {
        global.renderMathInElement(el, {
          delimiters: [{ left: "\\(", right: "\\)", display: false },
                       { left: "\\[", right: "\\]", display: true }],
          throwOnError: false
        });
      } catch (e) { /* leave raw on failure */ }
    }
  }

  /* ====================== reveal.js integration =========================== */
  var ENGINES = { regression: RegressionEngine, vmim: VmimEngine };
  var NeuralSummaries = {
    _engines: [],
    attach: function (Reveal) {
      var self = this;
      var init = function () {
        var nodes = document.querySelectorAll("[data-ns-explainer]");
        for (var i = 0; i < nodes.length; i++) {
          if (nodes[i]._nsEngine) continue;
          renderMath(nodes[i]);                      // pipeline boxes + objective (static)
          var kind = nodes[i].getAttribute("data-ns-kind") || "regression";
          var eng = new (ENGINES[kind] || RegressionEngine)(nodes[i]);
          nodes[i]._nsEngine = eng;
          self._engines.push({ section: nodes[i], engine: eng });
          self._wireReplay(nodes[i], eng);
        }
        self._sync(Reveal);
      };
      if (Reveal && Reveal.isReady && Reveal.isReady()) init();
      else if (Reveal) Reveal.on("ready", init);
      else document.addEventListener("DOMContentLoaded", init);
      if (Reveal) {
        Reveal.on("fragmentshown",  function () { self._sync(Reveal); });
        Reveal.on("fragmenthidden", function () { self._sync(Reveal); });
        Reveal.on("slidechanged",   function () {
          self._engines.forEach(function (e) { if (e.engine.resize) e.engine.resize(); });
          self._sync(Reveal); });
      }
      document.addEventListener("keydown", function (ev) {
        if (ev.key === "r" || ev.key === "R") { var on = self._cur(Reveal); if (on) on.autoplay(); } });
    },
    _wireReplay: function (s, eng) { var b = s.querySelector(".ns-replay");
      if (b) b.addEventListener("click", function (e) { e.preventDefault(); e.stopPropagation(); eng.autoplay(); }); },
    _cur: function (Reveal) { if (!Reveal) return this._engines[0] && this._engines[0].engine;
      var c = Reveal.getCurrentSlide();
      for (var i = 0; i < this._engines.length; i++) if (this._engines[i].section === c) return this._engines[i].engine;
      return null; },
    _sync: function (Reveal) {
      this._engines.forEach(function (e) {
        var frags = e.section.querySelectorAll(".ns-frag"), shown = 0;
        for (var i = 0; i < frags.length; i++) if (frags[i].classList.contains("visible")) shown += 1;
        e.engine.goTo(1 + shown);
      });
    }
  };
  global.NeuralSummaries = NeuralSummaries;
})(window);
