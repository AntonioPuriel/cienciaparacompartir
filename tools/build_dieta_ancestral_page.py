"""Genera ciencia-salud/dieta-ancestral/index.html (ES/EN/FR).
La página cuenta la historia completa en el mismo orden que la story:
fósiles → neandertales y almidón → Taforalt → pueblos actuales → la paleo de hoy → guías."""
import sys, pathlib
from healthkit import t, section, ref, CH, OLD, LEGEND_ITEMS, page

OUT = pathlib.Path(sys.argv[1])

# Etiquetas propias de este tema: evidencia arqueológica y genética.
CH['arq'] = ('obs', t('Yacimiento', 'Site', 'Site'))
CH['gen'] = ('lab', t('ADN antiguo', 'Ancient DNA', 'ADN ancien'))

LEGEND = f'''  <div class="legend">
    <p><span class="chip {CH['arq'][0]}">{CH['arq'][1]}</span><span>{t('Huesos, dientes, herramientas o restos de comida de un yacimiento. Dice qué se comió en ese lugar y momento, no qué comía toda la humanidad.', 'Bones, teeth, tools or food remains from a site. It tells what was eaten in that place and time, not what all of humanity ate.', 'Os, dents, outils ou restes alimentaires d’un site. Indique ce qu’on mangeait à cet endroit et à cette époque, pas ce que mangeait toute l’humanité.')}</span></p>
    <p><span class="chip {CH['gen'][0]}">{CH['gen'][1]}</span><span>{t('Genes de personas antiguas o bacterias del sarro dental. Muestran adaptaciones a lo largo de miles de años.', 'Genes from ancient people or bacteria in dental tartar. They show adaptations over thousands of years.', 'Gènes de personnes anciennes ou de bactéries du tartre dentaire. Ils montrent des adaptations sur des milliers d’années.')}</span></p>
    <p><span class="chip {CH['rev'][0]}">{CH['rev'][1]}</span><span>{t('Síntesis narrativa de expertos sobre lo publicado.', 'Narrative expert synthesis of the published work.', 'Synthèse narrative d’experts sur les travaux publiés.')}</span></p>
    <p><span class="chip {CH['meta'][0]}">{CH['meta'][1]}</span><span>{LEGEND_ITEMS['meta']}</span></p>
    <p><span class="chip {CH['obs'][0]}">{CH['obs'][1]}</span><span>{LEGEND_ITEMS['obs']}</span></p>
    <p><span class="chip rev">{OLD}</span><span>{t('Estudio de antes de 2020: lo citamos cuando sigue siendo la referencia original del hallazgo.', 'Study from before 2020: cited when it is still the original reference for the finding.', 'Étude antérieure à 2020 : citée quand elle reste la référence originale du résultat.')}</span></p>
  </div>
'''

S = []

