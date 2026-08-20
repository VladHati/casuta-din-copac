#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asambleaza GHID-CONSTRUCTIE-casa.html — ghid de santier, capitole + cuprins lateral."""
import json

GH = json.load(open('figs_ghid.json'))
D2 = json.load(open('figs_2d.json'))

def fig(svg, cap='', wide=False):
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure class="{"wide" if wide else ""}">{svg}{c}</figure>'

def steps(items):
    out=['<ol class="steps">']
    for i,(titlu, corp, svg) in enumerate(items,1):
        s = f'<div class="stepfig">{svg}</div>' if svg else ''
        out.append(f'<li><label class="tick"><input type="checkbox"><span></span></label>'
                   f'<div class="stepbody"><h4>{titlu}</h4>{corp}{s}</div></li>')
    out.append('</ol>')
    return '\n'.join(out)

CH = []

# ══════════════════════════════ E0 ══════════════════════════════
CH.append(dict(id='e0', n='E0', titlu='Scandura care lipseste',
    sub='Golul de la cele doua colturi din spate. Patru locuri identice.',
    zi='2–3 ore', body=f"""
<p class="lead">La ambele colturi din spate, podeaua nu ajunge pana la stalp — ramane un gol de aproximativ <b>100 mm</b>, si sub el nu e nimic. Stalpul e infipt in pamant <em>langa</em> marginea podelei, nu pe ea.</p>

<div class="gate">
<b>De ce e primul lucru:</b> talpa peretelui din spate se prinde prin podea, in grinzile de dedesubt, la fiecare 40 cm. Exact la colturi nu are in ce sa se prinda. Dupa ce peretele e ridicat, la coltul ala nu mai ajungi niciodata.
</div>

<div class="stop">
<b>Capitolul asta nu are inca desene — si nu le inventez.</b><br>
Nicio poza din proiect nu arata stalpul, marginea podelei si golul dintre ele in acelasi cadru. Desenele facute pana acum au fost reconstituite din descriere; erau gresite si au fost scoase.<br><br>
<b>Ce imi trebuie:</b> doua poze, cate una pe colt. Din picioare, de pe punte, incadrand simultan stalpul, marginea podelei si golul, cu <b>ruleta intinsa peste gol</b> ca sa se vada latimea reala. Dupa ele desenez planul si sectiunea, la scara.
</div>

<div class="need">
<h4>Ai nevoie — pentru <em>o latura</em></h4>
<ul>
<li><b>2</b> × vinclu 90×65</li>
<li><b>1</b> × blocaj de lemn, taiat pe loc</li>
<li><b>8</b> × surub scurt 5×40 (pentru vincluri)</li>
<li><b>5</b> × surub dulgherie 8×140</li>
<li><b>1</b> × scandura de calcat</li>
</ul>
<p class="small">Golul e in forma de L in jurul stalpului: latura A si latura B. Se face identic pe amandoua, apoi identic la celalalt colt — <b>de patru ori in total</b>. Deci 8 vincluri, 20 de suruburi 8×140, 32 de suruburi 5×40.</p>
</div>

<div class="stop">
<b>STOP inainte sa incepi:</b> ai 8 vincluri 90×65? Verifica intai ce a ramas din faza 1 — receptia n-a fost niciodata numarata. Daca nu ai, capitolul asta se face <b>dupa</b> drumul la Leroy (E2), nu inainte.
</div>

{steps([
 ('Doua vincluri pe grinda',
  '<p>Se prind cu suruburi scurte in <b>grinda groasa de la marginea podelei</b> — aia care tine deja toata puntea. Latura scurta a vinclului iese in gol, orizontala, ca o polita de raft.</p>', None),
 ('Blocajul se lasa pe vincluri',
  '<p>Asta e toata ideea: blocajul <b>nu pluteste si nu sta pe nimic de dedesubt</b> — se aseaza pe cele doua polite de metal. Ca o polita de biblioteca pe consolele ei. Se taie pe loc, la masura golului.</p>', None),
 ('Suruburi oblice, de sus',
  '<p>Trei suruburi 8×140 oblic in grinda groasa, doua in stalp. Se dau <b>de sus, stand pe punte</b> — nu trebuie sa cobori dedesubt.</p>', None),
 ('Scandura de calcat',
  '<p>Ultima piesa, la nivel cu restul podelei. E doar suprafata pe care calci — <b>nu duce nicio greutate</b>.</p>', None),
])}

<div class="warn">
<p><b>Nu pune doar o scandura peste gol.</b> Se sprijina pe marginile ei si pe nimic altceva. Tine cateva luni, apoi se lasa, scartaie si iese din plan — mai ales cand se umfla si se usuca de la ploaie. Vinclurile costa cativa lei si rezolva definitiv.</p>
</div>

<div class="ok"><b>E bine daca:</b> calci pe el cu toata greutatea si nu se misca, nu scartaie si nu suna a gol. Scandura e la acelasi nivel cu restul podelei.</div>
"""))

