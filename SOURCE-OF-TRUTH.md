# SURSA DE ADEVAR — Casuta din copac

Un singur loc care spune CINE guverneaza fiecare tip de informatie.
Regula: daca doua fisiere se contrazic, castiga fisierul canonic din tabelul de mai jos. Restul se aliniaza la el.

> **Actualizat 20.08.2026.** Geometria casei de sus a fost remasurata pe santier si e complet alta decat in planul vechi — adancimea reala e **1575**, nu 1100. Toate cotele casei din documentele de dinainte de 20.08 sunt moarte. Vezi `AUDIT-2026-08-20.md` pentru ce s-a gasit si de ce.

## Cine guverneaza ce

| Domeniu | Fisier canonic | Stare |
|---|---|---|
| **Casa de sus — executie, pasi, cumparaturi** | `PROIECT-CASA-2026-08-17.html` / `.pdf` (v3) | **canonic, 20.08** |
| **Casa de sus — desene la scara** | `SCHEME-CASA-2026-08-17.html` / `.pdf` (v4) | **canonic, 20.08** |
| **Casa de sus — lista de cumparaturi** | `LISTA-LEROY-2026-08-17.html` / `.pdf` | **canonic, 20.08** |
| **Casa de sus — masuratorile de santier** | `MASURATORI-CONFIRMARE-2026-08-20.html` | **canonic, 20.08** — cotele brute + verificarea geometrica |
| Casa de sus — detalii de perete (geam bucata cu bucata, straturi) | `GHID-SIMPLU-casa.html` | canonic **doar pe detaliile de perete**; geometria lui e istorica |
| Golul de podea de la colturile din spate | `BLOCAJ-COLT-2026-08-20.html` / `.pdf` | canonic — inlocuieste Detaliul 7 din SCHEME |
| Geometrie / cote — restul proiectului (structura, podea, stalpi) | `CASUTA-DIN-COPAC.md` | actual |
| Cantitati / buget / comanda | `Tracker_materiale_casuta.xlsx` | actual (vezi gol receptie) |
| Cerinte structurale | `Fisa-santier-casuta.pdf` (review 10.07) | actual |
| Instructiuni montaj (Faza 1) | `tools-fise/` -> `fisa-01..11` | actual |
| Noduri grinda-stalp | `NODURI-grinda-stalp.html` | actual |
| Podea (plan + sectiune) | `PODEA-plan-sectiune.html` | actual |
| Faza 2 — balustrada si scara | `MANUAL-FAZA-2.html` / `.pdf` | actual **doar pe balustrada si scara**; sectiunea F4 (casa) e depasita |
| Stadiu santier | `STATUS.md` + `timeline.html` | actual |
| Audit tehnic | `AUDIT-2026-08-20.md` (curent) · 08-17, 08-11, 08-06, 07-24, 07-23, 06-18 (istorice) | actual |

**Pe casa de sus, PROIECT-CASA bate orice alt fisier**, inclusiv MANUAL-FAZA-2 si GHID-SIMPLU. Singura exceptie: detaliile fine de perete raman in GHID (montajul geamului, straturile), pentru ca acolo GHID e mai detaliat si nu contrazice geometria noua.

Documentele absorbite sunt in `_archive/`.

## Cote blocate

### Structura si podeaua (as-built, migrat 24.07 — neschimbate)

Lant canonic de inaltimi: **varf stalpi fata / top polita+talpic = 1900 → top glulam = 2100 → top joiste = 2200 → top dusumea = 2228.** Vechiul lant 1872/2072/2172/2200 e istoric.

- Cadru 4 stalpi: 2100 × 1780, diagonale 2750.
- Podea (top dusumea): +2228 de la sol.
- Stalpi spate: intregi, 4 m. Stalpi fata (ai puntii): taiati ~1900.
- Consola balcon: 700.
- Balustrada (decizie 06.08): 1000 general, 1100 pe consola; goluri sub 90; M10 total 16 (8 stalpisori × 2).

### Casa de sus — MASURAT 20.08, inlocuieste tot ce era inainte

Cotele sunt **lumina intre fetele stalpilor**. Sursa: `MASURATORI-CONFIRMARE-2026-08-20.html`.

| | sus | jos | se taie pe |
|---|---|---|---|
| latime SPATE | 2000 | 1995 | **1990** |
| latime FATA | 1975 | 1985 | **1970** |
| adancime S1–S3 | 1600 | 1580 | **1580** |
| adancime S2–S4 | 1570 | 1570 | **1570** |

