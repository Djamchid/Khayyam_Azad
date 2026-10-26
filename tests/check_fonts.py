from pathlib import Path
from fontTools.ttLib import TTFont
root = Path(__file__).resolve().parents[1]
for path in (root/'fonts/KhayyamAzad-Regular.ttf', root/'fonts/KhayyamAzad-Regular.woff2'):
    font = TTFont(path)
    assert 'GSUB' in font and 'GPOS' in font
    assert len(font.getGlyphOrder()) == 1141
    assert 'ss01' not in {r.FeatureTag for r in font['GSUB'].table.FeatureList.FeatureRecord}
    for c in 'پچژگکی':
        assert ord(c) in font.getBestCmap(), f'Missing character: {c}'
    print(path.name, 'OK')
