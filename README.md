# Khayyam Azad — v1.000 engineering release (v0.4 Persian outlines)

**خیام آزاد** — A Persian Nastaliq font experiment, derived from **Noto Nastaliq Urdu**. This is **not an original typeface**. The Persian outlines retain the visually approved v0.4/v0.2 design, with the experimental `ss01` substitutions removed. v1.000 corrects naming and technical metrics and supplements the Latin Core character set from OFL-licensed Noto Sans.

## Files
- `fonts/KhayyamAzad-Regular.woff2` — web font (unchanged v0.4 binary)
- `fonts/KhayyamAzad-Regular.ttf` — desktop font (unchanged v0.4 binary)
- `source/base-v02.ttf` and `source/base-v02.ttx` — baseline plus editable OpenType table XML (TTX); this is not a native, hand-designed Glyphs/FontForge source project.
- `source/build.py` — repeatable generation from the included baseline, preserving the v0.4 shaping data
- `docs/` — example and previous screenshot specimens
- `OFL.txt` — upstream license and notices, which must be retained

## Install on your site
```css
@font-face {
  font-family: 'Khayyam Azad';
  src: url('/fonts/KhayyamAzad-Regular.woff2') format('woff2');
  font-style: normal;
  font-weight: 400;
  font-display: swap;
}
.poem-fa { font-family: 'Khayyam Azad', serif; direction: rtl; line-height: 2.6; }
```
Add `<p class="poem-fa" lang="fa" dir="rtl">...</p>`.

## Build and verify
```bash
python -m pip install -r requirements.txt
python source/build.py
python tests/check_fonts.py
```
`source/build.py` generates TTF and WOFF2 from the included base-v02.ttf using metadata repairs and Noto Sans Latin import. Note that WOFF2 compression can be non-byte-identical across tool versions; the shaping and outline equivalence tests are more meaningful.

## Origin and attribution
Base Noto Nastaliq Urdu. Khayyam Azad is a modified derivative, preserving Google and other original credits where present. The font is offered under the SIL OFL 1.1; see `OFL.txt`. The historic project was tested with 16 Khayyam quatrains. Licensing and reserved names need final upstream audit before a formal Google Fonts proposal.

## Google Fonts submission — IMPORTANT
This package is prepared for a **public GitHub repository**, not accepted into Google Fonts. Because its design mostly overlaps an existing Google Fonts family, a standalone submission may be rejected. Review upstream contribution first. The [latest FontBakery test](FONTBAKERY_STATUS_2026-10-26.md) has **1 FAIL and 19 WARN** (101 PASS). The package is **not yet compliant with all Google Fonts submission requirements** (native original outlines/source history, attribution audit, FontBakery review, differentiation). Do not represent it as Google-approved or fully original.

See `SUBMISSION.md` and `PROVENANCE.md`.
