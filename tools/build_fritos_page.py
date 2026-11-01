"""Genera ciencia-salud/fritos-inflamacion/index.html (ES/EN/FR), con tabla de regulación y bloque «Serie: colon»."""
import sys, pathlib
from healthkit import t, section, ref, legend, page

OUT = pathlib.Path(sys.argv[1])
NB = '&nbsp;'
S = []

S.append(section(t('Lo que sientes tras un frito', 'What you feel after fried food', 'Ce que l’on ressent après une friture'), '\n'.join([
    ref('Feinle-Bisset C, Azpiroz F · American Journal of Gastroenterology · 2013; 108(5): 737–747',
        'Dietary Lipids and Functional Gastrointestinal Disorders',
        t('La grasa frena el vaciado del estómago, en parte por la colecistoquinina (CCK), una hormona que se libera al digerirla, y retrasa el paso de los gases por el intestino. En personas sanas, una comida muy grasa puede dar síntomas frente a una baja en grasa; quienes tienen dispepsia funcional o colon irritable son mucho más sensibles. Los fritos están entre los alimentos que más se señalan como desencadenantes: en un grupo con colon irritable con diarrea, fueron el primero (59 %).',
          'Fat slows stomach emptying, partly through cholecystokinin (CCK), a hormone released as it’s digested, and it slows the passage of gas through the gut. In healthy people, a very fatty meal can cause symptoms compared with a low-fat one; people with functional dyspepsia or irritable bowel are far more sensitive. Fried foods are among the most commonly reported triggers: in one group with diarrhoea-predominant IBS they came first (59%).',
          'Les graisses ralentissent la vidange de l’estomac, en partie via la cholécystokinine (CCK), une hormone libérée pendant leur digestion, et ralentissent le passage des gaz dans l’intestin. Chez les personnes en bonne santé, un repas très gras peut provoquer des symptômes par rapport à un repas pauvre en graisses ; les personnes atteintes de dyspepsie fonctionnelle ou de côlon irritable y sont bien plus sensibles. Les fritures figurent parmi les déclencheurs les plus cités : dans un groupe atteint de côlon irritable à diarrhée, elles arrivaient en tête (59 %).'),
        ['rev'], doi='10.1038/ajg.2013.76', old=True),
    ref('British Journal of Nutrition · 2020; 124(7): 654–667',
        'Effects of dietary fat quality on metabolic endotoxaemia: a systematic review',
        t('Revisa ensayos en personas. Tras una comida rica en grasa saturada sube en sangre el LPS, un fragmento de la pared de algunas bacterias intestinales que activa la inflamación. Las grasas poliinsaturadas se asociaron con menos LPS. En los estudios a largo plazo, el tipo de grasa no cambió el LPS de forma clara.',
          'Reviews trials in people. After a meal rich in saturated fat, blood LPS rises; LPS is a fragment of the wall of some gut bacteria that triggers inflammation. Polyunsaturated fats were associated with less LPS. In long-term studies, fat type didn’t clearly change LPS.',
          'Passe en revue des essais chez l’humain. Après un repas riche en graisses saturées, le LPS augmente dans le sang ; c’est un fragment de la paroi de certaines bactéries intestinales qui déclenche l’inflammation. Les graisses polyinsaturées étaient associées à moins de LPS. Dans les études à long terme, le type de graisse n’a pas clairement modifié le LPS.'),
        ['meta'], doi='10.1017/S0007114520001658'),
]), t('Lo que notaste tras dos fritos es sobre todo digestivo y pasajero: no demuestra inflamación crónica. El pico de LPS tras una comida grasa dura horas. Lo que importa es la costumbre.',
      'What you notice after two fried meals is mostly digestive and short-lived: it doesn’t show chronic inflammation. The LPS spike after a fatty meal lasts hours. What matters is the habit.',
      'Ce qu’on ressent après deux fritures est surtout digestif et passager : cela ne montre pas une inflammation chronique. Le pic de LPS après un repas gras dure quelques heures. Ce qui compte, c’est l’habitude.')))

