# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.30.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-402 — Decision, approval and escalation register model`
Русское название текущего действия: `Модель реестра решений, утверждений и эскалаций`

## 1. Модель публикации

Эта редакция `0.30.0` сохраняет полное содержание дорожной карты `0.29.0` по immutable git blob и добавляет утверждение/закрытие AC-401 с переходом к AC-402.

Предыдущая редакция:

- версия: `0.29.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `d66f04e9b5b7636683b8bc3007967ccbe346d89c`.

Все ранее определённые этапы M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-401

`AC-401 — Company work/obligation register model` имеет статус:

`Complete / PASS`.

Утверждённая publication:

- `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL-v1.0.0.md` — `Approved 1.0.0`, blob `fa9f513b1434c7eda257ac412bf7472da400519d`;
- exact reviewed proposal: `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL.md` — `Proposed 0.9.0`, blob `0f4444fbd968e176a0a158771a7d0abe93549ecd`;
- cross-review: `docs/reviews/AC-401-COMPANY-WORK-OBLIGATION-REGISTER-CROSS-REVIEW.md` — `10 of maximum 10`, PASS, blob `7c0cbc178bf50a7babbd0403798091c4ddef996f`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-401-APPROVAL.md`, blob `408ee310b81d6d27af36e901e42358de2b48aa82`;
- explicit Owner approval wording: `AC-401 утверждаю`.

AC-401 устанавливает минимальный Company control substrate:

```text
Authoritative sources
        ↓ references + freshness
WORK-* / OBL-* Company control entries
        ↓
Position accountability + P0…P3 + control state
        ↓
attention / escalation need / next control point
        ↓
future specialized decision/risk/cash views
```

Реестр является canonical только для Company-level control representation в своём scope. Он не становится бухгалтерией, legal/contract source, product tracker или Arvectum OS authority.

## 3. M3 и предыдущие этапы

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3 — Product/module-candidate portfolio governed as investments` — `Complete / PASS`.

Полный M3 baseline остаётся в редакции roadmap `0.29.0`, AC-301…AC-307 и `docs/portfolio/PORTFOLIO.md`.

Закрытие M3 не означает profitability, market validation, legal compliance, customer readiness, production readiness, approved reusable production module, Stable Product Contract или Active Arvectum OS capability.

## 4. Phase 4 — Owner control and reference observability

Milestone:

`M4 — Owner control and reference-implementation observability established`.

Назначение M4: дать собственнику возможность видеть существенные работы, обязательства, решения, риски, cash/commitments и portfolio state без постоянного восстановления контекста из чатов и отдельных репозиториев, одновременно создавая наблюдаемое evidence того, работает ли AI-native organizational model на практике.

Текущий статус:

| ID | Работа | Статус |
|---|---|---|
| `AC-401` | Company work/obligation register model | `Complete / PASS` |
| `AC-402` | Decision, approval and escalation register model | `Current` |
| `AC-403` | Risk, exception and incident register model | `Planned` |
| `AC-404` | Cash, commitment and management reporting baseline | `Planned` |
| `AC-405` | Portfolio/module/priority review cadence | `Planned` |
| `AC-406` | Owner Mission Control / reference-implementation evidence view | `Planned` |
| `AC-407` | Management operating cadence and control review | `Planned` |

Software dashboard не является предпосылкой M4: manual/simpler controls допустимы, если они надёжны, пропорциональны и уменьшают Owner reconstruction burden.

## 5. AC-401 approved boundary carried forward

AC-402…AC-406 должны сохранять AC-401 semantics:

- `WORK-*` и `OBL-*` — Company control identities, а не копии lower-level truth;
- одна primary accountable `POS-*` Position на active item;
- `P0/P1/P2/P3` — sequencing context, не spend authorization;
- `open/waiting/blocked/closed` описывают Company control handling, а не юридическую/product/accounting truth;
- `normal/needs_attention/escalated` не являются approval states;
- due/trigger и source freshness не фабрикуются;
- закрытие work не означает satisfaction obligation без authoritative evidence;
- data minimization и reference-over-copy остаются default;
- visibility не создаёт authority, permission, credential или external-effect right;
- Company-specific semantics не переносятся в Arvectum OS без применимого governed boundary.

AC-401 `1.0.0` сам по себе не создаёт фактический live population `WORK-*`/`OBL-*`; первое наполнение может быть выполнено отдельным bounded evidence-producing шагом на подтверждённых current sources.

## 6. Текущее действие — AC-402

### AC-402 — Decision, approval and escalation register model

Статус: `Current`.

AC-402 должен определить отдельную Company-level семантику material decisions, pending/obtained approvals и escalations поверх утверждённого AC-401 control substrate.

Минимальные вопросы AC-402:

- как отличить proposal/recommendation от decision и approval;
- как привязать decision/approval/escalation к `WORK-*`, `OBL-*`, `PORT-*`, Position, `ROD-*`/`AM-*` и authoritative legal/corporate source без смешения сфер;
- как представить pending authority gate и exact decision owner/approver;
- как фиксировать explicit approval/decline/expiry/supersession без вывода approval из silence, AI recommendation или technical execution;
- как различать внутреннее Organizational Authority, требуемый legal/corporate act и technical execution authorization;
- как показать Owner только те decisions/escalations, которые действительно требуют его действия;
- как сохранить минимизацию данных, evidence references, reconstructability и fail-closed behavior.

AC-402 не должен автоматически создавать approval authority, legal power, budget, customer commitment, external mutation или OS Product Contract.

## 7. M4 exit direction

M4 должен завершиться только когда собственник может из устойчивого Company control layer видеть как минимум material work, obligations, pending decisions/approvals, risks/exceptions, cash/commitment signals, portfolio priorities и evidence, достаточное для оценки внутренней reference implementation.

Конкретные register semantics, cadence и presentation должны выводиться по AC-401…AC-407, а не проектироваться заранее ради полноты.

## 8. Authority boundary

Roadmap координирует работу, но не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant или production approval.

Material capital, external commitment, risk, legal/IP/data и Company↔Product↔Arvectum OS decisions продолжают проходить соответствующий evidence и authority path.