# AC-102 — Revenue, Cash, Recurring Cost and Obligation Baseline

Status: `Complete / PASS`
Version: `0.3.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-102 — Revenue, cash, recurring cost and obligation baseline`
Depends on: `AC-101 — Current business model and value proposition baseline`
Review: `docs/reviews/AC-102-FINANCIAL-BASELINE-CROSS-REVIEW.md`

## 1. Purpose and scope correction

AC-102 defines the Company-level economic structure needed to design and govern Arvectum as a business.

It is **not** a bookkeeping task, transaction audit, bank-reconciliation exercise, tax calculation or substitute for the Company's outsourced accounting function.

The Owner has clarified the operating boundary:

- accounting, tax records, bank reconciliation, statutory reporting and transaction-level financial administration are handled by the Company's professional accounting contour;
- Arvectum Company governance needs only the management/business model: where money can come from, where it structurally goes, which obligation classes matter, which costs are fixed/recurring versus variable/project-driven, and which economic information must reach the Owner for decisions.

Detailed receipts, individual subscriptions and account movements are deliberately outside this artifact unless a later management decision specifically requires them.

## 2. Financial operating boundary

The Company financial model has three distinct layers:

| Layer | Responsibility | Company-repository role |
|---|---|---|
| statutory/accounting layer | outsourced accounting, bank/accounting systems, tax and legal records | external source of truth; not duplicated here |
| management-finance layer | economic interpretation for Owner decisions, budgets, commitments, portfolio and risk | Company-level models and summaries |
| product/project economics | product revenue model, direct cost, implementation/support burden, unit economics | product/portfolio evidence feeding Company decisions |

Arvectum Company therefore needs **management visibility**, not a parallel accounting system.

## 3. Revenue architecture

Current and intended Company revenue is organized into the following business engines.

| Revenue engine | Value sold | Primary capture mechanisms | Current strategic role |
|---|---|---|---|
| flagship «ИИ-компания под ключ» | discovery, organizational design, deployment, configuration and transformation of a customer into an AI-native operating organization | implementation/project fee; later recurring support/runtime/module revenue | flagship commercial direction |
| reusable functional modules | reusable business-function capability embedded in customer organizations | module/license/subscription/service uplift or bundle | module candidates; admission requires evidence |
| Arvectum OS commercial reliance | domain-neutral organizational runtime/substrate where commercially exposed | bundled implementation, subscription/license or managed runtime are later packaging choices | enabling substrate, not a separate Company by itself |
| standalone software products | narrow software value outside a full AI-company deployment | license, subscription, project fee or service model per product | portfolio-specific |
| client automation/custom development | customer-specific automation, parsers, integrations and implementation work | project/customization fee | near-term cash/revenue line and market evidence |
| procurement supplier/contractor activity | delivery of goods and tender/procurement execution | contract/project margin | real business/domain line and proof environment |

No revenue engine is assumed profitable merely because it exists. Pricing and measured unit economics remain product/portfolio decisions where evidence is required.

## 4. Cash architecture

For Company-design purposes, cash movements are classified by business meaning rather than individual transaction.

### Cash inflows

- customer receipts from implementation/project work;
- product/license/subscription receipts;
- procurement contract receipts;
- owner capital/funding where applicable;
- financing or other non-revenue funding where explicitly approved.

### Cash outflows

- shared Company operating costs;
- product/module development and operation;
- project-specific delivery costs;
- procurement working capital and supplier payments;
- contractors/personnel;
- infrastructure/software/tools;
- legal, accounting, compliance and administrative costs;
- taxes and mandatory payments;
- financing/security/guarantee costs where applicable;
- approved capital expenditure.

The accounting contour determines actual balances and transaction treatment. Company governance uses these categories for decision-making and later management reporting.

## 5. Cost architecture

Costs are separated along two axes.

### 5.1 Behaviour

- **recurring/fixed or semi-fixed** — accounting service, core infrastructure, domains/mail, necessary software, repository/CI services where paid, baseline security/signing and other continuing Company operation;
- **variable/project-direct** — supplier purchases, logistics, customer-specific infrastructure, external contractors, integrations and project-specific services;
- **one-time/capital/investment** — incorporation, equipment, initial infrastructure, product creation and other non-recurring investment;
- **non-cash Owner investment** — Owner time and resources relevant to management economics but not treated here as accounting expenses.

