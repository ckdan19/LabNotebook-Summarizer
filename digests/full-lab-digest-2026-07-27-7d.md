# Full Lab Digest — 2026-07-21 to 2026-07-27 (7 days)

> 4 of 5 sources had activity in the last 7 days. 1 had none.

---

## Tumbling Oysters (Steven Roberts)

_No posts in the last 7 days._

---

## Ariana Huffmyer Lab Notebook

> Summarized from [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io)

---

### July Goals and Daily Entries
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-23
- **Categories**: goals, daily-entries
- **Key finding**: This is a running goals and daily log post for July 2026, updated this week with entries through July 23. Active priorities include submitting the PolyIC manuscript, drafting the Hawaii 2023 and Moorea 2023 papers, and pursuing an NSF IOS grant with H. Putnam. Daily log entries this week cover resazurin index analysis, oyster image analysis, PolyIC writing, and meetings with collaborators Yaamini, Hazel, and Callie.
- **Figures**: None

---

### New Publications - July 2026
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-20
- **Categories**: publications
- **Change this week**: Two figure image URLs were updated from externally hosted Wiley CDN links to locally mirrored copies stored in the repository's `images/notebook/20260720/` directory.

---

### Outplanting Repeat Priming Oysters at Westcott
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-20
- **Categories**: hardening, oyster, cgigas, wsg-usda
- **AI Use disclosure**: L0 None — AI was not used in conducting the work or writing this post.
- **Key finding**: The team outplanted Pacific oyster seed from a repeat thermal priming experiment (weekly +10C exposure for 6 weeks) at Westcott Shellfish, motivated by previous results showing increased stress tolerance following a 2-year outplant. Twelve replicate bags across three racks were placed at the upper tidal limit, with HOBO MX400 and robo-oyster temperature loggers distributed across bags for environmental monitoring. A field trial of resazurin dye also produced a visible color change over roughly 3 hours in both Pacific and Olympia oysters, prompting plans to preserve and plate-read samples in future trips.

---

### Predictive Resazurin Phenotyping Using VIMS Oyster Family Data
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-23
- **Categories**: resazurin, metabolism, cvirginica
- **AI Use disclosure**: L1 Editing — AI was used to adapt existing code and generate figures, and to write base text that was then edited by the author.
- **Key finding**: This analysis extracted 25 curve features from 4-hour resazurin metabolic assays across 48 eastern oyster (*C. virginica*) families from high- and low-salinity parentage groups, then tested whether those features could predict family-level survival performance under salinity challenge. Low-salinity survival was strongly and reliably predictable from metabolic capacity features (Vmax, early AUC, initial slope; LOFO cross-validation Spearman rho ~ 0.53), while high-salinity survival was only weakly predicted by metabolic timing and depression features and did not generalize across held-out families. The results indicate that the two survival conditions draw on fundamentally different physiological mechanisms and that a single universal resazurin metric cannot serve both screening targets.

---

## Sam's Notebook (Sam White)

> Summarized from [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook)

---

### qPCRs - C.gigas Lifestage Carryover cDNA
- **Author**: Sam White
- **Date**: 2024-03-25
- **URL**: https://robertslab.github.io/sams-notebook/posts/2024/2024-03-25-qPCRs---C.gigas-Lifestage-Carryover-cDNA/
- **Categories**: qPCR, SsoFast, CFX Connect, HSP70, HSP90, GAPDH, VIPERIN, ATPsynthase, cGAS, DMNT1, citrate synthase, Crassostrea gigas, Pacific oyster, cDNA
- **Change this week**: Link-only fix — a relative path to the `project-gigas-carryover` GitHub repo was replaced with an absolute GitHub URL. No new science content.
- **Key finding** (pre-existing): qPCRs were run on cDNA from seed and spat life stages of *C. gigas* as part of the lifestage carryover project, targeting eight genes associated with stress and immune response (HSP70, HSP90, GAPDH, VIPERIN, ATPsynthase, cGAS, DNMT1, citrate synthase). Samples were run in duplicate on a CFX Connect thermocycler using SsoAdvanced SYBR Green chemistry. Results tables and amplification/melt curve plots are provided for each primer pair.

