MODEL: haiku

# BRIEF — commit fise achizitie + Leroy (2026-08-06)

## GOAL
Comise: actualizarea Leroy din FISA-FAZA-2, noua FISA-ACHIZITIE si STATUS. Fara push (403 cunoscut — pushul e la Vlad).

## PASI
1. Un singur commit — mesaj: `fisa achizitie 3 obiecte + preturi/stoc Leroy Colosseum verificate live in FISA-FAZA-2`
   git add exact: `FISA-FAZA-2-casa-gard-scara.html`, `FISA-FAZA-2-casa-gard-scara.pdf`, `FISA-ACHIZITIE-faza-2.html`, `FISA-ACHIZITIE-faza-2.pdf`, `STATUS.md`.

## CONSTRAINTS
- Zero editare de continut. NU push. NU comite fisierul RUNNING al acestui brief.
- `NEEDS-INPUT-hygiene-push-2026-08-06.md` ramane in radacina (reminder activ pt push).
- Alte fisiere modificate/untracked in afara listei: lasa-le, noteaza-le.

## DONE MEANS
- `git status` curat, cu exact 2 exceptii: RUNNING-brieful asta + NEEDS-INPUT-hygiene-push.
- `git log -1` arata commit-ul de mai sus cu cele 5 fisiere.

## VERIFY
`git status` + `git show --stat HEAD`; confirma DONE MEANS punct cu punct; apoi o linie scurta in STATUS.md (data, hash, "push ramane la Vlad") comisa intr-un mic commit separat `STATUS: nota commit achizitie`.