S.append(section(t('Cuando es costumbre: el intestino', 'When it’s a habit: the gut', 'Quand ça devient une habitude : l’intestin'), '\n'.join([
    ref('Detopoulou P, Voulgaridou G, Seva V, et al. · International Journal of Molecular Sciences · 2024; 25(21): 11407',
        'Dietary Restriction of Advanced Glycation End-Products (AGEs) in Patients with Diabetes: A Systematic Review of Randomized Controlled Trials',
        t('Los productos de glicación avanzada (AGEs) se forman cuando azúcares y proteínas o grasas se combinan con calor seco e intenso, como al freír o asar. En 7 ensayos con personas con diabetes, una dieta baja en AGEs bajó los marcadores inflamatorios en los 4 que los midieron, y también el estrés oxidativo y los AGEs en sangre.',
          'Advanced glycation end-products (AGEs) form when sugars combine with proteins or fats under intense dry heat, as in frying or grilling. In 7 trials in people with diabetes, a low-AGE diet lowered inflammatory markers in all 4 that measured them, as well as oxidative stress and blood AGEs.',
          'Les produits de glycation avancée (AGE) se forment quand des sucres se combinent à des protéines ou des graisses sous une chaleur sèche et intense, comme en friture ou au gril. Dans 7 essais chez des personnes diabétiques, un régime pauvre en AGE a fait baisser les marqueurs inflammatoires dans les 4 qui les ont mesurés, ainsi que le stress oxydatif et les AGE sanguins.'),
        ['meta'], doi='10.3390/ijms252111407'),
    ref('Hu L, Huang L, Fang Z, et al. · Microorganisms · 2024; 12(6): 1210',
        'Fried Soybean Oil Causes Systemic Low-Grade Inflammation by Disrupting the Balance of Gut Microbiota in Mice',
        t('Aceite de soja usado 32 veces para freír pollo, papas y masa, dado a ratones durante 6 días. Con las dosis media y alta bajó la diversidad intestinal, subieron las Proteobacteria y <i>Escherichia–Shigella</i> se multiplicó hasta 39 veces. El TNF-α en sangre, una señal de inflamación, subió con todas las dosis.',
          'Soybean oil used 32 times to fry chicken, fries and dough, given to mice for 6 days. At medium and high doses gut diversity fell, Proteobacteria rose and <i>Escherichia–Shigella</i> multiplied up to 39-fold. Blood TNF-α, an inflammation signal, rose at every dose.',
          'Huile de soja utilisée 32 fois pour frire poulet, frites et pâte, donnée à des souris pendant 6 jours. Aux doses moyenne et forte, la diversité intestinale a baissé, les Proteobacteria ont augmenté et <i>Escherichia–Shigella</i> s’est multipliée jusqu’à 39 fois. Le TNF-α sanguin, un signal d’inflammation, a augmenté à toutes les doses.'),
        ['lab'], doi='10.3390/microorganisms12061210'),
    ref('Zhang J, Chen X, Yang R, et al. · Cancer Prevention Research · 2019; 12(11): 741–750',
        'Thermally Processed Oil Exaggerates Colonic Inflammation and Colitis-Associated Colon Tumorigenesis in Mice',
        t('Aceite de freír, preparado como en la restauración, añadido a la dieta de ratones. Empeoró la colitis y los tumores de colon asociados a la colitis, dañó la barrera intestinal y dejó pasar LPS y bacterias a la sangre. Los compuestos polares que se acumulan en el aceite al reutilizarlo reprodujeron el efecto por sí solos.',
          'Frying oil, prepared as in restaurants, added to mice’s diet. It worsened colitis and colitis-associated colon tumours, damaged the gut barrier and let LPS and bacteria into the blood. The polar compounds that build up in oil as it’s reused reproduced the effect on their own.',
          'Huile de friture, préparée comme en restauration, ajoutée à l’alimentation de souris. Elle a aggravé la colite et les tumeurs du côlon associées à la colite, abîmé la barrière intestinale et laissé passer LPS et bactéries dans le sang. Les composés polaires qui s’accumulent dans l’huile réutilisée ont reproduit l’effet à eux seuls.'),
        ['lab'], doi='10.1158/1940-6207.CAPR-19-0226', old=True),
]), t('Los ensayos de AGEs se hicieron en personas con diabetes, y ninguno mejoró la glucosa ni la HbA1c. Los dos estudios de aceite son en ratones: el de Hu duró 6 días, con 5 ratones por grupo, y solo midió inflamación en sangre; el de Zhang usó modelos de colitis inducida químicamente.',
      'The AGE trials were in people with diabetes, and none improved glucose or HbA1c. Both oil studies are in mice: Hu’s lasted 6 days with 5 mice per group and only measured blood inflammation; Zhang’s used chemically induced colitis models.',
      'Les essais sur les AGE portaient sur des personnes diabétiques, et aucun n’a amélioré la glycémie ni l’HbA1c. Les deux études sur l’huile sont chez la souris : celle de Hu a duré 6 jours avec 5 souris par groupe et n’a mesuré que l’inflammation sanguine ; celle de Zhang a utilisé des modèles de colite induite chimiquement.')))

