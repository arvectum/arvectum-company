# Arvectum Company Portfolio

Status: `Active`
Version: `0.4.0`
Created: `2026-08-20`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Current governance baseline: `AC-303 — Approved 1.0.0`

## 1. Publication model

This `0.4.0` publication preserves the complete portfolio baseline `0.3.0` by immutable git blob reference and overlays the approved AC-303 Company-level investment/cost/risk treatment as the current portfolio-governance baseline.

Previous publication:

- version: `0.3.0`;
- path: `docs/portfolio/PORTFOLIO.md`;
- immutable git blob SHA: `c0dfba93386a8b8b4e31ee82a046a21cb729f5d2`.

Approved AC-303 baseline:

- `docs/portfolio/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-BOUNDARIES-v1.0.0.md` — `Approved 1.0.0`;
- exact reviewed proposal: `docs/portfolio/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-BOUNDARIES.md` — `Proposed 0.9.0`, blob `e246d06e87b4221ad85718d2aeeb4e3486bf388e`;
- cross-review: `docs/reviews/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-CROSS-REVIEW.md` — `10 of maximum 10`, PASS;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-303-APPROVAL.md`.

The approved AC-301 identity/boundary/disposition baseline and AC-302 accountable-Position mapping remain fully in force except where AC-303 adds investment/cost/risk treatment and review semantics.

## 2. Current governed portfolio map

| ID | Primary Company-level name | Node type / state | Canonical repository | Disposition | Primary accountable Position | AC-303 investment treatment |
|---|---|---|---|---|---|---|
| `PORT-001` | `Arvectum Tender Agent` | standalone product | `arvectum/tender-agent` | `continue` | `POS-003 — Portfolio & Product Lead` | bounded continuation; material capital/customer/risk expansion requires evidence and Owner gate |
| `PORT-002` | `Discount Parser` | productized client solution / product | `arvectum/discount-parser` | `continue` | `POS-003 — Portfolio & Product Lead` | complete/maintain accepted client/product contour; material new recurring cost or scope expansion requires review |
| `PORT-003` | `Arvectum Proxy Launcher` | standalone product | `arvectum/proxy-launcher` | `continue` | `POS-003 — Portfolio & Product Lead` | bounded productization on verified track; material signing/dependency/market commitments remain gated |
| `PORT-004` | `Creative Test Agent` | standalone product / controlled-pilot solution | `arvectum/creative-test-agent` | `continue` | `POS-003 — Portfolio & Product Lead` | bounded controlled-pilot/productization; material customer/data/operational expansion requires review |
| `PORT-005` | `Tender Small-Volume Calculator` | contained product experiment | `arvectum/tender-app` | `contain` | `POS-003 — Portfolio & Product Lead` | maintenance/evidence preservation/reuse assessment only; no growth investment without explicit review |
| `PORT-006` | `Doors Parser` | contained completed client-delivery/product experiment | `arvectum/doors_parser` | `contain` | `POS-003 — Portfolio & Product Lead` | preserve support/completed-delivery/reuse evidence; no product growth by implication |
| `PORT-007` | `Data Platform` | internal initiative requiring definition | `arvectum/data-platform` | `clarify` | `POS-003 — Portfolio & Product Lead` | clarify before investment; no build/funding/platform status by implication |

## 3. AC-303 investment/cost/risk rule

AC-303 adds a Company-level evidence and review layer; it does not create budgets or automatically authorize spending.

For each portfolio node, decision preparation must make visible, where applicable:

- cash and recurring cost;
- engineering and operational effort;
- Owner-attention exposure and bottleneck risk;
- customer commitments and delivery obligations;
- security, privacy, data and access exposure;
- legal/IP and technology-sovereignty concerns;
- critical dependencies and replacement path;
- continuity and recovery implications;
- opportunity cost and downside/reversibility.

Unknown cost or risk is not interpreted as zero. Missing material evidence is a reason to obtain evidence or escalate, not a basis for automatic continuation.

## 4. Decision semantics

`continue` means continuation inside an already approved bounded envelope. It does not mean automatic funding, hiring, external commitment, production deployment or scope expansion.

`change` means a material change proposal must be prepared because evidence shows the current envelope, architecture, commercial contour, risk treatment or execution path should be altered.

`contain` means preserve obligations, evidence, reusable assets and necessary maintenance while preventing unapproved growth. It does not mean delete, abandon customers, rewrite history or destroy potentially valuable assets.

`stop / retire candidate` means prepare a decision packet for explicit competent approval. No technical test, repository inactivity, AI recommendation or sunk-cost argument alone is sufficient to terminate a material node.

## 5. Authority and functional-accountability boundary

AC-303 does not alter:

- AC-202 `ROD-01…ROD-09` Reserved Owner Decisions;
- AC-203 delegated-authority semantics and deny-by-default rule;
- AC-204 Position Registry;
- AC-205 Assignments;
- AC-206 access ceilings;
- AC-207 continuity/replacement/fallback rules;
- AC-302 `PORT-* → POS-003` Company-level stewardship mapping.

Functional evidence remains distributed:

- `POS-002` — customer/commercial evidence;
- `POS-004` — engineering/release evidence;
- `POS-005` — finance/economics/obligation evidence;
- `POS-006` — security/data/dependency/risk/continuity evidence;
- `POS-001` — Company operating integration and escalation;
- `POS-003` — portfolio stewardship and decision-packet preparation.

Material capital allocation/exposure, major portfolio/investment decisions, material risk acceptance, technology-sovereignty exceptions and material Company↔Product↔Arvectum OS commitments remain applicable Owner gates under `ROD-02`, `ROD-04`, `ROD-06`, `ROD-08`, `ROD-09` and other relevant `ROD-*` classes.

## 6. Source-of-truth and scope boundary

Product repositories remain canonical for product-specific implementation, technical status and product roadmaps. Arvectum OS remains canonical for OS Product Contracts/platform semantics. Legal/IP/data rights remain determined by applicable legal/contractual evidence. Customer authority remains customer-owned.

Technical `PASS`, a green CI run, deployment success, code volume, repository activity or previous expenditure do not prove profitability, legal compliance, customer readiness, security readiness or a Company investment decision.

## 7. Downstream governance

The following remain unresolved by design and belong to subsequent Phase 3 work:

- `AC-304` — standalone product / reference implementation / module candidate / Arvectum OS capability candidate classification;
- `AC-305` — inter-product dependencies and Arvectum OS Product Contract reconciliation, including the stale P6.02 repository locator;
- `AC-306` — portfolio prioritization by capital, economics and Owner attention;
- `AC-307` — final portfolio-governance review and M3 closure.

## 8. Source-of-truth rule

This file is canonical for the current Company-level portfolio map, accountable-Position relationship and approved AC-303 investment/cost/risk treatment. Its incorporated historical publications remain available by immutable blob reference.

If a product source conflicts with this file on implementation/status, the product source wins within product scope and this portfolio must be refreshed. If later approved Company governance changes identity, disposition, accountability or investment treatment, the later approved Company artifact wins within Company scope.
