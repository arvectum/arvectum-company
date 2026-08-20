# AC-002 — Arvectum Company ↔ Arvectum OS Authority and Responsibility Boundary

Status: `Approved`
Version: `1.0.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Approved: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-002 — Company ↔ Arvectum OS authority and responsibility boundary`
Company constitutional basis: `docs/constitution/COMPANY-CONSTITUTION.md` — Ratified `1.0.0`
Arvectum OS baseline: Constitution `1.2.0`; RFC-0001…RFC-0008 `1.0.0` — Accepted within their declared scopes
Cross-review: `docs/reviews/AC-002-COMPANY-OS-AUTHORITY-BOUNDARY-CROSS-REVIEW.md`
Approval: `docs/governance/decisions/DECISION-2026-08-20-AC-002-APPROVAL.md`
Approved proposal: `Proposed 0.9.0`, blob `faed6d8503dfe771b4505f02ff8fed23aa5e9cb0`

## 1. Purpose

This artifact defines the Company-specific authority and responsibility boundary between **Arvectum Company** and **Arvectum OS**.

Its purpose is to make later organizational design, Company workflows and AI/software execution possible without creating any of the following category errors:

- treating Arvectum OS as the source of corporate or Organizational Authority over ООО «Арвектум»;
- treating a Company policy, workflow or roadmap as authority to change Arvectum OS contracts;
- moving Company-specific or product-specific semantics into the domain-neutral platform merely for convenience;
- treating authentication, technical permissions, API access or successful execution as approval or decision authority;
- allowing one repository to create hidden commitments in another repository;
- turning OS canonical-state responsibility into legal ownership or business authority by implication.

This document is a **Company governance boundary artifact**. It does not amend the Company Constitution, Arvectum OS Constitution/RFCs, any product Product Contract, legal charter, corporate decision, power of attorney or contract.

## 2. Scope and non-goals

This artifact defines:

- the authority domains relevant to Company ↔ OS interaction;
- Company-owned, OS-owned and product-owned responsibilities;
- how Company authority may be represented and enforced through OS without being created by OS;
- when Company reliance on OS requires Product Contract or another explicit contract boundary;
- the minimum governed-execution rules for consequential Company work performed through OS;
- cross-repository change, conflict and reconciliation paths;
- failure, continuity and de-platformization expectations;
- unresolved questions that are deliberately deferred to later Company roadmap items.

This artifact does **not** define:

- the final Company organizational structure;
- Reserved Owner Decisions beyond the Ratified Constitution;
- delegated Position authority limits;
- Position Registry or Assignments;
- concrete IAM roles or permissions;
- final Company schemas in Arvectum OS;
- a new Arvectum OS capability, RFC, ADR, service or Product Contract;
- product-specific implementation, workflows or roadmap changes;
- legal advice or a substitute for applicable corporate/legal authority.

Those matters remain in their existing roadmap/governance paths.

## 3. Authority domains are separate, not one flat hierarchy

Company ↔ OS interaction must distinguish at least the following authority domains.

### 3.1 Legal and corporate authority

This domain determines whether a person or entity is legally entitled to bind, represent or act for ООО «Арвектум» in the relevant external or corporate scope.

Applicable sources include, within their scope:

- applicable law;
- the governing charter of ООО «Арвектум»;
- valid decisions of the participant or other competent corporate authority;
- powers of the General Director / sole executive body;
- powers of attorney;
- contracts and other legally effective authorizations.

A Company or OS artifact may record or reference such authority, but cannot create legal authority merely by declaring it.

### 3.2 Company Organizational Authority

This domain determines internal organizational entitlement to make, approve or execute Company decisions within the approved operating model.

Its sources include, within their scope:

- the Ratified Company Constitution;
- explicit Owner decisions;
- approved Company policies, delegations, Positions, assignments, workflows and decision records created under the Company governance path;
- later approved Reserved Owner Decision and delegated-authority artifacts.

Until explicit Company delegation exists, material internal residual authority remains with the applicable Owner/competent Principal under the Company Constitution.

