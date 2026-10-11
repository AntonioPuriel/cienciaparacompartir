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
