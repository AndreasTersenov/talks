/* ===========================================================================
 * BNT explainer — "shadows of a rotating cloud"
 * ---------------------------------------------------------------------------
 * One self-contained reveal.js slide that makes ONE effect intuitive:
 *
 *   Why does the BNT transform collapse the wavelet ell-1 norm's figure of
 *   merit (even with cross-maps) while leaving the CNN essentially lossless?
 *
 * The mechanism is the one proven in
 *   scripts/sbi/results/exploratory/flatsky_cross_2026_06/BNT_THEORY_DEEP_DIVE.md (§1)
 *   FLATSKY_BNT_RESULT.md
 * and summarised in HANDOFF_BNT_VIZ_TALK.md (§1 beats, §2 traps, §4 numbers).
 *
 * The picture (all five beats, in order):
 *   1. Four maps -> a fixed cloud of pixels in channel-space. A per-channel
 *      ell-1 is the cloud's SHADOW on one axis. The cloud is elongated along a
 *      "deep common mode" (the bins are deep, overlapping, redundant), so the
 *      original map axes both have a big projection on it -> rich shadows.
 *   2. BNT RE-ORIENTS the measuring axes off the long direction (it is an
 *      invertible *shear*, not a rotation -- the genuine rotation is the
 *      whitening Q). The new per-map axes point across the cloud, onto thin,
 *      signal-poor slices with amplified/correlated noise -> the shadows go
 *      blank. FoM3 falls to 0.26x. THE CLOUD ITSELF NEVER MOVES.
 *   3. The cosmology lives in the cloud's SHAPE -- the relations between maps.
 *      In this frame no single-map histogram can see it.
 *   4. The CNN mixes channels in its first layer, so it can draw its own axis
 *      back along the cloud (undo B for free) -> rich again, FoM3 ~ 0.96x.
 *      It is BASIS-ROBUST, not "smarter."
 *   5. Whitening rotates to a DIFFERENT clean frame -> the per-map shadows are
 *      rich again -> FoM3 recovers to 1.06x. Nothing was lost; the collapse
 *      was the BNT frame itself. (The irreducibly-joint share is ~ 0.)
 *
 * Traps avoided (HANDOFF §2): info is never destroyed (cloud fixed all acts);
 * the CNN is basis-robust, not stronger; the loss is a frame effect that
 * whitening fully reverses (NOT "irreducibly joint"); the lead cause is the
 * axes pointing onto signal-poor directions (geometry), with amplified noise
 * a secondary contributor -- not "noise washing out peaks."
 *
 * No build step, no external dependencies. Pure <canvas> + a little DOM, driven
 * by reveal's fragment events. Works dropped into any reveal.js deck.
 * ======================================================================== */
