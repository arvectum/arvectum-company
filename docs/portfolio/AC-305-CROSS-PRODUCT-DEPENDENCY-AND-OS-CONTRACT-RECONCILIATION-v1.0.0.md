# AC-305 — Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-305 — Inter-product dependency and Arvectum OS Product Contract reconciliation`
Approval: `docs/governance/decisions/DECISION-2026-08-21-AC-305-APPROVAL.md`
Cross-review: `docs/reviews/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `c27973c48b7bb5306e36f71d0f1007fc41896de9`
Related Arvectum OS proposal: blob `95f32a2625a3df2c18615021aa2ca46f83faa946`

## 1. Модель утверждённой публикации

Эта публикация фиксирует утверждение точной проверенной редакции AC-305 без переписывания прошедшего cross-review текста задним числом.

Утверждённая исходная редакция:

- файл: `docs/portfolio/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-RECONCILIATION.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `c27973c48b7bb5306e36f71d0f1007fc41896de9`.

Перекрёстная проверка:

- файл: `docs/reviews/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-CROSS-REVIEW.md`;
- iterations: `7 of maximum 7`;
- result: `Complete / PASS for dual Owner approval`;
- immutable git blob SHA: `369c42f8066ac8a10d3b00a0afd2fc034b8c7fe3`.

Решение собственника:

- `docs/governance/decisions/DECISION-2026-08-21-AC-305-APPROVAL.md` — `Approved`;
- явная формулировка: `AC-305 и P6.02 repository locator reconciliation в Arvectum OS утверждаю`.

Нормативное содержание `Proposed 0.9.0` включается в эту публикацию в полном объёме по указанному immutable blob SHA и считается утверждённым в пределах заявленного scope.

## 2. Утверждённый cross-product dependency result

В текущем canonical evidence baseline не установлено ни одной обязательной hard runtime/code/data dependency между `PORT-001…PORT-007`.

Утверждены следующие отношения:

- `PORT-005 — Tender Small-Volume Calculator` является selective procurement-family reference/evidence source для `PORT-001 — Arvectum Tender Agent`; монолитная code/runtime dependency отсутствует;
- `PORT-002 — Discount Parser` и `PORT-006 — Doors Parser` дают parser/data-acquisition family evidence, но не образуют shared runtime, shared datastore или generic parser автоматически;
- `PORT-007 — Data Platform` остаётся только `clarification-only` Company/product-family module candidate и не является действующей dependency для других продуктов;
- `PORT-003 — Arvectum Proxy Launcher` остаётся standalone-only в текущем dependency evidence и не считается обязательной инфраструктурой других portfolio nodes;
- common owner, common technology stack, code similarity и reference classification сами по себе не создают dependency.

## 3. Утверждённая карта Product Contracts Arvectum OS

| Portfolio node | Canonical product repository | OS Product / integration boundary | Exact dependency |
|---|---|---|---|
| `PORT-001 — Arvectum Tender Agent` | `arvectum/tender-agent` | `P6.02 — Provisional 0.1.0`; `P8.03 — Provisional 0.1.0` supplemental | `CAP-001 + CAP-004` в declared bounded scopes |
| `PORT-002 — Discount Parser` | `arvectum/discount-parser` | `P6.06 — Provisional 0.1.0` | `CAP-004 only` |
| `PORT-004 — Creative Test Agent` | `arvectum/creative-test-agent` | `P8.06 — Provisional 0.1.0`, optional external extension | `CAP-004 only` |
| `PORT-003 — Arvectum Proxy Launcher` | `arvectum/proxy-launcher` | none evidenced | none inferred |
| `PORT-005 — Tender Small-Volume Calculator` | `arvectum/tender-app` | none evidenced | none inferred |
| `PORT-006 — Doors Parser` | `arvectum/doors_parser` | none evidenced | none inferred |
| `PORT-007 — Data Platform` | `arvectum/data-platform` | none evidenced | none inferred |

`RI-OS-CONSUMER` означает реальный product-side validation/consumer contour, а не обязательную OS dependency всего продукта и не реализацию OS capability самим продуктом.

## 4. P6.02 repository locator reconciliation

AC-305 подтверждает Company-side identity correspondence:

- Company node: `PORT-001 — Arvectum Tender Agent`;
- current canonical implementation repository: `arvectum/tender-agent`;
- predecessor/historical locator in P6.02: `arutyunoveth/ai-corporation`.

Поскольку P6.02 является Arvectum OS canonical artifact, Company approval не переписывает его самостоятельно. Связанная exact proposal revision `95f32a2625a3df2c18615021aa2ca46f83faa946` утверждена собственником отдельно в Arvectum OS governance scope и публикуется там как locator/provenance reconciliation overlay.

Locator reconciliation не меняет P6.02 semantic Product Contract boundary, lifecycle или version identity. P6.02 остаётся `Provisional 0.1.0`; P8.03 сохраняет continuity без искусственного cascade version bump.

## 5. Boundary preservation

AC-305 не создаёт:

- repository merge;
- product merge;
- cross-product shared mutable state;
- shared library/service/runtime;
- code/data/history transfer authorization;
- новую Platform Capability;
- новый Product Contract вне отдельного OS governance action;
- Stable/Active lifecycle promotion;
- funding, budget или priority order;
- customer/legal/IP/data authority expansion.

AC-301 identities/dispositions, AC-302 accountability, AC-303 investment treatment и AC-304 role classification остаются в силе.

## 6. Source-of-truth rule

- Company governance остаётся canonical для `PORT-*` identity, portfolio relationship и Company-level dependency interpretation;
- product repositories остаются canonical для product-specific implementation/status/domain semantics;
- `arvectum/arvectum-os` остаётся canonical для Product Contracts, capability lifecycle и platform dependency semantics;
- selective reuse evidence не является скрытым cross-repository contract;
- любое новое material cross-product operational reliance требует явного contract/ownership/economic/risk review до появления скрытой зависимости.

## 7. Результат

`AC-305 — Complete / PASS`.

Следующее каноническое действие:

`AC-306 — Приоритизация портфеля по капиталу, экономике и вниманию собственника`.
