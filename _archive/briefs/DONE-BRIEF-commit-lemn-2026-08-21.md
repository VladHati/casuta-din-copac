MODEL: sonnet
EFFORT: medium

# BRIEF — comite ziua de 21.08: materiale, protectie, feronerie

## DE CE

Sesiunea Cowork din 21.08 a reconstruit lista de materiale a casei si a propagat totul prin generatoare. Fisierele sunt pe disc, verificate si **reproductibile byte-cu-byte din generatoare**, dar necomise. Commitul nu se poate face din Cowork: git rulat de pe mount-ul partajat lasa in urma `.git/index.lock` pe care nu-l poate sterge, iar lock-ul ramas blocheaza commitul urmator.

**Comiti dupa fiecare lot. Trei loturi, trei commituri.** Pushul e al lui Vlad — nu incerca, primesti 403.

## CE S-A SCHIMBAT

**Rama: rigla 48x48x4000 -> 46x46x3000.** 48x48 are stoc zero la Leroy Colosseum si nu se livreaza. Sectiunea scade cu 2 mm (88% din rezistenta la incovoiere, marja ramane peste 2x). `T` trece de la 48 la 46 in ambele generatoare; verticalele se recalculeaza singure — spate 1608, fata 1554, laterale 1577 / 1649 / 1726 / 1798. Verticalele laterale nu mai sunt cote verbatim: ies din lumina masurata `VL_CLEAR = [1669, 1741, 1818, 1890]` minus `2*T`. Materialele `r48` si `r46` s-au contopit in cheia `ram`. Suruburile de colt devin **6x80** — coltul are 92 mm.

**Lambriu: 12,5x96x3000 -> 19x116x4000.** La 12,5 mm scandura se cupeaza si crapa in jurul surubului pe un perete de exterior. Larice nu exista la Leroy, deci grosimea era singura parghie. Din 4 m ies doua randuri de 1990: 29 de scanduri in loc de 56. Consecinte propagate: suruburi **inox 4x50** in loc de 4x40, si panoul din spate creste la **~42-51 kg** la ridicare.

**Protectie: lazura pigmentata in loc de ulei de tec.** Randul de vopsea statea pe zero, cu motivul ca cei 2 L de ulei din inventar acopera casa. Suprafata reala de tratat e **48,4 m2**; cu doua straturi, **97 m2**. Doi litri fac ~20%, si uleiul n-are pigment, deci nu opreste UV-ul. Se cumpara 2 galeti de lazura Luxens de 5 L. Ordinea de vopsire e scrisa acum la E2, E3 si E4: rama intai, apoi scandurile pe toate cele sase suprafete, apoi montajul, apoi al doilea strat.

**Feronerie: zero vincluri de cumparat.** Inventarul lui Vlad (32x Parkside 40x40, 10x 70x55, 6x 90x60, 4x 90x100) acopera integral nevoia de 48. Criteriul de alocare e latimea: un vinclu nu poate fi mai lat decat lemnul pe care sta — de aceea cele de 90 nu merg pe rigla de 46, si cele de 40 da. Randurile de 90x65 (56 buc) si 100x90 (8 buc) au iesit; al doilea nu era cerut nicaieri in ghid.

**Auditul final** a mai gasit: Onduline trece pe maro (mai ieftin, stoc mai bun) - surub 8x140 de la 36 la 16, fiindca cele 20 pentru blocajele de colt sunt facute - surub 6x140 de la 45 la 24 - suruburile de 4x50 unificate intr-un singur rand de ~380 - sipca 3 bare in loc de 6 m si in cardul de la E6 - vincluri mutate din coloana Cumperi in Ai deja.

`gen_ghid.py` exporta acum `cote.json`, iar `build_ghid.py` scrie bonurile de taiere din el. Nicio cota din ghid nu mai e sir literal.

## LOT 1 — codul si documentele de executie

Comite, fara sa modifici nimic:

