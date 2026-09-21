# Full Lab Digest — 2026-09-14 to 2026-09-21 (7 days)

> 6 of 7 sources had activity in the last 7 days. 1 had none.

---

## Tumbling Oysters (Steven Roberts)

_Note: this notebook's agent-file format has no URL/published-permalink convention, so per its contract no URL line is included in the per-post blocks below — the closest reference is the GitHub tree link added here for each post._

### Population structure in Olympia oyster low-coverage WGS, and what a chromosome-scale assembly changes about it
- **Date**: 09-17-2026
- **Author**: Steven Roberts
- **Categories**: Genomics, Computing
- **Tree**: https://github.com/sr320/tumbling-oysters/tree/main/posts/89-oly-lcwgs-population-structure
- **Key finding**: Across 109 Olympia oyster libraries from 15 collection sites, low-coverage WGS reveals strong, real neutral population structure: two outer-coast collections (Coos Bay, OR and a site labeled "WB") form one cluster far from the Salish Sea, within which basins (Hood Canal, South Sound, North Sound, the Strait) separate on later PCs while sites within a basin overlap. Genome-wide Hudson Fst averages 0.115 among the 13 Salish Sea sites versus 0.174 between either outer-coast site and the Salish Sea. Careful re-analysis showed the "WB" site is genetically not Westcott Bay as recorded but is far more consistent with Willapa Bay, an outer-coast estuary — a mislabeling that also affects the companion GEA study. A new chromosome-scale assembly did not change the structure results (a coordinate-system property) but revealed that 38.7% of placeable SNPs fall in repeat-masked regions, meaning the absolute Fst magnitudes computed above are likely inflated and should be treated as provisional.
- **Figures**:
  - local: images/structure-fst-panel.png

---

### No Genotype-Environment Association in Olympia Oyster lcWGS
- **Date**: 09-19-2026
- **Author**: Steven Roberts
- **Categories**: Genomics, Computing
- **Tree**: https://github.com/sr320/tumbling-oysters/tree/main/posts/88-oly-lcwgs-rda
- **Key finding**: Using redundancy analysis on 12.86 million SNPs across 13-15 Olympia oyster collection sites, the study tested whether allele frequencies track local environmental conditions (temperature, salinity range, chlorophyll) beyond geography and ancestry. No genotype-environment association was detected at genome scale (adjusted R² = -0.004, p = 0.55), forward selection admitted zero predictors, and no locus or gene set passed FDR correction, while neutral population structure by ancestry was real and substantial (adjusted R² = 0.111). Two unplanned findings — a mislabeled collection site later reinterpreted as Willapa Bay, and evidence that the design's binding constraint is the number of sampled sites (13) rather than sequencing depth — turned out to matter more than the primary negative result, and the authors argue the negative finding does not rule out local adaptation given how coarse the environmental measurements were.
- **Figures**:
  - local: images/rda-summary.png
  - local: images/rda-genomewide.png

---

### Does a 4-hour resazurin trace forecast field performance? Mostly no
- **Date**: 09-19-2026
- **Author**: Steven Roberts
- **Categories**: Aquaculture, Computing
- **Tree**: https://github.com/sr320/tumbling-oysters/tree/main/posts/90-resazurin-index-catalogue
- **Key finding**: A catalogue of 284 distinct indices derived from individual-level 4-hour, 40°C resazurin metabolic assays on ~160 ploidy-trial oysters was tested against field survival, growth, condition index, and yield outcomes, with rigorous permutation-based multiplicity control. Zero of 284 indices cleared a family-wise p < 0.05 threshold for any phenotype; the closest leads were triploid growth/tissue weight (rho 0.40-0.42, p 0.08-0.11, consistent across related features) and diploid survival (AUC 0.74, but resting on only 9 deaths and running opposite to an earlier family-level USDA result). The authors attribute the weak signal mainly to using a single family (little heritable variation to resolve) and to scoring survival as a binary endpoint rather than duration, and conclude the assay is not yet usable as an individual-level field-performance screen, recommending a repeat with more deaths and recorded field duration.
- **Figures**:
  - local: images/survival_permutation_ceiling.png
  - local: images/association_heatmap_top_indices.png
  - local: images/best_index_scatter.png
  - local: images/nested_composite_cv.png
  - local: images/assay_duration.png
  - local: images/screening_utility.png

---

## Ariana Huffmyer Lab Notebook

_No new posts in the last 7 days._

---

## Sam's Notebook (Sam White)

