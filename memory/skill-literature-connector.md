---
name: skill-literature-connector
description: Literature Connector skill queries PubMed E-utilities (esearch + efetch) for papers in the last 12 months, filters strictly for relevance to a specific gene/protein/pathway/species, and categorizes each paper's relationship to a provided lab finding
metadata:
  type: project
---

The `literature-connector` skill lives at `.claude/skills/literature-connector/SKILL.md`. It takes a TOPIC and a lab FINDING, runs PubMed esearch with a 12-month date filter, fetches abstracts via efetch, applies a strict relevance filter (same specific gene/protein/pathway/organism — vague domain overlap disqualifies), and categorizes each paper as Supports / Conflicts / Adds context / Suggests next step. Always includes PMID and link.

**Key design choices:**
- Primary query uses organism + molecule/process terms (3–5 terms)
- One fallback allowed (drop least-specific term) before reporting no results
- Supplemental targeted searches for specific genes in the FINDING are run in parallel
- Papers are discarded if they don't share a named entity with the FINDING, not just a broad topic

**Tested on:** "PolyIC immune priming in Pacific oysters" vs Sam White's qPCR finding (HSP70/VIPERIN/cGAS-STING). Found 3 relevant papers: two MDA5/OASL dsRNA-sensing pathway papers in C. gigas (2026) and a cGAS-STING ecotox paper in M. gigas (2026).

**Why:** User wants a tool to connect specific lab qPCR findings to recent literature without hallucinated or loosely-matched papers.

**How to apply:** Invoke via `/literature-connector` skill. Always run supplemental gene-specific searches in parallel with the primary query.

**Disk caching (added 2026-08-03):** Raw API responses for all three live calls (PubMed esearch, PubMed efetch, Europe PMC search) are cached under `.cache/literature-connector/<sha256>.json`, keyed by `<call-type>|<exact query string>|<date window>`. Raw responses (not the filtered/categorized result) are cached so the same TOPIC query can be re-analyzed against a different FINDING. Before each live call, a fresh (< 48h) cache entry is reused and the output's "Data freshness" header notes cache use + original `fetched_at` timestamp; stale/missing → fetch live and rewrite entry. Hard rule preserved: a stale/missing cache entry + failed live fetch is still a failed fetch (report "unable to retrieve"); caching is never a fetch fallback. `.cache/` is git-ignored.
