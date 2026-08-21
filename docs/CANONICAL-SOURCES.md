# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `2.7.0`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `2.6.0` по неизменяемой ссылке на git blob и синхронизирует навигационный/источниковый слой с фактически утверждённым Phase 3 состоянием перед AC-307.

Предыдущая редакция:

- версия: `2.6.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `5943729d6bb14a55e188d27763d80b53e6034771`.

Все ранее зарегистрированные источники M0–M2, AC-201–AC-208, языково-терминологическая политика, границы Company/Product/Arvectum OS и правила внешних источников сохраняются без изменений, если прямо не уточнены ниже более новым утверждённым артефактом.

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

- `docs/roadmap/ROADMAP.md` — `Active 0.28.0`;
- текущий blob SHA: `009f3aa9341c01039cf7b1d217fb246cf51855fe`.

Текущее каноническое действие:

`AC-307 — Итоговая проверка управления портфелем и закрытие M3`.

Полный план M0–M8, включённый в текущую publication chain, восходит к roadmap `0.14.0`; после M3 следующим этапом является M4 `Owner control and reference-implementation observability`, начинающийся с `AC-401 — Company work/obligation register model`. Финальный M9/AC-901, добавленный позднее, остаётся самым последним плановым этапом после M8.

## 4. Действующий портфель

Канонический Company-level portfolio source:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.7.0`;
- текущий blob SHA: `e2e43ced1647d5fcbe6cd484b528770775097753`;
- текущий governance baseline: `AC-306 — Approved 1.0.0`.

Approved Phase 3 publications:

1. `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION-v1.0.0.md` — identity/boundary/ownership;
2. `docs/portfolio/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-MAPPING-v1.0.0.md` — accountable Position;
3. `docs/portfolio/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-BOUNDARIES-v1.0.0.md` — investment/cost/risk treatment;
4. `docs/portfolio/AC-304-PORTFOLIO-ROLE-CLASSIFICATION-v1.0.0.md` — standalone/reference/module/OS-candidate classification;
5. `docs/portfolio/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-RECONCILIATION-v1.0.0.md` — inter-product dependency and Arvectum OS Product Contract reconciliation;
6. `docs/portfolio/AC-306-PORTFOLIO-PRIORITIZATION-CAPITAL-ECONOMICS-OWNER-ATTENTION-v1.0.0.md` — capital/economics/Owner-attention prioritization.

AC-307 is the current final Phase 3 review. Until it is explicitly approved, M3 remains `Current`, not `Complete`.

## 5. Current Phase 3 meaning

The current governed portfolio has seven stable Company identities `PORT-001…PORT-007`.

Binding high-level state:

- `PORT-001` Tender Agent — `continue`, standalone + `RI-OS-CONSUMER`, AC-306 `A2`;
- `PORT-002` Discount Parser — `continue`, standalone + `RI-OS-CONSUMER + RI-PRODUCT-FAMILY`, AC-306 `A1`;
- `PORT-003` Proxy Launcher — `continue`, standalone, trigger-based `B1`;
- `PORT-004` Creative Test Agent — `continue`, standalone + `RI-OS-CONSUMER`, trigger-based `B2`;
- `PORT-005` Tender Small-Volume Calculator — `contain`, `RI-PRODUCT-FAMILY`, `D1`;
- `PORT-006` Doors Parser — `contain`, `RI-PRODUCT-FAMILY`, `D2`;
- `PORT-007` Data Platform — `clarify`, clarification-only Company/product-family module candidate, `C1`.

Между текущими `PORT-*` не установлено обязательной hard runtime/code/data dependency. Product repositories остаются источником implementation/status/domain semantics. Arvectum OS остаётся источником Product Contracts/platform semantics. Company portfolio documents не переписывают эти внешние источники.

## 6. Arvectum OS correspondence

Текущая Company interpretation применимых OS boundaries зафиксирована AC-305:

- `PORT-001` — P6.02 + P8.03, exact bounded reliance on `CAP-001 + CAP-004`;
- `PORT-002` — P6.06, `CAP-004 only`;
- `PORT-004` — P8.06 optional external extension, `CAP-004 only`.

P6.02 repository locator отдельно reconciled в `arvectum/arvectum-os` через approved locator/provenance overlay: current implementation locator `arvectum/tender-agent`, historical predecessor locator `arutyunoveth/ai-corporation`. P6.02 semantic contract остаётся `Provisional 0.1.0`.

## 7. Статус планирования

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3` — `Current`, AC-301…AC-306 `Complete / PASS`, AC-307 `Current`;
- `M4` — `Planned`, первый пункт `AC-401`;
- `M5` — `Planned`;
- `M6` — `Planned`;
- `M7` — `Future`;
- `M8` — `Future`;
- `M9` — финальный плановый этап, `AC-901` `Planned` после M8.

Параллельный bounded AC-108 discovery loop остаётся источником рыночных данных и не создаёт пилот, цену, SLA, production access или customer commitment по импликации.

## 8. Язык, терминология и публичная граница

Для новых человекочитаемых Company-документов действует русскоязычный режим и `docs/governance/TERMINOLOGY-GLOSSARY.md`.

Технические идентификаторы, code/API names и машинные материалы могут оставаться на английском, если их смысл не расходится с утверждённой терминологией.

Этот публичный репозиторий не является местом хранения секретов, reusable credentials, private keys, избыточных персональных данных, банковских/платёжных реквизитов, непубличных договорных материалов или customer-confidential payloads.

## 9. Конечный этап M9

`M9 — Человекочитаемая документация полностью русифицирована и согласована` остаётся самым последним плановым этапом после M8, если собственник отдельно не изменит последовательность.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` остаётся `Planned` и не подменяет текущую AC-307/M3 работу.
