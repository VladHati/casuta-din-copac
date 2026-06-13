# Manual Faza 1 — audit complet (3 agenti) · 13.06.2026

Sinteza a trei audituri paralele: geometrie/tehnic, design IKEA, coerenta/continut.
Sursa generatoare a manualului: `tools-fise/` — `iso.py` (randare izometrica), `fb.py` (date per fisa + coordonate), `det.py` (panouri zoom), `book.py` (asambleaza `PDF/Manual-Faza-1-complet.pdf`).

Verdict: continutul si geometria (coordonatele) sunt corecte. Ce e rupt e RANDAREA desenelor + scara/legibilitatea + cateva cantitati de BOM. iso.py e salvabil — proiectia si coordonatele raman, se repara sortarea pe adancime, cuplajul explode/cota, camera si modelul.

## 1. Geometrie / desene (cauza imaginilor gresite)

Coordonatele sunt corecte (grinzi pe latime x=2100; joiste pe adancime z=1780; joiste asezate la +2072 = top grinda; consola 700 pe fata; copac intre joistele 280-720 la S4). Bugurile de randare:

- **A. Sortare pe adancime gresita (BUG PRINCIPAL).** `iso.py` `_depth` (≈L14-16) + sort (≈L88) ordoneaza fiecare cutie dupa UN punct-centru. Doua piese lungi care se incruciseaza (grinda pe x vs joista pe z) nu pot fi ordonate dupa un singur centru → grinda din fata se deseneaza in MIJLOCUL sirului de joiste (peste unele, sub altele). Asta e „grinda tese printre joiste / orientarea pare ca se inverseaza" la pag. 23-24.
- **B. Prima joista pluteste (pag. 23 pasul 2).** `fb.py` (≈L152): joista plasata primeste `ex=(0,560,0)` → desenata 560 mm in sus, detasata; iar cota „700 consola" e ancorata la inaltimea FINALA → leaderul arata in gol. In plus, celelalte 5 joiste sunt trecute ca `built=True` → pare ca adaugi o joista pe un planseu deja gata.
- **C. Fara model unic care creste.** Fiecare pas reconstruieste cutiile de la zero (`base=...` in fiecare `stageN`). Stalpii isi schimba reprezentarea (`posts_full` → `posts_stub`, ≈L18-26). `W` per-apel + auto-incadrare (`iso.py` ≈L62-65) → camera si scara sar de la pas la pas.
- **D. Fete blocate pe un octant** (`box_faces` emite mereu top/front/right) — fragilitate latenta, nu defectul vizibil acum.
- **E. CORECT (a nu se „repara"):** orientarea grinda/joista, asezarea (top grinda 2072 = jos joista), axa/capatul consolei, lantul de cote 2200→1872→2072, pozitia copacului.

Recomandare: model parametric unic care creste (stalpi→polite→grinzi→joiste→dusumea→balustrada); fiecare pas randeaza `MODEL[:k]` (construit, palid) + piesa noua (highlight); sortare „behind-test" corecta (SAT pe extentele proiectate x,z,y) SAU spargere a pieselor lungi in sub-cutii per travee; o singura camera/scara comuna calculata din ansamblul final; stalp parametric mereu la inaltime reala (cut +1872 / +4000).

## 2. Design IKEA (oasele sunt bune; executia la scara de santier e problema)

Are deja: coperta, cuprins, „ce construim", inventar materiale pe sursa, pagina scule, pagina siguranta, BOM per pas cu coduri, izometrice cu sageti + ghost, panouri „ZOOM · cum se prinde", marcaje CRITIC, perechi do/don't, „gata cand", timp/dificultate/2-persoane.

Lipsuri (prioritizate):
1. **Desene prea mici → call-out-uri ilizibile.** `book.py` `.drawbox svg{max-height:72mm}` (≈L104) + fonturi in SVG hardcodate la 11-12.5 (`iso.py` ≈L130,141,158) → etichetele ajung ~6-7px pe pagina (vezi pozitiile joistelor 100/280/720… care se aglomereaza, pag. 23). **Cel mai mare castig.** Ridica plafonul la ~100mm, scoate indentul de 13mm (`.step .drawbox{margin-left:13mm}`), mareste fonturile SVG la 15-17 + `pad`.
2. **~5 pasi fara desen** (gauri polita p14; taiat blocaje p29; regula 5mm p35; uns p36; **POARTA p40** — cel mai relevant pt siguranta). Adauga desen mic la fiecare, mai ales poarta (unde pe S3, cum difera de o travee fixa).
3. **CRITIC generic** — acelasi string „opreste-te si verifica" de ~15 ori (`book.py` ≈L145). Fa-l specific per pas (ce anume verifici).
4. **Lungimea surubului la locul folosirii** — cardurile BOM arata doar cod+cantitate; lungimea e doar pe pag. 4. Adauga dimensiunea in nota cardului (datele exista in `PARTS`).
5. **Ghost doar fata-top + piese „built" spalacite.** Ghost wireframe complet (3 fete punctate); contrast mai bun la piesele deja montate; fiecare pas de „plasare" sa aiba `ex=` (sageata de directie) — pag. 24 (cele 6 joiste) nu are, pare stare finala.
6. **Legenda repetata 11×** dar nu reflecta toate piesele. Legenda completa o data (pe „Ce construim"), iar pe fisa doar culorile folosite acolo.
7. **Sculele = doar text.** Adauga pictograme monoline (bormasina, cheie, nivela, fierastrau, ruleta).

Plus: muta 2-3 reguli dure de siguranta ca banner pe pag. 2 (nu doar la final); checkbox-uri pe inventarul de materiale (bifezi inainte de start); cantitati structurale EXACTE (nu „~12 C2"); fixeaza rupturile de pagina (un pas+desen+zoom sa stea impreuna).

Nota: panourile ZOOM din `det.py` sunt deja de calitate IKEA — desenele principale trebuie aduse la aceeasi generozitate.

## 3. Coerenta / continut (PDF si fise sunt consecvente; cateva fixuri reale)

1. **C2 lipsa 2 buc.** Nevoie 14 (12 joiste + 2 grinda spate); trackerul comanda 12. Manualul deja noteaza „+2 grinda spate = de luat" dar comanda n-a fost actualizata. → comanda 14. [prioritate — lipsa structurala]
2. **Dusumea desenata cu 15 scanduri, nevoie 17.** `fb.py` `deck_g(15)` → planseul desenat se opreste ~230mm inainte de grinda spate (pag. 36,37,39, coperta). Numerele zic 17. → `deck_g(17)`.
3. **BM „bulon M10" vs poza = M12x120.** Textul/scula zic M10; `PARTS['BM']` refoloseste poza M12 (B2). Decizie: ramane M10 (potrivit pt stalpisor 58x58, textul+scula deja zic M10) → inlocuieste poza placeholder, adauga linie in tracker pt bulon M10 (Faza 1).
4. **H4: 204 nevoie vs 200 comandat** (17×6×2). Minor — comanda un al 3-lea pachet sau noteaza explicit.
5. (Web, in afara manualului dar aceeasi eroare de date) `ghid-montaj.html` pasul 4 omite coltarul C2 anti-smulgere si eticheteaza gresit „B1×4" (ar trebui H1 + C2). De aliniat la Fisa 4/PDF.

Restul (tabel specificatii pag.2, lant cote, pozitii joiste, coduri conectori, secventa buildabila, numerotare/cuprins, fara confuzie de faza) — verificat CORECT.
