#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asambleaza GHID-CONSTRUCTIE-casa.html — documentul de executie al casei.
8 capitole (E0-E7), cuprins lateral, bon de taiere si scule per capitol,
strat interactiv (localStorage, progres pe capitol, poarta e0->e3, reset)."""
import json

GH = json.load(open('figs_ghid.json'))
D2 = json.load(open('figs_2d.json'))

def fig(svg, cap='', wide=False):
    c = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure class="{"wide" if wide else ""}">{svg}{c}</figure>'

def steps(items):
    out=['<ol class="steps">']
    for (titlu, corp, svg) in items:
        s = f'<div class="stepfig">{svg}</div>' if svg else ''
        out.append(f'<li><label class="tick"><input type="checkbox" class="bx step"><span></span></label>'
                   f'<div class="stepbody"><h4>{titlu}</h4>{corp}{s}</div></li>')
    out.append('</ol>')
    return '\n'.join(out)

def bon(rows):
    head='<tr><th></th><th>Piesa</th><th>Din ce</th><th>Cota (mm)</th><th class="q">Buc</th></tr>'
    trs=[]
    for (piesa,din,cota,buc) in rows:
        trs.append(f'<tr><td class="bc"><label class="tick sm"><input type="checkbox" class="bx bon"><span></span></label></td>'
                   f'<td>{piesa}</td><td>{din}</td><td class="mono">{cota}</td><td class="q">{buc}</td></tr>')
    return (f'<details class="bon"><summary>Bon de taiere — {len(rows)} piese · se taie tot inainte de asamblat</summary>'
            f'<table class="t bontab">{head}{"".join(trs)}</table></details>')

CH = []

# ══════════════════════════════ E0 ══════════════════════════════
CH.append(dict(id='e0', n='E0', titlu='Scandura care lipseste',
    sub='Golul de la cele doua colturi din spate. Patru locuri identice.',
    zi='2–3 ore',
    scule='GSR — gaura pilot 6 mm + suruburile scurte (ambreiaj) · GDR — cele 8×140 in grinda si stalp · fierastrau sabie pentru blocaj',
    body=f"""
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
    zi='2–3 ore',
    scule='GSR — suruburile inox 5×60 (ambreiaj 8–12, T25, NU impact) · fierastrau sabie JR3070CT — cioata',
    body=f'''
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
    zi='o jumatate de zi',
    body=f'''
<p class="lead">Lista completa, cu linkuri si casute de bifat, e in <code>LISTA-LEROY-2026-08-17</code>. Aici e doar ce s-a schimbat si ce trebuie intrebat la fata locului.</p>

<div class="gate">
<b>Decizia de material (20.08):</b> rama tuturor peretilor se face din <b>rigla 48×48×4000, cumparata gata — 13 bucati</b>. Nu se mai taie niciun dulap in lung, nu se mai lamineaza nimic pentru pereti. Panoul din spate scade de la ~50 la <b>~32-41 kg</b> — se ridica mai usor in doi, pe punte fara balustrada.
</div>

<div class="need">
<h4>Ce s-a schimbat fata de lista veche</h4>
<table class="t">
<tr><th>Articol</th><th>Cat</th><th>De ce</th></tr>
<tr><td>Rigla 48×48×4000 <b>(nou)</b></td><td class="q">13</td><td>rama tuturor peretilor: talpi, cununi, verticale, contrafise. 29,90 lei/buc = <b>388,70 lei</b></td></tr>
<tr><td>Scandura 22×100×4000</td><td class="q">6</td><td>era 20; acum <b>doar pentru capriori</b> (raman laminati 44×100). 5 capriori × 1889, doi pe bara → 3 bare = 6 scanduri</td></tr>
<tr><td>Placa OSB3 12 mm, 2500×1250</td><td class="q">2</td><td>astereala acoperisului; sub 10° Onduline nu accepta sipci</td></tr>
<tr><td>Lambriu 12,5×96, pachet 2,88 m²</td><td class="q">6</td><td>imbraca toti peretii</td></tr>
<tr><td>Vinclu 90×65</td><td class="q">64</td><td>colturi, capriori, blocajele din spate, stalpii din fata</td></tr>
<tr><td>Surub dulgherie 8×140</td><td class="q">36</td><td>peretele din spate in stalpi + blocajele de colt + stalpii din fata</td></tr>
</table>
<p class="small">Rigla de <b>46×46×3000</b> ramane pe lista doar pentru <b>tocurile geamurilor si pragurile</b> — verticalele si proptelele au trecut pe rigla de 48×48, deci cantitatea de 46×46 e acum probabil prea mare. Vezi nota din <code>LISTA-LEROY</code>.</p>
</div>

<div class="gate">
<b>Ordinea in magazin:</b> intai <b>cuiele de Onduline</b> — la ultima verificare mai era <b>un singur set</b>. Daca s-a dus, iei suruburi de acoperis cu saiba de cauciuc din acelasi raion. Apoi placile: rosu erau 15, maro 153 si mai ieftin cu ~6 lei bucata.
</div>

{steps([
 ('Cele 13 rigle de 48×48',
  '<p>Rama tuturor peretilor. Le numeri inainte sa pleci — sunt piesa noua, e usor sa le uiti.</p>', None),
 ('Cuiele de Onduline, primele',
  '<p>Mai era un singur set. Daca s-a dus, iei suruburi de acoperis cu saiba de cauciuc din acelasi raion.</p>', None),
 ('Restul listei, bifat la casa',
  '<p>Tot ce e in <code>LISTA-LEROY-2026-08-17</code>, cu masuratorile M2–M5 facute inainte (lambriul se ia pe masuratori reale).</p>', None),
])}

