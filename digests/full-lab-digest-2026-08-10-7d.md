# Full Lab Digest — 2026-08-04 to 2026-08-10 (7 days)

> 4 of 5 sources had activity in the last 7 days. 1 had none.

---

## Tumbling Oysters (Steven Roberts)

_No new posts in the last 7 days._

---

## Ariana Huffmyer Lab Notebook

> Summarized from [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io)

### Initial statistical analysis of PolyIC qPCR data
- **Author**: Ariana Huffmyer
- **Date**: 2026-08-03
- **URL**: https://ahuffmyer.github.io/posts/2026-08-03-qPCR-polyIC-initial-analysis.html
- **Categories**: cgigas, oyster, polyic, analysis
- **AI-use disclosure**: Level 0 (None) — no AI used for the analyses or post.
- **Key finding**: Preliminary two-way ANOVAs on qPCR ΔCq values tested whether parental PolyIC immune priming affects offspring gene expression across seven immune/stress genes. Significant PolyIC effects appeared for HSP70, HSP90, and Viperin (higher expression in PolyIC-treated groups regardless of temperature), suggesting cross-priming links between immune exposure and thermal tolerance. Citrate Synthase and ATP Synthase showed significant effects driven by high variability in biological replicates A/B (assumption violations), so their validity is uncertain and non-parametric follow-up and downsampling are planned; DNMT1 and cGAS showed no effects.

### El Nino experimental conditions planning
- **Author**: Ariana Huffmyer
- **Date**: 2026-08-03
- **URL**: https://ahuffmyer.github.io/posts/2026-08-05-el-nino-conditions-design.html
- **Categories**: el-nino, experimental design
- **Key finding**: A literature review and design-planning post for a newly funded project on the effects of "super" El Nino conditions on oyster physiology and stress tolerance. Ariana identifies four primary El Nino stressors (warming of 2–5°C, elevated salinity, hypoxia, and reduced food availability) and reviews ~9 papers, noting that few studies combine these factors—especially with host physiology, metabolism, or cross-generational effects, and none in Pacific oysters. Two candidate experimental designs are proposed (Temperature × Salinity × Food, optionally adding Oxygen) using n=6 FTR tanks with a 4–6 week exposure, recovery period, and post-recovery acute thermal stress test, tracking growth, survival, and resazurin metabolism.

### Downsampling analysis of PolyIC qPCR data
- **Author**: Ariana Huffmyer
- **Date**: 2026-08-04
- **URL**: https://ahuffmyer.github.io/posts/2026-08-04-qPCR-polyIC-downsampling-analysis.html
- **Categories**: cgigas, oyster, polyic, analysis
- **AI-use disclosure**: Level 2 (Drafting/Coding) — AI used to help draft and edit the analysis code.
- **Key finding**: Follow-up to the Aug 3 analysis, testing whether the significant PolyIC effects on HSP70, HSP90, and Viperin are robust to unequal group sample sizes by randomly downsampling to the minimum n (as low as 8) over 1,000 ANOVA iterations. The PolyIC effect remained significant in 100% (HSP70), 99.8% (HSP90), and 80% (Viperin) of iterations, confirming robustness, while non-significant interaction/stress terms remained appropriately unstable. Cohen's D effect sizes for PolyIC were large for all genes except a medium effect for Viperin at high temperature; Ariana concludes the results are robust and will be incorporated into the manuscript.

### August Goals and Daily Entries
- **Author**: Ariana Huffmyer
- **Date**: 2026-08-05
- **URL**: https://ahuffmyer.github.io/posts/2026-08-01-goals.html
- **Categories**: goals, daily-entries
- **Key finding**: A logistical monthly planning post laying out August 2026 goals across writing/manuscripts (submit PolyIC paper with qPCR data, Hawaii 2023 discussion, Moorea 2023 and Westcott oyster priming drafts), grants (NSF IOS with H. Putnam), analysis (Moorea 2023 RNAseq and metabolomics), and field/lab work (summer site check-ups, oyster image analysis, Manchester hardening sampling). Daily log entries for Aug 3–5 record work on qPCR analysis, the PolyIC paper, oyster image analysis, El Nino project design, and a meeting with Steven.

_Note: the Aug 4 downsampling post contains a malformed image link in the source (a doubled `![](![](...)` wrapper around the `fc_genes.png` URL) worth flagging to the author._

---

## Sam's Notebook (Sam White)

