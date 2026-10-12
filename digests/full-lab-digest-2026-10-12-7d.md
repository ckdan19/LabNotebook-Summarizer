# Full Lab Digest — 2026-10-06 to 2026-10-12 (7 days)

> 5 of 7 sources had activity in the last 7 days. 2 had none.

---

## Tumbling Oysters (Steven Roberts)

### Chilean Flat Oyster WGBS: Three Populations, Nine Libraries
- **Date**: 10-10-2026
- **Author**: Steven Roberts
- **Categories**: Epigenetics, Genomics, Computing
- **Key finding**: Whole-genome bisulfite sequencing for *Ostrea chilensis* across three Chilean sites (Pumalin, Quilhua, Rio Pudeto) arrived as 15 files, but read-name and index-barcode checks showed these were only 9 true libraries — several files were subsampled duplicates or a mixture of two samples — leaving a 4-vs-4 Quilhua vs Rio Pudeto comparison (Pumalin n=1). Genome-wide, methylation followed the classic invertebrate pattern (concentrated in gene bodies, bimodal, tracking housekeeping vs. inducible gene function), and after filtering out differences explained by SNPs or repeat-region mapping artifacts, only one gene — GN020540, a putative partial Nup107 (nuclear pore) homolog — showed a robust, population-specific methylation difference, a result that held up after re-mapping to the haplotype-resolved Och_HapA reference.
- **Figures**:
  - local: images/landscape-features.png
  - local: images/landscape-metagene.png
  - local: images/snp-check-classes.png
  - local: images/gn020540-methylation.png
  - local: images/hapa-replication.png

---

### Chilean vs Olympia Oyster Methylation, and What Sits Inside GN020540
- **Date**: 10-10-2026
- **Author**: Steven Roberts
- **Categories**: Epigenetics, Genomics, Computing
- **Key finding**: Comparing measured *O. chilensis* gene-body methylation to genomic CpG o/e (a proxy for long-term germline methylation) in *O. lurida* across roughly 9,300 one-to-one orthologs showed strong concordance, indicating the two Ostrea species carry the long-term methylation footprint on largely the same set of genes. A closer look at GN020540 (the sole differentially methylated gene found in the companion post) revealed its intron contains a multi-copy interspersed repeat; the Rio Pudeto-specific hypomethylation at this particular copy is locus-specific rather than a genome-wide feature of the repeat family, isn't explained by any nearby SNP, and instead points to an upstream structural/haplotype difference as the likely cause, pending confirmation with long-read sequencing.
- **Figures**:
  - local: images/cpg-oe-by-species.png
  - local: images/ortholog-cpg-oe.png
  - local: images/och-gbm-vs-cpg-oe.png
  - local: images/gn020540-locus.png

---

## Ariana Huffmyer Lab Notebook

### Effort A Sequim Bay project final survival assay results
- **Date**: 2026-10-07
- **Author**: Ariana Huffmyer
- **Categories**: sequim-bay, hardening, experimental design
- **Key finding**: Analyzes final lab heat-survival assays for Effort A Sequim Bay outplants (control vs. 2-week daily 25°C hardening treatment, n=37–38/group) using Kaplan-Meier/Cox exploration followed by binomial logistic regression (status ~ time*group, random effect of length). A significant time:group interaction (P=0.026) and marginal post hoc difference (P=0.042) indicate slightly higher survival in treated oysters, with LT50 only ~1 hour higher (56.1 vs 55.1 hours) than controls, suggesting a small but real hardening effect.
- **Figures**:
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261007/temperature_rounds.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261007/survival_group.png?raw=true

_3 posts from this window were already covered in a previous digest and are omitted here._

---

## Sam's Notebook (Sam White)

### Data Analysis - Prototype M.gigas Gaping Pilot Project
- **Author**: Sam White
- **Date**: 2026-10-06
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-10-06-Data-Analysis---Prototype-M.gigas-Gaping-Pilot-Project/
- **Categories**: gaping, Magallanas gigas, Pacific oyster, magnetometer, RP2040, adalogger
- **Key finding**: Sam deployed the lab's first prototype oyster "gape logger" (a 3-axis magnetometer paired with magnets, run by an Adafruit Feather RP2040 Adalogger) on a single Pacific oyster for about five days. The magnetometer recorded only ~4 hours of data before seawater leaked into its sealed enclosure and shorted it out, and the oyster was found dead (tissue liquefied) upon retrieval; the recovered data show the shell opened ~1 hour after deployment and stayed open until sensor failure. The post also documents a full R/knitr analysis pipeline (timestamp reconstruction, magnetic-field-based gape event detection, per-unit calibration to convert field strength to gape distance in mm) built for processing this and future deployments, and flags the prototype's water sealing and short I2C cable range as key design problems to fix.
- **Figures**:
  - local: gape_monitor_deployed.jpg
  - local: magnetometer_fried.jpg

