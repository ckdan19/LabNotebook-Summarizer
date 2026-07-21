# Literature Connector Skill

Trigger this skill when the user asks to **find recent papers**, **check the literature**, **connect a finding to PubMed**, or **search for related publications** on a given topic in relation to a specific lab result.

## What this skill does

Searches both **PubMed** (peer-reviewed publications) and **bioRxiv** (preprints) for literature published in the last 12 months matching a user-supplied topic, fetches abstracts, and writes a brief (2–3 sentence, no direct quotes) characterization of each paper's relationship to a user-supplied lab finding. Relationships are categorized as one of: **Supports**, **Conflicts**, **Adds context**, or **Suggests next step**. Every entry is clearly labeled by source — **PubMed** or **bioRxiv preprint** — since preprints have not been peer-reviewed. If no genuinely relevant recent literature is found, the skill says so plainly — it does not stretch a loose match.

## Inputs

The skill takes two inputs from the user's message:

- **TOPIC** — the biological/scientific subject to search (e.g., `"PolyIC immune priming in Pacific oysters"`).
- **FINDING** — one or more sentences describing the specific lab result to compare against (e.g., `"HSP70 is driven by temperature stress, VIPERIN is driven by PolyIC, and cGAS-STING is unresponsive to PolyIC in Magallana gigas"`).

If the user omits the finding, ask for it before proceeding — the skill cannot categorize papers without it.

## Steps

Run Steps 1–3 (PubMed) and Steps 4–5 (bioRxiv) in parallel, then merge at Step 6.

---

### PubMed Search (Steps 1–3)

### 1. Build the PubMed search query

Transform the TOPIC into a PubMed query string. Apply the following rules:

- Identify the key species name and the key process/assay/molecule, and combine them with AND.
- Use `reldate=365` in the API call to restrict to the last 12 months — do not embed literal date strings in the query.
- Example: topic `"PolyIC immune priming in Pacific oysters"` → query `PolyIC AND "Pacific oyster" AND immune priming`.
- Keep the query short — 3–5 terms, no wildcards unless clearly needed.

### 2. Run esearch

Fetch PMIDs via:

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=QUERY&datetype=pdat&reldate=365&retmax=15&retmode=json&usehistory=n
```

Replace `QUERY` with the URL-encoded query string from step 1.

Parse `esearchresult.idlist` from the JSON response. If the list is empty:
- Try one fallback: broaden the query by dropping the least-specific term (e.g., drop the assay name, keep organism + molecule).
- If the fallback also returns an empty list, note "No papers matching [TOPIC] indexed on PubMed in the last 12 months." and continue to the bioRxiv search — do not stop the whole skill.

Cap processing at the first 10 PMIDs even if more are returned.

### 3. Fetch titles and abstracts via efetch

For the list of PMIDs, fetch full records in abstract text format:

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=PMID1,PMID2,...&rettype=abstract&retmode=text
```

**Fetch failure handling:** If the efetch call returns a non-200 HTTP status (including 403 Forbidden), do not generate any summary or characterization for those records. Report each affected PMID as "Unable to retrieve abstract — excluded from results" in the output header counts. Do not use the paper's title, any prior knowledge, or contextual inference to reconstruct what the abstract might say.

Parse the plain-text response. Each record begins with `PMID- ` and contains `TI  - ` (title), `AB  - ` (abstract), `DP  - ` (publication date), and `AU  - ` (authors).

Extract for each record:
- PMID
- Title
- Publication date (year + month)
- First author's last name
- Abstract text (full)

If an individual record in the response is missing its `AB` field, treat it the same as a failed fetch: mark it "unable to retrieve" and exclude it from all downstream processing. Do not summarize a paper based on its title alone.

---

### bioRxiv Search (Steps 4–5)

**Note on API choice:** `api.biorxiv.org` retrieves preprints by date range only (no keyword search), returning ~4,000–5,000 records per 3-week window — impractical for topic-specific retrieval. Instead, use the **Europe PMC API**, which indexes all bioRxiv preprints and supports keyword search. Results with `source: PPR` in the response are preprints from bioRxiv or medRxiv. This is the standard machine-access method for searching bioRxiv content by keyword.

### 4. Build the Europe PMC preprint query

Use the same core keywords as the PubMed query. Compute the 12-month start date as today's date minus 365 days, formatted as `YYYY-MM-DD`.

Construct the URL:

```
https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=KEYWORDS+SRC:PPR+AND+FIRST_PDATE:[START_DATE+TO+END_DATE]&resultType=core&pageSize=10&format=json
```

- Replace `KEYWORDS` with the URL-encoded topic keywords (same terms as PubMed, without field tags).
- Replace `START_DATE` with today minus 365 days (e.g., `2025-07-21`).
- Replace `END_DATE` with today's date (e.g., `2026-07-21`).
- `SRC:PPR` restricts results to preprints.
- `resultType=core` returns full abstracts.

If the query returns zero results, try one fallback by dropping the least-specific term (same strategy as PubMed step 2). If the fallback is also empty, note "No preprints matching [TOPIC] found on bioRxiv in the last 12 months." and continue with PubMed results only.

Cap processing at the first 10 preprint results.

### 5. Extract preprint metadata