### 3.3 Arvectum OS governance authority

This domain determines the valid architecture, contracts, lifecycle, conformance and governed behavior of **Arvectum OS itself**.

Its sources include, within their scope:

- Arvectum OS Constitution;
- Accepted RFCs;
- Accepted ADRs;
- approved OS policies, procedures, standards and catalogs;
- applicable Product Contracts and capability contracts;
- approved platform decisions and operational-readiness evidence where required.

OS governance authority can determine what the platform will accept, reject, preserve or enforce. It does **not** create corporate authority over ООО «Арвектум».

The current OS `DECISION-AUTHORITY-POLICY.md` remains `Proposed 0.2.1`; it is design reference only until approved and therefore must not be treated as a binding OS authority matrix.

### 3.4 Product governance authority

Product-specific business semantics, implementation and product operational decisions remain governed by the corresponding product repository, Product Contract and approved product decisions.

The Company may own the portfolio decision to fund, prioritize, continue, change or stop a product. That does not make the Company repository the canonical source of product implementation detail.

### 3.5 Technical authorization

Technical authorization answers whether an authenticated actor or component may attempt a specific operation on a governed resource.

Examples include:

- IAM role or grant;
- API permission;
- service credential scope;
- OS capability permission;
- runtime tool access;
- database or infrastructure access.

Technical authorization is necessary for many actions but is not sufficient evidence of Company Organizational Authority, legal authority or required approval.

### 3.6 Non-substitution rule

No authority domain above automatically substitutes for another.

In particular:

- legal capacity does not automatically create an approved internal workflow or technical permission;
- an internal Owner decision does not replace a legally required participant decision, General Director act, power of attorney, signature or other required corporate/legal form;
- Company Organizational Authority does not automatically create OS authorization or change an OS contract;
- OS governance approval does not authorize a Company business decision;
- technical authorization does not create legal, corporate or Organizational Authority;
- product implementation ownership does not create portfolio capital authority;
- AI recommendation, successful execution or workflow completion does not create approval.

## 4. Responsibility boundary

### 4.1 Arvectum Company owns Company-specific organizational meaning

The Company is responsible for the meaning, approval and lifecycle of Company-specific organizational semantics, including:

- mission, strategy and business model;
- Company functions and organizational units where justified;
- Positions and accountable outputs;
- Assignments and executor responsibility;
- Owner-reserved and delegated authority boundaries;
- budgets, capital allocation and risk appetite;
- portfolio priorities and initiative stop/continue decisions;
- Company policies, standards and procedures;
- Company business workflows and approvals;
- Company decisions, obligations, incidents and exceptions;
- Company AI Workforce design;
- Company-specific classification/use rules above mandatory legal/OS requirements;
- Company organizational knowledge content and meaning;
- customer-facing commitments and internal authority for making them.

The Company may use OS to store, version, relate, execute or reconstruct these objects. Such use does not transfer their organizational meaning or decision authority to OS.

### 4.2 Arvectum OS owns domain-neutral platform semantics and contracts

Arvectum OS is responsible for domain-neutral platform semantics and contracts within its accepted governance, including where applicable:

- Identity semantics;
- Canonical Record and immutable version semantics;
- authority-mode representation;
- Typed Relationships;
- Event semantics;
- Execution Context and Governed Execution;
- authentication/authorization architecture and enforcement semantics;
- Organization/tenant isolation;
- provenance and reconstruction semantics;
- document/artifact governance mechanisms;
- memory/knowledge/governed-learning mechanisms;
- security, privacy, minimization, retention/deletion and portability architecture;
- Product Contract and platform-capability lifecycle semantics;
- domain-neutral conformance and compatibility rules.

OS owns these **platform contracts and mechanisms**, not the underlying Company business decision that a record, grant, approval or workflow may represent.

### 4.3 Products own product/domain semantics

A product remains responsible for domain concepts and behavior such as:

- product-specific schemas and taxonomies;
- product-domain workflows;
- domain risk models and scoring;
- product prompts, agents and validators;
- product integrations and UX;
- product-specific search/ranking logic;
- product commercial packaging and support behavior;
- bounded Product Experiments before platform promotion.

