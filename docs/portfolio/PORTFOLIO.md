# Arvectum Company Portfolio

Status: `Active`
Version: `0.8.0`
Created: `2026-08-20`
Updated: `2026-08-21`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Current governance baseline: `AC-307 — Approved 1.0.0 / M3 Complete / PASS`

## 1. Publication model

Эта редакция `0.8.0` сохраняет полный portfolio baseline `0.7.0` по immutable git blob и добавляет утверждённую итоговую проверку AC-307 и закрытие M3.

Предыдущая редакция:

- version: `0.7.0`;
- path: `docs/portfolio/PORTFOLIO.md`;
- immutable git blob SHA: `e2e43ced1647d5fcbe6cd484b528770775097753`.

Approved AC-307 baseline:

- `docs/portfolio/AC-307-PORTFOLIO-GOVERNANCE-REVIEW-AND-M3-CLOSURE-v1.0.0.md` — `Approved 1.0.0`, blob `ff9a07d8c7161bfdaf3628e1c8e21d2a2d0f4435`;
- exact reviewed proposal: `docs/portfolio/AC-307-PORTFOLIO-GOVERNANCE-REVIEW-AND-M3-CLOSURE.md` — `Proposed 0.9.0`, blob `904b9e5ffa12caeb082b3bf23a89aff251ebe8c4`;
- cross-review: `docs/reviews/AC-307-PORTFOLIO-GOVERNANCE-M3-CLOSURE-CROSS-REVIEW.md` — `10 of maximum 10`, PASS, blob `bc3c4992f12dabaeb155f055373da292278cd791`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-307-APPROVAL-AND-M3-CLOSURE.md`.

Approved AC-301…AC-306 остаются в силе и являются составными слоями текущего M3 baseline.

## 2. Current governed portfolio map

| ID | Company-level name | Canonical repository | Disposition | Accountable Position | Role | Priority |
|---|---|---|---|---|---|---|
| `PORT-001` | `Arvectum Tender Agent` | `arvectum/tender-agent` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone + `RI-OS-CONSUMER` | `A2` bounded revenue/pilot/evidence |
| `PORT-002` | `Discount Parser` | `arvectum/discount-parser` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone + `RI-OS-CONSUMER + RI-PRODUCT-FAMILY` | `A1` finish/accept/stabilize/maintain |
| `PORT-003` | `Arvectum Proxy Launcher` | `arvectum/proxy-launcher` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone | `B1` named-trigger |
| `PORT-004` | `Creative Test Agent` | `arvectum/creative-test-agent` | `continue` | `POS-003 — Portfolio & Product Lead` | standalone + `RI-OS-CONSUMER` | `B2` named-trigger |
| `PORT-005` | `Tender Small-Volume Calculator` | `arvectum/tender-app` | `contain` | `POS-003 — Portfolio & Product Lead` | `RI-PRODUCT-FAMILY` | `D1` contain/reference |
| `PORT-006` | `Doors Parser` | `arvectum/doors_parser` | `contain` | `POS-003 — Portfolio & Product Lead` | `RI-PRODUCT-FAMILY` | `D2` contain/support/reference |
| `PORT-007` | `Data Platform` | `arvectum/data-platform` | `clarify` | `POS-003 — Portfolio & Product Lead` | clarification-only Company/product-family module candidate | `C1` clarification-only; no material build |

## 3. Dependency and Arvectum OS boundary

Между `PORT-001…PORT-007` не установлено обязательной hard runtime/code/data dependency.

Current governed OS correspondence:

| Node | OS boundary | Exact current platform dependency |
|---|---|---|
| `PORT-001` | P6.02 + supplemental P8.03 | `CAP-001 + CAP-004` в exact bounded scopes |
| `PORT-002` | P6.06 | `CAP-004 only` |
| `PORT-004` | P8.06 optional external extension | `CAP-004 only` |
| `PORT-003` | none evidenced | none inferred |
| `PORT-005` | none evidenced | none inferred |
| `PORT-006` | none evidenced | none inferred |
| `PORT-007` | none evidenced | none inferred |

P6.02 historical locator `arutyunoveth/ai-corporation` reconciled отдельным Approved Arvectum OS provenance overlay; current implementation locator — `arvectum/tender-agent`. Семантика P6.02 остаётся `Provisional 0.1.0`.

Reference/reuse evidence не создаёт shared runtime, library, datastore, module или Product Contract автоматически.

## 4. Default portfolio decision order

При отсутствии более высокого Company-level `P0` обязательства:

```text
A1  PORT-002 — Discount Parser
A2  PORT-001 — Arvectum Tender Agent
    ↓
B1  PORT-003 — Arvectum Proxy Launcher   ┐
B2  PORT-004 — Creative Test Agent       ├─ named trigger only
    ↓                                     ┘
C1  PORT-007 — Data Platform — clarification only
    ↓
D1  PORT-005 — Tender Small-Volume Calculator
D2  PORT-006 — Doors Parser
```

Это decision order, а не постоянная engineering queue, funding allocation или новый Company flagship.

AC-106 остаётся выше portfolio ranking:

`P0 obligations/cash/material risk → P1 flagship evidence + real operating model → P2 revenue/obligation/evidence-linked product/OS work → P3 speculative expansion`.

## 5. M3 closure result

`M3 — Product/module-candidate portfolio governed as investments` имеет статус:

`Complete / PASS`.

M3 установил достаточный Company-level baseline по:

- identity/disposition;
- accountable Position;
- investment/cost/risk treatment;
- standalone/reference/module/OS-candidate classification;
- inter-product and Arvectum OS dependency boundaries;
- capital/economics/Owner-attention priority.

Закрытие M3 не доказывает profitability, market validation, customer/production readiness, legal/IP/data completeness или Stable/Active Arvectum OS lifecycle.

## 6. Carry-forward discipline

Материальное новое evidence должно приводить к re-evaluation, а не silent re-banding.

Особенно остаются открыты:

- PORT-001 — real paid/pilot/deal economics and repeatability;
- PORT-002 — live client acceptance/support boundary и дальнейшее решение после accepted delivery;
- PORT-003 — legal/IP rights-basis evidence, separate-host gates и per-app stop-gate;
- PORT-004 — real design-partner/customer/commercial evidence;
- PORT-007 — named consumers, common contract и economic/continuity case до material build;
- portfolio-wide — unit economics, profitability, CAC/LTV/ROI и legal/customer readiness там, где они нужны для конкретного решения.

## 7. Source-of-truth rule

- этот файл — canonical Company-level portfolio map;
- product repositories — canonical для implementation/status/domain semantics;
- Arvectum OS — canonical для Product Contracts/platform capabilities;
- legal/accounting/customer systems — canonical для соответствующих правовых, финансовых, договорных и конфиденциальных фактов.

Repository locator, technical access, common ownership или common stack сами по себе не создают Organizational Authority, legal/IP ownership или cross-product commitment.

## 8. Handoff

`AC-307 — Complete / PASS`.

`M3 — Complete / PASS`.

Следующее каноническое Company action находится уже в M4:

`AC-401 — Company work/obligation register model`.