# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `2.9.0`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `2.8.0` по immutable git blob и добавляет утверждение AC-401 и переход к AC-402.

Предыдущая редакция:

- версия: `2.8.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `9b87bf5a78586307151202335405fe8fc20114c5`.

Все ранее зарегистрированные источники M0–M3, AC-201–AC-307, языково-терминологическая политика, Company/Product/Arvectum OS boundaries и правила внешних источников сохраняются без изменений, если прямо не уточнены более новым утверждённым артефактом.

## 2. Порядок приоритета источников

В своей области действуют:

1. применимое право и действительные юридические/корпоративные полномочия;
2. утверждённые документы управления Arvectum Company и явные решения собственника;
3. канонические документы Arvectum OS там, где Company фактически использует OS;
4. продуктовые репозитории и продуктовые решения в пределах продуктовой области;
5. дорожная карта как средство планирования, а не самостоятельный источник полномочий;
6. чаты, память модели, локальные копии и сгенерированные материалы как контекст, если они не были явно повышены до канонического источника.

## 3. Действующая дорожная карта

Канонический источник планирования:

- `docs/roadmap/ROADMAP.md` — `Active 0.30.0`;
- текущий blob SHA: `0ffc55769028405bd2f78ad6b2d0700b55e33469`.

Текущее каноническое действие:

`AC-402 — Decision, approval and escalation register model`.

Текущий этап:

`M4 — Owner control and reference-implementation observability established`.

## 4. Approved AC-401 control model

Каноническая approved publication:

- `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL-v1.0.0.md` — `Approved 1.0.0`;
- immutable publication blob SHA: `fa9f513b1434c7eda257ac412bf7472da400519d`.

Exact reviewed source:

- `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL.md` — `Proposed 0.9.0`;
- immutable proposal blob SHA: `0f4444fbd968e176a0a158771a7d0abe93549ecd`.

Cross-review:

- `docs/reviews/AC-401-COMPANY-WORK-OBLIGATION-REGISTER-CROSS-REVIEW.md`;
- `10 of maximum 10`;
- `Complete / PASS for Owner approval`;
- immutable blob SHA: `7c0cbc178bf50a7babbd0403798091c4ddef996f`.

Owner decision:

- `docs/governance/decisions/DECISION-2026-08-21-AC-401-APPROVAL.md` — `Approved`;
- immutable blob SHA: `408ee310b81d6d27af36e901e42358de2b48aa82`;
- explicit wording: `AC-401 утверждаю`.

AC-401 является binding Company control model в своём declared scope.

## 5. AC-401 canonicality boundary

AC-401 устанавливает два класса control identities:

- `WORK-*` — material Company-level work item;
- `OBL-*` — material obligation control item.

Company repository может быть authoritative для Company control metadata этих entries: identity, operating meaning, accountable Position, priority/control/attention state, due-or-trigger context, next control point, source/evidence references, review/closure history.

Underlying truth остаётся в соответствующих источниках:

- legal/corporate obligation — применимый юридический/корпоративный источник;
- accounting/banking/statutory fact — профессиональный учётный/банковский контур;
- customer/vendor fact — соответствующий contract/source contour;
- product implementation/status — product repository;
- Arvectum OS Product Contract/platform state — `arvectum/arvectum-os`.

Создание/изменение register entry не создаёт само obligation, approval, Organizational Authority, legal power, budget, spend, customer commitment, technical permission или OS lifecycle transition.

## 6. Действующий портфель и предыдущие этапы

Канонический Company-level portfolio source:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.8.0`;
- текущий blob SHA: `8a77be35225f9c4958531e52a4131abda13d0f`;
- governance baseline: `AC-307 — Approved 1.0.0 / M3 Complete / PASS`.

Статус этапов:

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3` — `Complete / PASS`;
- `M4` — `Current`, AC-402 `Current`;
- `M5` — `Planned`;
- `M6` — `Planned`;
- `M7` — `Future`;
- `M8` — `Future`;
- `M9` — финальный плановый этап, AC-901 `Planned` после M8.

Полный M3 portfolio baseline и Arvectum OS Product Contract correspondence сохраняются из `2.8.0` и Approved AC-301…AC-307.

## 7. Arvectum OS correspondence

AC-401 не создаёт Arvectum OS Product Contract или Company-specific Platform Capability.

Проверенный перед proposal текущий OS state включал завершённый `P9.04 — My Work / Needs Attention projection`, который остаётся derived/non-authoritative presentation mechanism.

Допустимая будущая интеграция Company register с Arvectum OS требует отдельного explicit admitted boundary и должна сохранять Organization/Actor, authorization/data-governance, minimization, freshness и authority separation.

## 8. M4 navigation

M4 теперь проходит так:

1. `AC-401` — Company work/obligation register model — `Complete / PASS`;
2. `AC-402` — Decision, approval and escalation register model — `Current`;
3. `AC-403` — Risk, exception and incident register model;
4. `AC-404` — Cash, commitment and management reporting baseline;
5. `AC-405` — Portfolio/module/priority review cadence;
6. `AC-406` — Owner Mission Control / reference-implementation evidence view;
7. `AC-407` — Management operating cadence and control review.

AC-401 сам по себе не создаёт live `WORK-*`/`OBL-*` population. Такое наполнение является отдельным evidence step и должно опираться только на подтверждённые current sources.

## 9. Язык, терминология и публичная граница

Для новых человекочитаемых Company-документов действует русскоязычный режим и `docs/governance/TERMINOLOGY-GLOSSARY.md`.

Этот публичный репозиторий не является местом хранения секретов, reusable credentials, private keys, избыточных персональных данных, банковских/платёжных реквизитов, непубличных договорных материалов или customer-confidential payloads.

## 10. Конечный этап M9

`M9 — Человекочитаемая документация полностью русифицирована и согласована` остаётся самым последним плановым этапом после M8, если собственник отдельно не изменит последовательность.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` остаётся `Planned`.