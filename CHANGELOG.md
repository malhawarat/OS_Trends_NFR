# Changelog

## 1.2.0 — 2026-10-03

Corrections and additions following a pre-submission review of the manuscript by six colleagues, and a full re-verification of every reported figure against its primary source. Three of these changes correct statements in earlier releases; they are listed first and in full, because anyone who read release 1.0.0 or 1.1.0 should know what changed.

### Corrections

**The Copilot corpus is mobile-app data, not Windows.** Releases 1.0.0 and 1.1.0 described `03_Usability/Copilot_Quantitative_Analysis/` as the Windows result and its 64.8% positive share as a Windows platform estimate. That was wrong. The Chhetri et al. (2025) corpus studies AI-powered *mobile* apps, and its Copilot rows carry the Android package identifiers `com.microsoft.copilot` and `com.microsoft.office.officehubrow`. The figure is now reported as a reference point for a voluntarily installed vendor assistant, is not comparable with the Apple and HarmonyOS estimates, and is not ranked against them. This study collected no user-sentiment data for Windows. Folder and file names are unchanged for link stability; the documentation inside them is corrected.

**The security/privacy inter-rater agreement was overstated.** Earlier releases reported κ = 0.81 with 87.0% raw agreement across all 108 rubric cells. Thirty-six of those cells are not-applicable for both raters because the platform did not exist at that time point, and agreement on them is automatic. The primary figure is now agreement on the 72 **assessable** cells: 58/72 = 80.6% raw, κ = 0.62, linear-weighted κ<sub>w</sub> = 0.69. The underlying scores are unchanged; only the summary statistic was wrong. The 108-cell figure is retained for completeness and clearly labelled.

**The three-method triangulation claim is withdrawn.** Earlier documentation described the "Forced Copilot integration" theme as one of three independent sources corroborating a consent-and-control finding, and the preliminary qualitative pass as another. That framing overstated what the evidence supports. The qualitative pass had no sampling frame, no query record, no second rater and no coding scheme. The Copilot theme is heterogeneous and comes from a mobile application, so it cannot corroborate a claim about the Windows shell. Measured directly against the raw corpus, imposition vocabulary appears in 72 of 7,104 negative phrases (1.0%), not the 1.9% the cluster size suggests. The consent finding now rests on the structured AI-reliability protocol, where it is measured rather than observed.

### Changes

- Title updated throughout to *"Evaluating User Sentiment, Security, and AI Reliability Across Modern Operating Systems"*. The NFR 1 construct is named user sentiment rather than usability: it is the positive share of expressed opinions, which bears on satisfaction and does not measure task success, efficiency, or error rates.
- `README.md`, `README_details.txt`, `CITATION.cff` and the Copilot provenance note updated for all of the above.
- The stale limitation about HarmonyOS theme shares being pre-validation was removed; they were re-derived from the 302 human-validated posts in release 1.1.0.

### Additions

- `verify_copilot_figures.py` — reproduces every Copilot number in the paper directly from the two Chhetri et al. parquet files, including the package-identifier provenance check and the imposition-vocabulary counts. Asserts each value and exits non-zero on mismatch.
- `03_Usability/Apple_HarmonyOS_Analysis/results/platform_comparison_sensitivity.csv` — the Apple–HarmonyOS comparison under four variants (main pair-level; YouTube-only, which removes the source confound; post-level with pipeline labels; post-level with the authors' own blind labels), each with cluster-bootstrap intervals for both platforms and for the difference itself. The difference excludes zero under all four.
- `03_Usability/Apple_HarmonyOS_Analysis/figures/fig_usability_forest.png` — replaced. The Copilot row is now separated under a "reference point" heading rather than appearing as the top row of a ranking, and the new sensitivity variants are included.

## 1.1.0 — 2026-10-02

HarmonyOS themes re-derived from the 302 human-validated posts (12 positive and 3 negative merged themes), replacing the pre-validation version in 1.0.0. Adds the validated-themes notebook, results and dendrogram.

## 1.0.0 — 2026-10-02

Initial release: AI-reliability test set and both raters' scores; security/privacy rubric with both raters' scores and reconciliation notes; Apple/HarmonyOS collection, labels, human validation and reproduction notebook; Copilot clustering outputs.
