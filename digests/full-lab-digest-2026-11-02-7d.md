# Full Lab Digest — 2026-10-26 to 2026-11-02 (7 days)

> 4 of 7 sources had activity in the last 7 days. 3 had none.

---

## Tumbling Oysters (Steven Roberts)

_No new posts in the last 7 days._

---

## Ariana Huffmyer Lab Notebook

### Re-analysis of PolyIC qPCR data with new normalizing gene
- **Date**: 2026-10-29
- **Author**: Ariana Huffmyer
- **Categories**: cgigas, oyster, polyic, analysis
- **AI-use disclosure**: Badge indicates "L0 None" — the original qPCR analysis script used AI for code editing, but the statistical models/figures presented were coded and analyzed by the author without AI.
- **Key finding**: In response to reviewer comments on the PolyIC manuscript, the author re-evaluated the qPCR normalizing gene after finding GAPDH was itself affected by treatment, and re-ran ANOVAs on Cq values to select cGAS as a stable new normalizer (sample sizes also increased to n=17-20/group via a new qPCR batch). Using delta-Cq values normalized to cGAS, ANOVA models showed a significant effect of parental Poly(I:C) exposure on HSP90 expression and a significant Poly(I:C) x stress interaction on DNMT1 expression, both most pronounced at 44°C, while Citrate Synthase and ATP Synthase were excluded due to batch effects/violated assumptions, and Viperin and GAPDH showed no treatment effects. The author concludes parental immune priming may be influencing offspring thermal tolerance and metabolism, and plans to revise the manuscript discussion accordingly ahead of a December 1 resubmission.
- **Figures**:
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261029/plot1.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261029/genes.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261029/citrate.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261029/atpsynthase.png?raw=true

_1 post from this window was already covered in a previous digest and is omitted here._

---

## Sam's Notebook (Sam White)

### RNA Quantification - R.philippinarum Gill RNA from 2008 Using Qubit High Sensitivity RNA Assay
- **Author**: Sam White
- **Date**: 2026-10-27
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-10-27-RNA-Quantification---R.philippinarum-Gill-RNA-from-2008-Using-Qubit-High-Sensitivity-RNA-Assay/
- **Categories**: Ruditapes philippinarum, Manila clam, gill, RNA, RNA quantification, Qubit
- **Key finding**: In preparation for testing new Manila clam qPCR primers, Sam re-quantified archival 2008 gill RNA (spun vs. control clams) using the Qubit HS RNA assay rather than relying on older, less-accurate NanoDrop values. Concentrations ranged roughly 70-200 ng/uL across the 10 samples; a pooled aliquot (1uL of each sample) was made for downstream cDNA synthesis, and both original and pooled RNA were returned to -80C storage.
- **Figures**: None embedded — results reported as a data table linked to an external Google Sheet, no static figures in this post.

---

### Reverse Transcription - R.philippinarum Pooled Gill RNA from 20261027
- **Author**: Sam White
- **Date**: 2026-10-28
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-10-28-Reverse-Transcription---R.philippinarum-Pooled-Gill-RNA-from-20261027/
- **Categories**: Ruditapes philippinarum, Manila clam, reverse transcriptase, cDNA
- **Key finding**: Using the previous day's pooled Manila clam gill RNA, Sam performed reverse transcription with the GoScript Reverse Transcription Kit (Promega), tripling the standard reaction volume (20uL to 60uL) to generate enough cDNA for triplicate qPCR testing of 13 primer sets. The protocol followed manufacturer instructions (300ng RNA, oligo dT priming, standard incubation steps), with an explicit note that the final inactivation incubation is required for valid downstream qPCR; resulting cDNA was stored at -20C after use.
- **Figures**: None — this is a protocol/methods post with calculations linked to an external Google Sheet, no static figures.

---

