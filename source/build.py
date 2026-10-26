"""Rebuild Khayyam Azad v1.000 from the preserved v0.2 baseline, without ss01."""
from pathlib import Path
from shutil import copy2
from tempfile import TemporaryDirectory
from subprocess import run
from fontTools.ttLib import TTFont
import sys

root=Path(__file__).resolve().parents[1]
out=root/'build'
out.mkdir(exist_ok=True)
with TemporaryDirectory() as tmp:
    d=Path(tmp)
    (d/'fonts').mkdir()
    ttf=d/'fonts/KhayyamAzad-Regular.ttf'
    copy2(root/'source/base-v02.ttf',ttf)
    font=TTFont(ttf)
    font.flavor='woff2'
    font.save(d/'fonts/KhayyamAzad-Regular.woff2')
    run([sys.executable,str(root/'source/fix_googlefonts.py')],cwd=d,check=True)
    run([sys.executable,str(root/'source/add_latin.py')],cwd=d,check=True)
    for name in ('KhayyamAzad-Regular.ttf','KhayyamAzad-Regular.woff2'):
        copy2(d/'fonts'/name,out/name)
        print('Built',out/name)
