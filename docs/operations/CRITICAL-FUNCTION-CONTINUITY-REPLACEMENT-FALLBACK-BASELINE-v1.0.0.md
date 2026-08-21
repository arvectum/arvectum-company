# AC-207 — Critical-Function Continuity, Replacement and Manual Fallback Baseline

Status: `Approved`
Version: `1.0.0`
Approved: `2026-08-21`
Published: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-207 — Critical-function continuity, replacement and manual fallback baseline`
Approval: `docs/governance/decisions/DECISION-2026-08-21-AC-207-APPROVAL.md`
Cross-review: `docs/reviews/AC-207-CRITICAL-FUNCTION-CONTINUITY-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `425ab4d83098aa3dbc73925305aa5d9981512818`

## 1. Approval publication

This document is the canonical Approved publication of AC-207 `1.0.0`.

The Owner-approved normative substance is the complete reviewed proposal preserved at:

`docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE.md`

and identified immutably by git blob SHA:

`425ab4d83098aa3dbc73925305aa5d9981512818`

The proposal is incorporated into this Approved publication **in full by immutable content reference**. No normative substance of the reviewed proposal is changed by this publication.

Owner approval is recorded in:

`docs/governance/decisions/DECISION-2026-08-21-AC-207-APPROVAL.md`.

## 2. Approved continuity model

AC-207 `1.0.0` establishes the binding Company continuity baseline for the six approved Positions and their material dependencies.

The governing invariant is:

```text
continuity ≠ bypass
replacement ≠ authority transfer
technical recovery ≠ business approval
mirror availability ≠ canonical promotion
manual fallback ≠ assumed human competence
```

The approved continuity modes are:

- `CM-0 — Normal`;
- `CM-1 — Bounded Continuity`;
- `CM-2 — Degraded`;
- `CM-3 — Fail Closed`;
- `CM-4 — Recovery / Reconciliation`.

The approved continuity evidence states are:

- `CE-0 — Unresolved`;
- `CE-1 — Defined / Untested`;
- `CE-2 — Operational Evidence Exists`;
- `CE-3 — Tested and Reviewed`.

No fallback is treated as tested merely because it is designed or plausible.

## 3. Position continuity boundary

The approved baseline preserves the AC-205 executor model:

- `POS-001 — Company Executive`: AI/runtime loss normally degrades to human operation; Owner/human absence does not transfer human `AM-2`, `ROD-*`, participant or General Director authority to AI;
- `POS-002 — Commercial & Customer Lead`: bounded pre-authorized mechanics may continue when evidence exists, but new material commitments, ambiguous scope/acceptance decisions and unsupported customer promises stop or queue;
- `POS-003 — Portfolio & Product Lead`: AI may continue evidence preparation during Owner absence but may not independently start/stop products, allocate material capital or redefine Company↔Product↔OS boundaries;
- `POS-004 — Engineering & Release Lead`: a specific AI model/agent/runtime is replaceable; runtime replacement is distinct from Principal replacement, and human fallback requires explicit Assignment and least-privilege access;
- `POS-005 — Finance & Obligation Control Lead`: accounting-provider work may continue inside its contracted professional contour, but payment, management-finance judgment and Owner-reserved authority do not transfer; unverifiable facts remain uncertain rather than fabricated;
- `POS-006 — Security, Risk & Continuity Lead`: AI may continue analysis but does not inherit material risk acceptance, security administration, sovereignty-exception or Owner authority.

## 4. Dependency and recovery boundary

GitHub remains the canonical Company remote under the current approved repository model. GitVerse/local clones may preserve bounded work/history during outage but do not become canonical automatically. Divergent state requires explicit `CM-4` reconciliation.

Product implementation truth remains product-owned. Company continuity does not recreate product implementation state in the Company repository.

Arvectum OS unavailability does not invalidate Company governance. Only workflows actually dependent on an admitted OS contract are affected, and their fallback remains subject to the applicable Product/OS semantics.

Missing or uncertain bank, signing, legal, customer-rights, trusted-state or security gates may legitimately force `CM-3 — Fail Closed`.

Customer/workstream data recovery must preserve organization scope, purpose, classification, retention/deletion and customer-rights boundaries.

## 5. Minimum continuity packet

Material workstreams should remain reconstructable without one Owner memory, one AI session or one device. The approved proposal defines a minimum continuity packet including current scope/exclusions, authoritative decision references, status/next safe action, commitments/obligations, canonical source pointers, data-rights constraints, required access classes, unresolved risks, stop conditions and pending decisions.

The packet may be distributed across canonical systems. AC-207 does not authorize copying restricted customer, financial or credential values into the public Company repository.

## 6. Current readiness honesty

Approval of AC-207 does not claim production-grade continuity or disaster-recovery readiness.

Material current gaps remain explicitly unresolved or untested, including:

- replacement human continuity for Owner-held Positions;
- extended Owner/legal-representation continuity;
- Company-wide credential rotation/recovery/revocation evidence;
- GitHub/GitVerse/local restore and reconciliation exercise;
- actual POS-004 AI-runtime swap evidence;
- local machine re-bootstrap evidence;
- customer continuity packet / seller-operator handoff evidence;
- accounting-provider replacement evidence;
- dedicated commercial sender/CRM failover evidence;
- signing certificate/token replacement evidence;
- customer-data backup/restore/expiry evidence.

These gaps are future implementation/test requirements, not permission to bypass the approved continuity boundary.

## 7. Authority boundary

AC-207 does not create authority, legal power, customer consent, credentials, alternate providers or automated consequential approval.

Approved AC-202 `ROD-01` through `ROD-09`, AC-203 authority semantics, AC-204 Position meaning, AC-205 Assignments and AC-206 access ceilings remain controlling.

A replacement runtime, device, technical administrator, mirror or service provider does not inherit authority by availability or urgency.

## 8. Cross-review and approval evidence

Cross-review:

- `docs/reviews/AC-207-CRITICAL-FUNCTION-CONTINUITY-CROSS-REVIEW.md`;
- iterations: `9 of maximum 10`;
- result: `Complete / PASS for Owner approval`.

Approved proposal:

- `docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `425ab4d83098aa3dbc73925305aa5d9981512818`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-21-AC-207-APPROVAL.md` — `Approved`.

## 9. Approval result

`AC-207 — Critical-function continuity, replacement and manual fallback baseline` is `Complete / PASS` and binding as Company continuity governance within its declared scope.

The next canonical Company action is:

`AC-208 — Reference-model transferability boundary and operating-model cross-review`.
