# Full Lab Digest — 2026-07-22 to 2026-07-28 (7 days)

> 4 of 5 sources had activity in the last 7 days. 1 had none.

---

## Tumbling Oysters (Steven Roberts)

_No posts in the last 7 days._

---

## Ariana Huffmyer Lab Notebook

## Ariana Huffmyer Notebook Digest — Week of 2026-07-21 to 2026-07-28

> Summarized from [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io)

### July Goals and Daily Entries
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-23
- **Categories**: goals, daily-entries
- **Key finding**: Running log of July 2026 goals and daily activities. This week's entries (July 20-23) cover data management for Westcott outplants, oyster image analysis protocols, PolyIC paper work, resazurin index analysis, peer review, and meetings (Yaamini, SORMI, Hazel, Callie). The July outplants/hardening goal was marked complete.
- **Figures**: none

---

### Predictive resazurin phenotyping using VIMS oyster family data
- **Author**: Ariana Huffmyer
- **Date**: 2026-07-23
- **Categories**: resazurin, metabolism, cvirginica
- **AI-use disclosure**: Level 1 (Editing) — AI used to adapt code, generate figures, and draft base text that was then edited.
- **Key finding**: Extracted 25 quantitative curve features from 4-hour resazurin metabolic assays across 48 *C. virginica* families (high- and low-salinity origin, ~1,255 individuals) to test whether metabolic curve shape predicts family-level survival. Family identity explained 15-19% of variation in curve features, and the best-discriminating feature differed by group (early-phase rate for high-salinity origin, sustained late-phase AUC for low-salinity origin). Critically, low-salinity survival was strongly and reliably predictable from metabolic-capacity features (Vmax composite index LOFO-CV rho = 0.53), while high-salinity survival was weakly predictable and failed cross-validation (rho = -0.26) — indicating the two conditions draw on distinct physiological mechanisms and require different screening metrics.
- **Figures**:
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

## Sam White Notebook Digest — Week of 2026-07-21 to 2026-07-28

> Summarized from [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook)

---

### qPCRs - C.gigas Lifestage Carryover cDNA
- **Author**: Sam White
- **Date**: 2024-03-25
- **URL**: https://robertslab.github.io/sams-notebook/posts/2024/2024-03-25-qPCRs---C.gigas-Lifestage-Carryover-cDNA/
- **Categories**: qPCR, C.gigas, lifestage carryover, cDNA
- **Change this week**: Cosmetic edit only. A single relative link to the `project-gigas-carryover` repo was replaced with a full GitHub URL (`https://github.com/RobertsLab/project-gigas-carryover/tree/main/lifestage_carryover`). No new science content. This is a historical entry Sam re-touched, not new work this week.

---

### qPCR Analysis - M.gigas PolyIC Data from Valentinas Project
- **Author**: Sam White
- **Date**: 2026-02-02
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-02-02-qPCR-Analysis---M.gigas-PolyIC-Data-from-Valentinas-Project/
- **Categories**: qPCR, Pacific oyster, Magallana gigas, Crassostrea gigas, polyIC, HSP70, HSP90, cGAS, VIPERIN, ATP Synthase, Citrate Synthase, DNMT1, GAPDH
- **Key finding**: This is a historical entry (dated 2026-02-02) that Sam edited this week — the change (+25 lines) added links to previously-run ATPase/HSP70 qPCR data files he tracked down for Valentina's project, not new analysis. The post analyzes qPCR expression of 8 genes in Magallana gigas under PolyIC (viral-mimic dsRNA) plus stress treatments (Temperature, Mechanical, Control), normalized to GAPDH via two-way ANOVA. Key results: VIPERIN is significantly induced by PolyIC alone (p = 0.00016), consistent with its antiviral role; ATP Synthase responds significantly to PolyIC (p = 7.3e-06) with the strongest effect under PolyIC+Temperature; HSP90 responds only to the PolyIC+Temperature combination; while cGAS, Citrate Synthase, and DNMT1 show no significant PolyIC response.
- **Figures**: None embedded (plots are generated by R code chunks at render time).

---

