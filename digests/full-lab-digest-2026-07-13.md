# Full Lab Digest — 2026-07-07 to 2026-07-13

> 5 of 5 sources had activity this week. 0 had none.

---

## Tumbling Oysters (Steven Roberts)

## sr320/tumbling-oysters — Posts from the Last 7 Days (2026-07-06 to 2026-07-13)

Four posts were updated or created across four commits. All are by Steven Roberts and fall under Genomics and/or Transcriptomics.

---

### Two-Genome Evidence
**Date**: 2026-07-07 | **Categories**: Genomics, Computing
**URL**: `posts/82-trout-recip-pav/index.qmd`

This post recasts the lean vs. siscowet lake trout comparison by running reciprocal presence/absence variation (PAV) analysis on each ecotype's own assembled genome, eliminating the lean-reference bias that had shaped all prior results. Integrating six independent lines of evidence, 2,895 genes were flagged by at least two native methods, with 109 genes supported by three or more. The key outcome is a striking bifurcation: the depth-adaptation calcium-channel signal (FDR 9×10⁻⁴) is robust to removing reference bias, while the previously reported lipid/buoyancy signal disappears entirely — suggesting it was largely a reference artifact.

---

### The case of the missing mussel
**Date**: 2026-07-08 | **Categories**: Genomics, Computing
**URL**: `posts/83-mytilus-reboot/index.qmd`

A Puget Sound bay mussel sample (93M, from the Smith Cove industrial site) had been logged as a low-quality dropout, but investigation revealed it had simply never been fully processed — only a small 10,000-read test run existed. After running the full whole-genome bisulfite sequencing pipeline, 93M produced 17.2 million CpG sites at 11.65% overall methylation, landing squarely in the middle of the 24-mussel cohort. The completed dataset establishes that *M. trossulus* methylation is low (~12%), bimodally distributed (on/off mosaic), and concentrated in gene bodies — and that CpG depletion in genes serves as a fossil record corroborating their long-term methylation history.

---

### Reading Methylation on Each Fish's Own Genome
**Date**: 2026-07-09 | **Categories**: Genomics, Computing
**URL**: `posts/84-trout-meth/index.qmd`

Building on the two-genome framework established in the prior post, lean and siscowet lake trout PacBio reads were each aligned to their own ecotype's assembled genome, and methylation was compared using shared gene IDs as a coordinate-system-agnostic bridge. Of 10,838 testable genes, 63 showed nominal differences between ecotypes, but none survived multiple-testing correction, and none of the ~180 previously identified reference-based differentially methylated regions were confirmed. The null result is attributed primarily to low statistical power (four fish per group, uneven coverage) rather than definitive evidence that the earlier signals were artifacts — deeper sequencing is the clear next step.

---

### What Genes Reveal About Sea Star Wasting Disease
**Date**: 2026-07-10 | **Categories**: Transcriptomics, Genomics
**URL**: `posts/85-seastar-wasting-go/index.qmd`

Gene Ontology enrichment was applied to day-12 differentially expressed genes from three sea star species (sunflower star ~6,200 DEGs, ochre star ~6,800, leather star ~3,400), using ortholog-matched genes to enable cross-species comparisons. While each species showed hundreds of species-specific enriched functions, eight functions were shared across all three: stress granule assembly, protein kinase signaling, ubiquitin-ligase adaptor activity, trans-Golgi network activity, adherens junction organization, and PPAR signaling — together describing a picture of cellular stress, protein quality control failure, and loss of tissue adhesion. This conserved core response, consistent across three phylogenetically distinct species, is identified as the most promising window into the central mechanism of sea star wasting disease.

---

## Ariana Huffmyer Lab Notebook

# Ariana Huffmyer Notebook Digest — Week of 2026-07-06 to 2026-07-13

> Summarized from [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io)

---

### July Goals and Daily Entries
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-01
- **Categories**: goals, daily-entries
- **Key finding**: This post outlines Ariana's research priorities for July 2026, spanning manuscript writing (including the PolyIC paper, Hawaii 2023, Moorea 2023, and Westcott priming manuscripts), grant applications (NSF IOS and Moore Foundation), and ongoing analyses (RNAseq and metabolomics). Field and lab activities for the month include oyster outplants at Westcott, seed hardening at Point Whitney, and site check-ups at Sequim, Baywater, and Goose Point. Daily log entries track specific activities from July 1 through July 7, including hatchery trips, Manchester sampling, and oyster image analysis work.

---

