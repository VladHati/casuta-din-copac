MODEL: haiku
EFFORT: low

# BRIEF — commit-only 18.08: SCHEME-CASA + LISTA-LEROY (fisiere noi) + corectia tijelor M12 + STATUS

## GOAL

Doar git. Niciun fisier nu se editeaza, nu se regenereaza, nu se rescrie — toate exista deja pe disc, scrise de Main prin bridge.

## PAS 0

Daca exista `.git/index.lock` (0 bytes, vechi): sterge-l O data si continua. Daca reapare dupa stergere: STOP, scrie NEEDS-INPUT cu eroarea exacta.

## COMMIT 1 — fisiere noi: SCHEME-CASA + LISTA-LEROY

```
git add SCHEME-CASA-2026-08-17.html SCHEME-CASA-2026-08-17.pdf LISTA-LEROY-2026-08-17.html LISTA-LEROY-2026-08-17.pdf
git commit -m "adauga SCHEME-CASA (5 schite la scara) + LISTA-LEROY (cumparaturi cu linkuri) - livrare 17.08 sincronizata cu intarziere (bridge deconectat)"
```

## COMMIT 2 — corectia tijelor M12 (AUDIT + PROIECT-CASA + gen_scheme.py)

```
git add AUDIT-2026-08-17.md PROIECT-CASA-2026-08-17.html PROIECT-CASA-2026-08-17.pdf gen_scheme.py
git commit -m "corectie: tijele M12 nu au existat niciodata pe santier (confirmat Vlad 18.08) - prindere finala stalpi fata rescrisa site-gated (bulon vs suruburi oblice), layout S0 mutat pe stalpii din fata; reparat si un bug vechi de etichete suprapuse in schema S4"
```

## COMMIT 3 — STATUS + arhivare hygiene

```
git add STATUS.md
git mv NEEDS-INPUT-commit-2026-08-17.md _archive/briefs/ 2>/dev/null || true
git mv DONE-BRIEF-commit-audit-proiect-2026-08-17.md _archive/briefs/ 2>/dev/null || true
git mv DONE-BRIEF-commit-continue-2026-08-17.md _archive/briefs/ 2>/dev/null || true
git add -A
git commit -m "STATUS 18.08 + arhivare briefuri procesate (NEEDS-INPUT rezolvat de brieful continue din 17.08, ambele DONE-BRIEF)"
```

Daca vreun `git mv` de mai sus da eroare (fisier deja mutat / nu exista), sari peste linia aia si continua — nu e blocant, doar hygiene de radacina.

## DONE MEANS

- 3 commituri noi peste HEAD-ul actual (ultimul cunoscut: `f1ef625`).
- `git status --short` curat, minus brieful asta (RUNNING) si eventuale fisiere .DS_Store.
- Push NU se face de aici (403 cunoscut, fara credentiale Builder) — ramane la Vlad.
