MODEL: sonnet

# BRIEF — consolidare: MANUAL-FAZA-2 devine sursa unica (2026-08-06)

## GOAL
`MANUAL-FAZA-2.html/.pdf` devine singurul document de Faza 2. Fisierele pe care le inlocuieste se arhiveaza, indexul canonic se actualizeaza, linkurile din site nu raman rupte. Fara push (403 cunoscut — pushul e la Vlad).

## PASI

### 1. Arhiveaza fisierele absorbite
Muta in `_archive/faza2-absorbite/` (creeaza folderul) urmatoarele, cu tot cu perechile lor .pdf unde exista:
- `PLAN-FAZA-2.html`
- `FISA-FAZA-2-casa-gard-scara.html` + `.pdf`
- `FISA-MONTAJ-balustrada.html` + `.pdf`
- `FISA-MONTAJ-scara.html` + `.pdf`
- `SCHEMA-scara.html` + `.pdf`
- `FISA-MONTAJ-casa.html` + `.pdf`
- `FISA-ACHIZITIE-faza-2.html` + `.pdf`
- `FISA-CONTINUARE-podea.html` + `.pdf`

**NU muta** `CASA-plan-constructie.html` — e legat din nav-ul site-ului (`desene.html` si generatorul). In loc de mutare, insereaza in el, imediat dupa `<div class="wrap">`, banner-ul:
```html
<div style="border:2px solid #C2693A;background:#fbeee4;color:#1a1a1a;padding:14px 18px;margin:0 0 18px;border-radius:8px">
<strong>DEPASIT — vezi MANUAL-FAZA-2.</strong> Pagina asta ramane ca istoric al conceptului si al preturilor de iulie 2026.
Adevarul curent pentru constructia casei e in <a href="MANUAL-FAZA-2.html" style="color:#C2693A">MANUAL-FAZA-2</a>.
</div>
```

### 2. Nu sterge nimic din `assets/iso/`
Manualul le referentiaza prin `<img src="assets/iso/...">`. Verifica dupa arhivare ca toate cele 14 SVG-uri (`bal-1..6`, `sc-1..5`, `ca-1..3`) sunt inca la locul lor.

### 3. Actualizeaza `SOURCE-OF-TRUTH.md`
In tabelul „Cine guverneaza ce", inlocuieste randurile pentru podea-faza / casa de sus / faza 2 cu un singur rand:

| Faza 2 completa (podea-final, balustrada, scara, casa) | `MANUAL-FAZA-2.html` / `.pdf` | actual — SURSA UNICA |

Adauga sub tabel linia: „Pentru Faza 2, MANUAL-FAZA-2 bate orice alt fisier. Documentele absorbite sunt in `_archive/faza2-absorbite/`."
Randurile pentru Faza 1 (geometrie, tracker, fise 01-11, review structural) raman neatinse.

### 4. Verifica linkurile
`grep -rn "FISA-MONTAJ\|FISA-ACHIZITIE\|PLAN-FAZA-2\|SCHEMA-scara\|FISA-CONTINUARE" --include=*.html --include=*.md .` (exclus `_archive/`).
Orice link ramas catre un fisier arhivat se rescrie catre `MANUAL-FAZA-2.html`. Raporteaza ce ai schimbat.

### 5. Commit
- Commit 1: `MANUAL-FAZA-2: sursa unica pentru faza 2 + set izometric complet (balustrada, scara, casa)`
  → `MANUAL-FAZA-2.html`, `MANUAL-FAZA-2.pdf`, `assets/iso/*`, `tools-fise/iso2.py`, `tools-fise/gen_balustrada.py`, `tools-fise/gen_scara.py`, `tools-fise/gen_casa.py`
- Commit 2: `consolidare: arhivare fise faza 2 absorbite + SoT actualizat + banner CASA-plan`
  → mutarile, `SOURCE-OF-TRUTH.md`, `CASA-plan-constructie.html`, orice link rescris
- Commit 3: `STATUS: nota consolidare` → o linie in STATUS.md (data, hash-uri, „push la Vlad")

## CONSTRAINTS
- NU edita continutul manualului. NU push. NU comite fisierul RUNNING al acestui brief.
- `NEEDS-INPUT-hygiene-push-2026-08-06.md` ramane in radacina.
- DONE-briefurile ramase in radacina: muta-le in `_archive/briefs/` si include in Commit 2.

## DONE MEANS
- `MANUAL-FAZA-2.pdf` deschis: 21 pagini, toate cele 14 imagini SVG se vad (nu casete goale).
- Radacina nu mai contine niciunul din cele 8 fisiere absorbite.
- `CASA-plan-constructie.html` are bannerul si e inca in radacina.
- `grep` nu mai gaseste linkuri catre fisiere arhivate in afara `_archive/`.
- `git status` curat, cu exceptiile permise.

## VERIFY
Deschide PDF-ul si confirma ca imaginile se randeaza; ruleaza grep-ul de la pasul 4 si arata rezultatul; `git show --stat` pe fiecare commit. Confirma fiecare DONE MEANS punct cu punct inainte de a raporta done.

## IF STUCK
- Daca o imagine SVG nu se randeaza in PDF: NU modifica manualul — raporteaza care si opreste-te.
- Daca un fisier absorbit e referentiat din generatorul de site (`emit2.py`/`idx2.py`): nu-l muta, pune-i banner ca la CASA-plan si noteaza.