> Summarized from [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook)

### Glycogen Assay - SORMI June 2026 M.gigas USDA Families 1 and 9 Sample Re-runs
- **Author**: Sam White
- **Date**: 2026-08-03
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-08-03-Glycogen-Assay---SORMI-June-2026-M.gigas-USDA-Families-1-and-9-Sample-Re-runs/
- **Categories**: glycogen, Glycogen-Glo, SORMI, Pacific oyster, Magallana gigas, Crassostrea gigas
- **Key finding**: Five *M. gigas* ctenidia samples from the 2026-07-30 Glycogen-Glo run were re-assayed at higher dilution (1:200 vs 1:25) — four that read above the standard curve's top standard and one with a high replicate CV. The 8x dilution brought all four out-of-range samples back into the quantifiable range (well concentrations 1.6-9.9 µg/mL against a 0.02-20 µg/mL curve, R^2 = 0.9886), and their in-range normalized values should replace the earlier extrapolated estimates in downstream analysis. The fifth sample (`1_04_36C`) was mistakenly diluted rather than re-run at its prior 1:25 and fell below the curve floor, so it still needs a proper re-assay.

### Glycogen Analysis - SORMI June 2026 M.gigas Family 1 vs Family 9
- **Author**: Sam White
- **Date**: 2026-08-06
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-08-06-Glycogen-Analysis---SORMI-June-2026-M.gigas-Family-1-vs-Family-9/
- **Categories**: glycogen, Glycogen-Glo, SORMI, Pacific oyster, Magallana gigas, Crassostrea gigas
- **Key finding**: This entry combines the 2026-07-30 and 2026-08-03 Glycogen-Glo runs into a reconciled 32-sample dataset (families 1 and 9, ambient vs 36°C), replacing the four extrapolated values with their new in-range re-assay measurements while retaining `1_04_36C`'s original value. Two-way ANOVA found no significant family effect, no significant temperature effect, and no significant family x temperature interaction. The interaction plot shows Family 1 trending down and Family 9 trending up from ambient to 36°C, but this should be read as a visual trend only, not a confirmed effect at this sample size. This post was knitted from an external `.Rmd` in RobertsLab/sormi-assay-development.

_Note: the 2026-08-03 post's front matter contains a typo, `draft: flase` (intended `false`); it was treated as published since the value is not literally `true`._

---

## Grace Crandall's Notebook

