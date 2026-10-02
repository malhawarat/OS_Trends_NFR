REPLICATION PACKAGE
"When Convenience Meets Risk: Evaluating User Sentiment, Security, and
AI Reliability Across Modern Operating Systems"
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
    of the 14 disagreements was resolved. Agreement is reported on the 72
    ASSESSABLE cells (the other 36 are not-applicable for both raters
    because the platform did not exist at that time point, so agreeing on
    them is automatic): 58/72 = 80.6% raw, Cohen's kappa = 0.62,
    linear-weighted kappa = 0.69 (Section 5.3.5). Over all 108 cells the
    figures are 87.0% and kappa = 0.81; earlier releases of this package
    quoted only those, which overstates agreement. The Trend tab auto-calculates
    Table 4's per-platform, per-time-point percentages from the Final
    Score column via formula.

===============================================================
03_Usability/
===============================================================
User sentiment toward AI features is measured as the positive share of
opinions, pos/(pos+neg), with cluster-bootstrap 95% confidence intervals
(Sections 4.3 and 5.2). The folder keeps the name 03_Usability for link
stability with earlier releases; the construct is sentiment, not usability.

Platform estimates (same pipeline, same kinds of source, directly
comparable): HarmonyOS 44.8% [36.4, 53.5]; Apple Intelligence 23.4%
[22.0, 24.9]; difference 21.3 pp [12.9, 30.0].

Reference point (NOT a platform estimate, not ranked against the two
above): Copilot mobile app 64.8% [64.1, 65.6].

  Copilot_Quantitative_Analysis/
    The Microsoft Copilot and Microsoft 365 MOBILE APPS, from the
    AI-app-review corpus of Chhetri et al. (2025),
    obtained from its authors and not redistributed here (see that folder's
    README_data_provenance.txt). Includes the clustering notebook, the 11/15
    merged themes (copilot_theme_clusters_final.csv), and the paper's theme
    figure (fig_themes_windows.png -- filename retained for link stability;
    its content is the mobile app, not Windows).

  Apple_HarmonyOS_Analysis/
    Apple Intelligence and HarmonyOS, from 28,422 public posts collected through
    official APIs (YouTube, Hacker News, Bluesky, Mastodon, Lemmy, App Store).
    Released "dehydrated" (URLs and labels, no post text). Includes the
    two-author human validation (consensus labels and rulebook) and a notebook,
    Reproduce_Usability_Results.ipynb, that recomputes every Apple/HarmonyOS
    number in the paper from the released files. See that folder's README.txt.

  Qualitative_Sentiment_Findings.docx
    A preliminary web-search qualitative pass over public Windows commentary,
    conducted before the Chhetri corpus was obtained. It had no sampling
    frame, no query record, no second rater and no coding scheme, and it is
    NOT a result of this study. The paper reports it as illustrative context
    only; no estimate or claim rests on it. Earlier releases described it as
    one of three independent sources in a consent/control triangulation --
    that framing has been withdrawn (see CHANGELOG.md).


===============================================================
KNOWN LIMITATIONS OF THIS PACKAGE (stated for transparency)
===============================================================
- Raw post text is not redistributed (API terms and privacy); posts can be
  re-fetched from their URLs, minus any deleted since collection.
- The Copilot mobile-app corpus belongs to Chhetri et al. (2025) and must be
  requested from its authors. Its rows carry the Android package identifiers
  com.microsoft.copilot and com.microsoft.office.officehubrow; it is not a
  measurement of Copilot as integrated into Windows, and this study collected
  no user-sentiment data for Windows.
- Re-running the Apple/HarmonyOS pipeline from scratch requires API keys and
  produces a new sample; the released files and the reproduction notebook
  reproduce the paper's numbers exactly.
- The extraction model's relevance decisions were too permissive (precision
  0.653 against the authors' consensus). The paper therefore bases HarmonyOS on
  hand-validated posts and Apple on detected English posts; Apple's hand
  validation covered a 100-post sample.
- HarmonyOS theme shares were re-derived from the 302 human-validated posts in
  release 1.1.0 (12 positive and 3 negative merged themes); the pre-validation
  version in release 1.0.0 is superseded.
- The security rubric's HarmonyOS and Fuchsia evidence relies more on
  secondary/journalistic sources than Apple/iOS and Windows; this asymmetry is
  visible in each row's Evidence column.
- The AI-reliability protocol's Rater 2 pre-reconciliation scores were not
  preserved as a separate file the way Rater 1's were; this is disclosed in the
  manuscript (Section 5.1.5).
