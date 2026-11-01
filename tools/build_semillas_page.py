"""Genera ciencia-salud/semillas/index.html (ES/EN/FR).
Miniserie en una página: ancestral, antiinflamatorio, intestino y moda, más una tabla de semillas,
la regulación y el bloque «Temas relacionados» que enlaza con dieta ancestral, dieta e inflamación
y la serie intestino."""
import sys, pathlib
import healthkit
from healthkit import t, section, ref, legend, page

OUT = pathlib.Path(sys.argv[1])
NB = '&nbsp;'

# Etiqueta propia de este tema: datación arqueológica o genética de cultivos.
healthkit.CH['arq'] = ('obs', t('Arqueología', 'Archaeology', 'Archéologie'))
healthkit.LEGEND_ITEMS['arq'] = t(
    'Restos de plantas fechados o genética de cultivos: dicen desde cuándo se come algo, no si es sano.',
    'Dated plant remains or crop genetics: they tell us how long something has been eaten, not whether it’s healthy.',
    'Restes de plantes datés ou génétique des cultures : ils disent depuis quand on mange quelque chose, pas si c’est sain.')

S = []

S.append(section(t('¿Alimento ancestral?', 'Ancestral food?', 'Aliment ancestral ?'), '\n'.join([
    ref('Smith BD · Science · 1997; 276(5314): 932–934',
        'The Initial Domestication of <i>Cucurbita pepo</i> in the Americas 10,000 Years Ago',
        t('En la cueva de Guilá Naquitz (Oaxaca, México) aparecieron semillas, tallos y cáscaras de calabaza más grandes que las silvestres. Nueve fechados por radiocarbono sitúan su cultivo hace entre 10 000 y 8000 años, más de 4000 años antes que el maíz y el frijol. La calabaza es la primera planta domesticada conocida en América.',
          'Seeds, stems and rind fragments of squash larger than wild ones turned up in Guilá Naquitz cave (Oaxaca, Mexico). Nine radiocarbon dates place their cultivation 10,000 to 8,000 years ago, more than 4,000 years before maize and beans. Squash is the earliest known domesticated plant in the Americas.',
          'Dans la grotte de Guilá Naquitz (Oaxaca, Mexique), on a trouvé des graines, pédoncules et morceaux d’écorce de courge plus grands que ceux des formes sauvages. Neuf datations au radiocarbone situent leur culture il y a 10 000 à 8000 ans, plus de 4000 ans avant le maïs et le haricot. La courge est la plus ancienne plante domestiquée connue en Amérique.'),
        ['arq'], doi='10.1126/science.276.5314.932', old=True),
    ref('Fu YB · Scientific Reports · 2025; 15: 8731',
        'Flax domestication processes as inferred from genome-wide SNP data',
        t('La linaza es uno de los cultivos fundadores del Creciente Fértil, domesticada para aceite y fibra. Con el genoma de 93 muestras, el estudio reconstruye varias domesticaciones y estima que la linaza de aceite y la de fibra llegaron a Europa hace unos 5800 años.',
          'Flax is one of the founder crops of the Fertile Crescent, domesticated for oil and fibre. Using genomes from 93 samples, the study reconstructs several domestication events and estimates that oil and fibre flax reached Europe about 5,800 years ago.',
          'Le lin est l’une des cultures fondatrices du Croissant fertile, domestiqué pour l’huile et la fibre. À partir du génome de 93 échantillons, l’étude reconstitue plusieurs domestications et estime que le lin à huile et le lin à fibre sont arrivés en Europe il y a environ 5800 ans.'),
        ['arq'], doi='10.1038/s41598-025-89498-9'),
]), t('Que algo se coma desde hace milenios no demuestra que sea sano: solo que no es una moda nueva. Fu 2025 parte de una fecha supuesta de domesticación (10 000 años) para calcular las demás. La tabla de abajo reúne otras semillas con historia larga.',
      'Something being eaten for millennia doesn’t show it’s healthy, only that it isn’t a new fad. Fu 2025 starts from an assumed domestication date (10,000 years) to estimate the others. The table below gathers other seeds with a long history.',
      'Qu’on mange quelque chose depuis des millénaires ne prouve pas que ce soit sain : seulement que ce n’est pas une mode récente. Fu 2025 part d’une date de domestication supposée (10 000 ans) pour estimer les autres. Le tableau ci-dessous réunit d’autres graines à longue histoire.')))

