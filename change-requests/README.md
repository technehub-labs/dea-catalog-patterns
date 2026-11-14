# Change Requests: dea-catalog-patterns

This index tracks every change request that lands on this repository.

| CR | Title | Status | Notes |
|----|-------|--------|-------|
| [CR-AP-CAT-01](CR-AP-CAT-01-catalogue-foundation.md) | Catalogue foundation (kit bring-up) | Landed (this PR) | Standard kit: pointer, dependencies, schema projection, gates 1-6, workflows, FOUNDATIONS, record standard. No records admitted. |
| CR-AP-CAT-02 | Initial population | Planned | Evidence-gated seed population per FOUNDATIONS §7. |

## Numbering

Series tag `CR-AP-CAT-NN`, sequential. Cross-repo CRs that touch this
repository are recorded here with their home-repo identifier.
| [CR-AP-CAT-02](CR-AP-CAT-02-cr-ap-cat-02.md) | Entity Ingestion Groundwork (candidate intake queue + gates) | **Proposed (this PR)** | Gated intake: queue + blocking queue gate + admission tool (candidate-state subtrees, content-derived ids); pin v2.6.0→v2.8.0 + shard-aware toolchain re-vendor. No records. |
| [AP-CAT-02](AP-CAT-02-ap-cat-02.md) | Entity Ingestion Groundwork (candidate intake queue + gates) | **Proposed (this PR)** | Gated intake: queue + blocking queue gate + admission tool (candidate-state subtrees, content-derived ids); pin v2.6.0→v2.8.0 + shard-aware toolchain re-vendor. No records. |
| [AP-CAT-03](AP-CAT-03-ap-cat-03.md) | ArchitecturePattern/Technology Candidate Corpus | **Landed (this PR)** | 2282 queue submissions from 2 bank(s); manifest with sha256s; queue gate CONFORMANT; no entities change. |
| [CR-AP-CAT-04](CR-AP-CAT-04-cr-ap-cat-04.md) | Pattern/Technology Candidate Admission Batch 01 (LinuxKit … RapidFort (member)) | **Landed (this PR)** | Admitted 500 `ArchitecturePattern/Technology` CANDIDATE records via the gated intake workflow (queue gate → admission tool → catalog gates); candidates +500, canonical unchanged; records at `lifecycle_status: proposed` in `candidates/` subtrees. |
