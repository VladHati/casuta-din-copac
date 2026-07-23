MODEL: sonnet

## GOAL
Update `timeline.html` on the live site so the checklist and phase view reflect real on-site progress as of 2026-07-22: the 4 posts are set, plumb-checked, and anchored per spec.

## CONTENT
Facts to reflect (verbatim, confirmed by Vlad on site):
- Toti 4 stalpi sunt in pozitie finala.
- Ancorare: papuc metalic + fundatie, exact cum indica proiectul (nu ingropati direct).
- Verticalitate verificata cu nivela pe toti 4 stalpii — drepti.
- Proptele temporare in X intre stalpii adiacenti (plus cateva spre gard) tin structura stabila; raman montate pana cand placajul e montat (poarta de secventa din Fisa-santier-casuta.pdf).
- Copacul (deja toaletat, ramurile mari taiate) sta in centrul cadrului, intre stalpi.
- Data confirmarii: 22 iulie 2026.

## CONSTRAINTS
- Edit only `timeline.html`. Do not touch other pages, do not regenerate PDFs.
- Do not touch `STATUS.md` — already updated by Main.
- In `ITEMS` array, item `id:'p1'` currently reads:
  `{id:'p1',g:'Platforma (Faza 1)',l:'1 · Stalpii in ancore (verticali, prinsi slab)'}`
  Change to reflect the real, stronger state — label should say something like
  `'1 · Stalpii montati (papuc + fundatie), verificati cu nivela — drepti'`
  and add a sub-note (`s:` field) along the lines of
  `'4 stalpi, proptele X temporare pana la placaj'`.
  Add `d:true` to this item so it shows pre-checked on a fresh (no localStorage) visit.
- Keep Romanian, no diacritics, same visual style (no CSS/structural changes).

## DONE MEANS
- `timeline.html` ITEMS p1 has updated label + sub + `d:true`.
- Page still renders with no JS errors (open locally or check syntax).
- Commit made locally on `main` with a clear message. Do NOT push — Builder account has no push credentials; Vlad pushes manually (same pattern as every prior STATUS.md entry).
- Append one line to nothing else — STATUS.md stays Main's responsibility.

## IF STUCK
None expected — this is a single-item text edit in a known array.