### qPCR - R.philippinarum Primer Testing
- **Author**: Sam White
- **Date**: 2026-10-28
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-10-28-qPCR---R.philippinarum-Primer-Testing/
- **Categories**: qPCR, Ruditapes philippinarum, Manila clam, primers, CFX Connect
- **Key finding**: Sam screened 13 new Manila clam primer sets (targeting C1qL3, eIF4A3, HPRT, HSF1, IAP, RPS14, Viperin) against pooled gill cDNA on a CFX Connect to assess amplification and specificity (no quantitative analysis performed). 9 of 13 sets amplified with clean single melt peaks and no NTC contamination, yielding one validated working primer set each for eIF4A3 (two sets), IAP, Viperin, and HSF1; HPRT and both C1qL3 sets failed to amplify, one RPS14 set showed primer dimer in NTCs, and several other sets showed inefficient "late" amplification (Cq ~35-36) and were deprioritized in favor of better-performing sets for the same gene.
- **Figures**:
  - local: ./SRID-1850.1-amp-plots.png, ./SRID-1850.1-melt-plots.png (HPRT)
  - local: ./SRID-1852.3-amp-plots.png, ./SRID-1852.3-melt-plots.png (RPS14)
  - local: ./SRID-1854.5-amp-plots.png, ./SRID-1854.5-melt-plots.png (RPS14)
  - local: ./SRID-1856.7-amp-plots.png, ./SRID-1856.7-melt-plots.png (eIF4A3)
  - local: ./SRID-1858.9-amp-plots.png, ./SRID-1858.9-melt-plots.png (eIF4A3)
  - local: ./SRID-1860.1-amp-plots.png, ./SRID-1860.1-melt-plots.png (C1qL3)
  - local: ./SRID-1862.3-amp-plots.png, ./SRID-1862.3-melt-plots.png (C1qL3)
  - local: ./SRID-1864.5-amp-plots.png, ./SRID-1864.5-melt-plots.png (IAP)
  - local: ./SRID-1866.7-amp-plots.png, ./SRID-1866.7-melt-plots.png (IAP)
  - local: ./SRID-1868.9-amp-plots.png, ./SRID-1868.9-melt-plots.png (Viperin)
  - local: ./SRID-1870.1-amp-plots.png, ./SRID-1870.1-melt-plots.png (Viperin)
  - local: ./SRID-1872.3-amp-plots.png, ./SRID-1872.3-melt-plots.png (HSF1)
  - local: ./SRID-1874.5-amp-plots.png, ./SRID-1874.5-melt-plots.png (HSF1)
  - also linked: qPCR PDF report and .pcrd source data file (local, relative paths)

No warnings were reported by the fetch script, and no cosmetic edits or draft posts were found in this window — all three posts are substantive new entries documenting a continuous RNA-to-qPCR primer-validation workflow for Manila clam (R. philippinarum) over 2026-10-27/28.

---

## Grace Crandall's Notebook

