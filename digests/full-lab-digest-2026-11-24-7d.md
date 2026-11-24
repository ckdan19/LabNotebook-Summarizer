# Full Lab Digest — 2026-11-18 to 2026-11-24 (7 days)

> 3 of 7 sources had activity in the last 7 days. 4 had none.

---

## Tumbling Oysters (Steven Roberts)

_No new posts in the last 7 days._

---

## Ariana Huffmyer Lab Notebook

_No new posts in the last 7 days._

---

## Sam's Notebook (Sam White)

_No new posts in the last 7 days._

---

## Grace Crandall's Notebook

### FHL 2026 - New Standard Curve Plate Run and Comparing to Previous Curve
- **Date**: 2026-11-17
- **URL**: https://grace-ac.github.io/comparing-std-curves/
- **Categories**: FHL2026
- **Key finding**: Grace made a fresh serial dilution of the qPCR standard curve and ran it alone to compare against curves used in previous plates. By comparing Cq values between the new plate (plate 10) and a previous plate (plate 9), she confirmed her suspicion that all prior qPCR runs had actually used a standard curve spanning 3.00E+07 down to 3.00E+01, rather than the intended 3.00E+06 down to 3.00E+00. She raises open questions about whether to standardize future runs on the 3.00E+07–3.00E+01 range and whether previously run plates need their standard curve designation corrected retroactively.
- **Figures**:
  - local: ../notebook-images/2026-11-17/plate10-setthreshold100.PNG
  - local: ../notebook-images/2026-11-17/plate10-cleaned-setthreshold100.PNG
  - local: ../notebook-images/2026-11-17/plate9and10-cq-chart.png

_1 post from this window was already covered in a previous digest and is omitted here._

---

## Megan Ewing Lab Notebook

_No new posts in the last 7 days._

---

## Kathleen Durkin Lab Notebook

## ceasmallr

### Identifying overlapping DMRs in parents and offspring
- **Project**: ceasmallr
- **Date**: 2026-11-04
- **URL**: https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_11_04_DMR_overlap.html
- **Author**: Kathleen Durkin
- **Categories**: ceasmallr
- **Key finding**: Extends the project's parent/offspring DML overlap work to the DMR level, defining an "overlap" using DSS's own DMR-calling criteria (≥50bp, ≥3 CpGs) across egg, sperm, zygote, and larvae DMR sets. Overlapping DMRs are overwhelmingly directionally concordant, and offspring-sperm overlaps are both larger and more concordant than offspring-egg overlaps, reinforcing the project's recurring finding that paternal methylation has a stronger influence on offspring. Only partial overlap between zygote and larvae stages again suggests partial epigenetic reprogramming during development.
- **Figures**:
  - local: ./images/13-DMR-overlap-CTmask_files/figure-gfm/unnamed-chunk-8-1.png
  - local: ./images/13-DMR-overlap-CTmask_files/figure-gfm/unnamed-chunk-9-1.png

---

### Obtaining C. virginica functional annotations
- **Project**: ceasmallr
- **Date**: 2026-11-11
- **URL**: https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_11_11_functional_annot.html
- **Author**: Kathleen Durkin
- **Categories**: ceasmallr
- **Key finding**: Built a Uniprot/SwissProt-based GO annotation lookup table for the C. virginica genome (BLAST proteome vs. SwissProt, map proteins to genes, retrieve GO terms, map to GOslim), following the Roberts Lab Handbook workflow; the approach is inherently limited to protein-coding genes. About 61% of 34,608 genes received a functional annotation, with the most common GO-BP terms covering anatomical development, cell differentiation, and signaling — a reasonable annotation rate for a non-model invertebrate.
- **Figures**: none

---

### Functionally annotating DMLs/DMRs
- **Project**: ceasmallr
- **Date**: 2026-11-12
- **URL**: https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_11_12_functional_enrich.html
- **Author**: Kathleen Durkin
- **Categories**: ceasmallr
- **Key finding**: Joined the newly built functional-annotation table to the parental-treatment DML/DMR sets to characterize genomic context and associated GO/GOslim functions. Across sets, DMLs/DMRs are concentrated in gene bodies and intergenic regions with few in promoters; next step is a proper enrichment test (topGO/goseq) using all tested CpGs as the statistical background rather than the whole genome, since enrichment so far only describes which functions are present, not over-represented.
- **Figures**:
  - local: ./images/2026_11_12_functional_enrich/region_counts.png
  - local: ./images/2026_11_12_functional_enrich/goslim_counts.png