A Company portfolio decision may govern investment and accountability, while product implementation remains in the product repository.

### 4.4 Technology owns no organizational meaning by default

A runtime, model, framework, database, cloud, secret store, scheduler or vendor executes or stores declared semantics. It does not become the source of organizational meaning or authority merely because it is technically necessary.

## 5. Canonical-state responsibility does not equal Organizational Authority

A central AC-002 rule is that **system-of-record responsibility and Organizational Authority are different concepts**.

Arvectum OS RFC-0001/RFC-0002 authority modes describe canonical responsibility for a governed object or representation:

- `Native`;
- `External Reference`;
- `Governed Replica`.

These modes must not be misread as corporate or organizational power.

### 5.1 Company governance record represented as `Native`

A Company-specific governance object may be stored as a `Native` Arvectum OS Canonical Record only when the Company has deliberately designated OS as the canonical system for that governed record type/scope **and** an applicable OS contract admits that representation.

In that case:

- OS is authoritative for the admitted canonical record/version, identity, provenance and lifecycle semantics within the declared scope;
- the Company remains the source of the organizational meaning and authority represented by that record;
- the record must preserve the attributable Company Principal/decision/delegation/policy that authorized the state;
- OS `Native` status does not create new legal or Organizational Authority;
- OS may reject a non-conforming mutation under its contracts, but it must not unilaterally rewrite the Company policy, delegation or decision semantics to make the record conform.

Example: a Company delegation approved by the competent Company authority may later be stored as a Native OS governance record. The delegation exists because the Company authority approved it, not because OS persisted it.

### 5.2 Legal/corporate facts and external authorities

Where an external legal, registry, banking, contractual or product system remains authoritative for an underlying fact, OS should use the applicable `External Reference` or `Governed Replica` model rather than creating competing truth.

OS may be authoritative for its reference/provenance/replica governance while the external source remains authoritative for the underlying fact scope.

### 5.3 Repository-first Company artifacts

During early Company development, a Company repository artifact may remain the canonical Company source while OS only references it or does not represent it at all.

Migration of such an artifact into OS canonical state is a separate governed change. It must identify:

- source authority;
- effective transition point;
- exact version admitted;
- migration/rollback behavior;
- whether the repository becomes historical evidence, a mirror, or continues as canonical source.

AC-002 does not pre-decide that migration; AC-003 and later implementation work must make the canonical home explicit per artifact class.

## 6. Translating Company authority into technical execution

The approved direction is:

`Company authority source → governed Company record/reference → technical authorization/enforcement → Governed Execution → evidence`

The reverse inference is prohibited.

### 6.1 Delegation example

A valid flow may be:

1. competent Company authority approves a bounded delegation;
2. the delegation is canonically recorded or referenced;
3. OS resolves the exact applicable delegation/version;
4. technical authorization grants only the permissions necessary to execute within that scope;
5. the workflow evaluates any separate approval/data-governance conditions;
6. Governed Execution performs the admitted operation;
7. evidence records actor, scope, material versions and result.

Invalid shortcuts include:

- `IAM role exists → therefore Company delegation exists`;
- `API token works → therefore actor may bind the Company`;
- `workflow succeeded → therefore approval was granted`;
- `AI recommended action → therefore authority exists`;
- `OS admin can change data → therefore admin owns the organizational decision`.

### 6.2 Revocation asymmetry

Revoking technical access must not erase historical evidence that an earlier action was validly authorized.

Granting technical access must not retroactively create authority for earlier actions.

Current permission and historical attribution are separate concerns.

## 7. When the Company may rely on Arvectum OS

Company reliance on OS is allowed only through an explicit, governed boundary appropriate to the interaction.

### 7.1 Product-mediated reliance

If a product or Product Experiment:

- consumes an OS Platform Capability;
- emits into shared OS governed history;
- reads or changes OS canonical platform state;

then the product must use the Product Contract boundary required by RFC-0001/RFC-0004.