# 1. Hace 2-3 millones de años
S.append(section(t('Los primeros homínidos: ¿la carne nos hizo humanos?', 'The first hominins: did meat make us human?', 'Les premiers hominines : la viande nous a-t-elle rendus humains ?'), '\n'.join([
    ref('Lüdecke T, Leichliter JN, Stratford D, et al. · Science · 2025; 387(6731): 309–314',
        'Australopithecus at Sterkfontein did not consume substantial mammalian meat',
        t('Midieron isótopos de nitrógeno atrapados en el esmalte dental de siete <i>Australopithecus</i> de Sterkfontein (Sudáfrica) y de los animales del mismo yacimiento. Su señal se parecía a la de los herbívoros, no a la de los carnívoros: una dieta variable pero basada en plantas, sin consumo regular de carne de mamífero.',
          'They measured nitrogen isotopes trapped in the tooth enamel of seven <i>Australopithecus</i> from Sterkfontein (South Africa) and of the animals from the same site. Their signal looked like that of herbivores, not carnivores: a variable but plant-based diet, with no regular eating of mammal meat.',
          'Ils ont mesuré les isotopes d’azote piégés dans l’émail dentaire de sept <i>Australopithecus</i> de Sterkfontein (Afrique du Sud) et des animaux du même site. Leur signal ressemblait à celui des herbivores, pas des carnivores : une alimentation variable mais végétale, sans consommation régulière de viande de mammifère.'),
        ['arq'], doi='10.1126/science.adq7315'),
    ref('Braun DR, Harris JWK, Levin NE, et al. · PNAS · 2010; 107: 10002–10007',
        'Early hominin diet included diverse terrestrial and aquatic animals 1.95 Ma in East Turkana, Kenya',
        t('En un yacimiento de hace 1,95 millones de años junto a un antiguo lago en Kenia aparecieron, con marcas de herramientas de piedra, huesos de antílopes y también de peces, tortugas y cocodrilos. Es la prueba más antigua de que nuestros antepasados comían animales acuáticos, una fuente de ácidos grasos omega-3 como el DHA.',
          'At a 1.95-million-year-old site by an ancient lake in Kenya, bones bearing stone-tool marks belonged to antelopes and also to fish, turtles and crocodiles. It is the oldest evidence that our ancestors ate aquatic animals, a source of omega-3 fatty acids such as DHA.',
          'Sur un site vieux de 1,95 million d’années au bord d’un ancien lac au Kenya, des os portant des marques d’outils en pierre appartenaient à des antilopes, mais aussi à des poissons, des tortues et des crocodiles. C’est la plus ancienne preuve que nos ancêtres mangeaient des animaux aquatiques, une source d’acides gras oméga-3 comme le DHA.'),
        ['arq'], doi='10.1073/pnas.1002181107', old=True),
    ref('Barr WA, Pobiner B, Rowan J, Du A, Faith JT · PNAS · 2022; 119(5): e2115540119',
        'No sustained increase in zooarchaeological evidence for carnivory after the appearance of Homo erectus',
        t('La idea de que «la carne nos hizo humanos» se apoya en que hay más huesos con marcas de corte cuando aparece <i>Homo erectus</i>. Este equipo reunió los yacimientos del este de África (de 2,6 a 1,2 millones de años) y vio que esas pruebas aumentan sobre todo porque esos periodos se han excavado más. Corrigiendo por el esfuerzo de excavación, no hay un aumento sostenido del consumo de carne.',
          'The idea that “meat made us human” rests on there being more bones with cut marks when <i>Homo erectus</i> appears. This team gathered the sites of eastern Africa (2.6 to 1.2 million years ago) and found that this evidence rises mainly because those periods have been excavated more. Correcting for excavation effort, there is no sustained increase in meat eating.',
          'L’idée que « la viande nous a rendus humains » repose sur le fait qu’on trouve plus d’os portant des traces de découpe quand apparaît <i>Homo erectus</i>. Cette équipe a rassemblé les sites d’Afrique de l’Est (de 2,6 à 1,2 million d’années) et a montré que ces indices augmentent surtout parce que ces périodes ont été davantage fouillées. En corrigeant par l’effort de fouille, il n’y a pas d’augmentation durable de la consommation de viande.'),
        ['arq', 'meta'], doi='10.1073/pnas.2115540119'),
    ref('Ben-Dor M, Sirtoli R, Barkai R · American Journal of Physical Anthropology · 2021; 175(S72): 27–56',
        'The evolution of the human trophic level during the Pleistocene',
        t('<b>La postura contraria.</b> A partir de 25 líneas de evidencia (fisiología, genética, arqueología, ecología), los autores sostienen que el linaje humano se volvió muy carnívoro desde <i>Homo habilis</i>, con un máximo en <i>Homo erectus</i>, y que solo volvió hacia las plantas en el Paleolítico superior y con la agricultura.',
          '<b>The opposing view.</b> Drawing on 25 lines of evidence (physiology, genetics, archaeology, ecology), the authors argue that the human lineage became highly carnivorous from <i>Homo habilis</i>, peaking in <i>Homo erectus</i>, and only turned back towards plants in the Upper Palaeolithic and with farming.',
          '<b>La position inverse.</b> À partir de 25 lignes de preuves (physiologie, génétique, archéologie, écologie), les auteurs soutiennent que la lignée humaine est devenue très carnivore dès <i>Homo habilis</i>, avec un maximum chez <i>Homo erectus</i>, et ne s’est tournée vers les végétaux qu’au Paléolithique supérieur et avec l’agriculture.'),
        ['rev'], doi='10.1002/ajpa.24247'),
]), t('Los yacimientos son pocos y dispersos: cada uno dice qué se comió en un lugar y un momento, no cuál era la dieta de la especie. Barr no demuestra que se comiera poca carne, sino que el registro no basta para afirmar que se comía cada vez más. Lüdecke estudió siete individuos de un solo sitio. Por eso la story dice «hoy se duda» y no «era falso»: el debate sigue abierto, como muestra Ben-Dor.',
      'Sites are few and scattered: each one tells what was eaten in one place and time, not what the species’ diet was. Barr doesn’t show that little meat was eaten, only that the record isn’t enough to claim it was eaten more and more. Lüdecke studied seven individuals from a single site. That’s why the story says “now in doubt” and not “it was false”: the debate is still open, as Ben-Dor shows.',
      'Les sites sont rares et dispersés : chacun dit ce qu’on mangeait en un lieu et à un moment, pas quelle était l’alimentation de l’espèce. Barr ne montre pas qu’on mangeait peu de viande, seulement que les données ne suffisent pas pour affirmer qu’on en mangeait de plus en plus. Lüdecke a étudié sept individus d’un seul site. C’est pourquoi la story dit « on en doute » et non « c’était faux » : le débat reste ouvert, comme le montre Ben-Dor.')))

