/**
 * theme-switch.js — per-slide light/dark backgrounds for the talks decks.
 *
 * The colours are handled entirely in CSS, scoped per <section> (see talks.css).
 * The only thing CSS can't reach is reveal.js's separate slide-background layer,
 * so this script gives each slide a matching background colour from its theme:
 *
 *     <section data-theme="light">  →  light background
 *     <section data-theme="dark">   →  dark background
 *     <section class="light-slide"> →  light background  (legacy alias)
 *
 * It runs ONCE, before Reveal.initialize() reads the backgrounds — so it works
 * in normal view AND in PDF export (every slide keeps its own theme). It is NOT
 * a live toggle: each slide's theme is fixed when you author it.
 *
 * Load at body end, BEFORE the reveal.js library <script>.
 */
(function () {
  var BG = { light: '#f7f5f0', dark: '#15161b' };

  function themeOf(el) {
    if (el.classList && el.classList.contains('light-slide')) { return 'light'; }
    return el.getAttribute('data-theme'); // 'light' | 'dark' | null
  }

  var tops = document.querySelectorAll('.reveal .slides > section');
  for (var i = 0; i < tops.length; i++) {
    var top = tops[i];
    var verticals = top.querySelectorAll(':scope > section');
    var slides = verticals.length ? verticals : [top];
    for (var j = 0; j < slides.length; j++) {
      var slide = slides[j];
      var theme = themeOf(slide) || themeOf(top);
      if (theme && BG[theme] && !slide.hasAttribute('data-background-color')) {
        slide.setAttribute('data-background-color', BG[theme]);
      }
    }
  }
})();
