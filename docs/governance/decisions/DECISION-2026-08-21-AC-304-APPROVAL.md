# Решение собственника — утверждение AC-304

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`

## 1. Явное решение

Собственник явно утвердил AC-304 формулировкой:

> `AC-304 утверждаю`

Утверждение относится к точной проверенной редакции:

- документ: `docs/portfolio/AC-304-PORTFOLIO-ROLE-CLASSIFICATION.md`;
- статус: `Proposed 0.9.0`;
- git blob SHA: `533ccef1d28bf9a154da9b99dd1c4226c19d166b`;
- перекрёстная проверка: `docs/reviews/AC-304-PORTFOLIO-ROLE-CLASSIFICATION-CROSS-REVIEW.md`;
- результат проверки: `10 of maximum 10`, `Complete / PASS for Owner approval`;
- git blob SHA cross-review: `94c70f2d9f168f54e4d4f948b754b22d177872ec`.

Указанные immutable blob SHA фиксируют именно ту редакцию и тот cross-review, которые были представлены собственнику перед утверждением.

## 2. Утверждённая модель классификации

Собственник утверждает разделение четырёх разных Company-level ролей:

1. `Standalone product` — самостоятельная продуктовая идентичность и product-owned lifecycle/domain semantics;
2. `Reference implementation` — существующая реализация или bounded experiment, намеренно сохраняемый как evidence/reference;
3. `Company/product-family module candidate` — гипотеза повторно используемого механизма выше отдельных продуктов, но ниже Arvectum OS;
4. `Company-side OS capability candidate` — только promotion hypothesis для отдельного Arvectum OS governance path, не lifecycle status OS.

Одна сущность может одновременно быть самостоятельным продуктом и референсной реализацией. Сам факт repository reuse, общего стека, code similarity или названия `platform` не создаёт module/platform status.

## 3. Утверждённая классификационная матрица

| ID | Standalone product | Reference implementation | Company/product-family module candidate | Company-side OS capability candidate | Основная роль |
|---|---|---|---|---|---|
| `PORT-001` | `YES` | `YES — RI-OS-CONSUMER` | `NO` | `NO` | самостоятельный продукт + референсный consumer Arvectum OS |
| `PORT-002` | `YES` | `YES — RI-OS-CONSUMER + RI-PRODUCT-FAMILY` | `NO` | `NO` | самостоятельный продукт + референсная реализация для OS и parser/data-extraction family evidence |
| `PORT-003` | `YES` | `NO` | `NO` | `NO` | самостоятельный продукт |
| `PORT-004` | `YES` | `YES — RI-OS-CONSUMER` | `NO` | `NO` | самостоятельный продукт + референсный внешний consumer Arvectum OS |
| `PORT-005` | `NO` | `YES — RI-PRODUCT-FAMILY` | `NO` | `NO` | contained procurement reference implementation / evidence source |
| `PORT-006` | `NO` | `YES — RI-PRODUCT-FAMILY` | `NO` | `NO` | contained completed-delivery reference implementation / evidence source |
| `PORT-007` | `NO` | `NO` | `YES — clarification-only candidate` | `NO` | кандидат в Company/product-family data acquisition/extraction module; не platform status |

В текущем портфеле ни один `PORT-*` не утверждается как Company-side кандидат в новую Platform Capability Arvectum OS.

## 4. Ключевые последствия

### `PORT-001 — Arvectum Tender Agent`

Сохраняется самостоятельным продуктом и одновременно является `RI-OS-CONSUMER`, поскольку bounded Tender Agent workflow уже используется как реальный Product Contract validation target Arvectum OS. Это не превращает tender/domain semantics в OS capability.

### `PORT-002 — Discount Parser`

Сохраняется самостоятельным продуктом. Одновременно является `RI-OS-CONSUMER` и `RI-PRODUCT-FAMILY`: существующий продукт даёт evidence как для Product Contract/OS validation, так и для будущего parser/data-extraction family design. Весь продукт не становится shared module.

### `PORT-003 — Arvectum Proxy Launcher`

Сохраняется самостоятельным продуктом. Текущего evidence недостаточно для отдельной reference/module/OS-candidate роли.

### `PORT-004 — Creative Test Agent`

Сохраняется самостоятельным продуктом и `RI-OS-CONSUMER` как внешний consumer Arvectum OS. Его marketing/creative semantics остаются product-owned.

### `PORT-005 — Tender Small-Volume Calculator`

Не получает active standalone-product role в AC-304. Сохраняется contained `RI-PRODUCT-FAMILY` / evidence source для procurement-family reuse без автоматического merge с Tender Agent и без growth mandate.

### `PORT-006 — Doors Parser`

Не получает active standalone-product role в AC-304. Сохраняется contained completed-delivery `RI-PRODUCT-FAMILY` / evidence source. Не объединяется автоматически с Discount Parser и не становится generic parser.

### `PORT-007 — Data Platform`

Утверждается только как `clarification-only` Company/product-family module candidate для bounded data acquisition/extraction гипотезы. Это не разрешение на material implementation, infrastructure, shared data contracts, data lake/vector/search build или Arvectum OS admission.

## 5. Граница Arvectum OS

AC-304 не создаёт lifecycle `Candidate`, `Incubating` или `Active` в Arvectum OS.

Существующие real Product Contract consumers остаются evidence для уже существующих OS capability/contracts. Любая новая OS capability promotion требует отдельного Arvectum OS governance path и должна удовлетворять domain-neutral reuse/admission criteria OS.

## 6. Сохранённые границы

Утверждение AC-304:

- не меняет AC-301 `PORT-*` identities и dispositions;
- не меняет AC-302 `PORT-* → POS-003` accountability mapping;
- не меняет AC-303 investment/cost/risk treatments;
- не переносит код, schemas, customer data или history между продуктами;
- не создаёт shared library/service/runtime;
- не создаёт и не меняет Product Contract Arvectum OS;
- не разрешает budget, spending, hiring, customer commitment или production deployment;
- не доказывает legal/IP/data rights;
- не выполняет AC-305 dependency/Product Contract reconciliation;
- не выполняет AC-306 capital/economics/Owner-attention prioritization.

## 7. Следующий этап

После публикации AC-304 как Approved и синхронизации `PORTFOLIO.md` и canonical roadmap следующим действием становится:

`AC-305 — Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS`.

Отдельно в AC-305 должен быть reconciled устаревший repository locator `arutyunoveth/ai-corporation` в P6.02 через надлежащий Arvectum OS governance path, без Company-side silent rewrite.

## 8. Границы решения

Это решение является Company-internal governance approval. Оно не заменяет product decisions, юридически необходимые корпоративные действия, права на данные/IP, customer approvals или Arvectum OS governance approvals, когда соответствующая сфера требует отдельного решения.
