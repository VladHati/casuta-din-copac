MODEL: haiku

# BRIEF — commit capitolul E0 detaliat + versiunile finale 2D

## GOAL

Doua commit-uri. Primul: ghidul si schemele in versiunea din care au fost scoase
izometriile. Al doilea: capitolul E0 nou, detaliat, plus fisa de masurat.
Toate fisierele sunt deja pe disc, scrise si verificate din Main. **Commit-only.**

## CONTEXT

`331dcd7` a comis o versiune intermediara a ghidului, cu 8 desene izometrice
reconstituite din descriere. Vlad le-a respins ("complet eronate"). Au fost scoase
toate. Apoi a cerut mult mai mult detaliu, in special pe scandura care lipseste la
colturile din spate — de acolo vine capitolul E0 separat.

## CONTENT

**Nu modifica, nu regenera.** Nu rula `gen_2d.py`, `gen_ghid.py`, `build_ghid.py`,
`gen_e0.py`, `build_e0.py`, `gen_masura.py`, `build_masura.py`.

### COMMIT 1 — versiunile fara izometrii

```
GHID-CONSTRUCTIE-casa.html
SCHEME-2D-casa.html
gen_2d.py
gen_ghid.py
build_ghid.py
```

Mesaj:

```
Scoase izometriile din ghid; totul pe desene 2D verificate

GHID-CONSTRUCTIE: de la 13 SVG la 5. Cele 8 izometrii
fusesera desenate din descriere, nu din geometria reala.
Ce a ramas sunt elevatii si sectiuni ortogonale derivate
din modelul numeric unic: cioata (E1), taierea dulapului
in fasii (E3), elevatia peretelui din spate si prinderea
in stalp (E4), ridicarea panoului pe rampa.

E0 nu mai are desene aici — a devenit document separat,
GHID-E0-golul-din-spate.html.

SCHEME-2D: 9 vederi (de la 7). Adaugate detaliul de
taiere a dulapului in lung si detaliul de prindere a
peretelui in stalp. Sectiunea #colt spune explicit ca
desenul lipseste si ce poza trebuie facuta.

Reparate suprapuneri de etichete in gen_ghid.py: "puntea"
si "taiat la 600-750" intrau in linia puntii, "= treapta
directa pe acoperis" intra in stalpul din dreapta (rupt
pe doua randuri), cota "700 dupa" statea pe piciorul
masutei, "unul jos, impinge" atingea rampa.
```

### COMMIT 2 — capitolul E0 si fisa de masurat

```
GHID-E0-golul-din-spate.html
MASOARA-GOL.html
kit.py
gen_e0.py
build_e0.py
gen_masura.py
build_masura.py
DONE-BRIEF-commit-scheme2d-aliniere-2026-08-20.md
```

Mesaj:

```
E0 in adancime: scandura care lipseste la colturile din spate

Capitol separat, 12 desene 2D, toate generate dintr-un
singur model numeric in gen_e0.py. Sectiuni si planuri
ortogonale — nicio izometrie.

Structura: situatia (unde e golul, plan + sectiune),
de ce nu merge doar o scandura peste el (comparatie
gresit/corect + drumul greutatii), piesele la scara cu
tabel de cantitati, patru pasi cu cate o sectiune
fiecare (vinclu, blocaj, suruburi 8x140 oblice, scandura
de calcat), si sectiunea finala. Sapte bife de progres.

Corectie fata de BLOCAJ-COLT: santul are lemn portant
doar pe o latura — pe cealalta e marginea puntii, adica
aer. Blocajul e deci o consola pe polite, nu o grinda pe
doua reazeme. Textul si desenele spun asta explicit.

Numarul de vincluri nu mai e fix la 2 pe fasie: se
calculeaza, unul la fiecare ~150 mm de sant.

A, B si C (latimile golului si adancimea) sunt INCA
NOMINALE — nu au fost masurate. Formele sunt corecte,
proportiile nu. MASOARA-GOL.html e fisa de teren pentru
cele trei numere; cand vin, se schimba trei linii in
capul lui gen_e0.py si toate desenele se refac la scara.

kit.py: trusa comuna de desen 2D (primitive in mm,
adnotari in px, bbox auto-fit, hasura de sectiune,
suruburi, vincluri, zone de necunoscut).
```

## CONSTRAINTS

- **Commit-only.** Daca ceva pare gresit, NU repara — noteaza in
  `NEEDS-INPUT-e0-2026-08-20.md` si comite restul.
- **Nu face push.** Contul Builder primeste 403. Push-ul ramane la Vlad.
- `figs_2d.json`, `figs_ghid.json`, `figs_ikea.json`, `figs_e0.json`, `figs_masura.json`
  sunt artefacte regenerabile — nu le comite. `.gitignore` are deja doua reguli `figs`;
  verifica sa le acopere pe toate, si completeaza daca nu.
- Fisierele `_*.png` si `_*.html` din radacina, daca apar, sunt randari de verificare —
  nu le comite.
- `_to_delete/` e in `.gitignore` — nu-l atinge. Nu atinge `_archive/`.

## DONE MEANS

- `git log --oneline -2` arata cele doua commit-uri noi, in ordinea de mai sus
- `git show --stat HEAD~1` listeaza exact cele 5 fisiere din COMMIT 1
- `git show --stat HEAD` listeaza exact cele 8 fisiere din COMMIT 2
- `git status --short` e curat, in afara de ce ignora `.gitignore`
- `git status -sb` arata `ahead 5` — NU s-a facut push

## VERIFY

Inainte de a scrie DONE in STATUS.md, ruleaza si confirma unul cate unul:
`git log --oneline -2`, `git show --stat HEAD~1`, `git show --stat HEAD`,
`git status --short`, `git status -sb`.

In plus, verifica numarul de desene cu `grep -c '<svg'`:

```
GHID-CONSTRUCTIE-casa.html      5
SCHEME-2D-casa.html             9
GHID-E0-golul-din-spate.html   12
MASOARA-GOL.html                2
```

Daca vreun numar nu se potriveste, fisierul de pe disc e o versiune veche —
opreste-te si scrie NEEDS-INPUT in loc sa comiti.

## IF STUCK

- `.git/index.lock` prezent → sterge-l intai. A aparut de trei ori azi; sesiunea Main
  nu-l poate sterge (mount-ul nu permite unlink), deci ramane in sarcina ta. Daca
  reapare imediat dupa stergere, ruleaza doua procese git in paralel — noteaza in STATUS.
- Conflict de merge → nu rezolva, scrie NEEDS-INPUT.
- Fisier deja comis de altcineva intre timp → sari peste el, noteaza in STATUS.

## IN PLUS — doua corectii in STATUS.md

1. Linia scrisa la `643cc55` spune ca M5 (inaltimea stalpilor din fata peste podea) e
   in asteptare. Nu e: Vlad a confirmat 20.08 ca **M5 = 1600**.
2. Adauga la golurile deschise: **golul de la colturile din spate nu e masurat**
   (A, B, C din `MASOARA-GOL.html`). E blocantul pentru E0, si E0 e poarta de faza
   inainte de peretele din spate.
