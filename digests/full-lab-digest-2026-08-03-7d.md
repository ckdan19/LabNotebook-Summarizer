# Full Lab Digest — 2026-07-28 to 2026-08-03 (7 days)

> 3 of 5 sources had activity in the last 7 days. 2 had none.

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
- **Key finding**: As part of the June 2026 SORMI project, Sam ran a Glycogen Glo Kit assay on previously homogenized *M. gigas* ctenidia samples from USDA Families 1 and 9 (ambient vs. 36°C), diluted 1:25 and read in triplicate on a Synergy plate reader. No significant family effect emerged (family 1 mean 27.1 vs. family 9 20.9 µg/mL/mg tissue; log-scale ANOVA p = 0.404), and no temperature or family × temperature effect was detectable (temperature p = 0.936, interaction p = 0.268), a conclusion robust to excluding the four samples that overshot the standard curve. Sam notes several caveats — four high-signal samples were extrapolated above the 20 µg/mL ceiling and should be re-run at higher dilution (~1:60 to ~1:150), standards were on a separate plate so plate-to-plate offset is uncorrected, and homogenization volume was not recorded — while a weight/glycogen correlation (Spearman rho = 0.66) is judged a fixed-dilution artifact largely removed by normalization.

---

## Grace Crandall's Notebook

