# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `3.0.0`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `2.9.0` по immutable git blob и добавляет утверждение AC-402 и переход к AC-403.

Предыдущая редакция:

- версия: `2.9.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `a7b9933622260f0037b56ddadbb9833a77038279`.

Все ранее зарегистрированные источники M0–M3, AC-201–AC-401, языково-терминологическая политика, Company/Product/Arvectum OS boundaries и правила внешних источников сохраняются без изменений, если прямо не уточнены более новым утверждённым артефактом.

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

- `docs/roadmap/ROADMAP.md` — `Active 0.31.0`;
- текущий blob SHA: `f02a2c6fe44d7465d976504706b8a52cbd48690d`.

Текущее каноническое действие:

`AC-403 — Risk, exception and incident register model`.

Текущий этап:

`M4 — Owner control and reference-implementation observability established`.

## 4. Approved AC-401 work/obligation control model

Каноническая approved publication:

- `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL-v1.0.0.md` — `Approved 1.0.0`;
- immutable publication blob SHA: `fa9f513b1434c7eda257ac412bf7472da400519d`.

Exact reviewed proposal:

- `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL.md` — `Proposed 0.9.0`;
- immutable blob SHA: `0f4444fbd968e176a0a158771a7d0abe93549ecd`.

AC-401 устанавливает `WORK-*` и `OBL-*` как Company-level control identities при сохранении underlying legal/accounting/customer/product/OS truth в соответствующих authoritative contours.

## 5. Approved AC-402 decision/approval/escalation model

Каноническая approved publication:

- `docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL-v1.0.0.md` — `Approved 1.0.0`;
- immutable publication blob SHA: `ae013d7e93dc51573f56b1ded2e907ee58182e57`.

Exact reviewed proposal:

- `docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL.md` — `Proposed 0.9.0`;
- immutable proposal blob SHA: `a48081ba3599e6f3c91b8a6562435ad1f0c152f4`.

Cross-review:

- `docs/reviews/AC-402-COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-CROSS-REVIEW.md`;
- `10 of maximum 10`;
- `Complete / PASS for Owner approval`;
- immutable blob SHA: `82cf1046178cde22387a04037e86cf7e1b224f9a`.

Owner decision:

- `docs/governance/decisions/DECISION-2026-08-21-AC-402-APPROVAL.md` — `Approved`;
- immutable blob SHA: `30dbae9a081b1dc1939923083b31e3f40be2a80c`;
- explicit wording: `AC-402 утверждаю`.

AC-402 является binding Company decision-control model в своём declared scope.

## 6. AC-402 canonicality and authority boundary

AC-402 устанавливает три control namespaces:

- `DEC-*` — material decision case / durable decision record;
- `APR-*` — approval gate / attributable approval act control record;
- `ESC-*` — escalation case.

Главная граница:

`recommendation ≠ decision ≠ approval ≠ legal/corporate act ≠ technical authorization ≠ execution`.

Company repository может быть canonical для внутреннего Company Organizational Authority act только в своём declared scope. Participant/General Director/customer/Product/Arvectum OS/legal/external facts остаются authoritative в собственных contours.

`ROD-01…ROD-09`, `AM-0…AM-4`, Position/Assignment/access boundaries сохраняются. `decision_outcome=approve` не является универсальным разрешением внешнего эффекта.

Current Arvectum OS `DECISION-AUTHORITY-POLICY.md` `Proposed 0.2.1` не принят AC-402 как Company governance.

## 7. Действующий портфель и предыдущие этапы

Канонический Company-level portfolio source:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.8.0`;
- текущий blob SHA: `8a77be35225f9c4958531e52a4131abda13d0f`;
- governance baseline: `AC-307 — Approved 1.0.0 / M3 Complete / PASS`.

Статус этапов:

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3` — `Complete / PASS`;
- `M4` — `Current`, AC-403 `Current`;
- `M5` — `Planned`;
- `M6` — `Planned`;
- `M7` — `Future`;
- `M8` — `Future`;
- `M9` — финальный плановый этап, AC-901 `Planned` после M8.

Полный M3 portfolio baseline и Arvectum OS Product Contract correspondence сохраняются из предыдущей source-register chain и Approved AC-301…AC-307.

## 8. M4 navigation

M4 теперь проходит так:

1. `AC-401` — Company work/obligation register model — `Complete / PASS`;
2. `AC-402` — Decision, approval and escalation register model — `Complete / PASS`;
3. `AC-403` — Risk, exception and incident register model — `Current`;
4. `AC-404` — Cash, commitment and management reporting baseline;
5. `AC-405` — Portfolio/module/priority review cadence;
6. `AC-406` — Owner Mission Control / reference-implementation evidence view;
7. `AC-407` — Management operating cadence and control review.

AC-401/AC-402 утверждают semantic/control models, но сами по себе не создают полную live population `WORK-*`/`OBL-*`/`DEC-*`/`APR-*`/`ESC-*`. Наполнение должно опираться на подтверждённые current sources и отдельное evidence.

## 9. Arvectum OS boundary

Company-specific control semantics принадлежат `arvectum/arvectum-company`.

Arvectum OS MAY позднее предоставлять domain-neutral persistence/projection/governed-execution mechanisms через отдельный admitted boundary. Никакая Company запись, UI projection или OS technical role не создаёт Organizational Authority по импликации.

## 10. Язык, терминология и публичная граница

Для новых человекочитаемых Company-документов действует русскоязычный режим и `docs/governance/TERMINOLOGY-GLOSSARY.md`.

Этот публичный репозиторий не является местом хранения секретов, reusable credentials, private keys, подписей, избыточных персональных данных, банковских/платёжных payloads, непубличных договорных/customer материалов, privileged incident details или chain-of-thought.

## 11. Конечный этап M9

`M9 — Человекочитаемая документация полностью русифицирована и согласована` остаётся самым последним плановым этапом после M8, если собственник отдельно не изменит последовательность.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` остаётся `Planned`.