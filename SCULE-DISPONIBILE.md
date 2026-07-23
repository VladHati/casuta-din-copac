# Scule pe care le am (inventar real)

Actualizat: 2026-07-22. Aceasta e situatia REALA (ce ai in mana, azi).
`scule.html` = lista ideala de pe Hornbach, pentru poze/linkuri de recunoscut pe raft — nu o confunda cu asta.

---

## AM — scule cu fir (vechi)

| Scula | Model | Specs | Alimentare |
|---|---|---|---|
| Fierastrau circular manual | Makita **HS7611K** | 1600 W, 5500 rpm, disc 190 mm, adancime **65-66 mm** la 90°, ghidaj lateral | cablu 230 V |
| Fierastrau sabie | Makita **JR3070CT** | 1510 W, cursa 32 mm | cablu 230 V |
| Fierastrau vertical (pendular) | Bosch **PST 700 E** | 500 W, taie **70 mm** in lemn, talpa inclinabila 45°, SDS schimbare panza | cablu 230 V |
| Slefuitor cu excentric | Makita **BO5041** | 300 W, taler 125 mm, 4000-10000 osc/min | cablu 230 V |
| Polizor unghiular | Makita **9558HNRG** | disc 125 mm | cablu 230 V |

## AM — set nou 18V Bosch Professional (cumparat 22 iulie 2026, Dedeman)

**Set 0615A50090** — 1.771 lei, cod produs Dedeman 1107913. Verificat live pe pagina produsului (pret, stoc si specs confirmate 22 iulie 2026):

| Componenta | Specs |
|---|---|
| **GDR 18V-215** (impact) | brushless, **215 Nm** max, 0-2100 rpm, pana la 3.800 percutii/min, 2 trepte de torsiune, prindere hexagon **1/4"** |
| **GSR 18V-65** (gaurit/insurubat) | brushless, **31/63 Nm**, 0-550 / 0-2100 rpm (2 viteze), cap scurt 166 mm, mandrina **13 mm**, ambreiaj (1-20 + simbol burghiu), KickBack Control, LED |
| Acumulatori | **2× 5 Ah** + incarcator rapid |
| Valiza | plastic, robusta |
| Garantie | 24 luni (extins la 3 ani daca inregistrezi produsul la Bosch) |

**Asta rezolva blocantul principal al proiectului**: masina de gaurit-insurubat 18V, mandrina 13mm, ambreiaj, ≥60 Nm, 2 acumulatori noi ≥4 Ah. GSR 18V-65 trece toate pragurile (63 Nm, 5 Ah).

**De ce doua scule, nu una:** GDR (impact, fara ambreiaj) da cei 100 de Heco 8×200 structurali. GSR (cu ambreiaj) da cele 300 de suruburi inox 5×60 la dusumea si gaurile pilot — un impact fara ambreiaj infunda capetele Heco sub lemn (pierzi reazemul la nodul de smulgere de la consola) si rupe capetele de inox (nu se mai scot din larice).

**Ghid de utilizare pentru cineva care nu a mai folosit sculele astea:** `GHID-scule-insurubat.md` (reglaje, ambreiaj, siguranta, exercitiu de 20 min inainte de prima zi de montaj).

## AM — scula veche de gaurit, pastrata ca a doua masina

| Scula | Model | Specs | Rol fix |
|---|---|---|---|
| Masina de gaurit / insurubat cu percutie | Makita **HP347DWE** | 14,4 V, mandrina 10 mm, 30 Nm dur/15 Nm moale, 2× acumulatori **1,5 Ah** (~6-7 ani, uzati) | **doar** gauri pilot 4-5mm, adancituri, suruburi usoare — niciodata 8×200, niciodata burghiul de 12mm |

Acumulatorii ei cad in sarcina mare, nu in repaus — de-aia ii dai treaba usoara, nu suruburile grele. Fara upgrade posibil: platforma G-series (BL1413G/BL1415G) e separata de LXT si practic abandonata.

## Acumulatori — 3 ecosisteme, nu le amesteca

