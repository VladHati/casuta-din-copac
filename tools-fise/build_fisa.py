# -*- coding: utf-8 -*-
from gen_cf import VIEWS

HEAD = """<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="utf-8">
<title>FISA MONTAJ — CONTRAVANTUIRI | Casuta din copac</title>
<style>
  @page { size: A4; margin: 13mm 12mm; }
  * { box-sizing: border-box; }
  body { font-family: Helvetica, Arial, sans-serif; font-size: 9.5pt; color: #1a1a1a; line-height: 1.45; margin: 0; }
  h1 { font-size: 17pt; margin: 0 0 2mm; letter-spacing: -0.3pt; }
  .sub { color: #555; font-size: 8.5pt; margin-bottom: 4mm; }
  h2 { font-size: 11.5pt; margin: 6mm 0 2mm; padding-bottom: 1mm; border-bottom: 1.5pt solid #1a1a1a; }
  h3 { font-size: 10pt; margin: 4mm 0 1.5mm; }
  table { border-collapse: collapse; width: 100%; margin: 2mm 0; }
  th, td { border: 0.5pt solid #999; padding: 1.4mm 2mm; text-align: left; vertical-align: top; font-size: 8.5pt; }
  th { background: #efefef; font-size: 8pt; text-transform: uppercase; letter-spacing: 0.4pt; }
  .mono { font-family: "Courier New", monospace; font-weight: bold; white-space: nowrap; }
  .warn { border: 1.5pt solid #b3261e; background: #fdf1f0; padding: 3mm 4mm; margin: 3mm 0; }
  .warn b { color: #b3261e; }
  .note { border-left: 2.5pt solid #1a1a1a; background: #f5f5f5; padding: 2mm 3mm; margin: 2mm 0; font-size: 8.8pt; }
  .fix { border: 1.2pt solid #1a6b3c; background: #f0f7f2; padding: 2.5mm 3.5mm; margin: 3mm 0; font-size: 8.8pt; }
  .fix b { color: #1a6b3c; }
  ul, ol { margin: 1mm 0 2mm; padding-left: 5mm; }
  li { margin-bottom: 1.2mm; }
  .step { border: 0.8pt solid #1a1a1a; margin: 3mm 0; page-break-inside: avoid; }
  .step-head { background: #1a1a1a; color: #fff; padding: 1.6mm 3mm; font-weight: bold; font-size: 10pt; }
  .step-body { padding: 2.5mm 3mm; }
  .gata { border: 0.8pt dashed #1a1a1a; background: #f7f7f2; padding: 2mm 3mm; margin: 2mm 0 0; font-size: 8.8pt; }
  .chk { color: #555; }
  svg { display: block; margin: 2mm auto; }
  .cap { text-align: center; font-size: 8pt; color: #555; margin-bottom: 3mm; }
  .pgbrk { page-break-before: always; }
  .fig { page-break-inside: avoid; margin: 3mm 0 4mm; }
</style>
</head>
<body>
"""


def fig(key, cap):
    return f'<div class="fig">{VIEWS[key]}<div class="cap">{cap}</div></div>'