### Multispeces - Pycno Day 12 DEG --> enrichment Results
- **Date**: 2026-11-01
- **URL**: https://grace-ac.github.io/musp-pycno-day12/
- **Categories**: MultiSpecies
- **Key finding**: DESeq2 comparison of SSWD-exposed vs. control *P. helianthoides* at Day 12 (samples taken just before exposed animals began showing disease signs) identified 5,686 DEGs (padj<0.05), 4,057 of which have GO annotations. topGO/Fisher enrichment (built with help from Ariana's code) followed by rrvgo term reduction collapsed 177 significant terms down to 47 parent terms. Open questions noted include whether to filter low-count genes before DESeq2 and whether figures should show BH-adjusted vs. raw Fisher p-values; next steps are code review and moving toward paper results.
- **Figures**:
  - local: ../notebook-images/2026-11-02/pyno-PCA.png
  - local: ../notebook-images/2026-11-02/pycno-day12-heatmap-top50degs.png
  - local: ../notebook-images/2026-11-02/pycno-volcano-degs.png
  - local: ../notebook-images/2026-11-02/pycno-enrichment-parentGO.png
  - local: ../notebook-images/2026-11-02/revigo-pycno-heatmap.png
  - local: ../notebook-images/2026-11-02/revigo-bubbleplot-pycno.png
  - local: ../notebook-images/2026-11-02/revigo-wordcloud-pycno.png
  - local: ../notebook-images/2026-11-02/revigo-treemap-pycno.png

---

### Multispeces - Dermasterias Day 12 DEG --> enrichment Results
- **Date**: 2026-11-02
- **URL**: https://grace-ac.github.io/derm-d12/
- **Categories**: MultiSpecies
- **Key finding**: Same DESeq2/topGO/rrvgo pipeline applied to *D. imbricata* at Day 12 (where exposed animals showed no disease signs yet) identified 2,804 DEGs (padj<0.05), 2,231 annotated, with enrichment reducing 195 significant GO terms to 55 parent terms. The post carries the same suite of PCA/heatmap/volcano/enrichment figures and the same open questions about low-count gene filtering and p-value choice for plots, with next steps being code review and progressing toward results/discussion.
- **Figures**:
  - local: ../notebook-images/2026-11-02/derm-pca.png
  - local: ../notebook-images/2026-11-02/derm-top50-deg-heatmap.png
  - local: ../notebook-images/2026-11-02/derm-deg-volcano.png
  - local: ../notebook-images/2026-11-02/derm-enrich-generatio.png
  - local: ../notebook-images/2026-11-02/derm-revigo-heatmap.png
  - local: ../notebook-images/2026-11-02/derm-revigo-bubbleplot.png
  - local: ../notebook-images/2026-11-02/derm-revigo-wordcloud.png
  - local: ../notebook-images/2026-11-02/derm-revigo-treemap.png

---

### Multispeces - Pisaster Day 12 DEG --> enrichment Results
- **Date**: 2026-11-02
- **URL**: https://grace-ac.github.io/pisaster-d12/
- **Categories**: MultiSpecies
- **Key finding**: Same pipeline applied to *P. ochraceus* at Day 12 (where one exposed animal was twisting and another had previously twisted but recovered) identified 4,376 DEGs (padj<0.05), 2,807 annotated, with enrichment reducing 154 significant GO terms to 47 parent terms. Figures mirror the other two species' posts (PCA, heatmap, volcano, enrichment plots), and the same open questions and next steps (code review, drafting paper results) are repeated.
- **Figures**:
  - local: ../notebook-images/2026-11-02/pisaster-PCA.png
  - local: ../notebook-images/2026-11-02/pisaster-top50degs-heatmap.png
  - local: ../notebook-images/2026-11-02/pisaster-deg-volcanoplot.png
  - local: ../notebook-images/2026-11-02/pisaster-enrich-meangeneratio.png
  - local: ../notebook-images/2026-11-02/pisaster-revigo-heatmap.png
  - local: ../notebook-images/2026-11-02/pisaster-revigo-bubbleplot.png
  - local: ../notebook-images/2026-11-02/pisaster-wordcloud.png
  - local: ../notebook-images/2026-11-02/pisaster-revigo-treemap.png

---

Note: all three posts belong to Grace Crandall's Multi-species SSWD RNAseq project (sea stars across three species at Day 12 post-exposure), each running the identical DESeq2 → topGO → rrvgo workflow on a different species. The underlying code/data repository (`grace-ac/project-pycno-multispecies-2023`) remains private pending collaborators' genome publication, so those links are not publicly resolvable yet.

---

## Megan Ewing Lab Notebook

_No new posts in the last 7 days._

---

## Kathleen Durkin Lab Notebook

_No new posts in the last 7 days._

---

## Genefish WordPress

### 10/26 Data collection with AI tool
- **Author**: Christina Zhang
- **Date**: 2026-10-26
- **URL**: https://genefish.wordpress.com/2026/10/26/10-26-data-collection-with-ai-tool/
- **Key finding**: Christina tested an in-house AI (streamlit-based oyster-measurer) tool for extracting oyster dimensions from photos containing many individuals per image. The tool performed well overall, with only a couple of erroneous points needing manual deletion or re-measurement, and results otherwise closely matched manual measurements. She plans to compile a dataset comparing AI vs. manual measurements to help future lab members decide when to use the tool.

---

### Daily Literature Connections — 2026-10-27
- **Author**: Cas Daniel
- **Date**: 2026-10-27
- **URL**: https://genefish.wordpress.com/2026/10/27/daily-literature-connections-2026-10-27/
- **Key finding**: This automated literature post links Christina Zhang's 10/26 AI-measurement finding to a peer-reviewed study using a CNN-based image-segmentation model to grade shell disease severity in a related oyster species with high accuracy. Although the external study measures disease area rather than body dimensions, it independently supports the plausibility that deep-learning pipelines applied to oyster photos can approach manual-assessment accuracy, consistent with the lab's own tool results.

---

### Tank room and water chemistry trial
- **Author**: Jesse Lowe
- **Date**: 2026-10-27
- **URL**: https://genefish.wordpress.com/2026/10/27/tank-room-and-water-chemistry-trial-3/
- **Key finding**: Routine water chemistry checks showed the three main holding tanks (left blue, right blue, right yellow) within normal ranges (30 ppt salinity, pH 7.6-7.8, 0-0.5 nitrite, ~40 nitrate). The dedicated water-chemistry trial tank remained severely degraded (pH 7.4, 80 alkalinity, 0.25+ ammonia, 1.5 nitrite, 60 nitrate), continuing a multi-day pattern of water quality collapse relative to the main tanks.

---

### Daily Literature Connections — 2026-10-28
- **Author**: Cas Daniel
- **Date**: 2026-10-28
- **URL**: https://genefish.wordpress.com/2026/10/28/daily-literature-connections-2026-10-28/
- **Key finding**: This post connects Jesse Lowe's 10/27 trial-tank water chemistry data to a peer-reviewed paper on ammonia transporter genes in Pacific oysters, which found that sustained ammonia exposure drives immune cell death and stress-gene upregulation. The connection supports treating the trial tank's persistently elevated ammonia as a genuine physiological stressor rather than a benign reading; a preprint search could not be completed due to a service outage.

---

### 10.28: GlycogenGlo Analysis (35 C repeat)
- **Author**: HazelAbrahamsonA
- **Date**: 2026-10-28
- **URL**: https://genefish.wordpress.com/2026/10/28/10-28-glycogenglo-analysis-35-c-repeat/
- **Key finding**: Hazel analyzed GlycogenGlo assay data from an experiment testing whether prior stress history affects oyster performance under a repeat 24-hour heat stress (35 C vs. 15 C control). Combined with preliminary summer data, results confirmed that heat stress significantly decreases glycogen, with only partial replenishment during recovery, and showed no significant difference in glycogen levels between oysters with versus without prior stress history during the second exposure. This suggests stress history does not meaningfully alter glycogen metabolism in subsequent stress events.

---

### Daily Literature Connections — 2026-10-29
- **Author**: Cas Daniel
- **Date**: 2026-10-29
- **URL**: https://genefish.wordpress.com/2026/10/29/daily-literature-connections-2026-10-29/
- **Key finding**: This post links Hazel's 10/28 glycogen findings to four peer-reviewed papers, one showing elevated temperature alone reduces glycogen and ATP in the same species, and three others showing glycogen depletion/mobilization is a general stress response across salinity, storage, and energy-deprivation stressors in Crassostrea gigas. No literature was found addressing whether prior stress history specifically blunts the glycogen response to a second stress event, leaving that part of the lab's finding without direct external support or contradiction.

---

### 10.29 – Stress exposure for 35 C experiment
- **Author**: HazelAbrahamsonA
- **Date**: 2026-10-29
- **URL**: https://genefish.wordpress.com/2026/10/29/10-29-stess-exposure-for-35-c-experiment/
- **Key finding**: Hazel initiated the second 24-hour stress (35 C) versus control (15 C) exposure in the ongoing repeat stress experiment. Samples will be collected the following day and used for RNA extraction, reverse transcription, and qPCR analysis.

---

### Image analysis progress 10/29/26
- **Author**: Christina Zhang
- **Date**: 2026-10-29
- **URL**: https://genefish.wordpress.com/2026/10/29/image-analysis-progress-10-29-26/
- **Key finding**: Christina spent one hour performing image analysis on the "10K Baywater" dataset using the oyster-measurer AI tool, nearly completing that batch. This is routine progress on the ongoing AI-assisted image measurement workflow.

---

### Tank room and water chemistry trial
- **Author**: Jesse Lowe
- **Date**: 2026-10-29
- **URL**: https://genefish.wordpress.com/2026/10/29/tank-room-and-water-chemistry-trial-4/
- **Key finding**: Jesse performed a water change on the left blue tank and replaced filters on both blue tanks. Main holding tanks remained within normal ranges, while the water-chemistry trial tank continued to show degraded conditions (0.25+ ammonia, 1.5 nitrite, 60+ nitrate); trial-tank oysters were fed 0.5 mL.

---

### Daily Literature Connections — 2026-10-30
- **Author**: Cas Daniel
- **Date**: 2026-10-30
- **URL**: https://genefish.wordpress.com/2026/10/30/daily-literature-connections-2026-10-30/
- **Key finding**: This post connects the 10/29 trial-tank water chemistry data to three sources: a PubMed paper on ammonia's immune-stress effects in Pacific oysters, a loosely related PubMed paper on nitrogen cycling in oyster aquaculture, and a Research Square preprint (not peer-reviewed) showing combined high alkalinity and disrupted ammonia excretion suppress survival and metabolism in a related Crassostrea species. The preprint is flagged as the most directly relevant, since it addresses the same combination of abnormal parameters (alkalinity and ammonia) seen in the trial tank, though no literature was found addressing the elevated nitrite specifically.

---

### 10.30: Sample collection for 35 C repeat
- **Author**: HazelAbrahamsonA
- **Date**: 2026-10-30
- **URL**: https://genefish.wordpress.com/2026/10/30/10-30-sample-collection-for-35-c-repeat/
- **Key finding**: Hazel concluded the second 24-hour temperature stress (35 C) versus control (15 C) incubation in the repeat stress experiment and collected samples into DNA/RNA shield. These samples will be analyzed via qPCR over the coming weeks to assess gene expression differences related to stress history.

No warnings were reported by the fetch script this week.

---

## Cross-Notebook Patterns & Connections

_This section analyzes the compiled per-source summaries for shared themes, follow-up narratives, apparent contradictions, and multi-week historical connections across the lab's notebooks. Connections are surfaced only when a specific named entity ties the sources together — never from vague thematic similarity._

### Shared Themes
- **C. gigas (Pacific oyster) response to heat/temperature stress** — Ariana Huffmyer's PolyIC qPCR re-analysis found parental Poly(I:C) immune priming significantly altered offspring HSP90 and DNMT1 expression under acute heat stress, most pronounced at 44°C. In the same window, HazelAbrahamsonA's (Genefish WordPress) repeat-stress project found that a second 24-hour 35°C heat exposure significantly depletes glycogen in C. gigas regardless of prior stress history. Both are independent projects studying C. gigas physiological/molecular responses to heat stress, via different pathways (immune priming/gene expression vs. energy metabolism) and different labs.

### Historical Connections
- **PolyIC qPCR data (GAPDH, DNMT1, cGAS, HSP90, VIPERIN)** — Ariana's Oct 29 re-analysis in this window directly builds on a new qPCR batch Sam White ran to increase sample sizes and support re-evaluation of the normalizing gene. See "qPCR - M.gigas Valentina PolyIC GAPDH DNMT1 cGAS HSP90 VIPERIN PolyIC Control Samples" · 2026-10-08 (Sam White, Sam's Notebook): https://robertslab.github.io/sams-notebook/posts/2026/2026-10-08-qPCR---M.gigas-Valentina-PolyIC-GAPDH-DNMT1-cGAS-HSP90-VIPERIN-PolyIC-Control-Samples/
- **Repeat 35°C heat stress experiment (C. gigas)** — HazelAbrahamsonA's second-exposure glycogen analysis and sample collection this window are the continuation of the same repeat-stress design first launched a few weeks earlier. See "10.01: Starting repeat stress at 35 C" · 2026-10-02 (HazelAbrahamsonA, Genefish WordPress): https://genefish.wordpress.com/2026/10/02/10-01-starting-repeat-stress-at-35-c/
- **Sea star wasting disease (SSWD) susceptibility across Pycnopodia, Pisaster, and Dermasterias** — Grace Crandall's Day 12 DEG/enrichment results for all three species this window follow directly from Steven Roberts' susceptibility ranking of the same three species (Pycnopodia most susceptible > Pisaster intermediate > Dermasterias least susceptible). See "The Pathogen Has a Plan, the Hosts Do Not" · 2026-09-11 (Steven Roberts, Tumbling Oysters): https://sr320.github.io/tumbling-oysters/posts/87-seastar-susceptibility-genomics/
- **Starfish interspecies comparative transcriptomics project** — Grace's three Day 12 DEG/enrichment posts this window are the latest installment of the same multi-species comparative transcriptomics project profiled in a genefish WordPress roadmap post. See "Starfish Interspecies Comparative Transcriptomics Project; Where It's Been and Where It's Headed" · 2026-10-15 (Samuel Slutz, Genefish WordPress): https://genefish.wordpress.com/2026/10/15/starfish-interspecies-comparative-transcriptomics-project-where-its-been-and-where-its-headed/