S.append(section(t('¿Y el cáncer de colon?', 'What about colon cancer?', 'Et le cancer du côlon ?'), '\n'.join([
    ref('Chiavarini M, Bertarelli G, Minelli L, Fabiani R · Nutrients · 2017; 9(5): 514',
        'Dietary Intake of Meat Cooking-Related Mutagens (HCAs) and Risk of Colorectal Adenoma and Cancer: A Systematic Review and Meta-Analysis',
        t('Al freír o asar carne a alta temperatura se forman aminas heterocíclicas. Varias se asociaron con más adenomas colorrectales, los pólipos que pueden convertirse en cáncer (RR de 1,10 a 1,22). Con el cáncer colorrectal, en cambio, casi ninguna mostró asociación (aminas totales: RR 0,93).',
          'Frying or grilling meat at high heat forms heterocyclic amines. Several were associated with more colorectal adenomas, the polyps that can turn into cancer (RR 1.10 to 1.22). With colorectal cancer itself, almost none showed an association (total amines: RR 0.93).',
          'Frire ou griller de la viande à haute température forme des amines hétérocycliques. Plusieurs étaient associées à plus d’adénomes colorectaux, les polypes qui peuvent devenir cancéreux (RR de 1,10 à 1,22). Avec le cancer colorectal lui-même, presque aucune ne montrait d’association (amines totales : RR 0,93).'),
        ['meta'], doi='10.3390/nu9050514', old=True),
    ref('Galeone C, La Vecchia C, Bosetti C, Pelucchi C · International Journal of Cancer · 2015; 136(12): 2912–2922',
        'Dietary acrylamide and cancer risk: an updated meta-analysis',
        t('32 publicaciones. La acrilamida, que se forma al freír o tostar alimentos ricos en almidón como las papas, no se asoció con el cáncer colorrectal (RR 0,94 entre la ingesta más alta y la más baja).',
          '32 publications. Acrylamide, which forms when frying or toasting starchy foods such as potatoes, wasn’t associated with colorectal cancer (RR 0.94 for highest vs lowest intake).',
          '32 publications. L’acrylamide, qui se forme quand on fait frire ou griller des aliments riches en amidon comme les pommes de terre, n’était pas associée au cancer colorectal (RR 0,94 entre l’apport le plus élevé et le plus faible).'),
        ['meta'], doi='10.1002/ijc.29339', old=True),
]), t('En personas no se ha demostrado que los fritos aumenten el cáncer de colon. Lo que sí está establecido es el papel de la carne procesada (riesgo convincente) y la carne roja (probable), según el Fondo Mundial de Investigación del Cáncer; freír no figura como factor propio. Las pistas del mecanismo vienen de ratones (Zhang 2019) y de la asociación con pólipos, no con cáncer. Ambos metaanálisis son anteriores a 2020: no encontramos uno más reciente sobre fritos y cáncer colorrectal.',
      'In people, fried food has not been shown to increase colon cancer. What is established is the role of processed meat (convincing risk) and red meat (probable), according to the World Cancer Research Fund; frying isn’t listed as a factor of its own. The mechanistic clues come from mice (Zhang 2019) and from the link with polyps, not cancer. Both meta-analyses predate 2020: we found no more recent one on fried food and colorectal cancer.',
      'Chez l’humain, il n’est pas démontré que les fritures augmentent le cancer du côlon. Ce qui est établi, c’est le rôle de la viande transformée (risque convaincant) et de la viande rouge (probable), selon le Fonds mondial de recherche contre le cancer ; la friture n’y figure pas comme facteur à part. Les pistes de mécanisme viennent de la souris (Zhang 2019) et du lien avec les polypes, pas avec le cancer. Les deux méta-analyses sont antérieures à 2020 : nous n’en avons pas trouvé de plus récente sur fritures et cancer colorectal.')))

