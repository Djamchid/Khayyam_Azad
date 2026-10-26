"""Low-risk Google Fonts fixes while preserving original glyphs and shaping."""
from pathlib import Path
from fontTools.ttLib import TTFont
for path in (Path('fonts/KhayyamAzad-Regular.ttf'),Path('fonts/KhayyamAzad-Regular.woff2')):
    f=TTFont(path)
    keep={k:f.getTableData(k) for k in ('glyf','GSUB','GPOS','GDEF','cmap','hmtx','loca')}
    n=f['name']
    for r in list(n.names):
        if r.nameID in (0,1,2,3,4,5,6,13,14,16,17):n.names.remove(r)
    entries={0:'Copyright 2026 The Khayyam Azad Project Authors (https://github.com/Djamchid/Khayyam_Azad)',1:'Khayyam Azad',2:'Regular',3:'1.000;KhayyamAzad-Regular',4:'Khayyam Azad Regular',5:'Version 1.000',6:'KhayyamAzad-Regular',13:'This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://openfontlicense.org',14:'https://openfontlicense.org/open-font-license-official-text/',16:'Khayyam Azad',17:'Regular'}
    for k,v in entries.items():
        n.setName(v,k,3,1,0x409)
        n.setName(v,k,1,0,0)
    f['head'].fontRevision=1.0
    f['head'].flags |= 1<<3
    os2=f['OS/2'];os2.fsSelection|=1<<7
    os2.usWinAscent=max(os2.usWinAscent,f['head'].yMax)
    os2.usWinDescent=max(os2.usWinDescent,-f['head'].yMin)
    f['hhea'].ascent=1500
    f['hhea'].descent=-500
    f['hhea'].lineGap=os2.sTypoLineGap
    f.save(path)
    g=TTFont(path)
    assert all(g.getTableData(k)==v for k,v in keep.items()),'Shaping or outlines unexpectedly changed'
    print(path,'fixed; glyph and shaping tables unchanged')
