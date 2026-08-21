MODEL: opus
EFFORT: xhigh

# BRIEF — corectia golului de geam, apoi desenele peretelui din fata

Doua treburi, in ordine. **Prima se comite singura, inainte sa incepi a doua.** Daca a doua nu iese, prima trebuie sa fie deja in git.

---

# COMMIT 1 — corectia campurilor de la golul de geam lateral

## Ce e gresit

Figurile `lat_stanga` si `lat_dreapta` din `gen_ghid.py` scriu amandoua campurile golului de geam ca **543 / 490 / 542**. Suma da **1575**, care e adancimea *medie* a casei — cifra din care s-a calculat panta acoperisului. N-are ce cauta intr-un layout de talpa.

Talpile reale sunt **1580** (stanga) si **1570** (dreapta). Pe peretele din dreapta desenul cere 1575 de material pe o talpa de 1570 — nu incape.

## Ce pui

Golul de **490** e centrat pe talpa. Campul = `(talpa − 490) / 2`.

| figura | talpa | campuri corecte |
|---|---|---|
| `lat_stanga` | 1580 | **545 / 490 / 545** |
| `lat_dreapta` | 1570 | **540 / 490 / 540** |

**Nu scrie cifrele ca siruri.** Calculeaza-le in cod din constanta talpii, ca sa nu mai poata divergе: campul se deduce, nu se tasteaza. Daca `DEP_L` / `DEP_R` exista deja, foloseste-le; daca nu, adauga `GEAM = 490` si calculeaza campul din ea.

Verifica si figura generala `e4_perete` (prima din capitol): acolo scrie 545 / 490 / 545 pe o talpa de 1580 — **corect**, se lasa. Dar subtitlul ei zice „cealalta laterala e 1570" fara sa dea campurile ei; adauga in acelasi rand si **540 / 490 / 540 pe dreapta**, ca sa nu ramana o singura cifra pe ecran cand omul lucreaza peretele celalalt.

## DONE MEANS — commit 1

- `grep -c "543\|542" gen_ghid.py` → **0**
- In HTML-ul construit, capitolul `e4` contine `545` si `540` ca valori de camp; `543` si `542` nu mai apar nicaieri.
- 545 + 490 + 545 = 1580 si 540 + 490 + 540 = 1570 — verifica aritmetic in cod, nu din ochi.
- `python3 gen_ghid.py && python3 build_ghid.py` ies 0.

**Comite aici, cu mesaj propriu, inainte sa treci mai departe.**

---

# COMMIT 2 — 4 desene pentru E5, peretele din fata

Peretele cel mai complicat din casa: usa, fereastra, patru jambe, bara de sus care calca pe doi stalpi. Are un singur desen general. Primeste patru detalii.

Toate in `gen_ghid.py`, cu clasa `Fig` existenta, montate in `build_ghid.py`, cu paleta si grosimile de linie ale figurilor existente. **Fara culori noi.**

**Regula:** fiecare cota desenata vine dintr-o constanta din capul lui `gen_ghid.py`, nu dintr-un sir. Daca o cota n-are constanta, o adaugi. Geometria s-a mutat de trei ori si desenele au ramas in urma de fiecare data.

### D1 — `fata_elev`: elevatie perete fata, la scara

Rama **1970**, verticale **1552**. Layout cotat cap la cap, masurat de la fata interioara a stalpului stang:

```
115 camp | jamba | fereastra 161 → 731 | jamba | usa 938 → 1488 | jamba | montant de camp 1650 → 1696 | colt 274
```

Coltul de **274** e locul propteaței de **250**. Prag + buiandrug fereastra: **570, intre jambe** — nu peste ele.
Caption: `Peretele din fata — rama 1970, verticale 1552. Cotele merg de la fata interioara a stalpului stang.`

### D2 — `fata_bara`: bara de sus, 100×60 taiata la 2155

