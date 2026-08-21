# Arvectum Company Portfolio

Status: `Active`
Version: `0.6.0`
Created: `2026-08-20`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Current governance baseline: `AC-305 — Approved 1.0.0`

## 1. Publication model

This `0.6.0` publication preserves the complete portfolio baseline `0.5.0` by immutable git blob reference and overlays the approved AC-305 cross-product dependency / Arvectum OS Product Contract reconciliation as the current dependency-contract baseline.

Previous publication:

- version: `0.5.0`;
- path: `docs/portfolio/PORTFOLIO.md`;
- immutable git blob SHA: `09f2a7f07ede40d5beee976f331f13b5ebd889e2`.

Approved AC-305 baseline:

- `docs/portfolio/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-RECONCILIATION-v1.0.0.md` — `Approved 1.0.0`;
- exact reviewed proposal: `docs/portfolio/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-RECONCILIATION.md` — `Proposed 0.9.0`, blob `c27973c48b7bb5306e36f71d0f1007fc41896de9`;
- cross-review: `docs/reviews/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-CROSS-REVIEW.md` — `7 of maximum 7`, PASS, blob `369c42f8066ac8a10d3b00a0afd2fc034b8c7fe3`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-305-APPROVAL.md`.

The approved AC-301 identity/disposition baseline, AC-302 accountable-Position mapping, AC-303 investment treatment and AC-304 role/reuse classification remain fully in force.

## 2. Current governed portfolio map

| ID | Primary Company-level name | Canonical repository | Disposition | Primary accountable Position | Standalone / reference role | Current hard inter-product dependency |
|---|---|---|---|---|---|---|
| `PORT-001` | `Arvectum Tender Agent` | `arvectum/tender-agent` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone + `RI-OS-CONSUMER` | none evidenced |
| `PORT-002` | `Discount Parser` | `arvectum/discount-parser` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone + `RI-OS-CONSUMER` + `RI-PRODUCT-FAMILY` | none evidenced |
| `PORT-003` | `Arvectum Proxy Launcher` | `arvectum/proxy-launcher` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone only | none evidenced |
| `PORT-004` | `Creative Test Agent` | `arvectum/creative-test-agent` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone + `RI-OS-CONSUMER` | none evidenced |
| `PORT-005` | `Tender Small-Volume Calculator` | `arvectum/tender-app` | `contain` | `POS-003 — Portfolio & Product Lead` | `RI-PRODUCT-FAMILY` | none; selective reference reuse into PORT-001 only |
| `PORT-006` | `Doors Parser` | `arvectum/doors_parser` | `contain` | `POS-003 — Portfolio & Product Lead` | `RI-PRODUCT-FAMILY` | none evidenced |
| `PORT-007` | `Data Platform` | `arvectum/data-platform` | `clarify` | `POS-003 — Portfolio & Product Lead` | clarification-only Company/product-family module candidate | none; not an operational dependency |

## 3. Approved inter-product dependency conclusions

No mandatory hard runtime/code/data dependency is currently established between `PORT-001…PORT-007`.

Approved relationship interpretation:

- `PORT-005 → PORT-001` is selective procurement-family reuse/evidence, not runtime coupling or a product merge;
- `PORT-002 + PORT-006` provide parser/data-acquisition family evidence but do not form a shared parser runtime/datastore automatically;
- `PORT-007` remains a clarification-only module hypothesis and must not become a hidden shared operational dependency before its explicit admission/economic/ownership review;
- `PORT-003` is not inferred to be Company-wide or OS infrastructure merely because its networking/release patterns may be useful;
- common owner, common technology stack, code similarity and reference status do not create a dependency contract.

## 4. Current Arvectum OS Product Contract / integration map

| Portfolio node | Governed OS boundary | Exact current platform dependency | Core-product OS mandatory? |
|---|---|---|---|
| `PORT-001 — Arvectum Tender Agent` | `P6.02 — Provisional 0.1.0`; supplemental `P8.03 — Provisional 0.1.0` | `CAP-001 + CAP-004` in exact bounded scopes | only for the governed contours declared by those contracts; not a blanket product-wide inference |
| `PORT-002 — Discount Parser` | `P6.06 — Provisional 0.1.0` | `CAP-004 only` | no blanket product-wide inference |
| `PORT-004 — Creative Test Agent` | `P8.06 — Provisional 0.1.0`, optional external extension | `CAP-004 only` | no; optional extension remains separately enableable/disableable |
| `PORT-003` | none evidenced | none inferred | no |
| `PORT-005` | none evidenced | none inferred | no |
| `PORT-006` | none evidenced | none inferred | no |
| `PORT-007` | none evidenced | none inferred | no |

`RI-OS-CONSUMER` is an evidence/reuse classification. It is not a statement that Arvectum OS is required for every core-product operation or that a product implements/owns an OS capability.

## 5. P6.02 locator reconciliation

P6.02 historically names `arutyunoveth/ai-corporation`. The approved Company identity map establishes `arvectum/tender-agent` as the current canonical implementation repository for `PORT-001`.

The conflict is now reconciled through the proper Arvectum OS governance path:

- OS approved publication: `arvectum/arvectum-os/docs/contracts/P6-02-REPOSITORY-LOCATOR-RECONCILIATION-v1.0.0.md`;
- OS Owner decision: `arvectum/arvectum-os/docs/governance/decisions/DECISION-2026-08-21-P6-02-REPOSITORY-LOCATOR-RECONCILIATION-APPROVAL.md`;
- historical locator remains `arutyunoveth/ai-corporation`;
- current implementation locator is `arvectum/tender-agent`;
- P6.02 Product Identity, semantic boundary, dependency set and lifecycle remain unchanged at `Provisional 0.1.0`.

No artificial P8.03 version cascade is created because only locator/provenance metadata changed.

## 6. Investment and authority boundaries remain binding

AC-305 does not replace AC-303 or create a priority order. Existing treatment remains:

- `PORT-001` — bounded continuation; material capital/customer/risk expansion requires evidence and Owner gate;
- `PORT-002` — complete/maintain accepted client/product contour; material recurring cost or scope expansion requires review;
- `PORT-003` — bounded productization; material signing/dependency/market commitments remain gated;
- `PORT-004` — bounded controlled-pilot/productization; material customer/data/operational expansion requires review;
- `PORT-005` — maintenance/evidence preservation/reuse assessment only;
- `PORT-006` — support/completed-delivery/reuse evidence only;
- `PORT-007` — clarify before investment; no build/funding/platform status by implication.

`ROD-*`, delegated authority, Assignments, access, continuity, legal/IP/data rights and customer authority are not altered by this dependency reconciliation.

## 7. Source-of-truth rule

This file is canonical for the current Company-level portfolio map and approved Company interpretation of inter-product dependencies and OS reliance.

Product repositories remain canonical for product implementation/status/domain semantics. Arvectum OS remains canonical for Product Contracts, platform capabilities and OS dependency semantics. If later OS contract evidence changes, this portfolio must be refreshed rather than overriding OS from Company scope.

## 8. Downstream governance

`AC-305 — Complete / PASS`.

Next canonical portfolio action:

`AC-306 — Приоритизация портфеля по капиталу, экономике и вниманию собственника`.

AC-306 may rank investment and Owner attention but must not reinterpret the dependency/contract boundaries established here without new evidence and applicable governance.
