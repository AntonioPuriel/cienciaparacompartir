"""Texto de las stories «dieta ancestral» (ES/EN/FR).
Versión publicada: DESIERTO (pasado → presente, una cifra grande por parada), con render_desierto.py.
STORIES es el borrador narrativo anterior, con el diseño estándar (render_stories.py).
Cada punto: (icono, texto con **negritas**, cita abreviada).
La historia completa, con todos los datos, va en la página del repo.
LAYOUT = 'pie': todo el texto sobre fondo crema y las dunas solo al pie."""

LAYOUT = "pie"

STORIES = {
    "es": {
        "eyebrow": "Ciencia para compartir",
        "title": "Dieta ancestral: ¿la clave está en comer como antes?",
        "sub": "Un viaje de 2 millones de años en tres paradas",
        "items": [
            ("🐢", "**Hace 2 millones de años,** junto a un lago de Kenia, ya se cortaban peces, tortugas y cocodrilos. ¿Comíamos sobre todo carne? Hoy se duda.",
             "Braun 2010 · Barr 2022 · yacimientos"),
            ("🌰", "**Hace 15 000 años,** en Marruecos y antes de la agricultura, la mitad de la dieta eran bellotas, piñones y legumbres silvestres.",
             "Moubtahij 2024 · isótopos"),
            ("🏹", "**Hoy,** quienes aún cazan y recolectan comen mitad planta, mitad animal, según el clima. Y los tsimane (Bolivia) tienen las arterias más sanas medidas.",
             "Pontzer 2021 · revisión · Kaplan 2017 · asociación"),
            ("🛒", "**¿Y la «paleo» del súper?** En ensayos, igual que otras dietas sanas.",
             "Jamka 2020 · metaanálisis"),
            ("🔍", "**Lo que no demuestran:** que una dieta sea mejor por ser antigua. Lo que se repite en todo el viaje: variedad, mucha planta, pescado y nada ultraprocesado.",
             "Jamka 2020 · Lane 2024"),
            ("📂", "**La historia completa,** con todas las fuentes, en el repo.", ""),
        ],
    },
    "en": {
        "eyebrow": "Science to share",
        "title": "Ancestral diet: is the key eating like we used to?",
        "sub": "A 2-million-year journey in three stops",
        "items": [
            ("🐢", "**2 million years ago,** by a lake in Kenya, fish, turtles and crocodiles were already being butchered. Did we eat mostly meat? That’s now in doubt.",
             "Braun 2010 · Barr 2022 · sites"),
            ("🌰", "**15,000 years ago,** in Morocco and before farming, half the diet was acorns, pine nuts and wild legumes.",
             "Moubtahij 2024 · isotopes"),
            ("🏹", "**Today,** people who still hunt and gather eat half plants, half animals, depending on climate. And the Tsimane (Bolivia) have the healthiest arteries ever measured.",
             "Pontzer 2021 · review · Kaplan 2017 · association"),
            ("🛒", "**And supermarket “paleo”?** In trials, no better than other healthy diets.",
             "Jamka 2020 · meta-analysis"),
            ("🔍", "**What they don’t show:** that a diet is better because it’s old. What repeats along the journey: variety, lots of plants, fish and nothing ultra-processed.",
             "Jamka 2020 · Lane 2024"),
            ("📂", "**The full story,** with every source, in the repo.", ""),
        ],
    },
    "fr": {
        "eyebrow": "La science à partager",
        "title": "Manger comme nos ancêtres, est-ce la clé ?",
        "sub": "Un voyage de 2 millions d’années en trois étapes",
        "items": [
            ("🐢", "**Il y a 2 millions d’années,** au bord d’un lac au Kenya, on découpait déjà poissons, tortues et crocodiles. Mangions-nous surtout de la viande ? On en doute aujourd’hui.",
             "Braun 2010 · Barr 2022 · sites"),
            ("🌰", "**Il y a 15 000 ans,** au Maroc et avant l’agriculture, la moitié de l’alimentation était faite de glands, de pignons et de légumineuses sauvages.",
             "Moubtahij 2024 · isotopes"),
            ("🏹", "**Aujourd’hui,** les chasseurs-cueilleurs mangent moitié végétal, moitié animal, selon le climat. Et les Tsimane (Bolivie) ont les artères les plus saines mesurées.",
             "Pontzer 2021 · revue · Kaplan 2017 · association"),
            ("🛒", "**Et le « paléo » du supermarché ?** Dans les essais, pas mieux que d’autres régimes sains.",
             "Jamka 2020 · méta-analyse"),
            ("🔍", "**Ce que les études ne démontrent pas :** qu’un régime soit meilleur parce qu’il est ancien. Ce qui revient tout au long du voyage : variété, beaucoup de végétal, du poisson et rien d’ultra-transformé.",
             "Jamka 2020 · Lane 2024"),
            ("📂", "**L’histoire complète,** avec toutes les sources, dans le repo.", ""),
        ],
    },
}

