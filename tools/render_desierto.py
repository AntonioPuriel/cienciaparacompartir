"""Story 1080x1920 con paisaje de saguaros (cielo azul, roca roja, cactus dorados)
y una cifra grande por punto. Ilustración original en SVG, inspirada en el desierto de Sonora.
Uso: python3 render_desierto.py <carpeta_destino> <modulo_story> [idiomas]
El módulo define DESIERTO = {lang: {eyebrow, title, sub, stops: [(num, unit, text, cite)], end: (text, cite), repo}}"""
import base64, html, importlib, pathlib, re, sys, asyncio
from playwright.async_api import async_playwright

FONTS = pathlib.Path(__file__).resolve().parent / 'fonts'
OUT = pathlib.Path(sys.argv[1])
D = importlib.import_module(sys.argv[2]).DESIERTO
LANGS = sys.argv[3].split(',') if len(sys.argv) > 3 else list(D)


def face(family, file, weight, style='normal'):
    b64 = base64.b64encode((FONTS / file).read_bytes()).decode()
    return f"@font-face{{font-family:'{family}';src:url(data:font/woff2;base64,{b64}) format('woff2');font-weight:{weight};font-style:{style}}}"


FACES = '\n'.join([
    face('Fraunces', 'fontsource-fraunces/files/fraunces-latin-600-normal.woff2', 600),
    face('Fraunces', 'fontsource-fraunces/files/fraunces-latin-400-italic.woff2', 400, 'italic'),
    face('DM Sans', 'fontsource-dm-sans/files/dm-sans-latin-400-normal.woff2', 400),
    face('DM Sans', 'fontsource-dm-sans/files/dm-sans-latin-700-normal.woff2', 700),
])


def md(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)


def saguaro(x, base, h, w, arms, flip=False):
    """Saguaro dorado: tronco + brazos en U, con costillas verticales."""
    g = 'url(#cact)'
    parts = [f'<rect x="{x - w/2}" y="{base - h}" width="{w}" height="{h + 40}" rx="{w/2}" fill="{g}"/>']
    for (ay, ah, side) in arms:
        s = -side if flip else side
        ax = x + s * (w * 1.15)
        aw = w * 0.72
        # codo horizontal + brazo vertical
        parts.append(f'<rect x="{min(x, ax) - aw/2}" y="{base - ay - aw/2}" width="{abs(ax - x) + aw}" height="{aw}" rx="{aw/2}" fill="{g}"/>')
        parts.append(f'<rect x="{ax - aw/2}" y="{base - ay - ah}" width="{aw}" height="{ah}" rx="{aw/2}" fill="{g}"/>')
    ribs = ''.join(f'<line x1="{x + d}" y1="{base - h + w*0.6}" x2="{x + d}" y2="{base + 40}" stroke="#000" stroke-opacity=".25" stroke-width="2"/>'
                   for d in (-w*0.28, 0, w*0.28))
    return '<g>' + ''.join(parts) + ribs + '</g>'


LANDSCAPE = f'''<svg id="bg" viewBox="0 0 1080 1920" preserveAspectRatio="none">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1A1438"/><stop offset=".38" stop-color="#3A1E52"/><stop offset=".56" stop-color="#7A2D5A"/><stop offset=".7" stop-color="#C84A45"/><stop offset=".79" stop-color="#F08A3E"/><stop offset=".84" stop-color="#FFC266"/>
  </linearGradient>
  <linearGradient id="rock" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#8E3326"/><stop offset=".55" stop-color="#6A2220"/><stop offset="1" stop-color="#3E1418"/>
  </linearGradient>
  <linearGradient id="cact" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#E9A24A"/><stop offset=".18" stop-color="#5A2A22"/><stop offset="1" stop-color="#22101A"/>
  </linearGradient>
</defs>
<rect width="1080" height="1920" fill="url(#sky)"/>
<radialGradient id="glow" cx="790" cy="1540" r="420" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFD27A" stop-opacity=".75"/><stop offset="1" stop-color="#FF8A3D" stop-opacity="0"/></radialGradient>
<circle cx="790" cy="1540" r="420" fill="url(#glow)"/>
<circle cx="790" cy="1560" r="125" fill="#FFD47E"/>
<path d="M-20 1920 L-20 1610 L90 1585 L150 1530 L210 1545 L260 1470 L330 1455 L360 1420 L520 1412 L560 1440 L600 1500 L680 1540 L760 1600 L860 1630 L980 1615 L1100 1640 L1100 1920 Z" fill="url(#rock)"/>
<path d="M360 1420 L520 1412 L540 1470 L500 1520 L430 1540 L380 1500 Z" fill="#E3763E" opacity=".28"/>
<path d="M600 1500 L680 1540 L760 1600 L700 1620 L640 1580 Z" fill="#5E1F10" opacity=".45"/>
<path d="M-20 1920 L-20 1770 C200 1745 420 1760 640 1775 S960 1760 1100 1770 L1100 1920 Z" fill="#3A1620"/>
<path d="M-20 1920 L-20 1835 C260 1820 520 1830 760 1840 S1000 1832 1100 1838 L1100 1920 Z" fill="#1E0C16"/>
{saguaro(78, 1880, 400, 50, [(230, 150, 1), (160, 110, -1)])}
{saguaro(1000, 1880, 440, 54, [(250, 170, -1), (190, 130, 1)])}
{saguaro(300, 1800, 170, 22, [(90, 70, 1)])}
{saguaro(820, 1810, 210, 26, [(110, 90, -1)])}
{saguaro(560, 1790, 120, 16, [])}
</svg>'''


