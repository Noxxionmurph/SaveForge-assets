# Final Fantasy (NES, US) class sprites: each class's standing battle-sprite pose (tiles 0-5 of its 2 rows at $9000 in
# bank 9, lut_BatSprCHR in Disch's disassembly) in the palette lutClassBatSprPalette picks, colour 0 transparent.
# Usage: python3 scripts/extract-ff1-nes-sprites.py "Final Fantasy (USA).nes" sprites/ff1/nes
import sys
from PIL import Image
# 2C02 palette (FCEUX default)
P=[0x747474,0x24188C,0x0000A8,0x44009C,0x8C0074,0xA80010,0xA40000,0x7C0800,0x402C00,0x004400,0x005000,0x003C14,0x183C5C,0,0,0,
0xBCBCBC,0x0070EC,0x2038EC,0x8000F0,0xBC00BC,0xE40058,0xD82800,0xC84C0C,0x887000,0x009400,0x00A800,0x009038,0x008088,0,0,0,
0xFCFCFC,0x3CBCFC,0x5C94FC,0xCC88FC,0xF478FC,0xFC74B4,0xFC7460,0xFC9838,0xF0BC3C,0x80D010,0x4CDC48,0x58F898,0x00E8D8,0x787878,0,0,
0xFCFCFC,0xA8E4FC,0xC4D4FC,0xD4C8FC,0xFCC4FC,0xFCC4D8,0xFCBCB0,0xFCD8A8,0xFCE4A0,0xE0FCA0,0xA8F0BC,0xB0FCCC,0x9CFCF0,0xC4C4C4,0,0]
rom=open(sys.argv[1],'rb').read(); out=sys.argv[2]
base=16+9*0x4000+0x1000
pals=[[0x0F,0x28,0x18,0x21],[0x0F,0x16,0x30,0x36]]
classpal=[1,0,0,1,1,0,1,1,0,1,1,0]
names='warrior thief monk red-mage white-mage black-mage knight ninja master red-wizard white-wizard black-wizard'.split()
def tile(t):
    b=rom[t:t+16]; return [[((b[y]>>(7-x))&1)|(((b[y+8]>>(7-x))&1)<<1) for x in range(8)] for y in range(8)]
for c,n in enumerate(names):
    im=Image.new('RGBA',(16,24),(0,0,0,0)); px=im.load()
    pal=pals[classpal[c]]
    for k in range(6):
        t=tile(base+c*0x200+k*16); ox=(k%2)*8; oy=(k//2)*8
        for y in range(8):
            for x in range(8):
                v=t[y][x]
                if v: rgb=P[pal[v]]; px[ox+x,oy+y]=((rgb>>16)&255,(rgb>>8)&255,rgb&255,255)
    im.save(f'{out}/{n}.png')
