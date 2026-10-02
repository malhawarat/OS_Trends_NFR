"""
Reproduces every Copilot figure reported in the manuscript directly from the
Chhetri et al. (2025) corpus.

Inputs (obtain from the corresponding author of Chhetri et al. 2025):
    ai-summary-sentiment-merged-se3.parquet
    ai-aspect_extraction-pre-processed.parquet

Usage:
    python verify_copilot_figures.py <dir containing the two parquet files>

Every assertion below corresponds to a number printed in the manuscript.
"""
import sys, pathlib
import pandas as pd

DATA = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")

sent = pd.read_parquet(DATA / "ai-summary-sentiment-merged-se3.parquet")
asp = pd.read_parquet(DATA / "ai-aspect_extraction-pre-processed.parquet")

# The corpus-level claim: 292 mobile applications.
assert sent.app_name.nunique() == 292, sent.app_name.nunique()
print(f"corpus apps                       : {sent.app_name.nunique()}  (manuscript: 292)")

# Provenance: the Copilot rows are Android packages, not Windows.
cp_pkgs = sorted(
    asp[asp.app_name.astype(str).str.contains("Microsoft Copilot|Microsoft 365 Copilot",
                                              regex=True, na=False)].app_pkg.dropna().unique()
)
print(f"Copilot package identifiers       : {cp_pkgs}")
assert "com.microsoft.copilot" in cp_pkgs

# Note the leading zero-width spaces in the first app name as distributed.
NAMES = ["​​Microsoft Copilot", "Microsoft Copilot", "Microsoft 365 Copilot"]
c = sent[sent.app_name.isin(NAMES)]

pairs = len(c)
reviews = c.rev_id.nunique()
pos = int((c["values"] == "positive").sum())
neg = int((c["values"] == "negative").sum())
share = 100 * pos / (pos + neg)

print(f"aspect-sentiment pairs            : {pairs:,}   (manuscript: 20,209)")
print(f"unique reviews                    : {reviews:,}   (manuscript: 15,821)")
print(f"positive pairs                    : {pos:,}   (manuscript: 13,105)")
print(f"negative pairs                    : {neg:,}    (manuscript: 7,104)")
print(f"positive share                    : {share:.2f}%  (manuscript: 64.8%)")
assert (pairs, reviews, pos, neg) == (20209, 15821, 13105, 7104)

# Imposition vocabulary across ALL negative phrases (Section 5.2.2).
negdf = c[c["values"] == "negative"].copy()
negdf["k"] = negdf["keys"].astype(str).str.lower()

BROAD = (r"\bforc|\bunwanted\b|cannot disable|can'?t disable|can not disable|"
         r"\bdisable\b|\bremove\b|\bopt out\b|\buninstall\b|\bintrusive\b|"
         r"\bpushy?\b|\bshoved?\b|\bimposed?\b|\bmandator|\bprominen")
STRICT = (r"\bforc|\bunwanted\b|cannot disable|can'?t disable|\bimposed?\b|"
          r"\bmandator|\bintrusive\b|\bshoved?\b")

nb = int(negdf.k.str.contains(BROAD, regex=True, na=False).sum())
ns = int(negdf.k.str.contains(STRICT, regex=True, na=False).sum())
print(f"imposition phrases (broad)        : {nb} = {100*nb/len(negdf):.2f}%  (manuscript: 72 = 1.0%)")
print(f"imposition phrases (strict)       : {ns} = {100*ns/len(negdf):.2f}%  (manuscript: 63 = 0.9%)")
assert (nb, ns) == (72, 63)

print("\nAll manuscript figures reproduced.")
