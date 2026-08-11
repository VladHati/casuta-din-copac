MODEL: opus
EFFORT: xhigh

# BRIEF — Casa de sus: aliniere la as-built (v2, inlocuieste brieful din 10.08)

## PAS 0 — OBLIGATORIU INAINTE DE ORICE

Rularea `FAILED-BRIEF-casa-geometrie-as-built-2026-08-10.md` a lasat in working tree editari **necomise** cu cifre care intre timp au fost **abandonate** (grinda 45×140, reazem spate 1840, panta 12,3°, caprior 1426, stalpi 70×70 retezati la 1558). Acele cifre sunt GRESITE acum.

```
git checkout -- MANUAL-FAZA-2.html tools-fise/gen_casa.py assets/iso/ca-1-panou.svg assets/iso/ca-2-ridicare.svg assets/iso/ca-3-acoperis.svg
```

Verifica dupa: `git status --short` nu mai arata `M` pe niciunul dintre cele 5. Abia apoi treci mai departe. Daca `git checkout` esueaza, opreste-te si scrie NEEDS-INPUT — nu incerca sa repari manual peste editarile vechi.

## GOAL

Aliniaza documentele canonice la geometria masurata pe santier si la deciziile luate de Vlad in 11.08. Cand termini, cut list-ul casei din MANUAL-FAZA-2 se poate debita direct, iar nicaieri in radacina proiectului nu mai exista cote estimate pentru casa de sus.

## CONTENT — cifrele finale

### Ce exista fizic pe santier (masurat de Vlad)

| Element | Stare | Cota |
|---|---|---|
| Stalpii din spate | cei 4 originali de 4 m, intregi, in ancore | **1700** peste dusumea |
| Stalpii din fata ai casei | **90×90**, deja montati, prinsi cu coltare in L **direct in grinda** (nu in scandurile podelei) + suporti laterali | **1600** peste dusumea |
| Tijele M12 din podea | montate inainte de dusumea, **nefolosite**, la sub 100 mm de stalpi | ies ~100 |
| Dulapi 46×250×3000 | **3 buc deja cumparate** (scara amanata); 1 se foloseste la casa | — |

### Geometria finala

| Marime | Valoare | Din ce rezulta |
|---|---|---|
| Reazem SPATE | **1950** | perete spate 1700 + dulap 46×250 pe muchie deasupra |
| Reazem FATA | **1642** | stalp 1600 + cununa 42 deasupra |
| Cadere pe A = 1100 | **308** | 1950 − 1642 |
| Panta acoperis | **308 / 1100 = 15,6°** | peste minimul de 10° al Onduline pe sipci |
| Inaltime libera la usa | **1600** | 1642 − 42, cu talpa taiata din dreptul usii dupa asamblare |
| Caprior (streasina 200 fata + 100 spate) | **1442** | √(1100² + 308²) + 300 |

**Stalpii din fata NU se taie si NU se cumpara.** Raman 1600, cum sunt montati.

### Dulapul din spate

`46×250` (nominal ~50 grosime), **taiat la 2200**, asezat **pe muchie** (250 in sus) peste capul stalpilor de 4 m SI peste cununa peretelui din spate — ambele sunt la 1700, deci reazemul e continuu pe toata lungimea, nu doar in doua puncte.

Fixare: **vinclu 90×90 pe ambele fete la fiecare ~500**, prins in dulap si in cununa; in plus **o placa metalica de imbinare pe fiecare fata, peste fiecare stalp de 4 m**. Se monteaza dupa ce peretele din spate e ridicat si in echer. Pana nu are capriori pe el, se propteste — 250 pe 46 se rastoarna lateral.

### Ancorajul stalpilor din fata

Coltarele in L prinse in grinda sunt bune la forfecare. Pentru smulgere se recupereaza tijele M12 existente: **coltar 100×100 cu o gaura Ø13 data in talpa lui**, pus peste tija, **saiba lata + piulita**, bratul vertical prins in stalp cu **4× surub 6×60** pregaurit Ø5. **Cate unul pe stalp, 2 in total.**

