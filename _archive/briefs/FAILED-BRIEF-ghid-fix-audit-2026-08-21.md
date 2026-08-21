MODEL: opus
EFFORT: high

# BRIEF — repara ghidul dupa auditul din 21.08

## REGULA CARE BATE TOT RESTUL

**Comiti dupa fiecare lot. Cinci loturi, cinci commituri.** Rularile mari anterioare au facut treaba corect si au murit inainte sa salveze. Daca ramai fara aer dupa doua loturi, doua loturi comise sunt un rezultat. Nu aduna munca pentru un commit final.

## CONTEXT

Fisierele `GHID-CONSTRUCTIE-casa.html`, `build_ghid.py`, `gen_ghid.py` au modificari NECOMISE fata de HEAD (`a28e565`): o rescriere care a redus ghidul de la 8 capitole (e0–e7) la 6 (e1–e6). Rescrierea a adaugat desene bune (ridicarea, prinderea in stalp, reazemul, sectiunile de colt la laterale) dar a sters capitolele E0 „Scandura care lipseste" si E1 „Restantele podelei si cioata", a scos elementul `.gatebar` (scriptul il cauta si nu-l gaseste — gate mort) si a introdus afirmatia falsa ca blocajele de colt sunt montate. Decizie Vlad 21.08: se pastreaza desenele noi, se restaureaza capitolele, gate-ul si numerotarea E0–E7.

Sursa pentru ce s-a sters: `git show HEAD:build_ghid.py` si `git show HEAD:GHID-CONSTRUCTIE-casa.html`. NU face checkout peste fisierele curente — pierzi desenele noi. Constatarile complete: `AUDIT-2026-08-21.md`.

## LOT 1 — restaurare capitole + gate + numerotare

1. In `build_ghid.py` curent, readauga din HEAD capitolele E0 („Scandura care lipseste") si E1 („Restantele podelei si cioata"), inaintea Leroy-ului. Renumeroteaza inapoi: E0 gol, E1 restante, E2 Leroy, E3 spate, E4 laterali, E5 fata, E6 acoperis, E7 geamuri — numerotarea din STATUS si din brief-urile existente.
2. Restaureaza elementul `.gatebar` cu `data-gate="e0"` pe sectiunea E3 (spate), cu butonul de „sar peste" si `.skipwarn`, exact ca in HEAD. Comportament: cu localStorage gol, E3 e blocat; bifezi tot E0, E3 se deblocheaza.
3. Sterge afirmatiile false: „blocajele deja montate" (pas E3) devine „talpa se prinde in blocajele facute la E0"; itemul din checklistul final „toate 4, deja montate" devine „toate 4, facute la E0" — bifabil, nu afirmatie.
4. In capitolul E0, pastreaza/readauga linkul catre `GHID-E0-golul-din-spate.html`.
5. Ruleaza `python3 gen_ghid.py && python3 build_ghid.py`. Verifica: 8 sectiuni e0–e7, cele 3 desene noi tot in ghid, referintele „la E7" (geamuri) si „la E4" (toc, laterale) acum rezolva corect. **Commit.**

## LOT 2 — materiale in ghid

Toate in generatoare, nu in HTML direct.

1. `6×120` → `6×100` peste tot in pasi (proptele/contrafise). Motiv, de pus in nota: coltul 48+48 are 96 mm; 120 iese 24 mm.
2. In tabelul „Tot ce cumperi" (capitolul Leroy) adauga randul: `Surub dulgherie 6×100 | ~60 | contrafisele si proptelele; ai 20 Heco 6×100 in stoc`.
3. Rigla 48×48: `14` → `13` (LISTA-LEROY e canon: 12,1 nevoie + 1 pierderi). Corecteaza si nota „a 13-a acopera pierderile, a 14-a e rezerva".
4. Scandura 22×100: `8` → `7`, cu planul de taiere in nota: un caprior = 2 straturi de 1889; o bara da 2 straturi; 5 bare → 5 capriori; a 6-a → 4 inchideri de 454; a 7-a rezerva. Corecteaza textul „(3 bare)" din capitolul acoperisului la „(5 bare, 2 straturi pe caprior)".
5. Adauga in tabelul Leroy: `Silicon de exterior | 2 tuburi` (cerut la geamuri, lipsea din drum).
6. Nota lambriu spate: „2 pe fiecare intersectie" → „un surub pe fiecare intersectie" (asa da 110 si asa zice pasul).
7. „vinclu 100×90" → „vinclu 90×65".
8. Preturile „de verificat" (rigla 46×46, sipca 18×28): ia-le din `LISTA-LEROY-2026-08-17.html` (sipca 8,29 lei/3 m, verificat 06.08).
9. Verifica aritmetic: fiecare rand din tabelul Leroy ≥ suma cardurilor de etapa pentru articolul respectiv, inclusiv E0. Ruleaza build-ul. **Commit.**

