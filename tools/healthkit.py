"""Piezas comunes para las páginas de fuentes de salud generadas por script (oxígeno, dieta).
Reutiliza t(), section() y HORIZON de pagekit y añade las etiquetas de evidencia de salud."""
from pagekit import t, section, HORIZON

CH = {
    'meta': ('meta', t('Síntesis', 'Synthesis', 'Synthèse')),
    'gui': ('db', t('Guía', 'Guideline', 'Recommandation')),
    'rct': ('rct', t('Ensayo', 'Trial', 'Essai')),
    'obs': ('obs', t('Observacional', 'Observational', 'Observationnelle')),
    'lab': ('lab', t('Ratón', 'Mice', 'Souris')),
    'rev': ('rev', t('Revisión', 'Review', 'Revue')),
}
OLD = t('Anterior a 2020', 'Pre-2020', 'Avant 2020')

LEGEND_ITEMS = {
    'meta': t('Revisión sistemática o metaanálisis: reúne todos los estudios sobre la misma pregunta.',
              'Systematic review or meta-analysis: gathers all the studies on the same question.',
              'Revue systématique ou méta-analyse : rassemble toutes les études sur la même question.'),
    'gui': t('Recomendación de una sociedad médica o un panel de expertos, basada en la evidencia disponible.',
             'Recommendation from a medical society or expert panel, based on the available evidence.',
             'Recommandation d’une société médicale ou d’un panel d’experts, fondée sur les preuves disponibles.'),
    'rct': t('Ensayo aleatorizado en personas: puede demostrar causa y efecto.',
             'Randomized trial in people: can show cause and effect.',
             'Essai randomisé chez l’humain : peut montrer une relation de cause à effet.'),
    'obs': t('Estudio en personas que muestra asociación, no causa.',
             'Study in people that shows association, not cause.',
             'Étude chez l’humain qui montre une association, pas une cause.'),
    'lab': t('Experimento en animales: explica un mecanismo, pero no prueba que ocurra igual en personas.',
             'Animal experiment: explains a mechanism, but doesn’t prove it works the same way in people.',
             'Expérience animale : explique un mécanisme, sans prouver qu’il fonctionne de la même façon chez l’humain.'),
    'rev': t('Síntesis narrativa de mecanismos a partir de estudios celulares, animales y humanos.',
             'Narrative synthesis of mechanisms from cell, animal and human studies.',
             'Synthèse narrative de mécanismes à partir d’études cellulaires, animales et humaines.'),
}


def legend(keys, old=True):
    rows = ''.join(f'\n    <p><span class="chip {CH[k][0]}">{CH[k][1]}</span><span>{LEGEND_ITEMS[k]}</span></p>' for k in keys)
    if not old:
        return f'  <div class="legend">{rows}\n  </div>\n'
    old = f'\n    <p><span class="chip rev">{OLD}</span><span>{t("Estudio de antes de 2020: lo citamos cuando sigue siendo la referencia original del hallazgo.", "Study from before 2020: cited when it is still the original reference for the finding.", "Étude antérieure à 2020 : citée quand elle reste la référence originale du résultat.")}</span></p>'
    return f'  <div class="legend">{rows}{old}\n  </div>\n'


def ref(cite, title, finding, chips, doi=None, url=None, label=None, old=False):
    chip_html = ''.join(f'<span class="chip {CH[c][0]}">{CH[c][1]}</span>' for c in chips)
    if old:
        chip_html += f'<span class="chip rev">{OLD}</span>'
    link = (f'<a class="doi" href="{url}">{label}</a>' if url
            else f'<a class="doi" href="https://doi.org/{doi}">doi.org/{doi}</a>')
    return f'''    <article class="ref">
      <p class="cite">{cite}</p>
      <p class="title">{title}</p>
      <p class="finding">{finding}</p>
      <div class="meta">{chip_html}{link}</div>
    </article>'''


def page(*, title_tag, description, h1, lede, legend_html, sections, alt, footer):
    html = f'''<!doctype html>
<html lang="es" data-lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_tag} · Ciencia para compartir</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=DM+Sans:wght@400;500;700&display=swap">
<link rel="stylesheet" href="../../assets/style.css">
</head>
<body>
{HORIZON}

<main class="wrap">
  <header>
    <div class="top">
      <a class="eyebrow" href="../">{t('← Ciencia y salud', '← Science and health', '← Science et santé')}</a>
      <div class="lang" role="group" aria-label="Idioma / Language / Langue">
        <button type="button" id="btn-es" data-set="es" aria-pressed="true">ES</button>
        <button type="button" id="btn-en" data-set="en" aria-pressed="false">EN</button>
        <button type="button" id="btn-fr" data-set="fr" aria-pressed="false">FR</button>
      </div>
    </div>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <p class="reviewed">{t('Evidencia revisada: oct 2026', 'Evidence reviewed: Oct 2026', 'Preuves revues : oct. 2026')}</p>
  </header>

{legend_html}
{''.join(sections)}
  <section>
    <div class="frame"><h2>{t('La story', 'The story', 'La story')}</h2></div>
    <img class="preview" src="preview.png" alt="{alt}" width="1600" height="900" loading="lazy">
  </section>

  <footer>
    <p>{footer}</p>
    <p>Antonio Puriel Hernández · <a href="../../">{t('Ciencia para compartir', 'Science to share', 'La science à partager')}</a> · <a href="../">{t('Más temas', 'More topics', 'Plus de sujets')}</a></p>
  </footer>
</main>
<script src="../../assets/lang.js"></script>
</body>
</html>
'''
    return html.replace(' %', '&nbsp;%')
