MODEL: sonnet

## GOAL
Update `timeline.html` item `p2` with a subtitle reflecting real partial progress: the front posts are cut, the +2200 level line is not. Do NOT check the box — the item covers two actions and only one is done.

## CONTENT
Facts confirmed by Vlad via photo, 22 iulie 2026 (evening, on-site):
- Stalpii din fata sunt vizibil mai scurti decat stalpii din spate — taiere confirmata prin poza directa (nu doar raport verbal).
- Stalpul din spatele trunchiului copacului nu e vizibil in poze (ascuns de crengi) — neconfirmat separat, dar Vlad a raportat verbal ca taierea e facuta.
- Inaltimea exacta (1872mm) nu se poate verifica dintr-o poza fara reper de masura — se noteaza ca "taiat", nu ca "masurat".
- Nivelul +2200 (trasarea liniei de nivel pe stalpii din spate) — Vlad a confirmat explicit ca NU e facut inca.

## EXACT EDIT
File: `timeline.html`

Find this exact line (inside the `ITEMS` array):
```
 {id:'p2',g:'Platforma (Faza 1)',l:'2 · Nivel +2200 + taiere stalpi fata la 1872'},
```

Replace with:
```
 {id:'p2',g:'Platforma (Faza 1)',l:'2 · Nivel +2200 + taiere stalpi fata la 1872',s:'Stalpii fata taiati (confirmat foto 22 iul); nivel +2200 inca de facut'},
```

Nothing else in the file changes. Do NOT add `d:true` — the item stays unchecked since only half the work (cutting, not leveling) is done.

## CONSTRAINTS
- Touch only `timeline.html`, only the `p2` object. No other file, no other ITEMS entry.
- Keep Romanian, no diacritics, no CSS/structural changes.
- Do not set `d:true` on this item under any circumstance — that would falsely mark the +2200 level as done too.
- A stale `.git/index.lock` may be present from earlier runs. safe-commit.sh clears locks older than 5 min automatically — let it.

## DONE MEANS
- `git diff timeline.html` shows exactly one changed line (the `p2` object) — only the `s:` field added, `l:` unchanged, no `d:true`.
- Inline script still valid (no trailing-comma / broken-literal errors).
- Commit made locally on `main` via safe-commit.sh (never a bare `git commit`):
  `/Users/Shared/Builds/bin/safe-commit.sh -m "santier 22-iul: p2 stalpi fata taiati (confirmat foto), nivel +2200 pending" -- timeline.html`
  Do NOT push — Vlad pushes manually.
- Confirm the commit hash in this brief's completion. If safe-commit reports HEAD-did-not-move, do NOT loop — stop and leave a NEEDS-INPUT note.

## IF STUCK
If the `p2` object no longer exists or its structure changed, OR the process crashes: stop, rename this file to `NEEDS-INPUT-timeline-p2-cut-partial.md`, write one sentence describing exactly what you found. Do not guess, do not silently fail.
