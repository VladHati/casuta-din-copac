MODEL: sonnet

# BRIEF — leaga cele 5 desene de perete lateral in capitolul E4

## GOAL

Cele 5 figuri ale peretilor laterali sunt deja desenate si randate. Nu sunt legate in ghid. Le montezi si comiti.

Rularea precedenta (`FAILED-BRIEF-desene-etape-casa.md`) a apucat sa scrie desenele in `gen_ghid.py` si sa le randeze in `figs_ghid.json`, apoi s-a oprit inainte sa atinga `build_ghid.py`. **Desenele sunt bune, verificate vizual. Nu le redesena, nu le atinge.**

## CE EXISTA DEJA

`figs_ghid.json` are aceste chei noi, nefolosite de nimeni:

| cheie | ce e |
|---|---|
| `lat_stanga` | elevatie perete lateral stanga (talpa 1580, cununa 1596) |
| `lat_dreapta` | elevatie perete lateral dreapta (talpa 1570, cununa 1586) |
| `lat_geam` | detaliu gol de geam, sectiune orizontala |
| `lat_colt` | detaliu colt cu contrafisa |
| `lat_sect` | sectiune prin perete cu lambriul in falt |

`gen_ghid.py` le genereaza deja. **Nu modifica `gen_ghid.py`.**

## CE FACI

In `build_ghid.py`, in blocul capitolului `e4` („Peretii laterali"):

1. Monteaza `lat_stanga` si `lat_dreapta` ca doua figuri separate, una dupa alta, **fiecare cu `figcaption` proprie**. Nu le pune in aceeasi figura si nu scrie o nota de tipul „la fel, dar cu 1570" — omul lucreaza cu un perete o data, iar cele doua talpi difera cu 10 mm.
   - caption stanga: `Perete lateral stanga — talpa 1580, cununa 1596`
   - caption dreapta: `Perete lateral dreapta — talpa 1570, cununa 1586`
2. Monteaza `lat_sect` imediat dupa elevatii. Caption: `Sectiune prin perete — rama 48×48, lambriu 12,5×96 in falt`
3. Monteaza `lat_geam` in dreptul pasului despre golul de geam. Caption: `Golul de geam — acrilic 440 in gol 490, 25 mm joc de jur imprejur`
4. Monteaza `lat_colt` in dreptul pasului despre contrafise. Caption: `Coltul — contrafisa 212 pe diagonala, brat 150`

Foloseste helperul `fig(svg, cap)` existent. Figurile de elevatie (`lat_stanga`, `lat_dreapta`) merg `wide=True`; restul normal.

## CURATENIE

`_check.html` si `_check.png` sunt fisiere de lucru ramase din rularea precedenta. Adauga-le in `.gitignore` (`_check.*`). Nu le comite.

## CONSTRAINTS

- Romana, fara diacritice.
- **Modifici un singur fisier de cod: `build_ghid.py`.** Plus `.gitignore`.
- Nu atinge `gen_ghid.py`, `gen_2d.py`, celelalte capitole, sau desenele existente din `e3`.
- Fara deploy.

## DONE MEANS

- Numarul de `<svg>` pe sectiune in HTML-ul construit: **e3=4 · e4=6 · e5=1 · e6=2 · e7=0**.
  (`e4` are 1 desen general dinainte + cele 5 noi.)
- Toate cele 5 chei `lat_*` apar folosite in `build_ghid.py`.
- Fiecare din cele 5 figuri noi are `figcaption`, cu textele de mai sus.
- `.gitignore` contine `_check.*`.
- `python3 build_ghid.py` iese 0. Consola paginii curata.

## VERIFY

Deschide rezultatul la desktop **si la 390 px**, consola curata, apoi confirma fiecare punct din DONE MEANS individual.

In plus:
- **Uita-te la capitolul e4 randat.** Cele doua elevatii trebuie sa fie vizibil diferite. Daca arata identic, ai montat aceeasi cheie de doua ori.
- La 390 px niciun desen nu forteaza scroll orizontal.
- **Scrie linia in `STATUS.md`, apoi comite.** Ultimele trei rulari au facut treaba si au murit fara sa raporteze. Raportarea e parte din treaba, nu un extra.

## IF STUCK

- **O cheie `lat_*` lipseste din `figs_ghid.json`** → ruleaza `python3 gen_ghid.py` o data ca sa regenerezi, apoi verifica din nou. Daca tot lipseste, monteaza-le pe cele care exista, si scrie in STATUS.md care lipseste.
- **Helperul `fig()` nu accepta `wide`** → monteaza-le normal, fara `wide`. Nu rescrie helperul.
