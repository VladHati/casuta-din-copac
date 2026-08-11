# BRIEF — commit fisa contravantuiri (2026-08-07)

## Context

Livrat din Main/Cowork: `FISA-MONTAJ-contravantuiri.html` + `.pdf` (10 pagini, 6 planse SVG generate din mm reali),
plus generatorul in `tools-fise/gen_cf.py` si `tools-fise/build_fisa.py`.

Fisa inlocuieste Fisa 9/11 pentru contravantuiri. Nu atinge nimic altceva.

## Ce faci

1. `git add` exact aceste fisiere:
   - `FISA-MONTAJ-contravantuiri.html`
   - `FISA-MONTAJ-contravantuiri.pdf`
   - `tools-fise/gen_cf.py`
   - `tools-fise/build_fisa.py`
   - `STATUS.md` (dupa pasul 3)
   - `SOURCE-OF-TRUTH.md` (dupa pasul 2)

2. In `SOURCE-OF-TRUTH.md`, in tabelul "Cine guverneaza ce", adauga un rand DUPA randul
   "Faza 2 (instructiuni de santier...)":

   | Contravantuiri (7 piese, as-built) | `FISA-MONTAJ-contravantuiri.html` / `.pdf` | actual (07.08) — inlocuieste Fisa 9/11 |

   Nu modifica nimic altceva in fisier.

3. In `STATUS.md`, adauga ca PRIMA linie sub titlu si sub linia de descriere:

   - 2026-08-07 (Main, Cowork) | Livrat `FISA-MONTAJ-contravantuiri.html/.pdf` (10 pag, 6 planse la scara: elevatie fata, elevatie spate, sectiune laterala cu consola, plan de sus, detaliu prindere, ordinea de montaj). Schema: **7 contrafise**, nu 6 ca in Fisa 9. **4 corectii iesite din desenarea la scara:** (1) pe as-built nu exista colt stalp-grinda la stalpii fata (stalpul se termina la 1900 unde incepe glulamul) → contrafisele nu pot fi pene taiate in colt, se prind **plat pe fetele laterale**; (2) Heco 8×200 prin contrafisa de 100 iese 10 mm prin glulam (90) → **8×160**, de cumparat; (3) planul **spate** lipsea din Fisa 9 — acolo glulamul sta IN FATA stalpilor, deci nu exista colt: solutie = diagonala lunga CF7 (rigla 45×145) sub cota 1900, cu unghi ~18°, marcata explicit ca cea mai slaba dintre cele 7 (proptelele de la varful stalpilor spate raman pana la peretii F4); (4) **CF1 s-ar fi batut cu trunchiul corcodusului** daca statea pe fata dinspre curte a glulamului → mutata pe fata interioara. Adaugat detaliu nou: **blocaj de reazem sub CF3/CF4** (aceeasi logica ca talpicul de la polita — sarcina consolei in compresiune, nu in forfecare pe suruburi). De cumparat: 1 rigla 45×145×2500 + 1 cutie Heco 8×160 + 6 buc 8×120. Restul din offcut. Generator in `tools-fise/gen_cf.py` + `build_fisa.py`. | URMEAZA: Vlad verifica pe teren cele 4 puncte din ultima sectiune a fisei (decalaj stalp-glulam, unde se termina contrafisele 45° existente, cat offcut 100×100 a ramas, confirmarea ca glulamul spate sta in fata stalpilor), apoi executa. **Vlad: `git push origin main`.**

4. Un singur commit, mesaj:
   `fisa montaj contravantuiri: 7 piese pe as-built, inlocuieste Fisa 9/11`

5. Raporteaza hash-ul commit-ului in STATUS ca linie de Builder.

## Ce NU faci

- Nu regenera PDF-ul. E deja randat si verificat vizual pagina cu pagina din Main.
- Nu atinge `tools-fise/fb.py`, fisa-09.html sau manualul. Fisa 9 ramane in istoric; precedenta e scrisa in SoT si in fisa noua.
- Nu face push (403 cunoscut). Pushul ramane la Vlad.

## Daca ceva nu se potriveste

Daca `SOURCE-OF-TRUTH.md` sau `STATUS.md` nu arata cum e descris mai sus, NU ghici:
scrie `NEEDS-INPUT-contravantuiri-2026-08-07.md` cu ce ai gasit si opreste-te.
