#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Capitolul E0 — scandura care lipseste la colturile din spate."""
import json
F=json.load(open('figs_e0.json'))

def fig(key, cap):
    return f'<figure>{F[key]}<figcaption>{cap}</figcaption></figure>'

def bifa(i, t):
    return (f'<label class="b"><input type="checkbox" data-i="{i}"><span></span>'
            f'<em>{t}</em></label>')

SECTIUNI = []

# ─── 1 ───
SECTIUNI.append(('situatia','Situatia', f'''
<p class="lead">La fiecare dintre cele doua colturi din spate, dusumea se opreste inainte
de stalp. Ramane un sant in forma de L, in jurul stalpului. Sub el nu e sprijin.</p>

{fig('e0_unde','Puntea vazuta de sus. Cele doua colturi din spate sunt identice, in oglinda. Tot ce urmeaza se face de doua ori.')}

{fig('e0_acum','Coltul, marit. Golul e o fasie in fata stalpului si una langa el. A si B sunt cele doua numere de masurat.')}

{fig('e0_acum_sect','Sectiune prin gol. Ce e sub el nu se stie inca — asta e al treilea numar, C.')}

<div class="box warn">
<b>Trei numere lipsesc, si desenele sunt nominale pana le primesc.</b>
Formele sunt corecte — proportiile nu. Vezi <code>MASOARA-GOL.html</code>:
<b>A</b> (latimea golului in fata stalpului), <b>B</b> (latimea langa stalp),
<b>C</b> (adancimea). Schimb trei numere in generator si toate desenele de mai jos
se refac la scara reala.
</div>
'''))

# ─── 2 ───
SECTIUNI.append(('principiu','De ce nu doar o scandura', f'''
<p class="lead">Prima idee e sa pui o scandura peste sant si sa treci mai departe. Nu tine,
si merita treizeci de secunde sa intelegi de ce.</p>

{fig('e0_principiu','Stanga: scandura peste sant. Un capat sta pe muchia dusumelei, celalalt pe nimic — dincolo e marginea puntii. Dreapta: blocajul sta pe o polita de metal prinsa in lemnul portant.')}

<p>Santul are lemn <b>doar pe o latura</b>. Pe cealalta e marginea puntii, adica aer.
O scandura pusa peste el nu e o grinda pe doua reazeme — e o consola sprijinita pe o
muchie de 28 mm. Tine cateva luni. Apoi ploua, lemnul se umfla si se usuca de cateva
ori, si scandura incepe sa scartaie si sa se lase.</p>

<p>Vinclul schimba complet situatia: bratul lui scurt devine o polita, blocajul se aseaza
pe ea, si greutatea pleaca lateral in lemnul care tine deja toata puntea.</p>

{fig('e0_forta','Drumul greutatii, de la talpa pana in pamant. Vinclul e nodul care scoate sarcina din sant.')}
'''))

# ─── 3 ───
SECTIUNI.append(('piese','Piesele', f'''
{fig('e0_piese','Piesele, la scara. Blocajul si scandura se taie pe loc, dupa masuratoare.')}

<table>
<tr><th>Piesa</th><th>Cantitate pe colt</th><th>Total (2 colturi)</th><th>Nota</th></tr>
<tr><td>Vinclu 90×65</td><td>3</td><td>6</td><td>deja pe lista Leroy</td></tr>
<tr><td>Blocaj de lemn</td><td>2</td><td>4</td><td>din offcut de 100, taiat pe loc</td></tr>
<tr><td>Scandura de calcat</td><td>2</td><td>4</td><td>larice 28, ca restul podelei</td></tr>
<tr><td>Surub 5×40</td><td>12</td><td>24</td><td>4 pe vinclu</td></tr>
<tr><td>Surub 8×140</td><td>10</td><td>20</td><td>5 pe fasie</td></tr>
<tr><td>Surub 5×60</td><td>8</td><td>16</td><td>4 pe scandura</td></tr>
</table>

<div class="box">
<b>Numarul de vincluri depinde de A si B.</b> Regula: unul la fiecare ~150 mm de sant,
si minimum unul sub fiecare capat de blocaj. Cu A si B la 100 mm ies trei pe colt.
Daca golul e mai lung, ies mai multe.
</div>

{fig('e0_plan_montaj','Unde vin vinclurile, vazute de sus. Bratul scurt intra in sant; cel lung se prinde de lemnul portant, sub dusumea.')}
'''))