### Cut list nou (inlocuieste integral tabelul din §8)

| Piesa | Sectiune | Lungime | Buc |
|---|---|---|---|
| Talpa + cununa spate / fata | 42×90 | L (2000) | 2 + 2 |
| Talpa + cununa laterale | 42×90 | A − 90 (1010) | 4 |
| **Dulap reazem spate** | **46×250** | **2200, pe muchie** | **1** (deja cumparat) |
| Montanti spate | 45×45 | **1616** | 5 |
| Montanti fata (cu dublurile de la goluri) | 45×45 | **1558** | 7 |
| Montanti laterali (in trepte pe panta) | 45×45 | **1558 / 1712 / 1866** | 6 |
| Buiandrug fereastra fata · praguri + buiandrugi geamuri laterale | 42×90 | 660 · 490×4 | 5 |
| Capriori | 42×90 | **1442** | 5 |
| Sipci acoperis | 45×45 | L + 200 (2200) | 4 |
| Stalpi fata | 90×90 | **deja montati la 1600 — nu se cumpara, nu se taie** | 2 |

Formule: montanti spate = M1 − 84 · montanti fata = 1642 − 84 · caprior = √(A² + 308²) + 300.

**Golul de usa nu mai are buiandrug propriu** — capul golului este cununa peretelui din fata, iar talpa se taie din dreptul usii dupa ce panoul e asamblat, drept si prins in colturi. Asta e ce da inaltimea libera de 1600. Scrie explicit in Pasul 1 ca taierea talpii se face **ultima**, nu la asamblare.

### Sistemul de perete — nu mai e OSB

Peretii nu mai sunt cutie-panou cu OSB. Varianta noua (lambriu orizontal pe sipci de ventilare, rigidizare cu diagonale de lemn, doua geamuri laterale fixe facute in casa) este complet detaliata in **`PLAN-pereti-lambriu.html` / `.pdf`**, care exista deja pe disc si trebuie comis in acest brief.

In MANUAL-FAZA-2 nu rescrie sistemul de perete. Fa doua lucruri:

1. In §8, unde apare OSB-ul ca element structural al peretilor, inlocuieste cu o **nota de trimitere**: sistemul de perete e in `PLAN-pereti-lambriu.html`, OSB-ul e eliminat, rigidizarea se face cu diagonale.
2. Scoate randul de OSB din cut list si din lista de cumparaturi.

### Cumparaturi — modificari

- **SCOATE** din Drum 2: `Stalp 70×70×3000, taiat 2× · 1 buc · ~90 lei` (stalpii exista, sunt 90×90).
- **SCOATE** din Drum 2: `LEROY OSB3 12 mm 2500×1250 · 4 buc · 79,33` (~317 lei).
- **ADAUGA** o linie de trimitere: pozitiile pentru pereti (lambriu, sipci, folie, scandura de diagonale, acrilic) sunt in `PLAN-pereti-lambriu`, delta **+883 lei**.
- **ADAUGA** in feronerie casa: `Coltar 100×100 cu gaura Ø13 peste tija M12 · 2 · ancoraj stalpi fata`; `Vinclu 90×90` creste cu ~10 buc (fixarea dulapului); `Placa metalica de imbinare · 4 · dulap → stalpii de 4 m`.

## CONSTRAINTS

- Romana fara diacritice.
- `MANUAL-FAZA-2.html` = sursa unica pentru Faza 2. Editezi acolo, apoi regenerezi PDF-ul.
- NU atinge §F2 (balustrada) si §F3 (scara). Vlad a amanat scara — vezi sectiunea Deschise.
- NU atinge `_archive/`.
- Editari punctuale, nu rescrieri de sectiuni intregi.

## FISIERE DE MODIFICAT

