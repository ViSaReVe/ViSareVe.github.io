# tools/

Scripts that generate the site's image assets. Excluded from the Jekyll
build (`_config.yml` → `exclude`), so nothing here is published.

Run everything from the repo root.

| Script | Generates | From |
|---|---|---|
| `make_logos.py` | `assets/img/logos/*.png` — 88px organization tiles, shown at 44px in Experience | `assets/img/logos/_src/` |
| `make_og.py` | `assets/img/og-card.png` (1200×630 share card) and `assets/img/apple-touch-icon.png` | generated — synthetic sEMG burst, fixed seed |

```bash
python3 tools/make_logos.py
python3 tools/make_og.py
```

Both are deterministic: re-running reproduces byte-identical output.

## Originals

`assets/img/logos/_src/` holds the logo files as received. Jekyll skips
underscore-prefixed directories, so they stay in version control without
being served. Keep them — the tiles cannot be re-derived at a different
size without them.

`brainsightai-wide.jpeg` is unused by the site; it's the horizontal
wordmark, kept for contexts where a wide lockup fits better than a tile.

## Adding a logo

1. Drop the original in `assets/img/logos/_src/`.
2. Add an entry to `LOGOS` in `make_logos.py` — `mode: "crop"` for a
   square-ish mark, `mode: "stack"` for a wide wordmark that needs its
   words restacked to stay legible at 44px.
3. Run the script, then set `logo:` on the matching entry in
   `_data/experience.yml`.
