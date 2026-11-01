"""Texto de las stories «fritos e inflamación» (ES/EN/FR), diseño «desierto» (render_desierto.py).
Cuatro cifras grandes, el recuadro de lo que no demuestran y el cierre hacia el repo.
La historia completa, con todos los datos y la regulación, va en la página del repo."""

N = " "

# Sin franja reservada para el sticker: el texto baja hasta las rocas.
LIMIT = 1660

DESIERTO = {
    "es": {
        "eyebrow": "Ciencia para compartir",
        "title": "Fritos e inflamación: ¿qué pasa cuando abusas?",
        "sub": "La pesadez de un día no es inflamación; la costumbre, sí cuenta",
        "stops": [
            (f"+28{N}%", "riesgo cardiovascular", "**Comer fritos a menudo** se asocia con más infartos e insuficiencia cardíaca.",
             "Qin 2021 · metaanálisis de cohortes"),
            (f"+22{N}%", "pólipos de colon", "**La carne muy frita o asada** forma aminas asociadas a más pólipos, los precursores del cáncer. Con el cáncer, no.",
             "Chiavarini 2017 · metaanálisis"),
            ("32", "frituras", "**El aceite reutilizado** dañó la barrera del intestino, disparó *E. coli* y aumentó los tumores de colon.",
             "Hu 2024 · Zhang 2019 · ratón"),
            ("4/4", "ensayos", "**Comer menos AGEs,** que se forman al freír a alta temperatura, bajó los marcadores inflamatorios en todos los ensayos que los midieron.",
             "Detopoulou 2024 · revisión de ensayos"),
        ],
        "end": ("**Lo que no demuestran:** que los fritos causen cáncer de colon. Los tumores se vieron en ratones; en personas solo hay relación con pólipos, y la acrilamida no se asocia. **La clave:** que no sea costumbre y no reutilizar el aceite.",
                "Chiavarini 2017 · Galeone 2015"),
        "repo": "**La historia completa,** con todas las fuentes, en el repo.",
    },
    "en": {
        "eyebrow": "Science to share",
        "title": "Fried food and inflammation: what if you overdo it?",
        "sub": "One heavy day isn’t inflammation; the habit is what counts",
        "stops": [
            ("+28%", "cardiovascular risk", "**Eating fried food often** is linked to more heart attacks and heart failure.",
             "Qin 2021 · meta-analysis of cohorts"),
            ("+22%", "colon polyps", "**Heavily fried or grilled meat** forms amines linked to more polyps, the precursors of cancer. Not to cancer itself.",
             "Chiavarini 2017 · meta-analysis"),
            ("32", "fryings", "**Reused frying oil** damaged the gut barrier, sent *E. coli* soaring and increased colon tumours.",
             "Hu 2024 · Zhang 2019 · mice"),
            ("4/4", "trials", "**Eating fewer AGEs,** which form when frying at high heat, lowered inflammatory markers in every trial that measured them.",
             "Detopoulou 2024 · review of trials"),
        ],
        "end": ("**What they don’t show:** that fried food causes colon cancer. The tumours were seen in mice; in people there’s only a link with polyps, and acrylamide isn’t associated. **The key:** don’t make it a habit, and don’t reuse the oil.",
                "Chiavarini 2017 · Galeone 2015"),
        "repo": "**The full story,** with every source, in the repo.",
    },
    "fr": {
        "eyebrow": "La science à partager",
        "title": "Fritures et inflammation : que se passe-t-il quand on abuse ?",
        "sub": "La lourdeur d’un jour n’est pas de l’inflammation ; c’est l’habitude qui compte",
        "stops": [
            (f"+28{N}%", "risque cardio-vasculaire", "**Manger souvent des fritures** est associé à plus d’infarctus et d’insuffisance cardiaque.",
             "Qin 2021 · méta-analyse de cohortes"),
            (f"+22{N}%", "polypes du côlon", "**La viande très frite ou grillée** forme des amines associées à plus de polypes, les précurseurs du cancer. Pas au cancer lui-même.",
             "Chiavarini 2017 · méta-analyse"),
            ("32", "fritures", "**L’huile de friture réutilisée** a abîmé la barrière intestinale, fait exploser *E. coli* et augmenté les tumeurs du côlon.",
             "Hu 2024 · Zhang 2019 · souris"),
            ("4/4", "essais", "**Manger moins d’AGE,** qui se forment en friture à haute température, a fait baisser les marqueurs inflammatoires dans tous les essais qui les ont mesurés.",
             "Detopoulou 2024 · revue d’essais"),
        ],
        "end": ("**Ce que les études ne démontrent pas :** que les fritures causent le cancer du côlon. Les tumeurs ont été vues chez la souris ; chez l’humain, il n’y a qu’un lien avec les polypes, et l’acrylamide n’est pas associé. **La clé :** que ça ne devienne pas une habitude, et ne pas réutiliser l’huile.",
                "Chiavarini 2017 · Galeone 2015"),
        "repo": "**L’histoire complète,** avec toutes les sources, dans le repo.",
    },
}