S.append(section(t('¿Antiinflamatorio?', 'Anti-inflammatory?', 'Anti-inflammatoire ?'), '\n'.join([
    ref('Musazadeh V, Morovatshoar R, Kavyani Z, Vajdi M, Askari G · Prostaglandins &amp; Other Lipid Mediators · 2024; 174: 106868',
        'Effects of flaxseed supplementation on inflammatory biomarkers: A GRADE-assessed systematic review and meta-analysis of randomized controlled trials',
        t('54 ensayos con unas 3000 personas de 12 países. La linaza bajó la proteína C reactiva (PCR) y la interleucina 6 (IL-6), dos marcadores de inflamación en sangre, pero no el TNF-α. La diferencia entre estudios fue muy alta (I² de 83 a 93 %).',
          '54 trials with about 3,000 people from 12 countries. Flaxseed lowered C-reactive protein (CRP) and interleukin 6 (IL-6), two blood markers of inflammation, but not TNF-α. Differences between studies were very large (I² 83 to 93%).',
          '54 essais avec environ 3000 personnes de 12 pays. Le lin a fait baisser la protéine C réactive (CRP) et l’interleukine 6 (IL-6), deux marqueurs sanguins d’inflammation, mais pas le TNF-α. Les différences entre études étaient très fortes (I² de 83 à 93 %).'),
        ['meta'], doi='10.1016/j.prostaglandins.2024.106868'),
    ref('Yang C, Xia H, Wan M, et al. · Nutrition &amp; Metabolism · 2021; 18: 91',
        'Comparisons of the effects of different flaxseed products consumption on lipid profiles, inflammatory cytokines and anthropometric indices in patients with dyslipidemia related diseases',
        t('31 ensayos con 1698 personas con colesterol alto, sobrepeso o hígado graso. Depende del producto: la linaza entera bajó el colesterol total, el LDL y los triglicéridos; el aceite de linaza no cambió los lípidos, pero bajó la IL-6 y la PCR ultrasensible. En conjunto, la PCR no cambió.',
          '31 trials with 1,698 people with high cholesterol, overweight or fatty liver. It depends on the product: whole flaxseed lowered total cholesterol, LDL and triglycerides; flaxseed oil didn’t change lipids but lowered IL-6 and high-sensitivity CRP. Overall, CRP didn’t change.',
          '31 essais avec 1698 personnes ayant un cholestérol élevé, un surpoids ou une stéatose. Cela dépend du produit : le lin entier a fait baisser le cholestérol total, le LDL et les triglycérides ; l’huile de lin n’a pas modifié les lipides mais a fait baisser l’IL-6 et la CRP ultrasensible. Globalement, la CRP n’a pas changé.'),
        ['meta'], doi='10.1186/s12986-021-00619-3'),
    ref('Archives of Medical Science · 2019; 15(1): 12–22',
        'A systematic review and meta-analysis of clinical trials investigating the effects of flaxseed supplementation on plasma C-reactive protein concentrations',
        t('17 ensayos con 1256 personas. La linaza no cambió la PCR de forma significativa (−0,25 mg/L, con un intervalo que incluye el cero), con ningún tipo de producto.',
          '17 trials with 1,256 people. Flaxseed didn’t significantly change CRP (−0.25 mg/L, with an interval that includes zero), with any type of product.',
          '17 essais avec 1256 personnes. Le lin n’a pas modifié significativement la CRP (−0,25 mg/L, avec un intervalle qui inclut zéro), quel que soit le produit.'),
        ['meta'], doi='10.5114/aoms.2018.81034', old=True),
    ref('Ren G-Y, Chen C-Y, et al. · Nutrients · 2016; 8(3): 136',
        'Effect of Flaxseed Intervention on Inflammatory Marker C-Reactive Protein: A Systematic Review and Meta-Analysis of Randomized Controlled Trials',
        t('20 estudios. En conjunto, la linaza no bajó la PCR. Solo hubo efecto en personas con obesidad (IMC de 30 o más): −0,83 mg/L.',
          '20 studies. Overall, flaxseed didn’t lower CRP. There was only an effect in people with obesity (BMI 30 or more): −0.83 mg/L.',
          '20 études. Globalement, le lin n’a pas fait baisser la CRP. Il n’y a eu d’effet que chez les personnes obèses (IMC de 30 ou plus) : −0,83 mg/L.'),
        ['meta'], doi='10.3390/nu8030136', old=True),
]), t('Los metaanálisis no coinciden: el más grande y reciente ve una bajada; los anteriores, no, salvo en obesidad o con el aceite. Bajar la PCR o la IL-6 es un cambio en un marcador, no la prueba de que se prevenga una enfermedad. Casi no hay datos de chía, girasol, calabaza o sésamo sobre inflamación.',
      'The meta-analyses disagree: the largest and most recent sees a drop; the earlier ones don’t, except in obesity or with the oil. Lowering CRP or IL-6 is a change in a marker, not proof that a disease is prevented. There’s almost no data on chia, sunflower, pumpkin or sesame and inflammation.',
      'Les méta-analyses ne concordent pas : la plus grande et la plus récente voit une baisse ; les précédentes non, sauf en cas d’obésité ou avec l’huile. Faire baisser la CRP ou l’IL-6 est un changement de marqueur, pas la preuve qu’une maladie est évitée. Il n’y a presque pas de données sur le chia, le tournesol, la courge ou le sésame et l’inflammation.')))

