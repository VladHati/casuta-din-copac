MODEL: opus

# BRIEF — Manual upgrade v2: fix the dependency crash, finish + commit

## CONTEXT
The previous brief (`FAILED-BRIEF-manual-upgrade.md`) ran correctly through the whole rebuild — the new drawings, legend, safety banner, per-step CRITIC text, BOM screw specs and tool icons are all in and verified good — but it crashed at the very end on `import fitz` in `tools-fise/book.py`: PyMuPDF is not installed in this environment. The engine rebuild is NOT the problem. Just finish it.

## GOAL
Remove the new `fitz` dependency, regenerate the full manual cleanly, fix one page-rhythm orphan, verify, commit local on `main` (Vlad pushes).

## FIX 1 — replace fitz with pypdf (the project already uses pypdf in build_pdfs.py)
In `tools-fise/book.py`:
- Remove `import fitz`.
- The TOC page-number pass currently does `d=fitz.open(OUT)` then `d[i].get_text()` to find which page each section lands on. Replace with pypdf:
  ```python
  from pypdf import PdfReader
  ...
  r = PdfReader(OUT)
  def pageof(needle):
      nn = needle.replace(' ','').upper()
      for i, pg in enumerate(r.pages):
          if nn in (pg.extract_text() or '').replace(' ','').upper():
              return str(i+1)
      return ''
  ```
  Keep the rest of the two-pass cuprins logic identical (build once with placeholder `··`, find pages, rebuild with real numbers).
- If `pypdf` text extraction proves unreliable for matching a section title, the acceptable fallback is to wrap the page-number pass in `try/except` and emit the manual with placeholder dots rather than crash — the build must NEVER fail on the TOC pass again.

## FIX 2 — page-rhythm orphan (lower priority)
Fisa 4's "GATA CAND" checklist spills onto its own near-empty page (was p24). Tighten so a fisa's "gata cand" stays with its last step, or starts each fisa on a fresh page so checklists don't strand. Do not let this block the commit — if it resists a quick fix, note it in STATUS.md and ship the rest.

## REGENERATE + VERIFY
- Run `tools-fise/book.py` then `python3 build_pdfs.py`. Both must exit 0.
- Render pages of the new `PDF/Manual-Faza-1-complet.pdf` and confirm the DONE-MEANS below by eye.

## DONE MEANS
- `book.py` runs to completion with NO fitz import and NO crash; `build_pdfs.py` runs clean.
- Cuprins shows real page numbers (not `··`), and they match the actual pages.
- Drawings still correct (no floating members; joists seat on both beams; front beam under joists; deck reaches back beam = 17 boards; posts consistent).
- Confirm the content fixes from the prior run are present: C2 = 14 in the tracker (Materiale + Comanda Hornbach + Platforma premium); H4 ≥ 204; BM = M10 with its own image (POZE/bolt-m10.svg) and a tracker line; ghid-montaj step 4 shows C2 + correct H1 label. If any are missing (the prior run may have crashed before them), apply them now per the original BRIEF-manual-upgrade Phase 3.
- STATUS.md updated; committed on `main`; NOT pushed.

## IF STUCK
- Do not reintroduce fitz or add any new pip dependency. pypdf and weasyprint are the only allowed libs (already in the project).
- If a content fix from Phase 3 is ambiguous, make the conservative choice and note it; don't stall the commit.
