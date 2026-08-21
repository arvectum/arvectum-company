# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `2.8.0`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `2.7.0` по immutable git blob и добавляет утверждение AC-307, закрытие M3 и переход к M4/AC-401.

Предыдущая редакция:

- версия: `2.7.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `80a6e1c03cf4b7d15dcc93dc5dd92b7c9b7b189e`.

Все ранее зарегистрированные источники M0–M2, AC-201–AC-208, языково-терминологическая политика, Company/Product/Arvectum OS boundaries и правила внешних источников сохраняются без изменений, если прямо не уточнены более новым утверждённым артефактом.

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

- `docs/roadmap/ROADMAP.md` — `Active 0.29.0`;
- текущий blob SHA: `d66f04e9b5b7636683b8bc3007967ccbe346d89c`.

Текущее каноническое действие:

`AC-401 — Company work/obligation register model`.

Текущий этап:

`M4 — Owner control and reference-implementation observability established`.

Полный план M0–M8 восходит к сохранённой roadmap chain; финальный M9/AC-901 остаётся последним плановым этапом после M8.

## 4. Действующий портфель

Канонический Company-level portfolio source:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.8.0`;
- текущий blob SHA: `8a77be35225f9c8c4958531e52a4131abda13d0f`;
- current governance baseline: `AC-307 — Approved 1.0.0 / M3 Complete / PASS`.

Approved M3 closure sources:

- `docs/portfolio/AC-307-PORTFOLIO-GOVERNANCE-REVIEW-AND-M3-CLOSURE-v1.0.0.md` — `Approved 1.0.0`, blob `ff9a07d8c7161bfdaf3628e1c8e21d2a2d0f4435`;
- reviewed proposal blob `904b9e5ffa12caeb082b3bf23a89aff251ebe8c4`;
- cross-review blob `bc3c4992f12dabaeb155f055373da292278cd791`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-307-APPROVAL-AND-M3-CLOSURE.md`.

Approved Phase 3 publications AC-301…AC-306 остаются binding layers текущего portfolio baseline.

## 5. M3 closure meaning

`M3 — Product/module-candidate portfolio governed as investments` имеет статус `Complete / PASS`.

Current governed state:

- `PORT-001` Tender Agent — `continue`, standalone + `RI-OS-CONSUMER`, `A2`;
- `PORT-002` Discount Parser — `continue`, standalone + `RI-OS-CONSUMER + RI-PRODUCT-FAMILY`, `A1`;
- `PORT-003` Proxy Launcher — `continue`, standalone, named-trigger `B1`;
- `PORT-004` Creative Test Agent — `continue`, standalone + `RI-OS-CONSUMER`, named-trigger `B2`;
- `PORT-005` Tender Small-Volume Calculator — `contain`, `RI-PRODUCT-FAMILY`, `D1`;
- `PORT-006` Doors Parser — `contain`, `RI-PRODUCT-FAMILY`, `D2`;
- `PORT-007` Data Platform — `clarify`, clarification-only Company/product-family module candidate, `C1`, no material build.

Между `PORT-*` не установлено обязательной hard runtime/code/data dependency. AC-306 ranking не является бюджетом. Product repositories остаются canonical для implementation/status/domain semantics; Arvectum OS — для Product Contracts/platform semantics.

## 6. Arvectum OS correspondence

Текущая Company interpretation применимых OS boundaries остаётся:

- `PORT-001` — P6.02 + P8.03, exact bounded reliance on `CAP-001 + CAP-004`;
- `PORT-002` — P6.06, `CAP-004 only`;
- `PORT-004` — P8.06 optional external extension, `CAP-004 only`.

P6.02 repository locator reconciled в `arvectum/arvectum-os` отдельным Approved locator/provenance overlay: current implementation locator `arvectum/tender-agent`, historical predecessor `arutyunoveth/ai-corporation`. P6.02 semantic contract остаётся `Provisional 0.1.0`.

## 7. Статус этапов

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3` — `Complete / PASS`;
- `M4` — `Current`, AC-401 `Current`;
- `M5` — `Planned`;
- `M6` — `Planned`;
- `M7` — `Future`;
- `M8` — `Future`;
- `M9` — финальный плановый этап, AC-901 `Planned` после M8.

Параллельный bounded AC-108 discovery loop остаётся источником рыночных данных и не создаёт pilot, price, SLA, production access или customer commitment по импликации.

## 8. M4 navigation

M4 должен сформировать Owner control/reference-observability layer без преждевременного dashboard theater.

План M4:

1. `AC-401` — Company work/obligation register model — `Current`;
2. `AC-402` — Decision, approval and escalation register model;
3. `AC-403` — Risk, exception and incident register model;
4. `AC-404` — Cash, commitment and management reporting baseline;
5. `AC-405` — Portfolio/module/priority review cadence;
6. `AC-406` — Owner Mission Control / reference-implementation evidence view;
7. `AC-407` — Management operating cadence and control review.

## 9. Язык, терминология и публичная граница

Для новых человекочитаемых Company-документов действует русскоязычный режим и `docs/governance/TERMINOLOGY-GLOSSARY.md`.

Этот публичный репозиторий не является местом хранения секретов, reusable credentials, private keys, избыточных персональных данных, банковских/платёжных реквизитов, непубличных договорных материалов или customer-confidential payloads.

## 10. Конечный этап M9

`M9 — Человекочитаемая документация полностью русифицирована и согласована` остаётся самым последним плановым этапом после M8, если собственник отдельно не изменит последовательность.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` остаётся `Planned`.