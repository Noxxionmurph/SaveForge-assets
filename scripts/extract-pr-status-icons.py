# Pixel Remaster status icons for the Final Fantasy editors' party windows: the 10x10 condition icons (blind, poison, mini,
# toad, stone, silence, KO) from Final Fantasy's UI icon bundle in the Pixel Remaster (PC) game. Which icon is which was
# read off the pictures. Needs UnityPy and Pillow. Reads the game's files, writes only to the output folder.
# Usage: python3 scripts/extract-pr-status-icons.py "<steamapps/common>/FINAL FANTASY PR/FINAL FANTASY_Data/StreamingAssets/aa/StandaloneWindows64" sprites
import glob
import os
import sys
import UnityPy

NAMES = {'UI_Condition_Icon01': 'blind', 'UI_Condition_Icon03': 'poison', 'UI_Condition_Icon05': 'mini',
         'UI_Condition_Icon06': 'toad', 'UI_Condition_Icon07': 'stone', 'UI_Condition_Icon08': 'silence',
         'UI_Condition_Icon13': 'ko'}
src, out = sys.argv[1:3]
os.makedirs(f'{out}/ff-status', exist_ok=True)
done = 0
for bundle in sorted(glob.glob(f'{src}/ui_icons_assets_all_*.bundle')):
    for o in UnityPy.load(bundle).objects:
        if o.type.name == 'Sprite':
            spr = o.read()
            if spr.m_Name in NAMES:
                img = spr.image.convert('RGBA')
                assert img.size == (10, 10), spr.m_Name
                assert set(img.getchannel('A').tobytes()) <= {0, 255}, spr.m_Name  # no half-transparent pixels
                img.save(f'{out}/ff-status/{NAMES[spr.m_Name]}.png', optimize=True)
                done += 1
assert done == len(NAMES), done
print(done, 'icons')
