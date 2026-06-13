MODEL: opus

# BRIEF — audit-fixes v2 (deciziile F1 + F3)

## GOAL
Aplica cele doua reparatii ramase din audit, acum ca Vlad a decis. Regenereaza fisele + PDF-urile afectate, commit local pe `main`. (Push-ul il face Vlad — contul Builder nu are credentiale.)

## DECIZII LUATE
- **F1: balustrada + masa = FAZA 1.** Faza 2 ramane DOAR pereti, acoperis, scara.
- **F3: coltarul C1 foloseste Heco 6×100** (ca si C2). Nodul D (contrafise) ramane 8×200 — NU il atinge.

## REPARATII

### F1 — muta balustrada + masa in Faza 1
- `ghid-montaj.html` L440 footer: schimba
  `Faza 1 — stalpi + podea. Urmeaza Faza 2: pereti, acoperis, balustrada, scara si masa-copac.`
  in
  `Faza 1 — stalpi, podea, balustrada, masa. Urmeaza Faza 2: pereti, acoperis, scara.`
- `tools-fise/book.py` L30: scoate grupul „Faza 2 / de ales" pentru piesele de balustrada — muta SB/SP/MC/BM intr-un grup de Faza 1 (sau in grupul principal de piese). F3 (topcoat) poate ramane „de ales". Scoate „balustrada (Faza 2)" / „(Faza 2)" de pe etichetele acestor piese.
- `tools-fise/fb.py`: cauta orice „(Faza 2)" pe piese de balustrada (ex. chip-uri SB/SP/MC/BM) si scoate-l. Verifica si textul „Cheie M10 ... balustrada (Faza 2)" din lista de scule (L155) → „balustrada".
- Verifica restul fisierelor pentru „balustrada" trecuta gresit la Faza 2 dupa schimbare: `grep -rn "balustrada" *.html tools-fise/*.py | grep -i "faza 2"` → trebuie 0.

### F3 — surub C1 = Heco 6×100
- `tools-fise/fb.py` fisa-05 (~L210): chip `('H1','~12','in coltare')` → `('H2','~12','in coltare')` (H2 = Heco 6×100).
- `imbinari.html` nodul A: „Heco 8×200" → „Heco 6×100" in text SI in chip-ul „Heco 8×200 ×4" → „Heco 6×100 ×4". Coltar 100×100 ramane.
- NU atinge nodul D (contrafise, 8×200 corect) si nici contul de suruburi de la celelalte noduri.

## DUPA EDITARI
- Regenereaza: `tools-fise/book.py` (fise HTML + Fisa-*.pdf + Manual + Fise-montaj), apoi `python3 build_pdfs.py` (sectiuni — imbinari.html s-a schimbat).
- Commit local pe `main` cu mesaj clar. NU face push.
- Scrie in STATUS.md o linie: data, F1+F3 aplicate, „URMEAZA: Vlad face git push".

## DONE MEANS
- `grep -rn "Faza 2" *.html tools-fise/*.py | grep -i balustrada` → 0 rezultate.
- `ghid-montaj.html` footer listeaza balustrada+masa in Faza 1; Faza 2 = pereti, acoperis, scara.
- `grep -rn "8×200\|8x200" imbinari.html` → apare DOAR la nodul D (contrafise), nu la nodul A.
- fisa-05.html arata „Heco 6×100 in coltare" pentru C1.
- Fise + PDF-uri regenerate (mtime nou).
- Commit pe `main`; lucruri NEpushuite raportate in STATUS.md.

## IF STUCK
- Daca un „(Faza 2)" e generat dintr-o variabila comuna (nu string direct), schimba la sursa, nu peste tot manual.
- Nu inventa cote sau coduri. Orice neclaritate → opreste si scrie in STATUS.md.
