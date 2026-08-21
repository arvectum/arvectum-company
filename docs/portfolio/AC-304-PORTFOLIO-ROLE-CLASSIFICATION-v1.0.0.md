# AC-304 — Разделение: самостоятельный продукт / эталонная реализация / кандидат в модуль / кандидат в возможность Arvectum OS

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-304 — Standalone product / reference implementation / module candidate / Arvectum OS capability candidate classification`
Approval: `docs/governance/decisions/DECISION-2026-08-21-AC-304-APPROVAL.md`
Cross-review: `docs/reviews/AC-304-PORTFOLIO-ROLE-CLASSIFICATION-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `533ccef1d28bf9a154da9b99dd1c4226c19d166b`

## 1. Модель утверждённой публикации

Эта публикация фиксирует утверждение точной проверенной редакции AC-304 без переписывания прошедшего cross-review текста задним числом.

Утверждённая исходная редакция:

- файл: `docs/portfolio/AC-304-PORTFOLIO-ROLE-CLASSIFICATION.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `533ccef1d28bf9a154da9b99dd1c4226c19d166b`.

Перекрёстная проверка:

- файл: `docs/reviews/AC-304-PORTFOLIO-ROLE-CLASSIFICATION-CROSS-REVIEW.md`;
- iterations: `10 of maximum 10`;
- result: `Complete / PASS for Owner approval`;
- immutable git blob SHA: `94c70f2d9f168f54e4d4f948b754b22d177872ec`.

Решение собственника:

- `docs/governance/decisions/DECISION-2026-08-21-AC-304-APPROVAL.md` — `Approved`;
- явная формулировка: `AC-304 утверждаю`.

Нормативное содержание `Proposed 0.9.0` включается в эту публикацию в полном объёме по указанному immutable blob SHA и считается утверждённым в пределах заявленного scope.

## 2. Утверждённая семантика ролей

AC-304 различает четыре независимые Company-level классификации:

- `Standalone product` — самостоятельная продуктовая идентичность и product-owned lifecycle/domain semantics;
- `Reference implementation` — существующая реализация или bounded experiment, намеренно сохраняемые как evidence/reference;
- `Company/product-family module candidate` — Company-level promotion hypothesis для повторно используемого механизма выше отдельных продуктов, но ниже Arvectum OS;
- `Company-side OS capability candidate` — только гипотеза для отдельного Arvectum OS governance review, не lifecycle status Arvectum OS.

Самостоятельный продукт может одновременно быть reference implementation. Ни repository reuse, ни общий стек, ни сходство кода, ни слово `platform` сами по себе не создают module/platform status.

## 3. Утверждённая матрица

| ID | Standalone product | Reference implementation | Company/product-family module candidate | Company-side OS capability candidate | Основная роль AC-304 |
|---|---|---|---|---|---|
| `PORT-001` | `YES` | `YES — RI-OS-CONSUMER` | `NO` | `NO` | самостоятельный продукт + референсный consumer Arvectum OS |
| `PORT-002` | `YES` | `YES — RI-OS-CONSUMER + RI-PRODUCT-FAMILY` | `NO` | `NO` | самостоятельный продукт + референсная реализация для OS и parser/data-extraction family evidence |
| `PORT-003` | `YES` | `NO` | `NO` | `NO` | самостоятельный продукт |
| `PORT-004` | `YES` | `YES — RI-OS-CONSUMER` | `NO` | `NO` | самостоятельный продукт + референсный внешний consumer Arvectum OS |
| `PORT-005` | `NO` | `YES — RI-PRODUCT-FAMILY` | `NO` | `NO` | contained procurement reference implementation / evidence source |
| `PORT-006` | `NO` | `YES — RI-PRODUCT-FAMILY` | `NO` | `NO` | contained completed-delivery reference implementation / evidence source |
| `PORT-007` | `NO` | `NO` | `YES — clarification-only candidate` | `NO` | кандидат в Company/product-family data acquisition/extraction module; не platform status |

В текущем Company portfolio нет ни одного нового Company-side кандидата в Platform Capability Arvectum OS.

## 4. Утверждённые reuse conclusions

1. `PORT-001`, `PORT-002` и `PORT-004` являются реальными reference consumers Arvectum OS в пределах уже существующих Provisional Product Contract contours. Они не являются реализациями самих OS capabilities.
2. `PORT-002`, `PORT-005` и `PORT-006` дают product-family reuse evidence, но не образуют автоматически shared parser/module/platform.
3. `PORT-005` и `PORT-006` сохраняются как contained reference implementations/evidence sources; reference status не создаёт growth mandate.
4. `PORT-007` является только clarification-only module candidate для bounded data acquisition/extraction hypothesis. Material build не разрешается этой классификацией.
5. `PORT-003` остаётся standalone-only в текущем evidence baseline.

## 5. Arvectum OS boundary

Утверждение AC-304 не меняет Arvectum OS lifecycle и не создаёт capability `Candidate`, `Incubating` или `Active`.

Product-domain semantics остаются product-owned. Domain-neutral Platform Capability admission и promotion остаются исключительно Arvectum OS governance scope.

Существующие Product Contract evidence contours:

- Tender Agent — реальный Product Contract consumer CAP-001/CAP-004;
- Discount Parser — отдельный Product Contract contour с CAP-004 и внешним effect/reconciliation pressure;
- Creative Test Agent — внешний CAP-004 consumer.

Эти contours являются reuse evidence для существующих OS mechanisms, а не основанием переносить целые продукты в platform ownership.

## 6. Сохранённые Company boundaries

AC-304 не изменяет:

- AC-301 identities/dispositions;
- AC-302 accountable-Position mapping;
- AC-303 investment/cost/risk treatments;
- `ROD-*`, delegated authority, Assignments, access или continuity boundaries;
- product-specific canonical implementation/status sources;
- legal/IP/data/customer authority;
- OS Product Contracts или capability lifecycle.

AC-304 не создаёт budget, shared implementation, repository merge, data migration, production deployment или customer commitment.

## 7. Downstream governance

Следующие вопросы остаются намеренно downstream:

- `AC-305` — межпродуктовые зависимости и Product Contract reconciliation с Arvectum OS, включая stale P6.02 repository locator `arutyunoveth/ai-corporation`;
- `AC-306` — относительная приоритизация портфеля по капиталу, экономике и Owner attention;
- `AC-307` — итоговая проверка M3.

## 8. Результат

`AC-304 — Complete / PASS`.

Следующее каноническое действие:

`AC-305 — Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS`.