---

## misc

### Ideas/Questions Log
- **Project**: misc
- **Date**: not specified (front matter uses `date: "last-modified"`, no fixed real date for this running log)
- **URL**: https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/misc/2024_01_30_Ideas.html
- **Author**: Kathleen Durkin
- **Categories**: miscellaneous
- **Key finding**: This is a running personal brain-dump of research ideas/questions rather than a dated science post; this week two new dated entries were appended. One (2026/11/18) notes that sparse functional annotation (~60% in C. virginica) likely hides biologically important stress-response transcripts that are ignored by necessity in differential-expression studies. The other (2026/11/16) raises a methodological concern that the antibiotic included in the lab's Resazurin metabolic-assay "master mix" (used to suppress shell-microbiome activity) could cause unintended long-term shifts in oyster microbiome composition, which may matter for long-term performance studies even if negligible in routine hatchery assays.
- **Figures**: none

---

## Genefish WordPress

### Tank room, SHORE room and water chemistry trials
- **Author**: Jesse Lowe
- **Date**: 2026-11-18
- **URL**: https://genefish.wordpress.com/2026/11/18/tank-room-shore-room-and-water-chemistry-trials-2/
- **Key finding**: Routine mortality checks and a full water change were performed across all tanks, with standard holding tanks staying near-zero for ammonia/nitrite while the dedicated water chemistry trial tank remained severely degraded (pH 7.6, 80 Alk, 0.25+ ppm ammonia, 0.5 ppm nitrite, 200+ ppm nitrate). Despite the extreme water chemistry, no new mortalities occurred since nitrate reached 200 ppm, leaving the trial total at 3 mortalities so far.

---

### 11.18: first exposure for sublethal/lethal experiment
- **Author**: HazelAbrahamsonA
- **Date**: 2026-11-18
- **URL**: https://genefish.wordpress.com/2026/11/18/11-18-first-exposure-for-sublethal-lethal-experiment/
- **Key finding**: This post documents the start of an experiment testing whether sublethal heat priming affects survival and physiology under subsequent lethal heat stress in oysters. A first 1-hour, 37°C exposure was delivered with improved temperature consistency (±0.3°C), a subset of oysters was sampled, and the rest returned to tanks for a week of recovery before a planned 44°C lethal exposure; samples will later be assessed for glycogen levels and heat-shock/metabolic gene expression.

---

### Daily Literature Connections — 2026-11-18
- **Author**: Cas Daniel
- **Date**: 2026-11-18
- **URL**: https://genefish.wordpress.com/2026/11/18/daily-literature-connections-2026-11-18/
- **Key finding**: This automated digest links Jesse Lowe's water chemistry trial observations to recent literature. It cites a PubMed study showing sustained ammonia exposure drives haemocyte death via an upregulated ammonia transporter gene in Pacific oysters, and a Research Square preprint on a related oyster species showing elevated alkalinity under low salinity suppresses ammonia excretion before survival losses appear — together suggesting the trial tank's low mortality may mask accumulating physiological stress.

---

### Water Quality Testing & Adjustment, Feeding Regimen Adjustment for Aquilonastras + Quick Transcriptomic Update
- **Author**: Samuel Slutz
- **Date**: 2026-11-19
- **URL**: https://genefish.wordpress.com/2026/11/19/water-quality-testing-adjustment-feeding-regimen-adjustment-for-aquilonastras-quick-transcriptomic-update/
- **Key finding**: Multi-day water quality troubleshooting for a starfish tank found problematically high nitrite/nitrate, which was addressed through successive partial water changes and reduced feeding, eventually bringing ammonia and nitrite back near zero. An attempted continuous water-exchange system between an auxiliary bucket and the main tank failed due to uneven pump flow rates and was reverted to the standard setup; separately, a mentoring arrangement with Grace was established for transcriptomics/bioinformatics work.

---

### Tank room, SHORE room and water chemistry trials
- **Author**: Jesse Lowe
- **Date**: 2026-11-20
- **URL**: https://genefish.wordpress.com/2026/11/20/tank-room-shore-room-and-water-chemistry-trials-3/
- **Key finding**: Routine mortality checks and water parameter logging across all tanks showed standard holding tanks remaining stable (near-zero ammonia/nitrite), while the water chemistry trial tank continued to show degraded conditions (pH 7.6, 40 Alk, 0.25+ ppm ammonia, 0.5 ppm nitrite, 200+ ppm nitrate). No new issues were reported beyond the ongoing elevated nitrogenous waste trend in the trial tank.

