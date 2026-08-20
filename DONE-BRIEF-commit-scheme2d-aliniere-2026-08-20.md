MODEL: haiku

# BRIEF — commit schemele 2D + alinierea documentelor vechi

## GOAL

Comite doua loturi din 20.08: schemele 2D noi ale casei, si alinierea documentelor vechi la geometria remasurata. Zero editari de continut — fisierele sunt scrise si verificate. Commit-only.

## CONTENT

Toate fisierele exista in radacina proiectului. **Nu le modifica, nu le regenera**, nu rula `gen_2d.py`, `gen_ghid.py`, `build_ghid.py` sau `build_pdfs.py`.

**COMMIT 1 — scheme 2D si ghidul de constructie**

```
SCHEME-2D-casa.html
gen_2d.py
GHID-CONSTRUCTIE-casa.html
gen_ghid.py
build_ghid.py
```

Mesaj:

```
Scheme 2D ale casei + ghid de constructie pe etape

SCHEME-2D-casa: sapte vederi ortogonale (plan, sectiune
longitudinala, elevatii spate/lateral/fata, plan acoperis,
detaliu straturi). Toate derivate dintr-un singur model
numeric in gen_2d.py, cu auto-verificare pe 18 marimi la
fiecare generare.

Inlocuiesc izometriile din GHID-CONSTRUCTIE si Detaliul 7
din SCHEME-CASA: acelea fusesera desenate din descriere,
nu din geometria reala, si erau gresite.

GHID-CONSTRUCTIE-casa: ghid de santier E0-E4 (golul de la
colturile din spate, restantele podelei si cioata, drumul
la Leroy, taierea fasiilor, peretele din spate), cu cuprins
lateral si bife de progres.

Detaliul coltului din spate NU e desenat inca — nu exista
o poza care sa arate stalpul, marginea podelei si golul in
acelasi cadru. De completat dupa ce apare poza.
```

**COMMIT 2 — alinierea documentelor vechi**

```
SOURCE-OF-TRUTH.md
project-instructions.md
CASUTA-DIN-COPAC.md
GHID-SIMPLU-casa.html
GHID-SIMPLU-casa.pdf
MANUAL-FAZA-2.html
MANUAL-FAZA-2.pdf
```

Mesaj:

```
Aliniere: documentele vechi nu mai contrazic geometria reala

Toate tineau planul dinainte de masuratorile din 20.08:
reazem 1950, panta 15,6 grade, caprior 1342, dulap 46x250,
adancime 1100.

SOURCE-OF-TRUTH rescris: nu stia ca exista PROIECT-CASA,
SCHEME-CASA sau LISTA-LEROY, si declara MANUAL-FAZA-2
sursa unica pentru casa. Acum are tabelul de guvernanta
corect, cotele masurate, si o lista de trasee moarte.

CASUTA-DIN-COPAC.md era declarat canonic pe geometrie si
purta si el cotele moarte.

GHID-SIMPLU si MANUAL-FAZA-2: banner de avertizare in cap,
tabelele de inaltimi corectate. Geometria veche e marcata
istorica, nu stearsa. In GHID a fost rescrisa si afirmatia
ca exista doua tije M12 in podea la stalpii casei - nu au
existat niciodata (corectat 18.08).

Ce ramane valabil: detaliile de perete din GHID, balustrada
si scara din MANUAL.
```

## CONSTRAINTS

- **Commit-only.** Daca ceva pare gresit intr-un document, NU-l repara — noteaza in `NEEDS-INPUT-scheme2d-2026-08-20.md` si comite restul.
- **Nu face push.** Contul Builder primeste 403. Push-ul ramane la Vlad.
- `_to_delete/` e in `.gitignore` — nu-l atinge, nu-l comite.
- `figs_2d.json` si `figs_ghid.json` sunt artefacte regenerabile — daca apar, nu le comite (verifica `.gitignore`; daca nu sunt acolo, adauga-le).
- `DONE-BRIEF-commit-geometrie-reala-2026-08-20.md` a ramas necomis din runda anterioara: comite-l in COMMIT 2, cu restul.
- Nu atinge `_archive/`.

## DONE MEANS

- `git log --oneline -2` arata cele doua commit-uri noi, in ordinea de mai sus
- `git status --short` e curat, in afara de ce ignora `.gitignore`
- `git show --stat HEAD~1` listeaza exact cele 5 fisiere din COMMIT 1
- `git show --stat HEAD` listeaza cele 7 fisiere din COMMIT 2 plus DONE-BRIEF-ul
- Niciun fisier pe care brieful nu-l numeste nu apare in `git diff HEAD~2 HEAD --stat`

## VERIFY

Inainte de a scrie DONE in STATUS.md: ruleaza `git log --oneline -2`, `git status --short`, `git show --stat HEAD~1` si `git show --stat HEAD`, apoi confirma fiecare punct din DONE MEANS unul cate unul. Verifica explicit ca nu ai facut push — `git status -sb` trebuie sa arate `ahead 2`. Daca ceva nu trece, repara si re-verifica; nu raporta done pe o verificare picata.

## IF STUCK

- Fisier lipsa → comite restul, noteaza in STATUS care lipsea.
- `.git/index.lock` prezent → sterge-l intai. (A fost deja curatat o data azi; daca reapare, e semn ca ruleaza doua procese git in paralel — noteaza asta in STATUS.)
- Conflict de merge → nu rezolva, opreste-te si scrie `NEEDS-INPUT-scheme2d-2026-08-20.md`.
- Daca `git log` arata ca vreun fisier din liste a fost deja comis de altcineva intre timp, **sari peste el** si scrie in STATUS care a fost — nu-l recomite si nu esua din cauza asta.
