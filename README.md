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
- AC-207 continuity/replacement/fallback baseline: `docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE-v1.0.0.md`
- Formal review evidence: `docs/reviews/`
- Durable Owner/governance decisions: `docs/governance/decisions/`

## Current Company state

`M0 — Company canonically founded` and `M1 — Business/economic reality and first market-validation plan captured` are `Complete / PASS`.

Phase 2 now has a complete operating-model chain through continuity governance:

```text
AC-201 functions
→ AC-202 Reserved Owner Decisions
→ AC-203 delegated Position authority semantics
→ AC-204 Initial Position Registry
→ AC-205 Assignments / executor classification
→ AC-206 access boundary
→ AC-207 continuity / replacement / fallback
→ AC-208 transferability / operating-model closure review
```

`AC-207 — Critical-function continuity, replacement and manual fallback baseline` is `Complete / PASS` after `9/10` cross-review iterations and explicit Owner approval.

The binding AC-207 baseline establishes five continuity modes (`CM-0` through `CM-4`) and four evidence states (`CE-0` through `CE-3`). It preserves the principle that continuity is not a bypass: runtime replacement, device recovery, mirror use or emergency operation do not transfer Organizational Authority, customer rights or legal/corporate powers.

Key operating implications:

- the current Owner human Principal remains a real continuity concentration for POS-001, POS-002, POS-003, POS-005 and POS-006; AI support does not make those Positions Owner-independent;
- `POS-004 — Engineering & Release Lead` is designed so a specific AI model/agent/runtime can be replaced without redefining the Position, but a new Principal still requires explicit Assignment/access;
- future sellers do not become active automatically during Owner absence;
- outsourced accounting may continue only inside its professional/contractual contour and does not inherit Company spending or management authority;
- GitVerse/local clones can preserve bounded work/history during GitHub outage but do not become canonical automatically;
- missing signing, bank/payment, legal/customer-rights or trusted-state gates may correctly force fail-closed behavior;
- the approved baseline deliberately records unresolved/untested continuity areas rather than claiming disaster-recovery readiness.

The current canonical Company action is:

**`AC-208 — Reference-model transferability boundary and operating-model cross-review`**.

AC-208 will close Phase 2 by testing the full AC-201–AC-207 chain for internal coherence and by separating what is reusable as the Arvectum organization-design method from what is specific to ООО «Арвектум» and must not be copied mechanically into a customer's organization.

The bounded AC-108 design-partner discovery loop remains separately authorized P1 market-evidence work and does not imply a pilot, price, SLA, privileged access or customer commitment.

## Repository boundary

Company-specific governance and organizational semantics belong here when suitable for repository storage. Product implementation remains canonical in the corresponding product repository. Domain-neutral platform architecture and contracts belong in `arvectum/arvectum-os`.

This repository is public. Do **not** commit secrets, reusable credentials, unnecessary personal data, signatures, bank/payment details, non-public customer/supplier/contract material or other restricted operational payloads.

## Remotes

GitHub `arvectum/arvectum-company` is the canonical remote. GitVerse is a resilience/sovereignty mirror and is not an independent source of Organizational Authority.
