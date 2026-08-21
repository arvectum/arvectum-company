# AC-306 — Приоритизация портфеля по капиталу, экономике и вниманию собственника

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-306 — Portfolio prioritization by capital, economics and Owner attention`
Approval: `docs/governance/decisions/DECISION-2026-08-21-AC-306-APPROVAL.md`
Cross-review: `docs/reviews/AC-306-PORTFOLIO-PRIORITIZATION-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `d254c6441baca5f22828648ecfa701d04c8344b1`

## 1. Модель утверждённой публикации

Эта публикация фиксирует утверждение точной проверенной редакции AC-306 без переписывания прошедшего cross-review текста задним числом.

Утверждённая исходная редакция:

- файл: `docs/portfolio/AC-306-PORTFOLIO-PRIORITIZATION-CAPITAL-ECONOMICS-OWNER-ATTENTION.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `d254c6441baca5f22828648ecfa701d04c8344b1`.

Перекрёстная проверка:

- файл: `docs/reviews/AC-306-PORTFOLIO-PRIORITIZATION-CROSS-REVIEW.md`;
- iterations: `10 of maximum 10`;
- result: `Complete / PASS for Owner approval`;
- immutable git blob SHA: `329c87d6a63e08564e8b52362b8af02b159d7b74`.

Решение собственника:

- `docs/governance/decisions/DECISION-2026-08-21-AC-306-APPROVAL.md` — `Approved`;
- явная формулировка: `AC-306 утверждаю`.

Нормативное содержание proposal blob `d254c6441baca5f22828648ecfa701d04c8344b1` включается в эту публикацию в полном объёме по immutable content reference и считается утверждённым в пределах заявленного scope.

## 2. Утверждённая priority hierarchy

AC-306 не заменяет Company-level priority model AC-106. Сохраняется последовательность:

1. `P0` — реальные обязательства, cash и material risk;
2. `P1` — flagship market evidence + минимальная реальная operating model Arvectum Company;
3. `P2` — product/OS work, непосредственно связанная с revenue, obligation, evidence или blocker removal;
4. `P3` — speculative productization/module/platform expansion.

Portfolio ranking действует внутри этой Company hierarchy и не делает продуктовый портфель новым Company flagship.

## 3. Утверждённый default portfolio ranking

| Band | Portfolio node | Утверждённый treatment |
|---|---|---|
| `A1` | `PORT-002 — Discount Parser` | `finish / accept / stabilize / maintain`; bounded customer-acceptance, defect, delivery and agreed-support work; после accepted delivery — maintenance/freeze без нового paid/second-consumer evidence |
| `A2` | `PORT-001 — Arvectum Tender Agent` | bounded revenue/pilot/evidence work; quality/reliability/evidence over feature breadth; без mass pilot/SaaS/submission-EDS expansion по импликации |
| `B1` | `PORT-003 — Arvectum Proxy Launcher` | preserve verified productized baseline; trigger-based investment; не тратить continuous Owner attention на известные unavailable physical gates |
| `B2` | `PORT-004 — Creative Test Agent` | maintain runnable pilot readiness; activate bounded work при qualified design-partner/customer evidence |
| `C1` | `PORT-007 — Data Platform` | clarification-only; no material build до concrete multi-consumer need + common contract + economic/continuity case |
| `D1` | `PORT-005 — Tender Small-Volume Calculator` | contain; maintenance/security/continuity/reference evidence only |
| `D2` | `PORT-006 — Doors Parser` | contain completed-delivery asset; support/reuse evidence only |

Этот порядок является default decision order для discretionary product attention, а не постоянной инженерной очередью и не автоматическим budget allocation.

## 4. Dynamic override rule

Реальный `P0` event временно вытесняет обычный ranking:

- existing customer defect/acceptance/support obligation;
- material cash/continuity issue;
- material security/data incident;
- иное конкретное обязательство, которое по Company baseline требует P0 treatment.

P0 override относится к конкретной работе, а не автоматически к identity/disposition всего node. После закрытия obligation node возвращается к утверждённому portfolio treatment, если новое explicit decision не установило иное.

Для Band B named trigger означает `re-evaluate/elevate bounded slice`, а не self-executing promotion.

## 5. Owner attention как management capital

Для material product work decision preparation должна показывать:

1. `why now` — obligation, revenue, evidence или blocker;
2. exact bounded outcome;
3. exact Owner action — reserved decision, judgment, local gate или execution;
4. что может быть подготовлено/исполнено без Owner;
5. stop condition;
6. какое следующее решение станет возможно благодаря evidence.

Owner attention не должен расходоваться как бесплатный ресурс на known-unavailable gate retries, speculative polish, raw test review и simultaneous expansion нескольких repos без ranked business reason.

## 6. Capital/economics evidence rule

AC-306 не создаёт fictional financial precision.

До появления реальных management/accounting/customer данных ranking остаётся качественным и evidence-backed. `Unknown` cost/risk/revenue не означает zero. Любой material spend или recurring-cost expansion требует применимого evidence/authority gate.

Technical maturity, code volume, repository activity, sunk cost, `RI-OS-CONSUMER` или `RI-PRODUCT-FAMILY` сами по себе не являются funding claim.

## 7. Сохраняемые границы

Утверждение AC-306:

- не меняет AC-301 identities/dispositions;
- не меняет AC-302 accountable Position mapping;
- не отменяет AC-303 investment/cost/risk boundaries;
- не меняет AC-304 role/reuse classification;
- не меняет AC-305 dependency/Product Contract reconciliation;
- не создаёт budget, price, SLA, customer/vendor commitment, hiring или production authorization;
- не создаёт shared library/service/runtime/module или Arvectum OS capability;
- не меняет Product Contract;
- не создаёт legal/IP/data rights;
- не делает blocked external/physical gate завершённым;
- не выполняет AC-307.

## 8. Authority

AC-306 является Owner-approved portfolio/capital priority decision в пределах `ROD-02` и `ROD-04`.

Specific material expenditure, external commitment, risk/dependency exception или Company↔Product↔Arvectum OS commitment продолжает требовать применимый отдельный evidence/authority path.

## 9. Результат

`AC-306 — Complete / PASS`.

Следующее каноническое действие:

`AC-307 — Итоговая проверка управления портфелем и закрытие M3`.
