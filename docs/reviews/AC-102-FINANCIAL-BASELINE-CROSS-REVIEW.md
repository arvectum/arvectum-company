# AC-102 — Revenue, Cash, Recurring Cost and Obligation Baseline Cross-Review

Status: `Complete / Blocked on evidence`
Review date: `2026-08-20`
Iterations completed: `6 of maximum 10`
Result: `BLOCKED — material review consensus reached; authoritative financial evidence is required before AC-102 can close`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-102 — Revenue, cash, recurring cost and obligation baseline`
Reviewed artifact: `docs/business/REVENUE-CASH-COST-OBLIGATION-BASELINE.md`
Reviewed publication: `0.2.0`
Reviewed publication commit: `69520e173216a0a8136167849b80bfbff232c329`
Prior start-state publication: `0.1.0`, commit `1cc6a9ddbafabde775c064943cbccfd178049229`
Maximum review iterations authorized by Owner: `10`

## 1. Review purpose

This review tests whether AC-102 gives the Owner an evidence-backed view of revenue, cash, recurring cost and obligations without fabricating financial truth from product status, email absence, provider receipts or strategic intent.

The review also tests whether the baseline is safe for a public repository and sufficient to determine whether AC-102 can proceed to `Complete / PASS` or must stop for authoritative financial intake.

The review is deliberately business-first. Its purpose is not to create an accounting system or a finance software layer. It is to establish the smallest reliable economic baseline needed for M1 decisions.

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

The labels are review perspectives only. They do not create Company Positions, authority, delegation or headcount.

## 3. Iteration 1 — Finance: source hierarchy and false-zero risk

**Primary lenses:** Finance, Owner, General Director.

**Material criticism:**

- the initial `0.1.0` artifact correctly used `Unknown`, but AC-102 still needed a stronger rule explaining which source is authoritative for cash, revenue, contractual obligation and provider cost;
- absence of bank statements, contracts or emails could be accidentally read as zero revenue or zero obligations;
- provider evidence could be mistaken for LLC-paid cash expense.

**Reconciliation:**

- publication `0.2.0` makes bank/accounting/contract/provider source roles explicit;
- `No evidence located ≠ 0` becomes an explicit rule;
- a separate state `Actual provider evidence / payer attribution unknown` is introduced;
- no business line is classified as zero-revenue, profitable or pre-revenue from repository/email absence.

**Result:** PASS. The baseline now prevents a false economic conclusion from missing evidence.

## 4. Iteration 2 — Revenue and Commercial: legal-entity attribution

**Primary lenses:** Commercial, Finance, Product & Portfolio, General Director.

**Material criticism:**

- Arvectum has product/client-delivery history, but delivery evidence does not prove that a contract, invoice or payment belongs to ООО «Арвектум» after incorporation;
- historical work can predate the LLC or belong to another contracting/payment context;
- the flagship «ИИ-компания под ключ» is a strategic direction, not current revenue merely because it is canonical strategy.

**Reconciliation:**

- revenue is organized by business line while `LLC contracted/invoiced` and `LLC cash received` remain separately evaluated;
- current product nodes remain `Unknown` financially until contract/bank/accounting evidence establishes LLC attribution;
- flagship monetization remains unproven and is not promoted into revenue.

**Result:** PASS on model; BLOCKED on values. The business-line structure is usable, but authoritative LLC revenue/cash values are still unavailable.

## 5. Iteration 3 — Cost and Operations: recurring run-rate versus Company-use resource

**Primary lenses:** Finance, Operations, Technology & Architecture, Risk & Continuity.

**Material criticism:**

- Company-use infrastructure can be evidenced without proving who paid it;
- a single payment does not establish a monthly recurring run-rate;
- operational emails saying a service was prolonged do not establish a durable subscription amount or current renewal obligation;
- personal and LLC-paid resources must remain distinct for both accounting truth and management economics.

**Reconciliation:**

- a private provider receipt supports one real `494 RUB` Company-use hosting renewal while payer/legal-entity attribution remains explicitly unknown;
- mail/domain-support service existence is recorded without inventing cost or cadence;
- a free certificate is not converted into a permanent zero-cost assumption;
- `Verified current LLC cash-paid recurring run-rate` remains `Unknown`;
- the baseline explicitly separates LLC cash cost from Owner-funded Company-use resources.

**Result:** PASS on classification; BLOCKED on full run-rate. Current private provider evidence improves the baseline but is insufficient to establish complete LLC cost economics.

## 6. Iteration 4 — Legal, Tax and Corporate Obligations: obligation must have a source

**Primary lenses:** Legal & Compliance, Finance, General Director, Owner.

**Material criticism:**

- the founding decision creates a concrete charter-capital funding requirement, but current evidence does not show settlement;
- the registration package includes a simplified-tax-system transition notification, but that filing cannot safely determine current tax object/rate or payable tax;
- an accounting-service offer must not become a recurring obligation merely because it was received;
- a Company accounting-policy order exists, but its unavailable appendices mean exact accounting/tax methods must not be inferred.

**Reconciliation:**

- charter capital is recorded as a `Known obligation / settlement Unknown` with the `10,000 RUB` amount and document-derived four-month boundary;
- the document-derived date `2026-10-24` is explicitly management derivation, not proof of unpaid status or a substitute for legal/accounting confirmation;
- tax notification filing and accounting-policy existence are recorded only to the level supported by evidence;
- offers, service-existence notices and potential renewals remain `Potential` or `Unknown` until commitment evidence exists.

**Result:** PASS. The baseline does not invent tax or contractual obligations beyond the available source scope.

## 7. Iteration 5 — Owner / Product / Portfolio: flagship investment burden

**Primary lenses:** Owner, Product & Portfolio, Finance, People & Organization.

**Material criticism:**

- the Company is investing substantial work in Arvectum Company, Arvectum OS and module/product candidates, but treating that work as zero-cost would distort the flagship business case;
- conversely, assigning arbitrary monetary values to Owner time or personal hardware would fabricate economics;
- shared Company/OS investment must not be allocated to one product without a later cost-allocation rule.

**Reconciliation:**

- the baseline separates LLC cash cost, Owner-funded Company-use resources, Owner time, one-time/sunk cost and recurring run-rate;
- Owner time is flagged as material but deferred for fuller workload measurement under AC-104;
- product/module-specific versus shared Company/OS cost remains an explicit unresolved attribution question;
- no transfer-pricing, reimbursement or capitalization rule is invented.

**Result:** PASS. The baseline preserves the economic burden as a management question without fabricating accounting treatment.

## 8. Iteration 6 — Security / Risk / all-lens convergence: can AC-102 honestly close?

**Primary lenses:** Security & Data, Risk & Continuity, Finance, Owner, all remaining lenses.

**Material criticism:**

- the public repository must not receive raw bank statements, account details or confidential transaction/customer data simply to make AC-102 look complete;
- the baseline still lacks the facts necessary to answer the core economic questions: customer cash received, bank balance, receivables/payables, LLC-paid recurring run-rate and settlement of the charter-capital contribution;
- consuming additional review iterations cannot create these facts.

**Reconciliation:**

- repository-safe summaries remain separated from private authoritative sources;
- the minimum Owner-local evidence intake is reduced to a business-account export from `2026-06-24 → current date`, with only the smallest necessary contract/obligation supplements;
- the baseline is explicitly marked `Blocked / Financial evidence intake required`;
- AC-103 is not activated automatically;
- review stops at `6/10` rather than spending iterations 7–10 on speculation;
- after evidence intake, review resumes at iteration 7, leaving at most four iterations under the Owner-authorized maximum.

**Result:** BLOCKED. This is a valid review result, not a failure of the artifact design.

## 9. Acceptance test

| Test | Result | Evidence / reason |
|---|---|---|
| financial source hierarchy is explicit | PASS | bank/accounting/contract/provider roles separated |
| missing evidence is not treated as zero | PASS | explicit `No evidence located ≠ 0` rule |
| LLC versus historical/personal activity can be separated | PASS on model | values still require bank/contract evidence |
| current LLC revenue can be stated | BLOCKED | authoritative LLC revenue reconciliation unavailable |
| current customer cash received can be stated | BLOCKED | authoritative bank transaction export unavailable |
| current cash balance can be stated | BLOCKED | authoritative bank statement unavailable |
| current receivables/payables can be stated | BLOCKED | no reconciled contract/accounting register available |
| current LLC-paid recurring run-rate can be stated | BLOCKED | partial provider evidence exists but payer/cadence/full set unresolved |
| known charter-capital obligation is represented without false unpaid claim | PASS | amount/boundary known; settlement explicitly Unknown |
| tax/accounting facts stay within available source scope | PASS | notification/order not over-interpreted |
| provider evidence is not confused with LLC payment | PASS | `494 RUB` classified with payer attribution unknown |
| flagship investment burden is represented without invented accounting | PASS with follow-up | cash/time/allocation values incomplete |
| public-repository data boundary is preserved | PASS | raw financial/private payload remains external |
| AC-102 is sufficient for profitability/runway conclusion | BLOCKED | key financial values remain Unknown |
| AC-102 may be marked Complete / PASS | NO | completion criteria not met |

## 10. Why the review stops at iteration 6 of 10

The Owner specified a maximum of ten cross-review iterations, not a requirement to consume ten iterations regardless of evidence value.

At iteration 6, every material remaining issue has the same root cause: missing authoritative banking/accounting/contract evidence. Additional review could only restate the same gap or speculate about numbers, which would violate the evidence-first and business-first rules.

Therefore the correct controlled stop is:

`6/10 — review convergence reached; execution blocked on Owner-local financial evidence intake.`

The iteration budget is preserved. If evidence is supplied, the review resumes at iteration 7 and may use no more than four further iterations for reconciliation and closure.

## 11. Required resume evidence

Primary required evidence:

- authoritative ООО «Арвектум» business-account transaction export or bank statement from `2026-06-24` through the current date at export.

Only where the bank record is insufficient, add:

- LLC contracts/orders/invoices summary;
- unpaid commitments not visible in cash transactions;
- recurring subscription/service list where cadence cannot be inferred;
- charter-capital payment confirmation;
- optional material Owner-paid Company-use resources for management economics, clearly separated from LLC accounting facts.

Raw evidence should remain private and must not be copied into the public repository by default.

## 12. Final conclusion

`BLOCKED — material review consensus reached at 6 of maximum 10 iterations.`

The AC-102 artifact itself is structurally sufficient for the declared scope, but the Company does not yet possess in the reviewed evidence set the authoritative data required to populate its core financial facts.

The roadmap must therefore remain on AC-102 with status `Blocked`, and no automatic transition to AC-103 should occur.

Resume condition:

> provide or reconcile the authoritative current LLC banking/accounting evidence, populate the material financial fields, then continue cross-review from iteration 7.

This result preserves the distinction between a technically complete template and a genuinely evidence-backed Company financial baseline.