# Versión «desierto»: narrativa pasado → presente, una cifra grande por parada.
# La renderiza render_desierto.py.
DESIERTO = {
    "es": {
        "eyebrow": "Ciencia para compartir",
        "title": "Dieta ancestral: ¿la clave está en comer como antes?",
        "sub": "De comer lo que había a comer carne sin medida",
        "stops": [
            ("1,95", "millones de años", "**Junto a un lago de Kenia** comíamos lo que había: peces, tortugas, cocodrilos y antílopes. ¿«La carne nos hizo humanos»? El registro no muestra más carne con *Homo erectus*.",
             "Braun 2010 · Barr 2022 · yacimientos"),
            ("50 %", "plantas", "**Hace 15 000 años, en Marruecos,** antes de la agricultura, la mitad de la dieta eran bellotas, piñones y legumbres silvestres.",
             "Moubtahij 2024 · isótopos"),
            ("×5", "más carne", "**Hoy producimos 361 millones de toneladas de carne al año,** cinco veces más que en 1961.",
             "FAO 2026 · estadísticas"),
            ("83 %", "de la tierra agrícola", "**se dedica a productos animales,** que solo dan el 18 % de las calorías que comemos.",
             "Poore 2018 · síntesis de 40 000 granjas"),
        ],
        "end": ("**Lo que no demuestran:** que nuestros antepasados no comieran carne. La comían cuando podían, y cuánta variaba según el lugar. Lo nuevo es la escala. **La clave** que se repite: mucha planta, pescado, poca carne y nada ultraprocesado.",
                "Pontzer 2021 · EAT-Lancet 2025"),
        "repo": "**La historia completa,** con todas las fuentes, en el repo.",
    },
    "en": {
        "eyebrow": "Science to share",
        "title": "Ancestral diet: is the key eating like we used to?",
        "sub": "From eating whatever was there to eating meat without limit",
        "stops": [
            ("1.95", "million years", "**By a lake in Kenya** we ate whatever was there: fish, turtles, crocodiles and antelopes. “Meat made us human”? The record shows no rise in meat with *Homo erectus*.",
             "Braun 2010 · Barr 2022 · sites"),
            ("50%", "plants", "**15,000 years ago in Morocco,** before farming, half the diet was acorns, pine nuts and wild legumes.",
             "Moubtahij 2024 · isotopes"),
            ("×5", "more meat", "**Today we produce 361 million tonnes of meat a year,** five times more than in 1961.",
             "FAO 2026 · statistics"),
            ("83%", "of farmland", "**goes to animal products,** which provide just 18% of the calories we eat.",
             "Poore 2018 · synthesis of 40,000 farms"),
        ],
        "end": ("**What they don’t show:** that our ancestors didn’t eat meat. They ate it when they could, and how much varied from place to place. What’s new is the scale. **The key** that keeps repeating: lots of plants, fish, little meat and nothing ultra-processed.",
                "Pontzer 2021 · EAT-Lancet 2025"),
        "repo": "**The full story,** with every source, in the repo.",
    },
    "fr": {
        "eyebrow": "La science à partager",
        "title": "Manger comme nos ancêtres, est-ce la clé ?",
        "sub": "De manger ce qu’il y avait à manger de la viande sans mesure",
        "stops": [
            ("1,95", "million d’années", "**Au bord d’un lac au Kenya,** on mangeait ce qu’il y avait : poissons, tortues, crocodiles et antilopes. « La viande nous a rendus humains » ? Les fouilles ne montrent pas plus de viande avec *Homo erectus*.",
             "Braun 2010 · Barr 2022 · sites"),
            ("50 %", "végétal", "**Il y a 15 000 ans au Maroc,** avant l’agriculture, la moitié de l’alimentation était faite de glands, de pignons et de légumineuses sauvages.",
             "Moubtahij 2024 · isotopes"),
            ("×5", "de viande", "**Aujourd’hui, on produit 361 millions de tonnes de viande par an,** cinq fois plus qu’en 1961.",
             "FAO 2026 · statistiques"),
            ("83 %", "des terres agricoles", "**servent aux produits animaux,** qui ne fournissent que 18 % des calories que nous mangeons.",
             "Poore 2018 · synthèse de 40 000 fermes"),
        ],
        "end": ("**Ce que les études ne démontrent pas :** que nos ancêtres ne mangeaient pas de viande. Ils en mangeaient quand ils pouvaient, et la quantité variait selon le lieu. Ce qui est nouveau, c’est l’échelle. **La clé** qui revient toujours : beaucoup de végétal, du poisson, peu de viande et rien d’ultra-transformé.",
                "Pontzer 2021 · EAT-Lancet 2025"),
        "repo": "**L’histoire complète,** avec toutes les sources, dans le repo.",
    },
}