The Product Contract must remain product/platform scope. It does not grant Company authority merely by existing.

### 7.2 Direct Company organizational reliance

AC-002 does **not** presume that an arbitrary internal Company workflow may bypass the RFC-0004 client/product/extension boundary merely because the Company owns Arvectum OS.

Direct Company use is permitted only where the current canonical OS contract explicitly admits the applicable platform-native administrative/governance operation for an Organization or authorized platform operator without requiring a Product Contract.

For ordinary Company operational workflows that consume a Platform Capability, emit governed shared history or read/change OS canonical state through a product, extension or other client boundary, the applicable RFC-0004 Product Contract requirement remains the default when triggered.

AC-002 does **not** invent a generic “Company Product Contract” or a new contract type. If the first real Company workflow cannot be expressed through an existing declared OS capability/operation boundary or an applicable Product Contract/extension contract, the Company must stop the governed reliance and open the minimum necessary OS governance/contract path before consequential use.

### 7.3 No private coupling

Company or product code must not rely on OS internals through:

- undocumented database tables;
- private imports;
- incidental log formats;
- private event streams;
- cache structure;
- undeclared implementation-specific APIs;
- administrator shortcuts.

Any such dependency is hidden coupling and must be removed, explicitly governed as a temporary exception, or promoted through the applicable OS contract path.

## 8. Governed Execution requirements for Company consequential work

When a Company workflow uses OS for consequential canonical change or external-effect preparation/execution, the applicable path must preserve the separation of:

- Identity;
- authentication evidence;
- technical Authorization;
- Company Organizational Authority;
- data-governance permission;
- validation;
- consequential approval where required;
- execution/enforcement.

### 8.1 Minimum execution evidence

Proportionate to consequence, the execution should be able to identify or resolve:

- explicit Company Organization scope;
- actual Actor/Principal;
- applicable Position/Assignment where modeled;
- exact effective Company authority/delegation/policy version materially relied upon;
- applicable Product Contract or other declared OS contract boundary;
- exact Workflow version where relevant;
- material inputs and authoritative sources;
- separate approval evidence where required;
- model/software/runtime references where materially relevant;
- result, side-effect class and required event/provenance evidence.

### 8.2 Fail-closed rule

If a consequential operation cannot determine the applicable Organization, authority source, contract boundary or required approval with sufficient certainty, it must stop, fail closed or escalate rather than infer broader authority.

### 8.3 Proportionality

AC-002 does not require every read, transient calculation or low-risk internal step to become a heavy governance record.

Controls and evidence remain proportionate to consequence, external effect, data sensitivity, reversibility and reconstruction need.

## 9. Cross-repository change paths

### 9.1 Company change that does not require OS change

If a Company policy, Position, workflow or decision can be represented using existing OS contracts without changing their meaning:

- make the Company change in the Company governance path;
- update exact references/versions used by the applicable workflow;
- do not modify OS merely to mirror Company wording.

### 9.2 Company need that requires OS change

If the Company needs platform behavior not admitted by current OS contracts:

1. record the Company requirement/business need in the Company scope;
2. identify whether it is Company-specific, product-specific or genuinely domain-neutral;
3. keep Company-specific behavior out of shared OS;
4. if a domain-neutral OS change is justified, propose it through the applicable OS RFC/ADR/capability/Product Contract path;
5. do not describe the requested OS change as committed until OS governance accepts it;
6. use a reversible Company/product-local fallback where economically justified while the OS path is unresolved.

A Company roadmap item or Owner priority does not automatically amend an OS RFC, contract or capability lifecycle.

### 9.3 OS change affecting Company reliance

An OS change does not automatically change Company Organizational Authority or business policy.

When an OS contract/version materially affects Company reliance, the Company must:

- evaluate compatibility and migration impact;
- pin or migrate exact versions according to the applicable contract;
- re-evaluate affected security/data/authority assumptions;
- update Company workflows/references where required;
- suspend or de-platformize the affected path if safe reliance cannot be preserved.