- `gen_ghid.py`, `gen_2d.py`, `build_ghid.py`, `build_2d.py`
- `GHID-CONSTRUCTIE-casa.html`, `SCHEME-2D-casa.html`
- `LISTA-LEROY-2026-08-17.html`
- `MATERIALE-casuta-2026-08-21.xlsx` — tabelul de materiale cu linkuri, generat pe 21.08

Adauga si `cote.json` daca nu e prins de `.gitignore`. Daca `figs_ghid.json` / `figs_2d.json` / `mats.json` sunt ignorate, lasa-le — se regenereaza.

Inainte de commit ruleaza `python3 gen_ghid.py && python3 gen_2d.py && python3 build_ghid.py && python3 build_2d.py`, apoi `git status`. **Cele doua HTML-uri trebuie sa ramana neschimbate dupa regenerare** — asta s-a verificat pe 21.08. Daca apar diferente, sau daca `gen_2d` nu raporteaza **0 nepotriviri**, **scrie NEEDS-INPUT si opreste-te**.

Mesaj de commit: o linie de titlu plus corpul cu motivele de mai sus. **Commit.**

## LOT 2 — auditul si brief-urile terminate

- `AUDIT-2026-08-21.md` — necomis, e sursa constatarilor.
- `DONE-BRIEF-ghid-fix-v2-2026-08-21.md` — muta-l in `_archive/briefs/`, apoi comite-l de acolo.
- Cele patru fisiere `FAILED-*` / `NEEDS-INPUT-*` care apar ca sterse in `git status` sunt deja arhivate; inregistreaza stergerile.

**Commit.**

## LOT 3 — STATUS si igiena

Cateva linii in `STATUS.md`: rama pe 46x46 cu motivul de stoc - lambriul pe 19x116 cu motivul de grosime - lazura in locul uleiului de tec - vincluri zero, acoperite din inventar - cosul Leroy Colosseum inchis la **2.525,65 lei pe 9 produse**, plus ~554 lei de luat de la raft, total drum ~3.080 lei.

In radacina exista `_to_delete/` cu doua fisiere pe care sesiunea Cowork nu le-a putut sterge (`_probe.lock`, `index.lock.*`). **Sterge folderul** — tu ai drepturi, puntea nu are. Verifica intai ca `.git/` nu are niciun `*.lock` ramas.

Cele ~20 de poze HEIC din `POZE/` raman netrackuite. **Nu le comite** fara sa intrebi.

**Commit.**

## DONE MEANS

- `git status --short` nu mai arata `M` sau `D` pe fisierele de la LOT 1 si LOT 2.
- `git log --oneline -3` arata cele trei commituri noi.
- Regenerarea nu schimba niciun HTML (verifica cu `md5sum` inainte si dupa).
- In `GHID-CONSTRUCTIE-casa.html`: `48x48` -> **1** (singura aparitie e explicatia de ce nu 48x48), `12,5x96` -> **0**, `6x100` -> **0**, `90x65` -> **0**, `section id="e0"` -> **0**. Foloseste caracterul x multiplicat din fisier, nu litera x.
- `cote.json` contine `"T": 46` si `"VB": 1608`.
- `.git/` nu contine niciun `*.lock`; `_to_delete/` nu mai exista.
- Commiturile nu sunt pushed.

## VERIFY

Deschide ghidul in Chromium headless la desktop si la 390 px: zero scroll orizontal, consola curata, sase capitole, 23 de desene, zero ancore moarte, toate bifele active de la incarcare. Bifezi cateva, dai refresh, bifele raman. Acelasi test pe `LISTA-LEROY-2026-08-17.html` — a avut un scroll orizontal la 390 px, reparat pe 21.08; verifica sa nu fi revenit. Apoi confirma fiecare item din DONE MEANS, unul cate unul.

## IF STUCK

Daca un `.git/*.lock` blocheaza commitul, sterge-l — rulezi local, ai voie. Daca build-ul nu reproduce fisierele de pe disc, **fisierele de pe disc sunt canonice** si generatoarele au o abatere: scrie NEEDS-INPUT cu diferenta si opreste-te. Nu rescrie fisierele HTML de mana.
