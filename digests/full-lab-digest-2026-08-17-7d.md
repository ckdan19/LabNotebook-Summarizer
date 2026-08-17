# Full Lab Digest — 2026-08-11 to 2026-08-17 (7 days)

> 4 of 5 sources had activity in the last 7 days. 1 had none.

---

## Tumbling Oysters (Steven Roberts)

_No new posts in the last 7 days._

---

## Ariana Huffmyer Lab Notebook

> Summarized from [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io)

### Manchester Hardening project final field sampling
- **Author**: Ariana Huffmyer
- **Date**: 2026-08-14
- **URL**: https://ahuffmyer.github.io/posts/2026-08-14-manchester-hardening-experiment-final-field-sampling.html
- **Categories**: manchester-hardening, experimental design
- **Key finding**: Final field sampling of the Manchester Heat Hardening experiment, in which 10 families of Pacific oysters were given a sublethal heat stress in June 2025 and deployed at NOAA NWFS Manchester with controls, then monitored for growth and survival over the past year. The team removed all bags from outplant cages, imaged and counted live/dead oysters, downloaded field loggers, and consolidated duplicate family/treatment bags into 20 red mesh bags subsampled to n=20 oysters each for upcoming lab survival assays. Bag metadata with live/dead counts and logger data were recorded to the manchester-hardening GitHub repo.
- **Figures**:
  - external: https://github.com/RobertsLab/manchester-hardening/blob/main/figures/loggers/Manchester_loggers_experiment.png?raw=true
  - external: https://github.com/RobertsLab/manchester-hardening/blob/main/figures/loggers/Manchester_loggers_field.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260814/pic8.jpeg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260814/pic1.jpeg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260814/pic6.jpeg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260814/pic7.jpeg?raw=true

---

### Manchester Hardening project final lab sampling plan
- **Author**: Ariana Huffmyer
- **Date**: 2026-08-14
- **URL**: https://ahuffmyer.github.io/posts/2026-08-11-manchester-hardening-experiment-lab-sampling-plan.html
- **Categories**: manchester-hardening, experimental design
- **Key finding**: Experimental design plan for acute stress survival assays on the Manchester oysters brought back to UW. The 20 red mesh bags (n=20 oysters each, tracked by bag number 1-20) will be tested across four weekly rounds from Aug 17 through Sept 11, using n=4 oysters per bag per round (~16 total per bag) in numbered cups heated to 36°C, with mortality scored twice daily until ~80-90% mortality. The post specifies required materials, the base survival protocol, and the datasheets to record (temperature in 5 cups, alive/dead counts, timing, and cup/bag/round metadata).
- **Figures**:
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260814/pic2.jpeg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260814/pic3.jpeg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260814/pic4.jpeg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260814/pic5.jpeg?raw=true

_1 post from this window (the recurring "August Goals and Daily Entries" entry) was already covered in a previous digest and is omitted here._

---

## Sam's Notebook (Sam White)

> Summarized from [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook)

### Trimming - Andy Dittman RNA-seq Data Using fastp FastQC MultiQC on Hyak
- **Author**: Sam White
- **Date**: 2026-08-10
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-08-10-Trimming---Andy-Dittman-RNA-seq-Data-Using-fastp-FastQC-MultiQC-on-Hyak/
- **Categories**: fastp, fastqc, multiqc, hyak, RNA-seq, trimming
- **Key finding**: Following an initial FastQC on Andy Dittman's raw RNA-seq reads (2026-08-06), Sam trimmed the reads with fastp on Hyak (adapter removal, quality trimming, 15 bp cut from the 5' end, poly-G/poly-A tail removal) and reassessed with FastQC/MultiQC. Trimming ran quickly and produced good-quality FastQs, with per-base sequence content much more consistent across read length; 96 fastp and 192 FastQC reports were aggregated into a MultiQC report. Andy will be notified.
- **Figures**: None embedded — QC results are provided as external output/MultiQC HTML links (gannet.fish.washington.edu) rather than static images.

---

