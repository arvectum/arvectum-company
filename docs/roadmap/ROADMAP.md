# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.32.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-404 — Cash, commitment and management reporting baseline`
Русское название текущего действия: `Базовая модель видимости денег, обязательств и управленческой отчётности`

## 1. Модель публикации

Эта редакция `0.32.0` сохраняет полное содержание дорожной карты `0.31.0` по immutable git blob и добавляет утверждение/закрытие AC-403 с переходом к AC-404.

Предыдущая редакция:

- версия: `0.31.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `f02a2c6fe44d7465d976504706b8a52cbd48690d`.

Все ранее определённые этапы M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-403

`AC-403 — Risk, exception and incident register model` имеет статус:

`Complete / PASS`.

Утверждённая publication:

- `docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL-v1.0.0.md` — `Approved 1.0.0`, blob `effef94f950d6d070c421a22c2eced00b5e561ad`;
- exact reviewed proposal: `docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL.md` — `Proposed 0.9.0`, blob `857b601423f78fc3d4636dbf9754d5410d8a1c55`;
- cross-review: `docs/reviews/AC-403-COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-CROSS-REVIEW.md` — `10 of maximum 10`, PASS, blob `37241051876a94f71035e532e19ed9cf69b4c785`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-403-APPROVAL.md`, blob `524cad548204d8721117989f3940f3295ab7d932`;
- explicit Owner approval wording: `AC-403 утверждаю`.

AC-403 устанавливает третий Company control layer:

```text
RSK-* material risk exposure/control
EXC-* material control exception request/decision control
INC-* material incident control
```

Ключевые инварианты:

`risk evidence ≠ accepted risk`

`exception request ≠ approved exception`

`incident detection ≠ authority to act`

`containment ≠ risk acceptance`

`recovery ≠ automatic obligation/risk closure`.

## 3. Утверждённый M4 control baseline

После AC-403 Company имеет три последовательных control layers:

1. `WORK-*` / `OBL-*` — material work и obligations;
2. `DEC-*` / `APR-*` / `ESC-*` — material decisions, approval gates/acts и escalations;
3. `RSK-*` / `EXC-*` / `INC-*` — material risks, control exceptions и incidents.

Сохраняются общие границы:

- Company control representation не подменяет legal/accounting/customer/product/OS truth;
- одна primary accountable Position на active Company control item;
- `P0…P3` — sequencing context, не spend authorization;
- `needs_attention`/`escalated` и incident severity не являются approval;
- risk acceptance и exception approval требуют applicable attributable authority act;
- emergency containment не передаёт material risk acceptance;
- stale/missing evidence и changed facts требуют explicit uncertainty/review/fail-closed behavior;
- public repository использует minimization и reference-over-copy;
- Company-specific semantics не переносятся в Arvectum OS по импликации.

## 4. Предыдущие этапы

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3 — Product/module-candidate portfolio governed as investments` — `Complete / PASS`.

Полный prior baseline остаётся доступным через immutable roadmap chain и утверждённые AC-001…AC-403 artifacts.

## 5. Phase 4 — Owner control and reference observability

Milestone:

`M4 — Owner control and reference-implementation observability established`.

Текущий статус:

| ID | Работа | Статус |
|---|---|---|
| `AC-401` | Company work/obligation register model | `Complete / PASS` |
| `AC-402` | Decision, approval and escalation register model | `Complete / PASS` |
| `AC-403` | Risk, exception and incident register model | `Complete / PASS` |
| `AC-404` | Cash, commitment and management reporting baseline | `Current` |
| `AC-405` | Portfolio/module/priority review cadence | `Planned` |
| `AC-406` | Owner Mission Control / reference-implementation evidence view | `Planned` |
| `AC-407` | Management operating cadence and control review | `Planned` |

Software dashboard не является предпосылкой M4: manual/simpler controls допустимы, если они надёжны, пропорциональны и уменьшают Owner reconstruction burden.

## 6. Текущее действие — AC-404

### AC-404 — Cash, commitment and management reporting baseline

Статус: `Current`.

AC-404 должен определить минимальный Company-level management layer, позволяющий собственнику видеть decision-relevant cash, material commitments и финансово-операционные сигналы, не создавая вторую бухгалтерию или банк.

Минимальные вопросы AC-404:

- какие cash facts и commitment signals действительно нужны Owner/Positions для текущих решений;
- как связать их с `OBL-*`, `WORK-*`, `DEC-*`, `APR-*`, `ESC-*`, `RSK-*`, `EXC-*`, `INC-*`, portfolio и authoritative accounting/bank/legal/customer sources;
- как различить bank/accounting transaction truth, management interpretation, forecast/hypothesis и approved commitment;
- как показать due cash obligations, recurring costs, receivables/payables, expected inflows/outflows и cash-gap uncertainty без fabricated precision;
- какие Company-level management aggregates допустимы без копирования полного ledger;
- как сохранить `P0` preemption для time-sensitive obligations/cash/material risk;
- как различить budget/limit, planned spend, approved commitment, incurred obligation и actual payment;
- как не вывести spend authority из наличия cash или dashboard visibility;
- как управлять freshness, reconciliation, confidentiality и restricted banking/accounting payload;
- какой минимальный management report нужен до AC-406 Owner Mission Control.

AC-404 не должен создавать бухгалтерскую систему, tax ledger, bank ledger, новые финансовые полномочия, бюджет, кредит/финансирование, spend approval, customer/vendor obligation или OS Product Contract по импликации.

## 7. M4 exit direction

M4 должен завершиться только когда собственник может из устойчивого Company control layer видеть material work, obligations, pending decisions/approvals, risks/exceptions/incidents, cash/commitment signals, portfolio priorities и evidence, достаточное для управления и оценки reference implementation без постоянной реконструкции контекста.

Конкретные cadence и presentation остаются AC-405…AC-407.

## 8. Authority boundary

Roadmap координирует работу, но не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant или production approval.

Material capital, spend, external commitment, risk acceptance, legal/IP/data и Company↔Product↔Arvectum OS decisions продолжают проходить соответствующий evidence и authority path.