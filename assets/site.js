/* Casuta din copac — animatii subtile la scroll. Enhancement pur.
   - respecta prefers-reduced-motion
   - aplica .rv DOAR pe blocuri aflate sub fold la incarcare => fara flash,
     iar elementele de sus raman normale (vizibile imediat)
   - fara JS (PDF/print) nu se intampla nimic: continutul ramane intact */
(function () {
  try {
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var run = function () {
      var sel = 'section, article, .card, .grp, .joint, .pcard, .step, .gc, .shotband, .gallery';
      var blocks = document.querySelectorAll(sel);
      if (!blocks.length) return;
      var hasIO = 'IntersectionObserver' in window;
      var io = hasIO ? new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
        });
      }, { rootMargin: '0px 0px -7% 0px', threshold: 0.05 }) : null;
      var vh = window.innerHeight || document.documentElement.clientHeight;
      blocks.forEach(function (el) {
        // doar blocurile de sub fold primesc animatia (fara flash pe ce e deja vizibil)
        if (io && el.getBoundingClientRect().top > vh * 0.86) {
          el.classList.add('rv');
          io.observe(el);
        }
      });
    };
    if (document.readyState !== 'loading') run();
    else document.addEventListener('DOMContentLoaded', run);
  } catch (e) { /* enhancement — daca pica ceva, pagina ramane intacta */ }
})();
