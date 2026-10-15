"""Genera las tres páginas de la serie «estrés hídrico» (ES/EN/FR), con el bloque «Serie» incluido.
Uso (desde tools/): python3 build_hidrico_pages.py"""
import os, re, pathlib
from pagekit import HORIZON

ROOT = pathlib.Path(__file__).resolve().parent.parent
NB = ' '

def frfix(s):
    s = re.sub(r' ([:;?!])', NB + r'\1', s)
    return s.replace('« ', '«' + NB).replace(' »', NB + '»')

def t(es, en, fr):
    return f'<span class="es">{es}</span><span class="en">{en}</span><span class="fr">{frfix(fr)}</span>'

CH = {
    'meta': ('meta', t('Síntesis', 'Synthesis', 'Synthèse')),
    'ma': ('meta', t('Metaanálisis', 'Meta-analysis', 'Méta-analyse')),
    'rev': ('rev', t('Revisión', 'Review', 'Revue')),
    'ag': ('rev', t('Agencia', 'Agency', 'Agence')),
    'obs': ('obs', t('Medición', 'Measurement', 'Mesures')),
    'db': ('db', t('Modelo', 'Model', 'Modèle')),
    'co': ('lab', t('Empresa', 'Company', 'Entreprise')),
    'pr': ('lab', t('Prensa', 'Press', 'Presse')),
    'old': ('rev', t('Anterior a 2020', 'Pre-2020', 'Avant 2020')),
}
LEG = {
    'meta': t('Síntesis de expertos o de un organismo internacional sobre lo publicado.', 'Synthesis of the published work by experts or an international body.', 'Synthèse des travaux publiés par des experts ou un organisme international.'),
    'ma': t('Combina los resultados de muchos estudios.', 'Pools the results of many studies.', 'Combine les résultats de nombreuses études.'),
    'rev': t('Revisión de lo publicado.', 'Review of the published work.', 'Revue des travaux publiés.'),
    'ag': t('Datos o informe de una agencia pública.', 'Data or report from a public agency.', 'Données ou rapport d’une agence publique.'),
    'obs': t('Datos medidos: pozos, satélites o torres de medición.', 'Measured data: wells, satellites or flux towers.', 'Données mesurées : puits, satellites ou tours de mesure.'),
    'db': t('Estimación calculada: depende de sus supuestos.', 'Calculated estimate: depends on its assumptions.', 'Estimation calculée : dépend de ses hypothèses.'),
    'co': t('Cifras publicadas por la propia empresa, sin revisión por pares.', 'Figures published by the company itself, not peer reviewed.', 'Chiffres publiés par l’entreprise elle-même, sans relecture par les pairs.'),
    'pr': t('Periodismo que recoge datos de otras fuentes: útil para el contexto, no como prueba.', 'Journalism compiling data from other sources: useful context, not proof.', 'Journalisme qui compile des données d’autres sources : utile pour le contexte, pas comme preuve.'),
    'old': t('Anterior a 2020: se usa porque es el trabajo de referencia.', 'Pre-2020: used because it is the reference work.', 'Avant 2020 : utilisé car c’est le travail de référence.'),
}

def ref(cite, title, finding, chips, doi=None, url=None, label=None):
    chip_html = ''.join(f'<span class="chip {CH[c][0]}">{CH[c][1]}</span>' for c in chips)
    link = f'<a class="doi" href="{url}">{label}</a>' if url else f'<a class="doi" href="https://doi.org/{doi}">doi.org/{doi}</a>'
    return f'''    <article class="ref">
      <p class="cite">{cite}</p>
      <p class="title">{title}</p>
      <p class="finding">{finding}</p>
      <div class="meta">{chip_html}{link}</div>
    </article>'''

def section(h, refs, note):
    return f'''  <section>
    <div class="frame"><h2>{h}</h2></div>
{chr(10).join(refs)}
    <p class="note">{note}</p>
  </section>
'''

def row(where, what, status, links):
    a = ' · '.join(f'<a href="{u}">{n}</a>' for n, u in links)
    cls, label = status
    return f'        <tr><td>{where}</td><td>{what} {a}</td><td><span class="st {cls}">{label}</span></td></tr>'

OK = ('ok', t('Vigente', 'In force', 'En vigueur'))
NOBIND = ('part', t('No vinculante', 'Non-binding', 'Non contraignant'))

def reg(intro, rows):
    return f'''  <section>
    <div class="frame"><h2>{t('Regulación en Europa y América', 'Regulation in Europe and the Americas', 'Réglementation en Europe et en Amérique')}</h2></div>
    <p class="note">{intro}</p>
    <div class="reg-wrap">
    <table class="reg">
      <thead><tr><th>{t('Dónde', 'Where', 'Où')}</th><th>{t('Qué', 'What', 'Quoi')}</th><th>{t('Estado', 'Status', 'Statut')}</th></tr></thead>
      <tbody>
{chr(10).join(rows)}
      </tbody>
    </table>
    </div>
  </section>
'''

UE = t('Unión Europea', 'European Union', 'Union européenne')
ES = t('España', 'Spain', 'Espagne')
FR = t('Francia', 'France', 'France')
MX = t('México', 'Mexico', 'Mexique')
CL = t('Chile', 'Chile', 'Chili')
US = t('EE. UU.', 'US', 'États-Unis')

# ---------------------------------------------------------------- serie
SERIE = [
    ('ciencia-ambiente/estres-hidrico', t('Ciencia y ambiente', 'Science and environment', 'Science et environnement'),
     t('Estrés hídrico: ¿nos estamos quedando sin agua?', 'Water stress: are we running out of water?', 'Stress hydrique : sommes-nous en train de manquer d’eau ?'),
     t('El problema', 'The problem', 'Le problème')),
    ('ciencia-tecnologia/ahorro-agua', t('Ciencia y tecnología', 'Science and technology', 'Science et technologie'),
     t('Estrés hídrico: ¿cómo se ahorra agua en el campo y la industria?', 'Water stress: how do farms and industry save water?', 'Stress hydrique : comment économiser l’eau aux champs et dans l’industrie ?'),
     t('Qué podemos hacer', 'What we can do', 'Ce qu’on peut faire')),
    ('ciencia-tecnologia/centros-datos-agua', t('Ciencia y tecnología', 'Science and technology', 'Science et technologie'),
     t('IA y centros de datos: ¿cuánta agua beben?', 'AI and data centres: how much water do they drink?', 'IA et centres de données : combien d’eau boivent-ils ?'),
     t('Un consumo nuevo', 'A new demand', 'Une nouvelle demande')),
]
HERE = t('Estás aquí', 'You are here', 'Vous êtes ici')

def serie_block(current):
    items = []
    for i, (path, cat, title, angle) in enumerate(SERIE, 1):
        rel = os.path.relpath(path, current) + '/'
        thumb = f'<img src="{rel}story-es.png" alt="" width="40" height="71" loading="lazy">'
        txt = f'<span><span class="cat-name">{i} · {cat} · {angle}</span><span class="t">{title}'
        if path == current:
            items.append(f'      <li class="here"><div aria-current="page">{thumb}{txt}<span class="here-tag">{HERE}</span></span></span></div></li>')
        else:
            items.append(f'      <li><a href="{rel}">{thumb}{txt}</span></span></a></li>')
    return ('  <!-- serie:hidrico -->\n  <nav class="serie" aria-label="Serie">\n'
            f'    <p class="serie-label">{t("Serie: estrés hídrico", "Series: water stress", "Série : stress hydrique")}</p>\n'
            '    <ol>\n' + '\n'.join(items) + '\n    </ol>\n  </nav>\n  <!-- /serie:hidrico -->\n')

# ---------------------------------------------------------------- página
def page(path, cat_back, title_html, title_plain, desc, lede, chips_used, sections, regsec, alt, footer_extra):
    legend = '  <div class="legend">\n' + '\n'.join(
        f'    <p><span class="chip {CH[c][0]}">{CH[c][1]}</span><span>{LEG[c]}</span></p>' for c in chips_used) + '\n  </div>\n'
    html = f'''<!doctype html>
<html lang="es" data-lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_plain} · Ciencia para compartir</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=DM+Sans:wght@400;500;700&display=swap">
<link rel="stylesheet" href="../../assets/style.css">
</head>
<body>
{HORIZON}

<main class="wrap">
  <header>
    <div class="top">
      <a class="eyebrow" href="../">{cat_back}</a>
      <div class="lang" role="group" aria-label="Idioma / Language / Langue">
        <button type="button" id="btn-es" data-set="es" aria-pressed="true">ES</button>
        <button type="button" id="btn-en" data-set="en" aria-pressed="false">EN</button>
        <button type="button" id="btn-fr" data-set="fr" aria-pressed="false">FR</button>
      </div>
    </div>
    <h1>{title_html}</h1>
    <p class="lede">{lede}</p>
    <p class="reviewed">{t('Evidencia revisada: oct 2026', 'Evidence reviewed: Oct 2026', 'Preuves revues : oct. 2026')}</p>
  </header>

{serie_block(path)}
{legend}
{''.join(sections)}{regsec}
  <section>
    <div class="frame"><h2>{t('La story', 'The story', 'La story')}</h2></div>
    <img class="preview" src="preview.png" alt="{alt}" width="1600" height="900" loading="lazy">
  </section>

  <footer>
    <p>{t('Contenido divulgativo; no sustituye el consejo profesional.' + footer_extra[0], 'For general information only; not professional advice.' + footer_extra[1], 'Contenu de vulgarisation ; ne remplace pas un avis professionnel.' + footer_extra[2])}</p>
    <p>Antonio Puriel Hernández · <a href="../../">{t('Ciencia para compartir', 'Science to share', 'La science à partager')}</a> · <a href="../">{t('Más temas', 'More topics', 'Plus de sujets')}</a></p>
  </footer>
</main>
<script src="../../assets/lang.js"></script>
</body>
</html>
'''
    html = html.replace(' %', '&nbsp;%').replace(NB, '&nbsp;')
    out = ROOT / path / 'index.html'
    out.write_text(html)
    print('ok', out.relative_to(ROOT), len(html))

