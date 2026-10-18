"""Renderiza las stories (1080x1920) y el preview (1600x900) con Chromium headless.
Uso: python3 render_stories.py <carpeta_destino>"""
import html, re, sys, asyncio, pathlib
from playwright.async_api import async_playwright
import importlib
_mod = importlib.import_module(sys.argv[2] if len(sys.argv) > 2 else "story_agua")
STORIES = _mod.STORIES
# LAYOUT = 'pie': todo el texto sobre el cielo y las dunas solo al pie (como dieta-cerebro).
# LAYOUT = 'franjas': texto repartido sobre las dunas (serie disruptores).
LAYOUT = getattr(_mod, 'LAYOUT', 'franjas')

FONTS = pathlib.Path(__file__).resolve().parent / 'fonts'  # ver tools/README.md
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
OUT = pathlib.Path(sys.argv[1])

# Bandas: índices de puntos que van en cada franja (cielo, ocre, terracota, oscuro)
BANDS = [(0, 3), (3, 5), (5, 8), (8, 9)]

import base64
def font_face(family, file, weight, style='normal'):
    b64 = base64.b64encode((FONTS / file).read_bytes()).decode()
    return f"@font-face{{font-family:'{family}';src:url(data:font/woff2;base64,{b64}) format('woff2');font-weight:{weight};font-style:{style}}}"

FACES = '\n'.join([
    font_face('Fraunces', 'fontsource-fraunces/files/fraunces-latin-600-normal.woff2', 600),
    font_face('Fraunces', 'fontsource-fraunces/files/fraunces-latin-400-italic.woff2', 400, 'italic'),
    font_face('DM Sans', 'fontsource-dm-sans/files/dm-sans-latin-400-normal.woff2', 400),
    font_face('DM Sans', 'fontsource-dm-sans/files/dm-sans-latin-500-normal.woff2', 500),
    font_face('DM Sans', 'fontsource-dm-sans/files/dm-sans-latin-700-normal.woff2', 700),
])

CACTUS = '<svg viewBox="0 0 60 100"><g fill="none" stroke="#5E7048" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"><path d="M30 100 V10"/><path d="M30 58 H12 V34"/><path d="M30 46 H47 V18"/></g></svg>'

def md(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)  # *cursiva* para nombres de especie