### Week 6 of seed hardening at Point Whitney
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-06
- **Categories**: hardening, oyster, cgigas, wsg-usda
- **Key finding**: This post documents the sixth week of a thermal hardening experiment on Pacific oyster (*C. gigas*) seed held at the Point Whitney hatchery. Because ambient water temperatures have risen to 20-22°C with warmer weather, the hardening treatment temperature was increased to 36°C to maintain the target +10°C differential over controls. Oysters in the high-temperature group were subjected to a 30-minute heat stress in a temperature-controlled bucket, then returned to ambient upweller tanks, while control oysters remained in their silos throughout.

---

### Oyster image size analysis protocol
- **Author**: Ariana Huffmyer, Noah Krebs
- **Date**: 2026-07-07
- **Categories**: protocol, image, oyster
- **Key finding**: This post provides a step-by-step protocol for measuring oyster size (length and width) from field images using ImageJ/Fiji, building on an existing protocol developed by Noah Krebs. The workflow covers opening images, annotating individual oysters with numbered points, setting a scale bar from an in-image caliper, and recording maximum length and width measurements for each individual. The approach is designed to support growth and survival tracking for oyster outplant experiments.

---

## Sam's Notebook (Sam White)

# Sam White Notebook Digest — Week of 2026-07-06 to 2026-07-13

> Summarized from [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook)

---

### qPCR Analysis - M.gigas PolyIC Data from Valentina's Project

- **Author**: Sam White
- **Date**: 2026-02-02 *(published to repo 2026-07-13)*
- **URL**: https://github.com/RobertsLab/sams-notebook/blob/master/posts/2026/2026-02-02-qPCR-Analysis---M.gigas-PolyIC-Data-from-Valentinas-Project/index.qmd
- **Categories**: qPCR, Pacific oyster, Magallana gigas, Crassostrea gigas, polyIC, HSP70, HSP90, cGAS, VIPERIN, ATP Synthase, Citrate Synthase, DNMT1, GAPDH
- **Key finding**: This post analyzes qPCR gene expression data from Pacific oysters (*Magallana gigas*) treated with PolyIC (a synthetic viral dsRNA mimic) and subjected to temperature stress, mechanical stress, or control conditions, with the goal of measuring immune and stress responses across eight target genes normalized to GAPDH. Two-way ANOVAs revealed that HSP70 was strongly upregulated by temperature stress regardless of PolyIC treatment, while HSP90 showed a distinct response specifically in the PolyIC + temperature combination. VIPERIN, an antiviral effector, was significantly induced by PolyIC alone (independent of stress type), whereas cGAS showed no significant response to any treatment, suggesting that PolyIC recognition in oysters may proceed through alternative immune sensing pathways rather than the cGAS pathway.

---

## Grace Crandall's Notebook

## Grace Crandall Notebook Digest -- Week of 2026-07-06 to 2026-07-13

