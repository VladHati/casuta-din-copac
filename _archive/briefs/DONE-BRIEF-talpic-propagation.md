MODEL: opus

# BRIEF — Propaga talpicul (bloc de compresiune sub polita spate)

## GOAL
Adauga talpicul lipsa (blocul de compresiune de sub polita din spate) in TOATE documentele de constructie, in generator, in paginile 3D si in tracker, ca oricine construieste din fise sa il monteze. Acum talpicul apare doar in `NODURI-grinda-stalp.html` si in reviewul structural `Fisa-santier-casuta.pdf`; fisele de montaj, ghidul, 3D-ul si lista de debitare il omit — exact golul P0 pe care il numeste reviewul ("polita atarnata in 2 buloane in forfecare = acolo cedeaza deck-ul").

## CONTENT — specul nodului (foloseste formularea din `NODURI-grinda-stalp.html`, deja corecta)
- **Nod SPATE (S1, S2):** stalpul e INTREG; grinda sta pe polita la +1872; **polita reazema pe un TALPIC** (bloc 100x100 dedesubt, prins pe fata stalpului) — greutatea trece prin **compresiune**, nu prin buloane. **2x M12 = doar pozitie + anti-smulgere.** 3x Heco 8x200 oblic grinda->stalp. C2 anti-smulgere in colt.
- **Nod FATA (S3, S4):** NESCHIMBAT — grinda pe varful stalpului taiat + C1 + Heco 6x100.
- **Piesa talpic:** 2 buc, offcut 100x100, ~180 mm lungime (confirma pe teren sub polita), unul pe fiecare stalp din spate.

## FILES — editeaza SURSA, nu doar output-ul generat
- `tools-fise/fb.py` — datele/textul fisei pentru nodul spate (fisa-03/fisa-04): cauta "polita" / "M12" / nodul "D". Adauga talpicul in descrierea nodului + BOM + orice linie de debitare emisa. **Aceasta e sursa** pentru `fisa-03.html`, `fisa-04.html` si PDF-urile lor — daca editezi doar HTML-ul generat, se suprascrie la regenerare.
- `ghid-montaj.html` — pasul cu polita/grinda spate (zona liniei ~189, "Fixeaz-o cu 2 buloane M12 ... Polita duce greutatea"): adauga talpicul; reformuleaza asa incat greutatea sa mearga prin talpic (compresiune), iar M12 = pozitie + anti-smulgere.
- `imbinari.html` (~135), `imbinare-3d.html` (~52), `montaj-3d-complet.html` (nod spate ~158-165), `platforma-3d.html` (~137), `FISA-scule-gauri-grinzi-joiste.html` (~226): adauga talpicul in descrierea/desenul nodului spate.
- `PODEA-plan-sectiune.html` (~108), `PODEA-impactum.html` (~129): arata talpicul sub polita in sectiune.
- `Tracker_materiale_casuta.xlsx`: foaia **Debitare** — adauga linia "2x talpic 100x100 ~180 mm (offcut)"; foaia **Platforma premium** — adauga talpicul la grupul politei; foaia **Materiale** — noteaza ca vine din offcut (fara cumparare in plus).

## CONSTRAINTS
- NU modifica nodul FATA (pe varf) — doar spatele (pe polita) primeste talpicul.
- Pastreaza formularea consecventa cu `NODURI-grinda-stalp.html`. Romana fara diacritice.
- Dupa ce editezi generatorul, ruleaza pipeline-ul in ordine (README): `cd tools-fise` -> `det.py` -> `fb.py` -> `emit2.py` -> `idx2.py` -> `book.py`; apoi din radacina `build_pdfs.py`. Regenereaza toate PDF-urile afectate.
- Commit local pe `main`. **NU face push** (Vlad face push). Raporteaza hash-ul de commit.

## DONE MEANS
- "talpic" (sau "bloc compresiune") apare in: `fisa-03.html`, `fisa-04.html` + PDF-urile lor, `ghid-montaj.html`, `imbinari.html`, `imbinare-3d.html`, `montaj-3d-complet.html`, `platforma-3d.html`, `FISA-scule-gauri-grinzi-joiste.html`, `PODEA-plan-sectiune.html`, `PODEA-impactum.html`.
- Tracker: foaia Debitare are linia de talpic; Platforma premium il listeaza.
- Textul nodului spate spune peste tot ca greutatea reazema pe talpic (compresiune) si M12 = doar pozitie + anti-smulgere. Nicio pagina nu mai zice "polita duce greutatea" doar din 2 M12.
- Pipeline rulat curat (fb.py / book.py / build_pdfs.py ies 0); PDF-uri regenerate.
- Hash de commit raportat.

## IF STUCK
- Daca textul nodului spate din `fb.py` nu e evident, cauta "polita" / "M12" / nodul "D" — acela e nodul spate. Adauga talpicul acolo ca sa curga in fisa + PDF.
- Daca lungimea talpicului e incerta, foloseste ~180 mm cu nota "confirma pe teren" — nu bloca.
- Daca o pagina are desenul nodului in SVG fara text-hook, adauga un dreptunghi etichetat TALPIC sub polita, copiind pattern-ul din `NODURI-grinda-stalp.html`. Daca un desen e prea complex de editat in siguranta, adauga o nota text clara langa el si marcheaza NEEDS-INPUT DOAR pentru fisierul acela, continuand restul.
