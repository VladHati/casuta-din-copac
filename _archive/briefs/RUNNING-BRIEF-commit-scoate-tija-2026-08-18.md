MODEL: haiku
EFFORT: low

# BRIEF — commit-only 18.08 (runda 2): tija SCOASA definitiv, ramane doar varianta cu suruburi

## CONTEXT

Brieful anterior (`DONE-BRIEF-commit-scheme-lista-corectie-tije-2026-08-18.md`) a comis deja o prima runda — varianta "site-gated" (tija+piulita SAU suruburi oblice, de decis pe santier). Intre timp Vlad a decis: podeaua e deja inchisa peste zona aia, nu se mai sparge acum pentru tija. A ramas DOAR varianta cu suruburi oblice. Fisierele de mai jos sunt deja rescrise pe disc (de Main, prin bridge) ca sa reflecte asta — inlocuiesc continutul comis de brieful anterior.

## GOAL

Doar git. Niciun fisier nu se editeaza, nu se regenereaza — toate exista deja pe disc.

## PAS 0

Daca exista `.git/index.lock` (0 bytes, vechi): sterge-l O data si continua. Daca reapare: STOP, scrie NEEDS-INPUT cu eroarea exacta.

## COMMIT 1 — varianta finala fara tija

```
git add AUDIT-2026-08-17.md PROIECT-CASA-2026-08-17.html PROIECT-CASA-2026-08-17.pdf LISTA-LEROY-2026-08-17.html LISTA-LEROY-2026-08-17.pdf SCHEME-CASA-2026-08-17.html SCHEME-CASA-2026-08-17.pdf gen_scheme.py
git commit -m "tija M12 scoasa definitiv (decizie Vlad 18.08 - podeaua deja inchisa, nu se mai sparge): prinderea finala a stalpilor din fata = doar 4 suruburi 8x140 oblice + 2 coltare 90x65, fara piulite, fara tija. Actualizat AUDIT, PROIECT-CASA S4, SCHEME-CASA (schema 6 redesenata), LISTA-LEROY (randul cu tija scos, cantitati suruburi/vincluri ajustate)"
```

## COMMIT 2 — STATUS

```
git add STATUS.md
git commit -m "STATUS: varianta finala fara tija (runda 2, 18.08)"
```

## DONE MEANS

- 2 commituri noi peste HEAD-ul actual (ultimul cunoscut: commit-ul din `DONE-BRIEF-commit-scheme-lista-corectie-tije-2026-08-18`).
- `git status --short` curat, minus brieful asta (RUNNING) si eventuale fisiere .DS_Store.
- Push NU se face de aici — ramane la Vlad.