---

## Data & Figures

_This section consolidates, grouped by source, the figure links and external data/repository links already surfaced in the per-source summaries above. It is a single entry point into the underlying data and figures for this window, not a new analysis._

### Ariana Huffmyer Lab Notebook
- Re-analysis of PolyIC qPCR data with new normalizing gene: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261029/plot1.png?raw=true
- Re-analysis of PolyIC qPCR data with new normalizing gene: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261029/genes.png?raw=true
- Re-analysis of PolyIC qPCR data with new normalizing gene: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261029/citrate.png?raw=true
- Re-analysis of PolyIC qPCR data with new normalizing gene: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261029/atpsynthase.png?raw=true

### Sam's Notebook (Sam White)
- qPCR - R.philippinarum Primer Testing: ./SRID-1850.1-amp-plots.png, ./SRID-1850.1-melt-plots.png (HPRT)
- qPCR - R.philippinarum Primer Testing: ./SRID-1852.3-amp-plots.png, ./SRID-1852.3-melt-plots.png (RPS14)
- qPCR - R.philippinarum Primer Testing: ./SRID-1854.5-amp-plots.png, ./SRID-1854.5-melt-plots.png (RPS14)
- qPCR - R.philippinarum Primer Testing: ./SRID-1856.7-amp-plots.png, ./SRID-1856.7-melt-plots.png (eIF4A3)
- qPCR - R.philippinarum Primer Testing: ./SRID-1858.9-amp-plots.png, ./SRID-1858.9-melt-plots.png (eIF4A3)
- qPCR - R.philippinarum Primer Testing: ./SRID-1860.1-amp-plots.png, ./SRID-1860.1-melt-plots.png (C1qL3)
- qPCR - R.philippinarum Primer Testing: ./SRID-1862.3-amp-plots.png, ./SRID-1862.3-melt-plots.png (C1qL3)
- qPCR - R.philippinarum Primer Testing: ./SRID-1864.5-amp-plots.png, ./SRID-1864.5-melt-plots.png (IAP)
- qPCR - R.philippinarum Primer Testing: ./SRID-1866.7-amp-plots.png, ./SRID-1866.7-melt-plots.png (IAP)
- qPCR - R.philippinarum Primer Testing: ./SRID-1868.9-amp-plots.png, ./SRID-1868.9-melt-plots.png (Viperin)
- qPCR - R.philippinarum Primer Testing: ./SRID-1870.1-amp-plots.png, ./SRID-1870.1-melt-plots.png (Viperin)
- qPCR - R.philippinarum Primer Testing: ./SRID-1872.3-amp-plots.png, ./SRID-1872.3-melt-plots.png (HSF1)
- qPCR - R.philippinarum Primer Testing: ./SRID-1874.5-amp-plots.png, ./SRID-1874.5-melt-plots.png (HSF1)
- qPCR - R.philippinarum Primer Testing: qPCR PDF report and .pcrd source data file (local, relative paths)

