# DECISION-2026-08-20 — AC-002 Company ↔ Arvectum OS Authority Boundary Approval

Status: `Approved`
Decision date: `2026-08-20`
Decision time: `08:42 +03:00`
Decision class: `Founding / Material Company Governance Boundary`
Decision authority: `Owner of Arvectum Company`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-002 — Company ↔ Arvectum OS authority and responsibility boundary`

## Decision

The Owner explicitly approved the exact proposal identified as:

- artifact: `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md`;
- proposal status/version: `Proposed 0.9.0`;
- approved proposal blob SHA: `faed6d8503dfe771b4505f02ff8fed23aa5e9cb0`;
- cross-review: `docs/reviews/AC-002-COMPANY-OS-AUTHORITY-BOUNDARY-CROSS-REVIEW.md`;
- cross-review result: `PASS — material consensus reached` after 7 of maximum 10 iterations.

Owner approval statement:

> Утверждаю AC-002 0.9.0

The proposal is therefore authorized for publication as `Approved 1.0.0` without changing its approved normative substance.

## Scope and authority effect

This decision approves the internal Company governance boundary between Arvectum Company and Arvectum OS.

It confirms, within Company governance scope, that:

- applicable legal/corporate authority remains distinct from Company Organizational Authority, OS governance authority, product governance and technical authorization;
- Arvectum OS may represent, constrain and execute Company authority under applicable contracts but does not create that authority merely through technical configuration or canonical persistence;
- Company-specific organizational semantics remain Company-owned, OS domain-neutral contracts remain OS-owned, and product/domain implementation semantics remain product-owned;
- cross-repository changes require the applicable governance/contract path in each affected repository;
- consequential Company reliance on OS must use admitted contracts, Governed Execution, appropriate approvals and fail-closed behavior where required;
- Company commercial commitments cannot silently create unsupported Arvectum OS lifecycle, compatibility, support or conformance obligations.

This approval does **not** amend the legal charter of ООО «Арвектум», create a power of attorney, alter the statutory competence of the participant or General Director, amend the Arvectum OS Constitution/RFCs, or approve any future OS change merely referenced by the boundary.

## Publication actions authorized

1. Publish `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md` as `Approved 1.0.0`, preserving the exact approved `Proposed 0.9.0` blob reference.
2. Preserve the seven-iteration AC-002 cross-review as review evidence and record this Owner approval as the subsequent binding decision.
3. Update `docs/CANONICAL-SOURCES.md` so the Company ↔ OS authority boundary and this approval record are canonical Company governance sources.
4. Update `docs/roadmap/ROADMAP.md` to close `AC-002` as `Complete / PASS` and advance `AC-003 — Canonical repository structure and artifact map` to `Current`.
5. Perform read-after-write verification and merge the AC-002 pull request.

## Approval result

`APPROVED — AC-002 1.0.0 AUTHORIZED FOR PUBLICATION`