# 2. Neandertales, marisco y almidón
S.append(section(t('Neandertales: marisco, piñones y almidón', 'Neanderthals: shellfish, pine nuts and starch', 'Néandertaliens : coquillages, pignons et amidon'), '\n'.join([
    ref('Zilhão J, Angelucci DE, Igreja MA, et al. · Science · 2020; 367(6485): eaaz7943',
        'Last Interglacial Iberian Neandertals as fisher-hunter-gatherers',
        t('En la cueva de Figueira Brava (Portugal), de hace unos 100 000 años, los neandertales dejaron montones de conchas de moluscos, cangrejos y peces, junto a piñones y animales terrestres. Explotaban el mar a la par que los humanos modernos del sur de África de la misma época.',
          'In the Figueira Brava cave (Portugal), about 100,000 years old, Neanderthals left heaps of mollusc shells, crabs and fish, together with pine nuts and land animals. They exploited the sea on a par with modern humans in southern Africa at the same time.',
          'Dans la grotte de Figueira Brava (Portugal), vieille d’environ 100 000 ans, les Néandertaliens ont laissé des amas de coquilles de mollusques, de crabes et de poissons, avec des pignons et des animaux terrestres. Ils exploitaient la mer autant que les humains modernes d’Afrique australe à la même époque.'),
        ['arq'], doi='10.1126/science.aaz7943'),
    ref('Fellows Yates JA, Velsko IM, Aron F, et al. · PNAS · 2021; 118(20): e2021655118',
        'The evolution and changing ecology of the African hominid oral microbiome',
        t('Secuenciaron el ADN de las bacterias del sarro dental de neandertales, humanos antiguos y actuales, chimpancés, gorilas y monos aulladores: 124 muestras, algunas de hace 100 000 años. Los neandertales y los humanos modernos compartían bacterias capaces de unirse a la amilasa de la saliva, la enzima que digiere el almidón. Los autores lo interpretan como una adaptación a comer alimentos ricos en almidón.',
          'They sequenced DNA from bacteria in the dental tartar of Neanderthals, ancient and present-day humans, chimpanzees, gorillas and howler monkeys: 124 samples, some 100,000 years old. Neanderthals and modern humans shared bacteria able to bind salivary amylase, the enzyme that digests starch. The authors read this as an adaptation to eating starch-rich foods.',
          'Ils ont séquencé l’ADN des bactéries du tartre dentaire de Néandertaliens, d’humains anciens et actuels, de chimpanzés, de gorilles et de singes hurleurs : 124 échantillons, certains vieux de 100 000 ans. Néandertaliens et humains modernes partageaient des bactéries capables de se lier à l’amylase salivaire, l’enzyme qui digère l’amidon. Les auteurs y voient une adaptation à une alimentation riche en amidon.'),
        ['gen'], doi='10.1073/pnas.2021655118'),
    ref('Yılmaz F, Karageorgiou C, Kim K, et al. · Science · 2024; 386: eadn0609',
        'Reconstruction of the human amylase locus reveals ancient duplications seeding modern-day variation',
        t('El gen de la amilasa salival (<i>AMY1</i>) se duplicó hace más de 800 000 años, antes de que nos separáramos de los neandertales. Los cazadores-recolectores de hace hasta 45 000 años ya tenían de 4 a 8 copias. Después, con la agricultura, las copias aumentaron en Europa, probablemente por dietas más ricas en almidón.',
          'The salivary amylase gene (<i>AMY1</i>) duplicated more than 800,000 years ago, before we split from Neanderthals. Hunter-gatherers from as far back as 45,000 years ago already had 4 to 8 copies. Later, with farming, copy numbers rose in Europe, probably because of starch-richer diets.',
          'Le gène de l’amylase salivaire (<i>AMY1</i>) s’est dupliqué il y a plus de 800 000 ans, avant notre séparation d’avec les Néandertaliens. Les chasseurs-cueilleurs d’il y a jusqu’à 45 000 ans avaient déjà 4 à 8 copies. Ensuite, avec l’agriculture, le nombre de copies a augmenté en Europe, probablement à cause d’alimentations plus riches en amidon.'),
        ['gen'], doi='10.1126/science.adn0609'),
]), t('Que los genes y las bacterias de la boca estén adaptados al almidón indica que lo comíamos desde hace mucho, no cuánto. Figueira Brava es un solo yacimiento costero: no dice que todos los neandertales comieran marisco.',
      'Genes and mouth bacteria adapted to starch indicate that we have eaten it for a long time, not how much. Figueira Brava is a single coastal site: it doesn’t say all Neanderthals ate shellfish.',
      'Que les gènes et les bactéries de la bouche soient adaptés à l’amidon indique qu’on en mange depuis longtemps, pas en quelle quantité. Figueira Brava est un seul site côtier : il ne dit pas que tous les Néandertaliens mangeaient des coquillages.')))

