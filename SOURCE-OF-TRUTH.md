# SURSA DE ADEVAR — Casuta din copac

Un singur loc care spune CINE guverneaza fiecare tip de informatie.
Regula: daca doua fisiere se contrazic, castiga fisierul canonic din tabelul de mai jos. Restul se aliniaza la el.

> **Actualizat 20.08.2026.** Geometria casei de sus a fost remasurata pe santier si e complet alta decat in planul vechi — adancimea reala e **1575**, nu 1100. Toate cotele casei din documentele de dinainte de 20.08 sunt moarte. Vezi `AUDIT-2026-08-20.md` pentru ce s-a gasit si de ce.

## Cine guverneaza ce

| Domeniu | Fisier canonic | Stare |
|---|---|---|
| **Casa de sus — executie (pasi, bife, bon de taiere, scule)** | `GHID-CONSTRUCTIE-casa.html` (din `gen_ghid.py` + `gen_2d.py` + `build_ghid.py`) | **canonic, 20.08 — documentul UNIC de executie a casei** |
| **Casa de sus — desene la scara** | `SCHEME-2D-casa.html` (din `gen_2d.py` + `build_2d.py`) | **canonic, 20.08** — anexa de desene a ghidului |
| **Casa de sus — lista de cumparaturi** | `LISTA-LEROY-2026-08-17.html` / `.pdf` | **canonic, 20.08** |
| **Casa de sus — masuratorile de santier** | `MASURATORI-CONFIRMARE-2026-08-20.html` | **canonic, 20.08** — cotele brute + verificarea geometrica |
| Casa de sus — plan / desene / detalii vechi | `PROIECT-CASA-2026-08-17` · `SCHEME-CASA-2026-08-17` · `GHID-SIMPLU-casa` · `PLAN-pereti-lambriu` | **DEPASIT** — poarta bara, inlocuite de GHID-CONSTRUCTIE + SCHEME-2D |
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

