"""Texto de las stories «fritos e inflamación» (ES/EN/FR), diseño «desierto» (render_desierto.py).
Cuatro cifras grandes, el recuadro de lo que no demuestran y el cierre hacia el repo.
La historia completa, con todos los datos y la regulación, va en la página del repo."""

N = " "

DESIERTO = {
    "es": {
        "eyebrow": "Ciencia para compartir",
        "title": "Fritos e inflamación: ¿qué pasa cuando abusas?",
        "sub": "La pesadez de un día no es inflamación; la costumbre, sí cuenta",
        "stops": [
            (f"+28{N}%", "riesgo cardiovascular", "**Comer fritos a menudo** se asocia con más infartos e insuficiencia cardíaca.",
             "Qin 2021 · metaanálisis de cohortes"),
            (f"+12{N}%", "ansiedad", f"**En 140{N}000 personas,** los fritos frecuentes se asociaron con más ansiedad, y un 7{N}% más de depresión.",
             "Wang 2023 · cohorte"),
            ("32", "frituras", "**El mismo aceite reutilizado 32 veces** bajó la diversidad intestinal y disparó *E. coli*.",
             "Hu 2024 · ratón"),
            ("4/4", "ensayos", "**Comer menos AGEs,** que se forman al freír a alta temperatura, bajó los marcadores inflamatorios en todos los ensayos que los midieron.",
             "Detopoulou 2024 · revisión de ensayos"),
        ],
        "end": ("**Lo que no demuestran:** que dos fritos te inflamen. La pesadez es digestión lenta, y el pico inflamatorio tras una comida grasa es pasajero. **La clave:** que no sea costumbre y no reutilizar el aceite.",
                "Feinle-Bisset 2013 · Br J Nutr 2020"),
        "repo": "**La historia completa,** con todas las fuentes, en el repo.",
    },
    "en": {
        "eyebrow": "Science to share",
        "title": "Fried food and inflammation: what if you overdo it?",
        "sub": "One heavy day isn’t inflammation; the habit is what counts",
        "stops": [
            ("+28%", "cardiovascular risk", "**Eating fried food often** is linked to more heart attacks and heart failure.",
             "Qin 2021 · meta-analysis of cohorts"),
            ("+12%", "anxiety", "**In 140,000 people,** frequent fried food was linked to more anxiety, and 7% more depression.",
             "Wang 2023 · cohort"),
            ("32", "fryings", "**The same oil reused 32 times** lowered gut diversity and sent *E. coli* soaring.",
             "Hu 2024 · mice"),
            ("4/4", "trials", "**Eating fewer AGEs,** which form when frying at high heat, lowered inflammatory markers in every trial that measured them.",
             "Detopoulou 2024 · review of trials"),
        ],
        "end": ("**What they don’t show:** that two fried meals inflame you. The heaviness is slow digestion, and the inflammatory spike after a fatty meal is short-lived. **The key:** don’t make it a habit, and don’t reuse the oil.",
                "Feinle-Bisset 2013 · Br J Nutr 2020"),
        "repo": "**The full story,** with every source, in the repo.",
    },
    "fr": {
        "eyebrow": "La science à partager",
        "title": "Fritures et inflammation : que se passe-t-il quand on abuse ?",
        "sub": "La lourdeur d’un jour n’est pas de l’inflammation ; c’est l’habitude qui compte",
        "stops": [
            (f"+28{N}%", "risque cardio-vasculaire", "**Manger souvent des fritures** est associé à plus d’infarctus et d’insuffisance cardiaque.",
             "Qin 2021 · méta-analyse de cohortes"),
            (f"+12{N}%", "anxiété", f"**Chez 140{N}000 personnes,** les fritures fréquentes étaient associées à plus d’anxiété, et à 7{N}% de dépression en plus.",
             "Wang 2023 · cohorte"),
            ("32", "fritures", "**La même huile réutilisée 32 fois** a réduit la diversité intestinale et fait exploser *E. coli*.",
             "Hu 2024 · souris"),
            ("4/4", "essais", "**Manger moins d’AGE,** qui se forment en friture à haute température, a fait baisser les marqueurs inflammatoires dans tous les essais qui les ont mesurés.",
             "Detopoulou 2024 · revue d’essais"),
        ],
        "end": ("**Ce que les études ne démontrent pas :** que deux fritures vous enflamment. La lourdeur, c’est une digestion lente, et le pic inflammatoire après un repas gras est passager. **La clé :** que ça ne devienne pas une habitude, et ne pas réutiliser l’huile.",
                "Feinle-Bisset 2013 · Br J Nutr 2020"),
        "repo": "**L’histoire complète,** avec toutes les sources, dans le repo.",
    },
}
