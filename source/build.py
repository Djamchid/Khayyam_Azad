"""Rebuild v0.4 from its included v0.2 source baseline without ss01."""
from pathlib import Path
from fontTools.ttLib import TTFont
root = Path(__file__).resolve().parents[1]
font = TTFont(root / 'source/base-v02.ttf')
for n in font['name'].names:
    if n.nameID == 5:
        value = 'Version 0.4 - stable rollback'
        n.string = value.encode('utf-16-be' if n.isUnicode() else 'latin1')
font['head'].fontRevision = 0.4
out = root / 'build'
out.mkdir(exist_ok=True)
for suffix in ('ttf', 'woff2'):
    font.flavor = 'woff2' if suffix == 'woff2' else None
    font.save(out / f'KhayyamAzad-Regular.{suffix}')
print('Built v0.4 in build/')
