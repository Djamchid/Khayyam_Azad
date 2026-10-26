# Khayyam Azad — Google Fonts submission text (draft)
## Project
Khayyam Azad (خیام آزاد) is a Persian nasta'liq font for readable editions of Khayyam's quatrains.

Repository: https://github.com/Djamchid/Khayyam_Azad

## Derivative status
Khayyam Azad derives from Noto Nastaliq Urdu; it is not a newly designed original typeface. Copyright attribution to Google and the upstream Noto designers is retained. License: SIL OFL 1.1, upstream reserved font names and provenance require review.

## Current technical status (2026-10-26)
- Metadata corrected in released TTF and WOFF2 (version 0.401) with outlines/cmap/GSUB/GPOS/GDEF/hmtx unchanged; commit 99c0b9185ced399eeebbd9a536b6bc9d83c0332a.
- Google Fonts FontBakery profile run on GitHub Actions: 236 checks, 97 PASS, 12 FAIL, 10 WARN, 7 INFO, 110 SKIP.
- Failing checks: `family/win_ascent_and_descent`, `integer_ppem_if_hinted`, `googlefonts/glyphsets/shape_languages`, `googlefonts/font_copyright`, `googlefonts/license/OFL_copyright`, `googlefonts/name/license`, `googlefonts/font_names`, `googlefonts/glyph_coverage`, `googlefonts/name/version_format`, `googlefonts/render_own_name`, `googlefonts/use_typo_metrics`, `googlefonts/vertical_metrics`.
- Latin Kernel: 68 of 95 printable ASCII codepoints not encoded. The Google Fonts guide specifies GF Latin Kernel for non-Latin fonts, and the new-font onboarding guide requires GF Latin Core. No compliance claim is made.
- Source files: editable OpenType XML (TTX) and compiled baseline. Native UFO/Glyphs files and a scalable build chain have not been supplied yet.
- FontBakery run: https://github.com/Djamchid/Khayyam_Azad/actions/runs/40308044423

## Request
Please evaluate whether Khayyam Azad can be considered as a distinct OFL family despite its derivation from an existing catalog font; whether the project merits any exception to source and character coverage requirements; or whether merging changes into upstream Noto is the appropriate course. The project owner is prepared to resolve documented QA issues before onboarding. This document is a request for review and does not claim the font is technically ready for acceptance.
