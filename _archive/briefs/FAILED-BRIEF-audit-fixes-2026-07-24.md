MODEL: opus

# BRIEF — audit fixes 2026-07-24

## GOAL

Aliniaza toate documentele si livrabilele la starea reala a santierului si la deciziile din 24.07, conform `AUDIT-2026-07-24.md` (I1-I17). Numai documentatie — zero schimbari de design in rest.

## DECIZII LUATE (nu le rediscuta)

- Cote: MIGRARE LA AS-BUILT. Lantul canonic: **varf stalpi fata / top polita+talpic = 1900 → top glulam = 2100 → top joiste = 2200 → top dusumea = 2228**. Vechiul lant 1872/2072/2172/2200 devine istoric; unde ramane mentionat, marcheaza "(plan initial 1872)".
- Talpic (P0 STR-01): **INCHIS as-built 24.07.** Fizic: talpic sub fiecare polita, fixat pe fata stalpului cu **3× Heco 8x200** + cele 2 tije M12 (pozitie/anti-smulgere) + **contrafisa 45°** sub nod. Nu e crestatura; redundanta a 3 cai de incarcare, acceptata pentru structura temporara (demontare ~2028).
- Balustrada: **PARCATA** (decizie 1000 vs 1100 amanata explicit de Vlad 24.07). NU modifica nimic legat de balustrada/M10 nicaieri.
- Receptie C2/inox: ramane DESCHISA (Vlad n-a numarat). Nu alinia cantitatile "platite"; doar pastreaza itemul deschis.
- Joiste (decizie 24.07): joistele de capat ALINIATE cu stalpii (X=0 si 2100, axa stalpilor), calaresc proeminenta glulamului spate, trecand prin fata stalpilor spate intregi; **capetele se dubleaza** (sister joist); pozitii intermediare raman 280/720/1120/1550; **toate 6+2 egale, taiate DOAR dupa masuratoare as-built** (tinta ~2430-2450, NU 2550); blocaje + ancore M12 inainte de dusumea; dusumeaua se decupeaza la stalpii spate.

## EDITS (per fisier)