> Summarized from [grace-ac/grace-ac.github.io](https://github.com/grace-ac/grace-ac.github.io)

### MultiSpecies - Preliminary Enrichment Results
- **Date**: 2026-07-30
- **URL**: https://grace-ac.github.io/enrichment-prelim/
- **Categories**: MultiSpecies
- **Key finding**: Grace reworked Steven and Claude's `topGO` enrichment pipeline into her own version (code 39/40) to compute GO Biological Process enrichment for three sea star species (P. helianthoides, P. ochraceus, D. imbricata) at Day 12, using annotated DEG lists as input and per-species annotated count matrices as background (dropping NA GO IDs and all-zero-count rows). Enrichment was assessed via Fisher's Exact test, producing top-50 and full result tables per species, and a dotplot showing the top 10 significantly enriched GO terms (Fisher p < 0.05) per species. She plans to share the figure and discuss the results in a casual meeting with Alyssa, Melanie, and Kate.

---

## Genefish WordPress

> Summarized from [genefish.wordpress.com](https://genefish.wordpress.com)

### Lab Notebook tweaks + Roadmap
- **Author**: Cas Daniel
- **Date**: 2026-07-28
- **URL**: https://genefish.wordpress.com/2026/07/28/lab-notebook-tweaks-roadmap/
- **Key finding**: Working with Dr. Roberts, Cas mapped out next steps for the notebook summarizer tool and executed a series of improvements: unit tests for the three Python scripts, consolidation of four near-identical notebook subagents into a shared output contract, simplified single-command subagent calls, and persistent state tracking to prevent re-reporting posts across digests. The build ran successfully; upcoming goals include automated digest scheduling, a digest index, and extending cross-section pattern analysis beyond a single week.

---

### A rough outline of my…
- **Author**: Samuel Slutz
- **Date**: 2026-07-29
- **URL**: https://genefish.wordpress.com/2026/07/29/a-rough-outline-of-my/
- **Key finding**: Samuel drafted pseudocode for an R program to compare collagen-related gene expression between exposed and unexposed samples. The logic loads a GO-tag-derived collagen gene sheet, an expression matrix, and cleaned BLAST results to map protein IDs, then iterates through the matrix summing even columns as exposed and odd columns as unexposed, averaging each, and writing the difference of means into the gene sheet.

---

### So, after scaling up the OAE oyster experiment (and throwing in some adults), they all died (again).
- **Author**: acasey2
- **Date**: 2026-07-29
- **URL**: https://genefish.wordpress.com/2026/07/29/so-after-scaling-up-the-oae-oyster-experiment-and-throwing-in-some-adults-they-all-died-again/
- **Key finding**: A scaled-up ocean alkalinity enhancement (OAE) experiment, now including adult oysters, again resulted in total mortality. Casey questions whether the deaths stem from the high pH and alkalinity themselves or from a secondary artifact — sodium carbonate precipitation — that would not occur in the field, and planned to clean the system and reconsider next steps.

---

### A bit of drama
- **Author**: acasey2
- **Date**: 2026-07-30
- **URL**: https://genefish.wordpress.com/2026/07/30/a-bit-of-drama/
- **Key finding**: Walking back the earlier post, Casey clarified that most but not all OAE oysters died, and the survivors were placed into resazurin assays (larvae in pH-adjusted resazurin matched to treatment, adults in standard working solution) for a 24-hour read. Both pH probes in the OAE bucket were found wildly miscalibrated, likely fouled by sodium carbonate precipitate, prompting a plan to possibly rerun next week after preparing new 30 ppt water.

---

### "Literature Connections" for acasey2
- **Author**: genefish
- **Date**: 2026-07-30
- **URL**: https://genefish.wordpress.com/2026/07/30/literature-connections-for-acasey2/
- **Key finding**: This automated literature-connector post links Casey's OAE findings to live PubMed and preprint searches across three themes. The consensus is that high alkalinity is not straightforwardly lethal to bivalves (mussels survived 21 days at pH 9.0) and that harm scales sharply with dose, substance, and exposure duration — supporting the lab's tank-artifact hypothesis — while confirming that rapid hydroxide dosing in calcium-bearing seawater expectedly precipitates carbonate that fouls probes, and validating resazurin as a metabolic viability readout in oysters with the caveat that it shifts with metabolic mode.

---

### This Week in Lab Notebooks
- **Author**: genefish
- **Date**: 2026-07-30
- **URL**: https://genefish.wordpress.com/2026/07/30/this-week-in-lab-notebooks/
- **Key finding**: This is an automatically generated weekly lab notebook digest post. No body content was captured by the fetch, so no substantive findings are available to summarize.

---

### Updates on Expression Helper
- **Author**: Samuel Slutz
- **Date**: 2026-07-31
- **URL**: https://genefish.wordpress.com/2026/07/31/updates-on-expression-helper/
- **Key finding**: Samuel made major progress with the R xlsx package, completing a script that reformats protein IDs to enable cross-referencing between sheets for gene expression analysis. The program combines data from multiple columns of the collagen-related genes sheet into a single new column so that protein ID formatting from the GO-tag-filtered UniProt process matches that of the initial BLAST outputs.

---

### Lab Digest Automation troubleshooting
- **Author**: Cas Daniel
- **Date**: 2026-07-31
- **URL**: https://genefish.wordpress.com/2026/07/31/lab-digest-automation-troubleshooting/
- **Key finding**: Cas spent two days attempting to fully automate the lab notebook summarizer, first hitting a wall with Claude Desktop's inability to access the WSL filesystem ("UNC file paths not supported"), then switching to WSL's cron scheduler with Claude Code, which worked after granting permanent permissions for the Python scripts. The remaining blocker is the literature-connector skill, whose required URLs and permissions change weekly; Cas began testing domain-scoped WebFetch permissions (limited to PubMed E-utilities and Europe PMC) but hit a session limit, planning to resume after reset and explore alternatives.

---

### Training for Oyster Image Analysis
- **Author**: maddyab
- **Date**: 2026-07-31
- **URL**: https://genefish.wordpress.com/2026/07/31/training-for-oyster-image-analysis/
- **Key finding**: Maddy began the oyster image annotation training, initially blocked by difficulty downloading and opening ImageJ, which was resolved using Steven's macOS Finder right-click bypass method. Over subsequent days she measured the training oysters in ImageJ and recorded the measurements in her copy of the data file, completing the training set by 8/1.

---

### Sunday Morning Notebook Summaries
- **Author**: genefish
- **Date**: 2026-08-02
- **URL**: https://genefish.wordpress.com/2026/08/02/sunday-morning-notebook-summaries/
- **Key finding**: This is an automatically generated notebook summary post. No body content was captured by the fetch, so no substantive findings are available to summarize.

_1 post from this window was already covered in a previous digest and is omitted here._

---

## Cross-Notebook Patterns & Connections

### Shared Themes
- **Sea star differential gene expression analysis** appears in two sources this window. Grace's notebook reports GO Biological Process enrichment of annotated DEG lists across three sea star species (*P. helianthoides*, *P. ochraceus*, *D. imbricata*) at Day 12, while the genefish WordPress notebook (Samuel Slutz, "A rough outline of my…" and "Updates on Expression Helper") describes building an R pipeline to compare collagen-related gene expression between exposed and unexposed starfish samples. Both center on sea star DEG analysis driven by GO-tag/UniProt annotation and BLAST-based protein-ID mapping, indicating parallel work on the same organism group and annotation workflow.

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

### Sea star differential gene expression / GO enrichment across species

**Source:** Grace Crandall's Notebook (and related starfish gene-expression work on genefish WordPress)
**Finding:** Fisher's exact test GO Biological Process enrichment on annotated DEG lists reveals distinct top-enriched GO terms per sea star species at Day 12 of a multi-species exposure experiment.

### Adds context [PubMed]: Precursors of sea star wasting: immune and microbial disruption during initial disease outbreak in southeast Alaska.
McCracken et al., 2026 · PMID: 42014077 · https://pubmed.ncbi.nlm.nih.gov/42014077/

This study integrated transcriptomic and microbial data from wild *Pycnopodia helianthoides* across sites affected and unaffected by sea star wasting, finding that exposed-but-asymptomatic individuals upregulated complement, pathogen-recognition, and immune-regulatory genes, alongside differential expression of extracellular matrix and tissue-remodeling genes. These functional categories are exactly the kind of GO Biological Process terms a per-species DEG enrichment on *P. helianthoides* would be expected to surface, offering a peer-reviewed reference point for interpreting which processes distinguish species or conditions. It reinforces that immune activation and ECM/tissue-remodeling pathways are the biologically meaningful axes in sea star differential-expression work.

**Literature summary:** One peer-reviewed publication (McCracken et al., 2026) provides directly comparable transcriptomic evidence in the same species (*P. helianthoides*), identifying immune and extracellular-matrix/tissue-remodeling pathways as the dominant differentially expressed categories — a useful external anchor for interpreting Grace's per-species GO enrichment. No relevant preprints were found on Europe PMC in the last 12 months, so the supporting evidence here rests entirely on peer-reviewed work.

---

### Effect of temperature on glycogen reserves in Pacific oyster families

**Source:** Sam's Notebook (Sam White)
**Finding:** A Glycogen Glo assay on *M. gigas* USDA Families 1 and 9 (ambient vs. 36°C) detected no significant family, temperature, or family × temperature effect on ctenidia glycogen content.

### Adds context [PubMed]: Effects of temperature and Nocardia crassostreae on the immune response of the Pacific oyster, Magallana gigas.
Mason et al., 2026 · PMID: 42476329 · https://pubmed.ncbi.nlm.nih.gov/42476329/

Over a 42-day challenge, elevated temperature independently reduced *M. gigas* glycogen stores, ATP, haemocyte viability, and gill Na+/K+-ATPase activity, while *Nocardia crassostreae* infection separately depleted mantle glycogen and mobilized energetic reserves, with no significant temperature × infection interaction. The temperature-driven glycogen depletion contrasts with Sam's null temperature effect, but the two differ sharply in design — chronic 42-day thermal + pathogen exposure and mantle tissue here versus an acute family comparison in ctenidia — so this paper frames rather than refutes the lab result, suggesting exposure duration and tissue choice may govern whether a thermal glycogen signal emerges. ⚠️ The apparent divergence would be resolved by matching exposure duration and tissue type.

### Adds context [PubMed]: Survival-enhancement potential of tea polyphenol-chitosan composites for Pacific oysters (Crassostrea gigas) during anhydrous low-temperature preservation and its multiple mechanisms.
Cheng et al., 2026 · PMID: 41950699 · https://pubmed.ncbi.nlm.nih.gov/41950699/

This food-science study showed that a tea polyphenol-chitosan coating raised post-harvest *C. gigas* survival and maintained higher glycogen levels (52.18 mg/g) and adenylate energy charge during 4°C anhydrous storage. Although the context is preservation rather than thermal-stress physiology, it independently treats glycogen as the key energy-reserve readout of oyster condition under temperature stress, corroborating the choice of glycogen as a physiological status marker in *M. gigas*.

**Literature summary:** Two peer-reviewed papers bear on this finding. Mason et al. (2026) report a temperature-driven glycogen decline under chronic exposure, which appears to diverge from Sam's null acute result but differs substantially in exposure length and tissue, so it contextualizes rather than contradicts; Cheng et al. (2026) reinforce glycogen as a standard energy-reserve marker in *C. gigas*. No relevant preprints were retrieved from Europe PMC.

---

### Ocean alkalinity enhancement (OAE) and bivalve survival

**Source:** Genefish WordPress (acasey2)
**Finding:** A scaled-up OAE experiment produced near-total oyster mortality, with the investigator suspecting a sodium-carbonate precipitation artifact rather than alkalinity toxicity per se.

### Adds context [PubMed]: Differential impacts of ocean acidification and alkalinization on shell microstructure and molecular responses in Mytilus edulis.
Chen et al., 2026 · PMID: 41806513 · https://pubmed.ncbi.nlm.nih.gov/41806513/

In a 21-day experiment, NaOH-based OAE at pH 9.0 left *Mytilus edulis* survival unaffected and actually enhanced shell integrity and growth-associated gene expression, while ocean acidification (pH 7.3) degraded shells and activated stress pathways; a core set of biomineralization genes (VWA7, CA14, ALPL) shifted across treatments. Because high alkalinity alone did not kill mussels at pH 9.0, this peer-reviewed result supports Casey's hypothesis that the observed oyster mortality more likely stems from a tank artifact (e.g., carbonate precipitation) than from alkalinity toxicity itself, though the species (mussel vs. oyster) and life stage differ.

**Literature summary:** One peer-reviewed study (Chen et al., 2026) provides direct organism-level evidence that NaOH-based OAE at pH 9.0 is not lethal to a bivalve and can even benefit shell formation, lending external support to the lab's tank-artifact interpretation of the OAE oyster mortality. The evidence is peer-reviewed but in a different species (*M. edulis*), so extrapolation to oysters remains provisional; no relevant preprints were found.

---

> Generated by the `full-lab-digest` skill · 2026-07-28 to 2026-08-03 (7-day window)
