# AC-002 — Company ↔ Arvectum OS Authority and Responsibility Boundary Cross-Review

Status: `Complete`
Review date: `2026-08-20`
Iterations completed: `7 of maximum 10`
Result: `PASS — material consensus reached; Owner approval subsequently recorded`
Reviewed artifact: `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md` — Proposed `0.9.0`, approved for publication as `1.0.0`
Repository branch: `ac-002-company-os-boundary`
Owner decision: `docs/governance/decisions/DECISION-2026-08-20-AC-002-APPROVAL.md`

## 1. Review purpose

This review tests AC-002 from the perspective of the Owner and the full set of executive-management functions required to challenge a Company ↔ Arvectum OS boundary before it becomes binding Company governance.

As in AC-001, most executive labels below are **functional review lenses only**. They do not create Positions, appointments, employment relationships, delegations, committees or Organizational Authority before the Company operating model is established under later roadmap items.

The legally existing General Director capacity is distinct from simulated executive lenses. The simulated `Owner` lens is also not actual Owner approval. Final approval remains a separate explicit act by the real Owner/competent Principal against the exact final proposal.

## 2. Canonical and authority baseline checked before review

### Arvectum Company

- canonical repository: `arvectum/arvectum-company`;
- `main` checked before drafting at `9b4651755c88eec1f462749b84261874c56b4d68`;
- `docs/constitution/COMPANY-CONSTITUTION.md` — Ratified `1.0.0`;
- `docs/roadmap/ROADMAP.md` — AC-002 is Current;
- `docs/CANONICAL-SOURCES.md` — Company/OS/legal authority source registry.

The Ratified Constitution already establishes the high-level boundary: Company owns concrete organizational semantics; OS owns domain-neutral platform contracts; OS is not the source of corporate authority; Company reliance uses the required Product Contract/contract boundary and Governed Execution path.

### Arvectum OS

Current canonical repository state was re-checked before review:

- canonical repository: `arvectum/arvectum-os`;
- observed `main` HEAD: `a5e6c15f735b85e952f646c885a3e5f019594276`;
- Constitution: Ratified `1.2.0`;
- RFC-0001 through RFC-0008: Accepted `1.0.0` within their declared scopes;
- RFC Index confirms those statuses;
- RFC-0001 canonical blob remains `1a8379e6626f2d8d5cc5517ad4f00ad32014ee73`;
- RFC-0003 canonical blob remains `27f75c3ab3d8ba673207bc83d43da86aea303355`;
- `docs/governance/DECISION-AUTHORITY-POLICY.md` remains `Proposed 0.2.1`, therefore non-binding.

Recent OS Phase 7 / recovery-portability commits do not amend the Constitution/RFC boundary used by AC-002 and do not become Company commitments merely because they exist.

### Legal/corporate source baseline

The private owner-managed source set recorded by the Company source registry was checked at the level needed for this internal boundary:

- ООО «Арвектум» operates under Типовой устав №23;
- the verified baseline has one participant;
- current corporate governance includes the General Director / sole executive body;
- internal governance cannot create external legal authority merely by technical representation.

No personal identifiers, signatures, addresses, tax identifiers or banking data are copied into the public review.

## 3. Review lenses

The cross-review used the following management perspectives:

1. Owner / Founder / residual authority and capital;
2. General Director / current executive management and external representation;
3. Finance / capital, budgets and commitments;
4. Operations / workflow execution, continuity and failure handling;
5. Product & Portfolio / product ownership and investment boundary;
6. Technology & Architecture / Company↔OS contract and responsibility boundary;
7. Commercial / customer claims and platform-dependent commitments;
8. Legal & Compliance / legal/corporate authority separation;
9. Security & Data / access, isolation, rights, secrets and sovereignty;
10. People & Organization / Position, Principal, Assignment and accountability;
11. Risk & Continuity / downside, exceptions, rollback and de-platformization.

## 4. Iterative review record

### Iteration 1 — Legal/corporate authority vs internal and technical authority

**Primary lenses:** Owner, General Director, Legal & Compliance.

**Material criticism:**

- the boundary could fail if `Owner`, General Director, Company Organizational Authority, OS governance authority and technical permission are flattened into one chain;
- an internal Owner decision must not be described as automatically satisfying a legally required participant decision, General Director act, signature or power of attorney;
- OS governance can decide platform behavior but must not be framed as corporate governance over ООО «Арвектум».

**Reconciliation incorporated:**

- AC-002 separates legal/corporate authority, Company Organizational Authority, OS governance authority, product governance and technical authorization;
- explicit non-substitution rules were added;
- the final proposal states that an internal Owner decision does not replace the legally required capacity/form of action;
- OS governance is authoritative only for OS architecture/contracts/lifecycle within OS scope.

