# AC-202 — Reserved Owner Decisions

Status: `Approved`
Version: `1.0.0`
Approved: `2026-08-20`
Published: `2026-08-20`
Owner: `Owner of Arvectum Company`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-202 — Reserved Owner Decisions`
Approval: `docs/governance/decisions/DECISION-2026-08-20-AC-202-APPROVAL.md`
Cross-review: `docs/reviews/AC-202-RESERVED-OWNER-DECISIONS-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `eabe1cb14be7d4b4134b263831744c50ce9f77a0`

## 1. Approval publication

This document is the canonical Approved publication of AC-202 `1.0.0`.

The Owner-approved normative substance is the complete reviewed proposal preserved at:

`docs/governance/RESERVED-OWNER-DECISIONS.md`

and identified immutably by git blob SHA:

`eabe1cb14be7d4b4134b263831744c50ce9f77a0`

The proposal is incorporated into this Approved publication **in full by immutable content reference**. No normative substance of the reviewed proposal is changed by this publication.

Owner approval is recorded in:

`docs/governance/decisions/DECISION-2026-08-20-AC-202-APPROVAL.md`.

## 2. Approved model

AC-202 `1.0.0` establishes the binding Company-internal Reserved Owner Decision model defined by the incorporated reviewed proposal, including:

1. separation of legal/corporate authority, Company Organizational Authority and technical authorization;
2. three authority buckets: `Reserved Owner Decision`, `Delegable decision/action`, and `Temporary residual Owner authority` pending approved delegation;
3. the rule that `material` does not automatically mean permanently Owner-only;
4. the nine-class Reserved Owner Decision catalog:
   - `ROD-01` — Mission, strategic direction and business-model identity;
   - `ROD-02` — Capital allocation and material financial exposure;
   - `ROD-03` — Material external commitments and non-standard commercial exposure;
   - `ROD-04` — Major portfolio, initiative and investment decisions;
   - `ROD-05` — Company constitutional governance, authority architecture and material delegation;
   - `ROD-06` — Risk appetite and material exception acceptance;
   - `ROD-07` — Customer/data sovereignty and material reuse/disclosure exceptions;
   - `ROD-08` — Core IP, critical dependency and technology-sovereignty exceptions;
   - `ROD-09` — Material Company↔Product↔Arvectum OS boundary and cross-repository commitments;
5. explicit identification of decision/action classes that should normally become delegable after AC-203 defines safe authority envelopes;
6. reservation of decision gates rather than whole AC-201 functions;
7. consequence-based materiality without invented numeric thresholds;
8. a bounded Reserved Owner Decision preparation packet so the Owner need not reconstruct raw context;
9. explicit approval semantics: recommendation, silence, technical execution or workflow completion do not constitute Owner approval;
10. separation of Owner approval from post-approval execution mechanics;
11. AI/software participation in evidence preparation, cross-review and bounded post-decision execution without Organizational Authority;
12. emergency containment rules that permit pre-authorized reversible safety actions without delegating material risk acceptance;
13. preservation of Company/Product/Arvectum OS/customer authority boundaries;
14. the transferability rule that the catalog is reference evidence and method, not a fixed customer template;
15. a negative authority boundary for AC-203.

## 3. Legal and corporate boundary

This Approved Company governance artifact does not amend the legal charter of ООО «Арвектум» and does not create powers that applicable law, the charter, a participant decision, the General Director's competence, a power of attorney, contract, bank authorization or another valid source does not provide.

Where a decision falls both within a `ROD-*` class and a legally/corporately regulated competence, the applicable gates remain separate:

```text
internal Owner decision
+ required corporate/legal act
+ required technical/execution authorization
```

No one gate implies the others.

## 4. Company / Product / Arvectum OS / customer boundary

AC-202 governs only Arvectum Company internal Owner-reserved decision classes.

A Company portfolio or boundary decision does not rewrite product implementation authority. A Company Owner approval does not approve an Arvectum OS RFC, ADR, Product Contract or platform lifecycle transition. Customer organizational authority, customer data rights and customer approvals remain with the applicable customer authority and legal/contractual basis.

Arvectum OS may later represent or enforce this approved Company authority model where an admitted contract exists, but it does not create the authority represented by the model.

## 5. Downstream authority rule

AC-203 MUST treat the incorporated `ROD-*` catalog as a negative boundary.

AC-203 may define Position authority, approval and automatic-execution envelopes for non-reserved work, but it MUST NOT silently delegate a `ROD-*` final decision.

Any future change that would remove, narrow, broaden or reclassify a Reserved Owner Decision requires an explicit approved Company governance change under the applicable authority path.

## 6. Cross-review and approval evidence

Cross-review:

- `docs/reviews/AC-202-RESERVED-OWNER-DECISIONS-CROSS-REVIEW.md`;
- iterations: `9 of maximum 10`;
- result: `Complete / PASS for Owner approval`.

Approved proposal:

- `docs/governance/RESERVED-OWNER-DECISIONS.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `eabe1cb14be7d4b4134b263831744c50ce9f77a0`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-20-AC-202-APPROVAL.md` — `Approved`.

## 7. Approval result

`AC-202 — Reserved Owner Decisions` is `Complete / PASS` and binding as Company-internal governance within its declared scope.

The next canonical Company action is:

`AC-203 — Delegated Position authority, approval and escalation model`.
