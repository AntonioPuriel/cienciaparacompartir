"""Genera ciencia-tecnologia/pfas-destruccion/index.html (ES/EN/FR)."""
import sys, pathlib
from pagekit import t, section, HORIZON

OUT = pathlib.Path(sys.argv[1])

CH = {
    'meta': ('meta', t('Síntesis', 'Synthesis', 'Synthèse')),
    'obs': ('obs', t('Medición', 'Measurement', 'Mesures')),
    'lab': ('lab', t('Laboratorio', 'Lab', 'Laboratoire')),
    'rev': ('rev', t('Revisión', 'Review', 'Revue')),
    'ag': ('rev', t('Agencia', 'Agency', 'Agence')),
    'db': ('db', t('Modelo', 'Model', 'Modèle')),
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

WATER = '../../ciencia-ambiente/disruptores-agua/'
HEALTH = '../../ciencia-salud/disruptores-endocrinos/'
S = []

S.append(section(t('Quitarlos del agua no es destruirlos', 'Removing them from water isn’t destroying them', 'Les retirer de l’eau n’est pas les détruire'), '\n'.join([
    ref('Crini G, Mongioví C, Lichtfouse É, et al. · Environmental Chemistry Letters · 2025',
        'Advantages and disadvantages of separation-based water treatment methods for the removal of per- and polyfluoroalkyl substances in drinking water: a review',
        t('Compara los tres métodos que hoy se usan en plantas potabilizadoras. El carbón activado granular es barato y eficaz, pero retiene poco o nada los PFAS de cadena corta. El intercambio iónico funciona y sus resinas se regeneran, aunque rinde menos cuando el agua trae otras sustancias que compiten. La ósmosis inversa es la más eficaz, pero gasta mucha energía. Los tres dejan un residuo cargado de PFAS que hay que gestionar.',
          'Compares the three methods used today in drinking-water plants. Granular activated carbon is cheap and effective, but retains short-chain PFAS poorly or not at all. Ion exchange works and its resins can be regenerated, though it performs worse when the water carries other competing substances. Reverse osmosis is the most effective, but energy-hungry. All three leave a PFAS-laden waste that has to be managed.',
          'Compare les trois méthodes utilisées aujourd’hui dans les usines d’eau potable. Le charbon actif en grains est bon marché et efficace, mais retient peu ou pas les PFAS à chaîne courte. L’échange d’ions fonctionne et ses résines se régénèrent, mais il perd en efficacité quand l’eau contient d’autres substances concurrentes. L’osmose inverse est la plus efficace, mais très énergivore. Les trois laissent un déchet chargé de PFAS qu’il faut gérer.'),
        ['rev'], doi='10.1007/s10311-025-01890-z'),
    ref('Herkert NJ, Merrill J, Peters C, et al. · Environmental Science &amp; Technology Letters · 2020; 7(3): 178–184',
        'Assessing the Effectiveness of Point-of-Use Residential Drinking Water Filters for Perfluoroalkyl Substances (PFASs)',
        t('Midieron PFAS antes y después del filtro en 73 hogares de Carolina del Norte (EE. UU.). Los filtros de ósmosis inversa bajo el fregadero y los de dos etapas eliminaron casi por completo todos los PFAS analizados. Los de carbón activado fueron irregulares: quitaron alrededor del 60–70 % de los de cadena larga y cerca del 40 % de los de cadena corta. En 4 de 8 sistemas de carbón para toda la casa, el agua filtrada tenía a veces más PFAS que la de entrada.',
          'They measured PFAS before and after the filter in 73 homes in North Carolina (US). Under-sink reverse osmosis and two-stage filters removed nearly all the PFAS tested. Activated carbon filters were inconsistent: about 60–70% of long-chain and around 40% of short-chain PFAS were removed. In 4 of 8 whole-house carbon systems, filtered water sometimes had more PFAS than the incoming water.',
          'Ils ont mesuré les PFAS avant et après le filtre dans 73 foyers de Caroline du Nord (États-Unis). Les filtres à osmose inverse sous l’évier et à deux étages ont éliminé presque tous les PFAS analysés. Les filtres à charbon actif ont été irréguliers : environ 60–70 % des PFAS à chaîne longue et près de 40 % de ceux à chaîne courte retirés. Dans 4 des 8 systèmes à charbon pour toute la maison, l’eau filtrée contenait parfois plus de PFAS que l’eau d’entrée.'),
        ['obs'], doi='10.1021/acs.estlett.0c00004'),
]), t('Un filtro en casa reduce lo que bebes, pero no lo que hay en el río: los PFAS retenidos acaban en el cartucho o en la salmuera de la ósmosis. El estudio de Herkert es de una sola región y midió filtros concretos; un modelo distinto puede comportarse de otra forma.',
      'A home filter reduces what you drink, not what’s in the river: the retained PFAS end up in the cartridge or in the reverse-osmosis brine. Herkert’s study covers one region and specific filters; a different model may behave differently.',
      'Un filtre à la maison réduit ce que vous buvez, pas ce qu’il y a dans la rivière : les PFAS retenus finissent dans la cartouche ou dans la saumure de l’osmose. L’étude de Herkert porte sur une seule région et des filtres précis ; un autre modèle peut se comporter autrement.')))

S.append(section(t('Quemarlos: ¿funciona del todo?', 'Burning them: does it fully work?', 'Les brûler : est-ce vraiment efficace&nbsp;?'), '\n'.join([
    ref('Wang J, Lin Z, He X, et al. · Environmental Science &amp; Technology · 2022; 56(9): 5355–5370',
        'Critical Review of Thermal Decomposition of Per- and Polyfluoroalkyl Substances: Mechanisms and Implications for Thermal Treatment Processes',
        t('La incineración y otros tratamientos térmicos están muy disponibles y, en las condiciones adecuadas, deberían mineralizar los PFAS. Pero los autores concluyen que aún no se conocen bien los mecanismos ni las vías de degradación, ni qué subproductos se forman, y que esas lagunas limitan su uso seguro como destino final de los residuos con PFAS.',
          'Incineration and other thermal treatments are widely available and, under the right conditions, should mineralize PFAS. But the authors conclude that the mechanisms, degradation pathways and byproducts are still poorly understood, and that these gaps limit their safe use as an end-of-life destination for PFAS waste.',
          'L’incinération et les autres traitements thermiques sont largement disponibles et, dans de bonnes conditions, devraient minéraliser les PFAS. Mais les auteurs concluent que les mécanismes, les voies de dégradation et les sous-produits restent mal connus, et que ces lacunes limitent leur usage sûr comme destination finale des déchets contenant des PFAS.'),
        ['rev'], doi='10.1021/acs.est.2c02251'),
    ref('U.S. EPA · 2026 (actualización anual desde 2025)',
        'Interim Guidance on the Destruction and Disposal of PFAS and Materials Containing PFAS',
        t('Guía no vinculante de la agencia ambiental de EE. UU. sobre las tres opciones disponibles a gran escala: incineración, vertederos e inyección en pozos profundos. Describe el estado de la ciencia y las incertidumbres de cada una. La edición de 2026 reconoce que la incineración puede ser eficaz, pero insiste en vigilar de cerca las condiciones de operación.',
          'Non-binding guidance from the US environmental agency on the three options available at scale: incineration, landfills and deep-well injection. It describes the state of the science and the uncertainties for each. The 2026 edition recognizes incineration can be effective, but stresses that operating conditions must be closely monitored.',
          'Guide non contraignant de l’agence américaine de l’environnement sur les trois options disponibles à grande échelle : incinération, décharges et injection en puits profonds. Il décrit l’état des connaissances et les incertitudes de chacune. L’édition 2026 reconnaît que l’incinération peut être efficace, mais insiste sur la surveillance étroite des conditions d’exploitation.'),
        ['ag'], url='https://www.epa.gov/pfas/interim-guidance-destroying-and-disposing-certain-pfas-and-pfas-containing-materials-are-not', label='epa.gov/pfas'),
]), t('Ninguna de las dos fuentes mide qué sale de una chimenea concreta: resumen lo que se sabe y lo que falta. Los vertederos y los pozos no destruyen nada; solo contienen.',
      'Neither source measures what comes out of a specific stack: they summarize what is known and what is missing. Landfills and wells destroy nothing; they only contain.',
      'Aucune des deux sources ne mesure ce qui sort d’une cheminée précise : elles résument ce que l’on sait et ce qui manque. Les décharges et les puits ne détruisent rien ; ils ne font que contenir.')))

S.append(section(t('Electricidad y luz', 'Electricity and light', 'Électricité et lumière'), '\n'.join([
    ref('U.S. EPA, Office of Research and Development · Research Brief · 2021',
        'Potential PFAS Destruction Technology: Electrochemical Oxidation',
        t('La oxidación electroquímica hace pasar corriente por el agua para arrancar electrones a los PFAS y quitarles el flúor. Ha eliminado PFOA y PFOS en varios estudios y gasta menos energía que incinerar, pero la EPA la sitúa en un nivel de madurez intermedio: casi todas las pruebas se hicieron con agua limpia de laboratorio, los electrodos de diamante dopado con boro son caros y, si hay cloruro, se forma perclorato, otro contaminante.',
          'Electrochemical oxidation passes current through water to strip electrons from PFAS and remove their fluorine. It has removed PFOA and PFOS in several studies and uses less energy than incineration, but the EPA rates it at an intermediate readiness level: nearly all tests used clean lab water, boron-doped diamond electrodes are expensive and, if chloride is present, it forms perchlorate, another pollutant.',
          'L’oxydation électrochimique fait passer un courant dans l’eau pour arracher des électrons aux PFAS et leur retirer le fluor. Elle a éliminé le PFOA et le PFOS dans plusieurs études et consomme moins d’énergie que l’incinération, mais l’EPA la classe à un niveau de maturité intermédiaire : presque tous les essais ont utilisé de l’eau propre de laboratoire, les électrodes en diamant dopé au bore sont chères et, en présence de chlorure, il se forme du perchlorate, un autre polluant.'),
        ['ag'], url='https://www.epa.gov/sites/default/files/2021-01/documents/pitt_research_brief_electrochemical_oxidation_final_jan_25_2021_508.pdf', label='epa.gov · PDF'),
    ref('González Fernández LA, Medellín Castillo NA, Sánchez Polo M, et al. · Catalysts · 2025; 15: 946',
        'Emerging Strategies for the Photoassisted Removal of PFAS from Water: From Fundamentals to Applications',
        t('Revisión de un equipo de la Universidad Autónoma de San Luis Potosí (México) con Granada y Ulm. Repasa la luz ultravioleta de vacío, la fotocatálisis, el persulfato activado con luz y el foto-Fenton. Algunas lámparas ultravioleta quitan el flúor al PFOA rápido sin añadir químicos, pero gastan mucha energía; el agua real (nitratos, cloruros, pH) frena las reacciones, la degradación incompleta deja PFAS más cortos y la luz solar casi no sirve.',
          'Review by a team from the Autonomous University of San Luis Potosí (Mexico) with Granada and Ulm. It covers vacuum ultraviolet light, photocatalysis, light-activated persulfate and photo-Fenton. Some UV lamps defluorinate PFOA quickly without added chemicals, but use a lot of energy; real water (nitrates, chlorides, pH) slows the reactions, incomplete degradation leaves shorter PFAS and sunlight barely works.',
          'Revue d’une équipe de l’Université autonome de San Luis Potosí (Mexique) avec Grenade et Ulm. Elle passe en revue l’ultraviolet du vide, la photocatalyse, le persulfate activé par la lumière et le photo-Fenton. Certaines lampes UV défluorent rapidement le PFOA sans ajout de produits, mais consomment beaucoup d’énergie ; l’eau réelle (nitrates, chlorures, pH) freine les réactions, la dégradation incomplète laisse des PFAS plus courts et la lumière du soleil ne sert presque à rien.'),
        ['rev'], doi='10.3390/catal15100946'),
]), t('El informe de la EPA es de 2021 y la propia agencia aclara que no respalda la tecnología. Ninguna de estas técnicas se ha demostrado aún tratando ríos o acuíferos: se aplican a concentrados pequeños, como la salmuera de la ósmosis.',
      'The EPA brief is from 2021 and the agency itself says it doesn’t endorse the technology. None of these techniques has yet been shown to treat rivers or aquifers: they are applied to small concentrates, such as reverse-osmosis brine.',
      'Le rapport de l’EPA date de 2021 et l’agence précise qu’elle ne cautionne pas la technologie. Aucune de ces techniques n’a encore fait ses preuves sur des rivières ou des nappes : on les applique à de petits concentrats, comme la saumure de l’osmose.')))

S.append(section(t('Química nueva en el laboratorio', 'New chemistry in the lab', 'Nouvelle chimie au laboratoire'), '\n'.join([
    ref('Trang B, Li Y, Xue XS, et al. · Science · 2022; 377(6608): 839–845',
        'Low-temperature mineralization of perfluorocarboxylic acids',
        t('Con sosa (NaOH) en una mezcla de dimetilsulfóxido y agua, a 80–120 °C y presión normal, mineralizaron ácidos perfluorocarboxílicos como el PFOA y el GenX: liberaron entre el 78 % y casi el 100 % del flúor en 24 horas. El PFOS, un sulfonato, no se degradó, y el ácido trifluoroacético, de cadena muy corta, se degradó muy despacio.',
          'Using lye (NaOH) in a dimethyl sulfoxide–water mix, at 80–120 °C and normal pressure, they mineralized perfluorocarboxylic acids such as PFOA and GenX, releasing 78% to nearly 100% of the fluorine within 24 hours. PFOS, a sulfonate, did not degrade, and very-short-chain trifluoroacetic acid degraded very slowly.',
          'Avec de la soude (NaOH) dans un mélange de diméthylsulfoxyde et d’eau, à 80–120 °C et pression normale, ils ont minéralisé des acides perfluorocarboxyliques comme le PFOA et le GenX, libérant de 78 % à presque 100 % du fluor en 24 heures. Le PFOS, un sulfonate, ne s’est pas dégradé, et l’acide trifluoroacétique, à chaîne très courte, s’est dégradé très lentement.'),
        ['lab'], doi='10.1126/science.abm8868'),
    ref('Yang L, Chen Z, Goult CA, et al. · Nature · 2025; 640(8057): 100–106',
        'Phosphate-enabled mechanochemical PFAS destruction for fluoride reuse',
        t('Molieron PFAS con sales de fosfato de potasio, sin disolventes, en un molino de bolas. Destruyeron varias clases de PFAS, incluidos plásticos fluorados como el teflón (PTFE), y recuperaron el flúor en forma de sales útiles para fabricar otros compuestos. El fosfato se puede reutilizar.',
          'They ground PFAS with potassium phosphate salts, without solvents, in a ball mill. They destroyed several PFAS classes, including fluorinated plastics such as Teflon (PTFE), and recovered the fluorine as salts that can be used to make other compounds. The phosphate can be reused.',
          'Ils ont broyé des PFAS avec des sels de phosphate de potassium, sans solvant, dans un broyeur à billes. Ils ont détruit plusieurs classes de PFAS, dont des plastiques fluorés comme le téflon (PTFE), et récupéré le fluor sous forme de sels réutilisables pour fabriquer d’autres composés. Le phosphate peut être réutilisé.'),
        ['lab'], doi='10.1038/s41586-025-08698-5'),
]), t('Son experimentos con PFAS puros o concentrados, en cantidades de laboratorio. No demuestran que funcionen con agua contaminada real ni a escala industrial, ni cuánto costarían.',
      'These are experiments with pure or concentrated PFAS, in lab quantities. They don’t show that the methods work on real contaminated water or at industrial scale, or what they would cost.',
      'Ce sont des expériences sur des PFAS purs ou concentrés, en quantités de laboratoire. Elles ne montrent pas que ces méthodes fonctionnent sur de l’eau contaminée réelle ni à l’échelle industrielle, ni ce qu’elles coûteraient.')))

S.append(section(t('¿Y los microbios?', 'What about microbes?', 'Et les microbes&nbsp;?'), '\n'.join([
    ref('Smorada CM, Sima MW, Jaffé PR · Current Opinion in Biotechnology · 2024; 88: 103170',
        'Bacterial degradation of perfluoroalkyl acids',
        t('Revisa las bacterias y genes capaces de quitar flúor a los PFAS más resistentes (ácidos perfluorados como el PFOA y el PFOS), con y sin oxígeno. La mayoría de los estudios trabajan con PFAS polifluorados, más fáciles de atacar; para los perfluorados la evidencia es escasa y falta pasar del laboratorio al ambiente.',
          'Reviews the bacteria and genes able to strip fluorine from the most resistant PFAS (perfluorinated acids such as PFOA and PFOS), with and without oxygen. Most studies work with polyfluorinated PFAS, which are easier to attack; for perfluorinated ones the evidence is thin and the jump from lab to environment is still missing.',
          'Passe en revue les bactéries et les gènes capables d’arracher le fluor des PFAS les plus résistants (acides perfluorés comme le PFOA et le PFOS), avec et sans oxygène. La plupart des études portent sur des PFAS polyfluorés, plus faciles à attaquer ; pour les perfluorés, les preuves sont minces et le passage du laboratoire à l’environnement reste à faire.'),
        ['rev'], doi='10.1016/j.copbio.2024.103170'),
]), t(f'Con los estrógenos los microbios sí ayudan; con los PFAS, casi nada. Lo contamos en <a href="{WATER}">Disruptores endocrinos: ¿ya están en el agua?</a>',
      f'Microbes do help with estrogens; with PFAS, barely. See <a href="{WATER}#en">Endocrine disruptors: are they already in the water?</a>',
      f'Les microbes aident pour les œstrogènes ; pour les PFAS, presque pas. Voir <a href="{WATER}#fr">Perturbateurs endocriniens&nbsp;: sont-ils déjà dans l’eau&nbsp;?</a>')))

S.append(section(t('¿Limpiar o dejar de emitir?', 'Clean up or stop emitting?', 'Dépolluer ou arrêter d’émettre&nbsp;?'), '\n'.join([
    ref('Ling AL, Aubert R, Bersi E, Horel S, Arp HPH · Environmental Science: Processes &amp; Impacts · 2026',
        'PFAS remediation across Europe: costs and limited impacts',
        t('Estima cuánto costaría limpiar los PFAS en Europa. Sanear la contaminación heredada costaría entre 1000 y 6000 millones de euros al año; seguir limpiando lo que se emite hoy, entre 52 000 y 200 000 millones al año. Aun en el escenario más ambicioso se retirarían solo 3–50 toneladas al año, menos del 2 % de las emisiones actuales. Los autores concluyen que la limpieza sola no basta y que reducir las emisiones en origen es mucho más eficaz.',
          'Estimates what it would cost to clean up PFAS in Europe. Remediating legacy pollution would cost €1–6 billion a year; continuing to clean up what is emitted today, €52–200 billion a year. Even in the most ambitious scenario, only 3–50 tonnes a year would be removed, less than 2% of current emissions. The authors conclude that cleanup alone isn’t enough and that cutting emissions at source is far more effective.',
          'Estime le coût de la dépollution des PFAS en Europe. Traiter la pollution héritée coûterait de 1 à 6 milliards d’euros par an ; continuer à nettoyer ce qui est émis aujourd’hui, de 52 à 200 milliards par an. Même dans le scénario le plus ambitieux, seules 3 à 50 tonnes par an seraient retirées, moins de 2 % des émissions actuelles. Les auteurs concluent que la dépollution seule ne suffit pas et que réduire les émissions à la source est bien plus efficace.'),
        ['db'], doi='10.1039/d5em00870k'),
]), t('Es un modelo económico para Europa: sus cifras dependen de los supuestos sobre emisiones y precios de tratamiento, y no se pueden trasladar tal cual a América. Participaron periodistas del Forever Pollution Project.',
      'It’s an economic model for Europe: its figures depend on assumptions about emissions and treatment prices, and can’t be transferred as-is to the Americas. Journalists from the Forever Pollution Project took part.',
      'C’est un modèle économique pour l’Europe : ses chiffres dépendent des hypothèses sur les émissions et les prix de traitement, et ne se transposent pas tels quels à l’Amérique. Des journalistes du Forever Pollution Project y ont participé.')))

def row(where, what, status, links):
    a = ' '.join(f'<a href="{u}">{n}</a>' for n, u in links)
    cls, label = status
    return f'        <tr><td>{where}</td><td>{what} {a}</td><td><span class="st {cls}">{label}</span></td></tr>'

reg_rows = [
    row(t('Mundial', 'Global', 'Monde'), t('Convenio de Estocolmo: el PFOS está restringido desde 2009 y el PFOA (2019), el PFHxS (2022) y los ácidos perfluorocarboxílicos de cadena larga (2025) están en la lista de eliminación. México y Brasil son parte del convenio.',
              'Stockholm Convention: PFOS has been restricted since 2009, and PFOA (2019), PFHxS (2022) and long-chain perfluorocarboxylic acids (2025) are on the elimination list. Mexico and Brazil are parties to the convention.',
              'Convention de Stockholm : le PFOS est restreint depuis 2009, et le PFOA (2019), le PFHxS (2022) et les acides perfluorocarboxyliques à chaîne longue (2025) figurent sur la liste d’élimination. Le Mexique et le Brésil sont parties à la convention.'),
        ('ok', t('Vigente', 'In force', 'En vigueur')), [('pops.int', 'https://chm.pops.int/Implementation/IndustrialPOPs/PFAS/Overview/tabid/5221/Default.aspx')]),
    row(t('Unión Europea', 'European Union', 'Union européenne'), t('Restricción universal de los PFAS como grupo: el comité de riesgos (RAC) apoyó una prohibición amplia en marzo de 2026; el comité socioeconómico (SEAC) prefiere prohibir con excepciones por uso y dará su opinión final a finales de 2026. Después decide la Comisión.',
              'Universal restriction of PFAS as a group: the risk committee (RAC) backed a broad ban in March 2026; the socio-economic committee (SEAC) prefers a ban with use-specific exemptions and will give its final opinion by the end of 2026. Then the Commission decides.',
              'Restriction universelle des PFAS en tant que groupe : le comité d’évaluation des risques (RAC) a soutenu une interdiction large en mars 2026 ; le comité d’analyse socio-économique (SEAC) préfère une interdiction avec dérogations par usage et rendra son avis final fin 2026. La Commission décidera ensuite.'),
        ('part', t('En evaluación', 'Under evaluation', 'En évaluation')), [('Linklaters, abr 2026', 'https://sustainablefutures.linklaters.com/post/102mp62/eu-universal-pfas-restriction-process-enters-its-decisive-phase-seac-draft-opin')]),
    row(t('EE. UU.', 'USA', 'États-Unis'), t('Guía de la EPA sobre destrucción y eliminación de PFAS (incineración, vertederos, pozos), actualizada cada año desde 2025.',
              'EPA guidance on destroying and disposing of PFAS (incineration, landfills, wells), updated yearly since 2025.',
              'Guide de l’EPA sur la destruction et l’élimination des PFAS (incinération, décharges, puits), mis à jour chaque année depuis 2025.'),
        ('part', t('No vinculante', 'Non-binding', 'Non contraignant')), [('epa.gov', 'https://www.epa.gov/pfas/interim-guidance-destroying-and-disposing-certain-pfas-and-pfas-containing-materials-are-not')]),
    row(t('EE. UU.', 'USA', 'États-Unis'), t('El Departamento de Defensa suspendió la incineración de espumas contra incendios con PFAS; levantó la moratoria y su guía de febrero de 2026 vuelve a admitirla.',
              'The Department of Defense halted incineration of PFAS firefighting foams; it lifted the moratorium and its February 2026 guidance allows it again.',
              'Le département de la Défense avait suspendu l’incinération des mousses anti-incendie aux PFAS ; il a levé le moratoire et son guide de février 2026 l’autorise de nouveau.'),
        ('rev', t('Revertida', 'Rolled back', 'Annulée')), [('Waste Dive', 'https://www.wastedive.com/news/afff-foam-pfas-management-incineration-pause-lift-effects/824442/')]),
    row(t('México', 'Mexico', 'Mexique'), t('Parte del Convenio de Estocolmo desde 2003, pero sin norma propia sobre cómo tratar o destruir residuos con PFAS ni límites de PFAS en el agua potable.',
              'A party to the Stockholm Convention since 2003, but with no national rule on how to treat or destroy PFAS waste, and no PFAS limits in drinking water.',
              'Partie à la convention de Stockholm depuis 2003, mais sans règle nationale sur le traitement ou la destruction des déchets contenant des PFAS, ni limite de PFAS dans l’eau potable.'),
        ('part', t('Sin norma específica', 'No specific rule', 'Pas de règle spécifique')), [('NOM-127-SSA1-2021', 'https://faolex.fao.org/docs/pdf/mex215630.pdf')]),
    row(t('Brasil', 'Brazil', 'Brésil'), t('Proyecto de ley de política nacional de PFAS (PL 2726/2023): sustitución por alternativas más seguras, vigilancia sanitaria y etiquetado. Sigue en comisiones de la Cámara de Diputados.',
              'Bill for a national PFAS policy (PL 2726/2023): substitution with safer alternatives, health surveillance and labelling. Still in Chamber of Deputies committees.',
              'Projet de loi de politique nationale sur les PFAS (PL 2726/2023) : substitution par des alternatives plus sûres, surveillance sanitaire et étiquetage. Toujours en commission à la Chambre des députés.'),
        ('part', t('Sin aprobar', 'Not passed', 'Non adopté')), [('PL 2726/2023', 'https://chemical.chemlinked.com/news/chemical-news/brazil-moves-towards-legislative-efforts-on-pfas-control')]),
]

REG = f'''  <section>
    <div class="frame"><h2>{t('Regulación en Europa y América', 'Regulation in Europe and the Americas', 'Réglementation en Europe et en Amérique')}</h2></div>
    <p class="note">{t(f'Normas sobre producir, emitir y destruir PFAS. Los límites en agua potable están en <a href="{WATER}">el tema del agua</a>; los de alimentos y cosméticos, en <a href="{HEALTH}">el de salud</a>.',
                       f'Rules on producing, emitting and destroying PFAS. Drinking-water limits are in <a href="{WATER}#en">the water topic</a>; food and cosmetics limits in <a href="{HEALTH}#en">the health topic</a>.',
                       f'Règles sur la production, l’émission et la destruction des PFAS. Les limites dans l’eau potable sont dans <a href="{WATER}#fr">le sujet sur l’eau</a> ; celles des aliments et cosmétiques dans <a href="{HEALTH}#fr">le sujet santé</a>.')}</p>
    <div class="reg-wrap">
    <table class="reg">
      <thead><tr><th>{t('Dónde', 'Where', 'Où')}</th><th>{t('Qué', 'What', 'Quoi')}</th><th>{t('Estado', 'Status', 'Statut')}</th></tr></thead>
      <tbody>
{chr(10).join(reg_rows)}
      </tbody>
    </table>
    </div>
  </section>
'''

LEGEND = f'''  <div class="legend">
    <p><span class="chip rev">{CH['rev'][1]}</span><span>{t('Síntesis de expertos sobre lo publicado.', 'Expert synthesis of the published work.', 'Synthèse d’experts sur les travaux publiés.')}</span></p>
    <p><span class="chip rev">{CH['ag'][1]}</span><span>{t('Guía o informe de una agencia pública (aquí, la EPA de EE. UU.).', 'Guidance or report from a public agency (here, the US EPA).', 'Guide ou rapport d’une agence publique (ici, l’EPA américaine).')}</span></p>
    <p><span class="chip obs">{CH['obs'][1]}</span><span>{t('Datos medidos en condiciones reales (aquí, en hogares).', 'Data measured in real conditions (here, in homes).', 'Données mesurées en conditions réelles (ici, dans des foyers).')}</span></p>
    <p><span class="chip lab">{CH['lab'][1]}</span><span>{t('Experimento de laboratorio: demuestra que algo es posible, no que funcione a gran escala.', 'Lab experiment: shows something is possible, not that it works at scale.', 'Expérience de laboratoire : montre que quelque chose est possible, pas que cela fonctionne à grande échelle.')}</span></p>
    <p><span class="chip db">{CH['db'][1]}</span><span>{t('Estimación calculada a partir de otros datos: depende de sus supuestos.', 'Estimate calculated from other data: depends on its assumptions.', 'Estimation calculée à partir d’autres données : dépend de ses hypothèses.')}</span></p>
  </div>
'''

TITLE = t('¿Se pueden destruir los PFAS?', 'Can PFAS be destroyed?', 'Peut-on détruire les PFAS&nbsp;?')

page = f'''<!doctype html>
<html lang="es" data-lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>¿Se pueden destruir los PFAS? · Ciencia para compartir</title>
<meta name="description" content="Las fuentes detrás de la story sobre cómo eliminar y destruir los PFAS: filtros, incineración, electroquímica, luz, química nueva, microbios, costes y regulación en Europa y América. / The sources behind the story on removing and destroying PFAS.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=DM+Sans:wght@400;500;700&display=swap">
<link rel="stylesheet" href="../../assets/style.css">
</head>
<body>
{HORIZON}

<main class="wrap">
  <header>
    <div class="top">
      <a class="eyebrow" href="../">{t('← Ciencia y tecnología', '← Science and technology', '← Science et technologie')}</a>
      <div class="lang" role="group" aria-label="Idioma / Language / Langue">
        <button type="button" id="btn-es" data-set="es" aria-pressed="true">ES</button>
        <button type="button" id="btn-en" data-set="en" aria-pressed="false">EN</button>
        <button type="button" id="btn-fr" data-set="fr" aria-pressed="false">FR</button>
      </div>
    </div>
    <h1>{t('¿Se pueden destruir los PFAS? <em>Las fuentes</em>', 'Can PFAS be destroyed? <em>The sources</em>', 'Peut-on détruire les PFAS&nbsp;? <em>Les sources</em>')}</h1>
    <p class="lede">{t(f'Los PFAS ya están en ríos, acuíferos y agua potable (<a href="{WATER}">lo contamos aquí</a>). ¿Qué puede hacer la tecnología? Sacarlos del agua es posible; destruirlos de verdad, mucho más difícil. Aquí están los estudios detrás de cada idea de la story, qué tipo de evidencia es cada uno y lo que no demuestra.',
                       f'PFAS are already in rivers, aquifers and drinking water (<a href="{WATER}#en">covered here</a>). What can technology do? Taking them out of water is possible; truly destroying them is much harder. Here are the studies behind each idea in the story, what kind of evidence each one is and what it doesn’t show.',
                       f'Les PFAS sont déjà dans les rivières, les nappes et l’eau potable (<a href="{WATER}#fr">nous en parlons ici</a>). Que peut faire la technologie&nbsp;? Les retirer de l’eau est possible ; les détruire vraiment, beaucoup plus difficile. Voici les études derrière chaque idée de la story, le type de preuve de chacune et ce qu’elle ne montre pas.')}</p>
    <p class="reviewed">{t('Evidencia revisada: oct 2026', 'Evidence reviewed: Oct 2026', 'Preuves revues : oct. 2026')}</p>
  </header>

{LEGEND}
{''.join(S)}{REG}
  <section>
    <div class="frame"><h2>{t('La story', 'The story', 'La story')}</h2></div>
    <img class="preview" src="preview.png" alt="Las stories en español, inglés y francés: ¿Se pueden destruir los PFAS? / Can PFAS be destroyed? / Peut-on détruire les PFAS ?" width="1600" height="900" loading="lazy">
  </section>

  <footer>
    <p>{t('Contenido divulgativo; no sustituye el consejo médico ni profesional. Si te preocupa el agua de tu casa, consulta los análisis de tu proveedor o de la autoridad sanitaria local antes de comprar un filtro.', 'For general information only; not medical or professional advice. If you’re concerned about your tap water, check your supplier’s or local health authority’s test results before buying a filter.', 'Contenu de vulgarisation ; ne remplace pas un avis médical ou professionnel. Si l’eau de votre robinet vous préoccupe, consultez les analyses de votre distributeur ou de l’autorité sanitaire locale avant d’acheter un filtre.')}</p>
    <p>Antonio Puriel Hernández · <a href="../../">{t('Ciencia para compartir', 'Science to share', 'La science à partager')}</a> · <a href="../">{t('Más temas', 'More topics', 'Plus de sujets')}</a></p>
  </footer>
</main>
<script src="../../assets/lang.js"></script>
</body>
</html>
'''
(OUT / 'index.html').write_text(page)
print('ok', len(page))
