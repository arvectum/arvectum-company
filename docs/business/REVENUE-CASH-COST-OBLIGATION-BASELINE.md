# AC-102 — Revenue, Cash, Recurring Cost and Obligation Baseline

Status: `Blocked / Financial evidence intake required`
Version: `0.2.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Evidence cutoff: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-102 — Revenue, cash, recurring cost and obligation baseline`
Depends on: `AC-101 — Current business model and value proposition baseline`
Review: `docs/reviews/AC-102-FINANCIAL-BASELINE-CROSS-REVIEW.md`

## 1. Purpose

This artifact establishes the first evidence-backed Company financial and commitment baseline for ООО «Арвектум».

Its purpose is to let the Owner distinguish:

- real ООО «Арвектум» revenue from intended monetization;
- contracted/invoiced value from cash actually received;
- current LLC activity from historical or personally contracted work outside the LLC;
- Company-use cost from cost demonstrably paid by the LLC;
- recurring run-rate from one-time or sunk investment;
- current cash-producing work from pre-revenue investment;
- known obligations from possible future obligations;
- actual figures from estimates and unknowns.

This is a management baseline, not an accounting ledger, tax return, bank statement, legal opinion or customer contract register.

## 2. Source hierarchy and repository-safety boundary

Financial truth remains with the applicable authoritative source.

Examples:

1. bank statement / bank transaction record for actual cash movement;
2. accounting and tax records for accounting/tax treatment and accrued obligations;
3. signed contract, accepted order, invoice or other applicable source for contractual commitment;
4. provider receipt for the fact and amount of a provider-side charge;
5. Company repository records for repository-safe management conclusions only.

A provider receipt or operational email does **not** by itself prove that the LLC bank account was the payer. A product repository, delivered feature, client conversation or strategic decision does **not** by itself prove revenue.

This public repository MUST NOT become the canonical store for:

- bank account numbers or raw bank statements;
- confidential transaction descriptions;
- non-public customer/supplier contracts or payment details;
- tax payloads beyond safe management conclusions;
- personal payment details;
- secrets, tokens, signatures or unnecessary personal data.

Private source documents may be used for reconciliation while this file retains only the minimum safe conclusion needed to manage the Company.

## 3. Evidence states

AC-102 uses the following states:

- `Actual / authoritative` — supported by the source that is authoritative for the stated fact;
- `Actual provider evidence / payer attribution unknown` — a real provider-side charge or service fact is evidenced, but payment by ООО «Арвектум» is not established;
- `Estimate` — explicit management estimate with basis and uncertainty;
- `Known obligation` — committed corporate/contractual/operational obligation with an identified source;
- `Potential obligation` — plausible future cash or performance burden not yet established as committed;
- `Unknown` — insufficient evidence;
- `Not applicable` — explicitly outside the current Company scope.

`No evidence located` is not equivalent to `0`.

## 4. Established corporate and financial-context facts

The current evidence supports the following safe facts:

1. ООО «Арвектум» was registered on `2026-06-24` and was recorded as active at issuance of the registry evidence.
2. The Company has an operational business banking relationship. Account existence does not establish current balance, turnover or revenue.
3. The founding decision established charter capital of `10,000 RUB`, payable in money within four months from state registration. The actual payment status and payment date are not established by the evidence currently available to AC-102.
4. The document-derived four-month boundary from the `2026-06-24` registration date is `2026-10-24`. This is a management date derived from the founding decision and does not substitute for confirmation of actual payment or applicable accounting/legal treatment.
5. The registration package records submission of a notification to transition to the simplified taxation system. AC-102 does not infer from that filing the current tax object, rate, accrued tax amount or filing calendar.
6. A Company accounting-policy approval order exists with an effective date from `2026-06-24`; the appendices containing detailed accounting/tax methods are not available in the current evidence set and their substance is therefore not inferred here.
7. The current flagship direction remains «ИИ-компания под ключ», but a strategic direction is not a revenue fact.

## 5. Revenue and cash baseline

### 5.1 Business-line view

| Business line / source | Contracted / invoiced by LLC | Cash received by LLC | Evidence result |
|---|---:|---:|---|
| flagship «ИИ-компания под ключ» | Unknown | Unknown | no authoritative contract/invoice/bank evidence available in current AC-102 evidence set |
| procurement supplier/contractor activity | Unknown | Unknown | business/domain direction exists; LLC economics not established |
| Tender Agent / procurement software | Unknown | Unknown | product existence and pilot/productization status do not establish paid LLC revenue |
| Discount Parser / client automation | Unknown | Unknown | delivery/client-solution evidence exists outside this financial baseline; LLC attribution and payment are unverified |
| Doors Parser / client automation | Unknown | Unknown | mature delivery history exists; current LLC attribution/payment are unverified |
| Creative Test Agent | Unknown | Unknown | product/pilot evidence does not establish paid LLC revenue |
| Arvectum Proxy Launcher | Unknown | Unknown | productization work does not establish sales or license revenue |
| other Company revenue | Unknown | Unknown | no complete authoritative LLC revenue/cash register is available |

