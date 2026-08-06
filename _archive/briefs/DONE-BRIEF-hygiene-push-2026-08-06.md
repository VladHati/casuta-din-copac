MODEL: sonnet

# BRIEF — igiena git + push (2026-08-06)

## GOAL
Repo-ul curat si pushuit: tot working tree-ul acumulat din 24.07 + livrabilele de azi comise, briefurile procesate arhivate, origin/main la zi, site-ul live la zi. Zero editare de continut — asta e doar livrare.

## CONTENT / PASI (in ordinea asta)
0. Sterge `.git/index.lock` (creat 06.08 10:12 de un audit din Cowork; e gol, sigur de sters). Daca nu exista, mergi mai departe.
1. Muta in `_archive/briefs/`: `FAILED-BRIEF-audit-fixes-2026-07-24.md` si `FAILED-BRIEF-audit-fixes-2026-07-24-v2.md`. (Cele 2 DONE-BRIEF din radacina sunt deja mutate pe disc — miscarea e doar necomisa.)
2. Commit 1 — mesaj: `podea as-built + audit 08-06 + fisa faza 2: livrabile, poze, decizii`
   Include (git add exact): `STATUS.md`, `CASA-plan-constructie.html`, `AUDIT-2026-07-24.md`, `AUDIT-2026-08-06.md`, `FISA-CONTINUARE-podea.html`, `FISA-CONTINUARE-podea.pdf`, `SCHEMA-montaj-podea.svg`, `SCHEMA-montaj-podea.pdf`, `SCHEMA-detaliu-coltar-C2.svg`, `SCHEMA-detaliu-coltar-C2.pdf`, `FISA-FAZA-2-casa-gard-scara.html`, `FISA-FAZA-2-casa-gard-scara.pdf`, `POZE/IMG_2270.jpeg` ... `POZE/IMG_2278.jpeg`, `POZE/IMG_2284.jpeg` ... `POZE/IMG_2288.jpeg`, `POZE/2A9524F8-D67F-4625-A41D-E5DB7A58376B.jpg`, `POZE/370FC8FA-F858-4C0D-A61B-7292E901D930.jpg`, `POZE/643DC17B-EB72-48FC-AECD-1D4C949154E6.jpg`.
3. Commit 2 — mesaj: `igiena: arhivare briefuri procesate (DONE 07-23, FAILED 07-24 v1+v2)`
   Include: stergerile din radacina (cele 2 DONE-BRIEF) + `_archive/briefs/` cu cele 4 fisiere mutate.
4. `git push origin main`.

## CONSTRAINTS
- NU edita continutul niciunui fisier. Doar mutari, add, commit, push.
- NU comite fisierul acestui brief (RUNNING-*).
- NU folosi `git add -A` orb — daca apar fisiere neasteptate fata de lista de mai sus, lasa-le necomise si noteaza-le in raportul final.

## DONE MEANS
- `git status` curat (singura exceptie permisa: fisierul RUNNING al acestui brief).
- `git rev-parse origin/main` == `git rev-parse HEAD` (push reusit).
- Radacina nu mai contine niciun `DONE-BRIEF-*` / `FAILED-BRIEF-*`; toate 4 sunt in `_archive/briefs/`.
- Site-ul live (casuta-din-copac.netlify.app/timeline.html) contine textul `Talpic + polite` — dovada ca fix-urile din 983b346 au ajuns live.

## VERIFY
Ruleaza `git status`, `git log --oneline -4`, `git rev-parse HEAD origin/main` si deschide timeline-ul live; confirma fiecare DONE MEANS punct cu punct inainte sa scrii DONE in STATUS.md. Adauga in STATUS.md o linie: data, commit-urile (hash-uri), push facut, site verificat.

## IF STUCK
- index.lock reapare la commit → sterge-l si reincearca o singura data; daca reapare iar, NEEDS-INPUT cu detalii.
- Push respins (non-fast-forward) → STOP, NEEDS-INPUT. NU face force push.
- Site-ul live nu reflecta push-ul dupa ~5 min → noteaza in STATUS (deploy Netlify intarziat), nu e blocant pentru DONE daca restul criteriilor trec.
