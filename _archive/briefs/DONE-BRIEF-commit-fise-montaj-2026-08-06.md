MODEL: haiku

# BRIEF — commit fise de montaj F2/F3/F4 (2026-08-06)

## GOAL
Comise cele 3 fise de montaj detaliate (balustrada, scara, casa), HTML + PDF, si STATUS. Fara push (403 cunoscut — pushul e la Vlad).

## PASI
1. Un singur commit — mesaj: `fise montaj detaliate: balustrada, scara, casa (desene la scara + cut list + pas cu pas)`
   git add exact: `FISA-MONTAJ-balustrada.html`, `FISA-MONTAJ-balustrada.pdf`, `FISA-MONTAJ-scara.html`, `FISA-MONTAJ-scara.pdf`, `FISA-MONTAJ-casa.html`, `FISA-MONTAJ-casa.pdf`, `STATUS.md`.

## CONSTRAINTS
- Zero editare de continut. NU push. NU comite fisierul RUNNING al acestui brief.
- `NEEDS-INPUT-hygiene-push-2026-08-06.md` ramane in radacina.
- Alte fisiere modificate/untracked in afara listei: lasa-le, noteaza-le in raport.

## DONE MEANS
- `git log -1` arata commit-ul cu exact cele 7 fisiere.
- `git status` curat cu exceptiile permise (RUNNING-brieful asta, NEEDS-INPUT, DONE-briefuri neaarhivate inca).

## VERIFY
`git show --stat HEAD` + `git status`; confirma DONE MEANS punct cu punct; apoi o linie scurta in STATUS (data, hash, "push la Vlad") intr-un commit separat `STATUS: nota commit fise montaj`.
