# Herramientas para generar stories y páginas

Scripts con los que se generaron los temas de la serie «disruptores endocrinos» (agua y PFAS). Los temas anteriores se hicieron a mano con la misma plantilla.

## Requisitos

- Python 3 con `playwright` y `Pillow`, y un Chromium. Ajusta `CHROME` en `render_stories.py` a tu ruta.
- Las fuentes Fraunces y DM Sans van en `tools/fonts/` (no se versionan). Se descargan de npm:

```bash
cd tools && mkdir -p fonts && cd fonts
npm pack @fontsource/fraunces @fontsource/dm-sans
for t in *.tgz; do tar xzf "$t" && mv package "${t%%-5*}"; done
```

## Uso (desde `tools/`)

```bash
# 1. Stories 1080×1920 (ES/EN/FR) + preview.png 1600×900
python3 render_stories.py ../ciencia-tecnologia/pfas-destruccion story_pfas

# 2. Página de fuentes (index.html)
python3 build_pfas_page.py ../ciencia-tecnologia/pfas-destruccion

# 3. Bloque «Serie» (desde la raíz del repo; es idempotente)
cd .. && python3 tools/add_serie.py
```

- `story_<tema>.py`: el texto de la story. Cada punto es (icono, texto con `**negritas**`, cita abreviada). Lleva 9 puntos repartidos en franjas `BANDS` = 3 sobre el cielo y 2 + 3 + 1 sobre las dunas, con el texto en blanco.
- `render_stories.py`: si el texto no cabe, reduce la escala sola. Las dunas se colocan después de que carguen las fuentes.
- `pagekit.py`: funciones comunes `t(es, en, fr)`, `section()`, `ref()` y el horizonte del encabezado.
- `build_<tema>_page.py`: referencias, notas de «lo que no demuestra» y la tabla de regulación.
- `add_serie.py`: inserta o actualiza el bloque que enlaza los temas de la serie. Vuelve a ejecutarlo después de regenerar una página.

## Serie «intestino» (salud)

```bash
# desde tools/
python3 render_stories.py ../ciencia-salud/oxigeno-intestino story_oxigeno
python3 render_stories.py ../ciencia-salud/dieta-inflamacion story_dieta_inflamacion
python3 build_oxigeno_page.py ../ciencia-salud/oxigeno-intestino
python3 build_dieta_page.py ../ciencia-salud/dieta-inflamacion
# desde la raíz del repo
python3 tools/add_serie_intestino.py
```

- `healthkit.py`: etiquetas de evidencia de salud (Síntesis, Guía, Ensayo, Observacional, Ratón, Revisión, «Anterior a 2020») y la plantilla de página.
- En los textos de las stories, `*cursiva*` sirve para los nombres de especie.

## Dieta ancestral (salud) · diseño «desierto al atardecer»

```bash
# desde tools/
python3 render_desierto.py ../ciencia-salud/dieta-ancestral story_dieta_ancestral   # stories ES/EN/FR + preview
python3 build_dieta_ancestral_page.py ../ciencia-salud/dieta-ancestral
```

- `render_desierto.py`: diseño propio de este tema (cielo al atardecer, roca roja y saguaros a contraluz) con una cifra grande por punto. Lee `DESIERTO` del módulo: `stops` = (cifra, unidad, texto, cita), más `end` (lo que no demuestran) y `repo`. Usa el Chromium de Playwright, sin ruta fija.
- Si el texto no cabe por encima de la roca (`LIMIT`), reduce la escala sola.

## Fritos e inflamación (salud) · diseño «desierto al atardecer»

```bash
# desde tools/
python3 render_desierto.py ../ciencia-salud/fritos-inflamacion story_fritos
python3 build_fritos_page.py ../ciencia-salud/fritos-inflamacion
cd .. && python3 tools/add_serie_intestino.py   # después de regenerar la página
```

- La página lleva los bloques «Serie: intestino» (cuarto tema) y «Serie: colon»; el tema de cáncer de colon en jóvenes aparece como «Próximamente» hasta que se publique.
- `healthkit.py` incluye la etiqueta «Laboratorio» (análisis de alimentos) además de «Ratón».

## README del repo

Cada categoría va en un bloque `<details>` (Ciencia y salud abierta por defecto) con una tabla `Fecha | Tema | Fuentes`: título solo en español y enlaces cortos `[ES](…) · [EN](…#en) · [FR](…#fr)`. Al añadir un tema, la fila nueva va arriba de su categoría y hay que actualizar el número de temas del `<summary>`.