# ─── 4 ───
SECTIUNI.append(('pasi','Pas cu pas', f'''
<h3>Pasul 1 &middot; vinclurile</h3>
{fig('e0_s1','Sectiune. Bratul lung (90) urca pe fata lemnului portant; cel scurt (65) iese orizontal in sant.')}
<p>Tine vinclul in pozitie si marcheaza gaurile cu creionul. <b>Pregauresti 3 mm</b> —
lemnul de la marginea dusumelei e la capat de fibra si crapa daca bagi surubul direct.
Patru suruburi 5&times;40 pe vinclu.</p>
<p>Fata de sus a bratului scurt trebuie sa ajunga la <b>118 mm sub podea</b>: 28 pentru
scandura de calcat, 90 pentru blocaj. Masoara de la fata dusumelei in jos, nu de la
altceva.</p>
{bifa(0,'Toate vinclurile montate, la acelasi nivel')}

<h3>Pasul 2 &middot; blocajele</h3>
{fig('e0_s2','Blocajul se lasa pe polite. Deasupra lui raman exact 28 mm, cat grosimea scandurii de calcat.')}
<p>Taie blocajul pe loc, dintr-un offcut. Latimea = latimea santului pe fasia aia.
Inaltimea = 90.</p>
<p><b>Proba:</b> blocajul trebuie sa se aseze singur pe vincluri. Daca trebuie sa-l bati
cu ciocanul, e prea mare — mai da-i un milimetru la rindea. Un blocaj fortat impinge
vinclurile si le desface din suruburi.</p>
{bifa(1,'Blocajele taiate si asezate, fara joc si fara forta')}

<h3>Pasul 3 &middot; suruburile</h3>
{fig('e0_s3','Suruburile 8×140, date oblic de sus. Varful trebuie sa treaca prin blocaj si sa intre in lemnul portant.')}
<p>Trei suruburi oblic in lemnul portant al puntii, doua in stalp. Toate se dau
<b>de sus, stand pe punte</b> — nu trebuie sa cobori dedesubt.</p>
<p>Unghiul: <b>~30&deg; fata de verticala</b>. Prea drept si surubul ramane in blocaj,
fara sa prinda nimic. Prea culcat si iese prin lateral. Pregauresti 5 mm prin blocaj,
ca sa nu-l crape si ca surubul sa traga blocajul spre lemn, nu sa-l impinga.</p>
{bifa(2,'Cinci suruburi 8×140 pe fiecare fasie')}
{bifa(3,'Blocajul nu se mai misca deloc cand il impingi cu mana')}

<h3>Pasul 4 &middot; scandura de calcat</h3>
{fig('e0_s4','Ultima piesa. La nivel cu restul podelei, cu acelasi rost de 5 mm fata de scandurile vecine.')}
<p>Doua bucati de larice 28, taiate exact pe forma fasiei. Patru suruburi 5&times;60
pe bucata.</p>
<p>Verifica nivelul cu o dreptare pusa peste scandurile vecine, nu din ochi.
O diferenta de 2 mm se simte cu piciorul gol si se vede la lumina joasa.</p>
{bifa(4,'Scandurile taiate, la nivel, cu rost de 5 mm')}
'''))

# ─── 5 ───
SECTIUNI.append(('gata','Gata', f'''
{fig('e0_gata','Sectiunea finala. Vinclurile raman ascunse dedesubt; de sus se vede doar podea.')}

<p><b>Proba finala:</b> calca pe scandura cu toata greutatea, langa stalp si la mijloc.
Nu trebuie sa se miste, sa scartaie sau sa sune a gol. Daca suna, blocajul nu sta pe
ambele vincluri — scoate scandura si verifica.</p>

<div class="box ok">
<b>Poarta de faza.</b> Asta se face inainte de peretele din spate. Talpa peretelui se
prinde exact pe zona asta &mdash; daca golul e inca acolo, talpa nu are in ce se insuruba
la capete.
</div>

{bifa(5,'Am calcat pe amandoua colturile. Nu se misca, nu suna a gol.')}
{bifa(6,'Gata — se poate trece la peretele din spate')}
'''))

