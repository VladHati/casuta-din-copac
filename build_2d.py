#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asambleaza SCHEME-2D-casa.html din figs_2d.json (produs de gen_2d.py).
Anexa de desene a GHID-CONSTRUCTIE-casa.html. Nu se editeaza HTML-ul direct:
desenele vin din gen_2d.py, textul din jur e in lista SECS de mai jos."""
import json

F = json.load(open('figs_2d.json'))

# (id, titlu, descriere, cheia figurii)   —   colt e caz special (fara desen)
SECS = [
 ('plan','Plan — casa vazuta de sus',
  'Ce e unde. Peretii din fata si din spate stau in banda stalpilor; lateralele traverseaza cei 1575 dintre ei.','plan'),
 ('sectiune','Sectiune longitudinala — fata in stanga, spate in dreapta',
  'De unde vine panta: 240 mm cadere pe 1670 intre reazeme.','sectiune'),
 ('spate','Elevatie — peretele din SPATE, din exterior',
  'Se face complet jos, pe iarba. Dupa ridicare, intre el si gard raman 30 cm. Rama e din rigla 48×48.','spate'),
 ('lateral','Elevatie — peretele LATERAL, din exterior',
  'Cununa e inclinata, deci fiecare verticala are alta lungime. Cele doua laterale difera intre ele cu 10 mm.','lateral'),
 ('fata','Elevatie — peretele din FATA, din exterior',
  'Bara de sus e mai lunga decat rama: trece peste amandoi stalpii, altfel nu-i leaga.','fata'),
 ('acoperis','Plan acoperis — vazut de sus',
  'Cinci lemne inclinate, doua placi de OSB. Fara sipci: la 8,2° producatorul cere suport continuu.','acoperis'),
 ('strat','Detaliu — straturile acoperisului',
  'De ce cuiele stau pe varful valului si nu in adancitura.','strat'),
 ('prindere','Detaliu — peretele din spate, prins in stalp',
  'Patru suruburi pe fiecare capat, cu gaura data inainte. Verticala de capat e rigla 48×48.','prindere'),
 ('reazem','Detaliu — reazemul din spate (dulapul de 200×50)',
  'O singura bara, taiata la 2200, asezata pe muchie cu 200 in sus peste cununa peretelui si peste '
  'capetele stalpilor (ambele la 1700) → reazem continuu la 1900. Nimic altceva nu se face din ea.','reazem'),
]

NAV = {'plan':'Plan','sectiune':'Sectiune','spate':'Spate','lateral':'Lateral','fata':'Fata',
       'acoperis':'Acoperis','strat':'Straturi','prindere':'Prindere','reazem':'Reazem','colt':'Colt — lipseste'}

STYLE = """<style>
:root{--bg:#faf9f6;--card:#fff;--ink:#1c1b18;--mut:#6b675e;--dim:#8f8b83;--line:#e2ddd3;--acc:#14532d;--acc2:#8a3016;
--mono:ui-monospace,Menlo,monospace;--sans:"Helvetica Neue",Helvetica,Arial,sans-serif;--serif:"Iowan Old Style",Georgia,serif}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 var(--sans)}
.w{max-width:1080px;margin:0 auto;padding:44px 24px 120px}
h1{font:600 34px/1.15 var(--sans);letter-spacing:-.02em;margin:0 0 8px}
.kick{font:600 11px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin-bottom:12px}
.sub{font:italic 17px/1.5 var(--serif);color:var(--mut);max-width:64ch;margin:0 0 6px}
.meta{font:12px/1.6 var(--mono);color:var(--dim);margin:16px 0 30px}
ul.n{list-style:none;display:flex;flex-wrap:wrap;gap:8px;padding:0;margin:0 0 34px}
ul.n a{display:block;font:12px var(--mono);color:var(--ink);text-decoration:none;border:1px solid var(--line);
border-radius:999px;padding:7px 13px;background:var(--card)}
ul.n a:hover{border-color:var(--acc);color:var(--acc)}
section{margin:0 0 54px;scroll-margin-top:16px}
h2{font:600 20px/1.3 var(--sans);margin:0 0 6px;letter-spacing:-.01em}
section p{color:var(--mut);margin:0 0 16px;max-width:70ch;font-size:15px}
figure{margin:0;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px}
.gap{background:#fdf3ee;border:1px solid var(--line);border-left:3px solid var(--acc2);border-radius:12px;padding:18px 20px}
.gap p{color:var(--ink);max-width:70ch}
a{color:var(--acc)}
footer{margin-top:40px;padding-top:20px;border-top:1px solid var(--line);font:12px/1.7 var(--mono);color:var(--dim)}
</style>"""

nav = ''.join(f'<li><a href="#{i}">{NAV[i]}</a></li>' for i,_,_,_ in SECS) + f'<li><a href="#colt">{NAV["colt"]}</a></li>'

secs = []
for i, h2, desc, key in SECS:
    secs.append(f'<section id="{i}"><h2>{h2}</h2><p>{desc}</p><figure>{F[key]}</figure></section>')
secs.append('''<section id="colt"><h2>Coltul din spate — lipseste</h2>
<div class="gap"><p><b>Nu exista desen pentru golul de la colturile din spate, si asta e intentionat.</b></p>
<p>Nicio poza din proiect nu arata stalpul, marginea podelei si golul dintre ele in acelasi cadru. Desenele facute pana acum au fost reconstituite din descriere, nu din realitate — de asta erau gresite si au fost scoase.</p>
<p><b>Ce imi trebuie:</b> doua poze, cate una pe colt. Din picioare, de pe punte, incadrand simultan stalpul, marginea podelei si golul, cu <b>ruleta intinsa peste gol</b> ca sa se vada latimea reala.</p></div></section>''')

HTML = f'''<!DOCTYPE html><html lang="ro"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Scheme 2D — casa de sus</title>{STYLE}</head><body><div class="w">
<div class="kick">Casuta din copac · casa de sus · anexa la <a href="GHID-CONSTRUCTIE-casa.html">GHID-CONSTRUCTIE-casa</a></div>
<h1>Scheme 2D</h1>
<p class="sub">Zece vederi ortogonale, fiecare derivata din acelasi model numeric. Nicio cota nu e scrisa de mana — toate se calculeaza din masuratorile de santier si se verifica automat la generare.</p>
<div class="meta">20 august 2026 · cote in mm · geometrie masurata 20.08 · rama = rigla 48×48 · generate din <code>gen_2d.py</code> + <code>build_2d.py</code></div>
<ul class="n">{nav}</ul>
{chr(10).join(secs)}
<footer>SCHEME-2D-casa · desenele care insotesc <a href="GHID-CONSTRUCTIE-casa.html">GHID-CONSTRUCTIE-casa.html</a> (documentul de executie). Inlocuiesc izometriile vechi si Detaliul 7 din SCHEME-CASA.<br>
Sursa cotelor: MASURATORI-CONFIRMARE-2026-08-20. Model + auto-verificare: gen_2d.py.</footer>
</div></body></html>'''

open('SCHEME-2D-casa.html','w',encoding='utf-8').write(HTML)
print('scris SCHEME-2D-casa.html', len(HTML), 'caractere ·', len(SECS)+1, 'sectiuni')