---

### Broodstock Resazurin Assay
- **Author**: jbalzer5
- **Date**: 2026-11-20
- **URL**: https://genefish.wordpress.com/2026/11/20/broodstock-resazurin-assay/
- **Key finding**: A resazurin-based metabolic assay was run on broodstock oysters of three size classes (10mm, 40mm, 70mm) to assess metabolic activity via fluorescence as a proxy for oxidative metabolism. Oysters and 12-well plate controls were incubated at 36°C for four hours with temperature and fluorescence measured every 30 minutes, and subsampled solution was later run on a 96-well plate for endpoint analysis.

---

### 11.20: Methods drafting
- **Author**: HazelAbrahamsonA
- **Date**: 2026-11-20
- **URL**: https://genefish.wordpress.com/2026/11/20/11-20-methods-drafting/
- **Key finding**: Planned RNA extractions were postponed because the lab ran out of DNase I, with a new order (placed by Sam) expected to arrive within 1-2 weeks. In the interim, the author pivoted to drafting the methods section of their senior thesis.

---

### Daily Literature Connections — 2026-11-21
- **Author**: Cas Daniel
- **Date**: 2026-11-21
- **URL**: https://genefish.wordpress.com/2026/11/21/daily-literature-connections-2026-11-21/
- **Key finding**: This automated digest again connects Jesse Lowe's trial tank data (degraded water chemistry, low mortality) to recent literature, adding two new PubMed papers beyond the prior post's citation. One shows moderate salinity optimizes oyster ammonia-excretion capacity while extremes impair it, and another finds ambient ammonia and nitrate shape pathogen-associated microbiome shifts in oysters/mussels — jointly suggesting the trial tank's chemistry could be driving sublethal immune, excretory, and microbiome-level stress not yet reflected in survival counts.

---

## Cross-Notebook Patterns & Connections

_This section analyzes the compiled per-source summaries for shared themes, follow-up narratives, apparent contradictions, and multi-week historical connections across the lab's notebooks. Connections are surfaced only when a specific named entity ties the sources together — never from vague thematic similarity._

### Temporal Narratives
- **Resazurin assay master mix (antibiotic component)** — Kathleen Durkin's Ideas/Questions log (2026-11-16) raises an open methodological question about whether the antibiotic in the lab's Resazurin assay "master mix" (used to suppress shell-microbiome activity) could cause unintended long-term oyster microbiome shifts. Four days later, the genefish WordPress notebook's "Broodstock Resazurin Assay" post (jbalzer5, 2026-11-20) documents an active Resazurin assay run on broodstock oysters using what appears to be the same master-mix protocol, with no indication the concern has yet been addressed.

### Historical Connections
- **Resazurin assay master mix (antibiotic component)** — the recipe Kathleen is questioning is documented in "Resazurin assay and heat stress experiment continued" (giselff250455090, 2026-10-21, wordpress): 5.87 mL DMSO and 58.74 mL antibiotic solution added to the resazurin stock, confirming the master mix this week's Broodstock Resazurin Assay post appears to continue using unchanged. See https://genefish.wordpress.com/2026/10/21/resazurin-assay-and-heat-stress-experiment-continued/
- **FHL2026 qPCR standard curve** — Grace's discovery this week that all prior FHL2026 qPCR plates used a 3.00E+07–3.00E+01 standard curve rather than the intended 3.00E+06–3.00E+00 range casts doubt on Cq-based results reported in earlier FHL2026 qPCR posts, including "Current FHL 2026 qPCR Results" (2026-10-13, Grace Crandall) and "qPCR - Plate 9 - FHL 2026 Eelgrass Swab DNA" (2026-10-13, Grace Crandall). ⚠️ Needs human verification — Grace or Sam should re-check whether those plates' Cq values were quantified against the mislabeled curve and whether result interpretations need correction. See https://grace-ac.github.io/updated-FHL-2026-qPCR_results/ and https://grace-ac.github.io/eelgrassswabDNA-qPCR-plate9/
- **DMR overlap pipeline (DSS/MACAU, parent-offspring methylation)** — this week's "Identifying overlapping DMRs in parents and offspring" (2026-11-04, surfaced above) builds directly on two same-day archived posts: "Rerunning DSS with C/T SNPs masked" defines the Offspring/Zygote/Larvae vs. Parents-Egg/Sperm categories used in the overlap analysis, and "Generating ceasmallr figures for GSS" produces the DML/DMR/offspring/sperm figure groundwork the overlap post extends. See https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_11_04_CTmask.html and https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_11_04_GSS_figures.html
- **Sublethal/lethal heat priming experiment** — HazelAbrahamsonA's "11.18: first exposure for sublethal/lethal experiment" (surfaced above) is a direct continuation of their own earlier post "10.21: Stress exposures for 35 C and sublethal/lethal projects" (2026-10-21), which laid out the same sublethal-priming-then-lethal-exposure design now being executed. See https://genefish.wordpress.com/2026/10/21/10-21-stress-exposures-for-35-c-and-sublethal-lethal-projects/