S.append(section(t('En el intestino', 'In the gut', 'Dans l’intestin'), '\n'.join([
    ref('Lagkouvardos I, Kläring K, Heinzmann SS, et al. · Molecular Nutrition &amp; Food Research · 2015; 59(8): 1614–1628',
        'Gut metabolites and bacterial community networks during a pilot intervention study with flaxseeds in healthy adult men',
        t('Nueve hombres sanos comieron 0,3 g de linaza por kilo de peso al día durante una semana. Subieron en sangre los enterolignanos, que las bacterias fabrican a partir de los lignanos de la linaza. La comunidad dominante de bacterias apenas cambió. La enterolactona se relacionó con dos especies de <i>Ruminococcus</i>.',
          'Nine healthy men ate 0.3 g of flaxseed per kilo of body weight a day for one week. Blood enterolignans rose; bacteria make them from flaxseed lignans. The dominant bacterial community barely changed. Enterolactone was linked to two <i>Ruminococcus</i> species.',
          'Neuf hommes en bonne santé ont mangé 0,3 g de lin par kilo de poids et par jour pendant une semaine. Les entérolignanes, que les bactéries fabriquent à partir des lignanes du lin, ont augmenté dans le sang. La communauté bactérienne dominante a peu changé. L’entérolactone était liée à deux espèces de <i>Ruminococcus</i>.'),
        ['rct'], doi='10.1002/mnfr.201500125', old=True),
    ref('Senizza A, Rocchetti G, Mosele JI, et al. · Molecules · 2020; 25(23): 5709',
        'Lignans and Gut Microbiota: An Interplay Revealing Potential Health Implications',
        t('Las semillas oleaginosas (linaza, sésamo, girasol) son las fuentes más ricas de lignanos. La mayor parte llega al colon, donde unas pocas especies de bacterias los convierten en enterodiol y enterolactona. Cuánto se produce varía mucho de una persona a otra, según su microbiota.',
          'Oilseeds (flax, sesame, sunflower) are the richest sources of lignans. Most reach the colon, where a few bacterial species turn them into enterodiol and enterolactone. How much is produced varies widely between people, depending on their microbiota.',
          'Les graines oléagineuses (lin, sésame, tournesol) sont les sources les plus riches en lignanes. La plupart arrivent au côlon, où quelques espèces bactériennes les transforment en entérodiol et entérolactone. La quantité produite varie beaucoup d’une personne à l’autre, selon son microbiote.'),
        ['rev']),
    ref('So D, Whelan K, Rossi M, et al. · American Journal of Clinical Nutrition · 2018; 107(6): 965–983',
        'Dietary fiber intervention on gut microbiota composition in healthy adults: a systematic review and meta-analysis',
        t('64 estudios con 2099 adultos sanos, con fibra de todo tipo (no solo de semillas). Más fibra subió las bifidobacterias y los lactobacilos, y el butirato en heces quedó justo en el límite de la significación. La diversidad de la microbiota no cambió.',
          '64 studies with 2,099 healthy adults, with all kinds of fibre (not just from seeds). More fibre raised bifidobacteria and lactobacilli, and faecal butyrate was right at the edge of significance. Microbiota diversity didn’t change.',
          '64 études avec 2099 adultes en bonne santé, avec tous types de fibres (pas seulement des graines). Plus de fibres a augmenté les bifidobactéries et les lactobacilles, et le butyrate fécal était tout juste à la limite de la significativité. La diversité du microbiote n’a pas changé.'),
        ['meta'], doi='10.1093/ajcn/nqy041', old=True),
    ref('Tian Y, Zhou Y, Liao W, et al. · Food &amp; Function · 2025; 16: 1389',
        'Flaxseed powder supplementation in non-alcoholic fatty liver disease: a randomized controlled clinical trial',
        t('50 personas con hígado graso, 12 semanas, la mitad con linaza en polvo además de una dieta sana. En el grupo de linaza subieron <i>Bifidobacterium</i> y otros grupos que fermentan fibra, como <i>Lachnospiraceae</i>.',
          '50 people with fatty liver, 12 weeks, half with flaxseed powder on top of a healthy diet. In the flaxseed group, <i>Bifidobacterium</i> and other fibre-fermenting groups such as <i>Lachnospiraceae</i> rose.',
          '50 personnes atteintes de stéatose, 12 semaines, la moitié avec de la poudre de lin en plus d’une alimentation saine. Dans le groupe lin, <i>Bifidobacterium</i> et d’autres groupes qui fermentent les fibres, comme <i>Lachnospiraceae</i>, ont augmenté.'),
        ['rct'], doi='10.1039/d4fo05847j'),
]), t('Son estudios pequeños: el de Lagkouvardos, con 9 hombres y sin grupo control; el de Tian, sin cegar, porque no encontraron un placebo parecido a la linaza. Ver más bifidobacterias o enterolactona no prueba menos enfermedad. Con la chía, casi todo lo que hay sobre microbiota viene de ratas y de modelos de laboratorio. Para el resto de la fibra y la inflamación intestinal, mira la serie intestino.',
      'These are small studies: Lagkouvardos had 9 men and no control group; Tian wasn’t blinded, as no placebo resembling flaxseed was found. More bifidobacteria or enterolactone doesn’t prove less disease. For chia, almost everything on the microbiota comes from rats and lab models. For the rest of fibre and gut inflammation, see the gut series.',
      'Ce sont de petites études : celle de Lagkouvardos, avec 9 hommes et sans groupe témoin ; celle de Tian, sans insu, faute de placebo ressemblant au lin. Plus de bifidobactéries ou d’entérolactone ne prouve pas moins de maladie. Pour le chia, presque tout ce qu’on sait sur le microbiote vient du rat et de modèles de laboratoire. Pour le reste des fibres et l’inflammation intestinale, voir la série intestin.')))

