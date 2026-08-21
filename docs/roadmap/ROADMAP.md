# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.34.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-406 — Owner Mission Control / reference-implementation evidence view`
Русское название текущего действия: `Представление Mission Control для собственника и доказательств эталонной реализации`

## 1. Модель публикации

Эта редакция `0.34.0` сохраняет полное содержание дорожной карты `0.33.0` по immutable git blob и добавляет утверждение/закрытие AC-405 с переходом к AC-406.

Предыдущая редакция:

- версия: `0.33.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `a409b059771f78d26dc529cc5d8bee74acfadfc6`.

Все ранее определённые этапы M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-405

`AC-405 — Portfolio/module/priority review cadence` имеет статус:

`Complete / PASS`.

Утверждённая publication:

- `docs/portfolio/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE-v1.0.0.md` — `Approved 1.0.0`, blob `8150c0b8ff009941220dd6d0ce48d721eb9e42d9`;
- exact reviewed proposal: `docs/portfolio/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE.md` — `Proposed 0.9.0`, blob `13d19b2a5418c2d1d3349e889fe54817dd9ee126`;
- cross-review: `docs/reviews/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE-CROSS-REVIEW.md` — `8 iterations`, PASS, blob `1192472888da43de4160499d828e5def87391197`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-405-APPROVAL.md`, blob `76bc7b8f9c560c3e2a3baf18b58c13de009e8eb4`;
- explicit Owner approval wording: `AC-405 утверждаю`.

AC-405 устанавливает portfolio review cadence:

```text
material event
→ scoped event-driven review
→ monthly asynchronous exception scan as backstop
→ quarterly integrated revalidation as broader backstop
→ reaffirm current treatment OR prepare exact material change decision
```

Календарные интервалы являются initial operating defaults и могут быть скорректированы последующим operating evidence через надлежащий governance path.

Ключевые ограничения:

- `review ≠ decision ≠ approval ≠ investment ≠ product roadmap change ≠ OS lifecycle change`;
- `P0 temporary execution priority ≠ permanent portfolio reclassification`;
- named trigger ≠ automatic promotion/funding;
- reuse/reference evidence ≠ automatic module admission;
- `POS-003` routine `AM-2` stewardship не заменяет applicable `ROD-*`/DEC/APR gates.

## 3. Утверждённый M4 control baseline после AC-405

Company имеет следующие связанные уровни управления и видимости:

1. `WORK-*` / `OBL-*` — material work и obligations;
2. `DEC-*` / `APR-*` / `ESC-*` — material decisions, approval gates/acts и escalations;
3. `RSK-*` / `EXC-*` / `INC-*` — material risks, control exceptions и incidents;
4. AC-404 management-finance projection — decision-relevant cash/commitment signals поверх authoritative sources;
5. AC-405 portfolio review cadence — event-driven и bounded calendar revalidation поверх M3 portfolio semantics и AC-401…AC-404 evidence.

Пятый уровень не создаёт нового portfolio authority или product/OS source of truth.

Сохраняются общие границы:

- Company control/management representation не подменяет legal/accounting/customer/product/OS truth;
- `P0…P3` — sequencing context, не spend authorization;
- risk/incident/financial/portfolio visibility не являются approval;
- material spend/commitment, portfolio investment, risk acceptance, module admission и Company↔Product↔OS boundary changes требуют applicable attributable authority act;
- cash, priority rank, review completion, technical access или UI visibility не создают authority;
- stale/missing evidence и changed facts требуют explicit uncertainty/review/fail-closed behavior;
- public repository использует minimization и reference-over-copy;
- Company-specific semantics не переносятся в Arvectum OS по импликации.

## 4. Предыдущие этапы

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3 — Product/module-candidate portfolio governed as investments` — `Complete / PASS`.

Полный prior baseline остаётся доступным через immutable roadmap chain и утверждённые AC-001…AC-405 artifacts.

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
| `AC-405` | Portfolio/module/priority review cadence | `Complete / PASS` |
| `AC-406` | Owner Mission Control / reference-implementation evidence view | `Current` |
| `AC-407` | Management operating cadence and control review | `Planned` |

Software dashboard не является предпосылкой M4: manual/simpler controls допустимы, если они надёжны, пропорциональны и уменьшают Owner reconstruction burden.

## 6. Текущее действие — AC-406

### AC-406 — Owner Mission Control / reference-implementation evidence view

Статус: `Current`.

AC-406 должен определить минимальное owner-facing **derived evidence view**, позволяющее собственнику видеть Company control state и exact required action без постоянной реконструкции контекста из чатов, репозиториев и source systems.

Минимальные вопросы AC-406:

- какие `WORK-*`/`OBL-*` должны быть видимы Owner и какие routine items должны быть скрыты;
- как показывать только реальные pending `DEC-*`/`APR-*`/`ESC-*`, где требуется Owner act;
- как показывать material `RSK-*`/`EXC-*`/`INC-*` без превращения каждого alert/issue в Owner queue;
- как включать AC-404 cash/commitment signals с `as_of`, freshness, uncertainty и source refs без публикации restricted financial payload;
- как показывать M3/AC-405 portfolio priorities, material review triggers и module-candidate evidence без автоматического re-ranking;
- как отделить source fact, Company interpretation, recommendation, decision/approval и execution state;
- как показывать exact question, `why now`, downside/uncertainty, authority basis, remaining gates и next execution handoff для Owner decision;
- как сделать reference-implementation evidence достаточным для оценки самой Arvectum Company как работающей AI-native организации, не подменяя реальную business evidence красивым dashboard;
- какие данные могут быть derived/aggregated, а какие должны оставаться references на authoritative sources;
- как сохранить least privilege, minimization, freshness, fail-closed и public/restricted boundary;
- нужен ли вообще software UI сейчас или достаточно стабильной Markdown/structured projection до появления доказанной потребности;
- если используется Arvectum OS workspace, какой explicit Product Contract/admitted boundary нужен и почему UI/runtime не становится источником Company authority.

AC-406 не должен создавать новый source of truth, authority, budget, approval, automated consequential execution, bank/accounting integration, product status, module admission, Product Contract или dashboard requirement по импликации.

## 7. M4 exit direction

M4 должен завершиться только когда собственник может из устойчивого Company control layer видеть material work, obligations, pending decisions/approvals, risks/exceptions/incidents, cash/commitment signals, portfolio priorities и evidence, достаточное для управления и оценки reference implementation без постоянной реконструкции контекста.

AC-406 создаёт owner-facing evidence model; AC-407 должен затем проверить/зафиксировать management operating cadence и реальный control burden.

## 8. Authority boundary

Roadmap координирует работу, но не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant или production approval.

Material capital, spend, external commitment, portfolio investment, risk acceptance, legal/IP/data и Company↔Product↔Arvectum OS decisions продолжают проходить соответствующий evidence и authority path.