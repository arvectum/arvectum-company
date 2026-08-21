# Решение собственника — утверждение AC-301

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`

## 1. Явное решение

Собственник явно утвердил AC-301 формулировкой:

> `AC-301 утверждаю.`

Утверждение относится к точной проверенной редакции:

- документ: `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION.md`;
- статус: `Proposed 0.9.0`;
- git blob SHA: `146b5868a21c09cf20b633e309e587b7a631ad32`;
- перекрёстная проверка: `docs/reviews/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-CROSS-REVIEW.md`;
- результат проверки: `10 of maximum 10`, `Complete / PASS for Owner approval`;
- review blob SHA: `b9a15ba2acc6c15f90c9b83d857e43942fd66ce8`.

## 2. Утверждённый результат

Собственник утверждает Company-level сверку семи существенных узлов портфеля и следующие устойчивые идентичности/состояния:

| ID | Основное имя | Текущий тип | Disposition |
|---|---|---|---|
| `PORT-001` | `Arvectum Tender Agent` | самостоятельный продукт | `continue` |
| `PORT-002` | `Discount Parser` | productized client solution / продукт с клиентским delivery contour | `continue` |
| `PORT-003` | `Arvectum Proxy Launcher` | самостоятельный продукт | `continue` |
| `PORT-004` | `Creative Test Agent` | самостоятельный продукт / controlled-pilot solution | `continue` |
| `PORT-005` | `Tender Small-Volume Calculator` | product experiment / локальный procurement MVP | `contain` |
| `PORT-006` | `Doors Parser` | client-delivery solution / завершённый product experiment | `contain` |
| `PORT-007` | `Data Platform` | внутренняя инициатива на стадии определения | `clarify` |

Утверждается правило, что `PORT-*` является устойчивой Company-level identity узла, тогда как repository path является каноническим locator реализации и может изменяться без автоматического создания нового продукта.

Организационное владение продуктом со стороны ООО «Арвектум» не является доказательством legal/IP title, прав на клиентские данные или иных исключительных/договорных прав.

## 3. Утверждённые границы

Утверждение сохраняет разделение сфер:

- Company определяет portfolio role, sponsorship, инвестиционное направление и соответствующие организационные решения в пределах Company authority;
- product repository остаётся каноническим для product-specific semantics, implementation, product roadmap, release и operational evidence;
- Arvectum OS остаётся каноническим для domain-neutral platform semantics, Product Contracts, capability lifecycle и governed platform behavior;
- наличие repository, GitHub admin permission, AI runtime или Product Contract само по себе не создаёт Organizational Authority или юридическое право.

Никакие потенциальные продуктовые семьи или reusable modules этим решением автоматически не создаются.

## 4. Специальные reconciliation conclusions

1. `Arvectum Tender Agent` и `Tender Small-Volume Calculator` остаются двумя разными `PORT-*` identities; merge/retirement не утверждаются.
2. Старый locator `arutyunoveth/ai-corporation` в OS Product Contract P6.02 признаётся stale locator относительно текущего `arvectum/tender-agent`; сам OS artifact этим Company decision не изменяется. Исправление относится к AC-305 и применимому Arvectum OS governance path.
3. `Discount Parser`, `Doors Parser` и `Data Platform` не объединяются автоматически в `Universal Parser`, `Arvectum Parser`, общий reusable module или OS capability.
4. `Creative Test Agent` не переименовывается в `Marketing Agent` без отдельного product-scope decision.
5. Название `Data Platform` само по себе не придаёт инициативе platform/OS status.

## 5. Границы решения

Это решение не:

- создаёт или меняет Position/Assignment;
- утверждает бюджет, цену, ROI, profitability, SLA или промышленную готовность;
- прекращает, продаёт или объединяет продукт;
- признаёт продукт reusable module или OS capability;
- изменяет Product Contract, RFC, ADR или lifecycle Arvectum OS;
- устанавливает legal/IP ownership;
- создаёт клиентские или иные внешние обязательства.

`continue / contain / clarify` являются bounded portfolio identity/boundary dispositions AC-301 и не заменяют инвестиционные решения AC-303/AC-306.

## 6. Следующий шаг

AC-301 закрывается как `Complete / PASS`.

Следующее каноническое действие дорожной карты:

`AC-302 — Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой`.
