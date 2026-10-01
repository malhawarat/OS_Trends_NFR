# When Convenience Meets Risk: Replication Package

Replication package for **"When Convenience Meets Risk: Evaluating Usability, Security, and AI Reliability Across Modern Operating Systems"** by Mohammad Alhawarat and Qasem Nijem (Al-Ahliyya Amman University), submitted to *Empirical Software Engineering*.

The study maps operating-system evolution (2015–2026) onto three non-functional requirements (usability, security/privacy, and AI reliability/trustworthiness) across Apple/iOS, HarmonyOS, Fuchsia, and Windows.

## Key results

| NFR | Method | Main result |
|---|---|---|
| AI reliability | 80-item dual-rated test protocol on Windows Copilot | 82.5% accuracy overall; 55% on disclosure/consent (κ = 0.61) |
| Security/privacy | 9-criterion dual-rated documentary rubric, 3 time points | 2025/26: Apple 100%, Windows 94.4%, HarmonyOS 94.4%, Fuchsia 44.4% (κ = 0.81) |
| Usability | LLM aspect-sentiment analysis, cluster-robust, human-validated | Positive share: Windows Copilot 64.8%, HarmonyOS 44.8%, Apple Intelligence 23.4% |

Human validation of the usability pipeline: inter-rater κ = 0.896 (relevance) and 0.934 (sentiment).

## Reproduce the usability results

Open [`03_Usability/Apple_HarmonyOS_Analysis/notebooks/Reproduce_Usability_Results.ipynb`](03_Usability/Apple_HarmonyOS_Analysis/notebooks/Reproduce_Usability_Results.ipynb) in Google Colab, set `BASE` to the `Apple_HarmonyOS_Analysis` folder, and run all cells. It recomputes every Apple/HarmonyOS usability number in the paper from the released files alone, with no API calls, in about a minute.

## Contents

| Folder | What it holds |
|---|---|
| [`01_AI_Reliability/`](01_AI_Reliability) | Windows Copilot test set (80 prompts, ground truth, both raters' scores, reconciliation notes); Rater 1's independent scores for reproducing κ |
| [`02_Security_Privacy/`](02_Security_Privacy) | Security/privacy rubric: 108 cells with both raters' scores, evidence sources, reconciliation notes, and the auto-calculating trend table |
| [`03_Usability/Copilot_Quantitative_Analysis/`](03_Usability/Copilot_Quantitative_Analysis) | Windows Copilot clustering notebook, themes, and figure (the source corpus of Chhetri et al. 2025 must be requested from its authors) |
| [`03_Usability/Apple_HarmonyOS_Analysis/`](03_Usability/Apple_HarmonyOS_Analysis) | 28,422 collected posts (URLs and labels only), aspect-sentiment pairs, human-validation labels and rulebook, pipeline and reproduction notebooks, results, figures |

File-by-file descriptions of every folder are in [`README_details.txt`](README_details.txt); the two usability folders also have their own READMEs.

## Data notes

- **No raw post text.** Posts are released "dehydrated": identified by public URL, with all labels and derived data. YouTube's API terms restrict redistribution of stored comments, and usernames raise privacy concerns. Text can be re-fetched from the URLs through the platforms' official APIs.
- **Windows Copilot corpus.** It belongs to Chhetri et al. (2025, IEEE Big Data) and is not redistributed here.

## Citation

Use the **"Cite this repository"** button (generated from `CITATION.cff`), and please also cite the article.

## License

Code: MIT (`LICENSE`). Data, labels, rubrics, figures, and documentation: CC BY 4.0 (`LICENSE-DATA.md`).