### Samples Received - Freezer Boxes from Katherine Silliman for Storage
- **Date**: 2026-09-10
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-09-10-Samples-Received---Freezer-Boxes-from-Katherine-Silliman-for-Storage/
- **Author**: Sam White
- **Categories**: Samples Received
- **Key finding**: Logistical post — the lab received frozen (-80°C, shipped on dry ice) sample boxes from Katherine Silliman (NOAA AOML) for long-term storage from her PhD research. Most boxes were transferred into the lab's primary -80°C freezer and logged in the freezer inventory spreadsheet, while a few large plastic boxes that didn't fit the primary freezer's racks were placed in the secondary -80°C freezer instead.
- **Figures**:
  - local: ./freezer-boxes-01.jpg
  - local: ./freezer-boxes-02.jpg

_1 post from this window was already covered in a previous digest and is omitted here (Gape Monitoring - Initial Configuration and Simulations, cosmetic image-filename fix only)._

---

## Grace Crandall's Notebook

### Oyster El Nino Bucket Temp, Sal Checks and Feeding Log
- **Date**: 2026-09-16
- **URL**: https://grace-ac.github.io/oysterbucket-checks/
- **Categories**: OysterBucket
- **Key finding**: Rolling log of daily temperature, salinity, and feeding checks for Control (~18C/20psu) vs. El Nino-simulated (~26C/30psu) oyster buckets from 9/11–9/16. On 9/16, adding freshwater to the El Nino bucket produced a bad smell, prompting a mortality check (12–28 morts per bag across 5 bags) and a full water change with 30ppt water after consulting Ariana on needed adjustments.
- **Figures**:
  - local: ../notebook-images/2026-oyster-bucket/IMG_8184.JPG

---

### Oyster Family Mortality Tracking and Rack Set Up
- **Date**: 2026-09-18
- **URL**: https://grace-ac.github.io/oyster-wetlab-setup-mortchecks/
- **Categories**: OysterMortRack
- **Key finding**: Tracks daily mortality across six oyster families (2, 5, 6, 7, 9, 10) in a 4-row/6-tank recirculating rack system set up on 9/9, with cumulative mortality by 9/18 ranging from 5% (family 7) to 26.7% (family 10). The recirculation tubing repeatedly popped out of the holding tank (9/13 and 9/14), draining the system each time and requiring emergency refills; plan is to source replacement valves and tubing pending Steven's approval.
- **Figures**:
  - local: ../notebook-images/2026-oyster-mort-check/lab-setup.JPG

---

### Oyster OA Mortality Log
- **Date**: 2026-09-18
- **URL**: https://grace-ac.github.io/oysterOA-mort-checks-log/
- **Categories**: OysterOA
- **Key finding**: Daily mortality log comparing a Control tank and an ocean-acidification (OA) treated tank from 9/12–9/18; by 9/18 the Control tank had accumulated 14 total mortalities versus 2 for the OA treatment. The same recirculation-tube failures noted in the mort-rack log briefly drained this system on 9/13 and 9/14, both resolved within the day.
- **Figures**: none

---

### Tank Room Water Chemistry Log
- **Date**: 2026-09-20
- **URL**: https://grace-ac.github.io/oysterwater-chem-log/
- **Categories**: OysterWaterChem
- **Key finding**: Covering for Jesse, Grace ran the weekly water-quality SOP (pH, nitrite, nitrate, ammonia, alkalinity via API/Tetra test strips) across four tanks (Blue Left/Right, Yellow Left/Right) from 9/8–9/20. Several elevated readings triggered water changes and filter-bag swaps (notably Yellow Left ammonia spiking to 8.0++ ppm on 9/14 and 9/16), and a spare batch of 30ppt seawater was prepared and labeled for other lab members' tank changes.
- **Figures**: none

**Warnings**:
- Skipped _posts/2026-09-13-oysterOA-mort-checks-log.md: deleted in this window.
- Skipped _posts/2026-09-13-oysterbucket-checks.md: deleted in this window.

---

## Megan Ewing Lab Notebook

### Who's That Clam?
- **Date**: 09-18-2026
- **URL**: https://meganewing.github.io/mewing-notebook/posts/2026-08/whosthatclam.html
- **Author**: Megan Ewing
- **Categories**: projects
- **Key finding**: This is a logistical reference post identifying and labeling the various clam and cockle groups left in the yellow tank. It documents the silo labeling scheme for manila seed (combination-, heat-, immune-primed, and control treatments), the mesh-bag coding for remaining Agate Pass basket cockles (treatment/priming/retrieval-time/replicate), and the cattle-tag ID ranges for field-collected manila clams from Agate Pass and Westcott sites, plus a note that some cockles escaped their bags during sampling and should be left in the silo or given to Andy for starfish feed. No experimental results are reported — it's purely an inventory/labeling reference for lab members.
- **Figures**: none