### Homogenization - SORMI June 2026 M.gigas Ctenidia from Families 5 and 7 for Citrate Synthase Assay
- **Author**: Sam White
- **Date**: 2026-08-11
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-08-11-Homogenization---SORMI-June-2026-M.gigas-Ctenidia-from-Families-5-and-7-for-Citrate-Synthase-Assay/
- **Categories**: SORMI, Magallana gigas, ctenidia, Pacific oyster, Crassostrea gigas, citrate synthase, homogenization
- **Key finding**: Ctenidia from Families 5 and 7 (ambient and 36°C, 8 samples each per treatment) were homogenized in preparation for the ABCAM Citrate Synthase Assay Kit (ab239712). Tissue was weighed to 0.1 mg and homogenized in 350 µL Assay Buffer 7 with glass beads on a pre-cooled Bullet Blender (10 min, Speed 12), then stored at -80°C. The 350 µL buffer volume (vs. the manufacturer's 100 µL) was chosen based on prior lab work by Matt George; sample weights were logged to a Google Sheet.
- **Figures**: None — this is a sample-prep entry with no plots.

---

### Protein Quantification - June 2026 SORMI M.gigas Ctenidia from Families 5 and 7 for Citrate Synthase Assay
- **Author**: Sam White
- **Date**: 2026-08-13
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-08-13-Protein-Quantification---June-2026-SORMI-M.gigas-Ctenidia-from-Famillies-5-and-7-for-Citrate-Synthase-Assay/
- **Categories**: SORMI, Magallana gigas, ctenidia, Pacific oyster, Crassostrea gigas, citrate synthase, BSA
- **Key finding**: Protein was quantified in the Families 5 and 7 ctenidia homogenates (homogenized 2026-08-11) via the Bio-Rad Quick Start Bradford assay in microplate format, to normalize the downstream citrate synthase assays. Samples with poor replicate CVs or falling outside the standard curve were flagged and re-assayed; the final re-assay plate had zero remaining QC failures. Per-sample concentrations (~260–2700 µg/mL across the 32 samples) were tabulated and written to `sample_concentrations.csv` in the sormi-assay-development repo.
- **Figures**: Plots are generated at render time from external `.Rmd` files (in RobertsLab/sormi-assay-development). Rendered outputs:
  - local: Gen5-20260813-mgig-sormi-BSA-F05-protein_files/figure-gfm/plot-standard-curve-1.png
  - local: Gen5-20260813-mgig-sormi-BSA-F05-protein_files/figure-gfm/plot-samples-on-curve-1.png
  - local: Gen5-20260813-mgig-sormi-BSA-F05-F07-reassay-protein_files/figure-gfm/plot-standard-curve-1.png
  - local: Gen5-20260813-mgig-sormi-BSA-F05-F07-reassay-protein_files/figure-gfm/plot-samples-on-curve-1.png

_1 post from this window (a cosmetic typo fix to the 2026-07-22 Families 1 and 9 glycogen homogenization entry) was already covered in a previous digest and is omitted here._

---

## Grace Crandall's Notebook

> Summarized from [grace-ac/grace-ac.github.io](https://github.com/grace-ac/grace-ac.github.io)

### FHL 2026 Eelgrass Swab DNA Extractions Part 2
- **Date**: 2026-08-10
- **URL**: https://grace-ac.github.io/eelgrassswabdna-part2/
- **Categories**: FHL2026
- **Key finding**: Grace extracted DNA from a second batch of 14 eelgrass swab samples (plus 2 blanks) from the FHL 2026 V. pectenicida / eelgrass / mussel experiment, using the Qiagen DNeasy PowerSoil Pro Kit with a swab-specific modification from Becca Maher. Samples span the ESW, EVP, EM, and EMVP treatments. Results are pending a qPCR run of 2 uL per sample targeting V. pec.
- **Figures**: none

---

### FHL 2026 Eelgrass Swab DNA Extractions Part 3
- **Date**: 2026-08-10
- **URL**: https://grace-ac.github.io/eelgrassswabdna-part3/
- **Categories**: FHL2026
- **Key finding**: This third and final batch of eelgrass swab extractions (14 samples plus 2 blanks) completes all eelgrass swab processing for the experiment. Grace logged a recovered protocol slip on sample S_EVP_08, where the swab and liquid were briefly mixed up during the CD2 transfer step but corrected immediately. Only 11 preps remain in the current kit; a replacement kit is en route for the upcoming mussel shell swabs.
- **Figures**: none

---

### FHL Experiment - qPCR Results from Plate 4
- **Date**: 2026-08-12
- **URL**: https://grace-ac.github.io/qPCR-plate4-FHL2026/
- **Categories**: FHL2026
- **Key finding**: Grace ran a fourth qPCR plate finishing the 2026 water filters and beginning the eelgrass swab DNA. The standard curve had a strong R^2 (0.954) but a problematic efficiency of 130% and a slope of -2.764 (outside the ideal -3.1 to -3.6), leading her to distrust the results. She suspects PCR inhibitors in the swab DNA (low template DNA argues against overloading) and has reached out to Colleen Burge and Melanie Prentice and opened a Roberts Lab GitHub issue; next step is sourcing a clean-up kit to remove inhibitors.
- **Figures**:
  - local: ../notebook-images/2026-08-12/20260812-plate4-2026FHL.PNG
  - local: ../notebook-images/2026-08-12/inforgraphic-efficiency.png

---

### Mussel Tissue DNA Extractions - Test with 2025 Samples
- **Date**: 2026-08-16
- **URL**: https://grace-ac.github.io/mussel2025-dna/
- **Categories**: FHL2025
- **Key finding**: Grace tested a mussel tissue DNA extraction protocol on 4 mussels (M4A, M4B, M5A, M5B) from bags 4 and 5 of the informal 2025 V. pectenicida exposure, using old Qiagen Blood and Tissue kits from Olivia Graham. She flagged three open issues: a critical Proteinase K shortage (only enough for ~10 of 36 needed samples), uncertainty about whether to homogenize whole mussel bodies before subsampling, and concern that a 300 uL double elution left the filter tip touching the eluate. Nanodrop results for 1 uL per sample are expected the following day.
- **Figures**: none

---

## Genefish WordPress

> Summarized from [genefish.wordpress.com](https://genefish.wordpress.com)

### Continued resazurin stability assays
- **Author**: naomikang44
- **Date**: 2026-08-10
- **URL**: https://genefish.wordpress.com/2026/08/10/continued-resazurin-stability-assays/
- **Key finding**: Naomi is tracking whether resazurin remains stable over a month of cold storage, reading the same heat-exposed 96-well plate (from 8/3) weekly on the Synergy HTX after fridge storage wrapped in parafilm and foil. This week's reading was logged as t2.5_week2.txt on GitHub, with further readings planned for 8/17 and 8/24. Final analysis will apply a standardized or self-calculated uncertainty margin (derived from earlier t0–t2.0 comparisons) to judge overall stability.

---

### Citrate Synthase Assay Kit Prep
- **Author**: gracehaaland
- **Date**: 2026-08-10
- **URL**: https://genefish.wordpress.com/2026/08/10/citrate-synthase-assay-kit-prep/
- **Key finding**: Grace prepared two Abcam Citrate Synthase Assay kits (ab239712), thawing and reconstituting all powdered components, then aliquoting them (CS Substrate Mix, DTNB, GSH Standard, CS Positive Control) at defined volumes for future assays. She calculated the reagent volumes needed to run 96 sample wells plus standards and controls, and noted a key limitation: running a full plate requires ~8 aliquots of CS Substrate Mix (234 µL), exceeding the 220 µL supplied in a single kit. Aliquots were labeled, dated (prep 8/10/26, use-by 10/10/26), and returned to the −20 °C freezer.

---

### Oyster_measurer updates
- **Author**: Christina Zhang
- **Date**: 2026-08-10
- **URL**: https://genefish.wordpress.com/2026/08/10/oyster_measurer-updates/
- **Key finding**: Christina restructured the oyster-measurement tool into four discrete skills (calibration, detection, measurement, and data export), and improved the detection model by masking all 50 oyster images, yielding markedly better detection against messy backgrounds than the earlier 20-image training set. The main blocker remains calibration: the AI cannot reliably locate the caliper or read it correctly, which she is addressing by supplying more ground-truth data for self-correction. Next steps include teaching the model to flag its own errors and warn the user, or building an interface where users can review and delete misdetected oysters.

---

### Tank room, and resazurin assays,
- **Author**: Jesse Lowe
- **Date**: 2026-08-11
- **URL**: https://genefish.wordpress.com/2026/08/11/tank-room-and-resazurin-assays/
- **Key finding**: Jesse recorded routine tank maintenance across 8/10–8/11, feeding the blue tanks 10 mL shellfish diet, logging water chemistry (salinity, pH, ammonia, nitrite, nitrate) for all four tanks, and performing a full water change plus filter-bag cleaning on the left blue tank. On 8/11, cockles and manilla clams were collected from Agate Pass with Megan and Grace. Prep for Wednesday's resazurin assays began, including labeling tubes and aliquoting prep solution.

---

### Roadmap updates
- **Author**: Cas Daniel
- **Date**: 2026-08-11
- **URL**: https://genefish.wordpress.com/2026/08/11/roadmap-updates/
- **Key finding**: Cas completed roadmap items 8 and 9 for the Lab Notebook Summarizer, adding a backward-looking Historical Connections subsection (8-week lookback) that correctly surfaced a multi-week analysis chain and flagged an apparent cross-week contradiction and an authorship question for human verification rather than auto-reconciling them. Item 9 delivered a daily literature-connector pipeline that fetches posts, skips logistical ones, runs the connector on real findings, and publishes a draft; a controlled test on Sam's February PolyIC finding produced a valid draft whose four citations all held up. Next steps are evaluating whether literature comments beat weekly posts and finishing item 10's Data & Figures section.

---

### Beginnings of automation
- **Author**: Cas Daniel
- **Date**: 2026-08-13
- **URL**: https://genefish.wordpress.com/2026/08/13/beginnings-of-automation/
- **Key finding**: Cas finished roadmap item 10 (a dedicated Data & Figures section in the digest) and added per-section explanatory notes so a cold reader has context. He then began automating the literature-connector to publish live rather than as drafts, gating live publishing behind an AUTHORIZATION.md file with an exact marker (defaulting back to draft if missing or altered) and adding a one-post-per-day hard cap to prevent duplicates. The process is documented for reproducibility with a sign-off log, and it remains deliberately paused by default; testing the automation and extending it to the weekly digest is planned for the next day.

---

### Oyster-measurer website beta version
- **Author**: Christina Zhang
- **Date**: 2026-08-14
- **URL**: https://genefish.wordpress.com/2026/08/14/oyster-measurer-website-beta-version/
- **Key finding**: Christina converted her trained oyster-measurement model into a working website, producing a beta workflow that is coherent to navigate. She plans to test additional images and verify whether it can be made publicly usable. The main outstanding issue is low calibration accuracy, which currently forces users to enter the px/mm scale manually.

---

## Cross-Notebook Patterns & Connections

_This section analyzes the compiled per-source summaries for shared themes, follow-up narratives, apparent contradictions, and multi-week historical connections across the lab's notebooks. Connections are surfaced only when a specific named entity ties the sources together — never from vague thematic similarity._

### Shared Themes
- **Citrate Synthase Assay (Abcam ab239712) on SORMI M. gigas ctenidia** — Sam White's notebook (homogenizing Families 5 & 7, then running Bradford protein quantification to normalize them) and genefish WordPress (Grace Haaland's "Citrate Synthase Assay Kit Prep" reconstituting and aliquoting the same Abcam ab239712 kit) are both preparing the same enzymatic citrate synthase assay on SORMI June 2026 Pacific oyster ctenidia. Same kit, same assay, same sample set — a shared assay pipeline running across the two notebooks.
- **36 °C acute thermal stress on Pacific oyster families** — Ariana Huffmyer's Manchester lab-sampling plan runs acute 36 °C survival assays across 20 bags of Pacific oyster families, while genefish WordPress reports 36 °C resazurin work (naomikang44's stability QC and Jesse Lowe prepping resazurin assays). The same organism and the same 36 °C acute-heat challenge recur across the two notebooks, differing in readout (survival scoring vs. resazurin metabolic assay).

### Temporal Narratives
- **Citrate synthase assay prep hand-off** — Grace Haaland's WordPress kit prep (Aug 10: reconstituting and aliquoting the Abcam ab239712 reagents, and flagging that CS Substrate Mix runs short of a full 96-well plate) is followed within days by Sam White homogenizing Families 5 & 7 (Aug 11) and running Bradford protein quantification to normalize them (Aug 13) for that same citrate synthase assay. The two notebooks show sequential steps converging on a single assay run.

### Historical Connections
- **SORMI June 2026 M. gigas assay development (glycogen → citrate synthase)** — Sam's current Citrate Synthase Assay prep on Families 5 & 7 extends the same SORMI June 2026 assay-development pipeline he ran the Glycogen-Glo assay on for Families 1 & 9 weeks earlier (which found no significant family or temperature effect on glycogen). See Glycogen Analysis - SORMI June 2026 M.gigas Family 1 vs Family 9 · 2026-08-06 (Sam White, sams-notebook): https://robertslab.github.io/sams-notebook/posts/2026/2026-08-06-Glycogen-Analysis---SORMI-June-2026-M.gigas-Family-1-vs-Family-9/
- **Resazurin stability month-long series** — naomikang44's current week-2 reading (fridge-stored plate re-read on the Synergy HTX) is the direct follow-up to the resazurin stability assay she set up the week before, which established the heat-exposed plate and the plan to re-read it weekly across a month. See Resazurin stability assays · 2026-08-03 (naomikang44, genefish WordPress): https://genefish.wordpress.com/2026/08/03/resazurin-stability-assays/
- **FHL V. pectenicida eelgrass/mussel biocontrol** — Grace's current eelgrass-swab and mussel-tissue DNA extractions follow up on her earlier water-filter qPCR result showing eelgrass- and/or mussel-containing treatments held very low V. pectenicida while the Vpec+seawater control stayed high; the swab and tissue extractions test whether the pathogen is being removed onto eelgrass biofilm or into mussel tissue. See FHL 2026 Water Filter qPCR Results So Far · 2026-08-04 (Grace Crandall, grace-ac.github.io): https://grace-ac.github.io/FHL2026-filter-prelim-results/

---

## Data & Figures

_This section consolidates, grouped by source, the figure links and external data/repository links already surfaced in the per-source summaries above. It is a single entry point into the underlying data and figures for this window, not a new analysis._

### Ariana Huffmyer Lab Notebook
- Manchester final field sampling — field loggers: https://github.com/RobertsLab/manchester-hardening/blob/main/figures/loggers/Manchester_loggers_experiment.png?raw=true
- Manchester final field sampling — field loggers: https://github.com/RobertsLab/manchester-hardening/blob/main/figures/loggers/Manchester_loggers_field.png?raw=true
- Manchester final field sampling — field photos: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260814/pic8.jpeg?raw=true , pic1.jpeg , pic6.jpeg , pic7.jpeg (same `20260814/` folder)
- Manchester lab sampling plan — photos: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260814/pic2.jpeg?raw=true , pic3.jpeg , pic4.jpeg , pic5.jpeg (same `20260814/` folder)
- Data: bag metadata (live/dead counts) and field logger data recorded to the RobertsLab/manchester-hardening GitHub repo

### Sam's Notebook (Sam White)
- Protein Quantification (Families 5 & 7) — BSA standard curve + samples-on-curve plots: `Gen5-20260813-mgig-sormi-BSA-F05-protein_files/figure-gfm/plot-standard-curve-1.png`, `plot-samples-on-curve-1.png`, and the F05-F07 re-assay equivalents
- Data: `sample_concentrations.csv` in the RobertsLab/sormi-assay-development repo

### Grace Crandall's Notebook
- FHL qPCR Plate 4 — plate result image: `../notebook-images/2026-08-12/20260812-plate4-2026FHL.PNG`
- FHL qPCR Plate 4 — efficiency infographic: `../notebook-images/2026-08-12/inforgraphic-efficiency.png`

### Genefish WordPress
- Continued resazurin stability assays — week-2 reading data: https://github.com/naomik44/Res_Stability/blob/main/Res_Stability08032026/t2.5_week2.txt

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

### Citrate synthase as a metabolic marker under thermal stress in bivalves

**Source:** Sam's Notebook (Citrate Synthase Assay prep on SORMI M. gigas ctenidia), cross-referenced with genefish WordPress (Citrate Synthase kit prep)
**Finding:** The lab is preparing an enzymatic citrate synthase (CS) activity assay on Pacific oyster (M. gigas) ctenidia from ambient and 36 °C SORMI families, using CS activity as a mitochondrial/aerobic-capacity metabolic marker.

**Adds context · [PubMed]: Energy metabolism under thermal stress in Mytilus galloprovincialis and Ruditapes decussatus: Insights from gene expression and enzyme activity profiles**
Papadopoulos et al., 2025 · PMID: 40627889 · https://pubmed.ncbi.nlm.nih.gov/40627889/

Over a 25-day rising-temperature exposure, this study tracked energy metabolism in a mussel and a clam by measuring citrate synthase enzyme activity alongside other metabolic enzymes (HOAD, LDH) and glycolytic gene transcription. CS activity, as an aerobic-capacity readout, shifted as the animals moved between aerobic and anaerobic metabolism at higher temperatures, with species-specific reliance on lipid oxidation versus glycolysis. It validates the use of citrate synthase activity to gauge mitochondrial/aerobic capacity under thermal stress in bivalves — the exact rationale behind the lab's CS assay on heat-exposed oyster ctenidia, here in mussel and clam rather than Pacific oyster.

**Literature summary:** One peer-reviewed paper (no relevant preprints were found) directly uses citrate synthase enzyme activity as a marker of aerobic capacity in thermally stressed bivalves, supporting the lab's use of the CS assay on heat-exposed oyster ctenidia. It covers mussel and clam species rather than Pacific oyster, so the specific M. gigas CS-activity response the lab is measuring remains to be characterized.

---

### Heat hardening and thermal tolerance in Pacific oysters

**Source:** Ariana Huffmyer Lab Notebook (Manchester Heat Hardening final field and lab sampling)
**Finding:** 10 families of Pacific oysters given a sublethal heat stress in June 2025 and outplanted for a year are being tested for growth, survival, and acute 36 °C thermal tolerance to assess whether heat hardening improves later performance.

**Adds context · [PubMed]: Transgenerational plasticity responses of larvae of Sydney rock oysters (Saccostrea glomerata) to ocean warming**
Filippini et al., 2026 · PMID: 41202725 · https://pubmed.ncbi.nlm.nih.gov/41202725/

Adults of two Sydney rock oyster families were conditioned at control (24 °C) versus warm (28 °C) temperatures, and their larvae were measured for development, abnormality, shell size, and LT50 across a 24–36 °C range. Larvae from warm-conditioned parents showed better development and, in one family, an LT50 raised by roughly 2 °C, indicating that prior parental heat exposure can buffer offspring thermal tolerance. This parallels the Manchester premise that a prior sublethal heat exposure improves later thermal tolerance/survival in oysters — here via a transgenerational route in a different oyster species; notably, S. Roberts (the lab's PI) is a co-author.

**Adds context · [PubMed]: Identifying the regulatory network of the key lipid metabolism transcription factor peroxisome proliferator-activated receptor in oysters**
Du et al., 2026 · PMID: 42331158 · https://pubmed.ncbi.nlm.nih.gov/42331158/

This study identified two PPAR subtypes in oysters and found PPARα expression and promoter activity were higher in the more cold-/heat-tolerant Crassostrea gigas than in C. angulata, mapping SNPs and candidate regulatory genes tied to PPARα and thermal adaptation. It provides molecular background on why thermal tolerance varies among oyster lineages, relevant to the family-level differences in heat tolerance the Manchester hardening experiment is designed to detect, though it concerns lipid-metabolism regulation rather than whole-organism hardening.

**Literature summary:** Two peer-reviewed papers add context to the lab's Pacific-oyster heat-hardening work: one shows transgenerational warming raises larval thermal tolerance (LT50) in Sydney rock oysters (co-authored by the lab's PI), and another maps a molecular regulator (PPARα) underlying heat-tolerance differences among oyster species. No preprint specifically addressed within-generation heat hardening in outplanted Pacific oyster families, so that specific design remains a distinctive contribution of the Manchester experiment.

---

> Generated by the `full-lab-digest` skill · 2026-08-11 to 2026-08-17 (7-day window)