### 9.4 Product change affecting Company portfolio

Product implementation changes remain in the product repository.

The Company repository records only material portfolio consequences such as:

- accountability;
- investment/cost boundary;
- material dependency;
- risk/obligation;
- continue/change/stop decision.

It must not duplicate the product roadmap or implementation history.

### 9.5 Paired decisions

A cross-repository change may require separate durable decisions in more than one repository.

Approval in one scope does not silently approve another scope. Where both Company and OS commitments change, each repository must preserve its own applicable decision/contract evidence and cross-reference the other where useful.

### 9.6 Commercial and lifecycle integrity across the boundary

A Company commercial commitment that relies on Arvectum OS must remain truthful about the current OS lifecycle, conformance, compatibility, support and operational-readiness state.

The Company must not:

- market an OS Product Experiment, `Candidate` or `Incubating` capability as an `Active` supported platform capability;
- create a stable OS compatibility, portability, support or operational obligation that OS governance has not approved;
- use a Company contract or sales promise to bypass an OS Product Contract or lifecycle boundary.

The Company may choose to accept its own business risk around a bounded internal or customer pilot only within competent Company authority and accurate external representation. That acceptance does not create a new OS obligation unless the applicable OS authority separately approves it.

## 10. Conflict and reconciliation rules

### 10.1 Legal/corporate conflict

If an internal Company or OS representation conflicts with applicable legal/corporate authority:

- do not execute the conflicting consequential action;
- treat the legal/corporate source as controlling within its scope;
- record the discrepancy proportionate to consequence;
- reconcile the Company/OS representation through the proper change path.

### 10.2 Company Constitution vs subordinate Company artifact

The Ratified Company Constitution prevails over ordinary Company policies, roadmaps and workflows within Company-specific internal governance scope unless amended through its own constitutional process.

### 10.3 Company rule vs mandatory OS contract

Company and OS are not related by one universal hierarchy.

If a Company workflow conflicts with a mandatory OS invariant or contract required for that workflow’s chosen OS reliance, the Company must choose one of the following:

- change the Company workflow;
- stop or defer the OS-backed path;
- use an approved alternative/fallback;
- pursue an OS governance change through the proper OS path.

The Company must not bypass OS contracts, and OS must not reinterpret Company authority to make the conflict disappear.

### 10.4 Product vs Company conflict

Company portfolio authority may decide whether a product continues, receives investment or must satisfy a Company risk/authority boundary.

Product-specific implementation truth remains in the product repository. If Company and product artifacts disagree on implementation state, the product canonical source governs that fact until explicitly reconciled.

### 10.5 Technical configuration conflict

Technical configuration never overrides higher authority by implication.

Examples:

- an overly broad permission does not expand Company delegation;
- a restrictive permission may block valid authority operationally, but does not revoke the underlying organizational decision unless the Company authority changes;
- a stale cache or projection does not become canonical truth.

### 10.6 Snapshot conflict

Convenience snapshots, ChatGPT Project Sources, generated summaries and model memory are non-canonical retrieval aids. Current canonical originals win when conflict exists.

## 11. Security, data and sovereignty boundary

Company use of OS inherits applicable OS security/privacy/sovereignty invariants and adds Company-specific controls where required.

At minimum:

- access is deny-by-default and least privilege;
- Organization scope must be explicit for governed or sensitive state;
- customer/partner data does not become shared Company or platform learning automatically;
- cross-Organization reuse requires explicit rights, purpose, classification and governance;
- secrets and reusable credentials must not be stored in ordinary canonical history, prompts or repositories merely for convenience;
- OS administrator capability must not imply unrestricted business-content authority;
- derived data and AI context inherit applicable handling constraints;
- failure must not silently broaden access or cross Organization boundaries;
- emergency/break-glass technical access may bypass ordinary authorization only through an explicitly governed, attributable, time-bounded and reviewable mechanism and must not create permanent Company delegation or Organizational Authority by implication.

Technology sovereignty remains a Company responsibility as an adoption/investment decision even where OS provides portability/security mechanisms.

