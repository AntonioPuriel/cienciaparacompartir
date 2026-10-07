// Language toggle (ES/EN). #en or #es in the URL picks the language; otherwise the last choice, then Spanish.
(function () {
  var root = document.documentElement;
  var buttons = document.querySelectorAll('.lang button');
  function setLang(l) {
    root.setAttribute('data-lang', l);
    root.lang = l;
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.set === l)); });
    try { localStorage.setItem('cpc-lang', l); } catch (e) {}
  }
  buttons.forEach(function (b) { b.addEventListener('click', function () { setLang(b.dataset.set); }); });
  var start = 'es';
  if (location.hash === '#en') start = 'en';
  else if (location.hash !== '#es') { try { start = localStorage.getItem('cpc-lang') || 'es'; } catch (e) {} }
  setLang(start === 'en' ? 'en' : 'es');
})();