# 3. Taforalt
S.append(section(t('Hace 15 000 años: antes de la agricultura, mucha planta', '15,000 years ago: before farming, lots of plants', 'Il y a 15 000 ans : avant l’agriculture, beaucoup de végétal'), '\n'.join([
    ref('Moubtahij Z, McCormack J, Bourgon N, et al. · Nature Ecology & Evolution · 2024; 8: 1035–1045',
        'Isotopic evidence of high reliance on plant food among Later Stone Age hunter-gatherers at Taforalt, Morocco',
        t('En la cueva de Taforalt (Marruecos), de hace 15 000 a 13 000 años, los isótopos de nitrógeno, carbono y zinc de huesos y dientes humanos sitúan a sus habitantes cerca de los herbívoros: alrededor de la mitad de su dieta eran plantas. Los restos carbonizados apuntan a bellotas, piñones y legumbres silvestres, y había piedras de moler. Un bebé parece haber sido destetado antes del año, quizá con papillas vegetales. Las caries eran frecuentes, algo que los autores relacionan con tanto almidón.',
          'At Taforalt cave (Morocco), 15,000 to 13,000 years ago, nitrogen, carbon and zinc isotopes from human bones and teeth place its inhabitants close to herbivores: about half their diet was plants. Charred remains point to acorns, pine nuts and wild legumes, and there were grinding stones. One infant seems to have been weaned before age one, perhaps on plant mush. Tooth decay was common, which the authors link to so much starch.',
          'Dans la grotte de Taforalt (Maroc), il y a 15 000 à 13 000 ans, les isotopes d’azote, de carbone et de zinc des os et des dents humains placent ses habitants près des herbivores : environ la moitié de leur alimentation était végétale. Les restes carbonisés indiquent des glands, des pignons et des légumineuses sauvages, et il y avait des meules. Un bébé semble avoir été sevré avant un an, peut-être avec des bouillies végétales. Les caries étaient fréquentes, ce que les auteurs relient à l’abondance d’amidon.'),
        ['arq'], doi='10.1038/s41559-024-02382-z'),
]), t('No eran vegetarianos: también hay huesos de animales con marcas de corte. Es un solo grupo en un solo lugar; en otros lugares y climas la proporción pudo ser muy distinta. Y las caries recuerdan que «natural» no es lo mismo que «sano en todo».',
      'They weren’t vegetarian: there are also animal bones with cut marks. It’s a single group in a single place; in other places and climates the share may have been very different. And the tooth decay is a reminder that “natural” isn’t the same as “healthy in every way”.',
      'Ils n’étaient pas végétariens : on trouve aussi des os d’animaux avec des traces de découpe. C’est un seul groupe en un seul lieu ; ailleurs et sous d’autres climats, la part a pu être très différente. Et les caries rappellent que « naturel » ne veut pas dire « sain en tout ».')))

