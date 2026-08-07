MODEL: haiku

# BRIEF — commit fise de montaj + hub actualizat (2026-08-06)

## GOAL
Comise: cele 3 fise de montaj (HTML+PDF), FISA-ACHIZITIE actualizata, PLAN-FAZA-2 rescrisa cu vizualuri, STATUS. Fara push (403 cunoscut — pushul e la Vlad).

## PASI
1. Un singur commit — mesaj: `fise montaj balustrada/scara/casa + hub cu vizualuri + corectii propagate (8 stalpisori, tacheti, M1-M5)`
   git add exact:
   `FISA-MONTAJ-balustrada.html`, `FISA-MONTAJ-balustrada.pdf`,
   `FISA-MONTAJ-scara.html`, `FISA-MONTAJ-scara.pdf`,
   `FISA-MONTAJ-casa.html`, `FISA-MONTAJ-casa.pdf`,
   `FISA-ACHIZITIE-faza-2.html`, `FISA-ACHIZITIE-faza-2.pdf`,
   `PLAN-FAZA-2.html`, `STATUS.md`.

## CONSTRAINTS
- Zero editare de continut. NU push. NU comite fisierul RUNNING al acestui brief.
- `NEEDS-INPUT-hygiene-push-2026-08-06.md` ramane in radacina (reminder activ pentru pushul manual).
- Daca `BRIEF-commit-fise-montaj-2026-08-06.md` a ramas neprocesat in radacina, muta-l in `_archive/briefs/` si include mutarea in acelasi commit (a fost inlocuit de brieful asta).
- Alte fisiere in afara listei: lasa-le necomise, noteaza-le in raport.

## DONE MEANS
- `git log -1` arata commit-ul cu cele 10 fisiere.
- `git status` curat, cu exceptiile permise (RUNNING-brieful asta, NEEDS-INPUT, DONE-briefuri neaarhivate).
- Radacina nu contine `BRIEF-commit-fise-montaj-2026-08-06.md` neprocesat.

## VERIFY
`git show --stat HEAD` + `git status`; confirma fiecare DONE MEANS punct cu punct; apoi o linie scurta in STATUS (data, hash, "push la Vlad") intr-un commit separat `STATUS: nota commit fise+hub`.