(function (global) {
  "use strict";

  /* ---- Locked palette (Wong, colourblind-safe; see TALK_BEST_PRACTICES.md) --
   * COLOUR encodes METHOD only: CNN = blue, L1 = vermillion. It never doubles
   * as a basis indicator. */
  var C_L1   = "#D55E00";   // ell-1 (wavelet)        -- Wong vermillion
  var C_CNN  = "#0072B2";   // CNN (VMIM)             -- Wong blue
  var C_INK  = "#1b2733";   // primary text / strokes
  var C_MUTE = "#7d8893";   // secondary
  var C_DEEP = "#1d6f5c";   // "deep common mode" guide (Wong-ish bluish green)
  var C_CLOUD = "#39516b";  // cloud points
  var C_PEAK  = "#d9a200";  // non-Gaussian peaks (rare high-kappa pixels)

  /* ---- Quantitative anchors (HANDOFF_BNT_VIZ_TALK.md §4) --------------------
   * Ratios are the arm-comparable headline (FoM3 is fragile -> ratio-led).
   * Absolute pairs are quoted only for the matched ell-1+product / CNN arms;
   * whitening is the L1-auto recovery ratio. */
  var FOM = {
    l1_nobnt_ratio: 1.00, l1_nobnt_abs: 3045,
    l1_bnt_ratio:   0.26, l1_bnt_abs:   779,    // 779/3045 = 0.256
    l1_whiten_ratio: 1.06,                      // L1-auto, M3
    cnn_nobnt_abs: 3326, cnn_bnt_ratio: 0.96, cnn_bnt_abs: 3186
  };

  /* ---- Toy geometry knobs (stylised; tuned to MATCH the proven behaviour) ---
   * Math convention: angles in degrees, y points UP (flipped at draw time).
   * The cloud's long "deep mode" sits at DEEP_DEG. */
  var DEEP_DEG = 45;        // cloud elongation direction
  var N_POINTS = 1300;
  var N_BINS   = 40;        // matches the pipeline's 40 SNR bins
  var HMIN = -3.0, HMAX = 4.6;   // fixed shadow-histogram range (scene units)
  var NOISE_SCALE = 0.30;        // base per-channel shape-noise std (scene units)

  var DEG = Math.PI / 180;

  /* Per-act target state. axes = the two per-map measuring axes (angle in deg,
   * n = shape-noise amplification of that channel). The collapse is driven by
   * BOTH small projection on the deep mode (axes ~ across the cloud) AND
   * amplified noise (n>1) -- exactly "signal-poor slice under amplified noise."
   * Whitening returns CLEAN noise (n=1) on a genuinely different orthogonal
   * frame; the CNN axis lies along the deep mode. */
  var ACTS = {
    1: { axes: [{ a:   0, n: 1.0 }, { a:  90, n: 1.0 }], cnn: 0, joint: 0.00, kmorph: 0,
         active: "l1" },
    2: { axes: [{ a: 118, n: 1.7 }, { a: 152, n: 1.8 }], cnn: 0, joint: 0.00, kmorph: 1,
         active: "l1" },
    3: { axes: [{ a: 118, n: 1.7 }, { a: 152, n: 1.8 }], cnn: 0, joint: 1.00, kmorph: 1,
         active: "l1" },
    4: { axes: [{ a: 118, n: 1.7 }, { a: 152, n: 1.8 }], cnn: 1, joint: 0.30, kmorph: 1,
         active: "cnn" },
    5: { axes: [{ a:  20, n: 1.0 }, { a: 110, n: 1.0 }], cnn: 0, joint: 0.00, kmorph: 1,
         active: "l1" }
  };
  var N_ACTS = 5;

  /* Captions + meter copy per act (talk-ready; concise). */
  var ACT_COPY = {
    1: { cap: "Four tomographic maps = one <b>cloud of pixels</b> in channel-space. " +
              "The <span class='c-l1'>ℓ1-norm</span> of a map is the cloud's " +
              "<b>shadow</b> on that axis. The cloud is stretched along a " +
              "<span class='c-deep'>deep common mode</span> (the bins are deep and " +
              "overlapping), so both shadows are <b>rich</b>.",
         ratio: "1.00×", abs: "FoM₃ 3045  ·  ℓ1 + product", marg: "" },
    2: { cap: "<b>BNT re-orients the measuring axes</b> off the deep mode, onto thin, " +
              "signal-poor slices (with amplified, correlated noise). The shadows " +
              "<b>flatten toward noise</b> — FoM₃ collapses to 0.26×. " +
              "<b>The cloud hasn't moved.</b>",
         ratio: "0.26×", abs: "3045 → 779", marg: "σ(σ₈) +65%  (calibrated loss)" },
    3: { cap: "So where did it go? The cosmology lives in the cloud's <b>shape</b> — " +
              "the <b>relations between maps</b>. In this frame, no single-map " +
              "histogram can see it.",
         ratio: "0.26×", abs: "3045 → 779", marg: "info is intact — just off-axis" },
    4: { cap: "The <span class='c-cnn'>CNN mixes channels first</span>, so it can draw " +
              "<b>its own axis back along the cloud</b> (undo B for free) — rich again, " +
              "FoM₃ ≈ 0.96×. <b>Basis-robust, not “smarter.”</b>",
         ratio: "0.96×", abs: "3326 → 3186  ·  CNN", marg: "channel-mixing ⇒ frame-agnostic" },
    5: { cap: "<b>Whitening</b> rotates to a <b>different clean frame</b> — the per-map " +
              "shadows come back, FoM₃ recovers to <b>1.06×</b>. " +
              "Nothing was lost; the collapse was the <b>frame</b>.",
         ratio: "1.06×", abs: "fully recovered", marg: "σ(σ₈) back to no-BNT  ·  any sane frame feeds the ℓ1" }
  };

  /* ===================== deterministic toy cloud ========================== */
  function mulberry32(seed) {
    return function () {
      seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
      var t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function gaussian(rng) {            // Box-Muller
    var u = 1 - rng(), v = rng();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  }

  /* Each pixel is a latent {L, S, noise}:
   *   L = coordinate along the deep mode -- SKEWED with a heavy positive tail
   *       (the non-Gaussian peaks: rare high-convergence pixels / clusters).
   *   S = coordinate across the deep mode -- small, near-Gaussian.
   *   noise = a fixed standard-normal draw, scaled at render time by the
   *           current axis's noise amplification (so the shadow broadens
   *           smoothly without shimmering).
   * The cosmological information lives in the deep-mode skew (L); projecting
   * across the deep mode (BNT axes) removes it. */
  function buildCloud() {
    var rng = mulberry32(20260615);
    var pts = [], peakThresh = 1.9;
    for (var i = 0; i < N_POINTS; i++) {
      var base = gaussian(rng) * 1.00;
      // heavy positive tail ~15% of the time -> non-Gaussian peaks along L
      var tail = (rng() < 0.16) ? Math.pow(rng(), 0.55) * 3.2 : 0;
      var L = base + tail - 0.45;          // recentre so the bulk sits near 0
      var S = gaussian(rng) * 0.34;        // thin across-mode spread
      pts.push({ L: L, S: S, noise: gaussian(rng), peak: (L > peakThresh) });
    }
    return pts;
  }

  /* ============================ the engine ================================ */
  function Engine(root) {
    this.root = root;
    this.cloudCanvas = root.querySelector(".bnt-cloud");
    this.kernCanvas  = root.querySelector(".bnt-kernels");
    this.meterEl     = root.querySelector(".bnt-meter");
    this.captionEl   = root.querySelector(".bnt-caption");
    this.kernCapEl   = root.querySelector(".bnt-kernels-caption");
    this.cloud = buildCloud();

    this.cur = this._stateForAct(1);   // animated state
    this.tgt = this._stateForAct(1);   // target state
    this.act = 1;
    this.running = false;
    this.autoTimer = null;

    this._buildMeter();
    this._applyCopy(1);
    this._setupCanvas(this.cloudCanvas);
    this._setupCanvas(this.kernCanvas);

    var self = this;
    this._loop = function () { self._frame(); };
    window.addEventListener("resize", function () {
      self._setupCanvas(self.cloudCanvas);
      self._setupCanvas(self.kernCanvas);
    });
  }

  /* Flatten an act into a tweenable numeric state. */
  Engine.prototype._stateForAct = function (act) {
    var A = ACTS[act];
    return {
      a1: A.axes[0].a * DEG, n1: A.axes[0].n,
      a2: A.axes[1].a * DEG, n2: A.axes[1].n,
      cnn: A.cnn, joint: A.joint, kmorph: A.kmorph,
      l1ratio:  (act >= 5) ? FOM.l1_whiten_ratio
              : (act >= 2) ? FOM.l1_bnt_ratio : FOM.l1_nobnt_ratio,
      cnnratio: FOM.cnn_bnt_ratio,
      cnnShow:  (act === 4) ? 1 : (act === 5 ? 0.45 : 0),
      active:   A.active
    };
  };

  Engine.prototype._setupCanvas = function (canvas) {
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var rect = canvas.getBoundingClientRect();
    // Fall back to the attribute size before first layout.
    var cssW = rect.width  || (canvas.width  / 2);
    var cssH = rect.height || (canvas.height / 2);
    canvas._cssW = cssW; canvas._cssH = cssH; canvas._dpr = dpr;
    canvas.width  = Math.round(cssW * dpr);
    canvas.height = Math.round(cssH * dpr);
  };

  /* ----------------------------- control --------------------------------- */
  Engine.prototype.goTo = function (act) {
    act = Math.max(1, Math.min(N_ACTS, act));
    this.act = act;
    this.tgt = this._stateForAct(act);
    this._applyCopy(act);
    this.start();
  };

  Engine.prototype.snapTo = function (act) {   // jump with no animation
    this.cur = this._stateForAct(act);
    this.goTo(act);
  };

  Engine.prototype.start = function () {
    if (!this.running) { this.running = true; requestAnimationFrame(this._loop); }
  };

  Engine.prototype.autoplay = function () {
    var self = this;
    if (this.autoTimer) { clearInterval(this.autoTimer); this.autoTimer = null; }
    this.snapTo(1);
    var act = 1;
    this.autoTimer = setInterval(function () {
      act += 1;
      if (act > N_ACTS) { clearInterval(self.autoTimer); self.autoTimer = null; return; }
      self.goTo(act);
    }, 2500);
  };

  /* ------------------------------ tween ---------------------------------- */
  Engine.prototype._frame = function () {
    var c = this.cur, t = this.tgt, k, moving = false;
    var SMOOTH = 0.12;
    var keys = ["a1", "n1", "a2", "n2", "cnn", "joint", "kmorph",
                "l1ratio", "cnnratio", "cnnShow"];
    for (var i = 0; i < keys.length; i++) {
      k = keys[i];
      var d = t[k] - c[k];
      if (Math.abs(d) > 1e-4) { c[k] += d * SMOOTH; moving = true; }
      else { c[k] = t[k]; }
    }
    c.active = t.active;

    this._drawCloud();
    this._drawKernels();
    this._updateMeter();

    if (moving) { requestAnimationFrame(this._loop); }
    else { this.running = false; }
  };

  /* ============================ cloud panel =============================== */
  Engine.prototype._drawCloud = function () {
    var canvas = this.cloudCanvas, ctx = canvas.getContext("2d");
    var W = canvas._cssW, H = canvas._cssH, dpr = canvas._dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);

    var cx = W * 0.46, cy = H * 0.52;
    var SC = Math.min(W, H) * 0.115;     // scene unit -> px

    // math (x,y up) -> screen
    function P(mx, my) { return [cx + mx * SC, cy - my * SC]; }

    var dHat = [Math.cos(DEEP_DEG * DEG), Math.sin(DEEP_DEG * DEG)];
    var pHat = [Math.cos((DEEP_DEG + 90) * DEG), Math.sin((DEEP_DEG + 90) * DEG)];

    // --- deep-mode guide line (faint, persistent) ---
    var gl = 3.7;
    var g0 = P(-gl * dHat[0], -gl * dHat[1]), g1 = P(gl * dHat[0], gl * dHat[1]);
    ctx.save();
    ctx.setLineDash([6, 6]); ctx.lineWidth = 1.5; ctx.strokeStyle = hexA(C_DEEP, 0.55);
    ctx.beginPath(); ctx.moveTo(g0[0], g0[1]); ctx.lineTo(g1[0], g1[1]); ctx.stroke();
    ctx.restore();
    // deep-mode label
    var lp = P(gl * dHat[0], gl * dHat[1]);
    label(ctx, "deep common mode", lp[0] + 6, lp[1] - 6, C_DEEP, "left", 13, true);

    // --- joint density highlight (act 3): the cloud's shape holds the info ---
    if (this.cur.joint > 0.01) {
      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(-DEEP_DEG * DEG);            // screen y-down => negative angle
      var grad = ctx.createRadialGradient(0, 0, 4, 0, 0, SC * 3.4);
      grad.addColorStop(0, hexA(C_DEEP, 0.30 * this.cur.joint));
      grad.addColorStop(1, hexA(C_DEEP, 0));
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.ellipse(SC * 0.5, 0, SC * 3.2, SC * 0.95, 0, 0, 2 * Math.PI);
      ctx.fill();
      ctx.restore();
    }

    // --- the cloud of points (cosmology-fixed; identical every act) ---
    for (var i = 0; i < this.cloud.length; i++) {
      var pt = this.cloud[i];
      var mx = pt.L * dHat[0] + pt.S * pHat[0];
      var my = pt.L * dHat[1] + pt.S * pHat[1];
      var s = P(mx, my);
      if (pt.peak) {
        ctx.fillStyle = hexA(C_PEAK, 0.95);
        ctx.beginPath(); ctx.arc(s[0], s[1], 2.6, 0, 2 * Math.PI); ctx.fill();
      } else {
        ctx.fillStyle = hexA(C_CLOUD, 0.5);
        ctx.beginPath(); ctx.arc(s[0], s[1], 1.7, 0, 2 * Math.PI); ctx.fill();
      }
    }

    // --- the two per-map measuring axes + their shadows ---
    var axColor = C_L1;   // these axes are always the per-map (ell-1) axes
    this._drawAxisAndShadow(ctx, P, cx, cy, SC, this.cur.a1, this.cur.n1, +1, axColor, "map i");
    this._drawAxisAndShadow(ctx, P, cx, cy, SC, this.cur.a2, this.cur.n2, -1, axColor, "map j");

    // --- the CNN's own axis along the deep mode (act 4) ---
    if (this.cur.cnn > 0.01) {
      ctx.save();
      ctx.globalAlpha = this.cur.cnn;
      this._drawAxisAndShadow(ctx, P, cx, cy, SC, DEEP_DEG * DEG, 1.0, +1, C_CNN,
                              "CNN axis", true);
      ctx.restore();
    }
  };

  /* Draw one measuring axis (arrow through the centre) and the histogram
   * "shadow" of the cloud projected onto it. side = +1/-1 chooses which
   * perpendicular side the ribbon sits on (keeps the two shadows apart). */
  Engine.prototype._drawAxisAndShadow = function (ctx, P, cx, cy, SC, ang, noiseAmp,
                                                   side, color, name, isCNN) {
    var uHat = [Math.cos(ang), Math.sin(ang)];
    var perp = [Math.cos(ang + side * 90 * DEG), Math.sin(ang + side * 90 * DEG)];

    // axis line through centre
    var L = 3.4;
    var aEnd = P(L * uHat[0], L * uHat[1]);
    var aBeg = P(-L * uHat[0], -L * uHat[1]);
    ctx.save();
    ctx.lineWidth = isCNN ? 3.0 : 2.2;
    ctx.strokeStyle = hexA(color, isCNN ? 0.95 : 0.85);
    ctx.beginPath(); ctx.moveTo(aBeg[0], aBeg[1]); ctx.lineTo(aEnd[0], aEnd[1]); ctx.stroke();
    // arrowhead at positive end
    arrowHead(ctx, aEnd, ang, color);
    ctx.restore();

    // --- the shadow histogram ---
    var hist = this._projectHistogram(ang, noiseAmp);

    /* "Richness" = how much of the cosmology-bearing deep-mode skew survives
     * the projection, divided by the channel's noise amplification. It drives
     * the shadow's height AND opacity, so a BNT (across-cloud, amplified-noise)
     * axis renders as low + pale + bland, while a deep-aligned, clean axis
     * renders as tall + solid + skewed. Monotone in the faithful quantity. */
    var skewSurv = Math.abs(Math.cos(ang - DEEP_DEG * DEG));   // 1 along deep mode
    var rich = Math.max(0, Math.min(1, skewSurv / noiseAmp));
    var heightScale = SC * (0.5 + 2.05 * rich) / hist.refPeak;
    var standoff = SC * 1.65;
    var opacity = 0.14 + 0.46 * rich;          // capped so the cloud shows through

    var nb = hist.counts.length;
    var basePts = [], topPts = [];
    for (var b = 0; b < nb; b++) {
      var s = HMIN + (b + 0.5) / nb * (HMAX - HMIN);
      var along = s;                          // scene units along the axis
      var bx = cx + (uHat[0] * along * SC) + perp[0] * standoff;
      var by = cy - (uHat[1] * along * SC) - perp[1] * standoff;   // y flip
      var h = hist.counts[b] * heightScale;
      basePts.push([bx, by]);
      topPts.push([bx + perp[0] * h, by - perp[1] * h]);
    }

    ctx.save();
    // baseline
    ctx.lineWidth = 1; ctx.strokeStyle = hexA(color, 0.35);
    ctx.beginPath(); ctx.moveTo(basePts[0][0], basePts[0][1]);
    for (var j = 1; j < basePts.length; j++) ctx.lineTo(basePts[j][0], basePts[j][1]);
    ctx.stroke();
    // filled histogram area
    ctx.beginPath();
    ctx.moveTo(basePts[0][0], basePts[0][1]);
    for (var k = 0; k < topPts.length; k++) ctx.lineTo(topPts[k][0], topPts[k][1]);
    for (var m = basePts.length - 1; m >= 0; m--) ctx.lineTo(basePts[m][0], basePts[m][1]);
    ctx.closePath();
    ctx.fillStyle = hexA(color, opacity);
    ctx.fill();
    ctx.lineWidth = 1.6; ctx.strokeStyle = hexA(color, Math.min(1, opacity + 0.25));
    ctx.beginPath();
    ctx.moveTo(topPts[0][0], topPts[0][1]);
    for (var q = 1; q < topPts.length; q++) ctx.lineTo(topPts[q][0], topPts[q][1]);
    ctx.stroke();

    // axis name near the ribbon's far end
    var nm = basePts[Math.round(nb * 0.86)];
    label(ctx, name, nm[0] + perp[0] * 14, nm[1] - perp[1] * 14, color, "center", 13, true);
    ctx.restore();
  };

  /* Histogram of (deep-mode-skewed signal projected on the axis) + amplified
   * shape noise. refPeak (the no-BNT peak count) is cached so all shadows share
   * ONE global height scale -- collapsed shadows are genuinely shorter. */
  Engine.prototype._projectHistogram = function (ang, noiseAmp) {
    var cs = Math.cos(ang - DEEP_DEG * DEG);          // weight on L (deep skew)
    var cp = Math.cos(ang - (DEEP_DEG + 90) * DEG);   // weight on S (across)
    var nb = N_BINS, counts = new Array(nb).fill(0);
    for (var i = 0; i < this.cloud.length; i++) {
      var pt = this.cloud[i];
      var s = pt.L * cs + pt.S * cp + pt.noise * NOISE_SCALE * noiseAmp;
      var b = Math.floor((s - HMIN) / (HMAX - HMIN) * nb);
      if (b >= 0 && b < nb) counts[b] += 1;
    }
    // light 3-tap smoothing for a clean curve
    var sm = counts.slice();
    for (var j = 1; j < nb - 1; j++) sm[j] = (counts[j-1] + 2*counts[j] + counts[j+1]) / 4;

    if (this._refPeak == null) {     // calibrate once on the no-BNT axis
      var p = 0; for (var r = 0; r < nb; r++) if (sm[r] > p) p = sm[r];
      this._refPeak = p || 1;
    }
    return { counts: sm, refPeak: this._refPeak };
  };

  /* ============================ kernel inset ============================== */
  /* Four broad, heavily-overlapping lensing kernels n(z) (no-BNT) morph into
   * 1 broad map + 3 thin lens-redshift slices (BNT) -- the physical reason the
   * cloud is elongated (deep shared field) and the nulled axes are signal-poor.
   * kmorph in [0,1] interpolates. Colours are a neutral sequential ramp so they
   * never read as the method colours. */
  Engine.prototype._drawKernels = function () {
    var canvas = this.kernCanvas, ctx = canvas.getContext("2d");
    var W = canvas._cssW, H = canvas._cssH, dpr = canvas._dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);

    var m = this.cur.kmorph;
    var padL = 30, padR = 8, padT = 8, padB = 22;
    var x0 = padL, x1 = W - padR, y0 = H - padB, yTop = padT;
    var zMin = 0, zMax = 2.0;
    function X(z) { return x0 + (z - zMin) / (zMax - zMin) * (x1 - x0); }
    function Y(v) { return y0 - v * (y0 - yTop); }    // v in [0,1]

    // axis
    ctx.strokeStyle = hexA(C_MUTE, 0.7); ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y0); ctx.stroke();
    label(ctx, "z", x1 - 4, y0 + 15, C_MUTE, "right", 12, false);

    // four kernels: broad overlapping (m=0) -> 1 broad + 3 thin shells (m=1)
    var broadMu = [0.45, 0.70, 0.98, 1.30], broadW = 0.46;
    var thinNu  = [0.45, 0.78, 1.12, 1.48];
    var thinW   = [0.42, 0.085, 0.085, 0.085];   // kernel 0 stays broad (kept map)
    var ramp = ["#c7d3df", "#9fb2c6", "#6f88a6", "#42607f"];

    for (var i = 0; i < 4; i++) {
      var mu = broadMu[i] + (thinNu[i] - broadMu[i]) * m;
      var w  = broadW + (thinW[i] - broadW) * m;
      // area-preserving-ish: thin shells get taller
      var amp = (0.62) * (broadW / w) * 0.62;
      amp = Math.min(amp, 1.0);
      var amp0 = 0.62;
      amp = amp0 + (amp - amp0) * m;

      ctx.beginPath();
      var started = false;
      for (var px = x0; px <= x1; px += 2) {
        var z = zMin + (px - x0) / (x1 - x0) * (zMax - zMin);
        var v = amp * Math.exp(-((z - mu) * (z - mu)) / (2 * w * w));
        var yy = Y(v);
        if (!started) { ctx.moveTo(px, yy); started = true; } else { ctx.lineTo(px, yy); }
      }
      ctx.lineTo(x1, y0); ctx.lineTo(x0, y0); ctx.closePath();
      ctx.fillStyle = hexA(ramp[i], 0.38);
      ctx.fill();
      ctx.strokeStyle = hexA(ramp[i], 0.95); ctx.lineWidth = 1.6;
      ctx.beginPath();
      started = false;
      for (var px2 = x0; px2 <= x1; px2 += 2) {
        var z2 = zMin + (px2 - x0) / (x1 - x0) * (zMax - zMin);
        var v2 = amp * Math.exp(-((z2 - mu) * (z2 - mu)) / (2 * w * w));
        var yy2 = Y(v2);
        if (!started) { ctx.moveTo(px2, yy2); started = true; } else { ctx.lineTo(px2, yy2); }
      }
      ctx.stroke();
    }

    var capNo = "deep, overlapping kernels (redundant)";
    var capYes = "1 broad map + 3 thin slices (signal-poor)";
    if (this.kernCapEl) this.kernCapEl.innerHTML = (m < 0.5) ? capNo : capYes;
  };

  /* ============================== meter =================================== */
  Engine.prototype._buildMeter = function () {
    this.meterEl.innerHTML =
      '<div class="bnt-meter-title">FoM₃ &nbsp;/&nbsp; no-BNT</div>' +
      '<div class="bnt-meter-plot">' +
        '<div class="bnt-bars">' +
          '<div class="bnt-baseline"><span>1.00×</span></div>' +
          '<div class="bnt-bar bnt-bar--l1">' +
            '<div class="bnt-bar-fill"></div>' +
            '<div class="bnt-bar-ratio"></div>' +
            '<div class="bnt-bar-name">ℓ1</div>' +
          '</div>' +
          '<div class="bnt-bar bnt-bar--cnn">' +
            '<div class="bnt-bar-fill"></div>' +
            '<div class="bnt-bar-ratio"></div>' +
            '<div class="bnt-bar-name">CNN</div>' +
          '</div>' +
        '</div>' +
      '</div>' +
      '<div class="bnt-meter-abs"></div>' +
      '<div class="bnt-meter-marg"></div>';
    this._m = {
      l1Fill:  this.meterEl.querySelector(".bnt-bar--l1 .bnt-bar-fill"),
      l1Ratio: this.meterEl.querySelector(".bnt-bar--l1 .bnt-bar-ratio"),
      cnnBar:  this.meterEl.querySelector(".bnt-bar--cnn"),
      cnnFill: this.meterEl.querySelector(".bnt-bar--cnn .bnt-bar-fill"),
      cnnRatio:this.meterEl.querySelector(".bnt-bar--cnn .bnt-bar-ratio"),
      abs:     this.meterEl.querySelector(".bnt-meter-abs"),
      marg:    this.meterEl.querySelector(".bnt-meter-marg"),
      baseline:this.meterEl.querySelector(".bnt-baseline")
    };
    // baseline at 1.00x within a 0..1.2 range
    this._m.baseline.style.bottom = (1.00 / 1.20 * 100) + "%";
  };

  Engine.prototype._updateMeter = function () {
    var RMAX = 1.20;
    var l1 = this.cur.l1ratio, cnn = this.cur.cnnratio, show = this.cur.cnnShow;
    this._m.l1Fill.style.height = (Math.min(l1, RMAX) / RMAX * 100) + "%";
    this._m.l1Ratio.textContent = l1.toFixed(2) + "×";
    this._m.cnnFill.style.height = (Math.min(cnn, RMAX) / RMAX * 100) + "%";
    this._m.cnnRatio.textContent = cnn.toFixed(2) + "×";
    this._m.cnnBar.style.opacity = show;
    // de-emphasise whichever method isn't active
    this._m.l1Fill.style.filter  = (this.cur.active === "l1")  ? "none" : "saturate(0.55)";
  };

  /* ============================ captions ================================= */
  Engine.prototype._applyCopy = function (act) {
    var c = ACT_COPY[act];
    if (!c) return;
    this.captionEl.innerHTML =
      '<span class="bnt-actno">' + act + '/5</span>' + c.cap;
    this._m.abs.innerHTML = c.abs;
    this._m.marg.innerHTML = c.marg;
  };

  /* ============================ helpers =================================== */
  function hexA(hex, a) {
    if (hex[0] !== "#") return hex;
    var r = parseInt(hex.substr(1, 2), 16),
        g = parseInt(hex.substr(3, 2), 16),
        b = parseInt(hex.substr(5, 2), 16);
    return "rgba(" + r + "," + g + "," + b + "," + a + ")";
  }
  function label(ctx, text, x, y, color, align, size, bold) {
    ctx.save();
    ctx.fillStyle = color;
    ctx.textAlign = align || "left";
    ctx.textBaseline = "middle";
    ctx.font = (bold ? "600 " : "400 ") + (size || 13) +
               "px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif";
    ctx.fillText(text, x, y);
    ctx.restore();
  }
  function arrowHead(ctx, tip, ang, color) {
    var s = 9;
    ctx.save();
    ctx.fillStyle = color;
    ctx.translate(tip[0], tip[1]);
    ctx.rotate(-ang);            // canvas y-down vs math y-up
    ctx.beginPath();
    ctx.moveTo(0, 0); ctx.lineTo(-s, -s * 0.5); ctx.lineTo(-s, s * 0.5);
    ctx.closePath(); ctx.fill();
    ctx.restore();
  }

  /* ====================== reveal.js integration =========================== */
  var BNTExplainer = {
    _engines: [],

    attach: function (Reveal) {
      var self = this;
      var init = function () {
        var nodes = document.querySelectorAll("[data-bnt-explainer]");
        for (var i = 0; i < nodes.length; i++) {
          if (nodes[i]._bntEngine) continue;
          var eng = new Engine(nodes[i]);
          nodes[i]._bntEngine = eng;
          self._engines.push({ section: nodes[i], engine: eng });
          self._wireReplay(nodes[i], eng);
        }
        self._syncFromReveal(Reveal);
      };

      if (Reveal && Reveal.isReady && Reveal.isReady()) { init(); }
      else if (Reveal) { Reveal.on("ready", init); }
      else { document.addEventListener("DOMContentLoaded", init); }

      if (Reveal) {
        Reveal.on("fragmentshown",  function () { self._syncFromReveal(Reveal); });
        Reveal.on("fragmenthidden", function () { self._syncFromReveal(Reveal); });
        Reveal.on("slidechanged",   function () {
          // re-measure canvases (reveal lays the slide out on entry) then sync
          self._engines.forEach(function (e) {
            e.engine._setupCanvas(e.engine.cloudCanvas);
            e.engine._setupCanvas(e.engine.kernCanvas);
          });
          self._syncFromReveal(Reveal);
        });
      }
      // 'R' replays the active slide's animation
      document.addEventListener("keydown", function (ev) {
        if (ev.key === "r" || ev.key === "R") {
          var on = self._currentEngine(Reveal);
          if (on) on.autoplay();
        }
      });
    },

    _wireReplay: function (section, eng) {
      var btn = section.querySelector(".bnt-replay");
      if (btn) btn.addEventListener("click", function (e) {
        e.preventDefault(); e.stopPropagation(); eng.autoplay();
      });
    },

    _currentEngine: function (Reveal) {
      if (!Reveal) return this._engines.length ? this._engines[0].engine : null;
      var cur = Reveal.getCurrentSlide();
      for (var i = 0; i < this._engines.length; i++) {
        if (this._engines[i].section === cur) return this._engines[i].engine;
      }
      return null;
    },

    // Current act = 1 + number of visible bnt fragments on the active slide.
    _syncFromReveal: function (Reveal) {
      this._engines.forEach(function (e) {
        var frags = e.section.querySelectorAll(".bnt-frag");
        var shown = 0;
        for (var i = 0; i < frags.length; i++) {
          if (frags[i].classList.contains("visible")) shown += 1;
        }
        e.engine.goTo(1 + shown);
      });
    }
  };

  global.BNTExplainer = BNTExplainer;
})(window);
