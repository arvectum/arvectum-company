# AC-102 — Revenue, Cash, Recurring Cost and Obligation Baseline Cross-Review

Status: `Complete / PASS`
Review date: `2026-08-20`
Iterations completed: `7 of maximum 10`
Result: `PASS — task scope corrected to Company-level business/economic structure; accounting detail remains delegated`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-102 — Revenue, cash, recurring cost and obligation baseline`
Reviewed artifact: `docs/business/REVENUE-CASH-COST-OBLIGATION-BASELINE.md`
Reviewed publication: `0.3.0`
Maximum review iterations authorized by Owner: `10`

## 1. Review purpose

This review tests whether AC-102 provides the economic structure needed to design and govern Arvectum Company without duplicating professional accounting work or turning the Company repository into a transaction ledger.

## 2. Review lenses

The cross-review uses eleven functional perspectives:

1. Owner / Founder;
2. General Director;
3. Finance;
4. Operations;
5. Product & Portfolio;
6. Technology & Architecture;
7. Commercial;
8. Legal & Compliance;
9. Security & Data;
10. People & Organization;
11. Risk & Continuity.

These are review lenses only and do not create Positions or authority.

## 3. Iterations 1–6 — retained findings

The first six iterations established several useful controls that remain valid:

- revenue intent must not be confused with actual revenue;
- accounting/banking/contract systems remain authoritative for their own facts;
- missing evidence must not be converted into fabricated numbers;
- provider-side cost evidence must not be confused with accounting treatment;
- personal/Owner resources and Company-paid costs should remain conceptually separable;
- public Company governance should not store raw bank statements, confidential contracts or unnecessary sensitive financial payloads;
- procurement has a distinct working-capital/cash-gap profile;
- shared Company/OS investment must not be silently attributed to one product.

However, iteration 6 incorrectly treated transaction-level financial reconciliation as a completion requirement for AC-102.

## 4. Iteration 7 — Owner scope correction: management model, not bookkeeping

**Primary lenses:** Owner, General Director, Finance, Operations, all remaining lenses.

**Owner correction:**

The Company already has outsourced accounting. AC-102 is intended to help describe the business structure and business model, not to make the Owner or ChatGPT inspect individual receipts, reconcile bank movements or recreate accounting work.

**Material criticism of the previous interpretation:**

- the task drifted from Company design into bookkeeping;
- detailed bank/receipt reconciliation creates Owner workload without improving the organizational model at this stage;
- the external accounting function already owns transaction-level accounting/tax truth;
- a Company-level financial baseline can be complete when it defines revenue engines, cash-flow categories, cost classes, obligation classes, working-capital logic and the accounting↔management interface;
- exact management reporting values/cadence belong later in AC-404 and operational finance, not as a blocker to business-model design.

**Reconciliation:**

Publication `0.3.0` is rewritten around the correct boundary:

- revenue architecture rather than transaction list;
- cash-in/cash-out categories rather than bank reconciliation;
- recurring/variable/investment cost architecture rather than receipt inventory;
- obligation classes rather than detailed payable register;
- procurement cash-gap logic at the business-model level;
- flagship investment pools and cost-ownership distinctions;
- outsourced accounting as the professional transaction/statutory layer;
- Company management as the layer that consumes summaries, budgets, commitments and exceptions;
- routine bookkeeping is explicitly excluded from Company/Owner work.

**Result:** PASS.

## 5. Acceptance test

| Test | Result |
|---|---|
| defines where Company revenue can structurally come from | PASS |
| distinguishes flagship, modules, standalone products, client automation and procurement revenue engines | PASS |
| defines business-meaningful cash inflow/outflow classes | PASS |
| distinguishes recurring, variable/project and one-time/investment costs | PASS |
| distinguishes shared Company/OS/product/project cost ownership | PASS |
| defines material obligation classes | PASS |
| captures procurement working-capital/cash-gap logic | PASS |
| captures flagship investment structure | PASS |
| keeps statutory/accounting truth with professional accounting systems | PASS |
| avoids parallel bookkeeping and manual Owner receipt classification | PASS |
| defines the future accounting→management interface | PASS |
| preserves public-repository safety | PASS |
| sufficient to continue Company business-structure work | PASS |

## 6. Why the review closes at iteration 7 of 10

The Owner authorized a maximum of ten iterations, not a requirement to consume all ten.

After the scope correction, no material contradiction remains. Iterations 8–10 would add detail without improving the business-model baseline and would violate the business-first principle.

## 7. Final conclusion

`PASS — material consensus reached at 7 of maximum 10 iterations.`

AC-102 is complete as a **Company-level management/economic baseline**. It intentionally does not determine individual transaction amounts, tax calculations, receipt attribution or bank balances.

Those operational facts remain with the outsourced accounting/banking contour and may later flow into management reporting when needed for actual decisions.

Recommended roadmap transition:

`AC-102 Complete / PASS → AC-103 Current`.