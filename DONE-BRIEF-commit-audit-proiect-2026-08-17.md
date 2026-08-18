MODEL: haiku
EFFORT: low

# BRIEF — commit-only: audit 17.08 + proiect casa + restante v3 (ZERO editari de continut)

## GOAL

Doar git. Niciun fisier nu se editeaza, nu se regenereaza, nu se rescrie. Toate fisierele exista deja pe disc.

## PAS 0

Daca exista `.git/index.lock` (0 bytes, vechi): sterge-l O data si continua. Daca reapare dupa stergere: STOP, scrie NEEDS-INPUT cu eroarea exacta.

## PAS 1 — verificare GHID (singura decizie din brief)

`git diff --stat -- GHID-SIMPLU-casa.html GHID-SIMPLU-casa.pdf`
Fisierele au mtime 12.08 fara intrare in STATUS. Daca diff-ul e gol sau minor (regen/whitespace/metadata PDF): intra in COMMIT 1. Daca arata modificari de continut substantiale: NU le comite, noteaza in NEEDS-INPUT-commit-2026-08-17.md ce arata diff-ul, si continua cu restul.

## COMMIT 1 — restante v3 + poze + status

```
git add assets/iso/ca-1-panou.svg assets/iso/ca-2-ridicare.svg assets/iso/ca-3-acoperis.svg MANUAL-FAZA-2.pdf POZE/ STATUS.md
git add GHID-SIMPLU-casa.html GHID-SIMPLU-casa.pdf   # DOAR daca PAS 1 a zis ok
git commit -m "regen v3 (SVG casa + MANUAL pdf, facute 11.08, fals-negativ #6) + poze 16.08 + STATUS 16-17.08"
```

## COMMIT 2 — livrabilele 17.08

```
git add AUDIT-2026-08-17.md PROIECT-CASA-2026-08-17.html PROIECT-CASA-2026-08-17.pdf
git commit -m "audit 17.08 + PROIECT-CASA: executie F4 pe etape, Leroy-only cu substituiri (laminat 44x100, 8x140, vincluri-ancora)"
```

## COMMIT 3 — arhivare briefuri procesate

```
git mv FAILED-BRIEF-continut-v3-2026-08-11.md "_archive/briefs/DONE-BRIEF-continut-v3-2026-08-11-fals-negativ-6.md"
git mv DONE-BRIEF-commit-only-2026-08-11.md _archive/briefs/
git commit -m "arhivare: v3 redenumit DONE (fals-negativ #6 - lucrarea era completa) + commit-only 11.08"
```

## DONE MEANS

- 3 commituri noi (sau 2 + NEEDS-INPUT daca GHID a fost scos).
- `git status --short` curat, minus brieful asta (RUNNING) si eventualul NEEDS-INPUT.
- O linie noua in STATUS.md cu hash-urile (append, nu rescrie intrarea 17.08).
- Push NU se face de aici (403 cunoscut) — ramane la Vlad.
