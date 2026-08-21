# AC-208 — Reference-Model Transferability and M2 Closure Cross-Review

Status: `Complete / PASS for Owner approval`
Review date: `2026-08-21`
Iterations completed: `10 of maximum 10`
Result: `PASS — AC-201 through AC-207 form a coherent business-first reference operating model; the proposal cleanly separates reusable derivation/control patterns from the Arvectum-specific organization instance, preserves Company/Product/Arvectum OS/customer authority boundaries, does not turn AI/access/continuity into authority, does not overclaim market or operational readiness, and supports M2 closure with AC-301 as the next roadmap action`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-208 — Reference-model transferability boundary and operating-model cross-review`
Reviewed artifact: `docs/organization/REFERENCE-MODEL-TRANSFERABILITY-AND-M2-CLOSURE.md`
Reviewed publication: `Proposed 0.9.0`
Reviewed blob SHA: `78b9c3333a23b196f34338c9fec9e9dd2f802d22`
Maximum review iterations: `10`
Approval status: `Pending explicit Owner approval of the exact reviewed proposal`
Arvectum OS main re-checked during proposal drafting: `2c0cc461504bab489cd5d4fe89456e634ef81e59`

## 1. Review purpose

This is the Phase 2 closure review. It tests the combined operating-model chain rather than reviewing AC-208 as an isolated document:

```text
M1 business evidence
→ functions
→ reserved decisions
→ delegated authority
→ Positions
→ Assignments/executors
→ access
→ continuity/replacement
→ transferability boundary
```

The review must reject M2 closure if the combined model contains a material contradiction, fake delegation/headcount, ambient AI authority, access-as-authority shortcut, Company↔OS boundary leak, unsupported transferability claim, or readiness claim not backed by evidence.

## 2. Iteration 1 — end-to-end derivation must remain traceable to business evidence

**Criticism:** Phase 2 could have drifted from the M1 business/economic/Owner-workload evidence into an internally elegant governance model that no longer serves real Company work.

**Reconciliation:** AC-208 traces each layer back to the preceding evidence boundary. AC-201 admits functions from real value, obligation, workload, control and continuity needs; AC-202 reserves consequential decision gates; AC-203 defines delegation; AC-204 creates only the Positions justified by those functions; AC-205 maps current executors; AC-206 derives access; AC-207 derives continuity.

The proposal explicitly treats the exact eight-function result as Arvectum-specific and carries forward M1 empirical gaps rather than “solving” them by design.

**Result:** PASS.

## 3. Iteration 2 — business-first discipline and Owner bottleneck honesty

**Criticism:** M2 could be declared successful merely because governance artifacts exist, while the actual Owner bottleneck remains essentially unchanged.

**Reconciliation:** AC-208 explicitly states that current Owner concentration remains real: the Owner human Principal still holds POS-001, POS-002, POS-003, POS-005 and POS-006; extended Owner/legal continuity is unresolved; access and continuity controls are not fully implemented/tested.

M2 is therefore framed correctly as **reference operating model and authority established**, not as proof that Owner workload has already fallen. Later operating evidence must measure whether delegation/automation creates real value.

**Result:** PASS.

## 4. Iteration 3 — authority domains must not collapse during synthesis

**Criticism:** Combining AC-202 through AC-207 could accidentally turn one of legal capacity, Owner authority, Position authority, technical access or workflow capability into a substitute for another.

**Reconciliation:** the proposal preserves the full non-substitution chain:

- exact `ROD-*` final decisions remain Owner-reserved unless explicitly amended;
- AC-203 delegation is Position-scoped and deny-by-default;
- Assignment cannot broaden Position authority;
- AC-206 access cannot create authority;
- AC-207 replacement/urgency cannot transfer authority;
- legal/corporate and customer authority remain distinct gates.

The effective-execution intersection remains coherent across the complete model.

**Result:** PASS.

## 5. Iteration 4 — no fake headcount and no universal six-Position org chart

**Criticism:** Once six Positions are approved and named, they can easily become a de facto “Arvectum method” sold as a standard org chart to customers.

**Reconciliation:** AC-208 classifies the exact F-01…F-08 model, POS-001…POS-006 registry, F-07/POS-001 bundling and Finance/Security split as `TR-3 — Arvectum Company organization instance; do not copy by default`.

The reusable rule is the **derivation method**: start from the customer's business/obligations/control needs and derive the smallest accountable Position set. Similarity to Arvectum's result is not evidence of applicability.

**Result:** PASS.

## 6. Iteration 5 — AI-led POS-004 must not become fake proof of an autonomous AI Position

**Criticism:** AC-205 already calls POS-004 AI-led. Closing M2 could be misread as proof that an economically and operationally validated AI-held Position exists, prematurely satisfying M6.

**Reconciliation:** AC-208 explicitly rejects that inference. POS-004 AI-led is a current **Assignment/executor baseline** with bounded AM-0/1/2 work and access/continuity semantics. M6 still requires real supervised operating evidence for value, quality, cost, risk and executor replacement/fallback.

AI remains an execution means, not the source of Position authority. No AM-3 or AM-4 is activated by M2 closure.

**Result:** PASS.

## 7. Iteration 6 — access and continuity controls must enable execution without creating ambient machine authority

**Criticism:** Strong least-privilege/fail-closed controls can make the organization non-operational; weak controls can turn an AI or credential into a de facto authority source.

**Reconciliation:** AC-208 correctly treats AC-206/207 as a pair:

- AI-led Engineering retains meaningful bounded write/build/test access;
- commercial AI can later operate inside a scoped sender/campaign boundary;
- bank/signing/Owner-wide admin/raw secrets remain excluded from ambient AI reach;
- replacement runtimes can preserve work without inheriting wider authority;
- legitimate legal/customer/security/payment gates may still stop consequential work.

This preserves the intended AI-native operating model without changing the authority source.

**Result:** PASS.

## 8. Iteration 7 — reusable method, governance pattern and implementation/module must remain distinct

**Criticism:** “Reusable” can hide several materially different claims: a useful diagnostic question, a governance pattern, a software module and a domain-neutral platform contract are not the same thing.

**Reconciliation:** AC-208 introduces five explicit dispositions:

- `TR-1` reusable derivation method;
- `TR-2` reusable governance/control pattern requiring customer-specific parameters;
- `TR-3` Arvectum-specific organization instance;
- `TR-4` product/module candidate requiring Phase 3/5 evidence;
- `TR-5` Arvectum OS domain-neutral semantics under OS governance.

The categories block the common shortcut `internal practice → reusable module → OS capability` and provide a ten-question admission test before customer reuse.

**Result:** PASS.

## 9. Iteration 8 — Company/Product/Arvectum OS/Customer ownership boundaries

**Criticism:** The flagship `«ИИ-компания под ключ»` creates pressure to treat Company experience as customer authority or to move reusable Company semantics directly into Arvectum OS.

**Reconciliation:** AC-208 requires customer-specific re-derivation beginning with the customer's own legal/corporate authority, contracts, business model, obligations, economics and risks. Customer Organizational Authority remains with customer-authorized Principals.

Product implementation remains product-owned. Domain-neutral platform semantics remain OS-owned and require the applicable RFC/ADR/capability/Product Contract path. Company conclusions create no OS lifecycle or contract effect.

The OS Decision Authority Policy remains Proposed and is not used as binding Company authority.

**Result:** PASS.

## 10. Iteration 9 — market/economic/readiness claims must remain evidence-bounded

**Criticism:** Closing a milestone titled “reference operating model established” could be interpreted externally as validated demand, a proven offer, customer readiness or production-grade continuity.

**Reconciliation:** AC-208 explicitly lists what M2 does **not** prove: demand, willingness to pay, price, ROI, repeatable acquisition/onboarding, implementation/support unit economics, profitability, measured Owner-time reduction, completed access implementation, production-grade DR, legal succession, reusable module readiness, proven AI Position economics or external deployment.

The AC-108 bounded discovery loop remains separate P1 market evidence. No pilot, SLA, price, privileged access or customer commitment follows from M2 closure.

**Result:** PASS.

## 11. Iteration 10 — M2 exit criteria and next-roadmap handoff

**Criticism:** A closure review must verify not only the model but also that the milestone's original exit criteria are met and that the next step follows the existing roadmap rather than being invented by AC-208.

**Reconciliation:** all original M2 exit criteria are explicitly tested in the proposal:

- Positions justified by real responsibility/control/economic need — PASS;
- authority/escalation explicit — PASS within design scope;
- humans/AI/software remain executors — PASS;
- sensitive access/fallback bounded — PASS as governance baseline with implementation gaps preserved;
- executor replacement preserves Position meaning — PASS as model;
- reusable vs non-reusable boundary explicit — PASS upon approval.

The incorporated full roadmap already defines Phase 3 / M3. Therefore the next action is not newly invented: `AC-301 — Portfolio product/node identity and ownership reconciliation` precedes accountable-Position mapping, investment criteria and module classification.

This is business-first because the current portfolio already contains seven mapped nodes with unresolved identity/ownership/overlap questions, while AC-208 correctly refuses to classify them as modules prematurely.

**Result:** PASS.

## 12. Acceptance test

| Test | Result |
|---|---|
| AC-201 through AC-207 form one traceable chain | PASS |
| Phase 2 remains grounded in M1 business evidence | PASS |
| no architecture/governance-completeness objective replaces business value | PASS |
| Owner/legal/Position/technical/customer authority remain distinct | PASS |
| ROD boundary preserved | PASS |
| delegation remains deny-by-default and executor-neutral | PASS |
| exact six Arvectum Positions are not made universal | PASS |
| exact eight functions and nine ROD classes are not made universal | PASS |
| no fake headcount or new department created | PASS |
| AI remains executor rather than authority source | PASS |
| POS-004 AI-led state does not prematurely satisfy M6 | PASS |
| no AM-3/AM-4 activation follows from M2 closure | PASS |
| AC-206 access design does not imply completed provisioning | PASS |
| AC-207 continuity design does not imply tested DR | PASS |
| access and continuity still permit meaningful bounded AI execution | PASS |
| TR-1 through TR-5 distinguish method/pattern/instance/module/OS semantics | PASS |
| customer organization must be re-derived from customer evidence | PASS |
| customer authority remains customer-owned | PASS |
| product implementation remains product-owned | PASS |
| OS domain-neutral semantics remain under OS governance | PASS |
| no hidden OS Product Contract/capability/lifecycle commitment created | PASS |
| market validation/pricing/ROI/profitability remain unproven | PASS |
| AC-108 stays a parallel bounded discovery loop | PASS |
| Owner bottleneck remains stated rather than falsely solved | PASS |
| all original M2 exit criteria tested | PASS |
| AC-301 is the existing canonical next Phase 3 action | PASS |
| no product is classified as a reusable module by AC-208 | PASS |
| M2 closure claim is limited to planning/governance scope | PASS |

## 13. Review-budget conclusion

This review uses all `10 of maximum 10` iterations because AC-208 is the aggregate Phase 2 closure point and materially joins business, authority, organization, executor, access, continuity, transferability and roadmap boundaries.

No material contradiction remains inside the declared Phase 2 design scope.

Remaining gaps require empirical operation, market evidence or concrete implementation/tests rather than further Phase 2 desk redesign. They therefore belong to AC-108 parallel discovery, Phase 3 portfolio governance, later management/operating implementation, M5/M6 proof work and eventual external deployment.

## 14. Final conclusion

`PASS — material consensus reached at 10 of maximum 10 iterations.`

AC-208 `Proposed 0.9.0`, exact reviewed blob `78b9c3333a23b196f34338c9fec9e9dd2f802d22`, is ready for explicit Owner approval.

If approved, AC-208 may be published as the binding transferability/M2 closure baseline; `M2 — Arvectum Company reference operating model and authority established` may close as `Complete / PASS`; and the canonical roadmap may advance to:

`AC-301 — Portfolio product/node identity and ownership reconciliation`.

The approval must not be interpreted as market validation, production/customer readiness, module admission, OS lifecycle promotion, budget approval, hiring, access provisioning or delegation beyond the already approved authority model.