def h1(es, en, fr):
    return t(f'{es} <em>Las fuentes</em>', f'{en} <em>The sources</em>', f'{fr} <em>Les sources</em>')

# ================================================================ 1 · estrés hídrico
S1 = [
section(t('Qué es y a cuánta gente afecta', 'What it is and how many people it affects', 'Ce que c’est et combien de personnes sont touchées'), [
    ref('Kuzma S, Bierkens MFP, Lakshman S, Luo T, Saccoccia L, Sutanudjaja EH, Van Beek R · World Resources Institute, nota técnica · 2023',
        'Aqueduct 4.0: Updated Decision-Relevant Global Water Risk Indicators',
        t('El atlas Aqueduct calcula, cuenca por cuenca, qué parte del agua renovable se extrae cada año: por encima del 40 % el estrés es alto y por encima del 80 %, extremadamente alto. Con datos de 2023, 25 países con una cuarta parte de la población mundial están en estrés extremo cada año, y unos 4000 millones de personas lo viven al menos un mes al año. Para 2050 se suman 1000 millones de personas más en estrés extremo, y el 31 % del PIB mundial quedaría expuesto; India, México, Egipto y Turquía concentran más de la mitad. México está en la categoría de estrés alto; Chile, Bélgica y Grecia, entre los 25 de estrés extremo.',
          'The Aqueduct atlas calculates, basin by basin, how much of the renewable water is withdrawn each year: above 40% stress is high, above 80% extremely high. With 2023 data, 25 countries holding a quarter of the world’s population face extreme stress every year, and about 4 billion people experience it at least one month a year. By 2050, another billion people face extreme stress, and 31% of global GDP would be exposed; India, Mexico, Egypt and Turkey account for more than half. Mexico is in the high-stress category; Chile, Belgium and Greece are among the 25 at extreme stress.',
          'L’atlas Aqueduct calcule, bassin par bassin, la part de l’eau renouvelable prélevée chaque année : au-delà de 40 % le stress est élevé, au-delà de 80 % extrêmement élevé. Avec les données de 2023, 25 pays qui regroupent un quart de la population mondiale sont en stress extrême chaque année, et environ 4 milliards de personnes le vivent au moins un mois par an. D’ici 2050, un milliard de personnes de plus seront en stress extrême, et 31 % du PIB mondial serait exposé ; l’Inde, le Mexique, l’Égypte et la Turquie en concentrent plus de la moitié. Le Mexique est en stress élevé ; le Chili, la Belgique et la Grèce figurent parmi les 25 en stress extrême.'),
        ['ag', 'db'], doi='10.46830/writn.23.00061'),
    ref('UN-Water / FAO · Indicador ODS 6.4.2 · datos 2023',
        'Level of water stress: freshwater withdrawal as a proportion of available freshwater resources',
        t('El indicador oficial de la ONU mide lo mismo a escala de país, descontando el caudal que necesitan los ecosistemas. A escala mundial se extrae en torno al 18 % del agua dulce renovable: la media no parece alarmante porque mezcla regiones con agua de sobra y regiones al límite.',
          'The UN’s official indicator measures the same thing at country level, after setting aside the flow ecosystems need. Globally about 18% of renewable freshwater is withdrawn: the average doesn’t look alarming because it mixes water-rich regions with regions at their limit.',
          'L’indicateur officiel de l’ONU mesure la même chose à l’échelle des pays, après avoir réservé le débit dont les écosystèmes ont besoin. À l’échelle mondiale, environ 18 % de l’eau douce renouvelable est prélevée : la moyenne ne paraît pas alarmante car elle mélange des régions riches en eau et d’autres à la limite.'),
        ['ag'], url='https://www.sdg6data.org/en/indicator/6.4.2', label='sdg6data.org/indicator/6.4.2'),
    ref('Caretta MA, Mukherji A, et al. · IPCC AR6, Grupo de Trabajo II, capítulo 4 · 2022; pp. 551–712',
        'Water. In: Climate Change 2022: Impacts, Adaptation and Vulnerability',
        t('El capítulo del IPCC sobre el agua estima que cerca de la mitad de la población mundial sufre escasez grave al menos parte del año, por causas climáticas y no climáticas (confianza media). Añade dos matices importantes: todavía no se puede cuantificar cuánto ha contribuido el cambio climático a la escasez actual, y el agotamiento de los acuíferos se debe sobre todo al riego intensivo (confianza alta). Hacia el futuro, los factores humanos seguirán dominando.',
          'The IPCC chapter on water estimates that roughly half the world’s population experiences severe scarcity at least part of the year, from climatic and non-climatic causes (medium confidence). It adds two key caveats: climate change’s contribution to today’s scarcity can’t yet be quantified, and aquifer depletion is mainly driven by intensive irrigation (high confidence). Looking ahead, human factors will keep dominating.',
          'Le chapitre du GIEC sur l’eau estime qu’environ la moitié de la population mondiale subit une pénurie grave au moins une partie de l’année, pour des causes climatiques et non climatiques (confiance moyenne). Il ajoute deux nuances importantes : on ne peut pas encore quantifier la contribution du changement climatique à la pénurie actuelle, et l’épuisement des nappes est surtout dû à l’irrigation intensive (confiance élevée). Pour l’avenir, les facteurs humains resteront dominants.'),
        ['meta'], doi='10.1017/9781009325844.006'),
], t('El estrés mide presión sobre el recurso, no falta de agua en el grifo: un país puede estar en estrés extremo y abastecer bien a su población si gestiona, recicla o desaliniza. Las cifras por país esconden cuencas al límite dentro de países sin estrés (Nuevo México en EE. UU., el Cabo Occidental en Sudáfrica). Las proyecciones a 2050 dependen de escenarios de clima y de demanda.',
     'Stress measures pressure on the resource, not a lack of water at the tap: a country can be at extreme stress and still supply its people well if it manages, recycles or desalinates. Country figures hide basins at their limit inside unstressed countries (New Mexico in the US, the Western Cape in South Africa). The 2050 projections depend on climate and demand scenarios.',
     'Le stress mesure une pression sur la ressource, pas un manque d’eau au robinet : un pays peut être en stress extrême et bien approvisionner sa population s’il gère, recycle ou dessale. Les chiffres par pays cachent des bassins à la limite dans des pays sans stress (le Nouveau-Mexique aux États-Unis, le Cap-Occidental en Afrique du Sud). Les projections à 2050 dépendent de scénarios de climat et de demande.')),

section(t('El agua que no vemos: los acuíferos', 'The water we don’t see: aquifers', 'L’eau qu’on ne voit pas : les nappes'), [
    ref('Jasechko S, Seybold H, Perrone D, Fan Y, Shamsudduha M, Taylor RG, Fallatah O, Kirchner JW · Nature · 2024; 625: 715–721',
        'Rapid groundwater decline and some cases of recovery in aquifers globally',
        t('Reunieron medidas de unos 170 000 pozos en 1693 acuíferos de más de 40 países. En el 36 % de los acuíferos el nivel baja más de 10 cm al año, y en el 12 %, más de 50 cm. En el 30 % el descenso se ha acelerado en las últimas cuatro décadas. Los peores casos están bajo cultivos en climas secos. Pero hay recuperaciones documentadas, como Albuquerque o Bangkok, gracias a límites de bombeo, trasvases o el cambio a agua superficial.',
          'They gathered measurements from about 170,000 wells in 1,693 aquifers in more than 40 countries. In 36% of aquifers the level drops more than 10 cm a year, and in 12% more than 50 cm. In 30% the decline has accelerated over the past four decades. The worst cases lie under cropland in dry climates. But recoveries are documented, such as Albuquerque or Bangkok, thanks to pumping limits, water transfers or a switch to surface water.',
          'Ils ont réuni les mesures d’environ 170 000 puits dans 1 693 nappes de plus de 40 pays. Dans 36 % des nappes, le niveau baisse de plus de 10 cm par an, et dans 12 %, de plus de 50 cm. Dans 30 %, la baisse s’est accélérée ces quatre dernières décennies. Les pires cas se trouvent sous les cultures des climats secs. Mais des rétablissements sont documentés, comme à Albuquerque ou Bangkok, grâce à des limites de pompage, des transferts d’eau ou le passage à l’eau de surface.'),
        ['obs'], doi='10.1038/s41586-023-06879-8'),
    ref('Khorrami M, Shirzaei M, Ghobadi-Far K, Werth S, Carlson G, Zhai G · Geophysical Research Letters · 2023; 50(5): e2022GL101962',
        'Groundwater Volume Loss in Mexico City Constrained by InSAR and GRACE Observations and Mechanical Models',
        t('Con radar de satélite (InSAR), que mide cuánto sube o baja el suelo, y con los satélites GRACE, que detectan cambios en la masa de agua, calcularon que partes de la cuenca de México se hunden hasta unos 35 cm al año. La causa principal es el bombeo del acuífero: estiman que desde 2014 se han extraído entre 1 y 13 km³ al año. Las superficies impermeables impiden además que la lluvia recargue el acuífero.',
          'Using satellite radar (InSAR), which measures how much the ground rises or sinks, and the GRACE satellites, which detect changes in water mass, they calculated that parts of the Mexico City basin are sinking by up to about 35 cm a year. The main cause is pumping from the aquifer: they estimate that 1 to 13 km³ have been extracted each year since 2014. Paved surfaces also keep rain from recharging the aquifer.',
          'Avec le radar satellitaire (InSAR), qui mesure de combien le sol monte ou descend, et les satellites GRACE, qui détectent les variations de masse d’eau, ils ont calculé que certaines zones du bassin de Mexico s’enfoncent jusqu’à environ 35 cm par an. La cause principale est le pompage de la nappe : ils estiment qu’entre 1 et 13 km³ ont été extraits chaque année depuis 2014. Les surfaces imperméables empêchent en outre la pluie de recharger la nappe.'),
        ['obs'], doi='10.1029/2022GL101962'),
], t('Los pozos medidos no cubren el mundo por igual: hay muchos datos de EE. UU., Europa e India y pocos de África. En Ciudad de México parte del hundimiento se debe a la compactación de las arcillas del antiguo lago, que no se revierte aunque se deje de bombear.',
     'The wells measured don’t cover the world evenly: there is plenty of data from the US, Europe and India and little from Africa. In Mexico City part of the sinking comes from the compaction of the old lakebed clays, which doesn’t reverse even if pumping stops.',
     'Les puits mesurés ne couvrent pas le monde de façon égale : beaucoup de données pour les États-Unis, l’Europe et l’Inde, peu pour l’Afrique. À Mexico, une partie de l’affaissement vient du tassement des argiles de l’ancien lac, qui ne s’inverse pas même si l’on cesse de pomper.')),

section(t('No solo en el desierto: Europa', 'Not just in deserts: Europe', 'Pas seulement dans le désert : l’Europe'), [
    ref('Agencia Europea de Medio Ambiente (EEA) · indicador WEI+ · 2025',
        'Use of freshwater resources in Europe',
        t('El índice de explotación del agua (WEI+) compara el agua consumida con la renovable disponible, trimestre a trimestre. En 2023, la escasez afectó al 28 % del territorio de la UE y al 32 % de su población; en un año típico, a cerca del 30 % y el 33 %. El sur de Europa concentra los casos, y el riego en primavera y verano es la principal presión.',
          'The water exploitation index (WEI+) compares the water consumed with the renewable water available, quarter by quarter. In 2023 scarcity affected 28% of EU territory and 32% of its population; in a typical year, about 30% and 33%. Southern Europe concentrates the cases, and spring and summer irrigation is the main pressure.',
          'L’indice d’exploitation de l’eau (WEI+) compare l’eau consommée à l’eau renouvelable disponible, trimestre par trimestre. En 2023, la pénurie a touché 28 % du territoire de l’UE et 32 % de sa population ; une année typique, environ 30 % et 33 %. Le sud de l’Europe concentre les cas, et l’irrigation au printemps et en été est la principale pression.'),
        ['ag'], url='https://www.eea.europa.eu/en/analysis/indicators/use-of-freshwater-resources-in-europe-1', label='eea.europa.eu · use of freshwater resources'),
], t('«Afectado al menos un trimestre» no significa todo el año: la escasez en Europa es sobre todo estacional. El índice no mide la calidad del agua, otro problema aparte.',
     '“Affected for at least one quarter” doesn’t mean all year: scarcity in Europe is mostly seasonal. The index doesn’t measure water quality, which is a separate problem.',
     '« Touché au moins un trimestre » ne veut pas dire toute l’année : la pénurie en Europe est surtout saisonnière. L’indice ne mesure pas la qualité de l’eau, un autre problème.')),

section(t('De crisis a «bancarrota hídrica»', 'From crisis to “water bankruptcy”', 'De la crise à la « faillite hydrique »'), [
    ref('Madani K (UNU-INWEH) · Universidad de las Naciones Unidas · enero de 2026',
        'Global Water Bankruptcy: Living Beyond Our Hydrological Means in the Post-Crisis Era',
        t('El informe del instituto del agua de la ONU propone dejar de hablar de «crisis», algo temporal, y hablar de bancarrota: extraer de forma persistente más de lo que se repone, hasta perder capital natural de forma irreversible o muy costosa de recuperar. Reúne datos de otras fuentes: cerca del 70 % de los grandes acuíferos en descenso, más de la mitad de los grandes lagos con menos agua que a principios de los 90, 410 millones de hectáreas de humedales perdidos en cinco décadas y alrededor del 70 % de las extracciones destinadas a la agricultura.',
          'The UN water institute’s report proposes no longer speaking of a “crisis”, which is temporary, but of bankruptcy: persistently withdrawing more than is replenished, until natural capital is lost irreversibly or at very high cost. It compiles data from other sources: about 70% of major aquifers in decline, more than half of large lakes holding less water than in the early 1990s, 410 million hectares of wetlands lost in five decades and around 70% of withdrawals going to agriculture.',
          'Le rapport de l’institut de l’eau de l’ONU propose de ne plus parler de « crise », passagère, mais de faillite : prélever durablement plus que ce qui se renouvelle, jusqu’à perdre du capital naturel de façon irréversible ou très coûteuse. Il compile des données d’autres sources : environ 70 % des grandes nappes en baisse, plus de la moitié des grands lacs avec moins d’eau qu’au début des années 1990, 410 millions d’hectares de zones humides perdus en cinq décennies et environ 70 % des prélèvements destinés à l’agriculture.'),
        ['meta'], doi='10.53328/INR26KAM001'),
    ref('Madani K · Water Resources Management · 2026; 40(2): 78',
        'Water Bankruptcy: The Formal Definition',
        t('El artículo que acompaña al informe define el término con precisión, para que se pueda medir: hay bancarrota cuando la extracción supera de forma sostenida la recarga renovable y los niveles de agotamiento seguros, y el daño ya no se puede revertir a un coste razonable.',
          'The paper accompanying the report defines the term precisely so it can be measured: bankruptcy occurs when withdrawals persistently exceed renewable recharge and safe depletion levels, and the damage can no longer be reversed at reasonable cost.',
          'L’article qui accompagne le rapport définit le terme avec précision, pour qu’il soit mesurable : il y a faillite quand les prélèvements dépassent durablement la recharge renouvelable et les niveaux d’épuisement sûrs, et que les dégâts ne peuvent plus être réparés à un coût raisonnable.'),
        ['rev'], doi='10.1007/s11269-025-04484-0'),
], t('«Bancarrota» es un marco para la gestión, no una medición nueva: el informe recopila datos de otros estudios. No todas las cuencas están en quiebra; el informe pide medir cuáles lo están en lugar de tratar el agua como un problema global uniforme.',
     '“Bankruptcy” is a management framework, not a new measurement: the report compiles data from other studies. Not every basin is bankrupt; the report calls for measuring which ones are, rather than treating water as a uniform global problem.',
     '« Faillite » est un cadre de gestion, pas une nouvelle mesure : le rapport compile des données d’autres études. Tous les bassins ne sont pas en faillite ; le rapport demande de mesurer lesquels le sont plutôt que de traiter l’eau comme un problème mondial uniforme.')),
]