1. **`MANUAL-FAZA-2.html`**
   - §2 tabel decizii, randul `Perete casa spate / fata | M1 / M1 − 300 | ... (~1772)` → `1700 (+250 dulap) / 1642 | masurat 11.08; stalpii fata sunt deja montati la 1600, 90×90`.
   - §2 randul `Panta acoperis | 300 / 1100 = 15,3°` → `308 / 1100 = 15,6°`.
   - §8 tabelul M1–M5: M1 nominal `~1772` → `1700 (masurat)`, coloana Real completata `1700`. M2, M3, M4, M5 raman de masurat.
   - §8 blocul STOP: scoate conditia `M1 e sub 1700`. Pune in loc: `dulapul de reazem are sub 250 inaltime — panta scade sub 13° si marja la Onduline se pierde`. Celelalte 3 conditii raman.
   - §8 cut list: inlocuit integral cu tabelul de mai sus.
   - §8 nota `Simplificare optionala ... cadru separat de 300 mm`: sterge — dulapul de 250 face acum acest lucru.
   - §F4 Pasul 2, punctul `Stalpii 70×70`: rescrie — stalpii sunt **90×90, deja montati**, prinsi cu coltare in L in grinda; pasul devine verificare (vertical pe doua fete, fara joc) **plus montarea celor 2 coltare cu gaura Ø13 peste tijele M12**.
   - §F4 Pasul 3: adauga taierea talpii din dreptul usii, ca ultima operatie pe peretele din fata.
   - §F4 Pasul 4: adauga montarea dulapului de 250 inainte de capriori, cu vincluri + placi metalice + avertismentul de rasturnare. `taiati oblic la 15,3°` → `15,6°`.
   - §Feronerie casa: modificarile de mai sus.
   - §9 Cumparaturi: modificarile de mai sus.
   - §11 Deschise: M1 marcat FACUT (1700, masurat 11.08); adauga rand `Scara — varianta simpla si usoara, decizie amanata de Vlad; pana exista acces sigur, copiii nu urca`.
   - §12 Istoricul corectiilor, 4 randuri noi:
     - `Casa: M1 = 1700 masurat, nu ~1772 estimat` / `masuratoare pe teren 10.08`.
     - `Casa: stalpii fata sunt 90×90 la 1600, deja montati cu coltare in L in grinda` / `montati de Vlad inainte ca planul sa fie finalizat; nu se taie si nu se cumpara.`
     - `Casa: reazem spate = dulap 46×250 pe muchie, nu grinda de 140` / `140 dadea panta de 10,2°, exact pe pragul Onduline; 250 duce spatele la 1950 si panta la 15,6°, iar dulapul era deja cumparat pentru scara.`
     - `Casa: usa fara buiandrug, talpa taiata din dreptul ei` / `cerinta Vlad: un copil de 1,60 sa intre fara sa se aplece. Cu buiandrug, golul ar fi iesit 1516.`

2. **`tools-fise/gen_casa.py`** — `A = 1100` ramane; `H = 1772` → `H = 1950`; `HF = H - 300` → `HF = 1642`. Eticheta de cota `"300 = panta pe 1100 → 15,3°"` → `"308 = panta pe 1100 → 15,6°"`. Regenereaza SVG-urile in `assets/iso/`.

3. **`SOURCE-OF-TRUTH.md`** — linia `- Perete casa de sus: 1800 spate / 1500 fata (inlocuieste vechiul 1300).` → `- Casa de sus (as-built 11.08): perete spate 1700 + dulap 46×250 pe muchie = reazem 1950; perete fata 1642 (stalpi 90×90 deja montati la 1600, nu se taie). Panta 308/1100 = 15,6°. Usa 1600 liber. Peretii: lambriu fara OSB — vezi PLAN-pereti-lambriu.html.` Adauga si un rand in tabelul "Cine guverneaza ce": `Pereti casa de sus (lambriu, rigidizare, geamuri laterale) | PLAN-pereti-lambriu.html | actual`.

