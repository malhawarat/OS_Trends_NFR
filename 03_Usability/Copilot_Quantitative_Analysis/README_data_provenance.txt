MICROSOFT COPILOT (MOBILE APP) QUANTITATIVE SENTIMENT ANALYSIS
================================================================

WHAT THIS CORPUS IS -- AND IS NOT
----------------------------------
This is NOT Windows data. The Chhetri et al. (2025) corpus is a study of user
feedback on AI-powered MOBILE apps, and the Copilot rows in it carry the
Android package identifiers com.microsoft.copilot (the Copilot app) and
com.microsoft.office.officehubrow (the Microsoft 365 app). Filtering the
corpus to Copilot therefore yields reviews of those mobile applications,
written by users who chose to install them on a phone -- not feedback on
Copilot as integrated into the Windows shell.

The paper reports the resulting 64.8% positive share as a REFERENCE POINT
only. It is not a platform estimate, it is not comparable with the Apple and
HarmonyOS figures, and it is not ranked against them. This study collected no
user-sentiment data for Windows. Earlier releases of this package described
this folder as the Windows result; that description was incorrect and has been
corrected here.

WHAT THIS FOLDER CONTAINS
--------------------------
  Copilot_Usability_Clustering.ipynb   The analysis notebook (Colab-ready): filters the
                                        source dataset to Microsoft Copilot, computes
                                        sentiment statistics, and clusters the extracted
                                        AI-feature aspect phrases into interpretable themes.

  copilot_theme_clusters_final.csv     The 38 resulting themes (18 positive, 20 negative)
                                        with cluster size, % share, and representative
                                        sample phrases. This is the source of Section 5.2's
                                        Windows subsection in the manuscript.

  copilot_summary_stats.json           Headline numbers: 20,209 aspect-sentiment pairs,
                                        15,821 unique reviews, 64.8% positive / 35.2%
                                        negative, plus the k-selection rationale.

WHAT THIS FOLDER DOES NOT CONTAIN
-----------------------------------
The underlying raw dataset (~894,000 AI-specific review rows across 292 apps) is NOT
included here. It originates from:

  Chhetri, V., Upadhyay, K., Siddique, A.B., and Farooq, U. (2025). "Large-Scale Analysis
  of User Feedback on AI-Powered Mobile Apps." 2025 IEEE International Conference on Big
  Data (Big Data), pp. 500-509. Also available as arXiv:2506.10785.

We obtained this dataset directly from the corresponding author (Umar Farooq, Louisiana
State University, ufarooq@lsu.edu) following a data-sharing request, since it was not yet
publicly hosted at the time of our request despite the paper's stated intent to release it.
It is redistributed here only in the derived, aggregated form above (cluster-level summary
statistics), not as raw review text, both out of respect for the original authors' right to
control distribution of their own unpublished release and because the raw files
(ai-summary-sentiment-merged-se3.parquet, ai-aspect_extraction-pre-processed.parquet) are
too large (>100MB each) for convenient inclusion in a manuscript replication package.

TO REPRODUCE FROM SCRATCH
----------------------------
1. Contact Umar Farooq (ufarooq@lsu.edu) requesting the dataset behind Chhetri et al.
   (2025), referencing the paper above. Check first whether it has since been publicly
   released (originally intended for Hugging Face, org: recmeapp).
2. Place the received parquet files in a Google Drive folder.
3. Open Copilot_Usability_Clustering.ipynb in Google Colab, update the DATA_DIR path if
   needed (the notebook auto-searches subfolders), and run all cells.
4. POS_K=18 and NEG_K=20 are fixed in the notebook based on a k=2-30 silhouette sweep
   (see the notebook's own markdown commentary for the full justification) -- re-run the
   sweep (Section 6) if reproducing with a different or updated dataset snapshot, since
   the optimal k may differ.

NOTE ON THEME NAMES
---------------------
The theme_name column in copilot_theme_clusters_final.csv reflects labels proposed after
reviewing each cluster's top terms and sample phrases. Per the same dual-rater discipline
used elsewhere in this study, both co-authors should independently review the cluster
samples (visible in the notebook's Section 8 output) before treating these labels as final.


DIAGNOSTIC FIGURES (added after fixing a clustering bug)
------------------------------------------------------------
  centroid_similarity_heatmaps.png
    Pairwise cosine-similarity heatmap between all raw cluster centroids
    (positive k=18, negative k=20). Shows the similarity matrix is diffuse
    with no clean block structure -- the reason a naive transitive
    (union-find) merge approach failed (see below).

  merge_dendrograms.png
    Average-linkage hierarchical clustering dendrogram for both sentiment
    classes, with the actual cut height (distance=0.45) marked in red.
    The "Forced Copilot integration" cluster (negative cluster 16) branches
    off at the highest distance in the tree, so it stayed distinct rather
    than being folded into another theme. NOTE: earlier releases called this
    "direct supporting evidence for the paper's key triangulation finding."
    That claim has been withdrawn. Remaining centroid-distinct is a property
    of the clustering resolution and merge threshold, not independent
    evidence that the underlying concern is distinct, and the cluster is
    heterogeneous: two of its five representative phrases ("unresponsive
    copilot", "unhelpful copilot") are performance complaints. Measured
    directly against the raw corpus, imposition vocabulary (forced,
    unwanted, intrusive, imposed, mandatory, unable to disable) appears in
    72 of the 7,104 negative phrases (1.0%), not the 1.9% the cluster size
    suggests. See verify_copilot_figures.py in the repository root.

NOTE ON THE MERGE ALGORITHM
------------------------------
The first version of the clustering pipeline used transitive (union-find)
merging: cluster A merges with C if A-B and B-C both cross a similarity
threshold, regardless of A-C similarity. On this data (diffuse similarity,
no clean gaps -- see the heatmap) this caused chaining: at threshold=0.58,
13 of 18 positive clusters collapsed into a single group. At threshold=0.80,
nothing merged at all. Neither is usable.

The pipeline was corrected to use average-linkage agglomerative clustering
(scipy.cluster.hierarchy, method='average'), which only merges a group if
its members are similar ON AVERAGE, not via one lucky connecting pair. This
produced a defensible, semantically coherent consolidation: 18->11 positive
meta-themes, 20->15 negative meta-themes (see copilot_theme_clusters_final.csv
and the dendrogram above). This is the version reported in the manuscript.


NOTE ON THIS RELEASE
---------------------
The notebook's saved outputs were cleared because one cell previewed rows of the
Chhetri et al. corpus, including review text that is not ours to redistribute.
All results it produced are saved in copilot_theme_clusters_final.csv and
copilot_summary_stats.json; the paper's figure is fig_themes_windows.png.
