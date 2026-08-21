MODEL: sonnet
EFFORT: high

# BRIEF — scoate din nou E0 si E1, scoate gate-ul mort

## DE CE

Lotul 1 din `BRIEF-ghid-fix-audit-2026-08-21` (commit `c7ba0f7`) a restaurat capitolele E0 „Scandura care lipseste" si E1 „Restantele podelei si cioata" si a repus gate-ul `e0 → e3`. **A fost o instructiune gresita** — pornea dintr-o versiune a auditului care presupunea ca lucrarea nu e facuta. Vlad a confirmat pe 21.08 ca e facuta: blocajele la toate cele 4 colturi din spate sunt montate, podeaua e inchisa integral, cioata e retezata. Brief-ul asta anuleaza lotul 1.

Lotul 2 al aceluiasi brief (commit `40026f7`, cifrele de material) e **corect si ramane** — nu-l da inapoi. Loturile 3–5 de acolo n-au mai apucat sa ruleze; le ia un brief separat, dupa asta. Nu le face aici.

**Comiti dupa fiecare lot. Trei loturi, trei commituri.**

## LOT 1 — sase capitole, fara gate

In `build_ghid.py` (si `gen_ghid.py` daca e nevoie):

1. Sterge capitolele E0 („Scandura care lipseste") si E1 („Restantele podelei si cioata"). Ghidul incepe cu drumul la Leroy.
2. Renumeroteaza: **E1 Leroy · E2 perete spate · E3 pereti laterali · E4 perete fata · E5 acoperis · E6 geamuri si verificare finala.** Actualizeaza si meniul lateral, si selectorul de pe telefon.
3. **Scoate gate-ul complet**, nu-l muta: elementul `.gatebar`, butonul de „sar peste", `.skipwarn`, stilurile `.locked` / `.gatebar` / `.gb-skip` / `.skipwarn` din CSS si ramura de JS care le foloseste. Nu lasa cod care cauta un element inexistent.
4. Corecteaza referintele interne la numerotarea noua: „se monteaza la E7" → „la E6"; „tocul pregatit la E4" → „la E3". Cauta si orice alta trimitere „la E<cifra>" si verifica fiecare.
5. In checklistul final, randul despre blocajele de colt ramane bifabil si spune ca lucrarea e facuta, fara sa trimita la un capitol care nu mai exista.
6. Ruleaza `python3 gen_ghid.py && python3 build_ghid.py`. **Commit.**

## LOT 2 — documentele care descriu munca terminata

1. `GHID-E0-golul-din-spate.html` si `MASOARA-GOL.html`: adauga sus o bara vizibila, in stilul barei „DEPASIT" folosite pe celelalte documente, cu textul: **„ISTORIC — blocajele de la colturile din spate sunt montate (21.08.2026). Documentul ramane pentru referinta."** Nu sterge fisierele.
2. `SOURCE-OF-TRUTH.md`, in „Goluri deschise": randul despre golul de podea la colturile din spate si randul despre pozele de la colturi trec la **INCHIS 21.08**. Randul de balustrada ramane deschis, neatins.
3. **Commit.**

## LOT 3 — STATUS si igiena

O linie in `STATUS.md`: ce s-a scos si de ce; ca lotul 2 din brief-ul precedent (`40026f7`) ramane in picioare; si ca **loturile 3–5 de acolo raman restanta** — alinierea `LISTA-LEROY` la inventarul din 21.08, legaturile material–etapa, si igiena. Daca au ramas briefuri FAILED sau NEEDS-INPUT in radacina, muta-le in `_archive/briefs/`. **Commit.**

## DONE MEANS

- `grep -c 'section id="e0"' GHID-CONSTRUCTIE-casa.html` → 0; sectiunile sunt e1–e6.
- `grep -c 'gatebar\|gb-skip\|skipwarn' GHID-CONSTRUCTIE-casa.html` → 0, inclusiv in CSS si in JS.
- Nicio trimitere „la E7" in ghid; trimiterea la toc arata catre E3.
- GHID-E0 si MASOARA-GOL poarta bara ISTORIC.
- SOURCE-OF-TRUTH: cele doua randuri de colturi marcate INCHIS 21.08; balustrada inca deschisa.
- Corectiile din commitul `40026f7` sunt intacte: rigla 13, scandura 7, randurile 6×100 si silicon in tabelul de cumparaturi, vinclu 90×65.

## VERIFY

Deschide ghidul in Chromium headless la desktop si la 390 px: zero scroll orizontal, consola curata, toate bifele active de la incarcare (nimic blocat). Bifezi cateva, dai refresh, bifele raman. Ruleaza pasul de voce din `/Users/Shared/Builds/VOICE.md` sectiunea 3 peste textele si microcopy-ul modificat. Apoi confirma fiecare item din DONE MEANS, unul cate unul.

## IF STUCK

Daca stergerea gate-ului strica persistenta bifelor, pastreaza cheile de localStorage exact cum sunt si scoate doar blocarea — bifele nu trebuie sa se piarda. Daca un lock `.git` blocheaza commitul, scrie NEEDS-INPUT si opreste-te; nu forta.
