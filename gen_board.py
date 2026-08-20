#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Tabla gata compusa pentru Freeform: un singur PNG, fundal transparent,
# carduri deschise la culoare (se citesc si pe tabla alba, si pe una inchisa).
import json, re
from playwright.sync_api import sync_playwright

F = json.load(open('figs_ikea.json'))


def fit(svg, h, w):
    m = re.search(r'viewBox="(-?[\d.]+) (-?[\d.]+) ([\d.]+) ([\d.]+)"', svg)
    vw, vh = float(m.group(3)), float(m.group(4))
    k = min(h / vh, w / vw)
    return re.sub(r'style="[^"]*"',
                  f'style="width:{vw*k:.0f}px;height:{vh*k:.0f}px;display:block;margin:0 auto"',
                  svg, count=1)


STEPS = [
    ('1', 'Asa e acum',              'acum',     'Gol ~100 mm. Dedesubt nu e nimic.'),
    ('2', 'Doua vincluri pe grinda', 'coltare',  'Suruburi scurte in grinda groasa. Latura scurta iese in gol, orizontala.'),
    ('3', 'Blocajul pe vincluri',    'blocaj',   'Aici sta. Pe cele doua polite de metal.'),
    ('4', 'Suruburi oblice, de sus', 'suruburi', '3 × 8×140 in grinda, 2 in stalp. Se dau stand pe punte.'),
    ('5', 'Scandura de calcat',      'scandura', 'La nivel cu podeaua. Cosmetica, nu duce greutate.'),
    ('6', 'Gata',                    'gata',     'Calca pe el. Daca nu se misca si nu suna a gol, e bun.'),
]

PARTS = [
    ('2', 'vinclu 90×65'),
    ('1', 'blocaj de lemn, taiat pe loc'),
    ('8', 'suruburi scurte 5×40'),
    ('5', 'suruburi dulgherie 8×140'),
    ('1', 'scandura de calcat'),
]

ROWS = ['Colt 1 · latura A', 'Colt 1 · latura B', 'Colt 2 · latura A', 'Colt 2 · latura B']

CSS = """
:root{--ink:#1c1b18;--muted:#6b675e;--line:#e2ddd3;--acc:#14532d;--acc2:#8a3016;
--mono:ui-monospace,"DejaVu Sans Mono",Menlo,monospace;
--sans:"Helvetica Neue",Helvetica,Arial,"DejaVu Sans",sans-serif;--serif:Georgia,serif}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:transparent}
.board{width:2260px;padding:34px;display:grid;gap:26px;
  grid-template-columns:1fr 1fr 1fr 700px;
  grid-template-areas:
   "hd hd hd hd"
   "s1 s2 s3 det"
   "s4 s5 s6 det"
   "mx mx mx nu";
  font:16px/1.5 var(--sans);color:var(--ink)}

.card{background:#faf9f6;border:1px solid var(--line);border-radius:10px;padding:20px 22px 22px}

.hd{grid-area:hd;background:#faf9f6;border:1px solid var(--line);border-radius:10px;
    padding:22px 26px;display:flex;align-items:baseline;gap:30px}
.hd .k{font:700 12px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--acc);white-space:nowrap}
.hd h1{font:700 34px/1.1 var(--sans);margin:0;letter-spacing:-.015em;white-space:nowrap}
.hd .s{font:italic 17px/1.4 var(--serif);color:var(--muted);flex:1}

.st .top{display:flex;align-items:baseline;gap:12px;border-bottom:1px solid var(--line);
  padding-bottom:10px;margin-bottom:8px}
.st .n{font:700 32px/1 var(--mono);color:var(--acc2)}
.st .t{font:600 18px/1.2 var(--sans)}
.st .fig{margin:8px 0 12px;text-align:center}
.st .c{font-size:14.5px;line-height:1.45;color:var(--muted);min-height:44px}
.st .pad{margin-top:12px;border-top:1px dashed #d9d3c7;height:66px}

.det{grid-area:det;display:flex;flex-direction:column}
.det .lbl{font:700 12px/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:14px}
.det h2{font:700 24px/1.25 var(--sans);margin:0 0 12px}
.det p{margin:0 0 12px;font-size:16px;line-height:1.55}
.det .fig{text-align:center;margin:6px 0 14px}
.chain{font:15px/1.7 var(--mono);color:var(--acc2);background:#fbf5ef;border-radius:6px;padding:12px 14px}
.parts{margin-top:16px;border-top:1px solid var(--line);padding-top:14px}
.parts .h{font:700 12px/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:10px}
.parts ul{margin:0;padding:0;list-style:none;font:15px/1.9 var(--mono);color:var(--ink)}
.parts b{color:var(--acc2);display:inline-block;width:42px}

.nu{grid-area:nu;background:#fdf6f1;border:1px solid #e5cdbe;border-radius:10px;padding:20px 22px;
    display:flex;gap:20px;align-items:center}
.nu h3{font:700 19px/1.2 var(--sans);margin:0 0 8px;color:var(--acc2)}
.nu p{margin:0;font-size:15px;line-height:1.5}

.mx{grid-area:mx}
.mx .h{font:700 12px/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:14px}
table{border-collapse:collapse;width:100%}
th{font:600 13px var(--mono);color:var(--muted);padding:0 0 10px;text-align:center}
th.l{text-align:left;width:230px}
td{padding:7px 0;text-align:center;border-top:1px solid var(--line)}
td.l{text-align:left;font:15px var(--sans);color:var(--ink)}
.bx{display:inline-block;width:30px;height:30px;border:2px solid #c3bcae;border-radius:5px}
.note{margin-top:14px;font-size:14px;color:var(--muted)}
"""


