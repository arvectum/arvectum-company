# AC-405 — Cross-review: Portfolio / Module / Priority Review Cadence

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `8`
Лимит Owner для AC-405: `не задан`; review остановлен после закрытия всех material objections по proportional-governance principle
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-405 — Portfolio/module/priority review cadence`

Проверенный exact proposal:

- `docs/portfolio/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `13d19b2a5418c2d1d3349e889fe54817dd9ee126`.

Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`.

## 1. Review gate

AC-405 должен быть отклонён, если cadence:

- превращает семь portfolio nodes в постоянную Owner meeting/administrative queue;
- позволяет `POS-003` в AM-2 самостоятельно менять Owner-approved disposition/band/investment/module classification;
- делает routine commits/tests/features portfolio events;
- превращает temporary P0 preemption в permanent portfolio promotion;
- считает named trigger автоматическим Band B promotion/funding authorization;
- превращает reference/reuse evidence в автоматическое module admission;
- разрешает material build `PORT-007` без отдельного evidence/authority gate;
- поднимает `PORT-005/006` из contain без material decision;
- выводит funding/investment authority из priority rank;
- дублирует WORK/OBL/DEC/APR/ESC/RSK/EXC/INC или AC-404 finance state;
- принимает product implementation status из Company interpretation вместо product canonical source;
- создаёт Arvectum OS Product Contract/capability lifecycle change из Company review;
- требует fake financial/KPI precision;
- позволяет stale/unknown customer/finance/legal/risk evidence считаться current;
- создаёт review-file explosion или artificial decision IDs для no-change scans;
- закрывает linked work/obligation/risk/decision по факту portfolio review;
- создаёт budget, customer commitment, product roadmap change или external effect по импликации.

## 2. Итерация 1 — Cadence должен ловить изменения, а не создавать meeting bureaucracy

**Критика:** слово `cadence` легко превращается в weekly/monthly portfolio meeting независимо от наличия нового evidence, что противоречит business-first и Owner-workload цели.

**Сверка:** proposal Section 4 использует `event-driven first, calendar backstop second`: material event review немедленный и scoped; monthly layer — asynchronous exception scan; quarterly layer — integrated revalidation. Section 11 прямо исключает monthly no-change scan из Owner work, Section 16 делает meetings exception-based.

Monthly scan не требует повторного deep review семи продуктов; допустим единый `no material portfolio change identified` checkpoint.

**Результат:** PASS.

## 3. Итерация 2 — Calendar defaults не должны стать вечной bureaucratic invariant

**Критика:** monthly + quarterly frequency пока не подтверждена operating history; жёсткая вечная частота была бы fabricated process precision.

**Сверка:** Section 4.3 явно определяет intervals как **initial operating defaults**, а не constitutional invariants. AC-407/subsequent evidence MAY предложить корректировку frequency, если observed burden/missed-change risk покажут необходимость.

Выбранный design создаёт bounded starting cadence, но сохраняет empirical adjustment path.

**Результат:** PASS.

## 4. Итерация 3 — Routine stewardship AM-2 не должен захватить ROD-02/ROD-04

**Критика:** `POS-003` имеет AM-2 routine prioritization, но AC-306 ranking и portfolio treatments уже Owner-approved; формулировка cadence не должна позволить Portfolio Lead переписывать их под видом review.

**Сверка:** Sections 2.4 и 7 разделяют:

- AM-2: reaffirm current treatment, refresh refs, routine sequencing внутри approved envelope, temporary exact P0 slice, Band B bounded re-evaluation;
- material gate: disposition change, permanent band/treatment change, material investment envelope, module admission, major start/stop, boundary change, risk exception, strategy effect.

Для material cases сохраняются `ROD-02`, `ROD-04` и иные applicable `ROD-*` + AC-402 DEC/APR semantics.

**Результат:** PASS.

## 5. Итерация 4 — P0 и named trigger не должны становиться silent portfolio reclassification

**Критика:** operational urgency может создать ошибочный вывод, что affected product теперь permanently highest priority; named trigger Band B может быть ошибочно прочитан как promotion.

**Сверка:** Section 10 устанавливает `P0 temporary execution priority ≠ permanent portfolio band/disposition change`; после P0 node возвращается к approved treatment без separate material decision.

Section 8 задаёт named-trigger chain `new evidence → bounded review → optional temporary elevation/work proposal` и прямо запрещает automatic permanent A-band promotion, budget, customer commitment, production approval или unlimited expansion.

**Результат:** PASS.

## 6. Итерация 5 — Reuse/reference evidence не должно автоматически создать Company module

**Критика:** M3 уже имеет RI-PRODUCT-FAMILY evidence и clarification-only `PORT-007`; cadence может начать механически повышать repeated code/patterns в module.

**Сверка:** Sections 5.5 и 9 требуют materially independent consumers/workflows, bounded common contract, economic/reuse case, continuity/sovereignty, data/security/rights, ownership/implementation locus и Company-vs-OS placement evidence.

`PORT-007` остаётся `clarify / C1 / no material build`; `PORT-005/006` остаются contained. Reference status сам по себе promotion evidence не создаёт.

Module admission остаётся material portfolio decision, не scan result.

**Результат:** PASS.

## 7. Итерация 6 — Finance/economics review не должен изобретать numbers или funding claim

**Критика:** portfolio review часто провоцирует scoring tables, ROI estimates и automatic rank calculation даже при отсутствии measured evidence.

**Сверка:** proposal использует AC-404 management-finance sources и требует known/unknown separation. Material spend/recurring-cost/economics changes являются review triggers, но никакая формула/score не вводится. `Unknown` остаётся evidence gap; priority rank не является budget/funding authorization.

Decision packet может использовать реальные margin/unit-economics/Owner-cost values только когда они source-backed и decision-relevant.

**Результат:** PASS.

## 8. Итерация 7 — Company / Product / Arvectum OS source separation

**Критика:** quarterly integrated review может начать копировать product roadmaps/status или решить, что reused mechanism должен стать OS capability.

**Сверка:** Sections 3, 5.3, 5.6, 13 и 15 сохраняют source hierarchy:

- Company owns portfolio identity/treatment/review meaning;
- product repository owns implementation/status/domain semantics;
- Arvectum OS owns Product Contracts/RFC/ADR/capability lifecycle;
- legal/customer/accounting sources retain their authority.

Current OS main was rechecked at `76504766353028540891ac1dfdbf1e5dc331a4af`; M9-alpha/P9.07 workspace progress does not create Company portfolio or OS lifecycle authority.

**Результат:** PASS.

## 9. Итерация 8 — Durable evidence должен быть reconstructable без review-log explosion

**Критика:** если monthly scan требует семь файлов, семь decision IDs и полный evidence packet даже без changes, governance overhead быстро превысит value.

**Сверка:** Section 12 разрешает один concise portfolio-wide checkpoint для changed nodes only; no-change review не создаёт artificial `DEC-*`. Full decision packet нужен только для material case. Minimum reconstructability ограничена Position/mode/period-or-trigger/evidence-as-of/changed nodes/result/next trigger.

Section 14 сохраняет public-repository minimization; raw confidential customer/bank/security payload и chain-of-thought не нужны.

**Результат:** PASS.

## 10. Acceptance matrix

| Проверка | Результат |
|---|---|
| event-driven review precedes calendar convenience | PASS |
| monthly scan is asynchronous/lightweight | PASS |
| quarterly review is revalidation, not mandatory meeting | PASS |
| cadence intervals explicitly revisitable with operating evidence | PASS |
| routine product activity does not become portfolio event | PASS |
| only affected nodes reviewed on event trigger | PASS |
| POS-003 AM-2 limited to approved envelope | PASS |
| Owner-approved disposition/bands not silently changed | PASS |
| material changes use DEC/APR/ROD path | PASS |
| P0 override does not permanently reclassify node | PASS |
| Band B named trigger is not automatic promotion | PASS |
| PORT-007 stays clarification-only/no material build | PASS |
| PORT-005/006 remain contain absent separate decision | PASS |
| reference/reuse evidence does not automatically create module | PASS |
| module review requires multi-consumer/common-contract/economics/continuity evidence | PASS |
| Unknown financial/economic evidence not converted to zero/score | PASS |
| priority rank does not create budget/funding authority | PASS |
| AC-401…AC-404 controls reused rather than duplicated | PASS |
| product implementation/status remains product-owned | PASS |
| OS Product Contract/capability lifecycle remains OS-owned | PASS |
| no artificial decision IDs for no-change review | PASS |
| no one-file-per-node-per-month requirement | PASS |
| Owner sees decision-ready material cases only | PASS |
| review closure does not close linked control records | PASS |
| public-repository minimization preserved | PASS |
| no product/customer/spend/external effect created by cadence | PASS |

## 11. Residual limitations intentionally carried forward

AC-405 proposal does **not** prove:

- that monthly/quarterly frequencies are optimal after long-term use;
- current completeness of all product/customer/economic/risk evidence;
- current profitability/unit economics of any node;
- existence of a production-ready reusable Company module;
- customer/market validation of portfolio theses;
- product/legal/IP/data/production readiness;
- usefulness of a future Mission Control UI;
- final Company-wide management cadence.

These are evidence gaps carried to ongoing operations, AC-406/AC-407 and future material decisions, not defects in the cadence model.

## 12. Cross-review conclusion

После 8 последовательных review iterations по workload, authority, dynamic priority, module admission, finance evidence, Company↔Product↔OS boundary и durable-record burden material blocking objections не осталось.

Итог:

`AC-405 cross-review — COMPLETE / PASS FOR OWNER APPROVAL`.

Exact reviewed proposal:

- `docs/portfolio/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE.md`;
- `Proposed 0.9.0`;
- blob `13d19b2a5418c2d1d3349e889fe54817dd9ee126`.

Cross-review не является Owner approval и не делает cadence binding.

## 13. Required next gate

Для закрытия AC-405 требуется явный attributable Owner act, однозначно утверждающий exact reviewed proposal.

Рекомендуемая краткая формулировка:

`AC-405 утверждаю`.

До такого акта:

- AC-405 остаётся `Proposed`;
- current `PORT-001…PORT-007` state не меняется;
- roadmap остаётся на AC-405;
- Approved `1.0.0` publication не создаётся;
- AC-406 не становится current canonical action.