REG1 = reg(t('Ninguna norma limita el estrés hídrico en sí: se regulan el reparto, las prioridades de uso y el caudal mínimo de los ríos. A escala mundial no existe un marco equivalente al del clima; la próxima Conferencia del Agua de la ONU será en Abu Dabi, del 8 al 10 de diciembre de 2026. Qué se hace con la tecnología está en el tema siguiente de la serie.',
             'No rule limits water stress as such: what is regulated is allocation, priorities of use and minimum river flows. Globally there is no framework equivalent to the climate one; the next UN Water Conference will be in Abu Dhabi, 8-10 December 2026. What technology can do is in the next topic of the series.',
             'Aucune règle ne limite le stress hydrique en soi : on réglemente le partage, les priorités d’usage et le débit minimal des rivières. À l’échelle mondiale, il n’existe pas de cadre équivalent à celui du climat ; la prochaine Conférence de l’ONU sur l’eau aura lieu à Abou Dhabi du 8 au 10 décembre 2026. Ce que fait la technologie est dans le sujet suivant de la série.'), [
    row(UE, t('Estrategia Europea de Resiliencia Hídrica (4 de junio de 2025): mejorar la eficiencia en el uso del agua al menos un 10 % para 2030 y reducir fugas. La recomendación de eficiencia deja que cada país fije su objetivo.',
              'European Water Resilience Strategy (4 June 2025): improve water efficiency by at least 10% by 2030 and cut leaks. The efficiency recommendation lets each country set its own target.',
              'Stratégie européenne de résilience hydrique (4 juin 2025) : améliorer l’efficacité de l’usage de l’eau d’au moins 10 % d’ici 2030 et réduire les fuites. La recommandation sur l’efficacité laisse chaque pays fixer son objectif.'),
        NOBIND, [('Comisión Europea', 'https://cyprus.representation.ec.europa.eu/news/commission-launches-strategy-enhance-water-security-people-economy-and-environment-2025-06-04_en')]),
    row(ES, t('Planes hidrológicos del tercer ciclo, 2022-2027 (Real Decreto 35/2023, BOE del 10 de febrero de 2023): fijan caudales ecológicos en los ríos, incluido el Tajo, ligado al trasvase Tajo-Segura.',
              'Third-cycle river basin plans, 2022-2027 (Royal Decree 35/2023, BOE 10 February 2023): set ecological flows in rivers, including the Tagus, linked to the Tagus-Segura transfer.',
              'Plans hydrologiques du troisième cycle, 2022-2027 (décret royal 35/2023, BOE du 10 février 2023) : fixent des débits écologiques dans les rivières, dont le Tage, lié au transfert Tage-Segura.'),
        OK, [('BOE', 'https://www.boe.es/eli/es/rd/2023/01/24/35')]),
    row(FR, t('Plan Eau (2023, 53 medidas): reducir un 10 % el agua extraída para 2030. Es un plan de acción, no una ley.',
              'Plan Eau (2023, 53 measures): cut water withdrawals by 10% by 2030. It is an action plan, not a law.',
              'Plan eau (2023, 53 mesures) : réduire de 10 % l’eau prélevée d’ici 2030. C’est un plan d’action, pas une loi.'),
        ('part', t('Plan, no ley', 'Plan, not law', 'Plan, pas une loi')), [('info.gouv.fr', 'https://www.info.gouv.fr/grand-dossier/preservons-notre-ressource-en-eau/les-53-mesures-du-plan-eau')]),
    row(MX, t('Ley General de Aguas y reforma a la Ley de Aguas Nacionales (DOF, 11 de diciembre de 2025): prioridad al uso personal y doméstico, prohibición de transmitir concesiones entre particulares (solo la CONAGUA reasigna), nuevo Registro Nacional del Agua y delitos hídricos.',
              'General Water Law and reform of the National Water Law (DOF, 11 December 2025): priority for personal and domestic use, ban on transferring concessions between private parties (only CONAGUA reallocates), a new National Water Registry and water crimes.',
              'Loi générale sur l’eau et réforme de la loi sur les eaux nationales (DOF, 11 décembre 2025) : priorité à l’usage personnel et domestique, interdiction de céder des concessions entre particuliers (seule la CONAGUA réattribue), nouveau Registre national de l’eau et délits liés à l’eau.'),
        OK, [('Cámara de Diputados', 'https://www.diputados.gob.mx/LeyesBiblio/ref/lan.htm')]),
    row(CL, t('Reforma del Código de Aguas (Ley 21.435, 6 de abril de 2022): reconoce el derecho humano al agua, da preferencia al consumo humano y limita los nuevos derechos de agua a 30 años.',
              'Water Code reform (Law 21,435, 6 April 2022): recognizes the human right to water, gives priority to human consumption and limits new water rights to 30 years.',
              'Réforme du Code de l’eau (loi 21.435, 6 avril 2022) : reconnaît le droit humain à l’eau, donne la priorité à la consommation humaine et limite les nouveaux droits d’eau à 30 ans.'),
        OK, [('Carey', 'https://www.carey.cl/api/archivo/entra-en-vigor-la-reforma-al-codigo-de-aguas?lang=es')]),
    row(US, t('Río Colorado: el Departamento del Interior aprobó el 21 de agosto de 2026 las reglas de operación para 2027-2028, con recortes de 1,25 millones de acres-pie al año a la cuenca baja. Son provisionales: no hay acuerdo completo entre los siete estados, y la negociación con México por el Tratado de 1944 va aparte.',
              'Colorado River: on 21 August 2026 the Interior Department approved operating rules for 2027-2028, cutting 1.25 million acre-feet a year from the Lower Basin. They are interim: the seven states have not fully agreed, and talks with Mexico under the 1944 Treaty are separate.',
              'Fleuve Colorado : le 21 août 2026, le département de l’Intérieur a approuvé les règles d’exploitation 2027-2028, avec des réductions de 1,25 million d’acres-pieds par an pour le bassin inférieur. Elles sont provisoires : les sept États ne sont pas entièrement d’accord, et la négociation avec le Mexique au titre du traité de 1944 est distincte.'),
        ('part', t('Provisional', 'Interim', 'Provisoire')), [('DOI', 'https://www.doi.gov/pressreleases/interior-department-finalizes-plans-2027-2028-colorado-river-operations')]),
])