S.append(section(t('Más allá del intestino', 'Beyond the gut', 'Au-delà de l’intestin'), '\n'.join([
    ref('Qin P, Zhang M, Han M, et al. · Heart · 2021; 107(19): 1567',
        'Fried-food consumption and risk of cardiovascular disease and all-cause mortality: a meta-analysis of observational studies',
        t('Metaanálisis de estudios observacionales. Comparando a quienes más fritos comen con quienes menos, el riesgo de eventos cardiovasculares mayores fue un 28 % más alto (RR 1,28), el de enfermedad coronaria un 22 % y el de insuficiencia cardíaca un 37 %, con una relación lineal: a más fritos, más riesgo.',
          'Meta-analysis of observational studies. Comparing those who eat the most fried food with those who eat the least, the risk of major cardiovascular events was 28% higher (RR 1.28), coronary heart disease 22% and heart failure 37%, with a linear relationship: more fried food, more risk.',
          'Méta-analyse d’études observationnelles. En comparant les plus gros consommateurs de fritures aux plus petits, le risque d’événements cardiovasculaires majeurs était 28 % plus élevé (RR 1,28), celui de maladie coronarienne 22 % et celui d’insuffisance cardiaque 37 %, avec une relation linéaire : plus de fritures, plus de risque.'),
        ['meta'], doi='10.1136/heartjnl-2020-317883'),
    ref('Wang A, Wan X, Zhuang P, et al. · PNAS · 2023',
        'High fried food consumption impacts anxiety and depression due to lipid metabolism disturbance and neuroinflammation',
        t('140 728 personas del UK Biobank seguidas 11 años. Comer fritos con frecuencia se asoció con un 12 % más de riesgo de ansiedad y un 7 % más de depresión. En el mismo trabajo, peces cebra expuestos a acrilamida durante 180 días mostraron conductas parecidas a la ansiedad e inflamación en el cerebro.',
          '140,728 UK Biobank participants followed for 11 years. Eating fried food often was associated with 12% higher risk of anxiety and 7% higher risk of depression. In the same work, zebrafish exposed to acrylamide for 180 days showed anxiety-like behaviour and brain inflammation.',
          '140 728 participants de l’UK Biobank suivis 11 ans. Manger souvent des fritures était associé à un risque d’anxiété 12 % plus élevé et de dépression 7 % plus élevé. Dans le même travail, des poissons-zèbres exposés à l’acrylamide pendant 180 jours ont montré des comportements de type anxieux et une inflammation cérébrale.'),
        ['obs'], doi='10.1073/pnas.2221097120'),
]), t('Ambos son asociaciones, no causas, y los efectos son pequeños. En el metaanálisis cardiovascular hubo mucha diferencia entre estudios, y los fritos no se asociaron con más mortalidad cardiovascular ni total.',
      'Both are associations, not causes, and the effects are small. The cardiovascular meta-analysis had large differences between studies, and fried food wasn’t associated with higher cardiovascular or total mortality.',
      'Ce sont des associations, pas des causes, et les effets sont faibles. La méta-analyse cardiovasculaire montrait de grandes différences entre études, et les fritures n’étaient pas associées à une mortalité cardiovasculaire ou totale plus élevée.')))

