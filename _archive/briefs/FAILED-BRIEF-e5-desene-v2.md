MODEL: opus
EFFORT: high

# BRIEF — 4 desene pentru E5, peretele din fata

## REGULA CARE BATE TOT RESTUL

**Comiti dupa fiecare desen. Patru desene, patru commituri.**

Nu aduna munca si nu comite la final. Ultimele trei rulari mari au facut treaba corect si au murit inainte sa o salveze — de fiecare data munca a stat necomisa pe disc si a trebuit recuperata de mana.

Ciclul, pentru fiecare desen, in ordine:

1. scrii figura in `gen_ghid.py`
2. `python3 gen_ghid.py && python3 build_ghid.py`
3. te uiti la figura randata
4. o montezi in `build_ghid.py` cu captionul ei
5. rulezi din nou, verifici
6. **`git add` + `git commit`**, cu mesaj propriu
7. abia apoi treci la urmatoarea

Daca ramai fara aer dupa doua desene, **doua desene comise sunt un rezultat**. Patru desene pierdute nu sunt.

La final, un al cincilea commit doar cu linia din `STATUS.md`.

## CONTEXT

Peretele din fata e cel mai complicat din casa: usa, fereastra, patru jambe, si bara de sus care calca pe doi stalpi. Are un singur desen general (`e5`, 1 svg). Primeste patru detalii.

Toate in `gen_ghid.py`, cu clasa `Fig` existenta, montate in `build_ghid.py`. Paleta si grosimile de linie ale figurilor existente — `INK`, `ACC`, `ACC2`, `MUT`, `LN`, `W1`–`W4`, `METAL`, `GLASS`. **Fara culori noi.**

**Cotele vin din constante, nu din siruri.** Constantele exista deja in capul fisierului (`VF`, `BARA_F`, `FER_F`, `WF`, `FP`…), puse de rularea precedenta, cu asserturi. Foloseste-le. Daca o cota n-are constanta, adaugi constanta plus assert, dupa tiparul lui `CAMP(dep)`.

## DESENELE

### 1 — `fata_elev`: elevatia peretelui, la scara

Rama **1970**, verticale **1552**. Layout cotat cap la cap, masurat de la fata interioara a stalpului stang:

```
115 camp | jamba | fereastra 161 → 731 | jamba | usa 938 → 1488 | jamba | montant de camp 1650 → 1696 | colt 274
```

Coltul de **274** e locul propteaței de **250**. Prag + buiandrug fereastra: **570, intre jambe** — nu peste ele.

Caption: `Peretele din fata — rama 1970, verticale 1552. Cotele merg de la fata interioara a stalpului stang.`

Commit: `E5: elevatia peretelui din fata`

### 2 — `fata_bara`: bara de sus, 100×60 taiata la 2155

Sectiune care arata **de ce 2155 si nu 1970**: bara trebuie sa calce pe rama SI pe amandoi stalpii de 90×90. Coteaza cat iese peste fiecare stalp. Latura de **60 in sus**, 100 pe orizontala.

Caption: `Bara de sus, 100×60 taiata la 2155 — calca pe rama si pe amandoi stalpii.`

Commit: `E5: bara de sus peste cei doi stalpi`

### 3 — `fata_stalp`: prinderea finala a stalpului din fata

**4 × surub dulgherie 8×140** oblic la **15–20°** in grinda de dedesubt — doua de-o parte, doua de cealalta — plus **coltar 90×65 pe fiecare fata a stalpului**. Doua vederi alaturate: din fata si in sectiune, cu unghiul cotat.

Scrie pe desen: **tot de sus, fara piulite, fara tije prin podea.**

Caption: `Prinderea finala a stalpului din fata — 4 suruburi 8×140 oblice plus coltare. Nu exista tije M12 in podea.`

Commit: `E5: prinderea finala a stalpilor din fata`

### 4 — `fata_usa`: golul de usa, ordinea de taiere

Doua stari alaturate:
- **inainte** — talpa intreaga, peretele rigid, gata de ridicat
- **dupa** — talpa taiata, gol **550** latime, **1600** liber pe verticala

Intre ele, eticheta: **taierea se face ultima, cu peretele deja ridicat, legat si verificat la echer.**

Caption: `Golul de usa — talpa se taie ultima, dupa ce peretele e ridicat si verificat la echer.`

Commit: `E5: golul de usa, taierea talpii la final`

## CONSTRAINTS

- Romana, fara diacritice.
- **Nu inventa cote.** Fiecare numar e in brief-ul asta sau in constantele existente. Daca un desen cere ceva ce n-ai — un unghi de teșire, o distanta intre suruburi — deseneaza-l fara cota aia si pune un bloc `stop` in capitol care spune ce lipseste. Precedentul e in `e0`. **Nu estima.**
- Citibil la **390 px**. Daca un desen nu incape, sparge-l in doua figuri cu captions separate.
- Nu atinge alte capitole, alte figuri, `gen_2d.py`, sau `LISTA-LEROY`.
- Fara deploy.

## DONE MEANS

- `<svg>` pe sectiune: **e3=4 · e4=6 · e5=5 · e6=2 · e7=0**
- Cele 4 chei `fata_*` folosite in `build_ghid.py`, fiecare cu captionul de mai sus.
- `grep` pe HTML gaseste in `e5`: `1970` `1552` `115` `161` `731` `938` `1488` `1650` `1696` `274` `570` `2155` `8×140` `90×65` `550` `1600`.
- **`git log --oneline -5` arata patru commituri separate de desen**, plus unul de STATUS.
- `python3 gen_ghid.py && python3 build_ghid.py` ies 0. Consola paginii curata.

## VERIFY

Dupa fiecare desen, inainte de commitul lui:
- **randeaza si uita-te la figura.** SVG valid nu inseamna desen corect. Cauta text iesit din cadru, cote suprapuse, linii de cota care arata spre nimic.

La final, peste tot capitolul:
- desktop **si 390 px**, consola curata, fiecare punct din DONE MEANS confirmat individual.
- **Testul de suma pe desenul 1:** `115 + jamba + (731−161) + jamba + (1488−938) + jamba + (1696−1650) + 274` trebuie sa dea **1970** cu jambele reale. Daca nu da, o cota e gresita — **opreste-te si scrie in STATUS.md**, nu ajusta pe ghicite.

## IF STUCK

- **Latimea jambei nu e nicaieri** → e distanta dintre cotele date (de exemplu 161 − 115 = 46). Daca suma nu se inchide, `stop` si STATUS.md.
- **Nu poti desena 3 fara grosimea grinzii de dedesubt** → ia-o din `SCHEME-2D-casa.html`, care are sectiuni prin podea. Daca nici acolo nu e, `stop`.
- **Ramai fara aer** → nu incepe un desen nou. Comite ce ai, scrie in STATUS.md exact care lipsesc, si opreste-te.
