# BRIEF: audit-fixes-2026-06-18

## GOAL
Aplica fixurile de FISIERE din `AUDIT-2026-06-18.html` (categoriile DOC, TECH si tracker), regenereaza output-urile afectate, comite pe `main`. Rezultat: paginile site si `Tracker_materiale_casuta.xlsx` devin consecvente intern si oneste pe buget. NU schimba geometria, cotele sau deciziile structurale in afara celor 14 puncte de mai jos. Fixurile FIZICE/de santier (papuc polita, poarta, sol moale) NU fac parte din acest brief.

## CONTENT — schimbarile exacte

### Pagini site
1. **DOC-01** — `materiale.html`: stalpisori balustrada `×6` → `×7` (sectiunea "Ce mai trebuie luat", ~L393). Daca valoarea vine dintr-un script sursa, corecteaza acolo.
2. **DOC-02** — `ghid-montaj.html`: in inventarul cumulativ (~L123) `C1×4 + C2×12` → `C1×4 + C2×14`, iar qty `16` → `18`. (Textul pasului grinda spate e deja corect; doar inventarul ramane in urma.)

### Tracker `Tracker_materiale_casuta.xlsx`
3. **DOC-02** — foaia `Debitare`, P22: `C2 90x90x65 (12)` → `C2 90x90x65 (14)`.
4. **DOC-05** — foaia `Materiale`, randul de nota din capul foii: scoate cuvantul `balustrada` din enumerarea "Faza 2 pereti/acoperis/balustrada/scara" (balustrada e Faza 1).
5. **BUD-01** — foaia `Materiale`, celula bugetului (`6600`) → `8500`.
6. **DOC-04 / BUD-02** — foaia `Materiale`, adauga un rand: Categorie `Balustrada` · Produs `Mana curenta + rigla jos` · Specificatie `45x70, ~9 m total` · Magazin `Hornbach` · Cant `2` · UM `buc` · Status `De cumparat` · Nota `Sus+jos pe 3 laturi; lipsea din tracker`.
7. **BUD-02 / SIG-03** — foaia `Materiale`, adauga un rand: Categorie `Balustrada` · Produs `Feronerie poarta` · Specificatie `2x balama cu arc (self-close) + zavor copil sus` · Cant `1` · UM `set` · Status `De cumparat` · Nota `Poarta auto-inchidere la capul scarii (SIG-03)`.
8. **DOC-06** — foaia `Platforma premium`, adauga o sectiune `BALUSTRADA` cu randurile: stalpisori 58x58 ×7; sipci 18x18 ~24; mana curenta 45x70 ~9 m; buloane M10 ×~14; feronerie poarta ×1 set. Preturi `est.` unde nu-s cunoscute.
9. **DOC-03** — foaia `Comanda Hornbach`, nota de subtotal: NU schimba subtotalul (3.886,24). Adauga la finalul notei: ` · DE VERIFICAT LA RECEPTIE: C2 14 vs 12 platit, inox 3 vs 2 platit`.

### Pipeline + repo
10. **PIPE-03** — creeaza `requirements.txt` in root cu: `weasyprint`, `markdown`, `pypdf`, `numpy`, `Pillow`.
11. **PIPE-02** — in `README.md`, documenteaza ordinea de rulare a pipeline-ului: `cd tools-fise && python3 det.py && python3 fb.py && python3 emit2.py && python3 idx2.py && python3 book.py` (se ruleaza din `tools-fise/`, caile `.pkl` sunt relative la CWD). Noteaza ca `*.pkl` se genereaza, nu-s in repo.
12. **GIT-03** — in `.gitignore`, adauga linia `~$*.xlsx` (lock-ul Excel pe Windows).
13. **DOC-07** — sterge `tools-fise/book.html` (restura de build, gitignorata).

### Regenerare
14. Dupa editari, regenereaza output-urile afectate: `PDF/06-Materiale.pdf` din `materiale.html` (prin `build_pdfs.py`). Daca `ghid-montaj.html` sau fisele se genereaza din `tools-fise/`, ruleaza pipeline-ul complet (ordinea de la pct. 11) apoi `build_pdfs.py`.

## CONSTRAINTS
- Romana fara diacritice.
- Pastreaza estetica EXISTENTA a paginilor (light, curata — NU dark, NU restiliza). Schimba doar valorile/textele listate.
- Fix la SURSA daca o pagina e generata dintr-un script; nu hand-edita output-ul generat.
- Nu atinge geometria, cotele sau alte cantitati in afara celor 14 puncte.
- Builder comite local pe `main`; `git push` il face Vlad (contul Builder nu poate push). Daca ai Netlify CLI configurat pentru acest site, poti face deploy; altfel lasa push-ul pe seama lui Vlad.

## DONE MEANS
- `materiale.html` arata stalpisori ×7; `PDF/06-Materiale.pdf` regenerat (contine ×7).
- `ghid-montaj.html` inventar: C2×14, qty 18; `Debitare` P22 = 14.
- Tracker: buget = 8500; exista randurile "mana curenta" + "feronerie poarta"; "balustrada" scos din nota Faza 2; `Platforma premium` are sectiunea balustrada; nota din `Comanda Hornbach` contine avertismentul de receptie.
- `requirements.txt` exista cu cele 5 pachete; `README.md` are ordinea pipeline; `.gitignore` contine `~$*.xlsx`; `tools-fise/book.html` nu mai exista.
- `build_pdfs.py` (si pipeline-ul, daca rulat) ies cu 0 erori.
- Tot comis pe `main`; `STATUS.md` are o linie noua: data, ce s-a schimbat, "URMEAZA: Vlad push".

## IF STUCK
- Numarul fizic al livrarii (C2 14 vs 12, inox 3 vs 2) NU e confirmat de Vlad. NU schimba cantitatile comandate sau subtotalul — doar adauga avertismentul de la pct. 9.
- Daca `materiale.html` / `ghid-montaj.html` sunt generate dintr-un script: corecteaza sursa (cauta in `tools-fise/` si `build_pdfs.py`) si regenereaza; nu hand-edita output-ul.
- Pret feronerie poarta necunoscut → est. (balama cu arc ~60-120 lei/buc, zavor ~30-60), marcat "de confirmat".
- Daca xlsx are lock (`.~lock...#` prezent): e vechi/stale, poti scrie; noteaza in STATUS.
- Daca regenerarea cere env lipsa (weasyprint/pango): foloseste `requirements.txt` nou + nota brew din README. Daca tot esueaza, lasa HTML-urile corectate si raporteaza in STATUS ce PDF n-ai putut regenera — nu bloca tot brief-ul pentru un PDF.
