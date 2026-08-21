# Arvectum Company Portfolio

Status: `Active`
Version: `0.3.0`
Created: `2026-08-20`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Current governance baseline: `AC-302 — Approved 1.0.0`

## 1. Publication model

This `0.3.0` publication preserves the complete portfolio baseline `0.2.0` by immutable git blob reference and overlays the approved AC-302 accountable-Position mapping as the current Company-level accountability baseline.

Previous publication:

- version: `0.2.0`;
- path: `docs/portfolio/PORTFOLIO.md`;
- immutable git blob SHA: `43a53565daef8c319d2d6b5ffe0b73fcb1d4a56f`.

Approved AC-302 baseline:

- `docs/portfolio/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-MAPPING-v1.0.0.md` — `Approved 1.0.0`;
- exact reviewed proposal: `docs/portfolio/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-MAPPING.md` — `Proposed 0.9.0`, blob `29bec89402118ddfc061501b8b25f5c0000d65a4`;
- cross-review: `docs/reviews/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-CROSS-REVIEW.md` — `10 of maximum 10`, PASS;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-302-APPROVAL.md`.

The `0.2.0` AC-301 identity/boundary/disposition baseline remains fully in force except where this publication adds the accountable-Position relationship.

## 2. Current governed portfolio map

| ID | Primary Company-level name | Node type / state | Canonical repository | Disposition | Primary accountable Position |
|---|---|---|---|---|---|
| `PORT-001` | `Arvectum Tender Agent` | standalone product | `arvectum/tender-agent` | `continue` | `POS-003 — Portfolio & Product Lead` |
| `PORT-002` | `Discount Parser` | productized client solution / product | `arvectum/discount-parser` | `continue` | `POS-003 — Portfolio & Product Lead` |
| `PORT-003` | `Arvectum Proxy Launcher` | standalone product | `arvectum/proxy-launcher` | `continue` | `POS-003 — Portfolio & Product Lead` |
| `PORT-004` | `Creative Test Agent` | standalone product / controlled-pilot solution | `arvectum/creative-test-agent` | `continue` | `POS-003 — Portfolio & Product Lead` |
| `PORT-005` | `Tender Small-Volume Calculator` | contained product experiment | `arvectum/tender-app` | `contain` | `POS-003 — Portfolio & Product Lead` |
| `PORT-006` | `Doors Parser` | contained completed client-delivery/product experiment | `arvectum/doors_parser` | `contain` | `POS-003 — Portfolio & Product Lead` |
| `PORT-007` | `Data Platform` | internal initiative requiring definition | `arvectum/data-platform` | `clarify` | `POS-003 — Portfolio & Product Lead` |

## 3. Meaning of the accountable-Position relation

`PORT-* → POS-003` means Company-level accountability for portfolio stewardship of the node: identity/status/source-reference integrity, portfolio role/disposition visibility, preparation of evidence for continue/change/stop/reuse/investment decisions, and correct escalation.

It does **not** make POS-003 the end-to-end owner of every function of a product.

Functional accountability remains:

- `POS-002` — commercial/customer;
- `POS-004` — engineering/release;
- `POS-005` — finance/economics/obligations;
- `POS-006` — security/data/dependency/risk/continuity;
- `POS-001` — Company operating integration and escalation.

Product repositories remain canonical for product-specific implementation, status and roadmap. Arvectum OS remains canonical for OS Product Contracts/platform semantics. Customer authority remains customer-owned. Legal/IP rights remain evidenced by applicable legal/contractual sources.

## 4. Authority, Assignment, access and continuity boundaries

AC-302 does not alter:

- AC-202 `ROD-01…ROD-09` Reserved Owner Decisions;
- AC-203 authority semantics;
- POS-003 initial ceiling `AM-0/AM-1/AM-2`;
- AC-205 Assignments/executor realization;
- AC-206 access ceilings/provisioning rules;
- AC-207 continuity/replacement/fallback rules.

The current Owner Principal may execute POS-003 through the approved AC-205 Assignment, but the accountable relation belongs to the Position and survives replacement of Principal/runtime unless an approved organizational change states otherwise.

## 5. Contained and clarify nodes

For `PORT-005` and `PORT-006`, POS-003 acts as portfolio custodian and owner of the continue/merge/reuse/retire question. The mapping does not authorize growth investment or scope expansion.

For `PORT-007`, POS-003 owns preparation of the clarification/admission question: business problem, consumers, boundary, strategic/economic hypothesis and evidence. The mapping does not admit Data Platform as a product, module or OS capability by implication.

## 6. Downstream governance

The following remain unresolved by design and belong to subsequent Phase 3 work:

- `AC-303` — investment, cost and risk boundaries; continue/change/stop criteria;
- `AC-304` — standalone product / reference implementation / module candidate / Arvectum OS capability candidate classification;
- `AC-305` — inter-product dependencies and Arvectum OS Product Contract reconciliation, including the stale P6.02 repository locator;
- `AC-306` — portfolio prioritization by capital, economics and Owner attention.

## 7. Source-of-truth rule

This file is canonical for the current Company-level portfolio map and accountable-Position relationship. Its incorporated historical publications remain available by immutable blob reference.

If a product source conflicts with this file on implementation/status, the product source wins within product scope and this portfolio must be refreshed. If Company governance changes the identity, disposition or accountability relation, the later approved Company artifact wins within Company scope.
