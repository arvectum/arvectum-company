# AC-503 — First Governed Workflow: Arvectum OS Reliance / Admission Mapping

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-503 — Arvectum OS reliance/admission mapping where applicable`
Milestone: `M5 — First real governed Company operating contour proven`
Workflow: `WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`
First application contour: `PORT-002 — Discount Parser`
Depends on: AC-501 `Approved 1.0.0`; AC-502 `Approved 1.0.0`; AC-002 Company↔OS boundary; current canonical Arvectum OS state
Approval status: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Decision question

AC-503 отвечает на один узкий практический вопрос:

> Требует ли первый реальный M5 proof для `WF-M5-001` фактической опоры на Arvectum OS, shared governed OS history, OS canonical state или admitted Platform Capability — и если да, какой минимальный Product Contract / capability admission path необходим до AC-504?

Результат AC-503 не должен выводиться из того, что Arvectum OS уже существует, что Discount Parser ранее использовался как Phase 6 validation target или что OS технически способен представить workflow/execution/evidence.

Business-first criterion:

```text
use OS when governed reliance is materially needed or creates enough value
≠
use OS because dogfooding is architecturally attractive
```

## 2. Exact proposed result

Предлагаемый результат AC-503:

**`NO-ADDITIONAL-OS-RELIANCE — no additional Arvectum OS reliance required for the first M5 proof of WF-M5-001`.**

Следствия этого результата:

1. AC-504 может реализовать первый bounded workflow contour на Company/product/customer-owned sources and tools без обязательной записи workflow instances в Arvectum OS.
2. Не требуется новый или изменённый Arvectum OS Product Contract до первого M5 proof.
3. Existing `P6.06 — Second Real Product / Workflow Product Contract Boundary` остаётся неизменным и применим только в своём exact scope.
4. `CAP-004 — Audit / Reconstruction Support` не становится dependency `WF-M5-001` по импликации.
5. Никакой Platform Capability lifecycle transition не требуется.
6. Никакой Arvectum OS repository change этим Company decision не создаётся и не считается committed.
7. AC-504 должен сохранить OS-neutral evidence boundary, чтобы позднее admitted reliance можно было добавить без потери Company history или переписывания бизнес-семантики.

Это **не** решение «Company не использует Arvectum OS». Это bounded admission decision только для первого M5 proof выбранного workflow.

## 3. Current canonical Arvectum OS re-check

Перед AC-503 повторно проверен `arvectum/arvectum-os` `main`:

`76504766353028540891ac1dfdbf1e5dc331a4af` — `R30 — M9-alpha Usability / Information Architecture Review`.

Current canonical baseline на этом commit:

- Constitution `1.2.0` — `Ratified`;
- RFC-0001 through RFC-0008 — `Accepted 1.0.0`;
- canonical OS roadmap `2.81.0`;
- current OS action: `P9.07 — Product-owned workspace surfaces / composition`;
- CAP-001 through CAP-004 — `Incubating / Provisional`;
- no Platform Capability is `Active`;
- P6.02, P6.06, P8.03 and P8.06 Product Contracts remain `Provisional` in their exact scopes;
- current operating environment remains `Local / Persistent Internal / owner-operated` with scoped conformance;
- Decision Authority Policy remains `Proposed 0.2.1` and therefore is not treated as a new binding Company/OS authority source.

This current state is materially relevant because technical usability, M9-alpha achievement or prior product validation does not itself create Stable Product Contract, Active Capability or broader reliance permission.

## 4. Higher-authority OS rules applied

### 4.1 Constitution `1.2.0`

The OS Constitution establishes several directly relevant rules:

- shared capabilities belong in OS when reuse is validated, strategically required, or necessary for governance/security/identity/provenance/interoperability;
- products may keep bounded reversible local experiments when uncertainty is high;
- shared platform semantics must remain domain-neutral;
- authoritative knowledge has one canonical source;
- organizational control/portability must not depend on a specific runtime/vendor;
- workflow formalization and human control are proportional to risk/consequence;
- architecture and governance serve organizational value;
- OS must not impose platform complexity where a simpler reversible solution is sufficient.

These rules permit — and in this case favor — a bounded Company/product-local M5 proof when no material OS dependency is required.

### 4.2 RFC-0004 `1.0.0`

Accepted RFC-0004 establishes:

- Product Contract as the explicit product/platform boundary;
- **no Product Contract requirement for a fully product-local bounded experiment that does not use platform capabilities, shared platform history or canonical platform state**;
- Product Contract is mandatory before governed platform reliance;
- Product Contract lifecycle is separate from Platform Capability lifecycle;
- hidden coupling through private implementation state is prohibited.

Therefore AC-503 must not create a Product Contract merely because one could be written. It must first establish actual governed platform reliance.

### 4.3 RFC-0005 `1.0.0`

Accepted RFC-0005 establishes domain-neutral Governed Execution semantics when OS governed execution is actually used, while explicitly leaving product-specific business workflows product-owned by default.

It also establishes that:

- exact Product Contract attribution is required where RFC-0004 applies;
- AI is an execution means, not Organizational Authority;
- Platform Capability activation/readiness does not follow merely from RFC acceptance or workflow evidence.

WF-M5-001 is therefore allowed to remain Company-owned and product/customer-referenced during first proof without pretending that its Company-specific states/classes are OS platform semantics.

## 5. Existing Discount Parser ↔ Arvectum OS boundary

Arvectum OS already contains:

`docs/contracts/P6-06-SECOND-REAL-PRODUCT-CONTRACT.md`

with status:

- Product Contract lifecycle: `Provisional`;
- version: `0.1.0`;
- product: `arvectum/discount-parser`;
- P6.06 result: `PASS` within the exact Phase 6 validation scope.

Its selected target is not the AC-502 feedback/correction workflow. Its exact scope is a **controlled Telegram publication workflow** from product-owned discount/promo data through publication eligibility to a manual or pre-authorized scheduled Telegram publication attempt, with governed reconstruction of the consequential external effect.

P6.06 has one minimum declared shared dependency:

`CAP-004 — Audit / Reconstruction Support` — lifecycle `Incubating`, contract `Provisional`.

P6.06 explicitly retains product ownership of source adapters, Offer semantics, classification, deduplication, scheduler, publication rules, Telegram integration, UI and other product-domain behavior.

### 5.1 Why P6.06 does not automatically govern WF-M5-001

`WF-M5-001` covers:

```text
customer feedback
→ Company classification
→ admitted correction
→ product engineering / verification
→ customer validation / acceptance evidence
```

P6.06 covers:

```text
eligible publication candidate
→ governed external Telegram publication attempt
→ external-effect evidence / reconstruction
```

They are materially different operations, authority surfaces and evidence questions.

Using P6.06 merely because both concern Discount Parser would violate the exact Product Contract boundary and risk hidden scope expansion.

If a future WF-M5-001 implementation genuinely needs OS governed execution/history/CAP-004, the Company must re-open admission and use the correct Product Contract/version/OS governance path; P6.06 `0.1.0` must not be silently stretched to cover it.

## 6. Platform Capability lifecycle check

Current active capability catalog is:

`docs/catalogs/PLATFORM-CAPABILITY-CANDIDATE-CATALOG.md` — `Active 1.2.1`.

Relevant facts:

- CAP-001…CAP-004 are `Incubating / Provisional`;
- `Incubating` authorizes bounded validation only and is not production/stable/SLA/commercial status;
- CAP-004 is retained for read-oriented reconstruction of consequential operations from governed evidence;
- product reports/narratives/review UX remain product-owned;
- no capability may become `Active` without separate admission, readiness and decision authority;
- successful product integration or roadmap milestone does not itself promote lifecycle.

The legacy `docs/architecture/CAPABILITY-CATALOG.md` is explicitly `Deprecated / Informative` and must not be used to infer lifecycle state.

AC-503 therefore creates no CAP-004 promotion or new CAP-004 reliance.

## 7. Company-owned semantics that must remain outside OS

The following approved AC-502 semantics are Company-owned and MUST NOT become shared OS semantics by convenience:

- `WF-M5-001` business purpose;
- customer-feedback intake meaning;
- states `W0…W11` as Company workflow states;
- classification taxonomy `CL-1…CL-7`;
- `POS-002` end-to-end accountability;
- `POS-004` technical-segment accountability;
- Company `ROD-*` and `AM-*` application to this workflow;
- defect vs input/config/environment vs new scope vs product limitation classification;
- customer validation/acceptance meaning;
- Company-specific escalation routing;
- M5 Owner-burden/business-value measurements.

Arvectum OS may later represent versioned workflow/execution/provenance objects through domain-neutral contracts if admitted, but OS must not own or redefine this business meaning.

## 8. Product- and customer-owned semantics that remain outside OS

`arvectum/discount-parser` remains canonical for:

- product code and implementation;
- product issue/root-cause/technical task detail;
- tests/build/release-candidate evidence;
- product-specific schemas/UX/configuration;
- source onboarding/mapping and parser behavior;
- product-local release/version state.

The applicable protected customer/workstream source remains authoritative evidence source for:

- raw feedback message/content;
- customer screenshots/logs/input where provided;
- customer environment facts as reported/verified;
- explicit customer validation/acceptance/rejection/change request.

The Company workflow stores/uses references and sanitized interpretation, not competing raw truth.

## 9. Actual dependency test for first M5 proof

AC-503 evaluates whether AC-504/AC-505 require OS for each plausible dependency class.

| Possible OS reliance | Needed for first M5 proof? | Reason |
|---|---|---|
| OS canonical Workflow record | `No` | Approved Company artifact already canonically defines WF-M5-001; first proof can pin exact Company version/reference. |
| OS Execution Context | `No` | first proof can reconstruct one case from Company case/evidence references plus product/customer sources without making OS execution history canonical. |
| OS Organization/Actor records | `No` | Company Position/Principal/Assignment attribution can be recorded through current Company governance/evidence; no OS-held identity is required for the first proof. |
| CAP-004 reconstruction | `No` | reconstruction can be achieved through exact references to feedback, classification, product PR/commit/tests/build and customer validation; CAP-004 adds platform coupling but is not necessary. |
| CAP-001 Documents/Artifacts | `No` | raw customer evidence and product artifacts remain customer/product-owned; no shared document admission is required. |
| CAP-002 Memory/Knowledge | `No` | validated reusable learning is not a prerequisite to prove the workflow; productization/learning promotion remains later evidence work. |
| CAP-003 Search/Index | `No` | discovery convenience is not required to execute or reconstruct the first case. |
| OS authority enforcement | `No` | current first contour keeps POS-002 human classification/customer gates and bounded POS-004 engineering under approved Company authority/access; no new automated consequential authority is being introduced. |
| OS shared event/provenance history | `No` | public-safe exact references and product/customer evidence are enough for first proof; OS event history may be considered later if reuse/value is validated. |
| Productive Workspace composition | `No` | useful UX may later reduce Owner workload, but P9.07/P9.10 work is not a dependency of AC-504/AC-505 first proof. |

Result: no dependency is currently necessary to make the first M5 proof valid, reconstructable or authority-safe.

## 10. Why `bounded existing OS reliance is sufficient` is not the selected result

That alternative would imply that WF-M5-001 actually relies on an already admitted OS boundary and merely needs no additional contract change.

Current evidence does not support that statement.

The existing P6.06 reliance is narrowly scoped to governed Telegram publication/reconstruction. WF-M5-001 has a different start/end, customer authority boundary and technical purpose. Declaring P6.06 “sufficient” would blur exact Product Contract scope.

Therefore the more accurate result is:

`no additional OS reliance required for first M5 proof`.

Existing P6.06 remains valid in its own scope and is neither revoked nor enlarged.

## 11. AC-504 implementation boundary after approval

If AC-503 is approved, AC-504 should implement the **smallest OS-neutral governed workflow mechanics** sufficient for actual operation.

Minimum durable/public-safe evidence shape should preserve, where applicable:

1. workflow identity/version reference (`WF-M5-001`, exact approved AC-502 publication/blob);
2. safe case identifier;
3. protected feedback source reference + received time;
4. customer/workstream/product/build context;
5. data classification/sanitization state;
6. current `W*` state and prior significant transitions;
7. current `CL-*` classification + attributable POS-002 act;
8. admitted technical scope/exclusions;
9. POS-004 implementation evidence: product issue/PR/commit/test/build references;
10. candidate-ready result/known limitations;
11. customer-facing handoff evidence where validly performed;
12. explicit customer validation/acceptance/rework/change evidence;
13. decision/escalation/risk/incident references where existing AC-401/402/403 material gates trigger;
14. Owner intervention/reconstruction/cycle/rework measurements required by AC-502;
15. explicit unknown/stale/blocked/uncertain fields rather than inferred success.

This evidence format is intentionally **OS-neutral**. It should use stable identifiers/references and exact versions so a future migration/admission can map the history without making today's runtime/platform choice authoritative.

AC-504 should not build a generic workflow engine, event bus, CAP-004 substitute, new Company-wide database or platform abstraction merely to avoid OS. A lightweight existing-tool/repository/product-local implementation is preferred where sufficient.

## 12. Future re-admission triggers

Re-open Company↔OS reliance mapping before or during AC-504/AC-505 if any of the following becomes necessary rather than merely convenient:

1. WF-M5-001 must write/read shared Arvectum OS canonical state;
2. the workflow must use OS Execution Context / Governed Execution for a consequential action;
3. multiple products need the same domain-neutral reconstruction semantics and local evidence handling becomes material duplication/risk;
4. CAP-004 becomes materially useful to Owner/control quality beyond its integration cost;
5. Productive Workspace becomes the actual operating surface and requires admitted product/workflow composition;
6. OS-held Organization/Actor/authorization enforcement becomes necessary for a consequential effect;
7. shared event/provenance history is required for trustworthy reconciliation or external-effect uncertainty;
8. a later `AM-4`/more autonomous workflow proposal requires stronger domain-neutral governed execution enforcement;
9. product/customer evidence is deliberately migrated into an OS-admitted canonical/replica model;
10. a second materially distinct Company workflow demonstrates validated reusable platform demand.

When a trigger is met, the required sequence is:

```text
Company need/evidence
→ identify Company vs Product vs OS ownership
→ inspect current OS contract/capability scope
→ use existing exact admitted boundary if truly applicable
OR
→ propose Product Contract/version/capability/RFC/ADR change through OS governance
→ explicit approval/admission
→ only then governed reliance
```

No hidden cross-repository commitment is permitted.

## 13. Sovereignty, portability and fallback

The proposed no-additional-reliance result has favorable first-proof sovereignty properties:

- customer/product/Company canonical evidence remains under current controlled repositories/workstream sources;
- no new runtime/vendor/platform dependency becomes necessary for continuation;
- the workflow can fall back to the existing human-led correction loop if automation/evidence tooling fails;
- POS-004 runtime may be replaced under AC-207 without changing workflow meaning;
- OS unavailability does not block the first correction/validation contour;
- stable references and exact versions preserve a future migration path.

This is not an argument against self-hosted Arvectum OS. It is a proportionality and dependency-admission decision: the first real Company proof should not gain a new critical dependency before its business/control value is demonstrated.

## 14. Risk and downside analysis

### Risk avoided by not adding OS now

- premature Company↔OS coupling;
- accidental expansion of P6.06 beyond its Provisional exact scope;
- treating CAP-004 incubation evidence as production/Active capability;
- additional implementation/control cost before M5 empirical value exists;
- moving Company/customer semantics into shared platform behavior;
- creating a second source of truth for customer/product workflow state;
- making OS availability a new operational dependency of current customer correction work.

### Risk introduced by not adding OS now

- first-proof reconstruction may be less automated/ergonomic than CAP-004;
- evidence links may remain distributed across customer/Product/Company sources;
- Owner may still do some manual state reconstruction;
- later OS admission may require mapping/migration work.

These risks are acceptable for the first bounded proof because AC-502 explicitly measures Owner reconstruction burden and AC-504 can preserve stable evidence references. AC-507 can then decide whether platform reliance creates enough value to justify the added dependency.

## 15. Evidence to carry into AC-505 / AC-507

To evaluate whether the no-additional-OS decision remains correct, real operation should capture:

- time/effort to reconstruct one case without OS;
- number of missing/broken evidence references;
- number of manual cross-source lookups needed by Owner/POS-002;
- ambiguity caused by distributed state;
- whether POS-004 can execute from minimized engineering packet;
- number/type of authority/escalation gates;
- rework cycles and cause;
- customer validation outcome;
- whether an OS capability would have eliminated a material repeated cost/risk;
- estimated/observed integration/control cost of adding OS reliance.

If evidence shows repeated reconstruction cost or control risk that CAP-004/domain-neutral OS execution can materially reduce, a later admission proposal becomes evidence-backed rather than architecture-driven.

## 16. Explicit non-effects

Approval of AC-503 would **not**:

- remove or deprecate Arvectum OS;
- revoke, alter or promote P6.06;
- alter CAP-001…CAP-004 lifecycle;
- create a new Product Contract;
- make any Product Contract `Stable`;
- make any Platform Capability `Active`;
- modify OS Constitution/RFC/ADR/policy/catalog;
- change Discount Parser product roadmap or implementation by itself;
- create customer promise/acceptance;
- activate `AM-3`/`AM-4`;
- grant access/credentials;
- prove M5 complete;
- preclude later OS reliance when evidence justifies it.

## 17. AC-503 acceptance criteria

AC-503 is ready for approval when all are true:

1. current OS canonical state has been re-checked;
2. higher-authority Constitution/RFC-0004/RFC-0005 constraints are applied;
3. existing P6.06 exact scope is distinguished from WF-M5-001;
4. current CAP-004 lifecycle is correctly represented as `Incubating / Provisional`;
5. Company/Product/customer/OS ownership is explicit;
6. every plausible first-proof OS dependency has a reasoned disposition;
7. result does not create a hidden cross-repo commitment;
8. AC-504 receives a minimal reversible OS-neutral implementation boundary;
9. future re-admission triggers are explicit;
10. sovereignty/fallback and evidence consequences are explicit.

## 18. Proposed handoff

Upon explicit Owner approval:

- publish AC-503 as `Approved 1.0.0`;
- record the Owner decision;
- synchronize Roadmap / Canonical Sources / README;
- mark `AC-503 — Complete / PASS`;
- advance current canonical action to:

`AC-504 — Bounded workflow implementation`.

AC-504 should implement only the minimum real operating/evidence mechanics required by approved AC-502/AC-503, without building generic platform layers or changing Arvectum OS unless a re-admission trigger is actually met.
