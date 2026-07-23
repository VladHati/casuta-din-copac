MODEL: opus

# BRIEF — Manual drawings: new z-buffer renderer for all 11 steps + integrate

## CONTEXT — read first
The old isometric engine (`tools-fise/iso.py`, used by `fb.py`) produced broken drawings (floating members, beam-vs-joist weave, overlaps). It is RETIRED for step drawings. A new, approved renderer already exists in `tools-fise/`:
- `axon.py` — the parametric model (same canonical geometry as `montaj-3d-complet.html`), the isometric projection (bird's-eye 3/4, camera ABOVE looking down), palettes, per-step visibility, and a vector SVG render() (reference only).
- `axon2.py` — the production renderer: pure-numpy **z-buffer rasteriser** (correct per-pixel occlusion) with auto edge-detection (clean black outlines, hidden lines removed), IKEA line-art style (white/grey parts, new part in warm accent, dashed accent ghost to final position), supersampled PNG output.

Vlad has reviewed and APPROVED the look of `axon2.py` (steps 1,6,9,11). Do NOT change the camera angle, palette, or line style — they are signed off. Build ON this engine.

Deps: numpy + Pillow (`pip install pillow numpy --break-system-packages` if missing).

## GOAL
Render all 11 step drawings with `axon2.py`, overlay IKEA-style labels/dimensions/part-badges/arrowheads as crisp vector on top of each render, replace the old `iso.py` drawings in the manual, regenerate `PDF/Manual-Faza-1-complet.pdf` + the `fisa-*.html` + section PDFs, commit local on `main` (Vlad pushes). Keep the prior IKEA design upgrade already in `fb.py`/`book.py` (per-step CRITIC text, BOM screw specs, tool icons, materiale checkboxes, safety banner, legend-once) — only the DRAWINGS change.

## PHASE 1 — label anchors in the renderer
Extend `axon2.render()` to also return/emit, per step, a JSON of 2D pixel anchor points for labels (so the page can place crisp vector text over the raster). Add a function that projects any 3D point through the SAME transform + supersample/downsample math used for the image, returning final-image (x,y) px. Emit `r_step{N}.json` next to each `r_step{N}.png` containing the anchors listed in Phase 3. Do NOT bake text into the PNG.

## PHASE 2 — render all 11
Render steps 1..11 to committed files in the repo, e.g. `img/steps/step-01.png … step-11.png` (create the folder; these are committed so Netlify + the PDF use them). Use the existing `axon2.render(step, path)`. Confirm each PNG: correct occlusion, new part in accent + dashed ghost, deck-up bird's-eye view, no solid-black slivers. Also render a clean **overview** image (full assembly, no explode) for the "Ce construim" page.

## PHASE 3 — overlay labels/dimensions (crisp vector over the PNG)
In `fb.py`/`book.py`, the step drawing becomes: the PNG as the image, with an absolutely-positioned overlay (an inline SVG or positioned HTML sized to the PNG's display box) carrying labels in the manual typography (Space Mono for data/dims, the accent for emphasis). Place each label at its anchor px from the JSON (scaled to display size). Minimum overlay content per step:
- 1: badge **ST** on a post; small note "S1·S2 spate (4 m) · S3·S4 fata (taiate)".
- 2: level marks **+2200** (podea) and **+1872** (taiere) with thin leader lines; "taie 1872, nu 2200".
- 3: **polita +1872**, **M12 ×2**.
- 4: **+2072**, **GR spate** (badge), "pe polita".
- 5: **+2072**, **GR fata** (badge), **C1** at the post tops.
- 6: **700 consola** (dimension on the cantilever), **JO ×6**, positions "100·280·720·1120·1550·1980", **C2** at reazeme.
- 7: **+2780** (tree cut), "joc 3–5 cm", **copac** badge.
- 8: **blocaje** badge.
- 9: **contrafise** badges on the diagonals, "scoate proptelele de la baza".
- 10: **DL 28×145**, "gol 5 mm".
- 11: **1 m**, "goluri <9 cm", **poarta · S3**.
Add small arrowheads at the tip of each dashed ghost line (pointing to the new part's final seat). Keep labels minimal and legible — IKEA restraint, not clutter.

## PHASE 4 — wire into the manual + retire old engine
- In `fb.py`, replace the per-step `iso.py` SVG drawing with the new PNG + overlay. Keep the `det.py` ZOOM detail panels, BOM PIESE cards, SCULE, GATA CAND, CRITIC blocks as they are.
- Update `montaj-3d-complet.html`? NO — leave the web 3D model alone (it works). This brief is the print/HTML manual drawings only.
- Move `iso.py` to `tools-fise/_arhiva/` (no longer used). Delete the stray prototype `/_proto-render.html` in the project root.
- If `book.py` still imports `fitz`: replace with `pypdf` (already a project dep) per the page-number pass — the build must not depend on PyMuPDF.

## PHASE 5 — regenerate + verify + commit
- Run `tools-fise/book.py` then `python3 build_pdfs.py`. Both exit 0.
- Render PDF pages and verify by eye: every step shows the new bird's-eye line-art drawing with correct occlusion, the new part in accent with ghost+arrow, labels placed correctly and legible, deck visible from above.
- Commit on `main` with a clear message. Do NOT push. Update STATUS.md.

## CONSTRAINTS
- Do NOT alter canonical geometry or the approved camera/palette/line style in axon.py/axon2.py.
- Romanian, no diacritics. Light/print aesthetic, editorial restraint, one accent.
- Change ONLY the drawings + their overlays + the iso retirement; leave other manual content intact.

## DONE MEANS
- `img/steps/step-01..11.png` exist, committed; manual + fise use them.
- Every step drawing is the new z-buffer line-art, bird's-eye, correct occlusion, accent new-part + ghost + arrowhead.
- Labels/dimensions per Phase 3 present, crisp (vector text, not baked raster), correctly anchored.
- `iso.py` retired to `_arhiva`; `_proto-render.html` deleted; no `fitz` import anywhere.
- `book.py` + `build_pdfs.py` run clean; manual PDF regenerated; committed on `main`, not pushed.

## IF STUCK
- Anchor scaling: the PNG is rendered at S=300, SS=4 then downsampled; project anchors with the downsampled transform (S, MARGIN, minx/miny from the same render). Expose those from render() rather than recomputing.
- If overlay positioning is hard in print CSS, render the labels as a second SVG layer with the exact pixel viewBox of the PNG and absolutely overlay it — same coordinate system, reliable in weasyprint.
- Pillow/numpy missing → install with --break-system-packages, don't skip.
- Never reintroduce iso.py drawings or fitz. Don't invent dimensions — use the values above / the canonical model.