**Result:** material legal/authority objection resolved; continue.

### Iteration 2 — Canonical authority mode vs Organizational Authority

**Primary lenses:** Technology & Architecture, Legal & Compliance, Owner, People & Organization.

**Material criticism:**

- RFC-0001/RFC-0002 terms `Native`, `External Reference` and `Governed Replica` could be misread as saying that OS becomes the organizational sovereign when it stores a Company policy/delegation as `Native`;
- the opposite overcorrection — forbidding `Native` for all Company governance objects — would incorrectly constrain legitimate future OS canonical-state use;
- a platform must be able to reject non-conforming writes without gaining power to rewrite the Company decision itself.

**Reconciliation incorporated:**

- the final proposal explicitly separates system-of-record/canonical responsibility from Organizational Authority;
- a Company governance object may be `Native` only after explicit Company designation **and** under an applicable OS contract;
- the Company remains the source of the organizational meaning/authority represented by the record;
- OS may reject a non-conforming mutation but must not silently reinterpret or rewrite Company policy/delegation semantics to force conformance;
- external legal/system facts retain their external authority through `External Reference` / `Governed Replica` as applicable.

**Result:** core architecture/authority ambiguity resolved; continue.

### Iteration 3 — Product Contract applicability and direct Company use

**Primary lenses:** Technology & Architecture, Product & Portfolio, Operations.

**Material criticism:**

- saying “Company uses OS directly” too broadly could invent a bypass around RFC-0004 Product Contract requirements;
- forcing every platform-native administrative operation through a fictional “Company Product Contract” would also invent a new contract type not established by OS governance;
- AC-002 must not decide a client pattern that OS has not canonically admitted.

**Reconciliation incorporated:**

- product/extension/client reliance continues to use the Product Contract boundary when RFC-0004 triggers it;
- direct Company use is allowed only for current canonical OS operations explicitly admitted for an Organization/platform operator without a Product Contract;
- AC-002 creates no generic Company Product Contract and no Product Contract-equivalent type;
- if the first real Company workflow cannot fit an existing admitted boundary, consequential reliance stops until the minimum OS governance/contract path is completed;
- the unresolved Company-native client pattern is explicitly deferred instead of guessed.

**Result:** hidden contract-bypass risk resolved; continue.

### Iteration 4 — Cross-repository commitments and change ownership

**Primary lenses:** Product & Portfolio, Technology & Architecture, Owner, Operations.

**Material criticism:**

- a Company roadmap or Owner priority could otherwise be mistaken for an OS implementation commitment;
- an OS change could silently break Company operating assumptions even though OS does not own Company authority;
- product implementation and Company portfolio authority require separate canonical homes;
- some real changes will need decisions in two repositories, not a single universal approval.

**Reconciliation incorporated:**

- separate paths now exist for Company-only change, Company need requiring OS change, OS change affecting Company reliance and product change affecting the portfolio;
- cross-repository changes may require paired decisions, each in its own authority scope;
- a Company artifact cannot silently amend OS and an OS commit cannot silently change Company policy;
- fallback, version pinning, migration, suspension and de-platformization are explicit reactions to incompatible OS change.

**Result:** material repository-boundary objection resolved; continue.

### Iteration 5 — Commercial, finance and lifecycle integrity

**Primary lenses:** Commercial, Finance, Product & Portfolio, Owner.

**Material criticism:**

- the Company could create unsupported platform obligations by promising customers compatibility, support, portability or readiness beyond the actual OS lifecycle state;
- Company willingness to accept business risk must not be confused with authority to represent an Incubating OS capability as Active;
- customer contracts cannot be used to force an undeclared OS commitment after the fact.

**Reconciliation incorporated:**

- a dedicated commercial/lifecycle boundary was added;
- Company commitments must truthfully reflect current OS lifecycle, conformance and readiness state;
- Company risk acceptance does not create a new OS obligation without separate OS authority;
- Company contracts/sales promises cannot bypass Product Contract or lifecycle boundaries.

**Result:** commercial/financial overcommitment risk resolved; continue.

### Iteration 6 — Security, sovereignty, continuity and business practicality

**Primary lenses:** Security & Data, Risk & Continuity, Operations, Finance, Owner.

**Material criticism:**

- the boundary must preserve deny-by-default, least privilege, Organization isolation, data-rights constraints and secret handling without duplicating all of RFC-0003;
- break-glass technical access must not accidentally become permanent Company delegation;
- an OS dependency must remain recoverable/de-platformizable;
- governance must not make every read or transient calculation expensive;
- adoption must be justified by Company value rather than by the fact that OS can model something.

**Reconciliation incorporated:**

