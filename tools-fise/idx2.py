import pickle
from fb import PROJ
DATA=pickle.load(open('data.pkl','rb'))
NAV='''<header class="topnav"><div class="tn-in"><a class="tn-logo" href="index.html"><span class="tn-mark">&#9651;</span>Casuta din copac</a><nav class="tn-links">
<a href="timeline.html" data-k="stadiu">Stadiu</a><a href="ghid-montaj.html" data-k="ghid">Ghid</a><a href="materiale.html" data-k="materiale">Materiale</a><a href="imbinari.html" data-k="imbinari">Imbinari</a><a href="modele-3d.html" data-k="3d">3D</a><a href="casuta-din-copac.html" data-k="dosar">Dosar</a>
</nav></div><div class="tn-crumb"><a href="index.html">Acasa</a><span>&rsaquo;</span><a href="ghid-montaj.html">Ghid</a><span>&rsaquo;</span><b>Fise montaj</b></div></header><script>(function(){var a=document.querySelector('.tn-links a[data-k="ghid"]');if(a)a.classList.add("on");})();</script>'''
cards=''
for s in DATA:
    crit='crit' if s['diff']=='CRITIC' else ''
    hero=s['steps'][0].get('svg') or s['steps'][1].get('svg')
    cards+=f'''<a class="fcard" href="{s['slug']}.html"><div class="thumb">{hero}</div><div class="b"><div class="num">{s['n']:02d}<span class="of">/11</span></div><h2>{s['title']}</h2><div class="row"><span class="t">~{s['time']}</span><span class="d {crit}">{s['diff']}</span></div></div></a>'''
html=f'''<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fise de montaj — Faza 1 · Casuta din copac</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>:root{{--ink:#161413;--soft:#5C574E;--faint:#9A9388;--line:#E7E3DB;--acc:#C2693A;--wash:#FAF8F4;--crit:#C2412B;}}
*{{box-sizing:border-box}}body{{margin:0;background:#fff;color:var(--ink);font-family:'Space Grotesk',system-ui,sans-serif;line-height:1.5}}
.wrap{{max-width:1040px;margin:0 auto;padding:0 22px}}a{{color:var(--acc);text-decoration:none}}
.hero{{padding:44px 0 22px}}.hero .kick{{font-family:'Space Mono',monospace;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--acc)}}
.hero h1{{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:clamp(32px,5.5vw,52px);margin:8px 0 12px;letter-spacing:-.02em}}
.hero p{{color:var(--soft);max-width:640px;margin:0;font-size:15px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;padding:18px 0 60px}}@media(max-width:860px){{.grid{{grid-template-columns:repeat(2,1fr)}}}}@media(max-width:560px){{.grid{{grid-template-columns:1fr}}}}
.fcard{{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:16px;overflow:hidden;background:#fff;color:var(--ink);box-shadow:0 1px 2px rgba(20,19,18,.04),0 8px 22px rgba(20,19,18,.05);transition:transform .16s,box-shadow .2s}}
.fcard:hover{{transform:translateY(-3px);box-shadow:0 16px 40px rgba(20,19,18,.11)}}
.thumb{{background:var(--wash);border-bottom:1px solid var(--line);padding:10px;height:172px;display:grid;place-items:center}}.thumb svg{{max-width:100%;max-height:152px}}
.b{{padding:14px 16px 18px}}.num{{font-family:'Space Mono',monospace;font-weight:700;font-size:13px;color:var(--acc)}}.num .of{{color:var(--faint)}}
.b h2{{font-family:'Fraunces',serif;font-weight:600;font-size:19px;margin:4px 0 10px}}.row{{display:flex;gap:8px}}
.row .t,.row .d{{font-family:'Space Mono',monospace;font-size:11px;border:1.5px solid var(--line);border-radius:999px;padding:3px 9px;color:var(--soft)}}.row .d.crit{{border-color:var(--crit);color:var(--crit)}}
footer{{padding:10px 0 70px;color:var(--faint);font-size:12.5px;text-align:center}}</style>
<link rel="stylesheet" href="assets/site.css"><script defer src="assets/site.js"></script></head><body>
{NAV}<div class="wrap"><header class="hero"><div class="kick">Faza 1 · platforma · stil IKEA</div><h1>Fise de montaj</h1>
<p>Cele 11 etape, fiecare ca o fisa de sine statatoare: piesele cu poza si cod, sculele, fiecare pas cu desenul lui (piesa noua intra cu sageata), bule de zoom la imbinari si verificarea de la final.</p></header>
<div class="grid">{cards}</div><footer class="mono">Casuta din copac · fise montaj Faza 1 · desene izometrice pas cu pas</footer></div></body></html>'''
open(f'{PROJ}/fise.html','w',encoding='utf-8').write(html); print('index ok')