### Grace Crandall's Notebook
- Multispeces - Pycno Day 12: ../notebook-images/2026-11-02/pyno-PCA.png
- Multispeces - Pycno Day 12: ../notebook-images/2026-11-02/pycno-day12-heatmap-top50degs.png
- Multispeces - Pycno Day 12: ../notebook-images/2026-11-02/pycno-volcano-degs.png
- Multispeces - Pycno Day 12: ../notebook-images/2026-11-02/pycno-enrichment-parentGO.png
- Multispeces - Pycno Day 12: ../notebook-images/2026-11-02/revigo-pycno-heatmap.png
- Multispeces - Pycno Day 12: ../notebook-images/2026-11-02/revigo-bubbleplot-pycno.png
- Multispeces - Pycno Day 12: ../notebook-images/2026-11-02/revigo-wordcloud-pycno.png
- Multispeces - Pycno Day 12: ../notebook-images/2026-11-02/revigo-treemap-pycno.png
- Multispeces - Dermasterias Day 12: ../notebook-images/2026-11-02/derm-pca.png
- Multispeces - Dermasterias Day 12: ../notebook-images/2026-11-02/derm-top50-deg-heatmap.png
- Multispeces - Dermasterias Day 12: ../notebook-images/2026-11-02/derm-deg-volcano.png
- Multispeces - Dermasterias Day 12: ../notebook-images/2026-11-02/derm-enrich-generatio.png
- Multispeces - Dermasterias Day 12: ../notebook-images/2026-11-02/derm-revigo-heatmap.png
- Multispeces - Dermasterias Day 12: ../notebook-images/2026-11-02/derm-revigo-bubbleplot.png
- Multispeces - Dermasterias Day 12: ../notebook-images/2026-11-02/derm-revigo-wordcloud.png
- Multispeces - Dermasterias Day 12: ../notebook-images/2026-11-02/derm-revigo-treemap.png
- Multispeces - Pisaster Day 12: ../notebook-images/2026-11-02/pisaster-PCA.png
- Multispeces - Pisaster Day 12: ../notebook-images/2026-11-02/pisaster-top50degs-heatmap.png
- Multispeces - Pisaster Day 12: ../notebook-images/2026-11-02/pisaster-deg-volcanoplot.png
- Multispeces - Pisaster Day 12: ../notebook-images/2026-11-02/pisaster-enrich-meangeneratio.png
- Multispeces - Pisaster Day 12: ../notebook-images/2026-11-02/pisaster-revigo-heatmap.png
- Multispeces - Pisaster Day 12: ../notebook-images/2026-11-02/pisaster-revigo-bubbleplot.png
- Multispeces - Pisaster Day 12: ../notebook-images/2026-11-02/pisaster-wordcloud.png
- Multispeces - Pisaster Day 12: ../notebook-images/2026-11-02/pisaster-revigo-treemap.png

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