---

## Kathleen Durkin Lab Notebook

### Lit review: how to statistically test for inheritance
- **Project**: ceasmallr
- **Date**: 2026-09-08
- **URL**: https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_09_08_enrichment_approach.html
- **Author**: Kathleen Durkin
- **Categories**: ceasmallr
- **Key finding**: Reviewed prior transgenerational-methylation papers (Rondon et al. 2017, Feiner et al. 2022, Peterson et al. 2024) looking for a close methodological match for testing inherited, treatment-induced DNA methylation, but concluded none share the ceasmallr design (treated parents, multi-lifestage offspring) closely enough to be directly useful. Turned instead to a methods survey (Shafi et al. 2017) of differential-methylation approaches for bisulfite sequencing data, concluding that beta-binomial mixed-model tools are the best fit, since logistic-regression tools (methylKit) ignore biological variation and smoothing tools handle sharp, single-CpG changes poorly. Singled out `DSS` (good for small samples, handles multiple covariates) and especially `MACAU` (the only reviewed tool that explicitly models population/relatedness structure) as the two candidates to pursue for handling pseudoreplication from shared parentage.
- **Figures**:
  - local: ./images/Shafi_Fig.png
  - local: ./images/Shafi_Table.png

---

### Details of DSS functionality
- **Project**: ceasmallr
- **Date**: 2026-09-09
- **URL**: https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_09_09_DSS_details.html
- **Author**: Kathleen Durkin
- **Categories**: ceasmallr
- **Key finding**: Documented the mechanics of the `DSS` workflow (`DMLtest()` with smoothing, then `callDML()`/`callDMR()` with a 0.25 methylation-difference and 0.01 adjusted-p threshold for DMLs, and region-calling parameters for DMRs) and the multifactor fitting function `DMLfit.multifactor()`. Clarified the conceptual difference between the additive model (`treatment + stage`), which assumes a constant treatment effect across lifestages, and the interaction model (`treatment + stage + treatment:stage`), which allows the treatment effect to vary by lifestage and directly tests whether parental exposure's effect changes from zygote to larvae.
- **Figures**:
  - local: ./images/DSS_models.png

---

### Rerunning offspring DSS with all samples
- **Project**: ceasmallr
- **Date**: 2026-09-09
- **URL**: https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_09_09_DSS_rerun_allsamp.html
- **Author**: Kathleen Durkin
- **Categories**: ceasmallr
- **Key finding**: Tested whether `DSS`'s better tolerance of missing data would let low-coverage samples previously excluded be retained, by re-running the offspring analysis with all 32 samples instead of the subsampled set. The full-sample run yielded more DMLs/DMRs in the multifactor (additive and interaction) models (e.g., additive: 11,356 DMLs/1,893 DMRs vs. 8,404/1,788) due to the sample-size gain outweighing fewer loci passing filtering, but fewer DMLs/DMRs in the single-stage smoothed runs, where the loss of loci after filtering dominated.

---

### Details of MACAU usage and functionality
- **Project**: ceasmallr
- **Date**: 2026-09-15
- **URL**: https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_09_15_MACAU.html
- **Author**: Kathleen Durkin
- **Categories**: ceasmallr
- **Key finding**: Worked through the `MACAU` user manual to understand how the tool's binomial mixed model accounts for population/relatedness structure, noting it requires complete count data (no missingness, unlike DSS) and needs a pre-computed relatedness matrix, which could come from SNP-calling on WGBS data (e.g., via `Revelio` + `GEMMA`) or more simply from pedigree/parent-ID information using R packages like `pedigree` or `nadiv`. Discovered partway through that a newer R package, `MACAU2`, exists, which avoids needing IT help to install the original command-line tool on the lab's compute cluster.

---

### Implementing MACAU
- **Project**: ceasmallr
- **Date**: 2026-09-16
- **URL**: https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_09_16_MACAU_implementation.html
- **Author**: Kathleen Durkin
- **Categories**: ceasmallr
- **Key finding**: Ran an initial `MACAU`-style differential methylation analysis (via `PQLseq2`, due to package incompatibilities with the MACAU2 R package) on all 32 offspring samples, using a simple half-sib relatedness matrix built from parent IDs; of 2,148,546 filtered sites, 799 treatment DMLs were identified at FDR < 0.05 (361 hyper-, 438 hypo-methylated in exposed offspring), far fewer than the 11,356 DMLs found by DSS on the same samples. Flagged a key confound: because all crosses were within-treatment (control x control, exposed x exposed), the parent-ID-based relatedness matrix is collinear with treatment (all cross-treatment relatedness values are 0), producing uninterpretable heritability (h2) estimates of 0/1/NA and indicating the fix will require building the relatedness matrix from actual genotype data (e.g., `Revelio` + `GEMMA`) rather than pedigree alone.
- **Figures**:
  - local: ./images/relatedness-diagnostics-1.png

