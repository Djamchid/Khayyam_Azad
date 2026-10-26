# FontBakery Google Fonts QA — 2026-10-26

## Latest verified run
- [GitHub Actions FontBakery report](https://github.com/Djamchid/Khayyam_Azad/actions/runs/40353885859)
- **236 executions: 101 PASS, 1 FAIL, 19 WARN, 7 INFO, 108 SKIP; no FATAL/ERROR.**
- Previous baseline: **12 FAIL, 10 WARN, 97 PASS**. Eleven of the original failures have been corrected.
- CI status: **failure**, correctly reflecting the last unresolved check. Do **not** advertise Google Fonts certification or full technical compliance yet.

## Resolved
- Misleading/version-mixed metadata and full name records.
- OFL 1.1 license metadata and URL; preserved upstream copyright.
- TrueType hinted flag, Windows vertical bounds, `USE_TYPO_METRICS` and hhea/OS2 consistency.
- GF Latin Core glyph coverage: licensed Latin characters imported from Noto Sans; the entire ASCII Latin Kernel included.
- Case-mapping pairs, nested Latin composite glyphs, own-name rendering.

## Still failing: `googlefonts/glyphsets/shape_languages`
The Unicode repertoire triggers shaping expectations for Latin combinations and other language orthographies. The imported Latin combining marks do not yet have correct production-quality GPOS attachment behavior. The original Persian/Urdu layout must not be compromised by an overly broad automatic substitution. The attempted generated `mark` GPOS lookup was rolled back after it introduced a new `dotted_circle` failure without resolving the language-shaping check. Real language-specific shaping support and visual review are still required; **do not suppress the failing check**.

## Reproducibility
- `python source/build.py` reconstructs the improved TTF/WOFF2 from `source/base-v02.ttf` using `source/fix_googlefonts.py` and `source/add_latin.py`.
- `source/add_latin_marks.py` is an **experimental, inactive prototype**; not part of the release build.
- The Persian glyph outline source is the same v0.4/v0.2 baseline; Latin glyphs are sourced from [Noto Sans](https://github.com/notofonts/noto-fonts) under SIL OFL 1.1. The original Persian GSUB/GPOS behavior is preserved.
- Run `python tests/check_fonts.py` and inspect `.github/workflows/googlefonts-qa.yml` for the complete QA.

## Remaining onboarding items
Besides the one FAIL, the current 19 WARN items and production-grade native editable design-source expectations should be reviewed with the Google Fonts team. The project remains a derivative of Noto Nastaliq Urdu.