### PolyIC immune priming effects on offspring gene expression in Pacific oysters

**Source:** Ariana Huffmyer Lab Notebook
**Finding:** Re-analysis of qPCR data after switching the normalizing gene to cGAS showed that parental Poly(I:C) immune priming significantly increased HSP90 expression and interacted with acute heat stress to increase DNMT1 expression in offspring, most pronounced at 44°C, while Viperin and GAPDH showed no treatment effect.

### Adds context [PubMed]: The RNA sensor MDA5 contributes to the antiviral immune response in Crassostrea gigas by modulating the MAVS-mediated signaling pathway
Xu et al., 2026 · PMID: 41605267 · https://pubmed.ncbi.nlm.nih.gov/41605267/

This study identified CgMDA5, an RNA-sensing receptor in Pacific oysters that is significantly upregulated by poly(I:C) stimulation and binds double-stranded RNA directly, triggering an antiviral signaling cascade through MAVS and downstream interferon-like genes. It establishes a concrete receptor-level mechanism for how poly(I:C) exposure is sensed and transduced into gene-expression changes in C. gigas. This offers mechanistic background for how the broodstock Poly(I:C) exposure in the priming design could plausibly alter downstream regulatory gene expression, though the paper does not test transgenerational effects or thermal tolerance directly.