S.append(section(t('¿Moda?', 'A fad?', 'Une mode ?'), '\n'.join([
    ref('TaghipourSheshdeh F, Behzadi M, Bashiri S, Mohammadi-Sartang M · Nutrition Reviews · 2025; 83(3): 448–465',
        'The Effect of Chia Seed on Blood Pressure, Body Composition, and Glycemic Control: A GRADE-Assessed Systematic Review and Dose-Response Meta-Analysis of Randomized Controlled Trials',
        t('8 ensayos. La chía no cambió el peso, el IMC, la grasa corporal, la cintura ni la glucosa. Sí bajó la presión arterial (sistólica −7 mmHg), aunque con pocos datos.',
          '8 trials. Chia didn’t change weight, BMI, body fat, waist or blood glucose. It did lower blood pressure (systolic −7 mmHg), though with little data.',
          '8 essais. Le chia n’a modifié ni le poids, ni l’IMC, ni la masse grasse, ni le tour de taille, ni la glycémie. Il a fait baisser la pression artérielle (systolique −7 mmHg), mais avec peu de données.'),
        ['meta'], doi='10.1093/nutrit/nuae113'),
    ref('Fateh HL, Ahmed DH, Najafabadi MS, Moludi J · Prostaglandins &amp; Other Lipid Mediators · 2024; 175: 106907',
        'The impact of chia seeds on diabetes, blood pressure, lipid profile, and obesity indicators: Systematic review and meta-regression analysis of 14 randomized controlled trials',
        t('14 ensayos con 835 personas. La chía bajó los triglicéridos, y el LDL y la presión sistólica solo con las dosis más altas.',
          '14 trials with 835 people. Chia lowered triglycerides, and LDL and systolic pressure only at the higher doses.',
          '14 essais avec 835 personnes. Le chia a fait baisser les triglycérides, et le LDL et la pression systolique seulement aux doses les plus élevées.'),
        ['meta'], doi='10.1016/j.prostaglandins.2024.106907'),
    ref('Strate LL, Liu YL, Syngal S, Aldoori WH, Giovannucci EL · JAMA · 2008; 300(8): 907–914',
        'Nut, Corn, and Popcorn Consumption and the Incidence of Diverticular Disease',
        t('47 228 hombres de 40 a 75 años seguidos 18 años. Comer nueces, maíz o palomitas no aumentó la diverticulitis ni el sangrado; con nueces y palomitas, incluso hubo menos diverticulitis. Es el estudio que desmontó el consejo de evitar «semillas» si hay divertículos.',
          '47,228 men aged 40 to 75 followed for 18 years. Eating nuts, corn or popcorn didn’t increase diverticulitis or bleeding; with nuts and popcorn there was even less diverticulitis. It’s the study that undid the advice to avoid “seeds” if you have diverticula.',
          '47 228 hommes de 40 à 75 ans suivis 18 ans. Manger des noix, du maïs ou du pop-corn n’a pas augmenté la diverticulite ni les saignements ; avec les noix et le pop-corn, il y a même eu moins de diverticulites. C’est l’étude qui a fait tomber le conseil d’éviter les « graines » en cas de diverticules.'),
        ['obs'], doi='10.1001/jama.300.8.907', old=True),
]), t('Que la chía no adelgace no la hace inútil: aporta fibra y omega-3 vegetal, y puede dar saciedad. Pero los ensayos son pocos y pequeños. Strate 2008 es una asociación en hombres y no midió semillas como la linaza o la chía directamente.',
      'Chia not slimming you down doesn’t make it useless: it provides fibre and plant omega-3 and may be filling. But the trials are few and small. Strate 2008 is an association in men and didn’t directly measure seeds such as flax or chia.',
      'Que le chia ne fasse pas maigrir ne le rend pas inutile : il apporte des fibres et des oméga-3 végétaux et peut rassasier. Mais les essais sont peu nombreux et petits. Strate 2008 est une association chez des hommes et n’a pas mesuré directement des graines comme le lin ou le chia.')))

