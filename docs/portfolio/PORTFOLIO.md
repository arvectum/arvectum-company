# Arvectum Company Portfolio

Status: `Active`
Version: `0.5.0`
Created: `2026-08-20`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Current governance baseline: `AC-304 — Approved 1.0.0`

## 1. Publication model

This `0.5.0` publication preserves the complete portfolio baseline `0.4.0` by immutable git blob reference and overlays the approved AC-304 portfolio-role classification as the current Company-level role/reuse baseline.

Previous publication:

- version: `0.4.0`;
- path: `docs/portfolio/PORTFOLIO.md`;
- immutable git blob SHA: `c8906a139833dfe76915f976260e2949a718f118`.

Approved AC-304 baseline:

- `docs/portfolio/AC-304-PORTFOLIO-ROLE-CLASSIFICATION-v1.0.0.md` — `Approved 1.0.0`;
- exact reviewed proposal: `docs/portfolio/AC-304-PORTFOLIO-ROLE-CLASSIFICATION.md` — `Proposed 0.9.0`, blob `533ccef1d28bf9a154da9b99dd1c4226c19d166b`;
- cross-review: `docs/reviews/AC-304-PORTFOLIO-ROLE-CLASSIFICATION-CROSS-REVIEW.md` — `10 of maximum 10`, PASS, blob `94c70f2d9f168f54e4d4f948b754b22d177872ec`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-304-APPROVAL.md`.

The approved AC-301 identity/boundary/disposition baseline, AC-302 accountable-Position mapping and AC-303 investment/cost/risk treatment remain fully in force.

## 2. Current governed portfolio map

| ID | Primary Company-level name | Disposition | Primary accountable Position | Standalone product | Reference implementation | Company/product-family module candidate | Company-side OS capability candidate |
|---|---|---|---|---|---|---|---|
| `PORT-001` | `Arvectum Tender Agent` | `continue` | `POS-003 — Portfolio & Product Lead` | `YES` | `YES — RI-OS-CONSUMER` | `NO` | `NO` |
| `PORT-002` | `Discount Parser` | `continue` | `POS-003 — Portfolio & Product Lead` | `YES` | `YES — RI-OS-CONSUMER + RI-PRODUCT-FAMILY` | `NO` | `NO` |
| `PORT-003` | `Arvectum Proxy Launcher` | `continue` | `POS-003 — Portfolio & Product Lead` | `YES` | `NO` | `NO` | `NO` |
| `PORT-004` | `Creative Test Agent` | `continue` | `POS-003 — Portfolio & Product Lead` | `YES` | `YES — RI-OS-CONSUMER` | `NO` | `NO` |
| `PORT-005` | `Tender Small-Volume Calculator` | `contain` | `POS-003 — Portfolio & Product Lead` | `NO` | `YES — RI-PRODUCT-FAMILY` | `NO` | `NO` |
| `PORT-006` | `Doors Parser` | `contain` | `POS-003 — Portfolio & Product Lead` | `NO` | `YES — RI-PRODUCT-FAMILY` | `NO` | `NO` |
| `PORT-007` | `Data Platform` | `clarify` | `POS-003 — Portfolio & Product Lead` | `NO` | `NO` | `YES — clarification-only candidate` | `NO` |

## 3. Meaning of the AC-304 role columns

`Standalone product` describes product identity and lifecycle. It does not by itself authorize growth investment, production launch or customer commitments.

`Reference implementation` describes an evidence/reuse role. `RI-OS-CONSUMER` means a real product-side consumer/reference contour used to validate Arvectum OS through an explicit Product Contract or external-consumer boundary. `RI-PRODUCT-FAMILY` means a product-family evidence source from which reusable patterns may be extracted after proper review. Reference status does not turn the full repository into a template, shared library or standard.

`Company/product-family module candidate` is a Company-level hypothesis for a reusable mechanism above individual products and below Arvectum OS. Candidate status is not implementation authorization.

`Company-side OS capability candidate` is only a Company-side promotion hypothesis. It is not Arvectum OS lifecycle `Candidate`. In the current baseline every `PORT-*` is `NO` in this column.

## 4. Approved reuse conclusions

- `PORT-001`, `PORT-002` and `PORT-004` are real Arvectum OS reference consumers without transferring their product-domain semantics into the OS.
- `PORT-002`, `PORT-005` and `PORT-006` provide parser/data-acquisition or product-family reuse evidence, but they do not automatically form one generic parser/module/platform.
- `PORT-005` and `PORT-006` remain contained; reference status creates no growth mandate.
- `PORT-007` is only a clarification-only candidate for a bounded Company/product-family data acquisition/extraction module hypothesis. Its name does not grant platform status.
- No new Arvectum OS Platform Capability candidate is created by AC-304.

## 5. AC-303 investment treatment remains binding

AC-304 role classification does not replace AC-303. The current investment treatments remain:

| ID | AC-303 treatment |
|---|---|
| `PORT-001` | bounded continuation; material capital/customer/risk expansion requires evidence and Owner gate |
| `PORT-002` | complete/maintain accepted client/product contour; material new recurring cost or scope expansion requires review |
| `PORT-003` | bounded productization on verified track; material signing/dependency/market commitments remain gated |
| `PORT-004` | bounded controlled-pilot/productization; material customer/data/operational expansion requires review |
| `PORT-005` | maintenance/evidence preservation/reuse assessment only; no growth investment without explicit review |
| `PORT-006` | preserve support/completed-delivery/reuse evidence; no product growth by implication |
| `PORT-007` | clarify before investment; no build/funding/platform status by implication |

## 6. Authority and source-of-truth boundary

AC-304 does not alter `ROD-*`, delegated-authority semantics, Assignments, access ceilings, continuity rules or the AC-302 `PORT-* → POS-003` stewardship mapping.

Product repositories remain canonical for product-specific implementation, technical status and product roadmaps. Arvectum OS remains canonical for Product Contracts, Platform Capability lifecycle and platform semantics. Legal/IP/data rights and customer authority are determined by applicable legal/contractual evidence, not by this portfolio map.

A Company classification cannot silently create an Arvectum OS lifecycle state, Product Contract, cross-repository code/data transfer, budget or customer commitment.

## 7. Downstream governance

The following remain unresolved by design:

- `AC-305` — inter-product dependencies and Arvectum OS Product Contract reconciliation, including the stale P6.02 repository locator `arutyunoveth/ai-corporation`;
- `AC-306` — portfolio prioritization by capital, economics and Owner attention;
- `AC-307` — final portfolio-governance review and M3 closure.

## 8. Source-of-truth rule

This file is canonical for the current Company-level portfolio map, accountable-Position relationship, AC-303 investment treatment and approved AC-304 role/reuse classification. Historical publications remain available by immutable blob reference.

If a product source conflicts with this file on implementation/status, the product source wins within product scope and this portfolio must be refreshed. If Arvectum OS sources conflict on Product Contract or capability lifecycle, the OS source wins within platform scope. Later approved Company governance supersedes this file only within Company scope.
