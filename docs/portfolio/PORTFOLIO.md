# Arvectum Company Portfolio

Status: `Active`
Version: `0.7.0`
Created: `2026-08-20`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Current governance baseline: `AC-306 — Approved 1.0.0`

## 1. Publication model

This `0.7.0` publication preserves the complete portfolio baseline `0.6.0` by immutable git blob reference and overlays the approved AC-306 capital/economics/Owner-attention prioritization as the current portfolio priority baseline.

Previous publication:

- version: `0.6.0`;
- path: `docs/portfolio/PORTFOLIO.md`;
- immutable git blob SHA: `c8243820fe1f7bd5acb817302c7332904c574459`.

Approved AC-306 baseline:

- `docs/portfolio/AC-306-PORTFOLIO-PRIORITIZATION-CAPITAL-ECONOMICS-OWNER-ATTENTION-v1.0.0.md` — `Approved 1.0.0`;
- exact reviewed proposal: `docs/portfolio/AC-306-PORTFOLIO-PRIORITIZATION-CAPITAL-ECONOMICS-OWNER-ATTENTION.md` — `Proposed 0.9.0`, blob `d254c6441baca5f22828648ecfa701d04c8344b1`;
- cross-review: `docs/reviews/AC-306-PORTFOLIO-PRIORITIZATION-CROSS-REVIEW.md` — `10 of maximum 10`, PASS, blob `329c87d6a63e08564e8b52362b8af02b159d7b74`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-306-APPROVAL.md`.

The approved AC-301 identity/disposition baseline, AC-302 accountable-Position mapping, AC-303 investment treatment, AC-304 role/reuse classification and AC-305 dependency/Product Contract reconciliation remain fully in force.

## 2. Current governed portfolio map

| ID | Primary Company-level name | Canonical repository | Disposition | Accountable Position | Role | AC-306 band |
|---|---|---|---|---|---|---|
| `PORT-001` | `Arvectum Tender Agent` | `arvectum/tender-agent` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone + `RI-OS-CONSUMER` | `A2` |
| `PORT-002` | `Discount Parser` | `arvectum/discount-parser` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone + `RI-OS-CONSUMER` + `RI-PRODUCT-FAMILY` | `A1` |
| `PORT-003` | `Arvectum Proxy Launcher` | `arvectum/proxy-launcher` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone only | `B1` |
| `PORT-004` | `Creative Test Agent` | `arvectum/creative-test-agent` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone + `RI-OS-CONSUMER` | `B2` |
| `PORT-005` | `Tender Small-Volume Calculator` | `arvectum/tender-app` | `contain` | `POS-003 — Portfolio & Product Lead` | `RI-PRODUCT-FAMILY` | `D1` |
| `PORT-006` | `Doors Parser` | `arvectum/doors_parser` | `contain` | `POS-003 — Portfolio & Product Lead` | `RI-PRODUCT-FAMILY` | `D2` |
| `PORT-007` | `Data Platform` | `arvectum/data-platform` | `clarify` | `POS-003 — Portfolio & Product Lead` | clarification-only Company/product-family module candidate | `C1` |

No mandatory hard runtime/code/data dependency is currently established between `PORT-001…PORT-007`; AC-305 remains authoritative for the exact relationship/Product Contract interpretation.

## 3. Approved default priority order

When no higher Company-level `P0` obligation exists, discretionary product attention follows:

```text
A1  PORT-002 — Discount Parser
A2  PORT-001 — Arvectum Tender Agent
    ↓
B1  PORT-003 — Arvectum Proxy Launcher
B2  PORT-004 — Creative Test Agent
    ↓
C1  PORT-007 — Data Platform
    ↓
D1  PORT-005 — Tender Small-Volume Calculator
D2  PORT-006 — Doors Parser
```

This is a decision order, not a permanent engineering queue, funding allocation or product-value ranking.

## 4. Current node treatments

### `A1 — PORT-002 — Discount Parser`

`finish / accept / stabilize / maintain`.

Prioritize bounded customer acceptance, defect correction, delivery continuity and clearly agreed support. After accepted delivery, default to maintenance/freeze unless new paid scope, second-consumer evidence or explicit product investment evidence justifies more work. Do not infer generic parser platformization.

### `A2 — PORT-001 — Arvectum Tender Agent`

Continue as bounded revenue/pilot/evidence product. Prefer quality, reliability and decision evidence tied to a specific qualified pilot/procurement opportunity/flagship hypothesis over broad feature accumulation. No mass pilot, SaaS, submission/EDS or autonomous consequential expansion by implication.

### `B1 — PORT-003 — Arvectum Proxy Launcher`

Preserve the verified productized baseline and perform trigger-based work. Real user/support/IP/release issues may justify attention. Known unavailable physical-host gates must not consume continuous Owner attention. Per-application expansion remains separately gated.

### `B2 — PORT-004 — Creative Test Agent`

Maintain runnable pilot readiness. Activate bounded product work when a qualified design partner/customer provides real inputs, success criteria and plausible commercial or flagship-learning value. Technical completeness or OS-reference value alone is not a funding claim.

### `C1 — PORT-007 — Data Platform`

Clarification-only. Allowed work is limited to named consumers, minimal common-contract hypothesis, ownership/data/sovereignty/continuity boundaries and an economic case for removing duplicated burden. No material shared-runtime/datastore/platform build is authorized.

### `D1 — PORT-005 — Tender Small-Volume Calculator`

Contain. Preserve maintenance/security/continuity and selective procurement-family reference evidence. Do not create a parallel procurement growth product without a new decision.

### `D2 — PORT-006 — Doors Parser`

Contain completed-delivery asset. Preserve support obligations and extraction/QA/reuse evidence. Do not expand into a generic parser or growth product without new evidence and decision.

## 5. Company-level override hierarchy

AC-306 remains subordinate to AC-106:

- `P0` — obligations, cash, material risk;
- `P1` — flagship `«ИИ-компания под ключ»` market evidence + minimal real Company operating model;
- `P2` — product/OS work directly tied to revenue, obligation, evidence or blocker removal;
- `P3` — speculative expansion.

A real customer/security/data/continuity obligation may temporarily override the portfolio order for the exact affected work. That does not silently change the node's disposition or AC-306 band.

## 6. Owner-attention rule

For material product work, decision preparation must state:

1. why now;
2. exact bounded outcome;
3. exact Owner action required;
4. what can proceed without Owner;
5. stop condition;
6. next decision enabled by evidence.

Owner attention is scarce management capital and must not be consumed by known-unavailable gate retries, speculative polish or unranked simultaneous feature expansion.

## 7. Capital and authority boundary

AC-306 creates no budget, numeric spend threshold, customer/vendor commitment, price, SLA, hiring authorization, Product Contract change, shared module or legal/IP/data right.

`ROD-02`, `ROD-04` and all other applicable Owner/authority gates remain binding for specific material effects.

## 8. Source-of-truth rule

- this file is canonical for the current Company-level portfolio map and default investment/attention order;
- product repositories remain canonical for product implementation/status/domain semantics;
- Arvectum OS remains canonical for Product Contracts/platform capability lifecycle;
- actual customer/accounting/legal evidence remains in its competent source of truth;
- material new evidence should trigger re-evaluation rather than silent re-banding.

## 9. Downstream governance

`AC-306 — Complete / PASS`.

Next canonical portfolio action:

`AC-307 — Итоговая проверка управления портфелем и закрытие M3`.
