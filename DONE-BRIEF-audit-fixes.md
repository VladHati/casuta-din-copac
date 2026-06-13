MODEL: opus

# BRIEF — Reparatii din auditul 13.06.2026

## GOAL
Repara cele 11 defecte gasite in audit (vezi `AUDIT-2026-06-13.html` / `PDF/Audit-complet-2026-06-13.pdf`), la SURSA (generatorul de fise), regenereaza fisele + PDF-urile, actualizeaza documentatia, commit + push pe `main` (deploy automat Netlify). Doua puncte raman blocate pe aprobarea lui Vlad — vezi APROBARI.

## DE STIUT INAINTE
- Fisele HTML (`fisa-01..11.html`, `fise.html`) sunt GENERATE de `tools-fise/fb.py` + `tools-fise/book.py`. NU edita fisa-*.html direct — modifica `fb.py` si regenereaza, altfel reapare la urmatorul build.
- PDF-urile de fisa + manualul combinat vin din `tools-fise/book.py`. PDF-urile de sectiune (00,02,03,04,05,06) vin din `build_pdfs.py`. Sunt doua sisteme.
- Inchide trackerul in LibreOffice inainte de editare (exista `.~lock.Tracker_materiale_casuta.xlsx#`).

## REPARATII (in ordine)

### F2 — stalpisor „7x7" → „58x58"
`tools-fise/fb.py`, dictionarul de piese (~L230): schimba
`'SB':('POZE/lemn.png','Stalpisor 7x7 (Faza 2)')`
in
`'SB':('POZE/lemn.png','Stalpisor 58x58')`

### F4 — taiere copac, eticheta gresita
In sursa fisei 7 din `tools-fise/fb.py` (textul si eticheta SVG cu „+2780"): schimba
`Reteaza corcodusul la ~+2780 (deasupra podelei).`
in
`Reteaza corcodusul la ~+2780 de la sol (≈580 peste podea).`
Eticheta SVG „reteaza la +2780" ramane, dar daca are subtext „deasupra podelei" scoate-l.

### F3 — surub coltar C1 (APROBARE NECESARA, vezi mai jos)
Daca Vlad confirma „6×100": in `tools-fise/fb.py` fisa-05 (~L210) schimba chip-ul `('H1','~12','in coltare')` in `('H2','~12','in coltare')`; si in `imbinari.html` nodul A schimba „Heco 8×200" → „Heco 6×100" (in text si in chip-ul „Heco 8×200 ×4"). NU atinge nodul D (contrafise) — acolo 8×200 e corect.

### Regenereaza dupa F2/F3/F4
Ruleaza `tools-fise/book.py` (regenereaza fisa-*.html + Fisa-*.pdf + Manual-Faza-1-complet.pdf + Fise-montaj-Faza-1.pdf). Apoi `python3 build_pdfs.py` pentru sectiuni daca s-a schimbat imbinari.html. Verifica: niciun „7x7" si niciun „(deasupra podelei)" ramas in fisa-*.html.

### F1 — granita de faza (APROBARE NECESARA)
Tinta recomandata: balustrada + masa = FAZA 1; Faza 2 = doar pereti, acoperis, scara. Aplica DOAR daca Vlad aproba aceasta granita. Atunci aliniaza:
- `ghid-montaj.html` L440 footer: scoate „balustrada" si „masa-copac" din lista Faza 2 → „Urmeaza Faza 2: pereti, acoperis, scara."
- `tools-fise/book.py` L30: muta SB/SP/MC/BM din grupul „Faza 2 / de ales" in grupul Faza 1; scoate „(Faza 2)" de pe etichete.
- `tools-fise/fb.py`: orice „(Faza 2)" pe piese de balustrada → scos.

### F6 — README „Structura"
Rescrie sectiunea „Structura" din `README.md`:
- Adauga paginile reale lipsa: `materiale.html`, `fise.html`, `fisa-01..11.html`, `scule.html`, `timeline.html`, `modele-3d.html`.
- Marcheaza redirect-urile ca atare: `catalog-piese.html`→materiale, `comanda-corespondent.html`→materiale, `imbinari-ghid.html`→imbinari, `imbinari-3d-ghid.html`→imbinari.
- Corecteaza afirmatia despre PDF: sectiunile (00,02,03,04,05,06) din `build_pdfs.py`; fisele + manualul din `tools-fise/book.py`.

### F7 — tracker „11 trepte”
In `Tracker_materiale_casuta.xlsx`, foaia „Platforma premium”: in celula Rol a randului trepte si in nota de jos, „11 trepte” → „10 trepte (11 niveluri)”. Cantitatea 10 ramane.

### F8 — cod mort
Confirma ca nimic activ nu importa `fise_gen.py` / `fise_emit.py` / `fise_build.py` / `fise_index.py` (doar se refera intre ele). Muta-le in `tools-fise/_arhiva/`. Nu sterge fb.py/book.py/det.py/iso.py/emit2.py/idx2.py.

### F10 / F11
F10: nu commite `.~lock.*#` (e deja in .gitignore — doar verifica). F11: optional, adauga un „01-” logic la sectiuni sau lasa cum e (cosmetic, fara actiune obligatorie).

## CONSTRAINTS
- Romana fara diacritice. Estetica curata, luminoasa (nu dark) — neschimbata.
- NU atinge cotele structurale (2200/1872/2072, consola 700, glulam 90×200, joiste 100×100, pozitii joiste). Sunt verificate corecte.
- Modifica DOAR ce e listat aici.

## DONE MEANS
- `grep -rn "7x7" fisa-*.html` → 0 rezultate; balustrada apare „58×58" peste tot.
- `grep -rn "deasupra podelei" fisa-*.html` → 0 rezultate.
- PDF-urile Fisa-01..11 au mtime nou (regenerate dupa editari).
- README „Structura" listeaza fise.html + fisa-01..11 si materiale.html; redirect-urile marcate.
- Tracker: „10 trepte (11 niveluri)”.
- (Daca aprobat F1) niciun fisier nu mai pune balustrada/masa in Faza 2.
- (Daca aprobat F3) C1 nu mai foloseste 8×200; nodul D inca da.
- Push pe `main` reusit; site live actualizat in ~1 min.

## APROBARI (asteapta raspunsul lui Vlad inainte de aceste doua)
1. **F1 granita de faza** — balustrada+masa in Faza 1 (recomandat) sau ramane Faza 2? Restul reparatiilor merg oricum.
2. **F3 surub C1** — confirma „Heco 6×100 in coltarul C1" (sau surubul de conector recomandat de producatorul coltarului Alberts). Pana la confirmare, lasa F3 nefacut si raporteaza-l ca pending.

## IF STUCK
- Daca `book.py` nu ruleaza (lipsa weasyprint/pango), instaleaza si reia; nu sari regenerarea PDF.
- Daca o eroare nu se gaseste la linia indicata (cod schimbat de la audit), cauta dupa string (`7x7`, `deasupra podelei`, `11 trepte`, `(Faza 2)`) si aplica acolo.
- Orice altceva neclar: nu inventa cote — opreste si raporteaza in STATUS.md.
