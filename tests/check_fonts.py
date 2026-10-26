from pathlib import Path
from fontTools.ttLib import TTFont
root = Path(__file__).resolve().parents[1]
for path in (root/'fonts/KhayyamAzad-Regular.ttf', root/'fonts/KhayyamAzad-Regular.woff2'):
    f=TTFont(path)
    assert 'GSUB' in f and 'GPOS' in f and 'GDEF' in f
    assert len(f.getGlyphOrder())>=1141
    assert 'ss01' not in {r.FeatureTag for r in f['GSUB'].table.FeatureList.FeatureRecord}
    cmap=f.getBestCmap()
    for char in 'پچژگکی':
        assert ord(char) in cmap, f'Missing Persian character: {char}'
    assert all(cp in cmap for cp in range(32,127)), 'ASCII Latin Kernel incomplete'
    assert f['head'].fontRevision>=1.0
    assert any(n.nameID==1 and n.toUnicode()=='Khayyam Azad' for n in f['name'].names)
    print(path.name,'OK —',len(f.getGlyphOrder()),'glyphs')