def build():
    steps = ''
    for i, (n, t, k, c) in enumerate(STEPS, 1):
        steps += (f'<div class="card st" style="grid-area:s{i}">'
                  f'<div class="top"><span class="n">{n}</span><span class="t">{t}</span></div>'
                  f'<div class="fig">{fit(F[k], 250, 420)}</div>'
                  f'<div class="c">{c}</div><div class="pad"></div></div>')

    parts = ''.join(f'<li><b>×{q}</b> {n}</li>' for q, n in PARTS)

    head = ''.join(f'<th>{i}</th>' for i in range(1, 7))
    rows = ''.join('<tr><td class="l">' + r + '</td>' +
                   ''.join('<td><span class="bx"></span></td>' for _ in range(6)) + '</tr>'
                   for r in ROWS)

    return f"""<!DOCTYPE html><html lang="ro"><head><meta charset="utf-8">
<style>{CSS}</style></head><body><div class="board">

<div class="hd">
  <span class="k">Casuta din copac</span>
  <h1>Golul de la coltul din spate</h1>
  <span class="s">Pe ce sta scandura noua: pe doua vincluri prinse in grinda groasa de la marginea podelei — nu pe gol. Se face de patru ori: doua laturi la fiecare colt din spate.</span>
</div>

{steps}

<div class="card det">
  <div class="lbl">Ce tine, de fapt</div>
  <div class="fig">{fit(F['detaliu'], 330, 620)}</div>
  <h2>Acelasi colt, din afara puntii, cu blocajul taiat</h2>
  <p>Latura orizontala a vinclului sta <b>sub</b> blocaj si il duce pe dedesubt. Nu e un coltar lipit pe lateral — e o polita.</p>
  <div class="chain">calci pe scandura → blocaj → vinclu →<br>grinda groasa → stalpii puntii → pamant</div>
  <div class="parts"><div class="h">Piese, pentru o latura</div><ul>{parts}</ul></div>
  <div class="pad" style="flex:1;min-height:80px"></div>
</div>

<div class="card mx">
  <div class="h">Unde am ajuns</div>
  <table>
    <tr><th class="l"></th>{head}</tr>
    {rows}
  </table>
  <div class="note">Bifeaza pe masura ce faci. Pasii 1–6 sunt cei din carduri.</div>
</div>

<div class="nu">
  <div style="flex:0 0 240px">{fit(F['nu'], 200, 240)}</div>
  <div>
    <h3>Nu pune doar o scandura peste gol</h3>
    <p>Se sprijina pe marginile ei si pe nimic altceva. Tine cateva luni, apoi se lasa si scartaie.</p>
  </div>
</div>

</div></body></html>"""


open('/tmp/board.html', 'w').write(build())

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg = b.new_page(viewport={'width': 2260, 'height': 1400}, device_scale_factor=2)
    pg.goto('file:///tmp/board.html')
    el = pg.query_selector('.board')
    el.screenshot(path='FREEFORM-PNG/00-TABLA-gol-colt.png', omit_background=True)
    b.close()
print('ok')
