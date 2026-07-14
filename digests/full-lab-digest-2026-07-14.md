# Full Lab Digest — 2026-07-07 to 2026-07-14

> 5 of 5 sources had activity this week. 0 had none.

---

## Tumbling Oysters (Steven Roberts)

> Summarized from [sr320/tumbling-oysters](https://github.com/sr320/tumbling-oysters)

Three posts were added or updated across five commits, spanning two projects (mussel methylation and lake trout epigenetics) and one sea star disease study. Ordered chronologically:

### The case of the missing mussel
- **Date**: 2026-07-08
- **URL**: https://github.com/sr320/tumbling-oysters/tree/main/posts/83-mytilus-reboot

A Puget Sound mussel sample (93M) believed to be a low-quality dropout from a study of PAH pollution and DNA methylation was discovered to have been simply never fully processed — its raw sequencing reads were a completely normal size. After running it through the same WGBS pipeline as the other 23 *Mytilus trossulus* samples, it came in 14th of 24 by overall methylation, indistinguishable from the rest. The post also delivers the first complete baseline methylome landscape for all 24 mussels: methylation is low (~12%), on/off mosaic in distribution, concentrated in gene bodies rather than promoters, and corroborated by the genome's own CpG-depletion fossil record — all consistent with the known invertebrate pattern.

### Reading Methylation on Each Fish's Own Genome
- **Date**: 2026-07-09
- **URL**: https://github.com/sr320/tumbling-oysters/tree/main/posts/84-trout-meth

To address a long-standing reference-genome bias in lake trout epigenetics, PacBio methylation reads for lean and siscowet ecotypes were each realigned to their own ecotype's assembled genome, and differences were assessed gene-by-gene (using shared gene IDs as a coordinate-free common language). Of 10,838 testable genes, 63 showed nominal methylation differences between ecotypes, but none survived multiple-testing correction and none of the ~180 previously flagged reference-based signals were confirmed. The result is attributed to underpowering (four fish per group, uneven coverage) rather than a definitive absence of biology, and it reinforces the project's central finding that signals depending heavily on a single reference genome weaken once that bias is removed.

### What Genes Reveal About Sea Star Wasting Disease
- **Date**: 2026-07-10
- **URL**: https://github.com/sr320/tumbling-oysters/tree/main/posts/85-seastar-wasting-go

Day-12 differentially expressed genes from three Pacific sea star species — sunflower star (*Pycnopodia helianthoides*), ochre star (*Pisaster ochraceus*), and leather star (*Dermasterias imbricata*) — were compared via Gene Ontology enrichment analysis using ortholog-matched gene families to ensure a fair cross-species comparison. Each species produced hundreds of uniquely enriched biological functions, but eight were shared across all three: stress granule assembly, protein kinase signaling, ubiquitin-ligase adaptor activity, trans-Golgi/axon transport, adherens junction organization, and PPAR metabolic signaling. This conserved core points to a common disease response centered on emergency stress signaling, protein quality control, and breakdown of tissue adhesion machinery — consistent with sea star wasting disease's hallmark of literal tissue disintegration.

---

## Ariana Huffmyer Lab Notebook

> Summarized from [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io)

### July Goals and Daily Entries
- **Date**: 2026-07-01
- **URL**: https://ahuffmyer.github.io/posts/2026-07-01-goals.qmd

This post outlines Ariana's goals for July 2026 across writing/manuscripts, grants, analysis, and field/lab work, with priorities including submitting the PolyIC paper, applying for an NSF IOS grant, and continuing oyster outplants at Westcott and hardening at Point Whitney. Daily log entries track activities through the month, including Manchester cage cleaning, growth/survival data assembly for SHIELD, and meetings on oyster image analysis and metabolomics. The post serves as a running log updated throughout the month.

### Week 6 of Seed Hardening at Point Whitney
- **Date**: 2026-07-06
- **URL**: https://ahuffmyer.github.io/posts/2026-07-06-point-whitney-seed-hardening.qmd

This post documents the sixth week of thermal hardening treatments on Pacific oyster (*C. gigas*) seed at the Point Whitney hatchery, part of an ongoing conditioning experiment. Because ambient seawater temperatures have risen to 20–22°C with warmer weather, the hardening treatment temperature was increased to 36°C to maintain a consistent +10°C differential over controls. The 30-minute heat stress was applied in a 5-gallon bucket with a recirculating pump and thermostat, with both treatment and control groups monitored via temperature loggers.

### Oyster Image Size Analysis Protocol
- **Date**: 2026-07-07
- **URL**: https://ahuffmyer.github.io/posts/2026-07-07-oyster-image-analysis-protocol.qmd

This post presents a step-by-step protocol for measuring oyster size (length and width) from field images using ImageJ/Fiji, adapted from Noah Krebs' existing lab notebook protocol. The workflow covers setting up a data sheet, annotating individual oysters with numbered points, calibrating a scale bar from a field caliper, and recording maximum shell length and width measurements for each oyster in millimeters. The protocol is designed for use with outplanted oysters photographed in the field, enabling consistent, reproducible size tracking across images.

---

## Sam's Notebook (Sam White)

> Summarized from [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook)

### qPCR Analysis - M.gigas PolyIC Data from Valentina's Project
- **Date**: 2026-02-02 *(index.qmd revised/re-knit this week)*
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-02-02-qPCR-Analysis---M.gigas-PolyIC-Data-from-Valentinas-Project/

This post analyzes qPCR gene expression data from Pacific oysters (*Magallana gigas*) treated with PolyIC (a synthetic viral mimic) and subjected to temperature, mechanical, or no additional stress, targeting eight genes normalized to GAPDH. Two-way ANOVA revealed that HSP70 was strongly upregulated by temperature stress regardless of PolyIC treatment, while VIPERIN was specifically induced by PolyIC alone. HSP90 showed a synergistic-like elevation specifically in the PolyIC + temperature combination, whereas cGAS and DNMT1 showed no significant response to any treatment, suggesting that immune sensing via PolyIC in oysters occurs through pathways other than cGAS.

### Resazurin Assays - USDA M.gigas Families in Response to Temperature Stress
- **Date**: 2026-07-13
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-07-13-Resazurin-Assays---USDA-M.gigas-Families-in-Response-to-Temperature-Stress/

Twenty adult Pacific oysters from each of four USDA families (1, 5, 7, and 9) were exposed to 36°C acute heat stress for four hours, and metabolic activity was tracked via resazurin fluorescence normalized to shell area. Family significantly affected size-normalized metabolic rate (AUC ANOVA: F=4.37, p=0.0069), with a significant time-by-family interaction emerging by 1.5 hours and strengthening through the full four-hour period (LME: p=0.0006). Family 7 had the highest mean metabolic activity and Family 9 the lowest, with this contrast being the only significant pairwise difference (Tukey: p=0.0051); Families 1 and 5 were intermediate and not significantly different from any other family.

---

## Grace Crandall's Notebook

> Summarized from [grace-ac/grace-ac.github.io](https://github.com/grace-ac/grace-ac.github.io)

### FHL 2026 Water Filter DNA Extractions Part 2
- **Date**: 2026-07-07
- **URL**: https://grace-ac.github.io/waterfilter-dna-part2/

This post documents the second batch of DNA extractions from 23 half-sections of 0.45 µm water filters (plus one blank control) using the ZymoBIOMICS DNA Miniprep Kit (D4300), covering treatments including eelgrass, mussel, *V. pectenicida*, and seawater controls. A centrifuge error in FTR 213 required shuttling between rooms, and during elution a tube rack fell, raising a potential cross-contamination concern for sample F_T0_01 — the remaining filter halves in -80°C storage provide a fallback for re-extraction if qPCR results look anomalous. Separately, a delayed delivery notification revealed that a TaqMan Fast Universal PCR Master Mix reagent had been sitting in central receiving since June 26; a customer service call confirmed it likely remained liquid and should be vortexed before use to check for precipitate.

### FHL 2026 Water Filter DNA Extractions Part 3
- **Date**: 2026-07-08
- **URL**: https://grace-ac.github.io/fhlfilter-dnaextraction-part3/

This post records the third batch of DNA extractions, processing 17 half-sections of 0.45 µm water filters spanning treatments such as eelgrass plus seawater, eelgrass plus *V. pectenicida*, mussel plus seawater, mussel shell plus seawater, and seawater-only controls, along with one blank. The protocol proceeded without major incident — an optional mid-protocol stopping point was taken for a meal break — and all extracted DNA was stored in the same -80°C box as previous batches in FTR. Next steps are to complete the remaining 18 filters during the week of July 21 (after travel July 10–20) and then run 2 µL of each extract on qPCR to detect *V. pectenicida* in late July.

---

## Genefish WordPress

> Summarized from [genefish.wordpress.com](https://genefish.wordpress.com)

### Mortality assessments
- **Author**: naomikang44 · **Date**: 2026-07-07
- **URL**: https://genefish.wordpress.com/2026/07/07/mortality-assessments/

Jesse and Naomi conducted the 20-hour mortality check on nine oyster families following 35°C heat exposure in the tank room (grey "Meredith" bin). Mortality status (alive = 0, dead = 1) and shell length for deceased individuals were recorded in a shared spreadsheet. This represented an early time point in what became an ongoing multi-day mortality tracking effort.

### Water quality testing, heat exposure, and mortality assessments
- **Author**: Jesse Lowe · **Date**: 2026-07-07
- **URL**: https://genefish.wordpress.com/2026/07/07/water-quality-testing-heat-exposure-and-mortality-assessments/

Jesse recorded water quality parameters across all four holding tanks (two blue, two yellow), all at 30 ppt salinity with pH in the 7.8–8 range, though the right blue tank showed elevated nitrite (3 ppm) and nitrate (80 ppm). A 30-minute heat exposure was run on oysters from the left blue tank in 25.4°C water. Mortality assessments were also completed as part of the ongoing heat stress trial.

### Heat exposure and mortality assessments
- **Author**: naomikang44 · **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/heat-exposure-and-mortality-assessments/

Jesse, Grace, and Naomi performed the 43-hour mortality assessment on nine oyster families held in 30 ppt water (grey Meredith bin) and 9 ppt water, both under 35°C heat exposure. Results were logged in the shared spreadsheet comparing performance across salinity treatments. This was an intermediate time point in the multi-day exposure trial spanning several salinity conditions.

### Repeat stress prelim — RNA quantification
- **Author**: HazelAbrahamsonA · **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/repeat-stress-prelim-rna-quantification/

Hazel used the Qubit RNA HS Assay Kit to quantify RNA previously extracted from oyster samples in a preliminary repeat heat stress experiment, yielding an average of approximately 30 ng/µL per sample. The quantification results were uploaded to GitHub and confirmed the samples are suitable for downstream work. The next step is reverse transcription to cDNA for use in qPCR targeting metabolic and stress-response genes (ATP synthase, citrate synthase, HSP70, HSP90).

### Water quality testing, heat exposure, and mortality assessments
- **Author**: Jesse Lowe · **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/water-quality-testing-heat-exposure-and-mortality-assessments-2/

Jesse recorded daily water quality checks across the four tanks, noting that the right blue tank continued to show low ammonia and elevated nitrite, and performed a full water change on the right yellow tank (manila clams). A heat exposure was run on left blue tank oysters, and mortality assessments were completed in parallel with the ongoing multi-day trial.

### More Claude skills: Marine Species Resolver + Phylogenetic tree builder
- **Author**: Cas Daniel · **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/more-claude-skills-marine-species-resolver-phylogenetic-tree-builder/

Cas extended a Claude Code tool originally built to query the World Register of Marine Species (WoRMS) for taxonomy and accepted scientific names, adding a new phylogenetic tree-building capability. The combined workflow allows a user to look up any marine species, retrieve taxonomic metadata, and automatically generate a visual phylogenetic tree. These skills are intended as reusable agents that can be invoked by other tools in the lab's growing Claude-based toolkit.

### Lab Notebook Summarizer: Building a Weekly Digest Tool
- **Author**: Cas Daniel · **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/lab-notebook-summarizer-building-a-weekly-digest-tool/

Cas built an automated weekly digest tool that queries the Roberts Lab WordPress notebook via the public API, groups posts by author, and generates a readable summary of the week's activity. The project lives at https://github.com/ckdan19/LabNotebook-Summarizer and consists of a Python fetch script and a Claude-based summarization layer. The goal is to give the whole lab an at-a-glance overview each week without requiring manual curation.

### Guava Muse successfully read
- **Author**: Christina Zhang · **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/guava-muse-successfully-read/

Christina troubleshot the Guava Muse flow cytometer, running two rounds of system-check backflush and complete cleaning cycles before a different check kit successfully passed validation. The original check kit had consistently returned values that were too low. The next planned step is to run the mitochondria kit and identify which organism's tissue is appropriate for the assay.

### Heat exposure and freshwater mortality assessments
- **Author**: naomikang44 · **Date**: 2026-07-09
- **URL**: https://genefish.wordpress.com/2026/07/09/heat-exposure-and-freshwater-mortality-assessments/

Jesse, Grace, and Naomi assessed mortality on nine oyster families at the 67-hour mark under 35°C heat exposure in both 30 ppt and 9 ppt (~11 ppt) water, and additionally assessed freshwater-exposed families at the 44-hour mark. A key finding was that oyster families in higher-salinity (30 ppt) water showed substantially higher mortality rates than those in lower-salinity (9 ppt) water. Early freshwater exposure data were also collected but showed lower mortality across families at that time point.

### "Oyster_measurer" in progress
- **Author**: Christina Zhang · **Date**: 2026-07-09
- **URL**: https://genefish.wordpress.com/2026/07/09/oyster_measurer-in-progress/

Christina began developing an AI agent called "oyster_measurer" that takes images of oysters and automatically calibrates scale from a ruler in the photo, identifies individual oysters against cluttered backgrounds, and measures each oyster's longest dimension and a perpendicular width. The tool aims to streamline morphometric data collection that would otherwise require manual measurement. It is still in development and being refined for accuracy.

### Water quality testing, heat exposure, and mortality assessments
- **Author**: Jesse Lowe · **Date**: 2026-07-09
- **URL**: https://genefish.wordpress.com/2026/07/09/water-quality-testing-heat-exposure-and-mortality-assessments-3/

Jesse recorded water quality across all four tanks, with the right blue tank again showing elevated nitrite (3 ppm) and nitrate (60 ppm). A heat exposure was run on left blue tank oysters in approximately 25°C water, and mortality assessments were conducted as part of the ongoing multi-day trial. Tank maintenance and monitoring continued as standard daily operations.

### Lab Notebook Summarizer — More additions & Exploration
- **Author**: Cas Daniel · **Date**: 2026-07-09
- **URL**: https://genefish.wordpress.com/2026/07/09/lab-notebook-summarizer-more-additions-exploration/

Cas expanded the lab notebook digest tool to cover individual GitHub-based lab notebooks in addition to the shared WordPress blog, creating dedicated Claude Code subagents for each lab member rather than relying on a single monolithic script. Each subagent is tailored to know the structure and format of that specific person's notebook, reducing token overhead and improving summary quality. This modular subagent architecture was tested and documented as a step toward a unified multi-source weekly digest.

### Heat exposure, freshwater, and mortality assessments continued
- **Author**: naomikang44 · **Date**: 2026-07-10
- **URL**: https://genefish.wordpress.com/2026/07/10/heat-exposure-freshwater-and-mortality-assessments-continued/

Jesse and Naomi performed the 92-hour (30 ppt) and 91-hour (9 ppt) mortality assessments on nine oyster families under 35°C heat exposure, along with a 69-hour freshwater exposure check. Results were again consistent with the trend that 9 ppt families showed lower mortality than 30 ppt families, with relatively little change from the previous day's counts. The data continue to accumulate toward a comparative analysis of how salinity affects heat stress tolerance across families.

### Water quality testing, PolyIC priming, heat exposure, and mortality assessments
- **Author**: Jesse Lowe · **Date**: 2026-07-10
- **URL**: https://genefish.wordpress.com/2026/07/10/water-quality-testing-polyic-priming/

Jesse completed routine water quality checks across all four tanks and administered a PolyIC priming treatment to a group of shellfish, a method used to stimulate innate immune responses. A heat exposure was run concurrently, and mortality assessments were performed as part of the ongoing multi-day trial. The addition of PolyIC priming suggests the lab is beginning to layer immune challenges on top of heat stress exposures.

### Water quality testing, heat exposure, and clam counts
- **Author**: Jesse Lowe · **Date**: 2026-07-12
- **URL**: https://genefish.wordpress.com/2026/07/12/water-quality-testing-heat-exposure-and-clam-counts/

Jesse recorded water quality for both blue tanks, noting the right blue tank still had detectable nitrite (1 ppm) and elevated nitrate (40 ppm), and ran a 30-minute heat exposure on left blue tank oysters. Jesse and Megan counted and bagged manila clams and cockles in preparation for transport the following day to the Suquamish field site. Clam bag sewing continued in preparation for deployment.

### Repeat Stress Prelim — cDNA synthesis
- **Author**: HazelAbrahamsonA · **Date**: 2026-07-13
- **URL**: https://genefish.wordpress.com/2026/07/13/repeat-stress-prelim-cdna-synthesis/

Hazel synthesized cDNA from RNA previously extracted and quantified in the repeat heat stress preliminary experiment, which is designed to investigate whether prior heat exposure can induce a thermal priming effect in oysters. The resulting cDNA will be used in qPCR to examine expression of metabolic genes (ATP synthase, citrate synthase) and stress-response genes (HSP70, HSP90). This step completes the RNA-to-cDNA phase and moves the experiment into the gene expression analysis stage.

### SORMI resazurin assays and mortality assessments
- **Author**: naomikang44 · **Date**: 2026-07-13
- **URL**: https://genefish.wordpress.com/2026/07/13/sormi-resazurin-assays-and-mortality-assessments/

Naomi and Sam conducted resazurin metabolic assays on 20 oysters each from Families 1, 5, 7, and 9 — representing the best and worst performers from earlier 30 ppt mortality trials — by placing them at 35°C for 4 hours and sampling every 30 minutes to track fluorescence as a proxy for metabolic activity. Naomi and Dr. Roberts also completed final mortality assessment rounds for oyster families held in 30 ppt and 9 ppt water, though several data inconsistencies were noted. Together, these datasets are building toward a profile of which oyster families are both tolerant and metabolically active under heat stress.

### Lab Notebook Digest Updates
- **Author**: Cas Daniel · **Date**: 2026-07-13
- **URL**: https://genefish.wordpress.com/2026/07/13/lab-notebook-digest-updates/

Cas finished building the final subagents for all active GitHub-based lab notebooks (including Sam and Grace), completing the set of five subagents that each know how to summarize a specific lab member's notebook. A wrapping subagent was also created to handle the weekly WordPress digest. With all subagents in place, Cas tested an end-to-end workflow where the main agent collects summaries from all five subagents and compiles them into a single cross-lab Markdown digest.

### Water quality, mortality assessments, and H2O2 exposure
- **Author**: Jesse Lowe · **Date**: 2026-07-14
- **URL**: https://genefish.wordpress.com/2026/07/14/water-quality-mortality-assessments-and-h2o2-exposure/

Jesse performed full water changes on both blue tanks, restoring all parameters to 30 ppt salinity and stable pH and alkalinity. Mortality assessments at the 164-hour mark (after 36°C heat exposure in freshwater overnight) found only one death — in Family 6 — though salinity had increased inside each individual tripour during incubation. Jesse then initiated a new hydrogen peroxide exposure trial, placing 20 oysters per family from all nine families into tripours with 500 mL freshwater and 40 mL H₂O₂.

---

## Cross-Notebook Patterns & Connections

### Shared Themes

- **Oyster image size measurement from photos** — Ariana Huffmyer posted a formal ImageJ/Fiji protocol for measuring oyster shell length and width from field photographs (2026-07-07). Independently, Christina Zhang (WordPress, 2026-07-09) began building an AI agent ("oyster_measurer") to automate the same ruler-calibrated length/width measurements from photos. Both are working on the same specific measurement task (shell length + width from images with a ruler), on the same organism, using the photo-to-millimeter approach as the common thread. Ariana's protocol also notes a meeting on "oyster image analysis" in her July goals log, suggesting the two efforts may be related or coordinated.

- **PolyIC immune priming in *M. gigas*** — Sam White's re-knit qPCR post (revised this week) delivers formal gene expression results from a PolyIC priming × temperature stress factorial in Pacific oysters, showing HSP70 upregulation by heat and VIPERIN induction by PolyIC. Ariana's July goals log (updated this week) lists "submitting the PolyIC paper" as a top priority. Jesse Lowe (WordPress, 2026-07-10) also administered PolyIC to shellfish in the tank room this week. PolyIC is a specific named treatment linking all three sources — the manuscript stage (Ariana), the formal analysis (Sam), and active lab application (Jesse).

- **HSP70, HSP90, ATP synthase, and citrate synthase as qPCR targets** — Sam White's PolyIC qPCR analysis (revised this week) used HSP70, HSP90, ATP synthase, and citrate synthase as target genes in *M. gigas* heat stress experiments. Hazel Abrahamson (WordPress, 2026-07-08 and 2026-07-13) is preparing qPCR from a separate repeat heat stress experiment targeting the same four genes in oysters. Both are using qPCR on the same species with the same named gene panel, making this a strong methodological overlap that could support cross-experiment comparison once Hazel's results are in.

- **Resazurin metabolic assays on USDA oyster families 1, 5, 7, and 9** — Sam White (sams-notebook, 2026-07-13) and Naomi Kang (WordPress, 2026-07-13) both document the same resazurin assay run on the same four USDA *M. gigas* families on the same day. Sam's post provides formal statistical results (Family 7 highest metabolic activity, Family 9 lowest; Tukey p=0.0051), while Naomi's post describes the experimental execution and broader mortality context. These are two notebook entries for the same experiment, providing complementary views of both the method and the analysis.

### Temporal Narratives

- **Resazurin experiment: bench → analysis on the same day** — Naomi's WordPress post (2026-07-13) records the execution of the resazurin assay (loading oysters into the incubator, sampling every 30 minutes), while Sam's notebook entry from the same day (2026-07-13) delivers the full statistical analysis: ANOVA, linear mixed effects model, and Tukey post-hoc tests with specific p-values. The two entries together form a same-day lab-to-analysis pipeline documented across two notebooks, with Sam's formal results directly answering the family-level question Naomi's post raised about which families are most metabolically active under heat stress.

- **Hazel's repeat heat stress pipeline across the week** — Hazel's RNA quantification post (WordPress, 2026-07-08) follows RNA extraction done the prior week; her cDNA synthesis post (WordPress, 2026-07-13) follows from that quantification result (~30 ng/µL confirmed sufficient). The pipeline is visibly advancing within this single week toward qPCR, and Sam's existing qPCR results on the same four gene targets (HSP70, HSP90, ATP synthase, citrate synthase, revised this week in sams-notebook) represent a directly comparable dataset Hazel's results will be able to speak to.

---

> Generated by the `full-lab-digest` skill · 2026-07-07 to 2026-07-14
