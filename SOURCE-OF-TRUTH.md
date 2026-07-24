# SURSA DE ADEVAR — Casuta din copac

Un singur loc care spune CINE guverneaza fiecare tip de informatie.
Regula: daca doua fisiere se contrazic, castiga fisierul canonic din tabelul de mai jos. Restul se aliniaza la el.

## Cine guverneaza ce

| Domeniu | Fisier canonic | Stare |
|---|---|---|
| Geometrie / cote | `CASUTA-DIN-COPAC.md` | actual |
| Cantitati / buget / comanda | `Tracker_materiale_casuta.xlsx` | actual (vezi gol receptie) |
| Cerinte structurale | `Fisa-santier-casuta.pdf` (review 10.07) | actual |
| Instructiuni montaj | `tools-fise/` -> `fisa-01..11` + Manual | actual |
| Noduri grinda-stalp | `NODURI-grinda-stalp.html` | actual |
| Podea (plan + sectiune) | `PODEA-plan-sectiune.html` | actual |
| Faza podea (instructiuni de santier) | `FISA-CONTINUARE-podea.html` / `.pdf` | actual (as-built 24.07) |
| Casa de sus | `CASA-plan-constructie.html` | actual (invelitoare + usa de ales) |
| Stadiu santier | `STATUS.md` + `timeline.html` | actual |
| Audit tehnic | `AUDIT-2026-07-24.md` (curent), `AUDIT-2026-07-23.html` + `AUDIT-2026-06-18.html` (istorice, cu banner de stare) | actual |

## Cote blocate (rezumat — detaliul e in dosar)

Lant canonic de inaltimi **as-built** (migrat 24.07): **varf stalpi fata / top polita+talpic = 1900 → top glulam = 2100 → top joiste = 2200 → top dusumea = 2228.** Vechiul lant 1872/2072/2172/2200 e istoric; unde ramane mentionat, e marcat "(plan initial ...)".

- Cadru 4 stalpi: 2100 x 1780, diagonale 2750.
- Podea (top dusumea): +2228 de la sol.
- Stalpi spate: intregi, 4 m. Stalpi fata: taiati ~1900 (plan initial 1872).
- Consola balcon: 700.
- Perete casa de sus: 1800 spate / 1500 fata (inlocuieste vechiul 1300).
- Balustrada: 1000, goluri sub 90.

## Goluri deschise (de inchis)

- **[P0 SIGURANTA — INCHIS 24.07] Talpic sub polita spate.** Propagarea in fise / tracker / 3D e FACUTA (commit 386f755). Fizic confirmat de Vlad: talpic sub fiecare polita, fixat pe fata stalpului cu 3× Heco 8x200 + 2 tije M12 (pozitie/anti-smulgere) + contrafisa 45° sub nod. DE VERIFICAT pe teren: contrafisa prezenta la AMBELE noduri spate.
- **[P2 COMANDA] Receptie C2 / inox — DESCHIS.** Cantitatile "platite" nu-s inca reconciliate (Vlad n-a numarat). Vlad numara la urmatoarea iesire, apoi se aliniaza.
- **[PARCAT] Balustrada 1000 vs 1100.** Decizie amanata explicit de Vlad (24.07). Nu propaga nimic legat de balustrada/inaltime/M10 pana la decizie.
- **[P2 BUGET] All-in.** Baza Faza 1 = 8500 (Tracker). Casa de sus ~1900-2100 (CASA-plan). Total ~10.400-10.600. Cifra veche 6600 (din `DE-LUAT-AZI-Hornbach.html`) e depasita — fisier arhivat.

## Reguli de propagare

- Cotele se schimba INTAI in `CASUTA-DIN-COPAC.md`, apoi in site / fise / 3D.
- Cantitatile se schimba INTAI in `Tracker`, apoi in `materiale.html`.
- Instructiunile de montaj se schimba in `tools-fise/` (generatorul), NU direct in `fisa-*.html` (se suprascriu la regenerare).
- Orice contradictie se rezolva in favoarea fisierului canonic de mai sus.
