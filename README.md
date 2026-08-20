# Arvectum Company

Canonical repository for the durable governance, planning, portfolio and organizational-model artifacts of ООО «Арвектум» as an owner-operated AI-native company.

Arvectum Company is a concrete organization. It is **not** Arvectum OS, a standalone AI agent or a universal software platform.

## Start here

- Company Constitution / Founding Charter: `docs/constitution/COMPANY-CONSTITUTION.md`
- Company ↔ Arvectum OS authority boundary: `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md`
- Canonical source registry: `docs/CANONICAL-SOURCES.md`
- Canonical Company roadmap: `docs/roadmap/ROADMAP.md`
- Initial Company portfolio: `docs/portfolio/PORTFOLIO.md`
- AC-201 function model: `docs/organization/MINIMAL-REAL-ORGANIZATIONAL-FUNCTION-MODEL.md`
- AC-202 Reserved Owner Decisions: `docs/governance/RESERVED-OWNER-DECISIONS-v1.0.0.md`
- AC-203 delegated Position authority model: `docs/governance/DELEGATED-POSITION-AUTHORITY-MODEL-v1.0.0.md`
- AC-204 Initial Position Registry: `docs/organization/INITIAL-POSITION-REGISTRY-v1.0.0.md`
- AC-205 Initial Assignments: `docs/organization/INITIAL-ASSIGNMENTS-AND-EXECUTOR-CLASSIFICATION-v1.0.0.md`
- AC-206 Company access boundary: `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY-v1.0.0.md`
- Formal review evidence: `docs/reviews/`
- Durable Owner/governance decisions: `docs/governance/decisions/`

## Current Company state

`M0 — Company canonically founded` and `M1 — Business/economic reality and first market-validation plan captured` are `Complete / PASS`.

Phase 2 has established the organization-first chain through Position, Assignment and access-governance design:

```text
AC-201 functions
→ AC-202 Reserved Owner Decisions
→ AC-203 delegated Position authority semantics
→ AC-204 Initial Position Registry
→ AC-205 Assignments / executor classification
→ AC-206 access boundary
→ AC-207 continuity / replacement / fallback
→ AC-208 transferability review
```

`AC-206 — Company data/tool/credential access boundary baseline` is `Complete / PASS` after `9/10` cross-review iterations and explicit Owner approval.

The binding AC-206 baseline establishes deny-by-default / least-privilege access governance, `DC-0` through `DC-3` data classes, `R/W/X/P/K/E` technical capability markers, `RA-01` through `RA-18` resource classes and Position/Assignment-specific access ceilings.

Key operating implications:

- technical access does not create Organizational Authority, legal/corporate power or customer rights;
- AI-led `POS-004 — Engineering & Release Lead` may receive meaningful bounded repository/build/test execution access without receiving Owner-wide admin, bank, signing or unrelated commercial/customer privilege;
- AI commercial work under `POS-002` is designed around scoped prospect/CRM state and a dedicated/scoped sender rather than the Owner's unrestricted mailbox;
- `POS-005` Finance and `POS-006` Security/Risk/Continuity remain separate access contexts even though the same current human Principal temporarily holds both Positions;
- reusable secrets, private keys, recovery codes, bank/signing authentication material and equivalent `DC-3` values are prohibited from the public Company repository and ordinary AI/model context;
- approval of the access boundary does not itself provision accounts or credentials and does not claim that rotation/recovery/break-glass/continuity controls are already fully implemented.

The current canonical Company action is:

**`AC-207 — Critical-function continuity, replacement and manual fallback baseline`**.

AC-207 must determine what continues, degrades or stops when an Owner, AI runtime, local device, repository host, credential path, outsourced provider or other material dependency is unavailable, while preserving Owner/legal/customer authority and deliberate security gates.

The bounded AC-108 design-partner discovery loop remains separately authorized P1 market-evidence work and does not imply a pilot, price, SLA, privileged access or customer commitment.

## Repository boundary

Company-specific governance and organizational semantics belong here when suitable for repository storage. Product implementation remains canonical in the corresponding product repository. Domain-neutral platform architecture and contracts belong in `arvectum/arvectum-os`.

This repository is public. Do **not** commit secrets, reusable credentials, unnecessary personal data, signatures, bank/payment details, non-public customer/supplier/contract material or other restricted operational payloads.

## Remotes

GitHub `arvectum/arvectum-company` is the canonical remote. GitVerse is a resilience/sovereignty mirror and is not an independent source of Organizational Authority.
