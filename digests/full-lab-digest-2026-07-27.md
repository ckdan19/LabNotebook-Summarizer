# Full Lab Digest — 2026-07-21 to 2026-07-27

> 4 of 5 sources had activity this week. 1 had none.

---

## Tumbling Oysters (Steven Roberts)

_No posts in the last 7 days._

The repo's most recent commit is `b6e15bab` ("sea star wasting") dated 2026-07-10, 17 days outside the window. The prior burst of activity (2026-07-04 to 2026-07-10) covered sea star wasting/enrichment, lake trout genome methylation and structural differences, and a *Mytilus* post.

---

## Ariana Huffmyer Lab Notebook

> Summarized from [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io)

8 commits landed in the last 7 days; 4 unique `.qmd` files under `posts/` changed.

---

### New publications - July 2026
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-20
- **Source**: `posts/2026-07-20-publications.qmd` → https://ahuffmyer.github.io/posts/2026-07-20-publications.html
- **Categories**: publications
- **Key finding**: Announces two open-access papers published July 20, 2026. The PeerJ paper validates resazurin fluorescence as a scalable proxy for whole-organism oyster metabolic rate, showing strong agreement with oxygen consumption, clear thermal optima and tipping points, greater survival among individuals that depressed metabolism under acute heat, and family-level genetic variation that tracked predicted performance in 50 selectively bred *C. virginica* families. The Ecology and Evolution paper reports seasonal physiology across *Acropora*, *Pocillopora*, and *Porites* in Mo'orea, finding cryptic-lineage-specific symbiont communities and "boom and bust" symbiont cycling in *Acropora* and *Pocillopora* versus greater symbiont stability and cool-season biomass gains in massive *Porites*.
- **Figures**:
  - external: https://dfzljdn9uc3pi.cloudfront.net/2026/21542/1/fig-1-2x.jpg
  - external: https://dfzljdn9uc3pi.cloudfront.net/2026/21542/1/fig-5-1x.jpg
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260720/ece374044-fig-0001-m.jpg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260720/ece374044-fig-0008-m.jpg?raw=true

---

### Outplanting repeat priming oysters at Westcott
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-20
- **Source**: `posts/2026-07-20-westcott-outplant.qmd` → https://ahuffmyer.github.io/posts/2026-07-20-westcott-outplant.html
- **Categories**: hardening, oyster, cgigas, wsg-usda
- **Key finding**: Documents outplanting a new cohort of thermally primed *C. gigas* seed (+10°C weekly for 6 weeks at UW and Point Whitney) at Westcott Shellfish on July 18, repeating an earlier experiment in which priming increased stress tolerance after a 2-year outplant. Twelve replicate bags were imaged with scale bars and cattle tags, placed in red mesh seed bags on three racks at the upper tidal limit, and instrumented with two Hobo MX400 and eight robo-oyster temperature loggers. A field trial of resazurin at the farm produced visible color change within about 3 hours in both Pacific and Olympia oysters; growth and survival checks are planned over the coming months.
- **Figures**:
  - external: https://img.shields.io/badge/AI%20Use-L0%20None-lightgrey (HTML `<img>`, AI-use badge)
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260717/pic2.jpeg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260717/pic5.PNG?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260717/pic3.jpeg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260717/pic1.jpeg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260717/pic4.jpeg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260717/pic6.jpeg?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260717/pic7.jpeg?raw=true

---

### July Goals and Daily Entries
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-23 (front matter; file is `posts/2026-07-01-goals.qmd`)
- **Source**: `posts/2026-07-01-goals.qmd` → https://ahuffmyer.github.io/posts/2026-07-01-goals.html
- **Categories**: goals, daily-entries
- **Key finding**: Running July 2026 goals-and-log post, updated this week with entries through July 23. Priorities are manuscript work (PolyIC submission, Hawaii 2023 discussion, Moorea 2023 and Westcott oyster priming drafts), an NSF IOS application with H. Putnam, and Moorea 2023 RNAseq and metabolomics analyses. The Westcott outplant and Point Whitney hardening field task is now struck through as complete, with remaining field work being summer check-ups at Sequim, Baywater, and Goose Point; recent days cover resazurin index analysis, oyster image analysis, and E5 proofs.
- **Figures**: none

---

### Predictive resazurin phenotyping using VIMS oyster family data
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-23
- **Source**: `posts/2026-07-23-VIMS-resazurin-data-curve-phenotyping.qmd` → https://ahuffmyer.github.io/posts/2026-07-23-VIMS-resazurin-data-curve-phenotyping.html
- **Categories**: resazurin, metabolism, cvirginica
- **Key finding**: Extracted 25 quantitative curve features from 4-hour resazurin assays on ~1,255 *C. virginica* individuals across 50 families (25 high-salinity, 25 low-salinity origin) and tested whether curve shape distinguishes families and predicts family survival. Family identity explained 15–19% of individual variation, but the best-discriminating feature differed by group — early-phase rate (`initial_slope`) for high-salinity families versus sustained late output (`auc_late`) for low-salinity families. Spearman correlations plus leave-one-family-out cross-validation showed metabolic capacity traits (`vmax`, `auc_early`, `initial_slope`) reliably predict low-salinity survival (composite index CV ρ = 0.53), whereas high-salinity survival was weakly and unreliably predicted (index CV ρ = −0.26), implying no single universal resazurin metric serves both conditions and that high-salinity screening may need a longer or thermally challenged assay.
- **Note**: Post carries an AI-use disclosure (L1 Editing) — AI was used to adapt code, generate figures, and draft base text that the author edited.
- **Figures**:
  - external: https://img.shields.io/badge/AI%20Use-L1%20Editing-blue (HTML `<img>`, AI-use badge)
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260723/curve_feature_family_effect_ranking.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260723/curve_feature_best_family_boxplots.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260723/curve_feature_family_mean_heatmap.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260723/curve_feature_trajectory_classes.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260723/feature_phenotype_correlation_ranking.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260723/feature_comparison_high_vs_low_salinity.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260723/best_single_predictor_scatter.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260723/resazurin_index_scatter.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260723/family_profile_heatmap.png?raw=true

