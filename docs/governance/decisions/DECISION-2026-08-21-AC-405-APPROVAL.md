# Решение собственника — утверждение AC-405

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`
Решение: `AC-405 — Portfolio/module/priority review cadence`

## 1. Явное решение

Собственник явно утвердил AC-405 формулировкой:

> `AC-405 утверждаю`

Утверждение относится к точной проверенной редакции:

- proposal: `docs/portfolio/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE.md`;
- proposal status: `Proposed 0.9.0`;
- immutable proposal blob SHA: `13d19b2a5418c2d1d3349e889fe54817dd9ee126`;
- cross-review: `docs/reviews/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE-CROSS-REVIEW.md`;
- cross-review result: `8 iterations`, `Complete / PASS for Owner approval`;
- immutable cross-review blob SHA: `1192472888da43de4160499d828e5def87391197`.

Эти blob SHA фиксируют именно те редакции, которые были представлены собственнику перед утверждением.

## 2. Утверждённый результат AC-405

Собственник утверждает Company-level review cadence для portfolio/module/priority governance поверх Approved M3 и AC-401…AC-404.

Утверждается, в частности, что:

- portfolio review работает по принципу `event-driven first, calendar backstop second`;
- material event вызывает scoped review затронутого node/scope без обязательного пересмотра всего портфеля;
- начальный operating default включает один лёгкий asynchronous portfolio exception scan в календарный месяц и одну integrated portfolio revalidation в квартал;
- эти интервалы являются стартовыми operating defaults, а не неизменяемыми constitutional requirements, и могут быть скорректированы последующим operating evidence через надлежащий governance path;
- routine commits, tests, bug fixes и feature progress внутри approved envelope сами по себе не являются portfolio-review triggers;
- `POS-003 — Portfolio & Product Lead` может в `AM-2` reaffirm current treatment, обновлять evidence references и выполнять bounded sequencing/status coordination внутри уже утверждённых Company/portfolio envelopes;
- `POS-003` не получает из AC-405 права самостоятельно менять Owner-approved disposition, permanent priority band, material investment envelope, module classification или Company↔Product↔Arvectum OS boundary;
- material portfolio changes требуют applicable `DEC-*`/`APR-*`/Owner gate и соответствующих `ROD-*`, включая прежде всего `ROD-02`, `ROD-04`, `ROD-06`, `ROD-08`, `ROD-09`, а при стратегическом эффекте — `ROD-01`;
- `P0` temporary execution priority не является permanent portfolio reclassification;
- Band B named trigger означает bounded re-evaluation exact slice, а не automatic permanent promotion, funding, customer commitment или unlimited expansion;
- reference/reuse evidence не создаёт Company reusable module автоматически;
- `PORT-007` остаётся `clarify / C1 / clarification-only / no material build` до отдельного material decision с достаточным multi-consumer/common-contract/economics/continuity/data/rights/ownership evidence;
- `PORT-005` и `PORT-006` остаются contained до отдельного material portfolio decision;
- review использует уже существующие `WORK/OBL`, `DEC/APR/ESC`, `RSK/EXC/INC` и AC-404 finance/economics sources и не создаёт дублирующие регистры;
- Company остаётся authoritative для Company-level portfolio meaning/treatment, product repositories — для implementation/status/domain semantics, Arvectum OS — для Product Contracts/RFC/ADR/capability lifecycle;
- no-change monthly scan не требует Owner meeting, отдельного decision ID или отдельного файла на каждый node;
- Owner получает только decision-ready material cases, а не routine portfolio administration.

## 3. Результат AC-405

`AC-405 — Portfolio/module/priority review cadence` закрывается со статусом:

`Complete / PASS`.

Русская смысловая формулировка результата:

**ООО «Арвектум» имеет утверждённый минимальный порядок пересмотра портфеля и кандидатов в модули, который реагирует на существенное новое evidence, но не превращает routine product activity в Owner bureaucracy и не позволяет review автоматически изменять инвестиционные или организационные решения.**

## 4. Что утверждение AC-405 не означает

AC-405 само по себе не:

- меняет текущие `PORT-001…PORT-007` disposition, role, priority band или investment treatment;
- утверждает новую инвестицию, бюджет, расход или funding allocation;
- переводит Band B node в Band A;
- разрешает material build `PORT-007`;
- выводит `PORT-005/006` из contain;
- создаёт reusable Company module, shared service/library/runtime или cross-product dependency;
- меняет product roadmap, implementation/status или customer commitment;
- создаёт или меняет Arvectum OS Product Contract/capability lifecycle;
- доказывает profitability, unit economics, market validation, legal/IP/data/production readiness;
- закрывает AC-406 или AC-407.

## 5. Следующее действие

Следующее каноническое действие M4:

`AC-406 — Owner Mission Control / reference-implementation evidence view`.

AC-406 должен определить owner-facing evidence projection поверх AC-401…AC-405 так, чтобы собственник видел material work/obligations, pending decisions/approvals, risks/exceptions/incidents, cash/commitment signals, portfolio priorities и exact action required без reconstruction burden, сохраняя source-of-truth и authority boundaries.

Это решение разрешает каноническую публикацию AC-405 `1.0.0`, синхронизацию roadmap/source registry/README и перевод current action на AC-406.

## 6. Границы решения

Решение является внутренним Company governance act в пределах заявленного scope. Оно не заменяет applicable legal/corporate acts, customer/vendor authority, product governance или Arvectum OS governance.