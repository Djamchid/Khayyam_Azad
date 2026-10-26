# Google Fonts readiness audit — 2026-10-26

Status: **NOT READY for Google Fonts onboarding**. The visual v0.4 is retained unchanged. This audit does not imply Google endorsement or acceptance.

## Inspected release
- `fonts/KhayyamAzad-Regular.ttf` (binary audited locally); WOFF2 also present.
- 1,141 glyphs; 284 encoded code points; `GSUB` and `GPOS` present; `ss01` absent.
- `OS/2.fsType = 0` (no embedding restriction).
- `head.fontRevision ≈ 0.400`.
- Font family name (name ID 1 and 16): **Khayyam Azad**; style **Regular**.
- **Inconsistent internal version/provenance**: name ID 0 says `Preview v0.1`, name ID 3 says `v0.2 2026`, name ID 5 says `Version 0.4 - stable rollback`. Other names still mention Monotype/Noto; preserve attributions pending verification.
- Basic ASCII coverage test (U+0020..U+007E): **incomplete**. Google Fonts' non-Latin minimum (GF Latin Kernel) must be checked before claiming compliance.
- Complete FontBakery Google Fonts profile **NOT run** in this audit: FontBakery was not installed in the execution environment. Earlier project-specific scripts are NOT a replacement.
- Full shaping proof and pixel comparison against baseline **NOT performed** for this audit.

## Major onboarding gaps
1. **Uniqueness / inclusion rationale**: The font is a minimally changed derivative of the existing Google Fonts family Noto Nastaliq Urdu. The Google Fonts team may prefer upstream fixes or reject duplicate-looking submissions.
2. **Authoritative editable sources**: TTX + a compiled base TTF is not equivalent to a native designer source (UFO/Glyphs/FontForge). Google Fonts asks for editor sources and a scalable/reproducible production chain.
3. **Licensing audit**: Check the actual upstream source and its OFL notices, all Reserved Font Names, naming metadata, and attribution consistency. The local OFL is an adaptation, not independently verified against a pinned upstream upstream commit.
4. **Metadata**: Version, copyright, contributors, designer and vendor records require a coherent cleanup, subject to preserving legal notices.
5. **QA**: FontBakery googlefonts profile, Persian shaping regression, web-browser proofs, glyph-outline inspection, mobile test, and Latin Kernel check.
6. **Process**: Open a Google Fonts issue before any PR, after the blocking items above are resolved.

## Recommended decision
**Keep v0.4 publicly available as an experimental derivative**, but do **not** submit as a distinct new Google Fonts family now. First discuss whether the improvements should be proposed upstream to Noto Nastaliq Urdu. No edits to the font binaries are proposed in this audit.

## Primary references
- https://googlefonts.github.io/gf-guide/onboarding.html
- https://googlefonts.github.io/gf-guide/requirements.html
- https://googlefonts.github.io/gf-guide/production.html
- https://googlefonts.github.io/gf-guide/upstream.html
- https://github.com/google/fonts/blob/main/CONTRIBUTING.md
- https://github.com/notofonts/nastaliq