# Tabla de semillas
def srow(name, origin, what, ev):
    return f'        <tr><td>{name}</td><td>{origin}. {what}</td><td><span class="st {ev[0]}">{ev[1]}</span></td></tr>'

MUCHOS = ('ok', t('Muchos ensayos', 'Many trials', 'Nombreux essais'))
POCOS = ('part', t('Pocos ensayos', 'Few trials', 'Peu d’essais'))
NOREV = ('part', t('No revisada aquí', 'Not reviewed here', 'Non revue ici'))
seed_rows = [
    srow(t('Linaza', 'Flax', 'Lin'), t('Creciente Fértil', 'Fertile Crescent', 'Croissant fertile'),
         t('Omega-3 vegetal (ALA), lignanos y fibra soluble.', 'Plant omega-3 (ALA), lignans and soluble fibre.', 'Oméga-3 végétal (ALA), lignanes et fibres solubles.'), MUCHOS),
    srow(t('Chía', 'Chia', 'Chia'), t('Mesoamérica', 'Mesoamerica', 'Mésoamérique'),
         t('Omega-3 vegetal y una fibra que forma gel con el agua (mucílago).', 'Plant omega-3 and a fibre that forms a gel with water (mucilage).', 'Oméga-3 végétal et une fibre qui forme un gel avec l’eau (mucilage).'), POCOS),
    srow(t('Calabaza', 'Pumpkin', 'Courge'), t('Mesoamérica (Oaxaca)', 'Mesoamerica (Oaxaca)', 'Mésoamérique (Oaxaca)'),
         t('Grasas insaturadas, proteína y minerales.', 'Unsaturated fats, protein and minerals.', 'Graisses insaturées, protéines et minéraux.'), NOREV),
    srow(t('Girasol', 'Sunflower', 'Tournesol'), t('Norteamérica', 'North America', 'Amérique du Nord'),
         t('Omega-6 (ácido linoleico) y vitamina E.', 'Omega-6 (linoleic acid) and vitamin E.', 'Oméga-6 (acide linoléique) et vitamine E.'), NOREV),
    srow(t('Sésamo', 'Sesame', 'Sésame'), t('Sur de Asia o África (se discute)', 'South Asia or Africa (debated)', 'Asie du Sud ou Afrique (débattu)'),
         t('Lignanos propios, como la sesamina.', 'Its own lignans, such as sesamin.', 'Ses propres lignanes, comme la sésamine.'), NOREV),
    srow(t('Cáñamo', 'Hemp', 'Chanvre'), t('Asia', 'Asia', 'Asie'),
         t('Proteína, omega-3 y omega-6. Próxima entrega.', 'Protein, omega-3 and omega-6. Coming in a future topic.', 'Protéines, oméga-3 et oméga-6. Prochain sujet.'), NOREV),
    srow(t('Amaranto', 'Amaranth', 'Amarante'), t('Mesoamérica y Andes', 'Mesoamerica and the Andes', 'Mésoamérique et Andes'),
         t('Proteína; se come como cereal (alegrías).', 'Protein; eaten like a cereal (as in Mexican <i>alegrías</i>).', 'Protéines ; se mange comme une céréale (les <i>alegrías</i> mexicaines).'), NOREV),
]
S.append(f'''  <section>
    <div class="frame"><h2>{t('Las semillas, una por una', 'The seeds, one by one', 'Les graines, une par une')}</h2></div>
    <p class="note">{t('Todas llevan miles de años en la mesa, pero casi todos los ensayos en personas son de linaza y chía. Solo la calabaza y la linaza llevan fuente de origen en esta página; los demás orígenes son generales y los documentaremos cuando ampliemos el tema.',
                       'All have been on the table for thousands of years, but almost all trials in people are on flax and chia. Only pumpkin and flax have a source for their origin on this page; the other origins are general and will be documented when we expand the topic.',
                       'Toutes sont sur la table depuis des milliers d’années, mais presque tous les essais chez l’humain portent sur le lin et le chia. Seuls la courge et le lin ont une source pour leur origine sur cette page ; les autres origines sont générales et seront documentées quand nous élargirons le sujet.')}</p>
    <div class="reg-wrap">
    <table class="reg">
      <thead><tr><th>{t('Semilla', 'Seed', 'Graine')}</th><th>{t('Origen y qué aporta', 'Origin and what it provides', 'Origine et apports')}</th><th>{t('Evidencia', 'Evidence', 'Preuves')}</th></tr></thead>
      <tbody>
{chr(10).join(seed_rows)}
      </tbody>
    </table>
    </div>
  </section>
''')