# ══════════════════════════════ E1 ══════════════════════════════
CH.append(dict(id='e1', n='E1', titlu='Restantele podelei si cioata',
    sub='Lucruri mici ramase in urma. Toate se inchid intr-o dimineata.',
    zi='2–3 ore', body=f'''
<p class="lead">Trei restante de pe podea, plus decizia cu cioata. Niciuna nu e grea, dar toate blocheaza ceva mai departe.</p>

{steps([
 ('Suruburile lipsa de pe scandurile late',
  '<p>Pe scandurile late sunt multe gauri pregatite, fara surub. Se completeaza cu <b>surub inox 5×60</b>.</p>'
  '<p class="tool">Masina: <b>GSR</b>, treapta de ambreiaj <b>8–12</b>, varf <b>T25</b>. '
  '<b class="bad">Niciodata cu masina de impact</b> — inoxul e moale, rupe capul si nu-l mai scoti din larice.</p>',
  None),
 ('Numaratoarea cumparaturilor vechi',
  '<p>O data pentru totdeauna: cate <b>coltare C2</b>, suruburi <b>inox 5×60</b>, <b>6×80</b> si <b>6×100</b> au mai ramas. '
  'Ce ai deja scade din lista de la E2 — si tot aici afli daca ai cele 8 vincluri pentru E0.</p>',
  None),
 ('Cioata de 1,5 m → masuta',
  '<p>Se retează la <b>600–750</b> si primeste un blat. 10 minute cu fierastraul electric (JR3070CT).</p>'
  '<p>Motivul e in desen: la 1500, varful ei ajunge la <b>138 mm sub muchia viitoare a acoperisului</b>. '
  'Ca butuc te catari greu pe el. Ca masuta devine o treapta plata, la fix — si de acolo se urca pe Onduline, '
  'care nu tine greutate. Cadere ~1,9 m pe terasa, iar terasa n-are inca balustrada.</p>',
  GH['e1_cioata']),
 ('Scara mobila jos',
  '<p>Culcata, intre orice doua zile de lucru. Cat timp sta rezemata, puntea e accesibila copiilor si n-are balustrada.</p>',
  None),
])}

<div class="ok"><b>E bine daca:</b> nicio gaura fara surub pe scandurile late · stiu cate piese am pe stoc · cioata e la 600–750 · scara e jos.</div>
'''))

