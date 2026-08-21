# AC-301 — Сверка идентичности, границ и владения продуктами и инициативами портфеля

Статус: `Approved`
Версия: `1.0.0`
Дата утверждения: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-301 — Portfolio product/node identity and ownership reconciliation`

## 1. Модель утверждённой публикации

Эта публикация фиксирует утверждение точной проверенной редакции AC-301 без переписывания прошедшего cross-review текста задним числом.

Утверждённая исходная редакция:

- файл: `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION.md`;
- статус исходной редакции: `Proposed 0.9.0`;
- immutable git blob SHA: `146b5868a21c09cf20b633e309e587b7a631ad32`.

Перекрёстная проверка:

- файл: `docs/reviews/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-CROSS-REVIEW.md`;
- iterations: `10 of maximum 10`;
- result: `Complete / PASS for Owner approval`;
- blob SHA: `b9a15ba2acc6c15f90c9b83d857e43942fd66ce8`.

Решение собственника:

- `docs/governance/decisions/DECISION-2026-08-21-AC-301-APPROVAL.md` — `Approved`.

Нормативное содержание `Proposed 0.9.0` включается в эту публикацию по указанному immutable blob SHA и считается утверждённым в полном объёме в пределах заявленного scope.

## 2. Утверждённая карта идентичности

| ID | Основное Company-level имя | Тип | Canonical repository | Disposition |
|---|---|---|---|---|
| `PORT-001` | `Arvectum Tender Agent` | самостоятельный продукт | `arvectum/tender-agent` | `continue` |
| `PORT-002` | `Discount Parser` | productized client solution / продукт с клиентским delivery contour | `arvectum/discount-parser` | `continue` |
| `PORT-003` | `Arvectum Proxy Launcher` | самостоятельный продукт | `arvectum/proxy-launcher` | `continue` |
| `PORT-004` | `Creative Test Agent` | самостоятельный продукт / controlled-pilot solution | `arvectum/creative-test-agent` | `continue` |
| `PORT-005` | `Tender Small-Volume Calculator` | product experiment / локальный procurement MVP | `arvectum/tender-app` | `contain` |
| `PORT-006` | `Doors Parser` | client-delivery solution / завершённый product experiment | `arvectum/doors_parser` | `contain` |
| `PORT-007` | `Data Platform` | внутренняя инициатива на стадии определения | `arvectum/data-platform` | `clarify` |

`PORT-*` является устойчивой Company-level identity. Repository path является locator реализации и не определяет саму продуктовую идентичность.

## 3. Границы утверждения

AC-301 утверждает identity/boundary/organizational-ownership baseline, но не подменяет последующие Phase 3 gates.

В частности:

- accountable Position и Assignment относятся к AC-302;
- investment/cost/risk boundaries и stop/change/continue criteria — к AC-303;
- product/reference implementation/module/OS-capability classification — к AC-304;
- cross-product dependencies и OS Product Contract reconciliation — к AC-305;
- capital/economics/Owner-attention prioritization — к AC-306.

Организационное владение ООО «Арвектум» не является юридическим доказательством исключительных прав, прав на данные или иных договорных прав.

## 4. Reconciliation conclusions

Утверждены следующие ограничения:

- `Arvectum Tender Agent` и `Tender Small-Volume Calculator` не объединяются автоматически;
- stale locator `arutyunoveth/ai-corporation` в P6.02 должен исправляться через AC-305 и Arvectum OS governance, а не Company-side silent rewrite;
- `Discount Parser`, `Doors Parser` и `Data Platform` не образуют автоматически generic parser/module/platform;
- `Creative Test Agent` не становится `Marketing Agent` без отдельного product decision;
- `Data Platform` не получает OS/platform status по названию.

## 5. Результат

`AC-301 — Complete / PASS`.

Следующее каноническое действие:

`AC-302 — Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой`.
