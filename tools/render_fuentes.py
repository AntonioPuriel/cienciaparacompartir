"""Imagen «Las fuentes» de un tema (fuentes-es.png, fuentes-en.png, fuentes-fr.png): 1080 px de ancho, alto según haga falta.
Lee la página de fuentes ya generada (<carpeta>/index.html): título, fecha de revisión, referencias por sección
con su tipo de evidencia y DOI, y la leyenda de los tipos usados.
Uso (desde tools/): python render_fuentes.py ../ciencia-salud/semillas [más carpetas...]
         o bien:    python render_fuentes.py --todos"""
import asyncio, base64, html, pathlib, re, sys
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

TOOLS = pathlib.Path(__file__).resolve().parent
ROOT = TOOLS.parent
FONTS = TOOLS / 'fonts'
LANGS = ['es', 'en', 'fr']
BRAND = {'es': 'Ciencia para compartir', 'en': 'Science to share', 'fr': 'La science à partager'}
HEAD = {'es': ('Las fuentes', 'Estudio', 'Evidencia', 'Qué significa cada tipo'),
        'en': ('The sources', 'Study', 'Evidence', 'What each type means'),
        'fr': ('Les sources', 'Étude', 'Preuve', 'Ce que veut dire chaque type')}
AND = {'es': 'y', 'en': 'and', 'fr': 'et'}
COLON = {'es': ': ', 'en': ': ', 'fr': ' : '}
SITE = 'antoniopuriel.github.io/cienciaparacompartir'


def face(family, file, weight, style='normal'):
    b64 = base64.b64encode((FONTS / file).read_bytes()).decode()
    return f"@font-face{{font-family:'{family}';src:url(data:font/woff2;base64,{b64}) format('woff2');font-weight:{weight};font-style:{style}}}"


FACES = '\n'.join([
    face('Fraunces', 'fontsource-fraunces/files/fraunces-latin-600-normal.woff2', 600),
    face('Fraunces', 'fontsource-fraunces/files/fraunces-latin-400-italic.woff2', 400, 'italic'),
    face('DM Sans', 'fontsource-dm-sans/files/dm-sans-latin-400-normal.woff2', 400),
    face('DM Sans', 'fontsource-dm-sans/files/dm-sans-latin-700-normal.woff2', 700),
])


def only(el, lang):
    """Copia del elemento con solo el idioma pedido."""
    el = BeautifulSoup(str(el), 'html.parser')
    for other in LANGS:
        if other != lang:
            for s in el.select(f'.{other}'):
                s.decompose()
    return el


def text(el, lang):
    return only(el, lang).get_text(' ', strip=True).replace(' ,', ',') if el else ''


def short_cite(cite, lang):
    """«Musazadeh V, Morovatshoar R, … · Revista · 2024; 174: 106868» -> («Musazadeh et al. 2024», «Revista»).
    Agencias, prensa y webs: el primer campo tal cual y el año."""
    parts = [p.strip() for p in cite.split('·')]
    m = re.search(r'\b(19|20)\d{2}\b', cite)
    year = m.group(0) if m else ''
    journal = parts[1] if len(parts) >= 3 else ''
    first = re.sub(r'\s*\([^)]*\)\s*$', '', parts[0])  # quita «(ensayo X)», «(Google)», «(42 autores)»
    names = [n.strip() for n in first.split(',') if n.strip() and not n.strip().startswith('et al')]
    etal = 'et al' in first
    initials = re.compile(r'^(.*[a-zà-ÿ].*?)\s+[A-Z][A-Z\-]{0,4}$')
    if names and '/' not in first and initials.match(names[0]):
        sur = [initials.match(n).group(1) if initials.match(n) else n for n in names]
        if len(sur) == 1 and not etal:
            who = sur[0]
        elif len(sur) == 2 and not etal:
            who = f'{sur[0]} {AND[lang]} {sur[1]}'
        else:
            who = f'{sur[0]} et al.'
    else:
        who = first.split(',')[0].strip() if ',' in first else parts[0]
        if re.search(r'\b(19|20)\d{2}\b', journal):
            journal = ''
    if year and year not in who:
        who += f' {year}'
    return who, journal


