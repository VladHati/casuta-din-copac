MODEL: opus

# BRIEF — Manual Faza 1: rebuild drawings + IKEA upgrade

## GOAL
Rebuild the step-drawing engine so the isometrics are geometrically correct and legible, then bring the whole manual to genuine IKEA-assembly quality, then fix the content/BOM gaps. One source of truth, regenerated into `PDF/Manual-Faza-1-complet.pdf`, the per-fisa PDFs, and `fisa-01..11.html`. Commit local on `main` (Vlad pushes).

Full diagnosis with line refs: `MANUAL-AUDIT-findings.md` (read it first). Generator lives in `tools-fise/`: `iso.py` (iso renderer), `fb.py` (per-step data + coordinates), `det.py` (zoom panels — already good, mostly leave), `book.py` (assembles the manual + CSS). The active system is fb.py/book.py; the old `fise_*.py` are archived in `tools-fise/_arhiva/` — ignore them.

## CANONICAL GEOMETRY (the truth every drawing must show — do not change these)
- Frame: 4 posts, 2100 mm width (x, left-right) × 1780 mm depth (z, front-back). Floor +2200.
- Posts: S1,S2 back = full 4000, continuous, carry the manual's tall corners. S3,S4 front = cut at +1872.
- Beams: 2× glulam 90×200 along the 2100 width. Front beam on top of cut front posts; back beam on a wooden ledger (polita) bolted to the tall back posts with 2× M12. Both beam tops +2072.
- Joists: 6× 100×100 front-to-back, resting on top of both beams, cantilever 700 mm past the FRONT beam (balcony). Positions from corner S4 (along width): 100/280/720/1120/1550/1980.
- Decking: larice 28×145, 17 boards, perpendicular to joists.
- Tree (corcodus) Ø160 through the floor near S4 (front-left), between joists 280 and 720, cut at +2780 from ground (~580 above floor). Table fixed to the floor frame, NOT the tree.
- Bracing: diagonals + C2 anti-uplift at the cantilever back end; temporary props at tall back-post tops until Faza 2 walls.
- Balustrade (FAZA 1): 1 m, gaps <90 mm, gate on S3 (opposite the tree on S4).
- Connectors: C1 bracket 100×100×90 + Heco 6×100; C2 bracket 90×90×65 + Heco 6×100; ledger 2× M12; contrafise Heco 8×200 (timber-timber, no bracket); decking inox 5×60; balustrade M10.

---

## PHASE 1 — Rebuild the drawing engine (correctness)

Keep iso.py's projection formula and fb.py's coordinate constants — they are correct. Rebuild the parts that fail:

