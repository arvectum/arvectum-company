# Arvectum Company Portfolio

Status: `Active`
Version: `0.2.0`
Created: `2026-08-20`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Current governance baseline: `AC-301 — Approved 1.0.0`

## 1. Publication model

This `0.2.0` publication preserves the complete initial portfolio map `0.1.0` by immutable git blob reference and overlays the approved AC-301 identity/boundary/organizational-ownership reconciliation as the current Company-level baseline.

Previous publication:

- version: `0.1.0`;
- path: `docs/portfolio/PORTFOLIO.md`;
- immutable git blob SHA: `8c5ed000ef6c89d25360ccb22f07720d7ec2c17c`.

Approved reconciliation:

- `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION-v1.0.0.md` — `Approved 1.0.0`;
- exact reviewed proposal: `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION.md` — `Proposed 0.9.0`, blob `146b5868a21c09cf20b633e309e587b7a631ad32`;
- cross-review: `docs/reviews/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-CROSS-REVIEW.md` — `10 of maximum 10`, PASS;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-301-APPROVAL.md`.

Where the old `0.1.0` map conflicts with the approved AC-301 baseline on Company-level identity, node type, repository locator, ownership interpretation or disposition, AC-301 prevails. Product repositories remain canonical for product-specific implementation/status/roadmaps; Arvectum OS remains canonical for OS Product Contracts and platform semantics.

## 2. Current governed portfolio map

| ID | Primary Company-level name | Current node type | Canonical implementation repository | Organizational owner | Disposition |
|---|---|---|---|---|---|
| `PORT-001` | `Arvectum Tender Agent` | standalone product | `arvectum/tender-agent` | ООО «Арвектум» as portfolio sponsor/product organizational owner; accountable Position pending AC-302 | `continue` |
| `PORT-002` | `Discount Parser` | productized client solution / product with client delivery contour | `arvectum/discount-parser` | ООО «Арвектум» as portfolio sponsor/product organizational owner; accountable Position pending AC-302 | `continue` |
| `PORT-003` | `Arvectum Proxy Launcher` | standalone product | `arvectum/proxy-launcher` | ООО «Арвектум» as portfolio sponsor/product organizational owner; accountable Position pending AC-302 | `continue` |
| `PORT-004` | `Creative Test Agent` | standalone product / controlled-pilot solution | `arvectum/creative-test-agent` | ООО «Арвектум» as portfolio sponsor/product organizational owner; accountable Position pending AC-302 | `continue` |
| `PORT-005` | `Tender Small-Volume Calculator` | product experiment / local procurement MVP | `arvectum/tender-app` | ООО «Арвектум» as sponsor of the existing experiment asset; no new Assignment created by AC-301 | `contain` |
| `PORT-006` | `Doors Parser` | client-delivery solution / completed product experiment | `arvectum/doors_parser` | ООО «Арвектум» as organizational sponsor/portfolio-node holder; legal/IP boundaries remain separately evidenced | `contain` |
| `PORT-007` | `Data Platform` | internal initiative at definition stage | `arvectum/data-platform` | ООО «Арвектум» as initiative sponsor; product/Position authority not yet inferred | `clarify` |

## 3. Identity rule

`PORT-*` is the stable Company-level identity of a portfolio node. Repository names, repository moves, marketing names, historical aliases and OS Product Contract identities do not create a second Company product automatically.

A new `PORT-*` is required only when a genuinely new independent object of investment/accountability is created.

## 4. Boundary rule

For all nodes:

- Company owns portfolio sponsorship, strategic/investment direction and Company-level governance within approved authority;
- the product repository owns product-specific domain semantics, implementation, product roadmap and product operational/release evidence;
- Arvectum OS owns only its domain-neutral platform semantics, Product Contracts, capability lifecycle and governed platform behavior;
- technical access, GitHub ownership/admin status, AI execution or Product Contract possession does not create Organizational Authority;
- Company-level organizational ownership does not prove legal/IP title, customer-data rights or contractual rights.

## 5. Approved reconciliation conclusions

1. `PORT-001` and `PORT-005` remain separate identities. Domain overlap does not authorize a silent merge.
2. OS P6.02 still contains the historical locator `arutyunoveth/ai-corporation`; the current implementation repository is `arvectum/tender-agent`. The OS artifact must be reconciled through AC-305 and applicable Arvectum OS governance, preserving lineage.
3. `Discount Parser`, `Doors Parser` and `Data Platform` do not automatically form `Universal Parser`, `Arvectum Parser`, a reusable module or an OS capability.
4. `Creative Test Agent` remains the current product identity; `Marketing Agent` is not the current product identity without a separate product-scope decision.
5. `Data Platform` receives no Product/OS/platform authority merely from its repository name.

## 6. Disposition semantics

- `continue` — identity and current boundary are sufficient for bounded work; no budget/priority conclusion follows.
- `contain` — preserve the asset and current bounded scope, but do not expand it into a strategic-growth product or module without a later decision.
- `clarify` — resolve business hypothesis, consumers and boundary before the next material investment step.
- `retire candidate` — candidate for later stop/archive decision; no node currently has this state under AC-301.

These states are not substitutes for AC-303 investment limits or AC-306 prioritization.

## 7. Current Product Contract / OS reliance notes

The initial `0.1.0` OS-reliance map remains valid except as explicitly reconciled here:

- `PORT-001` Tender Agent: P6.02 remains `Provisional 0.1.0`; its stale repository locator is a known reconciliation defect, not a second product identity.
- `PORT-002` Discount Parser: P6.06 remains the currently evidenced Provisional OS Product Contract boundary; it does not transfer parser-domain semantics into Arvectum OS.
- no other node receives inferred OS reliance merely from this portfolio publication.

## 8. Next governance action

AC-301 is `Complete / PASS`.

Next canonical portfolio action:

`AC-302 — Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой`.

AC-302 must assign accountability using the approved M2 Position model or explicitly justify a Position-registry change; it must not infer authority from repository ownership or current executor identity.

## 9. Refresh triggers

Refresh this portfolio when materially affected by:

- creation, merge, rename, sale, containment, stop or retirement of a node;
- canonical repository relocation;
- accountable Position approval/change;
- AC-303 investment/stop criteria;
- AC-304 module/OS-candidate classification;
- AC-305 dependency/Product Contract reconciliation;
- AC-306 prioritization;
- Product Contract lifecycle change;
- material legal/IP/contractual boundary evidence that changes the organizational interpretation recorded here.
