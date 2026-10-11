"""Inserta (o actualiza) el bloque «Serie: disruptores endocrinos» en las páginas de la serie.
Se ejecuta desde la raíz del repo, después de los generadores."""
import re, os
NB = '&nbsp;'
def t(es, en, fr): return f'<span class="es">{es}</span><span class="en">{en}</span><span class="fr">{fr}</span>'
SERIE = [
    ('ciencia-salud/disruptores-endocrinos', t('Ciencia y salud', 'Science and health', 'Science et santé'),
     t('¿Por qué hay una caída de la testosterona?', 'Why is testosterone falling?', f'Pourquoi la testostérone baisse-t-elle{NB}?'),
     t('En tu cuerpo', 'In your body', 'Dans votre corps')),
    ('ciencia-ambiente/disruptores-agua', t('Ciencia y ambiente', 'Science and environment', 'Science et environnement'),
     t('Disruptores endocrinos: ¿ya están en el agua?', 'Endocrine disruptors: are they already in the water?', f'Perturbateurs endocriniens{NB}: sont-ils déjà dans l’eau{NB}?'),
     t('En el agua', 'In the water', 'Dans l’eau')),
    ('ciencia-tecnologia/pfas-destruccion', t('Ciencia y tecnología', 'Science and technology', 'Science et technologie'),
     t('¿Se pueden destruir los PFAS?', 'Can PFAS be destroyed?', f'Peut-on détruire les PFAS{NB}?'),
     t('Qué podemos hacer', 'What we can do', 'Ce qu’on peut faire')),
]
HERE = t('Estás aquí', 'You are here', 'Vous êtes ici')

def block(current):
    items = []
    for i, (path, cat, title, angle) in enumerate(SERIE, 1):
        rel = os.path.relpath(path, current) + '/'
        thumb = f'<img src="{rel}story-es.png" alt="" width="40" height="71" loading="lazy">'
        txt = f'<span><span class="cat-name">{i} · {cat} · {angle}</span><span class="t">{title}'
        if path == current:
            items.append(f'      <li class="here"><div aria-current="page">{thumb}{txt}<span class="here-tag">{HERE}</span></span></span></div></li>')
        else:
            items.append(f'      <li><a href="{rel}">{thumb}{txt}</span></span></a></li>')
    return ('  <!-- serie:disruptores -->\n  <nav class="serie" aria-label="Serie">\n'
            f'    <p class="serie-label">{t("Serie: disruptores endocrinos", "Series: endocrine disruptors", "Série : perturbateurs endocriniens")}</p>\n'
            '    <ol>\n' + '\n'.join(items) + '\n    </ol>\n  </nav>\n  <!-- /serie:disruptores -->\n')

for path, *_ in SERIE:
    f = f'{path}/index.html'
    s = open(f).read()
    s = re.sub(r'  <!-- serie:disruptores -->.*?<!-- /serie:disruptores -->\n', '', s, flags=re.S)
    assert s.count('  </header>\n') == 1, f
    s = s.replace('  </header>\n', '  </header>\n\n' + block(path), 1)
    open(f, 'w').write(s)
    print('ok', f)