<div class="ok"><b>E bine daca:</b> cele 13 rigle de 48×48 sunt in masina · tot ce e pe lista e bifat la casa · cuiele de Onduline sunt in portbagaj.</div>
'''))

# ══════════════════════════════ E3 · peretele din spate ══════════════════════════════
CH.append(dict(id='e3', n='E3', titlu='Peretele din spate',
    sub='Singurul perete care se face complet jos, pe iarba. Dupa ridicare nu mai ajungi la el.',
    zi='o zi',
    scule='HS7611K — rigla si dulapul la lungime · GSR — gauri pilot 4 mm + suruburile · GDR — cele 8×140 in stalpi · doi oameni la ridicare',
    blocat_de='e0',
    blocat_motiv='talpa peretelui din spate se prinde prin podea, in grinzile de dedesubt, la fiecare 40 cm. Exact la colturi nu are in ce sa intre. Dupa ce peretele e ridicat, la coltul ala nu se mai ajunge niciodata. Deci golul din colt (E0) se inchide inainte.',
    bon=[
     ('Talpa + cununa','rigla 48×48','1990','2'),
     ('Verticale','rigla 48×48','1604','5'),
     ('Contrafise colturi','rigla 48×48 (rest)','2× 424 jos · 2× 212 sus','4'),
     ('Reazemul din spate','dulap 200×50 (il ai)','2200','1'),
     ('Lambriu','12,5×96','randuri de ~1990','~4,3 m²'),
    ],
    body=f'''
<p class="lead">Intre peretele din spate si gard raman <b>30 cm</b>. Ce nu e gata cand il ridici — scanduri, vopsea, suruburi — ramane asa pentru totdeauna. De asta se face complet jos, pe iarba, si abia apoi se urca pe punte.</p>

{fig(D2['spate'], 'Elevatie la scara, din exterior. Cinci verticale de 1604, talpa si cununa de 1990, proptele in colturi.')}

{steps([
 ('Rama pe iarba',
  '<p>Talpa si cununa (rigla 48×48, taiate la <b>1990</b>) paralele. Insemnezi pe amandoua unde vin cele 5 verticale: <span class="mono">0 · 498 · 995 · 1493 · 1990</span>.</p>'
  '<p>Verticalele sunt rigla 48×48 taiata la <b>1604</b> (= 1700 − doua talpi de 48). Le prinzi cu cate 2 suruburi prin talpa si 2 prin cununa, <b>cu gaura de 4 mm data inainte</b> — capetele de rigla crapa altfel.</p>', None),
 ('Diagonalele — inainte de orice altceva',
  '<p>Masori ambele diagonale ale ramei. Trebuie egale, <b>voie 3 mm</b>. Corectezi acum, impingand de colturi.</p>'
  '<p class="why-inline">Proptelele ingheata forma exact cum o gasesc. Daca rama e stramba cand le pui, ramane stramba, si se vede la lambriu.</p>', None),
 ('Proptelele din colturi',
  '<p>Din restul de rigla 48×48: jos brate de 300 (taiate la <b>424</b> pe diagonala), sus brate de 150 (taiate la <b>212</b>). Cate 2 suruburi 6×120 la fiecare capat.</p>', None),
 ('Vopsea, apoi lambriul',
  '<p>Vopsea de protectie pe <b>toate fetele</b> scandurilor, inclusiv cele care nu se mai vad niciodata. Apoi lambriul, cat peretele e culcat: primul rand jos, fiecare rand calca 2 cm peste cel de sub el, un surub in fiecare verticala.</p>', None),
 ('Ridicarea — pasul periculos',
  '<p>Panoul cantareste <b>~32-41 kg</b> cu lambriu si vopsea. Trebuie sa ajunga de pe iarba pe punte, la <b>2,2 m</b>. Puntea <b>nu are balustrada</b> — margine libera pe toate laturile, tot capitolul.</p>'
  '<ul>'
  '<li><b>Zi fara vant.</b> Panoul e o suprafata de vela de 3,4 m².</li>'
  '<li><b>Doi adulti,</b> nu unul.</li>'
  '<li>Panoul urca <b>culcat, pe muchia lunga</b>, sprijinit pe marginea puntii, apoi se roteste in picioare pe punte.</li>'
  '<li>Se <b>leaga provizoriu de stalpi</b> inainte sa i se dea drumul din maini.</li>'
  '<li><b>Copiii nu sunt pe punte</b> si nu sunt sub panou.</li>'
  '</ul>',
  GH['e4_ridicare']),
 ('Prinderea de stalpi',
  '<p><b>4 suruburi de dulgherie 8×140</b> pe fiecare capat, in stalpii de 4 m: unul jos, doua pe mijloc, unul sus. <b>Gaura de 6 mm data inainte in stalp.</b></p>',
  D2['prindere']),
 ('Reazemul din spate',
  '<p>Dulapul de <b>200×50</b> (il ai deja), taiat la <b>2200</b>, se aseaza <b>pe muchie, cu 200 in sus</b>, peste cununa peretelui SI peste capetele stalpilor — ambele la 1700 — ca sa faca un reazem continuu la <b>1900</b>. Fixat cu <b>vinclu 90×65 pe ambele fete, la ~500 mm</b> + o placa metalica pe fiecare stalp.</p>',
  D2['reazem']),
 ('Talpa in grinzi',
  '<p>Prin podea, in grinzile de dedesubt: <b>surub 6×140 la fiecare 40 cm</b>, pe liniile trase cu creta. Plus coltare metalice pe interior.</p>'
  '<p class="why-inline">Scandurile podelei au doar 28 mm — nu tin nimic singure. La colturile din spate, talpa se prinde in <b>blocajele facute la E0</b>. De aia E0 e obligatoriu inainte.</p>', None),
])}

