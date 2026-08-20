#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

F = json.load(open('figs_ikea.json'))

import re

def fit(svg, h, w):
    """dimensiuni explicite in px, calculate din viewBox (WeasyPrint nu deduce raportul)."""
    m = re.search(r'viewBox="(-?[\d.]+) (-?[\d.]+) ([\d.]+) ([\d.]+)"', svg)
    vw, vh = float(m.group(3)), float(m.group(4))
    k = min(h / vh, w / vw)
    return re.sub(r'style="width:100%;height:auto;display:block"',
                  f'style="width:{vw*k:.0f}px;height:{vh*k:.0f}px;display:block;margin:0 auto"',
                  svg, count=1)



CSS = """
:root{--ink:#1c1b18;--muted:#6b675e;--paper:#faf9f6;--line:#e2ddd3;--acc:#14532d;--acc2:#8a3016;
--mono:ui-monospace,"SF Mono",Menlo,monospace;--sans:"Avenir Next","Helvetica Neue",Helvetica,"Segoe UI",Arial,sans-serif;--serif:Georgia,serif}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:15px/1.55 var(--sans)}
.page{max-width:960px;margin:0 auto;padding:48px 40px 80px}
header.doc{border-bottom:3px solid var(--ink);padding-bottom:18px}
.kicker{font:600 11px/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--acc)}
h1{font:700 34px/1.08 var(--sans);margin:10px 0 8px;letter-spacing:-.015em}
.sub{font:italic 15.5px/1.55 var(--serif);color:var(--muted);max-width:62ch}
.meta{display:flex;gap:18px;flex-wrap:wrap;margin-top:14px;font:12px var(--mono);color:var(--muted)}
h2{font:700 13px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--muted);
   margin:44px 0 14px;padding-top:14px;border-top:1px solid var(--line)}
.note{border-left:3px solid var(--acc2);background:#fbf5ef;padding:12px 16px;margin:22px 0;font-size:13.5px;max-width:70ch}
.note b{color:var(--acc2)}

.where{display:flex;gap:26px;align-items:center;margin:6px 0 0}
.where .p{width:160px;flex:none}
.where p{margin:0;font-size:13.5px;color:var(--muted);max-width:52ch}

.parts{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:6px}
.part{border:1px solid var(--line);border-radius:5px;background:#fff;padding:12px 12px 10px;text-align:center}
.part .ic{height:80px;display:flex;align-items:center;justify-content:center}
.part .q{font:700 20px var(--mono);color:var(--acc2);margin-top:8px}
.part .n{font-size:11.5px;line-height:1.35;color:var(--muted);margin-top:3px}

.steps{display:grid;grid-template-columns:1fr 1fr;gap:20px 24px}
.step{border:1px solid var(--line);border-radius:6px;background:#fff;padding:13px 16px 15px;break-inside:avoid;page-break-inside:avoid}
.step .hd{display:flex;align-items:baseline;gap:11px;border-bottom:1px solid var(--line);padding-bottom:7px;margin-bottom:4px}
.step .num{font:700 27px/1 var(--mono);color:var(--acc2)}
.step .ti{font:600 14.5px/1.25 var(--sans)}
.step .fig{margin:3px 0 8px;text-align:center}
.step p{margin:0;font-size:12.5px;line-height:1.48;color:var(--muted)}

.hero{border:1px solid var(--line);border-radius:6px;background:#fff;padding:20px 24px 22px;break-inside:avoid;page-break-inside:avoid}
.hero .grid{display:flex;gap:30px;align-items:center}
.hero .fig{flex:0 0 46%}
.hero .txt{flex:1 1 48%}
.hero h3{font:700 19px/1.25 var(--sans);margin:0 0 10px}
.hero p{margin:0 0 10px;font-size:13.5px;line-height:1.55}
.chain{font:12.5px/1.7 var(--mono);color:var(--acc2);background:#fbf5ef;border-radius:4px;padding:10px 12px;margin-top:4px}

.bad{border:1px solid #e5cdbe;border-radius:6px;background:#fdf6f1;padding:18px 22px;break-inside:avoid;page-break-inside:avoid}
.bad .grid{display:flex;gap:28px;align-items:center}
.bad .fig{flex:0 0 34%}
.bad h3{font:700 17px/1.2 var(--sans);margin:0 0 8px;color:var(--acc2)}
.bad p{margin:0;font-size:13.5px;line-height:1.55}

footer.doc{margin-top:52px;border-top:2px solid var(--ink);padding-top:14px;font-size:12.5px;color:var(--muted)}
svg{display:block}

@media print{
 body{background:#fff}
 .page{max-width:none;padding:0}
 h2{page-break-after:avoid;break-after:avoid}
 .steps{gap:14px 18px}
 h2{margin-top:30px}
 @page{size:A4;margin:13mm 12mm}
}
@media(max-width:760px){.steps{grid-template-columns:1fr}.parts{grid-template-columns:repeat(2,1fr)}
 .hero .grid,.bad .grid,.where{flex-direction:column;align-items:flex-start}}
"""