---

## Grace Crandall's Notebook

_No new posts in the last 7 days._

---

## Megan Ewing Lab Notebook

### ICSR 2026 Slides: Thermal and Immune Stress Priming Improves Resilience in Manila Clams and Basket Cockles
- **Author**: Megan Ewing
- **Date**: 10-07-2026
- **URL**: https://meganewing.github.io/mewing-notebook/posts/projects/icsr2026_slides.html
- **Categories**: projects
- **Key finding**: This post embeds the conference slide deck (via an iframe) presented at ICSR 2026, covering work on thermal and immune stress priming in Manila clams and basket cockles. The deck argues that pre-exposing these bivalves to mild thermal and immune stressors improves their resilience to subsequent stress events. No additional narrative text accompanies the embed in the post body itself.
- **Figures**: none found (the post embeds a Google Slides iframe rather than image figures)

---

## Kathleen Durkin Lab Notebook

_No new posts in the last 7 days._

---

## Genefish WordPress

### Tank room and survival assays
- **Author**: Jesse Lowe
- **Date**: 2026-10-05
- **URL**: https://genefish.wordpress.com/2026/10/05/tank-room-and-survival-assays-12/
- **Key finding**: Routine tank maintenance included a full water change on the right blue tank and water-chemistry checks (pH, alkalinity, ammonia, nitrite, nitrate) across all four tanks, which were in generally good condition (0-0.5 ppm nitrite, 0-20 ppm nitrate). The 24-hour mortality check for the oyster survival assay recorded 3 total mortalities.

---

### Daily Literature Connections — 2026-10-06
- **Author**: Cas Daniel
- **Date**: 2026-10-06
- **URL**: https://genefish.wordpress.com/2026/10/06/daily-literature-connections-2026-10-06/
- **Key finding**: This automated literature-linking post connected the prior day's 3-mortality tank survival result to three PubMed studies on oyster resilience. It noted that oysters can tolerate substantial salinity/toxicity stress over 24-48 hours with little to no mortality, and that hatchery-scale mortality variability is often tied to microbial community differences rather than water chemistry alone, offering supporting (not mechanistic) context for the low mortality count observed.

---

### Water chemistry trial
- **Author**: Jesse Lowe
- **Date**: 2026-10-07
- **URL**: https://genefish.wordpress.com/2026/10/07/water-chemistry-trial/
- **Key finding**: A new pilot test was set up to monitor water quality in a smaller aquarium fully stocked with oysters, with daily measurements planned over the following week. Baseline readings at trial start were 7.8 pH, 80 alkalinity, and 0 ammonia/nitrite/nitrate.

---

### Tank room and survival assays
- **Author**: Jesse Lowe
- **Date**: 2026-10-07
- **URL**: https://genefish.wordpress.com/2026/10/07/tank-room-and-survival-assays-13/
- **Key finding**: Full water changes were performed on the right blue and left blue tanks after readings showed elevated nitrite (~3 ppm) in two tanks prior to the change; post-change readings returned nitrite to near zero. The 72-hour oyster mortality assay check found 12 oysters still alive, and grey bins of 30 ppt seawater were prepped for further water changes on Thursday.

---

### Daily Literature Connections — 2026-10-08
- **Author**: Cas Daniel
- **Date**: 2026-10-08
- **URL**: https://genefish.wordpress.com/2026/10/08/daily-literature-connections-2026-10-08/
- **Key finding**: This automated post linked the prior day's tank nitrite readings (~3 ppm) and 12 surviving oysters to a preprint showing oysters can internally accumulate measurable nitrite from ambient exposure without a direct mortality effect. It concluded this is a comparative data point consistent with, but not a direct mechanistic explanation for, the survival observed in the lab's tanks.

---