<div class="ok"><b>E bine daca:</b> diagonalele au fost egale la asamblare · 8 suruburi groase in stalpi · reazemul de 200×50 calca si pe cununa si pe stalpi · talpa prinsa in grinzi pe toata lungimea, inclusiv la colturi · scandurile complete si vopsite pe toate fetele · peretele nu atinge gardul nicaieri.</div>
'''))

# ══════════════════════════════ E4 · peretii laterali ══════════════════════════════
CH.append(dict(id='e4', n='E4', titlu='Peretii laterali',
    sub='Doi pereti, fiecare pe cota lui. Se asambleaza pe punte — sunt prea lungi ca sa fie urcati gata.',
    zi='o zi',
    scule='HS7611K — rigla la lungime · GSR — gauri pilot + suruburi + tocul geamului · fierastrau vertical PST 700 E — golul de geam',
    bon=[
     ('Talpa','rigla 48×48','1580 stanga · 1570 dreapta','2'),
     ('Cununa inclinata','rigla 48×48','1596 stanga · 1586 dreapta','2'),
     ('Verticale','rigla 48×48','1573 · 1645 · 1722 · 1794','4 / perete'),
     ('Prag + buiandrug geam','rigla 48×48 (rest)','intre verticalele golului','2 / perete'),
     ('Contrafise','rigla 48×48 (rest)','4× 212 (brat 150)','4 / perete'),
     ('Toc geam','rigla 46×46','gol 490 · geam 440×440','1 / perete'),
     ('Geam fix','plexi 4 mm','440×440','2 total'),
     ('Lambriu','12,5×96','randuri','~m²'),
    ],
    body=f'''
<p class="lead">Cununa e inclinata — acoperisul urca spre spate — deci fiecare din cele 4 verticale are alta lungime. Cele doua laterale difera intre ele cu 10 mm: nu le taia dupa acelasi tipar.</p>

{fig(D2['lateral'], 'Elevatie la scara. Fata in stanga (mai jos), spate in dreapta (mai sus). Golul de geam centrat, 490×490, prag la 950.')}

<div class="gate"><b>Dreptunghiul casei nu e la echer</b> — e in afara cu ~20 mm. De aceea peretii sunt trapeze usoare, iar <b>fiecare talpa se taie la fata locului</b>, dupa masura reala dintre stalpi, nu din tabel.</div>

{steps([
 ('Rama, pe punte',
  '<p>Talpa (rigla 48×48): <b>1580</b> pe latura din stanga (S1–S3), <b>1570</b> pe dreapta (S2–S4). Cununa inclinata: <b>1596</b> stanga, <b>1586</b> dreapta.</p>'
  '<p>Cele 4 verticale, dinspre fata spre spate: <b>1573 · 1645 · 1722 · 1794</b>. Sunt diferite intentionat — nu le incurca intre ele. Marcaje pe talpa, de la fata: <span class="mono">0 · 543 · 1033 · pana la capat</span>.</p>', None),
 ('Golul de geam',
  '<p>Centrat: <b>543 camp · 490 gol · 542 camp</b> (campurile se ajusteaza la talpa reala; golul ramane 490). Intre verticalele de la 543 si 1033 pui un <b>prag la 950</b> si un buiandrug deasupra, la 950+490. Aceeasi metoda ca la orice fereastra.</p>', None),
 ('Echerul si contrafisele',
  '<p>Verticalele perpendiculare pe talpa, cununa la panta ei. Cand forma e buna, pui contrafise in <b>toate cele 4 colturi</b>: rigla 48×48 taiata la <b>212</b> pe diagonala (brat de 150). Cate 2 suruburi 6×120 la capat.</p>', None),
 ('Vopsea si lambriu',
  '<p>Vopsea pe toate fetele, apoi lambriul — la fel ca la spate. Golul de geam ramane liber.</p>', None),
 ('Tocul geamului',
  '<p>In golul de 490 intra un <b>toc separat</b> din rigla 46×46, iar geamul fix de <b>440×440</b> (plexi de 4 mm) se prinde cu <b>sipci pe ambele fete</b>. Gaurile in plexi se dau cu <b>+1 mm</b> fata de surub — altfel plexiul crapa la strans. Geamul propriu-zis se monteaza la E7, din exterior.</p>', None),
 ('Prinderea peretelui',
  '<p>Talpa in grinzile de dedesubt: <b>6×140 la fiecare 40 cm</b>. La colturi, unde se intalneste cu peretele din spate si cu cel din fata: cate <b>2 vincluri 100×90 pe colt</b>.</p>', None),
])}

<div class="ok"><b>E bine daca:</b> ambele laterale stau la echer pe podea · golul de geam e 490 curat, cu prag la 950 · contrafise in toate colturile · talpa prinsa in grinzi si colturile in vincluri.</div>

<div class="warn"><p>Al doilea perete lateral are <b>alte cote</b> (talpa 1570, cununa 1586). Nu-l taia dupa primul — masoara-l separat pe latura lui.</p></div>
'''))

# ══════════════════════════════ E5 · peretele din fata ══════════════════════════════
CH.append(dict(id='e5', n='E5', titlu='Peretele din fata',
    sub='Peretele cu usa si fereastra. Doua lucruri se fac altfel: bara de sus e solida, iar usa se taie la final.',
    zi='o zi',
    scule='HS7611K — rigla si bara de sus 100×60 · GSR — gauri pilot + suruburile oblice · fierastrau sabie — taierea talpii la usa, la final',
    bon=[
     ('Talpa (intreaga)','rigla 48×48','1970','1'),
     ('Verticale (jambe + montanti)','rigla 48×48','1552','5'),
     ('Prag + buiandrug fereastra','rigla 48×48 (rest)','570, intre jambe','2'),
     ('Bara de sus','bara solida 100×60 (o ai)','2155','1'),
     ('Contrafise sus','rigla 48×48 (rest)','2× 212 (brat 150)','2'),
     ('Contrafisa jos-dreapta','rigla 48×48 (rest)','~350 (brat 250)','1'),
     ('Fereastra','PVC 56×56 (cumparata)','—','1'),
     ('Lambriu','12,5×96','randuri, fara zona usii','~m²'),
    ],
    body=f'''