OS can provide portable contracts and export mechanisms; the Company decides whether a concrete external dependency is acceptable for its market, risk appetite, jurisdictional exposure, availability and replacement strategy.

## 12. Continuity, portability and de-platformization

Arvectum OS is a strategic platform, but it remains a replaceable technology and execution foundation rather than the source of Company existence or authority.

For Company-critical OS reliance, the Company must be able to understand, proportionate to risk:

- which Company organizational assets are stored or referenced through OS;
- how identities, versions, authority records, workflows, decisions and evidence can be exported or reconstructed;
- which external authorities remain outside OS;
- how credentials/secrets are replaced rather than assumed exportable;
- how an affected workflow can pause, degrade, revert to manual/product-local execution or migrate;
- what history remains necessary after de-platformization.

De-platformization does not mean rewriting valid historical evidence. It means preserving lawful organizational meaning/history while stopping future dependency on the affected OS path.

## 13. Business-first adoption rule

Company use of OS must create enough value to justify its integration and governance cost.

A Company workflow should not move into OS merely because OS can represent it.

Before material reliance, the Company should identify at least one concrete expected benefit such as:

- lower owner workload;
- safer delegation;
- improved reconstruction/explainability;
- lower integration cost across products;
- better continuity/portability;
- reduced security/governance risk;
- reusable organizational knowledge/workflow capability.

If the platform path materially increases cost, delay or operational fragility without compensating value, the Company may keep the workflow local, simplify the boundary or de-platformize it, subject to any existing contractual/history obligations.

## 14. Minimal pre-reliance checklist

Before a new Company workflow materially relies on Arvectum OS, confirm:

1. **Ownership:** Is this Company, Product or OS scope?
2. **Business purpose:** What measurable value or control need justifies OS reliance?
3. **Authority:** What Company authority/delegation/approval governs the action?
4. **Legal basis:** Does any external effect require legal/corporate authority beyond internal governance?
5. **Contract boundary:** Which Product Contract, capability contract or other declared OS boundary applies?
6. **Canonical source:** What is authoritative for each material fact/policy/object?
7. **Organization/data scope:** Which Organization, classification, purpose and rights apply?
8. **Execution:** Does consequence require Governed Execution and exact version pinning?
9. **Evidence:** What must be reconstructable, and what sensitive data should not be retained?
10. **Failure:** What happens if authority, dependency or outcome is uncertain?
11. **Fallback:** Can the Company pause, revert, migrate or execute manually?
12. **Cross-repo effect:** Does another repository need a separate approved change?

A “yes” to OS technical availability is never a substitute for these questions where they are materially relevant.

## 15. Deferred questions and non-blocking follow-up

The following questions remain deliberately unresolved because deciding them now would pre-empt later Company or OS work without evidence:

### 15.1 Canonical home for each Company artifact class

Whether a Position, Assignment, Company policy, decision, workflow or knowledge asset is initially canonical in Git, in Arvectum OS, or represented through a hybrid reference model belongs to `AC-003` and later implementation evidence.

### 15.2 Detailed Company decision authority matrix

Reserved Owner Decisions and delegated Position authority limits belong to `AC-202` and `AC-203`.

AC-002 only establishes that OS must represent/enforce the effective Company authority rather than invent it.

### 15.3 Company-native OS client pattern

The first real direct Company workflow may reveal whether current OS capability contracts are sufficient for a non-product internal Company client or whether a minimal explicit extension/Product Contract-equivalent pattern is needed.

No new generic contract type is created by AC-002. Until canonical OS contracts explicitly admit such a non-product operational client, ordinary consequential Company use must not assume that path exists; it should use an admitted product/extension/client boundary or wait for the applicable OS governance decision.

### 15.4 Concrete identity/tenant/IAM implementation

How ООО «Арвектум», Company Positions, human Principals, service Principals and AI-mediated actors map into the concrete runtime belongs to later Company data/access and OS implementation work.

These deferred questions do **not** block `AC-003` because AC-003 can define canonical repository homes and artifact classes without selecting the later runtime implementation.

