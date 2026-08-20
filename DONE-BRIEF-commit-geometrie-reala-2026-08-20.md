MODEL: haiku

# BRIEF — commit lotul de geometrie reala (20.08.2026)

## GOAL

Comite in git lotul de corectii din 20.08 al casei, plus munca necomisa a sesiunii paralele de azi. Zero editari de continut — fisierele sunt deja scrise si verificate. Commit-only.

## CONTENT

Toate fisierele exista deja in radacina proiectului. Nu le modifica, nu le regenera, nu rula `gen_scheme.py` sau `build_pdfs.py`.

**COMMIT 1 — geometria remasurata a casei**

```
AUDIT-2026-08-20.md
MASURATORI-CONFIRMARE-2026-08-20.html
PROIECT-CASA-2026-08-17.html
PROIECT-CASA-2026-08-17.pdf
SCHEME-CASA-2026-08-17.html
SCHEME-CASA-2026-08-17.pdf
LISTA-LEROY-2026-08-17.html
LISTA-LEROY-2026-08-17.pdf
gen_scheme.py
figs.json
```

Mesaj de commit:

```
Geometrie reala a casei, din masuratori de santier (20.08)

Adancimea masurata e 1575, nu 1100 cum scria planul: span intre
reazeme 1670, panta 12,3 -> 8,2 grade, caprior 1331 -> 1889.
Sub 10 grade Onduline cere astereala continua (verificat pe
uk.onduline.com), deci acoperisul trece pe 2 placi OSB3 de 12 si
ies cele 4 sipci plus sipca diagonala.

Latimi masurate: 1995 spate / 1975 fata, lumina intre fete;
stalpi 100x100 si 90x90 verificati cu ruleta. Peretii se taie
fiecare pe cota lui (1990 / 1970) — dreptunghiul e in afara
echerului cu 20 mm.

Corectat si un P0 din auditul de azi: verticalele lateralelor
1556/1709/1862 erau aritmetica pantei moarte de 15,6 grade.
Acum 1581/1653/1730/1802.

Cantitati: lambriu 5->6, rigla 27->20, scandura 28->20, OSB 0->2,
vinclu 52->64, 8x140 16->36. Buget ~3.360-3.500 lei.

Bug-uri de desen reparate in gen_scheme.py: capriori F5 desenati
100 lati in loc de 44, panta F1 desenata din span gresit, stalpii
F4 desenati de la 44 in sus, jargon mort "ancora anti-vant".
```

**COMMIT 2 — golul de colt si desenele pentru Freeform (munca sesiunii paralele, necomisa)**

```
BLOCAJ-COLT-2026-08-20.html
BLOCAJ-COLT-2026-08-20.pdf
gen_ikea.py
gen_doc_ikea.py
gen_board.py
gen_png.py
figs_ikea.json
FREEFORM-PNG/
```

Mesaj de commit:

```
Blocajul de la coltul din spate + desenele pentru Freeform

Detaliul 7 din SCHEME-CASA e depasit: blocajul se aseaza pe doua
vincluri montate ca polite pe grinda groasa, nu pe un singur
coltar lateral. Se repeta pe 2 laturi x 2 colturi.

FREEFORM-PNG: desenele exportate ca PNG cu fundal transparent
pentru tabla din Freeform.
```

**COMMIT 3 — STATUS**

```
STATUS.md
```

Mesaj: `STATUS: audit multi-agent + geometrie remasurata (20.08)`

## CONSTRAINTS

- **Commit-only.** Nu edita niciun fisier de continut. Daca ceva pare gresit intr-un document, NU-l repara — scrie observatia in `NEEDS-INPUT-commit-geometrie-2026-08-20.md` si comite restul.
- **Nu face push.** Contul Builder primeste 403. Push-ul ramane la Vlad, de fiecare data.
- Daca `.git/index.lock` exista, sterge-l inainte (blocaj cunoscut, s-a mai intamplat de doua ori in proiectul asta).
- Daca vreun fisier din liste lipseste, comite restul si noteaza care lipsea in STATUS.
- Nu atinge `_archive/`.

## DONE MEANS

- `git log --oneline -3` arata cele trei commit-uri noi, in ordinea de mai sus
- `git status --short` e curat, cu exceptia fisierelor pe care le ignora `.gitignore`
- `git show --stat HEAD~2` listeaza cele 10 fisiere din COMMIT 1
- Nicio modificare de continut: `git diff HEAD~3 HEAD --stat` arata doar fisierele enumerate mai sus, si niciun fisier pe care brieful nu-l numeste

## VERIFY

Inainte de a scrie DONE in STATUS.md: ruleaza `git log --oneline -3`, `git status --short` si `git show --stat HEAD~2`, apoi confirma fiecare punct din DONE MEANS unul cate unul. Verifica explicit ca nu ai facut push (`git status -sb` trebuie sa arate `ahead`). Daca ceva nu trece, repara si re-verifica; nu raporta done pe o verificare picata.

## IF STUCK

- Fisier din lista lipseste → comite restul, noteaza in STATUS care lipsea, nu inventa continut.
- Conflict de merge → nu rezolva, opreste-te si scrie `NEEDS-INPUT-commit-geometrie-2026-08-20.md` cu ce ai gasit.
- `FREEFORM-PNG/` e mare (~5 MB) → e in regula, se comite ca atare; daca `.gitignore` il exclude deja, sari peste el si noteaza in STATUS.