> Summarized from [grace-ac/grace-ac.github.io](https://github.com/grace-ac/grace-ac.github.io)

---

### Orthogroup - Enrichment Day 12
- **Date**: 2026-07-05
- **URL**: https://grace-ac.github.io/enrichment/
- **Categories**: SRMtg
- **Summary**: Grace tested whether Day 12 differentially expressed genes (DEGs) unique to each of three sea star species -- _Dermasterias imbricata_, _Pisaster ochraceus_, and _Pycnopodia helianthoides_ -- showed functional enrichment when using shared orthogroups across all three species as the DAVID background. No enrichment was detected for any species, meaning the species-specific Day 12 DEG sets did not return any significant GO-term results under this analytical framework.

---

### Agenda for Meeting with Steven Tomorrow
- **Date**: 2026-07-06
- **URL**: https://grace-ac.github.io/SRmtg_agenda/
- **Categories**: SRMtg
- **Summary**: This is a pre-meeting agenda post summarizing two items to discuss with advisor Steven: (1) the null enrichment result from DAVID for Day 12 DEGs using shared orthogroups as the background, and (2) progress on DNA extractions for water filters from the FHL 2026 field experiment. No new analytical results are presented; the post serves as a check-in summary of completed work.

---

### FHL 2026 Water Filter DNA Extractions Part 1
- **Date**: 2026-07-06
- **URL**: https://grace-ac.github.io/fhl-waterfilter-extractinos/
- **Categories**: FHL2026
- **Summary**: Grace extracted DNA from the first batch of 17 half-sections of 0.45 um water filters (plus one extraction blank) collected during the FHL 2026 experiment, using the ZymoBIOMICS DNA MiniPrep Kit (D4300) and eluting into 50 ul of water; remaining filter halves are stored at -80C as backup. The centrifuge in FTR 213 holds only 18 tubes, so future batches were planned using a 24-tube centrifuge. Next steps are to finish the remaining 58 filters and then run qPCR for _Vibrio pectenicida_ detection in late July.

---

### FHL 2026 Water Filter DNA Extractions Part 2
- **Date**: 2026-07-07
- **URL**: https://grace-ac.github.io/waterfilter-dna-part2/
- **Categories**: FHL2026
- **Summary**: Grace processed a second batch of 23 half-filters plus one blank using the same ZymoBIOMICS D4300 protocol, this time using the 24-tube centrifuge in FTR 209 due to an error code on the unit in FTR 213. A handling incident near the final elution step caused tubes to fall, raising a potential cross-contamination concern for one sample (F_T0_01), which received a double elution volume; re-extraction from the archived half-filter is available as a fallback if qPCR results look anomalous. Grace also discovered that a TaqMan Fast Universal PCR Master Mix shipment had been sitting at SAFS for over a week without a delivery notification; a call to the vendor confirmed the reagent appears intact and should be vortexed before use to check for precipitate.

---

### FHL 2026 Water Filter DNA Extractions Part 3
- **Date**: 2026-07-08
- **URL**: https://grace-ac.github.io/fhlfilter-dnaextraction-part3/
- **Categories**: FHL2026
- **Summary**: Grace completed a third DNA extraction batch covering 17 half-filters spanning treatments including eelgrass + seawater, eelgrass + _V. pectenicida_, _V. pectenicida_ + seawater, eelgrass + mussel combinations, mussel + _V. pectenicida_, mussel + seawater, mussel shell + seawater, and seawater controls, plus one blank; all used the ZymoBIOMICS D4300 kit eluting 50 ul into water. The protocol proceeded smoothly with one planned break at the optional stopping point after Step 2. The next extraction batch of 18 remaining filters is scheduled for the week of July 21, with qPCR for _V. pectenicida_ planned for late July.

---

## Genefish WordPress

# genefish WordPress Digest — Week of 2026-07-06 to 2026-07-13

> Summarized from [genefish.wordpress.com](https://genefish.wordpress.com)

---

### Water quality testing, and water changes.
- **Author**: Jesse Lowe
- **Date**: 2026-07-06
- **URL**: https://genefish.wordpress.com/2026/07/06/water-quality-testing-and-water-changes-2/
- **Key finding**: Jesse performed routine maintenance on the lab tanks, conducting a half water change on the right blue tank and a full water change on the right yellow tank. Water quality parameters (salinity, pH, alkalinity, ammonia, nitrite, nitrate) were measured across all four tanks before the changes, with the right blue tank showing slightly elevated ammonia (0.25) and nitrite (3) prior to its water change.

---

### Agentic AI Week 1 Journal
- **Author**: Cas Daniel
- **Date**: 2026-07-06
- **URL**: https://genefish.wordpress.com/2026/07/06/agentic-ai-week-1-journal/
- **Key finding**: Cas reflected on the first week of team meetings covering LLM fundamentals, including tokenization, embeddings, attention mechanisms, and the importance of context window management in agentic workflows. The team also discussed the ethics and environmental costs of generative AI, emphasizing the need for fact-checking AI-related reporting. Upcoming plans include building Claude skills connected to GitHub and learning more about the lab's oyster research to develop targeted tools.

---

### Mortality assessments
- **Author**: naomikang44
- **Date**: 2026-07-07
- **URL**: https://genefish.wordpress.com/2026/07/07/mortality-assessments/
- **Key finding**: Jesse and Naomi conducted mortality assessments on nine families of oysters at the 20-hour mark of a 35 degrees C heat exposure experiment, recording whether individual oysters were alive or dead and measuring the length of mortalities. A subset of 20 oysters from each family was also placed in saltwater containers to prepare for a potential saltwater versus freshwater comparison experiment.

---

### Water quality testing, heat exposure, and mortality assessments
- **Author**: Jesse Lowe
- **Date**: 2026-07-07
- **URL**: https://genefish.wordpress.com/2026/07/07/water-quality-testing-heat-exposure-and-mortality-assessments/
- **Key finding**: Jesse recorded water quality parameters across all four tanks, performed a 30-minute heat exposure on oysters from the left blue tank (25.4 to 24.9 degrees C), and completed mortality checks on nine oyster families in two separate bins. The Dorian bin families showed very few mortalities (only 2 across all 9 families), while the Meredith bin families were assessed at the 20-hour post-heat-exposure mark with results logged in a shared spreadsheet.

---

### Heat exposure and mortality assessments
- **Author**: naomikang44
- **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/heat-exposure-and-mortality-assessments/
- **Key finding**: Jesse, Grace, and Naomi conducted mortality assessments at the 43-hour mark for nine oyster families exposed to 35 degrees C heat in both 30 ppt and 9 ppt salinity water. Data were logged across two experimental conditions (labeled 0706-35C and 0706-35C09ppt), continuing the time-series tracking of heat stress outcomes across salinity treatments.

---

### Water quality testing, heat exposure, and mortality assessments
- **Author**: Jesse Lowe
- **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/water-quality-testing-heat-exposure-and-mortality-assessments-2/
- **Key finding**: Jesse logged water quality readings for all four tanks and performed a 30-minute heat exposure on left blue tank oysters. Mortality assessments were conducted alongside Naomi and Grace at the 44-hour mark for nine oyster families across the 30 ppt and 9 ppt heat exposure treatments, with data recorded in a shared spreadsheet.

---

### Repeat stress prelim — RNA quantification
- **Author**: HazelAbrahamsonA
- **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/repeat-stress-prelim-rna-quantification/
- **Key finding**: Hazel used the Qubit RNA HS Assay Kit to quantify RNA extracted from oyster samples in a preliminary experiment on the effects of repeated heat stress, with samples yielding approximately 30 ng/uL on average. The next step is reverse transcription to cDNA for use in qPCR to examine expression of metabolism and stress response genes, with results to be compared against GlycogenGlo glycogen data from the same samples. An additional RNA extraction from remaining samples was completed the following day using the Zymo DNA/RNA Miniprep Plus kit.

---

### More Claude skills: Marine Species Resolver + Phylogenetic tree builder
- **Author**: Cas Daniel
- **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/more-claude-skills-marine-species-resolver-phylogenetic-tree-builder/
- **Key finding**: Cas extended a prior Claude skill that resolves marine species taxonomy via the World Register of Marine Species (WoRMS) by adding a phylogenetic tree-building capability using the alterlab-phylogenetics skill from skills.sh. The pipeline fetched COX1 barcode sequences for six oyster species from GenBank, aligned them with MAFFT, and built a maximum-likelihood tree with IQ-TREE2, which cleanly separated flat oysters (Olympia, European flat, Sydney rock) from cupped oysters (Pacific, Kumamoto, Eastern). A notable finding was that the native Olympia oyster clusters with European flat oysters rather than the Crassostrea species dominant in PNW aquaculture, though Cas flagged accuracy verification against published phylogenies as a key next step.

---

### Lab Notebook Summarizer: Building a Weekly Digest Tool
- **Author**: Cas Daniel
- **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/lab-notebook-summarizer-building-a-weekly-digest-tool/
- **Key finding**: Cas built a two-part tool consisting of a Python script that queries the WordPress REST API for the past week's posts and a Claude Code skill that summarizes each post and groups results by author. A test run on the previous week's posts produced a digest covering four contributors and was saved both as a Markdown file in the GitHub repo and as a Google Doc. Future plans include extending the tool to summarize GitHub-based lab notebooks and potentially flagging connections between lab findings and recently published oyster research.

---

### Guava Muse successfully read
- **Author**: Christina Zhang
- **Date**: 2026-07-08
- **URL**: https://genefish.wordpress.com/2026/07/08/guava-muse-successfully-read/
- **Key finding**: Christina troubleshot the Guava Muse flow cytometer by running backflush cycles and complete cleans before the system check passed using a kit that had previously worked on the machine. The next step is to test the mitochondria kit on oyster or mussel tissue to confirm the instrument is reporting biologically accurate results.

---

### Heat exposure and freshwater mortality assessments
- **Author**: naomikang44
- **Date**: 2026-07-09
- **URL**: https://genefish.wordpress.com/2026/07/09/heat-exposure-and-freshwater-mortality-assessments/
- **Key finding**: Jesse, Grace, and Naomi conducted mortality assessments at the 67-hour mark for nine oyster families exposed to 35 degrees C heat in 30 ppt and approximately 11 ppt salinity water, finding that high-salinity families showed substantially higher mortality than low-salinity families. A parallel freshwater exposure dataset was also collected at the 44-hour mark, with very few mortalities observed compared to the saltwater heat treatments. A complicating factor noted was that some oysters were physically attached to each other and were counted as separate individuals, inflating counts in certain families.

---

### "Oyster_measurer" in progress
- **Author**: Christina Zhang
- **Date**: 2026-07-09
- **URL**: https://genefish.wordpress.com/2026/07/09/oyster_measurer-in-progress/
- **Key finding**: Christina began developing an image-analysis agent that detects a ruler in oyster photos to calibrate pixel-to-millimeter conversions, identifies individual oysters, and measures each one's length and width before exporting results as a CSV. The model currently struggles to distinguish oysters from cluttered backgrounds, so Christina plans to manually annotate 20 or more images in yellow to build a training dataset. Separately, Christina also reviewed the Mito Potential Kit manual and plans to test it on oyster or mussel tissue as a follow-up to the Cytek instrument work.

---

### Water quality testing, heat exposure, and mortality assessments
- **Author**: Jesse Lowe
- **Date**: 2026-07-09
- **URL**: https://genefish.wordpress.com/2026/07/09/water-quality-testing-heat-exposure-and-mortality-assessments-3/
- **Key finding**: Jesse recorded water quality across all four tanks and performed a 30-minute heat exposure on left blue tank oysters. Mortality assessments with Naomi and Grace at the 66-hour mark confirmed that oysters held in lower-salinity water (11 ppt and freshwater) had significantly more survivors than those in 30 ppt water following 35 degrees C heat exposure, reinforcing the trend observed in earlier time points.

---

### Lab Notebook Summarizer — More additions & Exploration
- **Author**: Cas Daniel
- **Date**: 2026-07-09
- **URL**: https://genefish.wordpress.com/2026/07/09/lab-notebook-summarizer-more-additions-exploration/
- **Key finding**: Cas extended the lab notebook digest tool to handle individual GitHub-based notebooks by creating separate Claude Code subagents for each lab member's notebook format, rather than using a single monolithic script. Subagents for Dr. Roberts' tumbling-oysters notebook and Ariana's notebook were built and tested successfully, with a key troubleshooting lesson learned: newly created subagents must be tested in a fresh Claude Code session to load properly. The longer-term vision is a main agent that dispatches all subagents, compiles their summaries, identifies cross-notebook patterns, and eventually connects lab findings to broader published oyster research.

---

### Heat exposure, freshwater, and mortality assessments continued
- **Author**: naomikang44
- **Date**: 2026-07-10
- **URL**: https://genefish.wordpress.com/2026/07/10/heat-exposure-freshwater-and-mortality-assessments-continued/
- **Key finding**: Jesse and Naomi conducted a third round of mortality assessments at approximately the 91-92 hour mark for oyster families in the 35 degrees C, 30 ppt and 9 ppt conditions, as well as the 69-hour mark for freshwater-exposed families. Changes from the previous day were minimal, with the 9 ppt families continuing to show the highest mortality rates. Two suspected parasites (possibly mud worms) were found in the 30 ppt treatment group, one from Family 2 and one of unknown family origin.

---

### Water quality testing, PolyIC priming,...
- **Author**: Jesse Lowe
- **Date**: 2026-07-10
- **URL**: https://genefish.wordpress.com/2026/07/10/water-quality-testing-polyic-priming/
- **Key finding**: Jesse recorded water quality parameters across all four tanks, assisted Megan with PolyIC immune priming of Manila clams and cockles from the yellow tanks, and performed a full water change on the right yellow tank following the priming procedure. A routine heat exposure on left blue tank oysters was also completed, and Jesse and Naomi conducted the 66-hour mortality assessments across the 30 ppt, 11 ppt, and freshwater oyster family groups. Two parasites were again noted in the 30 ppt heat treatment samples.

---

### Water quality testing, heat exposure, and clam counts
- **Author**: Jesse Lowe
- **Date**: 2026-07-12
- **URL**: https://genefish.wordpress.com/2026/07/12/water-quality-testing-heat-exposure-and-clam-counts/
- **Key finding**: Jesse conducted routine water quality checks on the left and right blue tanks and performed a 30-minute heat exposure on left blue tank oysters. Jesse and Megan then counted and bagged Manila clams and cockles in preparation for transport to the Suquamish field site the following day, and Jesse continued sewing clam bags ahead of a planned deployment at a second site.

---

> Generated by the `full-lab-digest` skill · 2026-07-07 to 2026-07-13