S.append(section(t('¿Y la freidora de aire?', 'What about the air fryer?', 'Et la friteuse à air ?'), '\n'.join([
    ref('Navruz-Varlı S, Mortaş H · Frontiers in Nutrition · 2024; 10: 1297069',
        'Acrylamide formation in air-fried versus deep and oven-fried potatoes',
        t('Compararon papas hechas en freidora de aire, en aceite y al horno. La acrilamida no fue menor en la freidora de aire (12,2 µg/kg, frente a 8,9 en aceite y 7,4 al horno), aunque las diferencias no fueron significativas. Remojar las papas 10 minutos en agua antes de cocinarlas la redujo en los tres métodos.',
          'They compared potatoes cooked in an air fryer, in oil and in the oven. Acrylamide wasn’t lower in the air fryer (12.2 µg/kg, versus 8.9 deep-fried and 7.4 oven-baked), though the differences weren’t significant. Soaking the potatoes in water for 10 minutes before cooking reduced it in all three methods.',
          'Ils ont comparé des pommes de terre cuites en friteuse à air, dans l’huile et au four. L’acrylamide n’était pas plus faible en friteuse à air (12,2 µg/kg, contre 8,9 en friture et 7,4 au four), mais les différences n’étaient pas significatives. Faire tremper les pommes de terre 10 minutes dans l’eau avant cuisson l’a réduite dans les trois méthodes.'),
        ['food'], doi='10.3389/fnut.2023.1297069'),
]), t('La freidora de aire usa mucho menos aceite, y eso sí cuenta. Pero este estudio fue pequeño (24 muestras), y no midió los productos de oxidación del aceite. La regla práctica: no requemar el aceite, no pasarse de dorado y remojar las papas.',
      'The air fryer uses far less oil, and that does count. But this study was small (24 samples) and didn’t measure oil oxidation products. The practical rule: don’t overheat the oil, don’t go past golden, and soak the potatoes.',
      'La friteuse à air utilise beaucoup moins d’huile, et cela compte. Mais cette étude était petite (24 échantillons) et n’a pas mesuré les produits d’oxydation de l’huile. La règle pratique : ne pas surchauffer l’huile, ne pas dépasser le doré et faire tremper les pommes de terre.')))


def row(where, what, status, links):
    a = ' · '.join(f'<a href="{u}">{n}</a>' for n, u in links)
    cls, label = status
    return f'        <tr><td>{where}</td><td>{what} {a}</td><td><span class="st {cls}">{label}</span></td></tr>'