---

## Sam's Notebook (Sam White)

> Summarized from [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook)

Four `posts/**/index.qmd` files changed in the last 7 days (8 commits total; the rest were render-only commits touching `docs/`). Two are brand new/substantive additions, two are edits to older-dated posts (a link fix and a Markdown formatting fix).

---

### qPCRs - C.gigas Lifestage Carryover cDNA
- **Author**: Sam White
- **Date**: 2024-03-25
- **URL**: https://robertslab.github.io/sams-notebook/posts/2024/2024-03-25-qPCRs---C.gigas-Lifestage-Carryover-cDNA/
- **Categories**: qPCR, SsoFast, CFX Connect, HSP70, HSP90, GAPDH, VIPERIN, ATPsynthase, cGAS, DMNT1, citrate synthase, Crassostrea gigas, Pacific oyster, cDNA
- **Change this week**: link-only fix (corrected the `project-gigas-carryover` repo link) — no new science content.
- **Key finding**: Eight primer sets (ATP synthase, HSP70, GAPDH, HSP90, cGAS, VIPERIN, citrate synthase, DNMT1) were run in duplicate on lifestage-carryover cDNA using SsoAdvanced SYBR Green on a CFX Connect. Amplification and melt curves looked good across all targets, with no NTC amplification except late, low-melt-temp signal in GAPDH and cGAS that was judged non-concerning. GAPDH showed a ~2 Cq range, deemed acceptable as the normalizing gene; a handful of samples (244, 223, 243, 285, 296, 298) had loose technical replicates.
- **Figures**: 16 local PNGs (amplification and melt plots per target), e.g. `sam_2024-03-25_06-10-54-ATPsynthase-amp-plots.png`, `sam_2024-03-25_10-33-37-DNMT1-melt-plots.png`. No external images.

---

### qPCR Analysis - M.gigas PolyIC Data from Valentinas Project
- **Author**: Sam White
- **Date**: 2026-02-02
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-02-02-qPCR-Analysis---M.gigas-PolyIC-Data-from-Valentinas-Project/
- **Categories**: qPCR, Pacific oyster, Magallana gigas, Crassostrea gigas, polyIC, HSP70, HSP90, cGAS, VIPERIN, ATP Synthase, Citrate Synthase, DNMT1, GAPDH
- **Change this week**: Markdown formatting fix to the results section.
- **Key finding**: Full delta-Cq / delta-delta-Cq analysis of seven target genes (GAPDH normalizer) in oysters given PolyIC (viral dsRNA mimic) crossed with temperature, mechanical, or control stress, using two-way ANOVA plus post-hoc contrasts. HSP70 responded overwhelmingly to temperature stress regardless of PolyIC, VIPERIN was induced by PolyIC alone (control vs PolyIC control, p = 0.024), and HSP90 was significant only in the PolyIC + temperature combination. Citrate synthase, DNMT1, and — unexpectedly — cGAS showed no significant treatment effects; ATP synthase was significant for both factors but failed Levene's test, so its result is flagged as tentative.
- **Figures**: none embedded as static links (all plots are generated by R code chunks at render time).

---

### Data Received - Full RNA-seq Data for Andy Dittman and NOAA
- **Author**: Sam White
- **Date**: 2026-07-15
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-07-15-Data-Received---Full-RNA-seq-Data-for-Andy-Dittman-and-NOAA/
- **Categories**: Data Received, RNA-seq
- **Key finding**: The remainder of the RNA-seq data for Andy Dittman (NOAA) arrived from UW's Northwest Genomics Center, completing a set whose earlier subset was received 2026-05-08 and QC'd 2026-05-19 amid concerns about Bionalyzer RIN scores. Transfer to the Owl server via GlobusConnect took a full 24 hours, and this week's commit added the detailed MD5 verification output — all ~220 fastq.gz files passed. Data now lives at `owl.fish.washington.edu/nightingales/dittman_grc_rnaseq_1/`.
- **Figures**: none.

---

### Homogenization - June 2026 SORMI M.gigas Ctenidia from Families 1 and 9 for Glycogen Glo Assay
- **Author**: Sam White
- **Date**: 2026-07-22
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-07-22-Homogenization---June-2026-SORMI-M.gigas-Ctenidia-from-Families-1-and-9-for-Glycogen-Glo-Assay/
- **Categories**: SORMI, Magallana gigas, ctenidia, Pacific oyster, Crassostrea gigas, glycogen, Glycogen Glo, homogenization
- **Key finding**: Sample-prep entry for the `sormi-assay-development` project: frozen ctenidia from USDA Families 1 and 9 (ambient and 36 °C treatments, n = 8 per treatment per family, 32 samples total) from the 2026-06-26 sampling event were weighed and homogenized for glycogen quantification. Tissue was bead-beaten in a Bullet Blender 5E Gold+ (10 min, speed 12) in PBS with 0.3N HCl, then neutralized with TRIS buffer per the Glycogen Glo protocol and stored at -20 °C. Sample weights ranged widely (1.8–25.7 mg), which will matter for normalization downstream. Family selection was made by Steven.
- **Figures**: none (post includes a 32-row table of oyster IDs and ctenidia weights).