# ══════════════════════════════ E2 ══════════════════════════════
CH.append(dict(id='e2', n='E2', titlu='Drumul la Leroy',
    sub='Un singur magazin, un singur drum. Colosseum.',
    zi='o jumatate de zi', body='''
<p class="lead">Lista completa, cu linkuri si casute de bifat, e in <code>LISTA-LEROY-2026-08-17</code>. Aici e doar ce s-a schimbat si ce trebuie intrebat la fata locului.</p>

<div class="stop">
<b>Intrebarea care schimba tot:</b> la raionul de lemn — <b>taiati pe lungime?</b> (nu la capat, in lung). Daca da, ceri fasii de 100 mm din dulapii de 46×250 si scapi complet de E3. Daca nu, tai tu acasa, cu ghidaj.
</div>

<div class="need">
<h4>Ce s-a schimbat fata de lista veche</h4>
<table class="t">
<tr><th>Articol</th><th>Cat</th><th>De ce</th></tr>
<tr><td>Dulap nerindeluit 46×250×4000</td><td class="q">5</td><td>inlocuieste cele 20 de scanduri de 22×100 — se taie in lung in fasii de 100, fara laminare</td></tr>
<tr><td>Placa OSB3 12 mm, 2500×1250</td><td class="q">2</td><td>astereala acoperisului; sub 10° Onduline nu accepta sipci</td></tr>
<tr><td>Lambriu 12,5×96, pachet 2,88 m²</td><td class="q">6</td><td>era 5; peretii laterali sunt mult mai lungi decat in planul vechi</td></tr>
<tr><td>Rigla 46×46×3000</td><td class="q">10</td><td>era 20; fasiile de rest din dulapi acopera jumatate din verticale</td></tr>
<tr><td>Vinclu 90×65</td><td class="q">64</td><td>era 52; +8 pentru colturile din spate, +4 la stalpii din fata</td></tr>
<tr><td>Surub dulgherie 8×140</td><td class="q">36</td><td>era 16; +20 la blocajele de colt</td></tr>
</table>
</div>

<div class="gate">
<b>Ordinea in magazin:</b> intai <b>cuiele de Onduline</b> — la ultima verificare mai era <b>un singur set</b>. Daca s-a dus, iei suruburi de acoperis cu saiba de cauciuc din acelasi raion. Apoi placile: rosu erau 15, maro 153 si mai ieftin cu ~6 lei bucata.
</div>

<div class="ok"><b>E bine daca:</b> tot ce e pe lista e bifat la casa · cuiele de Onduline sunt in portbagaj · stii daca taie in lung sau nu.</div>
'''))

# ══════════════════════════════ E3 ══════════════════════════════
CH.append(dict(id='e3', n='E3', titlu='Fasiile',
    sub='Din dulapi de 250 ies barele de rama. Se sare peste, daca a taiat magazinul.',
    zi='o dupa-amiaza', body=f'''
<p class="lead">Rama peretilor si lemnele acoperisului cer o sectiune de aproximativ <b>46×100</b>. Leroy nu are asa ceva — gama sare de la 46×46 direct la 46×250. Deci o faci din dulapul de 250, taiat in lung.</p>

{fig(D2['taiere'], 'Sectiune prin dulap. Doua fasii de 100 pentru rama si capriori, una de ~42 care inlocuieste rigla la verticale.')}

{steps([
 ('Pregatesti ghidajul',
  '<p>O rigla dreapta prinsa cu cleme pe dulap, paralela cu marginea, la distanta corecta fata de talpa circularului. '
  '<b class="bad">Nu taia din ochi.</b> Patru metri de taietura care fuge cu 3 mm inseamna o fasie de aruncat.</p>'
  '<p class="tool">Masina: <b>HS7611K</b>, adancime de taiere reglata la ~50 mm.</p>',
  None),
 ('Doua taieturi per dulap',
  '<p>Prima la 100 de la margine, a doua la inca 100. Ce ramane — o fasie de ~42 — nu e rest, e material: '
  'are aproape aceeasi sectiune ca rigla de 46×46 si intra la verticale.</p>'
  '<p><b>5 dulapi × 2 taieturi = 10 taieturi de 4 m.</b> Rezultat: 10 fasii de 100 (9 necesare + 1 rezerva) si 5 fasii de ~42.</p>',
  None),
 ('Stivuiesti plat si astepti',
  '<p>Lemnul masiv taiat in lung <b>elibereaza tensiuni interne</b> si se poate arcui. O fasie de 4 m se misca vizibil in cateva zile.</p>'
  '<p>Le stivuiesti <b>plat, cu distantieri intre ele</b>, la umbra, si le lasi cateva zile inainte sa le folosesti. '
  'Cele care se arcuiesc mai tare le tai in piese scurte — inchideri, praguri — unde arcuirea nu conteaza.</p>',
  None),
 ('Cei doi dulapi de rezerva ai tai',
  '<p>Tot acum, cat ai ghidajul prins: cele doua bare de <b>200×50×4000</b> ramase se taie in lung in <b>3 fasii de ~65×50</b> fiecare. '
  'Ies 6 fasii, ~24 m — inca material pentru verticale.</p>'
  '<p class="small">Sugestie: taie <b>una singura</b> intai si vezi cum se comporta. A doua o lasi intreaga — e singura ta rezerva de sectiune mare daca se rupe ceva.</p>',
  None),
])}

<div class="ok"><b>E bine daca:</b> ai 10 fasii de 100 drepte si de aceeasi latime · sunt stivuite plat, la umbra · fasiile de rest sunt puse deoparte, nu aruncate.</div>
'''))

