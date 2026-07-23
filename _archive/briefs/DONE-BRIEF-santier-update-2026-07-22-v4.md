MODEL: sonnet

## GOAL
Update `timeline.html` so the checklist reflects real on-site progress as of 2026-07-22: the 4 posts are set, plumb-checked, anchored per spec. Attempts v1/v2/v3 all failed with `exit 1` / $0 cost — root cause was an **expired Builder OAuth login + dropped internet**, not the brief. Both fixed 2026-07-22 ~11:17 (login successful, `claude -p` returns Hello). This v4 is the clean rerun of the same trivial one-line edit.

## CONTENT
Facts confirmed by Vlad on site, 22 iulie 2026:
- Toti 4 stalpi sunt in pozitie finala, ancorati pe papuc metalic + fundatie (exact cum indica proiectul, nu ingropati direct).
- Verticalitate verificata cu nivela pe toti 4 stalpii — drepti.
- Proptele temporare in X intre stalpii adiacenti (plus cateva spre gard) tin structura stabila; raman montate pana cand placajul e montat.
- Copacul (deja toaletat) sta in centrul cadrului, intre stalpi.

## EXACT EDIT
File: `timeline.html`

Find this exact line (inside the `ITEMS` array, at line 118):
```
 {id:'p1',g:'Platforma (Faza 1)',l:'1 · Stalpii in ancore (verticali, prinsi slab)'},
```

Replace with:
```
 {id:'p1',g:'Platforma (Faza 1)',l:'1 · Stalpii montati (papuc + fundatie), verificati cu nivela',s:'4 stalpi, proptele X temporare pana la placaj',d:true},
```

Nothing else in the file changes.

## CONSTRAINTS
- Touch only `timeline.html`. Do not touch any other file (no PDFs, no STATUS.md, no other HTML pages).
- If the find string above does not match exactly (whitespace, quotes), open `timeline.html`, find the object with `id:'p1'` in the `ITEMS` array, and apply the same three additions: change `l:` to `'1 · Stalpii montati (papuc + fundatie), verificati cu nivela'`, add `s:'4 stalpi, proptele X temporare pana la placaj'`, add `d:true`. Do not modify any other object.
- Keep Romanian, no diacritics, no CSS/structural changes.
- A stale `.git/index.lock` may be present from the interrupted runs. safe-commit.sh clears locks older than 5 min automatically — let it. Do NOT manually delete a fresh lock.

## DONE MEANS
- `git diff timeline.html` shows exactly one changed line (the `p1` object) — nothing else touched.
- Inline script still valid (no trailing-comma / broken-literal errors).
- Commit made locally on `main` via safe-commit.sh (never a bare `git commit`):
  `/Users/Shared/Builds/bin/safe-commit.sh -m "santier 22-iul: p1 stalpi montati papuc+fundatie, verificat nivela, pre-bifat" -- timeline.html`
  Do NOT push — Builder account has no push credentials; Vlad pushes manually.
- Confirm the commit hash in this brief's completion. If safe-commit reports HEAD-did-not-move, do NOT loop — stop and leave the NEEDS-INPUT note.

## IF STUCK
If `timeline.html` structure changed (e.g. `p1` no longer exists), OR the process crashes again before doing any work: stop, rename this file to `NEEDS-INPUT-santier-update-2026-07-22.md`, and write one sentence describing exactly what you found (or the exact error). Do not guess, do not silently fail.
