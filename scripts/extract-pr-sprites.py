# Pixel Remaster battle sprites for the Final Fantasy I, II and III editors' party windows: the standing pose ("Default_00")
# of every class (I), every playable character (II) and every job (III, plus each hero's Onion Knight), read from the
# Pixel Remaster (PC) games' own character bundles (bc_ff<n>_pNNN, bc_ff3_p022_c00 ... c03). Which file is who comes from
# each game's character_asset, job and message tables. Every sprite is cut from the same place in its 32x32 cell, 19x25,
# so the feet stay on one line and all three games share one frame. Needs UnityPy and Pillow. Reads the games' files,
# writes only to the output folder.
# Usage: python3 scripts/extract-pr-sprites.py "<steamapps/common folder holding the three FINAL FANTASY ... PR folders>" sprites
import glob
import os
import re
import sys
import UnityPy

FRAME = (7, 7, 26, 32)  # left, top, right, bottom inside the cell
GAMES = {
    'ff1': ('FINAL FANTASY PR/FINAL FANTASY_Data', {
        'p001': 'warrior', 'p002': 'thief', 'p003': 'monk', 'p004': 'red-mage', 'p005': 'white-mage', 'p006': 'black-mage',
        'p007': 'knight', 'p008': 'ninja', 'p009': 'master', 'p010': 'red-wizard', 'p011': 'white-wizard', 'p012': 'black-wizard'}),
    'ff2': ('FINAL FANTASY II PR/FINAL FANTASY II_Data', {
        'p001': 'firion', 'p002': 'maria', 'p003': 'guy', 'p004': 'minwu', 'p005': 'josef', 'p006': 'leila', 'p007': 'gordon',
        'p008': 'ricard', 'p009': 'leon', 'p010': 'scott'}),
    'ff3': ('FINAL FANTASY III PR/FINAL FANTASY III_Data', {
        'p001': 'warrior', 'p002': 'thief', 'p003': 'monk', 'p004': 'red-mage', 'p005': 'white-mage', 'p006': 'black-mage',
        'p007': 'knight', 'p008': 'ninja', 'p009': 'black-belt', 'p010': 'sage', 'p011': 'devout', 'p012': 'magus',
        'p013': 'ranger', 'p014': 'scholar', 'p015': 'geomancer', 'p016': 'dragoon', 'p017': 'viking', 'p018': 'bard',
        'p019': 'dark-knight', 'p020': 'evoker', 'p021': 'summoner',
        'p022_c00': 'onion-knight-0', 'p022_c01': 'onion-knight-1', 'p022_c02': 'onion-knight-2', 'p022_c03': 'onion-knight-3'}),
}
common, out = sys.argv[1:3]
for game, (folder, files) in GAMES.items():
    os.makedirs(f'{out}/{game}/pr/jobs', exist_ok=True)
    done = 0
    for bundle in sorted(glob.glob(f'{common}/{folder}/StreamingAssets/aa/StandaloneWindows64/bc_{game}_p*_assets_all_*.bundle')):
        found = re.match(rf'bc_{game}_(p\d+(?:_c\d+)?)_assets_all', os.path.basename(bundle))
        key = found and found.group(1)
        if key not in files:
            continue
        for o in UnityPy.load(bundle).objects:
            if o.type.name == 'Texture2D':
                tex = o.read()
                if tex.m_Name == 'Default_00':
                    cell = tex.image.convert('RGBA')
                    assert cell.size == (32, 32), key
                    left, top, right, bottom = cell.getbbox()
                    assert left >= FRAME[0] and top >= FRAME[1] and right <= FRAME[2] and bottom <= FRAME[3], (game, key, cell.getbbox())
                    assert set(cell.getchannel('A').tobytes()) <= {0, 255}, key  # no half-transparent pixels
                    cell.crop(FRAME).save(f'{out}/{game}/pr/jobs/{files[key]}.png', optimize=True)
                    done += 1
    assert done == len(files), (game, done)
    print(game, done, 'sprites')