# 4. Hoy
S.append(section(t('Hoy: quienes aún cazan, pescan y recolectan', 'Today: people who still hunt, fish and gather', 'Aujourd’hui : ceux qui chassent, pêchent et cueillent encore'), '\n'.join([
    ref('Pontzer H, Wood BM · Annual Review of Nutrition · 2021; 41: 363–385',
        'Effects of Evolution, Ecology, and Economy on Human Diet: Insights from Hunter-Gatherers and Other Small-Scale Societies',
        t('En los cazadores-recolectores actuales de climas cálidos lo habitual es una dieta de mitad planta, mitad animal, pero las proporciones varían mucho. En climas fríos y en pueblos que viven de la pesca o del pastoreo se come más carne; donde hay algo de agricultura, más planta. Los hadza de Tanzania, por ejemplo, comen mucha fibra y suficiente proteína, y su dieta cambia de un mes a otro. No hubo una sola «dieta paleolítica».',
          'Among present-day hunter-gatherers in warm climates, a half-plant, half-animal diet is typical, but proportions vary widely. In cold climates and among peoples who live from fishing or herding, more meat is eaten; where there is some farming, more plants. The Hadza of Tanzania, for instance, eat lots of fibre and enough protein, and their diet changes from month to month. There was no single “Palaeolithic diet”.',
          'Chez les chasseurs-cueilleurs actuels des climats chauds, une alimentation moitié végétale, moitié animale est habituelle, mais les proportions varient beaucoup. Dans les climats froids et chez les peuples qui vivent de la pêche ou de l’élevage, on mange plus de viande ; là où il y a un peu d’agriculture, plus de végétal. Les Hadza de Tanzanie, par exemple, mangent beaucoup de fibres et assez de protéines, et leur alimentation change d’un mois à l’autre. Il n’y a pas eu une seule « alimentation paléolithique ».'),
        ['rev'], doi='10.1146/annurev-nutr-111120-105520'),
    ref('Kaplan H, Thompson RC, Trumble BC, et al. · The Lancet · 2017; 389(10080): 1730–1739',
        'Coronary atherosclerosis in indigenous South American Tsimane: a cross-sectional cohort study',
        t('Hicieron un TAC del corazón a 705 tsimane de la Amazonía boliviana, de 40 a 94 años. El 85 % no tenía calcio en las arterias coronarias, la prevalencia de aterosclerosis más baja medida en cualquier población. Su dieta: un 72 % de carbohidratos sin procesar (arroz, plátano macho, yuca, maíz), un 14 % de proteína, sobre todo de caza y pescado, y un 14 % de grasa. Y pasan solo un 10 % del día inactivos.',
          'They gave heart CT scans to 705 Tsimane from the Bolivian Amazon, aged 40 to 94. 85% had no calcium in their coronary arteries, the lowest prevalence of atherosclerosis measured in any population. Their diet: 72% unprocessed carbohydrates (rice, plantain, manioc, maize), 14% protein, mostly from game and fish, and 14% fat. And they spend only 10% of the day inactive.',
          'Ils ont fait un scanner du cœur à 705 Tsimane de l’Amazonie bolivienne, âgés de 40 à 94 ans. 85 % n’avaient pas de calcium dans les artères coronaires, la plus faible prévalence d’athérosclérose mesurée dans une population. Leur alimentation : 72 % de glucides non transformés (riz, banane plantain, manioc, maïs), 14 % de protéines, surtout issues de la chasse et de la pêche, et 14 % de graisses. Et ils ne passent que 10 % de la journée inactifs.'),
        ['obs'], doi='10.1016/S0140-6736(17)30752-3', old=True),
]), t('Los cazadores-recolectores actuales no son fósiles vivientes: comercian, algunos cultivan y viven en ambientes concretos. Los tsimane no siguen una dieta ancestral pura (comen arroz y cultivan), y el estudio es transversal: no separa el efecto de la dieta del de la actividad física y el resto de su modo de vida.',
      'Present-day hunter-gatherers aren’t living fossils: they trade, some farm, and they live in specific environments. The Tsimane don’t follow a pure ancestral diet (they eat rice and farm), and the study is cross-sectional: it can’t separate the effect of diet from that of physical activity and the rest of their way of life.',
      'Les chasseurs-cueilleurs actuels ne sont pas des fossiles vivants : ils commercent, certains cultivent et vivent dans des milieux particuliers. Les Tsimane ne suivent pas une alimentation ancestrale pure (ils mangent du riz et cultivent), et l’étude est transversale : elle ne sépare pas l’effet de l’alimentation de celui de l’activité physique et du reste de leur mode de vie.')))