---

### Adds context [PubMed]: An OASL homologue involved in IFN-like antiviral signal by binding MDA5 in the Pacific oyster Crassostrea gigas
Zeng et al., 2026 · PMID: 41580101 · https://pubmed.ncbi.nlm.nih.gov/41580101/

This study found that CgOASL, an interferon-stimulated gene in C. gigas, is significantly upregulated by poly(I:C) stimulation and physically interacts with the MDA5 receptor to help execute antiviral signaling. It shows that a single poly(I:C) challenge activates a broader, interconnected network of immune-signaling genes in this species, not just one marker. This supports the plausibility that poly(I:C) immune priming leaves a lasting imprint on regulatory gene networks, relevant background for interpreting the lab's finding of altered HSP90/DNMT1 expression in primed offspring.

**Literature summary:** Two peer-reviewed 2026 papers from the same research group characterize poly(I:C)-responsive innate-immune receptor signaling (MDA5, OASL) in Crassostrea gigas, confirming that poly(I:C) reliably activates this species' antiviral gene network at the receptor level. Neither paper tests transgenerational priming or thermal-tolerance gene expression directly, so they provide mechanistic context for the signaling pathway rather than direct support or conflict for the lab's HSP90/DNMT1 finding. No bioRxiv or other preprints were found on this topic in the last 12 months.

---

### Repeat heat stress and glycogen metabolism in Crassostrea gigas

**Source:** Genefish WordPress (HazelAbrahamsonA)
**Finding:** A second 24-hour 35°C heat stress exposure significantly decreased glycogen in C. gigas relative to 15°C controls, with only partial recovery, and glycogen depletion did not differ between oysters with vs. without prior stress history — suggesting stress history does not meaningfully alter glycogen metabolism in a subsequent stress event.

### Supports [PubMed]: Effects of temperature and Nocardia crassostreae on the immune response of the Pacific oyster, Magallana gigas
Mason et al., 2026 · PMID: 42476329 · https://pubmed.ncbi.nlm.nih.gov/42476329/

This study experimentally exposed Pacific oysters to elevated temperature and the pathogen Nocardia crassostreae for 42 days and found that elevated temperature independently reduced glycogen stores, ATP concentration, and haemocyte viability, regardless of infection status. This directly corroborates the lab's finding that heat stress alone drives significant glycogen depletion in C. gigas. The paper adds that temperature and pathogen stress act largely independently rather than synergistically, a distinction the lab's stress-history comparison did not test.

---

### Adds context [PubMed]: Investigating the molecular mechanism of plasmalogen and quality changes in Pacific oyster (Crassostrea gigas) depurated under salinity stress
Song et al., 2026 · PMID: 42169268 · https://pubmed.ncbi.nlm.nih.gov/42169268/

This study tracked glycogen and lipid changes in C. gigas depurated across a range of salinities, finding that high salinity increased glycogen content and immune capacity while low salinity reduced both. It demonstrates that glycogen is a generalizable physiological readout of stress across multiple stressor types in this species, not just heat. This broadens the context for the lab's glycogen-based stress assay, though the stressor tested (salinity) differs from the lab's heat-stress design.

---

### Adds context [PubMed]: Survival-enhancement potential of tea polyphenol-chitosan composites for Pacific oysters (Crassostrea gigas) during anhydrous low-temperature preservation and its multiple mechanisms
Cheng et al., 2026 · PMID: 41950699 · https://pubmed.ncbi.nlm.nih.gov/41950699/

This study found that a protective coating helped C. gigas maintain higher glycogen levels and better survival during cold, anhydrous low-temperature storage compared to untreated controls. It reinforces that glycogen depletion is a sensitive, consistent indicator of physiological strain under temperature-related stress in this species, in this case cold rather than heat exposure. This is complementary background for interpreting glycogen as a stress biomarker, though the stress direction (cold storage vs. acute heat) differs from the lab's design.

---

### Adds context [PubMed]: Glycophagy is an ancient bilaterian pathway supporting metabolic adaptation through STBD1 structural evolution
Ren et al., 2026 · PMID: 41559265 · https://pubmed.ncbi.nlm.nih.gov/41559265/

This study identified the glycogen cargo receptor STBD1 in C. gigas and showed that the species uses glycophagy (autophagic glycogen breakdown) to mobilize glycogen reserves during energy deprivation. It provides a plausible molecular mechanism for the glycogen depletion the lab observes under heat stress, and suggests a pathway (glycophagy flux) that could be probed to understand why recovery is only partial. This is background on the underlying mobilization mechanism rather than a direct test of stress history effects.