def story(lang):
    d = D[lang]
    stops = ''.join(f'''<div class="stop"><div class="num"><span class="n">{html.escape(n)}</span><span class="u">{html.escape(u)}</span></div>
      <div><p class="tx">{md(t)}</p><p class="cite">{html.escape(c)}</p></div></div>''' for n, u, t, c in d['stops'])
    et, ec = d['end']
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>
{FACES}
*{{box-sizing:border-box;margin:0}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#1A1438}}
body{{position:relative;font-family:'DM Sans',sans-serif;color:#fff}}
#bg{{position:absolute;inset:0;width:1080px;height:1920px}}
.page{{position:relative;padding:84px 96px 0 96px}}
.eyebrow{{font-size:24px;font-weight:700;letter-spacing:.24em;text-transform:uppercase;color:#F3C45A}}
h1{{font-family:'Fraunces',serif;font-weight:600;font-size:var(--h1,84px);line-height:1.02;margin-top:22px;letter-spacing:-.01em;text-shadow:0 2px 18px rgba(20,8,40,.5)}}
.sub{{font-family:'Fraunces',serif;font-style:italic;font-size:42px;color:#FBD98A;margin-top:18px;line-height:1.1}}
.stops{{margin-top:var(--gap0,54px);display:flex;flex-direction:column;gap:var(--gap,34px)}}
.stop{{display:grid;grid-template-columns:230px 1fr;gap:26px;align-items:start}}
.num{{display:flex;flex-direction:column;align-items:flex-end;text-align:right;border-right:3px solid rgba(243,196,90,.7);padding-right:22px}}
.n{{font-family:'Fraunces',serif;font-weight:600;font-size:var(--n,88px);line-height:.95;color:#F3C45A;letter-spacing:-.02em}}
.u{{font-size:19px;font-weight:700;letter-spacing:.05em;line-height:1.25;text-transform:uppercase;color:#FBD98A;margin-top:8px;max-width:200px}}
.tx{{font-size:var(--tx,31px);line-height:1.3}}
.tx b{{font-weight:700;color:#FFF3D6}}
.cite{{font-size:20px;color:rgba(255,255,255,.72);margin-top:8px}}
.end{{margin-top:var(--gap0,46px);background:rgba(30,14,40,.62);border-left:5px solid #F3C45A;border-radius:6px 18px 18px 6px;padding:26px 30px}}
.end .tx b{{color:#F3C45A}}
.repo{{margin-top:24px;font-size:28px;font-weight:700;color:#FFF3D6;text-shadow:0 1px 10px rgba(40,10,30,.8)}}
</style></head><body>
{LANDSCAPE}
<div class="page" id="page">
<p class="eyebrow">{html.escape(d['eyebrow'])}</p>
<h1>{html.escape(d['title'])}</h1>
<p class="sub">{html.escape(d['sub'])}</p>
<div class="stops">{stops}</div>
<div class="end"><p class="tx">{md(et)}</p><p class="cite">{html.escape(ec)}</p></div>
<p class="repo">{md(d['repo'])}</p>
</div></body></html>'''


# Límite inferior del texto: deja libre la franja de roca para el sticker de enlace.
LIMIT = 1470


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        for lang in LANGS:
            await pg.set_content(story(lang))
            await pg.evaluate('document.fonts.ready')
            # Si no cabe, reduce tamaños poco a poco.
            for k in [1, .96, .92, .88, .85, .82]:
                await pg.evaluate(f'''(() => {{const s=document.documentElement.style;
                  s.setProperty('--h1','{84*k}px');s.setProperty('--n','{88*k}px');s.setProperty('--tx','{31*k}px');
                  s.setProperty('--gap','{34*k}px');s.setProperty('--gap0','{50*k}px');}})()''')
                bottom = await pg.evaluate('document.getElementById("page").getBoundingClientRect().bottom')
                if bottom <= LIMIT:
                    break
            print(lang, 'scale', k, 'bottom', round(bottom))
            await pg.screenshot(path=str(OUT / f'story-{lang}.png'))
        await b.close()

asyncio.run(main())
