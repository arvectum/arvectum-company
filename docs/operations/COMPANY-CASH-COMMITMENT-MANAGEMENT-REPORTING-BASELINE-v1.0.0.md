# AC-404 — Cash, Commitment and Management Reporting Baseline

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-404 — Cash, commitment and management reporting baseline`
Решение: `docs/governance/decisions/DECISION-2026-08-21-AC-404-APPROVAL.md`
Cross-review: `docs/reviews/AC-404-CASH-COMMITMENT-MANAGEMENT-REPORTING-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `80c7b620cf446ed28b76143a0325ce89b1939ac0`

## 1. Approval publication

Этот документ является канонической Approved publication AC-404 `1.0.0`.

Утверждённое собственником нормативное содержание — полная проверенная редакция:

`docs/operations/COMPANY-CASH-COMMITMENT-MANAGEMENT-REPORTING-BASELINE.md`

с immutable git blob SHA:

`80c7b620cf446ed28b76143a0325ce89b1939ac0`.

Proposal включён в эту publication **целиком по immutable content reference**. Настоящая publication не меняет нормативное содержание проверенной редакции.

Явное решение собственника зафиксировано в:

`docs/governance/decisions/DECISION-2026-08-21-AC-404-APPROVAL.md`.

## 2. Approved model

AC-404 `1.0.0` устанавливает binding Company-level cash/commitment/management-reporting baseline в пределах incorporated proposal, включая:

1. source-of-truth separation между bank/accounting facts, Company management interpretation, forecasts и Company control state;
2. различение `cash fact`, `budget / limit`, `planned spend`, `approved internal commitment`, `incurred obligation`, `actual payment`, `receivable` и `expected inflow`;
3. запрет считать forecast/conditional inflow доступными денежными средствами до authoritative confirmation;
4. запрет автоматически покрывать confirmed material outflow speculative/uncertain inflow;
5. management report как derived decision-support projection, а не ledger/bank statement/tax register/payment proof/budget approval/profitability proof;
6. отсутствие отдельного Company transaction namespace `FIN-*`/`PAY-*`/`TX-*`;
7. переиспользование `OBL-*`, `DEC-*`/`APR-*`/`ESC-*`, `RSK-*`/`EXC-*`/`INC-*` вместо дублирующих financial identities;
8. minimum management-finance view с `as_of`, source freshness, material due outflows, receivables/payables, recurring-cost signal, expected inflows/outflows, approved-not-yet-incurred exposure, procurement cash-gap cases, economic signals, linked risks/incidents/decisions и explicit unknowns/gaps;
9. explicit uncertainty/freshness behavior и fail-closed/escalation для material consequential decisions при недостаточном decision-relevant evidence;
10. `P0` attention только для material/time-sensitive cash/obligation/risk conditions, а не routine bookkeeping rows;
11. `POS-005 — Finance & Obligation Control Lead` как accountable Company management-finance boundary без создания spend/payment/signature authority;
12. outsourced accounting/tax service как external professional/statutory source contour, а не Company Position или parallel ledger;
13. distinction management-control reconciliation от transaction-level bank/accounting reconciliation;
14. confidentiality/minimization/reference-over-copy для публичного Company repository;
15. сохранение product/project economics и portfolio truth в их собственных authoritative contours;
16. отсутствие fabricated runway, burn-rate, probability, liquidity confidence, CAC/LTV/ROI или Company-wide profitability precision без evidence;
17. absence of fixed arbitrary reporting cadence; cadence остаётся AC-407, presentation — AC-406;
18. Arvectum OS M9-alpha/P9.07 как возможный будущий presentation/composition substrate только через отдельный admitted boundary, без Company financial authority/Product Contract/lifecycle effect;
19. отсутствие budget, spend approval, payment, financing, guarantee, customer/vendor obligation, treasury system, financial automation или external effect по импликации.

## 3. Authority boundary

AC-404 не создаёт Organizational Authority или legal/payment authority.

Наличие cash, финансового отчёта, dashboard visibility, prepared payment, credentials, banking access, Position title или favorable management interpretation не даёт права расходования средств или создания обязательства.

Approved AC-202 `ROD-*`, AC-203 `AM-*`, Position/Assignment/access boundaries, legal/corporate competence, bank/signature authorization и customer/vendor/legal gates продолжают действовать независимо.

## 4. Source-of-truth boundary

Company repository может быть canonical для Company-level management interpretation/control state в declared scope, но не заменяет:

- bank/payment truth;
- accounting/tax/statutory truth;
- contracts/legal/corporate acts;
- customer/vendor authoritative facts;
- product/project economics implementation evidence;
- portfolio governance source;
- Arvectum OS Product Contract/platform lifecycle truth.

При конфликте management projection с authoritative source приоритет имеет source в своей области, а projection должна быть reconciled либо marked stale/uncertain.

## 5. Cross-review and approval evidence

Cross-review:

- `docs/reviews/AC-404-CASH-COMMITMENT-MANAGEMENT-REPORTING-CROSS-REVIEW.md`;
- iterations: `8`;
- result: `Complete / PASS for Owner approval`;
- immutable blob SHA: `3519f63ef7c09f075aa75b6d0d83ccd770911141`.

Approved proposal:

- `docs/operations/COMPANY-CASH-COMMITMENT-MANAGEMENT-REPORTING-BASELINE.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `80c7b620cf446ed28b76143a0325ce89b1939ac0`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-21-AC-404-APPROVAL.md` — `Approved`;
- explicit wording: `AC-404 утверждаю`.

## 6. Approval result

`AC-404 — Cash, commitment and management reporting baseline` имеет статус `Complete / PASS` и является binding Company management-finance/control baseline в пределах заявленного scope.

Следующее каноническое действие:

`AC-405 — Portfolio/module/priority review cadence`.

AC-405 должен определить минимальную review cadence для portfolio/module/priority decisions поверх утверждённых M3 и AC-401…AC-404 semantics, без создания meeting bureaucracy, automatic re-prioritization или новых authority effects.