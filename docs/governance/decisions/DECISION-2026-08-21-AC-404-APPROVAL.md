# Решение собственника — утверждение AC-404

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`
Решение: `AC-404 — Cash, commitment and management reporting baseline`

## 1. Явное решение

Собственник явно утвердил AC-404 формулировкой:

> `AC-404 утверждаю`

Утверждение относится к точной проверенной редакции:

- proposal: `docs/operations/COMPANY-CASH-COMMITMENT-MANAGEMENT-REPORTING-BASELINE.md`;
- proposal status: `Proposed 0.9.0`;
- immutable proposal blob SHA: `80c7b620cf446ed28b76143a0325ce89b1939ac0`;
- cross-review: `docs/reviews/AC-404-CASH-COMMITMENT-MANAGEMENT-REPORTING-CROSS-REVIEW.md`;
- cross-review result: `8 iterations`, `Complete / PASS for Owner approval`;
- immutable cross-review blob SHA: `3519f63ef7c09f075aa75b6d0d83ccd770911141`.

Эти blob SHA фиксируют именно те редакции, которые были представлены собственнику перед утверждением.

## 2. Утверждённый результат AC-404

Собственник утверждает Company-level baseline управленческой видимости cash, commitments и decision-relevant financial signals поверх Approved AC-401…AC-403.

Утверждается, в частности, что:

- bank/accounting facts, Company management interpretation, forecasts, budgets/limits, planned spend, approved internal commitments, incurred obligations и actual payments являются разными состояниями и не выводятся друг из друга автоматически;
- authoritative bank/accounting/tax/legal/customer/vendor facts остаются в соответствующих source contours;
- Company management report является derived decision-support projection и не заменяет ledger, bank statement, tax register, legal proof, payment evidence, budget approval или profitability evidence;
- AC-404 не вводит отдельный Company transaction namespace `FIN-*`, `PAY-*`, `TX-*` или аналогичный параллельный ledger;
- material obligations используют уже утверждённые `OBL-*`, material decisions/approvals/escalations — `DEC-*`/`APR-*`/`ESC-*`, financial risks/exceptions/incidents — `RSK-*`/`EXC-*`/`INC-*`;
- forecasted or conditional inflow не считается available cash до подтверждения authoritative source;
- confirmed material outflow не может автоматически считаться покрытым speculative/uncertain inflow;
- `unknown`/stale/incomplete evidence должно быть показано явно и может блокировать либо эскалировать consequential commitment decision пропорционально consequence;
- `P0` остаётся exception/materiality-driven и не превращает routine accounting rows в Owner queue;
- `POS-005 — Finance & Obligation Control Lead` отвечает за management-finance/cash/commitment visibility в утверждённых границах, но это не создаёт payment, signature или spend-approval authority;
- outsourced accounting/tax service остаётся external professional contour и source of accounting/statutory facts;
- technical bank access, наличие cash, prepared payment, report/dashboard visibility или Position title не создают Organizational Authority;
- public Company repository хранит semantic model, safe management metadata и references, а не restricted bank/accounting/payment/customer payload;
- product/project unit economics остаются product/project evidence и не поглощаются Company management reporting;
- current Arvectum OS M9-alpha/P9.07 MAY позднее использоваться как presentation/composition substrate только через отдельный admitted boundary и не создаёт Company finance authority, Stable Product Contract или Active Capability;
- конкретная recurring cadence не фиксируется AC-404 и остаётся предметом AC-407; presentation/Owner Mission Control остаётся AC-406.

## 3. Результат AC-404

`AC-404 — Cash, commitment and management reporting baseline` закрывается со статусом:

`Complete / PASS`.

Русская смысловая формулировка результата:

**ООО «Арвектум» имеет утверждённую Company-level модель управленческой финансовой видимости, которая позволяет связывать существенные денежные и обязательственные сигналы с Company control state, не создавая вторую бухгалтерию и не превращая наличие денег или финансовую видимость в право расходования.**

## 4. Что утверждение AC-404 не означает

AC-404 само по себе не:

- подтверждает текущий остаток денежных средств или достаточность ликвидности;
- доказывает полноту/актуальность receivables, payables или live `OBL-*` population;
- утверждает бюджет, лимит расхода, planned spend или конкретный expenditure;
- создаёт spend approval, payment/signature authority, bank authorization, borrowing, financing, guarantee или иной финансовый инструмент;
- создаёт customer/vendor/legal obligation;
- подтверждает profitability, runway, burn rate, CAC/LTV/ROI или unit economics;
- заменяет бухгалтерский, налоговый, банковский или юридический source of truth;
- создаёт live accounting integration, treasury system, payment workflow или financial automation;
- меняет `ROD-*`, `AM-*`, Position/Assignment/access boundaries;
- создаёт Product Contract или меняет Arvectum OS capability lifecycle;
- закрывает AC-405…AC-407.

## 5. Следующее действие

Следующее каноническое действие M4:

`AC-405 — Portfolio/module/priority review cadence`.

AC-405 должен определить минимальную review cadence для portfolio/module/priority decisions, используя уже утверждённые M3 portfolio semantics и AC-401…AC-404 control/evidence layers, без создания постоянной meeting bureaucracy или автоматического изменения portfolio disposition/priority.

Это решение разрешает каноническую публикацию AC-404 `1.0.0`, синхронизацию roadmap/source register/README и перевод current action на AC-405.

## 6. Границы решения

Решение является внутренним Company governance act в пределах заявленного scope. Оно не заменяет применимые юридические/корпоративные акты, банковские полномочия, договорные approvals, customer/vendor authority или иные обязательные внешние gates.