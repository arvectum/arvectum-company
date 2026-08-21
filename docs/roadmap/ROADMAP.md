# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.27.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-306 — Portfolio prioritization by capital, economics and Owner attention`
Русское название текущего действия: `Приоритизация портфеля по капиталу, экономике и вниманию собственника`

## 1. Модель публикации

Эта редакция `0.27.0` сохраняет полное содержание дорожной карты `0.26.0` по неизменяемой ссылке на git blob и добавляет закрытие AC-305 с переводом текущего действия на AC-306.

Предыдущая редакция:

- версия: `0.26.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `d4f57d03cf5ae3a500035eba67259cce4f6da6a9`.

Все ранее определённые этапы M0–M9, принципы приоритизации, границы Company/Product/Arvectum OS, параллельные циклы и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-305

`AC-305 — Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS` имеет статус:

`Complete / PASS`.

Утверждённая Company publication:

- `docs/portfolio/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-RECONCILIATION-v1.0.0.md` — `Approved 1.0.0`;
- exact reviewed proposal: `docs/portfolio/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-RECONCILIATION.md` — `Proposed 0.9.0`, blob `c27973c48b7bb5306e36f71d0f1007fc41896de9`;
- cross-review: `docs/reviews/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-CROSS-REVIEW.md` — `7 of maximum 7`, PASS, blob `369c42f8066ac8a10d3b00a0afd2fc034b8c7fe3`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-305-APPROVAL.md`.

Связанный Arvectum OS governance action также утверждён:

- `arvectum/arvectum-os/docs/contracts/P6-02-REPOSITORY-LOCATOR-RECONCILIATION-v1.0.0.md` — `Approved 1.0.0`;
- approved reviewed proposal blob: `95f32a2625a3df2c18615021aa2ca46f83faa946`;
- OS Owner decision: `arvectum/arvectum-os/docs/governance/decisions/DECISION-2026-08-21-P6-02-REPOSITORY-LOCATOR-RECONCILIATION-APPROVAL.md`.

Канонический portfolio map синхронизирован:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.6.0`.

## 3. Главные результаты AC-305

Утверждено:

- между `PORT-001…PORT-007` не установлено ни одной обязательной hard runtime/code/data dependency;
- `PORT-005 → PORT-001` является selective procurement-family reuse/evidence relation, а не runtime coupling или product merge;
- `PORT-002`, `PORT-006` и `PORT-007` не образуют автоматически shared parser/runtime/datastore/platform;
- `PORT-007` остаётся clarification-only Company/product-family module candidate и не является operational dependency;
- `PORT-003` не является скрытой Company-wide/OS инфраструктурной зависимостью;
- common owner, common stack, similarity и reference status сами по себе dependency не создают.

Текущая OS reliance matrix:

| Portfolio node | OS boundary | Exact dependency |
|---|---|---|
| `PORT-001 — Arvectum Tender Agent` | `P6.02` + supplemental `P8.03` | `CAP-001 + CAP-004` в exact bounded scopes |
| `PORT-002 — Discount Parser` | `P6.06` | `CAP-004 only` |
| `PORT-004 — Creative Test Agent` | `P8.06` optional external extension | `CAP-004 only` |
| `PORT-003` | none | none inferred |
| `PORT-005` | none | none inferred |
| `PORT-006` | none | none inferred |
| `PORT-007` | none | none inferred |

`RI-OS-CONSUMER` остаётся evidence/reuse classification, а не blanket OS dependency всего продукта.

## 4. P6.02 locator reconciliation closed

Stale P6.02 locator теперь reconciled через надлежащий Arvectum OS governance path:

- historical/predecessor locator: `arutyunoveth/ai-corporation`;
- current implementation locator: `arvectum/tender-agent`;
- Company correspondence: `PORT-001 — Arvectum Tender Agent`.

Это locator/provenance reconciliation only. P6.02 остаётся `Provisional 0.1.0`; Product Identity, semantic boundary, CAP-001/CAP-004 dependency set, authority/data/security restrictions и P8.03 continuity не изменены.

Исторический P6.02 artifact не переписывается задним числом; approved OS reconciliation publication является current resolver overlay.

## 5. Phase 3 — управление портфелем и кандидатами в повторно используемые модули

Этап: `M3 — Product/module-candidate portfolio governed as investments`.

Текущий план Phase 3:

| ID | Работа | Статус |
|---|---|---|
| `AC-301` | Сверка идентичности, границ и владения продуктами и инициативами портфеля | `Complete / PASS` |
| `AC-302` | Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой | `Complete / PASS` |
| `AC-303` | Границы инвестиций, затрат и рисков; критерии продолжить/изменить/остановить | `Complete / PASS` |
| `AC-304` | Разделение: самостоятельный продукт / эталонная реализация / кандидат в модуль / кандидат в возможность Arvectum OS | `Complete / PASS` |
| `AC-305` | Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS | `Complete / PASS` |
| `AC-306` | Приоритизация портфеля по капиталу, экономике и вниманию собственника | `Current` |
| `AC-307` | Итоговая проверка управления портфелем и закрытие M3 | `Planned` |

## 6. Текущее действие — AC-306

### AC-306 — Portfolio prioritization by capital, economics and Owner attention

Статус: `Current`.

Цель: ранжировать `PORT-001…PORT-007` как инвестиционный портфель с учётом уже утверждённых identity, accountability, investment boundaries, role/reuse classification и dependency/Product Contract state.

AC-306 должен как минимум:

- отделить обязательства/continuity от discretionary growth investment;
- оценить ближайший client/revenue/value path по каждому node;
- учитывать cash и recurring cost, engineering effort и operational burden;
- учитывать expected value, unit economics и evidence quality;
- учитывать downside, reversibility, security/data/legal/IP/sovereignty exposure;
- учитывать dependency/lock-in и replacement path;
- учитывать Owner attention как ограниченный капитал, а не бесплатный ресурс;
- определить relative priority bands и stop/defer/continue/change recommendations;
- не превращать ranking в автоматическую authorisation spending/customer commitment;
- сохранить `contain` для PORT-005/006 и `clarify before investment` для PORT-007, пока отдельное evidence не обосновывает изменение;
- оставить M3 final review/closure для AC-307.

## 7. Границы AC-306

AC-306 может подготовить portfolio ranking и decision recommendations, но сам по себе не:

- создаёт budget или spend authorization;
- заключает customer/vendor commitments;
- меняет legal/IP/data rights;
- меняет Product Contract Arvectum OS;
- создаёт shared module или Platform Capability;
- меняет product implementation roadmap без product-side decision;
- отменяет AC-301…AC-305 без нового evidence/governance action.

## 8. Напоминание о полномочиях

Дорожная карта координирует работу, но не создаёт организационные или юридические полномочия. Material capital allocation, material risk acceptance, существенные Company↔Product↔OS commitments и иные Reserved Owner Decisions требуют соответствующего явного решения уполномоченного Principal.