**Literature summary:** One peer-reviewed paper directly supports the lab's core finding that heat stress depletes glycogen in C. gigas, independent of other stressors. Three additional peer-reviewed papers add context by showing glycogen is a broadly stress-responsive reserve across other stressor types (salinity, cold storage) in the same species, and by identifying the glycophagy/STBD1 pathway as a likely mechanism underlying glycogen mobilization. None of the four papers specifically tested whether prior stress history blunts the glycogen response to a second stress event, so the lab's novel stress-history result remains without direct external support or conflict. No preprints were found on this topic in the last 12 months.

---

### Manila clam (Ruditapes philippinarum) qPCR gene expression methodology

**Source:** Sam's Notebook (Sam White)
**Finding:** Screening of 13 new Manila clam primer sets against pooled gill cDNA validated working qPCR primers for eIF4A3, IAP, Viperin, and HSF1 (among others), while HPRT and C1qL3 primers failed to amplify — establishing a qPCR toolkit for future Manila clam gene expression work.

### Adds context [PubMed]: Genome-wide identification and comparative analysis of Leucine-Rich Repeat Containing (LRRC) gene and their expression responses to Vibrio alginolyticus infection in the Manila clam (Ruditapes philippinarum)
Wang et al., 2026 · PMID: 42727169 · https://pubmed.ncbi.nlm.nih.gov/42727169/

This study characterized a large family of leucine-rich repeat-containing immune genes in the Manila clam and used qPCR to profile their expression changes following Vibrio alginolyticus challenge, finding diverse response patterns across family members. It demonstrates that qPCR-based gene expression profiling of immune-related genes is an established, active approach in this species. This supports the relevance of Sam's newly validated primer panel, several of which target immune-related genes (e.g., IAP, Viperin), for future Manila clam immune/stress expression studies.

**Literature summary:** One peer-reviewed paper confirms that qPCR-based expression profiling of immune-related gene families is a current, active research method in Ruditapes philippinarum, supporting the utility of the primer panel validated this week, though it does not test the specific genes Sam validated or address primer design itself. No preprints were found on this topic in the last 12 months.

---

### Sea star wasting disease (SSWD) susceptibility and transcriptomic response across species

**Source:** Grace Crandall's Notebook
**Finding:** DESeq2/GO enrichment analysis of Day 12 post-SSWD-exposure samples across three sea star species (Pycnopodia helianthoides, Dermasterias imbricata, Pisaster ochraceus) identified thousands of differentially expressed genes per species (2,804–5,686 DEGs), with GO enrichment reduced via rrvgo to 47–55 parent terms per species.

### Adds context [PubMed]: A Comparison of Juvenile and Adult Sunflower Sea Star Transcriptomic Responses to Challenge With Sea Star Wasting Disease Tissue Homogenates
Crandall et al., 2026 · PMID: 42780574 · https://pubmed.ncbi.nlm.nih.gov/42780574/

In this peer-reviewed paper by the same research group (including Grace Crandall and Steven Roberts), juvenile and adult Pycnopodia helianthoides were experimentally challenged with SSWD tissue homogenates and compared transcriptomically, finding a shared core response to disease challenge across age classes, including genes related to defense response to bacterium, development, and stress/metabolism regulation. This establishes the precedent transcriptomic framework (disease challenge, differential expression analysis, functional annotation) that the current multi-species Day 12 DEG/enrichment analysis extends from a single-species age comparison to a three-species susceptibility comparison. It supports the general premise that SSWD exposure triggers substantial, functionally organized transcriptional responses in sea stars.

---

### Adds context [PubMed]: Precursors of sea star wasting: immune and microbial disruption during initial disease outbreak in southeast Alaska
McCracken et al., 2026 · PMID: 42014077 · https://pubmed.ncbi.nlm.nih.gov/42014077/

This study found that wild Pycnopodia helianthoides exposed to SSWD but not yet showing visible disease signs already had elevated expression of complement system, pathogen recognition, and immune regulatory genes, alongside signs of tissue remodeling. This gives a specific, independently observed set of immune pathways likely to appear among the thousands of DEGs and enriched GO terms Grace's Day 12 analysis identified in Pycnopodia, since Day 12 in her design was also described as pre-symptomatic for that species. It suggests immune/complement pathway terms are a promising place to look when interpreting which of the 47 parent GO terms are most biologically meaningful.

**Literature summary:** Two peer-reviewed papers support interpreting this week's multi-species DEG/enrichment results: one, co-authored by the same lab, establishes the transcriptomic disease-challenge framework the current analysis builds on; the other, from an independent group, identifies specific immune and tissue-remodeling pathways activated in pre-symptomatic Pycnopodia, pointing to candidate biological signal within the thousands of DEGs now being filtered through GO enrichment. No preprints were found on this topic in the last 12 months.

---

> Generated by the `full-lab-digest` skill · 2026-10-26 to 2026-11-02 (7-day window)