EU = t('Unión Europea', 'European Union', 'Union européenne')
OK = ('ok', t('Vigente', 'In force', 'En vigueur'))
reg_rows = [
    row(EU, t('Reglamento (UE) 2017/2158 sobre acrilamida, en vigor desde abril de 2018: fabricantes y restaurantes deben aplicar medidas para reducirla (remojar o escaldar las papas, freír por debajo de 175 °C, desnatar el aceite). Fija niveles de referencia, no límites máximos: superarlos no impide vender el producto.',
              'Regulation (EU) 2017/2158 on acrylamide, in force since April 2018: manufacturers and restaurants must apply measures to reduce it (soaking or blanching potatoes, frying below 175 °C, skimming the oil). It sets benchmark levels, not maximum limits: exceeding them doesn’t stop a product being sold.',
              'Règlement (UE) 2017/2158 sur l’acrylamide, en vigueur depuis avril 2018 : fabricants et restaurants doivent appliquer des mesures pour la réduire (tremper ou blanchir les pommes de terre, frire sous 175 °C, écumer l’huile). Il fixe des niveaux de référence, pas des limites maximales : les dépasser n’empêche pas la vente.'),
        ('part', t('Vigente, sin límite máximo', 'In force, no maximum', 'En vigueur, sans maximum')),
        [('Food Standards Scotland', 'https://www.foodstandards.gov.scot/sites/default/files/2025-07/Acrylamide_Regulation_Guidance.pdf')]),
    row(EU, t('Reglamento (UE) 2019/649: como máximo 2 g de grasas trans industriales por cada 100 g de grasa, desde abril de 2021. Afecta a los aceites parcialmente hidrogenados que se usaban para freír.',
              'Regulation (EU) 2019/649: at most 2 g of industrial trans fat per 100 g of fat, since April 2021. It affects the partially hydrogenated oils once used for frying.',
              'Règlement (UE) 2019/649 : au maximum 2 g de graisses trans industrielles pour 100 g de graisses, depuis avril 2021. Il vise les huiles partiellement hydrogénées autrefois utilisées pour la friture.'),
        OK, [('EUR-Lex', 'https://eur-lex.europa.eu/eli/reg/2019/649/oj/eng')]),
    row(EU, t('Aceite de freír degradado: no hay límite a nivel europeo. Alemania usa como referencia la recomendación de la Sociedad Alemana de Investigación de Grasas: desechar el aceite cuando los compuestos polares superan el 24 %. Unos pocos países tienen límites nacionales parecidos.',
              'Degraded frying oil: there’s no EU-level limit. Germany uses the German Society for Fat Science recommendation as its reference: discard the oil once polar compounds exceed 24%. A few countries have similar national limits.',
              'Huile de friture dégradée : pas de limite au niveau européen. L’Allemagne se réfère à la recommandation de la Société allemande de recherche sur les graisses : jeter l’huile au-delà de 24 % de composés polaires. Quelques pays ont des limites nationales similaires.'),
        ('part', t('Recomendación', 'Recommendation', 'Recommandation')),
        [('OFI, 2024', 'https://www.ofimagazine.com/content-images/news/Deep-frying-regulatory-update.pdf')]),
    row(t('EE. UU.', 'USA', 'États-Unis'), t('California, Proposición 65: obliga a advertir de la acrilamida como cancerígena. En 2019 la agencia estatal (OEHHA) eximió al café, por considerar la dosis demasiado baja; las papas fritas y otros alimentos siguen sujetos a advertencia. A nivel federal no hay límite para la acrilamida ni para el aceite de freír.',
              'California, Proposition 65: requires warnings about acrylamide as a carcinogen. In 2019 the state agency (OEHHA) exempted coffee, judging the dose too low; fries and other foods remain subject to warnings. At federal level there’s no limit for acrylamide or frying oil.',
              'Californie, Proposition 65 : impose d’avertir que l’acrylamide est cancérogène. En 2019, l’agence de l’État (OEHHA) a exempté le café, jugeant la dose trop faible ; les frites et autres aliments restent soumis à avertissement. Au niveau fédéral, aucune limite pour l’acrylamide ni pour l’huile de friture.'),
        ('rev', t('Revertido para el café', 'Reversed for coffee', 'Annulé pour le café')),
        [('Food Safety News', 'https://www.foodsafetynews.com/2019/06/no-cancer-warnings-required-on-coffee-sold-in-california-after-all')]),
    row(t('México', 'Mexico', 'Mexique'), t('Reforma a la Ley General de Salud (DOF, 24 de marzo de 2023; en vigor el 20 de septiembre de 2023): prohíbe los aceites parcialmente hidrogenados y limita las grasas trans industriales a 2 partes por cada 100 de grasa total.',
              'Reform of the General Health Law (DOF, 24 March 2023; in force 20 September 2023): bans partially hydrogenated oils and limits industrial trans fat to 2 parts per 100 of total fat.',
              'Réforme de la Loi générale de santé (DOF, 24 mars 2023 ; en vigueur le 20 septembre 2023) : interdit les huiles partiellement hydrogénées et limite les graisses trans industrielles à 2 parts pour 100 de graisses totales.'),
        OK, [('NCD Alliance', 'https://ncdalliance.org/stories/news-blogs/2023/a-celebratory-occasion-mexicos-law-for-the-elimination-of-industrially')]),
    row(t('Brasil', 'Brazil', 'Brésil'), t('ANVISA: límite del 2 % de grasas trans en aceites refinados desde julio de 2021 y prohibición de los aceites parcialmente hidrogenados desde enero de 2023.',
              'ANVISA: 2% trans fat limit in refined oils since July 2021 and a ban on partially hydrogenated oils since January 2023.',
              'ANVISA : limite de 2 % de graisses trans dans les huiles raffinées depuis juillet 2021 et interdiction des huiles partiellement hydrogénées depuis janvier 2023.'),
        OK, [('FoodNavigator', 'https://www.foodnavigator.com/Article/2019/12/19/Brazil-s-ANVISA-announces-2023-trans-fat-ban/')]),
]

