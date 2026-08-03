# Full Lab Digest — 2026-07-28 to 2026-08-03 (7 days)

> 3 of 5 sources had activity in the last 7 days. 2 had none.
>
> _Note: this run was executed for pipeline-testing purposes. De-duplication against `digests/.digest-state.json` was intentionally not applied, so some posts below were already covered in the digest published earlier today (commit `efa0bb1`, WordPress post 2026-08-03). See the operator's note at the end of this file._

---

## Tumbling Oysters (Steven Roberts)

_No new posts in the last 7 days._

---

## Ariana Huffmyer Lab Notebook

_No new posts in the last 7 days._

---

## Sam's Notebook (Sam White)

> Summarized from [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook)

### Glycogen Assay - SORMI June 2026 M.gigas USDA Families 1 and 9 Comparisons Using Glycogen Glo Kit
- **Author**: Sam White
- **Date**: 2026-07-30
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-07-30-Glycogen-Assay---SORMI-June-2026-M.gigas-USDA-Families-1-and-9-Comparisons-Using-Glycogen-Glo-Kit/
- **Categories**: glycogen, Glycogen-Glo, SORMI, Pacific oyster, Magallana gigas, Crassostrea gigas
- **Key finding**: Sam ran the Glycogen-Glo assay on *Magallana gigas* ctenidia homogenates (32 samples, 2 USDA families × 2 temperatures, triplicate wells, 1:25 dilution) to compare glycogen content between families 1 and 9 and between ambient and 36°C exposure. Neither a family effect (27.1 vs 20.9 µg/mL/mg tissue, log-scale ANOVA p = 0.404) nor a temperature effect (p = 0.936) nor their interaction (p = 0.268) was statistically significant, and the conclusion held even after excluding four samples whose luminescence fell above the standard curve and had to be extrapolated. Sam flagged those four out-of-range samples for re-assay at higher, sample-specific dilutions (roughly 2×–6× further dilution) to get reliable direct measurements.

---

## Grace Crandall's Notebook

