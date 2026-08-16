# dea-catalog-patterns

> DEA catalog for **Architecture Pattern** (+ Technology, shared repo) — OpenDEAM v0.2.1 (ADR-0002).

## Architecture Pattern (`AP`)

- **Entity id:** `dea:entity-architecture-pattern`
- **Allocation:** L2 · L2-reusable-knowledge · discriminator `pattern_kind`
- **Status:** planned

A reusable architecture pattern (e.g. API Gateway, Event Sourcing, CQRS) that
resolves a recurring design problem.

## Technology (`TEC`) — shared catalog repo (ADR-0002 D6)

- **Entity id:** `dea:entity-technology`
- **Allocation:** L5 · L5-technology · discriminator `technology_kind`

A governed technology adopted for enterprise use (graduates from the
Technology Radar via `TRE → TEC`).

## Relationships (from the OpenDEAM model)

- **BLU → AP** — composed of (composition, 1:1..N)
- **TEC → APC** — implements (dependency, 0..N:0..N)
- **TRE → TEC** — graduates to (realization, 0..1:0..1)
- **GRD → TEC** — governs (governance, 0..N:0..N)

## Allocation contract

This repo's `metamodel-pointer.yaml` is validated in CI against the pinned
OpenDEAM root model (`v0.2.1`) via the reusable
`validate-against-model.yml` workflow. Drift fails CI.

Content (entity instances) lands when the entity promotes from
`planned` to `scaffold` per the model lifecycle.

## License

Apache 2.0 — see [LICENSE](./LICENSE) and [NOTICE](./NOTICE).