page('ciencia-ambiente/estres-hidrico', t('← Ciencia y ambiente', '← Science and environment', '← Science et environnement'),
     h1('Estrés hídrico: ¿nos estamos quedando sin agua?', 'Water stress: are we running out of water?', 'Stress hydrique&nbsp;: sommes-nous en train de manquer d’eau&nbsp;?'),
     'Estrés hídrico: ¿nos estamos quedando sin agua?',
     'Las fuentes detrás de la story sobre el estrés hídrico: qué mide, cuánta gente lo sufre, acuíferos que bajan y la «bancarrota hídrica». / The sources behind the story on water stress.',
     t('Extraemos más agua de la que se repone en muchas cuencas del mundo, y casi siempre para regar. Aquí están los estudios detrás de cada idea de la story: qué mide el estrés hídrico, cuánta gente lo sufre, qué pasa bajo tierra y por qué la ONU habla ahora de bancarrota. Con el tipo de evidencia de cada uno y lo que no demuestra.',
       'In many basins around the world we take more water than is replenished, mostly for irrigation. Here are the studies behind each idea in the story: what water stress measures, how many people face it, what happens underground and why the UN now speaks of bankruptcy. With the type of evidence for each one and what it doesn’t show.',
       'Dans de nombreux bassins du monde, on prélève plus d’eau que ce qui se renouvelle, surtout pour irriguer. Voici les études derrière chaque idée de la story : ce que mesure le stress hydrique, combien de personnes le subissent, ce qui se passe sous terre et pourquoi l’ONU parle désormais de faillite. Avec le type de preuve de chacune et ce qu’elle ne montre pas.'),
     ['meta', 'rev', 'ag', 'obs', 'db'], S1, REG1,
     'Las stories en español, inglés y francés: Estrés hídrico: ¿nos estamos quedando sin agua? / Water stress: are we running out of water? / Stress hydrique : sommes-nous en train de manquer d’eau ?',
     ('', '', ''))