### Data Received - Full RNA-seq Data for Andy Dittman and NOAA
- **Author**: Sam White
- **Date**: 2026-07-15
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-07-15-Data-Received---Full-RNA-seq-Data-for-Andy-Dittman-and-NOAA/
- **Categories**: Data Received, RNA-seq
- **Key finding**: Logistical/data-receipt entry. Sam received the full RNA-seq dataset for Andy Dittman (NOAA) from UW's Northwest Genomics Center, the remainder following a preliminary subset received on 2026-05-08. Data was downloaded to the Owl server via Globus (a full 24-hour transfer) to `owl.fish.washington.edu/nightingales/dittman_grc_rnaseq_1/`, and all MD5 checksums were verified as OK.
- **Figures**: None (data-receipt post; the body is a checksum verification listing).

---

### Homogenization - June 2026 SORMI M.gigas Ctenidia from Families 1 and 9 for Glycogen Glo Assay
- **Author**: Sam White
- **Date**: 2026-07-22
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-07-22-Homogenization---June-2026-SORMI-M.gigas-Ctenidia-from-Families-1-and-9-for-Glycogen-Glo-Assay/
- **Categories**: SORMI, Magallana gigas, ctenidia, Pacific oyster, Crassostrea gigas, glycogen, Glycogen Glo, homogenization
- **Key finding**: Sample-prep entry for the `sormi-assay-development` project. Sam homogenized frozen ctenidia from two USDA oyster families (1 and 9), ambient and 36°C treatments (n = 8 each), from the June 2026 SORMI sampling event, to prepare for a Glycogen Glo Assay evaluating glycogen content (family selection made by Steven). Weighed tissue was homogenized in a Bullet Blender 5E Gold+ (10 min, Speed 12) with glass beads, PBS, and 0.3N HCl, then TRIS buffer was added and samples stored at -20°C; a table of oyster IDs and tissue weights (mg) was recorded.
- **Figures**: None (sample-prep post; content is a methods description and a sample-weight table).

**Warnings**
- posts/2026/2026-02-02-qPCR-Analysis...index.qmd: 34344 chars omitted from the middle (post exceeds the 60000-char cap); head and tail are intact.

---

## Grace Crandall's Notebook

## Grace Crandall Notebook Digest — Week of 2026-07-21 to 2026-07-28