- Stalpi: **100×100 spate, 90×90 fata** — verificate cu ruleta. Peste podea: 1700 spate, **1600 fata (M5 confirmat 20.08)**.
- Adancime de proiectare **1575**. Span intre reazeme **1670**.
- Reazeme: spate **1900** (perete 1700 + dulap real 200×50 pe muchie), fata **1660** (stalp 1600 + bara solida 100×60).
- Cadere 240 → **panta 8,2°**. Caprior **1889**. Streasina 100 fata + 100 spate. FARA jgheab. Muchia la **1646** peste podea.
- **Acoperis pe astereala continua de OSB3 12 mm, NU pe sipci.** Sub 10° producatorul Onduline cere suport continuu (verificat pe uk.onduline.com). Sipcile si sipca diagonala au iesit din plan.
- Verticale: spate **1612** ×5 · fata **1556** ×5 · laterale **1581 · 1653 · 1730 · 1802**, cate 4 pe perete.
- Goluri (neschimbate, sunt cote de siguranta): usa **550** cu **1600** liber · geam lateral **490×490**, prag 950 · fereastra fata gol **570×570**.
- Pereti: lambriu 12,5×96 **direct pe rama** — fara folie, fara sipci de aerisire, fara OSB pe pereti. Contrafise in colturi. Interior liber.
- Dreptunghiul stalpilor e in afara echerului cu ~20 mm: **peretii sunt trapeze usoare, fiecare talpa se taie la fata locului**.
- Scara AMANATA (11.08) — va fi o varianta mai usoara, discutie separata.

## Goluri deschise (de inchis)

- **[P0 SIGURANTA — DESCHIS 20.08] Balustrada nu e in checklist-ul final al casei.** `PROIECT-CASA` §9 a fost corectat, dar regula generala ramane: **casa terminata nu inseamna punte sigura**. Copiii nu urca pana la balustrada F2.
- **[GATE — DESCHIS] Golul de podea la colturile din spate.** Se rezolva cu blocaj + 2 vincluri ca polite, per `BLOCAJ-COLT-2026-08-20`. **Obligatoriu inainte de S2** — talpa peretelui din spate nu are in ce se prinde acolo. De facut de 4 ori (2 laturi × 2 colturi).
- **[DESCHIS] Poze la colturile din spate** — nefacute; de confirmat ca solutia se potriveste cu terenul.
- **[INCHIS 20.08] Cioata de 1,5 m de pe terasa.** Se retează la ~600-750 si devine masuta. La 1500 varful ar fi stat la ~138 mm sub muchia acoperisului = treapta directa pe Onduline.
- **[P2 COMANDA] Receptie C2 / inox — DESCHIS.** Cantitatile "platite" nu-s inca reconciliate.
- **[INCHIS 24.07] Talpic sub polita spate.** Fizic confirmat: talpic pe fata stalpului, 3× Heco 8×200 + 2 tije M12 + contrafisa 45°. *(Tijele astea sunt reale si sunt la nodul grinda-stalp — a nu se confunda cu presupusele tije M12 din podea, la stalpii casei, care nu au existat niciodata.)*
- **[INCHIS 06.08] Balustrada 1000 vs 1100** si **dublarea joistelor (sisters) — SKIP DEFINITIV.**
- **[P2 BUGET] All-in.** Baza Faza 1 = 8500 (Tracker). Casa de sus **~3.360-3.500** (LISTA-LEROY, recalculat 20.08). Total ~11.900-12.000.

## Trasee moarte — nu le reinvia

Daca le gasesti scrise ca active intr-un document vechi, documentul e depasit, nu planul:

reazem 1950 · fata 1642 · panta 15,6° sau 10,2° · caprior 1342 sau 1331 · dulap 46×250 (real e 200×50) · adancime casa 1100 · latime 2000 peste tot · verticale laterale 1556/1709/1862 sau 1712 · sipci de acoperis si sipca diagonala · streasina 200 · jgheab si burlan · OSB sau folie **pe pereti** (pe acoperis OSB e obligatoriu) · sipci de aerisire · diagonale in X pe pereti · acrilic 500×250 · contrafise cu brate de 300 uniform · **doua tije M12 in podea la stalpii casei — nu au existat niciodata** · tirfoane M10 si ancore anti-vant · lemn de 42×90 (nu exista la Leroy) · lemn de scara din barele 200×50.

## Reguli de propagare

- Cotele **casei de sus** se schimba INTAI in `PROIECT-CASA`, apoi in SCHEME (prin `gen_scheme.py`), apoi in LISTA.
- Cotele **restului proiectului** se schimba INTAI in `CASUTA-DIN-COPAC.md`, apoi in site / fise / 3D.
- Cantitatile se schimba INTAI in `Tracker`, apoi in `materiale.html`.
- Instructiunile de montaj Faza 1 se schimba in `tools-fise/` (generatorul), NU direct in `fisa-*.html` — se suprascriu la regenerare.
- Desenele casei se schimba in `gen_scheme.py`, NU direct in HTML — SVG-urile se suprascriu la regenerare. Textul din jurul lor (captions, legende) e intretinut manual.
- Orice contradictie se rezolva in favoarea fisierului canonic de mai sus.
