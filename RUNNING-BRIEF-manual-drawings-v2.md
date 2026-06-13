MODEL: opus

# BRIEF — Manual drawings v2: finish + fix the failed run, then commit

## CONTEXT — read first
The previous run (`FAILED-BRIEF-manual-drawings.md`) got most of the way and is sitting UNCOMMITTED in the working tree:
- DONE & good: every fisa HERO drawing is now the new z-buffer 3D render (`tools-fise/axon2.py`) with overlay labels + caption (verified pages 22 Fisa 8, 31 Fisa 11). All 11 step PNGs + overview exist in `img/steps/`. Keep these.
- NOT done / broken: the numbered SUB-STEP drawings inside each fisa are 2D schematics, and several have TEXT-OVERLAP bugs. Builder correctly did not commit.

Vlad's decision on style: **3D for placement, 2D for fastening.** The hero render already provides the 3D placement view per fisa, so KEEP: hero = 3D render (placement), sub-steps = 2D schematic (fastening/detail/marking) + the ZOOM panels. Do NOT add a 3D render to every sub-step. The job is to FINISH and FIX, not rebuild.

Engine is approved and frozen: do not change camera/palette/line style in `axon.py`/`axon2.py`.

## GOAL
Fix the broken 2D sub-step drawings, verify all 11 fise (hero + sub-steps + ZOOM) are clean, commit on `main`. Vlad pushes.

## PHASE 1 — fix every text/graphic overlap in the 2D sub-step schematics
Audit ALL numbered sub-step drawings across the 11 fise. No label may sit on top of geometry or another label. Known offenders to fix (and sweep for more):
- Fisa 10 (dusumea), oiling sub-step: caption "Dupa montaj…" overlaps the oil-bottle graphic, and "ulei tec F1" floats over it (manual ~p30). Move caption clear of the bottle.
- Fisa 8 (blocaje), sub-step 1: "taie pe masura" label overlaps a joist bar (~p23). Reposition.
Fix the label-placement logic in the schematic generator (the per-step 2D drawing functions), not by nudging one PDF. After fixing, EVERY sub-step drawing must have all text in clear space.

## PHASE 2 — verify the heroes (all 11)
Confirm each fisa hero is the new render with: correct occlusion, bird's-eye, new part in accent + dashed ghost + arrowhead, and the overlay label/dimension/caption placed correctly (per the Phase-3 list in the prior brief). Re-render any that are missing/wrong via `axon2.py`. The overview page ("Ce construim") should use `img/steps/overview.png`.

## PHASE 3 — retire old engine + dependency hygiene (if not already done)
- `tools-fise/iso.py` no longer used for drawings → move to `tools-fise/_arhiva/`.
- Delete the stray `/_proto-render.html` if still present.
- No `fitz` import anywhere (book.py uses pypdf). Confirm.
- Commit the new files: `tools-fise/axon.py`, `tools-fise/axon2.py`, `img/steps/*`.

## PHASE 4 — regenerate, verify by eye, commit
- Run `tools-fise/book.py` then `python3 build_pdfs.py`. Both exit 0.
- Page through the regenerated `PDF/Manual-Faza-1-complet.pdf`: every fisa hero = clean 3D render; every sub-step drawing = clean (no overlaps); ZOOM panels intact; BOM/CRITIC/tools/checkboxes intact. Fix anything that isn't clean — do not stop at "it ran".
- Commit on `main` with a clear message (include axon.py, axon2.py, img/steps). Do NOT push. Update STATUS.md.

## CONSTRAINTS
- Don't touch canonical geometry or the frozen render style.
- Romanian, no diacritics. Light/print, editorial restraint, one accent.
- Change only the sub-step drawings (fixes) + engine retirement + commit. Leave hero renders, BOM, CRITIC text, tools, materiale, safety as they are.

## DONE MEANS
- Zero text/graphic overlaps on any drawing in the manual (heroes + sub-steps + ZOOM).
- All 11 heroes are the new 3D render with correct overlays; overview page uses the render.
- iso.py archived; no fitz; axon.py/axon2.py/img-steps committed.
- `book.py` + `build_pdfs.py` exit 0; manual regenerated; committed on `main`, not pushed; STATUS.md updated.

## IF STUCK
- If a sub-step schematic's layout is hard to de-collide, simplify it (fewer labels, more space) rather than leaving an overlap. Clarity over density.
- Never reintroduce iso.py drawings or fitz. Don't invent dimensions.
- If a hero render anchor/overlay is misplaced, fix the anchor projection in axon2 (use the render's own S/MARGIN/min transform), don't hand-place.
- Anything genuinely ambiguous: make the clean conservative choice, finish the rest, note it in STATUS.md. Do not fail the whole run on one detail.
