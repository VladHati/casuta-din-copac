#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
F=json.load(open('figs_masura.json'))

HTML=f'''<!doctype html><html lang="ro"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Masoara golul din spate</title>
<style>
:root{{--bg:#faf8f3;--ink:#1c1b18;--mut:#6b675e;--ln:#e3ddd0;--warn:#a8541c;--acc:#14532d;--card:#fff}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);
 font:16px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace;-webkit-text-size-adjust:100%}}
.wrap{{max-width:820px;margin:0 auto;padding:32px 20px 80px}}
h1{{font:600 clamp(24px,5vw,34px)/1.15 ui-monospace,Menlo,monospace;margin:0 0 8px;letter-spacing:-.02em}}
.lead{{color:var(--mut);margin:0 0 36px;font-size:15px}}
h2{{font-size:15px;letter-spacing:.14em;text-transform:uppercase;color:var(--mut);
 margin:44px 0 14px;font-weight:600}}
figure{{margin:0 0 8px;background:var(--card);border:1px solid var(--ln);border-radius:3px;padding:18px}}
figcaption{{color:var(--mut);font-size:13px;margin:10px 2px 0;line-height:1.5}}
table{{width:100%;border-collapse:collapse;margin:14px 0 6px;font-size:15px}}
th,td{{text-align:left;padding:11px 10px;border-bottom:1px solid var(--ln);vertical-align:top}}
th{{font-weight:600;color:var(--mut);font-size:12px;letter-spacing:.09em;text-transform:uppercase}}
td.k{{font-weight:700;color:var(--warn);width:56px;font-size:19px}}
td.blank{{color:#c9c2b3}}
.box{{border-left:2px solid var(--warn);padding:2px 0 2px 16px;margin:22px 0;color:var(--ink)}}
.box b{{color:var(--warn)}}
.ok{{border-left-color:var(--acc)}} .ok b{{color:var(--acc)}}
code{{background:#efeade;padding:2px 6px;border-radius:2px;font-size:14px}}
footer{{margin-top:64px;padding-top:18px;border-top:1px solid var(--ln);color:var(--mut);font-size:12px}}
</style></head><body><div class="wrap">

<h1>Masoara golul din spate</h1>
<p class="lead">Trei numere pe colt. Doua colturi. Cinci minute cu ruleta.<br>
Fara ele nu pot desena scandura la scara &mdash; si nu vreau sa ti-o desenez gresit a doua oara.</p>

<h2>1 &middot; Vedere de sus</h2>
<figure>{F['masura_plan']}</figure>
<figcaption>Stalpul din spate, cu decupajul din dusumea in jurul lui. Golul are forma de L:
o fasie in fata stalpului (latimea <b>A</b>) si una langa el (latimea <b>B</b>).
Desenul e la 100&times;100 nominal &mdash; formele sunt corecte, numerele nu.</figcaption>

<h2>2 &middot; Sectiune</h2>
<figure>{F['masura_sect']}</figure>
<figcaption>Acelasi gol, taiat vertical. <b>C</b> e cat de adanc vezi pana dai de ceva solid.</figcaption>

<h2>3 &middot; Tabelul de completat</h2>
<table>
<tr><th></th><th>Ce masori</th><th>Colt stanga</th><th>Colt dreapta</th></tr>
<tr><td class="k">A</td><td>De la fata stalpului (spre interiorul puntii) pana la prima scandura</td><td class="blank">___ mm</td><td class="blank">___ mm</td></tr>
<tr><td class="k">B</td><td>De la lateralul stalpului pana la prima scandura</td><td class="blank">___ mm</td><td class="blank">___ mm</td></tr>
<tr><td class="k">C</td><td>Cat de adanc vezi in gol, pana dai de ceva</td><td class="blank">___ mm</td><td class="blank">___ mm</td></tr>
<tr><td class="k">?</td><td>Se vede grinda groasa dedesubt?</td><td class="blank">DA / NU</td><td class="blank">DA / NU</td></tr>
</table>

<div class="box"><b>Daca decupajul nu e dreptunghiular</b> &mdash; daca e in trepte, pentru ca fiecare
scandura a fost taiata separat &mdash; nu incerca sa-l fortezi in trei numere. Spune-mi doar
&bdquo;e in trepte&rdquo; si fa o poza. Redesenez dupa poza.</div>

<div class="box ok"><b>Poza care ajuta cel mai mult:</b> stai pe punte, tine ruleta intinsa peste gol,
si prinde in acelasi cadru <b>stalpul, marginea dusumelei si golul dintre ele</b>.
O singura poza asa valoreaza cat toate cele trei numere.</div>

<footer>MASOARA-GOL &middot; 20 august 2026 &middot; cote in mm &middot; desenele sunt nominale pana primesc numerele</footer>
</div></body></html>'''

open('MASOARA-GOL.html','w',encoding='utf-8').write(HTML)
print('scris', len(HTML), 'caractere')
