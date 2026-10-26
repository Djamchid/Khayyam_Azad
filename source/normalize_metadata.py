"""Normalize font name metadata without altering outlines, metrics, cmap, GSUB or GPOS."""
from pathlib import Path
from fontTools.ttLib import TTFont

PATHS = [Path("fonts/KhayyamAzad-Regular.ttf"), Path("fonts/KhayyamAzad-Regular.woff2")]
FAMILY = "Khayyam Azad"
VERSION = "Version 0.401"
UNIQUE = "Khayyam Azad;0.401;2026"
COPYRIGHT = ("Copyright 2017 Google Inc. All Rights Reserved. "
             "Original Noto Nastaliq Urdu. Modified derivative Khayyam Azad 2026. "
             "See OFL.txt and PROVENANCE.md.")
for path in PATHS:
    font = TTFont(path)
    before = {tag: font.getTableData(tag) for tag in ("glyf", "cmap", "GSUB", "GPOS", "GDEF", "hmtx")}
    font["head"].fontRevision = 0.401
    name = font["name"]
    # Remove inconsistent previous localized previews; preserve trademark/vendor and attribution fields.
    for rec in list(name.names):
        if rec.nameID in (0, 1, 2, 3, 4, 5, 6, 16, 17):
            name.names.remove(rec)
    vals = {0: COPYRIGHT, 1: FAMILY, 2: "Regular", 3: UNIQUE,
            4: FAMILY, 5: VERSION, 6: "KhayyamAzad-Regular",
            16: FAMILY, 17: "Regular"}
    for ident, content in vals.items():
        name.setName(content, ident, 3, 1, 0x409)
        if ident != 0:
            name.setName(content, ident, 1, 0, 0)
    # Persian localization; preserve accurate Persian family naming, no 'preview'.
    for ident, content in ((1, "خیام آزاد"), (2, "عادی"), (4, "خیام آزاد"),
                           (16, "خیام آزاد"), (17, "عادی")):
        name.setName(content, ident, 3, 1, 0x429)
    font.save(path)
    check = TTFont(path)
    assert all(check.getTableData(tag) == data for tag, data in before.items()), path
    assert check["head"].fontRevision >= 0.400
    print("Metadata normalized; outlines and shaping identical:", path)