---

### qPCR Analysis - M.gigas PolyIC Data from Valentinas Project
- **Author**: Sam White
- **Date**: 2026-02-02
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-02-02-qPCR-Analysis---M.gigas-PolyIC-Data-from-Valentinas-Project/
- **Categories**: qPCR, Pacific oyster, Magallana gigas, Crassostrea gigas, polyIC, HSP70, HSP90, cGAS, VIPERIN, ATP Synthase, Citrate Synthase, DNMT1, GAPDH
- **Key finding**: This post presents a two-factor ANOVA analysis of qPCR data from *M. gigas* treated with PolyIC (a synthetic viral mimic) across three stress conditions — control, mechanical, and thermal — examining expression of eight target genes normalized to GAPDH. The clearest results show HSP70 is strongly and independently upregulated by temperature stress, while VIPERIN responds specifically to PolyIC treatment regardless of stress type, and HSP90 requires the combination of PolyIC plus temperature for significant induction. Unexpectedly, cGAS showed no significant response to PolyIC, suggesting that innate immune sensing of dsRNA analogs in oysters may proceed through alternative pathways or on different timescales.
- **Figures**: Plots are generated by R code chunks at render time; no static figure files are embedded in the post.

---

### Data Received - Full RNA-seq Data for Andy Dittman and NOAA
- **Author**: Sam White
- **Date**: 2026-07-15
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-07-15-Data-Received---Full-RNA-seq-Data-for-Andy-Dittman-and-NOAA/
- **Categories**: Data Received, RNA-seq
- **Key finding**: The complete RNA-seq dataset for Andy Dittman at NOAA was received from UW's Northwest Genomics Center and downloaded to the lab server (Owl) via GlobusConnect over a 24-hour transfer. The data follows an earlier partial delivery from May 2026, and MD5 checksums were verified for all files confirming data integrity. The full dataset is now publicly accessible at the lab's Owl server under the `dittman_grc_rnaseq_1` directory.
- **Figures**: No figures embedded in this post.

---

### Homogenization - June 2026 SORMI M.gigas Ctenidia from Families 1 and 9 for Glycogen Glo Assay
- **Author**: Sam White
- **Date**: 2026-07-22
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-07-22-Homogenization---June-2026-SORMI-M.gigas-Ctenidia-from-Families-1-and-9-for-Glycogen-Glo-Assay/
- **Categories**: SORMI, Magallana gigas, ctenidia, Pacific oyster, Crassostrea gigas, glycogen, Glycogen Glo, homogenization
- **Key finding**: Frozen ctenidia samples from *M. gigas* USDA Families 1 and 9 (n = 8 per treatment per family) were processed for glycogen content measurement following a June 2026 SORMI sampling event comparing ambient and 36°C heat-stress treatments. Small tissue portions were weighed, combined with glass beads and PBS, immediately acidified with HCl per the Glycogen Glo Assay protocol, and homogenized in a Bullet Blender for 10 minutes at Speed 12. Processed samples were stored at -20°C pending downstream assay; this post documents the homogenization step and records individual tissue weights.
- **Figures**: No figures embedded in this post.

> **Note**: The PolyIC qPCR analysis post (2026-02-02) exceeded the 60,000-character processing cap; head and tail content is intact so front matter, methods, and conclusions are present, but some mid-post content was omitted.

---

## Grace Crandall's Notebook

