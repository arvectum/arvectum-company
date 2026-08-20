# AC-102 — Revenue, Cash, Recurring Cost and Obligation Baseline

Status: `Current / Evidence collection`
Version: `0.1.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-102 — Revenue, cash, recurring cost and obligation baseline`
Depends on: `AC-101 — Current business model and value proposition baseline`

## 1. Purpose

This artifact starts the first evidence-backed Company financial/commitment baseline.

It must let the Owner distinguish:

- real ООО «Арвектум» revenue from intended monetization;
- contracted/invoiced value from cash actually received;
- current LLC activity from historical work outside the LLC;
- recurring cost from one-time investment;
- current cash-producing work from pre-revenue investment;
- known obligations from possible future obligations;
- actual figures from estimates and unknowns.

This public repository is **not** the canonical store for bank transactions, confidential contracts, payment details, tax records or customer/supplier financial payloads. Those remain in their appropriate authoritative systems. This file stores only repository-safe management conclusions and safe source locators.

## 2. Current evidence boundary

At AC-102 start, the Company repository and current Project Sources provide a corporate/business structure but **do not provide sufficient authoritative transaction-level financial evidence** to close this task.

Known safe facts:

- ООО «Арвектум» exists as a registered legal entity from `2026-06-24`;
- the Company has an owner-managed banking relationship / operational payment reference;
- the founding decision established charter capital of `10,000 RUB` and required its monetary payment within the stated post-registration period;
- the current AC-101 flagship direction is «ИИ-компания под ключ»;
- the portfolio contains current product/client-solution nodes, but repository/product evidence does not establish the amount, date or legal-entity attribution of revenue/cash from them;
- the current Company repository contains no authoritative bank statement, accounting ledger, receivables/payables register, recurring-subscription ledger or full contract-obligation register.

No balance, transaction, revenue, margin, cost or debt figure is inferred from the existence of a bank account, repository, product, delivered feature or historical client conversation.

## 3. Financial evidence states

AC-102 uses:

- `Actual` — supported by authoritative financial/accounting/banking/contract evidence;
- `Estimate` — explicit management estimate with basis and uncertainty;
- `Known obligation` — legally/contractually/operationally committed with source;
- `Potential obligation` — plausible but not yet committed;
- `Unknown` — insufficient evidence;
- `Not applicable` — explicitly outside the current Company scope.

## 4. Revenue and cash baseline — current start state

| Business line / source | Contracted / invoiced | Cash received | Current evidence state | AC-102 action |
|---|---:|---:|---|---|
| flagship «ИИ-компания под ключ» | Unknown | Unknown | no canonical financial evidence currently available; strategic direction is not a revenue fact | verify whether any customer/discovery/pilot payment or signed commitment already exists |
| procurement supplier/contractor activity | Unknown | Unknown | business/domain direction exists; current ООО «Арвектум» revenue/cash not evidenced in Company repo | reconcile contracts/invoices/bank receipts, if any |
| Tender Agent / procurement software | Unknown | Unknown | product exists; SaaS/productized monetization direction does not prove current revenue | verify current paid users/contracts/subscriptions, if any |
| Discount Parser / client automation | Unknown | Unknown | productized client-solution evidence exists; current LLC revenue attribution is unverified | reconcile customer contract/invoice/payment and whether it belongs to LLC |
| Doors Parser / client automation | Unknown | Unknown | mature delivery evidence exists; current LLC revenue attribution is unverified | reconcile historical delivery/payment legal entity and date |
| Creative Test Agent | Unknown | Unknown | controlled product/pilot evidence; no Company financial evidence in current repo | verify paid/discounted/unpaid pilot status and any commitment |
| Arvectum Proxy Launcher | Unknown | Unknown | productization evidence; Company-level monetization not fixed | verify current sales/license/payment state |
| other Company revenue | Unknown | Unknown | no complete authoritative revenue register available | compare bank/accounting sources to product/business map |

**Current conclusion:** no business line is classified as revenue-producing or pre-revenue solely from repository/product status. AC-102 requires authoritative financial evidence.

## 5. Cost baseline — evidence collection map