<p class="lead">Are doua lucruri care nu mai apar nicaieri: lemnul de sus e o <b>bara solida</b>, nu o rama, iar golul de usa se taie <b>la final</b>, dupa ce peretele e ridicat si legat — altfel isi pierde rigiditatea la transport.</p>

{fig(D2['fata'], 'Elevatie la scara. Cinci verticale de 1552, bara de sus 100×60 peste amandoi stalpii, fereastra la stanga, usa la mijloc.')}

{steps([
 ('Rama — cu talpa INTREAGA',
  '<p>Talpa (rigla 48×48) taiata la <b>1970</b>, <b>necrestata inca pentru usa</b>. Cinci verticale de <b>1552</b> (= 1600 − o singura talpa de 48; sus nu e cununa, e bara solida). Masurate de la fata interioara a stalpului stang: <span class="mono">115 · fereastra 161→731 · usa 938→1488 · montant de camp 1650→1696</span>, plus coltul de <b>274</b> pentru propteaua de jos.</p>', None),
 ('Fereastra',
  '<p>Intre jambe (161→731), gol <b>570×570</b>, cu prag + buiandrug ca la geamurile laterale (inaltimea pragului o vezi pe <code>SCHEME-2D</code>, elevatie fata). Aici intra <b>fereastra PVC de 56×56</b> — singura care se deschide, spre terasa. Se monteaza la E7.</p>', None),
 ('Bara de sus',
  '<p>Nu rama, nu laminat: <b>bara solida 100×60</b> (o ai), cu latura de <b>60 in sus</b>, taiata la <b>2155</b>. Trebuie sa calce pe rama SI pe amandoi stalpii — de aia e mai lunga decat peretele. Nu se inlocuieste cu rigla.</p>', None),
 ('Contrafisele',
  '<p>Sus: <b>2× 212</b> (brat 150). Jos-dreapta: una lunga, <b>~350</b> (brat 250). Jos-stanga <b>se sare</b> — acolo coltul e chiar stalpul de 90×90, deja rigid.</p>', None),
 ('Vopsea, lambriu, ridicare',
  '<p>Vopsea pe toate fetele, lambriu peste tot mai putin zona usii. Apoi se ridica pe punte, ca la spate: doi oameni, culcat pe muchie, legat de stalpi provizoriu.</p>', None),
 ('Prinderea finala a stalpilor',
  '<p>La fiecare stalp din fata: <b>4 suruburi de dulgherie 8×140</b> infiletate <b>oblic, la ~15-20°</b>, in grinda de dedesubt (2 de-o parte, 2 de cealalta) + <b>un coltar 90×65 pe fiecare fata</b> a stalpului. Tot de sus, <b>fara piulite</b>.</p>'
  '<p class="why-inline">Nu exista tije M12 in podea si nu au existat niciodata. Nu cauta gauri de bulon — nu sunt.</p>', None),
 ('Usa — abia acum',
  '<p>Dupa ce peretele e ridicat, legat si <b>verificat la echer</b>: tai talpa pentru usa. Gol de <b>550</b> latime, care lasa <b>1600 liber</b>.</p>'
  '<p class="why-inline">Daca tai talpa mai devreme, peretele se indoaie la transport si la ridicare. Talpa intreaga il tine drept pana sus.</p>', None),
])}

<div class="ok"><b>E bine daca:</b> talpa a stat intreaga pana dupa ridicare · bara de sus calca pe amandoi stalpii · stalpii prinsi cu 4 suruburi oblice + coltar fiecare, fara tije · golul de usa taiat la final, 550 latime, 1600 liber.</div>
'''))

# ══════════════════════════════ E6 · acoperisul ══════════════════════════════
CH.append(dict(id='e6', n='E6', titlu='Acoperisul',
    sub='Cinci lemne inclinate, doua placi de OSB, trei placi de Onduline. Sub 10° nu merg sipci.',
    zi='o zi',
    scule='HS7611K — capriorii si placile OSB · GDR/GSR — laminarea (4×40) + OSB (4×45) · suruburi de acoperis cu saiba (GSR) sau cuie cu capac pentru Onduline',
    bon=[
     ('Capriori (laminati)','2× scandura 22×100','1889','5'),
     ('Inchideri intre capriori','scandura (rest)','454','4'),
     ('Astereala','OSB3 12 mm','2200×1250 + 2200×639','2 placi'),
     ('Invelitoare','Onduline 2000×860','intregi, nu se taie','3'),
    ],
    body=f'''
<p class="lead">Panta reala e <b>8,2°</b> — sub 10°, deci acoperisul merge pe <b>astereala continua de OSB</b>, nu pe sipci. Placa de OSB tine si bracajul, singura.</p>

{fig(D2['acoperis'], 'Plan acoperis. Cinci capriori in dreptul verticalelor, doua placi de OSB, inchideri de 454 intre capriori.')}

{steps([
 ('Lamineaza capriorii — singurul lemn laminat',
  '<p>Capriorii sunt <b>44×100</b>, facuti din <b>2 scanduri de 22×100</b> insurubate una peste alta cu <b>4×40 in zigzag la 300 mm</b>. 5 capriori de <b>1889</b> lungime → din cele 6 scanduri (3 bare laminate).</p>'
  '<p class="why-inline">Capriorii NU trec pe rigla 48×48 — sectiunea patrata s-ar indoi la spanul de 1670. Aici, si numai aici, se lamineaza.</p>', None),
 ('Aseaza capriorii',
  '<p>Pas <b>498</b> intre ei, in dreptul verticalelor din pereti. <b>Orientarea conteaza: 100 pe verticala, 44 pe orizontala.</b> Pus invers, capriorul lucreaza pe axa slaba. Fiecare capat: <b>2 vincluri 90×65</b>.</p>', None),
 ('Inchiderile',
  '<p>Intre capriori, la capete, pui inchideri scurte de <b>454</b> (= 498 − 44). Tin capriorii la distanta si inchid streasina.</p>', None),
 ('Astereala de OSB',
  '<p><b>2 placi OSB3 de 12 mm</b>, taiate la <b>2200×1250</b> si <b>2200×639</b>. Insurubate in capriori cu <b>4×45 la ~250 mm</b>. Placa asta e si bracajul acoperisului — de aia nu mai exista nicio sipca in diagonala.</p>', None),
 ('Onduline',
  '<p><b>3 placi, una langa alta, intregi.</b> Panta masoara 1889, placa are 2000 — nu se taie nimic pe lungime. Streasina <b>100</b> in fata si <b>100</b> in spate. Prinderea: cuie cu capac SAU suruburi de acoperis cu saiba de cauciuc, <b>numai pe varful valului</b> — in adancitura curge apa, fiecare gaura de acolo e o infiltratie.</p>',
  D2['strat']),
])}

