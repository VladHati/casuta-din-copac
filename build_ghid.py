#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asambleaza GHID-CONSTRUCTIE-casa.html — documentul de executie al casei.
6 capitole (E1-E6), cuprins lateral, bon de taiere si scule per capitol,
strat interactiv (localStorage, progres pe capitol, reset)."""
import json

GH = json.load(open('figs_ghid.json'))
MATS = json.load(open('mats.json'))
D2 = json.load(open('figs_2d.json'))
C  = json.load(open('cote.json'))   # cotele derivate din gen_ghid: nimic scris de mana mai jos
VB,VF,VL,TT = C['VB'],C['VF'],C['VL'],C['T']
VLs = ' · '.join(str(v) for v in VL)

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


# ══════════════ MATERIALE PE ETAPA ══════════════
# (nume, cantitate, unitate, nota).  Cantitatile sunt NETE, calculate din bonul de taiere.
MAT = {
 'e2': dict(buy=[
    ('Rigla 46×46×3000',      7,   'bare',  'talpa+cununa 2×1990, verticale 5×1608, contrafise 2×424+2×212. Pe bara de 3 m intra o singura piesa lunga — de aceea 7, nu 4,4.'),
    ('Lambriu 19×116×4000',   9,   'scanduri','17 randuri de 1990, toata inaltimea. Dintr-o scandura de 4 m ies DOUA randuri (1990+1990). PASTREAZA capetele — acopera tot peretele din fata.'),
    ('Surub dulgherie 8×140', 8,   'buc',   'cate 4 la fiecare capat, in stalpii de 4 m'),
    ('Surub dulgherie 6×140', 6,   'buc',   'talpa prin podea, in grinzi, la 400'),
    ('Conector lemn 90×200',  4,   'buc',   'placi metalice deasupra fiecarui stalp, sub reazem'),
    ('Surub inox 4×50',       85,  'buc',   'un surub pe fiecare intersectie lamela-verticala: 17 randuri × 5 verticale. La 19 mm grosime, 4×40 e prea scurt.'),
    ('Lazura exterior',       1.9, 'litri', 'rama pe 4 fete + scandurile pe toate cele 6 suprafete, doua straturi. 13,6 m² × 2.'),
 ], have=[
    ('Dulap 200×50×4000', 1, 'bara', 'reazemul acoperisului — se taie la 2200, pe muchie, 200 in sus'),
    ('Vinclu Parkside 40×40', 4, 'buc', 'colturile ramei, pe interior. 40 mm incap pe rigla de 46; cel de 90 ar iesi in aer. 2 pungi × 16 = 32 in total.'),
    ('Vinclu 70×55', 10, 'buc', 'reazemul de sus, dulapul de 200×50, pe ambele fete. Exact 10 cate ai. 55 mm pe un dulap de 50 — iese 5 mm, acceptabil.'),
    ('Stalpi spate 100×100', 2, 'buc', 'montati pe santier, 1700 peste podea. Nu se cumpara, nu se taie — peretele se prinde IN ei.'),
 ]),
 'e3': dict(buy=[
    ('Rigla 46×46×3000',      12,  'bare',  'ambii pereti: talpi 1580+1570, cununi 1596+1586, 8 verticale, 4 praguri de 490, 8 contrafise. Verticalele si talpile iau cate o bara fiecare.'),
    ('Lambriu 19×116×4000',   14,  'scanduri','7 pe fiecare perete. Dintr-o scandura de 4 m ies doua randuri de 1580. Randurile de sus se scurteaza pe panta.'),
    ('Rigla 46×46×3000',      2,   'bare',  'tocurile celor doua geamuri — gol 490, 4×490 pe toc. Acelasi material ca rama: resturile lungi de mai sus pot acoperi tocurile.'),
    ('Placa plexiglas 500×1000×4', 1, 'placa', 'amandoua geamurile de 440×440 ies dintr-una'),
    ('Surub dulgherie 6×140', 10,  'buc',   'talpile prin podea, la 400'),
    ('Surub inox 4×50',       144, 'buc',   '18 randuri × 4 verticale × 2 pereti'),
    ('Lazura exterior',       3.1, 'litri', 'ambii pereti: rama, scandurile pe toate fetele, canturile golurilor de geam. 21,7 m² × 2 straturi.'),
 ], have=[
    ('Vinclu Parkside 40×40', 8, 'buc', 'cate 4 colturi pe perete. Pe rigla de 46 intra doar cele de 40.'),
    ('Stalpi 100×100 si 90×90', 4, 'buc', 'toti patru sunt montati. Fiecare perete lateral se prinde intre un stalp de spate si unul de fata.'),
 ]),
 'e4': dict(buy=[
    ('Rigla 46×46×3000',      6,   'bare',  'talpa 1970, 5 verticale 1554, prag+buiandrug 570, 3 contrafise'),
    ('Lambriu 19×116×4000',   6,   'scanduri','sau aproape zero scanduri noi: bucatile de aici sunt toate sub 940 mm (938 · 482 · 207 · 161), deci ies din capetele pastrate la E2 si E3.'),
    ('Fereastra PVC 56×56',   1,   'buc',   'singura care se deschide'),
    ('Surub dulgherie 8×140', 8,   'buc',   'prinderea finala a stalpilor: 4 oblice pe stalp'),
    ('Surub dulgherie 6×140', 6,   'buc',   'talpa prin podea, la 400'),
    ('Surub inox 4×50',       80,  'buc',   '16 randuri × 5 verticale'),
    ('Lazura exterior',       1.4, 'litri', 'rama + scanduri. Peretele are ~90 de capete taiate, fiecare pensulat pe loc.'),
 ], have=[
    ('Vinclu 90×60', 4, 'buc', 'prinderea finala a stalpilor de 90×90. Latimea de 60 sta bine pe fata de 90.'),
    ('Vinclu Parkside 40×40', 2, 'buc', 'cele doua colturi de rama.'),
    ('Bara 100×60×3000', 1, 'bara', 'lemnul de sus — se taie la 2155, latura de 60 in sus'),
    ('Stalpi fata 90×90', 2, 'buc', 'montati pe santier la 1600 peste podea. Nu se cumpara — aici doar se face prinderea finala.'),
 ]),
 'e5': dict(buy=[
    ('Scandura 22×100×4000',  7,   'bare',  '5 capriori laminati de 1889 (5 bare, 2 straturi pe caprior) + 4 inchideri de 454 (a 6-a); a 7-a rezerva'),
    ('Placa OSB3 12 mm',      2,   'placi', 'taiate 2200×1250 si 2200×639'),
    ('Onduline 2000×860',     3,   'placi', 'intregi, una langa alta — panta 1889 < 2000'),
    ('Cuie Onduline, set 400', 1,  'set',   'un singur set in stoc la ultima verificare'),
    ('Surub 4×45',            150, 'buc',   'OSB in capriori, la 250'),
    ('Lazura exterior',       0.5, 'litri', 'capriorii si inchiderile, inainte sa intre sub OSB.'),
    ('Surub 4×40',            110, 'buc',   'laminarea capriorilor, zigzag la 300'),
 ], have=[]),
 'e6': dict(buy=[
    ('Sipca 18×28×3000',      3,   'bare',  'strang geamurile pe ambele fete: 2 geamuri × 2 fete × 4 laturi de 490 = 7,84 m. Doua bare (6 m) nu ajung.'),
    ('Silicon de exterior',   2,   'tuburi',''),
    ('Surub inox 4×50',       50,  'buc',   'sipcile de geam — aceeasi masura ca la lambriu, un singur rand de cumparat'),
 ], have=[
    ('Vinclu Parkside 40×40', 18, 'buc', 'cate 2 la fiecare capat de caprior. Caprior 44 lat → 40 incape. 1550 N bucata, imbinarea cere ~92 kg. Ultimele 18 din cele 32.'),
    ('Vinclu 90×60', 2, 'buc', 'ultimele doua capete de caprior — Parkside-ul se termina la 32.'),
 ]),
}

# Ce cumperi de fapt vs ce cere suma etapelor. Diferenta e explicata, nu ascunsa.
CUMPERI = [
 ('Rigla 46×46×3000',           '27',  '~673 lei', 'rama TUTUROR peretilor <b>si</b> tocurile de geam — un singur material. Planul de taiere cere <b>25</b> de bare (E2 7 · E3 12 · E4 6); tocurile incap in resturile lungi de la laterale, nu cer bare in plus. <b>Ultimele 2 sunt rezerva</b> — 54 de taieri in lemn brut, cu noduri si capete crapate. Net 52,4 m din 75 cumparati: pierderea de 30% vine din faptul ca pe o bara de 3 m nu intra doua piese de 1550–1990. 24,91 lei/buc, stoc 188 la Colosseum.', ('e2','e3','e4','e6')),
 ('Lambriu 19×116×4000, pachet 2,78 m²','5', '1.015 lei', '<b>29 de scanduri</b> de 4 m: spate 9 · laterale 14 · fata 6. Cinci pachete dau 30 — <b>rezerva e o singura scandura</b>. Sunt 133 in stoc la Colosseum, deci o completare e usoara. Din 4 m ies doua randuri de 1990 sau doua de 1580; asta injumatateste numarul fata de scandurile de 3 m.', ('e2','e3','e4')),
 ('Scandura 22×100×4000',       '7',   '~139 lei', '5 capriori laminati (5 bare, 2 straturi pe caprior) plus inchiderile de 454 (a 6-a); a 7-a rezerva.', ('e5',)),
 ('Placa OSB3 12 mm',           '2',   '~150 lei', 'astereala acoperisului.', ('e5',)),
 ('Onduline Base 2000×860 maro','3',   '124 lei',  'maro 41,23 lei/placa fata de 46,88 la rosu, si stocul e 146 fata de 15. Verificat 21.08. Se pun intregi, nu se taie.', ('e5',)),
 ('Cuie Onduline 65×2,8, set 400','1', '97 lei',   '<b>Nu se pot adauga online</b> — ultima bucata din stoc e blocata pe site. Se iau de la raft, primul lucru. Daca s-au terminat: <b>surub de acoperis cu saiba de cauciuc, minim 65 mm</b>. Valul Onduline are ~38 mm inaltime plus 12 mm de OSB dedesubt — orice sub 55 mm nu ajunge in astereala. Cele de 4,8×19 din raion NU merg.', ('e5',)),
 ('Placa plexiglas 500×1000×4', '1',   '72 lei',   'amandoua geamurile ies dintr-una.', ('e3','e6')),
 ('Fereastra PVC 56×56',        '1',   '127 lei',  'peretele din fata.', ('e4','e6')),
 ('Sipca 18×28×3000',           '3 bare', '~25 lei', 'baghetele geamurilor laterale. Doua geamuri × doua fete × 4 laturi de 490 = <b>7,84 m</b>; doua bare (6 m) NU ajung. 8,29 lei/bara, verificat 06.08.', ('e6',)),
 ('Lazura exterior Luxens 5 L, pe baza de apa', '2 galeti', '~284 lei', 'stejar mediu. Suprafata reala de tratat e <b>48,4 m²</b> — lambriul pe DOUA fete plus canturi (31 m²), rama pe patru fete (15 m²), capriorii (3 m²). Doua straturi = 97 m². La 70 m²/galeata ies 6,9 L, deci doua galeti. <b>Cei 2 L de ulei de tec din stoc NU acopera casa</b> — ajung la ~20% si n-au pigment, deci nu opresc UV-ul. Uleiul ramane pentru dusumeaua de larice si blatul cioatei, unde e produsul corect.', ('e2','e3','e4','e5')),
 ('Silicon de exterior',        '2 tuburi', '~30 lei', 'rosturile geamurilor laterale si ale ferestrei din fata.', ('e6',)),
 ('Conector lemn 90×200×2,5',   '4',   '~36 lei',  'placile de deasupra fiecarui stalp, sub reazem. <b>Singurul metal care se mai cumpara</b> — vincluri nu, le ai pe toate.', ('e2',)),
 ('Surub dulgherie 8×140',      '16',  '~32 lei',  'peretele din spate in stalpi 8 · stalpii din fata 8. <b>Nu 36</b> — cele 20 pentru blocajele de colt au iesit, lucrarea e facuta din 21.08.', ('e2','e4')),
 ('Surub dulgherie 6×140',      '24',  '~38 lei',  'talpile prin podea, in grinzi, la 400: spate 6 · laterali 10 · fata 6 = 22, plus 2 rezerva.', ('e2','e3','e4')),
 ('Surub dulgherie 6×80',       '~60', '~26 lei',  'contrafisele si proptelele, 2 la fiecare capat. Coltul din rigla 46+46 are 92 mm: unul de 100 ar iesi 8 mm pe partea cealalta. Ai 20 Heco 6×80 in stoc.', ('e2','e3','e4')),
 ('Surub inox A2 4×50',        '~380','~155 lei', 'lambriul: un surub pe fiecare intersectie lamela-verticala — spate 85 · laterale 144 · fata 80 = 309; plus <b>50 pentru sipcile de geam</b> la E6, plus rezerva. <b>4×50, nu 4×40</b>: lamela are 19 mm, ii trebuie macar 25 mm in rigla. Nu ai niciunul — stocul din faza 1 s-a dus tot in podea.', ('e2','e3','e4','e6')),
 ('Surub 4×45 · 4×40',          'cutii','~60 lei', 'OSB in capriori (150 buc de 4×45) si laminarea capriorilor (110 buc de 4×40). Cele de 4×50 sunt in randul de inox de mai sus.', ('e5',)),
]

def mat(mid):
    m = MAT.get(mid)
    if not m: return ''
    def rows(items, cls):
        out=[]
        for (nume,cant,um,nota) in items:
            c = f'{cant:g}'.replace('.', ',')
            n = f'<div class="mnote">{nota}</div>' if nota else ''
            out.append(f'<li class="{cls}"><span class="mq">{c} {um}</span>'
                       f'<span class="mn">{nume}{n}</span></li>')
        return '\n'.join(out)
    b = f'<div class="mcol buy"><h4>Cumperi</h4><ul>{rows(m["buy"],"b")}</ul></div>' if m['buy'] else ''
    h = f'<div class="mcol have"><h4>Ai deja pe punte</h4><ul>{rows(m["have"],"h")}</ul></div>' if m['have'] else ''
    return (f'<div class="mat" id="mat-{mid}"><div class="mhead">Materiale pentru etapa asta'
            f'<a class="matback" href="#e1">toate cumparaturile →</a></div>'
            f'<div class="mgrid">{b}{h}</div></div>')

NUME_CH = {'e2':'E2','e3':'E3','e4':'E4','e5':'E5','e6':'E6'}

# unde apare fiecare material, ca sa se poata sari direct din legenda in capitol
MAT_CH = {
 'ram':('e2','e3','e4','e6'), 'cap':('e5',), 'scn':('e5',),
 'lam':('e2','e3','e4'), 'osb':('e5',), 'ond':('e5',), 'sip':('e6',),
 'plx':('e3','e6'), 'pvc':('e4','e6'), 'st10':('e2','e3'), 'st9':('e3','e4'),
 'dul':('e2','e5'), 'bara':('e4',), 'dus':('e2','e3','e4'), 'gri':('e2','e3','e4'),
}
ORD = ['ram','cap','scn','lam','osb','ond','sip','plx','pvc',
       'st10','st9','dul','bara','dus','gri','met']

def cheia_materialelor():
    def rand(k):
        fill,short,lung,exist = MATS[k]
        hx = ('<span class="sw-hx"></span>' if exist else '')
        chips = ' '.join(f'<a class="chip" href="#{i}">{NUME_CH[i]}</a>' for i in MAT_CH.get(k,()))
        marca = '<b>pe santier</b>' if exist else 'se cumpara'
        return (f'<tr><td class="swc"><span class="sw" style="background:{fill}">{hx}</span></td>'
                f'<td>{lung}</td><td class="small">{marca}</td><td class="q">{chips}</td></tr>')
    return ('<table class="t mtab"><tr><th></th><th>Material si sectiune</th>'
            '<th>De unde vine</th><th class="q">Capitole</th></tr>'
            + ''.join(rand(k) for k in ORD if k in MATS) + '</table>')

def chip_links(ids):
    if not ids: return ''
    lk = ' '.join(f'<a class="chip" href="#{i}">{NUME_CH[i]}</a>' for i in ids)
    return f'<div class="uses">se foloseste la {lk}</div>'

def cumperi_tabel():
    trs=''.join(
      f'<tr><td>{a}</td><td class="q mono">{b}</td><td class="q mono">{c}</td>'
      f'<td class="small">{d}{chip_links(e)}</td></tr>'
      for (a,b,c,d,e) in CUMPERI)
    return ('<table class="t cump"><tr><th>Articol</th><th class="q">Cat</th><th class="q">~Lei</th>'
            '<th>De ce atat · unde intra</th></tr>'+trs+'</table>')


CH = []

# ══════════════════════════════ E1 · Leroy ══════════════════════════════
CH.append(dict(id='e1', n='E1', titlu='Drumul la Leroy',
    sub='Un singur magazin, un singur drum. Colosseum.',
    zi='o jumatate de zi',
    body=f'''
<p class="lead">Un singur drum. Tot ce urmeaza in ghid presupune ca te intorci cu lista de mai jos completa.</p>

<div class="gate">
<b>Rama tuturor peretilor e din rigla 46×46×3000, cumparata gata.</b> Nu se lamineaza si nu se taie nimic in lung. Cu lambriul de <b>19 mm</b> ales pe 21.08, panoul din spate iese la <b>~42-51 kg</b> — se ridica in doi, pe o punte care nu are balustrada.
</div>

<div class="need">
<h4>Tot ce cumperi</h4>
<p class="small">Cantitatile vin din bonurile de taiere ale celor cinci etape, adunate.</p>
{cumperi_tabel()}
</div>



<div class="exist"><b>Vincluri: nu se cumpara niciunul.</b> Inventarul din 21.08 acopera tot: <b>32× Parkside 40×40</b> (2 pungi, zincate termic ≥19 μm, 1550 N) → colturile de rama si capetele de capriori, fiindca 40 mm incap pe rigla de 46 · <b>10× 70×55</b> → reazemul din spate · <b>6× 90×60</b> → stalpii din fata (4) si ultimele doua capete de caprior · <b>4× 90×100</b> → rezerva; 100 mm latime cer lemn de 100, adica doar stalpii din spate. Regula: <b>latimea vinclului nu poate depasi latimea lemnului pe care sta.</b></div>
<div class="exist">
<b>Ce e deja pe santier si NU se cumpara:</b> cei patru stalpi ai casei — <b>100×100 in spate</b> (intregi, 4 m, ies 1700 peste podea) si <b>90×90 in fata</b> (taiati, 1600 peste podea) — plus podeaua, dulapul de 200×50 pentru reazem si bara de 100×60 pentru peretele din fata. Peretii se prind <b>in</b> stalpi. Rigla de 46×46 pe care o cumperi e rama dintre ei, nu un al doilea rand de stalpi.
</div>

<div class="need">
<h4>Cheia lemnului — ce e fiecare piesa din desene</h4>
<p class="small">Fiecare desen din ghid isi poarta legenda lui. Aceasta e cheia completa: culoarea din desen, materialul si sectiunea lui. Piesele hasurate sunt cele care exista deja pe santier.</p>
{cheia_materialelor()}
</div>

<div class="gate">
<b>Ordinea in magazin:</b> intai <b>cuiele de Onduline</b> — stocul e mic. Daca s-au terminat, iei suruburi de acoperis cu saiba de cauciuc din acelasi raion. Apoi placile: ia maro, e mai ieftin si e stoc.
</div>

{steps([
 ('Cele 27 de rigle de 46×46',
  '<p>Rama tuturor peretilor <b>si</b> tocurile de geam — un singur material pe tot santierul. Planul de taiere cere <b>25</b> de bare: <b>7</b> la spate, <b>12</b> la laterali, <b>6</b> la fata. Tocurile de geam ies din resturile lungi de la laterali, nu cer bare in plus. <b>Ultimele doua sunt rezerva.</b> Le numeri inainte sa pleci.</p>'
  '<p class="why-inline">De ce 25 si nu 17: pe o bara de 3 m nu intra doua piese de 1550–1990, iar 26 din cele 54 de piese sunt exact atat. Fiecare consuma o bara intreaga. Pierderea de 30% e in plan, nu e risipa — nu o "optimiza" la magazin.</p>'
  '<p class="why-inline">De ce nu rigla de 48×48 la 4 m, cum scria planul pana pe 21.08: are <b>stoc zero</b> la Colosseum si nu se livreaza — e produs doar de ridicat din magazin. La 46×46 pierzi 2 mm de sectiune (88% din rezistenta la incovoiere) si castigi materialul pe raft azi.</p>', None),
 ('Masoara o rigla inainte sa pleci din magazin',
  '<p>Rigla e <b>bruta, nerindeluita</b>: 46×46 e cota nominala, nu garantata. Pune ruleta pe doua-trei bare din stiva si notezi cat ies cu adevarat.</p>'
  '<p class="why-inline">Toate verticalele sunt calculate ca <b>lumina minus doua grosimi de rigla</b>: 1608 la spate, 1554 la fata, 1577·1649·1726·1798 la laterale. Daca rigla iese 44 in loc de 46, fiecare verticala e cu 4 mm prea scurta si peretele are joc; daca iese 48, e cu 4 mm prea lunga si nu intra. <b>Corectia e simpla: verticala = lumina − 2 × grosimea masurata.</b> Lumina e 1700 la spate, 1600 la fata, 1669·1741·1818·1890 la laterale.</p>', None),
 ('Cuiele de Onduline, primele',
  '<p>Stocul e mic. Daca s-au terminat, iei suruburi de acoperis cu saiba de cauciuc din acelasi raion.</p>', None),
 ('Restul listei, bifat la casa',
  '<p>Tot ce e in <code>LISTA-LEROY-2026-08-17</code>, cu masuratorile M2–M5 facute inainte (lambriul se ia pe masuratori reale).</p>', None),
])}

<div class="ok"><b>E bine daca:</b> cele 27 de rigle de 46×46 sunt in masina · tot ce e pe lista e bifat la casa · cuiele de Onduline sunt in portbagaj.</div>
'''))

# ══════════════════════════════ E2 · peretele din spate ══════════════════════════════
CH.append(dict(id='e2', n='E2', titlu='Peretele din spate',
    sub='Singurul perete care se face complet jos, pe iarba. Dupa ridicare nu mai ajungi la el.',
    zi='o zi',
    scule='HS7611K — rigla si dulapul la lungime · GSR — gauri pilot 4 mm + suruburile · GDR — cele 8×140 in stalpi · doi oameni la ridicare',
    bon=[
     ('Talpa + cununa','rigla 46×46','1990','2'),
     ('Verticale','rigla 46×46',str(VB),'5'),
     ('Contrafise colturi','rigla 46×46 (rest)','2× 424 jos · 2× 212 sus','4'),
     ('Reazemul din spate','dulap 200×50 (il ai)','2200','1'),
     ('Lambriu','19×116×4000','17 randuri de 1990, cate doua pe scandura','9'),
    ],
    body=f'''
<p class="lead">Intre peretele din spate si gard raman <b>30 cm</b>. Ce nu e gata cand il ridici — scanduri, vopsea, suruburi — ramane asa pentru totdeauna. De asta se face complet jos, pe iarba, si abia apoi se urca pe punte.</p>

{fig(D2['spate'], f'Elevatie la scara, din exterior. Cinci verticale de {VB}, talpa si cununa de 1990, proptele in colturi. <a class="dwg" href="SCHEME-2D-casa.html#spate">desenul la scara →</a>')}

{steps([
 ('Rama pe iarba',
  '<p>Talpa si cununa (rigla 46×46, taiate la <b>1990</b>) paralele. Insemnezi pe amandoua unde vin cele 5 verticale: <span class="mono">0 · 498 · 995 · 1493 · 1990</span>.</p>'
  f'<p>Verticalele sunt rigla 46×46 taiata la <b>{VB}</b> (= 1700 − doua talpi de {TT}). Le prinzi cu cate 2 suruburi prin talpa si 2 prin cununa, <b>cu gaura de 4 mm data inainte</b> — capetele de rigla crapa altfel.</p>', None),
 ('Diagonalele — inainte de orice altceva',
  '<p>Masori ambele diagonale ale ramei. Trebuie egale, <b>voie 3 mm</b>. Corectezi acum, impingand de colturi.</p>'
  '<p class="why-inline">Proptelele ingheata forma exact cum o gasesc. Daca rama e stramba cand le pui, ramane stramba, si se vede la lambriu.</p>', None),
 ('Proptelele din colturi',
  '<p>Din restul de rigla 46×46: jos brate de 300 (taiate la <b>424</b> pe diagonala), sus brate de 150 (taiate la <b>212</b>). Cate 2 suruburi <b>6×80</b> la fiecare capat.</p>'
  '<p class="why-inline">Surub de <b>6×80</b>, nu de 100: coltul din rigla 46+46 are 92 mm grosime; unul de 100 iese 8 mm pe partea cealalta, la inaltimea capului de copil. Ai 20 de Heco 6×80 in stoc.</p>', None),
 ('Lazura — inainte de lambriu, nu dupa',
  '<p>Rama e incheiata si e in echer. <b>Acum</b> primeste lazura, pe toate cele patru fete ale fiecarei rigle. Dupa ce vine lambriul peste ea, fata exterioara a ramei dispare pentru totdeauna.</p>'
  '<p>Apoi tai scandurile de lambriu la lungimile randurilor. <b>Tai intai, vopsesti dupa</b> — daca vopsesti scandura intreaga de 4 m si abia apoi o tai, fiecare taietura ramane lemn crud si tot te intorci sa retusezi.</p>'
  '<p><b>Fiecare scandura primeste lazura pe toate cele sase suprafete:</b> fata, spatele, ambele canturi (lamba si ulucul), ambele capete.</p>'
  '<ul>'
  '<li><b>Spatele</b> — dupa insurubare nu mai ajungi la el niciodata. Crud, trage umezeala, si scandura se cupeaza exact cum n-ai vrut cand ai luat-o de 19 mm.</li>'
  '<li><b>Lamba si ulucul</b> — se imbuca. Vara scandura se contracta si, daca sunt crude, apare o dunga deschisa de lemn nevopsit pe fiecare rost, pe tot peretele.</li>'
  '<li><b>Capetele taiate</b> — lemnul trage apa prin capat de zece pana la douazeci de ori mai repede decat prin fata. Fiecare taietura e o gura deschisa. Se pensuleaza pe loc, imediat dupa taiere.</li>'
  '</ul>'
  '<p>Lasi sa se usuce cat scrie pe galeata. Ai nevoie de loc: 4-5 scanduri de 4 m, vopsite pe ambele fete, nu se pot atinge intre ele. Doua capre si niste sipci de distantare.</p>', None),
 ('Lambriul, apoi al doilea strat',
  '<p>Insurubezi scandurile cat peretele e culcat: primul rand jos, fiecare rand calca peste cel de sub el, un surub inox 4×50 in fiecare verticala.</p>'
  '<p>La final, <b>al doilea strat de lazura peste tot peretele</b>, cat inca sta pe iarba. Acopera capetele suruburilor si urmele de la manipulare, si iese o suprafata uniforma in loc de 9 scanduri vopsite fiecare putin altfel.</p>', None),
 ('Ridicarea — pasul periculos',
  '<p>Panoul cantareste <b>~42-51 kg</b> cu lambriu si vopsea. Trebuie sa ajunga de pe iarba pe punte, la <b>2,2 m</b>. Puntea <b>nu are balustrada</b> — margine libera pe toate laturile, tot capitolul.</p>'  '<p class="why-inline">E cu <b>10 kg mai greu</b> decat scria planul pana pe 21.08, fiindca lambriul a trecut de la 12,5 la 19 mm. Grosimea aia e buna pe perete — nu se cupeaza in soare — dar se plateste exact aici. <b>Peretele asta e singurul care trebuie imbracat inainte de ridicare</b> (dupa aceea raman 30 cm pana la gard). La laterale si la fata poti pune lambriul dupa ce stau in picioare, deci acolo greutatea nu conteaza.</p>'
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
  '<p>Dulapul de <b>200×50</b> (il ai deja), taiat la <b>2200</b>, se aseaza <b>pe muchie, cu 200 in sus</b>, peste cununa peretelui SI peste capetele stalpilor — ambele la 1700 — ca sa faca un reazem continuu la <b>1900</b>. Fixat cu <b>vinclu 70×55 (le ai) pe ambele fete, la ~500 mm</b> + o placa metalica pe fiecare stalp.</p>',
  D2['reazem']),
 ('Talpa in grinzi',
  '<p>Prin podea, in grinzile de dedesubt: <b>surub 6×140 la fiecare 40 cm</b>, pe liniile trase cu creta. Plus coltare metalice pe interior.</p>'
  '<p class="why-inline">Scandurile podelei au doar 28 mm — nu tin nimic singure. La colturile din spate, talpa se prinde in <b>blocajele montate</b>.</p>', None),
])}

<div class="ok"><b>E bine daca:</b> diagonalele au fost egale la asamblare · 8 suruburi groase in stalpi · reazemul de 200×50 calca si pe cununa si pe stalpi · talpa prinsa in grinzi pe toata lungimea, inclusiv la colturi · scandurile complete si vopsite pe toate fetele · peretele nu atinge gardul nicaieri.</div>

{fig(GH['nod_colt_spate'], 'Coltul din spate, in plan. Peretele din spate si cel lateral nu se ating — fiecare se prinde in stalp, cu 8×140 oblice. Bagheta de colt acopera imbinarea lambriului.')}
'''))

# ══════════════════════════════ E3 · peretii laterali ══════════════════════════════
CH.append(dict(id='e3', n='E3', titlu='Peretii laterali',
    sub='Doi pereti, fiecare pe cota lui. Se asambleaza pe punte — sunt prea lungi ca sa fie urcati gata.',
    zi='o zi',
    scule='HS7611K — rigla la lungime · GSR — gauri pilot + suruburi + tocul geamului · fierastrau vertical PST 700 E — golul de geam',
    bon=[
     ('Talpa','rigla 46×46','1580 stanga · 1570 dreapta','2'),
     ('Cununa inclinata','rigla 46×46','1596 stanga · 1586 dreapta','2'),
     ('Verticale','rigla 46×46',VLs,'4 / perete'),
     ('Prag + buiandrug geam','rigla 46×46 (rest)','intre verticalele golului','2 / perete'),
     ('Contrafise','rigla 46×46 (rest)','4× 212 (brat 150)','4 / perete'),
     ('Toc geam','rigla 46×46','gol 490 · geam 440×440','1 / perete'),
     ('Geam fix','plexi 4 mm','440×440','2 total'),
     ('Lambriu','19×116×4000','randuri de 1580 / 1570, cate doua pe scandura','7 / perete'),
    ],
    body=f'''
<p class="lead">Cununa e inclinata — acoperisul urca spre spate — deci fiecare din cele 4 verticale are alta lungime. Cele doua laterale difera intre ele cu 10 mm: nu le taia dupa acelasi tipar.</p>

{fig(D2['lateral'], 'Elevatie la scara. Fata in stanga (mai jos), spate in dreapta (mai sus). Golul de geam centrat, 490×490, prag la 950.')}

<div class="gate"><b>Dreptunghiul casei nu e la echer</b> — e in afara cu ~20 mm. De aceea peretii sunt trapeze usoare, iar <b>fiecare talpa se taie la fata locului</b>, dupa masura reala dintre stalpi, nu din tabel.</div>

{fig(GH['lat_stanga'], 'Perete lateral stanga — talpa 1580, cununa 1596', wide=True)}

{fig(GH['lat_dreapta'], 'Perete lateral dreapta — talpa 1570, cununa 1586. <a class="dwg" href="SCHEME-2D-casa.html#lateral">desenul la scara →</a>', wide=True)}

{fig(GH['lat_sect'], 'Sectiune prin perete — rama 46x46, lambriu 12,5x96 in falt')}

{steps([
 ('Rama, pe punte',
  '<p>Talpa (rigla 46×46): <b>1580</b> pe latura din stanga (S1–S3), <b>1570</b> pe dreapta (S2–S4). Cununa inclinata: <b>1596</b> stanga, <b>1586</b> dreapta.</p>'
  f'<p>Cele 4 verticale, dinspre fata spre spate: <b>{VLs}</b>. Sunt diferite intentionat — nu le incurca intre ele. Marcaje pe talpa, de la fata: <span class="mono">0 · camp · camp+490 · capat</span>. Campul e <b>545</b> pe stanga (talpa 1580), <b>540</b> pe dreapta (1570).</p>', None),
 ('Golul de geam',
  '<p>Golul de <b>490</b> se centreaza pe talpa: campul = (talpa − 490) / 2. Pe stanga (1580) iese <b>545 · 490 · 545</b>, pe dreapta (1570) <b>540 · 490 · 540</b>. Golul ramane 490 pe amandoua; doar campul difera. Intre verticalele care margineau golul pui un <b>prag la 950</b> si un buiandrug deasupra, la 950+490. Aceeasi metoda ca la orice fereastra.</p>'
  + fig(GH['lat_geam'], 'Golul de geam — acrilic 440 in gol 490, 25 mm joc de jur imprejur'),
  None),
 ('Echerul si contrafisele',
  '<p>Verticalele perpendiculare pe talpa, cununa la panta ei. Cand forma e buna, pui contrafise in <b>toate cele 4 colturi</b>: rigla 46×46 taiata la <b>212</b> pe diagonala (brat de 150). Cate 2 suruburi <b>6×80</b> la capat.</p>'
  + fig(GH['lat_colt'], 'Coltul — contrafisa 212 pe diagonala, brat 150'),
  None),
 ('Lazura si lambriu — aceeasi ordine ca la spate',
  '<p>Lazura pe rama intai, cat mai ai acces la toate fetele. Apoi tai scandurile, le vopsesti pe toate cele sase suprafete (fata, spate, lamba, uluc, ambele capete), le lasi sa se usuce, le montezi, si dai al doilea strat peste tot peretele.</p>'
  '<p>Golul de geam ramane liber. <b>Vopseste si canturile golului</b> — sunt capete taiate, trag apa cel mai repede.</p>', None),
 ('Tocul geamului',
  '<p>In golul de 490 intra un <b>toc separat</b> din rigla 46×46, iar geamul fix de <b>440×440</b> (plexi de 4 mm) se prinde cu <b>sipci pe ambele fete</b>. Gaurile in plexi se dau cu <b>+1 mm</b> fata de surub — altfel plexiul crapa la strans. Geamul propriu-zis se monteaza la E6, din exterior.</p>', None),
 ('Prinderea peretelui',
  '<p>Talpa in grinzile de dedesubt: <b>6×140 la fiecare 40 cm</b>. La colturi, unde se intalneste cu peretele din spate si cu cel din fata: cate <b>2 vincluri Parkside 40×40 pe colt</b>.</p>', None),
])}

<div class="ok"><b>E bine daca:</b> ambele laterale stau la echer pe podea · golul de geam e 490 curat, cu prag la 950 · contrafise in toate colturile · talpa prinsa in grinzi si colturile in vincluri.</div>

<div class="warn"><p>Al doilea perete lateral are <b>alte cote</b> (talpa 1570, cununa 1586). Nu-l taia dupa primul — masoara-l separat pe latura lui.</p></div>

{fig(GH['nod_sus_spate'], 'Capatul din spate al peretelui lateral. Trece cu 193 peste cununa spatelui, pe langa dulapul de reazem, pana sub caprior.')}
{fig(GH['nod_sus_fata'], 'Capatul din fata. Se opreste sub caprior, langa bara de 100×60. Cununa inclinata se taie lunga si se scrie la fata locului — asa inghite si cei 20 mm de echer.')}
'''))

# ══════════════════════════════ E4 · peretele din fata ══════════════════════════════
CH.append(dict(id='e4', n='E4', titlu='Peretele din fata',
    sub='Peretele cu usa si fereastra. Doua lucruri se fac altfel: bara de sus e solida, iar usa se taie la final.',
    zi='o zi',
    scule='HS7611K — rigla si bara de sus 100×60 · GSR — gauri pilot + suruburile oblice · fierastrau sabie — taierea talpii la usa, la final',
    bon=[
     ('Talpa (intreaga)','rigla 46×46','1970','1'),
     ('Verticale (jambe + montanti)','rigla 46×46',str(VF),'5'),
     ('Prag + buiandrug fereastra','rigla 46×46 (rest)','570, intre jambe','2'),
     ('Bara de sus','bara solida 100×60 (o ai)','2155','1'),
     ('Contrafise sus','rigla 46×46 (rest)','2× 212 (brat 150)','2'),
     ('Contrafisa jos-dreapta','rigla 46×46 (rest)','~350 (brat 250)','1'),
     ('Fereastra','PVC 56×56 (cumparata)','—','1'),
     ('Lambriu','19×116×4000','bucati sub 940 — ies din capetele pastrate','6 sau 0'),
    ],
    body=f'''
<p class="lead">Are doua lucruri care nu mai apar nicaieri: lemnul de sus e o <b>bara solida</b>, nu o rama, iar golul de usa se taie <b>la final</b>, dupa ce peretele e ridicat si legat — altfel isi pierde rigiditatea la transport.</p>

{fig(D2['fata'], f'Elevatie la scara. Cinci verticale de {VF}, bara de sus 100×60 peste amandoi stalpii, fereastra la stanga, usa la mijloc. <a class="dwg" href="SCHEME-2D-casa.html#fata">desenul la scara →</a>')}

{steps([
 ('Rama — cu talpa INTREAGA',
  '<p>Talpa (rigla 46×46) taiata la <b>1970</b>, <b>necrestata inca pentru usa</b>. Cinci verticale de <b>{VF}</b> (= 1600 − o singura talpa de {TT}; sus nu e cununa, e bara solida). Masurate de la fata interioara a stalpului stang: <span class="mono">115 · fereastra 161→731 · usa 938→1488 · montant de camp 1650→1696</span>, plus coltul de <b>274</b> pentru propteaua de jos.</p>', None),
 ('Fereastra',
  '<p>Intre jambe (161→731), gol <b>570×570</b>, prag la <b>950</b> de la podea, exact ca la geamurile laterale. Aici intra <b>fereastra PVC de 56×56</b> — singura care se deschide, spre terasa. Se monteaza la E6.</p>', GH['fata_fereastra']),
 ('Bara de sus',
  '<p>Nu rama, nu laminat: <b>bara solida 100×60</b> (o ai), cu latura de <b>60 in sus</b>, taiata la <b>2155</b>. Trebuie sa calce pe rama SI pe amandoi stalpii — de aia e mai lunga decat peretele. Nu se inlocuieste cu rigla.</p>', GH['fata_bara']),
 ('Contrafisele',
  '<p>Sus: <b>2× 212</b> (brat 150). Jos-dreapta: una lunga, <b>~350</b> (brat 250). Jos-stanga <b>se sare</b> — acolo coltul e chiar stalpul de 90×90, deja rigid.</p>', None),
 ('Vopsea, lambriu, ridicare',
  '<p>Lazura pe rama, apoi scandurile vopsite pe toate cele sase suprafete, apoi lambriul peste tot mai putin zona usii, apoi al doilea strat. Aceeasi ordine ca la spate.</p>'
  '<p>Peretele asta are cele mai multe taieturi scurte — bucati de 938, 482, 207, 161. <b>Fiecare are doua capete</b>, deci sunt ~90 de capete de pensulat. Le faci pe masura ce tai, nu la sfarsit.</p>'
  '<p>Apoi se ridica pe punte, ca la spate: doi oameni, culcat pe muchie, legat de stalpi provizoriu.</p>', None),
 ('Prinderea finala a stalpilor',
  '<p><b>Stalpii sunt deja pe santier</b> — 90×90, montati la 1600 peste podea. Aici nu se ridica niciun stalp; se face doar legatura definitiva.</p>'
  '<p>La fiecare stalp: <b>4 suruburi de dulgherie 8×140</b> infiletate <b>oblic, la ~15-20°</b>, in grinda de dedesubt (2 de-o parte, 2 de cealalta) + <b>un vinclu 90×60 (le ai) pe fiecare fata</b> a stalpului. Tot de sus, <b>fara piulite</b>.</p>'
  '<p class="why-inline">Nu exista tije M12 in podea si nu au existat niciodata. Nu cauta gauri de bulon — nu sunt.</p>', GH['fata_stalp']),
 ('Usa — abia acum',
  '<p>Dupa ce peretele e ridicat, legat si <b>verificat la echer</b>: tai talpa pentru usa. Gol de <b>550</b> latime, care lasa <b>1600 liber</b>.</p>'
  '<p class="why-inline">Daca tai talpa mai devreme, peretele se indoaie la transport si la ridicare. Talpa intreaga il tine drept pana sus.</p>', GH['fata_usa']),
])}

<div class="ok"><b>E bine daca:</b> talpa a stat intreaga pana dupa ridicare · bara de sus calca pe amandoi stalpii · stalpii prinsi cu 4 suruburi oblice + coltar fiecare, fara tije · golul de usa taiat la final, 550 latime, 1600 liber.</div>

{fig(GH['nod_colt_fata'], 'Coltul din fata, in plan. Acelasi nod ca la spate, pe stalp de 90×90.')}
'''))

# ══════════════════════════════ E5 · acoperisul ══════════════════════════════
CH.append(dict(id='e5', n='E5', titlu='Acoperisul',
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

{fig(D2['acoperis'], 'Plan acoperis. Cinci capriori in dreptul verticalelor, doua placi de OSB, inchideri de 454 intre capriori. <a class="dwg" href="SCHEME-2D-casa.html#acoperis">desenul la scara →</a>')}

{steps([
 ('Lamineaza capriorii — singurul lemn laminat',
  '<p>Capriorii sunt <b>44×100</b>, facuti din <b>2 scanduri de 22×100</b> insurubate una peste alta cu <b>4×40 in zigzag la 300 mm</b>. 5 capriori de <b>1889</b> → <b>5 bare, doua straturi pe caprior</b> (o bara de 4000 da doua straturi de 1889). A 6-a bara da cele 4 inchideri de 454; a 7-a e rezerva.</p>'
  '<p class="why-inline">Capriorii NU trec pe rigla 46×46 — sectiunea patrata s-ar indoi la spanul de 1670. Aici, si numai aici, se lamineaza.</p>', None),
 ('Aseaza capriorii',
  '<p>Pas <b>498</b> intre ei, in dreptul verticalelor din pereti. <b>Orientarea conteaza: 100 pe verticala, 44 pe orizontala.</b> Pus invers, capriorul lucreaza pe axa slaba. Fiecare capat: <b>2 vincluri Parkside 40×40</b> — caprior 44 lat, vinclu 40, incape.</p>', None),
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

# ══════════════════════════════ E6 · geamurile si verificarea finala ══════════════════════════════
CH.append(dict(id='e6', n='E6', titlu='Geamurile si verificarea finala',
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
  '<p>Doua geamuri fixe de <b>440×440</b> (plexi de 4 mm, amandoua dintr-o placa de 500×1000), in tocul pregatit la E3. Sipci pe <b>ambele fete</b>, gaurile in plexi cu <b>+1 mm</b> fata de surub. Montate <b>din exterior</b>, cu un rost de silicon pe contur.</p>', GH['lat_geam']),
 ('Fereastra din fata',
  '<p>Fereastra PVC de <b>56×56</b> in golul de 570×570, prinsa in jambe, siliconata pe contur. Se deschide spre terasa — singura care se deschide.</p>', GH['fata_fereastra']),
])}

<h3>Checklist final</h3>

<div class="balustrada">
<b>Balustrada nu exista.</b> Terasa are margine libera la 2,2 m. Casa poate fi terminata integral, cu toate bifele verzi, si copiii tot nu au voie sus. Balustrada e faza urmatoare (F2). Pana atunci, scara se ia de langa punte intre sesiunile de lucru.
</div>

{steps([
 ('Colturile din spate au blocaj',
  '<p>Toate 4 montate — podeaua inchisa integral. Talpa peretelui din spate se prinde in ele.</p>', None),
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
  '<p>Lazura pe toate fetele, inclusiv capetele taiate. Verifici ca n-a ramas lemn crud pe niciun cant si in niciun rost. Scara luata de langa punte.</p>', None),
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


.mat{margin:16px 0;background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.mat .mhead{padding:13px 16px;font:600 12px/1.3 var(--sans);letter-spacing:.06em;
 border-bottom:1px solid var(--line);color:var(--acc)}
.mgrid{display:grid;grid-template-columns:1fr 1fr;gap:0}
.mcol{padding:14px 16px}
.mcol+.mcol{border-left:1px solid var(--line)}
.mcol h4{margin:0 0 10px;font:600 10.5px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase}
.mcol.buy h4{color:var(--acc2)}
.mcol.have h4{color:var(--acc)}
.mcol ul{list-style:none;margin:0;padding:0}
.mcol li{display:flex;gap:11px;padding:7px 0;border-top:1px solid var(--line);align-items:baseline}
.mcol li:first-child{border-top:0}
.mq{flex:0 0 78px;font:600 13.5px var(--mono);text-align:right;letter-spacing:-.01em}
.mcol.buy .mq{color:var(--acc2)}
.mcol.have .mq{color:var(--acc)}
.mn{flex:1;font-size:14.5px;line-height:1.4}
.mnote{color:var(--dim);font-size:12.5px;line-height:1.45;margin-top:2px}
table.cump{table-layout:fixed;width:100%}
table.cump td.q{white-space:nowrap}
table.cump td:last-child,table.cump th:last-child{width:42%}
.uses{margin-top:5px;font:11px var(--mono);color:var(--dim)}
.mtab td.swc{width:34px}
.sw{display:inline-block;width:26px;height:14px;border:1px solid var(--ink);border-radius:2px;position:relative;overflow:hidden;vertical-align:-2px}
.sw-hx{position:absolute;inset:0;background:repeating-linear-gradient(45deg,#00000026 0 2.6px,transparent 2.6px 8px)}
.mtab td .chip{margin-left:3px}
.uses .chip{display:inline-block;text-decoration:none;color:var(--acc);border:1px solid var(--line);
 border-radius:6px;padding:1px 7px;margin-right:4px}
.uses .chip:hover{background:var(--acc-s)}
.matback{float:right;font:11px var(--mono);color:var(--dim);text-decoration:none;text-transform:none;letter-spacing:0}
.matback:hover{color:var(--acc)}
.exist{background:var(--acc-s);border:1px solid var(--line);border-left:3px solid var(--acc);
 border-radius:12px;padding:14px 16px;margin:16px 0;font-size:14.5px}
.dwg{display:inline-block;margin-top:8px;font:11px var(--mono);color:var(--acc);text-decoration:none;
 border:1px solid var(--line);border-radius:6px;padding:3px 9px}
.dwg:hover{background:var(--acc-s)}
@media(max-width:720px){
 table.cump,table.cump tbody,table.cump tr,table.cump td{display:block;width:auto}
 table.cump tr:first-child{display:none}
 table.cump tr{border-top:1px solid var(--line);padding:9px 0}
 table.cump td{border:0;padding:1px 0}
 table.cump td:first-child{font-weight:600}
 table.cump td.q{display:inline-block;margin-right:12px;color:var(--acc2)}
 table.cump td:last-child{width:auto;color:var(--dim);font-size:12.5px;line-height:1.45;margin-top:3px}
}
@media(max-width:720px){ .mgrid{grid-template-columns:1fr} .mcol+.mcol{border-left:0;border-top:1px solid var(--line)} .mq{flex-basis:66px} }
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
main a{color:var(--acc);text-decoration:underline;text-underline-offset:2px;text-decoration-thickness:1px}
main a:hover{color:var(--acc2)}
.matlinks{margin-top:2px;font:11px/1.5 var(--mono);color:var(--dim)}
.matlinks a{color:var(--acc)}
td.q a,.cump a{font-family:var(--mono);font-size:12px;white-space:nowrap}
.backlink{font:11px var(--mono);color:var(--dim);margin:0 0 6px}
.backlink a{color:var(--acc)}
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

 allBoxes.forEach(function(inp){
   inp.addEventListener('change',function(){
     if(inp.checked) set(inp.dataset.key,'1'); else del(inp.dataset.key);
     updProgress();
   });
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
     updProgress();
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

 updProgress();
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
                f'<div class="gb-txt"><b>Blocat de {pn}.</b> {c["blocat_motiv"]} '
                f'<a href="GHID-E0-golul-din-spate.html">Desenele E0 →</a></div>'
                f'<button class="gb-skip" type="button">sar peste</button></div>')
        skipw = (f'<div class="skipwarn" style="display:none"><b>Ai sarit peste blocajul {pn}.</b> '
                 f'{c["blocat_motiv"]}</div>')
    bon_html = bon(c['bon']) if c.get('bon') else ''
    mat_html = mat(c['id'])
    return f'''<section id="{c['id']}" data-ch="{c['id']}">
<header class="ch"><div class="cn-big">{c['n']}</div><h2>{c['titlu']}</h2><p class="chsub">{c['sub']}</p>
<div class="chmeta"><span class="zi">{c['zi']}</span>{scule}</div></header>
{gate}{skipw}
<div class="chbody">
{bon_html}
{mat_html}
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
 <div class="meta">21 august 2026 · cote in mm<br>geometrie masurata pe santier</div>
 <label class="phone-jump"><select id="jump">{opts}</select></label>
 <ol>{nav}</ol>
 <div class="prog">progres global <span id="pt">0 / 0</span><div class="bar"><i id="pb"></i></div>
  <div class="navbtns"><button class="tgl" onclick="tt()">lumina / intuneric</button><button id="resetAll" type="button">sterge toate bifele</button></div>
 </div>
</nav>
<main>
{secs}
<footer class="doc">
GHID-CONSTRUCTIE-casa · 21.08.2026 · E1–E6 · documentul de executie al casei.<br>
Cotele vin din masuratorile de santier (<code>MASURATORI-CONFIRMARE-2026-08-20</code>).<br>
Desene la scara: <code>SCHEME-2D-casa.html</code> · cumparaturi: <code>LISTA-LEROY-2026-08-17</code>.<br>
Bifele se tin minte in browser (localStorage) — raman dupa refresh. Butonul „sterge toate bifele" le sterge.
</footer>
</main>
</div>
{SCRIPT}
</body></html>'''

open('GHID-CONSTRUCTIE-casa.html','w',encoding='utf-8').write(HTML)
print('scris', len(HTML), 'caractere ·', len(CH), 'capitole')