# 5. La paleo de hoy
S.append(section(t('¿Y la dieta «paleo» de hoy?', 'And today’s “paleo” diet?', 'Et le régime « paléo » d’aujourd’hui ?'), '\n'.join([
    ref('Jamka M, Kulczyński B, Juruć A, et al. · Journal of Clinical Medicine · 2020; 9(2): 296',
        'The Effect of the Paleolithic Diet vs. Healthy Diets on Glucose and Insulin Homeostasis: A Systematic Review and Meta-Analysis of Randomized Controlled Trials',
        t('Reunió 4 ensayos aleatorizados con 98 personas con diabetes tipo 2, prediabetes o síndrome metabólico, que duraron de 2 a 12 semanas. Compararon la paleo, que suele excluir cereales, lácteos y legumbres, con otras dietas sanas, como la mediterránea o la recomendada para la diabetes. No hubo diferencias en glucosa, insulina ni hemoglobina glicosilada: ambas mejoraron.',
          'It pooled 4 randomized trials with 98 people with type 2 diabetes, prediabetes or metabolic syndrome, lasting 2 to 12 weeks. They compared paleo, which usually excludes grains, dairy and legumes, with other healthy diets, such as the Mediterranean diet or the one recommended for diabetes. There were no differences in glucose, insulin or glycated haemoglobin: both improved.',
          'Elle a réuni 4 essais randomisés portant sur 98 personnes atteintes de diabète de type 2, de prédiabète ou de syndrome métabolique, d’une durée de 2 à 12 semaines. Ils comparaient le régime paléo, qui exclut en général céréales, produits laitiers et légumineuses, à d’autres régimes sains, comme le méditerranéen ou celui recommandé pour le diabète. Aucune différence sur la glycémie, l’insuline ou l’hémoglobine glyquée : les deux ont amélioré.'),
        ['meta'], doi='10.3390/jcm9020296'),
    ref('Lane MM, Gamage E, Du S, et al. · BMJ · 2024; 384: e077310',
        'Ultra-processed food exposure and adverse health outcomes: umbrella review of epidemiological meta-analyses',
        t('Revisión de 45 análisis combinados con casi 10 millones de personas. Comer más ultraprocesados se asoció con 32 problemas de salud. La evidencia más sólida fue para la mortalidad cardiovascular (un 50 % más de riesgo entre quienes más comen) y la diabetes tipo 2 (un 12 % más por cada 10 % de la dieta en ultraprocesados). Es lo único que ninguna de las dietas de este recorrido tenía.',
          'Review of 45 pooled analyses covering almost 10 million people. Eating more ultra-processed food was linked to 32 health problems. The strongest evidence was for cardiovascular death (50% higher risk among the highest consumers) and type 2 diabetes (12% higher for every 10% of the diet from ultra-processed food). It’s the one thing none of the diets on this journey had.',
          'Revue de 45 analyses combinées portant sur près de 10 millions de personnes. Manger plus d’ultra-transformés était associé à 32 problèmes de santé. Les preuves les plus solides concernaient la mortalité cardiovasculaire (50 % de risque en plus chez les plus gros consommateurs) et le diabète de type 2 (12 % de plus pour chaque 10 % de l’alimentation en ultra-transformés). C’est la seule chose qu’aucune des alimentations de ce voyage n’avait.'),
        ['meta', 'obs'], doi='10.1136/bmj-2023-077310'),
]), t('Jamka tiene pocos ensayos, pequeños y cortos, en personas con exceso de peso: no dice nada del largo plazo ni de la población general. Que la paleo no sea mejor no significa que sea mala; quitar ultraprocesados ya mejora las cifras, y eso lo hacen las dos dietas comparadas. Lane reúne estudios observacionales: muestran asociación, no causa, y la calidad de la evidencia según GRADE va de muy baja a moderada.',
      'Jamka has few trials, small and short, in people with excess weight: it says nothing about the long term or the general population. Paleo not being better doesn’t make it bad; cutting ultra-processed food already improves the numbers, and both compared diets do that. Lane pools observational studies: they show association, not cause, and the GRADE quality of evidence ranges from very low to moderate.',
      'Jamka compte peu d’essais, petits et courts, chez des personnes en surpoids : rien sur le long terme ni sur la population générale. Que le paléo ne soit pas meilleur ne veut pas dire qu’il soit mauvais ; supprimer les ultra-transformés améliore déjà les chiffres, et les deux régimes comparés le font. Lane réunit des études observationnelles : elles montrent une association, pas une cause, et la qualité des preuves selon GRADE va de très faible à modérée.')))


# 6. Guías y normas
def row(where, what, status, links):
    a = ' '.join(f'<a href="{u}">{n}</a>' for n, u in links)
    cls, label = status
    return f'        <tr><td>{where}</td><td>{what} {a}</td><td><span class="st {cls}">{label}</span></td></tr>'