### Oysters H2O2 priming experiment set-up
- **Author**: giselff250455090
- **Date**: 2026-10-08
- **URL**: https://genefish.wordpress.com/2026/10/08/oysters-h2o2-priming-experiment-set-up/
- **Key finding**: A new priming experiment was set up with nine containers (three replicates each of control, low-H2O2, and high-H2O2 treatments) in artificial seawater, to be left overnight with a mortality check planned for the next day. Supporting water system (grey bin) was refilled and tested, showing acceptable nitrate (~20 ppm), nitrite (0.5 ppm), alkalinity (~120 ppm), pH (7.8), and salinity (~32 ppt).

---

### 10.09-10: Sample point 2 for repeat stress at 35C
- **Author**: HazelAbrahamsonA
- **Date**: 2026-10-10
- **URL**: https://genefish.wordpress.com/2026/10/10/10-09-10-sample-point-2-for-repeat-stress-at-35c/
- **Key finding**: A second round of 24-hour heat/no-heat exposures at 35°C was conducted on oysters previously assigned to heat or control conditions and allowed a week to recover, creating four treatment groups by exposure history (heat/heat, no heat/heat, heat/no heat, no heat/no heat). Mortality after this second exposure was similar across all four groups (27-36%), suggesting no strong protective or sensitizing effect of prior heat exposure; survivors were sampled for future glycogen and qPCR gene expression analysis, though glycogen samples were only stored (not yet homogenized) due to time constraints.

---

### Daily Literature Connections — 2026-10-11
- **Author**: Cas Daniel
- **Date**: 2026-10-11
- **URL**: https://genefish.wordpress.com/2026/10/11/daily-literature-connections-2026-10-11/
- **Key finding**: This automated post connected the repeat-stress mortality result (similar mortality across all four exposure-history groups) to two external studies: a peer-reviewed paper showing shell-corroding endolithic symbionts can buffer oysters against heat stress by as much as 9.5°C, and a preprint showing parental immune-priming effects on offspring heat tolerance can reverse direction across a narrow temperature window. Together these suggested plausible explanations for why prior heat exposure didn't clearly protect or sensitize oysters in the lab's fixed 35°C challenge, though neither study used the same same-generation heat-preconditioning design.

---

## Cross-Notebook Patterns & Connections

_This section analyzes the compiled per-source summaries for shared themes, follow-up narratives, apparent contradictions, and multi-week historical connections across the lab's notebooks. Connections are surfaced only when a specific named entity ties the sources together — never from vague thematic similarity._

_No cross-notebook connections identified in this window._

### Historical Connections
- **GN020540 / Nup107 methylation in *Ostrea chilensis***: This week's Tumbling Oysters finding — a robust, population-specific methylation difference at GN020540 between Quilhua and Rio Pudeto — builds directly on the earlier site-level scan that first identified 62 CpG sites separating these same two populations. See [62 CpGs Separate Quihua From Rio Pudeto](https://sr320.github.io/tumbling-oysters/posts/86-och-dml-sites/) · 2026-08-21 (Steven Roberts, Tumbling Oysters).
- **Effort A Sequim Bay hardening project**: This week's final survival analysis (Ariana Huffmyer, 2026-10-07) traces back to the plan that established the 25°C daily hardening protocol and to the field closure that generated the oysters it was run on. See [Fall 2026 lab survival assessment plan](https://ahuffmyer.github.io/posts/2026-09-21-fall-lab-survival-assessment-plan.html) · 2026-09-21 (Ariana Huffmyer, Ariana Huffmyer Lab Notebook) and [Final assessment and closing Effort A experiment at Sequim Bay](https://ahuffmyer.github.io/posts/2026-09-23-sequim-final-field-assessment.html) · 2026-09-23 (Ariana Huffmyer, Ariana Huffmyer Lab Notebook).
- **Repeat heat-stress-at-35°C thesis project**: This week's second-exposure sample point (genefish WordPress, 2026-10-10) is the direct continuation of the same round that started and was first sampled just days earlier. See [10.01: Starting repeat stress at 35 C](https://genefish.wordpress.com/2026/10/02/10-01-starting-repeat-stress-at-35-c/) · 2026-10-02 (HazelAbrahamsonA, Genefish WordPress) and [10.02: Sample point 1 for repeat stress at 35 C](https://genefish.wordpress.com/2026/10/02/10-02-sample-point-1-for-repeat-stress-at-35-c/) · 2026-10-02 (HazelAbrahamsonA, Genefish WordPress).
- **Gape Monitoring project**: Sam White's prototype field deployment this week builds directly on his own earlier system design and simulation work for the same gape-monitoring hardware (magnetometer + RP2040 Adalogger). See [Gape Monitoring - Initial Configuration and Simulations](https://robertslab.github.io/sams-notebook/posts/2026/2026-09-08-Gape-Monitoring---Initial-Configuration-and-Simulations/) · 2026-09-08 (Sam White, Sam's Notebook).