def story_html(lang, scale):
    d = STORIES[lang]
    items = []
    for i, (icon, text, cite) in enumerate(d['items']):
        band = 0 if LAYOUT == 'pie' else next(b for b, (a, z) in enumerate(BANDS) if a <= i < z)
        cls = 'item sky' if band == 0 else 'item dune'
        if LAYOUT != 'pie' and i == BANDS[1][0]:
            cls += ' first-dune'
        cite_html = f'<p class="cite">{html.escape(cite)}</p>' if cite else ''
        items.append(f'<div class="{cls}" data-band="{band}"><span class="ic">{icon}</span><div><p class="tx">{md(text)}</p>{cite_html}</div></div>')
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>
{FACES}
*{{box-sizing:border-box;margin:0}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#F1E9DA}}
body{{position:relative;font-family:'DM Sans',sans-serif;color:#3B2618}}
#bg{{position:absolute;inset:0;width:1080px;height:1920px}}
.page{{position:relative;padding:86px 72px 0 72px}}
.eyebrow{{font-size:{25*scale:.1f}px;font-weight:700;letter-spacing:.24em;text-transform:uppercase;color:#B4532A}}
h1{{font-family:'Fraunces',serif;font-weight:600;font-size:{86*scale:.1f}px;line-height:1.02;margin-top:24px;letter-spacing:-.01em}}
.sub{{font-family:'Fraunces',serif;font-style:italic;font-size:{44*scale:.1f}px;color:#B4532A;margin-top:22px;line-height:1.1}}
.items{{margin-top:{52*scale:.0f}px;display:flex;flex-direction:column;gap:{30*scale:.0f}px}}
.item{{display:grid;grid-template-columns:68px 1fr;gap:24px;align-items:start}}
.ic{{width:68px;height:68px;border-radius:50%;display:grid;place-items:center;font-size:{33*scale:.0f}px;font-family:'Noto Color Emoji';background:#E5D6BC}}
.dune .ic{{background:rgba(255,255,255,.2)}}
.tx{{font-size:{31*scale:.1f}px;line-height:1.32}}
.tx b{{font-weight:700}}
.cite{{font-size:{20.5*scale:.1f}px;color:#7A5A44;margin-top:7px;line-height:1.3}}
.dune .tx{{color:#FFFFFF}}
.dune .cite{{color:rgba(255,255,255,.82)}}
.first-dune{{margin-top:{110*scale:.0f}px}}
.deco{{position:absolute}}
</style></head><body>
<svg id="bg" viewBox="0 0 1080 1920"></svg>
<div class="page">
<p class="eyebrow">{html.escape(d['eyebrow'])}</p>
<h1>{html.escape(d['title'])}</h1>
<p class="sub">{html.escape(d['sub'])}</p>
<div class="items">{''.join(items)}</div>
</div>
<script>
const LAYOUT='{LAYOUT}';
document.fonts.ready.then(()=>{{
function y(el){{return el.getBoundingClientRect().top}}
function yb(el){{return el.getBoundingClientRect().bottom}}
const items=[...document.querySelectorAll('.item')];
if (LAYOUT==='pie'){{
  const last=yb(items[items.length-1]);
  const hz=Math.min(Math.max(last+70,1730),1790);
  const W=1080;
  function wave(top,amp,ph){{return `M0 ${{top+amp*Math.sin(ph)}} C 270 ${{top-amp}} 540 ${{top+amp}} 810 ${{top-amp*0.4}} S 1080 ${{top+amp*0.6}} 1080 ${{top+amp*0.2}} L1080 1920 L0 1920 Z`}}
  const svg=document.getElementById('bg');
  svg.innerHTML=`<circle cx="860" cy="${{hz-6}}" r="70" fill="#E9A24A"/>`+
  `<path d="${{wave(hz-20,14,0.3)}}" fill="#E3CBA0"/>`+
  `<path d="${{wave(hz+38,12,1.2)}}" fill="#B0702E"/>`+
  `<path d="${{wave(hz+82,10,2.0)}}" fill="#9A4730"/>`+
  `<path d="${{wave(hz+124,8,0.7)}}" fill="#6E3022"/>`;
  function cactus(x,h,w){{const d=document.createElement('div');d.className='deco';d.innerHTML=`{CACTUS}`;d.style.cssText=`left:${{x}}px;top:${{hz-20-h+14}}px;width:${{w}}px;height:${{h}}px`;document.body.appendChild(d);d.firstChild.style.cssText='width:100%;height:100%'}}
  cactus(112,86,78);cactus(310,30,24);cactus(972,64,52);
  window.__overflow = last > 1700;
  window.__done = true;
  return;
}}
const firstOf=b=>items.find(i=>+i.dataset.band===b);
const lastOf=b=>[...items].reverse().find(i=>+i.dataset.band===b);
// horizon: between last sky item and first dune item
const h0=yb(lastOf(0)), h1=y(firstOf(1));
const hz=h1-34;
const b2=(yb(lastOf(1))+y(firstOf(2)))/2, b3=(yb(lastOf(2))+y(firstOf(3)))/2;
const W=1080;
function wave(top,amp,ph){{return `M0 ${{top+amp*Math.sin(ph)}} C 270 ${{top-amp}} 540 ${{top+amp}} 810 ${{top-amp*0.4}} S 1080 ${{top+amp*0.6}} 1080 ${{top+amp*0.2}} L1080 1920 L0 1920 Z`}}
const svg=document.getElementById('bg');
svg.innerHTML=`<circle cx="860" cy="${{hz-12}}" r="74" fill="#E9A24A"/>`+
`<path d="${{wave(hz-26,14,0.3)}}" fill="#E3CBA0"/>`+
`<path d="${{wave(hz,12,1.2)}}" fill="#B0702E"/>`+
`<path d="${{wave(b2,9,2.0)}}" fill="#9A4730"/>`+
`<path d="${{wave(b3,8,0.7)}}" fill="#6E3022"/>`;
// circle hidden below ridge: draw ridge after sun (done). Cactus:
function cactus(x,h,w){{const d=document.createElement('div');d.className='deco';d.innerHTML=`{CACTUS}`;d.style.cssText=`left:${{x}}px;top:${{hz-26-h+14}}px;width:${{w}}px;height:${{h}}px`;document.body.appendChild(d);d.firstChild.style.cssText='width:100%;height:100%'}}
cactus(112,86,78);cactus(310,30,24);cactus(972,64,52);
window.__overflow = yb(items[items.length-1]) > 1860;
window.__gap = h1-h0;
window.__done = true;
}});
</script></body></html>'''

async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.on('console', lambda m: print('console:', m.text))
        pg.on('pageerror', lambda e: print('pageerror:', e))
        for lang in STORIES:
            scale = 1.0
            while True:
                f = OUT.parent / f'_tmp_{lang}.html'
                f.write_text(story_html(lang, scale))
                await pg.goto(f'file://{f.resolve()}')
                await pg.evaluate('document.fonts.ready')
                await pg.wait_for_function('window.__done === true')
                await pg.wait_for_timeout(300)
                f.unlink()
                if not await pg.evaluate('window.__overflow') or scale < 0.8:
                    break
                scale -= 0.02
            print(lang, 'scale', round(scale, 2))
            await pg.screenshot(path=str(OUT / f'story-{lang}.png'))
        # preview
        imgs = ''.join(f'<img src="file://{OUT.resolve()}/story-{l}.png">' for l in STORIES)
        prev = f'''<html><body style="margin:0;width:1600px;height:900px;background:linear-gradient(#E9E0CF 0 690px,#E3CBA0 690px 820px,#B4532F 820px)">
<div style="display:flex;gap:71px;padding:60px 71px">{imgs}</div>
<style>img{{width:438px;height:779px;border-radius:28px;display:block}}</style></body></html>'''
        await pg.set_viewport_size({'width': 1600, 'height': 900})
        await pg.set_content(prev, wait_until='load')
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=str(OUT / 'preview.png'))
        await b.close()

asyncio.run(main())
