// Botones para guardar una sola imagen del tema: la story o la tabla de fuentes, en el idioma elegido.
// En el iPhone abre el menú de compartir («Guardar imagen», Instagram…); en la computadora la descarga.
(function () {
  var preview = document.querySelector('img.preview');
  if (!preview) return;
  var root = document.documentElement;
  var T = {
    story: { es: 'Guardar story', en: 'Save story', fr: 'Enregistrer la story' },
    fuentes: { es: 'Guardar fuentes', en: 'Save sources', fr: 'Enregistrer les sources' },
    hint: { es: 'Una imagen, en el idioma elegido arriba.', en: 'One image, in the language chosen above.', fr: 'Une image, dans la langue choisie en haut.' },
    wait: { es: 'Preparando…', en: 'Preparing…', fr: 'Préparation…' }
  };
  function tri(o) {
    return '<span class="es">' + o.es + '</span><span class="en">' + o.en + '</span><span class="fr">' + o.fr + '</span>';
  }
  function lang() { return root.getAttribute('data-lang') || 'es'; }
  var slug = location.pathname.replace(/\/index\.html$/, '/').split('/').filter(Boolean).pop() || 'tema';

  function save(kind, btn) {
    var l = lang();
    var name = kind + '-' + l + '.png';
    var label = btn.innerHTML;
    btn.disabled = true;
    btn.textContent = T.wait[l];
    fetch(name).then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.blob();
    }).then(function (blob) {
      var file = new File([blob], slug + '-' + name, { type: 'image/png' });
      if (navigator.canShare && navigator.canShare({ files: [file] })) {
        return navigator.share({ files: [file] }).catch(function () {});
      }
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = file.name;
      document.body.appendChild(a);
      a.click();
      setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
    }).catch(function () {
      location.href = name; // si algo falla, abre la imagen sola
    }).then(function () {
      btn.disabled = false;
      btn.innerHTML = label;
    });
  }

  var box = document.createElement('div');
  box.className = 'save';
  box.innerHTML = '<div class="save-row">' +
    '<button type="button" data-kind="story">' + tri(T.story) + '</button>' +
    '<button type="button" data-kind="fuentes">' + tri(T.fuentes) + '</button>' +
    '</div><p>' + tri(T.hint) + '</p>';
  preview.insertAdjacentElement('afterend', box);
  box.querySelectorAll('button').forEach(function (b) {
    b.addEventListener('click', function () { save(b.dataset.kind, b); });
  });
  // Sin imagen de fuentes todavía: quita ese botón.
  fetch('fuentes-es.png', { method: 'HEAD' }).then(function (r) {
    if (!r.ok) box.querySelector('[data-kind="fuentes"]').remove();
  }).catch(function () {});
})();
