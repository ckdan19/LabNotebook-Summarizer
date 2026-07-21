# Literature Connector Skill

Trigger this skill when the user asks to **find recent papers**, **check the literature**, **connect a finding to PubMed**, or **search for related publications** on a given topic in relation to a specific lab result.

## What this skill does

Queries the PubMed E-utilities API for papers published in the last 12 months matching a user-supplied topic, fetches their abstracts, and writes a brief (2–3 sentence, no direct quotes) characterization of each paper's relationship to a user-supplied lab finding. Relationships are categorized as one of: **Supports**, **Conflicts**, **Adds context**, or **Suggests next step**. Every entry includes the PMID and a PubMed link. If no genuinely relevant recent papers are found, the skill says so plainly — it does not stretch a loose match.

## Inputs

The skill takes two inputs from the user's message:

- **TOPIC** — the biological/scientific subject to search (e.g., `"PolyIC immune priming in Pacific oysters"`).
- **FINDING** — one or more sentences describing the specific lab result to compare against (e.g., `"HSP70 is driven by temperature stress, VIPERIN is driven by PolyIC, and cGAS-STING is unresponsive to PolyIC in Magallana gigas"`).

If the user omits the finding, ask for it before proceeding — the skill cannot categorize papers without it.

## Steps

### 1. Build the PubMed search query

Transform the TOPIC into a PubMed query string. Apply the following rules:

- Identify the key species name and the key process/assay/molecule, and combine them with AND.
- Append `AND ("last 12 months"[PDat] OR hasabstract[text])` — use `reldate=365` in the API call, not a literal date string in the query.
- Example: topic `"PolyIC immune priming in Pacific oysters"` → query `PolyIC AND "Pacific oyster" AND immune priming`.
- Keep the query short — 3–5 terms, no wildcards unless the term is clearly needed.

### 2. Run esearch

Fetch PMIDs via:

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=QUERY&datetype=pdat&reldate=365&retmax=15&retmode=json&usehistory=n
```

Replace `QUERY` with the URL-encoded query string from step 1.

Parse `esearchresult.idlist` from the JSON response. If the list is empty:
- Try one fallback: broaden the query by dropping the least-specific term (e.g., drop the assay name, keep organism + molecule).
- If the fallback also returns an empty list, report: "No papers matching [TOPIC] indexed on PubMed in the last 12 months." and stop.

Cap processing at the first 10 PMIDs even if more are returned.

### 3. Fetch titles and abstracts via efetch

For the list of PMIDs, fetch full records in abstract text format:

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=PMID1,PMID2,...&rettype=abstract&retmode=text
```

Parse the plain-text response. Each record begins with `PMID- ` and contains `TI  - ` (title), `AB  - ` (abstract), `DP  - ` (publication date), and `AU  - ` (authors).

Extract for each record:
- PMID
- Title
- Publication date (year + month)
- First author's last name
- Abstract text (full)

### 4. Relevance filter

For each paper, read the abstract and apply a strict relevance test:

**A paper is relevant if and only if** its abstract discusses at least one specific entity shared with FINDING or TOPIC (same gene, protein, pathway, organism species, or experimental method). Shared vague domain (e.g., "marine biology", "immunity") does not qualify.

Discard papers that fail this test. If all papers are discarded:
- Report: "Retrieved [N] recent papers on [TOPIC] but none specifically addressed [key entity from FINDING]. Closest result: [title, PMID]."

### 5. Categorize and summarize each relevant paper

For each paper that passes the relevance filter, write a single entry with:

1. **Relationship tag** — choose exactly one:
   - `Supports` — abstract reports a result consistent with or confirming the FINDING
   - `Conflicts` — abstract reports a result that contradicts the FINDING (note what specifically differs)
   - `Adds context` — abstract provides background, mechanism, or comparative data that informs interpretation of the FINDING without directly confirming or contradicting it
   - `Suggests next step` — abstract identifies a gap, method, or question that follows naturally from the FINDING

2. **Summary** — 2–3 sentences written in your own words. No direct quotes from the abstract. Cover: what the paper did, what it found, and why that matters for the FINDING.

3. **Citation line** — `[First Author et al., Year] PMID: [PMID] — https://pubmed.ncbi.nlm.nih.gov/[PMID]/`

### 6. Assemble the output

Format the final output as:

```
# Literature Connector — [TOPIC]

**Lab finding:** [FINDING]

**Search query used:** [exact PubMed query string]
**Date range:** last 12 months (from [today minus 365 days] to [today])
**Papers retrieved:** [N] · **Papers relevant:** [M]

---

## Relevant Papers

### [Relationship tag]: [Paper Title]
[First Author et al., Year] · PMID: [PMID] · https://pubmed.ncbi.nlm.nih.gov/[PMID]/

[2–3 sentence summary]

---

[repeat for each relevant paper]

## Summary

[2–4 sentences synthesizing what the literature as a whole says about the FINDING: is it well-supported, contested, novel, or pointing toward an unstudied gap?]
```

If no relevant papers passed the filter, replace the "Relevant Papers" section with a plain-language explanation per step 4.

### 7. Caveats

- Always note at the bottom: "Coverage limited to papers indexed on PubMed in the last 12 months. Preprints and conference abstracts are not included."
- Do not speculate about paper content beyond what is stated in the abstract.
- Never fabricate a PMID or paper title. If a fetch fails, skip that PMID and note it.
