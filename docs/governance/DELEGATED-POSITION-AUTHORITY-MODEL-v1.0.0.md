# AC-203 — Delegated Position Authority, Approval and Escalation Model

Status: `Approved`
Version: `1.0.0`
Approved: `2026-08-20`
Published: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-203 — Delegated Position authority, approval and escalation model`
Approval: `docs/governance/decisions/DECISION-2026-08-20-AC-203-APPROVAL.md`
Cross-review: `docs/reviews/AC-203-DELEGATED-POSITION-AUTHORITY-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `ba89771f7b3ead7f70b0482f06d7d04bc68df2ea`

## 1. Approval publication

This document is the canonical Approved publication of AC-203 `1.0.0`.

The Owner-approved normative substance is the complete reviewed proposal preserved at:

`docs/governance/DELEGATED-POSITION-AUTHORITY-MODEL.md`

and identified immutably by git blob SHA:

`ba89771f7b3ead7f70b0482f06d7d04bc68df2ea`

The proposal is incorporated into this Approved publication **in full by immutable content reference**. No normative substance of the reviewed proposal is changed by this publication.

Owner approval is recorded in:

`docs/governance/decisions/DECISION-2026-08-20-AC-203-APPROVAL.md`.

## 2. Approved model

AC-203 `1.0.0` establishes the binding Company-internal delegated Position authority, approval and escalation semantics defined by the incorporated reviewed proposal, including:

1. Position authority is executor-neutral and survives replacement of the current human, AI, service, software or runtime;
2. an Assignment may narrow Position authority but cannot broaden it;
3. authority is deny-by-default and must not be inferred from job title, technical capability, system role, credentials, admin access, workflow participation or AI capability;
4. five authority modes:
   - `AM-0 — Prepare / Recommend`;
   - `AM-1 — Execute Pre-Decided Work`;
   - `AM-2 — Bounded Decision`;
   - `AM-3 — Delegated Approval`;
   - `AM-4 — Pre-Authorized Automatic Execution`;
5. AC-202 `ROD-01` through `ROD-09` remain a hard negative boundary and cannot be silently delegated;
6. practical delegation envelopes must declare permitted decision/action classes, excluded decisions, consequence/financial/customer/data/risk limits, review/expiry conditions and escalation path proportionate to scope;
7. effective executable scope is bounded by the intersection:

```text
Position authority envelope
∩ Assignment scope
∩ technical authorization/access
∩ current workflow/data/risk conditions
= maximum executable action
```

8. recommendation, analysis, technical execution or workflow completion do not constitute approval;
9. AI/software remain execution means rather than independent Organizational Authority sources;
10. where per-instance consequential approval is not intended, bounded automation should normally be represented as `AM-4` pre-authorized automatic execution rather than fictitious AI approval;
11. stale facts, missing/expired authority, exceeded limits, `ROD-*` entry, non-standard commitments, unclear customer rights, material exceptions, cross-repository obligations, irreversible consequences, authority/access mismatch and uncertain external effects require escalation or fail-closed behavior;
12. correct escalation is a successful fulfillment of a Position boundary rather than operator failure;
13. bounded reversible emergency containment may later be pre-authorized without delegating material risk acceptance;
14. parent/child tasks and technical execution chains do not inherit ambient authority;
15. delegation may be revoked, expire or require review without changing the enduring Position meaning;
16. AC-204 must now create concrete Positions using these semantics without treating one AC-201 function as automatically equal to one Position.

## 3. Legal and corporate boundary

This Approved Company governance artifact does not amend the legal charter of ООО «Арвектум» and does not create powers that applicable law, the charter, a participant decision, General Director competence, a power of attorney, contract, bank authorization or another valid source does not provide.

Internal Organizational Authority, legal/corporate authority and technical authorization remain separate gates.

A Position delegation cannot create legal authority the Company does not possess and cannot override customer authority, a binding contract, approved Product governance or applicable Arvectum OS contracts/governance.

## 4. AC-202 negative boundary

Approved AC-202 `ROD-01` through `ROD-09` remain reserved final Owner decisions unless AC-202 itself is explicitly amended and approved.

AC-203 therefore authorizes the **model for delegation**, not delegation of every consequential decision.

Concrete delegation records created later MUST identify applicable excluded `ROD-*` classes and MUST escalate when a case crosses those boundaries.

## 5. AI/software and automatic-execution boundary

AI/software may be assigned to work within a Position and may perform bounded decisions or automated execution when the governing delegation and workflow explicitly permit it.

Neither Assignment nor runtime capability creates authority by itself.

`AM-3 — Delegated Approval` requires explicit approver eligibility. AI/software are not sole consequential approvers merely because they occupy or execute a Position.

Where competent authority has pre-approved the action class, limits, evidence, data boundary, failure behavior and rollback/compensation path, `AM-4 — Pre-Authorized Automatic Execution` is the appropriate semantic model.

## 6. Downstream handoff

AC-204 may now create the Initial Position Registry.

For each proposed Position, AC-204 must derive the Position from real business responsibility, workload, control need or economic value and identify which AC-201 functions/responsibilities it carries.

AC-204 should reference the AC-203 authority semantics but MUST NOT by itself:

- assign a concrete human/AI/software Principal;
- create technical access or credentials;
- invent legal powers;
- silently grant a `ROD-*` decision;
- treat one function as requiring one Position by default.

Assignments remain AC-205, access remains AC-206, and continuity/replacement proof remains AC-207.

## 7. Cross-review and approval evidence

Cross-review:

- `docs/reviews/AC-203-DELEGATED-POSITION-AUTHORITY-CROSS-REVIEW.md`;
- iterations: `9 of maximum 10`;
- result: `Complete / PASS for Owner approval`.

Approved proposal:

- `docs/governance/DELEGATED-POSITION-AUTHORITY-MODEL.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `ba89771f7b3ead7f70b0482f06d7d04bc68df2ea`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-20-AC-203-APPROVAL.md` — `Approved`.

## 8. Approval result

`AC-203 — Delegated Position authority, approval and escalation model` is `Complete / PASS` and binding as Company-internal governance within its declared scope.

The next canonical Company action is:

`AC-204 — Initial Position Registry`.