### 5.2 Economic ownership

- shared Company cost;
- Arvectum OS/shared platform investment;
- product/module-specific cost;
- customer/project-direct cost;
- procurement working-capital cost.

Exact cost allocation is not required at this phase. The important baseline is that these classes remain distinguishable so one product is not accidentally credited with shared costs or burdened with unrelated Company expenditure.

## 6. Obligation architecture

Material Company obligations fall into six management classes:

1. **corporate/statutory** — legal, tax, accounting and other mandatory obligations handled in the professional accounting/legal contour;
2. **customer** — signed delivery, acceptance, support, warranty, confidentiality, data/security and other commitments;
3. **supplier/contractor** — payments, acceptance and dependencies created by external performers/providers;
4. **recurring operating** — infrastructure, software, domains, services and renewals needed for continuity;
5. **procurement/financing** — working-capital commitments, supplier prepayment, contract/bid security, guarantees or financing;
6. **product/support** — commitments created by selling, licensing, hosting or supporting Arvectum products/modules.

A strategic idea, roadmap item or technical capability does not create an obligation by itself. External obligations require the appropriate contract/authority path.

## 7. Procurement cash-gap model

Procurement remains one business line rather than the Company center, but it has a structurally distinct financial profile.

A procurement deal can create:

`customer payment timing → supplier payment timing → working-capital gap → financing/security cost → delivery/direct cost → realized project margin`

Therefore procurement decisions must consider cash-gap size/duration, supplier terms, customer payment terms, guarantees/security and downside exposure before commitment. The exact calculation belongs to the deal/product workflow, not this Company baseline.

## 8. Flagship investment model

The flagship «ИИ-компания под ключ» is supported by four investment pools:

- Arvectum Company as the internal reference implementation;
- Arvectum OS as the domain-neutral substrate;
- reusable module/product candidates;
- customer-discovery, implementation and commercial work.

For management decisions, future reviews should distinguish:

- shared capability investment versus customer-specific work;
- reusable module investment versus standalone-product investment;
- recurring operating burden versus one-time development;
- Owner workload versus external cash cost;
- customer implementation cost versus recurring support cost.

This is enough for current business-structure design. Detailed capitalization, reimbursement or accounting treatment belongs to the accounting/legal contour.

## 9. Accounting and management interface

Outsourced accounting is treated as a professional external operating function, not something Arvectum Company should recreate internally.

The Company operating model needs a simple interface from that contour into Owner management:

- current available cash / material liquidity issue;
- taxes or mandatory payments requiring attention;
- material receivables/payables;
- material new or overdue obligations;
- unusual or high-value cash movement requiring management context;
- periodic management summary sufficient for budget and portfolio decisions.

The exact report format/cadence belongs later in `AC-404 — Cash, commitment and management reporting baseline` and the operating model. It does not block AC-102.

## 10. Management rules derived from the baseline

1. Do not build a parallel bookkeeping system inside Arvectum Company.
2. Do not require the Owner to manually classify routine receipts and bank transactions when professional accounting already owns that function.
3. Company governance works with economic classes, commitments, budgets and exceptions; accounting systems retain transaction truth.
4. A new initiative should identify its plausible revenue mechanism, recurring burden, direct-cost class and material obligation boundary before meaningful investment.
5. A customer project must distinguish implementation revenue from recurring support/runtime burden.
6. A reusable module must eventually demonstrate economics independently from the fact that its underlying product/repository exists.
7. Procurement deals require explicit working-capital/risk treatment because revenue and cash timing can diverge materially.
8. Owner attention should be pulled by exceptions and decisions, not routine bookkeeping.

## 11. AC-102 result

AC-102 establishes a sufficient Company-level baseline for:

- revenue architecture;
- cash-flow categories;
- recurring/variable/investment cost structure;
- obligation classes;
- procurement working-capital boundary;
- flagship investment structure;
- the boundary between outsourced accounting and Company management.

Transaction-level amounts are intentionally **not an AC-102 completion criterion**. They may be consumed later through accounting/management reporting when an actual business decision needs them.

Cross-review result: `PASS at iteration 7 of maximum 10` after the Owner corrected the task boundary from transaction-level financial evidence collection to business/economic structure.

Next canonical action: `AC-103 — Current customer/client lifecycle and real value-stream map`.