---

## Data & Figures

_This section consolidates, grouped by source, the figure links and external data/repository links already surfaced in the per-source summaries above. It is a single entry point into the underlying data and figures for this window, not a new analysis._

### Grace Crandall's Notebook
- FHL 2026 - New Standard Curve Plate Run and Comparing to Previous Curve: ../notebook-images/2026-11-17/plate10-setthreshold100.PNG
- FHL 2026 - New Standard Curve Plate Run and Comparing to Previous Curve: ../notebook-images/2026-11-17/plate10-cleaned-setthreshold100.PNG
- FHL 2026 - New Standard Curve Plate Run and Comparing to Previous Curve: ../notebook-images/2026-11-17/plate9and10-cq-chart.png

### Kathleen Durkin Lab Notebook
- Identifying overlapping DMRs in parents and offspring: ./images/13-DMR-overlap-CTmask_files/figure-gfm/unnamed-chunk-8-1.png
- Identifying overlapping DMRs in parents and offspring: ./images/13-DMR-overlap-CTmask_files/figure-gfm/unnamed-chunk-9-1.png
- Functionally annotating DMLs/DMRs: ./images/2026_11_12_functional_enrich/region_counts.png
- Functionally annotating DMLs/DMRs: ./images/2026_11_12_functional_enrich/goslim_counts.png

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

### Resazurin assay antibiotic exposure and oyster microbiome

**Source:** Kathleen Durkin's notebook (Ideas/Questions log) and genefish WordPress (Broodstock Resazurin Assay)
**Finding:** Kathleen raised an open question about whether the antibiotic included in the lab's Resazurin metabolic-assay master mix (used to suppress shell-microbiome activity) could cause unintended long-term shifts in oyster microbiome composition.

### [Adds context] [PubMed]: The resistome of European coastal environments revealed by high-resolution targeted metagenomics in oysters
Auguste et al., 2026 · PMID: 42934726 · https://pubmed.ncbi.nlm.nih.gov/42934726/

Using targeted metagenomic sequencing across four European sites, researchers mapped the full antibiotic-resistance-gene (ARG) "resistome" of the Pacific oyster *Magallana gigas*, finding over 33,000 ARG sequences spanning 450+ genes concentrated in multidrug efflux systems. ARG abundance was higher at sites with greater human impact, and a small number of bacterial taxa carried a disproportionate share of resistance genes despite low relative abundance. This confirms oyster-associated microbial communities already carry substantial latent antibiotic-resistance capacity, relevant background for interpreting how a lab antibiotic additive might reshape or select within that existing resistome.

---

### [Adds context] [PubMed]: Vibrio Community Structure Shapes the Diversity of Carbenicillin-Hydrolysing Class A β-Lactamase Circulating in European Coastal Environments
Reggiardo et al., 2026 · PMID: 42554126 · https://pubmed.ncbi.nlm.nih.gov/42554126/

This study characterized β-lactamase antibiotic-resistance genes circulating among Vibrio bacteria associated with European oyster-farming environments, finding that specific Vibrio clades structure which resistance genes dominate and that circulation dynamics track seawater temperature. It shows antibiotic-resistance genes in oyster-associated microbiomes are already shaped by environmental and seasonal pressures rather than static, suggesting an added antibiotic exposure could interact with an already-dynamic resistance landscape.

---

### [Supports] [PubMed]: Effects of aquaculture practices on oyster microbiome and pathogenic Vibrio levels
Almuhaideb et al., 2026 · PMID: 41395968 · https://pubmed.ncbi.nlm.nih.gov/41395968/