def build(folder, lang):
    soup = BeautifulSoup((folder / 'index.html').read_text(encoding='utf-8'), 'html.parser')
    main = soup.find('main')
    # título del tema: el h1 sin «: las fuentes» (se pone aparte)
    h1 = text(main.find('h1'), lang)
    title = re.sub(r'[\s:]*\b(las fuentes|the sources|les sources)\s*$', '', h1, flags=re.I).strip()
    reviewed = text(main.find('p', class_='reviewed'), lang)
    rows, used = [], {}
    for sec in main.find_all('section', recursive=False):
        arts = sec.find_all('article', class_='ref')
        if not arts:
            continue
        rows.append(f'<tr class="sec"><td colspan="3">{html.escape(text(sec.find("h2"), lang))}</td></tr>')
        for a in arts:
            who, journal = short_cite(a.find('p', class_='cite').get_text(' ', strip=True), lang)
            meta = a.find('div', class_='meta')
            chips = ''
            for c in meta.find_all('span', class_='chip'):
                cls = c['class'][1]
                lab = text(c, lang)
                used.setdefault(lab, cls)
                chips += f'<span class="chip {cls}">{html.escape(lab)}</span>'
            link = meta.find('a')
            href = link['href'] if link else ''
            m = re.match(r'https?://(?:dx\.)?doi\.org/(.+)', href)
            where = f'doi.org/{m.group(1)}' if m else re.sub(r'^https?://(www\.)?', '', href).split('/')[0]
            rows.append(f'<tr><td><b>{html.escape(who)}</b><span class="j">{html.escape(journal)}</span></td>'
                        f'<td class="chips">{chips}</td><td class="doi">{html.escape(where)}</td></tr>')
    legend = ''
    for p in main.select('.legend > p'):
        c = p.find('span', class_='chip')
        lab = text(c, lang)
        if lab in used:
            legend += f'<p><span class="chip {c["class"][1]}">{html.escape(lab)}</span><span>{html.escape(text(c.find_next_sibling("span"), lang))}</span></p>'
    url = f'{SITE}/{folder.parent.name}/{folder.name}/' + ('' if lang == 'es' else f'#{lang}')
    h_src, h_study, h_ev, h_leg = HEAD[lang]
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>
{FACES}
*{{box-sizing:border-box;margin:0}}
html,body{{width:1080px;background:#F4EAD9}}
body{{font-family:'DM Sans',sans-serif;color:#3B2618;padding:72px 72px 0}}
.eyebrow{{font-size:22px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:#5E6B4C}}
h1{{font-family:'Fraunces',serif;font-weight:600;font-size:60px;line-height:1.05;margin-top:18px;letter-spacing:-.01em}}
h1 em{{font-style:italic;font-weight:400;color:#A84E28}}
.rev{{margin-top:16px;font-size:20px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#5E6B4C}}
table{{width:100%;border-collapse:collapse;margin-top:36px}}
th{{text-align:left;font-size:17px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#6E4A31;padding:0 12px 10px 0;border-bottom:2px solid #CF9E62}}
td{{vertical-align:top;padding:16px 12px 16px 0;border-bottom:1px solid #E3D2B4;font-size:24px;line-height:1.25}}
tr.sec td{{font-family:'Fraunces',serif;font-weight:600;font-size:28px;color:#A84E28;padding-top:30px;border-bottom:1.5px solid #CF9E62}}
td b{{display:block}}
.j{{display:block;font-size:19px;color:#6E4A31;margin-top:4px}}
.chips{{width:250px}}
.chip{{display:inline-block;font-size:15px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;padding:3px 10px;border-radius:999px;border:2px solid currentColor;margin:0 6px 6px 0;white-space:nowrap}}
.chip.rct{{color:#A84E28}}.chip.obs{{color:#5E6B4C}}.chip.db{{color:#6E4A31}}.chip.meta{{color:#3B2618}}
.chip.rev{{color:#6E4A31;border-style:dashed}}.chip.lab{{color:#6E4A31;border-style:dotted}}
td.doi{{width:330px;font-size:18px;color:#A84E28;overflow-wrap:anywhere}}
.legend{{margin-top:40px;background:#EBDCC2;border-radius:20px;padding:26px 28px;display:flex;flex-direction:column;gap:14px}}
.legend h2{{font-family:'Fraunces',serif;font-weight:600;font-size:28px}}
.legend p{{display:flex;gap:14px;align-items:baseline;font-size:21px;line-height:1.3}}
.legend .chip{{flex:none;margin:0}}
.foot{{margin-top:34px;padding:22px 0 60px;border-top:2px solid #CF9E62;font-size:20px;color:#6E4A31}}
.foot b{{color:#3B2618}}
</style></head><body>
<p class="eyebrow">{BRAND[lang]}</p>
<h1>{html.escape(title)}{'<br>' if title[-1:] in '?!' else COLON[lang]}<em>{h_src if title[-1:] in '?!' else h_src.lower()}</em></h1>
<p class="rev">{html.escape(reviewed)}</p>
<table><thead><tr><th>{h_study}</th><th>{h_ev}</th><th>DOI</th></tr></thead><tbody>
{''.join(rows)}
</tbody></table>
<div class="legend"><h2>{h_leg}</h2>{legend}</div>
<p class="foot"><b>{SITE}</b><br>{html.escape(url.split(SITE)[1])}</p>
</body></html>'''


async def main(folders):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        for folder in folders:
            for lang in LANGS:
                await pg.set_content(build(folder, lang))
                await pg.evaluate('document.fonts.ready')
                await pg.screenshot(path=str(folder / f'fuentes-{lang}.png'), full_page=True)
                h = await pg.evaluate('document.documentElement.scrollHeight')
                print(f'{folder.parent.name}/{folder.name} {lang}: 1080×{h}')
        await b.close()


if __name__ == '__main__':
    args = sys.argv[1:]
    if args == ['--todos']:
        folders = sorted(p.parent for p in ROOT.glob('ciencia-*/*/index.html'))
    else:
        folders = [pathlib.Path(a).resolve() for a in args]
    asyncio.run(main(folders))