1. `SOURCE-OF-TRUTH.md`: (a) Cote blocate → lantul as-built de mai sus; "Stalpi fata: taiati ~1900 (plan initial 1872)"; "Podea: +2228". (b) Goluri deschise: P0 talpic → "INCHIS 24.07 — doc in 386f755, fizic confirmat de Vlad (3× Heco 8x200 + M12 + contrafisa); de verificat contrafisa prezenta la AMBELE noduri spate". (c) Receptie ramane deschis, adauga "Vlad numara la urmatoarea iesire". (d) Adauga item "PARCAT: balustrada 1000 vs 1100 — nu propaga nimic pana la decizie". (e) Coloana stare "actual dupa fix talpic" → "actual".
2. Cote as-built in: `PODEA-plan-sectiune.html`, `PODEA-impactum.html`, `NODURI-grinda-stalp.html`, `CASUTA-DIN-COPAC.md`, `casuta-din-copac.html`, iar pentru fise EXCLUSIV prin generator (`tools-fise/` — fb.py/emit2.py), apoi regenereaza. Niciun edit direct in `fisa-*.html`.
3. `NODURI-grinda-stalp.html` + fisa-03 (generator): adauga nota as-built nod spate: "As-built 24.07: talpic fixat pe fata cu 3× Heco 8x200 + 2 M12 + contrafisa 45° sub nod (nu crestatura). Verifica contrafisa la ambele noduri."
4. Joiste (decizia de mai sus) in: `PODEA-plan-sectiune.html`, `PODEA-impactum.html`, generator fise unde apar offseturi/lungimi, `CASUTA-DIN-COPAC.md`. Tracker `Debitare`: joiste "taie dupa masuratoare as-built (~2430-2450)"; adauga rand "2× joista suplimentara pt dublare capete — DE CUMPARAT, lungime dupa masuratoare".
5. `timeline.html`: p2 eticheta "la 1872" → "la ~1900" (p2 ramane NEbifat — nivelul +2200 nefacut). p3 eticheta → "Talpic + polite pe stalpii din spate (+1900)". Bifeaza itemii acoperiti de starea confirmata 24.07: polite+talpic montate, grinda spate montata, grinda fata montata. Joistele = in curs, nebifat.
6. `STATUS.md`, intrarea "2026-07-22 (Vlad, poza)": prefixeaza cu "**[RETRACTAT 07-23: pozele erau EXIF 10 iul — verificarea foto nu se sustine; taierea ramane acceptata pe raportul verbal, 07-23.]** " — nu sterge textul original.
7. `materiale.html`: adauga rand talpic (2× bloc 100x100 ~180, din offcut, 0 lei) in sectiunea potrivita. Apoi regenereaza `PDF/06-Materiale.pdf`.
8. Tracker, foaia "Platforma premium": statusuri "De cumparat" → "SOSIT 18.06" DOAR pentru piesele pe care foile Materiale/Comanda le au SOSIT. Nu atinge cantitatile C2/inox.
9. `CASA-plan-constructie.html`: sectiunea de layout stalpi casa → stalpii casei stau pe joistele de capat DUBLATE, aliniati in dreptunghiul celor 4 stalpi ai structurii; banner sus: "Layout actualizat 24.07; cut list de refacut dupa masuratorile as-built — NU taia dupa lista veche." Nu redesena restul.
10. `AUDIT-2026-07-23.html`: banner: "Actualizat 24.07 — cauza celor 3 briefuri esuate: OAuth Builder expirat (v. brief v4); starea constatarilor: AUDIT-2026-07-24.md." Leaga `AUDIT-2026-06-18.html` + `AUDIT-2026-07-23.html` in `desene.html` (sectiune "Audituri").
11. `AUDIT-2026-06-18.html`: banner de stare per STR: "STR-01 INCHIS 24.07 (talpic as-built + contrafisa). STR-02 (M12x140): regula acceptata — OK daca piulita prinde filet complet; verificare pe santier DESCHISA. STR-03 (consola anti-uplift) si STR-04 (contrafise): partial — contrafisa nod spate montata 24.07; restul DESCHIS."
12. `project-instructions.md`: linia cu perete 1300 → "Cote si decizii curente: guverneaza SOURCE-OF-TRUTH.md (pereti 1800 spate / 1500 fata, acoperis intr-o apa, lant inaltimi as-built 1900/2100/2200/2228)."
13. Igiena: muta `DONE-BRIEF-talpic-propagation.md` + `DONE-BRIEF-reconcile-publish-cleanup.md` in `_archive/briefs/`; `git add` pozele noi din `POZE/` (IMG_2270-2288).
14. Regenereaza TOATE fisele + TOATE PDF-urile (build_pdfs.py); niciun PDF mai vechi decat sursa lui.
15. STATUS.md: o intrare noua cu ce ai facut + hash-uri. Commit-uri logice separate (cote / talpic+joiste / igiena). **NU face push** — pushul ramane la Vlad.

## DONE MEANS

- `grep -rn "2072" *.html` → doar aparitii marcate "plan initial"; zero in fise regenerate.
- `timeline.html` p3 contine "Talpic"; p2 contine "~1900" si nu e bifat.
- STATUS intrarea 07-22 contine "[RETRACTAT".
- `materiale.html` contine "talpic"; `PDF/06-Materiale.pdf` mai nou decat `materiale.html`.
- Diff-ul NU atinge nimic cu "balustrada", "1100", "M10".
- `desene.html` linkuiaza ambele audituri; `project-instructions.md` contine "SOURCE-OF-TRUTH".
- Zero DONE-BRIEF in radacina; `git status` curat (poze comise).

## IF STUCK

- Orice conflict de cifre: castiga lantul 1900/2100/2200/2228 si decizia de joiste de mai sus.
- Daca geometria noua nu inchide intr-un desen (generator sau PODEA), nu improviza: noteaza vizibil "layout 24.07, desen de refacut" si marcheaza NEEDS-INPUT cu diff-ul incercat.
- Fisele se ating NUMAI prin generator; daca generatorul nu acopera un text, NEEDS-INPUT.