Comparing on-bottom vs. floating-cage oyster aquaculture systems over several months, this study found that husbandry practice significantly altered the diversity of the oyster microbiome, including the distribution of phage, antibiotic-resistance, and virulence-factor genes, with floating cages showing higher genetic representation of pathogenic Vibrio. This directly supports the premise behind Kathleen's question: oyster microbiome composition is measurably sensitive to differences in husbandry conditions, lending plausibility to the concern that a recurring antibiotic additive could produce a lasting compositional shift.

**Literature summary:** All three retrieved papers are peer-reviewed (no preprints met the relevance bar). None test Kathleen's exact scenario — repeated antibiotic exposure during a brief metabolic assay — but together they establish that oyster-associated microbiomes already carry a large, environmentally-responsive pool of antibiotic-resistance genes, and that husbandry/environmental differences measurably reshape oyster microbiome composition. This supports treating Kathleen's concern as a plausible, testable hypothesis rather than a purely theoretical one.

---

### Parent-offspring DMR overlap and paternal methylation influence in C. virginica

**Source:** Kathleen Durkin's notebook ("Identifying overlapping DMRs in parents and offspring")
**Finding:** Offspring-sperm DMR overlaps are larger and more directionally concordant than offspring-egg overlaps in the eastern oyster (*Crassostrea virginica*), indicating paternal methylation has a stronger influence on offspring methylation patterns; partial zygote-larvae overlap suggests incomplete epigenetic reprogramming during development.

### [Adds context] [bioRxiv preprint — not peer-reviewed]: Prior exposure to hypoxia alters DNA methylation patterns in the eastern oyster
McDonough et al., 2025 · DOI: 10.64898/2025.12.15.694390 · https://doi.org/10.64898/2025.12.15.694390

This preprint exposed juvenile eastern oysters (*Crassostrea virginica*) to hypoxia at two life timepoints and used methylRAD sequencing to show that earlier stress exposure leaves a lasting signature on gene-body DNA methylation, with differentially methylated genes concentrated in oxidative-stress, metabolism, and transcription pathways. While this is a within-individual environmental "memory" effect rather than parent-to-offspring inheritance, it reinforces that in *C. virginica*, DNA methylation is concentrated in gene bodies and can encode a durable, condition-specific record of past exposure — relevant background for interpreting why paternal (sperm) methylation signatures might persist more strongly into offspring than maternal (egg) signatures.

**Literature summary:** No peer-reviewed PubMed papers matched Kathleen's specific parent-offspring DMR overlap finding in the last 12 months. One bioRxiv preprint (not yet peer-reviewed) on hypoxia-induced methylation memory in the same species provides indirect supporting context for gene-body methylation as a durable epigenetic signal, but it does not directly test paternal vs. maternal transmission.

---

### Chronic ammonia/nitrite stress masking mortality in a water chemistry trial tank

**Source:** genefish WordPress (Jesse Lowe's tank room/water chemistry trial posts)
**Finding:** A water chemistry trial tank with chronically elevated ammonia (0.25+ ppm), nitrite (0.5 ppm), and nitrate (200+ ppm) showed no additional oyster mortality across multiple checks, suggesting sublethal physiological stress not reflected in survival counts.

### [Supports] [PubMed]: Multi-Omics Analysis of Hepatopancreatic Responses to Ammonia Nitrogen Stress in Diploid Pacific Oysters
Qiu et al., 2026 · PMID: 42738581 · https://pubmed.ncbi.nlm.nih.gov/42738581/

Exposing diploid Pacific oysters to ammonia nitrogen stress for up to 48 hours, this study combined histopathology, antioxidant enzyme assays, transcriptomics, and metabolomics to show progressive hepatopancreatic tissue injury and coordinated shifts in oxidative-stress response, transmembrane transport, and amino-acid metabolism. This directly supports the trial tank's observation that chronically degraded ammonia chemistry produced no additional mortality: this paper shows ammonia stress causes substantial sublethal tissue and metabolic damage that would not necessarily appear as mortality on the timescale observed.

**Literature summary:** One peer-reviewed paper directly supports the hypothesis that the trial tank's degraded ammonia/nitrite/nitrate chemistry is producing sublethal physiological damage not captured by mortality counts alone.

---

> Coverage limited to papers indexed on PubMed and preprints discoverable via Europe PMC (which indexes bioRxiv, Authorea Preprints, Research Square, medRxiv, and other preprint servers), restricted to the last 12 months. **Preprints have not been peer-reviewed** and should be interpreted with appropriate caution.

---

> Generated by the `full-lab-digest` skill · 2026-11-18 to 2026-11-24 (7-day window)
