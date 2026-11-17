# Credits

SaveForge is an unofficial, free, non-commercial fan tool. It is not affiliated with or endorsed by Nintendo,
Game Freak, Creatures Inc. or Square Enix. Pokémon and Final Fantasy, and everything that belongs to them, are theirs.

The pictures are not part of this code repository. They live in a separate repository,
[SaveForge-assets](https://github.com/Noxxionmurph/SaveForge-assets), and the site loads them from there, so the editor works
the same (without the pictures) if they are ever removed. This is who made them.

## Pokémon, item and type icons

From **PokéSprite** by msikma (https://github.com/msikma/pokesprite), copied unchanged except for renaming the
Pokémon files to their National Dex number (and Unown's other letters to `201-<letter>.png`, with `!` and `?` as
`201-exclamation.png` and `201-question.png`). The shiny icons in `sprites/pokemon/shiny/` are PokéSprite's own shiny versions of the same icons. PokéSprite's own code is MIT licensed; the artwork is not covered by that
licence.

## The ??? type icon

`sprites/types/unknown.png` (the ??? type, Curse's in Gen 2) is drawn for this repository in the style of PokéSprite's
Gen 8 type icons, which have none for it: a circle in ???'s teal with a white question mark, in the Inter Display font.
`scripts/make-unknown-type.py` redraws it.

## Type labels

`sprites/type-labels/<type>.png` (each type's name in its coloured box, 32x16) are Pokémon Emerald's own summary screen
labels, from the pret/pokeemerald disassembly (https://github.com/pret/pokeemerald, `graphics/types/`), in the colours
the game gives them, with the background made transparent and renamed to the editor's type names (`fight` to `fighting`,
`mystery` to `unknown`). Gen 1 and Gen 2 have no coloured type labels of their own. `scripts/extract-type-labels.py`
redoes them.

## Shiny mark

`sprites/marks/shiny.svg` is the two-sparkle shiny mark from Pokémon Sword and Shield's summary screen (used by the
games since), traced by hand as a vector shape in the game's colour.

## Gym badges

The eight Kanto badges (`sprites/badges/1.png` to `8.png`) are cut from the Red/Blue "Trainer Card" sheet on The Spriters Resource
(https://www.spriters-resource.com/game_boy_gbc/pokemonredblue/asset/8733/, ripped by FrenchOrange), using the Super
Game Boy colour panel. `scripts/extract-badges.py` redoes the cut.

The eight Johto badges (`sprites/badges/johto/1.png` to `8.png`, Zephyr to Rising) are Gold and Silver's own trainer card
badges, from the pret/pokegold disassembly (https://github.com/pret/pokegold, `gfx/trainer_card/badges.png`), in the
colours the game gives them on a Game Boy Color (its badge palette). `scripts/extract-johto-badges.py` redoes them.

The eight Hoenn badges (`sprites/badges/hoenn/1.png` to `8.png`, Stone to Rain) are Ruby, Sapphire and Emerald's own
trainer card badges, from the pret/pokeemerald disassembly (https://github.com/pret/pokeemerald,
`graphics/trainer_card/badges.png`), in the sheet's own colours (the games show them in silver), with the background
made transparent. SaveForge's `scripts/extract-hoenn-badges.py` redoes them.

The eight Kanto badges FireRed and LeafGreen show (`sprites/badges/frlg/1.png` to `8.png`, Boulder to Earth) are their
own trainer card badges, from the pret/pokefirered disassembly (https://github.com/pret/pokefirered,
`graphics/trainer_card/badges.png`), treated the same way (`scripts/extract-hoenn-badges.py <dir> frlg`).

## Battle Frontier symbols

Emerald's seven Battle Frontier symbols (`sprites/frontier/silver-1.png` to `silver-7.png` and `gold-1.png` to
`gold-7.png`, Tower to Pyramid) are the Frontier Pass's own symbols, from the pret/pokeemerald disassembly
(`graphics/frontier_pass/medals.png`), in the silver and gold palettes the game loads for them (`silver.pal`,
`gold.pal`), with the background made transparent. SaveForge's `scripts/extract-frontier-symbols.py` redoes them.

## Gen 3 ribbons

The 32 Gen 3 ribbons (`sprites/ribbons/gen3/0.png` to `31.png`, numbered like the games' ribbon ids: 0 Champion,
1-20 the Cool, Beauty, Cute, Smart and Tough contest ribbons from Normal to Master Rank, 21-24 Winning, Victory, Artist
and Effort, 25-31 Marine to World) are the PokéNav's own 32x32 ribbon pictures, from the pret/pokeemerald disassembly
(`graphics/pokenav/ribbons/icons_big.png`), each in the palette the game gives it (`icons1.pal` to `icons5.pal`), with
the background made transparent. SaveForge's `scripts/extract-gen3-ribbons.py` redoes them.

## Final Fantasy class sprites and portraits

`sprites/ff1/nes/<class>.png` (16x24) are each class's standing pose from Final Fantasy (NES, US): the battle sprite tiles
at $9000 in bank 9 (`lut_BatSprCHR` in Disch's disassembly, https://github.com/Entroper/FF1Disassembly) in the palette
the game gives that class, with colour 0 transparent. `scripts/extract-ff1-nes-sprites.py` redoes them from the ROM.

`sprites/ff1/psp/<class>.png` (48x42) are the party pictures from Final Fantasy (PSP, US) as its load screen draws them,
taken from the game running in PPSSPP: three screens of the same window with different classes, so the window's own
pixels could be told apart from the sprites, with the drop shadow left out.

`sprites/ff1/gba/<class>.png` (26x24) are the party pictures from Final Fantasy I & II: Dawn of Souls (GBA, US) as its
load screen draws them, taken from the game running in mGBA with a save whose three files hold all twelve classes.
The window behind them is one colour per row, so every pixel that differs from its row's colour is the sprite.

`sprites/ff1/wsc/<class>.png` (26x24) are the party pictures from Final Fantasy (WonderSwan Color, Japan) as its main
menu draws them, taken from the game running in Mednafen's WonderSwan core with a save whose four characters were set to
each of the twelve classes in turn. The window behind them is one flat colour, so every pixel that differs from it is the
sprite.

`sprites/ff2/gba/<character>.png` (28x28) are the menu portraits from Final Fantasy II in the same Dawn of Souls
cartridge (Firion, Maria, Guy, Minwu, Josef, Gordon, Leila, Ricard), taken from its party menu in mGBA the same way.

`sprites/ff2/gba/battle/firion.png` (26x24, the same frame as the Final Fantasy I ones) is Firion's battle sprite from that
Final Fantasy II, standing in the party line: his sprite tiles and palette read out of video memory during a battle in
mGBA, with colour 0 transparent.

`sprites/ff2/nes/<character>.png` (24x32) are the menu portraits from Final Fantasy II on the Famicom (Firion, Maria,
Guy, Minwu, Josef, Gordon, Leila, Ricard, Leon): their tiles read out of the cartridge (11 portraits of 3x4 tiles from
ROM offset 0x24010) and coloured to match the party menu as the game draws it.

`sprites/ff2/wsc/<character>.png` (28x28) are the menu portraits from Final Fantasy II on the WonderSwan Color
(Firion, Maria, Guy, Minwu, Josef, Gordon, Leila, Ricard, Leon), taken from its party menu in Mednafen's WonderSwan core
with a save whose first character was set to each of them in turn.

`sprites/ff2/psp/<character>.png` (52x60) are the menu portraits from Final Fantasy II Anniversary Edition on the PSP
(Firion, Maria, Guy, Leon, Minwu, Josef, Gordon, Leila, Ricard, Scott): the `ff2_face_*` pictures in the disc's data
archive, unpacked (SSZL, a plain LZSS), drawn from their 16x16 tiles with the palette stored beside each one, colour 0
transparent.

`sprites/ff3/nes/<job>.png` (16x24) are each job's standing battle pose from Final Fantasy III on the Famicom (the
first 6 of the 42 tiles each job has at ROM offset 0x50010) in the battle palette the game gives that job, colour 0
transparent. The Onion Kid's palette goes by party member instead, so it is there three times (`onion-kid.png` for the
first and fourth members, `onion-kid-2.png`, `onion-kid-3.png`). Checked against the game running in an emulator: the
tiles and palettes are the ones a battle shows. `scripts/extract-ff3-nes-sprites.py` redoes them from the ROM.

`sprites/ff1/pr/warrior.png`, `sprites/ff2/pr/firion.png` and `sprites/ff3/pr/onion-knight.png` (18x24, one frame for
all three) are the standing battle poses of Final Fantasy's Warrior, Final Fantasy II's Firion and Final Fantasy III's
first Onion Knight from the Pixel Remasters, for the landing page tiles. They are cut from the "Playable Characters"
sheets for the Pixel Remasters (PC) on The Spriters Resource (for example
https://www.spriters-resource.com/pc_computer/finalfantasy3pixelremaster/), where each sheet's page names who ripped it.
`scripts/extract-pr-tile-sprites.py` redoes the cut.

`sprites/ff1/pr/jobs/<class>.png`, `sprites/ff2/pr/jobs/<character>.png` and `sprites/ff3/pr/jobs/<job>.png` (19x25, one
frame for all) are the standing battle poses of all twelve Final Fantasy classes, all ten Final Fantasy II characters and
all 21 Final Fantasy III jobs plus the four heroes' Onion Knights (`onion-knight-0.png` to `-3.png`, Luneth to Ingus),
for every editor's party window. They are the "Default_00" frames in the Pixel Remaster (PC) games' own character files,
which the games' tables tie to the class, character and job names. Only these frames are kept, not the games' files.
`scripts/extract-pr-sprites.py` redoes the cut from installed copies.

## Pikachu's reactions

`sprites/pikachu.png` (two 40x40 frames for each of the 18 ways your Pokémon Yellow starter reacts when you talk to it,
one reaction per row) holds Pokémon Yellow's own pictures in the Super Game Boy colours. They are cut from the
"Pikachu's moods" sheet on Serebii (https://www.serebii.net/yellow/pikachu.shtml), which is built from the game's
graphics. `scripts/extract-pikachu.py` redoes the cut. Frames that also exist in the pret/pokeyellow disassembly
(https://github.com/pret/pokeyellow, `gfx/pikachu/`) are pixel-identical to it, which is how each row was matched to
the game's name for it.

## Game data

Save layouts and tables were worked out with the help of the pret disassemblies
([pokered](https://github.com/pret/pokered), [pokeyellow](https://github.com/pret/pokeyellow)) and checked against
cartridge dumps the author owns (`scripts/verify-against-rom.mjs`; nothing from the ROMs is stored in this repository).

All the artwork is © Nintendo / Creatures Inc. / GAME FREAK Inc.

## Gen 3 Pokéblocks

The 14 Pokéblock colours (`sprites/pokeblocks/1.png` to `14.png`, numbered like the colour a save stores: 1 Red ...
14 Gold) are the 8x8 Pokéblock from the pret/pokeemerald disassembly (`graphics/pokeblock/pokeblock.png`), in each of
the palettes the game uses for it (`red.pal` to `gold.pal`), with the background made transparent. SaveForge's
`scripts/extract-pokeblocks.py` redoes them.

## Window frames

The frames the games' OPTION menu offers under FRAME (`sprites/frames/`, numbered like the menu's TYPE 1, TYPE 2 ...)
are each laid out as 3x3 tiles of 8x8 (corners, edges and a middle the games never draw). Gold, Silver and Crystal
share eight: the six 1bpp tiles of the pret/pokecrystal disassembly's `gfx/frames/1.png` to `8.png` (identical in
pret/pokegold), with the top and bottom edge both the game's ─ tile and both sides its │ tile, as the game draws them,
in black on transparent so the editor can draw them in the window's own colours. Ruby and Sapphire's twenty are
pret/pokeruby's `graphics/text_window/1.png` to `20.png`, and Emerald's (nine of them redrawn) pret/pokeemerald's, in
the colours the GBA shows, as are FireRed and LeafGreen's ten (pret/pokefirered's `graphics/text_window/`), with colour 0 (which the game leaves see-through) made transparent. SaveForge's
`scripts/extract-frames.py` redoes them.

## Secret bases

The secret base pictures (`sprites/secret-bases/`) come from the pret/pokeemerald disassembly. `red_cave.png`,
`brown_cave.png`, `blue_cave.png`, `yellow_cave.png`, `tree.png` and `shrub.png` are every metatile of the secret base
tileset (`data/tilesets/secondary/secret_base/metatiles.bin`, which the rooms and the decorations share), drawn from the
primary secret base tiles and that kind's own tiles and palettes, 16 to a row. `dolls/<decoration id>.png` are the
dolls and cushions, which the game shows as sprites: the first frame of each one's picture in
`graphics/object_events/pics/` in its object palette, with colour 0 made transparent. SaveForge's
`scripts/extract-secret-bases.py` redoes them.
