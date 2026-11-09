# Full Lab Digest — 2026-11-03 to 2026-11-09 (7 days)

> 5 of 7 sources had activity in the last 7 days. 2 had none.

---

## Tumbling Oysters (Steven Roberts)

_No new posts in the last 7 days._

---

## Ariana Huffmyer Lab Notebook

## Ariana Huffmyer Notebook Digest — Week of 2026-11-02 to 2026-11-09

> Summarized from [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io)

### October Goals and Daily Entries
- **Author**: Ariana Huffmyer
- **Date**: 2026-10-28
- **URL**: https://ahuffmyer.github.io/posts/2026-10-01-goals.html
- **Categories**: goals, daily-entries
- **Key finding**: This is the monthly goals/daily-log post for October, updated this week with the final two daily entries (Oct 29–30), covering continued NSF IOS grant application work, PolyIC manuscript qPCR analysis and revisions, and an Oyster CAP R&D meeting. No figures or formal results — logistical tracking of ongoing tasks.
- **Figures**: none

---

### November 2026 Goals and Daily Entries
- **Author**: Ariana Huffmyer
- **Date**: 2026-11-01
- **URL**: https://ahuffmyer.github.io/posts/2026-11-01-goals.html
- **Categories**: goals, daily-entries
- **Key finding**: New monthly goals post laying out priorities for November: revising/advancing several manuscripts (PolyIC, Hawaii 2023, Moorea 2023, Westcott oyster priming, Manchester oyster, oyster review hardening data), continuing the NSF IOS grant with H. Putnam, Moorea 2023 RNAseq/metabolomics analysis, oyster image analysis, developing an Oyster CAP resazurin protocol, and preparing an MCR AIM talk plus planning a 2028 SICB symposium. Daily log entries for Nov 2–3 note continued NSF grant work and oyster growth data processing.
- **Figures**: none

---

### Manchester Hardening project growth and survival analysis
- **Author**: Ariana Huffmyer
- **Date**: 2026-11-03
- **URL**: https://ahuffmyer.github.io/posts/2026-11-03-manchester-hardening-experiment-growth-survival-analysis.html
- **Categories**: manchester-hardening, experimental design
- **AI-use disclosure**: Level 0 (L0 — None)
- **Key finding**: Analyzed survival and growth data across four time points (May 2025–Aug 2026) for 10 oyster families under Control vs. High hardening treatment. Mixed models showed a significant effect of family on survival but no overall treatment effect, with family-level survival differences emerging modestly after one year and more strongly by the end of the second summer; growth analysis likewise found a significant day x family x treatment interaction with no main effect of treatment alone. Comparing these results to prior acute thermal-stress tests showed hardening effects are highly family-specific — some families gained thermal tolerance and grew more after hardening, while others showed the opposite pattern or no size effect at all.
- **Figures**:
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261103/family_mortality.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261103/family_only_mortality.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261103/treatment_mortality.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261103/family_treatment_size_box.png
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261103/family_treatment_size_box_transformed.png?raw=true

---

## Sam's Notebook (Sam White)

## Sam White Notebook Digest — Week of 2026-11-02 to 2026-11-09

> Summarized from [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook)