def row(where, what, status, links):
    a = ' · '.join(f'<a href="{u}">{n}</a>' for n, u in links)
    cls, label = status
    return f'        <tr><td>{where}</td><td>{what} {a}</td><td><span class="st {cls}">{label}</span></td></tr>'


EU = t('Unión Europea', 'European Union', 'Union européenne')
OK = ('ok', t('Vigente', 'In force', 'En vigueur'))
reg_rows = [
    row(EU, t('Reglamento (UE) 432/2012: un alimento que sea al menos «fuente de omega-3» puede decir que el ALA contribuye a mantener niveles normales de colesterol, siempre que indique que el efecto se obtiene con 2 g de ALA al día.',
              'Regulation (EU) 432/2012: a food that is at least a “source of omega-3” may claim that ALA contributes to maintaining normal blood cholesterol, provided it states the effect is obtained with 2 g of ALA a day.',
              'Règlement (UE) 432/2012 : un aliment au moins « source d’oméga-3 » peut indiquer que l’ALA contribue au maintien d’une cholestérolémie normale, à condition de préciser que l’effet est obtenu avec 2 g d’ALA par jour.'),
        OK, [('EUR-Lex', 'https://eur-lex.europa.eu/eli/reg/2012/432')]),
    row(EU, t('Chía como «nuevo alimento». El Reglamento de Ejecución (UE) 2020/24 amplió sus usos (chocolate, lácteos, bebidas, postres…) en alimentos que no se calienten a 120 °C o más; los productos horneados quedaron pendientes por la posible formación de acrilamida.',
              'Chia as a “novel food”. Implementing Regulation (EU) 2020/24 extended its uses (chocolate, dairy, drinks, desserts…) to foods not heated to 120 °C or more; baked goods were left pending over possible acrylamide formation.',
              'Le chia comme « nouvel aliment ». Le règlement d’exécution (UE) 2020/24 a étendu ses usages (chocolat, produits laitiers, boissons, desserts…) aux aliments non chauffés à 120 °C ou plus ; les produits cuits au four sont restés en attente à cause d’une possible formation d’acrylamide.'),
        OK, [('legislation.gov.uk', 'https://www.legislation.gov.uk/eur/2020/24/introduction/adopted')]),
    row(EU, t('Cáñamo: límites máximos de THC (Reglamento (UE) 2022/1393, desde el 1 de enero de 2023): 3,0 mg/kg en semillas y productos secos, 7,5 mg/kg en aceite. Hoy están recogidos en el Reglamento (UE) 2023/915 de contaminantes.',
              'Hemp: maximum THC levels (Regulation (EU) 2022/1393, since 1 January 2023): 3.0 mg/kg in seeds and dry products, 7.5 mg/kg in oil. They are now in the contaminants Regulation (EU) 2023/915.',
              'Chanvre : teneurs maximales en THC (règlement (UE) 2022/1393, depuis le 1er janvier 2023) : 3,0 mg/kg dans les graines et produits secs, 7,5 mg/kg dans l’huile. Elles figurent aujourd’hui dans le règlement (UE) 2023/915 sur les contaminants.'),
        OK, [('EUR-Lex', 'https://eur-lex.europa.eu/eli/reg/2022/1393/oj/eng'), ('FoodNavigator', 'https://www.foodnavigator.com/ARTICLE/2022/03/16/EU-WIDE-ADOPTION-OF-MAX-THC-LIMITS-IN-HEMP-SEED-FOODS-A-SIGNIFICANT-WIN-FOR-SECTOR')]),
    row(t('EE. UU.', 'USA', 'États-Unis'), t('La FDA no puso objeciones (20 de diciembre de 2018) a que tres ingredientes de semilla de cáñamo se consideren seguros (GRAS): semilla descascarillada, proteína en polvo y aceite.',
              'The FDA raised no questions (20 December 2018) about three hemp seed ingredients being generally recognized as safe (GRAS): hulled seed, protein powder and oil.',
              'La FDA n’a soulevé aucune objection (20 décembre 2018) à ce que trois ingrédients de graine de chanvre soient reconnus sûrs (GRAS) : graine décortiquée, protéine en poudre et huile.'),
        OK, [('FDA', 'https://www.fda.gov/Food/NewsEvents/ConstituentUpdates/ucm628910.htm')]),
    row(t('México', 'Mexico', 'Mexique'), t('Cáñamo: COFEPRIS publicó en octubre de 2018 lineamientos que permitían alimentos y bebidas con derivados de cannabis, y los revocó en marzo de 2019 por contradecir la Ley General de Salud. No encontramos una norma específica para semillas de cáñamo en alimentos.',
              'Hemp: COFEPRIS issued guidelines in October 2018 allowing foods and drinks with cannabis derivatives, and revoked them in March 2019 for contradicting the General Health Law. We found no specific rule for hemp seeds in food.',
              'Chanvre : la COFEPRIS a publié en octobre 2018 des lignes directrices autorisant aliments et boissons à base de dérivés du cannabis, puis les a révoquées en mars 2019 car contraires à la Loi générale de santé. Nous n’avons pas trouvé de règle spécifique pour les graines de chanvre dans l’alimentation.'),
        ('rev', t('Revocado', 'Revoked', 'Révoqué')),
        [('Expansión', 'https://expansion.mx/empresas/2019/03/27/cofepris-revoca-los-lineamientos-para-productos-de-mariguana-con-thc')]),
]