# ================================================================ 2 · ahorro de agua
S2 = [
section(t('En el campo: regar lo justo', 'On the farm: irrigating just enough', 'Aux champs : irriguer juste ce qu’il faut'), [
    ref('Singh M, Singh P, Singh S, Saini RK, Angadi SV · Scientific Reports · 2021; 11: 22095',
        'A global meta-analysis of yield and water productivity responses of vegetables to deficit irrigation',
        t('Combinaron 185 estudios de 30 países sobre ocho hortalizas regadas por debajo de lo que piden. Con un riego leve (más del 80 % del completo), la cosecha cae de media un 6,9 %; con un riego muy escaso (menos del 35 %), un 51 %. A cambio, la productividad del agua (kilos por litro) sube entre un 8 % y un 30 %. Por encima del 65 % del riego completo la pérdida es pequeña; en suelos francos, clima templado e invernadero, menor aún.',
          'They pooled 185 studies from 30 countries on eight vegetables irrigated below their needs. With mild deficit (more than 80% of full irrigation), yield falls 6.9% on average; with severe deficit (below 35%), 51%. In return, water productivity (kilos per litre) rises by 8% to 30%. Above 65% of full irrigation the loss is small; in loam soils, temperate climates and greenhouses, even smaller.',
          'Ils ont combiné 185 études de 30 pays sur huit légumes irrigués en deçà de leurs besoins. Avec un déficit léger (plus de 80 % de l’irrigation complète), la récolte baisse en moyenne de 6,9 % ; avec un déficit sévère (moins de 35 %), de 51 %. En échange, la productivité de l’eau (kilos par litre) augmente de 8 à 30 %. Au-dessus de 65 % de l’irrigation complète, la perte est faible ; en sol limoneux, en climat tempéré et sous serre, encore plus.'),
        ['ma'], doi='10.1038/s41598-021-01433-w'),
    ref('Volk JM, Huntington JL, Melton FS, et al. (31 autores) · Nature Water · 2024; 2: 193–205',
        'Assessing the accuracy of OpenET satellite-based evapotranspiration data to support water resource and land management applications',
        t('OpenET calcula con satélites cuánta agua evaporan y transpiran los cultivos de cada parcela en el oeste de EE. UU. Lo compararon con 152 torres que miden la evapotranspiración en el terreno: en cultivos anuales el error ronda el 10-20 % por mes, temporada o año, y baja del 10 % en el pico de la temporada en clima mediterráneo. En frutales es mayor, en torno al 17 %. Se usa para saber cuánto riega cada finca y para gestionar el agua en cuencas como la del Colorado.',
          'OpenET uses satellites to calculate how much water crops evaporate and transpire on each field in the western US. They compared it with 152 towers that measure evapotranspiration on the ground: for annual crops the error is about 10-20% per month, season or year, and below 10% at peak season in Mediterranean climates. For orchards it is higher, around 17%. It is used to know how much each farm irrigates and to manage water in basins such as the Colorado.',
          'OpenET calcule par satellite combien d’eau les cultures de chaque parcelle évaporent et transpirent dans l’ouest des États-Unis. Ils l’ont comparé à 152 tours qui mesurent l’évapotranspiration sur le terrain : pour les cultures annuelles, l’erreur est d’environ 10-20 % par mois, saison ou année, et passe sous 10 % au pic de saison en climat méditerranéen. Pour les vergers, elle est plus élevée, autour de 17 %. Il sert à savoir combien chaque exploitation irrigue et à gérer l’eau dans des bassins comme celui du Colorado.'),
        ['obs'], doi='10.1038/s44221-023-00181-7'),
], t('El metaanálisis trata solo hortalizas: en cereales, frutales o forrajes la respuesta puede ser distinta. Medir la evaporación con satélite no ahorra agua por sí solo: sirve si alguien decide regar menos o reparte el agua con esos datos.',
     'The meta-analysis covers only vegetables: cereals, fruit trees or forage may respond differently. Measuring evaporation by satellite doesn’t save water by itself: it helps if someone decides to irrigate less or allocates water using that data.',
     'La méta-analyse ne porte que sur les légumes : céréales, vergers ou fourrages peuvent réagir autrement. Mesurer l’évaporation par satellite n’économise pas d’eau en soi : cela sert si quelqu’un décide d’irriguer moins ou répartit l’eau avec ces données.')),

section(t('Agua regenerada', 'Reclaimed water', 'Eau réutilisée'), [
    ref('Ministerio para la Transición Ecológica (MITECO) · Real Decreto 1085/2024, de 22 de octubre',
        'Reglamento de reutilización del agua',
        t('España es el país europeo que más agua regenera: unos 400 hm³ al año, sobre todo para riego. El nuevo reglamento adapta la norma de 2007 a la europea, fija los tratamientos y controles según el uso y se propone duplicar el agua regenerada en los próximos años, para liberar agua dulce para el abastecimiento.',
          'Spain reclaims more water than any other European country: about 400 hm³ a year, mostly for irrigation. The new regulation updates the 2007 rules to match EU law, sets treatment and monitoring by use and aims to double reclaimed water in the coming years, freeing fresh water for drinking supply.',
          'L’Espagne est le pays européen qui réutilise le plus d’eau : environ 400 hm³ par an, surtout pour l’irrigation. Le nouveau règlement adapte la norme de 2007 au droit européen, fixe traitements et contrôles selon l’usage et vise à doubler l’eau réutilisée dans les prochaines années, pour libérer de l’eau douce pour l’alimentation en eau potable.'),
        ['ag'], url='https://www.miteco.gob.es/es/prensa/ultimas-noticias/2024/octubre/aprobado-el-real-decreto-de-reutilizacion-de-las-aguas.html', label='miteco.gob.es · RD de reutilización'),
    ref('Comisión Europea · WISE Freshwater · Water reuse',
        'Water reuse in Europe',
        t('En la UE se depuran unos 40 000 hm³ de agua residual al año, pero solo se regeneran y reutilizan unos 1000 hm³: el 2,4 %. Desde el 26 de junio de 2023 rige un reglamento común con requisitos mínimos de calidad para regar cultivos con agua regenerada.',
          'The EU treats about 40,000 hm³ of wastewater a year, but only about 1,000 hm³ is further treated and reused: 2.4%. Since 26 June 2023 a common regulation sets minimum quality requirements for irrigating crops with reclaimed water.',
          'L’UE épure environ 40 000 hm³ d’eaux usées par an, mais seuls 1 000 hm³ environ sont traités davantage et réutilisés : 2,4 %. Depuis le 26 juin 2023, un règlement commun fixe des exigences minimales de qualité pour irriguer les cultures avec de l’eau réutilisée.'),
        ['ag'], url='https://water.europa.eu/freshwater/europe-freshwater/water-reuse', label='water.europa.eu · water reuse'),
], t('Reutilizar no crea agua nueva: en un río, el agua depurada que se vierte también la usa alguien aguas abajo o el ecosistema. Donde se vierte al mar, como en la costa mediterránea, sí es un recurso adicional. Regenerar cuesta energía y exige controles para no llevar patógenos o contaminantes al campo.',
     'Reuse doesn’t create new water: on a river, treated water that is discharged is also used by someone downstream or by the ecosystem. Where it is discharged to the sea, as on the Mediterranean coast, it is an extra resource. Reclaiming costs energy and requires monitoring so as not to carry pathogens or pollutants to the fields.',
     'Réutiliser ne crée pas d’eau nouvelle : sur un fleuve, l’eau épurée rejetée est aussi utilisée par quelqu’un en aval ou par l’écosystème. Là où elle est rejetée en mer, comme sur la côte méditerranéenne, c’est une ressource en plus. Réutiliser coûte de l’énergie et exige des contrôles pour ne pas apporter de pathogènes ou de polluants aux champs.')),

section(t('En la industria: enfriar sin agua', 'In industry: cooling without water', 'Dans l’industrie : refroidir sans eau'), [
    ref('Qin Y, Wang Y, Li S, Deng H, Wanders N, Bosmans J, Huang L, Hong C, Byers E, Gingerich D, Bielicki JM, He G · Nature Water · 2023; 1(8): 682–693',
        'Global assessment of the carbon–water tradeoff of dry cooling for thermal power generation',
        t('Las centrales térmicas (carbón, gas, nuclear) usan agua para enfriarse: suponen entre el 40 y el 50 % de las extracciones de agua en EE. UU. y cerca del 40 % en Europa. Enfriar con aire (refrigeración en seco) casi elimina esa agua, pero la central rinde menos: según el lugar y el clima, se pierde entre un 1 y un 15 % de la producción, con más emisiones de CO₂ por cada kWh. Enfriar con agua residual o salobre es una alternativa con menos penalización, si hay una fuente cerca.',
          'Thermal power plants (coal, gas, nuclear) use water for cooling: they account for 40-50% of water withdrawals in the US and about 40% in Europe. Air (dry) cooling nearly eliminates that water, but the plant performs worse: depending on location and climate, 1 to 15% of output is lost, with more CO₂ per kWh. Cooling with wastewater or brackish water is an alternative with a smaller penalty, if a source is nearby.',
          'Les centrales thermiques (charbon, gaz, nucléaire) utilisent de l’eau pour se refroidir : elles représentent 40 à 50 % des prélèvements d’eau aux États-Unis et environ 40 % en Europe. Le refroidissement à l’air (sec) supprime presque cette eau, mais la centrale rend moins : selon le lieu et le climat, on perd de 1 à 15 % de la production, avec plus de CO₂ par kWh. Refroidir avec des eaux usées ou saumâtres est une alternative moins pénalisante, s’il y a une source à proximité.'),
        ['db'], doi='10.1038/s44221-023-00120-6'),
], t('Gran parte del agua que extraen las centrales vuelve al río, más caliente: «extraer» no es lo mismo que «consumir». La penalización del 1-15 % es una estimación de modelo que depende del clima local. Los centros de datos tienen el mismo dilema, y los tratamos en el tema siguiente de la serie.',
     'Much of the water power plants withdraw returns to the river, warmer: “withdrawing” is not the same as “consuming”. The 1-15% penalty is a model estimate that depends on the local climate. Data centres face the same dilemma, covered in the next topic of the series.',
     'Une grande partie de l’eau prélevée par les centrales retourne à la rivière, plus chaude : « prélever » n’est pas « consommer ». La pénalité de 1-15 % est une estimation de modèle qui dépend du climat local. Les centres de données ont le même dilemme, traité dans le sujet suivant de la série.')),

section(t('La paradoja de la eficiencia', 'The efficiency paradox', 'Le paradoxe de l’efficacité'), [
    ref('Grafton RQ, Williams J, Perry CJ, Molle F, Ringler C, Steduto P, Udall B, Wheeler SA, Wang Y, Garrick D, Allen RG · Science · 2018; 361(6404): 748–750',
        'The paradox of irrigation efficiency',
        t('Con riego tradicional, buena parte del agua que «se pierde» vuelve al acuífero o al río y la usa otro. El goteo hace que la planta aproveche más agua, así que se consume más y vuelve menos. Si además el agricultor usa el agua ahorrada para ampliar la superficie regada, el consumo total de la cuenca sube. Los autores revisan casos de varios países y piden medir el consumo real, no solo la eficiencia, y limitar las extracciones al subvencionar riego eficiente.',
          'With traditional irrigation, much of the water that is “lost” returns to the aquifer or river and is used by someone else. Drip makes the plant use more of the water, so more is consumed and less returns. If the farmer also uses the saved water to irrigate more land, total basin consumption rises. The authors review cases from several countries and call for measuring actual consumption, not just efficiency, and capping withdrawals when subsidizing efficient irrigation.',
          'Avec l’irrigation traditionnelle, une bonne partie de l’eau « perdue » retourne à la nappe ou à la rivière et sert à quelqu’un d’autre. Le goutte-à-goutte fait que la plante utilise davantage l’eau : on consomme plus et il en revient moins. Si l’agriculteur utilise en plus l’eau économisée pour irriguer plus de surface, la consommation totale du bassin augmente. Les auteurs examinent des cas de plusieurs pays et demandent de mesurer la consommation réelle, pas seulement l’efficacité, et de plafonner les prélèvements quand on subventionne l’irrigation efficace.'),
        ['rev', 'old'], doi='10.1126/science.aat9314'),
    ref('Lankford BA · Agricultural Water Management · 2023; 287: 108437',
        'Resolving the paradoxes of irrigation efficiency: Irrigated systems accounting analyses depletion-based water conservation for reallocation',
        t('Matiza la paradoja: no es una ley universal. Con un modelo que sigue el agua entre la zona regada, la zona que se amplía y la que reutiliza las pérdidas, muestra que mejorar la eficiencia puede ahorrar agua real o no, según lo que se haga después. Si se riega más superficie con lo ahorrado, el consumo sube un 7 %; si se combinan varias medidas y se limita la superficie, el ahorro real llega al 69 % sin perder cosecha.',
          'It nuances the paradox: it isn’t a universal law. With a model tracking water between the irrigated area, the area that expands and the area that reuses losses, it shows that improving efficiency may or may not save real water, depending on what happens next. If the savings irrigate more land, consumption rises 7%; if several measures are combined and the area is capped, real savings reach 69% with no loss of crop.',
          'Il nuance le paradoxe : ce n’est pas une loi universelle. Avec un modèle qui suit l’eau entre la zone irriguée, la zone qui s’étend et celle qui réutilise les pertes, il montre qu’améliorer l’efficacité peut économiser de l’eau réelle ou non, selon ce qui suit. Si l’eau économisée irrigue plus de surface, la consommation augmente de 7 % ; si l’on combine plusieurs mesures et plafonne la surface, l’économie réelle atteint 69 % sans perte de récolte.'),
        ['db'], doi='10.1016/j.agwat.2023.108437'),
], t('Las cifras de Lankford salen de un caso modelo con supuestos fijos, no de una cuenca medida. Ninguno de los dos dice que el riego eficiente sea inútil: dice que, sin límites a lo que se extrae, el ahorro en la parcela no se traduce en ahorro en la cuenca.',
     'Lankford’s figures come from a model case with fixed assumptions, not from a measured basin. Neither paper says efficient irrigation is useless: they say that, without limits on withdrawals, savings on the field don’t translate into savings in the basin.',
     'Les chiffres de Lankford viennent d’un cas modèle aux hypothèses fixes, pas d’un bassin mesuré. Aucun des deux ne dit que l’irrigation efficace est inutile : sans limite aux prélèvements, l’économie à la parcelle ne se traduit pas en économie dans le bassin.')),
]

