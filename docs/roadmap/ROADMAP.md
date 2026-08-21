# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.33.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-405 — Portfolio/module/priority review cadence`
Русское название текущего действия: `Порядок регулярного пересмотра портфеля, кандидатов в модули и приоритетов`

## 1. Модель публикации

Эта редакция `0.33.0` сохраняет полное содержание дорожной карты `0.32.0` по immutable git blob и добавляет утверждение/закрытие AC-404 с переходом к AC-405.

Предыдущая редакция:

- версия: `0.32.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `9b373bba42b1270a521cbcf6855aa84f23fb358c`.

Все ранее определённые этапы M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-404

`AC-404 — Cash, commitment and management reporting baseline` имеет статус:

`Complete / PASS`.

Утверждённая publication:

- `docs/operations/COMPANY-CASH-COMMITMENT-MANAGEMENT-REPORTING-BASELINE-v1.0.0.md` — `Approved 1.0.0`, blob `519330a5460ef9c712d7e6045dbb07475b021954`;
- exact reviewed proposal: `docs/operations/COMPANY-CASH-COMMITMENT-MANAGEMENT-REPORTING-BASELINE.md` — `Proposed 0.9.0`, blob `80c7b620cf446ed28b76143a0325ce89b1939ac0`;
- cross-review: `docs/reviews/AC-404-CASH-COMMITMENT-MANAGEMENT-REPORTING-CROSS-REVIEW.md` — `8 iterations`, PASS, blob `3519f63ef7c09f075aa75b6d0d83ccd770911141`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-404-APPROVAL.md`, blob `8e6ea741f14bb6471d250c6d39a76f15bdfb8ff3`;
- explicit Owner approval wording: `AC-404 утверждаю`.

AC-404 устанавливает management-finance projection layer поверх уже утверждённых control identities и сохраняет фундаментальное различие:

```text
bank/accounting fact
≠ management interpretation
≠ forecast
≠ budget/limit
≠ planned spend
≠ approved internal commitment
≠ incurred obligation
≠ actual payment
```

AC-404 не создаёт `FIN-*`, `PAY-*`, `TX-*` или иной параллельный transaction ledger.

## 3. Утверждённый M4 control baseline после AC-404

Company имеет четыре последовательных уровня управленческого контроля/видимости:

1. `WORK-*` / `OBL-*` — material work и obligations;
2. `DEC-*` / `APR-*` / `ESC-*` — material decisions, approval gates/acts и escalations;
3. `RSK-*` / `EXC-*` / `INC-*` — material risks, control exceptions и incidents;
4. AC-404 management-finance projection — decision-relevant cash/commitment signals поверх authoritative bank/accounting/legal/customer/product sources и уже существующих Company control identities.

Четвёртый уровень не является новым transaction register или source of accounting truth.

Сохраняются общие границы:

- Company control/management representation не подменяет legal/accounting/customer/product/OS truth;
- одна primary accountable Position на active Company control item;
- `P0…P3` — sequencing context, не spend authorization;
- `needs_attention`/`escalated`, risk/incident state и financial visibility не являются approval;
- risk acceptance, exception approval, material spend/commitment и external effect требуют applicable attributable authority act;
- cash availability или banking access не создают spend/payment authority;
- forecasted/conditional inflow не является cash до authoritative confirmation;
- stale/missing evidence и changed facts требуют explicit uncertainty/review/fail-closed behavior;
- public repository использует minimization и reference-over-copy;
- Company-specific semantics не переносятся в Arvectum OS по импликации.

## 4. Предыдущие этапы

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3 — Product/module-candidate portfolio governed as investments` — `Complete / PASS`.

Полный prior baseline остаётся доступным через immutable roadmap chain и утверждённые AC-001…AC-404 artifacts.

## 5. Phase 4 — Owner control and reference observability

Milestone:

`M4 — Owner control and reference-implementation observability established`.

Текущий статус:

| ID | Работа | Статус |
|---|---|---|
| `AC-401` | Company work/obligation register model | `Complete / PASS` |
| `AC-402` | Decision, approval and escalation register model | `Complete / PASS` |
| `AC-403` | Risk, exception and incident register model | `Complete / PASS` |
| `AC-404` | Cash, commitment and management reporting baseline | `Complete / PASS` |
| `AC-405` | Portfolio/module/priority review cadence | `Current` |
| `AC-406` | Owner Mission Control / reference-implementation evidence view | `Planned` |
| `AC-407` | Management operating cadence and control review | `Planned` |

Software dashboard не является предпосылкой M4: manual/simpler controls допустимы, если они надёжны, пропорциональны и уменьшают Owner reconstruction burden.

## 6. Текущее действие — AC-405

### AC-405 — Portfolio/module/priority review cadence

Статус: `Current`.

AC-405 должен определить минимальный устойчивый порядок пересмотра Company portfolio/module-candidate/priority state, используя:

- Approved M3 portfolio governance (`PORT-001…PORT-007`, dispositions, roles, priority bands, Company↔Product↔Arvectum OS boundaries);
- AC-106 `P0…P3` business-first priority hierarchy;
- AC-401 work/obligation evidence;
- AC-402 decision/approval/escalation evidence;
- AC-403 risk/exception/incident evidence;
- AC-404 management-finance/cash/commitment evidence.

Минимальные вопросы AC-405:

- какие события/изменения действительно требуют portfolio review, а какие должны оставаться product-local routine work;
- когда пересматривать disposition, role, investment class, module candidacy и priority;
- как отличать scheduled review от event-triggered review;
- какие evidence inputs должны быть актуальны до continue/change/contain/stop или material investment recommendation;
- как учитывать customer/revenue/obligation, economics, Owner workload, risk/continuity, reuse и technology-sovereignty evidence;
- какие portfolio decisions остаются `ROD-04`/иными applicable Owner gates, а какие routine stewardship могут оставаться в допустимом `AM-2` scope;
- как не превращать календарный review в обязательный Owner meeting, если material evidence не изменилось;
- как сохранить source-of-truth separation: Company owns portfolio meaning, product repos own implementation/status, OS owns Product Contracts/platform lifecycle;
- как передать только material Owner actions в будущий AC-406 Mission Control;
- какие cadence details действительно нужны сейчас, а какие должны быть проверены реальным использованием в AC-407.

AC-405 не должен автоматически менять `PORT-*` disposition/priority, создавать бюджет/инвестицию, продвигать candidate в reusable module, менять product roadmap, создавать cross-product dependency или Arvectum OS Product Contract/lifecycle state.

## 7. M4 exit direction

M4 должен завершиться только когда собственник может из устойчивого Company control layer видеть material work, obligations, pending decisions/approvals, risks/exceptions/incidents, cash/commitment signals, portfolio priorities и evidence, достаточное для управления и оценки reference implementation без постоянной реконструкции контекста.

AC-405 определяет portfolio review discipline; AC-406 — owner-facing evidence view; AC-407 — итоговую management operating cadence и проверку control burden.

## 8. Authority boundary

Roadmap координирует работу, но не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant или production approval.

Material capital, spend, external commitment, portfolio investment, risk acceptance, legal/IP/data и Company↔Product↔Arvectum OS decisions продолжают проходить соответствующий evidence и authority path.