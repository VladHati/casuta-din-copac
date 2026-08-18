# NEEDS-INPUT — commit-audit-proiect-2026-08-17

## PAS 1: GHID-SIMPLU-casa.html / .pdf — Confirmare modificari

Fisierele au mtime 12.08 fara intrare in STATUS sau brief care sa explice editarile.

`git diff --stat` arata:
```
GHID-SIMPLU-casa.html | 994 ++++++++++++++++++++++++++++++++++++++++++++------
GHID-SIMPLU-casa.pdf  | Bin 63653 -> 199926 bytes
```

Delta = 890 insertari + 104 stereri in HTML + binary change mare in PDF.

**Intrebari pentru Vlad:**

1. **Ai modificat tu GHID-SIMPLU-casa (12.08) intr-o sesiune nedocumentata?** (vs. regen automata din pipeline = normal + expect in brief)
   - DA: includ in COMMIT 1, procursez normal
   - NU / altu: nu le includ, noteaza mai jos ce ai vrut

2. **Daca NU tu: ce continut ar trebui sa fie in GHID-SIMPLU (versiunea canonica)?**

---

## RESTUL BRIEFULUI

Pend de raspunsul asta. Poti raspunde inline (edit-ezi asta) sau nou brief cu raspunsul, si voi merge commits-urile (COMMIT 1, 2, 3) normal.
