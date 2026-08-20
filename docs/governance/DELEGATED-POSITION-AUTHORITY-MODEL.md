# AC-203 — Delegated Position Authority, Approval and Escalation Model

Status: `Proposed`
Version: `0.9.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-203 — Delegated Position authority, approval and escalation model`
Review: `docs/reviews/AC-203-DELEGATED-POSITION-AUTHORITY-CROSS-REVIEW.md`
Depends on: Company Constitution `1.0.0`; AC-002 Company↔OS authority boundary; AC-201 function model; AC-202 Approved `1.0.0`
Approval required: explicit Owner approval before this model becomes binding Company governance

## 1. Purpose

AC-203 defines the **Company-wide semantic model for delegated Position authority** before AC-204 creates concrete Positions and before AC-205 assigns humans, AI or software to them.

The purpose is to make the following distinction operational:

```text
what a function is responsible for
≠ what a Position may decide
≠ what requires approval
≠ what may execute automatically
≠ what must escalate to Owner
≠ who/what is currently assigned to execute the Position
```

AC-203 must reduce unnecessary Owner involvement without converting job titles, AI capability, technical access, credentials or workflow participation into authority.

It does not create any concrete Position, Assignment, access grant, budget, legal power, bank authority, customer authority, Product Contract or Arvectum OS lifecycle change.

## 2. Governing boundary

Authority under this model is subordinate to:

1. applicable law and valid legal/corporate authority;
2. the acting charter and valid corporate decisions;
3. the Ratified Company Constitution;
4. Approved AC-202 Reserved Owner Decisions;
5. other approved Company governance and explicit Owner decisions;
6. product-specific canonical authority within product scope;
7. customer authority and rights within customer scope;
8. applicable Arvectum OS contracts/governance where Company relies on OS.

A Company delegation can authorize only what the delegating authority itself is entitled to delegate.

Technical authorization, possession of credentials, repository admin rights, system roles or physical access never enlarge Organizational Authority.

## 3. Position-first authority rule

Delegation should attach to a **Position authority envelope**, not to a named executor by default.

The intended sequence is:

```text
Function responsibility
→ Position
→ approved Position authority envelope
→ Assignment of Principal
→ runtime/tool/data access constrained by that envelope
→ governed execution / evidence
```

A replacement Principal or Runtime does not automatically alter the Position authority envelope.

An Assignment MAY narrow Position authority for a particular Principal. It MUST NOT broaden Position authority without a separately approved delegation change.

## 4. Authority modes

AC-203 defines five modes that later Position definitions may combine by decision/action class.

### `AM-0 — Prepare / Recommend`

The Position may gather evidence, analyze, draft, classify, compare options and make recommendations.

`AM-0` creates no decision authority and no external commitment.

### `AM-1 — Execute Pre-Decided Work`

The Position may perform actions whose relevant decision has already been made by competent authority or whose deterministic operating rule is already approved.

Examples may include publication mechanics, routine QA, approved release steps, evidence synchronization or execution of an already approved bounded obligation.

The executor MUST NOT reinterpret the approved scope into a broader commitment.

### `AM-2 — Bounded Decision`

The Position may make a decision inside an explicitly approved envelope when all required inputs, limits and conditions are satisfied.

Examples may later include routine qualification, priority selection inside an approved queue, issue classification, ordinary tool choice, bounded spend or ordinary customer handling.

A material exception or unclear limit escalates.

### `AM-3 — Delegated Approval`

The Position may approve a consequential action inside an explicit delegated approval class.

`AM-3` requires stronger evidence than ordinary execution and MUST define approver eligibility, scope, limits, excluded decisions and attributable approval evidence.

A `ROD-*` final decision can never be admitted to `AM-3` without explicit amendment of AC-202.

### `AM-4 — Pre-Authorized Automatic Execution`

A class of action may execute automatically without a per-instance human approval only when competent authority has previously approved the class, limits, data boundary, evidence, failure behavior and rollback/compensation or reconciliation path.

`AM-4` is **not delegated discretionary authority to software or AI**. It is execution of a pre-authorized bounded rule.

Any condition outside the approved envelope MUST stop/fail closed or escalate.

## 5. Minimum delegation envelope

A material delegation is valid only when the applicable record identifies, directly or by governed reference:

1. `delegating_authority` — who/what valid authority grants the delegation;
2. `position_scope` — the Position or Position class receiving authority;
3. `authority_modes` — applicable `AM-0` through `AM-4` modes;
4. `decision_action_scope` — exact classes of decisions/actions permitted;
5. `business_object_scope` — products, customers, workstreams, assets or other subject boundaries where applicable;
6. `financial_budget_limits` — where money/exposure is relevant;
7. `external_commitment_limits` — what customer/supplier/public obligations may or may not be created;
8. `data_classification_scope` — what data categories/purposes may be handled;
9. `risk_consequence_limit` — maximum approved consequence/risk class;
10. `prerequisites` — required inputs, evidence, validations or prior approvals;
11. `approval_eligibility` — which Principal classes may perform an `AM-3` approval where required;
12. `excluded_decisions` — always including applicable `ROD-*` classes;
13. `effective_period` — effective date, expiry or review condition;
14. `escalation_path` — where cases go when bounds are exceeded or unclear;
15. `revocation_path` — how authority is withdrawn or narrowed;
16. `evidence_requirement` — what must be preserved to reconstruct a consequential decision/action;
17. `fallback_continuity_rule` — what happens if the Position/Principal/runtime is unavailable.

Not every low-risk delegation needs a heavyweight record, but the semantic boundary above must remain reconstructable proportionate to consequence.

## 6. Default deny and no ambient authority

Delegated authority is deny-by-default.

A Position may act only when the action is:

- explicitly inside its delegated decision/action class; and
- inside all applicable limits; and
- supported by required current evidence; and
- not excluded by AC-202, law, contract, customer authority, Product governance or Arvectum OS governance.

Authority MUST NOT be inferred from:

- Position title;
- prior similar decision;
- repository ownership;
- IAM/admin role;
- API permission;
- credential possession;
- Assignment existence;
- AI/model capability;
- workflow reachability;
- urgency;
- silence from Owner;
- historical habit.

## 7. Delegation limits without invented Company-wide numbers

Current evidence does not justify universal ruble, percentage, SLA, duration or data-volume thresholds.

AC-203 therefore defines **limit dimensions**, while concrete values belong to later Position/delegation records when evidence exists.

Limit dimensions include:

- single-action financial exposure;
- aggregate period budget/exposure;
- recurring-cost commitment;
- customer/supplier liability or support obligation;
- reversibility and recovery cost/time;
- customer/data classification and processing purpose;
- external disclosure scope;
- security privilege level;
- dependency/lock-in consequence;
- product/workstream scope;
- production/external-effect class;
- contractual deviation from approved standard terms;
- duration until mandatory review.

Where no reliable threshold exists, the default is not arbitrary delegation. The case remains residual Owner authority or escalates until evidence supports a bounded envelope.

## 8. Mandatory escalation triggers

A Position MUST stop/fail closed or escalate when any of the following applies:

1. the case enters `ROD-01` through `ROD-09`;
2. authority is absent, ambiguous, conflicting, expired or revoked;
3. any financial, commitment, data, risk, customer, product or time limit is exceeded;
4. material facts or evidence changed after a relevant approval;
5. required evidence is stale, missing, inconsistent or cannot be reconstructed;
6. a non-standard external term or liability falls outside the approved envelope;
7. customer rights, consent, purpose or authority are unclear;
8. a security/privacy/data/continuity gap requires material risk acceptance;
9. execution would create a new Company↔Product↔OS obligation outside approved contracts;
10. an irreversible or difficult-to-reverse consequence exceeds the approved class;
11. technical authorization exists but Organizational Authority is not established;
12. an external consequential action has uncertain outcome and retry may duplicate the effect;
13. emergency containment would need to turn into continued operation with an unresolved consequential gap.

Escalation is not failure of the Position. Correct escalation is part of the Position's accountable output.

## 9. Approval semantics

Preparation, recommendation, validation and execution are distinct from approval.

A delegated approval under `AM-3` must be:

- attributable to an eligible Principal acting for the Position;
- within an active delegation envelope;
- based on the required evidence and exact subject/scope;
- explicit enough to distinguish approve, reject, defer or approve-with-conditions;
- preserved proportionately when the action is consequential.

Silence, workflow completion, technical success, AI confidence or a favorable score are not approval.

## 10. Human, AI and software eligibility

Position authority and executor identity are separate.

### 10.1 Human Principal

A human assigned to a Position may exercise the Position's delegated authority only within the Assignment and authority envelope.

### 10.2 AI / software Principal

AI/software may perform `AM-0`, `AM-1`, `AM-2` or `AM-4` work when an approved workflow/delegation expressly admits that class and the required controls exist.

AI/software MUST NOT be treated as the **source** of authority.

For `AM-3 — Delegated Approval`, the delegation MUST explicitly define approver eligibility. By default, an AI/software Principal is not eligible to serve as the sole approver of a consequential action merely because it is assigned to the Position.