STEPS = [
    ('1', 'Asa e acum',
     'acum',
     'Intre stalp si marginea podelei e un gol de aproximativ 100 mm. Sub el nu e nimic — nici grinda, nici sprijin. Se vede pamantul.'),
    ('2', 'Doua vincluri pe grinda',
     'coltare',
     'Se prind cu suruburi scurte in grinda groasa de la marginea podelei — aia care deja tine toata puntea. Latura scurta iese in gol, orizontala, ca o polita de raft.'),
    ('3', 'Blocajul se lasa pe vincluri',
     'blocaj',
     'Asta e raspunsul la intrebare: blocajul nu pluteste si nu sta pe scandura de dedesubt — se aseaza pe cele doua polite de metal. Ca o polita de biblioteca pe cele doua console ale ei.'),
    ('4', 'Suruburi oblice, de sus',
     'suruburi',
     'Trei suruburi 8×140 oblic in grinda groasa, doua in stalp. Se dau de sus, stand pe punte — nu trebuie sa cobori dedesubt. Dupa astea blocajul nu se mai misca deloc.'),
    ('5', 'Scandura de calcat',
     'scandura',
     'Ultima piesa, la nivel cu restul podelei. E doar suprafata pe care calci — nu duce nicio greutate. Daca o scoti maine, blocajul ramane exact unde e.'),
    ('6', 'Gata',
     'gata',
     'Totul la nivel cu podeaua, vinclurile raman ascunse dedesubt. Calca pe el inainte sa treci mai departe: daca nu se misca si nu suna a gol, e bun.'),
]

PARTS = [
    ('ic_coltar',   '2',  'Vinclu 90×65<br>(deja in lista Leroy)'),
    ('ic_blocaj',   '1',  'Blocaj de lemn<br>taiat pe loc'),
    ('ic_surub',    '8',  'Suruburi scurte 5×40<br>pentru vincluri'),
    ('ic_surub',    '5',  'Suruburi 8×140<br>dulgherie'),
    ('ic_scandura', '1',  'Scandura de calcat<br>deasupra'),
]


def build():
    parts = ''.join(
        f'<div class="part"><div class="ic">{F[ic]}</div>'
        f'<div class="q">×{q}</div><div class="n">{n}</div></div>'
        for ic, q, n in PARTS)

    steps = ''.join(
        f'<div class="step"><div class="hd"><span class="num">{n}</span>'
        f'<span class="ti">{t}</span></div>'
        f'<div class="fig">{fit(F[k], 162, 320)}</div><p>{p}</p></div>'
        for n, t, k, p in STEPS)

    return f"""<!DOCTYPE html><html lang="ro"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pe ce sta scandura noua — golul de la coltul din spate</title>
<style>{CSS}</style></head><body><div class="page">

<header class="doc">
<div class="kicker">Casuta din copac · un singur subiect</div>
<h1>Pe ce sta scandura noua</h1>
<p class="sub">Golul de la coltul din spate, montat pas cu pas. Desene in perspectiva, ca la instructiunile de mobila: fiecare pas o imagine, fara text lung. Se citeste in doua minute, se face in doua ore.</p>
<div class="meta"><span>20 august 2026</span><span>cote in mm</span><span>inlocuieste Detaliul 7 din SCHEME-CASA</span></div>
</header>

<div class="note"><b>Am schimbat ceva fata de Detaliul 7.</b> Acolo blocajul se sprijinea pe un singur vinclu la stalp plus suruburi lungi in grinda. Cand am verificat lungimile, suruburile nu ajungeau destul de adanc in grinda — golul e mai lat decat surubul. Varianta de aici: <b>doua vincluri montate ca doua polite pe grinda groasa</b>. Mai simplu de facut, mai solid, si foloseste acelasi vinclu 90×65 care e deja pe lista de la Leroy. Restul planului nu se schimba.</div>

<h2>Unde</h2>
<div class="where">
  <div class="p">{fit(F['plan'], 150, 150)}</div>
  <p>Golul e in forma de L, in jurul stalpului: latura <b>A</b> si latura <b>B</b>. Desenele de mai jos arata o singura latura. Se face identic pe cealalta, si apoi identic la celalalt colt din spate — deci de <b>patru ori</b> in total. Cantitatile din lista de piese sunt pentru <b>o latura</b>.</p>
</div>

<h2>Piese, pentru o latura</h2>
<div class="parts">{parts}</div>

<h2>Pas cu pas</h2>
<div class="steps">{steps}</div>

<h2>Ce tine, de fapt</h2>
<div class="hero"><div class="grid">
  <div class="fig">{fit(F['detaliu'], 300, 360)}</div>
  <div class="txt">
    <h3>Acelasi colt, privit din afara puntii, cu blocajul taiat in doua</h3>
    <p>Aici se vede piesa care conteaza: latura orizontala a vinclului sta <b>sub</b> blocaj si il duce pe dedesubt. Nu e un coltar lipit pe lateral — e o polita.</p>
    <p>Greutatea nu ramane in blocaj si nu se lasa pe gol. Merge in grinda groasa de la marginea podelei, adica exact in lemnul care tine deja toata puntea si pe care calci in fiecare zi.</p>
    <div class="chain">calci pe scandura → blocaj → vinclu → grinda groasa → stalpii puntii → pamant</div>
  </div>
</div></div>

<h2>Greseala de evitat</h2>
<div class="bad"><div class="grid">
  <div class="fig">{fit(F['nu'], 200, 280)}</div>
  <div>
    <h3>Nu pune doar o scandura peste gol</h3>
    <p>O scandura asezata peste gol se sprijina pe marginile ei si pe nimic altceva. Tine cateva luni, apoi se lasa, scartaie si iese din plan — mai ales cand se umfla si se usuca de la ploaie. Vinclurile costa cateva lei si rezolva definitiv.</p>
  </div>
</div></div>

<footer class="doc">BLOCAJ-COLT-2026-08-20 · desene in izometrie, generate din cotele reale · se repeta pe 2 laturi × 2 colturi din spate · vezi PROIECT-CASA pentru planul complet si GHID-SIMPLU-casa pentru detaliile de perete.</footer>
</div></body></html>"""


open('BLOCAJ-COLT-2026-08-20.html', 'w').write(build())
print('ok')
