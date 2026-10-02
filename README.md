# When Convenience Meets Risk: Replication Package

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23098900.svg)](https://doi.org/10.5281/zenodo.23098900)

Replication package for **"When Convenience Meets Risk: Evaluating User Sentiment, Security, and AI Reliability Across Modern Operating Systems"** by Mohammad Alhawarat and Qasem Nijem (Al-Ahliyya Amman University), submitted to *Empirical Software Engineering*.

The study maps operating-system evolution (2015–2026) onto three non-functional requirements (user sentiment toward AI features, security/privacy, and AI reliability/trustworthiness) across Apple/iOS, HarmonyOS, Fuchsia, and Windows.

> **Note on folder names.** Folders are named `03_Usability/...` for link and DOI stability with earlier releases. The construct they hold is *user sentiment toward AI features* — the positive share of expressed opinions — which bears on the satisfaction facet of quality in use and does not measure task success, efficiency, or error rates. See the paper's Section 4.3.

## Key results

| NFR | Method | Main result |
|---|---|---|
| AI reliability | 80-item dual-rated test protocol on Windows Copilot | 82.5% accuracy overall [72.7, 89.3]; 55.0% on disclosure/consent [34.2, 74.2]; κ = 0.61 |
| Security/privacy | 9-criterion dual-rated documentary rubric, 3 time points | 2025/26: Apple 100%, Windows 94.4%, HarmonyOS 94.4%, Fuchsia 44.4%; κ = 0.62 on the 72 assessable cells (κ<sub>w</sub> = 0.69) |
| User sentiment | LLM aspect-sentiment analysis, cluster-robust, human-validated | Positive share: HarmonyOS 44.8% [36.4, 53.5] vs Apple Intelligence 23.4% [22.0, 24.9]; difference 21.3 pp [12.9, 30.0] |

Human validation of the sentiment pipeline: inter-rater κ = 0.896 (relevance) and 0.934 (sentiment).

**Two reporting points that matter for reading these numbers:**

- **The security/privacy κ.** Earlier releases reported κ = 0.81 with 87.0% raw agreement over all 108 cells. That figure is inflated: 36 of the 108 cells are not-applicable for both raters because the platform did not exist at that time point, and agreeing on those is automatic. The paper now reports agreement on the **72 assessable cells** as the primary figure: 58/72 = 80.6% raw, κ = 0.62, linear-weighted κ<sub>w</sub> = 0.69. The 108-cell figure is retained in the paper for completeness only.
- **The Copilot corpus is not Windows.** The Copilot slice of the Chhetri et al. (2025) corpus consists of reviews of the Microsoft Copilot and Microsoft 365 **mobile apps** — the rows carry the Android package identifiers `com.microsoft.copilot` and `com.microsoft.office.officehubrow`. Its 64.8% positive share [64.1, 65.6] is reported in the paper as a **reference point**, not as a platform estimate, and is not ranked against the two platform figures above. This study collected no user-sentiment data for Windows.

## Reproduce the results

**Apple/HarmonyOS sentiment.** Open [`03_Usability/Apple_HarmonyOS_Analysis/notebooks/Reproduce_Usability_Results.ipynb`](03_Usability/Apple_HarmonyOS_Analysis/notebooks/Reproduce_Usability_Results.ipynb) in Google Colab, set `BASE` to the `Apple_HarmonyOS_Analysis` folder, and run all cells. It recomputes every Apple/HarmonyOS number in the paper from the released files alone, with no API calls, in about a minute.

**Copilot figures.** Run [`verify_copilot_figures.py`](verify_copilot_figures.py) against the two Chhetri et al. parquet files (which must be requested from their authors — see below). It asserts every Copilot number in the paper, including the provenance package identifiers and the imposition-vocabulary counts, and exits non-zero on any mismatch.

**Security/privacy and AI reliability.** Both workbooks carry each rater's independent scores alongside the reconciled values, so every κ and every cell score can be recomputed directly; see [`README_details.txt`](README_details.txt).

## Contents

| Folder | What it holds |
|---|---|
| [`01_AI_Reliability/`](01_AI_Reliability) | Windows Copilot test set (80 prompts, ground truth, both raters' scores, reconciliation notes); Rater 1's independent scores for reproducing κ |
| [`02_Security_Privacy/`](02_Security_Privacy) | Security/privacy rubric: 108 cells with both raters' scores, evidence sources, reconciliation notes, and the auto-calculating trend table |
| [`03_Usability/Copilot_Quantitative_Analysis/`](03_Usability/Copilot_Quantitative_Analysis) | Copilot **mobile-app** clustering notebook, themes, and figure (the source corpus of Chhetri et al. 2025 must be requested from its authors) |
| [`03_Usability/Apple_HarmonyOS_Analysis/`](03_Usability/Apple_HarmonyOS_Analysis) | 28,422 collected posts (URLs and labels only), aspect-sentiment pairs, human-validation labels and rulebook, pipeline and reproduction notebooks, results, figures |

File-by-file descriptions of every folder are in [`README_details.txt`](README_details.txt); the two sentiment folders also have their own READMEs. Release-to-release changes are in [`CHANGELOG.md`](CHANGELOG.md).

## Data notes

- **No raw post text.** Posts are released "dehydrated": identified by public URL, with all labels and derived data. YouTube's API terms restrict redistribution of stored comments, and usernames raise privacy concerns. Text can be re-fetched from the URLs through the platforms' official APIs.
- **The Copilot mobile-app corpus** belongs to Chhetri et al. (2025, IEEE Big Data) and is not redistributed here.

## Citation

Archived at Zenodo: [10.5281/zenodo.23098900](https://doi.org/10.5281/zenodo.23098900). Use the **"Cite this repository"** button (generated from `CITATION.cff`), and please also cite the article.

## License

Code: MIT (`LICENSE`). Data, labels, rubrics, figures, and documentation: CC BY 4.0 (`LICENSE-DATA.md`).