Where a consequential class is intended to run without per-instance human approval, the correct model is normally `AM-4 — Pre-Authorized Automatic Execution`, approved in advance by competent authority, rather than pretending that software independently “approved” the action.

Reserved Owner Decisions always remain outside AI/software final decision authority.

## 11. Assignment and technical-access relationship

Later AC-205/AC-206 work must follow:

```text
Position authority envelope
∩ Assignment scope
∩ technical authorization/access
∩ current workflow/data/risk conditions
= maximum executable action
```

The effective action scope is the **intersection**, never the union.

If technical access is broader than organizational authority, organizational authority still limits action.

If organizational authority is broader than technical access, the action cannot execute until legitimate access exists.

## 12. Parent/child work and no authority inheritance by implication

A child task, subprocess, AI agent, delegated worker or tool call does not automatically inherit all authority of the initiating Position.

Sub-work must receive only the minimum authority/access necessary for its declared action.

A Position MUST NOT bypass its own approval/escalation boundary by spawning another executor or service with broader technical permissions.

## 13. Emergency, containment and continuity

AC-202 permits later pre-authorization of bounded reversible containment.

AC-203 therefore allows an authority envelope to include immediate containment actions such as revocation, isolation, safe shutdown, evidence preservation, approved degraded mode or tested restoration where the action is protective and within an approved incident rule.

Containment authority does not include material risk acceptance.

Resumption with an unresolved material gap, acceptance of new liability or broadening of risk appetite remains escalated to the applicable `ROD-*` authority.

## 14. Revocation, expiry and stale authority

Delegation must be revocable.

A delegation should have a review/expiry trigger where consequence, organizational change or uncertainty makes indefinite authority inappropriate.

Authority is no longer usable when:

- the delegation is revoked or expired;
- the Position is retired or materially redefined;
- the relevant business/data/product scope no longer matches;
- a higher-authority rule changes incompatibly;
- a material incident or evidence invalidates the basis on which delegation was approved.

Historical decisions/actions remain attributable even after current authority is revoked.

## 15. Company / Product / OS / customer boundary

### Company

Company governance owns the meaning and approval of Company Position authority.

### Product

A Company Position may have product-facing responsibilities, but Product implementation/domain authority remains governed by the product repository. Company delegation cannot silently modify product canonical truth.

### Arvectum OS

Arvectum OS may represent/enforce a Company delegation under admitted platform contracts. OS technical roles or authorization do not create the Company delegation.

The current OS Decision Authority Policy is still Proposed `0.2.1` and is not adopted as Company authority by AC-203.

### Customer

A Company delegation cannot create authority to make customer-reserved decisions, waive customer rights or broaden customer data use. Customer-side authority must be independently established.

## 16. Handoff to AC-204

AC-204 may create concrete Positions only after using AC-201 responsibility domains and this authority model together.

Each proposed Position should identify:

- durable accountable outcomes;
- functions/responsibilities carried;
- applicable authority modes;
- intended delegated decision/action classes;
- explicit `ROD-*` exclusions;
- escalation path;
- whether later Assignments may be human, AI, software or hybrid;
- evidence that the Position is justified by workload, control need or economic value.

AC-204 MUST NOT mechanically create one Position per AC-201 function.

## 17. Prospective evidence

Later real operation should measure:

- Owner escalations caused by genuinely reserved decisions vs missing delegation;
- unnecessary escalations that should become delegated cases;
- decisions/actions that exceeded authority or should have escalated;
- approval latency and evidence quality;
- frequency of stale/ambiguous authority;
- delegated decisions reversed because limits were poorly designed;
- automatic actions stopped by fail-closed rules;
- executor replacements that preserved Position authority semantics;
- cases where technical access and Organizational Authority diverged.

The target is not maximum delegation. The target is **minimum sufficient Owner involvement with explicit accountable authority**.

## 18. Completion / approval boundary

AC-203 is substantively complete when the Company has a reusable delegation model that:

- keeps `ROD-*` final decisions outside delegated Position authority;
- supports routine delegated decisions and bounded automatic execution;
- separates Position authority from Principal/Assignment/runtime/access;
- defines explicit delegation fields and limit dimensions;
- fails closed/escalates on ambiguity or exceeded bounds;
- separates approval from preparation/execution;
- permits safe emergency containment without delegating material risk acceptance;
- preserves Company/Product/OS/customer boundaries;
- gives AC-204 a sufficient basis for concrete Position design without creating Positions prematurely.

Because AC-203 defines how material Company authority may be delegated, this `0.9.0` proposal MUST NOT become binding solely because AI drafted it or cross-review passes.

Required governance gate after review:

> explicit Owner approval of the exact reviewed `Proposed 0.9.0` content.