1. **Single growing model.** Replace the per-stage `base=...` rebuilds with ONE ordered model list built once (posts → polite → back beam → front beam → joists → tree+headers → blocking → bracing/props → decking → balustrade). Each step N renders `MODEL[:k]` as already-built (faint) + the step's new piece(s) highlighted. No step re-invents geometry.
2. **Correct depth ordering.** Replace the centroid-only sort (`iso.py` `_depth` + the `sorted(...,key=_depth)` at the draw call). Implement a real back-to-front order: either (a) split every long member into sub-boxes per span (each joist = inter-beam segment(s) + cantilever segment; each beam = segments between joists) so no two drawn boxes overlap in plan and centroid sort becomes valid, OR (b) a pairwise "is-behind" test (separating axis on projected x, z, y extents) with a dependency sort. Result required: front beam sits visually UNDER all joists, joists clearly rest ON both beams, nothing weaves.
3. **Fix the floating first joist.** In the "place the first joist" step (fb.py ≈L152): the highlighted joist must sit at its real height (top at +2072) — if you keep an explode arrow, the `700 consola` dimension and leader must move with the same offset (couple dim/label/arrow to the box's `ex`), so the leader never points into empty space. Prefer: draw the joist in place (highlighted), show the 700 cantilever dimension on the actual drawn geometry. Do NOT draw the other 5 joists as `built` in this step — show them as faint ghosts or omit them, so "place the first joist" reads as a first action.
4. **One shared camera + scale.** Compute global bounds/scale ONCE from the final full assembly; pass fixed framing into every render call so the model sits in the same frame and grows in place (no per-step re-zoom). Remove the per-call auto-framing.
5. **Parametric posts.** One post function, always full height with the correct cut (front +1872, back +4000). Posts must not morph between fise (kill the posts_full vs posts_stub split).
6. **Decking 17 boards.** `deck_g(15)` → `deck_g(17)` everywhere (steps + cover hero) so the drawn deck reaches the back beam.

DONE-MEANS (Phase 1): render the manual and confirm, by eye on the PDF — (a) no floating member, no leader pointing into empty space; (b) on the joist steps the front beam is under the joists and joists seat on both beams; (c) same camera/scale across all 3D pages; (d) deck reaches the back beam; (e) posts identical shape across fise.

---

## PHASE 2 — IKEA design upgrade (legibility + clarity)

1. **Make the drawing the page.** Raise `book.py` `.drawbox svg{max-height:72mm}` to ~100mm; remove the `.step .drawbox{margin-left:13mm}` indent so step drawings run near full content width. In `iso.py` bump all in-SVG font sizes (badges/labels/dimensions) from 11-12.5 to ~15-17 and increase `pad` so nothing clips. Target: every call-out readable on a phone.
2. **A drawing for every step.** Add a small figure to the ~5 text-only steps: drill 2 holes in polita (Fisa 3); cut blocking (Fisa 8); 5 mm spacer rule (Fisa 10); oiling (Fisa 10); and especially the GATE (Fisa 11) — show WHERE on side S3 the gap goes and how the gate bay differs from a fixed bay. Reuse the model with highlight where possible.
3. **Specific CRITIC text.** Replace the single hardcoded `CRITIC — opreste-te si verifica` with a per-step string saying WHAT to check. The `warn=True` flags in fb.py already mark the steps; change them to carry the text. Examples (RO, no diacritics): Fisa 1 "Verifica fiecare stalp la plumb pe 2 fete inainte de a strange"; Fisa 2 "Linia +1872 identica pe toti 4 stalpii"; Fisa 4/5 "Ambele grinzi la +2072, perfect orizontale"; Fisa 6 "Consola 700 egala la toate joistele; C2 la fiecare reazem"; Fisa 9 "Contrafise prinse la ambele capete INAINTE de a scoate proptelele"; Fisa 11 "Goluri <9 cm peste tot; stalpisori de cadru; testeaza prin impingere". Write a fitting one for each warn step.
4. **Screw length at point of use.** In the per-step PIESE cards, append the dimension to the note (data is in `PARTS`). E.g. "Heco 8x200 · 3 oblice/capat", "Inox 5x60 · 2/joista".
5. **Stronger built/new contrast + full ghost.** Built parts: mid-grey outline (not near-white wash). Ghost target: full wireframe (all 3 faces dashed), not just the top face. Every placement step has an explode arrow showing where the new part comes from.
6. **Tool pictograms.** Add ~6 reusable monoline inline-SVG icons (drill, wrench, level, saw, tape+pencil, 2-person) next to the existing tool text chips.
7. **Legend once + per-page filter.** Full color legend on the "Ce construim" page; on each fisa show only the colors used there (filter by that fisa's parts).
8. **Front-load safety.** Add a small banner on the "Ce construim" page (p2) with the 3 hardest rules: "Copacul nu tine nimic", "Balustrada goluri <9 cm, la 2,2 m", "Nimeni pe consola inainte de contrafise". Keep the full safety page too.
9. **Inventory tick-off.** Add checkboxes to the Materiale cards (reuse the existing `.check .bx` style) so it's a count-before-you-start list.
10. **Page rhythm.** Keep each step's text+drawing+zoom together (no orphaned step on its own page). 

Aesthetic guardrails: this is a print/light document. Preserve and strengthen the existing editorial restraint — serif for the emotional/cover moments, mono for data/dimensions, clean grotesque for structure, ONE surgical accent (the existing orange). No template/SaaS look, no decorative clutter, no new default fonts. Keep RO, no diacritics.

---

## PHASE 3 — Content / BOM fixes

1. **C2 = 14.** fb.py Materiale data + `Tracker_materiale_casuta.xlsx` (sheets Materiale, Comanda Hornbach, Platforma premium): C2 (738910) quantity 12 → 14 (12 joists + 2 back beam). The "+2 grinda spate" note already exists — make the ordered quantity match.
2. **BM = M10, real part.** Keep the balustrade bolt as M10 (text + "Cheie M10" tool already say M10). Stop reusing the M12 photo for `PARTS['BM']` — use a neutral/own image. Add a tracker line for the M10 bolts (Faza 1, ~12, balustrade) so it's budgeted.
3. **H4 ≥ 204.** Decking needs 204 (17×6×2); 200 ordered. Either add a 3rd pack (→300) or note "204 necesare, ia 3 pachete". Pick the 3-pack.
4. **(Web, same data bug — fix while here)** `ghid-montaj.html` step 4 (back beam): add the C2 anti-uplift connector and fix the drawing label "B1 ×4" → it should be H1 (+ C2). Align with Fisa 4/PDF. This is the only non-manual file in scope, included because it's a safety-relevant content error sharing the same fact.

---

## PHASE 4 — Regenerate + verify + commit

- Regenerate: run `tools-fise/book.py` (fise HTML + Fisa-*.pdf + Manual-Faza-1-complet.pdf + Fise-montaj-Faza-1.pdf), then `python3 build_pdfs.py` (section PDFs).
- Self-verify by rendering pages of the new `PDF/Manual-Faza-1-complet.pdf` and checking the DONE-MEANS below. Iterate until they pass — nobody is watching, so do not stop at "it ran".
- Update STATUS.md with one line. Commit local on `main` (do NOT push). Leave a NEEDS-INPUT note only if blocked.

## DONE MEANS (whole brief — all checkable on the regenerated PDF)
- No floating members anywhere; every dimension leader touches the geometry it measures.
- On the joist steps: front beam under joists, joists visibly resting on BOTH beams, 700 cantilever reads as the front balcony.
- Same camera/scale on all 3D pages; posts identical across fise; deck reaches the back beam (17 boards).
- Every step has a drawing (incl. the S3 gate). Drawing call-outs legible (fonts ≥15 in-SVG, drawing box ≥100mm).
- CRITIC blocks carry step-specific text, not the generic line.
- BOM cards show screw length; tool icons present; legend full once + filtered per fisa; safety banner on p2; checkboxes on Materiale.
- C2 = 14 and H4 ≥ 204 in the tracker; BM = M10 with its own image + a tracker line.
- ghid-montaj step 4 shows C2 + correct H1 label.
- `tools-fise/book.py` and `build_pdfs.py` both run clean; commit on `main`; not pushed.

## IF STUCK
- The depth-sort is the hard part. If a full behind-test is too much, the "split long members into per-span sub-boxes" approach is acceptable and sufficient — correctness over elegance.
- If a new per-step drawing is hard to derive from the model, a clear simple schematic (like the det.py zoom panels) is acceptable for that step.
- Do NOT change any canonical dimension or the projection formula. Do NOT touch `tools-fise/_arhiva/`.
- If weasyprint/pango is missing, install and continue — do not skip PDF regeneration.
- Anything genuinely ambiguous: make the conservative choice, finish the rest, and record the open question in STATUS.md. Do not stall the whole build on one detail.
