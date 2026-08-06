# NEEDS-INPUT — hygiene-push-2026-08-06

## Problema

`git push origin main` esuat cu 403 — Builder nu are credentiale GitHub configurate.
Acesta e comportamentul cunoscut al contului Builder (toate sesiunile anterioare au notat "contul Builder nu poate push").

## Starea curenta

Commits locale (gata de push):

| Hash | Mesaj |
|------|-------|
| b2aed2d | podea as-built + audit 08-06 + fisa faza 2: livrabile, poze, decizii |
| e05a360 | igiena: arhivare briefuri procesate (DONE 07-23, FAILED 07-24 v1+v2) |

Plus commit-urile anterioare nelivrate:
| 9ecb06a | audit-fixes v2: regenerare fise + PDF-uri + randari pasi (as-built) |
| 983b346 | audit-fixes v2: cote as-built + talpic + bannere audituri + tracker (surse text) |

Total 4 commit-uri in fata lui origin/main.

## Ce trebuie facut de Vlad

Din contul principal (Main):
```
cd "/Users/Shared/Builds/CASUTA DIN COPAC"
git push origin main
```

## Fisiere necomise — actiune Vlad necesara

Dupa executia celor 3 commit-uri, `git status` arata fisiere modificate/noi (au aparut in timp ce brieful rula — probabil un alt proces pe contul Main):

**Necomise (modificate, in afara brief-ului):**
- `CASA-plan-constructie.html` — modificat (nu era in lista brief-ului ca modified)
- `SOURCE-OF-TRUTH.md` — modificat (in afara scopului brief-ului)

**Necomis (nou, in lista brief-ului dar aparut dupa Commit 1):**
- `FISA-FAZA-2-casa-gard-scara.html` — a aparut pe disc dupa ce Commit 1 fusese deja facut
- `FISA-FAZA-2-casa-gard-scara.pdf` — inca absent de pe disc

Acestea au fost lasate intentionat necomise conform instructiunii din brief ("daca apar fisiere neasteptate fata de lista, lasa-le necomise si noteaza-le"). Vlad sa decida: commit suplimentar sau las-le pentru urmatoarea sesiune.