---

## Genefish WordPress

### Full Lab Digest — 2026-09-08 to 2026-09-14 (7 days)
- **Author**: Cas Daniel
- **Date**: 2026-09-14
- **URL**: https://genefish.wordpress.com/2026/09/14/full-lab-digest-2026-09-08-to-2026-09-14-7-days/
- **Key finding**: Automated cross-notebook digest aggregating activity from six affiliated lab notebooks (Tumbling Oysters, Ariana Huffmyer Lab, and others) for the week of 09-07 to 09-14. Highlights included a genomic comparison finding sea star wasting disease pathogen virulence genes intact across host species with no clear resistance-gene explanation, family-specific survival responses to heat-hardening in a Manchester oyster trial, and a delayed-onset mortality pattern (1/39 dead at 2 days, 16/39 by one week) following 24-hour ocean alkalinity enhancement (OAE) exposure that appears to conflict with a mussel study showing no OAE mortality effect.

---

### 09.15: GAPDH qPCR on 35 C repeat stress samples
- **Author**: HazelAbrahamsonA
- **Date**: 2026-09-15
- **URL**: https://genefish.wordpress.com/2026/09/15/09-15-qpcr-on-35-c-repeat-stress-samples/
- **Key finding**: Logistical qPCR run measuring GAPDH expression in samples from a repeated 35°C temperature-stress experiment, using cDNA reverse-transcribed the prior week. This housekeeping-gene data will be used to normalize expression of the target genes (HSP70/90, ATP synthase, citrate synthase) in subsequent analyses.

---

### 09.16: HSP70/90 qPCR and mortality evaluation
- **Author**: HazelAbrahamsonA
- **Date**: 2026-09-16
- **URL**: https://genefish.wordpress.com/2026/09/16/09-16-hsp70-90-qpcr/
- **Key finding**: In the 35°C repeated heat-stress experiment, HSP70 and possibly HSP90 expression decreased after heat exposure, with a smaller decrease in oysters previously primed by an earlier heat exposure, suggesting a priming effect consistent with an earlier 32°C/48-hour experiment. In a separate lethal priming experiment (37°C prime, 44°C challenge), both primed and unprimed oysters showed 100% survival, contrary to literature-based expectations, possibly due to inconsistent water heating noted in a prior post.

---

### 09.17: ATP synthase/citrate synthase qPCR
- **Author**: HazelAbrahamsonA
- **Date**: 2026-09-17
- **URL**: https://genefish.wordpress.com/2026/09/17/09-17-atp-synthase-citrate-synthase-qpcr/
- **Key finding**: ATP synthase and citrate synthase expression (normalized to GAPDH) was evaluated in the same 35°C repeated-stress samples, showing high variability but a visual trend of higher expression in heat-primed oysters, consistent with the HSP70/HSP90 pattern. This contradicts a previous experiment under different exposure conditions where primed oysters showed lower ATP synthase expression, a discrepancy the author plans to investigate further.

---

### 09-9-2026 and 09-10-2026 In Lab Post
- **Author**: Samuel Slutz
- **Date**: 2026-09-17
- **URL**: https://genefish.wordpress.com/2026/09/17/09-9-2026-and-09-10-2026-in-lab-post/
- **Key finding**: Logistical post describing assistance to a labmate (Megan) with resazurin well-plate assays, including pipetting reagent, arranging and photographing cockles and manila clams, transferring clams between plates, washing labware, and reading plates. No original results reported; framed as a mentorship/training experience.

---

### 09-17-2026 Update
- **Author**: Samuel Slutz
- **Date**: 2026-09-17
- **URL**: https://genefish.wordpress.com/2026/09/17/09-17-2026-update/
- **Key finding**: Refined a UniProt GO-term search strategy for extracellular matrix proteins, switching from the keyword "collagen" (which returned irrelevant hits) to the specific GO tag GO:0031012, in order to identify structural/matrix-related proteins more precisely. Noted an unexplained finding that D. imbricata expresses a venom phosphodiesterase (typically found in rattlesnake venom) in coelomic fluid, speculating it may function as an anti-clotting agent, with follow-up comparison across body regions proposed.

---

### PCSGA conference, results, and slides
- **Author**: acasey2
- **Date**: 2026-09-17
- **URL**: https://genefish.wordpress.com/2026/09/17/pcsga-conference-results-and-slides/
- **Key finding**: Presented preliminary results at PCSGA from in situ and lab-based ocean alkalinity enhancement (OAE, NaOH) exposures. In situ OAE increased growth in Pacific oysters but had no effect or worsened growth in Olympia oysters, while lab-based OAE exposures reduced metabolic rate across all life stages tested.

