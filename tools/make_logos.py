"""Regenerate the experience-logo tiles from the archived originals.

Sources live in assets/img/logos/_src/ (versioned, not published — Jekyll
skips underscore-prefixed directories). Output is an 88px square PNG per
organization, displayed at 44px in the Experience list.

Run from the repo root:  python3 tools/make_logos.py
"""

from PIL import Image
import numpy as np
import pathlib

SRC = pathlib.Path("assets/img/logos/_src")
OUT = pathlib.Path("assets/img/logos")
SIZE = 88
INK_THRESHOLD = 200      # pixels darker than this count as ink
WORD_GAP = 60            # blank columns that separate two words
BAND_MIN_HEIGHT = 10     # ignore ink bands thinner than this

LOGOS = [
    # Already square-ish: centre-crop and keep the native background.
    {"src": "usc-isi.jpg",             "out": "usc-isi.png",      "mode": "crop"},
    {"src": "brainsightai-square.png", "out": "brainsightai.png", "mode": "crop"},
    {"src": "hmal-iiit.jpeg",          "out": "hmal-iiit.png",    "mode": "crop"},
    # A ~7.5:1 wordmark. Letterboxed into a square it renders ~5px tall, so
    # restack its own words onto two lines to fill the tile.
    {"src": "coor-lab.png",            "out": "coor-usc.png",     "mode": "stack",
     "band": 0, "bg": "#ffffff", "pad": 6, "gap": 5},
]


def ink_bands(ink):
    """Row ranges containing ink, top to bottom."""
    rows = ink.sum(axis=1) > 0
    bands, start = [], None
    for i, filled in enumerate(rows):
        if filled and start is None:
            start = i
        elif not filled and start is not None:
            if i - start > BAND_MIN_HEIGHT:
                bands.append((start, i))
            start = None
    if start is not None:
        bands.append((start, len(rows)))
    return bands


def split_words(ink, band):
    """Column ranges for each word inside one ink band."""
    filled = ink[band[0]:band[1]].sum(axis=0) > 0
    words, start, gap = [], None, 0
    for i, c in enumerate(filled):
        if c:
            if start is None:
                start = i
            gap = 0
        elif start is not None:
            gap += 1
            if gap > WORD_GAP:
                words.append((start, i - gap))
                start = None
    if start is not None:
        words.append((start, len(filled)))
    return words


def crop_square(im):
    w, h = im.size
    s = min(w, h)
    return im.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s)) \
             .resize((SIZE, SIZE), Image.LANCZOS)


def stack_words(im, band_index, bg, pad, gap):
    ink = np.asarray(im.convert("L")) < INK_THRESHOLD
    band = ink_bands(ink)[band_index]

    lines = []
    for x0, x1 in split_words(ink, band):
        rows = np.where(ink[band[0]:band[1], x0:x1].sum(axis=1) > 0)[0]
        lines.append(im.crop((x0, band[0] + int(rows[0]), x1, band[0] + int(rows[-1]) + 1)))

    avail_w = SIZE - 2 * pad
    avail_h = SIZE - 2 * pad - gap * (len(lines) - 1)
    scale = min(avail_w / max(l.size[0] for l in lines),
                avail_h / sum(l.size[1] for l in lines))
    lines = [l.resize((max(1, round(l.size[0] * scale)),
                       max(1, round(l.size[1] * scale))), Image.LANCZOS) for l in lines]

    tile = Image.new("RGB", (SIZE, SIZE), bg)
    y = (SIZE - (sum(l.size[1] for l in lines) + gap * (len(lines) - 1))) // 2
    for l in lines:
        tile.paste(l, ((SIZE - l.size[0]) // 2, y))
        y += l.size[1] + gap
    return tile


for spec in LOGOS:
    im = Image.open(SRC / spec["src"]).convert("RGB")
    if spec["mode"] == "crop":
        tile = crop_square(im)
    else:
        tile = stack_words(im, spec["band"], spec["bg"], spec["pad"], spec["gap"])
    tile.save(OUT / spec["out"], optimize=True)
    print(f"{spec['out']:<20} <- {spec['src']}")
