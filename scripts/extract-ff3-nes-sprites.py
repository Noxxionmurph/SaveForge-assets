# Final Fantasy III (Famicom) job sprites: each job's standing battle pose (the first 6 of the 42 tiles each job has at
# $8000 in bank $28, ROM offset 0x50010 + job * 0x2A0) in the battle palette the game gives that job, colour 0
# transparent. The Onion Kid's palette depends on the party member instead (members 1-4 use 0, 1, 2, 0), so it comes
# out three times: onion-kid.png, onion-kid-2.png, onion-kid-3.png. The tables are in bank $2E: palette per job at
# $9E4A, the three character palettes at entries $FC-$FE of the battle colour palettes at $8C00 (3 bytes each, colour 0
# is always black). The same in the English fan translation.
# Usage: python3 scripts/extract-ff3-nes-sprites.py "Final Fantasy III (Japan).nes" sprites/ff3/nes
import sys
from PIL import Image
# 2C02 palette (FCEUX default), as for the Final Fantasy I sprites
P=[0x747474,0x24188C,0x0000A8,0x44009C,0x8C0074,0xA80010,0xA40000,0x7C0800,0x402C00,0x004400,0x005000,0x003C14,0x183C5C,0,0,0,
0xBCBCBC,0x0070EC,0x2038EC,0x8000F0,0xBC00BC,0xE40058,0xD82800,0xC84C0C,0x887000,0x009400,0x00A800,0x009038,0x008088,0,0,0,
0xFCFCFC,0x3CBCFC,0x5C94FC,0xCC88FC,0xF478FC,0xFC74B4,0xFC7460,0xFC9838,0xF0BC3C,0x80D010,0x4CDC48,0x58F898,0x00E8D8,0x787878,0,0,
0xFCFCFC,0xA8E4FC,0xC4D4FC,0xD4C8FC,0xFCC4FC,0xFCC4D8,0xFCBCB0,0xFCD8A8,0xFCE4A0,0xE0FCA0,0xA8F0BC,0xB0FCCC,0x9CFCF0,0xC4C4C4,0,0]
rom=open(sys.argv[1],'rb').read(); out=sys.argv[2]
assert len(rom)==16+512*1024, 'expected a 512 KB iNES ROM'
at=lambda bank,cpu: 16+bank*0x2000+(cpu&0x1fff)
gfx=at(0x28,0x8000)
member_pal=list(rom[at(0x2E,0x9E4A):at(0x2E,0x9E4A)+4])
job_pal=list(rom[at(0x2E,0x9E4E):at(0x2E,0x9E4E)+22])
pals=[[0x0F]+list(rom[at(0x2E,0x8C00)+i*3:at(0x2E,0x8C00)+i*3+3]) for i in (0xFC,0xFD,0xFE)]
assert member_pal==[0,1,2,0] and pals[0]==[0x0F,0x36,0x30,0x16], (member_pal,pals)
names=('onion-kid fighter monk white-wizard black-wizard red-wizard archer knight thief scholar geomancer dragoon viking '
       'master magic-knight conjurer bard warlock shaman summoner sage ninja').split()
def tile(t):
    b=rom[t:t+16]; return [[((b[y]>>(7-x))&1)|(((b[y+8]>>(7-x))&1)<<1) for x in range(8)] for y in range(8)]
def sprite(job,pal):
    im=Image.new('RGBA',(16,24),(0,0,0,0)); px=im.load()
    for k in range(6):
        t=tile(gfx+job*0x2A0+k*16); ox=(k%2)*8; oy=(k//2)*8
        for y in range(8):
            for x in range(8):
                v=t[y][x]
                if v: rgb=P[pals[pal][v]]; px[ox+x,oy+y]=((rgb>>16)&255,(rgb>>8)&255,rgb&255,255)
    return im
for j,n in enumerate(names):
    if j==0:
        for p in range(3): sprite(0,p).save(f'{out}/onion-kid{"-%d"%(p+1) if p else ""}.png')
    else: sprite(j,job_pal[j]).save(f'{out}/{n}.png')