---

## Data & Figures

_This section consolidates, grouped by source, the figure links and external data/repository links already surfaced in the per-source summaries above. It is a single entry point into the underlying data and figures for this window, not a new analysis._

### Tumbling Oysters (Steven Roberts)
- Chilean Flat Oyster WGBS: Three Populations, Nine Libraries: images/landscape-features.png
- Chilean Flat Oyster WGBS: Three Populations, Nine Libraries: images/landscape-metagene.png
- Chilean Flat Oyster WGBS: Three Populations, Nine Libraries: images/snp-check-classes.png
- Chilean Flat Oyster WGBS: Three Populations, Nine Libraries: images/gn020540-methylation.png
- Chilean Flat Oyster WGBS: Three Populations, Nine Libraries: images/hapa-replication.png
- Chilean vs Olympia Oyster Methylation, and What Sits Inside GN020540: images/cpg-oe-by-species.png
- Chilean vs Olympia Oyster Methylation, and What Sits Inside GN020540: images/ortholog-cpg-oe.png
- Chilean vs Olympia Oyster Methylation, and What Sits Inside GN020540: images/och-gbm-vs-cpg-oe.png
- Chilean vs Olympia Oyster Methylation, and What Sits Inside GN020540: images/gn020540-locus.png

### Ariana Huffmyer Lab Notebook
- Effort A Sequim Bay project final survival assay results: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261007/temperature_rounds.png?raw=true
- Effort A Sequim Bay project final survival assay results: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261007/survival_group.png?raw=true

### Sam's Notebook (Sam White)
- Data Analysis - Prototype M.gigas Gaping Pilot Project: gape_monitor_deployed.jpg
- Data Analysis - Prototype M.gigas Gaping Pilot Project: magnetometer_fried.jpg

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

### Thermal tolerance mechanisms in Pacific oysters (Crassostrea gigas)

**Source:** Ariana Huffmyer Lab Notebook (Effort A Sequim Bay project final survival assay results)
**Finding:** Two weeks of daily pre-exposure to 25°C significantly improved Pacific oyster survival during a later heat-stress challenge (time:group interaction P=0.026), though the absolute effect was small (LT50 56.1h treated vs. 55.1h control).

### [Adds context] [PubMed]: Identifying the regulatory network of the key lipid metabolism transcription factor peroxisome proliferator-activated receptor in oysters
Du et al., 2026 · PMID: 42331158 · https://pubmed.ncbi.nlm.nih.gov/42331158/

Identified two PPAR subtypes in oysters and found that PPARα, a transcription factor governing lipid metabolism, is more highly expressed and more stress-responsive in the relatively cold-tolerant *Crassostrea gigas* than in the warmer-adapted *C. angulata*, with an expression GWAS turning up dozens of candidate regulatory genes and a novel ubiquitination-degradation pathway controlling PPARα levels. This offers a possible molecular basis — lipid-metabolism gene regulation — for genetic variation in heat tolerance within *C. gigas*, though it does not test behavioral hardening or priming directly.

---

### [Adds context] [PubMed]: Epitranscriptomic erasers in bivalves: Evolutionary divergence and species-specific transcriptional plasticity of the ALKBH family under acute thermal stress
Xiong et al., 2026 · PMID: 42322884 · https://pubmed.ncbi.nlm.nih.gov/42322884/

Compared ALKBH (RNA/DNA demethylase) gene expression dynamics across 35 bivalve species and found that under acute heat shock, *C. gigas* sustains elevated ALKBH3 expression — unlike the more heat-sensitive scallop *Chlamys nobilis* — proposing this as a contributor to the oyster's comparatively strong thermal tolerance. This adds a potential epitranscriptomic layer relevant to how *C. gigas* copes with heat stress, complementing survival-curve data like this week's LT50 comparison, though it examines acute heat shock rather than multi-week hardening.

---

### [Adds context] [PubMed]: Integrated metabolomics and flow cytometry assessment reveals immune-metabolic modulation of Crassostrea (=Magallana) gigas hemolymph under hypoxic and elevated temperature conditions
Kim et al., 2026 · PMID: 42134734 · https://pubmed.ncbi.nlm.nih.gov/42134734/