# ══════════════════════════════ E4 ══════════════════════════════
CH.append(dict(id='e4', n='E4', titlu='Peretele din spate',
    sub='Singurul perete care se face complet jos, pe iarba. Dupa ridicare nu mai ajungi la el.',
    zi='o zi', body=f'''
<p class="lead">Intre peretele din spate si gard raman <b>30 cm</b>. Ce nu e gata cand il ridici — scanduri, vopsea, suruburi — ramane asa pentru totdeauna. De asta se face complet jos.</p>

<h3>Ce tai</h3>
<table class="t">
<tr><th>Piesa</th><th>Din ce</th><th>Taiat la</th><th class="q">Buc</th></tr>
<tr><td>Talpa + cununa</td><td>fasie 46×100</td><td class="mono">1990</td><td class="q">2</td></tr>
<tr><td>Lemnele verticale</td><td>rigla 46×46 sau fasie de rest</td><td class="mono">1608</td><td class="q">5</td></tr>
<tr><td>Proptelele din colturi</td><td>rigla 46×46</td><td class="mono">2× 424 (jos) + 2× 212 (sus)</td><td class="q">4</td></tr>
<tr><td>Scandurile (lambriul)</td><td>12,5×96</td><td class="mono">randuri de ~1990</td><td class="q">~4,3 m²</td></tr>
</table>
<p class="why-inline"><b>1990</b> = distanta libera masurata intre stalpii de 4 m (1995) minus 5 mm joc de montaj. Peretele se strecoara <em>intre</em> stalpi — la cota exacta nu intra.<br>
<b>1608</b> = 1700 minus cele doua talpi de 46. Peretele trebuie sa iasa exact 1700, ca scandura groasa de deasupra sa calce si pe el, si pe capetele stalpilor.</p>

{fig(D2['spate'], 'Elevatie la scara, din exterior. Verticalele la ~498, proptele lungi jos si scurte sus.')}

{steps([
 ('Rama pe iarba',
  '<p>Talpa si cununa paralele. Insemnezi pe <b>amandoua</b> unde vin verticalele: <span class="mono">0 · 498 · 995 · 1493 · 1990</span>.</p>'
  '<p>Prinzi cele 5 verticale cu cate 2 suruburi prin talpa si 2 prin cununa, <b>cu gaura de 4 mm data inainte</b> — capetele de rigla crapa altfel.</p>',
  None),
 ('Diagonalele — inainte de orice altceva',
  '<p>Masori ambele diagonale ale ramei. Trebuie sa fie egale, <b>voie 3 mm</b>. Corectezi acum, impingand de colturi.</p>'
  '<p class="why-inline">Proptelele ingheata forma exact cum o gasesc. Daca rama e stramba cand le pui, ramane stramba, si se vede la lambriu.</p>',
  None),
 ('Proptelele',
  '<p>Jos cele de 424, sus cele de 212. Cate 2 suruburi 6×120 la fiecare capat.</p>',
  None),
 ('Vopsea, apoi scandurile',
  '<p>Vopsea de protectie pe <b>toate fetele</b> scandurilor, inclusiv cele care nu se mai vad niciodata. Apoi lambriul, cat peretele e culcat: primul rand jos, fiecare rand calca 2 cm peste cel de sub el, un surub in fiecare verticala.</p>',
  None),
 ('Ridicarea — pasul periculos',
  '<p>Panoul are <b>2,0 × 1,7 m</b> si cantareste <b>~50 kg</b> cu lambriu si vopsea. Trebuie sa ajunga de pe iarba pe punte, la <b>2,2 m</b>. Puntea nu are inca balustrada.</p>'
  '<ul>'
  '<li><b>Zi fara vant.</b> Panoul e o suprafata de vela de 3,4 m².</li>'
  '<li><b>Doi adulti.</b> Unul jos impinge, unul sus trage. Nu se face singur.</li>'
  '<li><b>Doua scanduri ca rampa</b>, sprijinite de marginea puntii. Panoul urca pe cant, alunecand, nu ridicat pe brate.</li>'
  '<li><b>O franghie</b> legata de stalpul de 4 m si de rama. Daca scapa, nu pleaca peste margine.</li>'
  '<li><b>Copiii nu sunt pe punte</b> si nu sunt sub panou.</li>'
  '</ul>',
  GH['e4_ridicare']),
 ('Prinderea de stalpi',
  '<p><b>4 suruburi de dulgherie 8×140</b> pe fiecare capat, in stalpii de 4 m: unul jos, doua pe mijloc, unul sus. '
  '<b>Gaura de 6 mm data inainte in stalp.</b></p>',
  D2['prindere']),
 ('Talpa in grinzi',
  '<p>Prin podea, in grinzile de dedesubt: <b>surub 6×140 la fiecare 40 cm</b>, pe liniile trase cu creta. Plus coltare metalice pe interior.</p>'
  '<p class="why-inline">Scandurile podelei au doar 28 mm — nu tin nimic singure. Tot ce se prinde de podea trebuie sa intre in grinda de dedesubt. La colturile din spate, in blocajele facute la E0.</p>',
  None),
])}

<div class="ok"><b>E bine daca:</b> diagonalele au fost egale la asamblare · 8 suruburi groase in stalpi · talpa prinsa in grinzi pe toata lungimea, inclusiv la colturi · scandurile complete si vopsite pe toate fetele · peretele nu atinge gardul nicaieri.</div>

<div class="gate"><b>Urmeaza:</b> peretii laterali, tot pe punte. Dar aia e alt capitol — ghidul asta se opreste aici, ca sa vedem intai daca formatul e bun.</div>
'''))