- AC-002 references inherited OS security/privacy/sovereignty invariants and only adds Company-specific boundary consequences;
- break-glass behavior is explicitly attributable, time-bounded, reviewable and non-authority-creating;
- continuity/export/fallback/de-platformization expectations are explicit;
- proportionality excludes heavy canonical treatment for every low-risk read or transient computation;
- a business-first adoption test and minimal pre-reliance checklist were added.

**Result:** material control-vs-practicality objection resolved; full-panel convergence required.

### Iteration 7 — Full-management convergence and contradiction check

**Primary lenses:** all 11 review lenses.

**Checks performed:**

- Owner authority vs General Director/legal corporate capacity;
- Company authority vs OS governance authority;
- Organizational Authority vs technical authorization;
- `Native` canonical state vs organizational sovereignty;
- Company organizational semantics vs OS domain-neutral contracts;
- portfolio authority vs product implementation authority;
- Product Contract requirements vs direct Company use;
- OS contract enforcement vs Company policy ownership;
- Company business risk acceptance vs OS lifecycle/support obligations;
- Governed Execution vs owner-bottleneck/over-governance risk;
- security/isolation vs operational usability;
- continuity/portability vs rewriting historical evidence;
- AI/software execution vs authority creation;
- cross-repository coordination vs hidden commitments.

**Result:** no remaining material contradiction was identified.

Remaining future questions are intentionally deferred to AC-003, AC-202/203, AC-206/207 and the first real Company OS-reliance workflow. Resolving them now would create speculative implementation or authority commitments without evidence.

**Stop:** iteration `7/10` because additional changes would be terminology/style-level or belong to later roadmap items.

## 5. Final perspective matrix

| Review lens | Final result | Main condition preserved |
|---|---|---|
| Owner | PASS | Company residual/strategic authority is not transferred to OS; actual Owner approval recorded separately after review |
| General Director | PASS | internal/OS governance does not replace legally required executive capacity or form |
| Finance | PASS | Company commitments cannot create unsupported OS obligations; adoption must justify cost/value |
| Operations | PASS | contract boundary, failure, fallback and proportional execution rules are usable |
| Product & Portfolio | PASS | Company controls investment/accountability; product implementation stays product-owned |
| Technology & Architecture | PASS | Company/OS responsibility is explicit; `Native` semantics and Product Contract rules are reconciled |
| Commercial | PASS | customer claims remain within real OS lifecycle/conformance/support state |
| Legal & Compliance | PASS with supremacy condition | legal/corporate authority remains controlling within its scope |
| Security & Data | PASS | deny-by-default, isolation, rights, secrets and break-glass boundaries are preserved |
| People & Organization | PASS | OS represents/enforces but does not create Position/Assignment/delegation authority |
| Risk & Continuity | PASS | uncertainty fails closed; migration/de-platformization and fallback remain available |

## 6. Deferred work is deliberate, not a review failure

The following remain later work:

- canonical repository/artifact map — `AC-003`;
- portfolio map — `AC-004`;
- Reserved Owner Decisions — `AC-202`;
- delegated Position authority/approval/escalation matrix — `AC-203`;
- Position Registry / Assignments — `AC-204` / `AC-205`;
- data/tool/credential access baseline — `AC-206`;
- continuity/fallback baseline — `AC-207`;
- first real Company OS admission/reliance mapping — `AC-503`;
- any OS change required by real Company use — through the applicable Arvectum OS RFC/ADR/capability/Product Contract path.

This keeps AC-002 a boundary contract rather than turning it into premature implementation design.

## 7. Cross-review conclusion

AC-002 reached material management consensus at the **proposal** level after seven iterations.

The proposal was suitable for Owner decision because it:

- distinguishes legal/corporate authority, Company Organizational Authority, OS governance, product governance and technical authorization;
- establishes that canonical record authority mode is not organizational sovereignty;
- preserves Company-specific meaning in Company scope and domain-neutral platform contracts in OS scope;
- respects RFC-0004 Product Contract boundaries without inventing a Company-specific bypass or new contract type;
- requires Governed Execution and fail-closed behavior for consequential reliance;
- prevents hidden cross-repository and unsupported customer commitments;
- preserves security, data rights, isolation, portability and technology sovereignty;
- keeps OS adoption reversible and economically justified;
- leaves unresolved implementation/authority details to the roadmap items that have the evidence to decide them.

The cross-review itself did **not** constitute Owner approval. Subsequent explicit Owner approval of the exact `Proposed 0.9.0` artifact is recorded in `docs/governance/decisions/DECISION-2026-08-20-AC-002-APPROVAL.md`, authorizing publication as `Approved 1.0.0` without changing the approved normative substance.
