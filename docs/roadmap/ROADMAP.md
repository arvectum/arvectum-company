# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.28.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-307 — Final portfolio governance review and M3 closure`
Русское название текущего действия: `Итоговая проверка управления портфелем и закрытие M3`

## 1. Модель публикации

Эта редакция `0.28.0` сохраняет полное содержание дорожной карты `0.27.0` по immutable git blob и добавляет утверждение/закрытие AC-306 с переводом текущего действия на AC-307.

Предыдущая редакция:

- версия: `0.27.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `afad4b60275c207008c06c569a292dc8bec2cb28`.

Все ранее определённые этапы M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, параллельные evidence loops и конечный AC-901 остаются в силе, если прямо не изменены более новым утверждённым решением.

## 2. Закрытие AC-306

`AC-306 — Приоритизация портфеля по капиталу, экономике и вниманию собственника` имеет статус:

`Complete / PASS`.

Утверждённая publication:

- `docs/portfolio/AC-306-PORTFOLIO-PRIORITIZATION-CAPITAL-ECONOMICS-OWNER-ATTENTION-v1.0.0.md` — `Approved 1.0.0`;
- exact reviewed proposal: `docs/portfolio/AC-306-PORTFOLIO-PRIORITIZATION-CAPITAL-ECONOMICS-OWNER-ATTENTION.md` — `Proposed 0.9.0`, blob `d254c6441baca5f22828648ecfa701d04c8344b1`;
- cross-review: `docs/reviews/AC-306-PORTFOLIO-PRIORITIZATION-CROSS-REVIEW.md` — `10 of maximum 10`, `Complete / PASS for Owner approval`, blob `329c87d6a63e08564e8b52362b8af02b159d7b74`;
- Owner decision: `docs/governance/decisions/DECISION-2026-08-21-AC-306-APPROVAL.md`;
- explicit Owner approval wording: `AC-306 утверждаю`.

Канонический portfolio map синхронизирован:

- `docs/portfolio/PORTFOLIO.md` — `Active 0.7.0`.

## 3. Утверждённая portfolio prioritization

При отсутствии более высокого Company-level `P0` обязательства default discretionary product order:

| Band | Node | Treatment |
|---|---|---|
| `A1` | `PORT-002 — Discount Parser` | finish / accept / stabilize / maintain |
| `A2` | `PORT-001 — Arvectum Tender Agent` | bounded revenue / pilot / evidence work |
| `B1` | `PORT-003 — Arvectum Proxy Launcher` | trigger-based; preserve verified baseline |
| `B2` | `PORT-004 — Creative Test Agent` | trigger-based bounded pilot activation |
| `C1` | `PORT-007 — Data Platform` | clarification-only; no material build |
| `D1` | `PORT-005 — Tender Small-Volume Calculator` | contain / reference evidence |
| `D2` | `PORT-006 — Doors Parser` | contain / support / reuse evidence |

Это decision order, а не permanent engineering queue, budget allocation или автоматическая lifecycle promotion.

## 4. Company priority hierarchy остаётся выше portfolio ranking

AC-106 hierarchy остаётся binding:

1. `P0` — protect current obligations, cash and material risk;
2. `P1` — flagship market evidence + minimal real Arvectum operating model;
3. `P2` — product/OS work directly tied to revenue, obligation, evidence or blocker removal;
4. `P3` — speculative productization/module/platform expansion.

Реальный customer/security/data/continuity obligation может временно поднять exact work slice в P0 независимо от portfolio band. После closure это не меняет node treatment без отдельного решения.

## 5. Phase 3 — управление портфелем и кандидатами в повторно используемые модули

Этап: `M3 — Product/module-candidate portfolio governed as investments`.

| ID | Работа | Статус |
|---|---|---|
| `AC-301` | Сверка идентичности, границ и владения продуктами и инициативами портфеля | `Complete / PASS` |
| `AC-302` | Закрепление ответственной организационной позиции за каждым активным продуктом/инициативой | `Complete / PASS` |
| `AC-303` | Границы инвестиций, затрат и рисков; критерии продолжить/изменить/остановить | `Complete / PASS` |
| `AC-304` | Разделение standalone/reference/module/OS-capability candidate roles | `Complete / PASS` |
| `AC-305` | Сверка межпродуктовых зависимостей и контрактов продуктов с Arvectum OS | `Complete / PASS` |
| `AC-306` | Приоритизация портфеля по капиталу, экономике и вниманию собственника | `Complete / PASS` |
| `AC-307` | Итоговая проверка управления портфелем и закрытие M3 | `Current` |

## 6. Текущее действие — AC-307

### AC-307 — Final portfolio governance review and M3 closure

Статус: `Current`.

Цель: проверить AC-301…AC-306 как единый Company-level portfolio governance baseline и определить, выполнен ли milestone M3 без скрытых contradictions, missing ownership, unauthorized coupling, unfunded growth mandates или размывания Company/Product/Arvectum OS boundaries.

AC-307 должен как минимум проверить:

- каждый `PORT-*` имеет стабильную Company identity, repository locator, disposition и accountable Position;
- investment/cost/risk treatment AC-303 совместим с role classification AC-304;
- AC-305 dependency/Product Contract map не противоречит current portfolio state;
- AC-306 ranking не создаёт скрытый budget, customer commitment или automatic lifecycle promotion;
- `PORT-005/006` реально остаются contained, а `PORT-007` clarification-only;
- Band B nodes требуют named trigger, а не continuous speculative work;
- Company flagship и AC-106 `P0…P3` hierarchy остаются выше portfolio ranking;
- Owner attention, capital, obligations, risk and evidence boundaries согласованы;
- no hidden cross-repository shared runtime/data/authority commitment создан в M3;
- Product repositories остаются canonical для implementation/status/domain semantics;
- Arvectum OS остаётся canonical для Product Contracts/platform capabilities;
- unresolved items после M3 явно вынесены в downstream roadmap rather than hidden as completed;
- M3 closure не заявляет profitability, market validation, legal compliance, customer readiness или production readiness без evidence.

## 7. AC-307 exit condition

M3 может быть закрыт только если final review показывает coherent governed portfolio baseline и все material contradictions либо устранены, либо явно classified/carried forward с owner, boundary и next action.

Если review PASS, AC-307 должен:

1. зафиксировать M3 closure evidence;
2. синхронизировать `PORTFOLIO.md` и canonical roadmap при необходимости;
3. определить следующее каноническое действие после M3 согласно уже утверждённой Company roadmap sequence;
4. не выполнять downstream milestone работу преждевременно.

## 8. Authority boundary

Дорожная карта не создаёт организационные или юридические полномочия. AC-306 approval не является blanket spend authorization. Material capital allocation, material external commitments, risk acceptance, legal/IP/data exceptions и Company↔Product↔Arvectum OS commitments продолжают требовать соответствующий evidence и authority path.
