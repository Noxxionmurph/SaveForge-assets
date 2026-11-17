# Pixel Remaster battle sprites for SaveForge's landing page tiles: the standing pose of Final Fantasy's Warrior, Final
# Fantasy II's Firion and Final Fantasy III's first Onion Knight, from The Spriters Resource's Pixel Remaster (PC)
# "Playable Characters" sheets. Each sheet is a grid of 32x32 cells on magenta lines, the background transparent, and
# the standing pose is the top-left cell of each character's block. All three come out in one 18x24 frame, cut from the
# same place in their cells, so their feet stay on one line and they keep their spacing.
# Usage: python3 scripts/extract-pr-tile-sprites.py FF1_SHEET FF2_SHEET FF3_SHEET sprites
import os
import sys
from PIL import Image

FRAME = (7, 8, 25, 32)  # left, top, right, bottom inside a cell
CUTS = [  # which sheet, the cell's top-left corner on it, where it goes
    (0, (1, 1), 'ff1/pr/warrior.png'),
    (1, (1, 1), 'ff2/pr/firion.png'),
    (2, (1, 1), 'ff3/pr/onion-knight.png'),
]
MAGENTA = (255, 0, 255, 255)

sheets = [Image.open(p).convert('RGBA') for p in sys.argv[1:4]]
out = sys.argv[4]
for k, (x, y), name in CUTS:
    sheet = sheets[k]
    # The cell must be one: magenta all round it.
    for i in range(34):
        for px in ((x - 1 + i, y - 1), (x - 1 + i, y + 32), (x - 1, y - 1 + i), (x + 32, y - 1 + i)):
            assert sheet.getpixel(px) == MAGENTA, (name, px)
    cell = sheet.crop((x, y, x + 32, y + 32))
    left, top, right, bottom = cell.getbbox()
    assert left >= FRAME[0] and top >= FRAME[1] and right <= FRAME[2] and bottom <= FRAME[3], (name, cell.getbbox())
    assert set(cell.getchannel('A').tobytes()) <= {0, 255}, name  # no half-transparent pixels
    sprite = cell.crop(FRAME)
    os.makedirs(os.path.dirname(f'{out}/{name}'), exist_ok=True)
    sprite.save(f'{out}/{name}', optimize=True)
    print(name, sprite.size)
