# AC-404 — Cross-review: Cash, Commitment and Management Reporting Baseline

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `8`
Лимит Owner для AC-404: `не задан`; review остановлен после устранения/закрытия всех material objections по принципу proportional governance
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-404 — Cash, commitment and management reporting baseline`

Проверенный exact proposal:

- `docs/operations/COMPANY-CASH-COMMITMENT-MANAGEMENT-REPORTING-BASELINE.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `80c7b620cf446ed28b76143a0325ce89b1939ac0`.

Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`.

## 1. Review gate

AC-404 должен быть отклонён, если модель:

- создаёт параллельную бухгалтерию, bank ledger или transaction register;
- требует от Owner вручную классифицировать routine bank/accounting transactions;
- превращает forecast/receivable/expected inflow в available cash;
- смешивает budget, planned spend, approval, incurred obligation и payment;
- выводит spend/payment authority из наличия денег, Position title, banking access, dashboard visibility или prepared payment;
- позволяет material commitment при stale/unknown decision-relevant liquidity evidence без fail-closed/escalation;
- считает speculative inflow покрытием confirmed outflow без explicit bounded model/evidence;
- делает каждый invoice/overdue item P0 или Owner work;
- делает Company repository authoritative для bank/accounting/tax/customer/vendor facts;
- публикует sensitive bank/accounting/payment/customer data ради management convenience;
- создаёт fake Company-wide profitability/runway/risk precision;
- поглощает product/project unit economics или portfolio truth;
- принимает Arvectum OS M9-alpha/P9.07 как finance Product Contract/authority;
- преждевременно фиксирует arbitrary weekly/monthly reporting cadence;
- создаёт budget, spend approval, payment, borrowing, financing, guarantee, customer/vendor obligation или OS lifecycle effect по импликации.

## 2. Итерация 1 — Не создать вторую бухгалтерию

**Критика:** AC-404 расположен после трёх Company registers, поэтому естественный, но опасный путь — добавить `FIN-*`, `PAY-*` или transaction-level register и начать копировать bank/accounting facts.

**Сверка:** proposal Section 4 закрепляет three-layer source model, Section 5 прямо запрещает новый financial transaction namespace, а Section 11 оставляет accounting/tax provider внешним professional source. `OBL-*`, `DEC-*`, `RSK-*` переиспользуются вместо дублирования.

AC-102 Owner scope correction также требует management model, а не bookkeeping.

**Результат:** PASS.

## 3. Итерация 2 — Cash, budget, plan, approval, obligation и payment должны быть разными состояниями

**Критика:** термин `commitment` может смешать внутреннее решение потратить, юридически возникшее обязательство и фактический платёж.

**Сверка:** Section 6 разделяет:

- `cash fact`;
- `budget / limit`;
- `planned spend`;
- `approved internal commitment`;
- `incurred obligation`;
- `actual payment`;
- `receivable / expected inflow`.

Section 13 дополнительно фиксирует последовательность `proposal → finance evidence → DEC/APR → internal approval → external/legal act → OBL when obligation exists → actual payment when source confirms` и запрещает вывод одного шага из другого.

**Результат:** PASS.

## 4. Итерация 3 — Forecast не должен создавать ложную ликвидность

**Критика:** derived management report особенно опасен, если conditional customer receipt визуально компенсирует уже подтверждённый supplier/tax outflow.

**Сверка:** Sections 8 и 14 запрещают fabricated runway/probabilities и автоматическое netting confirmed outflows against speculative inflows. Любая liquidity-margin formula допустима только с explicit source set, common as-of, inclusion/exclusion rules и маркировкой как management projection.

`liquidity_status=sufficient_for_known_case` должен читаться только в пределах включённого source/case scope; он не является утверждением универсальной Company solvency. Это implementation invariant для AC-406/любой будущей projection.

**Результат:** PASS.

## 5. Итерация 4 — Видимость денег не должна стать spend authority

**Критика:** POS-005, Owner, General Director и banking actor могут физически совпадать в одном человеке; future UI может ошибочно представить наличие cash или доступ к банку как permission to spend.

**Сверка:** proposal сохраняет ROD-02/ROD-03 и AC-203 deny-by-default; Section 12 закрепляет POS-005 accountability без payment/spend approval authority; Section 13 прямо говорит `technical bank access ≠ spend authority`; Section 23 запрещает создание budget/payment/financing authority.

Это совместимо с AC-202/AC-203 и AC-205, где Assignment/access сами authority не создают.

**Результат:** PASS.

## 6. Итерация 5 — P0 и Owner attention не должны превратить бухгалтерию в emergency queue

**Критика:** финансовые данные часто содержат множество due/overdue rows; если каждый из них становится P0/Owner attention, M4 увеличит Owner workload вместо его снижения.

**Сверка:** Section 9 делает P0 consequence/time-sensitive, а не row-driven. Routine bookkeeping, reconciliation, invoice matching и receipt classification исключены из Owner work. P0 возникает для material due obligations, mandatory payment risk, material commitment without current evidence, material overdue exposure, procurement cash gap или material bank/accounting incident.

**Результат:** PASS.

## 7. Итерация 6 — Freshness и accounting interface должны быть достаточны для decision, но не требовать transaction reconciliation

**Критика:** `reconciliation` можно снова прочитать как требование сверять все bank transactions, что уже было отклонено Owner в AC-102.

**Сверка:** Section 10.2 явно переопределяет AC-404 reconciliation как **management-control reconciliation**: проверить source availability/freshness, соответствие interpretation, linked control state и changed facts. Transaction-level bank reconciliation остаётся professional accounting contour.

Section 16 требует refresh/evidence re-check на material decision/event triggers, но не придумывает fixed cadence.

**Результат:** PASS.

## 8. Итерация 7 — Management visibility не должна утечь в публичный repository

**Критика:** exact cash balances, invoices, tax documents, bank details и payment incidents способны сделать public Company repo operationally dangerous.

**Сверка:** Section 17 прямо запрещает bank/payment credentials, transaction exports, signatures/keys/tokens, sensitive tax/accounting documents, confidential customer/vendor materials, unnecessary PII, confidential exact cash balances и privileged payment/fraud details. Public repo хранит semantic model/safe metadata/references; exact values остаются restricted/source-owned.

Это согласуется с AC-401…AC-403 minimization boundaries.

**Результат:** PASS.

## 9. Итерация 8 — Portfolio, Arvectum OS, cadence и software boundary

**Критика:** AC-404 может преждевременно превратиться либо в Company finance dashboard на Arvectum OS, либо в unit-economics system для всех products, либо в fixed reporting bureaucracy.

**Сверка:** Section 18 оставляет product/project economics в source/product contours и не фабрикует CAC/LTV/ROI/margin. Section 19 трактует Owner Mission Control/OS только как future derived presentation through an explicit admitted boundary. Current OS at `76504766353028540891ac1dfdbf1e5dc331a4af` has M9-alpha internal usability evidence and P9.07 current, but no Company finance Product Contract/authority is inferred. Sections 16, 20 and 22 defer cadence to AC-407 and presentation/software to AC-406 while allowing the simplest replaceable report now.

**Результат:** PASS.

## 10. Acceptance matrix

| Проверка | Результат |
|---|---|
| accounting/bank transaction truth remains external | PASS |
| no parallel `FIN/PAY/TX` ledger namespace | PASS |
| management report is derived decision-support projection | PASS |
| cash fact separated from management interpretation | PASS |
| budget/limit ≠ obligation/spend requirement | PASS |
| planned spend ≠ approval/payable | PASS |
| internal approval ≠ external incurred obligation | PASS |
| incurred obligation ≠ actual payment | PASS |
| receivable/forecast ≠ available cash | PASS |
| speculative inflow cannot silently cover confirmed outflow | PASS |
| no fabricated runway/probability/liquidity precision | PASS |
| explicit as-of/freshness/unknown behavior | PASS |
| material unknown can block/escalate consequential decision | PASS |
| P0 remains material/exception-driven | PASS |
| routine bookkeeping does not become Owner work | PASS |
| POS-005 accountability without spend/payment authority | PASS |
| outsourced accounting remains professional external contour | PASS |
| proposer/finance-evidence role does not imply self-approval | PASS |
| AC-401 OBL identities reused for material obligations | PASS |
| AC-402 DEC/APR/ESC identities reused for authority gates | PASS |
| AC-403 RSK/EXC/INC identities reused for financial risk/events | PASS |
| public repository minimization preserved | PASS |
| product/portfolio economics truth not duplicated | PASS |
| OS M9-alpha/P9.07 does not create Company finance authority | PASS |
| no Stable Product Contract/Active Capability inferred | PASS |
| fixed arbitrary cadence not invented | PASS |
| minimum report packet defined before AC-406 | PASS |
| no budget/spend/payment/financing/customer obligation created | PASS |

## 11. Residual limitations intentionally carried forward

AC-404 proposal does **not** prove:

- current cash balance or liquidity;
- completeness/currentness of actual receivables/payables;
- completeness of live `OBL-*` population;
- profitability, runway, burn rate or unit economics;
- accounting/tax/legal compliance;
- live accounting↔management integration;
- actual usefulness of the report in repeated daily operations;
- tested continuity of accounting/banking inputs;
- final AC-405 portfolio review cadence;
- AC-406 presentation;
- AC-407 management cadence.

Эти ограничения являются честными evidence gaps, а не material defects модели.

## 12. Cross-review conclusion

После 8 последовательных Company-finance, authority, operational, workload, confidentiality и Company↔Product↔Arvectum OS boundary checks material blocking objection не осталось.

Итог:

`AC-404 cross-review — COMPLETE / PASS FOR OWNER APPROVAL`.

Exact reviewed proposal:

- `docs/operations/COMPANY-CASH-COMMITMENT-MANAGEMENT-REPORTING-BASELINE.md`;
- `Proposed 0.9.0`;
- blob `80c7b620cf446ed28b76143a0325ce89b1939ac0`.

Cross-review не является Owner approval и не делает proposal binding.

## 13. Required next gate

Для закрытия AC-404 требуется явный attributable Owner act, однозначно утверждающий exact reviewed proposal.

Рекомендуемая краткая формулировка:

`AC-404 утверждаю`.

До такого акта:

- AC-404 остаётся `Proposed`;
- roadmap остаётся на AC-404;
- Approved `1.0.0` publication не создаётся;
- AC-405 не становится current canonical action.
