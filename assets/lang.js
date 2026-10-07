// Language toggle (ES/EN/FR). #es, #en or #fr in the URL picks the language; otherwise the last choice, then Spanish.
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
  var langs = ['es', 'en', 'fr'];
  var start = location.hash.slice(1);
  if (langs.indexOf(start) < 0) { try { start = localStorage.getItem('cpc-lang') || 'es'; } catch (e) { start = 'es'; } }
  setLang(langs.indexOf(start) < 0 ? 'es' : start);
})();