Exposed *C. gigas* to hypoxia alone or combined with elevated temperature (28°C) for 13 days and found the combined stress depleted key amino acids and antioxidant metabolites while increasing hemocyte mortality and reducing phagocytic capacity, suggesting an energy-conservation strategy that trades immune function for survival under multi-stressor conditions. This offers physiological context suggesting that oysters surviving a heat challenge — such as those in this week's Effort A assay — may carry a hidden immune cost that a pure survival-curve analysis would not capture.

**Literature summary:** Three peer-reviewed papers (Du et al. 2026; Xiong et al. 2026; Kim et al. 2026), all in *Crassostrea gigas*, converge on distinct molecular and physiological mechanisms of thermal tolerance — a lipid-metabolism transcription factor (PPARα), an RNA-demethylase gene family (ALKBH), and an immune-metabolic trade-off under combined hypoxia/heat stress. None tests pre-exposure hardening directly, but together they point to multiple pathways that could underlie the small but real survival benefit observed in 25°C-hardened Effort A oysters, and flag hidden physiological costs that a survival curve alone would miss.

---

### Valve-gape biologging as a bivalve stress indicator

**Source:** Sam's Notebook (Data Analysis - Prototype M.gigas Gaping Pilot Project)
**Finding:** A prototype magnetometer-based gape logger on a Pacific oyster recorded the shell opening about 1 hour after deployment and remaining open until the oyster died and the sensor failed from water ingress roughly 4 hours later.

### [Adds context] [PubMed]: Behavioural and biochemical effects of underwater noise from vessel traffic on Baltic sea mussels (Mytilus spp.)
El-Dairi et al., 2026 · PMID: 41581363 · https://pubmed.ncbi.nlm.nih.gov/41581363/

Used continuous valve-gape recording alongside antioxidant and neurotoxicity biomarkers to show that underwater vessel noise alters mussel valve-closure behavior and oxidative-stress enzyme profiles, with effects depending on exposure duration. This demonstrates that fine-scale valve-gape biologging — the same general method as the lab's prototype magnetometer logger — reliably detects sub-lethal behavioral stress responses in bivalves, even though the stressor and species differ from this week's oyster heat/mortality application.

---

### [Adds context] [PubMed]: Effects of chemical leachates from offshore wind farm infrastructure on heart rate and valve gape of blue mussels
Alter et al., 2025 · PMID: 40602351 · https://pubmed.ncbi.nlm.nih.gov/40602351/

Paired continuous valve-gape and cardiac-activity monitoring with a thermal ramp to test how offshore-wind-farm coating leachates affect blue mussel stress physiology, finding leachate exposure altered cardiac-arrest frequency but not the temperature thresholds at which heart rate peaked or valves closed. This illustrates a design pattern — combining valve-gape telemetry with a second physiological signal — that could inform future iterations of the lab's gape logger, which currently records magnetometer-based valve position alone.

---

### [Adds context] [Preprints.org preprint — not peer-reviewed]: Development of the BioSentinel Health Index: A Proposed Framework to Support Sustainable Management of Marinas
Cottingham et al., 2026 · DOI: 10.20944/preprints202607.2368.v1 · https://doi.org/10.20944/preprints202607.2368.v1

Developed a framework (the "BioSentinel Health Index") that turns continuous, minute-scale bivalve valve-gape data from marina-deployed mussels into an ecosystem-health score, incorporating metrics like percent-time-open, rhythmic consistency, and coordinated valve-closure "alarm" events. This offers a ready-made set of analytical metrics for interpreting the kind of continuous valve-position time series the lab's prototype is designed to produce, suggesting concrete next-step analyses once the current sealing and reliability issues are resolved.

**Literature summary:** Two peer-reviewed papers (El-Dairi et al. 2026; Alter et al. 2025) and one preprint (Cottingham et al. 2026, not yet peer-reviewed) all use continuous valve-gape monitoring as a bivalve stress or health biomarker, though in mussels rather than oysters and for different stressors (noise, chemical leachates, general ecosystem health) than this week's lethal heat/mortality context. Together they support valve-gape biologging as an established, informative method and point to specific next steps — pairing gape data with a secondary physiological signal, or applying standardized health-index metrics — for strengthening future iterations of the lab's prototype gape logger.

---

> Generated by the `full-lab-digest` skill · 2026-10-06 to 2026-10-12 (7-day window)