REG2 = reg(t('Las normas que más empujan el ahorro en el campo y la industria regulan el agua regenerada y la calidad de los vertidos. Las que reparten el agua entre usos están en el tema anterior de la serie.',
             'The rules that most push savings on farms and in industry regulate reclaimed water and the quality of discharges. Those that allocate water between uses are in the previous topic of the series.',
             'Les règles qui poussent le plus aux économies aux champs et dans l’industrie encadrent l’eau réutilisée et la qualité des rejets. Celles qui répartissent l’eau entre usages sont dans le sujet précédent de la série.'), [
    row(UE, t('Reglamento (UE) 2020/741 sobre requisitos mínimos para la reutilización del agua en el riego agrícola. Se aplica desde el 26 de junio de 2023; cada país puede decidir no usarlo o limitarlo.',
              'Regulation (EU) 2020/741 on minimum requirements for water reuse in agricultural irrigation. It has applied since 26 June 2023; each country may decide not to use it or to limit it.',
              'Règlement (UE) 2020/741 relatif aux exigences minimales applicables à la réutilisation de l’eau pour l’irrigation agricole. Il s’applique depuis le 26 juin 2023 ; chaque pays peut décider de ne pas y recourir ou de le limiter.'),
        OK, [('EUR-Lex', 'https://eur-lex.europa.eu/eli/reg/2020/741/oj')]),
    row(ES, t('Real Decreto 1085/2024, de 22 de octubre, reglamento de reutilización del agua: sustituye al de 2007 y se adapta al reglamento europeo.',
              'Royal Decree 1085/2024 of 22 October, water reuse regulation: replaces the 2007 rules and aligns with the EU regulation.',
              'Décret royal 1085/2024 du 22 octobre, règlement sur la réutilisation de l’eau : remplace celui de 2007 et s’aligne sur le règlement européen.'),
        OK, [('BOE', 'https://www.boe.es/eli/es/rd/2024/10/22/1085')]),
    row(FR, t('Decreto 2023-835, de 29 de agosto de 2023, sobre los usos y condiciones de uso del agua de lluvia y de las aguas residuales tratadas: amplía los usos permitidos más allá del riego.',
              'Decree 2023-835 of 29 August 2023 on the uses and conditions of use of rainwater and treated wastewater: broadens permitted uses beyond irrigation.',
              'Décret n° 2023-835 du 29 août 2023 relatif aux usages et aux conditions d’utilisation des eaux de pluie et des eaux usées traitées : élargit les usages autorisés au-delà de l’irrigation.'),
        OK, [('FAOLEX / UNEP', 'https://leap.unep.org/en/countries/fr/national-legislation/decret-ndeg-2023-835-du-29-aout-2023-relatif-aux-usages-et-aux')]),
    row(MX, t('NOM-001-SEMARNAT-2021 (DOF, 11 de marzo de 2022): nuevos límites de contaminantes en las descargas de aguas residuales a ríos, lagos y mar, aplicables desde 2023. Sustituye a la norma de 1996.',
              'NOM-001-SEMARNAT-2021 (DOF, 11 March 2022): new pollutant limits for wastewater discharges into rivers, lakes and the sea, applicable since 2023. Replaces the 1996 standard.',
              'NOM-001-SEMARNAT-2021 (DOF, 11 mars 2022) : nouvelles limites de polluants dans les rejets d’eaux usées vers les rivières, lacs et la mer, applicables depuis 2023. Remplace la norme de 1996.'),
        OK, [('Holland & Knight', 'https://www.hklaw.com/es/insights/publications/2022/03/nom-001-semarnat-2021-limites-contaminantes-en-descargas')]),
])

page('ciencia-tecnologia/ahorro-agua', t('← Ciencia y tecnología', '← Science and technology', '← Science et technologie'),
     h1('Estrés hídrico: ¿cómo se ahorra agua en el campo y la industria?', 'Water stress: how do farms and industry save water?', 'Stress hydrique&nbsp;: comment économiser l’eau aux champs et dans l’industrie&nbsp;?'),
     'Estrés hídrico: ¿cómo se ahorra agua en el campo y la industria?',
     'Las fuentes detrás de la story sobre cómo se ahorra agua: riego deficitario, satélites, agua regenerada, refrigeración en seco y la paradoja de la eficiencia. / The sources behind the story on saving water.',
     t('Si el riego se lleva la mayor parte del agua, ahí está el mayor margen de ahorro; en la industria, en cómo se enfrían las centrales. Aquí están los estudios detrás de cada idea de la story: regar lo justo, medir desde el espacio, regenerar el agua residual, enfriar sin agua y por qué ahorrar en la parcela no siempre ahorra en la cuenca.',
       'If irrigation takes most of the water, that is where the biggest savings lie; in industry, in how power plants are cooled. Here are the studies behind each idea in the story: irrigating just enough, measuring from space, reclaiming wastewater, cooling without water and why saving on the field doesn’t always save in the basin.',
       'Si l’irrigation absorbe la plus grande part de l’eau, c’est là que se trouve la plus grande marge d’économie ; dans l’industrie, dans la façon de refroidir les centrales. Voici les études derrière chaque idée de la story : irriguer juste ce qu’il faut, mesurer depuis l’espace, réutiliser les eaux usées, refroidir sans eau et pourquoi économiser à la parcelle n’économise pas toujours dans le bassin.'),
     ['ma', 'rev', 'ag', 'obs', 'db', 'old'], S2, REG2,
     'Las stories en español, inglés y francés: ¿Cómo se ahorra agua en el campo y la industria? / How do farms and industry save water? / Comment économiser l’eau aux champs et dans l’industrie ?',
     ('', '', ''))