---

### Checking Oyster Mortality in El Niño Experiment
- **Author**: robertsblr
- **Date**: 2026-09-18
- **URL**: https://genefish.wordpress.com/2026/09/18/checking-oyster-mortality-in-el-nino-experiment/
- **Key finding**: Mortality was tallied across 12 oyster bags (6 simulated El Niño/elevated-temperature, 6 control) at 10am, with El Niño bags re-checked at 1pm due to rapidly rising deaths. El Niño bags showed sharply escalating mortality (several exceeding 50% dead within about 3 hours) while control bags remained largely unaffected (roughly 2-12% mortality), indicating a fast-onset, severe thermal stress response.

---

### Daily Literature Connections — 2026-09-18
- **Author**: Cas Daniel
- **Date**: 2026-09-18
- **URL**: https://genefish.wordpress.com/2026/09/18/daily-literature-connections-2026-09-18/
- **Key finding**: Automated literature-linking post connecting three notebook findings (PCSGA OAE results, and the 09.16/09.17 qPCR posts) to recent publications. Relevant papers indicated NaOH-based OAE is comparatively mild on oyster microbiomes, heat stress reorganizes multiple energy- and oxidative-stress gene pathways in Pacific oysters, and heat-responsive metabolic gene regulation varies genetically between oyster subspecies — offering plausible explanations for the lab's inconsistent ATP synthase results across experiments.

---

### Daily Literature Connections — 2026-09-19
- **Author**: Cas Daniel
- **Date**: 2026-09-19
- **URL**: https://genefish.wordpress.com/2026/09/19/daily-literature-connections-2026-09-19/
- **Key finding**: Automated literature-linking post tied to the "Today I re-ran a qPCR" post, connecting its heat-priming/dampened stress-gene-response finding to studies on a haemocyte oxidative-damage regulator, shell-corrosion-based thermal resistance in oysters, and a preprint on parental immune priming. Together the cited literature suggests Pacific oysters have multiple, non-exclusive heat-tolerance mechanisms and that priming effects are temperature-limited, consistent with the lab's own dampened-but-not-eliminated stress response.

---

### Today I re-ran a qPCR…
- **Author**: HazelAbrahamsonA
- **Date**: 2026-09-18
- **URL**: https://genefish.wordpress.com/2026/09/18/today-i-re-ran-a-qpcr/
- **Key finding**: Re-ran the ATP synthase qPCR after detecting no-template-control amplification in the prior run, obtaining cleaner data with slightly reduced variation but the same overall pattern. Neither heat exposure significantly altered ATP synthase or citrate synthase transcript levels (HSP70 was the only gene significantly affected), but all four genes showed a shared visual trend of a less dramatic decrease during a second heat exposure in previously heat-primed (H/H) oysters, supporting a priming-effect hypothesis.

---

### Daily Literature Connections — 2026-09-20
- **Author**: Cas Daniel
- **Date**: 2026-09-20
- **URL**: https://genefish.wordpress.com/2026/09/20/daily-literature-connections-2026-09-20/
- **Key finding**: Automated literature-linking post tied to the El Niño mortality-count post, citing a study on shell-corroding symbionts that enhance thermal tolerance in Pacific oysters and a preprint showing non-linear, threshold-dependent mortality above 40°C in heat-exposed oyster offspring. Both are proposed as plausible explanations for the sharp bag-to-bag divergence and rapid escalation in mortality observed during the El Niño exposure experiment.

No warnings were reported by the fetch script.

---

## Cross-Notebook Patterns & Connections

_This section analyzes the compiled per-source summaries for shared themes, follow-up narratives, apparent contradictions, and multi-week historical connections across the lab's notebooks. Connections are surfaced only when a specific named entity ties the sources together — never from vague thematic similarity._

### Temporal Narratives
- **El Nino bucket mortality escalation** — Grace Crandall's Sept 16 log on the El Nino-simulated bucket documented a bad smell after a freshwater addition and a mortality check finding 12–28 dead per bag across 5 bags, prompting a full water change; two days later, robertsblr's Sept 18 WordPress post ("Checking Oyster Mortality in El Niño Experiment") found the same named El Nino/control bucket experiment escalating sharply — several El Nino bags exceeded 50% mortality within about 3 hours, while paired ambient controls stayed at 2–12%. Grace's early water-quality problem plausibly set the stage for the more severe mortality event checked two days later.

