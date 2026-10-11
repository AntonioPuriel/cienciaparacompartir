"""Genera ciencia-ambiente/disruptores-agua/index.html (ES/EN/FR) con la misma plantilla que los temas de salud."""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None

def t(es, en, fr):
    return f'<span class="es">{es}</span><span class="en">{en}</span><span class="fr">{fr}</span>'

CHIPS = {
    'meta': t('Síntesis', 'Synthesis', 'Synthèse'),
    'obs': t('Observacional', 'Observational', 'Observationnelle'),
    'rct': t('Experimento', 'Experiment', 'Expérience'),
    'lab': t('Laboratorio', 'Lab', 'Laboratoire'),
    'rev': t('Revisión', 'Review', 'Revue'),
    'db': t('Modelo', 'Model', 'Modèle'),
}
OLD = t('Anterior a 2020', 'Pre-2020', 'Avant 2020')

def ref(cite, title, finding, chips, doi, old=False, url=None):
    chip_html = ''.join(f'<span class="chip {c}">{CHIPS[c]}</span>' for c in chips)
    if old:
        chip_html += f'<span class="chip rev">{OLD}</span>'
    link = f'<a class="doi" href="{url}">{doi}</a>' if url else f'<a class="doi" href="https://doi.org/{doi}">doi.org/{doi}</a>'
    return f'''    <article class="ref">
      <p class="cite">{cite}</p>
      <p class="title">{title}</p>
      <p class="finding">{finding}</p>
      <div class="meta">{chip_html}{link}</div>
    </article>'''

def section(h, body, note=None):
    n = f'\n    <p class="note">{note}</p>' if note else ''
    return f'''  <section>
    <div class="frame"><h2>{h}</h2></div>
{body}{n}
  </section>
'''

HORIZON = '''<div class="horizon" aria-hidden="true">
  <div class="sun"></div>
  <svg class="cactus c1" viewBox="0 0 60 100"><g fill="none" stroke="currentColor" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"><path d="M30 100 V10"/><path d="M30 58 H12 V34"/><path d="M30 46 H47 V18"/></g></svg>
  <svg class="cactus c2" viewBox="0 0 60 100"><g fill="none" stroke="currentColor" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"><path d="M30 100 V10"/><path d="M30 58 H12 V34"/><path d="M30 46 H47 V18"/></g></svg>
  <svg viewBox="0 0 1080 120" preserveAspectRatio="none"><path d="M0 52 C200 18 380 26 560 52 S900 78 1080 40 L1080 120 L0 120 Z" fill="var(--dune1)"></path><path d="M0 80 C180 56 360 60 520 80 S860 100 1080 70 L1080 120 L0 120 Z" fill="var(--dune2)"></path><path d="M0 104 C220 88 420 94 620 104 S900 112 1080 98 L1080 120 L0 120 Z" fill="var(--dune3)"></path></svg>
</div>'''

