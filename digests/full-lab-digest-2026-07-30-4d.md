# Full Lab Digest — 2026-07-27 to 2026-07-30 (4 days)

> 1 of 5 sources had activity in the last 4 days. 4 had none.

---

## Tumbling Oysters (Steven Roberts)

_No new posts in the last 4 days._

---

## Ariana Huffmyer Lab Notebook

_No new posts in the last 4 days._

---

## Sam's Notebook (Sam White)

_No new posts in the last 4 days._

---

## Grace Crandall's Notebook

_No new posts in the last 4 days._

---

## Genefish WordPress

> Summarized from [genefish.wordpress.com](https://genefish.wordpress.com)

### Lab Notebook tweaks + Roadmap
- **Author**: Cas Daniel
- **Date**: 2026-07-28
- **URL**: https://genefish.wordpress.com/2026/07/28/lab-notebook-tweaks-roadmap/
- **Key finding**: Development work on the notebook summarizer tool focused on hardening and simplifying the pipeline, adding unit tests for the three Python fetch/publish scripts and collapsing multi-command subagent calls into a single script invocation to speed up digest generation. Four near-identical notebook subagents were consolidated around a shared output-contract reference file, and persistent state tracking was added so repeat digests in the same week don't re-report posts. Planned next steps are automated digest scheduling, a digest index for organization, and extending cross-section pattern analysis beyond a single week.

---

### A rough outline of my…
- **Author**: Samuel Slutz
- **Date**: 2026-07-29
- **URL**: https://genefish.wordpress.com/2026/07/29/a-rough-outline-of-my/
- **Key finding**: Pseudocode was drafted for a program comparing collagen-related gene expression, joining a GO-tag-derived gene list, an expression matrix, and cleaned BLAST results to translate between base means and protein IDs. The logic loops through each examined gene, locates its protein ID in the expression matrix, then partitions columns 2–25 by even/odd index to separate exposed from unexposed samples. Each group is averaged over 12 replicates and the unexposed mean subtracted from the exposed mean to yield a per-gene difference score.

---

### So, after scaling up the OAE oyster experiment (and throwing in some adults), they all died (again).
- **Author**: acasey2
- **Date**: 2026-07-29
- **URL**: https://genefish.wordpress.com/2026/07/29/so-after-scaling-up-the-oae-oyster-experiment-and-throwing-in-some-adults-they-all-died-again/
- **Key finding**: A scaled-up ocean alkalinity enhancement trial that added adult oysters resulted in another round of near-total mortality. The open question is whether high pH and alkalinity are directly lethal, or whether mortality stems from a tank-specific artifact such as sodium carbonate precipitation that wouldn't occur in the field. The immediate plan was to clean out the system with Jake and reconsider the experimental approach.

---

### A bit of drama
- **Author**: acasey2
- **Date**: 2026-07-30
- **URL**: https://genefish.wordpress.com/2026/07/30/a-bit-of-drama/
- **Key finding**: A walk-back of the prior day's post: most but not all OAE oysters died, and the survivors were moved into resazurin assays, with larvae in pH-adjusted resazurin matched to treatment and adults in standard working solution for a 24-hour read. Both pH probes in the OAE bucket were found to be badly out of calibration, likely from sodium carbonate precipitate fouling, which undermines confidence in the recorded exposure conditions. Because the system was overdosed with alkalinity and fresh 30 ppt water needs time to cool, the rerun was deferred to the following week and repurposed as practice for Jake and Jaycee.

---

### This Week in Lab Notebooks
- **Author**: genefish
- **Date**: 2026-07-30
- **URL**: https://genefish.wordpress.com/2026/07/30/this-week-in-lab-notebooks/
- **Key finding**: No summary available — the API returned this post with an empty content body, so there is no text to synthesize. Based on the title and author it appears to be an automated cross-notebook digest post. Worth checking the live URL directly if its contents matter.

_1 post from this window was already covered in a previous digest and is omitted here._

---

## Cross-Notebook Patterns & Connections

_No cross-notebook connections identified in this window._

---

## Literature Connections

> Note: this section performs live PubMed and bioRxiv searches for each notable finding. Only findings with at least one relevant retrieved paper are shown.

### Near-total oyster mortality under scaled-up ocean alkalinity enhancement

**Source:** Genefish WordPress (acasey2, 2026-07-29 and 2026-07-30)
**Finding:** A scaled-up OAE exposure with high pH and total alkalinity killed most larval and adult oysters in the system; it is unresolved whether the lethality comes from the carbonate chemistry itself or from a closed-tank artifact such as sodium carbonate precipitation that would not occur in the field.

### Conflicts [PubMed]: Differential impacts of ocean acidification and alkalinization on shell microstructure and molecular responses in Mytilus edulis
Chen et al., 2026 · PMID: 41806513 · https://pubmed.ncbi.nlm.nih.gov/41806513/

Blue mussels were held for 21 days under ocean acidification (pH 7.3) and NaOH-based alkalinity enhancement (pH 9.0), with shell microstructure and transcriptomics as endpoints. Survival was unaffected in both treatments, and the alkalinized animals actually showed improved shell integrity and growth-associated gene expression relative to acidified ones. This is a direct counterpoint to near-total mortality at high pH — the differences to reconcile are species (mussel vs. oyster), life stage, and how the alkalinity was dosed and held.

### Adds context [PubMed]: Olivine and dissolved alkalinity trigger different bacterial community shifts in water and oyster gills: insights from a mesocosm experiment
Antoni et al., 2025 · PMID: 41852431 · https://pubmed.ncbi.nlm.nih.gov/41852431/

European flat oysters were chronically exposed in mesocosms to seawater alkalinized either by olivine weathering or by dissolved NaOH, at 250 and 500 µmol/L above control, with microbiome and ecotoxicological endpoints. Dissolved-alkalinity treatments produced minimal change relative to controls while olivine caused distinct community shifts and favored potentially pathogenic Vibrio at high alkalinity. The contrast in dose is the key interpretive point: chronic exposure at a few hundred µmol/L was largely benign for oysters, so mortality in an overdosed system points toward the dosing level or a tank-specific mechanism rather than alkalinity per se.

### Adds context [PubMed]: Assessing the effects of ocean alkalinity enhancement on marine protozoa: physiological dynamics and transcriptomic responses
Gao et al., 2026 · PMID: 42402041 · https://pubmed.ncbi.nlm.nih.gov/42402041/

Two heterotrophic nanoflagellates were exposed acutely and after acclimation to NaHCO3 and NaOH at roughly 2,600 and 4,000 µmol/L, with growth, reactive oxygen species, and transcriptomes measured. Both species reacted negatively to acute exposure, tolerance after acclimation was species-specific, and high-level treatments were consistently more damaging than low-level ones. It establishes that OAE harm is strongly dose- and substance-dependent even within a single functional group, supporting a dose-first interpretation of the oyster mortality.

### Adds context [bioRxiv preprint — not peer-reviewed]: The effects of elevated seawater pH and total alkalinity following dosing of sodium hydroxide in Calanus finmarchicus
Murray et al., 2026 · DOI: 10.64898/2026.02.03.700700 · https://doi.org/10.64898/2026.02.03.700700

Copepods were exposed to NaOH-dosed seawater at pH 10.5 (~5,000 µmol/kg TA) and pH 9.0 (~3,150 µmol/kg TA) for exposure durations of 1–30 minutes chosen to mimic field OAE plumes, then tracked for 72 hours. Almost no treatment increased mortality, though escape response was impaired in adults at the highest pH, and routine metabolic rate was unchanged. Exposure duration emerges as the pivotal variable: minutes at pH 10.5 were survivable for a copepod, which makes sustained residence in an overdosed tank a plausible explanation for the oyster deaths.

### Adds context [Research Square preprint — not peer-reviewed]: Alkalinity enhancement with sodium hydroxide in coastal ocean waters
Wynn-Edwards et al., 2025 · DOI: 10.21203/rs.3.rs-7042100/v1 · https://doi.org/10.21203/rs.3.rs-7042100/v1

The first Australian OAE field trial continuously added aqueous NaOH at a coastal Tasmanian site and tracked the resulting plume with a containerized carbonate chemistry laboratory. Alkalinity rose about 545 µmol/kg at the release point but the plume dispersed within meters, leaving downstream pCO2 signals of only a few percent. This speaks directly to the tank-artifact question: in the field, organisms experience a steep and short-lived gradient, not the sustained elevated pH and alkalinity of a closed bucket.

**Literature summary:** The peer-reviewed record does not support high alkalinity being straightforwardly lethal to bivalves — mussels survived 21 days at pH 9.0 with no mortality, and oysters chronically exposed at a few hundred µmol/L added alkalinity showed only microbiome-level responses. What the literature does establish, across peer-reviewed protozoan work and a bioRxiv copepod study, is that harm scales sharply with dose, substance, and exposure duration, and a Research Square field trial shows real-world OAE plumes disperse within meters. Together these point away from "high pH kills oysters" and toward the overdose plus sustained closed-system exposure as the likely driver, which is consistent with the lab's own tank-artifact hypothesis. Note that two of the five entries here are preprints and have not been peer-reviewed.

---

### Sodium carbonate precipitation and loss of pH measurement confidence in an alkalinity-dosed tank

**Source:** Genefish WordPress (acasey2, 2026-07-30)
**Finding:** Both pH probes in the OAE bucket were found badly out of calibration, apparently fouled by sodium carbonate precipitate, so the recorded exposure pH for the mortality experiment cannot be trusted.

### Supports [PubMed]: Alkaline materials for coastal ocean alkalinity enhancement: A comparative study of natural silicates and industrial byproducts
Li et al., 2026 · PMID: 41650710 · https://pubmed.ncbi.nlm.nih.gov/41650710/

Four alkaline materials were compared over 31-day seawater incubations and in situ deployments for alkalinity release and environmental impact. Steel slag stood out by driving a rapid pH increase that was then followed by alkalinity being consumed through secondary carbonate precipitation — a distinct pathway from the others. This confirms that fast, large pH increases in seawater can trigger secondary carbonate precipitation that removes alkalinity from solution, which is the same chemistry implicated in the fouled probes.

### Adds context [PubMed]: A new pathway to enhance the oceanic carbon sink: inorganic carbonate precipitation driven by calcium-alkali coupling
Liu et al., 2026 · PMID: 42349294 · https://pubmed.ncbi.nlm.nih.gov/42349294/

Adding Ca2+ together with OH- to seawater was tested from bench scale up to a 1,000 m³ offshore demonstration, deliberately converting dissolved inorganic carbon into solid CaCO3. Under a dose of 1.79 mmol Ca2+ and 3.58 mmol OH- per liter, DIC in the field system dropped by 1,763 µmol/kg as solid carbonate formed. The mechanism is instructive in reverse: hydroxide dosed into calcium-bearing seawater readily precipitates solid carbonate, so visible precipitate in an overdosed tank is an expected consequence rather than a contamination mystery.

### Suggests next step [PubMed]: Maximizing Carbonate Weathering Rates in an Open-System Benchtop Reactor as a Means of CO2 Capture
Moran et al., 2025 · PMID: 41359802 · https://pubmed.ncbi.nlm.nih.gov/41359802/

Fourteen benchtop seawater reactor experiments tested how gas flow, recycling, grain size, and mineralogy affect carbonate weathering rates and CO2 capture. Among the practical findings, diluting with seawater after the calcite experiments prevented carbonate from reprecipitating, and dolomite products did not reprecipitate at all. Post-experiment seawater dilution is a concrete, already-tested handle on reprecipitation in a benchtop system, and worth trying in the OAE tank to keep precipitate off probe surfaces.

### Suggests next step [PubMed]: High frequency in situ total alkalinity measurement for monitoring ocean alkalinity enhancement field trials
Zabihihesari et al., 2026 · PMID: 42020707 · https://pubmed.ncbi.nlm.nih.gov/42020707/

An autonomous lab-on-a-chip total alkalinity analyzer was deployed alongside pH, salinity, and temperature sensors during a magnesium hydroxide OAE trial, producing 314 alkalinity measurements plus 52 onboard certified reference material checks over 40 days. The onboard reference-material measurements were what kept the alkalinity record trustworthy across the deployment, and the high-frequency data revealed cumulative alkalinity retention that discrete bottle sampling would have missed. It argues for pairing pH readings with independent total alkalinity measurements and routine reference-material checks so a drifting probe is caught during the experiment rather than after.

### Suggests next step [PubMed]: High-Precision Performance of a Full-Ocean-Depth pH Sensor: Calibration and Assessment under Simulated Hadal Pressure Conditions
Mao et al., 2026 · PMID: 42263663 · https://pubmed.ncbi.nlm.nih.gov/42263663/

A solid-state electrochemical pH sensor was built with a deliberately fouling-resistant sulfonated polymer/ionic liquid composite IrOx working electrode and a stabilized ionic liquid reference electrode, then calibrated against Tris-artificial seawater buffers. Drift was held to about 0.01 pH units over 65 hours of continuous operation, with the buffer calibration protocol doing the verification work. The relevant transfer is methodological — fouling-resistant electrode materials and scheduled Tris-seawater buffer checks are the established defenses against exactly the kind of drift seen in the OAE bucket.

**Literature summary:** All four supporting entries here are peer-reviewed, with no preprints involved. The chemistry behind the lab's problem is well documented: rapid hydroxide-driven pH increases in calcium-bearing seawater precipitate solid carbonate and consume alkalinity, so precipitate in an overdosed tank is expected rather than anomalous. The literature also offers three practical mitigations — post-experiment seawater dilution to prevent reprecipitation, independent high-frequency total alkalinity measurement with certified reference material checks, and fouling-resistant electrodes on a Tris-seawater buffer calibration schedule.

---

### Resazurin as a viability and metabolic readout in surviving OAE oysters

**Source:** Genefish WordPress (acasey2, 2026-07-30)
**Finding:** Surviving OAE larvae and adults were moved into resazurin assays for a 24-hour read, with larvae in pH-adjusted resazurin matched to their treatment and adults in standard working solution.

### Supports [PubMed]: From blue to pink: resazurin as a high-throughput proxy for metabolic rate in oysters
Huffmyer et al., 2026 · PMID: 42495017 · https://pubmed.ncbi.nlm.nih.gov/42495017/ (originally posted as bioRxiv preprint: https://doi.org/10.1101/2025.11.06.686367)

This study validated a whole-organism resazurin metabolic assay in Crassostrea gigas and C. virginica, showing resazurin fluorescence tracks oxygen consumption and recovers expected thermal performance curves including metabolic tipping points. It also found that individuals showing greater metabolic depression under acute thermal stress were more likely to survive, and detected family-level genetic variation in metabolic response. This is the direct methodological warrant for the OAE readout, and its stress-survival result means the assay may do more than confirm viability — it could rank the survivors.

### Adds context [PubMed]: Cytotoxicity of polystyrene nanoplastics involves mitochondrial dysfunction and DNA damage in hemocytes of the Pacific oyster
de Carvalho Penha et al., 2025 · PMID: 41115343 · https://pubmed.ncbi.nlm.nih.gov/41115343/

Pacific oyster hemocytes were exposed for 24 hours to ~90 nm polystyrene nanoplastics and assessed with paired cytotoxicity assays. Metabolic activity measured by resazurin proved more sensitive than lysosomal integrity by neutral red (LC50 91.6 vs. 252.3 mg/L), and manipulating aerobic versus anaerobic metabolism shifted the toxicity outcome. The sensitivity ranking is useful for the OAE work, but so is the caution: resazurin signal responds to the animal's metabolic mode, so pH-driven metabolic shifts could themselves move the readout.

### Adds context [bioRxiv preprint — not peer-reviewed]: Hemocyte Viability Assay as an Alternative Method for Testing Bacterial Pathogenicity in Bivalves
Samson et al., 2025 · DOI: 10.1101/2025.11.04.686564 · https://doi.org/10.1101/2025.11.04.686564

A resazurin-based viability assay was optimized on eastern oyster hemocytes and used to derive LC50 values for Vibrio coralliilyticus RE22, a probiont, and hatchery bacterial isolates. Isolates with hemocyte LC50 below 200 MOI reliably went on to kill oyster larvae, while those at or above 690 MOI did not, validating the cell-level assay against whole-larvae outcomes. It shows a resazurin readout can be calibrated to predict larval mortality, which is the inference the OAE experiment needs from its 24-hour read.

**Literature summary:** Two peer-reviewed papers establish resazurin as a validated readout in Crassostrea — one at the whole-organism level against oxygen consumption, one at the hemocyte level where it outperformed lysosomal integrity for sensitivity — and one bioRxiv preprint, not yet peer-reviewed, demonstrates the readout can be calibrated to predict larval mortality. The assay choice for the surviving OAE animals is therefore well grounded. The main caveat carried by this literature is that resazurin reports metabolic activity and shifts with metabolic mode, so pH-adjusted and standard working solutions may not be directly comparable without a within-treatment control.

---

> Generated by the `full-lab-digest` skill · 2026-07-27 to 2026-07-30 (4-day window)
