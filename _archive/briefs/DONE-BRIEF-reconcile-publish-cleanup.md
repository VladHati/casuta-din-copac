MODEL: opus

# BRIEF — Reconciliere: timeline onest + leaga desenele + curatenie + commit

Ruleaza ACEST brief DUPA `BRIEF-talpic-propagation.md` (ca timeline/tracker sa nu fie editate de ambele in acelasi timp).

## GOAL
Adu repo-ul la o singura stare onesta, comisa si publicabila: repara afirmatia din timeline-ul live, leaga cele 4 pagini noi de desene in site, reconciliaza setul de documente, arhiveaza artefactele vechi si comite restanta de 5 saptamani — FARA sa publici afirmatia neverificata "confirmat foto".

## TASKS

### 1. Timeline onest (`timeline.html`, linia 119)
Inlocuieste subtitlul obiectului p2. Actual:
`{id:'p2',g:'Platforma (Faza 1)',l:'2 · Nivel +2200 + taiere stalpi fata la 1872',s:'Stalpii fata taiati (confirmat foto 22 iul); nivel +2200 inca de facut'},`
Nou `s`: `'Stalpii fata taiati la ~1900; nivel +2200 pe stalpii spate inca de facut'` — scoate "confirmat foto". Item-ul ramane DESCHIS (nebifat). Nu marca p2 complet.

### 2. Leaga cele 4 (+1) pagini de desene in site
Fa reachable din nav fiecare: `PODEA-plan-sectiune.html`, `PODEA-impactum.html`, `NODURI-grinda-stalp.html`, `FISA-scule-gauri-grinzi-joiste.html`, `CASA-plan-constructie.html`.
- Creeaza `desene.html` — pagina-index luminoasa (copiaza structura + nav + `assets/site.css` din `modele-3d.html`), care listeaza:
  - "Podea — plan + sectiune" -> `PODEA-plan-sectiune.html` (varianta dark: `PODEA-impactum.html`, link secundar)
  - "Noduri grinda-stalp" -> `NODURI-grinda-stalp.html`
  - "Fisa scule — gauri grinzi/joiste" -> `FISA-scule-gauri-grinzi-joiste.html`
  - "Casa de sus — plan constructie" -> `CASA-plan-constructie.html`
- Adauga UN link de nav "Desene" -> `desene.html` in bara comuna (`tn-links`) pe TOATE paginile principale (index, timeline, ghid-montaj, materiale, imbinari, modele-3d, casuta-din-copac, fise + cele 4 pagini noi). Ordine nav: Stadiu, Ghid, Materiale, Imbinari, 3D, Desene, Dosar.
- Pune aceeasi bara de nav comuna pe cele 4 pagini noi, ca sa nu fie fundaturi.

### 3. Reconciliere documente (deja scrise pe Main — doar comite + aliniaza site-ul)
- `SOURCE-OF-TRUTH.md` (nou, in folder) — comite.
- `CASUTA-DIN-COPAC.md` (editat: perete 1800/1500, ref CASA) — comite.
- Aliniaza mentiunile de perete "1300" ramase pe site la "1800 spate / 1500 fata": `casuta-din-copac.html` (card stat ~162, eticheta svg ~274, pas ~449) si `audit.html` (~103). NU atinge fisierele de audit istorice (`AUDIT-2026-06-*`).

### 4. Arhivare / curatenie
- Muta in `_archive/`: `AUDIT-2026-06-13.html`, `PDF/Audit-complet-2026-06-13.pdf` (inlocuite de 06-18).
- Creeaza `_archive/briefs/` si muta acolo toate `DONE-BRIEF-*.md` si `FAILED-BRIEF-*.md`.
- Muta in `_archive/`: `PROMPT-chatgpt-*.md` (decizia surubelnitei rezolvata), `DE-LUAT-AZI-Hornbach.html`, `REZOLVARE-santier.html` (one-off-uri consumate, buget vechi 6600).
- Sterge cruft: `.~lock.Tracker_materiale_casuta.xlsx#`, `.DS_Store`. Daca `casuta-render.pdf` + `casuta-render.png` NU sunt referite de niciun html/md (verifica cu grep), muta-le in `_archive/`.
- `.gitignore`: adauga `bin/` (opreste un commit accidental de 14 MB micromamba).

### 5. Git — comite restanta curat (NU face push; Vlad face push)
- Confirma ca cele 3 stergeri trackuite (`FAILED-BRIEF-manual-drawings.md`, `NEEDS-INPUT-audit-fixes.md`, `RUNNING-BRIEF-manual-drawings-v2.md`) sunt intentionate (mutate/redenumite) si stage-uieste-le.
- Stage-uieste lucrul untracked legitim: `AUDIT-2026-06-18.html`, `AUDIT-2026-07-23.html`, NODURI, PODEA x2, CASA, FISA-scule, modificarile timeline, `SOURCE-OF-TRUTH.md`, `desene.html`, editarile dosar, `STATUS.md`.
- Secventa de commit-uri cu sens (NU un singur bloc `git add -A`): (a) "reconcile: SoT + dosar cote 1800/1500 + leaga desene"; (b) "timeline p2 onest (fara confirmat foto)"; (c) "arhiva audituri/briefuri vechi + cruft + gitignore bin".
- Regenereaza orice PDF a carui sursa s-a schimbat (`build_pdfs.py` pt 04/05/06 daca audit.html/dosar/materiale s-au schimbat).
- Raporteaza hash-urile si o linie "gata de push".

## CONSTRAINTS
- Tema luminoasa, romana fara diacritice, respecta `assets/site.css` + pattern-ul de nav (copiaza din `modele-3d.html`).
- NU face push. NU marca p2 complet. NU modifica fisierele de audit istorice sau reviewul structural.
- Adauga STATUS.md o linie cu ce s-a facut (data, ce s-a schimbat, ce urmeaza).

## DONE MEANS
- Subtitlul p2 din `timeline.html` NU mai contine "confirmat foto"; scrie taiere ~1900 + "+2200 inca de facut"; item-ul ramane deschis.
- Fiecare din cele 4+1 pagini de desene e reachable din index prin nav "Desene"; `desene.html` se randeaza in stilul site-ului.
- Nicio mentiune de perete "1300" nu mai ramane pe site-ul live (`casuta-din-copac.html`, `audit.html`); `SOURCE-OF-TRUTH.md` + dosarul actualizat sunt comise.
- `_archive` contine auditurile inlocuite, briefurile, prompturile si one-off-urile consumate; radacina nu mai are `DONE-/FAILED-BRIEF-*` sau lock/DS_Store; `.gitignore` are `bin/`.
- Secventa de commit-uri curata pe `main`, hash-uri raportate, nimic pushuit.

## IF STUCK
- Daca nu esti sigur ca un fisier e referit, fa grep prin `*.html *.md` inainte sa il muti; daca e referit, lasa-l si noteaza.
- Daca o stergere-fantoma pare neintentionata, pastreaza fisierul si marcheaza NEEDS-INPUT doar pentru acel item.
- Daca `build_pdfs.py` da eroare pe o pagina fara legatura, regenereaza doar sectiunile schimbate si noteaza restul.