> Summarized from [grace-ac/grace-ac.github.io](https://github.com/grace-ac/grace-ac.github.io)

### MultiSpecies - Preliminary Enrichment Results
- **Date**: 2026-07-30
- **URL**: https://grace-ac.github.io/enrichment-prelim/
- **Categories**: MultiSpecies
- **Key finding**: Grace re-derived GO enrichment analysis (biological process only) for three sea star species (*P. helianthoides*, *P. ochraceus*, *D. imbricata*) at Day 12, building her own `topGO` workflow after reviewing code Steven and Claude had produced earlier. She used annotated DEG lists (removing NA GO annotations) against annotated count-matrix backgrounds (removing zero-count rows) run through Fisher's exact test, then produced a dotplot summarizing the top 10 significantly enriched GO terms per species (point size = number of DEGs, x-axis = -log10 p-value). The post notes this analysis was prepared for a casual check-in the following day with collaborators Alyssa, Melanie, and Kate.

---

## Genefish WordPress

> Summarized from [genefish.wordpress.com](https://genefish.wordpress.com)

### Tank room
- **Author**: Jesse Lowe
- **Date**: 2026-07-27
- **URL**: https://genefish.wordpress.com/2026/07/27/tank-room/
- **Key finding**: Routine tank-room check logging water quality across four tanks (Left/Right Blue, Left/Right Yellow), all at 30 ppt salinity with pH ranging 7.5–8.0 and zero ammonia/nitrite (nitrate 0–10 ppm). Both blue and yellow tanks were fed 10 mL of diluted shellfish diet at 11:00, and the bag filter on the Right Blue tank was replaced.

---

### Lab Notebook tweaks + Roadmap
- **Author**: Cas Daniel
- **Date**: 2026-07-28
- **URL**: https://genefish.wordpress.com/2026/07/28/lab-notebook-tweaks-roadmap/
- **Key finding**: Working with Dr. Roberts, Cas mapped out next steps for the notebook-summarizer tool and shipped several improvements: unit tests for the three Python scripts, consolidation of four near-duplicate notebook subagents into a shared output contract, simplified single-command subagent calls, and persistent state tracking to prevent re-reporting posts across digests. The build ran successfully; next goals are automated digest scheduling, a digest index, and extending cross-section pattern analysis beyond a single week.

---

### So, after scaling up the OAE oyster experiment (and throwing in some adults), they all died (again).
- **Author**: acasey2
- **Date**: 2026-07-29
- **URL**: https://genefish.wordpress.com/2026/07/29/so-after-scaling-up-the-oae-oyster-experiment-and-throwing-in-some-adults-they-all-died-again/
- **Key finding**: A scaled-up ocean alkalinity enhancement (OAE) experiment, now including adult oysters, again produced near-total mortality. Casey questions whether the deaths are due to the high pH/alkalinity itself or a secondary sodium-carbonate precipitation artifact that wouldn't occur in the field, and planned to clean the system with Jake before deciding next steps.

---

### A rough outline of my…
- **Author**: Samuel Slutz
- **Date**: 2026-07-29
- **URL**: https://genefish.wordpress.com/2026/07/29/a-rough-outline-of-my/
- **Key finding**: Samuel drafted pseudocode for an R program comparing collagen-related gene expression between exposed and unexposed samples. The logic loads a GO-tag-derived collagen gene sheet, an expression matrix, and cleaned BLAST results to map protein IDs, then sums even columns as "exposed" and odd columns as "unexposed," averages each, and writes the difference of means back into the gene sheet.

---

### This Week in Lab Notebooks
- **Author**: genefish
- **Date**: 2026-07-30
- **URL**: https://genefish.wordpress.com/2026/07/30/this-week-in-lab-notebooks/
- **Key finding**: Automatically generated weekly lab-notebook digest post. No body content was captured by the fetch, so no substantive findings can be summarized from it directly.

---

### A bit of drama
- **Author**: acasey2
- **Date**: 2026-07-30
- **URL**: https://genefish.wordpress.com/2026/07/30/a-bit-of-drama/
- **Key finding**: Walking back the earlier "all died" report, Casey clarified that most but not all OAE oysters died; survivors (larvae and adults) were placed into resazurin viability assays for a 24-hour read, with larvae in treatment-matched pH-adjusted resazurin and adults in standard solution. Both pH probes in the OAE bucket were found badly miscalibrated, likely fouled by sodium carbonate precipitate, so the team plans new 30 ppt water and possibly a rerun next week.

---

### "Literature Connections" for acasey2
- **Author**: genefish
- **Date**: 2026-07-30
- **URL**: https://genefish.wordpress.com/2026/07/30/literature-connections-for-acasey2/
- **Key finding**: Automated literature-connector post linking Casey's OAE observations to live PubMed/preprint searches. The literature indicates high alkalinity alone is not straightforwardly lethal to bivalves (mussels survived 21 days at pH 9.0) and that harm scales with dose/substance/duration — supporting a tank-artifact explanation — while also confirming that rapid hydroxide dosing in calcium-rich seawater predictably precipitates carbonate that fouls pH probes, and validating resazurin as a viability readout (with the caveat that it shifts with metabolic mode).

---

### Training for Oyster Image Analysis
- **Author**: maddyab
- **Date**: 2026-07-31
- **URL**: https://genefish.wordpress.com/2026/07/31/training-for-oyster-image-analysis/
- **Key finding**: Maddy began oyster image annotation training, initially blocked by difficulty installing/opening ImageJ, resolved via Steven's macOS Finder right-click bypass. She then measured the training oyster images in ImageJ and logged results to her data file, completing the training set by 8/1.

---

### Lab Digest Automation troubleshooting
- **Author**: Cas Daniel
- **Date**: 2026-07-31
- **URL**: https://genefish.wordpress.com/2026/07/31/lab-digest-automation-troubleshooting/
- **Key finding**: Cas spent two days trying to fully automate the lab digest workflow, first hitting a dead end with Claude Desktop ("UNC file paths not supported" for the WSL filesystem), then switching to WSL's cron with Claude Code, which worked after granting persistent permissions for the fetch/publish scripts. The remaining blocker is the literature-connector skill, whose required domains change weekly; Cas began testing domain-scoped WebFetch permissions (PubMed E-utilities, Europe PMC) but hit a session limit and plans to resume after reset.

---

### Updates on Expression Helper
- **Author**: Samuel Slutz
- **Date**: 2026-07-31
- **URL**: https://genefish.wordpress.com/2026/07/31/updates-on-expression-helper/
- **Key finding**: Samuel finished an R script (using the xlsx package) that reformats protein IDs so they can be cross-referenced across sheets for gene-expression analysis. It concatenates data from multiple columns of the collagen gene sheet into a new column, aligning the GO-tag-filtered UniProt ID format with that of the original BLAST outputs.

---

### Sunday Morning Notebook Summaries
- **Author**: genefish
- **Date**: 2026-08-02
- **URL**: https://genefish.wordpress.com/2026/08/02/sunday-morning-notebook-summaries/
- **Key finding**: Automatically generated notebook summary post. No body content was captured by the fetch, so no substantive findings can be summarized from it directly.

---

## Cross-Notebook Patterns & Connections

### Shared Themes
- **Sea star gene-expression/annotation work spans two sources.** Grace Crandall's notebook reports a `topGO`-based GO Biological Process enrichment (Fisher's exact test) on annotated DEG lists across three sea star species (*P. helianthoides*, *P. ochraceus*, *D. imbricata*) at Day 12. In parallel, genefish WordPress (Samuel Slutz, "A rough outline of my…" and "Updates on Expression Helper") describes building an R pipeline that uses a GO-tag-derived collagen gene sheet and BLAST/UniProt protein-ID mapping to compare gene expression between exposed and unexposed samples — the same GO-tag/UniProt annotation approach, on what a previously-digested post from this project ("my rough protocol for collagen gene expression analysis in starfish," 2026-07-24) identifies as starfish samples. Both efforts are independently building GO-annotation-driven differential-expression pipelines on sea star data in the same window.

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv/Europe PMC searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

### Sea star GO enrichment / differential expression across species

**Source:** Grace Crandall's Notebook (related to ongoing starfish gene-expression work on genefish WordPress)
**Finding:** Fisher's exact test GO Biological Process enrichment on annotated DEG lists reveals distinct top-enriched GO terms per sea star species (*P. helianthoides*, *P. ochraceus*, *D. imbricata*) at Day 12 of a multi-species exposure experiment.

### Adds context [PubMed]: Precursors of sea star wasting: immune and microbial disruption during initial disease outbreak in southeast Alaska
McCracken et al., 2026 · PMID: 42014077 · https://pubmed.ncbi.nlm.nih.gov/42014077/

Integrating transcriptomic and microbial data from wild *Pycnopodia helianthoides* across sites affected and unaffected by sea star wasting disease, this study found that exposed-but-asymptomatic individuals upregulated complement, pathogen-recognition, and immune-regulatory genes, along with differential expression of extracellular-matrix and tissue-remodeling genes. These are exactly the functional categories a per-species GO Biological Process enrichment on *P. helianthoides* would be expected to surface, giving a peer-reviewed reference point for interpreting which processes distinguish species or conditions in Grace's analysis.

### Adds context [Authorea Preprints preprint — not peer-reviewed]: Genome-Resolved Antibacterial Immune Response Conserved in Juvenile and Adult Sunflower Sea Stars
Crandall et al., 2026 · DOI: 10.22541/au.177502918.81646805/v1 · https://doi.org/10.22541/au.177502918.81646805/v1

This preprint — co-authored by Grace Crandall, Sam White, and Steven Roberts, the same lab notebook holders in this digest — compared transcriptomic immune responses of juvenile and adult *P. helianthoides* across two independent SSWD disease-challenge trials, finding a largely shared core response dominated by antibacterial immune genes plus some age-driven differences in development, signaling, and metabolism genes. It is closely related in silico work by the same research group and directly informs how to interpret age- or species-specific GO terms in the current Day-12 enrichment analysis.

### Adds context [bioRxiv preprint — not peer-reviewed]: When bacteria meet many arms: Autecological insights into Vibrio pectinicida FHCF-3 in echinoderms
Hewson, 2025 · DOI: 10.1101/2025.08.15.670479 · https://doi.org/10.1101/2025.08.15.670479

Investigating the candidate SSWD pathogen *Vibrio pectenicida* FHCF-3 in archival genomic/transcriptomic data, this preprint reports inconsistent detection of the bacterium in diseased *P. helianthoides* and shows it can be experimentally enriched at the body-wall surface of *Pisaster ochraceus* — two of the three species in Grace's enrichment analysis — before lesion onset. It suggests SSWD-associated gene expression signatures may reflect a broader bacterial-community response rather than one specific pathogen, a relevant caveat for interpreting cross-species GO term differences.

**Literature summary:** One peer-reviewed publication (McCracken et al., 2026) and two preprints (Crandall et al. and Hewson) bear on this finding, all in the same species group. The peer-reviewed paper anchors which GO categories (immune, ECM/tissue-remodeling) are biologically meaningful in *P. helianthoides* differential expression; the two preprints — one from the same research group — add further immune and host-microbe context but have not yet been peer-reviewed.

---

### Effect of temperature on glycogen reserves in Pacific oyster families

**Source:** Sam's Notebook (Sam White)
**Finding:** A Glycogen-Glo assay on *M. gigas* USDA Families 1 and 9 (ambient vs. 36°C) found no significant family, temperature, or family × temperature effect on ctenidia glycogen content.

### Conflicts [PubMed]: Effects of temperature and Nocardia crassostreae on the immune response of the Pacific oyster, Magallana gigas
Mason et al., 2026 · PMID: 42476329 · https://pubmed.ncbi.nlm.nih.gov/42476329/

Over a 42-day challenge, this study found that elevated temperature independently reduced *M. gigas* glycogen stores, ATP concentration, haemocyte viability, and gill Na+/K+-ATPase activity, while *Nocardia crassostreae* infection separately depleted mantle glycogen without a significant temperature × infection interaction. This contradicts Sam's null temperature effect on the surface, but the two experiments differ substantially in design — a chronic 42-day thermal/pathogen challenge on mantle tissue here versus an acute family comparison on ctenidia in Sam's assay — so exposure duration and tissue choice are plausible explanations for the discrepancy rather than a true conflict in the underlying biology. ⚠️ Needs human verification — matching exposure duration and tissue type between the two studies would clarify whether the discrepancy is due to design differences or a true absence of a thermal glycogen effect in this family/timepoint.

**Literature summary:** One peer-reviewed paper (Mason et al., 2026) reports temperature-driven glycogen depletion in *M. gigas* under a different (chronic, multi-stressor) design, which sits in tension with Sam's null acute result. No relevant preprints were retrieved from Europe PMC for this topic.

---

### Ocean alkalinity enhancement (OAE) and bivalve mortality

**Source:** Genefish WordPress (acasey2)
**Finding:** A scaled-up OAE experiment with adult and larval oysters produced near-total mortality; the working hypothesis is a sodium-carbonate precipitation artifact rather than direct alkalinity toxicity.

### Adds context [PubMed]: Olivine and dissolved alkalinity trigger different bacterial community shifts in water and oyster gills: insights from a mesocosm experiment
Antoni et al., 2025 · PMID: 41852431 · https://pubmed.ncbi.nlm.nih.gov/41852431/

In a mesocosm experiment chronically exposing European flat oysters (*Ostrea edulis*) to alkalinity-enhanced seawater (250–500 µmol·L⁻¹) via olivine weathering or dissolved NaOH, the alkalization method — not just alkalinity level — was the primary driver of microbial community shifts in both the water and the oyster gill microbiome, with high-alkalinity olivine treatments favoring potentially pathogenic *Vibrio* taxa. This adds a microbial dimension the lab hadn't considered: if the OAE tank's water chemistry shifted the microbiome toward opportunistic pathogens, that could compound or be mistaken for a pH/precipitation artifact.

### Adds context [bioRxiv preprint — not peer-reviewed]: The effects of elevated seawater pH and total alkalinity following dosing of sodium hydroxide in Calanus finmarchicus
Murray et al., 2026 · DOI: 10.64898/2026.02.03.700700 · https://doi.org/10.64898/2026.02.03.700700

This preprint exposed the copepod *Calanus finmarchicus* to NaOH-dosed seawater at pH 9.0–10.5 for short durations (1–30 minutes) and found no mortality except in one extreme combination, though escape-response behavior was more sensitive to high pH than survival was. Because short high-pH pulses were largely tolerated by this marine invertebrate, the near-total mortality in the lab's oyster experiment looks more consistent with a sustained exposure or water-chemistry artifact (e.g., carbonate precipitation) than with brief alkalinity exposure alone — though species and exposure duration both differ from the lab's setup.

### Suggests next step [Research Square preprint — not peer-reviewed]: Guidance on integrating marine environmental impacts of marine technologies into life cycle assessment — Application to ocean alkalinity enhancement
Delval et al., 2026 · DOI: 10.21203/rs.3.rs-9573704/v1 · https://doi.org/10.21203/rs.3.rs-9573704/v1

This methodological preprint identifies "the effect of added alkalinity on a broader range of marine calcifiers" as an explicit research priority for assessing OAE's ecological risk, noting that existing impact-assessment models only partially capture ecotoxicity pathways for marine organisms. It directly frames the kind of controlled, species-specific mortality/dose-response experiment the lab is already running as a recognized evidence gap in the OAE literature.

**Literature summary:** One peer-reviewed paper (Antoni et al., 2025) and two preprints (Murray et al. and Delval et al.) bear on this finding. The peer-reviewed study adds a microbiome-shift dimension not yet considered in the lab's tank-artifact hypothesis; the preprints — not yet peer-reviewed — offer a comparative low-mortality result in a different taxon under brief exposure, and frame the lab's experiment as addressing a recognized gap in OAE risk assessment for marine calcifiers.

---

> Generated by the `full-lab-digest` skill · 2026-07-28 to 2026-08-03 (7-day window)
>
> **Operator note (testing run):** de-duplication against `digests/.digest-state.json` was skipped by explicit instruction for this run, so several posts above (the Sam White and Grace Crandall entries, and most of the genefish WordPress entries) duplicate content already published in the digest generated earlier today by a separate automation (commit `efa0bb1`, WordPress post "Full Lab Digest — 2026-07-28 to 2026-08-03 (7 days)"). `.digest-state.json` was left untouched, since it already correctly reflects all of these URLs as covered.