| Cost class | Current amount/cadence | Evidence state | Notes / source needed |
|---|---:|---|---|
| banking/account services | Unknown | Unknown | bank tariff/statement or accounting record |
| accounting/tax administration | Unknown | Unknown | accountant/service contract, tax calendar, paid invoices |
| domains/DNS/email | Unknown | Unknown | registrar, Cloudflare/mail/provider invoices if Company-paid |
| hosting/servers/VPS/storage | Unknown | Unknown | provider invoices and payment source |
| AI/model/software subscriptions | Unknown | Unknown | distinguish personal tools from Company-paid tools; identify only materially Company-borne cost |
| Git/repository/CI services | Unknown | Unknown | actual paid tier/cost only, not assumed from repository existence |
| signing/certificates/tokens | Unknown | Unknown | actual Company-paid acquisition/renewal cost only |
| hardware/equipment | Unknown | Unknown | distinguish existing personal assets from Company purchase/capital expenditure |
| contractors/freelancers | Unknown | Unknown | contract/invoice/payment evidence |
| customer/project direct costs | Unknown | Unknown | supplier, logistics, API/service, delivery or project-specific spend |
| procurement working capital | Unknown | Unknown | supplier prepayment/payment timing vs customer payment timing |
| legal/compliance/registrations | Unknown | Unknown | actual fees/services only |
| other recurring Company costs | Unknown | Unknown | identify from bank/accounting evidence rather than memory alone |

## 6. Obligations baseline — current start state

### 6.1 Known corporate obligation requiring status confirmation

The founding decision established charter capital of `10,000 RUB` with monetary payment required within the stated post-registration period.

AC-102 must confirm the **actual payment status and date** from authoritative banking/accounting evidence. This artifact does not assume either paid or unpaid status.

### 6.2 Obligation classes requiring reconciliation

The following are not declared current obligations until evidence confirms them:

- taxes and mandatory payments;
- accounting service fees;
- recurring software/infrastructure subscriptions;
- customer delivery obligations;
- supplier/contractor payables;
- refunds, warranties or support commitments;
- financing/credit/guarantee obligations;
- procurement security/guarantee requirements;
- employee/contractor compensation;
- domain/certificate renewals;
- external product/support commitments;
- first-design-partner obligations for the flagship offer.

## 7. Flagship investment burden

The flagship «ИИ-компания под ключ» is currently supported by substantial internal work across:

- Arvectum Company governance and operating-model development;
- Arvectum OS;
- product/module candidates;
- infrastructure and development tooling;
- Owner time.

The existence of this work is evidenced, but its financial cost is **not yet measured**.

AC-102 should separate at minimum:

1. **cash cost** — actual external money spent by ООО «Арвектум»;
2. **Owner-funded/personal resource contribution** — Company-relevant resources paid personally or provided without Company cash payment, if the Owner chooses to include them in management economics;
3. **Owner time investment** — measured later in detail under AC-104, but AC-102 may flag it as a material non-cash investment;
4. **sunk experiment cost** versus **recurring run-rate**;
5. costs specific to one product/module versus shared Company/OS capability cost.

No transfer-pricing or accounting treatment is established by this management distinction.

## 8. Minimum evidence bundle needed to complete AC-102

The smallest practical evidence package is:

1. **Banking:** transaction export/statement from the start of ООО «Арвектум» activity to the current date, or an Owner-prepared aggregate with every material inflow/outflow categorized. Raw bank details do not belong in this public repo.
2. **Revenue/contracts:** list of contracts/orders/invoices issued by the LLC, with customer identity redacted here if confidential; include amount, date, payment state and business line.
3. **Payables/obligations:** list of signed customer/supplier/contractor commitments, unpaid invoices, expected mandatory payments and material renewal dates.
4. **Recurring costs:** monthly/annual Company-borne subscriptions and services with amount, cadence and payer.
5. **One-time Company spend:** incorporation, signing, hardware, software, contractors or infrastructure paid by the LLC.
6. **Owner-paid Company resources:** optional but economically useful list of material Company-use costs currently paid personally, clearly separated from LLC accounting facts.
7. **Charter capital:** confirmation of payment status/date.

The Owner may provide either source documents privately or a compact aggregate table. AC-102 does not require publication of raw financial evidence.

## 9. Suggested safe input format

For fast reconciliation, each material financial item can be supplied as:

```text
Date | Type | Business line | Amount | Currency | Cash/Accrual | Counterparty category | Paid/Unpaid | Recurring? | Source | Notes
```

Where confidentiality matters, use categories such as `client-A`, `supplier-B`, `hosting`, `accounting`, `software-subscription` instead of names.

## 10. Current status and blocker

AC-102 has started and the evidence model is established.

**Current blocker:** authoritative current financial/obligation data is not available in the Company repository or Project Sources at the level needed to populate actual revenue, cash, recurring cost and obligation figures.

The next execution step is financial evidence intake and reconciliation. Once the minimum evidence bundle is available, this artifact can be completed without redesigning the model.

AC-102 must not be marked `Complete / PASS` until actual Company financial evidence replaces the material `Unknown` fields.