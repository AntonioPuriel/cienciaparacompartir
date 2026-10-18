"""Inserta (o actualiza) el bloque «Serie: intestino» en las tres páginas de la serie.
Se ejecuta desde la raíz del repo, después de los generadores. Es idempotente."""
import re, os
NB = '&nbsp;'
def t(es, en, fr): return f'<span class="es">{es}</span><span class="en">{en}</span><span class="fr">{fr}</span>'
SERIE = [
    ('ciencia-salud/inflamacion-intestinal',
     t('Intestino inflamado, microbiota empobrecida', 'Inflamed gut, depleted microbiota', f'Intestin enflammé, microbiote appauvri'),
     t('El bucle', 'The loop', 'La boucle')),
    ('ciencia-salud/oxigeno-intestino',
     t('Oxígeno en tu intestino: ¿cuándo sí y cuándo no?', 'Oxygen in your gut: when yes and when no?', f'L’oxygène dans ton intestin{NB}: quand oui et quand non{NB}?'),
     t('La clave: el oxígeno', 'The key: oxygen', 'La clé : l’oxygène')),
    ('ciencia-salud/dieta-inflamacion',
     t('¿Qué comida inflama tu colon y cuál lo calma?', 'Which foods inflame your colon and which calm it?', f'Quels aliments enflamment ton côlon et lesquels l’apaisent{NB}?'),
     t('Qué comer', 'What to eat', 'Quoi manger')),
]
HERE = t('Estás aquí', 'You are here', 'Vous êtes ici')
OPEN, CLOSE = '  <!-- serie:intestino -->', '<!-- /serie:intestino -->'

def block(current):
    items = []
    for i, (path, title, angle) in enumerate(SERIE, 1):
        rel = os.path.relpath(path, current) + '/'
        thumb = f'<img src="{rel}story-es.png" alt="" width="40" height="71" loading="lazy">'
        txt = f'<span><span class="cat-name">{i} · {angle}</span><span class="t">{title}'
        if path == current:
            items.append(f'      <li class="here"><div aria-current="page">{thumb}{txt}<span class="here-tag">{HERE}</span></span></span></div></li>')
        else:
            items.append(f'      <li><a href="{rel}">{thumb}{txt}</span></span></a></li>')
    return (f'{OPEN}\n  <nav class="serie" aria-label="Serie">\n'
            f'    <p class="serie-label">{t("Serie: intestino", "Series: the gut", "Série : l’intestin")}</p>\n'
            '    <ol>\n' + '\n'.join(items) + f'\n    </ol>\n  </nav>\n  {CLOSE}\n')

for path, *_ in SERIE:
    f = f'{path}/index.html'
    s = open(f).read()
    s = re.sub(re.escape(OPEN) + r'.*?' + re.escape(CLOSE) + r'\n', '', s, flags=re.S)
    assert s.count('  </header>\n') == 1, f
    s = s.replace('  </header>\n', '  </header>\n\n' + block(path), 1)
    open(f, 'w').write(s)
    print('ok', f)