S.append(f'''  <section>
    <div class="frame"><h2>{t('Regulación en Europa y América', 'Regulation in Europe and the Americas', 'Réglementation en Europe et en Amérique')}</h2></div>
    <p class="note">{t('Las semillas comunes se venden como cualquier alimento. Las normas tocan tres cosas: qué se puede prometer en la etiqueta, la chía como alimento nuevo en Europa y el THC del cáñamo. No encontramos normas específicas en otros países de Latinoamérica.',
                       'Common seeds are sold like any other food. Rules touch three things: what a label may promise, chia as a novel food in Europe, and THC in hemp. We found no specific rules in other Latin American countries.',
                       'Les graines courantes se vendent comme n’importe quel aliment. Les règles portent sur trois points : ce que l’étiquette peut promettre, le chia comme nouvel aliment en Europe et le THC du chanvre. Nous n’avons pas trouvé de règles spécifiques dans d’autres pays d’Amérique latine.')}</p>
    <div class="reg-wrap">
    <table class="reg">
      <thead><tr><th>{t('Dónde', 'Where', 'Où')}</th><th>{t('Qué', 'What', 'Quoi')}</th><th>{t('Estado', 'Status', 'Statut')}</th></tr></thead>
      <tbody>
{chr(10).join(reg_rows)}
      </tbody>
    </table>
    </div>
  </section>
''')


