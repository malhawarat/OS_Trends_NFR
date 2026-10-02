REPLICATION PACKAGE
"When Convenience Meets Risk: Evaluating Usability, Security, and AI
Reliability Across Modern Operating Systems"
Mohammad Alhawarat (corresponding author), Qasem Nijem
Al-Ahliyya Amman University

This package accompanies the manuscript's Data and Code Availability
statement and contains the primary materials for all three non-functional
requirements (NFRs) evaluated in the paper.

===============================================================
01_AI_Reliability/
===============================================================
The Windows Copilot structured reliability test (Section 4.5 / 5.1).

  Final_Reconciled_Test_Set.xlsx
    All 80 items (20 each: Factual Q&A, Summarization, Code Generation,
    Disclosure/Consent), with prompts, ground truth, Copilot responses,
    both raters' independent scores, the reconciled Final Score, and
    per-item justification notes. This is the source of Table 1 and all
    of Section 5.1.

  Rater1_Independent_Nijem.xlsx
    Dr. Nijem's independent, pre-reconciliation scores, kept separately
    from the final file specifically so the inter-rater reliability
    statistic in Section 5.1.5 (Cohen's kappa = 0.61) can be
    independently reproduced: compare this file's Rater 1 column against
    the Rater 2 column in Final_Reconciled_Test_Set.xlsx.

  Results_Writeup.docx
    The Section 5.1 results narrative as originally drafted from this data.

  To recompute: pair Rater1_Independent_Nijem.xlsx (column "Rater 1
  Score") with Final_Reconciled_Test_Set.xlsx (column "Rater 2 Score")
  by item ID, then compute raw agreement and Cohen's kappa over the
  four-category scale (Correct / Partially Correct /
  Hallucinated-Incorrect / N/A).

===============================================================
02_Security_Privacy/
===============================================================
The security/privacy scoring rubric (Section 4.4 / 5.3), NOW THE
DUAL-RATER RECONCILED VERSION.

  Security_Privacy_Rubric_Scored.xlsx
    Four tabs: Instructions, Rubric, Scoring, and Trend. The Scoring tab
    has 108 rows (4 platforms x 3 time points x 9 criteria), each with:
    Rater 1 score + evidence (M. Alhawarat), Rater 2 score + evidence
    (Q. Nijem), Final Score, and Reconciliation Notes explaining how each
    of the 14 disagreements was resolved. Raw agreement was 87.0%,
    Cohen's kappa = 0.81 (Section 5.3.5). The Trend tab auto-calculates
    Table 4's per-platform, per-time-point percentages from the Final
    Score column via formula.

===============================================================
03_Usability/
===============================================================
Usability is measured as the positive share of AI-feature opinions,
pos/(pos+neg), with cluster-bootstrap 95% confidence intervals (Sections 4.3
and 5.2). Final estimates: Windows Copilot 64.8% [64.1, 65.6]; HarmonyOS
44.8% [36.4, 53.5]; Apple Intelligence 23.4% [22.0, 24.9].

  Copilot_Quantitative_Analysis/
    Windows Copilot, from the AI-app-review corpus of Chhetri et al. (2025),
    obtained from its authors and not redistributed here (see that folder's
    README_data_provenance.txt). Includes the clustering notebook, the 11/15
    merged themes (copilot_theme_clusters_final.csv), and the paper's theme
    figure (fig_themes_windows.png).

  Apple_HarmonyOS_Analysis/
    Apple Intelligence and HarmonyOS, from 28,422 public posts collected through
    official APIs (YouTube, Hacker News, Bluesky, Mastodon, Lemmy, App Store).
    Released "dehydrated" (URLs and labels, no post text). Includes the
    two-author human validation (consensus labels and rulebook) and a notebook,
    Reproduce_Usability_Results.ipynb, that recomputes every Apple/HarmonyOS
    number in the paper from the released files. See that folder's README.txt.

  Qualitative_Sentiment_Findings.docx
    A preliminary web-search qualitative pass over public commentary. It is
    not the usability result; its Windows findings are one of the three
    independent sources in the Discussion's consent/control triangulation.


===============================================================
KNOWN LIMITATIONS OF THIS PACKAGE (stated for transparency)
===============================================================
- Raw post text is not redistributed (API terms and privacy); posts can be
  re-fetched from their URLs, minus any deleted since collection.
- The Windows Copilot corpus belongs to Chhetri et al. (2025) and must be
  requested from its authors.
- Re-running the Apple/HarmonyOS pipeline from scratch requires API keys and
  produces a new sample; the released files and the reproduction notebook
  reproduce the paper's numbers exactly.
- The extraction model's relevance decisions were too permissive (precision
  0.653 against the authors' consensus). The paper therefore bases HarmonyOS on
  hand-validated posts and Apple on detected English posts; Apple's hand
  validation covered a 100-post sample.
- HarmonyOS themes (Figure 5) are derived from the 302 hand-validated posts
  (notebooks/HarmonyOS_Validated_Themes.ipynb); for its 208 negative phrases
  the silhouette criterion selected three clusters, so those themes are broad.
- The security rubric's HarmonyOS and Fuchsia evidence relies more on
  secondary/journalistic sources than Apple/iOS and Windows; this asymmetry is
  visible in each row's Evidence column.
- The AI-reliability protocol's Rater 2 pre-reconciliation scores were not
  preserved as a separate file the way Rater 1's were; this is disclosed in the
  manuscript (Section 5.1.5).
