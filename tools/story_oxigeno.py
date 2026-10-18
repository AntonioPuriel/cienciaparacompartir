"""Texto de las stories «oxígeno en el intestino» (ES/EN/FR).
Cada punto: (icono, texto con **negritas**, cita abreviada).
LAYOUT = 'pie': todo el texto sobre fondo crema y las dunas solo al pie."""

LAYOUT = "pie"

STORIES = {
    "es": {
        "eyebrow": "Ciencia para compartir",
        "title": "Oxígeno en tu intestino: ¿cuándo sí y cuándo no?",
        "sub": "Depende del momento y del lugar",
        "items": [
            ("👶", "**Al nacer,** tu intestino tiene oxígeno. Las primeras bacterias lo gastan y dejan sitio a las que no lo soportan, como *Bifidobacterium*.",
             "Neumann 2025 · cohorte de 30 bebés"),
            ("⬇️", "**Estómago e intestino delgado** tienen oxígeno. En el **colon** es casi indetectable.",
             "Friedman 2018 · ratón"),
            ("🧱", "**Pegado a la pared** del colon hay una franja fina con algo de oxígeno, con bacterias que lo toleran.",
             "Albenberg 2014 · humanos + ratón"),
            ("🚫", "**Dentro del colon adulto, el oxígeno es mala señal:** desplaza a las bacterias del butirato y gana *E. coli*.",
             "Byndloss 2017 · ratón · Lloyd-Price 2019 · humanos"),
            ("🔄", "**El giro:** en la colitis ulcerosa el **tejido** inflamado suele estar falto de oxígeno. Con cámara hiperbárica, 5 de 10 pacientes entraron en remisión, frente a 0 de 8.",
             "Dulai 2018 · ensayo, n=18"),
            ("🔍", "**Lo que no demuestran:** que respirar más oxígeno sirva a cualquiera. Los estudios con cámara son pocos y pequeños.",
             "McCurdy 2022 · metaanálisis, evidencia baja"),
            ("📂", "**Oxígeno en el tejido ≠ oxígeno dentro del intestino.** Más en el repo.", ""),
        ],
    },
    "en": {
        "eyebrow": "Science to share",
        "title": "Oxygen in your gut: when yes and when no?",
        "sub": "It depends on the moment and the place",
        "items": [
            ("👶", "**At birth,** your gut contains oxygen. The first bacteria use it up and make room for those that can’t stand it, like *Bifidobacterium*.",
             "Neumann 2025 · cohort of 30 babies"),
            ("⬇️", "The **stomach and small intestine** have oxygen. In the **colon** it’s almost undetectable.",
             "Friedman 2018 · mice"),
            ("🧱", "**Right against the colon wall** there’s a thin band with some oxygen, home to bacteria that tolerate it.",
             "Albenberg 2014 · humans + mice"),
            ("🚫", "**Inside the adult colon, oxygen is a bad sign:** it pushes out butyrate bacteria and *E. coli* wins.",
             "Byndloss 2017 · mice · Lloyd-Price 2019 · humans"),
            ("🔄", "**The twist:** in ulcerative colitis the inflamed **tissue** is often short of oxygen. With a hyperbaric chamber, 5 of 10 patients reached remission, versus 0 of 8.",
             "Dulai 2018 · trial, n=18"),
            ("🔍", "**What they don’t show:** that breathing more oxygen helps anyone. Chamber studies are few and small.",
             "McCurdy 2022 · meta-analysis, low evidence"),
            ("📂", "**Oxygen in the tissue ≠ oxygen inside the gut.** More in the repo.", ""),
        ],
    },
    "fr": {
        "eyebrow": "La science à partager",
        "title": "L’oxygène dans ton intestin : quand oui et quand non ?",
        "sub": "Ça dépend du moment et de l’endroit",
        "items": [
            ("👶", "**À la naissance,** ton intestin contient de l’oxygène. Les premières bactéries le consomment et font place à celles qui ne le supportent pas, comme *Bifidobacterium*.",
             "Neumann 2025 · cohorte de 30 bébés"),
            ("⬇️", "L’**estomac et l’intestin grêle** contiennent de l’oxygène. Dans le **côlon**, il est presque indétectable.",
             "Friedman 2018 · souris"),
            ("🧱", "**Contre la paroi du côlon,** une fine couche contient un peu d’oxygène, avec des bactéries qui le tolèrent.",
             "Albenberg 2014 · humains + souris"),
            ("🚫", "**Dans le côlon adulte, l’oxygène est mauvais signe :** il chasse les bactéries du butyrate et *E. coli* l’emporte.",
             "Byndloss 2017 · souris · Lloyd-Price 2019 · humains"),
            ("🔄", "**Le retournement :** dans la rectocolite hémorragique, le **tissu** enflammé manque souvent d’oxygène. En caisson hyperbare, 5 patients sur 10 sont entrés en rémission, contre 0 sur 8.",
             "Dulai 2018 · essai, n=18"),
            ("🔍", "**Ce que les études ne démontrent pas :** que respirer plus d’oxygène aide tout le monde. Les études en caisson sont rares et petites.",
             "McCurdy 2022 · méta-analyse, preuves faibles"),
            ("📂", "**Oxygène dans le tissu ≠ oxygène dans l’intestin.** Plus dans le repo.", ""),
        ],
    },
}
