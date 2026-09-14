/**
 * pipeline.js — the recurring weak-lensing analysis chain.
 *
 * The diagram appears on the thesis-statement slide and again on every act
 * opener with a different stage lit, so it lives ONCE in a <template> and is
 * cloned into each `<div class="pipeline-slot">`.  Edit the template and every
 * copy follows; five hand-maintained copies would drift within a week.
 *
 *   <div class="pipeline-slot" data-active="maps"></div>
 *   <div class="pipeline-slot" data-variant="compact" data-active="summaries"></div>
 *
 * `data-active` takes one or more stage ids, space separated:
 *   catalogue · shear · maps · summaries · inference · posterior
 * Omit it for the neutral state (nothing lit, nothing dimmed).
 *
 * Runs synchronously at load, before Reveal.initialize, so the clones are in
 * the DOM before reveal indexes slides and before the KaTeX pass on 'ready'.
 * (The template deliberately carries no math, so that ordering is belt and
 * braces rather than load-bearing.)
 */
(function () {
	'use strict';

	/**
	 * Naming two adjacent stages means the step BETWEEN them, not two separate
	 * boxes — so the arrow joining them stays lit too. Done by walking the DOM
	 * rather than by authoring arrow ids, so `data-active="shear maps"` just
	 * works and there is nothing extra to keep in sync in the template.
	 */
	function lightTransitions(pipe, cls) {
		cls = cls || 'is-active';
		var kids = Array.prototype.slice.call(pipe.children);
		kids.forEach(function (node, i) {
			if (!node.classList.contains('arw')) { return; }
			var prev = kids[i - 1], next = kids[i + 1];
			if (prev && next &&
			    prev.classList.contains(cls) &&
			    next.classList.contains(cls)) {
				node.classList.add(cls);
			}
		});
	}

	/**
	 * `data-steps` — several focus sets on ONE diagram, walked by clicks.
	 *
	 *   <span class="qstep s1 fragment" data-fragment-index="2"></span>
	 *   ...
	 *   <div class="pipeline-slot"
	 *        data-steps="shear maps | maps | summaries inference | summaries systematics">
	 *
	 * Step k marks its stages (and the arrows between adjacent ones) with `on-k`;
	 * which step is showing is decided in CSS off reveal's own `.current-fragment`
	 * on the matching `.qstep` marker.  Doing it in CSS rather than on a
	 * `fragmentshown` listener is what keeps ?print-pdf correct — the PDF export
	 * sets `visible`/`current-fragment` directly and fires no fragment events.
	 */
	function markSteps(pipe, spec) {
		var sets = spec.split('|');
		sets.forEach(function (set, i) {
			var cls = 'on-' + (i + 1);
			set.split(/\s+/).filter(Boolean).forEach(function (id) {
				var el = pipe.querySelector('[data-stage="' + id + '"]');
				if (el) { el.classList.add(cls); }
				else if (window.console) {
					console.warn('[pipeline] step ' + (i + 1) + ': no stage "' + id + '"');
				}
			});
			lightTransitions(pipe, cls);
		});
		pipe.classList.add('steps-armed');
	}

	function build() {
		var tpl = document.getElementById('wl-pipeline');
		if (!tpl || !tpl.content) { return; }

		var slots = document.querySelectorAll('.pipeline-slot');
		Array.prototype.forEach.call(slots, function (slot) {
			if (slot.dataset.pipelineDone) { return; }

			var frag = tpl.content.cloneNode(true);
			var pipe = frag.querySelector('.pipeline');
			if (!pipe) { return; }

			pipe.classList.add('pipeline--' + (slot.dataset.variant || 'full'));

			// Two ways to focus a pipeline:
			//   data-active="..."            -> focused from the moment the slide opens
			//   data-focus-on-fragment="..." -> stages are MARKED now, but the dimming is
			//                                  held until a .pipe-focus fragment earlier in
			//                                  the same section becomes visible. The switch
			//                                  is done in CSS, keyed on reveal's own
			//                                  `.visible` class, so it survives ?print-pdf —
			//                                  a JS listener on `fragmentshown` would not,
			//                                  because print-pdf never fires it.
			if (slot.dataset.steps) { markSteps(pipe, slot.dataset.steps); }

			var active = (slot.dataset.active || '').split(/\s+/).filter(Boolean);
			var deferred = false;
			if (!active.length && slot.dataset.focusOnFragment) {
				active = slot.dataset.focusOnFragment.split(/\s+/).filter(Boolean);
				deferred = true;
			}
			if (active.length) {
				pipe.classList.add(deferred ? 'focus-armed' : 'is-focused');
				active.forEach(function (id) {
					var el = pipe.querySelector('[data-stage="' + id + '"]');
					if (el) { el.classList.add('is-active'); }
					else if (window.console) {
						console.warn('[pipeline] no stage "' + id + '" in the template');
					}
				});
				lightTransitions(pipe);
			}

			slot.appendChild(frag);
			slot.dataset.pipelineDone = '1';
		});
	}

	/**
	 * The flowchart (<template id="wl-chart">), same idea as the chain: cloned into
	 * every `.chart-slot`.  Elements carry data-key, wires carry data-key="a-b".
	 *   data-steps="a b | c d e"  -> on-1, on-2 … (one set per .qstep click)
	 *   data-focus="a b c"        -> is-lit (shown when a .pipe-focus fragment is visible)
	 * A wire lights when both of its ends are in the set.
	 */
	function buildCharts() {
		var tpl = document.getElementById('wl-chart');
		if (!tpl || !tpl.content) { return; }
		var slots = document.querySelectorAll('.chart-slot');
		Array.prototype.forEach.call(slots, function (slot) {
			if (slot.dataset.chartDone) { return; }
			var frag = tpl.content.cloneNode(true);
			var chart = frag.querySelector('.chart');
			if (!chart) { return; }
			// Arrowheads as plain triangles at the end of each wire, added here rather
			// than as SVG markers: markers are referenced by id, the chart is cloned
			// several times, and a marker on a hidden slide does not render.  Paths use
			// M / H / V only, so the end direction is read off the last two points.
			Array.prototype.forEach.call(chart.querySelectorAll('.wires path.w'), function (w) {
				var d = w.getAttribute('d') || '', x = 0, y = 0, px = 0, py = 0;
				var re = /([MHV])\s*(-?[\d.]+)(?:[\s,]+(-?[\d.]+))?/g, t;
				while ((t = re.exec(d))) {
					px = x; py = y;
					if (t[1] === 'M') { x = +t[2]; y = +t[3]; }
					else if (t[1] === 'H') { x = +t[2]; }
					else { y = +t[2]; }
				}
				var L = 13, W = 6, pts;
				if (y === py) { var sx = x > px ? 1 : -1; pts = [[x, y], [x - sx * L, y - W], [x - sx * L, y + W]]; }
				else { var sy = y > py ? 1 : -1; pts = [[x, y], [x - W, y - sy * L], [x + W, y - sy * L]]; }
				var head = document.createElementNS('http://www.w3.org/2000/svg', 'path');
				head.setAttribute('class', w.getAttribute('class') + ' hd');
				head.setAttribute('d', 'M' + pts.map(function (p) { return p[0] + ' ' + p[1]; }).join(' L') + ' Z');
				head.dataset.key = w.dataset.key;
				w.parentNode.insertBefore(head, w.nextSibling);
			});
			function mark(set, cls) {
				var keys = set.split(/\s+/).filter(Boolean);
				keys.forEach(function (k) {
					var el = chart.querySelector('.el[data-key="' + k + '"]');
					if (el) { el.classList.add(cls); }
					else if (window.console) { console.warn('[chart] no element "' + k + '"'); }
				});
				Array.prototype.forEach.call(chart.querySelectorAll('.wires .w'), function (w) {
					var ends = (w.dataset.key || '').split('-');
					if (keys.indexOf(ends[0]) >= 0 && keys.indexOf(ends[1]) >= 0) { w.classList.add(cls); }
				});
			}
			if (slot.dataset.steps) {
				slot.dataset.steps.split('|').forEach(function (set, i) { mark(set, 'on-' + (i + 1)); });
			}
			if (slot.dataset.focus) { mark(slot.dataset.focus, 'is-lit'); }
			slot.appendChild(frag);
			slot.dataset.chartDone = '1';
		});
	}

	function buildAll() { build(); buildCharts(); }

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', buildAll);
	} else {
		buildAll();
	}
})();