def rel(href, cat, title):
    return f'''      <li><a href="{href}"><img src="{href}story-es.png" alt="" width="40" height="71" loading="lazy"><span><span class="cat-name">{cat}</span><span class="t">{title}</span></span></a></li>'''


RELACIONADOS = f'''  <!-- relacionados:semillas -->
  <nav class="serie" aria-label="Temas relacionados / Related topics / Sujets liés">
    <p class="serie-label">{t('Temas relacionados', 'Related topics', 'Sujets liés')}</p>
    <ol>
{rel('../dieta-ancestral/', t('Ancestral', 'Ancestral', 'Ancestral'), t('Dieta ancestral: ¿la clave está en comer como antes?', 'Ancestral diet: is the key eating like we used to?', f'Manger comme nos ancêtres, est-ce la clé{NB}?'))}
{rel('../dieta-inflamacion/', t('Inflamación', 'Inflammation', 'Inflammation'), t('¿Qué comida inflama tu colon y cuál lo calma?', 'Which foods inflame your colon and which calm it?', f'Quels aliments enflamment ton côlon et lesquels l’apaisent{NB}?'))}
{rel('../inflamacion-intestinal/', t('Serie intestino', 'Gut series', 'Série intestin'), t('Intestino inflamado, microbiota empobrecida: ¿quién empieza?', 'Inflamed gut, depleted microbiota: which comes first?', f'Intestin enflammé, microbiote appauvri{NB}: qui commence{NB}?'))}
    </ol>
  </nav>
  <!-- /relacionados:semillas -->
'''

html = page(
    title_tag='Semillas',
    description='Las fuentes detrás de la story sobre semillas: su historia milenaria, qué se sabe de la inflamación, qué hacen en el intestino, qué es moda y la regulación en Europa y América. / The sources behind the story on seeds.',
    h1=t('Semillas: <em>las fuentes</em>', 'Seeds: <em>the sources</em>', 'Graines&nbsp;: <em>les sources</em>'),
    lede=t('Linaza, chía, calabaza, girasol, sésamo… ¿son alimento ancestral, antiinflamatorio o moda? Un poco de todo. Aquí están los estudios detrás de cada cifra de la story, una tabla con las semillas más comunes y lo que los estudios no demuestran. Con el tipo de evidencia de cada uno.',
           'Flax, chia, pumpkin, sunflower, sesame… ancestral food, anti-inflammatory or fad? A bit of each. Here are the studies behind each number in the story, a table of the most common seeds and what the studies don’t show. With the type of evidence for each.',
           'Lin, chia, courge, tournesol, sésame… aliment ancestral, anti-inflammatoire ou mode ? Un peu de tout. Voici les études derrière chaque chiffre de la story, un tableau des graines les plus courantes et ce que les études ne démontrent pas. Avec le type de preuve de chacune.'),
    legend_html=legend(['meta', 'rct', 'obs', 'rev', 'arq']),
    sections=S,
    alt='Las stories en español, inglés y francés: Semillas: ¿alimento ancestral, antiinflamatorio o moda? / Seeds: ancestral food, anti-inflammatory or fad? / Graines : aliment ancestral, anti-inflammatoire ou mode ?',
    footer=t('Contenido divulgativo; no sustituye el consejo médico. Si tienes alguna enfermedad o tomas medicación, consulta a tu médico antes de añadir grandes cantidades de semillas a tu dieta.',
             'For general information only, not medical advice. If you have a medical condition or take medication, check with your doctor before adding large amounts of seeds to your diet.',
             'Contenu de vulgarisation, pas un avis médical. Si vous avez une maladie ou prenez un traitement, consultez votre médecin avant d’ajouter de grandes quantités de graines à votre alimentation.'),
)
html = html.replace('Evidencia revisada: oct 2026', 'Evidencia revisada: nov 2026').replace('Evidence reviewed: Oct 2026', 'Evidence reviewed: Nov 2026').replace('Preuves revues : oct. 2026', 'Preuves revues : nov. 2026')
assert html.count('  </header>\n') == 1
html = html.replace('  </header>\n', '  </header>\n\n' + RELACIONADOS, 1)
(OUT / 'index.html').write_text(html)
print('ok', len(html))