> Summarized from [grace-ac/grace-ac.github.io](https://github.com/grace-ac/grace-ac.github.io)

### FHL 2026 Water Filter DNA Extractions Part 4
- **Date**: 2026-07-21
- **URL**: https://grace-ac.github.io/waterfilter-dna-extractions-batch4/
- **Categories**: FHL2026
- **Key finding**: Completed the fourth and final batch of DNA extractions from the 0.45um water filters for the 2026 FHL experiment, processing n=18 half-filters plus 2 blank controls using the ZymoBIOMICS DNA Miniprep Kit (D4300); the remaining filter halves stay archived at -80C. Extraction went smoothly aside from an intentional stopping point at Step 2 (post-lysis, pre-bead-beating) for a check-in with Drew. Next steps are qPCR of 2ul per sample across four plates targeting *V. pectenicida* (n=80 with blanks) and starting eelgrass swab DNA extractions (n=32).

---

### Post-SR Meeting Notes and To-Dos
- **Date**: 2026-07-22
- **URL**: https://grace-ac.github.io/postSRmtg-todos/
- **Categories**: SRMtg
- **Key finding**: Notes from a check-in with Steven covering two threads: the Coyle crab paper was rejected by Wiley Molecular Ecology but offered a transfer to another Wiley journal, and a discrepancy between enrichment results from Steven's `topGO` analysis versus Grace's earlier DAVID analysis. Decisions were to transfer the submission to Journal of Fish Diseases the same day and to prioritize learning the `topGO` package because it is reproducible (unlike DAVID). The aim is to have multispecies enrichment results ready for the next Wednesday pycno check-in meeting.

---

### Paper Submission Transfer - Coyle et al Crab Paper
- **Date**: 2026-07-22
- **URL**: https://grace-ac.github.io/resubmit-crab/
- **Categories**: CoyleCrab
- **Key finding**: After Wiley Molecular Ecology rejected the Coyle et al. crab paper, they offered a transfer to Ecology and Evolution, Journal of Fish Diseases, or Journal of Fish Biology. Grace and Steven selected the Journal of Fish Diseases as the best fit given its focus on disease in wild and cultured fish and shellfish. Grace submitted the paper via the journal's submission-transfer option the same day.

---

### FHL Experiment - 2026 Water Filter qPCR Plates 1 and 2
- **Date**: 2026-07-24
- **URL**: https://grace-ac.github.io/2026filter-qpcr-plate1and2/
- **Categories**: FHL2026
- **Key finding**: Ran the first two qPCR plates (2ul DNA each) from the half water filters, targeting *V. pectenicida*. Plate 1 had a clean standard curve (R^2=0.995, E=96.4%); Plate 2's curve was poor unfiltered (R^2=0.85) but improved to R^2=0.979 (E=102.5%) after removing an outlier standard replicate (D3). A rough Excel figure plots mean starting quantity per sample by treatment group; roughly six more plates remain to finish all filter, eelgrass swab, mussel tissue, and mussel swab samples, and Grace notes she needs to order more TaqMan Master Mix, 10X EXO IPC Mix, and 50X EXO IPC DNA.
- **Figures**:
  - local: ../notebook-images/2026-07-24/2026-waterfilters-rough-fig.png

---

## Genefish WordPress

# genefish WordPress Digest — Week of 2026-07-21 to 2026-07-28

> Summarized from [genefish.wordpress.com](https://genefish.wordpress.com)

### "Oyster Measurer" training updates
- **Author**: Christina Zhang
- **Date**: 2026-07-21
- **URL**: https://genefish.wordpress.com/2026/07/21/oyster-measurer-training-updates/
- **Key finding**: Christina worked on training an AI tool to automatically identify and measure oysters from photos, editing 20 masked images and refining prompts to prevent misidentification of snails, crabs, and other background objects. After re-emphasizing use of the blue masks, the AI correctly separated individual oysters, though it still struggles with caliper detection and ruler calibration. She plans to shift toward training a YOLOv8 model so oysters can be identified without manual masks, noting more training images are needed for higher accuracy.

---

### Building & compiling the first final draft of weekly lab digests
- **Author**: Cas Daniel
- **Date**: 2026-07-21
- **URL**: https://genefish.wordpress.com/2026/07/21/building-compiling-the-first-final-draft-of-weekly-lab-digests/
- **Key finding**: Cas built the final component of the lab notebook summarization tool, a literature-connector skill that searches PubMed and bioRxiv for research related to the week's findings. After early problems with 403 errors and fabricated summaries, an explicit rule was added to exclude any source whose fetch fails, which resolved the issue and successfully retrieved a real preprint via Europe PMC. Both citations in the resulting digest (Ariana's resazurin paper and Hazel's glycogen results) were manually verified as accurate before the integration was committed, with next steps focused on setting up authenticated WordPress posting under human review.

---

### Today Steven and I upscaled…
- **Author**: acasey2
- **Date**: 2026-07-22
- **URL**: https://genefish.wordpress.com/2026/07/22/today-steven-and-i-upscaled/
- **Key finding**: The OAE oyster project was scaled up from buckets to trash bins to increase rearing volume. The stated goal is to determine whether observed mortalities stem from a volume or husbandry issue rather than being a true effect of ocean alkalinity enhancement (OAE).

---

### Shell strength testing
- **Author**: acasey2
- **Date**: 2026-07-22
- **URL**: https://genefish.wordpress.com/2026/07/22/shell-strength-testing/
- **Key finding**: The team conducted shell strength testing to compare Pacific oysters exposed in-situ to OAE versus ambient conditions in Port Angeles Harbor. This was a lab-based measurement effort assessing whether ocean alkalinity enhancement affects shell mechanical properties.

---

### Full Lab Digest — 2026-07-15 to 2026-07-21
- **Author**: Cas Daniel
- **Date**: 2026-07-23
- **URL**: https://genefish.wordpress.com/2026/07/23/full-lab-digest-2026-07-15-to-2026-07-21/
- **Key finding**: This is an automated cross-lab digest compiling activity from five notebook sources for the prior week, with three sources active. It summarizes thermal hardening and outplanting of primed oysters (Ariana), resazurin and coral physiology publications, RNA-seq data receipt (Sam White), and multiple genefish heat-stress and H2O2 mortality trials. A cross-notebook pattern section highlights convergent C. gigas heat-stress work at 35–36°C, and a literature-connector section links lab findings to external papers on resazurin metabolic assays and heat-induced glycogen depletion.

---

### Creating a publishing skill for Lab Notebook Digests
- **Author**: Cas Daniel
- **Date**: 2026-07-23
- **URL**: https://genefish.wordpress.com/2026/07/23/creating-a-publishing-skill-for-lab-notebook-digests/
- **Key finding**: Cas completed a WordPress-publishing skill that lets the Lab Notebook agent automatically post weekly digests to the site as drafts awaiting human review. This required registering the tool as a WordPress app, connecting it via OAuth, and generating an access token so the skill could convert markdown to HTML and upload drafts. The first test succeeded aside from a minor duplicate-header issue, completing the full pipeline of five subagents, a compiler, cross-notebook pattern detection, a literature connector, and automated publishing, with formatting refinements planned next.

---

### My rough protocol for collagen gene expression analysis in starfish
- **Author**: Samuel Slutz
- **Date**: 2026-07-24
- **URL**: https://genefish.wordpress.com/2026/07/24/my-rough-protocol-for-collagen-gene-expression-analysis-in-starfish/
- **Key finding**: Samuel outlined a draft workflow for identifying and analyzing collagen-related gene expression across three starfish species. The pipeline runs BLAST results through UniProt, uses GO tags to isolate collagen genes, and feeds species-specific expression matrices and BLAST sheets into a custom "Expression Helper" program built with the rxlsx library. The program is being developed to calculate differences in mean gene expression between exposed and unexposed stars for each gene per species.

---

### Tank room
- **Author**: Jesse Lowe
- **Date**: 2026-07-27
- **URL**: https://genefish.wordpress.com/2026/07/27/tank-room/
- **Key finding**: Jesse recorded routine water quality checks across four tanks, all at 30 ppt salinity with pH ranging 7.5–8.0 and ammonia and nitrite at zero; nitrate was 10 in the blue tanks and 0 in the yellow tanks. Both blue and yellow tanks were fed 10 ml of diluted shellfish diet at 11:00, and the bag filter on the right blue tank was replaced. This is a routine husbandry and maintenance log entry.

---

## Cross-Notebook Patterns & Connections

### Shared Themes
- **PolyIC / viral-mimic immune work in *Magallana gigas*** — Sam White's re-touched qPCR analysis of PolyIC-treated *M. gigas* (VIPERIN, HSP70/90, ATP Synthase, cGAS) and Ariana Huffmyer's daily-entry note of ongoing "PolyIC paper work" both point to the same PolyIC oyster-immunity effort running across the two notebooks this week.
- **Glycogen content in heat-stressed *M. gigas*** — Sam White homogenized SORMI *M. gigas* ctenidia from ambient vs 36°C treatments for a Glycogen Glo assay, and the genefish WordPress full-lab-digest post references "Hazel's glycogen results" and heat-induced glycogen depletion. Shared entity: glycogen assays in thermally stressed Pacific oysters.
- **Resazurin metabolic assay in oysters** — Ariana's VIMS resazurin curve-phenotyping post centers on the resazurin metabolic assay, and the genefish WordPress digest-tooling posts explicitly cite "Ariana's resazurin paper." (Note: the WordPress mention is a downstream reference to Ariana's own work rather than an independent result.)
- **Automated oyster image measurement** — Ariana's daily entry lists work on "oyster image analysis protocols," and Christina Zhang's genefish WordPress post describes training an AI/YOLOv8 "Oyster Measurer" to identify and size oysters from photos. Shared theme: automated measurement of oysters from images.
- **SORMI project** — the SORMI sampling/assay work appears in both Sam White's notebook (June 2026 SORMI ctenidia homogenization) and Ariana's daily entries (a SORMI meeting), tying the two notebooks to the same named project.

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

### PolyIC-induced antiviral gene expression in Pacific oysters

**Source:** Sam's Notebook (Sam White); related to Ariana Huffmyer's PolyIC paper work
**Finding:** In *M. gigas* qPCR, VIPERIN is significantly induced by PolyIC (viral-mimic dsRNA) alone (p=0.00016) consistent with an antiviral role, while ATP Synthase responds most strongly under PolyIC+Temperature and cGAS/DNMT1 show no significant PolyIC response.

### Supports [PubMed]: An OASL homologue involved in IFN-like antiviral signal by binding MDA5 in the Pacific oyster Crassostrea gigas
Zeng et al., 2026 · PMID: 41580101 · https://pubmed.ncbi.nlm.nih.gov/41580101/

This study identifies CgOASL, an interferon-stimulated gene (ISG) in *C. gigas* whose haemocyte expression is significantly upregulated by poly(I:C), and shows it binds dsRNA and interacts with the sensor CgMDA5 to drive ISG expression. Because VIPERIN is likewise an ISG, this independently confirms that poly(I:C) induces the antiviral ISG program in Pacific oyster, matching the direction of the lab's VIPERIN result. It reinforces that the PolyIC-responsive genes in the lab data sit within a genuine oyster interferon-like antiviral pathway.

### Adds context [PubMed]: The RNA sensor MDA5 contributes to the antiviral immune response in Crassostrea gigas by modulating the MAVS-mediated signaling pathway
Xu et al., 2026 · PMID: 41605267 · https://pubmed.ncbi.nlm.nih.gov/41605267/

This paper characterizes CgMDA5, a cytoplasmic dsRNA sensor in *C. gigas* that is upregulated by poly(I:C) and signals through CgMAVS to activate the CgIRF–CgIFNLP antiviral cascade. It describes the upstream sensing machinery that would detect PolyIC and drive downstream effectors such as VIPERIN, providing a mechanistic frame for why VIPERIN (but not cGAS) responds to PolyIC in the lab data. This helps distinguish the RLR/MDA5 dsRNA-sensing route from the cGAS DNA-sensing route that showed no PolyIC response.

### Adds context [PubMed]: The significant regulatory role of cytochrome P450 in the innate immune response of the Zhikong scallop (Chlamys farreri)
Zhao et al., 2026 · PMID: 42331123 · https://pubmed.ncbi.nlm.nih.gov/42331123/

In this scallop study, Cf-CYP450 is shown to be poly(I:C)-inducible and to dose-dependently modulate poly(I:C)/IRF1-driven ISRE (interferon-stimulated response element) activity. It offers comparative-mollusc evidence that poly(I:C) engages an IRF/interferon-response module in bivalves, contextualizing the PolyIC-specific induction seen in the oyster qPCR data. The regulatory (suppressive) role it reports also hints at layered control over the poly(I:C) response beyond simple induction.

**Literature summary:** Three peer-reviewed papers from the last 12 months support and contextualize the lab's PolyIC result: two in the same species (*C. gigas*) show that poly(I:C) upregulates antiviral ISGs (OASL) and engages the MDA5–MAVS–IRF–IFN sensing pathway, consistent with VIPERIN induction by PolyIC and with the lack of response from the cGAS DNA-sensing arm. A third, in scallop, adds comparative evidence that poly(I:C) drives IRF/ISRE-based signaling in bivalves. No preprints were retrieved for this finding; all support comes from peer-reviewed literature.

### Resazurin as a whole-organism metabolic proxy predicting oyster survival

**Source:** Ariana Huffmyer Lab Notebook
**Finding:** Resazurin metabolic-curve features vary at the family level across ~48–50 *C. virginica* families and predict family survival/performance, with metabolic depression associated with higher survival under acute thermal stress.

### Supports [PubMed]: From blue to pink: resazurin as a high-throughput proxy for metabolic rate in oysters
Huffmyer et al., 2026 · PMID: 42495017 · https://pubmed.ncbi.nlm.nih.gov/42495017/ (originally posted as bioRxiv preprint: https://doi.org/10.1101/2025.11.06.686367)

This is the peer-reviewed publication underlying the notebook finding: it validates resazurin fluorescence against oxygen consumption in *C. gigas* and *C. virginica*, and reports that individuals with greater metabolic depression are more likely to survive acute thermal stress. It also detects significant family-level variation and shows that metabolic rate across 50 selectively bred *C. virginica* families correlates with predicted performance. It directly supports the notebook's family-level, survival-predictive resazurin phenotyping.

### Adds context [bioRxiv preprint — not peer-reviewed]: Hemocyte Viability Assay as an Alternative Method for Testing Bacterial Pathogenicity in Bivalves
Samson et al., 2025 · DOI: 10.1101/2025.11.04.686564 · https://doi.org/10.1101/2025.11.04.686564

This preprint optimizes a resazurin-based viability assay on eastern oyster (*C. virginica*) hemocytes to rank bacterial pathogen virulence via LC50 values, validated against larval mortality. It demonstrates the same resazurin readout deployed as a scalable, predictive screening tool in oysters, though for pathogen virulence rather than metabolic phenotyping. It shows the breadth of resazurin's utility as a high-throughput oyster assay complementary to the metabolic application.

### Adds context [PubMed]: Cytotoxicity of polystyrene nanoplastics involves mitochondrial dysfunction and DNA damage in hemocytes of the Pacific oyster
de Carvalho Penha et al., 2025 · PMID: 41115343 · https://pubmed.ncbi.nlm.nih.gov/41115343/

This study uses the resazurin assay as a metabolic-activity readout in *C. gigas* hemocytes and finds it more sensitive than the neutral-red lysosomal assay for detecting nanoplastic cytotoxicity. It corroborates that resazurin is a sensitive, quantitative index of oyster metabolic state, supporting its use as a phenotyping tool. It also illustrates how the assay's metabolic sensitivity extends across whole-organism and cellular oyster contexts.

**Literature summary:** The finding is directly supported by its own peer-reviewed publication (Huffmyer et al., PeerJ 2026), which reports the family-level variation and survival-prediction results described in the notebook; the bioRxiv preprint of that same paper was detected and merged into this entry. Two additional sources — one peer-reviewed, one preprint — independently validate resazurin as a sensitive, scalable metabolic/viability readout in *C. gigas* and *C. virginica*, reinforcing the assay's reliability though in different applications.

### Heat-stress depletion of glycogen in Pacific oyster tissue

**Source:** Sam's Notebook (Sam White); related to genefish WordPress ("Hazel's glycogen results")
**Finding:** Glycogen content is being assayed (Glycogen Glo) in *M. gigas* ctenidia from ambient vs 36°C treatments, on the premise that thermal stress alters glycogen reserves.

### Adds context [PubMed]: Effects of temperature and Nocardia crassostreae on the immune response of the Pacific oyster, Magallana gigas
Mason et al., 2026 · PMID: 42476329 · https://pubmed.ncbi.nlm.nih.gov/42476329/

This experiment shows that elevated temperature independently reduced glycogen stores and ATP concentration in *M. gigas*, alongside reduced haemocyte viability and gill Na+/K+-ATPase activity, indicating thermally driven energetic strain. It provides direct, recent, same-species evidence that heat stress depletes glycogen reserves — the exact rationale behind assaying glycogen in ambient vs 36°C ctenidia. It also frames glycogen as an energetic-reserve readout that responds measurably to temperature, supporting the assay's biological relevance.

**Literature summary:** One peer-reviewed paper from the last 12 months directly supports the biological premise of the glycogen assay: elevated temperature independently depletes glycogen (and ATP) in *M. gigas*, matching the ambient-vs-36°C contrast Sam is preparing to measure. No relevant preprints were retrieved for this finding.

---

> Generated by the `full-lab-digest` skill · 2026-07-22 to 2026-07-28 (7-day window)