- **Bosch verde** (Power for All, 1600A011T8/1600A00ZR8) — sculele de gradina, nu ale proiectului.
- **Makita G-series** (in HP347DWE) — separata de LXT, muribunda, fara upgrade.
- **Bosch Professional albastru** (nou, in setul GDR/GSR) — platforma principala a proiectului de acum inainte.

---

## CE MAI LIPSESTE — blocante ramase

### 1. Fierastrau care taie DREPT prin 100×100 — acum URGENT

Niciuna din sculele de mai sus rezolva asta: HS7611K (66mm, insuficient), JR3070CT (trece, dar niciodata drept — scula de demolare), PST 700E (70mm nominal, dar panza fuge in lateral in material gros). Capul stalpului e portant — taietura stramba = reazem pe muchie (`AUDIT-2026-06-18.html`, review 2026-07-10).

**De ce e urgent acum:** conform STATUS.md (22 iulie), toti 4 stalpii sunt in pozitie si verificati la nivela. Urmatorul pas (`timeline.html`, pasul 2) e taierea stalpilor din fata la 1872mm — exact taietura pentru care nu ai scula potrivita.

**Metoda: DECISA 22 iulie — varianta B.** Tai cu HS7611K pe toate 4 fetele (trasat cu echer) + finisezi miezul (~30mm) cu panza de mana. Panza de mana — confirmata direct de Vlad in chat (fierastrau clasic occidental, de impins), detinuta deja. Varianta A (inchiriat) respinsa.

**Executia fizica insa ramane NECONFIRMATA.** Vlad a spus ca stalpii sunt deja taiati, dar n-a trimis nicio poza (verificat: folder uploads gol). Nu presupune „gata" pe timeline.html/STATUS.md pana nu vine o poza clara a taieturii reale.

### 2. Burghiu de 12mm lung, pentru buloanele M12
Masoara intai grosimea reala prin care trece bulonul (stalp + grinda + papuc). Bosch Expert Self Cut Speed 12×400mm (auto-avans, coada hexagonala) — varianta de 95mm de la Dedeman e prea scurta daca gauresti prin 100×100.

### 3. Accesorii mici
- Biti Torx impact-rated, 50-55mm: T40 (Heco 8×200), T30 (Heco 6×100/6×80), T25 (inox 5×60, verifica pe cutie). Pe impact driver, bitii obisnuiti se rup, nu doar se uzeaza.
- Suport magnetic pentru biti (impact-rated).
- Adancitor (countersink), optional, pentru capete de surub la nivel la dusumea.

### 4. Curent la copac
Toate sculele cu fir + acum si un al treilea incarcator → prelungitor pe tambur (sectiune corecta) + PRCD/diferential portabil (lucrezi afara, pe pamant).

---

## URMATOAREA ACHIZITIE (in ordine)

1. ~~Masina de gaurit-insurubat 18V, mandrina 13mm, ≥60Nm~~ — **REZOLVAT 22 iulie** (setul Bosch 0615A50090).
2. ~~Metoda de taiere~~ — **REZOLVAT 22 iulie** (varianta B, panza de mana confirmata detinuta). Ramane doar de confirmat FIZIC ca taierea a avut loc — poza inca neprimita.
3. Burghiu lemn 12mm lung (auto-avans, coada hexagonala).
4. Biti Torx impact-rated T40/T30/T25 + suport magnetic.
5. Prelungitor tambur + PRCD.
6. Chei tubulare + clichet pentru M12/M10 (verifica daca ai deja).
7. Cleme de strangere ×2-4 (verifica daca ai deja).
8. Disc de metal 125mm pentru polizor (taiat tija M12).

Nota lifespan: casuta e temporara (~2028). Fierastraul de retezat e scula de specialitate pentru un weekend — inchiriaza, nu cumpara. Setul de gaurit-insurubat e altceva: cea mai folosita scula dintr-o casa, te tine 10+ ani indiferent de casuta — nu se socoteste la bugetul proiectului.