REC = ('part', t('Recomendación', 'Recommendation', 'Recommandation'))
LAW = ('ok', t('Vigente', 'In force', 'En vigueur'))
reg_rows = [
    row(t('México', 'Mexico', 'Mexique'), t('Guías Alimentarias saludables y sostenibles (2023): sobre todo alimentos vegetales sin procesar, frijol, lenteja o haba a diario, menos carne de res y procesada, evitar ultraprocesados y bebidas azucaradas.',
              'Healthy and sustainable dietary guidelines (2023): mainly unprocessed plant foods, beans, lentils or fava beans daily, less beef and processed meat, avoid ultra-processed food and sugary drinks.',
              'Recommandations alimentaires saines et durables (2023) : surtout des aliments végétaux non transformés, haricots, lentilles ou fèves chaque jour, moins de bœuf et de viande transformée, éviter les ultra-transformés et les boissons sucrées.'),
        REC, [('gob.mx', 'https://www.gob.mx/cms/uploads/attachment/file/863927/Infografi_a_de_Policy_Brief_y_Recomendaciones_generales_16Oct23OK.pdf')]),
    row(t('México', 'Mexico', 'Mexique'), t('Sellos de advertencia en el frente del envase (exceso de azúcares, sodio, grasas, calorías): modificación de la NOM-051 publicada en el DOF el 27 de marzo de 2020.',
              'Front-of-pack warning seals (excess sugars, sodium, fats, calories): amendment to NOM-051 published in the Official Gazette on 27 March 2020.',
              'Logos d’avertissement sur le devant de l’emballage (excès de sucres, sodium, graisses, calories) : modification de la NOM-051 publiée au Journal officiel le 27 mars 2020.'),
        LAW, [('gob.mx', 'https://www.gob.mx/cms/uploads/attachment/file/653810/Manual_NOM-051_versio_n_final.pdf')]),
    row(t('México', 'Mexico', 'Mexique'), t('Prohibida la venta de comida de bajo valor nutricional en todas las escuelas: acuerdo publicado en el DOF el 30 de septiembre de 2024, en vigor desde el 29 de marzo de 2025.',
              'Ban on selling low-nutrition food in all schools: agreement published in the Official Gazette on 30 September 2024, in force since 29 March 2025.',
              'Interdiction de vendre des aliments de faible valeur nutritionnelle dans toutes les écoles : accord publié au Journal officiel le 30 septembre 2024, en vigueur depuis le 29 mars 2025.'),
        LAW, [('chihuahua.gob.mx', 'https://www.chihuahua.gob.mx/sites/default/atach2/noticias/adjuntos/2025-03/Inicia%20el%2029%20de%20marzo%20prohibici%C3%B3n%20de%20venta%20de%20comida%20chatarra%20en%20escuelas.docx-1.pdf')]),
    row(t('España', 'Spain', 'Espagne'), t('AESAN (2022): como máximo 3 raciones de carne a la semana, mejor aves y conejo, mínimo de carne procesada; al menos 3 de pescado y 4 de legumbres.',
              'AESAN (2022): at most 3 servings of meat a week, preferably poultry and rabbit, minimal processed meat; at least 3 of fish and 4 of legumes.',
              'AESAN (2022) : au plus 3 portions de viande par semaine, de préférence volaille et lapin, un minimum de viande transformée ; au moins 3 de poisson et 4 de légumineuses.'),
        REC, [('aesan.gob.es', 'https://aesan.gob.es/actualidad/actualidad-noticias/recomendaciones_dieteticas')]),
    row(t('Francia', 'France', 'France'), t('PNNS 4 / Santé publique France (2019): menos de 500 g de carne roja y 150 g de embutido a la semana, legumbres al menos dos veces y pescado dos veces por semana, limitar mucho los ultraprocesados.',
              'PNNS 4 / Santé publique France (2019): under 500 g of red meat and 150 g of cured meats a week, legumes at least twice and fish twice a week, strongly limit ultra-processed food.',
              'PNNS 4 / Santé publique France (2019) : moins de 500 g de viande rouge et 150 g de charcuterie par semaine, légumineuses au moins deux fois et poisson deux fois par semaine, limiter fortement les ultra-transformés.'),
        REC, [('Que Choisir', 'https://www.quechoisir.org/actualite-alimentation-une-assiette-plus-verte-que-rouge-n63807/')]),
    row(t('EE. UU.', 'USA', 'États-Unis'), t('Guías Alimentarias 2025–2030 (7 de enero de 2026): suben la proteína a 1,2–1,6 g por kilo al día, incluyen la carne roja y tres raciones de lácteos enteros, mantienen el límite del 10 % de grasa saturada y piden evitar los alimentos «muy procesados». En proteína y lácteos enteros difieren de las guías europeas y mexicanas.',
              'Dietary Guidelines 2025–2030 (7 January 2026): raise protein to 1.2–1.6 g per kilo a day, include red meat and three servings of whole-fat dairy, keep the 10% saturated-fat limit and advise avoiding “highly processed” foods. On protein and whole-fat dairy they differ from the European and Mexican guidelines.',
              'Recommandations alimentaires 2025–2030 (7 janvier 2026) : protéines relevées à 1,2–1,6 g par kilo et par jour, viande rouge et trois portions de laitages entiers incluses, limite de 10 % de graisses saturées maintenue, et conseil d’éviter les aliments « très transformés ». Sur les protéines et les laitages entiers, elles diffèrent des recommandations européennes et mexicaines.'),
        REC, [('Morrison Foerster', 'https://www.mofo.com/resources/insights/260108-new-u-s-dietary-guidelines-released')]),
    row(t('Unión Europea', 'European Union', 'Union européenne'), t('El etiquetado nutricional frontal armonizado quedó bloqueado en 2025 por falta de acuerdo entre países. El Nutri-Score sigue siendo voluntario en Francia, España, Bélgica, Alemania, Países Bajos, Luxemburgo y Portugal.',
              'Harmonised front-of-pack nutrition labelling stalled in 2025 for lack of agreement between countries. Nutri-Score remains voluntary in France, Spain, Belgium, Germany, the Netherlands, Luxembourg and Portugal.',
              'L’étiquetage nutritionnel harmonisé sur le devant des emballages a été bloqué en 2025 faute d’accord entre pays. Le Nutri-Score reste volontaire en France, en Espagne, en Belgique, en Allemagne, aux Pays-Bas, au Luxembourg et au Portugal.'),
        ('rev', t('Bloqueado', 'Stalled', 'Bloqué')), [('FoodNavigator', 'https://www.foodnavigator.com/Article/2025/03/04/has-the-european-commission-abandoned-nutriscore/')]),
]