### Historical Connections
- **El Nino heat-wave protocol** — this week's rapid, severe mortality in the El Nino buckets plays out a design Ariana Huffmyer laid out weeks earlier: her post specified that simulated heat waves would run longer (9 days) under El Nino than under control conditions, a design choice that plausibly explains why El Nino bags are now failing sharply while controls hold steady. See [El Nino experimental conditions planning] · 2026-08-03 (Ariana Huffmyer, Ariana Huffmyer Lab Notebook): https://ahuffmyer.github.io/posts/2026-08-05-el-nino-conditions-design.html
- **Resazurin-ploidy field-performance correlation** — Tumbling Oysters' large-scale index catalogue this week found essentially no resazurin index reliably predicts field survival or growth in ploidy-trial oysters (284 indices tested, none surviving multiplicity correction), which appears to conflict with Ariana Huffmyer's earlier finding of resazurin-ploidy performance correlations in VIMS diploid/triploid oysters. ⚠️ Needs human verification — resolving this requires checking whether the two analyses used the same oyster cohort/family and the same definition of "correlation" (Ariana's preliminary correlation vs. Tumbling Oysters' multiplicity-corrected significance test). See [VIMS Diploid/Triploid performance-resazurin correlations] · 2026-09-10 (Ariana Huffmyer, Ariana Huffmyer Lab Notebook): https://ahuffmyer.github.io/posts/2026-09-10-vims-diploid-triploid-resazurin-performance-correlations.html
- **OAE preconditioning + resazurin heat-stress protocol** — acasey2's PCSGA presentation this week synthesizes lab-based OAE exposure results showing reduced metabolic rate; the same OAE-preconditioning-then-heat-stress design (resazurin assay after 36°C challenge) was run independently in Sam's Notebook weeks earlier. See [Resazurin Assays - USDA M.gigas Juveniles OAE Preconditioning Effect on 36C Heat Stress Response] · 2026-08-31 (Sam White, Sam's Notebook): https://robertslab.github.io/sams-notebook/posts/2026/2026-08-31-Resazurin-Assays---USDA-M.gigas-Juveniles-OAE-Preconditioning-Effect-on-36C-Heat-Stress-Response/

---

## Data & Figures

_This section consolidates, grouped by source, the figure links and external data/repository links already surfaced in the per-source summaries above. It is a single entry point into the underlying data and figures for this window, not a new analysis._

### Tumbling Oysters (Steven Roberts)
- Population structure in Olympia oyster low-coverage WGS...: `images/structure-fst-panel.png`
- No Genotype-Environment Association in Olympia Oyster lcWGS: `images/rda-summary.png`
- No Genotype-Environment Association in Olympia Oyster lcWGS: `images/rda-genomewide.png`
- Does a 4-hour resazurin trace forecast field performance? Mostly no: `images/survival_permutation_ceiling.png`
- Does a 4-hour resazurin trace forecast field performance? Mostly no: `images/association_heatmap_top_indices.png`
- Does a 4-hour resazurin trace forecast field performance? Mostly no: `images/best_index_scatter.png`
- Does a 4-hour resazurin trace forecast field performance? Mostly no: `images/nested_composite_cv.png`
- Does a 4-hour resazurin trace forecast field performance? Mostly no: `images/assay_duration.png`
- Does a 4-hour resazurin trace forecast field performance? Mostly no: `images/screening_utility.png`

### Sam's Notebook (Sam White)
- Samples Received - Freezer Boxes from Katherine Silliman for Storage: `./freezer-boxes-01.jpg`
- Samples Received - Freezer Boxes from Katherine Silliman for Storage: `./freezer-boxes-02.jpg`

### Grace Crandall's Notebook
- Oyster El Nino Bucket Temp, Sal Checks and Feeding Log: `../notebook-images/2026-oyster-bucket/IMG_8184.JPG`
- Oyster Family Mortality Tracking and Rack Set Up: `../notebook-images/2026-oyster-mort-check/lab-setup.JPG`

### Kathleen Durkin Lab Notebook
- Lit review: how to statistically test for inheritance: `./images/Shafi_Fig.png`
- Lit review: how to statistically test for inheritance: `./images/Shafi_Table.png`
- Details of DSS functionality: `./images/DSS_models.png`
- Implementing MACAU: `./images/relatedness-diagnostics-1.png`

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv/Europe PMC searches for each notable finding. Only findings with at least one relevant retrieved paper are shown. A fourth candidate finding (Olympia oyster lcWGS population structure / Willapa Bay mislabeling) was searched but returned no relevant literature on PubMed or Europe PMC, and is omitted per the no-hallucination rule.

### El Nino-simulated heat-wave mortality in oyster buckets

**Source:** Grace Crandall's Notebook; Genefish WordPress (robertsblr)
**Finding:** Simulated El Nino heat-wave conditions (~26°C, elevated salinity) produced rapid, severe mortality in oyster buckets — several bags exceeded 50% mortality within about 3 hours of a mortality check — while paired ambient-temperature control bags remained largely unaffected (roughly 2-12% mortality).

### Supports [PubMed]: Short-term heat stress adaptation in intertidal oysters (Crassostrea sikamea): Integrative biochemical, transcriptomic and metabolomic insights
Liu et al., 2026 · PMID: 41401620 · https://pubmed.ncbi.nlm.nih.gov/41401620/

This study exposed Kumamoto oysters to a range of sublethal-to-lethal temperatures and tracked survival from 0.5 hours up to the onset of shell-gaping (3–4 hours). Mortality was minimal below 45°C, but survival collapsed to 14% after just 1 hour at 45°C, with anything hotter proving completely lethal — demonstrating that oyster heat mortality can flip from negligible to near-total within a matter of hours once a threshold is crossed. This mirrors the lab's own rapid mortality spike in El Nino buckets within about 3 hours, though the lab's temperatures (~26°C) are far below this study's lethal range, suggesting the bucket mortality event may involve additional stressors (e.g., water quality) beyond heat alone.

---

### Adds context [PubMed]: Microbial endolithic symbiosis in oysters enhances thermal resistance through shell corrosion
Zardi et al., 2026 · PMID: 42430847 · https://pubmed.ncbi.nlm.nih.gov/42430847/

Pacific oysters with symbiont-driven shell corrosion survive heat exposure significantly better than uncorroded oysters, with a thermal buffer as large as 9.5°C in the field. This offers a possible explanation for bag-to-bag variability in mortality outcomes within the same nominal treatment, since individual oysters' symbiont load and shell condition could differ even under identical simulated El Nino conditions.

---

### Adds context [PubMed]: Integrated metabolomics and flow cytometry assessment reveals immune-metabolic modulation of Crassostrea (=Magallana) gigas hemolymph under hypoxic and elevated temperature conditions
Kim et al., 2026 · PMID: 42134734 · https://pubmed.ncbi.nlm.nih.gov/42134734/

Pacific oysters exposed to combined hypoxia and elevated temperature (28°C) showed suppressed anaerobic metabolism and significantly increased hemocyte mortality, linked to impaired immune function and summer mortality. This supports a mechanism by which elevated temperature — especially combined with the poor water quality noted in the lab's own bucket log — could drive the rapid, severe mortality seen in the El Nino bags.

---

### Adds context [EcoEvoRxiv preprint — not peer-reviewed]: Intertidal Exposure Modulates Time-Integrated Heat Tolerance of the Eastern Oyster Crassostrea virginica
Villeneuve et al., 2026 · DOI: 10.32942/x2cw9d · https://doi.org/10.32942/x2cw9d

Using thermal death time curves and a dynamic survival model, this preprint shows that oyster survival under heat exposure depends heavily on exposure type (immersed vs. emersed) and that even modest (2°C) warming can trigger disproportionate survival drops. This supports the plausibility of a sharp, threshold-like mortality response to the lab's simulated El Nino warming.

---

### Adds context [bioRxiv preprint — not peer-reviewed]: Parental immune priming reshapes offspring growth, metabolism, and thermal tolerance in the Pacific Oyster
Baird et al., 2025 · DOI: 10.64898/2025.12.10.693539 · https://doi.org/10.64898/2025.12.10.693539

This preprint found that Pacific oyster offspring's heat tolerance is threshold-dependent and can flip direction with only a 2°C increase (lower mortality at 40°C but higher mortality at 42°C than controls). This supports the idea that oyster heat-mortality responses are highly nonlinear and threshold-sensitive, consistent with the lab's observation of a rapid escalation from low to high mortality in the El Nino bags over just a few hours.

**Literature summary:** Three peer-reviewed papers and two preprints together support the plausibility of the lab's rapid, threshold-like mortality response in simulated El Nino buckets. One peer-reviewed study (Liu et al.) directly demonstrates that oyster heat mortality can flip from negligible to near-total within hours once a critical temperature is crossed, while two further peer-reviewed papers (Zardi et al.; Kim et al.) point to symbiont-mediated variability and hypoxia-heat interactions as plausible sources of the sharp bag-to-bag differences observed. Two preprints (Villeneuve et al.; Baird et al.), not yet peer-reviewed, add supporting context on exposure-type sensitivity and threshold-dependent, nonlinear mortality responses to small temperature increases.

---

### Resazurin metabolic assay as a predictor of field performance in ploidy-trial oysters

**Source:** Tumbling Oysters (Steven Roberts)
**Finding:** A catalogue of 284 distinct indices derived from individual-level 4-hour, 40°C resazurin metabolic assays on ~160 diploid/triploid ploidy-trial oysters showed zero indices significantly associated with field survival, growth, condition index, or yield after permutation-based multiplicity correction, suggesting the assay is not yet usable as an individual-level field-performance screen.

### Conflicts [PubMed]: From blue to pink: resazurin as a high-throughput proxy for metabolic rate in oysters
Huffmyer et al., 2026 · PMID: 42495017 · https://pubmed.ncbi.nlm.nih.gov/42495017/ (originally posted as bioRxiv preprint: https://doi.org/10.1101/2025.11.06.686367)

This foundational validation study (co-authored by several of the same lab's researchers) established resazurin fluorescence as a reliable whole-organism metabolic proxy in Crassostrea gigas and C. virginica, finding that individuals with greater metabolic depression under acute thermal stress were more likely to survive, and that metabolic rates of 50 selectively bred C. virginica families correlated significantly with predicted family-level performance. This is very likely the "earlier family-level USDA result" the current finding explicitly says its individual-level result runs opposite to — the two studies together suggest resazurin may predict field performance at the family/genetic level even though it failed to do so at the individual level in the current single-family catalogue.

**Literature summary:** One peer-reviewed paper — from the same research group's own earlier validation work — directly conflicts with (or at least complicates) the current finding: it found resazurin-based metabolic rate predicted field performance at the family level across 50 selectively bred families, while the current study found no predictive individual-level signal within a single family. This is consistent with the current post's own explanation that a single-family design has little heritable variation to resolve, suggesting the assay's predictive power may operate mainly at the family/genetic level rather than the individual level.

---

### Ocean alkalinity enhancement (OAE) effects on oyster growth and metabolic rate

**Source:** Genefish WordPress (acasey2, PCSGA conference results)
**Finding:** In situ ocean alkalinity enhancement (NaOH) increased growth in Pacific oysters but had no effect or worsened growth in Olympia oysters, while lab-based OAE exposures reduced metabolic rate across all life stages tested.

### Adds context [PubMed]: Olivine and dissolved alkalinity trigger different bacterial community shifts in water and oyster gills: insights from a mesocosm experiment
Antoni et al., 2025 · PMID: 41852431 · https://pubmed.ncbi.nlm.nih.gov/41852431/

Comparing olivine-based versus dissolved NaOH-based ocean alkalinity enhancement on European flat oysters (Ostrea edulis), this study found that NaOH-based OAE produced only minimal changes to gill and water bacterial communities compared to untreated controls, whereas olivine-based OAE caused larger microbial shifts and favored potentially pathogenic Vibrios. This supports the lab's apparent choice of NaOH over mineral-based alkalinization as the comparatively lower-risk OAE method, though it does not directly address the growth or metabolic-rate effects the lab observed.

---

### Adds context [bioRxiv preprint — not peer-reviewed]: The effects of elevated seawater pH and total alkalinity following dosing of sodium hydroxide in Calanus finmarchicus
Murray et al., 2026 · DOI: 10.64898/2026.02.03.700700 · https://doi.org/10.64898/2026.02.03.700700

Testing short-term NaOH-driven pH/alkalinity spikes on a copepod species, this preprint found no effect on routine metabolic rate immediately after a 10-minute high-pH exposure, though escape-response behavior was impaired. This offers a point of comparison from a different taxon: unlike the lab's oysters, this copepod's metabolic rate was not measurably affected by short-term NaOH-based OAE exposure, suggesting the metabolic-rate-reducing effect the lab observed in oysters may be species- or exposure-duration-specific rather than a universal NaOH-OAE effect.

**Literature summary:** One peer-reviewed paper supports the lab's implicit framing of NaOH as a comparatively benign OAE method (at least for microbiome impacts), while one preprint — not yet peer-reviewed — adds context suggesting that OAE's effect on metabolic rate may not generalize across taxa, since a copepod species showed no short-term metabolic-rate change under similar NaOH dosing.

---

> Coverage limited to papers indexed on PubMed and preprints discoverable via Europe PMC (which indexes bioRxiv, Authorea Preprints, Research Square, medRxiv, EcoEvoRxiv, and other preprint servers), restricted to the last 12 months. **Preprints have not been peer-reviewed** and should be interpreted with appropriate caution. Preprints that have since been published in a peer-reviewed journal are reported in their published form where detected.

---

> Generated by the `full-lab-digest` skill · 2026-09-14 to 2026-09-21 (7-day window)
