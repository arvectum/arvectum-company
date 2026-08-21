# AC-502 — First Governed Workflow: Position, Authority, Data and Evidence Contract

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-502 — Workflow, accountable Position, authority/data/evidence contract`
Milestone: `M5 — First real governed Company operating contour proven`
Selected workflow: `WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`
First application contour: `PORT-002 — Discount Parser`
Depends on: AC-501 `Approved 1.0.0`; AC-202…AC-207; AC-401…AC-407
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение и тип документа

AC-502 формализует выбранный AC-501 workflow как **Company workflow governance contract** до его bounded implementation и supervised real-operation proof.

Термин `contract` здесь означает внутренний Company operating contract: scope, accountable Positions, authority boundary, data boundary, evidence contract, state transitions, escalation/failure behavior и measurement inputs.

Этот документ **не является**:

- договором с заказчиком;
- SLA, гарантией, офертой или коммерческим обещанием;
- Product Contract Arvectum OS;
- product specification Discount Parser;
- новой Position/Assignment/access grant;
- production approval;
- автоматическим workflow-runtime implementation.

Главный инвариант:

```text
customer evidence
→ bounded Company classification
→ admitted technical work
→ technical evidence
→ bounded customer-facing handoff
→ customer validation/acceptance evidence

≠
AI output → automatic customer commitment/acceptance
```

## 2. Governing baseline и current evidence

AC-502 подчинён применимым legal/corporate sources, Ratified Company Constitution и Approved Company governance.

Ключевые controlling artifacts:

- AC-501 — selected workflow and first application contour;
- AC-202 — `ROD-01…ROD-09` hard negative boundary;
- AC-203 — `AM-0…AM-4`, deny-by-default authority semantics;
- AC-204 — Position accountability boundaries;
- AC-205 — current Assignments/executor realizations;
- AC-206 — `DC-0…DC-3`, `RA-*` and least-privilege access ceilings;
- AC-207 — `CM-0…CM-4`, continuity/replacement/fail-closed semantics;
- AC-401 — Company work/obligation control model;
- AC-402 — decision/approval/escalation separation;
- AC-403 — risk/exception/incident separation;
- AC-404…AC-407 — management control, reporting and Owner-attention baseline.

Product implementation truth remains in `arvectum/discount-parser`.

Current product state was re-checked at `main` commit:

`a8c1b29702a8ce40bd30b5d972ac2541367900e1`.

Relevant current evidence includes the merged customer-feedback correction sequence around DP-CUST-005…DP-CUST-012, including repeated runtime defects, installer/update problems, source-configuration UX changes and the later assisted confirm-only mapping flow. This demonstrates that the selected pattern is a real recurring operating contour rather than a theoretical workflow.

The product's `FINAL_ACCEPTANCE_CHECKLIST.md` separately states that full product production acceptance requires real target-machine checks; therefore a successful correction case under this workflow MUST NOT be inflated into a claim of full product production acceptance unless the applicable full acceptance evidence actually exists.

## 3. Workflow objective

`WF-M5-001` exists to convert real customer feedback into a controlled, reconstructable outcome while reducing unstructured Owner coordination and preventing technical work from silently creating customer/commercial authority.

The workflow must produce one of the following explicit outcomes:

1. confirmed in-scope correction delivered for customer validation and explicitly accepted/resolved;
2. rework required with preserved prior evidence;
3. customer/configuration/input issue handled without falsely labeling it a product defect;
4. clarification/evidence request because the case is not decision-ready;
5. change/new-scope/product decision routed outside the correction path;
6. material security/data/risk/incident case escalated into the proper control path;
7. blocked/stopped case with explicit reason and next safe control point.

The workflow is not optimized for maximum automated throughput. It is optimized for correct bounded execution, customer value, reduced reconstruction, evidence quality and safe escalation.

## 4. Entry and exit boundary

### 4.1 Entry trigger

A workflow instance starts when Company receives identifiable customer/user feedback about an active or previously delivered Discount Parser behavior and the feedback may require diagnosis, correction, clarification, re-delivery or an acceptance-state decision.

Minimum entry evidence:

- source/channel reference;
- attributable customer/workstream context sufficient to understand which delivered/product state is affected;
- feedback content or a protected reference to it;
- receipt time/date where available;
- affected version/build/environment if known;
- confidentiality/data classification assessment sufficient to choose the next handling path.

Missing version, screenshots, logs or reproduction details do not prevent intake; they may prevent later classification or technical admission.

### 4.2 Exit conditions

A workflow instance exits only when one of these conditions is evidenced:

- `Resolved / Customer accepted`;
- `Resolved / Customer confirmed no correction required`;
- `Reclassified — new scope/change/product decision` with a separate next control point;
- `Reclassified — customer input/configuration/environment` with bounded follow-up completed or queued;
- `Escalated — material risk/incident/authority boundary` into the applicable control path;
- `Blocked` with explicit blocking source, owner and next review trigger;
- `Stopped/Cancelled` by competent authority or because the underlying customer/workstream no longer requires continuation.

Internal tests, merged code or a generated installer alone do **not** satisfy customer acceptance.

Customer silence does **not** constitute acceptance unless an authoritative customer/legal source explicitly establishes such a rule for the case; AC-502 creates no such rule.

## 5. Internal workflow state model

The following states are workflow semantics, not a new universal Company register namespace.

| State | Meaning | Required gate to enter |
|---|---|---|
| `W0 — Feedback Received` | source feedback captured/referenceable | identifiable source evidence |
| `W1 — Intake Packet Ready` | minimum context normalized and data boundary assessed | source + product/workstream context |
| `W2 — Classification Ready` | sufficient business/technical evidence exists for routine classification | scope/evidence sufficient; unknowns explicit |
| `W3 — Classified` | case assigned an explicit classification | attributable POS-002 routine classification or proper escalation |
| `W4 — Technical Correction Admitted` | an in-scope technical correction may start | classification + bounded technical scope + no unresolved stop gate |
| `W5 — In Technical Execution` | POS-004 work is in progress | valid workstream/repo/access boundary |
| `W6 — Internal Verification` | candidate implementation exists and is being tested/reviewed | implementation evidence available |
| `W7 — Candidate Ready` | technical evidence supports a bounded candidate for customer validation | required tests/build/provenance evidence complete enough |
| `W8 — Customer Validation Pending` | candidate/instructions were validly handed to customer and explicit customer result is awaited | valid external-effect/customer-contact gate |
| `W9 — Rework Required` | customer/internal evidence disproves resolution | new evidence linked to prior candidate |
| `W10 — Resolved / Accepted` | applicable customer validation/acceptance evidence exists | explicit customer/authorized-source evidence |
| `W11 — Reclassified / Escalated / Blocked` | case leaves normal correction path | explicit reason + target control path/next trigger |

State transitions MUST remain reconstructable. Routine implementation substeps remain product-local and need not become Company workflow states.

## 6. Classification taxonomy

At `W3`, the case must be assigned one primary current classification. Classification may change when new evidence arrives; prior classification/history must remain reconstructable.

| Class | Meaning | Default path |
|---|---|---|
| `CL-1 — In-scope defect` | expected/committed current behavior is not met and correction stays inside accepted scope | admit bounded technical correction |
| `CL-2 — Customer/input/configuration/environment` | product may be functioning as designed but customer data/setup/environment is the blocker | bounded guidance/clarification; technical work only if separately justified |
| `CL-3 — Evidence insufficient / not reproduced` | current evidence cannot support a reliable defect/change conclusion | request evidence; remain fail-closed on commitment expansion |
| `CL-4 — Change / new scope` | requested outcome extends or changes accepted commitment | leave correction path; commercial/product decision required |
| `CL-5 — Product limitation / product-design question` | behavior reflects a product capability/design boundary rather than an ordinary defect | POS-003/product decision path before material build |
| `CL-6 — Security / data / material-risk / incident` | correction implicates material security, data rights, credentials, incident or risk exception | POS-006 + AC-403 path; P0 where consequence warrants |
| `CL-7 — Duplicate / already addressed / superseded` | same issue is already represented or current product state supersedes the report | link evidence; avoid duplicate technical work |

A classification is a Company operating judgment, not a legal admission of liability and not customer acceptance.

## 7. Accountability model

### 7.1 Primary end-to-end accountable Position

**`POS-002 — Commercial & Customer Lead`** is accountable for the end-to-end workflow outcome because AC-204 assigns it customer-context continuity, defect-vs-scope-vs-change classification, delivery/acceptance coordination and bounded support state.

Accountability includes ensuring that:

- customer meaning is not lost between feedback and engineering;
- classification is explicit;
- no new promise is created silently;
- the customer-facing validation state remains visible;
- a case does not close merely because engineering finished;
- material/ambiguous cases reach the correct authority instead of remaining in Owner memory.

Current AC-205 human Assignment for POS-002 remains the Owner Principal. AC-502 does not assign a new AI co-holder to POS-002.

### 7.2 Technical execution accountable Position

**`POS-004 — Engineering & Release Lead`** is accountable for the technical correction segment after `W4` admission and until bounded `W7 — Candidate Ready` evidence exists.

POS-004 owns:

- technical decomposition;
- product-code correction;
- routine reversible engineering choices;
- automated/manual verification;
- release/build candidate provenance;
- explicit known limitations;
- technical handback to POS-002.

It does not own customer scope, customer acceptance, commercial commitment or material risk acceptance.

### 7.3 Conditional supporting Positions

- `POS-003 — Portfolio & Product Lead`: when a case is `CL-4`/`CL-5`, raises reuse/productization/roadmap/portfolio meaning or risks turning customer correction into product investment;
- `POS-006 — Security, Risk & Continuity Lead`: for `CL-6`, security/data/access/dependency/continuity questions and incident/exception treatment;
- `POS-005 — Finance & Obligation Control Lead`: when payment/receivable/cost/contractual-obligation economics materially affects a decision;
- `POS-001 — Company Executive`: cross-Position coordination or decision-ready escalation where existing delegated boundaries do not resolve the case;
- Owner/legal/corporate/customer authorities remain separate capacities, not Positions created by this workflow.

One workflow therefore has one end-to-end accountable Position but multiple bounded execution/control handoffs.

## 8. Authority contract

### 8.1 POS-002 authority

Inside the already Approved AC-203/AC-204/AC-205 envelope, the current human POS-002 Assignment may:

- `AM-0`: assemble/interpret customer evidence and prepare options;
- `AM-1`: execute already committed delivery/feedback-handling steps;
- `AM-2`: make routine issue classification, follow-up, scheduling and delivery-coordination decisions inside accepted scope and approved criteria.

POS-002 MUST escalate rather than decide when the case creates or may create:

- material/non-standard customer commitment (`ROD-03`);
- material portfolio/investment change (`ROD-04`);
- material risk acceptance (`ROD-06`);
- customer/data-rights exception (`ROD-07`);
- critical dependency/technology-sovereignty exception (`ROD-08`);
- material Company↔Product↔Arvectum OS commitment (`ROD-09`);
- strategy/business-model change (`ROD-01`);
- financial exposure entering `ROD-02`;
- legally/corporately regulated act requiring another capacity.

The AI support class currently assigned under POS-002 is **not silently broadened** by AC-502 into autonomous support classification or customer commitment. AI may prepare drafts/evidence when permitted by an existing Assignment/tooling context, but the initial `W3` customer-facing classification act remains attributable to the current human POS-002 Assignment unless a later explicit Assignment change is approved.

### 8.2 POS-004 authority

The AI-led POS-004 Assignment may:

- `AM-0`: analyze technical evidence and propose root cause/correction;
- `AM-1`: implement, test, correct, package and perform already-approved release mechanics;
- `AM-2`: choose routine reversible engineering/testing/tooling approaches inside admitted scope, product architecture, data/security constraints and actual access.

POS-004 MUST stop/escalate when:

- customer/business scope is unclear;
- the correction changes promised outcome or creates a new feature obligation;
- raw customer data/credentials outside approved access are required;
- a material security/data/dependency exception is needed;
- technical success depends on a consequential external action not already admitted;
- a `ROD-*` boundary is implicated;
- required access is absent;
- external effect outcome is uncertain or not safely recoverable.

`W7 — Candidate Ready` is a technical handoff, **not** an approval to send, deploy, promise or declare customer acceptance.

### 8.3 No AM-3/AM-4 activation

AC-502 does not activate `AM-3` or `AM-4` for this workflow.

In particular it does not authorize:

- autonomous customer-facing consequential sending;
- autonomous customer acceptance;
- automatic production deployment;
- automatic exception approval;
- automatic portfolio/product scope expansion.

Any future AM-4 proposal must be evidence-backed and separately approved under AC-203 rather than inferred from M5 success.

## 9. Data contract

### 9.1 Data classes likely in the workflow

Workflow instances may contain:

- `DC-0 — Public`: public site URLs, public product behavior, public repository evidence;
- `DC-1 — Internal`: internal case state, non-sensitive working notes, internal technical status;
- `DC-2 — Confidential`: customer messages, screenshots, non-public requirements, customer environment/logs, commercial context, private sample data;
- `DC-3 — Restricted`: passwords, tokens, Telegram/API credentials, signing/authentication material or equivalent secrets accidentally included in feedback/logs.

Uncertain classification defaults to the more restrictive handling until resolved.

### 9.2 Source and storage boundary

The public Company repository MUST NOT store raw customer-confidential payload, screenshots/logs containing sensitive customer information, credentials, personal data beyond what is necessary, private commercial terms or restricted security data.

The public Company workflow evidence should normally store:

- safe case/reference identifier;
- source location/reference accessible to authorized users;
- sanitized classification summary;
- product commit/PR/test/artifact references;
- approval/escalation references where applicable;
- public-safe measurement/closure metadata.

Raw customer evidence remains in the applicable protected customer/workstream source contour.

### 9.3 Engineering packet boundary

POS-004 receives the **minimum engineering packet** needed for technical correction, ideally:

- affected product version/build;
- reproducible behavior;
- expected behavior as already established by accepted scope/product evidence;
- sanitized logs/screenshots/test input when sufficient;
- environment facts needed for reproduction;
- explicit exclusions and unresolved unknowns.

Raw `DC-2` customer content is not passed to the AI engineering runtime merely because the Owner can access it. `DC-3` MUST NOT enter ordinary model context.

If technical resolution genuinely requires raw confidential data, access must be separately justified/provisioned inside AC-206 and customer/data-rights boundaries; otherwise the workflow stays blocked or uses a human/sanitization path.

### 9.4 Reuse boundary

Customer-specific data, wording, examples and business history do not become reusable Company/product/cross-customer training knowledge automatically.

A generalized technical learning MAY be proposed for productization only after:

- customer-specific content is removed/minimized;
- rights/purpose permit reuse;
- POS-003 evaluates product meaning where material;
- any data/IP/security boundary is resolved.

## 10. Access/tool contract

AC-502 does not provision access. Actual execution is limited by current AC-206 ceilings and product-local controls.

For the first contour:

- POS-002 human may use scoped customer/workstream sources and product evidence needed for delivery/acceptance;
- POS-004 AI may use `RA-02` product repository/worktree `R/W` only for the admitted active workstream, `RA-12` approved engineering environment `R/W/X`, and `RA-13` build/test/artifact operations inside current access ceilings;
- no bank/payment/signing/admin/customer-system privilege is implied;
- no Owner general mailbox or raw secret access is implied;
- product repository access does not create customer/commercial authority.

If actual M5 proof reveals that a required technical/data access is not provisioned, the correct result is `blocked/escalate`, not credential sharing by convenience.

## 11. Evidence contract

Each real workflow instance should preserve enough evidence to reconstruct consequential transitions without storing chain-of-thought or restricted payload.

### 11.1 Minimum evidence set

| Evidence | Required meaning |
|---|---|
| `E1 — Source feedback` | attributable source/reference, time/context, protected raw evidence location if non-public |
| `E2 — Scope/product-state reference` | version/build and accepted behavior/scope evidence sufficient for classification, or explicit `unknown` |
| `E3 — Classification record` | classification, attributable Position/capacity, rationale summary and unresolved uncertainty |
| `E4 — Technical admission packet` | bounded correction objective, exclusions and stop/escalation conditions |
| `E5 — Implementation provenance` | product issue/branch/commit/PR/diff references as applicable |
| `E6 — Verification evidence` | tests, reproduction before/after, regression/packaging evidence proportionate to case |
| `E7 — Candidate provenance` | version/build/artifact identifier and known limitations |
| `E8 — Customer handoff evidence` | attributable evidence that candidate/instructions were actually sent or made available through an authorized channel |
| `E9 — Customer validation/acceptance` | explicit customer result or authoritative acceptance source; absence remains pending |
| `E10 — Closure/reclassification record` | final workflow outcome and next control point if not accepted |
| `E11 — Escalation/risk/control references` | linked `DEC/APR/ESC/RSK/EXC/INC/WORK/OBL` only where material qualification applies |
| `E12 — M5 measurement data` | Owner interventions, blocking/rework loops, cycle markers, execution/control effort where feasible |

### 11.2 Evidence does not mean duplicate system of record

AC-502 prefers references over copying.

- Product code/test/release truth remains product-owned.
- Customer feedback/acceptance truth remains in the customer/communication source contour.
- Legal/contractual obligation truth remains in its authoritative source.
- Company register entries are created only when AC-401/402/403 material qualification requires them.

AC-502 does **not** introduce a universal `WFCASE-*` register or duplicate the product issue tracker.

## 12. Transition gates

### W0 → W1

Allowed when source feedback can be referenced and data handling is safe enough to normalize minimum context.

Stop if feedback contains uncontained `DC-3`; remove/quarantine the secret from ordinary workflow context and follow the applicable security path.

### W1 → W2

Allowed when enough scope/product/environment evidence exists to make a routine classification decision.

If not, remain `CL-3 / evidence insufficient` and request targeted evidence instead of guessing.

### W2 → W3

Routine classification is a POS-002 `AM-2` act inside accepted scope.

Ambiguous material commitment/risk/data/product-boundary cases escalate rather than being forced into `CL-1`.

### W3 → W4

Only `CL-1` normally enters correction immediately.

`CL-2` may produce guidance/configuration work; `CL-4/5/6` leave the normal correction path until the relevant authority/product/risk gate resolves them.

### W4 → W5

Requires bounded technical objective, actual POS-004 access, product workstream context and no unresolved stop gate.

### W5 → W6 → W7

Requires implementation and proportionate verification evidence. Tests must match the observed failure mode where feasible; a green unrelated test suite is insufficient evidence by itself.

### W7 → W8

Requires an authorized customer-facing handoff. In the initial M5 configuration, this is not an autonomous AI external effect.

### W8 → W10

Requires explicit customer/authorized acceptance/resolution evidence for the applicable correction.

Customer validation of one correction does not imply full Discount Parser production acceptance unless the complete relevant product acceptance gate is actually satisfied.

### W8 → W9

New customer evidence disproves the correction or reveals another in-scope failure. A new loop retains prior candidate provenance.

## 13. Unknown, stale and contradictory evidence behavior

Workflow facts are not assumed current forever.

The case MUST stop/review when material evidence is:

- missing;
- stale relative to a newer delivered/build state;
- contradicted by current customer evidence;
- superseded by a newer product version or customer instruction;
- based only on model memory/chat summary without source support;
- dependent on an expired/revoked approval/access basis.

Specific rules:

1. unknown product version → do not assume current main equals customer installation;
2. unknown accepted scope → do not promise correction as an existing obligation;
3. unknown customer validation → remain pending, not accepted;
4. changed customer reproduction evidence after candidate creation → re-open/reclassify rather than preserve stale PASS;
5. test PASS against a different environment → label the mismatch rather than infer target-machine success.

## 14. Escalation matrix

| Trigger | Primary target | Required behavior |
|---|---|---|
| non-standard/material customer promise or scope | Owner/legal path through POS-002/POS-001 | prepare decision-ready packet; no promise before decision |
| productization/reuse/roadmap meaning | POS-003 | separate customer correction from product investment decision |
| material security/data/access/dependency issue | POS-006 | AC-403 risk/incident/exception path where qualified |
| material cost/cash/obligation consequence | POS-005 | source-backed finance/obligation evidence before decision |
| missing/unclear authority | actual competent authority | fail closed; do not route everything to Owner if another authority owns it |
| customer acceptance/consent required | customer-authorized Principal/source | Company cannot approve on customer's behalf |
| legal/corporate act required | legally competent capacity | Position/AI approval does not substitute legal act |
| potential Arvectum OS dependency/contract implication | AC-503 + OS governance if applicable | do not infer OS admission in AC-502 |

Correct escalation is a successful workflow outcome when the case exceeds the admitted envelope.

## 15. Failure, rollback and continuity behavior

### 15.1 Technical failure

If implementation/test evidence fails:

- do not advance to `W7`;
- preserve failed candidate evidence where useful;
- revert/adjust within product-local safe engineering practices;
- if failure introduces a material incident/risk, route to AC-403.

### 15.2 Incorrect candidate after customer delivery

If the delivered candidate worsens behavior or creates a new defect:

- stop further distribution of that candidate where controllable;
- preserve previous known-good version/reference where available;
- re-enter `W9 — Rework Required` or incident path according to consequence;
- do not claim resolution until new customer evidence exists.

AC-502 does not assert that every product version has a tested automatic rollback mechanism; AC-506 must later drill actual recovery/fallback behavior.

### 15.3 Owner/POS-002 unavailability

AI does not inherit POS-002 human `AM-2`, Owner `ROD-*` or customer-commitment authority.

Permitted degraded behavior:

- preserve intake/source evidence;
- perform safe non-consequential technical/evidence preparation already inside an existing Assignment;
- queue customer/business classification where the human decision is required;
- fail closed on new commitments/exceptions.

### 15.4 POS-004 AI runtime loss

A specific model/agent/runtime may be replaced if an eligible replacement can operate inside the same Assignment/access boundary.

If no eligible AI runtime exists, technical work pauses or an explicit human/replacement Assignment is created through the proper path. Owner availability does not silently create a human POS-004 Assignment.

### 15.5 Customer unavailable

Candidate readiness is preserved, but the case remains `W8 — Customer Validation Pending` or explicit blocked state. Silence is not acceptance.

## 16. Company control-register mapping

AC-502 uses M4 control models proportionately rather than creating a record for every product task.

Create/link Company-level records only when the material qualification gates are met:

- `WORK-*` — material Company control work;
- `OBL-*` — material Company obligation requiring Company-level visibility;
- `DEC-*` / `APR-*` / `ESC-*` — material decision/approval/escalation instance;
- `RSK-*` / `EXC-*` / `INC-*` — material risk/exception/incident.

Routine product bug correction remains product-local plus workflow evidence unless its business consequence qualifies for Company-level control.

Closing a technical task does not automatically satisfy an `OBL-*`. Customer acceptance/contract source remains a separate gate.

## 17. Initial real-operation execution model

For M5 supervised proof, the intended first instance pattern is:

```text
customer feedback arrives
→ POS-002 human normalizes customer meaning / identifies missing evidence
→ POS-004 AI may analyze technical evidence and prepare root-cause/correction evidence
→ POS-002 human performs routine CL-* classification inside AM-2, or escalates
→ if CL-1: bounded technical packet admitted
→ POS-004 AI executes correction + tests + package/candidate evidence
→ POS-002 human checks business/scope handback and performs authorized customer handoff
→ customer validates
→ explicit acceptance / rework / reclassification / escalation
→ evidence + M5 measurement captured
```

This is intentionally less autonomous than a future mature workflow. M5 proves governed operation first; M6 and later evidence may justify executor/authority changes.

## 18. M5 measurement inputs

AC-505/AC-507 must be able to evaluate value without inventing historical baselines.

For each real instance, capture where feasible:

### Customer/value

- customer-confirmed resolved/not-resolved outcome;
- number of rework loops;
- whether the case stayed inside accepted scope or became new scope;
- whether evidence/clarification prevented unnecessary engineering;
- whether validation occurred on the relevant real environment.

### Owner burden

- number of Owner/POS-002 interventions;
- intervention class: routine classification, material decision, customer handoff, exception, local/credential gate, state reconstruction;
- whether intervention was planned or interrupt-driven;
- blocking wait attributable to Owner/human decision where materially useful;
- repeated context reconstruction that a workflow packet avoided or failed to avoid.

### Engineering/quality

- correction cycle markers: admitted → candidate ready → customer result;
- failed internal verification attempts/rework loops;
- regressions or candidate rollback/replacement events;
- evidence completeness/reconstructability;
- AI/runtime replacement or failure if observed.

### Cost/control burden

- material human effort estimate at useful granularity where available;
- AI/tool/runtime effort/cost evidence if measurable without disproportionate instrumentation;
- governance/control steps that created value versus ceremony;
- any duplicated evidence capture or unnecessary Owner gate.

AC-502 does not set fabricated numerical success thresholds. AC-505 must obtain real supervised evidence; AC-507 will make the continue/change/stop judgment from that evidence.

## 19. M5 proof claims permitted and prohibited

If later evidence supports it, M5 may claim only what was actually observed, for example:

- workflow transitions were followed on real customer cases;
- Position/authority separation worked;
- POS-004 performed bounded AI-led technical execution;
- escalation/fail-closed behavior occurred correctly;
- evidence permitted reconstruction;
- Owner involvement changed in a measurable direction;
- customer correction outcomes were accepted or not accepted.

M5 MUST NOT infer from those facts alone:

- Company-wide AI autonomy;
- product profitability;
- market validation;
- full product production readiness;
- legal compliance;
- generic customer acceptance model;
- universal support SLA;
- Stable Product Contract / Active Arvectum OS capability;
- readiness of unrelated Company workflows.

## 20. Arvectum OS non-assumption boundary

AC-502 does not require Arvectum OS to execute `WF-M5-001` and does not create a new Product Contract or platform dependency.

Current Company portfolio evidence records an existing bounded Discount Parser ↔ Arvectum OS correspondence, but whether the selected **workflow itself** should rely on any OS contract/capability must be determined separately in:

`AC-503 — Arvectum OS reliance/admission mapping where applicable`.

AC-503 may conclude `no additional OS reliance required`. AC-502 does not prejudice that result.

## 21. Approval effect and non-effects

If approved, AC-502 becomes binding Company workflow-governance semantics for the first M5 proof.

Approval would authorize only:

- use of the defined workflow states/classification/evidence contract;
- execution inside already Approved Position/Assignment/authority/access envelopes;
- preparation of AC-503/AC-504 based on this bounded contract.

Approval would **not**:

- create a customer/legal obligation;
- change accepted customer scope;
- grant new credentials/access;
- create a new Assignment;
- activate `AM-3`/`AM-4`;
- authorize spend/payment/signing;
- approve a product release or production deployment by implication;
- approve raw customer data use by AI;
- change PORT-002 disposition/investment;
- create an Arvectum OS Product Contract/lifecycle change;
- close M5.

## 22. AC-502 completion criterion and handoff

AC-502 is complete when the exact reviewed workflow contract is explicitly approved and the Company can answer, before implementation:

- what starts/ends one workflow instance;
- who is accountable end-to-end;
- who owns technical execution;
- which decisions are allowed at which authority mode;
- what remains human/Owner/customer/legal authority;
- what data may flow where;
- what evidence is required for each consequential transition;
- how unknown/stale/conflicting facts stop progression;
- how failures/escalations/fallback behave;
- what measurements AC-505/AC-507 must capture;
- that AC-502 does not silently create OS reliance.

После approval следующее каноническое действие:

`AC-503 — Arvectum OS reliance/admission mapping where applicable`.
