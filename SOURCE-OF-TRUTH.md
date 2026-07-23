# SURSA DE ADEVAR — Casuta din copac

Un singur loc care spune CINE guverneaza fiecare tip de informatie.
Regula: daca doua fisiere se contrazic, castiga fisierul canonic din tabelul de mai jos. Restul se aliniaza la el.

## Cine guverneaza ce

| Domeniu | Fisier canonic | Stare |
|---|---|---|
| Geometrie / cote | `CASUTA-DIN-COPAC.md` | actual |
| Cantitati / buget / comanda | `Tracker_materiale_casuta.xlsx` | actual (vezi gol receptie) |
| Cerinte structurale | `Fisa-santier-casuta.pdf` (review 10.07) | actual |
| Instructiuni montaj | `tools-fise/` -> `fisa-01..11` + Manual | actual dupa fix talpic |
| Noduri grinda-stalp | `NODURI-grinda-stalp.html` | actual |
| Podea (plan + sectiune) | `PODEA-plan-sectiune.html` | actual |
| Casa de sus | `CASA-plan-constructie.html` | actual (invelitoare + usa de ales) |
| Stadiu santier | `STATUS.md` + `timeline.html` | actual |
| Audit tehnic | `AUDIT-2026-07-23.html` (curent), `AUDIT-2026-06-18.html` (ultimul complet) | actual |

## Cote blocate (rezumat — detaliul e in dosar)

- Cadru 4 stalpi: 2100 x 1780, diagonale 2750.
- Podea: +2200 de la sol.
- Stalpi spate: intregi, 4 m. Stalpi fata: taiati (~1872 pe plan, ~1900 pe teren).
- Consola balcon: 700.
- Perete casa de sus: 1800 spate / 1500 fata (inlocuieste vechiul 1300).
- Balustrada: 1000, goluri sub 90.

## Goluri deschise (de inchis)

- **[P0 SIGURANTA] Talpic sub polita spate.** Blocul de compresiune lipseste din fise / tracker / 3D. Fizic: se pune sub polita INAINTE de incarcarea grinzii. Doc: `BRIEF-talpic-propagation.md`.
- **[P2 COMANDA] Receptie.** C2: 14 necesare vs 12 platite. Inox: 3 pachete necesare vs 2 platite. De verificat la receptie / cumparat diferenta.
- **[P2 BUGET] All-in.** Baza Faza 1 = 8500 (Tracker). Casa de sus ~1900-2100 (CASA-plan). Total ~10.400-10.600. Cifra veche 6600 (din `DE-LUAT-AZI-Hornbach.html`) e depasita — fisier arhivat.

## Reguli de propagare

- Cotele se schimba INTAI in `CASUTA-DIN-COPAC.md`, apoi in site / fise / 3D.
- Cantitatile se schimba INTAI in `Tracker`, apoi in `materiale.html`.
- Instructiunile de montaj se schimba in `tools-fise/` (generatorul), NU direct in `fisa-*.html` (se suprascriu la regenerare).
- Orice contradictie se rezolva in favoarea fisierului canonic de mai sus.