# ================================================================ 3 · centros de datos
S3 = [
section(t('Cuánta energía usan', 'How much energy they use', 'Combien d’énergie ils consomment'), [
    ref('Agencia Internacional de la Energía (IEA) · 2025',
        'Energy and AI',
        t('Los centros de datos consumieron unos 415 TWh en 2024, cerca del 1,5 % de la electricidad mundial. En el escenario base de la IEA, la cifra se duplica hasta unos 945 TWh en 2030, algo menos del 3 %, impulsada sobre todo por la IA.',
          'Data centres used about 415 TWh in 2024, around 1.5% of global electricity. In the IEA’s base case, that doubles to about 945 TWh by 2030, just under 3%, driven mainly by AI.',
          'Les centres de données ont consommé environ 415 TWh en 2024, près de 1,5 % de l’électricité mondiale. Dans le scénario de base de l’AIE, ce chiffre double pour atteindre environ 945 TWh en 2030, un peu moins de 3 %, surtout à cause de l’IA.'),
        ['ag'], url='https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai', label='iea.org · Energy and AI'),
], t('Es una proyección con escenarios: la IEA presenta también casos con más y menos crecimiento. El 1,5 % es un promedio mundial; en algunas regiones, como Irlanda o Virginia, los centros de datos pesan mucho más en la red.',
     'It is a scenario-based projection: the IEA also presents higher- and lower-growth cases. The 1.5% is a global average; in some regions, such as Ireland or Virginia, data centres weigh far more on the grid.',
     'C’est une projection par scénarios : l’AIE présente aussi des cas de croissance plus forte et plus faible. Les 1,5 % sont une moyenne mondiale ; dans certaines régions, comme l’Irlande ou la Virginie, les centres de données pèsent bien plus sur le réseau.')),

section(t('Por qué las cifras varían tanto', 'Why the figures vary so much', 'Pourquoi les chiffres varient autant'), [
    ref('Lei N, Lu J, Shehabi A, Masanet ER · Resources, Conservation and Recycling · 2025; 219: 108310',
        'The water use of data center workloads: A review and assessment of key determinants',
        t('Revisión del Laboratorio Nacional Lawrence Berkeley y la Universidad de California. Un centro de datos usa agua en el propio edificio, sobre todo si se enfría evaporando agua, y fuera, en las centrales que producen su electricidad. Según cómo se combinen esos factores, el agua por tarea puede variar más de 10 000 veces: el agua por kWh de la red cambia más de 1000 veces entre lugares, y la eficiencia de los servidores, unas 10 veces. Los factores que más pesan son la eficiencia de los servidores, el agua de la red eléctrica, el uso de los servidores, el tipo de refrigeración y el clima. No hay una receta única: depende de cada sitio.',
          'A review by Lawrence Berkeley National Laboratory and the University of California. A data centre uses water on site, especially if it cools by evaporating water, and off site, in the power plants that produce its electricity. Depending on how these factors combine, water per task can vary more than 10,000-fold: grid water per kWh varies more than 1,000-fold between locations, and server efficiency about 10-fold. The biggest factors are server efficiency, grid water intensity, server utilization, cooling type and climate. There is no single recipe: it depends on each site.',
          'Revue du Lawrence Berkeley National Laboratory et de l’Université de Californie. Un centre de données utilise de l’eau sur place, surtout s’il se refroidit par évaporation, et ailleurs, dans les centrales qui produisent son électricité. Selon la combinaison de ces facteurs, l’eau par tâche peut varier de plus de 10 000 fois : l’eau par kWh du réseau varie de plus de 1 000 fois d’un lieu à l’autre, et l’efficacité des serveurs d’environ 10 fois. Les facteurs qui pèsent le plus sont l’efficacité des serveurs, l’eau du réseau électrique, l’utilisation des serveurs, le type de refroidissement et le climat. Il n’y a pas de recette unique : cela dépend de chaque site.'),
        ['rev'], doi='10.1016/j.resconrec.2025.108310'),
], t('La revisión compara escenarios posibles, no centros reales medidos uno a uno. Que la refrigeración sin agua ahorre agua en el edificio no significa que ahorre en total: si gasta más electricidad y esa electricidad viene de centrales que se enfrían con agua, parte del ahorro se pierde.',
     'The review compares possible scenarios, not real centres measured one by one. Waterless cooling saving water in the building doesn’t mean it saves water overall: if it uses more electricity and that electricity comes from water-cooled power plants, part of the saving is lost.',
     'La revue compare des scénarios possibles, pas des centres réels mesurés un par un. Qu’un refroidissement sans eau économise l’eau dans le bâtiment ne veut pas dire qu’il en économise au total : s’il consomme plus d’électricité et que celle-ci vient de centrales refroidies à l’eau, une partie de l’économie est perdue.')),

section(t('Cuánta agua: dos maneras de contar', 'How much water: two ways of counting', 'Combien d’eau : deux façons de compter'), [
    ref('de Vries-Gao A · Patterns · 2026; 7(1): 101430',
        'The carbon and water footprints of data centers and what this could mean for artificial intelligence',
        t('A partir de los informes de las empresas y de la potencia estimada del hardware de IA, calcula que la IA consumió en 2025 entre 312 000 y 765 000 millones de litros de agua, del orden de toda el agua embotellada que se bebe en el mundo. Incluye el agua de la electricidad, con una media de 3,4 litros por kWh, que en las redes de EE. UU. va de 0,7 a 12 litros según el lugar. Como referencia, la IEA estimó unos 560 000 millones de litros para todos los centros de datos en 2023, la mayor parte por la electricidad.',
          'Using company reports and the estimated power of AI hardware, it calculates that AI consumed between 312 and 765 billion litres of water in 2025, on the order of all the bottled water drunk worldwide. It includes the water behind the electricity, averaging 3.4 litres per kWh, which on US grids ranges from 0.7 to 12 litres depending on location. For reference, the IEA estimated about 560 billion litres for all data centres in 2023, mostly from electricity.',
          'À partir des rapports des entreprises et de la puissance estimée du matériel d’IA, il calcule que l’IA a consommé en 2025 entre 312 et 765 milliards de litres d’eau, de l’ordre de toute l’eau en bouteille bue dans le monde. Il inclut l’eau de l’électricité, avec une moyenne de 3,4 litres par kWh, qui va de 0,7 à 12 litres selon les réseaux américains. Pour comparaison, l’AIE a estimé environ 560 milliards de litres pour tous les centres de données en 2023, surtout à cause de l’électricité.'),
        ['db'], doi='10.1016/j.patter.2025.101430'),
    ref('Elsworth C, Huang K, Patterson D, Dean J, Vahdat A, et al. (Google) · arXiv 2508.15734 · agosto de 2025',
        'Measuring the environmental impact of delivering AI at Google Scale',
        t('Google midió en su propia infraestructura el consumo de una consulta de texto típica a Gemini: 0,24 Wh de energía y 0,26 mL de agua, unas cinco gotas. El agua se calcula multiplicando la energía por el agua que consumen sus centros al enfriarse (1,15 litros por kWh). No incluye el agua de las centrales que producen la electricidad.',
          'Google measured, on its own infrastructure, the footprint of a typical Gemini text prompt: 0.24 Wh of energy and 0.26 mL of water, about five drops. The water is calculated by multiplying the energy by the water its data centres consume for cooling (1.15 litres per kWh). It doesn’t include the water used by the power plants that produce the electricity.',
          'Google a mesuré sur sa propre infrastructure l’empreinte d’une requête texte typique à Gemini : 0,24 Wh d’énergie et 0,26 mL d’eau, environ cinq gouttes. L’eau est calculée en multipliant l’énergie par l’eau que ses centres consomment pour se refroidir (1,15 litre par kWh). Elle n’inclut pas l’eau des centrales qui produisent l’électricité.'),
        ['co'], url='https://arxiv.org/abs/2508.15734', label='arxiv.org/abs/2508.15734'),
], t('Las dos cifras no se contradicen: cuentan cosas distintas. Una consulta gasta poquísima agua, pero se hacen miles de millones al día, y el entrenamiento de los modelos va aparte. La estimación de de Vries-Gao tiene mucha incertidumbre porque las empresas no separan el consumo de la IA del resto de su nube; la de Google no está revisada por pares.',
     'The two figures don’t contradict each other: they count different things. A single prompt uses very little water, but billions are made every day, and model training comes on top. De Vries-Gao’s estimate is highly uncertain because companies don’t separate AI consumption from the rest of their cloud; Google’s is not peer reviewed.',
     'Les deux chiffres ne se contredisent pas : ils comptent des choses différentes. Une requête consomme très peu d’eau, mais il s’en fait des milliards par jour, et l’entraînement des modèles s’y ajoute. L’estimation de de Vries-Gao est très incertaine car les entreprises ne séparent pas la consommation de l’IA du reste de leur cloud ; celle de Google n’est pas relue par les pairs.')),

section(t('Dónde se construyen', 'Where they are built', 'Où ils sont construits'), [
    ref('Xataka México · 29 de agosto de 2025 (con datos de BBC, El País e IPS)',
        'México está recibiendo más centros de datos que nunca, mientras hay un problema paralelo: la escasez de agua',
        t('Querétaro concentra la mayor parte de los centros de datos de México, con más de 10 000 millones de dólares de inversión prevista en una década. Es una región semiárida: en 2024 vivió una de sus peores sequías, y siete de sus once acuíferos están sobreexplotados. Las estimaciones de consumo de los nuevos centros van de millones de litros al año a unos 15 000 millones (cerca del 13 % del consumo de la zona metropolitana), pero las cifras oficiales no son públicas. Una de las empresas asegura usar refrigeración en circuito cerrado.',
          'Querétaro hosts most of Mexico’s data centres, with more than 10 billion dollars of investment planned over a decade. It is a semi-arid region: in 2024 it went through one of its worst droughts, and seven of its eleven aquifers are overdrawn. Estimates of the new centres’ water use range from millions of litres a year to about 15 billion (around 13% of the metro area’s consumption), but official figures are not public. One of the companies says it uses closed-loop cooling.',
          'Querétaro concentre la plupart des centres de données du Mexique, avec plus de 10 milliards de dollars d’investissement prévus sur une décennie. C’est une région semi-aride : en 2024, elle a connu l’une de ses pires sécheresses, et sept de ses onze nappes sont surexploitées. Les estimations de consommation des nouveaux centres vont de millions de litres par an à environ 15 milliards (près de 13 % de la consommation de la zone métropolitaine), mais les chiffres officiels ne sont pas publics. L’une des entreprises affirme utiliser un refroidissement en circuit fermé.'),
        ['pr'], url='https://www.xataka.com.mx/robotica-e-ia/mexico-esta-recibiendo-centros-datos-que-nunca-hay-problema-paralelo-escasez-agua', label='xataka.com.mx'),
    ref('Meganoticias · 17 de septiembre de 2024',
        'Google renuncia al proyecto original de data center en Cerrillos',
        t('En Santiago de Chile, el proyecto original de Google en Cerrillos preveía extraer 169 litros por segundo del acuífero Santiago Central para enfriarse, en plena megasequía. En febrero de 2024 el Segundo Tribunal Ambiental anuló parcialmente su aprobación ambiental tras el reclamo de una vecina. Google renunció a ese diseño y anunció que el nuevo proyecto se enfriará con aire.',
          'In Santiago, Chile, Google’s original project in Cerrillos planned to draw 169 litres per second from the Santiago Central aquifer for cooling, in the middle of a megadrought. In February 2024 the Second Environmental Court partially annulled its environmental approval after a complaint by a local resident. Google dropped that design and announced the new project will be air-cooled.',
          'À Santiago du Chili, le projet initial de Google à Cerrillos prévoyait de prélever 169 litres par seconde dans la nappe de Santiago Central pour se refroidir, en pleine méga-sécheresse. En février 2024, le deuxième tribunal environnemental a partiellement annulé son autorisation environnementale après le recours d’une habitante. Google a renoncé à ce projet et annoncé que le nouveau serait refroidi à l’air.'),
        ['pr'], url='https://www.meganoticias.cl/nacional/459226-google-renuncia-proyecto-original-data-center-cerrillos-razones-pdp-17-9-2024.html', label='meganoticias.cl'),
], t('Son fuentes de prensa: sirven para ver el problema, no para cuantificarlo. Que un centro esté en una zona con estrés no prueba que agote el acuífero; para saberlo harían falta los datos de extracción, que en México no se publican por centro. Lo que sí muestran es que, cuando se exige, las empresas pueden cambiar a refrigeración sin agua.',
     'These are press sources: they show the problem but don’t quantify it. A data centre being in a stressed area doesn’t prove it depletes the aquifer; that would require extraction data, which in Mexico is not published per facility. What they do show is that, when required, companies can switch to waterless cooling.',
     'Ce sont des sources de presse : elles montrent le problème sans le quantifier. Qu’un centre se trouve dans une zone en stress ne prouve pas qu’il épuise la nappe ; il faudrait les données de prélèvement, qui au Mexique ne sont pas publiées par site. Elles montrent en revanche que, lorsqu’on l’exige, les entreprises peuvent passer à un refroidissement sans eau.')),
]