From the `resultList.result` array in the JSON response, extract for each record:
- `id` (e.g., `PPR1225898`) — used as the preprint identifier
- `title`
- `firstPublicationDate`
- First author name from `authorList.author[0]` (use `fullName` or `lastName`)
- `abstractText`
- `doi`
- Confirm `source` is `PPR`; discard any record where source is not `PPR`
- Skip any record where `abstractText` is missing — do not guess content from the title alone

**Authoritative abstract source:** The `abstractText` field returned by Europe PMC is the sole authoritative basis for preprint summaries. Do **not** attempt to fetch the preprint source URL (bioRxiv.org, Authorea, medRxiv.org, etc.) to retrieve or supplement the abstract — these fetches are unreliable and frequently return 403 errors or authentication walls. If `abstractText` is absent or empty in the Europe PMC response, skip that record entirely; report it as "abstract not available via Europe PMC — excluded." Never infer or reconstruct abstract content from a failed fetch, from the preprint ID, from the title, or from prior knowledge about what a paper with that title would likely say.

---

### Merge and Filter (Steps 6–8)

### 6. Deduplication

Before applying the relevance filter, check for overlap between the PubMed results and the bioRxiv preprint results:

- For each bioRxiv preprint, check whether its title closely matches any PubMed paper title (high word overlap, allowing for minor wording differences between preprint and published versions).
- If a match is found: **keep the PubMed entry only**, and append to its citation line: `(originally posted as bioRxiv preprint: https://doi.org/[bioRxiv DOI])`.
- Remove the matching bioRxiv entry from the preprint pool.

### 7. Relevance filter

Apply the same strict relevance test to all remaining PubMed papers and bioRxiv preprints:

**A paper is relevant if and only if** its abstract discusses at least one specific entity shared with FINDING or TOPIC (same gene, protein, pathway, organism species, or experimental method). Shared vague domain (e.g., "marine biology", "immunity") does not qualify.

Discard papers that fail this test. If all papers from a given source are discarded, note this plainly (e.g., "Retrieved N bioRxiv preprints on [TOPIC] but none specifically addressed [key entity from FINDING].").

### 8. Categorize and summarize each relevant paper

For each paper that passes the relevance filter, write a single entry with:

1. **Source badge** — one of:
   - `[PubMed]` for peer-reviewed publications
   - `[bioRxiv preprint — not peer-reviewed]` for preprints

2. **Relationship tag** — choose exactly one:
   - `Supports` — abstract reports a result consistent with or confirming the FINDING
   - `Conflicts` — abstract reports a result that contradicts the FINDING (note what specifically differs)
   - `Adds context` — abstract provides background, mechanism, or comparative data that informs interpretation of the FINDING without directly confirming or contradicting it
   - `Suggests next step` — abstract identifies a gap, method, or question that follows naturally from the FINDING

3. **Summary** — 2–3 sentences written in your own words. No direct quotes from the abstract. Cover: what the paper did, what it found, and why that matters for the FINDING.

4. **Citation line**:
   - For PubMed: `[First Author et al., Year] · PMID: [PMID] · https://pubmed.ncbi.nlm.nih.gov/[PMID]/`
   - For bioRxiv: `[First Author et al., Year] · DOI: [doi] · https://doi.org/[doi]`

---

### 9. Assemble the output

Format the final output as:

```
# Literature Connector — [TOPIC]

**Lab finding:** [FINDING]

**PubMed query:** [exact query string]
**bioRxiv query:** [exact keywords + date range used]
**Date range:** last 12 months (from [today minus 365 days] to [today])
**PubMed papers retrieved:** [N] · **relevant:** [M]
**bioRxiv preprints retrieved:** [N] · **relevant:** [M]
**Excluded (retrieval failed):** [N total — list each as: PMID/DOI · reason (e.g. HTTP 403, abstract field absent, timeout); or "none" if all fetches succeeded]

---

## Relevant Literature

### [Relationship tag] [Source badge]: [Paper Title]
[First Author et al., Year] · [PMID or DOI] · [link]

[2–3 sentence summary]

---

[repeat for each relevant paper — PubMed entries first, then bioRxiv preprints]

## Summary

[2–4 sentences synthesizing what the literature as a whole says about the FINDING. Explicitly call out which supporting findings come from peer-reviewed publications vs. preprints — e.g., "Two peer-reviewed papers support this finding; one additional preprint points in the same direction but has not yet been peer-reviewed."]
```

If no relevant papers passed the filter from either source, replace the "Relevant Literature" section with a plain-language explanation.

---

### 10. Caveats

Always include at the bottom of the output:

> Coverage limited to papers indexed on PubMed and bioRxiv preprints discoverable via Europe PMC (which indexes all bioRxiv content), restricted to the last 12 months. **bioRxiv preprints have not been peer-reviewed** and should be interpreted with appropriate caution. Preprints that have since been published in a peer-reviewed journal are reported in their published form where detected.

Additional rules:
- Do not speculate about paper content beyond what is stated in the retrieved abstract.
- Never fabricate a PMID, DOI, or paper title.
- **Failed fetches — hard rule:** If any HTTP request returns a non-200 response (including 403 Forbidden, 401 Unauthorized, 500, etc.), that record must be reported as "unable to retrieve" and excluded from all results. Do not generate any summary, characterization, relationship tag, or inference from a failed fetch under any circumstances — not from the title, not from the DOI, not from contextual knowledge about the authors or topic, not from assumptions about what such a paper would likely say. A paper only appears in the results section if its abstract was successfully retrieved and is being directly cited.