### 5.2 Cash position

| Measure | Current result | Reason |
|---|---:|---|
| opening funded cash after registration | Unknown | no authoritative transaction export available |
| cash received from customers | Unknown | no authoritative bank/accounting evidence available |
| other cash inflows / owner funding | Unknown | no authoritative bank/accounting evidence available |
| current bank cash balance | Unknown | account existence is not balance evidence |
| accounts receivable | Unknown | no receivables register / contract reconciliation available |
| accounts payable | Unknown | no payables register / contract reconciliation available |

**Management conclusion:** AC-102 has no evidence basis to classify any current business line as `0 revenue`, `revenue-producing`, `profitable` or `pre-revenue` at the LLC level solely from repository or email absence. Those classifications remain unresolved until banking/accounting/contract evidence is reconciled.

## 6. Cost and recurring run-rate baseline

The evidence set contains some real Company-use service evidence, but it does not yet establish the complete LLC-paid run-rate.

| Cost / service class | Evidenced amount / state | Attribution state | Current conclusion |
|---|---:|---|---|
| Company-use web hosting | `494 RUB` provider receipt dated `2026-07-03` | `Actual provider evidence / payer attribution unknown` | real provider-side renewal cost is evidenced; do not classify as LLC cash outflow until payer is reconciled |
| Company-use mail hosting | amount Unknown; service renewal/prolongation evidenced | payer and current continuation Unknown | operational service exists in the evidence set; monthly/annual run-rate not established |
| domain/support add-on service | amount Unknown; short-period prolongation evidenced | payer and current continuation Unknown | service existence does not establish a durable recurring obligation or run-rate |
| DomainSSL for `arvectum.com` | free certificate evidenced for the then-current issuance period | pre-incorporation acquisition context / future renewal Unknown | current zero-price certificate evidence does not imply future certificate cost is zero |
| banking/account services | Unknown | Unknown | bank tariff/statement required |
| accounting/tax administration | proposal/service information exists; accepted service/payment not evidenced | Unknown | treat as potential service only; do not create a recurring obligation from an offer |
| AI/model/software subscriptions | Unknown | Unknown | personal versus Company-funded usage must be separated |
| Git/repository/CI services | Unknown | Unknown | repository existence is not cost evidence |
| servers/VPS/storage beyond the hosting evidence above | Unknown | Unknown | provider/payment evidence required |
| signing/certificates/tokens beyond the free certificate fact above | Unknown | Unknown | actual acquisition/renewal evidence required |
| hardware/equipment | Unknown | Unknown | existing personal assets must be separated from Company purchase/capital expenditure |
| contractors/freelancers | Unknown | Unknown | contract/invoice/payment evidence required |
| customer/project direct costs | Unknown | Unknown | supplier/logistics/API/project spend requires reconciliation |
| legal/compliance/registrations | Unknown | Unknown | actual paid fee/service evidence required |

**Verified current LLC cash-paid recurring run-rate:** `Unknown`.

**Repository-safe provider-side cost evidence:** at least one `494 RUB` Company-use web-hosting renewal is evidenced privately, but payer/legal-entity attribution remains unresolved. It is therefore not counted as an ООО «Арвектум» cash outflow in this baseline.

## 7. Obligations baseline

### 7.1 Known corporate obligation

| Obligation | Amount / boundary | Status | Evidence result |
|---|---:|---|---|
| charter-capital monetary contribution | `10,000 RUB`; founding decision states payment within four months from state registration | `Known obligation / settlement Unknown` | actual payment status/date must be reconciled from banking/accounting evidence |

The management date derived from the founding decision is `2026-10-24`. AC-102 does not claim the obligation remains unpaid; it records that settlement cannot currently be verified.

### 7.2 Tax and accounting obligations

The evidence establishes that a simplified-tax-system transition notification was submitted at registration and that an accounting-policy approval order exists. It does **not** establish, for this AC-102 baseline:

- the currently applicable tax object/rate;
- accrued tax payable;
- insurance or payroll obligations;
- reporting deadlines that have already become payable obligations;
- accounting-service fees.

Those facts must be taken from current accounting/tax records or an authoritative accounting-service confirmation rather than inferred from registration filings.

### 7.3 Other obligation classes

Current status is `Unknown` unless separately evidenced:

- signed customer delivery obligations;
- supplier or contractor payables;
- refunds, warranties or support commitments;
- financing, credit, leasing or guarantee obligations;
- procurement bid/security/guarantee commitments;
- employee/contractor compensation;
- software/infrastructure subscriptions with binding renewal terms;
- domain/certificate renewal obligations;
- external product/support commitments;
- first-design-partner obligations for the flagship offer.

The evidence of a service existing or an offer being received is not converted automatically into a contractual or recurring obligation.

## 8. Procurement working-capital boundary

Procurement remains a Company business/domain line but is not the Company strategic center.

AC-102 must eventually capture for any live procurement deal, if one exists:

- supplier payment timing;
- customer advance/payment timing;
- cash-gap amount and duration;
- bid/contract security and guarantee requirements;
- logistics/direct cost;
- margin before financing and risk cost;
- committed versus merely quoted amounts.

No live procurement cash gap is invented in the absence of current contract, supplier and bank evidence.

## 9. Flagship investment burden

The flagship «ИИ-компания под ключ» is supported by material internal work across:

- Arvectum Company governance and operating-model development;
- Arvectum OS;
- product/module candidates;
- development/infrastructure tooling;
- Owner time.

The existence of that work is evidenced, but current monetary investment is not yet sufficiently measured.

AC-102 therefore separates:

1. **LLC cash cost** — actual external cash paid by ООО «Арвектум»;
2. **Owner-funded Company-use resources** — Company-relevant resources personally paid or contributed without LLC cash payment;
3. **Owner time investment** — material non-cash input, to be measured more fully by AC-104;
4. **one-time / sunk experiment cost** versus **recurring run-rate**;
5. **product/module-specific cost** versus **shared Company/Arvectum OS cost**.

The `494 RUB` web-hosting receipt demonstrates why this distinction matters: the Company-use service and amount are evidenced, while the LLC-payer fact is not.

No accounting, transfer-pricing, reimbursement or capitalization treatment is established by this management distinction.

## 10. Current management baseline

| Question | AC-102 current answer |
|---|---|
| How much revenue has ООО «Арвектум» earned? | `Unknown` — no authoritative revenue/accounting reconciliation available |
| How much customer cash has the LLC received? | `Unknown` |
| What is the current cash balance? | `Unknown` |
| What are current receivables/payables? | `Unknown` |
| What is the verified LLC-paid recurring monthly run-rate? | `Unknown` |
| Is there real Company-use external spending? | `Yes` — at least one `494 RUB` hosting renewal is provider-evidenced, but LLC payer attribution is unknown |
| Is the charter-capital requirement known? | `Yes` — `10,000 RUB`; settlement status/date Unknown |
| Are current tax amounts known? | `No` — registration filing evidence is insufficient to calculate current liability |
| Is flagship cash investment known? | `No` — internal work is evidenced, monetary attribution is incomplete |
| Can AC-102 support a profitability/runway conclusion? | `No` — not without authoritative banking/accounting evidence |

This is intentionally an evidence baseline rather than a fabricated P&L.

## 11. Completion gate and minimum Owner-local evidence intake

The smallest sufficient next input is an authoritative export for the ООО «Арвектум» business account covering:

`2026-06-24 → current date at time of export`.

Accepted practical forms:

- CSV/XLSX transaction export;
- PDF bank statement;
- or an Owner-prepared aggregate derived from the bank statement if every material inflow/outflow is categorized and traceable to the original source.

Raw financial data may remain private and MUST NOT be committed to this public repository.

If the bank export alone does not explain economic meaning, add only the smallest necessary supplements:

1. list of LLC contracts/orders/invoices with amount, date, business line and paid/unpaid state;
2. unpaid supplier/contractor/customer obligations not visible from bank movements;
3. recurring services/subscriptions not inferable from transaction history;
4. confirmation of charter-capital payment status/date;
5. any material owner-paid Company-use resources that the Owner wants included in management economics, clearly separated from LLC accounting facts.

Counterparty names may be replaced by stable aliases such as `client-A`, `supplier-B`, `hosting` or `software-subscription` in repository-safe outputs.

## 12. Cross-review result and current blocker

The AC-102 cross-review reached material convergence after `6 of maximum 10` iterations.

Result:

`BLOCKED — evidence model, source hierarchy and privacy boundary pass; the financial baseline cannot be closed without authoritative current banking/accounting evidence.`

Further review iterations were not consumed merely to reach the numerical maximum because the unresolved questions are evidence gaps rather than contradictory design choices. Cross-review resumes at iteration `7` after the authoritative financial intake, leaving at most four additional iterations under the Owner-set maximum of ten.

AC-102 MUST NOT be marked `Complete / PASS` and AC-103 MUST NOT be activated automatically while material revenue, cash, run-rate and obligation fields remain unresolved.

## 13. Resume and completion criteria

After the evidence intake, AC-102 must:

1. reconcile every material LLC inflow to a business line or explicitly classify it as non-revenue funding/other inflow;
2. reconcile material LLC outflows into recurring cost, one-time investment, project direct cost, tax/mandatory payment or other explicit class;
3. separate LLC-paid from Owner-paid Company-use resources;
4. establish current cash balance and material receivables/payables as of the chosen cutoff;
5. confirm charter-capital settlement status;
6. identify material known obligations and renewal/commitment dates;
7. calculate a repository-safe current recurring run-rate or explain why a cadence cannot yet be established;
8. identify which activities are evidenced cash-generating, cash-consuming or pre-revenue without using absence as zero;
9. update the flagship investment-burden view;
10. resume cross-review at iteration 7 and close only if no material financial-evidence gap remains for the declared AC-102 scope.

Until those criteria are met, the correct roadmap status is `Blocked`, not `Complete / PASS`.