<div class="stop"><b>De ce OSB si nu sipci:</b> verificat pe uk.onduline.com — intre 5° si 10° producatorul cere astereala continua (<em>„must be installed on full deck"</em>). Sipcile sunt permise abia peste 10°. Suntem la 8,2°.</div>

<div class="ok"><b>E bine daca:</b> capriorii sunt cu 100 pe verticala · OSB acopera tot, insurubat des · Onduline intreg, cuiele pe varf, streasina egala fata-spate.</div>
'''))

# ══════════════════════════════ E7 · geamurile si verificarea finala ══════════════════════════════
CH.append(dict(id='e7', n='E7', titlu='Geamurile si verificarea finala',
    sub='Ultimele piese, apoi lista care spune daca s-a terminat cu adevarat.',
    zi='o jumatate de zi',
    scule='GSR — sipcile geamurilor (ambreiaj, delicat) · silicon de exterior la rosturi · fereastra PVC se prinde in jambe',
    bon=[
     ('Geam fix lateral','plexi 4 mm','440×440','2'),
     ('Sipci de geam','sipca 18×28','pe ambele fete','—'),
     ('Fereastra fata','PVC 56×56','in gol 570×570','1'),
    ],
    body=f'''
<p class="lead">Doua geamuri fixe pe laterale, o fereastra care se deschide pe fata, si checklist-ul final.</p>

{steps([
 ('Geamurile laterale',
  '<p>Doua geamuri fixe de <b>440×440</b> (plexi de 4 mm, amandoua dintr-o placa de 500×1000), in tocul pregatit la E4. Sipci pe <b>ambele fete</b>, gaurile in plexi cu <b>+1 mm</b> fata de surub. Montate <b>din exterior</b>, cu un rost de silicon pe contur.</p>', None),
 ('Fereastra din fata',
  '<p>Fereastra PVC de <b>56×56</b> in golul de 570×570, prinsa in jambe, siliconata pe contur. Se deschide spre terasa — singura care se deschide.</p>', None),
])}

<h3>Checklist final</h3>

<div class="balustrada">
<b>Balustrada nu exista.</b> Terasa are margine libera la 2,2 m. Casa poate fi terminata integral, cu toate bifele verzi, si copiii tot nu au voie sus. Balustrada e faza urmatoare (F2). Pana atunci, scara se ia de langa punte intre sesiunile de lucru.
</div>

{steps([
 ('Colturile din spate au blocaj',
  '<p>Toate 4 (E0). Talpa peretelui din spate se prinde in ele.</p>', None),
 ('Peretele din spate — prins si rezemat',
  '<p>8 suruburi in stalpi, talpa in grinzi pe toata lungimea, reazemul de 200×50 pe cununa si pe stalpi.</p>', None),
 ('Peretii laterali — la echer, prinsi',
  '<p>Colturile in vincluri, talpa in grinzi, contrafise in toate colturile.</p>', None),
 ('Peretele din fata — usa taiata la final',
  '<p>Stalpii prinsi cu 4 suruburi oblice + coltar fiecare (fara tije), golul de usa 550/1600 taiat dupa ridicare.</p>', None),
 ('Acoperisul',
  '<p>Capriori cu 100 pe verticala, OSB peste tot, Onduline intreg, streasina 100/100, cuiele pe varf.</p>', None),
 ('Geamurile',
  '<p>Doua laterale fixe + fereastra PVC, toate siliconate.</p>', None),
 ('Vopsea si scara',
  '<p>Vopsea pe toate fetele, inclusiv capetele taiate. Scara luata de langa punte.</p>', None),
])}

<div class="ok"><b>Gata cand:</b> toate bifele de mai sus sunt verzi — <b>mai putin eticheta de balustrada</b>, care nu se bifeaza niciodata. Casa e terminata; puntea inca nu e sigura pentru copii.</div>
'''))

# ══════════════════════════════ STYLE ══════════════════════════════
STYLE = """<style>
:root{
 --bg:#faf9f6; --card:#fff; --ink:#1c1b18; --mut:#6b675e; --dim:#8f8b83; --line:#e2ddd3;
 --acc:#14532d; --acc-s:#eef4ef; --acc2:#8a3016; --acc2-s:#fdf3ee; --warn-s:#fdf8ec; --warn:#8a6b16;
 --mono:ui-monospace,"SF Mono",Menlo,monospace;
 --sans:"Helvetica Neue",Helvetica,Arial,sans-serif;
 --serif:"Iowan Old Style",Georgia,serif;
}
html[data-t="dark"]{
 --bg:#16161a; --card:#1d1d22; --ink:#e9e7e2; --mut:#8e8a82; --dim:#6a675f; --line:#2e2e36;
 --acc:#6fbf95; --acc-s:#18211c; --acc2:#e0834f; --acc2-s:#221a15; --warn-s:#221e14; --warn:#d9b45e;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:var(--bg);color:var(--ink);font:16px/1.65 var(--sans)}
img,svg{max-width:100%}

.wrap{display:grid;grid-template-columns:264px 1fr;gap:0;max-width:1280px;margin:0 auto}
nav{position:sticky;top:0;align-self:start;height:100vh;overflow-y:auto;padding:34px 22px 60px;border-right:1px solid var(--line);background:var(--bg)}
nav .brand{font:600 11px/1 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--acc);margin-bottom:6px}
nav h1{font:600 21px/1.25 var(--sans);letter-spacing:-.01em;margin:0 0 4px}
nav .meta{font:11px/1.5 var(--mono);color:var(--dim);margin-bottom:24px}
nav ol{list-style:none;margin:0;padding:0}
nav li a{display:block;padding:11px 12px;border-radius:9px;text-decoration:none;color:var(--ink);font-size:14.5px;line-height:1.35}
nav li a:hover{background:var(--acc-s)}
nav li a.on{background:var(--acc-s);box-shadow:inset 3px 0 0 var(--acc)}
nav .cn{display:block;font:600 10px/1 var(--mono);letter-spacing:.14em;color:var(--acc);margin-bottom:3px}
nav li a em{display:block;font:italic 12px/1.4 var(--serif);color:var(--dim);margin-top:2px}
nav .chprog{float:right;font:10px/1.4 var(--mono);color:var(--dim)}
nav li a.done .cn{color:var(--acc)}
nav li a.done .chprog{color:var(--acc)}
nav li a.done .chprog::after{content:" ✓"}
.prog{margin-top:22px;padding-top:18px;border-top:1px solid var(--line);font:11px/1.6 var(--mono);color:var(--dim)}
.bar{height:5px;border-radius:3px;background:var(--line);margin-top:7px;overflow:hidden}
.bar i{display:block;height:100%;background:var(--acc);width:0;transition:width .25s}
.navbtns{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.tgl,#resetAll{font:11px var(--mono);color:var(--dim);background:none;border:1px solid var(--line);border-radius:7px;padding:6px 10px;cursor:pointer}
.phone-jump{display:none}
.phone-jump select{width:100%;font:13px var(--mono);padding:10px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink);margin-top:8px}

main{padding:34px 46px 140px;min-width:0}

section{scroll-margin-top:14px;padding-bottom:44px;margin-bottom:44px;border-bottom:1px solid var(--line)}
section:last-child{border-bottom:none}
header.ch{margin-bottom:16px}
.cn-big{font:600 12px/1 var(--mono);letter-spacing:.2em;color:var(--acc)}
header.ch h2{font:600 34px/1.15 var(--sans);letter-spacing:-.02em;margin:8px 0 8px}
.chsub{font:italic 17px/1.5 var(--serif);color:var(--mut);margin:0;max-width:60ch}
.chmeta{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:baseline;margin-top:12px}
.zi{display:inline-block;font:11px var(--mono);letter-spacing:.08em;text-transform:uppercase;
 color:var(--mut);border:1px solid var(--line);border-radius:999px;padding:5px 11px}
.scule{font:12px/1.5 var(--mono);color:var(--mut);max-width:70ch}
.scule b{color:var(--ink)}

section.locked .chbody{opacity:.4}
.gatebar{display:flex;gap:14px;align-items:center;justify-content:space-between;background:var(--acc2-s);
 border:1px solid var(--acc2);border-left:3px solid var(--acc2);border-radius:12px;padding:14px 16px;margin:16px 0}
.gatebar .gb-txt{font-size:14.5px}
.gb-skip{flex:none;font:12px var(--mono);color:var(--acc2);background:none;border:1px solid var(--acc2);
 border-radius:7px;padding:8px 13px;cursor:pointer}
.skipwarn{background:var(--warn-s);border:1px solid var(--warn);border-left:3px solid var(--warn);
 border-radius:10px;padding:12px 15px;margin:14px 0;font-size:14px}

details.bon{margin:16px 0;background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}
details.bon>summary{cursor:pointer;padding:14px 16px;font:600 12px/1.3 var(--sans);letter-spacing:.06em;
 text-transform:uppercase;color:var(--acc);list-style:none}
details.bon>summary::-webkit-details-marker{display:none}
details.bon>summary::before{content:"▸ ";color:var(--dim)}
details.bon[open]>summary::before{content:"▾ "}
table.bontab{margin:0 16px 14px}
table.bontab td.bc{width:34px}

h3{font:600 13px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--acc);margin:36px 0 12px}
h4{font:600 17px/1.35 var(--sans);margin:0 0 8px}
p{margin:0 0 12px;max-width:70ch}
.lead{font-size:17px;color:var(--mut);max-width:66ch}
.small{font-size:13.5px;color:var(--mut)}
code{font:13.5px var(--mono);background:var(--acc-s);padding:2px 6px;border-radius:5px}
.mono{font-family:var(--mono)}
b.bad{color:var(--acc2)}

figure{margin:20px 0;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px;overflow:hidden}
figure svg{display:block;margin:0 auto;max-height:480px}
figcaption{margin-top:14px;font:13px/1.6 var(--mono);color:var(--dim);max-width:74ch}

ol.steps{list-style:none;margin:22px 0;padding:0;counter-reset:s}
ol.steps>li{display:flex;gap:16px;padding:20px 0;border-top:1px solid var(--line)}
ol.steps>li:last-child{border-bottom:1px solid var(--line)}
.stepbody{min-width:0;flex:1}
.stepbody h4::before{counter-increment:s;content:counter(s) "  ";font-family:var(--mono);color:var(--acc);font-weight:600}
.stepfig{margin-top:14px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}
.stepfig svg{max-height:400px;display:block;margin:0 auto}
.tick{flex:none;cursor:pointer;padding-top:2px}
.tick input{position:absolute;opacity:0;width:0;height:0}
.tick span{display:block;width:26px;height:26px;border:2px solid var(--line);border-radius:8px;transition:.15s;background:var(--card)}
.tick input:checked+span{background:var(--acc);border-color:var(--acc);
 background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E");
 background-size:18px;background-position:center;background-repeat:no-repeat}
.tick input:disabled+span{opacity:.4}
.tick.sm span{width:22px;height:22px}
li.done .stepbody{opacity:.5}

.gate,.stop,.ok,.need,.warn,.why,.balustrada{border-radius:12px;padding:16px 18px;margin:20px 0;font-size:15px}
.gate{background:var(--acc-s);border-left:3px solid var(--acc)}
.stop{background:var(--acc2-s);border-left:3px solid var(--acc2)}
.ok{background:var(--acc-s);border:1px solid var(--line);border-left:3px solid var(--acc)}
.need{background:var(--card);border:1px solid var(--line)}
.need h4{font:600 11px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--acc);margin-bottom:12px}
.need ul{margin:0;padding-left:20px} .need li{margin:4px 0}
.warn{background:var(--acc2-s);border:1px solid var(--line)}
.balustrada{background:var(--acc2-s);border:1px solid var(--acc2);border-left:4px solid var(--acc2);font-size:15px}
.why{background:var(--card);border:1px solid var(--line)}
.why-inline{font:italic 15px/1.6 var(--serif);color:var(--mut);border-left:2px solid var(--line);padding-left:14px;margin:12px 0}
.tool{font-size:14.5px;background:var(--warn-s);border-radius:9px;padding:11px 14px}

table.t{width:100%;border-collapse:collapse;font-size:14.5px;margin:14px 0}
table.t th{text-align:left;font:600 10.5px/1 var(--sans);letter-spacing:.13em;text-transform:uppercase;
 color:var(--dim);padding:0 10px 10px 0;border-bottom:1px solid var(--line)}
table.t td{padding:10px 10px 10px 0;border-bottom:1px solid var(--line);vertical-align:baseline}
table.t .q{font-family:var(--mono);text-align:right;white-space:nowrap}
table.t td.mono{font-family:var(--mono)}

.chreset{margin-top:30px;padding-top:16px;border-top:1px dashed var(--line)}
.reset-ch{font:11px var(--mono);color:var(--dim);background:none;border:1px solid var(--line);border-radius:7px;padding:6px 10px;cursor:pointer}
.cfm{margin-left:8px;font:12px var(--mono);color:var(--acc2)}
.cfm button{font:11px var(--mono);border:1px solid var(--line);border-radius:6px;padding:3px 9px;margin-left:4px;cursor:pointer;background:var(--card);color:var(--ink)}
footer.doc{margin-top:50px;font:12px/1.7 var(--mono);color:var(--dim)}

@media(max-width:720px){
 .wrap{grid-template-columns:1fr}
 nav{position:sticky;top:0;z-index:20;height:auto;overflow:visible;border-right:none;border-bottom:1px solid var(--line);padding:12px 16px}
 nav h1,nav .meta,nav ol,nav .prog{display:none}
 nav .brand{margin:0}
 .phone-jump{display:block}
 main{padding:20px 16px 90px}
 header.ch h2{font-size:27px}
 .tick{padding:9px;margin:-9px 0}
 .tick span{width:26px;height:26px}
 ol.steps>li{gap:10px}
 table.bontab{margin:0 8px 12px;font-size:13px}
}
</style>"""

# ══════════════════════════════ SCRIPT ══════════════════════════════
SCRIPT = """<script>
(function(){
 var LS='ghid.';
 function get(k){try{return localStorage.getItem(LS+k);}catch(e){return null;}}
 function set(k,v){try{localStorage.setItem(LS+k,v);}catch(e){}}
 function del(k){try{localStorage.removeItem(LS+k);}catch(e){}}

 var secs=[].slice.call(document.querySelectorAll('section[data-ch]'));
 secs.forEach(function(sec){
   var ch=sec.dataset.ch;
   [].slice.call(sec.querySelectorAll('input.step')).forEach(function(inp,i){ inp.dataset.key=ch+'.s'+i; });
   [].slice.call(sec.querySelectorAll('input.bon')).forEach(function(inp,i){ inp.dataset.key=ch+'.b'+i; });
 });
 var allBoxes=[].slice.call(document.querySelectorAll('input.bx'));
 allBoxes.forEach(function(inp){ if(get(inp.dataset.key)==='1'){ inp.checked=true; } });

 function chSteps(ch){ return [].slice.call(document.querySelectorAll('section[data-ch="'+ch+'"] input.step')); }
 function chComplete(ch){ var s=chSteps(ch); return s.length>0 && s.every(function(i){return i.checked;}); }

 function updProgress(){
   var all=[].slice.call(document.querySelectorAll('input.step'));
   var n=all.filter(function(i){return i.checked;}).length;
   document.getElementById('pt').textContent=n+' / '+all.length;
   document.getElementById('pb').style.width=(all.length?100*n/all.length:0)+'%';
   secs.forEach(function(sec){
     var ch=sec.dataset.ch, s=chSteps(ch), c=s.filter(function(i){return i.checked;}).length;
     var link=document.querySelector('nav a[data-ch="'+ch+'"]');
     if(link){ var cp=link.querySelector('.chprog'); if(cp) cp.textContent=c+'/'+s.length;
       link.classList.toggle('done', s.length>0 && c===s.length); }
     s.forEach(function(i){ var li=i.closest('li'); if(li) li.classList.toggle('done', i.checked); });
   });
 }

 function updGates(){
   secs.forEach(function(sec){
     var bar=sec.querySelector('.gatebar'); if(!bar) return;
     var skipped=get('skip.'+sec.dataset.ch)==='1';
     var locked=!chComplete(bar.dataset.gate) && !skipped;
     sec.classList.toggle('locked', locked);
     bar.style.display=locked?'':'none';
     var sw=sec.querySelector('.skipwarn'); if(sw) sw.style.display=skipped?'':'none';
     [].slice.call(sec.querySelectorAll('.chbody input.bx')).forEach(function(i){ i.disabled=locked; });
   });
 }

 allBoxes.forEach(function(inp){
   inp.addEventListener('change',function(){
     if(inp.checked) set(inp.dataset.key,'1'); else del(inp.dataset.key);
     updProgress(); updGates();
   });
 });

 [].slice.call(document.querySelectorAll('.gb-skip')).forEach(function(btn){
   btn.addEventListener('click',function(){ set('skip.'+btn.closest('section').dataset.ch,'1'); updGates(); });
 });

 function confirmInline(host, onYes){
   if(host.querySelector('.cfm')) return;
   var w=document.createElement('span'); w.className='cfm';
   w.innerHTML='sigur? <button type="button" class="cy">da</button><button type="button" class="cnn">nu</button>';
   host.appendChild(w);
   w.querySelector('.cy').onclick=function(){ onYes(); w.parentNode.removeChild(w); };
   w.querySelector('.cnn').onclick=function(){ w.parentNode.removeChild(w); };
 }
 [].slice.call(document.querySelectorAll('.reset-ch')).forEach(function(btn){
   btn.addEventListener('click',function(){
     confirmInline(btn.parentNode,function(){
       var sec=btn.closest('section');
       [].slice.call(sec.querySelectorAll('input.bx')).forEach(function(i){ i.checked=false; del(i.dataset.key); });
       updProgress(); updGates();
     });
   });
 });
 var ra=document.getElementById('resetAll');
 if(ra) ra.addEventListener('click',function(){
   confirmInline(ra.parentNode,function(){
     allBoxes.forEach(function(i){ i.checked=false; del(i.dataset.key); });
     secs.forEach(function(sec){ del('skip.'+sec.dataset.ch); });
     updProgress(); updGates();
   });
 });

 var jump=document.getElementById('jump');
 if(jump) jump.addEventListener('change',function(){ var el=document.getElementById(jump.value); if(el) el.scrollIntoView(); });
 var links=[].slice.call(document.querySelectorAll('nav ol a'));
 var obs=new IntersectionObserver(function(es){
   es.forEach(function(e){ if(e.isIntersecting){
     links.forEach(function(l){l.classList.remove('on');});
     var l=document.querySelector('nav a[data-ch="'+e.target.dataset.ch+'"]'); if(l) l.classList.add('on');
     if(jump) jump.value=e.target.id;
   }});
 },{rootMargin:'-10% 0px -75% 0px'});
 secs.forEach(function(s){obs.observe(s);});

 updProgress(); updGates();
})();
function tt(){var h=document.documentElement;h.dataset.t=h.dataset.t==='dark'?'':'dark';}
</script>"""

# ══════════════════════════════ ASAMBLARE ══════════════════════════════
nav = '\n'.join(
 f'<li><a href="#{c["id"]}" data-ch="{c["id"]}"><span class="cn">{c["n"]}</span>{c["titlu"]}<em>{c["zi"]}</em><span class="chprog"></span></a></li>'
 for c in CH)
opts = ''.join(f'<option value="{c["id"]}">{c["n"]} — {c["titlu"]}</option>' for c in CH)

def section(c):
    scule = f'<span class="scule"><b>Scule:</b> {c["scule"]}</span>' if c.get('scule') else ''
    gate=''; skipw=''
    if c.get('blocat_de'):
        pn = next(x['n'] for x in CH if x['id']==c['blocat_de'])
        gate = (f'<div class="gatebar" data-gate="{c["blocat_de"]}">'
                f'<div class="gb-txt"><b>Blocat de {pn}.</b> {c["blocat_motiv"]}</div>'
                f'<button class="gb-skip" type="button">sar peste</button></div>')
        skipw = (f'<div class="skipwarn" style="display:none"><b>Ai sarit peste blocajul {pn}.</b> '
                 f'{c["blocat_motiv"]}</div>')
    bon_html = bon(c['bon']) if c.get('bon') else ''
    return f'''<section id="{c['id']}" data-ch="{c['id']}">
<header class="ch"><div class="cn-big">{c['n']}</div><h2>{c['titlu']}</h2><p class="chsub">{c['sub']}</p>
<div class="chmeta"><span class="zi">{c['zi']}</span>{scule}</div></header>
{gate}{skipw}
<div class="chbody">
{bon_html}
{c['body']}
<div class="chreset"><button class="reset-ch" type="button">sterge bifele din capitolul asta</button></div>
</div>
</section>'''

secs = '\n'.join(section(c) for c in CH)

HTML = f'''<!DOCTYPE html>
<html lang="ro"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ghid de constructie — casa de sus</title>
{STYLE}</head><body>
<div class="wrap">
<nav>
 <div class="brand">Casuta din copac</div>
 <h1>Ghid de constructie<br>casa de sus</h1>
 <div class="meta">20 august 2026 · cote in mm<br>geometrie masurata pe santier</div>
 <label class="phone-jump"><select id="jump">{opts}</select></label>
 <ol>{nav}</ol>
 <div class="prog">progres global <span id="pt">0 / 0</span><div class="bar"><i id="pb"></i></div>
  <div class="navbtns"><button class="tgl" onclick="tt()">lumina / intuneric</button><button id="resetAll" type="button">sterge toate bifele</button></div>
 </div>
</nav>
<main>
{secs}
<footer class="doc">
GHID-CONSTRUCTIE-casa · 20.08.2026 · E0–E7 · documentul de executie al casei.<br>
Cotele vin din masuratorile de santier confirmate pe 20.08 (<code>MASURATORI-CONFIRMARE-2026-08-20</code>).<br>
Desene la scara: <code>SCHEME-2D-casa.html</code> · cumparaturi: <code>LISTA-LEROY-2026-08-17</code>.<br>
Bifele se tin minte in browser (localStorage) — raman dupa refresh. Butonul „sterge toate bifele" le sterge.
</footer>
</main>
</div>
{SCRIPT}
</body></html>'''

open('GHID-CONSTRUCTIE-casa.html','w',encoding='utf-8').write(HTML)
print('scris', len(HTML), 'caractere ·', len(CH), 'capitole')
