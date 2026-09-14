# Full Lab Digest — 2026-08-25 to 2026-08-31 (7 days)

> 4 of 6 sources had activity in the last 7 days. 2 had none.

---

## Tumbling Oysters (Steven Roberts)

_No new posts in the last 7 days._

---

## Ariana Huffmyer Lab Notebook

## Ariana Huffmyer Notebook Digest — Week of 2026-08-24 to 2026-08-31

> Summarized from [AHuffmyer/ahuffmyer.github.io](https://github.com/AHuffmyer/ahuffmyer.github.io)

### Goose Point site growth analysis from 20250522 sampling
- **Date**: 2026-08-18
- **Author**: Ariana Huffmyer
- **Categories**: cgigas, goose-point, hardening, oyster, growth
- **Key finding**: Photo-based growth analysis (volume predicted from length/width, R²=0.96) was updated through the May 2026 assessment for the Goose Point thermal and salinity hardening experiments. Neither temperature nor salinity hardening produced a lasting survival or growth difference — significant treatment×time interactions were driven by transient differences at earlier (2025) time points, with no difference detected at the most recent sampling.
- **Figures**:
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/Rplot.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/model.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/temp-plot.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/salinity-plot.png?raw=true

---

### Sequim Bay site growth analysis from 20250531 sampling
- **Date**: 2026-08-25
- **Author**: Ariana Huffmyer
- **Categories**: cgigas, sequim-bay, hardening, oyster, growth
- **Key finding**: Growth analysis was brought up to date through the May 2026 assessment for two Sequim Bay projects — the PolyIC cross-generational immune priming outplant and the Effort A thermal hardening experiment. Neither immune priming nor thermal hardening treatment affected field growth (only a strong effect of time was significant), and bag-level survival did not differ between PolyIC treatments.
- **Figures**:
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/sequim-effortA.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/polyic-plot.png?raw=true
  - external: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/polyic-surv.png?raw=true

_1 post from this window was already covered in a previous digest and is omitted here._

---

## Sam's Notebook (Sam White)

# Sam White Notebook Digest — Week of 2026-08-24 to 2026-08-31

> Summarized from [RobertsLab/sams-notebook](https://github.com/RobertsLab/sams-notebook)

Note: `commits_scanned` = 9 over the last 7 days, yielding 5 changed posts, all `change_class: substantive`. All five are extremely long, code-heavy R-knitted posts; the fetch script truncated the middle of each (front matter, intro/callouts, and RESULTS/SUMMARY sections at head and tail remain intact) — noted per-post below.

### Citrate Synthase Assay - SORMI June 2026 M.gigas Family 5 Ambient Ctenidia Re-assay
- **Date**: 2026-08-24
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-08-24-Citrate-Synthase-Assay---SORMI-June-2026-M.gigas-Family-5-Ambient-Ctenidia-Re-assay/
- **Author**: Sam White
- **Categories**: SORMI, Magallana gigas, ctenidia, Pacific oyster, Crassostrea gigas, citrate synthase, ABCAM
- **Key finding**: Re-assay of the same Family 5 ambient homogenates that failed QC on 20260811, using a shorter 20-min read window and a pooled (rather than paired per-sample) background control. This run succeeded outright — all 8 samples pass the 15% CV threshold (0.8–4.6%), zero flagged standard-curve outliers (R²=0.998), no compromised wells — and the entry states it supersedes the original ambient results and does not need re-assay. One caution carried forward: the positive control's three replicates disagreed by 22.8% CV, worse than any individual sample, worth watching on future plates; real inter-individual variation is seen at ambient (169% spread) vs. the uniform 36°C plate.
- **Figures**:
  - local: `Gen5-20260824-mgig-sormi-citrate_synthase-F05-ambient_files/figure-gfm/plot-activity-1.png`
  - local: `Gen5-20260824-mgig-sormi-citrate_synthase-F05-ambient_files/figure-gfm/plot-activity-normalized-1.png`
- **Note**: content truncated (~98,900 characters omitted from the middle; head and tail intact).

---

### Citrate Synthase Assay - SORMI June 2026 M.gigas Family 7 Ambient and 36C Ctenidia
- **Date**: 2026-08-24
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-08-24-Citrate-Synthase-Assay---SORMI-June-2026-M.gigas-Family-7-Ambient-and-36C-Ctenidia/
- **Author**: Sam White
- **Categories**: SORMI, Magallana gigas, ctenidia, Pacific oyster, Crassostrea gigas, citrate synthase, ABCAM
- **Key finding**: All 16 Family 7 individuals (8 ambient + 8 36°C) assayed together on one plate specifically to avoid the between-plate timing issues seen in the Family 5 comparison. The background control failed — Reaction Mix appears to have been pipetted into all three pooled background wells instead of Background Control Mix — so reported rates are raw/uncorrected (background correction = 0); since background has historically been only ~2–7% of signal, the entry judges this a modest, unconfirmed overestimate rather than grounds to redo the whole plate (recommends re-running just the background triplicate). One sample (`F07_03_ambient`) had a dead well and was salvaged from 2 of 3 replicates; protein normalization looks biologically appropriate here (raw rate strongly correlates with total protein, r=+0.94).
- **Figures**:
  - local: `Gen5-20260824-mgig-sormi-citrate_synthase-F07-ambient_and_36C_files/figure-gfm/plot-activity-1.png`
  - local: `Gen5-20260824-mgig-sormi-citrate_synthase-F07-ambient_and_36C_files/figure-gfm/plot-activity-normalized-1.png`
- **Note**: content truncated (~107,500 characters omitted from the middle; head and tail intact).

---

### Citrate Synthase Analysis - SORMI June 2026 M.gigas Family 5 vs Family 7 Temperature Response
- **Date**: 2026-08-25
- **URL**: https://robertslab.github.io/sams-notebook/posts/2026/2026-08-25-Citrate-Synthase-Analysis---SORMI-June-2026-M.gigas-Family-5-vs-Family-7-Temperature-Response/
- **Author**: Sam White
- **Categories**: SORMI, Magallana gigas, ctenidia, Pacific oyster, Crassostrea gigas, citrate synthase, ABCAM
- **Key finding**: Downstream 2×2 (family × temperature) statistical comparison combining the three finished per-plate results above (32 individuals total, n=8/cell), with background correction stripped from all plates so every group is treated identically (the F07 plate has no usable background estimate). A two-way ANOVA on log10(activity) finds a significant family × temperature interaction (p=1e-05, 23% of variance): Family F05 loses citrate synthase activity at 36°C (114.2→40.6 mU/mg protein, a 64% drop, p=2e-07 after Tukey adjustment), while Family F07 shows essentially no temperature response (129.5→129.0 mU/mg, p=1); the two families are indistinguishable at ambient temperature, so the effect is family-specific heat sensitivity rather than a baseline difference. Removing the background correction does not drive the result (correction was only 0–11.3% of activity, median 0.8%).
- **Figures**:
  - local: `Gen5-20260825-mgig-sormi-citrate_synthase-F05-F07-temperature-comparison_files/figure-gfm/plot-activity-by-group-1.png`
  - local: `Gen5-20260825-mgig-sormi-citrate_synthase-F05-F07-temperature-comparison_files/figure-gfm/plot-interaction-1.png`
  - local: `Gen5-20260825-mgig-sormi-citrate_synthase-F05-F07-temperature-comparison_files/figure-gfm/plot-individuals-1.png`
  - local: `Gen5-20260825-mgig-sormi-citrate_synthase-F05-F07-temperature-comparison_files/figure-gfm/plot-background-effect-1.png`
- **Note**: content truncated (~18,200 characters omitted from the middle; head and tail intact). Front matter also sets a thumbnail `image:` pointing to the first plot above.

All five posts are part of a single continuous SORMI citrate-synthase workflow (Families 5 & 7, ambient vs. 36°C) and are knitted from R Markdown source files in `RobertsLab/sormi-assay-development`; the "Notebook was knitted from ...Rmd" links are metadata only and were not treated as content.

_2 posts from this window were already covered in a previous digest and are omitted here._

---

## Grace Crandall's Notebook

_No new posts in the last 7 days._

---

## Megan Ewing Lab Notebook

### Field Days: Retrieval 1 & Assay Planning
- **Date**: 08-11-2026
- **URL**: https://meganewing.github.io/mewing-notebook/posts/2026-08/fieldretrieval1.html
- **Author**: Megan Ewing
- **Categories**: projects
- **Change this week**: Cosmetic whitespace-only edit — removed trailing spaces after three subheadings ("Assay Options", "Option 1/'Plan A'", "Option 3"). No new science content; the post's substance (retrieval counts for Westcott/Agate Pass manilas and cockles, pilot survival/resazurin assay results, and the four candidate thermal-assay designs) is unchanged from a prior week.

---

### Clam and Cockle Priming: Preliminary Assay Results
- **Date**: 08-25-2026
- **URL**: https://meganewing.github.io/mewing-notebook/posts/projects/CnC-retreival1_prelims.html
- **Author**: Megan Ewing
- **Categories**: projects
- **Key finding**: This new post is a reveal.js slide deck (embedded via a Google Slides iframe) presenting preliminary results from the clam and cockle thermal-priming assays discussed in the prior planning post. The post body itself contains no extractable narrative text beyond the embed, so detailed results (survival/metabolism differences across temperature treatments) are only viewable in the linked slides, not in the post source.
- **Figures**: none found (content is an embedded external Google Slides presentation, not a markdown/HTML image).

Note: both posts this week are authored "Megan Ewing"; no posts from the boilerplate template authors (Tristan O'Malley, Harlow Malloc) were changed in this window.

---

## Genefish WordPress

# genefish WordPress Digest — Week of 2026-08-24 to 2026-08-31

> Summarized from [genefish.wordpress.com](https://genefish.wordpress.com)

### Resazurin stability and round 2 survival assays
- **Author**: naomikang44
- **Date**: 2026-08-24
- **URL**: https://genefish.wordpress.com/2026/08/24/resazurin-stability-and-round-2-survival-assays/
- **Key finding**: A third-week (refrigerated) reading of a resazurin stability plate showed modest, row-dependent drift relative to the prior timepoint, suggesting the reagent is not perfectly stable in storage. An evening survival check for the Manchester sampling experiment found no new mortalities but several "double oyster" cups, prompting a decision to track only the larger oyster per cup going forward, with results logged to a shared spreadsheet.

---

### Full Lab Digest — 2026-08-18 to 2026-08-24 (7 days)
- **Author**: Cas Daniel
- **Date**: 2026-08-24
- **URL**: https://genefish.wordpress.com/2026/08/24/full-lab-digest-2026-08-18-to-2026-08-24-7-days/
- **Key finding**: An automated cross-notebook digest tying together the week's activity: Sam White's citrate synthase assays on Family 5 oyster ctenidia (clean 36 °C run vs. a QC-flagged ambient run, with a read-duration mismatch flagged as a confound) paired against genefish's own 36 °C Manchester Hardening survival assay, where mortality overshot expectations and ended the trial early despite visible family-level survival differences. It also connected a surviving heat-plus-polyIC-primed cockle to prior priming literature, concluding the single survivor is suggestive but not yet strong evidence of a priming effect.

---

### 8/24 OAE Oysters update
- **Author**: jbalzer5
- **Date**: 2026-08-24
- **URL**: https://genefish.wordpress.com/2026/08/24/8-24-oae-oysters-update/
- **Key finding**: The HOBO logger was calibrated and placed in the treatment water in preparation for an ocean acidification exposure (OAE) run on oysters. The planned exposure was postponed because the two pH probes were not reading in sync with each other.

---

### Mortality Checks and Inventory
- **Author**: maddyab
- **Date**: 2026-08-25
- **URL**: https://genefish.wordpress.com/2026/08/25/mortality-checks-and-inventory/
- **Key finding**: Morning and afternoon mortality checks on heat-stressed oysters were complicated by low overnight water levels (skewing temperatures) and ambiguous shell responses — several oysters presumed dead reflexively closed when jostled, so their identities were lost before they could be returned to water. Lab inventory work continued in rooms 209/213, with completed drawers tagged with QR codes and a note left about codes needing reprinting.

---

### Tank room and survival assays
- **Author**: Jesse Lowe
- **Date**: 2026-08-26
- **URL**: https://genefish.wordpress.com/2026/08/26/tank-room-and-survival-assays-5/
- **Key finding**: Routine water quality checks and a full water change were performed across the four tanks, with salinity holding at 30 ppt and ammonia at zero throughout. The Manchester oyster hardening assay was concluded at the 52-hour mark with 10 of the original animals surviving (three from the same family), after which the oysters were disposed of and cups cleaned for the next round.

---

### Tank room and survival assays
- **Author**: Jesse Lowe
- **Date**: 2026-08-26
- **URL**: https://genefish.wordpress.com/2026/08/26/tank-room-and-survival-assays-4/
- **Key finding**: A near-duplicate log of the same day's tank maintenance and final mortality assessment for the Manchester oyster hardening assay, again reporting 10 survivors at 52 hours (three sharing a family) and slightly different nitrate readings in the left yellow tank. The experiment was ended and cups cleaned for reuse.

---

### Mortality Check
- **Author**: maddyab
- **Date**: 2026-08-26
- **URL**: https://genefish.wordpress.com/2026/08/26/mortality-check/
- **Key finding**: A 10am mortality check found heavy die-off, with only about 20 oysters still alive, coinciding with a tank leak that had lowered the water level and stopped circulation. The author questioned whether infrequent checks were limiting the data quality and suggested more frequent monitoring might also help with an associated odor.

---

### Tank room
- **Author**: Jesse Lowe
- **Date**: 2026-08-28
- **URL**: https://genefish.wordpress.com/2026/08/28/tank-room-3/
- **Key finding**: Full water changes were completed on the left blue and right yellow tanks, both testing clean on ammonia/nitrite/nitrate at 30 ppt salinity, while the right blue tank retained detectable nitrite and nitrate. The left yellow tank (previously housing cockles) was shut down, its silos cleaned, and refilled with fresh seawater but left empty of animals.

---

### After the green pH probe…
- **Author**: acasey2
- **Date**: 2026-08-31
- **URL**: https://genefish.wordpress.com/2026/08/31/after-the-green-ph-probe/
- **Key finding**: The green pH probe, which had been giving erratic readings, was restored to normal operation after soaking in electrode cleaner and storage solution. With the probe fixed, another 24-hour OAE exposure was planned for the same day, followed by a resazurin assay the next day (4-hour run with 30-minute heat exposure intervals).

---

## Cross-Notebook Patterns & Connections

_This section analyzes the compiled per-source summaries for shared themes, follow-up narratives, apparent contradictions, and multi-week historical connections across the lab's notebooks. Connections are surfaced only when a specific named entity ties the sources together — never from vague thematic similarity._

_No cross-notebook connections identified in this window._

### Historical Connections
- **Citrate synthase / SORMI M. gigas Family 5** — This week's finding that Family 5 loses 64% of its citrate synthase activity at 36°C while Family 7 shows none rests on data from the originally QC-failed ambient-temperature plate, which had been flagged as needing to be repeated. See "Citrate Synthase Assay - SORMI June 2026 M.gigas Family 5 Ambient Ctenidia" · 2026-08-11 (Sam White, Sam's Notebook): https://robertslab.github.io/sams-notebook/posts/2026/2026-08-11-Citrate-Synthase-Assay---SORMI-June-2026-M.gigas-Family-5-Ambient-Ctenidia/
- **PolyIC immune priming, Sequim Bay** — This week's null result for field growth/survival under PolyIC cross-generational immune priming follows an earlier molecular-level statistical pass at qPCR data from the same PolyIC-treatment groups. See "Initial statistical analysis of PolyIC qPCR data" · 2026-08-03 (Ariana Huffmyer, Ariana Huffmyer Lab Notebook): https://ahuffmyer.github.io/posts/2026-08-03-qPCR-polyIC-initial-analysis.html
- **Manila clam & cockle thermal priming** — Megan's preliminary assay-results slide deck this week follows a genefish literature-connection post that surfaced published research on priming's effects on Manila clam microbiota/pathogen dynamics, for the same priming cohort referenced in Megan's earlier retrieval-planning post. See "Daily Literature Connections — 2026-08-24" · 2026-08-24 (Cas Daniel, Genefish WordPress): https://genefish.wordpress.com/2026/08/24/daily-literature-connections-2026-08-24/

---

## Data & Figures

_This section consolidates, grouped by source, the figure links and external data/repository links already surfaced in the per-source summaries above. It is a single entry point into the underlying data and figures for this window, not a new analysis._

### Ariana Huffmyer Lab Notebook
- Goose Point site growth analysis from 20250522 sampling: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/Rplot.png?raw=true
- Goose Point site growth analysis from 20250522 sampling: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/model.png?raw=true
- Goose Point site growth analysis from 20250522 sampling: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/temp-plot.png?raw=true
- Goose Point site growth analysis from 20250522 sampling: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/salinity-plot.png?raw=true
- Sequim Bay site growth analysis from 20250531 sampling: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/sequim-effortA.png?raw=true
- Sequim Bay site growth analysis from 20250531 sampling: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/polyic-plot.png?raw=true
- Sequim Bay site growth analysis from 20250531 sampling: https://github.com/AHuffmyer/ahuffmyer.github.io/blob/main/images/notebook/20260825/polyic-surv.png?raw=true

### Sam's Notebook (Sam White)
- Citrate Synthase Assay - Family 5 Ambient Ctenidia Re-assay: `Gen5-20260824-mgig-sormi-citrate_synthase-F05-ambient_files/figure-gfm/plot-activity-1.png`
- Citrate Synthase Assay - Family 5 Ambient Ctenidia Re-assay: `Gen5-20260824-mgig-sormi-citrate_synthase-F05-ambient_files/figure-gfm/plot-activity-normalized-1.png`
- Citrate Synthase Assay - Family 7 Ambient and 36C Ctenidia: `Gen5-20260824-mgig-sormi-citrate_synthase-F07-ambient_and_36C_files/figure-gfm/plot-activity-1.png`
- Citrate Synthase Assay - Family 7 Ambient and 36C Ctenidia: `Gen5-20260824-mgig-sormi-citrate_synthase-F07-ambient_and_36C_files/figure-gfm/plot-activity-normalized-1.png`
- Citrate Synthase Analysis - Family 5 vs Family 7 Temperature Response: `Gen5-20260825-mgig-sormi-citrate_synthase-F05-F07-temperature-comparison_files/figure-gfm/plot-activity-by-group-1.png`
- Citrate Synthase Analysis - Family 5 vs Family 7 Temperature Response: `Gen5-20260825-mgig-sormi-citrate_synthase-F05-F07-temperature-comparison_files/figure-gfm/plot-interaction-1.png`
- Citrate Synthase Analysis - Family 5 vs Family 7 Temperature Response: `Gen5-20260825-mgig-sormi-citrate_synthase-F05-F07-temperature-comparison_files/figure-gfm/plot-individuals-1.png`
- Citrate Synthase Analysis - Family 5 vs Family 7 Temperature Response: `Gen5-20260825-mgig-sormi-citrate_synthase-F05-F07-temperature-comparison_files/figure-gfm/plot-background-effect-1.png`

---

## Literature Connections

_Live PubMed and Europe PMC/bioRxiv literature searches could not be completed in this run — outbound network access via the available tools (WebFetch, direct HTTP) was not granted in this environment. Per the literature-connector skill's no-hallucination rule, no literature content is fabricated in place of a live search. No Literature Connections section is reported for this digest; this should be re-run when network access is available._

---

> Generated by the `full-lab-digest` skill · 2026-08-25 to 2026-08-31 (7-day window)
