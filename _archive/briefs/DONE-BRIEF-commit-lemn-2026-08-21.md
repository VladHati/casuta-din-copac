MODEL: sonnet
EFFORT: medium

# BRIEF — comite lucrul pe lemn din 21.08

## DE CE

Sesiunea Cowork din 21.08 a schimbat materialul de rama si materialul de lambriu, a propagat cotele prin generatoare si a rescris lista de cumparaturi. Fisierele sunt pe disc si verificate, dar **necomise**. Commitul nu se poate face din Cowork: git rulat de pe mount-ul partajat lasa in urma `.git/index.lock` pe care nu-l poate sterge, si lock-ul ramas blocheaza commitul urmator.

**Comiti dupa fiecare lot. Trei loturi, trei commituri.** Pushul e al lui Vlad, nu al tau — nu incerca, primesti 403.

## CE S-A SCHIMBAT, PE SCURT

**Rama peretilor: rigla 48×48×4000 → 46×46×3000.** Motivul: 48×48 are stoc zero la Leroy Colosseum si nu se livreaza, e produs doar de ridicat din magazin. La 46×46 sectiunea scade cu 2 mm (88% din rezistenta la incovoiere, marja ramane peste 2×) si materialul e pe raft. `T` trece de la 48 la 46 in ambele generatoare; verticalele se recalculeaza singure: spate 1608, fata 1554, laterale 1577 · 1649 · 1726 · 1798. Suruburile de colt devin **6×80** — coltul are 92 mm, unul de 100 ar iesi 8 mm pe partea cealalta.

**Lambriu: 12,5×96×3000 → 19×116×4000.** Motivul: la 12,5 mm scandura se cupeaza si crapa in jurul surubului pe un perete de exterior. Bonus de la lungime — din 4 m ies doua randuri de 1990, deci 29 de scanduri in loc de 56. Consecinte propagate: suruburi **4×50** in loc de 4×40 (~320 in loc de ~450) si panoul din spate creste la **~42-51 kg** la ridicare.

**Materialele `r48` si `r46` s-au contopit** intr-o singura cheie `ram`, fiindca sunt acelasi produs.

**`gen_ghid.py` exporta acum `cote.json`**, iar `build_ghid.py` scrie bonurile de taiere din el. Nicio cota din ghid nu mai e sir literal.

Constatarile complete ale auditului de lemn: vezi `AUDIT-2026-08-21.md` si memoria de proiect.

## LOT 1 — codul si documentele de executie

Comite, fara sa modifici nimic:

- `gen_ghid.py`, `gen_2d.py`, `build_ghid.py`, `build_2d.py`
- `GHID-CONSTRUCTIE-casa.html`, `SCHEME-2D-casa.html`
- `LISTA-LEROY-2026-08-17.html`

Adauga si `cote.json` daca nu e prins de `.gitignore`; daca `figs_ghid.json` / `figs_2d.json` / `mats.json` sunt ignorate, lasa-le ignorate — se regenereaza.

Inainte de commit, ruleaza `python3 gen_ghid.py && python3 gen_2d.py && python3 build_ghid.py && python3 build_2d.py` si verifica ca `gen_2d` raporteaza **0 nepotriviri**. Daca iese diferit, **scrie NEEDS-INPUT si opreste-te** — nu comite un build care nu se verifica singur.

Mesaj de commit, o linie de titlu plus corpul cu motivele de mai sus. **Commit.**

## LOT 2 — auditul si brief-ul terminat

- `AUDIT-2026-08-21.md` — necomis, e sursa constatarilor.
- `DONE-BRIEF-ghid-fix-v2-2026-08-21.md` — mutat in `_archive/briefs/`, apoi comis de acolo.
- Cele patru fisiere `FAILED-*` / `NEEDS-INPUT-*` care apar ca sterse in `git status` sunt deja arhivate; inregistreaza stergerile.

**Commit.**

## LOT 3 — STATUS si igiena

Doua-trei linii in `STATUS.md`: rama pe 46×46 cu motivul de stoc, lambriul pe 19×116 cu motivul de grosime, cosul Leroy Colosseum inchis la 2.679 lei pe 10 produse.

In radacina exista un folder `_to_delete/` cu doua fisiere pe care sesiunea Cowork nu le-a putut sterge (`_probe.lock`, `index.lock.*`). **Sterge folderul** — tu ai drepturi, puntea nu are. Verifica intai ca `.git/` nu are niciun `*.lock` ramas.

Cele ~20 de poze HEIC din `POZE/` raman netrackuite. **Nu le comite** fara sa intrebi — nu stim daca sunt duplicate ale celor din 20.08.

**Commit.**

## DONE MEANS

- `git status --short` nu mai arata `M` sau `D` pe niciunul dintre fisierele de la LOT 1 si LOT 2.
- `git log --oneline -3` arata cele trei commituri noi.
- `grep -c "48×48" GHID-CONSTRUCTIE-casa.html` → **1** (singura aparitie e explicatia „de ce nu 48×48").
- `grep -c "12,5×96" GHID-CONSTRUCTIE-casa.html` → **0**.
- `grep -c "6×100" GHID-CONSTRUCTIE-casa.html` → **0**.
- `cote.json` contine `"T": 46` si `"VB": 1608`.
- `.git/` nu contine niciun `*.lock`; `_to_delete/` nu mai exista.
- Commiturile nu sunt pushed — pushul ramane al lui Vlad.

## VERIFY

Deschide ghidul in Chromium headless la desktop si la 390 px: zero scroll orizontal, consola curata, sase capitole, toate bifele active de la incarcare. Bifezi cateva, dai refresh, bifele raman. Apoi confirma fiecare item din DONE MEANS, unul cate unul.

## IF STUCK

Daca un `.git/*.lock` blocheaza commitul, sterge-l — rulezi local, ai voie. Daca build-ul nu reproduce fisierele de pe disc byte-cu-byte, **fisierele de pe disc sunt canonice** si generatoarele au o abatere: scrie NEEDS-INPUT cu diferenta si opreste-te. Nu rescrie fisierele HTML de mana.
