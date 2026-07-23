MODEL: sonnet

## GOAL
Update `timeline.html` on the live site so the checklist reflects real on-site progress as of 2026-07-22: the 4 posts are set, plumb-checked, and anchored per spec. Prior attempt (`FAILED-BRIEF-santier-update-2026-07-22.md`) failed with no recorded diff, no commit, and no logged reason — this v2 gives the exact literal edit to remove ambiguity.

## CONTENT
Facts confirmed by Vlad on site, 22 iulie 2026:
- Toti 4 stalpi sunt in pozitie finala, ancorati pe papuc metalic + fundatie (exact cum indica proiectul, nu ingropati direct).
- Verticalitate verificata cu nivela pe toti 4 stalpii — drepti.
- Proptele temporare in X intre stalpii adiacenti (plus cateva spre gard) tin structura stabila; raman montate pana cand placajul e montat.
- Copacul (deja toaletat) sta in centrul cadrului, intre stalpi.

## EXACT EDIT
File: `timeline.html`

Find this exact line (inside the `ITEMS` array, around line 118):
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
- If the find string above does not match exactly (whitespace, quotes, etc.), open `timeline.html`, locate the `ITEMS` array, find the object with `id:'p1'`, and apply the same three additions to it: change the `l:` text to `'1 · Stalpii montati (papuc + fundatie), verificati cu nivela'`, add `s:'4 stalpi, proptele X temporare pana la placaj'`, add `d:true`. Do not modify any other object in the array.
- Keep Romanian, no diacritics, no CSS/structural changes.

## DONE MEANS
- `git diff timeline.html` shows exactly one changed line (the `p1` object) — nothing else touched.
- File has valid JS (no trailing comma errors, no broken object literal — check by eye or run `node -c` style syntax check on the inline script if tooling allows).
- Commit made locally on `main` with message describing the change. Do NOT push — Builder account has no push credentials.
- Report in the brief's completion (rename to DONE-BRIEF-...) or leave a one-line note in this file itself confirming what was actually changed and the commit hash — so failure mode from last time (silent, unexplained) cannot repeat.

## IF STUCK
If `timeline.html` structure has changed since this brief was written (e.g. `p1` no longer exists), stop, rename this file to `NEEDS-INPUT-santier-update-2026-07-22.md`, and write one sentence in it explaining exactly what you found instead. Do not guess, do not silently fail.
