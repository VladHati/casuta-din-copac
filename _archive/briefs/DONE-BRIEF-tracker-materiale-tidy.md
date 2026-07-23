# BRIEF — tidy: tracker contrafise word + materiale.html align to 14/300

## GOAL
Two cosmetic alignments so the docs match decisions already shipped (C2=14, H4=3 packs). Commit local on `main`. Vlad pushes. Do NOT touch the manual, the drawings, or any quantity that's already correct.

## FIX 1 — Tracker xlsx, stray "contrafise" word
`Tracker_materiale_casuta.xlsx`, sheet **"Platforma premium"**: the Heco 6×100 row's role/Rol cell reads "...conectori, **contrafise**". Contrafise use Heco **8×200** (their own row), not 6×100. Remove the word "contrafise" from the 6×100 role cell (leave "coltare, conectori"). Change nothing else — no quantities, no prices.

## FIX 2 — materiale.html: align C2 + inox to the decisions (no longer "gaps")
The tracker order is now C2=14 and H4=3 packs (300). `materiale.html` still frames these as gaps. Update:
- **Line ~188** (C2 rol): `...anti-ridicare (2/joista). +2 pt grinda spate = vezi „ce mai trebuie luat”.` → `...anti-ridicare (2/joista), inclusiv +2 pt grinda spate. Total 14, comandat.`
- **Line ~349** (table C2 row): qty `×12 + 2` → `×14`; cod `comandat 12 · 738910 (+2 anti-smulgere de luat)` → `comandat 14 · 738910`; status badge: change `<span class="stt gap">+2</span>` → a non-gap badge (e.g. `<span class="stt ok">COMANDAT</span>` using the existing `--ok` colour).
- **Line ~353** (table H4 row): qty `~204 buc` keep; cod `comandat · 2×100 buc · 10528829` → `comandat · 3×100 buc · 10528829`; status `<span class="stt gap">LA LIMITA</span>` → `<span class="stt ok">COMANDAT</span>`.
- **Lines ~375-376** (H4 explainer): `200 buc comandate, ~204 necesare … ar trebui sa ajunga la fix.` + the `→ Daca vrei margine…` line → replace with one line: `300 buc comandate (3×100), ~204 necesare — margine confortabila.` Remove the now-moot "mai iei o cutie" action line.
- **Lines ~389-391** (the "2 coltare in plus / anti-smulgere" card): the +2 are now in the ordered 14 — either delete this card or change its body to: `Cele 2 coltare anti-smulgere pentru grinda spate sunt deja in cele 14 comandate. Nimic de luat in plus.` and drop the `→` action line.
Keep everything else on the page intact.

## DONE MEANS
- Tracker "Platforma premium" 6×100 role no longer contains "contrafise"; 8×200 row unchanged.
- materiale.html: C2 shows 14 comandat (no "+2" gap badge); H4 shows 3×100 / 300 (no "LA LIMITA"); no remaining "ce mai trebuie luat" framing for C2/inox.
- `python3 build_pdfs.py` runs clean (materiale.html feeds 06-Materiale.pdf — regenerate it).
- Committed on `main`, NOT pushed. STATUS.md updated.

## CONSTRAINTS
Romanian, no diacritics. Change ONLY these two files (+ the regenerated 06-Materiale.pdf). Don't touch the manual, fise, drawings, or correct quantities.

## IF STUCK
- If the `.stt` badge classes differ, match an existing non-gap/positive badge style already used on the page. Don't invent new CSS.
- Don't change the manual's BOM (it's already 14/300 correct).