TOC = '\n'.join(f'<a href="#{k}"><i>{i+1}</i>{t}</a>' for i,(k,t,_) in enumerate(SECTIUNI))
BODY = '\n'.join(f'<section id="{k}"><h2><i>{i+1}</i>{t}</h2>{b}</section>'
                 for i,(k,t,b) in enumerate(SECTIUNI))
NB = sum(s[2].count('type="checkbox"') for s in SECTIUNI)

HTML=f'''<!doctype html><html lang="ro"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>E0 · Scandura care lipseste</title>
<style>
:root{{
 --bg:#faf8f3;--card:#fff;--ink:#1c1b18;--mut:#6b675e;--ln:#e3ddd0;
 --warn:#a8541c;--acc:#14532d;--chip:#f0ebdf;
}}
html[data-t="d"]{{
 --bg:#17181a;--card:#1e2023;--ink:#e9e5db;--mut:#9a958a;--ln:#2e3135;
 --warn:#d98b4a;--acc:#7fb894;--chip:#24272b;
}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);
 font:16px/1.65 ui-monospace,SFMono-Regular,Menlo,monospace;
 -webkit-text-size-adjust:100%;transition:background .2s,color .2s}}
.shell{{display:grid;grid-template-columns:230px minmax(0,1fr);gap:56px;
 max-width:1180px;margin:0 auto;padding:40px 26px 120px}}
nav{{position:sticky;top:32px;align-self:start}}
nav .kicker{{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--mut);margin-bottom:18px}}
nav a{{display:flex;gap:10px;padding:7px 0;color:var(--mut);text-decoration:none;font-size:14px;line-height:1.35}}
nav a i{{font-style:normal;opacity:.5;min-width:14px}}
nav a:hover{{color:var(--ink)}}
nav a.on{{color:var(--ink);font-weight:600}} nav a.on i{{opacity:1;color:var(--warn)}}
.prog{{margin-top:24px;padding-top:18px;border-top:1px solid var(--ln);font-size:12px;color:var(--mut)}}
.bar{{height:2px;background:var(--ln);margin-top:8px;border-radius:2px;overflow:hidden}}
.bar>i{{display:block;height:100%;width:0;background:var(--acc);transition:width .3s}}
header{{margin-bottom:14px}}
h1{{font:600 clamp(28px,4.4vw,42px)/1.1 ui-monospace,Menlo,monospace;margin:0 0 10px;letter-spacing:-.025em}}
.sub{{color:var(--mut);font-size:15px;margin:0 0 8px}}
.meta{{color:var(--mut);font-size:12px;letter-spacing:.06em}}
section{{margin-top:64px;scroll-margin-top:28px}}
h2{{display:flex;gap:14px;align-items:baseline;font-size:22px;margin:0 0 22px;
 padding-bottom:14px;border-bottom:1px solid var(--ln);font-weight:600;letter-spacing:-.01em}}
h2 i{{font-style:normal;font-size:13px;color:var(--warn);opacity:.9}}
h3{{font-size:16px;margin:44px 0 14px;font-weight:600;letter-spacing:.01em}}
h3:first-of-type{{margin-top:8px}}
p{{margin:0 0 15px}} .lead{{color:var(--mut)}}
figure{{margin:24px 0 10px;background:var(--card);border:1px solid var(--ln);
 border-radius:3px;padding:20px}}
figcaption{{color:var(--mut);font-size:13px;line-height:1.5;margin:14px 2px 0}}
html[data-t="d"] figure{{background:#f3f0e7;border-color:#33363a}}
html[data-t="d"] figcaption{{color:var(--mut)}}
table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}}
th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--ln)}}
th{{font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--mut);font-weight:600}}
.box{{border-left:2px solid var(--ln);padding:2px 0 2px 18px;margin:24px 0;font-size:15px}}
.box.warn{{border-left-color:var(--warn)}} .box.warn b{{color:var(--warn)}}
.box.ok{{border-left-color:var(--acc)}} .box.ok b{{color:var(--acc)}}
code{{background:var(--chip);padding:2px 6px;border-radius:2px;font-size:13px}}
.b{{display:flex;gap:12px;align-items:flex-start;margin:12px 0;cursor:pointer;font-size:15px}}
.b input{{display:none}}
.b span{{flex:0 0 17px;height:17px;margin-top:3px;border:1.5px solid var(--ln);border-radius:2px;
 position:relative;transition:.15s}}
.b input:checked+span{{background:var(--acc);border-color:var(--acc)}}
.b input:checked+span:after{{content:"";position:absolute;left:5px;top:1.5px;width:4px;height:9px;
 border:solid #fff;border-width:0 1.8px 1.8px 0;transform:rotate(43deg)}}
.b em{{font-style:normal}} .b input:checked~em{{color:var(--mut);text-decoration:line-through}}
.tog{{position:fixed;right:20px;bottom:20px;z-index:9;background:var(--card);color:var(--mut);
 border:1px solid var(--ln);border-radius:3px;padding:8px 13px;font:12px ui-monospace,Menlo,monospace;
 cursor:pointer;letter-spacing:.06em}}
footer{{margin-top:80px;padding-top:20px;border-top:1px solid var(--ln);color:var(--mut);font-size:12px;line-height:1.7}}
@media(max-width:880px){{
 .shell{{grid-template-columns:1fr;gap:0;padding:26px 18px 90px}}
 nav{{position:static;margin-bottom:34px;padding-bottom:20px;border-bottom:1px solid var(--ln)}}
 nav a{{display:inline-flex;margin-right:16px}}
 section{{margin-top:48px}}
}}
</style></head><body>
<button class="tog" onclick="tg()">lumina / intuneric</button>
<div class="shell">
<nav>
 <div class="kicker">E0 · cuprins</div>
 {TOC}
 <div class="prog">progres <b id="pn">0</b>/{NB}<div class="bar"><i id="pb"></i></div></div>
</nav>
<main>
<header>
 <h1>Scandura care lipseste</h1>
 <p class="sub">Golul de la colturile din spate, de la ce e acum pana la podea intreaga.</p>
 <p class="meta">20 august 2026 &middot; cote in mm &middot; se face de doua ori, cate o data pe colt</p>
</header>
{BODY}
<footer>
GHID E0 &middot; toate desenele sunt generate din acelasi model numeric (<code>gen_e0.py</code>);
cotele nu sunt scrise de mana.<br>
A, B si C sunt inca nominale &mdash; vezi <code>MASOARA-GOL.html</code>. Cand vin numerele,
desenele se refac la scara reala.<br>
Inlocuieste Detaliul 7 din SCHEME-CASA si versiunea in izometrie din BLOCAJ-COLT.
</footer>
</main></div>
<script>
function tg(){{const h=document.documentElement;
 h.dataset.t = h.dataset.t==='d' ? '' : 'd';}}
const boxes=[...document.querySelectorAll('.b input')],pn=document.getElementById('pn'),pb=document.getElementById('pb');
function upd(){{const n=boxes.filter(b=>b.checked).length;
 pn.textContent=n;pb.style.width=(n/boxes.length*100)+'%';}}
boxes.forEach(b=>b.addEventListener('change',upd));
const links=[...document.querySelectorAll('nav a')];
const io=new IntersectionObserver(es=>{{es.forEach(e=>{{if(e.isIntersecting)
 links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id));}});}},
 {{rootMargin:'-15% 0px -70% 0px'}});
document.querySelectorAll('section').forEach(s=>io.observe(s));
</script></body></html>'''

open('GHID-E0-golul-din-spate.html','w',encoding='utf-8').write(HTML)
print('scris', len(HTML), 'caractere ·', NB, 'bife ·', len(SECTIUNI), 'sectiuni')