S.append(f'''  <section>
    <div class="frame"><h2>{t('Regulación en Europa y América', 'Regulation in Europe and the Americas', 'Réglementation en Europe et en Amérique')}</h2></div>
    <p class="note">{t('Nadie regula cuántos fritos comer: las normas actúan sobre lo que se forma al freír (acrilamida), sobre las grasas trans y, en pocos países, sobre cuándo desechar el aceite usado.',
                       'No one regulates how much fried food to eat: rules act on what forms during frying (acrylamide), on trans fats and, in a few countries, on when to discard used oil.',
                       'Personne ne réglemente la quantité de fritures à manger : les règles portent sur ce qui se forme à la cuisson (acrylamide), sur les graisses trans et, dans quelques pays, sur le moment de jeter l’huile usagée.')}</p>
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

SERIE = f'''  <!-- serie:colon -->
  <nav class="serie" aria-label="Serie">
    <p class="serie-label">{t('Serie: colon', 'Series: the colon', 'Série : le côlon')}</p>
    <ol>
      <li class="here"><div aria-current="page"><img src="story-es.png" alt="" width="40" height="71" loading="lazy"><span><span class="cat-name">1 · {t('Fritos', 'Fried food', 'Fritures')}</span><span class="t">{t('Fritos e inflamación: ¿qué pasa cuando abusas?', 'Fried food and inflammation: what if you overdo it?', f'Fritures et inflammation{NB}: que se passe-t-il quand on abuse{NB}?')}<span class="here-tag">{t('Estás aquí', 'You are here', 'Vous êtes ici')}</span></span></span></div></li>
      <li><div><span></span><span><span class="cat-name">2 · {t('Próximamente', 'Coming soon', 'Bientôt')}</span><span class="t">{t('Cáncer de colon en jóvenes: ¿por qué aumenta?', 'Colon cancer in young people: why is it rising?', f'Cancer du côlon chez les jeunes{NB}: pourquoi augmente-t-il{NB}?')}</span></span></div></li>
    </ol>
  </nav>
  <!-- /serie:colon -->
'''

html = page(
    title_tag='Fritos e inflamación',
    description='Las fuentes detrás de la story sobre fritos e inflamación: qué notas tras una comida grasa, qué pasa cuando es costumbre, el colon, el corazón, la freidora de aire y la regulación en Europa y América. / The sources behind the story on fried food and inflammation.',
    h1=t('Fritos e inflamación: <em>las fuentes</em>', 'Fried food and inflammation: <em>the sources</em>', 'Fritures et inflammation&nbsp;: <em>les sources</em>'),
    lede=t('Dos comidas con fritos en una semana y lo notas. ¿Es inflamación? Aquí están los estudios detrás de cada cifra de la story: qué pasa tras una comida grasa, qué cambia cuando se vuelve costumbre, qué se sabe del colon y del cáncer, y qué no demuestran. Con el tipo de evidencia de cada uno.',
           'Two fried meals in a week and you feel it. Is it inflammation? Here are the studies behind each number in the story: what happens after a fatty meal, what changes when it becomes a habit, what’s known about the colon and cancer, and what they don’t show. With the type of evidence for each.',
           'Deux repas frits dans la semaine et on le sent. Est-ce de l’inflammation ? Voici les études derrière chaque chiffre de la story : ce qui se passe après un repas gras, ce qui change quand cela devient une habitude, ce qu’on sait du côlon et du cancer, et ce qu’elles ne montrent pas. Avec le type de preuve de chacune.'),
    legend_html=legend(['meta', 'obs', 'lab', 'food', 'rev']),
    sections=S,
    alt='Las stories en español, inglés y francés: Fritos e inflamación: ¿qué pasa cuando abusas? / Fried food and inflammation: what if you overdo it? / Fritures et inflammation : que se passe-t-il quand on abuse ?',
    footer=t('Contenido divulgativo; no sustituye el consejo médico. Si tienes sangre en las heces, dolor abdominal persistente o cambios en el ritmo intestinal, consulta a tu médico.',
             'For general information only, not medical advice. If you have blood in your stool, persistent abdominal pain or changes in bowel habits, see your doctor.',
             'Contenu de vulgarisation, pas un avis médical. En cas de sang dans les selles, de douleurs abdominales persistantes ou de changement du transit, consultez votre médecin.'),
)
assert html.count('  </header>\n') == 1
html = html.replace('  </header>\n', '  </header>\n\n' + SERIE, 1)
(OUT / 'index.html').write_text(html)
print('ok', len(html))
