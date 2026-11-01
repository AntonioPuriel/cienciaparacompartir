"""Texto de las stories «semillas» (ES/EN/FR), diseño «desierto» (render_desierto.py).
Miniserie en una sola story: ancestral, antiinflamatorio, intestino y moda, una cifra por ángulo.
La historia completa, la tabla de semillas y la regulación van en la página del repo."""

N = " "  # espacio de no separación

# Sin franja reservada para el sticker: el texto baja hasta las rocas.
LIMIT = 1660

DESIERTO = {
    "es": {
        "eyebrow": "Ciencia para compartir",
        "title": "Semillas: ¿alimento ancestral, antiinflamatorio o moda?",
        "sub": "Linaza, chía y compañía: qué dicen los estudios y qué no",
        "stops": [
            ("10", "mil años", "**Ya se cultivaba calabaza en Oaxaca;** la linaza fue de los primeros cultivos del Creciente Fértil.",
             "Smith 1997 · arqueología"),
            ("54", "ensayos", "**¿Antiinflamatorio?** La linaza bajó la PCR y la IL-6, aunque los estudios varían mucho.",
             "Musazadeh 2024 · metaanálisis"),
            ("1", "semana", "**En el intestino,** las bacterias convierten los lignanos de la linaza en enterolactona, que llega a la sangre.",
             "Lagkouvardos 2015 · ensayo piloto"),
            (f"0{N}kg", "¿moda?", "**La chía no adelgaza:** no cambió el peso ni la grasa corporal en los ensayos.",
             "TaghipourSheshdeh 2025 · metaanálisis"),
        ],
        "end": ("**Lo que no demuestran:** casi todos los ensayos son de linaza y chía, pequeños y cortos, y bajar un marcador no es prevenir una enfermedad. **La clave:** ni remedio ni moda, un alimento antiguo con efectos modestos.",
                "Askarpour 2019 · Musazadeh 2024"),
        "repo": "**La historia completa,** con todas las fuentes, en el repo.",
    },
    "en": {
        "eyebrow": "Science to share",
        "title": "Seeds: ancestral food, anti-inflammatory or fad?",
        "sub": "Flax, chia and friends: what the studies say and what they don’t",
        "stops": [
            ("10", "thousand years", "**Squash was already grown in Oaxaca;** flax was among the first crops of the Fertile Crescent.",
             "Smith 1997 · archaeology"),
            ("54", "trials", "**Anti-inflammatory?** Flaxseed lowered CRP and IL-6, though results vary widely between studies.",
             "Musazadeh 2024 · meta-analysis"),
            ("1", "week", "**In the gut,** bacteria turn flaxseed lignans into enterolactone, which reaches the blood.",
             "Lagkouvardos 2015 · pilot trial"),
            ("0 kg", "fad?", "**Chia doesn’t slim you down:** it didn’t change weight or body fat in trials.",
             "TaghipourSheshdeh 2025 · meta-analysis"),
        ],
        "end": ("**What they don’t show:** almost all trials are on flax and chia, small and short, and lowering a marker isn’t preventing a disease. **The key:** neither remedy nor fad, an ancient food with modest effects.",
                "Askarpour 2019 · Musazadeh 2024"),
        "repo": "**The full story,** with every source, in the repo.",
    },
    "fr": {
        "eyebrow": "La science à partager",
        "title": f"Graines{N}: aliment ancestral, anti-inflammatoire ou mode{N}?",
        "sub": f"Lin, chia et compagnie{N}: ce que disent les études et ce qu’elles ne disent pas",
        "stops": [
            ("10", "mille ans", f"**On cultivait déjà la courge à Oaxaca{N};** le lin fut l’une des premières cultures du Croissant fertile.",
             "Smith 1997 · archéologie"),
            ("54", "essais", f"**Anti-inflammatoire{N}?** Le lin a fait baisser la CRP et l’IL-6, mais les résultats varient beaucoup.",
             "Musazadeh 2024 · méta-analyse"),
            ("1", "semaine", "**Dans l’intestin,** les bactéries transforment les lignanes du lin en entérolactone, qui passe dans le sang.",
             "Lagkouvardos 2015 · essai pilote"),
            (f"0{N}kg", f"mode{N}?", f"**Le chia ne fait pas maigrir{N}:** il n’a changé ni le poids ni la masse grasse dans les essais.",
             "TaghipourSheshdeh 2025 · méta-analyse"),
        ],
        "end": (f"**Ce que les études ne démontrent pas{N}:** presque tous les essais portent sur le lin et le chia, petits et courts, et faire baisser un marqueur n’est pas prévenir une maladie. **La clé{N}:** ni remède ni mode, un aliment ancien aux effets modestes.",
                "Askarpour 2019 · Musazadeh 2024"),
        "repo": "**L’histoire complète,** avec toutes les sources, dans le repo.",
    },
}