REG3 = reg(t('La UE es la única que obliga a los centros de datos a declarar cuánta agua usan. En América, el agua de los centros de datos se rige por las mismas concesiones y evaluaciones ambientales que cualquier otra industria.',
             'The EU is the only one requiring data centres to report how much water they use. In the Americas, data-centre water is governed by the same concessions and environmental assessments as any other industry.',
             'L’UE est la seule à obliger les centres de données à déclarer leur consommation d’eau. En Amérique, l’eau des centres de données relève des mêmes concessions et évaluations environnementales que toute autre industrie.'), [
    row(UE, t('Directiva de Eficiencia Energética (UE) 2023/1791 y Reglamento Delegado (UE) 2024/1364: los centros de datos con un consumo energético significativo deben reportar a una base de datos europea su energía y su huella hídrica.',
              'Energy Efficiency Directive (EU) 2023/1791 and Delegated Regulation (EU) 2024/1364: data centres with significant energy use must report their energy and water footprint to an EU database.',
              'Directive (UE) 2023/1791 relative à l’efficacité énergétique et règlement délégué (UE) 2024/1364 : les centres de données à forte consommation d’énergie doivent déclarer leur énergie et leur empreinte eau dans une base de données européenne.'),
        OK, [('Comisión Europea', 'https://energy.ec.europa.eu/topics/energy-efficiency/energy-efficiency-targets-directive-and-rules/energy-efficiency-directive/energy-performance-data-centres_en')]),
    row(UE, t('Sistema común de calificación de la sostenibilidad de los centros de datos, propuesto por la Comisión el 21 de septiembre de 2026. Se prepara además una propuesta de requisitos mínimos de rendimiento, prevista para 2027.',
              'Common EU sustainability rating scheme for data centres, proposed by the Commission on 21 September 2026. A proposal for minimum performance standards is also being prepared, expected in 2027.',
              'Système commun de notation de la durabilité des centres de données, proposé par la Commission le 21 septembre 2026. Une proposition d’exigences minimales de performance est aussi en préparation, attendue en 2027.'),
        ('part', t('Propuesta', 'Proposed', 'Proposé')), [('Comisión Europea', 'https://energy.ec.europa.eu/topics/energy-efficiency/energy-efficiency-targets-directive-and-rules/energy-efficiency-directive/energy-performance-data-centres_en')]),
    row(CL, t('Caso Cerrillos (Santiago): el Segundo Tribunal Ambiental anuló parcialmente en febrero de 2024 la aprobación ambiental del centro de datos de Google por su uso de agua; la empresa rehízo el proyecto con refrigeración por aire.',
              'Cerrillos case (Santiago): in February 2024 the Second Environmental Court partially annulled the environmental approval of Google’s data centre over its water use; the company redesigned it with air cooling.',
              'Affaire Cerrillos (Santiago) : en février 2024, le deuxième tribunal environnemental a partiellement annulé l’autorisation environnementale du centre de données de Google pour sa consommation d’eau ; l’entreprise a refait le projet avec un refroidissement à l’air.'),
        ('part', t('Fallo judicial', 'Court ruling', 'Décision de justice')), [('Meganoticias', 'https://www.meganoticias.cl/nacional/459226-google-renuncia-proyecto-original-data-center-cerrillos-razones-pdp-17-9-2024.html')]),
    row(MX, t('No hay una norma específica para centros de datos. Necesitan concesión de agua como cualquier industria, ahora bajo la Ley General de Aguas (DOF, 11 de diciembre de 2025), y no están obligados a publicar su consumo.',
              'There is no specific rule for data centres. They need a water concession like any industry, now under the General Water Law (DOF, 11 December 2025), and are not required to publish their consumption.',
              'Il n’existe pas de règle spécifique aux centres de données. Ils ont besoin d’une concession d’eau comme toute industrie, désormais sous la loi générale sur l’eau (DOF, 11 décembre 2025), et ne sont pas tenus de publier leur consommation.'),
        ('rev', t('Sin norma', 'No rule', 'Pas de règle')), [('Cámara de Diputados', 'https://www.diputados.gob.mx/LeyesBiblio/ref/lan.htm')]),
    row(US, t('No hay obligación federal de declarar el agua de los centros de datos; lo que se publica son informes voluntarios de cada empresa.',
              'There is no federal requirement to report data-centre water; what is published are each company’s voluntary reports.',
              'Il n’y a pas d’obligation fédérale de déclarer l’eau des centres de données ; ce qui est publié, ce sont les rapports volontaires de chaque entreprise.'),
        ('rev', t('Sin norma', 'No rule', 'Pas de règle')), []),
])

page('ciencia-tecnologia/centros-datos-agua', t('← Ciencia y tecnología', '← Science and technology', '← Science et technologie'),
     h1('IA y centros de datos: ¿cuánta agua beben?', 'AI and data centres: how much water do they drink?', 'IA et centres de données&nbsp;: combien d’eau boivent-ils&nbsp;?'),
     'IA y centros de datos: ¿cuánta agua beben?',
     'Las fuentes detrás de la story sobre la IA, los centros de datos y el agua: cuánta energía y agua usan, por qué las cifras varían tanto y dónde se construyen. / The sources behind the story on AI, data centres and water.',
     t('La IA no corre en la nube: corre en edificios llenos de servidores que hay que enfriar, a menudo con agua, y que consumen electricidad que también la necesita. Aquí están los estudios detrás de cada idea de la story: cuánta energía usan, por qué las cifras de agua varían tanto, qué cuenta cada estimación y qué pasa cuando se construyen en zonas con estrés hídrico.',
       'AI doesn’t run in the cloud: it runs in buildings full of servers that must be cooled, often with water, and that use electricity that needs water too. Here are the studies behind each idea in the story: how much energy they use, why water figures vary so much, what each estimate counts and what happens when they are built in water-stressed areas.',
       'L’IA ne tourne pas dans le nuage : elle tourne dans des bâtiments remplis de serveurs qu’il faut refroidir, souvent avec de l’eau, et qui consomment une électricité qui en a aussi besoin. Voici les études derrière chaque idée de la story : combien d’énergie ils consomment, pourquoi les chiffres d’eau varient autant, ce que compte chaque estimation et ce qui se passe quand ils s’installent dans des zones en stress hydrique.'),
     ['rev', 'ag', 'db', 'co', 'pr'], S3, REG3,
     'Las stories en español, inglés y francés: IA y centros de datos: ¿cuánta agua beben? / AI and data centres: how much water do they drink? / IA et centres de données : combien d’eau boivent-ils ?',
     ('', '', ''))
