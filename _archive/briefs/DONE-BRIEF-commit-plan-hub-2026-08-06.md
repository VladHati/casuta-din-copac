MODEL: haiku

# BRIEF — commit plan hub faza 2 (2026-08-06)

## GOAL
Comis: noua pagina-hub `PLAN-FAZA-2.html` + STATUS actualizat. Fara push (403 cunoscut — pushul e la Vlad).

## PASI
1. Un singur commit — mesaj: `PLAN-FAZA-2: pagina-hub navigabila a fazei 2 (stare, decizii, F1-F4, cumparaturi, siguranta)`
   git add exact: `PLAN-FAZA-2.html`, `STATUS.md`.

## CONSTRAINTS
- Zero editare de continut. NU push. NU comite fisierul RUNNING al acestui brief.
- NEEDS-INPUT-hygiene-push ramane in radacina. Alte fisiere in afara listei: lasa-le, noteaza-le.
- NU lega inca pagina in nav-ul site-ului (desene.html / generator) — aia e treaba separata, doar daca Vlad o cere.

## DONE MEANS
- `git log -1` arata commit-ul cu exact cele 2 fisiere.
- `git status` curat cu exceptiile permise (RUNNING-brieful asta, NEEDS-INPUT, eventuale DONE-briefuri de arhivat data viitoare).

## VERIFY
`git show --stat HEAD` + `git status`; confirma DONE MEANS punct cu punct; o linie scurta in STATUS (data, hash, "push la Vlad") intr-un commit separat `STATUS: nota commit plan-hub`.
