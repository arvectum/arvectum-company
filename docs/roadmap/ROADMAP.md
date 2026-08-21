# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.31.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-403 — Risk, exception and incident register model`
Русское название текущего действия: `Модель реестра рисков, исключений и инцидентов`

## 1. Модель публикации

Эта редакция `0.31.0` сохраняет полное содержание дорожной карты `0.30.0` по immutable git blob и добавляет утверждение/закрытие AC-402 с переходом к AC-403.

Предыдущая редакция:

- версия: `0.30.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `0ffc55769028405bd2f78ad6b2d0700b55e33469`.

Все ранее определённые этапы M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-402

`AC-402 — Decision, approval and escalation register model` имеет статус:

`Complete / PASS`.

Утверждённая publication:

- `docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL-v1.0.0.md` — `Approved 1.0.0`, blob `ae013d7e93dc51573f56b1ded2e907ee58182e57`;
- exact reviewed proposal: `docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL.md` — `Proposed 0.9.0`, blob `a48081ba3599e6f3c91b8a6562435ad1f0c152f4`;
- cross-review: `docs/reviews/AC-402-COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-CROSS-REVIEW.md` — `10 of maximum 10`, PASS, blob `82cf1046178cde22387a04037e86cf7e1b224f9a`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-402-APPROVAL.md`, blob `30dbae9a081b1dc1939923083b31e3f40be2a80c`;
- explicit Owner approval wording: `AC-402 утверждаю`.

AC-402 устанавливает Company decision-control substrate:

```text
proposal / recommendation
        ↓
DEC-* material decision case
        ↕
APR-* approval gate / attributable act
        ↕
ESC-* escalation to exact authority
        ↓
effect readiness only after all required gates
```

Фундаментальное правило:

`recommendation ≠ decision ≠ approval ≠ legal/corporate act ≠ technical authorization ≠ execution`.

AC-402 не создаёт authority, budget, customer commitment, runtime или Arvectum OS Product Contract.

## 3. Утверждённый M4 control baseline на текущем этапе

AC-401 и AC-402 вместе создают два последовательных Company control layers:

1. `WORK-*` / `OBL-*` — material work и obligations;
2. `DEC-*` / `APR-*` / `ESC-*` — material decisions, approval gates/acts и escalations.

Сохраняются обязательные границы:

- одна primary accountable Position на active Company control item;
- Company control summary не подменяет underlying legal/accounting/customer/product/OS truth;
- `P0…P3` — sequencing context, не spend authorization;
- `needs_attention` / `escalated` не являются approval;
- decision outcome не равен readiness к consequential effect;
- physical Principal не сливает разные legal/organizational/technical capacities;
- stale/missing evidence и changed facts требуют review/fail-closed пропорционально consequence;
- visibility/credential/IAM access не создают Organizational Authority;
- public repository использует minimization и reference-over-copy.

## 4. Предыдущие этапы

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3 — Product/module-candidate portfolio governed as investments` — `Complete / PASS`.

Полный M3 baseline остаётся в AC-301…AC-307 и `docs/portfolio/PORTFOLIO.md`.

Закрытие M3 не означает profitability, market validation, legal compliance, customer readiness, production readiness, approved reusable production module, Stable Product Contract или Active Arvectum OS capability.

## 5. Phase 4 — Owner control and reference observability

Milestone:

`M4 — Owner control and reference-implementation observability established`.

Назначение M4: дать собственнику возможность видеть существенные работы, обязательства, решения, риски, cash/commitments и portfolio state без постоянного восстановления контекста из чатов и отдельных репозиториев, одновременно создавая наблюдаемое evidence того, работает ли AI-native organizational model на практике.

Текущий статус:

| ID | Работа | Статус |
|---|---|---|
| `AC-401` | Company work/obligation register model | `Complete / PASS` |
| `AC-402` | Decision, approval and escalation register model | `Complete / PASS` |
| `AC-403` | Risk, exception and incident register model | `Current` |
| `AC-404` | Cash, commitment and management reporting baseline | `Planned` |
| `AC-405` | Portfolio/module/priority review cadence | `Planned` |
| `AC-406` | Owner Mission Control / reference-implementation evidence view | `Planned` |
| `AC-407` | Management operating cadence and control review | `Planned` |

Software dashboard не является предпосылкой M4: manual/simpler controls допустимы, если они надёжны, пропорциональны и уменьшают Owner reconstruction burden.

## 6. Текущее действие — AC-403

### AC-403 — Risk, exception and incident register model

Статус: `Current`.

AC-403 должен определить отдельную Company-level семантику material risks, control exceptions и incidents поверх уже утверждённых AC-401/AC-402.

Минимальные вопросы AC-403:

- как различить risk, issue, exception, incident и accepted risk;
- как связать risk/incident с `WORK-*`, `OBL-*`, `DEC-*`, `APR-*`, `ESC-*`, `PORT-*`, Positions и source evidence;
- как отличить наблюдение/assessment риска от его принятия уполномоченной authority;
- как фиксировать exception request/approval/expiry без вывода waiver из silence или технического обхода;
- как представить incident detection, containment, impact, recovery и closure без подмены product/security source truth;
- когда incident/risk должен стать `P0`, `needs_attention` или escalation;
- как сохранять least privilege, minimization, confidentiality и evidence freshness;
- как не превращать реестр в duplicate security tracker, bug tracker или incident-management runtime.

AC-403 не должен автоматически принимать risk, разрешать exception, создавать incident response authority, spending authority, customer commitment или Arvectum OS Product Contract.

## 7. M4 exit direction

M4 должен завершиться только когда собственник может из устойчивого Company control layer видеть как минимум material work, obligations, pending decisions/approvals, risks/exceptions, cash/commitment signals, portfolio priorities и evidence, достаточное для оценки внутренней reference implementation.

Конкретные register semantics, cadence и presentation должны выводиться по AC-401…AC-407, а не проектироваться заранее ради полноты.

## 8. Authority boundary

Roadmap координирует работу, но не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant или production approval.

Material capital, external commitment, risk, legal/IP/data и Company↔Product↔Arvectum OS decisions продолжают проходить соответствующий evidence и authority path.