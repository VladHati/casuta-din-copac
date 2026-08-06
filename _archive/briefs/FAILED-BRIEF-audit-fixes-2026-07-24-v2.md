MODEL: opus

# BRIEF — audit fixes v2 (finalizare dupa FAILED fals-negativ)

## GOAL

Termina ce a ramas din `FAILED-BRIEF-audit-fixes-2026-07-24.md`. Rularea v1 a facut corect ~70% din editari (toate sursele text), dar a murit la commit pe un `.git/index.lock` vechi si a fost marcata FAILED. **Editarile din working tree sunt CORECTE si verificate — NU le reface, NU le reverta.** Faci doar ce lipseste, apoi commit.

## PASUL 0 — deblocheaza git (fara asta totul pica iar)

`rm -f .git/index.lock` (e din 24.07 16:48, niciun proces git activ). Verifica `git status` functioneaza. Daca lock-ul reapare in timpul rularii: un singur proces git o data, fara operatii paralele.

## CE LIPSESTE (verificat 24.07, dupa rularea v1)

1. `materiale.html`: adauga efectiv randul talpic (2× bloc 100×100 ~180, offcut, 0 lei) — v1 a facut doar swapul 1872→1900, grep "talpic" = zero.
2. Tracker `Tracker_materiale_casuta.xlsx` (openpyxl, NU atinge cantitatile C2/inox):
   - Debitare P4: "~2550" → "taie dupa masuratoare as-built (~2430-2450)"; pozitii → `0/280/720/1120/1550/2100 (capete dublate)`; adauga rand "2× joista-sora KVH 100×100×4000 — DE CUMPARAT (Hornbach 7337253), lungime dupa masuratoare".
   - Debitare P2: "+1872" → "~1900 as-built".
   - Foaia "Platforma premium": statusuri "De cumparat" → "SOSIT 18.06" DOAR pt piesele pe care foaia Comanda le are SOSIT.
   - Materiale: coltar C2 nota: necesarul a crescut la 18 (16 reazeme joiste+surori + 2 grinda spate) — "de cumparat 4 (sau 6 daca la numaratoare ies 12)".
3. `AUDIT-2026-07-23.html`: banner sus: "Actualizat 24.07 — cauza celor 3 briefuri esuate: OAuth Builder expirat (v. brief v4). Starea constatarilor si auditul curent: AUDIT-2026-07-24.md. Cotele din pagina = istorice (lant as-built: 1900/2100/2200/2228)."
4. `AUDIT-2026-06-18.html`: banner: "STR-01 INCHIS 24.07 (talpic as-built: 3× Heco 8×200 + 2 M12 + contrafisa 45°). STR-02 (M12×140): regula acceptata — OK daca piulita prinde filet complet; verificare santier DESCHISA. STR-03/STR-04: partial — contrafisa nod spate montata 24.07, restul DESCHIS."
5. `desene.html`: (a) sectiune noua "Audituri" cu linkuri la AUDIT-2026-06-18.html si AUDIT-2026-07-23.html + nota ca auditul curent e AUDIT-2026-07-24.md; (b) in cardul Podea, descrierea "6 joiste la 100/.../1980" → "6+2 joiste, capete dublate pe axa stalpilor (0/2100)"; (c) adauga link la `FISA-CONTINUARE-podea.html` (fisa de santier pt faza podelei, 24.07).
6. `ghid-montaj.html` (~linia 311): SVG-ul planului de joiste are inca axele 100/.../1980 langa textul nou 0/.../2100 — ori redeseneaza pozitiile in SVG, ori pune pe SVG eticheta vizibila "desen vechi (plan initial) — pozitiile corecte: 0/280/720/1120/1550/2100, capete dublate".
7. `PODEA-plan-sectiune.html` + `PODEA-impactum.html`: nota veche "dusumeaua iese ~50-70 mm peste joistele de capat" e din layoutul vechi — cu capetele pe 0/2100 scandurile de 2100 se termina pe axele joistelor; corecteaza sau marcheaza.
8. `CASA-plan-constructie.html` pasul "pune o joista sub linia stalpilor fata (la 1100)": marcheaza DEPASIT (layoutul 24.07 pune stalpii casei pe joistele-pereche de capat, axa 0/2100); regula "M12 inainte de dusumea" ramane.
9. `SOURCE-OF-TRUTH.md`: randul "Audit tehnic" → curent = `AUDIT-2026-07-24.md`; adauga rand "Faza podea (instructiuni de santier)" → `FISA-CONTINUARE-podea.html/.pdf`.
10. REGENEREAZA TOT: fisele prin generator (`tools-fise/` — fb.py are deja toate fixurile; asta repara singur fisa-02..06 + cardurile din fise.html), manualul + Fise-montaj prin `tools-fise/book.py`, PDF-urile de sectiune prin `build_pdfs.py`. Verifica: niciun PDF mai vechi decat sursa lui; grep "2072|1980" in fisa-*.html regenerate = zero (in afara de mentiuni marcate "plan initial").
11. Igiena: muta `DONE-BRIEF-talpic-propagation.md` + `DONE-BRIEF-reconcile-publish-cleanup.md` in `_archive/briefs/`; `git add` POZE/IMG_2270-2288, `AUDIT-2026-07-24.md`, `FISA-CONTINUARE-podea.html`, `FISA-CONTINUARE-podea.pdf`.
12. STATUS.md: intrare Builder cu ce ai facut + hash-uri. 3 commit-uri logice (cote+continut v1 / completari v2+regen / igiena+poze). **NU face push.**

## CONSTRAINTS

- NU atinge: balustrada (1000/1100), M10, cantitatile C2/inox din tracker (doar nota de necesar la C2).
- Fisele NUMAI prin generator.
- Working tree-ul existent e bun: v2 = completare, nu re-rulare.

## DONE MEANS

- `git status` curat; 3 commit-uri noi peste 26c5242; zero index.lock.
- `grep -i talpic materiale.html` ≥ 1; `PDF/06-Materiale.pdf` mai nou decat sursa.
- Tracker: Debitare P4 contine "2430" si "0/280/720/1120/1550/2100"; Platforma premium fara "De cumparat" la piese SOSIT.
- `desene.html` contine "Audituri" + link FISA-CONTINUARE; fisa-06.html regenerata contine "2100" ca pozitie de capat si niciun "1980" nemarcat.
- Diff-ul v2 nu contine modificari la balustrada/M10.

## IF STUCK

- index.lock nu se poate sterge → STOP, marcheaza NEEDS-INPUT cu mesajul exact (nu lucra pe langa git).
- Orice conflict de cifre: castiga lantul 1900/2100/2200/2228 + layoutul 0/280/720/1120/1550/2100 cu capete dublate + lungime "dupa masuratoare (~2430-2450)".
- Generatorul nu acopera un text → NEEDS-INPUT, nu edita fisa-*.html direct.