## LOT 3 — LISTA-LEROY aliniata la inventarul din 21.08

In `LISTA-LEROY-2026-08-17.html` (+ PDF daca se regenereaza usor): randul `6×120` devine `6×100` (acelasi motiv, cost egal); randul Sadolin Extra 2,5 L iese (2 L ulei de tec in stoc; −150 lei); totalul recalculat, in jur de 3.490 lei; nota scurta „aliniat la receptia din 21.08 — INVENTAR-2026-08-21". **Commit.**

## LOT 4 — legaturi material ↔ etapa ↔ desen

1. Cardurile „Materiale pentru etapa asta" primesc id-uri (`mat-e0` … `mat-e7`).
2. Fiecare rand din tabelul Leroy primeste, in coloana „De ce atat", linkuri catre capitolele care consuma articolul: `→ E3 · E4 · E5`.
3. Fiecare card de etapa primeste sus un link „toate cumparaturile → E2".
4. Pasii care au desen la scara in `SCHEME-2D-casa.html` primesc link la ancora figurii respective.
5. Gate-ul de pe E3 primeste link catre `GHID-E0-golul-din-spate.html`. **Commit.**

## LOT 5 — igiena

Muta `FAILED-BRIEF-e5-desene.md`, `FAILED-BRIEF-e5-desene-v2.md`, `NEEDS-INPUT-BRIEF-e5-desene.md`, `NEEDS-INPUT-BRIEF-e5-desene-v2.md` in `_archive/briefs/`. Comite si `AUDIT-2026-08-21.md`. O linie in STATUS.md. **Commit.**

## DONE MEANS

- Ghidul are 8 sectiuni e0–e7; la localStorage gol E3 e blocat; bifand tot E0 se deblocheaza; bifele supravietuiesc refresh-ului.
- `grep -c "6×120" GHID-CONSTRUCTIE-casa.html LISTA-LEROY-2026-08-17.html` → 0 si 0; `grep -c "deja montate" GHID-CONSTRUCTIE-casa.html` → 0.
- Tabelul Leroy contine randurile 6×100 si silicon; rigla 13; scandura 7.
- Fiecare rand din tabelul Leroy are cel putin un link de capitol; fiecare card de etapa are linkul inapoi.
- Cele 3 desene noi (ridicare, prindere stalp, reazem) si cele 5 lat_* sunt in continuare in ghid.
- 5 commituri in git log (sau cate loturi s-au terminat), plus linia din STATUS.

## VERIFY

Deschide ghidul in Chromium headless la desktop si la 390 px: zero scroll orizontal, consola curata, gate-ul functioneaza cum e descris. Ruleaza pasul de voce din `/Users/Shared/Builds/VOICE.md` sectiunea 3 peste textele si microcopy-ul modificat. Apoi confirma fiecare item din DONE MEANS, unul cate unul, inainte sa scrii DONE.

## IF STUCK

Daca gate-ul din HEAD nu se lasa altoit pe structura rescrisa, ia structura de sectiuni din HEAD ca baza si muta desenele noi in ea (figurile stau in `gen_ghid.py`, montajul in `build_ghid.py`) — rezultatul conteaza, nu directia merge-ului. Daca un lock `.git` blocheaza commitul, scrie NEEDS-INPUT si opreste-te; nu forta.