BODY = f"""
<h1>FISA MONTAJ — CONTRAVANTUIRI</h1>
<div class="sub">7 august 2026 &#183; se face pe structura as-built (podea partiala, X-uri temporare inca montate) &#183;
inlocuieste <b>Fisa 9/11</b>, care a fost desenata pe alta geometrie &#183;
<b>7 piese</b>, din care 6 din offcut 100&#215;100</div>

<div class="warn">
<b>Trei reguli care nu se negociaza:</b>
<ol>
<li><b>Un plan pe rand.</b> Monteaza ambele contrafise dintr-un plan, verifica aplombul, si abia apoi scoate X-ul temporar din acel plan. Doua plane descoperite simultan = cadrul se poate deforma cu tine pe scara.</li>
<li><b>Proptelele de la varful stalpilor din spate NU se ating.</b> Ele raman pana la peretii casei (F4). Fisa asta scoate doar X-urile de la baza.</li>
<li><b>Contrafisa prinsa la AMBELE capete</b> inainte sa atingi orice proptea. O contrafisa prinsa doar sus e o bucata de lemn atarnata.</li>
</ol>
</div>

<h2>De ce ai nevoie de asta acum</h2>
<p>Baza stalpilor e articulata &#8212; papuc U + M12 prin aripi. Papucul tine stalpul sa nu se ridice si sa nu alunece,
dar <b>nu-l tine drept</b>. Tot ce opreste azi structura sa se legene lateral sunt X-urile temporare.
Le scoti fara sa pui contrafise si ramai cu patru picioare articulate sub o podea de 2,2 m.</p>

<div class="fix">
<b>Contrafisele 45&#176; de sub talpic, la nodurile din spate, nu se pun la socoteala.</b>
Alea sunt reazem local in compresiune sub polita &#8212; tin nodul sa nu cedeze in jos.
Contravantuirea e alt lucru: tine cadrul sa nu se deformeze lateral. Cele doua nu se substituie.
</div>

<div class="note">
<b>Dusumeaua ajuta, dar nu rezolva.</b> Cand e integral insurubata pe cele 6 joiste devine o diafragma buna
&#8212; adica planul podelei nu se mai deformeaza. Nu impiedica insa stalpii sa se incline sub ea.
De aia contrafisele merg in planele <i>verticale</i>.
</div>

<h2>Corectia fata de Fisa 9/11</h2>
<p>Fisa 9 spune 6 contrafise, taiate ca pene si prinse in colt. Pe geometria construita nu merge peste tot:</p>
<table>
<tr><th style="width:22%">Ce zicea Fisa 9</th><th style="width:39%">De ce nu merge as-built</th><th>Ce faci in loc</th></tr>
<tr><td>Pene taiate la 45&#176; in coltul stalp&#8211;grinda</td>
    <td>La stalpii din <b>fata</b> nu exista colt: stalpul se termina exact la 1900, unde incepe glulamul. Nu ai doua fete perpendiculare in care sa se aseze pana.</td>
    <td>Contrafise <b>prinse plat pe fetele laterale</b>, peste ambele piese. Nu se taie in colt, se suprapun.</td></tr>
<tr><td>3&#215; Heco 8&#215;200 la fiecare capat</td>
    <td>Contrafisa e 100 groasa. 8&#215;200 patrunde 100 mm: iese exact la fata pe spatele stalpului (100) si <b>10 mm afara</b> prin glulam (90). Varf de surub la inaltimea unui copil.</td>
    <td><b>Heco 8&#215;160</b> &#8212; 60 mm patrundere, nu iese nicaieri. De cumparat, nu-i ai.</td></tr>
<tr><td>Cate o contrafisa in planul stang, drept si fata</td>
    <td>Planul <b>spate</b> lipsea din numaratoare. Acolo glulamul sta <b>in fata</b> stalpilor, nu peste ei, deci nici pana, nici contrafisa scurta nu au unde sa se prinda.</td>
    <td>O <b>diagonala lunga</b> (CF7) pe fetele din fata ale stalpilor spate, sub cota 1900.</td></tr>
<tr><td>Contrafisa sub nasul consolei, separat</td>
    <td>Ar fi a 7-a si a 8-a piesa degeaba: contrafisa transversala de pe stalpul din fata poate merge <b>inainte</b> in loc de inapoi si face ambele treburi.</td>
    <td><b>CF3 / CF4</b> merg spre nas. Contravantuiesc planul lateral <i>si</i> proptesc consola.</td></tr>
</table>

<h2>Cele 7 piese</h2>
<table>
<tr><th>#</th><th>Plan</th><th>De la</th><th>La</th><th>Jos</th><th>Sus</th><th>Deschidere</th><th>Pe ce fata se prinde</th></tr>
<tr><td class="mono">CF1</td><td>Fata</td><td>stalp S4</td><td>glulam fata</td><td class="mono">1400</td><td class="mono">2000</td><td class="mono">600 spre S3</td><td>fata dinspre <b>interior</b> (sub podea)</td></tr>
<tr><td class="mono">CF2</td><td>Fata</td><td>stalp S3</td><td>glulam fata</td><td class="mono">1400</td><td class="mono">2000</td><td class="mono">600 spre S4</td><td>idem, in oglinda</td></tr>
<tr><td class="mono">CF3</td><td>Lateral stanga</td><td>stalp S4</td><td>joista x=0, spre nas</td><td class="mono">1500</td><td class="mono">2150</td><td class="mono">650 inainte</td><td>fata exterioara (spre stanga)</td></tr>
<tr><td class="mono">CF4</td><td>Lateral dreapta</td><td>stalp S3</td><td>joista x=2100, spre nas</td><td class="mono">1500</td><td class="mono">2150</td><td class="mono">650 inainte</td><td>fata exterioara (spre dreapta)</td></tr>
<tr><td class="mono">CF5</td><td>Lateral stanga</td><td>stalp S1</td><td>joista x=0</td><td class="mono">1450</td><td class="mono">2150</td><td class="mono">700 inainte</td><td>fata exterioara (spre stanga)</td></tr>
<tr><td class="mono">CF6</td><td>Lateral dreapta</td><td>stalp S2</td><td>joista x=2100</td><td class="mono">1450</td><td class="mono">2150</td><td class="mono">700 inainte</td><td>fata exterioara (spre dreapta)</td></tr>
<tr><td class="mono">CF7</td><td>Spate</td><td>stalp S1</td><td>stalp S2</td><td class="mono">700 (S1)</td><td class="mono">1400 (S2)</td><td class="mono">2100</td><td>fetele dinspre curte ale ambilor stalpi spate</td></tr>
</table>

<div class="note">
<b>Cotele sunt masurate de la sol</b>, acelasi reper ca lantul as-built (1900 / 2100 / 2200 / 2228).
Marcheaza-le pe stalp cu creionul si o ruleta lunga inainte sa tai ceva.
</div>

<h2>Cut list si feronerie</h2>
<table>
<tr><th>Piesa</th><th>Sectiune</th><th>Lungime taiata</th><th>Buc</th><th>De unde</th></tr>
<tr><td>CF1, CF2</td><td class="mono">100&#215;100</td><td class="mono">950</td><td>2</td><td>offcut stalpi / joiste</td></tr>
<tr><td>CF3, CF4</td><td class="mono">100&#215;100</td><td class="mono">1050</td><td>2</td><td>offcut</td></tr>
<tr><td>CF5, CF6</td><td class="mono">100&#215;100</td><td class="mono">1120</td><td>2</td><td>offcut</td></tr>
<tr><td>CF7</td><td class="mono">45&#215;145</td><td class="mono">2400</td><td>1</td><td><b>de cumparat</b> &#183; 1 rigla 2500&#8211;3000</td></tr>
<tr><td>Blocaj de reazem sub CF3 / CF4</td><td class="mono">90&#215;100</td><td class="mono">120</td><td>2</td><td>offcut</td></tr>
<tr><td>Heco 8&#215;160 (sau 8&#215;180 doar in stalpi)</td><td>&#8212;</td><td>&#8212;</td><td>~40</td><td><b>de cumparat</b> &#183; 1 cutie</td></tr>
<tr><td>Heco 8&#215;120 (capetele CF7, rigla de 45)</td><td>&#8212;</td><td>&#8212;</td><td>6</td><td>8&#215;160 prin 45 ar iesi prin stalp &#8212; ia 6 buc separat</td></tr>
</table>
<p><b>Total de cumparat: 1 rigla 45&#215;145 + 1 cutie Heco 8&#215;160.</b> Restul iese din offcut. Lungimile de taiere includ
~100 mm rezerva la fiecare capat &#8212; tai pe potriveala, la fata locului, dupa ce marchezi cotele pe stalp.</p>

<div class="pgbrk"></div>
<h2>1 &#183; Planul din fata &#8212; CF1, CF2</h2>
{fig('front', 'Elevatie fata &#183; contrafisa prinsa plat peste stalp si peste glulam &#183; deschidere 600, urcare 600, adica exact 45&#176;')}

<div class="warn">
<b>De ce pe fata dinspre interior si nu spre curte.</b> Trunchiul corcodusului trece la ~200 mm in fata
stalpilor, deplasat spre S4, si urca prin toata zona in care ar fi stat CF1 daca o puneai pe fata exterioara
a glulamului. Desenul in plan arata suprapunerea. Pe fata interioara nu atinge nimic, si in plus capetele
de surub raman sub podea, unde nu ajunge nimeni cu mana.
</div>

<div class="note">
<b>Decalajul de 5 mm.</b> Glulamul e 90, stalpul 100. Daca glulamul e centrat pe stalp, fata lui sta cu 5 mm
in spatele fetei stalpului si contrafisa nu reazema pe ambele. <b>Masoara cu o rigla dreapta pusa peste amandoua.</b>
Daca e decalaj, pui o pana de placaj de grosimea masurata sub capatul de sus al contrafisei. Fara pana,
suruburile din glulam preiau tot &#8212; exact ce nu vrei.
</div>

<div class="pgbrk"></div>
<h2>2 &#183; Planul din spate &#8212; CF7</h2>
{fig('back', 'Elevatie spate &#183; glulamul sta IN FATA stalpilor (pe polite), deci nu exista colt pentru o contrafisa scurta &#183; solutia e o diagonala lunga, sub cota 1900')}

<div class="warn">
<b>CF7 e cea mai slaba dintre cele 7</b> &#8212; unghiul iese ~18&#176;, nu 45&#176;, pentru ca talpicul, polita si contrafisele
45&#176; existente ocupa fata stalpului intre 1450 si 1900. O diagonala asa de intinsa lucreaza cu forte mai mari
in suruburi. De aceea: <b>proptelele de la varful stalpilor din spate raman montate pana la peretii casei din F4.</b>
Peretele imbracat in OSB e adevarata contravantuire a planului spate; CF7 e ce poti face pana atunci.
</div>

<div class="note">
<b>Inainte sa gauresti CF7:</b> masoara unde se termina coada contrafisei 45&#176; existente la fiecare stalp spate.
Capatul lui CF7 se aseaza cu cel putin 50 mm sub ea. Daca la S2 coada coboara sub 1400, lasa capatul mai jos
si accepta un unghi si mai mic &#8212; nu tai contrafisa existenta.
</div>

<div class="pgbrk"></div>
<h2>3 &#183; Planele laterale &#8212; CF3, CF5 (si oglinda lor CF4, CF6)</h2>
{fig('side', 'Sectiune prin planul x=0 &#183; CF5 urca din stalpul spate in joista, CF3 urca inainte sub consola &#183; ambele trec pe langa glulame, fara sa le atinga')}

<div class="fix">
<b>Blocajul de reazem sub CF3 / CF4 &#8212; obligatoriu.</b> Astea doua duc si sarcina consolei: cand calca cineva pe nas,
joista apasa in jos pe contrafisa, iar contrafisa impinge in stalp. Daca singurul lucru care o tine sa nu alunece
in jos sunt suruburile, sarcina atarna in forfecare &#8212; <b>fix greseala pe care proiectul a corectat-o deja la polita
din spate cu talpicul</b>. Pui un bloc de 90&#215;100&#215;120 din offcut pe fata stalpului, imediat sub capatul de jos al
contrafisei, cu 3&#215; Heco 8&#215;160. Contrafisa se aseaza pe el. Atunci greutatea trece prin lemn in compresiune,
nu prin suruburi.
</div>

<p><b>De ce merg CF3 si CF4 inainte, nu inapoi:</b> in ambele directii triangulezi planul lateral la fel de bine
&#8212; joista e prinsa de stalp printr-un triunghi in orice caz. Dar numai varianta care merge inainte proptesteste si
nasul consolei de 700. Aceeasi piesa, doua treburi.</p>

<div class="pgbrk"></div>
<h2>Toate cele 7, in plan</h2>
{fig('plan', 'Plan de sus &#183; CF1&#8211;CF2 pe fata interioara a glulamului fata, CF3&#8211;CF6 pe fetele exterioare stanga/dreapta, CF7 pe fetele dinspre curte ale stalpilor spate &#183; niciuna nu cade peste corcodus')}

<h2>Detaliul de prindere &#8212; identic la toate</h2>
{fig('detail', 'Contrafisa suprapusa peste ambele piese &#183; suruburi in triunghi, niciodata in linie &#183; margine minima 40 mm de la capatul contrafisei')}

<table>
<tr><th>Unde</th><th>Cate suruburi</th><th>Lungime</th><th>Patrundere</th><th>De ce</th></tr>
<tr><td>In stalp (100 lat)</td><td>3, in triunghi</td><td class="mono">8&#215;160</td><td class="mono">60 mm</td><td>3 suruburi in triunghi opresc rotirea; 3 in linie nu.</td></tr>
<tr><td>In glulam (90 gros, 200 inalt)</td><td>3, in triunghi</td><td class="mono">8&#215;160</td><td class="mono">60 mm</td><td>Inaltime destula pentru distante de margine confortabile.</td></tr>
<tr><td>In joista (100 inalta)</td><td><b>2</b>, decalate</td><td class="mono">8&#215;160</td><td class="mono">60 mm</td><td>Joista are doar 100 inaltime &#8212; al 3-lea surub ar cadea prea aproape de muchie si crapa lemnul.</td></tr>
<tr><td>Capetele CF7 (45 gros)</td><td>3</td><td class="mono">8&#215;120</td><td class="mono">75 mm</td><td>8&#215;160 prin 45 ar iesi prin stalp.</td></tr>
</table>

<div class="note">
<b>Pregauresti &#216;5 numai prin contrafisa</b>, nu si in piesa din spate. Asa surubul trage contrafisa strans pe fata
stalpului in loc sa o departeze. Insurubezi cu <b>GSR pe ambreiaj</b>, nu cu GDR &#8212; impactul ingroapa capul si rupe filetul in lemn moale.
</div>

<div class="pgbrk"></div>
<h2>Pas cu pas</h2>

<div class="step"><div class="step-head">PAS 1 &#183; Marcheaza cotele, inainte sa tai ceva</div><div class="step-body">
Cu ruleta de la sol, pe fiecare stalp: <span class="mono">1400</span> (CF1/CF2), <span class="mono">1500</span> (CF3/CF4),
<span class="mono">1450</span> (CF5/CF6), <span class="mono">700</span> si <span class="mono">1400</span> pe stalpii spate (CF7).
Trage o linie orizontala scurta cu boloboc, nu doar un punct.
<div class="gata"><b>Gata cand</b> <span class="chk">&#9744;</span> toate cele 4 stalpuri au marcaje vizibile &#183;
<span class="chk">&#9744;</span> ai masurat decalajul stalp&#8211;glulam cu rigla dreapta si l-ai notat</div>
</div></div>

<div class="step"><div class="step-head">PAS 2 &#183; Taie cele 6 contrafise din offcut</div><div class="step-body">
Lungimile din cut list, cu capetele taiate la 45&#176; (cosmetic &#8212; nu reazema pe ele, dar nu agata si scurg apa).
Taie <b>una singura</b> intai, prezint-o pe pozitie, verifica ca acopera minim 250 mm pe fiecare piesa, apoi taie-le pe restul dupa ea.
<div class="gata"><b>Gata cand</b> <span class="chk">&#9744;</span> 6 contrafise + 2 blocaje de reazem taiate &#183;
<span class="chk">&#9744;</span> prima a fost probata pe structura, nu doar masurata pe banc</div>
</div></div>

<div class="step"><div class="step-head">PAS 3 &#183; CRITIC &#183; Planul stanga: CF5, apoi CF3, apoi blocajul de reazem</div><div class="step-body">
Blocajul de reazem se monteaza <b>inainte</b> de CF3, ca sa ai pe ce aseza contrafisa. Prinzi capatul de sus primul
(tine singura), verifici cu bolobocul ca n-ai impins stalpul, apoi capatul de jos.
<b>Abia dupa ce ambele contrafise sunt prinse la ambele capete</b> scoti X-ul temporar de pe stanga.
<div class="gata"><b>Gata cand</b> <span class="chk">&#9744;</span> CF5 + CF3 prinse la ambele capete &#183;
<span class="chk">&#9744;</span> blocaj sub CF3 &#183; <span class="chk">&#9744;</span> stalpii S1 si S4 verificati cu bolobocul dupa &#183;
<span class="chk">&#9744;</span> X-ul de pe stanga scos</div>
</div></div>

<div class="step"><div class="step-head">PAS 4 &#183; CRITIC &#183; Planul dreapta: CF6, CF4, blocaj</div><div class="step-body">
Identic cu pasul 3, in oglinda. X-ul de pe dreapta se scoate ultimul, dupa verificarea cu bolobocul.
<div class="gata"><b>Gata cand</b> <span class="chk">&#9744;</span> CF6 + CF4 + blocaj &#183;
<span class="chk">&#9744;</span> S2 si S3 la aplomb &#183; <span class="chk">&#9744;</span> X-ul de pe dreapta scos</div>
</div></div>

<div class="step"><div class="step-head">PAS 5 &#183; Planul fata: CF1, CF2</div><div class="step-body">
Cu pana de placaj sub capatul de sus, daca ai masurat decalaj la pasul 1. Scoti X-ul din fata la final.
<div class="gata"><b>Gata cand</b> <span class="chk">&#9744;</span> CF1 + CF2 prinse &#183;
<span class="chk">&#9744;</span> pana montata unde era nevoie &#183; <span class="chk">&#9744;</span> X-ul din fata scos</div>
</div></div>

<div class="step"><div class="step-head">PAS 6 &#183; Planul spate: CF7</div><div class="step-body">
Verifici intai unde se termina contrafisele 45&#176; existente si cobori capetele sub ele.
Rigla de 45&#215;145 se ridica in doi oameni &#8212; prinde un surub la fiecare capat, verifica, apoi completeaza la 3.
<b>Proptelele de la varful stalpilor spate raman.</b>
<div class="gata"><b>Gata cand</b> <span class="chk">&#9744;</span> CF7 prinsa cu 3+3 suruburi &#183;
<span class="chk">&#9744;</span> X-ul de la baza planului spate scos &#183; <span class="chk">&#9744;</span> proptelele de la varf INCA montate</div>
</div></div>

<h2>Ordinea, pe scurt</h2>
{fig('seq', 'Un plan pe rand &#183; contrafisa intai, proptea dupa')}

<h2>Gata de tot cand</h2>
<div class="gata">
<span class="chk">&#9744;</span> 7 contrafise montate, fiecare prinsa la ambele capete<br>
<span class="chk">&#9744;</span> 2 blocaje de reazem sub CF3 si CF4<br>
<span class="chk">&#9744;</span> toate cele 4 X-uri temporare de la baza scoase<br>
<span class="chk">&#9744;</span> proptelele de la varful stalpilor din spate INCA pe pozitie (se scot in F4)<br>
<span class="chk">&#9744;</span> niciun varf de surub iesit prin partea cealalta a vreunei piese &#8212; treci cu mana pe toate fetele<br>
<span class="chk">&#9744;</span> te urci pe podea si te legeni intentionat: structura nu mai da din colt
</div>

<h2>De verificat pe teren inainte de a incepe</h2>
<table>
<tr><th>Ce</th><th>De ce conteaza</th><th>Ce faci daca nu se potriveste</th></tr>
<tr><td>Decalajul dintre fata stalpului si fata glulamului la S3/S4</td><td>Decide daca CF1/CF2 au nevoie de pana</td><td>Pana de placaj de grosimea masurata, taiata la latimea contrafisei</td></tr>
<tr><td>Unde se termina coada contrafiselor 45&#176; la S1/S2</td><td>Decide cota capetelor CF7</td><td>Cobori capetele CF7; nu tai niciodata contrafisa existenta</td></tr>
<tr><td>Cat offcut 100&#215;100 mai ai</td><td>Ai nevoie de ~6,2 m liniari</td><td>Daca lipseste, 1 rigla 100&#215;100&#215;3000 acopera doua contrafise</td></tr>
<tr><td>Daca glulamul spate chiar sta in fata stalpilor (nu peste ei)</td><td>Toata plansa 2 se bazeaza pe asta</td><td>Daca sta altfel decat in desen, opreste-te si trimite o poza inainte de CF7</td></tr>
</table>

<div class="note" style="margin-top:5mm">
Fisa asta guverneaza contravantuirile. La contradictie cu Fisa 9/11 sau cu manualul, castiga fisa asta &#8212;
ele au fost desenate inainte ca structura sa fie ridicata. Cotele de baza (1900 / 2100 / 2200 / 2228) raman
cele din <span class="mono">SOURCE-OF-TRUTH.md</span>.
</div>

</body></html>
"""

with open("FISA-MONTAJ-contravantuiri.html", "w", encoding="utf-8") as f:
    f.write(HEAD + BODY)
print("written", len(HEAD + BODY))