# ══════════════════════════════ HTML ══════════════════════════════
nav = '\n'.join(f'<li><a href="#{c["id"]}"><span class="cn">{c["n"]}</span>{c["titlu"]}<em>{c["zi"]}</em></a></li>' for c in CH)
secs = '\n'.join(f'''<section id="{c['id']}">
<header class="ch"><div class="cn-big">{c['n']}</div><h2>{c['titlu']}</h2><p class="chsub">{c['sub']}</p><span class="zi">{c['zi']}</span></header>
{c['body']}
</section>''' for c in CH)

HTML = f'''<!DOCTYPE html>
<html lang="ro"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ghid de constructie — casa de sus</title>
<style>
:root{{
 --bg:#faf9f6; --card:#fff; --ink:#1c1b18; --mut:#6b675e; --dim:#8f8b83; --line:#e2ddd3;
 --acc:#14532d; --acc-s:#eef4ef; --acc2:#8a3016; --acc2-s:#fdf3ee; --warn-s:#fdf8ec; --warn:#8a6b16;
 --mono:ui-monospace,"SF Mono",Menlo,monospace;
 --sans:"Helvetica Neue",Helvetica,Arial,sans-serif;
 --serif:"Iowan Old Style",Georgia,serif;
}}
html[data-t="dark"]{{
 --bg:#16161a; --card:#1d1d22; --ink:#e9e7e2; --mut:#8e8a82; --dim:#6a675f; --line:#2e2e36;
 --acc:#6fbf95; --acc-s:#18211c; --acc2:#e0834f; --acc2-s:#221a15; --warn-s:#221e14; --warn:#d9b45e;
}}
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0;background:var(--bg);color:var(--ink);font:16px/1.65 var(--sans)}}
img,svg{{max-width:100%}}

.wrap{{display:grid;grid-template-columns:264px 1fr;gap:0;max-width:1280px;margin:0 auto}}
nav{{position:sticky;top:0;align-self:start;height:100vh;overflow-y:auto;padding:34px 22px 60px;border-right:1px solid var(--line)}}
nav .brand{{font:600 11px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin-bottom:6px}}
nav h1{{font:600 21px/1.25 var(--sans);letter-spacing:-.01em;margin:0 0 4px}}
nav .meta{{font:11px/1.5 var(--mono);color:var(--dim);margin-bottom:24px}}
nav ol{{list-style:none;margin:0;padding:0}}
nav li a{{display:block;padding:11px 12px;border-radius:9px;text-decoration:none;color:var(--ink);font-size:14.5px;line-height:1.35}}
nav li a:hover{{background:var(--acc-s)}}
nav li a.on{{background:var(--acc-s);box-shadow:inset 3px 0 0 var(--acc)}}
nav .cn{{display:block;font:600 10px/1 var(--mono);letter-spacing:.14em;color:var(--acc);margin-bottom:3px}}
nav li a em{{display:block;font:italic 12px/1.4 var(--serif);color:var(--dim);margin-top:2px}}
.prog{{margin-top:22px;padding-top:18px;border-top:1px solid var(--line);font:11px/1.6 var(--mono);color:var(--dim)}}
.bar{{height:5px;border-radius:3px;background:var(--line);margin-top:7px;overflow:hidden}}
.bar i{{display:block;height:100%;background:var(--acc);width:0;transition:width .25s}}
.tgl{{margin-top:16px;font:11px var(--mono);color:var(--dim);background:none;border:1px solid var(--line);
 border-radius:7px;padding:6px 10px;cursor:pointer}}

main{{padding:34px 46px 140px;min-width:0}}
@media(max-width:900px){{
 .wrap{{grid-template-columns:1fr}}
 nav{{position:static;height:auto;border-right:none;border-bottom:1px solid var(--line);padding:22px}}
 main{{padding:22px 18px 90px}}
}}

section{{scroll-margin-top:14px;padding-bottom:44px;margin-bottom:44px;border-bottom:1px solid var(--line)}}
section:last-child{{border-bottom:none}}
header.ch{{margin-bottom:22px}}
.cn-big{{font:600 12px/1 var(--mono);letter-spacing:.2em;color:var(--acc)}}
header.ch h2{{font:600 34px/1.15 var(--sans);letter-spacing:-.02em;margin:8px 0 8px}}
.chsub{{font:italic 17px/1.5 var(--serif);color:var(--mut);margin:0;max-width:60ch}}
.zi{{display:inline-block;margin-top:12px;font:11px var(--mono);letter-spacing:.08em;text-transform:uppercase;
 color:var(--mut);border:1px solid var(--line);border-radius:999px;padding:5px 11px}}

h3{{font:600 13px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--acc);margin:36px 0 12px}}
h4{{font:600 17px/1.35 var(--sans);margin:0 0 8px}}
p{{margin:0 0 12px;max-width:70ch}}
.lead{{font-size:17px;color:var(--mut);max-width:66ch}}
.small{{font-size:13.5px;color:var(--mut)}}
code{{font:13.5px var(--mono);background:var(--acc-s);padding:2px 6px;border-radius:5px}}
.mono{{font-family:var(--mono)}}
b.bad{{color:var(--acc2)}}

figure{{margin:20px 0;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px;overflow:hidden}}
figure svg{{display:block;margin:0 auto;max-height:480px}}
figcaption{{margin-top:14px;font:13px/1.6 var(--mono);color:var(--dim);max-width:74ch}}

ol.steps{{list-style:none;margin:22px 0;padding:0;counter-reset:s}}
ol.steps>li{{display:flex;gap:16px;padding:20px 0;border-top:1px solid var(--line)}}
ol.steps>li:last-child{{border-bottom:1px solid var(--line)}}
.stepbody{{min-width:0;flex:1}}
.stepbody h4::before{{counter-increment:s;content:counter(s) "  ";font-family:var(--mono);color:var(--acc);font-weight:600}}
.stepfig{{margin-top:14px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}}
.stepfig svg{{max-height:400px;display:block;margin:0 auto}}
.tick{{flex:none;cursor:pointer;padding-top:2px}}
.tick input{{position:absolute;opacity:0;width:0;height:0}}
.tick span{{display:block;width:26px;height:26px;border:2px solid var(--line);border-radius:8px;transition:.15s}}
.tick input:checked+span{{background:var(--acc);border-color:var(--acc);
 background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E");
 background-size:18px;background-position:center;background-repeat:no-repeat}}
li.done .stepbody{{opacity:.45}}

.gate,.stop,.ok,.need,.warn,.why{{border-radius:12px;padding:16px 18px;margin:20px 0;font-size:15px}}
.gate{{background:var(--acc-s);border-left:3px solid var(--acc)}}
.stop{{background:var(--acc2-s);border-left:3px solid var(--acc2)}}
.ok{{background:var(--acc-s);border:1px solid var(--line);border-left:3px solid var(--acc)}}
.need{{background:var(--card);border:1px solid var(--line)}}
.need h4{{font:600 11px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--acc);margin-bottom:12px}}
.need ul{{margin:0;padding-left:20px}} .need li{{margin:4px 0}}
.warn{{background:var(--acc2-s);border:1px solid var(--line)}}
.why{{background:var(--card);border:1px solid var(--line)}}
.why-inline{{font:italic 15px/1.6 var(--serif);color:var(--mut);border-left:2px solid var(--line);padding-left:14px;margin:12px 0}}
.tool{{font-size:14.5px;background:var(--warn-s);border-radius:9px;padding:11px 14px}}

table.t{{width:100%;border-collapse:collapse;font-size:14.5px;margin:14px 0}}
table.t th{{text-align:left;font:600 10.5px/1 var(--sans);letter-spacing:.13em;text-transform:uppercase;
 color:var(--dim);padding:0 10px 10px 0;border-bottom:1px solid var(--line)}}
table.t td{{padding:10px 10px 10px 0;border-bottom:1px solid var(--line);vertical-align:baseline}}
table.t .q{{font-family:var(--mono);text-align:right;white-space:nowrap}}
table.t td.mono{{font-family:var(--mono)}}
footer.doc{{margin-top:50px;font:12px/1.7 var(--mono);color:var(--dim)}}
</style></head><body>
<div class="wrap">
<nav>
 <div class="brand">Casuta din copac</div>
 <h1>Ghid de constructie<br>casa de sus</h1>
 <div class="meta">20 august 2026 · cote in mm<br>geometrie masurata pe santier</div>
 <ol>{nav}</ol>
 <div class="prog">progres <span id="pt">0 / 0</span><div class="bar"><i id="pb"></i></div></div>
 <button class="tgl" onclick="tt()">lumina / intuneric</button>
</nav>
<main>
{secs}
<footer class="doc">
GHID-CONSTRUCTIE-casa · 20.08.2026 · E0–E4<br>
Cotele vin din masuratorile de santier confirmate pe 20.08 (<code>MASURATORI-CONFIRMARE-2026-08-20</code>).<br>
Referinta completa: <code>PROIECT-CASA-2026-08-17</code> · desene la scara: <code>SCHEME-CASA-2026-08-17</code> · cumparaturi: <code>LISTA-LEROY-2026-08-17</code>.<br>
Bifele se pierd la reincarcarea paginii — sunt pentru o sesiune de lucru, nu pentru evidenta.
</footer>
</main>
</div>
<script>
function tt(){{const h=document.documentElement;h.dataset.t = h.dataset.t==='dark'?'':'dark';}}
const boxes=[...document.querySelectorAll('.tick input')];
function upd(){{
 const n=boxes.filter(b=>b.checked).length;
 document.getElementById('pt').textContent=n+' / '+boxes.length;
 document.getElementById('pb').style.width=(boxes.length?100*n/boxes.length:0)+'%';
}}
boxes.forEach(b=>b.addEventListener('change',()=>{{b.closest('li').classList.toggle('done',b.checked);upd();}}));
upd();
const links=[...document.querySelectorAll('nav a')];
const secs=links.map(a=>document.querySelector(a.getAttribute('href')));
new IntersectionObserver(es=>{{
 es.forEach(e=>{{ if(e.isIntersecting){{
   links.forEach(l=>l.classList.remove('on'));
   const i=secs.indexOf(e.target); if(i>=0) links[i].classList.add('on');
 }}}});
}},{{rootMargin:'-10% 0px -75% 0px'}}).observe.length;
const obs=new IntersectionObserver(es=>{{
 es.forEach(e=>{{ if(e.isIntersecting){{
   links.forEach(l=>l.classList.remove('on'));
   const i=secs.indexOf(e.target); if(i>=0) links[i].classList.add('on');
 }}}});
}},{{rootMargin:'-10% 0px -75% 0px'}});
secs.forEach(s=>s&&obs.observe(s));
</script>
</body></html>'''

open('GHID-CONSTRUCTIE-casa.html','w',encoding='utf-8').write(HTML)
print('scris', len(HTML), 'caractere')