> Summarized from [grace-ac/grace-ac.github.io](https://github.com/grace-ac/grace-ac.github.io)

### FHL Experiment - 2026 Water Filter qPCR Plates 1, 2 and 3
- **Date**: 2026-08-03
- **URL**: https://grace-ac.github.io/2026filter-qpcr-plate3/
- **Categories**: FHL2026
- **Key finding**: Logs qPCR results for Plate 3 of DNA extracted from half of the 0.45um water filters from the FHL 2026 experiment, targeting _V. pectenicida_. The standard curve was strong (R^2 = 0.992, efficiency 112.9%), with links to the plate map, protocol notes, and Google Drive results files. Summary figures across all three plates were deferred to the following day.

### August Goals
- **Date**: 2026-08-03
- **URL**: https://grace-ac.github.io/august-goals/
- **Categories**: MonthlyGoals
- **Key finding**: Sets monthly goals across dissertation chapters: final journal revisions for Chapter 1 (due Aug 25th), finishing enrichment results and drafting Chapter 2 (Multispecies), and completing DNA extractions plus 3-4 more qPCR plates for Chapter 4 (FHL eelgrass/mussel/_V. pec_ experiment). Also notes the crab paper is being transferred to a different Wiley journal, remote work Aug 19-26, and a rescheduled Quals Q3 on Aug 28th.

### FHL 2026 Water Filter qPCR Results So Far
- **Date**: 2026-08-04
- **URL**: https://grace-ac.github.io/FHL2026-filter-prelim-results/
- **Categories**: FHL2026
- **Key finding**: Synthesizes qPCR results for _V. pectenicida_ across water filter samples from the FHL 2026 experiment, with all extraction and water blanks testing negative. Treatments containing eelgrass and/or mussels showed only very low _V. pec_ levels, suggesting these organisms decrease _V. pec_ in the water, while the Vpec+seawater treatment stayed high (though lower than Time 0). Next steps are extracting DNA from eelgrass swabs and mussel tissue to test whether _V. pec_ is removed via biofilm formation or mussel accumulation.
- **Figures**:
  - local: ../notebook-images/2026-08-04/2026-SQmean-stderror-by-sample_y-axis-break.png
  - local: ../notebook-images/2026-08-04/2026-SQMean-stderror-by-treatment.png

### MultiSpecies - Preliminary Enrichment Results Part II
- **Date**: 2026-08-04
- **URL**: https://grace-ac.github.io/musp-enrichment-current/
- **Categories**: MultiSpecies
- **Key finding**: Reports GO Biological Process enrichment (topGO, Fisher p < 0.05) on annotated DEG lists for three sea star species (_Dermasterias_, _Pisaster_, _Pycnopodia_) at Day 6, Day 12, and the day-by-SSWD-exposure interaction. Day 12 showed by far the most DEGs and enriched processes across all species, and figures show the top 10 enriched processes per species. Interpretation of the specific processes is pending code double-checks and literature review; next steps include attempting orthogroup-based enrichment and a cross-species PCA.
- **Figures**:
  - local: ../notebook-images/2026-08-04/allspecies-top10-enrich-day6.png
  - local: ../notebook-images/2026-08-04/allspecies-topGO-enrich-day12.png
  - local: ../notebook-images/2026-08-04/allspecies-topGO-INTERACTION-enrich.png

### Post-SR Meeting Notes and To-Dos
- **Date**: 2026-08-06
- **URL**: https://grace-ac.github.io/postSRmtg-notes/
- **Categories**: SRMtg
- **Key finding**: Meeting notes and to-dos from a check-in with Steven. Actions include responding to Chapter 1 reviewer/editor comments (due Aug 25th), building per-species gene expression PCAs and starting to write up enrichment results for Chapter 2, and continuing DNA extractions/qPCR for Chapter 4. Also decided to transfer the crab paper to Wiley Environmental Microbiology and noted the Aug 28th Quals Q3 re-do followed by finalizing the PhD proposal.

### FHL 2026 Eelgrass Swab DNA Extractions Part 1
- **Date**: 2026-08-09
- **URL**: https://grace-ac.github.io/eelgrassswab_dna-extractions-part1/
- **Categories**: FHL2026
- **Key finding**: Tests a Becca Maher-modified Qiagen DNeasy PowerSoil Pro protocol on eelgrass swabs by extracting DNA from one sample per treatment plus two blanks before processing the remaining 28. Nanodrop checks of 1ul per sample confirmed DNA was recovered (total DNA, not yet _V. pec_-specific). A note for next time is to preheat the heat block to 65C before starting.
- **Figures**:
  - local: ../notebook-images/2026-08-09/nanodrop-eelgrassswabdna-20260809.PNG

---

## Genefish WordPress

> Summarized from [genefish.wordpress.com](https://genefish.wordpress.com)

### Resazurin stability assays
- **Author**: naomikang44
- **Date**: 2026-08-03
- **URL**: https://genefish.wordpress.com/2026/08/03/resazurin-stability-assays/
- **Key finding**: This experiment tested whether resazurin signal remains stable over time under heat exposure. Oysters in a 12-well plate were incubated at 36C for two hours, with 200mL samples transferred to a 96-well plate and read on the Synergy HTX every 30 minutes. The 96-well plate will be re-read after a week of refrigerated storage to assess longer-term stability.

### Tank room
- **Author**: Jesse Lowe
- **Date**: 2026-08-03
- **URL**: https://genefish.wordpress.com/2026/08/03/tank-room-2/
- **Key finding**: Routine tank-room maintenance and water-quality monitoring across four tanks, all reading 30ppt salinity with acceptable ammonia/nitrite/nitrate levels, though the right blue tank showed elevated nitrate (40) prompting a full water change. The right blue tank was drained, cleaned, and refitted with new filter tubing and bags, and all tanks were fed diluted shellfish diet. Mortality assessments recorded one death in bag 029 and two deaths among the 36C heat-exposure manillas from the right blue tank.

### Roadmap + Archive work
- **Author**: Cas Daniel
- **Date**: 2026-08-05
- **URL**: https://genefish.wordpress.com/2026/08/05/roadmap-archive-work/
- **Key finding**: Development progress on the Lab Notebook Summarizer, including disk caching for the literature-connector (48-hour TTL) and a digest-index skill that builds a browsable README table. The main effort was a full-text searchable archive, built by refactoring shared post-parsing logic and backfilling all five sources (4,633 posts total) using git blob SHA comparison for incremental updates. A test query on glycogen samples reading above the standard curve successfully surfaced eight months of relevant history, validating the tool; next steps include extending cross-pattern connections beyond a single week and a daily literature-connector skill.

### Lab Inventory
- **Author**: maddyab
- **Date**: 2026-08-06
- **URL**: https://genefish.wordpress.com/2026/08/06/lab-inventory/
- **Key finding**: Logistical inventory of lab supplies was started, nearly completing room 209 except for the fridge, chemical storage, and back-of-room office supply cabinets. Completed drawers and cabinets received QR code labels, with three exceptions needing new labels printed. Those three were recorded on a pink post-it left on the lab bench in 209.

### Oyster Image Analysis
- **Author**: maddyab
- **Date**: 2026-08-06
- **URL**: https://genefish.wordpress.com/2026/08/06/oyster-image-analysis-2/
- **Key finding**: Image analysis support for Ariana using ImageJ, completing measurements for Sequim sample 20260531_tag013 and nearly finishing tag014, with data entered into the shared spreadsheet. A minor issue arose while adding numbered points to oysters, which was posted to GitHub and is now resolvable.

### Oyster Image Analysis – from…
- **Author**: gracehaaland
- **Date**: 2026-08-06
- **URL**: https://genefish.wordpress.com/2026/08/06/oyster-image-analysis-from/
- **Key finding**: Ongoing image-analysis work for Ariana measuring oyster length and width in Fiji/ImageJ for Manchester bags 52-92 (May 28 2026), following an established protocol after a test image validated measurements within acceptable error. Recurring challenges include shadow-obscured edges, oysters grown together, and overlapping individuals, all noted in the spreadsheet. On 8/6 a "Flag" column and screenshot-based flag IDs were added to streamline Ariana's review, and prior bags were revisited to apply flags retroactively.

### pH probe clean-up and fine-tuning OAE dosing system
- **Author**: acasey2
- **Date**: 2026-08-06
- **URL**: https://genefish.wordpress.com/2026/08/06/ph-probe-clean-up-and-fine-tuning-oae-dosing-system/
- **Key finding**: Precipitate buildup on the OAE pH probe and HOBO loggers caused inaccurate pH readings, so they were cleaned in electrode cleaner and recalibrated—though one HOBO could not calibrate and likely needs a new electrode. The dosing system was set to a max pH of 8.5 as a safety cap against NaOH overdose, with plans to target pH 9 once mixing is controlled, and the base source was switched to Ebb Carbon NaOH to rule out Capture6 effluent as the cause of prior issues. Going forward, the protocol will use 24-hour OAE exposures with mortality counts followed by resazurin at 36C, reading plates every 30 minutes for four hours.

---

## Cross-Notebook Patterns & Connections

### Shared Themes
- **Oyster image analysis (Fiji/ImageJ) for Ariana's growth data** — Two WordPress posts (maddyab, "Oyster Image Analysis"; gracehaaland, "Oyster Image Analysis – from…") report measuring oyster length/width in Fiji/ImageJ for Ariana's Manchester and Sequim bag samples, while Ariana's own "August Goals and Daily Entries" lists oyster image analysis as an active task and daily-log item. The same measurement pipeline is being run collaboratively across the WordPress team and Ariana's notebook.
- **Resazurin metabolic assay at 36 °C** — WordPress reports a resazurin stability/QC test at 36 °C read every 30 min (naomikang44) and an OAE dosing protocol that ends in a 36 °C resazurin readout every 30 min for four hours (acasey2), while Ariana's El Niño experimental design proposes tracking resazurin-based metabolism in a post-recovery acute thermal-stress test. The same assay, temperature, and readout cadence recur across WordPress and Ariana's notebook.

### Temporal Narratives
- **Glycogen samples reading above the standard curve** — Sam re-ran out-of-range SORMI Glycogen-Glo samples at higher dilution (Aug 3) and folded the corrected in-range values into his Family 1 vs 9 analysis (Aug 6); independently, Cas Daniel's WordPress "Roadmap + Archive work" post (Aug 5) reports that the new full-text lab archive was validated with a test query on "glycogen samples reading above the standard curve," which surfaced eight months of relevant history. The tooling post and Sam's assay both center on the same specific analytical problem in the same window.

### Historical Connections
- **FHL eelgrass/mussel + _Vibrio pectenicida_ experiment** — Grace's current qPCR result (eelgrass- and/or mussel-containing treatments show only very low _V. pectenicida_, while the Vpec+seawater control stays high) directly answers the founding question of the FHL 2026 experiment she set up eight weeks earlier. See _FHL 2026 Experiment - Can eelgrass and/or mussels decrease the amount of Vibrio pectenicida in seawater?_ · 2026-06-10 (Grace Crandall, grace-ac.github.io): https://grace-ac.github.io/FHL2026_expt/
- **MultiSpecies SSWD GO enrichment (Day 12)** — Grace's "Preliminary Enrichment Results Part II" (Day 12 has by far the most DEGs/enriched processes across _Dermasterias_, _Pisaster_, and _Pycnopodia_) is the direct continuation of her Part I enrichment post from the prior week, and her planned orthogroup-based re-analysis follows up on an earlier orthogroup enrichment attempt that found no Day 12 enrichment with shared orthogroups. See _MultiSpecies - Preliminary Enrichment Results_ · 2026-07-30 (Grace Crandall, grace-ac.github.io): https://grace-ac.github.io/enrichment-prelim/
- **Shared stress-gene qPCR panel (HSP70, HSP90, citrate synthase, ATP synthase)** — Ariana's PolyIC priming analysis reports effects on the same immune/stress qPCR gene panel that Hazel Abrahamson ran for the repeat temperature-stress preliminary work earlier in the summer, indicating a shared assay/panel developing in parallel across the lab's PolyIC and repeat-stress projects. See _Repeat stress prelim – qPCR data_ · 2026-07-16 (HazelAbrahamsonA, genefish WordPress): https://genefish.wordpress.com/2026/07/16/repeat-stress-prelim-qpcr-data/
- **Glycogen and temperature — apparent contradiction across experiments** — Sam's SORMI Glycogen-Glo assay found no significant temperature effect on glycogen in _M. gigas_ Families 1 and 9 (ambient vs 36 °C), whereas Hazel's repeat temperature-stress work earlier in the summer reported that heat exposure significantly depleted glycogen. See _48-hour temp stress round 2 – GlycogenGlo results_ · 2026-06-30 (HazelAbrahamsonA, genefish WordPress): https://genefish.wordpress.com/2026/06/30/48-hour-temp-stress-trial-2/ ⚠️ Needs human verification — the two used different stocks, exposure regimes (repeated 32–35 °C timed stress with recovery vs a single 36 °C SORMI comparison), and small sample sizes, any of which could explain the divergence.
- **Resazurin whole-organism metabolic assay** — This week's resazurin stability QC (naomikang44) and OAE-experiment resazurin readout (acasey2) operationalize the whole-organism resazurin metabolic assay the lab formally validated and published earlier in the summer. See _New publications - July 2026_ · 2026-07-20 (Ariana Huffmyer, ahuffmyer.github.io): https://ahuffmyer.github.io/posts/2026-07-20-publications.html

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

### Parental PolyIC immune priming in Pacific oysters

**Source:** Ariana Huffmyer Lab Notebook
**Finding:** Parental PolyIC immune priming significantly increased offspring expression of HSP70, HSP90, and Viperin regardless of temperature, and the effect was robust to downsampling — suggesting cross-priming between antiviral immune exposure and thermal stress response.

#### Supports · [bioRxiv preprint — not peer-reviewed]: Parental immune priming reshapes offspring growth, metabolism, and thermal tolerance in the Pacific Oyster
Baird et al., 2025 · DOI: 10.64898/2025.12.10.693539 · https://doi.org/10.64898/2025.12.10.693539

Broodstock were exposed to a Poly(I:C) immune challenge and their offspring reared to seed and tested under thermal stress. Primed offspring grew faster and survived better at 40 °C (but worse at 42 °C), and showed temperature-dependent shifts in metabolic activity. This is the same parental Poly(I:C) priming paradigm and immune-to-thermal cross-talk Ariana reports, here measured at the whole-organism and metabolic level rather than in gene expression.

#### Adds context · [PubMed]: CgSMARCC2 modulates chromatin accessibility to regulate haemocyte proliferation in the immune priming of oyster Crassostrea gigas
Zhou et al., 2026 · PMID: 42162879 · https://pubmed.ncbi.nlm.nih.gov/42162879/

The study identifies a SWI/SNF chromatin-remodeling subunit in C. gigas and shows it regulates chromatin accessibility and haemocyte proliferation during immune priming, an evolutionarily conserved trained-immunity mechanism. It characterizes how oyster immune priming is established mechanistically, providing background for the persistent expression changes Ariana observes, though it does not address transgenerational priming or the HSP/Viperin genes.

#### Adds context · [PubMed]: The specifically enhanced immune response of oyster Crassostrea gigas against the secondary encountered same pathogen
Zuo et al., 2026 · PMID: 41407080 · https://pubmed.ncbi.nlm.nih.gov/41407080/

Oysters primed with Vibrio splendidus mounted a pathogen-specific enhanced response on re-exposure, with upregulated immune effectors and increased histone modifications. It supports the general reality of durable, specific immune priming in C. gigas but concerns within-generation bacterial priming rather than the transgenerational antiviral (Poly(I:C)) priming Ariana studies.

#### Adds context · [PubMed]: Identification and expression profile of serotonin receptors in the developmental stages and hemocytes of the Pacific oyster (Crassostrea gigas)
Xu et al., 2026 · PMID: 41621550 · https://pubmed.ncbi.nlm.nih.gov/41621550/

The paper characterizes thirteen serotonin receptors in C. gigas and finds several are significantly upregulated in hemocytes after secondary Vibrio challenge, implicating serotonergic signaling in immune priming. It adds mechanistic breadth to the immune-priming landscape but does not touch the stress-gene or transgenerational axis of Ariana's finding.

**Literature summary:** One bioRxiv preprint (not peer-reviewed) directly parallels the lab's result, using the same parental Poly(I:C) priming to demonstrate offspring thermal-tolerance and metabolic shifts in Pacific oysters. Three peer-reviewed papers characterize the mechanisms of C. gigas immune priming (chromatin remodeling, pathogen specificity, serotonergic signaling) but all concern within-generation bacterial priming; none test the transgenerational HSP/HSP90/Viperin thermal cross-priming axis, which remains a distinctive contribution of Ariana's analysis.

---

### Eelgrass/mussels reducing Vibrio pectenicida in seawater

**Source:** Grace Crandall's Notebook
**Finding:** In the FHL 2026 experiment, water-filter qPCR showed eelgrass- and/or mussel-containing treatments had only very low _V. pectenicida_ while the Vpec+seawater control stayed high, suggesting eelgrass/mussels decrease _V. pectenicida_ in the water column.

#### Adds context · [PubMed]: Microbe Profile: Vibrio pectenicida — the deadly marine bacteria with strains impacting sea stars and scallops
Blackwood et al., 2026 · PMID: 42455634 · https://pubmed.ncbi.nlm.nih.gov/42455634/

This profile summarizes V. pectenicida as a facultatively anaerobic marine bacterium of coastal waters, with strain FHCF-3 causing sea star wasting disease and strain A365 causing larval scallop mortality via a haemocyte-killer toxin. It establishes the identity and waterborne ecology of the exact pathogen Grace quantifies, framing why its abundance in seawater matters.

#### Adds context · [PubMed]: Vibrio pectenicida strain FHCF-3 is a causative agent of sea star wasting disease
Prentice et al., 2025 · PMID: 40760083 · https://pubmed.ncbi.nlm.nih.gov/40760083/

Using exposure experiments and deep sequencing, the authors fulfill Koch's postulates to show V. pectenicida FHCF-3 causes SSWD in sunflower sea stars. This is the foundational identification of the pathogen underlying Grace's whole research program; notably, Grace Crandall (GA Crandall) is a co-author.

#### Adds context · [bioRxiv preprint — not peer-reviewed]: When bacteria meet many arms: Autecological insights into Vibrio pectinicida FHCF-3 in echinoderms
Hewson, 2025 · DOI: 10.1101/2025.08.15.670479 · https://doi.org/10.1101/2025.08.15.670479

Re-analysis of 2013–2015 genomic/transcriptomic data found V. pectenicida FHCF-3 inconsistently across wasting sea stars, but experimental organic-matter amendment enriched it at the animal–water interface, where it surged ~24 h before lesions appeared. This speaks directly to environmental drivers of V. pectenicida abundance in water, the same quantity Grace is measuring and attempting to modulate with eelgrass/mussels.

**Literature summary:** No retrieved paper directly tests eelgrass or mussel biocontrol of V. pectenicida, so Grace's specific result stands as novel. The surrounding literature — two peer-reviewed papers and one preprint — instead establishes V. pectenicida as a waterborne pathogen of sea stars and scallops and shows its abundance responds to organic-matter and environmental conditions, which makes biological/environmental modulation of V. pectenicida in seawater biologically plausible. Grace is a co-author on the peer-reviewed paper that first identified V. pectenicida as the SSWD agent.

---

### Transcriptomic host response to sea star wasting disease (multi-species GO enrichment)

**Source:** Grace Crandall's Notebook
**Finding:** GO Biological Process enrichment on DEGs from _Dermasterias_, _Pisaster_, and _Pycnopodia_ exposed to SSWD tissue homogenates showed Day 12 with by far the most DEGs and enriched processes across all three species.

#### Adds context · [PubMed]: Precursors of sea star wasting: immune and microbial disruption during initial disease outbreak in southeast Alaska
McCracken et al., 2026 · PMID: 42014077 · https://pubmed.ncbi.nlm.nih.gov/42014077/

Integrating transcriptomics and microbial data from wild Pycnopodia helianthoides during an early SSW outbreak, the authors found exposed-but-asymptomatic stars had elevated complement, pathogen-recognition, and immune-regulatory expression, plus extracellular-matrix/tissue-remodeling changes preceding visible disease, with certain Vibrio abundances correlating to immune gene expression. This is a field-based transcriptomic parallel to Grace's experimental multi-species DEG/enrichment work, and points to the immune and tissue-remodeling process categories she may expect to see enriched.

**Literature summary:** One peer-reviewed transcriptomic study of wild Pycnopodia during an SSW outbreak reports immune (complement, pathogen recognition) and tissue-remodeling expression changes preceding visible disease, providing an independent, field-based complement to Grace's experimental multi-species enrichment result. Other retrieved Pycnopodia papers concerned predator–prey ecology and thermal tolerance rather than the transcriptomic disease response and were not specific enough to this finding to include.

---

### Resazurin as a whole-organism metabolic assay in oysters

**Source:** genefish WordPress (resazurin stability QC and OAE readouts), cross-referenced with Ariana Huffmyer Lab Notebook
**Finding:** This week's resazurin stability QC and OAE resazurin readouts rely on a resazurin-based whole-organism metabolic assay for oysters, with plates read every 30 minutes under 36 °C heat exposure.

#### Supports · [PubMed]: From blue to pink: resazurin as a high-throughput proxy for metabolic rate in oysters
Huffmyer et al., 2026 · PMID: 42495017 · https://pubmed.ncbi.nlm.nih.gov/42495017/ (originally posted as bioRxiv preprint: https://doi.org/10.1101/2025.11.06.686367)

This paper validates a whole-organism resazurin assay in Crassostrea gigas and C. virginica, showing resazurin fluorescence is strongly correlated with oxygen consumption, capturing temperature-dependent metabolic optima and tipping points, and linking greater metabolic depression to higher survival under acute thermal stress. It is the methodological foundation the lab's resazurin QC and OAE readouts rest on — and is the lab's own paper.

#### Adds context · [PubMed]: Cytotoxicity of polystyrene nanoplastics involves mitochondrial dysfunction and DNA damage in hemocytes of the Pacific oyster
de Carvalho Penha et al., 2025 · PMID: 41115343 · https://pubmed.ncbi.nlm.nih.gov/41115343/

In an in vitro assay of C. gigas hemocytes exposed to polystyrene nanoplastics, the resazurin metabolic-activity readout (LC50 = 91.6 mg/L) was more sensitive than the neutral-red lysosomal assay. It independently demonstrates resazurin's utility and sensitivity as a metabolic proxy in oyster tissue, reinforcing the assay's reliability at the cellular level.

**Literature summary:** The lab's own peer-reviewed paper (published in PeerJ, developed from a 2025 bioRxiv preprint) validates the resazurin metabolic assay in oysters against oxygen consumption and ties metabolism to thermal stress and survival, directly grounding this week's resazurin stability QC and OAE readouts. A second peer-reviewed study independently uses resazurin as a sensitive metabolic-activity readout in oyster hemocytes, further reinforcing the assay's reliability.

---

> Generated by the `full-lab-digest` skill · 2026-08-04 to 2026-08-10 (7-day window)