4. **`CASUTA-DIN-COPAC.md`** — randul `| Perete casa de sus | 1800 mm spate / 1500 mm fata |` si paragraful din §"Casa de sus" (`pereti 1800 (spate) -> 1500 (fata)`) → cifrele noi. Sterge `Ramase de ales: invelitoarea (Onduline vs policarbonat) si usa vs gol` (ambele decise). Trimiterea catre `CASA-plan-constructie.html` → `MANUAL-FAZA-2.html`.

5. **`PLAN-pereti-lambriu.html` + `.pdf`** — exista pe disc, se comit ca atare. **Nu le edita.**

6. **`MANUAL-FAZA-2.pdf`** — regenerat din HTML.

7. **`STATUS.md`** — o linie noua in capul fisierului, formatul obisnuit.

8. **Igiena:** muta `FAILED-BRIEF-casa-geometrie-as-built-2026-08-10.md` in `_archive/briefs/`.

## DONE MEANS

- `git status --short` la finalul PAS 0 nu arata modificari reziduale din brieful din 10.08.
- `grep -n "1772\|15,3°\|M1 − 300\|1840\|12,3°\|1426\|45×140\|1800 spate\|1500 fata"` in radacina (fara `_archive/`) intoarce rezultate **doar** in §12 Istoricul corectiilor din MANUAL-FAZA-2 si in coloana "IN MANUAL" din tabelul de comparatie al `PLAN-pereti-lambriu.html`. Oriunde altundeva = bug.
- `MANUAL-FAZA-2.html` contine `1950`, `1642`, `15,6°`, `1442`, `1616`, `1558`, `1866`, `46×250`, `90×90`.
- `MANUAL-FAZA-2.pdf` regenerat, se deschide, cut list-ul din §8 nu e taiat intre pagini.
- SVG-urile casei regenerate, fara text suprapus.
- `PLAN-pereti-lambriu.html` si `.pdf` sunt in repo.
- `STATUS.md` are linia noua; brieful vechi e in `_archive/briefs/`.
- Comis pe `main`. **Push-ul NU se face de aici** — ramane la Vlad.

## VERIFY

Deschide rezultatul la latime desktop si la 390px, consola curata, apoi confirma fiecare punct din DONE MEANS individual inainte de a raporta done. In plus:

1. Ruleaza tu aritmetica: `1950 − 1642 = 308`; `atan(308/1100) = 15,64°`; `√(1100² + 308²) = 1142`; `1142 + 200 + 100 = 1442`; `1642 − 42 = 1600`; `1700 − 84 = 1616`; `1642 − 84 = 1558`; `1950 − 84 = 1866`. Orice cifra din manual care nu se potriveste e gresita — repar-o.
2. Randeaza PDF-ul si **uita-te** la paginile casei: cut list intreg pe o pagina, desene fara text suprapus, `GATA CAND`-urile fara orfani.
3. Verifica coerenta intre MANUAL-FAZA-2 si PLAN-pereti-lambriu pe cele 6 cifre cheie: 1950, 1642, 308, 15,6°, 1442, 1600. Trebuie sa fie identice in ambele.

## IF STUCK

- **Daca `git checkout` din PAS 0 nu merge** (index.lock, conflicte): sterge `.git/index.lock` daca e gol si vechi, reincearca o data. Daca tot pica: **opreste-te**, scrie NEEDS-INPUT si NU edita niciun fisier. Un brief aplicat peste editari vechi produce un amestec de cifre — cel mai prost rezultat posibil.
- **Daca `gen_casa.py` nu ruleaza** (dependinte lipsa): recreeaza env-ul (micromamba: weasyprint + pypdf + numpy + pillow). Daca tot pica, comite editarile de text si de cod, marcheaza SVG-urile ca neregenerate in STATUS, si NU raporta done pe punctul de SVG.
- **Daca gasesti si alte fisiere din radacina cu cote vechi de casa** in afara celor 4 numite: aliniaza-le si listeaza-le in STATUS.
- **Daca brieful contrazice fisierul:** brieful castiga la cifre, fisierul castiga la structura.
