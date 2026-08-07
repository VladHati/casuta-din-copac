MODEL: haiku

# BRIEF — igiena v2: restul commit-ului (2026-08-06)

## GOAL
Ultimul delta comis: fix-ul de layout din FISA (tabel totaluri) + SoT + STATUS, si DONE-brieful v1 arhivat. Fara push (403 cunoscut — pushul e la Vlad, deja notat in STATUS si NEEDS-INPUT).

## PASI
1. Commit — mesaj: `fisa faza 2: fix tabel totaluri + SoT decizii 06.08 + STATUS main`
   git add exact: `FISA-FAZA-2-casa-gard-scara.html`, `FISA-FAZA-2-casa-gard-scara.pdf`, `SOURCE-OF-TRUTH.md`, `STATUS.md`.
2. Muta `DONE-BRIEF-hygiene-push-2026-08-06.md` in `_archive/briefs/` si include mutarea intr-un al doilea commit: `igiena: arhivare brief hygiene-push v1`.
3. `NEEDS-INPUT-hygiene-push-2026-08-06.md` RAMANE in radacina — e reminderul activ pentru pushul manual al lui Vlad. NU-l arhiva.

## CONSTRAINTS
- Zero editare de continut. NU incerca push. NU comite fisierul RUNNING al acestui brief.
- Daca apar alte fisiere modificate/untracked fata de lista: lasa-le, noteaza-le in STATUS.

## DONE MEANS
- `git status` curat, cu exact 2 exceptii permise: RUNNING-brieful asta + `NEEDS-INPUT-hygiene-push-2026-08-06.md`.
- `git log -2` arata cele 2 commit-uri de mai sus.
- Radacina: fara DONE-BRIEF-*.

## VERIFY
Ruleaza `git status` + `git log --oneline -3`, confirma fiecare DONE MEANS, apoi adauga in STATUS.md o linie scurta (data, hash-uri, "push ramane la Vlad") si include-o in commitul 1 (fa intai linia, apoi commit).
