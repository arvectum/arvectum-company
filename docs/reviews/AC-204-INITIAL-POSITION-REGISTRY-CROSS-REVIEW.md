# AC-204 — Initial Position Registry Cross-Review

Status: `Complete / PASS for Owner approval`
Review date: `2026-08-20`
Iterations completed: `10 of maximum 10`
Result: `PASS — after the Owner rejected the initial Finance+Security/Assurance bundle, the proposal now defines six evidence-backed executor-neutral Company Positions, separates finance/obligation control from security/risk/continuity assurance, places organizational state/evidence with Company Executive, covers all eight AC-201 functions, and preserves AC-202 Reserved Owner Decisions, AC-203 delegation semantics and legal/corporate/customer/Product/OS boundaries without creating fake headcount`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-204 — Initial Position Registry`
Reviewed artifact: `docs/organization/INITIAL-POSITION-REGISTRY.md`
Reviewed publication: `Proposed 0.9.1`
Reviewed blob SHA: `9804a57a6cee027712e0c95bbf95bd428f848410`
Maximum review iterations: `10`
Approval status: `Pending explicit Owner approval of the exact reviewed proposal`
Arvectum OS main re-checked: `dff9591a9897743c48c56bbe2320260c2e0a071c`

## 1. Review purpose

This review tests whether AC-204 creates the **minimum useful Position structure** for the real current Company rather than:

- mechanically creating one Position per AC-201 function;
- turning familiar department labels into fake headcount;
- preserving the Owner as universal operator under a new title;
- confusing Owner/participant/General Director legal capacities with an internal Position;
- making AI agents, products, repositories or runtimes into Positions;
- granting authority that AC-202/AC-203 do not support;
- over-bundling responsibilities until accountability/control domains lose meaning;
- or creating separation that exists only on paper while current-scale execution can no longer be practical.

Review lenses include Owner/legal authority, Company operating integration, Commercial/Customer, Portfolio/Product, Engineering/Release, Finance/Obligations, Organizational State/Evidence, Security/Data, Risk/Continuity, organizational design, Product/OS boundaries and flagship transferability.

These are review perspectives only and do not create extra Positions.

## 2. Iteration 1 — reject one-function-one-Position modeling

**Criticism:** AC-201 contains eight functions. Creating eight Positions would convert the analytical function map directly into headcount-shaped organization without evidence.

**Reconciliation:** the proposal applies a separate Position admission test. Functions may be bundled where current accountability/context supports it, while distinct Positions require a real responsibility, control or continuity reason.

The initial draft admitted five Positions rather than eight.

**Result:** PASS as a modeling principle. The exact Position count remained reviewable and was later changed by iteration 10.

## 3. Iteration 2 — Owner, participant, General Director and Company Executive must not collapse into one authority source

**Criticism:** `POS-001 — Company Executive` could be read as equivalent to Owner or General Director and accidentally manufacture legal/corporate authority from an internal Position.

**Reconciliation:** Owner, participant/general-meeting competence and General Director legal office are explicit **non-Position authority anchors**. `POS-001` owns delegated operating integration only.

Its title creates no General Director power, participant competence, bank/signature authority, `ROD-*` authority or external representation right.

A later AC-205 Assignment may place the same natural person in several capacities, but the authority sources remain distinct.

**Result:** PASS.

## 4. Iteration 3 — Commercial and Customer Delivery: split or bundle?

**Criticism:** `F-02` Commercial Discovery and `F-03` Customer Delivery are different lifecycle stages and could be separate Sales and Delivery/Customer Success Positions.

**Counter-evidence:** current evidence identifies customer-context continuity itself as a material bottleneck. Discovery meaning, scope, defect-vs-change classification and acceptance are still tightly coupled, while a repeatable acquisition engine is not proven.

**Reconciliation:** `POS-002 — Commercial & Customer Lead` keeps `F-02` and `F-03` together for now, with explicit authority exclusions and split triggers for scale, incentive conflict, customer concurrency and independent support workload.

**Result:** PASS.

## 5. Iteration 4 — Portfolio/Product accountability must be distinct from Engineering

**Criticism:** current-scale execution often combines deciding what to build with building it, so a minimal model could merge `F-04` and `F-05`.

**Risk:** that would preserve the Owner/universal-interpreter priority bottleneck and allow implementation sunk cost to influence portfolio authority.

**Reconciliation:** separate `POS-003 — Portfolio & Product Lead` and `POS-004 — Engineering & Release Lead` are retained. Product repositories remain canonical for detailed implementation, while major investment/start/stop/reclassification remains under AC-202.

**Result:** PASS.

## 6. Iteration 5 — initial Finance + Organizational State + Security/Risk bundle

**Criticism:** the initial `POS-005 — Company Operations & Assurance Lead` combined `F-06`, `F-07` and `F-08`. Finance, organizational evidence and security/risk are materially different domains and could eventually create independence conflicts or a control bottleneck.

**Initial reconciliation:** because current evidence did not justify CFO/CISO/PMO headcount, the first proposal bundled them and denied `AM-3` self-approval, with future split triggers.

**Initial result:** provisional PASS at iteration 5.

**Later status:** **superseded by the Owner's iteration-10 correction.** The Owner explicitly judged Finance and Security better represented as separate authority/accountability boundaries. That correction is accepted as a material organizational-design improvement rather than treated as a staffing request.

## 7. Iteration 6 — authority model must not outrun available evidence

**Criticism:** AC-203 defines `AM-0` through `AM-4`. Immediately granting delegated approval or consequential automation would pre-empt AC-205 Principal eligibility, AC-206 access and concrete workflow evidence.

**Reconciliation:** the initial design ceiling for every Position remains `AM-0`, `AM-1` and `AM-2` only. No Position receives `AM-3` or `AM-4` initially.

This remains true after the Finance/Security split.

**Result:** PASS.

## 8. Iteration 7 — product, customer, external service and Arvectum OS boundaries

**Criticism:** cross-company Positions could accidentally internalize authority that belongs to product repositories, customers, accounting/banking systems, legal/corporate actors or Arvectum OS governance.

**Reconciliation:** the proposal explicitly preserves all of those boundaries. The Position Registry creates no Product Contract, OS Position, customer authority, statutory-accounting authority, legal office or cross-repository commitment.

Current Arvectum OS `main` was re-checked at `dff9591a9897743c48c56bbe2320260c2e0a071c`; the OS Constitution remains Ratified `1.2.0`, while the OS Decision Authority Policy remains Proposed `0.2.1` and is not treated as binding Company authority.

**Result:** PASS.

## 9. Iteration 8 — Positions must not become AI-agent slots or a staffing plan

**Criticism:** named Positions can be mistaken for required employees or mechanically translated into one AI agent per Position.

**Reconciliation:** Position count is explicitly separate from executor count. One Principal may hold several Assignments; one Position may use human/AI/software hybrid execution; external services may provide inputs; and executor replacement does not change Position meaning.

This remains true after the registry grows from five to six Positions: the split creates **two accountability/authority contexts**, not an extra mandatory employee.

**Result:** PASS.

## 10. Iteration 9 — end-to-end completeness before Owner review

**Criticism:** after aggressive minimality, the model could leave a function ownerless, preserve a hidden universal coordinator or become too rigid for future scale.

**Initial reconciliation:** the five-Position draft covered all eight functions and recorded major handoffs/split triggers. It therefore reached PASS-for-Owner-review at 9/10.

**Important limitation discovered by Owner review:** coverage completeness did not prove that every bundle was the correct durable authority boundary. In particular, Finance and Security/Assurance were covered but insufficiently separated.

**Result:** PASS for completeness, but not final after Owner correction.

## 11. Iteration 10 — Owner correction: separate Finance from Security/Risk/Continuity

**Owner criticism:** Finance and Security are better represented as **two authority/accountability boundaries**, rather than one `Company Operations & Assurance` Position.

**Cross-review of the correction:** the change is materially justified for four reasons:

1. **different controlled objects:** finance controls cash, commitments, economics and obligations; security/continuity controls access, data, risk, critical dependencies and safe operation;
2. **different evidence and escalation:** a finance exception and a security/data/continuity exception require different inputs, expertise and future delegation limits;
3. **independence and challenge:** security/risk may need to constrain commercial, engineering or financial action independently; combining it with finance makes future assurance separation harder;
4. **Position ≠ headcount:** separate Positions do not require separate people now. AC-205 may assign the same Principal to both while preserving separate capacities, evidence and authority.

**Secondary design question:** where should `F-07 — Organizational State / Evidence / Improvement` move after the bundle is removed?

**Reconciliation:** `F-07` moves to `POS-001 — Company Executive`, because current organizational-state synchronization, decision routing, roadmap/evidence reconstruction and governed improvement are part of Company operating integration. They are not naturally a Security/Risk responsibility, and present evidence does not justify a separate Governance/Knowledge/PMO Position.

**Revised six-Position coverage:**

- `F-01` + `F-07` → `POS-001 — Company Executive`;
- `F-02` + `F-03` → `POS-002 — Commercial & Customer Lead`;
- `F-04` → `POS-003 — Portfolio & Product Lead`;
- `F-05` → `POS-004 — Engineering & Release Lead`;
- `F-06` → `POS-005 — Finance & Obligation Control Lead`;
- `F-08` → `POS-006 — Security, Risk & Continuity Lead`.

Both new control Positions retain only `AM-0`/`AM-1`/`AM-2` initial ceilings. Material financial decisions remain excluded by `ROD-02`/`ROD-03`/applicable `ROD-06`; material security/data/risk/sovereignty decisions remain excluded by `ROD-06`/`ROD-07`/`ROD-08`/applicable `ROD-09`.

The revised proposal explicitly states that the same Principal may initially occupy both Positions, but executor consolidation cannot merge the two authority contexts.

**Result:** PASS. The Owner correction improves durable accountability without creating fake headcount.

## 12. Final acceptance test

| Test | Result |
|---|---|
| Positions derived from real AC-201 functions/workload/control needs | PASS |
| one-function-one-Position rule rejected | PASS |
| all eight AC-201 functions have primary Position accountability | PASS |
| six Positions are justified after Owner control-boundary correction | PASS |
| Owner is not modeled as a Position | PASS |
| participant/general meeting and General Director competence remain separate | PASS |
| Company Executive title creates no legal/corporate authority | PASS |
| Commercial + Customer bundle remains justified by current context continuity | PASS |
| Portfolio/Product remains separated from Engineering | PASS |
| Finance/Obligation Control is separate from Security/Risk/Continuity | PASS |
| F-07 Organizational State/Evidence is coherently placed with Company Executive | PASS |
| Finance does not duplicate statutory accounting/banking truth | PASS |
| Security/Risk Position cannot approve its own material exceptions | PASS |
| same Principal may hold Finance + Security without merging Position authority | PASS |
| no fake CFO/CISO/PMO headcount created | PASS |
| AC-202 `ROD-*` remains hard negative boundary | PASS |
| AC-203 `AM-*` semantics preserved | PASS |
| initial modes limited to `AM-0`/`AM-1`/`AM-2` | PASS |
| `AM-3`/`AM-4` not fabricated without downstream evidence | PASS |
| no named human/AI/software Principal assigned | PASS |
| Position count not treated as employee/agent count | PASS |
| product implementation remains product-repository canonical | PASS |
| customer authority/data rights remain customer-scoped | PASS |
| legal/accounting/banking authority not internalized | PASS |
| Arvectum OS governance remains separate | PASS |
| no Product Contract/capability lifecycle effect created | PASS |
| split/merge/retirement triggers explicit | PASS |
| AC-205 handoff preserves separate Position capacities | PASS |
| flagship transferability remains method-level, not a fixed customer org chart | PASS |

## 13. Maximum-iteration boundary

The authorized cross-review budget is now fully used: **10 of maximum 10 iterations**.

The remaining questions are explicitly downstream or empirical:

- which Principal(s) currently hold the six Position Assignments;
- whether one human temporarily carries several Positions;
- which work is executed by AI/software/hybrid Assignments;
- Assignment-specific narrowing of authority;
- concrete data/tool/credential access;
- workflow-specific `AM-4` eligibility;
- tested continuity/replacement behavior;
- whether observed workload later justifies further Position splits/merges;
- actual escalation and conflict frequency.

These belong to AC-205–AC-207 and operating evidence. They must not be fabricated inside AC-204.

Because the maximum review count has been reached, any **new material redesign** beyond the reviewed proposal would require a new explicit review cycle/version rather than an eleventh iteration silently exceeding the Owner's limit.

## 14. Final conclusion

`PASS — material consensus reached at 10 of maximum 10 iterations after the Owner's Finance/Security boundary correction.`

AC-204 `Proposed 0.9.1`, blob `9804a57a6cee027712e0c95bbf95bd428f848410`, is ready for explicit Owner approval.

Approval is required because the registry creates material Company accountability structure under AC-202 `ROD-05`.

After approval, the unchanged substance may be published as the binding Initial Position Registry, registered canonically, AC-204 may close as `Complete / PASS`, and the roadmap may advance to:

`AC-205 — Initial Assignments and executor classification`.