**Pe casa de sus, `GHID-CONSTRUCTIE-casa.html` bate orice alt fisier.** Executia, cotele, cumparaturile si detaliile de perete sunt acolo, iar `SCHEME-2D-casa.html` tine desenele la scara. `PROIECT-CASA`, `SCHEME-CASA`, `GHID-SIMPLU` si `PLAN-pereti-lambriu` sunt depasite (poarta bara „DEPASIT"). `MANUAL-FAZA-2` ramane canonic doar pe balustrada si scara (Faza 2), nu pe casa.

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
- Reazeme: spate **1900** (perete 1700 + dulap real 200×50 pe muchie, taiat la 2200), fata **1660** (stalp 1600 + bara solida 100×60, taiata la 2155).
- Cadere 240 → **panta 8,2°**. Caprior **1889** (laminat 44×100, NU pe rigla 48×48). Pas capriori 498, inchideri 454. Streasina 100 fata + 100 spate. FARA jgheab. Muchia la **1646** peste podea.
- **Acoperis pe astereala continua de OSB3 12 mm, NU pe sipci.** Sub 10° producatorul Onduline cere suport continuu (verificat pe uk.onduline.com). Sipcile si sipca diagonala au iesit din plan.
- **Rama tuturor peretilor = rigla 48×48×4000 cumparata gata** (decizie Vlad 20.08, 13 buc). Nu laminat, nu dulap taiat in lung. Talpa si cununa 48, deci verticalele scad cu 8 (fata doar cu 4 — sus e bara solida, nu cununa).
- Verticale: spate **1604** ×5 (= 1700 − 2×48) · fata **1552** ×5 (= 1600 − 48) · laterale **1573 · 1645 · 1722 · 1794**, cate 4 pe perete.
- Goluri (neschimbate, sunt cote de siguranta): usa **550** cu **1600** liber · geam lateral **490×490**, prag 950 · fereastra fata gol **570×570**.
- Pereti: lambriu 12,5×96 **direct pe rama** — fara folie, fara sipci de aerisire, fara OSB pe pereti. Contrafise in colturi. Interior liber.
- Dreptunghiul stalpilor e in afara echerului cu ~20 mm: **peretii sunt trapeze usoare, fiecare talpa se taie la fata locului**.
- Scara AMANATA (11.08) — va fi o varianta mai usoara, discutie separata.

## Goluri deschise (de inchis)

- **[P0 SIGURANTA — DESCHIS 20.08] Balustrada nu e in checklist-ul final al casei.** `PROIECT-CASA` §9 a fost corectat, dar regula generala ramane: **casa terminata nu inseamna punte sigura**. Copiii nu urca pana la balustrada F2.
- **[INCHIS 21.08] Golul de podea la colturile din spate.** Blocajele montate la toate 4 colturile — podeaua inchisa integral.
- **[INCHIS 21.08] Poze la colturile din spate** — confirmat de Vlad 21.08: lucrarea e facuta.
- **[INCHIS 20.08] Cioata de 1,5 m de pe terasa.** Se retează la ~600-750 si devine masuta. La 1500 varful ar fi stat la ~138 mm sub muchia acoperisului = treapta directa pe Onduline.
- **[P2 COMANDA] Receptie C2 / inox — DESCHIS.** Cantitatile "platite" nu-s inca reconciliate.
- **[INCHIS 24.07] Talpic sub polita spate.** Fizic confirmat: talpic pe fata stalpului, 3× Heco 8×200 + 2 tije M12 + contrafisa 45°. *(Tijele astea sunt reale si sunt la nodul grinda-stalp — a nu se confunda cu presupusele tije M12 din podea, la stalpii casei, care nu au existat niciodata.)*
- **[INCHIS 06.08] Balustrada 1000 vs 1100** si **dublarea joistelor (sisters) — SKIP DEFINITIV.**
- **[P2 BUGET] All-in.** Baza Faza 1 = 8500 (Tracker). Casa de sus **~3.360-3.500** (LISTA-LEROY, recalculat 20.08). Total ~11.900-12.000.

## Trasee moarte — nu le reinvia

Daca le gasesti scrise ca active intr-un document vechi, documentul e depasit, nu planul:

**Material si metoda moarta:** rama peretilor din bara laminata 44×100 sau din dulap taiat in lung in fasii de 100 (real: **rigla 48×48 cumparata gata**) · grosime rama T=46 (real 48) · verticale spate 1612 sau 1608, fata 1556, laterale 1581/1653/1730/1802 (real **1604 / 1552 / 1573·1645·1722·1794**) · capriorii pe rigla 48×48 (raman laminati 44×100).

**Geometria moarta:** sipci de acoperis si sipca diagonala (real: astereala OSB) · streasina 200 · jgheab si burlan · OSB sau folie **pe pereti** (pe acoperis OSB e obligatoriu) · sipci de aerisire · diagonale in X pe pereti · acrilic 500×250 · contrafise cu brate de 300 uniform · adancime casa 1100.

**Noduri false care revin des:** **doua tije M12 in podea la stalpii casei — nu au existat niciodata** · tirfoane M10 si ancore anti-vant · lemn de 42×90 (nu exista la Leroy) · lemn de scara din barele 200×50.

## Reguli de propagare

- Cotele **casei de sus** se schimba INTAI in generatoare (`gen_ghid.py` = grosimea ramei T + izometrii · `gen_2d.py` = modelul numeric + desene, cu auto-verificare), apoi se ruleaza `build_ghid.py` + `build_2d.py`, apoi se aliniaza `LISTA-LEROY`.
- Cotele **restului proiectului** se schimba INTAI in `CASUTA-DIN-COPAC.md`, apoi in site / fise / 3D.
- Cantitatile se schimba INTAI in `Tracker`, apoi in `materiale.html`.
- Instructiunile de montaj Faza 1 se schimba in `tools-fise/` (generatorul), NU direct in `fisa-*.html` — se suprascriu la regenerare.
- Desenele casei se schimba in `gen_2d.py` (model unic, auto-verificare la rulare), NU direct in HTML — SVG-urile se suprascriu la `build_ghid.py` / `build_2d.py`. Textul din jur e in `build_2d.py` (lista SECS) si in capitolele din `build_ghid.py`. (`gen_scheme.py` alimenta documentele vechi, acum depasite.)
- Orice contradictie se rezolva in favoarea fisierului canonic de mai sus.
