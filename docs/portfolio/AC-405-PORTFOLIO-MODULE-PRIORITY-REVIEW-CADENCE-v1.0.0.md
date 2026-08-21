# AC-405 — Portfolio / Module / Priority Review Cadence

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-405 — Portfolio/module/priority review cadence`
Решение: `docs/governance/decisions/DECISION-2026-08-21-AC-405-APPROVAL.md`
Cross-review: `docs/reviews/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `13d19b2a5418c2d1d3349e889fe54817dd9ee126`

## 1. Approval publication

Этот документ является канонической Approved publication AC-405 `1.0.0`.

Утверждённое собственником нормативное содержание — полная проверенная редакция:

`docs/portfolio/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE.md`

с immutable git blob SHA:

`13d19b2a5418c2d1d3349e889fe54817dd9ee126`.

Proposal включён в эту publication целиком по immutable content reference. Настоящая publication не меняет нормативное содержание проверенной редакции.

Явное решение собственника зафиксировано в:

`docs/governance/decisions/DECISION-2026-08-21-AC-405-APPROVAL.md`.

## 2. Approved model

AC-405 `1.0.0` устанавливает binding Company-level portfolio/module/priority review cadence в пределах incorporated proposal, включая:

1. `event-driven first, calendar backstop second`;
2. immediate scoped review при material event без обязательного reopening всего portfolio;
3. начальный monthly asynchronous exception scan;
4. начальную quarterly integrated portfolio revalidation;
5. возможность корректировки cadence по реальному operating evidence через последующий governance path;
6. исключение routine commits/tests/features из portfolio triggers;
7. `POS-003` AM-2 stewardship только внутри уже approved envelope;
8. запрет silent изменения Owner-approved disposition, permanent band, material investment treatment и module classification;
9. material portfolio changes через applicable `DEC-*`/`APR-*`/`ROD-*` gates;
10. `P0 temporary execution priority ≠ permanent portfolio reclassification`;
11. Band B named trigger как bounded re-evaluation, а не automatic promotion/funding;
12. reuse/reference evidence как review input, а не automatic module admission;
13. `PORT-007` clarification-only / no material build до отдельного evidence-backed material decision;
14. `PORT-005`/`PORT-006` remain contained absent separate material decision;
15. reuse of AC-401…AC-404 controls/evidence without duplicate portfolio finance/risk/decision registers;
16. Company/Product/Arvectum OS source-of-truth separation;
17. concise no-change durable checkpoint without artificial decision IDs/file explosion;
18. Owner-facing escalation only for actual decision-ready material cases;
19. absence of budget, funding, product roadmap, customer commitment, module admission, cross-product dependency or OS lifecycle effect by implication.

## 3. Authority boundary

AC-405 не создаёт Organizational Authority.

`POS-003` получает только уже предусмотренную Approved Position/AC-203 возможность routine stewardship в `AM-0…AM-2` внутри действующих boundaries. `AM-3`/`AM-4` для major portfolio approval/reclassification этим документом не активируются.

Material portfolio/investment/module/boundary changes продолжают использовать applicable `ROD-*` и AC-402 decision/approval/escalation semantics.

## 4. Source-of-truth boundary

- Company repository authoritative для Company-level portfolio identity, treatment, review interpretation и approved portfolio decisions в своём scope;
- product repositories authoritative для implementation/status/domain semantics;
- Arvectum OS authoritative для Product Contracts, RFC/ADR, Platform Capability lifecycle и platform semantics;
- legal/customer/accounting/security sources authoritative в своих scopes.

Review не переписывает source facts и не создаёт cross-repository authority.

## 5. Cross-review and approval evidence

Cross-review:

- `docs/reviews/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE-CROSS-REVIEW.md`;
- iterations: `8`;
- result: `Complete / PASS for Owner approval`;
- immutable blob SHA: `1192472888da43de4160499d828e5def87391197`.

Approved proposal:

- `docs/portfolio/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `13d19b2a5418c2d1d3349e889fe54817dd9ee126`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-21-AC-405-APPROVAL.md` — `Approved`;
- explicit wording: `AC-405 утверждаю`.

## 6. Approval result

`AC-405 — Portfolio/module/priority review cadence` имеет статус `Complete / PASS` и является binding Company portfolio-review baseline в пределах заявленного scope.

Следующее каноническое действие:

`AC-406 — Owner Mission Control / reference-implementation evidence view`.

AC-406 должен определить owner-facing derived evidence projection поверх AC-401…AC-405, не создавая новый source of truth, authority, dashboard prerequisite или hidden execution path.