Sectiune care arata **de ce 2155 si nu 1970**: bara trebuie sa calce pe rama SI pe amandoi stalpii de 90×90. Coteaza cat iese peste fiecare stalp. Latura de **60 in sus**, 100 pe orizontala.
Caption: `Bara de sus, 100×60 taiata la 2155 — calca pe rama si pe amandoi stalpii.`

### D3 — `fata_stalp`: prinderea finala a stalpului din fata

**4 × surub dulgherie 8×140** oblic la **15–20°** in grinda de dedesubt — doua de-o parte, doua de cealalta — plus **coltar 90×65 pe fiecare fata a stalpului**. Doua vederi alaturate: din fata si in sectiune, cu unghiul cotat.
Scrie pe desen: **tot de sus, fara piulite, fara tije prin podea.**
Caption: `Prinderea finala a stalpului din fata — 4 suruburi 8×140 oblice plus coltare. Nu exista tije M12 in podea.`

### D4 — `fata_usa`: golul de usa, ordinea de taiere

Doua stari alaturate:
- **inainte** — talpa intreaga, peretele rigid, gata de ridicat
- **dupa** — talpa taiata, gol **550** latime, **1600** liber pe verticala

Intre ele, eticheta: **taierea se face ultima, cu peretele deja ridicat, legat si verificat la echer.**
Caption: `Golul de usa — talpa se taie ultima, dupa ce peretele e ridicat si verificat la echer.`

## CONSTRAINTS

- Romana, fara diacritice.
- **Nu inventa cote.** Fiecare numar e in brief-ul asta sau in constantele existente. Daca un desen cere o cota care nu exista — un unghi de teșire, o distanta intre suruburi — deseneaza-l fara ea si pune un bloc `stop` in capitol care spune ce lipseste. Precedentul e in `e0`. **Nu estima.**
- Desenele trebuie citibile la **390 px**. Daca unul nu incape, sparge-l in doua figuri cu captions separate — mai bine doua clare decat unul ilizibil.
- Nu atinge `e0`, `e1`, `e2`, `e3`, `e6`, `e7`, si nici figurile din `e4` in afara corectiei de la COMMIT 1.
- Fisier autonom, fara CDN. Fara deploy.

## DONE MEANS — commit 2

- `<svg>` pe sectiune: **e3=4 · e4=6 · e5=5 · e6=2 · e7=0**
- Cele 4 chei `fata_*` sunt folosite in `build_ghid.py`, fiecare cu `figcaption`-ul de mai sus.
- `grep` pe HTML gaseste in `e5`: `1970` `1552` `115` `161` `731` `938` `1488` `1650` `1696` `274` `570` `2155` `8×140` `90×65` `550` `1600`.
- `python3 gen_ghid.py && python3 build_ghid.py` ies 0. Consola paginii curata.

## VERIFY

Deschide rezultatul la desktop **si la 390 px**, consola curata, apoi confirma fiecare punct din DONE MEANS individual.

In plus, obligatoriu:
- **Randeaza fiecare desen nou si uita-te la el.** SVG valid nu inseamna desen corect. Cauta: text iesit din cadru, cote suprapuse, linii de cota care arata spre nimic.
- **Testul de suma pe D1:** 115 + jamba + (731−161) + jamba + (1488−938) + jamba + (1696−1650) + 274 trebuie sa dea 1970 cu jambele reale. Daca nu da, o cota e gresita — **opreste-te si scrie in STATUS.md**, nu ajusta pe ghicite.
- **Scrie linia in STATUS.md, apoi comite.** Raportarea e parte din treaba.

## IF STUCK

- **Latimea jambei nu e nicaieri** → e distanta dintre cotele date (de exemplu 161 − 115). Daca nu se inchide aritmetic, `stop` si STATUS.md.
- **Nu poti desena D3 fara grosimea grinzii de dedesubt** → ia-o din `SCHEME-2D-casa.html`, care are sectiuni prin podea. Daca nici acolo nu e, `stop`.
- **Ramai fara aer inainte de a patra figura** → comite cate ai facut, cu figurile montate, si scrie in STATUS.md exact care lipseste. Trei desene montate si raportate bat patru desene pierdute.
