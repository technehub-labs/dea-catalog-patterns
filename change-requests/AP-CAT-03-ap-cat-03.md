# AP-CAT-03: ArchitecturePattern/Technology Candidate Corpus

**Status**: Landed (this PR)
**Layer**: Catalog content (candidate corpus intake)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-11-15
**Admission authority**: candidate corpus only (canonical admission remains the evidence-gated step; FOUNDATIONS D-4/D-5)
**Trigger**: Catalog population programme (2026-11 owner directive). Patterns is eighth: curated published architecture-pattern catalogs (Azure, microservices.io, EIP, Google Cloud) plus the CNCF Landscape Technology projection are the candidate seed sources named per FOUNDATIONS §7.
**Carrier**: Single PR on feature branch `feat/ap-cat-03`. PR review, not direct push.
**Lands against**: `main`
**Depends on**: AP-CAT-02 (ingestion groundwork).

## 1. What this CR lands

**2282 ArchitecturePattern/Technology candidate submissions** in `contributions/queue/<shard>/<slug>.yaml` from 2 evidence bank(s):

| Bank | Source | Records |
|---|---|---|
| curated-catalogs.json | Curated published architecture-pattern catalogs (Azure, microservices.io, EIP, Google Cloud) | 85 |
| landscape-technologies.json | CNCF Landscape (cncf/landscape hosted YAML) \u2014 Technology projection | 2197 |

Provenance in `ingestion/manifest.yaml` (bank sha256s, source URLs, retrieval dates, mapping note). Every submission carries `source_ref`, a `published-document` evidence citation, and published description prose. Provisional field mappings are documented per record and in the manifest; per-organization values are canonical-admission decisions.


## 2. What changes

- `contributions/queue/<shard>/` — 2282 intake submissions (`status: queued`)
- `ingestion/manifest.yaml` — corpus provenance record (new)
- No `CATALOG.yaml` change (queue ≠ index)
- This CR file and the index row

## 3. Verification

- `check_contributions.py`: CONFORMANT (2282 queue files)
- No directory holds 800+ entries (slug-prefix distribution)
- Spot-checks: records trace to their published source identifiers

## 4. NOT-List

- NOT record admission (nothing under `entities/` changes; admission follows in AP-CAT-04+).
- NOT a modification of gates, schemas, or intake tooling.
- NOT an authoritative assessment of provisional mapped values.

## 5. Acceptance criteria

1. 2282 gate-CONFORMANT submissions; manifest carries bank sha256s + source URLs.
2. Submissions carry no `id`; `status: queued`; `submitted_by: Emmanuel A. Otchere`.
3. `CATALOG.yaml` counts unchanged.