S.append(f'''  <section>
    <div class="frame"><h2>{t('Qué dicen hoy las guías oficiales', 'What official guidelines say today', 'Ce que disent aujourd’hui les recommandations officielles')}</h2></div>
    <p class="note">{t('Ninguna recomienda «comer como en el Paleolítico». Pero varias coinciden con lo que se repite en el recorrido: más legumbres y plantas, pescado, menos carne roja y procesada, y menos ultraprocesados.',
                       'None recommends “eating like in the Palaeolithic”. But several match what repeats along the journey: more legumes and plants, fish, less red and processed meat, and less ultra-processed food.',
                       'Aucune ne recommande de « manger comme au Paléolithique ». Mais plusieurs rejoignent ce qui revient tout au long du voyage : plus de légumineuses et de végétaux, du poisson, moins de viande rouge et transformée, et moins d’ultra-transformés.')}</p>
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

html = page(
    title_tag='Dieta ancestral',
    description='Las fuentes detrás de la story sobre la dieta ancestral: fósiles, neandertales, Taforalt, cazadores-recolectores actuales, la dieta paleo y las guías oficiales. / The sources behind the story on ancestral diets.',
    h1=t('Dieta ancestral: <em>la historia completa</em>', 'Ancestral diet: <em>the full story</em>', 'Alimentation ancestrale&nbsp;: <em>l’histoire complète</em>'),
    lede=t('La story recorre 2 millones de años en tres paradas. Aquí está el viaje entero, en el mismo orden: qué comían nuestros antepasados según los fósiles, los genes y el sarro de sus dientes; qué comen hoy quienes aún cazan y recolectan; qué dicen los ensayos sobre la dieta «paleo» y qué recomiendan las guías oficiales. Cada estudio, con su tipo de evidencia y lo que no demuestra.',
           'The story covers 2 million years in three stops. Here is the whole journey, in the same order: what our ancestors ate according to fossils, genes and the tartar on their teeth; what people who still hunt and gather eat today; what trials say about the “paleo” diet and what official guidelines recommend. Each study, with its type of evidence and what it doesn’t show.',
           'La story parcourt 2 millions d’années en trois étapes. Voici le voyage complet, dans le même ordre : ce que mangeaient nos ancêtres d’après les fossiles, les gènes et le tartre de leurs dents ; ce que mangent aujourd’hui ceux qui chassent et cueillent encore ; ce que disent les essais sur le régime « paléo » et ce que recommandent les recommandations officielles. Chaque étude, avec son type de preuve et ce qu’elle ne démontre pas.'),
    legend_html=LEGEND,
    sections=S,
    alt='Las stories en español, inglés y francés: Dieta ancestral: ¿la clave está en comer como antes? / Ancestral diet: is the key eating like we used to? / Manger comme nos ancêtres, est-ce la clé ?',
    footer=t('Contenido divulgativo; no sustituye el consejo médico ni de un dietista. Si tienes diabetes u otra enfermedad, consulta cualquier cambio de dieta con tu equipo de salud.',
             'For general information only, not medical or dietary advice. If you have diabetes or another condition, discuss any diet change with your care team.',
             'Contenu de vulgarisation, pas un avis médical ou diététique. Si vous avez un diabète ou une autre maladie, parlez de tout changement alimentaire à votre équipe soignante.'),
)
(OUT / 'index.html').write_text(html)
print('ok', len(html))