## 16. Boundary invariants

The following invariants summarize AC-002:

1. **Company authority originates in applicable legal/corporate and Company governance sources, not in OS.**
2. **OS may represent and enforce Company authority, but technical access cannot create it.**
3. **OS canonical authority mode is not the same thing as corporate or Organizational Authority.**
4. **Company owns Company-specific organizational meaning; OS owns domain-neutral platform contracts; products own product/domain implementation semantics.**
5. **Company-specific behavior does not enter shared OS without the applicable OS governance path.**
6. **Product/Company reliance on OS uses declared contracts and Governed Execution rather than private coupling.**
7. **One repository cannot create a hidden obligation in another repository.**
8. **A change in OS does not silently change Company authority; a Company decision does not silently amend OS.**
9. **Security, Organization isolation, data rights and portability remain mandatory across the boundary.**
10. **OS reliance is justified by business value and remains reversible where practicable.**
11. **AI, software, models and runtimes remain executors, not authority sources.**
12. **When authority or outcome is uncertain, consequential execution fails closed or escalates rather than inferring permission.**
13. **Company commercial commitments cannot silently create unsupported OS lifecycle, compatibility, support or conformance obligations.**

## 17. Acceptance criteria

AC-002 is ready for acceptance when all are true:

- the artifact is consistent with the Ratified Company Constitution `1.0.0`;
- the current canonical Arvectum OS Constitution/RFC state has been re-checked;
- legal/corporate authority remains separate from internal Organizational Authority and technical authorization;
- Company/OS/Product responsibility boundaries are explicit;
- Product Contract and Governed Execution reliance is conditional on the applicable OS contract rather than invented by Company;
- cross-repository change and conflict paths are explicit;
- no hidden cross-repository commitment is created;
- deferred questions are bounded and do not block AC-003;
- functional cross-review reaches material consensus or the maximum ten iterations;
- the Owner/competent Principal explicitly approves the final proposal before it becomes binding Company governance.

All acceptance criteria are satisfied. Owner approval is recorded in `docs/governance/decisions/DECISION-2026-08-20-AC-002-APPROVAL.md`, and this artifact is binding Company governance as `Approved 1.0.0` within its declared scope.

## 18. Source baseline checked for this proposal

### Arvectum Company

- `arvectum/arvectum-company` main checked before drafting at commit `9b4651755c88eec1f462749b84261874c56b4d68`;
- `docs/constitution/COMPANY-CONSTITUTION.md` — Ratified `1.0.0`;
- `docs/roadmap/ROADMAP.md` — AC-002 was Current at proposal drafting;
- `docs/CANONICAL-SOURCES.md` — Company/OS/legal authority registry.

### Arvectum OS

Current canonical state was re-checked before drafting:

- `arvectum/arvectum-os` main observed at commit `a5e6c15f735b85e952f646c885a3e5f019594276`;
- Constitution remains Ratified `1.2.0`;
- RFC-0001…RFC-0008 remain Accepted `1.0.0` within their declared scopes;
- RFC-0001 and RFC-0003 canonical blobs used by this boundary remain unchanged from the current Project Source pack;
- `docs/governance/DECISION-AUTHORITY-POLICY.md` remains `Proposed 0.2.1` and is therefore non-binding.

Later OS roadmap/recovery work does not become a Company commitment merely because it occurred after the Project Source snapshot.

### Legal/corporate baseline

The private owner-managed source set recorded in `docs/CANONICAL-SOURCES.md` confirms the Company is an existing ООО operating under Типовой устав №23 with one participant and a General Director/sole executive body at the verified baseline.

No personal identifiers, signatures, tax identifiers, addresses or banking data are copied into this public governance artifact.

---

**Approved conclusion:** Arvectum OS is the governed execution/platform substrate for organizational meaning; it is not the sovereign source of that meaning. Arvectum Company remains the source of its Company-specific organizational authority and business policy, while OS provides domain-neutral contracts to represent, constrain, execute and reconstruct that authority without silently creating or changing it.