> Summarized from [grace-ac/grace-ac.github.io](https://github.com/grace-ac/grace-ac.github.io)

---

### FHL 2026 Water Filter DNA Extractions Part 4
- **Date**: 2026-07-21
- **URL**: https://grace-ac.github.io/waterfilter-dna-extractions-batch4/
- **Categories**: FHL2026
- **Key finding**: This post documents the fourth and final batch of DNA extractions from 0.45 um water filters collected during the 2026 FHL experiment, processing 18 filter halves and 2 extraction blanks using the ZymoBIOMICS DNA MiniPrep Kit. Samples span multiple treatment groups including eelgrass, mussel, shell, and V. pectenicida combinations. Next steps are to run all 80 extracted DNA samples across 4 qPCR plates targeting V. pectenicida by August 4th, and to begin DNA extractions from eelgrass swab samples.
- **Figures**: None

---

### Post-SR Meeting Notes and To-Dos
- **Date**: 2026-07-22
- **URL**: https://grace-ac.github.io/postSRmtg-todos/
- **Categories**: SRMtg
- **Key finding**: Grace met with Steven to discuss two agenda items: the rejection of the Coyle et al. crab paper from Wiley Molecular Ecology (with a transfer option to other Wiley journals) and discrepancies between GO enrichment results obtained via DAVID versus Steven's use of the topGO R package for seastar wasting disease data. The decision was to transfer the crab paper to the Journal of Fish Diseases and to prioritize learning topGO over DAVID because topGO is reproducible and auditable. Grace aims to have multispecies enrichment results ready for the following Wednesday's pycno check-in meeting.
- **Figures**: None

---

### Paper Submission Transfer - Coyle et al Crab Paper
- **Date**: 2026-07-22
- **URL**: https://grace-ac.github.io/resubmit-crab/
- **Categories**: CoyleCrab
- **Key finding**: Following rejection from Wiley Molecular Ecology, the Coyle et al. crab paper was transferred to the Journal of Fish Diseases, chosen from three Wiley transfer options (Ecology and Evolution, Journal of Fish Diseases, and Journal of Fish Biology). The Journal of Fish Diseases covers disease in both wild and cultured fish and shellfish, making it an appropriate venue. The submission transfer was completed and is now pending review.
- **Figures**: None

---

### FHL Experiment - 2026 Water Filter qPCR Plates 1 and 2
- **Date**: 2026-07-24
- **URL**: https://grace-ac.github.io/2026filter-qpcr-plate1and2/
- **Categories**: FHL2026
- **Key finding**: qPCR targeting V. pectenicida was run on DNA from 48 of the 0.45 um water filter samples across two plates, with Plate 1 yielding strong efficiency (R^2 = 0.995, E = 96.4%) and Plate 2 requiring removal of one outlier standard replicate to achieve acceptable efficiency (R^2 = 0.979, E = 102.5%). A rough Excel figure of mean starting quantities by sample ID shows preliminary detection patterns across treatment groups. Six more qPCR plates are needed to cover all remaining sample types (water filters, eelgrass swabs, mussel tissue, mussel swabs), and key reagents — TaqMan Master Mix, 10X EXO IPC Mix, and 50X EXO IPC DNA — need to be reordered before proceeding.

---

## Genefish WordPress

> Summarized from [genefish.wordpress.com](https://genefish.wordpress.com)

---

### I took oysters out of...
- **Author**: genefish
- **Date**: 2026-07-21
- **URL**: https://genefish.wordpress.com/2026/07/21/i-took-oysters-out-of/
- **Key finding**: Oysters were removed from the Young lab incubator set at 36 degrees C, with 33 individuals counted against a target of 36 and zero mortality observed at the time of removal. Cold deionized water was added and the incubator was returned to service, reset to 46 degrees C at 9 am. This is a brief logistical checkpoint entry with no associated analysis.

---

### "Oyster Measurer" training updates
- **Author**: Christina Zhang
- **Date**: 2026-07-21
- **URL**: https://genefish.wordpress.com/2026/07/21/oyster-measurer-training-updates/
- **Key finding**: Christina completed manual masking of 20 oyster images and tested an AI-based measurement pipeline, finding that the model correctly separated individual oysters once instructed to use the provided blue masks, but struggled with caliper identification and ruler calibration. To move beyond the dependency on manual masks, the next step is training a YOLOv8 model to detect oysters autonomously, which will require additional training images to reach acceptable accuracy. The work also established an export protocol that saves annotated, measured images alongside collected data in an xlsx file for human verification.

---

### Building & compiling the first final draft of weekly lab digests
- **Author**: Cas Daniel
- **Date**: 2026-07-21
- **URL**: https://genefish.wordpress.com/2026/07/21/building-compiling-the-first-final-draft-of-weekly-lab-digests/
- **Key finding**: Cas completed and verified a literature-connector skill that searches PubMed and bioRxiv for publications relevant to the week's lab findings, adding a safeguard that entirely excludes any source that returns a failed or unparseable fetch rather than generating a speculative summary. Both citations produced in the first real digest run were manually verified against their actual PubMed pages and DOIs, confirming accuracy. Planning then began for a WordPress posting component requiring OAuth2 authentication, with an intentional design requirement for human review before any draft is published.

---

### Today Steven and I upscaled...
- **Author**: acasey2
- **Date**: 2026-07-22
- **URL**: https://genefish.wordpress.com/2026/07/22/today-steven-and-i-upscaled/
- **Key finding**: The OAE (ocean alkalinity enhancement) oyster experiment was scaled up from buckets to trash bins to investigate whether elevated mortality observed previously reflects a husbandry or water volume issue rather than a direct biological effect of OAE. This entry is a brief logistical note with no results reported yet; the experiment appears to be in progress.

---

### Shell strength testing
- **Author**: acasey2
- **Date**: 2026-07-22
- **URL**: https://genefish.wordpress.com/2026/07/22/shell-strength-testing/
- **Key finding**: Shell strength was tested in Pacific oysters that had been exposed in situ to OAE versus ambient seawater conditions in Port Angeles Harbor, with the goal of detecting any differences attributable to OAE treatment. The entry notes the testing took place in a climate-controlled lab setting but does not report quantitative results or conclusions. This appears to be a brief progress note, with full analysis presumably forthcoming.

---

### Full Lab Digest — 2026-07-15 to 2026-07-21
- **Author**: Cas Daniel
- **Date**: 2026-07-23
- **URL**: https://genefish.wordpress.com/2026/07/23/full-lab-digest-2026-07-15-to-2026-07-21/
- **Key finding**: This is the first published full-lab digest, compiling activity summaries from three of five monitored notebook sources (Ariana Huffmyer, Sam White, and the Genefish WordPress) for the week of July 15-21, with cross-notebook pattern detection highlighting convergent thermal stress experiments on Pacific oysters at 35-36 degrees C across independent research threads. A literature connection section identified and manually verified two relevant external publications: a peer-reviewed paper by Huffmyer et al. validating resazurin fluorescence as a metabolic proxy in oysters, and a 2026 PubMed study by Mason et al. showing that elevated temperature independently depletes glycogen in Pacific oysters, consistent with Hazel's GlycogenGlo results. The digest represents the complete assembled pipeline of five subagents, cross-notebook pattern detection, and live literature search.

---

### Creating a publishing skill for Lab Notebook Digests
- **Author**: Cas Daniel
- **Date**: 2026-07-23
- **URL**: https://genefish.wordpress.com/2026/07/23/creating-a-publishing-skill-for-lab-notebook-digests/
- **Key finding**: Cas built and successfully tested a WordPress publisher skill that reads the most recent digest file from the repository, converts it from Markdown to HTML, and posts it to WordPress as a draft pending human review before any public publication. Setup required registering the summarizer tool as a WordPress app, completing an OAuth2 flow, and generating an access token from the terminal — a multi-step process that encountered several credential and bash-related issues before working. With this component in place, the full pipeline is now complete: five notebook subagents, a digest compiler, cross-notebook pattern detection, a literature connector, and automated draft publishing.

---

### My rough protocol for collagen gene expression analysis in starfish
- **Author**: Samuel Slutz
- **Date**: 2026-07-24
- **URL**: https://genefish.wordpress.com/2026/07/24/my-rough-protocol-for-collagen-gene-expression-analysis-in-starfish/
- **Key finding**: Samuel outlined a multi-step workflow for identifying collagen-related gene expression differences in three starfish species exposed to stress, using BLAST results fed into UniProt for GO-term-based filtering to isolate collagen-related genes. A custom program called Expression Helper, written using the rxlsx library in R, is being developed to cross-reference the gene expression matrix with the BLAST results and calculate mean expression differences between exposed and unexposed individuals for each species. The protocol is described as a rough draft, with the software tool still under active development.

---

## Cross-Notebook Patterns & Connections

### Shared Themes

- **PolyIC immune priming experiment in *M. gigas***: Sam White's notebook (updated this week) presents a two-factor ANOVA qPCR analysis of *M. gigas* treated with PolyIC, showing VIPERIN responds specifically to dsRNA treatment, HSP70 to temperature stress, and HSP90 requires both together; cGAS showed no significant response, pointing toward alternative dsRNA sensing pathways. Ariana Huffmyer's July goals post lists submitting the PolyIC manuscript as an active monthly priority, naming it alongside meetings with collaborators involved in the same work. Both sources reference the same named experiment by the same lab, with Sam's analysis serving as a direct upstream data input to Ariana's manuscript preparation.

- **GO term analysis on starfish gene expression**: Grace Crandall's post-SR meeting notes describe an ongoing effort to apply the topGO R package (in preference to DAVID) for GO enrichment analysis on seastar wasting disease transcriptomic data, with multispecies results targeted for a Wednesday check-in meeting. Samuel Slutz's WordPress entry this week describes a parallel workflow for identifying collagen-related genes in three starfish species under stress via BLAST → UniProt → GO-term filtering. Both work streams are applying GO term-based analyses to starfish multi-gene expression datasets, though targeting different biological questions.

### Temporal Narratives

- **PolyIC qPCR results → manuscript pipeline**: Sam White's PolyIC qPCR analysis post (February 2026, updated this week with a link correction) provides the quantitative two-factor ANOVA gene expression results for *M. gigas* that Ariana Huffmyer's July goals identify as a manuscript in active preparation. The dataset Sam analyzed appears to be the primary evidence base for the PolyIC submission, making this a lab-internal sequential pipeline: analysis complete → manuscript writing in progress.

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

---

### PolyIC dsRNA sensing pathways in Pacific oysters (cGAS non-response)

**Source:** Sam's Notebook (Sam White)
**Finding:** VIPERIN responds specifically to PolyIC treatment in *M. gigas* regardless of stress type, HSP70 responds to temperature stress, and HSP90 requires both; cGAS showed no significant response to PolyIC, suggesting dsRNA sensing proceeds through alternative pathways in Pacific oysters.

**Adds context** [PubMed]: The RNA Sensor MDA5 Contributes to the Antiviral Immune Response in *Crassostrea gigas* by Modulating the MAVS-Mediated Signaling Pathway
Xu et al., 2026 · PMID: 41605267 · https://pubmed.ncbi.nlm.nih.gov/41605267/

This study identified CgMDA5, a dsRNA helicase in *C. gigas*, and found that poly(I:C) stimulation significantly upregulates CgMDA5 expression in haemocytes. CgMDA5 physically interacts with CgMAVS to activate an IRF-IFN-like signaling cascade, establishing a mechanistic basis for how Pacific oysters sense viral dsRNA. The finding that dsRNA recognition proceeds through the MDA5-MAVS axis — rather than cGAS — is consistent with the lab's observation that cGAS showed no significant response to PolyIC in the two-factor qPCR experiment.

---

**Adds context** [PubMed]: An OASL Homologue Involved in IFN-Like Antiviral Signal by Binding MDA5 in the Pacific Oyster *Crassostrea gigas*
Zeng et al., 2026 · PMID: 41580101 · https://pubmed.ncbi.nlm.nih.gov/41580101/

This study identified CgOASL as an interferon-stimulated gene in *C. gigas* that is upregulated by poly(I:C) and regulated through the IFN-like signaling pathway. CgOASL specifically interacts with CgMDA5 but not with CgRIG-I, reinforcing MDA5 as the central hub for dsRNA recognition in oysters. Together with the MDA5/MAVS paper above, this points to a well-developed non-cGAS antiviral sensing system in Pacific oysters, providing a mechanistic explanation for why cGAS did not respond to PolyIC in the lab experiment.

**Literature summary:** Two peer-reviewed papers published in 2026 collectively establish that dsRNA sensing in *C. gigas* proceeds primarily through a MDA5-MAVS-IRF axis, with OASL serving as a co-sensor that specifically augments MDA5 activity. This literature provides mechanistic context for the cGAS non-response: Pacific oysters appear to rely on RIG-I-like receptor pathways rather than the cGAS-STING pathway for viral dsRNA detection. Both supporting papers are peer-reviewed; no relevant preprints were found on this topic.

---

### Resazurin predictive phenotyping for oyster family survival

**Source:** Ariana Huffmyer Lab Notebook
**Finding:** Resazurin curve features extracted from 4-hour assays across 48 *C. virginica* families strongly predict low-salinity survival (Vmax, early AUC, initial slope; Spearman rho ~ 0.53 cross-validated) but only weakly predict high-salinity survival, suggesting the two survival conditions draw on fundamentally different physiological mechanisms and that a single universal resazurin metric cannot serve both screening targets.

**Supports** [PubMed]: From Blue to Pink: Resazurin as a High-Throughput Proxy for Metabolic Rate in Oysters
Huffmyer et al., 2026 · PMID: 42495017 · https://pubmed.ncbi.nlm.nih.gov/42495017/

This peer-reviewed study validated resazurin fluorescence as a proxy for oxygen consumption in both *C. gigas* and *C. virginica* across multiple experimental contexts, demonstrating clear temperature-dependent metabolic performance curves and identifying individuals with greater metabolic depression as more likely to survive acute thermal stress. Importantly, the study detected significant family-level differences in metabolic responses across selectively bred *C. virginica* families, with metabolic rates significantly correlated with predicted performance outcomes. This directly supports the lab's approach of using resazurin curve features as a predictive screening tool for family-level performance differentiation, and establishes the published foundation on which this week's VIMS analysis is built.

**Literature summary:** One peer-reviewed paper (Huffmyer et al., 2026) directly validates the resazurin-based platform for whole-organism metabolism measurement in *C. virginica* and demonstrates that family-level genetic variation in metabolic responses is detectable with this assay. The lab's current VIMS analysis extends this by testing whether specific curve shape features predict salinity-specific survival — a more targeted phenotyping application of the same validated platform. No contradicting literature was found; no relevant preprints were identified.

---

### Glycogen depletion under thermal stress in *M. gigas* (SORMI Glycogen Glo assay)

**Source:** Sam's Notebook (Sam White)
**Finding:** Frozen ctenidia from *M. gigas* USDA Families 1 and 9 exposed to 36°C heat stress versus ambient conditions are being homogenized for Glycogen Glo assay to measure glycogen content differences across treatment groups.

**Adds context** [PubMed]: Effects of Temperature and *Nocardia crassostreae* on the Immune Response of the Pacific Oyster, *Magallana gigas*
Mason et al., 2026 · PMID: 42476329 · https://pubmed.ncbi.nlm.nih.gov/42476329/

Mason et al. experimentally challenged *M. gigas* with elevated temperature and bacterial infection for 42 days and quantified energetic parameters including mantle glycogen, ATP, ADP, and AMP alongside immune markers. Elevated temperature was found to independently reduce mantle glycogen stores, haemocyte viability, and gill Na+/K+-ATPase activity, demonstrating thermally driven energetic strain even in the absence of infection. This peer-reviewed result directly supports the biological rationale for Sam's SORMI Glycogen Glo comparison: if glycogen depletion is confirmed at 36°C, the Mason et al. findings provide an independent controlled confirmation of thermally driven energy mobilization in *M. gigas*.

**Literature summary:** One peer-reviewed paper (Mason et al., 2026) confirms that elevated temperature independently depletes glycogen stores in *M. gigas*, providing direct mechanistic context for the SORMI Glycogen Glo assay. The Mason et al. study used a longer treatment duration (42 days) and included a bacterial co-challenge, while the SORMI assay focuses on a shorter-term heat treatment with USDA selected families — comparison of the two datasets will help resolve whether glycogen depletion kinetics differ by family genetic background. No contradicting literature was found; no relevant preprints were identified.

---

### *Vibrio pectenicida* detection via qPCR in water filter eDNA

**Source:** Grace Crandall's Notebook
**Finding:** qPCR targeting *V. pectenicida* was run on DNA extracted from 0.45 µm water filters from the FHL 2026 experiment across multiple treatment groups (eelgrass, mussel, shell, and *V. pectenicida* combinations), with Plates 1 and 2 yielding acceptable efficiencies (R² = 0.995 and 0.979) and showing preliminary detection patterns across treatment groups.

**Adds context** [PubMed]: Microbe Profile: *Vibrio pectenicida*: the Deadly Marine Bacteria with Strains Impacting Sea Stars and Scallops
Blackwood et al., 2026 · PMID: 42455634 · https://pubmed.ncbi.nlm.nih.gov/42455634/

This Microbe Profile characterizes *V. pectenicida* as a coastal marine pathogen associated with sea star wasting disease and high mortality in larval scallops in hatcheries, providing a reference on the bacterium's pathogenicity across multiple marine host taxa. The profile's inclusion of shellfish (larval scallop) mortality is directly relevant to Grace's FHL experiment, which monitors *V. pectenicida* in water from shellfish and eelgrass treatment groups. This peer-reviewed profile establishes the published biological rationale for why monitoring water column concentrations of this pathogen is important.

---

**Adds context** [PubMed]: *Vibrio pectenicida* Strain FHCF-3 is a Causative Agent of Sea Star Wasting Disease
Prentice et al., 2025 · PMID: 40760083 · https://pubmed.ncbi.nlm.nih.gov/40760083/

Prentice et al. fulfilled Koch's postulates for *V. pectenicida* strain FHCF-3 as a causative agent of sea star wasting disease in sunflower sea stars (*Pycnopodia helianthoides*), establishing definitive causation rather than correlation. If the same FHCF-3 strain (or a closely related strain) is being used in Grace's FHL experiment, this paper establishes its confirmed pathogenicity and provides the biological justification for monitoring its presence in water across different treatment substrates.

---

**Adds context** [PubMed]: Draft Genome Sequence of *Vibrio pectenicida* Strain FHCF-3, a Causative Agent of Sea Star Wasting Disease, Reveals the Genetic Potential to Produce Aerolysin-Like Toxins
Zhong et al., 2025 · PMID: 40810621 · https://pubmed.ncbi.nlm.nih.gov/40810621/

This paper reported the 4.37 Mbp draft genome of *V. pectenicida* FHCF-3 and identified aerolysin-like toxin genes as candidate virulence factors. Knowledge of the FHCF-3 genome underpins qPCR primer design for strain-specific detection; the availability of this sequence supports the specificity of the qPCR assay Grace is using for water filter monitoring.

---

**Adds context** [bioRxiv preprint — not peer-reviewed]: When Bacteria Meet Many Arms: Autecological Insights into *Vibrio pectenicida* FHCF-3 in Echinoderms
Hewson, 2025 · DOI: 10.1101/2025.08.15.670479 · https://doi.org/10.1101/2025.08.15.670479

This preprint examined the ecology of *V. pectenicida* FHCF-3 across echinoderm species and raised the possibility that this bacterium may act as an opportunistic or saprobic agent in some host contexts rather than a strict primary pathogen. For Grace's water filter monitoring, this interpretive nuance is relevant: *V. pectenicida* detected in water filters may reflect active infection pressure, environmental carriage, or both, and the treatment group detection patterns will require careful interpretation. This is a preprint and has not yet been peer-reviewed.

**Literature summary:** Three peer-reviewed papers from 2025–2026 collectively establish *V. pectenicida* FHCF-3 as a confirmed causative agent of sea star wasting disease with a characterized genome (including aerolysin-like toxin genes) and documented pathogenicity extending to larval shellfish. One additional preprint raises the interpretive complexity that *V. pectenicida* may be opportunistic rather than strictly pathogenic in some host contexts. This literature provides strong biological justification for the water-filter qPCR monitoring approach but does not directly address the sensitivity of 0.45 µm filter eDNA extraction for *V. pectenicida* detection — the FHL plates represent new empirical data on detection feasibility in this experimental system.

---

> Generated by the `full-lab-digest` skill · 2026-07-21 to 2026-07-27 (7-day window)