### Temperature Monitoring - ESP32 Tank Temperature Hub and Gannet Receiver
- **Date**: 2026-11-04
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-11-04-Temperature-Monitoring---ESP32-Tank-Temperature-Hub-and-Gannet-Receiver/
- **Author**: Sam White
- **Categories**: (none, beyond the bare year)
- **Key finding**: Sam is building a continuous temperature-logging system for the SHORE tank room: ESP32 "hub" microcontrollers each read five DS18B20 probes and POST readings over HTTPS to a Python receiver running in a Docker container on the Gannet Synology server (chosen over PHP due to a security issue, and over a server-side "fetch" design because UW's device Wi-Fi lacks fixed IPs/DHCP reservations). On the bench, one hub with three probes read plausible temperatures (17–19 degrees C) and the receiver on Gannet passed all local tests (valid uploads, backlog, bad tokens, malformed JSON, etc.) and responded correctly both over VPN and from off-campus. The full hub-to-Gannet upload path and operation on UW's actual device Wi-Fi have not yet been tested; next steps are running the firmware end-to-end, registering both hubs on UW Wi-Fi, wiring/calibrating the second hub, building the tank-mapping/calibration processing step, and adding monitoring alerts.
- **Figures**: No figures embedded in this post (it includes a mermaid flowchart diagram and a JSON data sample, but no image links).

No other posts were changed in RobertsLab/sams-notebook in the last 7 days (commits_scanned: 2).

---

## Grace Crandall's Notebook

# Grace Crandall Notebook Digest — Week of 2026-11-02 to 2026-11-09

> Summarized from [grace-ac/grace-ac.github.io](https://github.com/grace-ac/grace-ac.github.io)

### November Goals
- **Date**: 2026-11-01
- **URL**: https://grace-ac.github.io/nov-goals/
- **Categories**: MonthlyGoals
- **Key finding**: Logistical/planning post listing November priorities: wrapping up Day 12 DEG-to-enrichment results for the multi-species (Chapter 2) analysis and adding them to the paper draft, running remaining DNA extraction/qPCR plates for FHL mussel samples (pending a functional bullet blender), and finishing the PhD proposal to send to committee members and schedule the general exam. Also notes a busy stretch from coordinating the Graduate Student Symposium (Nov 6), weekly TA duties (lab sections, grading, office hours), and TA-ing two weekend low-tide surveys.
- **Figures**: none
- **⚠ Date mismatch**: Front-matter date 2026-11-01 differs from commit date 2026-11-03

---

### Multispeces - All 3 Species UPDATED Day 12 DEG --> Enrichment Results
- **Date**: 2026-11-03
- **URL**: https://grace-ac.github.io/muspdat12-updates/
- **Categories**: MultiSpecies
- **Key finding**: Re-ran DESeq2 for all three sea star species (P. helianthoides, P. ochraceus, D. imbricata) at Day 12 (SSWD-exposed vs. control), this time excluding low-count genes and re-plotting enrichment results using Benjamini-Hochberg-corrected p-values instead of Fisher p-values. Filtering modestly reduced DEG counts for P. helianthoides and P. ochraceus but barely changed D. imbricata, and it substantially shifted which GO terms came out significant (e.g., P. ochraceus moved from a single epithelial-morphogenesis term to sensory-perception/flagellated-sperm-motility terms). Grace decided to move forward with the filtered-gene DEG lists and their downstream enrichment as the results to use going forward in the paper.
- **Figures**:
  - local: ../notebook-images/2026-11-03/pycD12_enrichment_parent_terms-BH.png
  - local: ../notebook-images/2026-11-03/pisaD12_enrichment_parent_terms-BH.png
  - local: ../notebook-images/2026-11-03/derD12_enrichment_parent_terms-BH.png
  - local: ../notebook-images/2026-11-03/pycD12_enrichment_terms-BH.png
  - local: ../notebook-images/2026-11-03/pisaD12_enrichment_terms-BH.png
  - local: ../notebook-images/2026-11-03/derD12_enrichment_terms-BH.png

---

## Megan Ewing Lab Notebook

_No new posts in the last 7 days._

---

## Kathleen Durkin Lab Notebook

All three changed posts this week belong to the same project (ceasmallr — the parental-exposure/offspring methylation study), so there is only one project section plus no daily-log activity.

# Kathleen Durkin Notebook Digest — Week of 2026-11-02 to 2026-11-09

> Summarized from [shedurkin/Roberts-LabNotebook](https://github.com/shedurkin/Roberts-LabNotebook)

## ceasmallr

### Rerunning DSS with C/T SNPs masked
- **Project**: ceasmallr
- **Date**: 2026-11-04
- **URL**: https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_11_04_CTmask.html
- **Author**: Kathleen Durkin
- **Categories**: ceasmallr
- **Key finding**: To avoid false-positive unmethylated calls from C→T SNP variants, Kathleen called SNPs with BS-Snper on both offspring and (newly) parent data, then reran the DSS differential-methylation pipeline on both datasets with C/T SNPs masked from the input coverage files. Comparing masked vs. unmasked outputs showed only a modest, expected reduction in input loci, DMLs, and DMRs overall, but masking actually *increased* detected DMLs/DMRs in the egg samples specifically — consistent with masking removing some SNP-artifact signals while also unmasking true signal previously obscured by nearby SNPs.
- **Figures**: None found (the post's only `<img>` tags are AI-use disclosure badges, not data figures).

---

### Generating ceasmallr figures for GSS
- **Project**: ceasmallr
- **Date**: 2026-11-04
- **URL**: https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_11_04_GSS_figures.html
- **Author**: Kathleen Durkin
- **Categories**: ceasmallr
- **Key finding**: In preparation for a Graduate Student Symposium talk, Kathleen built presentation figures classifying offspring (zygote/larvae) DMLs and DMRs by whether the same differentially methylated loci/regions also appear in exposed-parent egg and/or sperm gamete data. The resulting stacked bar charts (full and zoomed-in versions excluding "offspring only" loci) summarize how much offspring differential methylation overlaps with parental gamete methylation changes, by stage and by parent-of-origin.
- **Figures**:
  - local: ./images/2026_11_04_GSS_offspring_parent_overlap.png
  - local: ./images/2026_11_04_GSS_offspring_parent_overlap_zoom.png

---

No warnings were reported by the fetch script (`commits_scanned`: 3).

_1 post from this window was already covered in a previous digest and is omitted here._

---

## Genefish WordPress

### Tank room and water chemistry trial
- **Author**: Jesse Lowe
- **Date**: 2026-11-02
- **URL**: https://genefish.wordpress.com/2026/11/02/tank-room-and-water-chemistry-trial-5/
- **Key finding**: Routine water-quality checks showed the lab's three main oyster holding tanks remained within normal parameters (salinity, pH, nitrate), while the dedicated water-chemistry trial tank continued to show elevated ammonia and nitrite along with low alkalinity. Full water changes were prepared and performed on tanks currently in use to maintain conditions.

---

### 11/2/26 Resazurin assay data
- **Author**: giselff250455090
- **Date**: 2026-11-02
- **URL**: https://genefish.wordpress.com/2026/11/02/11-2-26-resazurin-assay-data/
- **Key finding**: A GitHub repository was created to organize resazurin assay data, coding scripts, and a shell-length spreadsheet for the oyster priming experiment. Next steps planned are finishing the analysis code with a labmate's help to generate graphs, plus a visual summary of the heat stress experiment data.

---

### Daily Literature Connections — 2026-11-03
- **Author**: Cas Daniel
- **Date**: 2026-11-03
- **URL**: https://genefish.wordpress.com/2026/11/03/daily-literature-connections-2026-11-03/
- **Key finding**: An automated post linked Jesse Lowe's 2026-11-02 tank chemistry observations to a 2026 Crassostrea gigas study showing that elevated ammonia upregulates the CgAMT1 transporter and drives haemocyte (immune cell) death under bacterial challenge. This supports the interpretation that the trial tank's persistently high ammonia is a genuine physiological stressor, though the cited paper tested infection-driven rather than external ammonia exposure directly.

---

### 11/3/26 Coding with the resazurin assay data
- **Author**: giselff250455090
- **Date**: 2026-11-03
- **URL**: https://genefish.wordpress.com/2026/11/03/11-3-26-coding-with-the-resazurin-assay-data/
- **Key finding**: Worked with a labmate to debug R errors and finish compiling resazurin assay data spreadsheets. Plotting was not completed this session and was deferred to the next work day.

---

### Aquilonastra Sp. Star Project Setup Part 1
- **Author**: Samuel Slutz
- **Date**: 2026-11-03
- **URL**: https://genefish.wordpress.com/2026/11/03/aquilonastra-sp-star-project-setup-part-1/
- **Key finding**: A new project was launched to assess how heat priming alters metabolic stress responses to subsequent thermal stress, using small tropical Aquilonastra sp. starfish as a tractable model (chosen for abundance, hardiness, and small size) since heat-priming research in Asterozoa is underdeveloped relative to Pacific coast sea stars. The holding tank was set at 22°C (with consideration of raising to 23°C), and plans were made to feed the animals nori and acclimate them via a drip line upon arrival the following week.

---

### 11.05: RNA extraction test
- **Author**: HazelAbrahamsonA
- **Date**: 2026-11-05
- **URL**: https://genefish.wordpress.com/2026/11/05/11-05-rna-extraction-test/
- **Key finding**: RNA was extracted from a small subset of samples from a repeat 35°C heat-stress experiment to test whether a protocol adjustment would resolve previously low yields. The test samples showed much higher RNA yields than before, so extraction was planned to proceed to the remaining samples the next day.

---

### 11.06: Continued RNA extraction
- **Author**: HazelAbrahamsonA
- **Date**: 2026-11-06
- **URL**: https://genefish.wordpress.com/2026/11/06/11-06-continued-rna-extraction/
- **Key finding**: RNA extraction continued on additional samples from the 24-hour, 35°C repeat stress experiment. Qubit fluorometer calibration issues prevented same-day quantification, so RNA yield measurement was deferred to the following day.

---

### Aquilonastra Stars Tank Setup and Early Stage Rearing Plans (11/6/2026)
- **Author**: Samuel Slutz
- **Date**: 2026-11-06
- **URL**: https://genefish.wordpress.com/2026/11/06/aquilonastra-stars-tank-setup-and-early-stage-rearing-plans-11-6-2026/
- **Key finding**: An experimental tank was cleaned, connected to the manifold system, and fitted with a heater set to 23°C in preparation for receiving at least 24 Aquilonastra stars. A rearing schedule was decided: drip-acclimate the animals for about an hour on arrival, feed them nori, and check on them at least daily for the first week before reassessing the monitoring frequency.

---

### Daily Literature Connections — 2026-11-07
- **Author**: Cas Daniel
- **Date**: 2026-11-07
- **URL**: https://genefish.wordpress.com/2026/11/07/daily-literature-connections-2026-11-07/
- **Key finding**: An automated post connected Hazel Abrahamson's 2026-11-05 RNA extraction yield improvement to two recent papers showing that extraction kit/protocol choice is a major, reproducible driver of nucleic-acid yield variability in oyster and other bivalve tissue. While neither cited paper tests heat-stress conditions directly, both support the plausibility that a technique adjustment, rather than biological variability, explains the yield jump observed in the lab.

---

### 11/07 Data analysis
- **Author**: Christina Zhang
- **Date**: 2026-11-07
- **URL**: https://genefish.wordpress.com/2026/11/07/11-07-data-analysis/
- **Key finding**: Completed analysis of all baywater oyster size data that had been provided, a one-hour task with no further details reported.

---

### 11.07: RNA quantification
- **Author**: HazelAbrahamsonA
- **Date**: 2026-11-07
- **URL**: https://genefish.wordpress.com/2026/11/07/11-07-rna-quantification/
- **Key finding**: Quantified RNA extracted earlier in the week using a Qubit fluorometer. The prior calibration problem (low sample fluorescence) was successfully resolved, allowing quantification to proceed.

---

### Coding for the resazurin assay
- **Author**: giselff250455090
- **Date**: 2026-11-09
- **URL**: https://genefish.wordpress.com/2026/11/09/coding-for-the-resazurin-assay/
- **Key finding**: Compiled day-2 resazurin assay data (shell length, treatment group, time) for 30 oysters primed with hydrogen peroxide and analyzed it in RStudio to produce graphs and box plots. Preliminary statistics showed no significant difference in metabolic response between the control group and the low- or high-H2O2 priming groups.

---

### Aquilonastra Stars
- **Author**: Samuel Slutz
- **Date**: 2026-11-09
- **URL**: https://genefish.wordpress.com/2026/11/09/aquilonastra-stars/
- **Key finding**: Approximately 39 Aquilonastra stars were received and transported carefully to maintain warmth, then drip-acclimated into a heated holding tank supplied with nori. The animals showed high size variability (roughly 5 mm to just over 1 cm), and several individuals appeared flipped over and not self-righting, possibly due to cold shock during transit; their condition will be monitored going forward.

No warnings were reported by the fetch script.

---

## Cross-Notebook Patterns & Connections

_This section analyzes the compiled per-source summaries for shared themes, follow-up narratives, apparent contradictions, and multi-week historical connections across the lab's notebooks. Connections are surfaced only when a specific named entity ties the sources together — never from vague thematic similarity._

### Shared Themes
- **Pacific coast sea stars (Pisaster ochraceus, Pycnopodia helianthoides, Dermasterias imbricata)** — Samuel Slutz's new Aquilonastra sp. heat-priming project (Genefish WordPress) explicitly frames itself as filling a gap in starfish heat-priming research "relative to Pacific coast sea stars" — the exact species group Grace Crandall is currently re-analyzing in her updated Day-12 DEG/enrichment results for sea star wasting disease (SSWD).

### Temporal Narratives
- **Tank room temperature/water-chemistry monitoring** — Sam White's new ESP32-based continuous temperature-logging system, built this week for the SHORE tank room, targets the same kind of manual daily "tank room and water chemistry" checks Jesse Lowe has been recording on Genefish WordPress for months (e.g., this week's "Tank room and water chemistry trial" post); the new infrastructure appears designed to eventually automate the recurring manual monitoring.

### Historical Connections
- **Tank room water-chemistry monitoring** — Sam White's new ESP32 temperature-logging system follows months of manual daily tank-room/water-chemistry checks in the same physical space. See "Tank room and water chemistry trial" · 2026-10-29 (Jesse Lowe, Genefish WordPress): https://genefish.wordpress.com/2026/10/29/tank-room-and-water-chemistry-trial-4/
- **Starfish heat-tolerance priming** — Samuel Slutz's Aquilonastra heat-priming project this week directly follows up on a project idea he floated two weeks earlier. See "To Do (10/24/26-11/07/26)" · 2026-10-24 (Samuel Slutz, Genefish WordPress): https://genefish.wordpress.com/2026/10/24/to-do-10-24-26-11-07-26/
- **Pisaster ochraceus / Pycnopodia helianthoides / Dermasterias imbricata (SSWD species)** — Grace's current Day-12 DEG/enrichment re-analysis of these three species builds on earlier lab genomics work establishing the same species' differential SSWD susceptibility. See "The Pathogen Has a Plan, the Hosts Do Not" · 2026-09-11 (Steven Roberts, Tumbling Oysters): https://sr320.github.io/tumbling-oysters/posts/87-seastar-susceptibility-genomics/
- **Manchester Hardening survival testing** — This week's four-time-point family x treatment survival/growth analysis consolidates data first reported as standalone lab survival test results two months earlier. See "Manchester Hardening project lab survival testing results" · 2026-09-08 (Ariana Huffmyer): https://ahuffmyer.github.io/posts/2026-09-08-manchester-hardening-project-survival-test-results.html
- **BS-Snper SNP calling (ceasmallr)** — This week's C/T-SNP-masked DSS rerun reuses the BS-Snper SNP-calling method Kathleen first set up for MACAU modeling. See "Calling SNPs with BS-Snper" · 2026-09-22 (Kathleen Durkin): https://shedurkin.github.io/Roberts-LabNotebook/posts/projects/ceasmallr/2026_09_22_BS-Snper.html
- **Multispecies Day-12 DEG → enrichment results (P. helianthoides, P. ochraceus, D. imbricata)** — This week's "UPDATED" enrichment post is a direct re-analysis of the original per-species Day-12 DEG/enrichment write-ups posted one to two days earlier. See "Multispeces - Pycno Day 12 DEG --> enrichment Results" · 2026-11-01, "Multispeces - Pisaster Day 12 DEG --> enrichment Results" · 2026-11-02, and "Multispeces - Dermasterias Day 12 DEG --> enrichment Results" · 2026-11-02 (Grace Crandall): https://grace-ac.github.io/musp-pycno-day12/, https://grace-ac.github.io/pisaster-d12/, https://grace-ac.github.io/derm-d12/
- **Oyster H2O2 (hydrogen peroxide) priming experiment** — This week's resazurin data compilation (no significant metabolic difference between control and priming groups) analyzes the same experiment giselff250455090 set up roughly a month earlier. See "Oysters H2O2 priming experiment set-up" · 2026-10-08 (giselff250455090, Genefish WordPress): https://genefish.wordpress.com/2026/10/08/oysters-h2o2-priming-experiment-set-up/

---

## Data & Figures

_This section consolidates, grouped by source, the figure links and external data/repository links already surfaced in the per-source summaries above. It is a single entry point into the underlying data and figures for this window, not a new analysis._

### Ariana Huffmyer Lab Notebook
- Manchester Hardening project growth and survival analysis: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261103/family_mortality.png?raw=true
- Manchester Hardening project growth and survival analysis: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261103/family_only_mortality.png?raw=true
- Manchester Hardening project growth and survival analysis: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261103/treatment_mortality.png?raw=true
- Manchester Hardening project growth and survival analysis: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261103/family_treatment_size_box.png
- Manchester Hardening project growth and survival analysis: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20261103/family_treatment_size_box_transformed.png?raw=true

### Grace Crandall's Notebook
- Multispeces - All 3 Species UPDATED Day 12 DEG --> Enrichment Results: ../notebook-images/2026-11-03/pycD12_enrichment_parent_terms-BH.png
- Multispeces - All 3 Species UPDATED Day 12 DEG --> Enrichment Results: ../notebook-images/2026-11-03/pisaD12_enrichment_parent_terms-BH.png
- Multispeces - All 3 Species UPDATED Day 12 DEG --> Enrichment Results: ../notebook-images/2026-11-03/derD12_enrichment_parent_terms-BH.png
- Multispeces - All 3 Species UPDATED Day 12 DEG --> Enrichment Results: ../notebook-images/2026-11-03/pycD12_enrichment_terms-BH.png
- Multispeces - All 3 Species UPDATED Day 12 DEG --> Enrichment Results: ../notebook-images/2026-11-03/pisaD12_enrichment_terms-BH.png
- Multispeces - All 3 Species UPDATED Day 12 DEG --> Enrichment Results: ../notebook-images/2026-11-03/derD12_enrichment_terms-BH.png

### Kathleen Durkin Lab Notebook
- Generating ceasmallr figures for GSS: ./images/2026_11_04_GSS_offspring_parent_overlap.png
- Generating ceasmallr figures for GSS: ./images/2026_11_04_GSS_offspring_parent_overlap_zoom.png

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

### Sea star heat-priming research gap (Pacific coast sea stars vs. Aquilonastra)

**Source:** Genefish WordPress (Samuel Slutz) and Grace Crandall's Notebook
**Finding:** A new heat-priming project in Aquilonastra sp. starfish was initiated this week to address an underdeveloped area of thermal-stress research relative to well-studied Pacific coast sea stars (Pisaster ochraceus, Pycnopodia helianthoides, Dermasterias imbricata) affected by sea star wasting disease — the same three species Grace Crandall is currently re-analyzing for Day-12 DEG/enrichment results.

### Adds context [PubMed]: A Comparison of Juvenile and Adult Sunflower Sea Star Transcriptomic Responses to Challenge With Sea Star Wasting Disease Tissue Homogenates
Crandall et al., 2026 · PMID: 42780574 · https://pubmed.ncbi.nlm.nih.gov/42780574/ (originally posted as a preprint: https://doi.org/10.22541/au.177502918.81646805/v1)

This UW/Roberts Lab study (co-authored by Grace Crandall and Sam White) compared transcriptomic immune responses in juvenile vs. adult Pycnopodia helianthoides challenged with SSWD-affected tissue homogenates across two independent trials. Both age classes showed consistent disease signs and shared most differentially expressed genes, pointing to a conserved core defense response rather than an age-specific driver of the higher adult mortality seen in the wild. This underscores how developed the Pacific coast SSWD research base already is — exactly the comparison point Samuel Slutz's new Aquilonastra project positions itself against.

---

### Adds context [PubMed]: Precursors of sea star wasting: immune and microbial disruption during initial disease outbreak in southeast Alaska
McCracken et al., 2026 · PMID: 42014077 · https://pubmed.ncbi.nlm.nih.gov/42014077/

Using wild Pycnopodia helianthoides sampled during an active SSWD outbreak, this study found that visibly healthy but exposed individuals already showed elevated complement and immune-regulatory gene expression alongside shifts in microbial community composition, suggesting disease progression begins before visible wasting signs appear. This reinforces why the Pacific coast SSWD system is a comparatively mature research model relative to the newly-launched heat-priming work in a different starfish genus.

---

### Adds context [PubMed]: Field experiments predict ecological response to a large-scale epidemic of an anti-keystone pathogen
Wootton et al., 2026 · PMID: 42863057 · https://pubmed.ncbi.nlm.nih.gov/42863057/

Long-term intertidal surveys showed that Pisaster ochraceus populations collapsed by 90% following the SSWD epidemic and only partially recovered, triggering competitive release of mussels and a decline in sessile species diversity. This demonstrates ecosystem-level consequences of exactly the kind of species-specific SSWD susceptibility that Grace's enrichment analysis is characterizing at the molecular level.

**Literature summary:** All three retrieved papers are peer-reviewed studies from the existing Pacific coast Pycnopodia/Pisaster SSWD research base — one of them co-authored by Grace Crandall and Sam White themselves — underscoring why Samuel Slutz's new Aquilonastra project explicitly frames itself as filling a comparative gap in a less-studied starfish system.

---

### Family-specific survival/growth effects of oyster hardening (Manchester Hardening project)

**Source:** Ariana Huffmyer Lab Notebook
**Finding:** Across four time points over roughly two years, ten Pacific oyster families showed significant family-level differences in survival and a day×family×treatment growth interaction under a hardening (High vs. Control) treatment, with no consistent overall effect of treatment alone — some families gained thermal tolerance and grew more after hardening while others did not.

### Adds context [PubMed]: Evaluation of genomic selection to improve survival of eastern oysters infected with Perkinsus marinus
Delomas et al., 2026 · PMID: 42394946 · https://pubmed.ncbi.nlm.nih.gov/42394946/

In a family-based breeding program for eastern oysters (Crassostrea virginica), genome-wide association testing found that no single SNP explained more than 4% of genetic variance in survival following Perkinsus marinus disease challenge, though genomic selection modestly outperformed pedigree-based prediction. While the stressor differs (disease vs. thermal hardening), this supports the general pattern that family identity — rather than a single dominant genetic factor or uniform treatment effect — drives survival outcomes in oyster breeding/conditioning programs, consistent with the family-specific hardening response Ariana observed.

**Literature summary:** One peer-reviewed paper on a different oyster species and stressor supports the general pattern that family-level, polygenic variation (not a uniform treatment effect) governs survival outcomes in oyster breeding/conditioning programs.

---

### Resazurin metabolic response to hydrogen peroxide priming in oysters

**Source:** Genefish WordPress (giselff250455090)
**Finding:** A resazurin-based metabolic assay comparing oysters primed with low or high hydrogen peroxide doses versus unprimed controls found no significant difference in metabolic response between groups.

### Adds context [PubMed]: From blue to pink: resazurin as a high-throughput proxy for metabolic rate in oysters
Huffmyer et al., 2026 · PMID: 42495017 · https://pubmed.ncbi.nlm.nih.gov/42495017/

This validation study (co-authored by members of this same lab group) established that resazurin fluorescence tracks oxygen consumption in both C. gigas and C. virginica, reliably detects temperature-dependent metabolic shifts, and is sensitive enough to resolve family-level genetic differences in metabolic rate. Because the assay has been shown capable of detecting even subtle, family-level metabolic differences, this supports treating this week's null H2O2-priming result as a genuine absence of a metabolic effect rather than an insensitivity of the resazurin method itself.

**Literature summary:** One peer-reviewed paper — from this same lab — validates the resazurin assay's sensitivity to real metabolic differences, which strengthens confidence that this week's null H2O2-priming result reflects biology rather than assay noise.

---

> Coverage limited to papers indexed on PubMed and preprints discoverable via Europe PMC (which indexes bioRxiv, Authorea Preprints, Research Square, medRxiv, and other preprint servers), restricted to the last 12 months. **Preprints have not been peer-reviewed** and should be interpreted with appropriate caution. Preprints that have since been published in a peer-reviewed journal are reported in their published form where detected.

---

> Generated by the `full-lab-digest` skill · 2026-11-03 to 2026-11-09 (7-day window)
