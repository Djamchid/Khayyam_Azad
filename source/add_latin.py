"""Add GF Latin Core characters from Noto Sans (SIL OFL 1.1) without changing Persian glyphs."""
from fontTools.ttLib import TTFont
from copy import deepcopy
from pathlib import Path
from urllib.request import urlretrieve

URL = 'https://raw.githubusercontent.com/notofonts/noto-fonts/main/hinted/ttf/NotoSans/NotoSans-Regular.ttf'
TMP = Path('/tmp/khayyam-noto-sans-donor.ttf')
if not TMP.exists():
    urlretrieve(URL, TMP)
donor = TTFont(TMP)
assert donor['head'].unitsPerEm == 1000

def valid(cp):
    return (0x20<=cp<=0x024F or 0x1E00<=cp<=0x1EFF or
            0x2000<=cp<=0x218F or 0x2C60<=cp<=0x2C7F or
            0xA720<=cp<=0xA7FF or cp in (0x25CC,0x2212,0xFB01,0xFB02))

def enrich(path):
    font=TTFont(path)
    assert font['head'].unitsPerEm == donor['head'].unitsPerEm
    # Binary-equality check of the Persian features and original cmap mappings.
    baseline={k:font.getTableData(k) for k in ('GSUB','GPOS','GDEF')}
    glyph_order=list(font.getGlyphOrder())
    orig_map=dict(font.getBestCmap())
    existing=set(glyph_order)
    cache={}
    def copy_glyph(name):
        if name in cache:
            return cache[name]
        renamed='kaLatin_'+name
        if renamed in existing:
            cache[name]=renamed
            return renamed
        glyph=deepcopy(donor['glyf'][name])
        cache[name]=renamed
        if glyph.isComposite():
            for part in glyph.components:
                part.glyphName=copy_glyph(part.glyphName)
        font['glyf'][renamed]=glyph
        font['hmtx'][renamed]=donor['hmtx'][name]
        glyph_order.append(renamed)
        existing.add(renamed)
        return renamed
    added={}
    for cp,name in donor.getBestCmap().items():
        if cp not in orig_map and valid(cp):
            added[cp]=copy_glyph(name)
    for table in font['cmap'].tables:
        if table.isUnicode():
            table.cmap.update({cp:g for cp,g in added.items()
                               if cp<=0xFFFF or table.format in (12,13)})
    font.setGlyphOrder(glyph_order)
    font['glyf'].glyphOrder=glyph_order
    print('Glyph order',len(glyph_order),'glyph table',len(font['glyf'].glyphs))
    assert len(glyph_order)==len(font['glyf'].glyphs), 'Glyph order mismatch'
    font['maxp'].numGlyphs=len(glyph_order)
    font.save(path)
    final=TTFont(path)
    assert all(final.getTableData(k)==v for k,v in baseline.items())
    assert all(final.getBestCmap().get(cp)==g for cp,g in orig_map.items())
    assert all(cp in final.getBestCmap() for cp in range(32,127))
    print('Added',len(added),'Latin codepoints to',path)
    return final

f=enrich('fonts/KhayyamAzad-Regular.ttf')
f.flavor='woff2'
f.save('fonts/KhayyamAzad-Regular.woff2')
