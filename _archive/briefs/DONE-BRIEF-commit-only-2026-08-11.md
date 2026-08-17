MODEL: haiku

# BRIEF — Commit-only: salveaza munca existenta (ZERO editari de continut)

## GOAL

Tot ce e pe disc intra in git, exact cum e. Nu editezi, nu regenerezi, nu "repari" nimic. Doar git add / git mv / git commit.

## CONTEXT

Rularea v2 (FAILED 11.08) a lasat editari de continut CORECTE si necomise. Auditul din 11.08 (`AUDIT-2026-08-11.md`) le-a verificat: sunt bune. Brieful asta doar le salveaza. Continutul se aduce la zi intr-un brief separat, DUPA asta.

## PASI

1. Verifica ca `.git/index.lock` NU exista. Daca exista si e gol/vechi, sterge-l. Daca nu se poate sterge, STOP → NEEDS-INPUT.

2. **Commit 1 — editarile rularii v2 (as-built casa):**
   `MANUAL-FAZA-2.html` · `SOURCE-OF-TRUTH.md` · `CASUTA-DIN-COPAC.md` · `tools-fise/gen_casa.py` · `assets/iso/ca-1-panou.svg` · `assets/iso/ca-2-ridicare.svg` · `assets/iso/ca-3-acoperis.svg`
   Mesaj: `casa as-built: 1950/1642/15,6 in manual+SoT+dosar+gen_casa (continut din rularea v2, verificat de audit 11.08)`

3. **Commit 2 — livrabilele noi (untracked):**
   `GHID-SIMPLU-casa.html` + `.pdf` · `PLAN-pereti-lambriu.html` + `.pdf` · `FISA-MONTAJ-contravantuiri.html` + `.pdf` · `tools-fise/gen_cf.py` · `tools-fise/build_fisa.py` · `AUDIT-2026-08-11.md` · `STATUS.md`
   Mesaj: `ghid simplu pereti (canonic v2) + plan pereti v1 + fisa contravantuiri + audit 11.08 + STATUS`

4. **Commit 3 — igiena briefuri:** muta in `_archive/briefs/`:
   `DONE-BRIEF-consolidare-manual-faza2.md` · `FAILED-BRIEF-casa-geometrie-as-built-2026-08-10.md` · `FAILED-BRIEF-casa-as-built-v2-2026-08-11.md` · `FAILED-BRIEF-commit-contravantuiri-2026-08-07.md` · `NEEDS-INPUT-BRIEF-commit-contravantuiri-2026-08-07.md` · `NEEDS-INPUT-hygiene-push-2026-08-06.md`
   Mesaj: `arhivare briefuri procesate`

5. Adauga o linie noua in capul listei din `STATUS.md` (singura editare permisa): data, "commit-only executat, 3 commituri: <hash1> <hash2> <hash3>", urmeaza: Vlad push + brief continut v3. Amendeaz-o la Commit 2 sau fa un commit 4 mic — cum e mai simplu.

## INTERZIS

- Orice editare de continut in orice fisier (exceptia: linia STATUS de la pasul 5).
- Orice regenerare de PDF/SVG.
- `git push` (ramane la Vlad).
- `git checkout` / `git restore` pe orice.

## DONE MEANS

- `git status --short` arata curat (fara M, fara ??; brieful asta cu prefixul lui e singurul untracked permis).
- 3-4 commituri noi pe `main`, hash-urile scrise in STATUS.
- Niciun diff de continut in afara liniei STATUS: `git diff HEAD~3 --stat` (sau ~4) arata exact fisierele listate mai sus, nimic altceva.

## VERIFY

Ruleaza `git status --short` si `git log --oneline -5`, apoi confirma fiecare punct din DONE MEANS. Daca vreun add/mv esueaza pe index.lock, sterge lockul o singura data si reia; daca reapare, STOP → NEEDS-INPUT cu mesajul exact al erorii.