---

## Grace Crandall's Notebook

> Summarized from [grace-ac/grace-ac.github.io](https://github.com/grace-ac/grace-ac.github.io) (default branch `master`)

4 unique `_posts/*.md` files changed across 6 commits in the last 7 days. Each post file was touched by exactly one commit (no repeat edits). Two additional commits touched only `notebook-images/2026-07-24/` (a figure PNG and a readme) and are excluded as non-post files.

---

### FHL 2026 Water Filter DNA Extractions Part 4
- **Date**: 2026-07-21
- **URL**: https://grace-ac.github.io/waterfilter-dna-extractions-batch4/
- **Source**: `_posts/2026-07-21-waterfilter-dna-extractions-batch4.md`
- **Categories**: FHL2026
- **Key finding**: Completed the fourth and final DNA extraction batch from the halved 0.45 µm water filters of the 2026 FHL experiment — n=18 filter halves plus 2 extraction blanks (two blanks were needed to balance the centrifuge), using the ZymoBIOMICS DNA MiniPrep Kit (D4300) with 50 µL water elutions. The run used the protocol's optional stopping point at Step 2 (after lysis solution addition but before bead beating) to accommodate a check-in meeting; otherwise extraction proceeded without issue and DNA is stored with the prior three batches in the FTR -80 °C. Next steps are qPCR screening of all n=80 filter DNA samples for *V. pectenicida* across four plates (target: before the Aug 4 meeting) and starting the n=32 eelgrass swab extractions.
- **Figures**: none

---

### Post-SR Meeting Notes and To-Dos
- **Date**: 2026-07-22
- **URL**: https://grace-ac.github.io/postSRmtg-todos/
- **Source**: `_posts/2026-07-22-postSRmtg-todos.md`
- **Categories**: SRMtg
- **Key finding**: Check-in notes with Steven covering two items: the crab paper's rejection from Wiley Molecular Ecology with an offer to transfer to Ecology and Evolution, Journal of Fish Diseases, or Journal of Fish Biology; and a discrepancy between GO enrichment results obtained with `topGO` versus DAVID. Decisions were to transfer the submission to Journal of Fish Diseases that day, and to switch enrichment work to `topGO` because it is reproducible while DAVID's copy-paste workflow is error-prone and hard to track. Roberts Lab MOPE was flagged as a secondary resource to test, with the goal of having multispecies results ready for the following Wednesday's pycno check-in.
- **Figures**: none

---

### Paper Submission Transfer - Coyle et al Crab Paper
- **Date**: 2026-07-22
- **URL**: https://grace-ac.github.io/resubmit-crab/
- **Source**: `_posts/2026-07-22-resubmit-crab.md`
- **Categories**: CoyleCrab
- **Key finding**: Follow-through on the crab paper rejection: of the three Wiley transfer options offered, Journal of Fish Diseases was selected as the best scope fit given its coverage of disease in wild and cultured fish and shellfish. The manuscript was submitted the same day via Wiley's submission transfer option, so no new formatting or resubmission from scratch was required. Outcome pending.
- **Figures**: none

---

### FHL Experiment - 2026 Water Filter qPCR Plates 1 and 2
- **Date**: 2026-07-24
- **URL**: https://grace-ac.github.io/2026filter-qpcr-plate1and2/
- **Source**: `_posts/2026-07-24-2026filter-qpcr-plate1and2.md`
- **Categories**: FHL2026
- **Key finding**: First two qPCR plates (24 samples each, 2 µL DNA) targeting *V. pectenicida* on the 2026 FHL water filter extractions were run and assessed. Plate 1 gave a clean standard curve (R² = 0.995, slope -3.411, E = 96.4%); Plate 2 was initially poor (R² = 0.85) but recovered to R² = 0.979, slope -3.266, E = 102.5% after dropping one standard curve replicate (well D3) from the analysis. A rough Excel figure of mean starting quantity per sample shows results by treatment group (T0, VPSW, EVP, EMVP, MVP, EM, MSW, ShSW, SW, blanks). Supply audit indicates at least 6 more plates are needed to finish all filter, eelgrass swab, mussel tissue, and mussel swab samples, requiring reorders of TaqMan Master Mix, 10X EXO IPC Mix, and 50X EXO IPC DNA; plates, primers, probe, and standards are sufficient.
- **Figures**:
  - local: `../notebook-images/2026-07-24/2026-waterfilters-rough-fig.png`

---

## Genefish WordPress

> Summarized from [genefish.wordpress.com](https://genefish.wordpress.com)

### I took oysters out of…
- **Author**: genefish
- **Date**: 2026-07-21
- **URL**: https://genefish.wordpress.com/2026/07/21/i-took-oysters-out-of/
- **Key finding**: A short logistical checkpoint recording removal of oysters from the Young lab incubator, where the intended count of 36 turned out to be 33 individuals and no mortality was observed. The water was swapped for cold deionized water and the animals were returned to the incubator, which was reset to 46°C at 9 am. No analysis accompanied the entry.

---

### "Oyster Measurer" training updates
- **Author**: Christina Zhang
- **Date**: 2026-07-21
- **URL**: https://genefish.wordpress.com/2026/07/21/oyster-measurer-training-updates/
- **Key finding**: Christina hand-masked 20 oyster photos to train an AI measurement workflow, pairing them with the raw images and writing a detailed prompt that specified excluding non-oyster organisms and debris, exporting per-image tabs to a spreadsheet, and including annotated images for verification. The model initially clustered oysters together but separated them correctly once it was directed to rely on the supplied blue masks; caliper and ruler recognition remained unreliable, so calibration is still an open problem. The next step is training a YOLOv8 detector so masks are no longer needed, which will require additional training images.

---

### Building & compiling the first final draft of weekly lab digests
- **Author**: Cas Daniel
- **Date**: 2026-07-21
- **URL**: https://genefish.wordpress.com/2026/07/21/building-compiling-the-first-final-draft-of-weekly-lab-digests/
- **Key finding**: Cas completed a literature-connector skill that appends PubMed/bioRxiv matches to the weekly lab digest, adding an explicit rule that any failed fetch must be excluded outright after early tests produced a summary from an unretrievable paper. A re-run recovered the same record through Europe PMC instead of the broken bioRxiv link, and manual checks of both citations in the real digest run (Ariana's resazurin paper and Hazel's glycogen results) confirmed they were genuine and accurately described. The integration was committed, giving the digest three sections — per-notebook summaries, cross-notebook patterns, and literature connections — and planning began on OAuth2-authenticated posting to WordPress with human review before publication.

---

### Shell strength testing
- **Author**: acasey2
- **Date**: 2026-07-22
- **URL**: https://genefish.wordpress.com/2026/07/22/shell-strength-testing/
- **Key finding**: Brief note that shell strength testing was carried out in the lab on Pacific oysters that had been exposed in situ to ocean alkalinity enhancement versus ambient conditions in Port Angeles Harbor. The entry logs that the comparison was performed but reports no results.

---

### Today Steven and I upscaled…
- **Author**: acasey2
- **Date**: 2026-07-22
- **URL**: https://genefish.wordpress.com/2026/07/22/today-steven-and-i-upscaled/
- **Key finding**: The OAE oyster experiment was scaled up from buckets into trash bins. The stated motivation is to distinguish whether the mortalities seen so far stem from limited water volume and husbandry conditions or represent a genuine ocean alkalinity enhancement effect.

---

### Creating a publishing skill for Lab Notebook Digests
- **Author**: Cas Daniel
- **Date**: 2026-07-23
- **URL**: https://genefish.wordpress.com/2026/07/23/creating-a-publishing-skill-for-lab-notebook-digests/
- **Key finding**: Cas built the final piece of the Lab Notebook Digest pipeline: a wordpress-publisher skill that locates the newest digest file, reads a stored access token, converts Markdown to HTML, and uploads the result as a WordPress draft for human review. Getting there required registering the summarizer as a WordPress app, linking it to the account, and generating an access token via the terminal, with most trouble coming from shell commands and credential handling. The first test succeeded apart from a duplicated header, completing the end-to-end pipeline (five notebook subagents, compiler, cross-notebook pattern detection, literature connector, publisher), with formatting and layout refinements planned next.

---

### Full Lab Digest — 2026-07-15 to 2026-07-21
- **Author**: Cas Daniel
- **Date**: 2026-07-23
- **URL**: https://genefish.wordpress.com/2026/07/23/full-lab-digest-2026-07-15-to-2026-07-21/
- **Key finding**: The first published output of the automated digest pipeline, covering three of five notebook sources with activity (Ariana Huffmyer's notebook, Sam's Notebook, and genefish WordPress; Tumbling Oysters and Grace Crandall had none). Content spans week 7 of oyster seed thermal hardening and outplanting at Westcott, two new open-access papers on resazurin as a metabolic proxy and seasonal coral physiology, receipt of full RNA-seq data for a NOAA collaborator, and several genefish entries on repeat 35°C stress assays, mitochondrial potential protocols, and family-level mortality assessments. The cross-notebook section flagged convergent 35–36°C thermal stress work on *C. gigas* across two notebooks, and the literature section linked two findings to verified external publications.

---

### My rough protocol for collagen gene expression analysis in starfish
- **Author**: Samuel Slutz
- **Date**: 2026-07-24
- **URL**: https://genefish.wordpress.com/2026/07/24/my-rough-protocol-for-collagen-gene-expression-analysis-in-starfish/
- **Key finding**: Samuel outlined a draft workflow for identifying collagen-related gene expression in three sea star species, in which BLAST hits are mapped through UniProt and filtered using GO annotations to isolate collagen-associated genes. Per-species results are consolidated into Excel sheets and fed into an in-progress "Expression Helper" program he is writing with the rxlsx library. The tool combines each species' gene expression matrix with its BLAST results to compute the difference in mean expression between exposed and unexposed stars.

---

## Cross-Notebook Patterns & Connections

### Shared Themes

- **Acute elevated-temperature treatment of *Magallana/Crassostrea gigas*** appears in three sources. Sam homogenized ctenidia from ambient and **36 °C** SORMI treatments (USDA Families 1 and 9); Ariana outplanted *C. gigas* seed given **+10 °C weekly for 6 weeks** of thermal priming at UW and Point Whitney; and genefish logged an incubator heat exposure of 33 oysters with the unit reset to a high setpoint the same morning. Same species, same class of acute thermal challenge, three independent experiments running concurrently.

- **qPCR is the shared assay of the week across two notebooks, with standard-curve/replicate QC as the common bottleneck.** Grace ran the first two TaqMan plates for *V. pectenicida* on FHL water-filter DNA and had to drop standard-curve replicate D3 from Plate 2 to bring R² from 0.85 to 0.979; Sam's two edited posts both concern SYBR Green qPCR panels on *C. gigas* cDNA, where GAPDH's ~2 Cq spread and a set of loose technical replicates were the QC calls. Different targets, identical failure mode and remediation pattern.

- **Family-level phenotyping of selectively bred oyster stocks** ties Ariana's and Sam's work. Ariana's VIMS analysis partitioned resazurin curve variation across **50 *C. virginica* families** (family identity explaining 15–19%); Sam's glycogen prep is restricted to **USDA Families 1 and 9**, with the family selection made by Steven. Both are family-as-unit designs on selectively bred material, and the prior week's published digest already flagged family-level mortality assessment as an active thread.

- **The resazurin metabolic assay** spans Ariana's notebook and the genefish WordPress source. Ariana ran an in-field resazurin trial at Westcott Shellfish (visible color change within ~3 h in both Pacific and Olympia oysters) and a full curve-phenotyping analysis of the VIMS family data; the genefish digest post published the same PeerJ resazurin paper to the lab-wide audience. The assay moved from validation to field deployment to predictive screening inside one week.

- **Automated measurement of oyster photographs** connects Ariana's and Christina's work through a specific shared problem: physical scale calibration from images. Ariana's Westcott bags were photographed with scale bars and cattle tags, and her July log lists oyster image analysis among the week's tasks; Christina's "Oyster Measurer" separated individual oysters correctly once directed to the supplied masks, but **caliper and ruler recognition remained unreliable**, leaving calibration unresolved before the planned YOLOv8 step.

### Temporal Narratives

- **The resazurin paper propagated across sources within three days.** Ariana announced the PeerJ publication on 2026-07-20; on 2026-07-23 the genefish digest post carried it into the first published lab-wide digest; and on the same day Ariana posted the VIMS curve-phenotyping analysis, which takes the newly validated assay and asks the next question — whether curve *shape* can screen families predictively rather than merely index metabolism.

- **Glycogen work handed off between sources.** The 2026-07-23 genefish digest post records glycogen results from the prior week as one of two findings it fact-checked against the literature; Sam's 2026-07-22 post then prepared 32 SORMI *M. gigas* ctenidia homogenates for the Glycogen Glo assay, with family selection made by Steven. Same assay, same species, same project line, consecutive steps.

- **Manuscript preparation appears to be driving notebook cleanup.** Ariana's July goals list **PolyIC submission** as a top manuscript priority; in the same window Sam's only two post edits were housekeeping on exactly that project's records — a broken `project-gigas-carryover` repo link and a Markdown formatting fix in the PolyIC qPCR analysis. Neither edit added science, which is consistent with a pre-submission pass over the cited notebook entries.

### Apparent Contradictions

- **Which direction of metabolic response predicts survival is inconsistent between Ariana's two posts this week.** The PeerJ paper announced on 2026-07-20 reports that individuals showing *greater metabolic depression* under acute heat were more likely to survive, whereas the 2026-07-23 VIMS analysis finds that *higher metabolic capacity* traits (`vmax`, `auc_early`, `initial_slope`) predict better family survival in low-salinity stocks (CV ρ = 0.53). ⚠️ Needs human verification — the two results are likely reconcilable because they use different stressors (acute thermal challenge vs. low-salinity origin/performance) and different units of analysis (individual vs. family mean), but the resazurin index as currently defined would rank the same animals oppositely under the two framings.

- **Sam's PolyIC panel found cGAS unresponsive to a dsRNA mimic**, which sits oddly beside the same post's finding that VIPERIN — a canonical interferon-stimulated gene — was significantly induced by PolyIC alone. ⚠️ Needs human verification — resolving this requires establishing which cytosolic sensor carries the dsRNA signal in *M. gigas*, since cGAS is a DNA sensor and the RIG-I/MDA5–MAVS axis is the expected route for PolyIC (see Literature Connections below).

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

### Resazurin curve phenotyping as a predictive family-screening tool

**Source:** Ariana Huffmyer Lab Notebook
**Finding:** 25 curve features from 4-hour resazurin assays on ~1,255 *C. virginica* across 50 families show family identity explains 15–19% of individual variation, and metabolic capacity traits predict family survival in low-salinity stocks but not high-salinity stocks.

### Supports [PubMed]: From blue to pink: resazurin as a high-throughput proxy for metabolic rate in oysters
Huffmyer et al., 2026 · PMID: 42495017 · https://pubmed.ncbi.nlm.nih.gov/42495017/ (originally posted as bioRxiv preprint: https://doi.org/10.1101/2025.11.06.686367)

This is the peer-reviewed publication underpinning the new analysis: it validates resazurin fluorescence against oxygen consumption in *C. gigas* and *C. virginica*, maps thermal optima and tipping points, and reports significant family-level differences in metabolic response. It also shows that metabolic rates of the same 50 selectively bred *C. virginica* families correlated with predicted performance. That establishes the family-level signal the curve-feature work is now trying to convert into a usable screening metric, while its separate result that greater metabolic depression predicted survival under acute heat is the source of the directional tension flagged above.

### Adds context [PubMed]: Cytotoxicity of polystyrene nanoplastics involves mitochondrial dysfunction and DNA damage in hemocytes of the Pacific oyster
de Carvalho Penha et al., 2025 · PMID: 41115343 · https://pubmed.ncbi.nlm.nih.gov/41115343/

Using *C. gigas* hemocytes, this study found the resazurin metabolic-activity endpoint more sensitive to nanoplastic exposure than lysosomal integrity, and showed that shifting cells toward mitochondrial versus anaerobic metabolism changed the measured toxicity. That metabolic-substrate dependence is directly relevant to interpreting curve features: it implies resazurin reduction rate reflects which energy pathway is dominant at the time of assay, not total metabolic capacity alone. This offers a mechanistic reason why early-phase and late-phase curve features could diverge between family groups.

### Adds context [bioRxiv preprint — not peer-reviewed]: Hemocyte Viability Assay as an Alternative Method for Testing Bacterial Pathogenicity in Bivalves
Samson et al., 2025 · DOI: 10.1101/2025.11.04.686564 · https://doi.org/10.1101/2025.11.04.686564

This preprint optimized a resazurin-based assay on eastern oyster (*C. virginica*) hemocytes and derived LC50 values for *Vibrio coralliilyticus* RE22 and hatchery isolates, then validated the thresholds against larval mortality outcomes. It demonstrates the same dye producing a quantitative, predictive phenotype in the same species at the cellular level. It also suggests a comparison worth making: whether family differences in whole-organism curve features track hemocyte-level resazurin response.

**Literature summary:** The lab's own peer-reviewed PeerJ paper anchors the assay's validity and the existence of family-level variation, so the new curve-feature analysis is an extension of an established result rather than a novel claim. One additional peer-reviewed paper indicates that resazurin reduction is sensitive to which metabolic pathway is active, which is a plausible mechanism for why different curve features discriminate high- versus low-salinity families. A preprint applying the same dye to *C. virginica* hemocytes points toward a cellular-level cross-check but has not been peer-reviewed.

---

### PolyIC induces VIPERIN but not cGAS in *Magallana gigas*

**Source:** Sam's Notebook
**Finding:** In a seven-gene qPCR panel, VIPERIN was significantly induced by PolyIC alone (p = 0.024), HSP70 responded to temperature regardless of PolyIC, and cGAS unexpectedly showed no significant treatment effect.

### Adds context [PubMed]: The RNA sensor MDA5 contributes to the antiviral immune response in Crassostrea gigas by modulating the MAVS-mediated signaling pathway
Xu et al., 2026 · PMID: 41605267 · https://pubmed.ncbi.nlm.nih.gov/41605267/

This study identified CgMDA5 in *C. gigas*, showed its haemocyte expression is significantly upregulated by poly(I:C) and 5'-ppp dsRNA, and demonstrated in vitro binding to poly(I:C) with a preference for longer dsRNA. RNAi of CgMDA5 or CgMAVS reduced downstream CgIRF1, CgIRF8 and CgIFNLP expression, placing dsRNA sensing on an MDA5–MAVS–IRF–IFNLP axis. This provides a direct explanation for the cGAS result: in *C. gigas*, poly(I:C) is expected to signal through the RLR family, not through the DNA-sensing cGAS branch, so a null cGAS response is the predicted outcome rather than an anomaly.

### Supports [PubMed]: An OASL homologue involved in IFN-like antiviral signal by binding MDA5 in the Pacific oyster Crassostrea gigas
Zeng et al., 2026 · PMID: 41580101 · https://pubmed.ncbi.nlm.nih.gov/41580101/

CgOASL, an interferon-stimulated gene homologue, was significantly upregulated in *C. gigas* haemocytes after poly(I:C) and recombinant IFN-like protein stimulation, and that induction was suppressed by RNAi of CgIFNLP or its receptor CgIFNR-3. The recombinant protein bound dsRNA and interacted specifically with CgMDA5 rather than CgRIG-I. This supports the VIPERIN result: interferon-stimulated genes in this species are inducible by poly(I:C) through an IFN-like pathway, which is the same class of response VIPERIN represents.

**Literature summary:** Two peer-reviewed papers from the last 12 months converge on an MDA5–MAVS–IRF–IFNLP pathway as the route by which poly(I:C) is sensed in *C. gigas*, with interferon-stimulated genes as the downstream readout. Together they reframe the notebook's "unexpected" cGAS null result as consistent with current mechanism, and they place VIPERIN's PolyIC-specific induction squarely within the expected ISG response. No preprints matching this topic were retrieved.

---

### Repeat thermal priming and hardening of *C. gigas* seed

**Source:** Ariana Huffmyer Lab Notebook (Westcott outplant); related 36 °C treatments in Sam's Notebook and genefish WordPress
**Finding:** A second cohort of *C. gigas* seed given +10 °C weekly for 6 weeks was outplanted at Westcott, repeating an earlier experiment in which priming increased stress tolerance after a 2-year outplant.

### Adds context [PubMed]: Embryonic Hormetic Priming Modulates Later-Life Thermal Tolerance
Lugue et al., 2026 · PMID: 42017008 · https://pubmed.ncbi.nlm.nih.gov/42017008/

Two bi-parental progenies of black-lip pearl oyster (*Pinctada margaritifera*) were thermally primed as embryos and reared four months under common conditions before thermal challenge. Priming enhanced spat thermal tolerance in one family and reduced it in the other, while the core heat-stress molecular pathways were conserved and priming-independent; the environmental "memory" showed up instead as reorganization of gene networks, notably the unfolded protein response. This is a direct caution for the repeat-priming design: priming benefit may be family-dependent rather than a general effect, which argues for tracking family identity through the Westcott outplant rather than treating primed seed as one group.

### Adds context [bioRxiv preprint — not peer-reviewed]: Parental immune priming reshapes offspring growth, metabolism, and thermal tolerance in the Pacific Oyster
Baird et al., 2025 · DOI: 10.64898/2025.12.10.693539 · https://doi.org/10.64898/2025.12.10.693539

Broodstock *Magallana gigas* were given a Poly(I:C) immune challenge and their offspring assessed for survival, growth, and metabolism under thermal stress. Primed offspring grew faster and survived better at 40 °C but worse at 42 °C, and showed higher metabolic activity at 36 °C yet lower activity at 40 °C than controls. This preprint links the lab's PolyIC and thermal-hardening threads directly and warns that priming benefits are bounded by temperature — a relevant framing for both the +10 °C hardening cohort and the 36 °C SORMI treatments, though it has not been peer-reviewed.

**Literature summary:** One peer-reviewed paper on a different oyster genus shows that thermal priming can help one family and harm another, with the priming signature carried by network reorganization rather than by the canonical heat-shock response. A preprint on *M. gigas* itself reports that priming benefits reverse above a thermal threshold and that primed animals differ in metabolic response specifically at 36 °C and 40 °C. Both point the same direction — priming outcome is conditional on family and on challenge temperature — but only the first has been peer-reviewed.

---

### Glycogen depletion in *M. gigas* under elevated temperature

**Source:** Sam's Notebook (SORMI ctenidia homogenization); glycogen thread also carried in the genefish WordPress digest
**Finding:** Ctenidia from ambient and 36 °C treatments in USDA Families 1 and 9 (n = 8 per treatment per family) were homogenized for Glycogen Glo quantification, with sample weights spanning 1.8–25.7 mg.

### Adds context [PubMed]: Effects of temperature and Nocardia crassostreae on the immune response of the Pacific oyster, Magallana gigas
Mason et al., 2026 · PMID: 42476329 · https://pubmed.ncbi.nlm.nih.gov/42476329/

*M. gigas* were challenged for 42 days with elevated temperature and/or *Nocardia crassostreae*, then assayed for energetic and immune parameters. Elevated temperature independently reduced glycogen stores, ATP concentration, haemocyte viability, and gill Na+/K+-ATPase activity, while infection separately reduced condition index and mantle glycogen with elevated glucose, ADP and AMP; no significant temperature-by-infection interaction was detected. This sets a clear directional expectation for the SORMI assay — lower glycogen in the 36 °C group — and, because the effect was measured in mantle rather than ctenidia, raises tissue choice as a variable worth noting when interpreting results.

**Literature summary:** A single peer-reviewed study from this month establishes that elevated temperature alone depletes glycogen in *M. gigas* alongside broader energetic strain, giving the SORMI glycogen measurements a specific predicted direction. It also indicates that thermal and pathogen effects on glycogen operate largely independently in this species. No preprints on this topic were retrieved.

---

### qPCR screening of seawater filters for *Vibrio pectenicida*

**Source:** Grace Crandall's Notebook
**Finding:** All n=80 FHL water-filter DNA extractions are being screened by TaqMan qPCR for *V. pectenicida*; the first two plates yielded usable standard curves (E = 96.4% and, after dropping one replicate, 102.5%).

### Adds context [PubMed]: Vibrio pectenicida strain FHCF-3 is a causative agent of sea star wasting disease
Prentice et al., 2025 · PMID: 40760083 · https://pubmed.ncbi.nlm.nih.gov/40760083/

Exposure experiments using tissue extracts, coelomic fluid and effluent water from wasting sunflower sea stars induced disease and mortality with none in controls, and deep sequencing of diseased coelomic fluid was dominated by *V. pectenicida* reads. Culturing strain FHCF-3 and reproducing disease fulfilled Koch's postulates. The paper explicitly frames broad-scale screening for pathogen presence and abundance in laboratory and field samples as the follow-on need — which is precisely what the filter qPCR series is doing; note that G. A. Crandall is a co-author, so this is the lab's own foundational result for the assay.

### Adds context [PubMed]: Microbe Profile: Vibrio pectenicida: the deadly marine bacteria with strains impacting sea stars and scallops
Blackwood et al., 2026 · PMID: 42455634 · https://pubmed.ncbi.nlm.nih.gov/42455634/

This profile summarizes *V. pectenicida* as a coastal-water, facultatively anaerobic bacterium first described in 1998, with distinct strain types: A365 associated with larval scallop mortality via a haemocyte-killer toxin, and FHCF-3 associated with sea star wasting. It notes that current effort is going into isolating additional strains to test their disease role. The multi-strain structure matters for interpreting environmental qPCR positives, since a species-level assay on seawater DNA will not by itself distinguish FHCF-3 from other strain types present in the water column.

### Conflicts [bioRxiv preprint — not peer-reviewed]: When bacteria meet many arms: Autecological insights into *Vibrio pectenicida* FHCF-3 in echinoderms
Hewson, 2025 · DOI: 10.1101/2025.08.15.670479 · https://doi.org/10.1101/2025.08.15.670479

This reanalysis of 2013–2015 genomic and transcriptomic data detected FHCF-3 16S rRNA in abnormal *Pycnopodia helianthoides* body wall from public aquaria but not in other species sampled at mass-mortality sites, and found detection in coelomic fluid inconsistent and inversely related to abundance at specimen surfaces. Organic-matter amendment of *Pisaster ochraceus* enriched FHCF-3 at the animal–water interface, surging 24 h before lesions appeared. The tension with a straightforward water-column screening interpretation is that abundance at the animal surface and in the surrounding water may decouple from host infection status, so filter positives may index copiotrophic bloom conditions as much as host disease; this is a preprint and has not been peer-reviewed.

**Literature summary:** Two peer-reviewed sources establish *V. pectenicida* FHCF-3 as a causative agent of sea star wasting and describe the species' multi-strain structure in coastal waters, together justifying environmental screening while flagging that a species-level assay may not resolve strains. One preprint reports that FHCF-3 detection is inconsistent across tissues and can surge at the animal–water interface ahead of lesions, which complicates the mapping from a water-filter qPCR signal to host infection; it has not been peer-reviewed. The experimental design of the FHL series — treatment groups spanning seawater, eelgrass, mussel and sea star exposures — is well suited to testing exactly that decoupling.

---

### Ocean alkalinity enhancement and Pacific oyster shell strength

**Source:** Genefish WordPress
**Finding:** Shell strength was tested on Pacific oysters exposed in situ to ocean alkalinity enhancement versus ambient conditions in Port Angeles Harbor; a parallel entry scaled the OAE experiment from buckets to trash bins to test whether observed mortality reflects husbandry or a genuine OAE effect.

### Adds context [PubMed]: Differential impacts of ocean acidification and alkalinization on shell microstructure and molecular responses in Mytilus edulis
Chen et al., 2026 · PMID: 41806513 · https://pubmed.ncbi.nlm.nih.gov/41806513/

Blue mussels were held 21 days under ocean acidification (pH 7.3) or NaOH-based OAE (pH 9.0) and assessed by shell microstructure analysis and transcriptomics. Survival was unaffected in both; acidification degraded shell and activated stress pathways, whereas OAE improved shell integrity, stimulated growth-associated processes, and caused minimal disruption of biomineralization. The direct prediction for the Port Angeles comparison is that OAE-exposed shells should be no weaker — and possibly stronger — than ambient, which also bears on whether the observed mortality is attributable to OAE at all.

### Adds context [PubMed]: Oyster farming acts as a marine carbon dioxide removal (mCDR) hotspot for climate change mitigation
Chen et al., 2025 · PMID: 40892922 · https://pubmed.ncbi.nlm.nih.gov/40892922/

Field mesocosms showed that oyster filter-feeding accelerates particulate and dissolved organic carbon formation and organic carbon deposition in sediments, shifting the water column toward a more autotrophic and alkaline state. Net carbon sequestered via oyster-driven organic carbon production was 2.39 times that stored in shells. This matters for OAE experimental design: the oysters themselves push local carbonate chemistry alkaline, so enclosure volume influences the carbonate environment — relevant to the decision to move from buckets to trash bins.

**Literature summary:** One peer-reviewed study on a closely related bivalve provides the only direct organism-level evidence retrieved for alkalinization effects on shell, and it points toward neutral-to-improved shell integrity under OAE rather than harm. A second peer-reviewed paper shows that farmed oysters themselves alkalinize their surrounding water column, which means container volume is a carbonate-chemistry variable and not only a husbandry one. No preprints on this topic were retrieved.

---

### Collagen-related gene expression in exposed versus unexposed sea stars

**Source:** Genefish WordPress
**Finding:** A draft workflow maps BLAST hits through UniProt and filters by GO annotation to isolate collagen-associated genes in three sea star species, then computes the difference in mean expression between exposed and unexposed animals.

### Supports [PubMed]: Precursors of sea star wasting: immune and microbial disruption during initial disease outbreak in southeast Alaska
McCracken et al., 2026 · PMID: 42014077 · https://pubmed.ncbi.nlm.nih.gov/42014077/

Transcriptomic and microbial data from wild *Pycnopodia helianthoides* across affected and unaffected southeast Alaska sites showed that individuals exposed to wasting but without visible lesions had elevated expression of complement components, pathogen recognition and immune regulatory pathways relative to naive animals. Critically for this workflow, the same comparison also revealed differential expression of **extracellular matrix and tissue remodelling genes**, interpreted as disruption of tissue homeostasis preceding visible disease signs. That is independent support for treating collagen and other ECM transcripts as an informative exposed-versus-unexposed contrast, and it suggests the signal may be detectable before gross lesions appear. Microbial network analysis further linked *Vibrio* abundance to tissue-integrity gene expression, though *V. pectenicida* itself was too rare in the samples for detailed analysis.

**Literature summary:** A single peer-reviewed study supports the premise of this analysis: extracellular matrix and tissue-remodelling genes are differentially expressed in wasting-exposed sea stars relative to naive ones, and the shift precedes visible lesions. It also indicates the contrast is informative in asymptomatic exposed animals, which argues for retaining exposure status rather than lesion status as the grouping variable. No preprints on this topic were retrieved.

> Coverage limited to papers indexed on PubMed and preprints discoverable via Europe PMC (which indexes bioRxiv, Authorea Preprints, Research Square, medRxiv, and other preprint servers), restricted to the last 12 months. **Preprints have not been peer-reviewed** and should be interpreted with appropriate caution. Preprints that have since been published in a peer-reviewed journal are reported in their published form where detected.

---

> Generated by the `full-lab-digest` skill · 2026-07-21 to 2026-07-27
