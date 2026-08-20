# AC-003 — Canonical Repository Structure and Artifact Map Cross-Review

Status: `Complete`
Review date: `2026-08-20`
Iterations completed: `7 of maximum 10`
Result: `PASS — material consensus reached; explicit Owner approval still required`
Reviewed artifact: `docs/governance/CANONICAL-REPOSITORY-STRUCTURE.md` — Proposed `0.9.0`
Reviewed proposal blob SHA: `2e6c70848beb3adcf9856a23fae2d26c0e20ff0e`
Repository branch: `ac-003-canonical-repository-map`
Owner decision: `Pending`

## 1. Review purpose

This review tests AC-003 from the perspective of the Owner and the full set of executive-management functions needed to challenge the proposed repository structure before it becomes binding Company governance.

As in AC-001 and AC-002, most executive labels below are **functional review lenses only**. They do not create Positions, appointments, employment relationships, departments, committees, delegations or Organizational Authority before the Company operating model is established under later roadmap items.

The legally existing General Director capacity is distinct from simulated executive lenses. The simulated `Owner` lens is also not actual Owner approval. Final approval remains a separate explicit act by the real competent Principal against the exact final proposal.

## 2. Canonical and authority baseline checked before review

### Arvectum Company

- canonical repository: `arvectum/arvectum-company`;
- `main` checked before drafting at `4490b3ca19d83908d7303cc1be69df46ed8bdc50`;
- `docs/constitution/COMPANY-CONSTITUTION.md` — Ratified `1.0.0`;
- `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md` — Approved `1.0.0`;
- `docs/roadmap/ROADMAP.md` — `AC-003` is `Current`;
- `docs/CANONICAL-SOURCES.md` — Active `0.4.0`;
- repository visibility observed as public;
- current tree contains Constitution, governance/decisions, roadmap, reviews, Project Source snapshots, helper tools and GitHub/GitVerse mirror automation.

### Arvectum OS

The current OS repository was checked before review to ensure AC-003 does not invent an OS boundary:

- canonical repository: `arvectum/arvectum-os`;
- observed current `main` HEAD: `bbc58231ef513e825cdf733216305816750f1de2`;
- Constitution `1.2.0` and Accepted RFC-0001 through RFC-0008 remain the controlling platform architecture within their scopes;
- recent observed OS movement is roadmap/implementation work and does not transfer OS canonical responsibilities into the Company repository.

The review relies particularly on the existing separation already established by AC-001/AC-002: Company owns concrete organizational semantics; OS owns domain-neutral platform contracts/capabilities; product repositories own product-specific implementation; AI/software execution does not create Organizational Authority.

### Legal/corporate source baseline

The Company source registry already establishes that legal/corporate originals are owner-managed external authorities and should not be copied into the public repository by default when they contain personal data, signatures, tax identifiers, addresses, banking data or other unnecessary sensitive content.

AC-003 therefore treats the repository as a canonical home only for **repository-suitable** Company artifacts and explicitly preserves external canonical sources where appropriate.

## 3. Review lenses

The cross-review used the same full-management functional panel as AC-002:

1. Owner / Founder / residual authority and capital;
2. General Director / current executive management and external representation;
3. Finance / capital, accounting adjacency, budgets and commitments;
4. Operations / workflow execution, usability, continuity and failure handling;
5. Product & Portfolio / portfolio authority and product-repository boundaries;
6. Technology & Architecture / canonical source, repository and OS boundary;
7. Commercial / customer/supplier confidentiality and external commitments;
8. Legal & Compliance / legal/corporate records, personal data and authority separation;
9. Security & Data / secrets, repository visibility, retention and access risk;
10. People & Organization / Position, Assignment and personnel-data boundaries;
11. Risk & Continuity / source-of-truth conflict, hosting failure, rollback and recovery.

## 4. Iterative review record

### Iteration 1 — Repository as canonical governance home vs repository as universal database

**Primary lenses:** Owner, Technology & Architecture, Operations, General Director.

**Material criticism:**

- the phrase “canonical repository structure” could be interpreted as requiring every Company fact, contract, payment, execution, incident and future OS record to live in Git;
- that would create operational friction, security exposure and competing sources of truth with legal, accounting, product and OS systems;
- conversely, leaving “canonical home” undefined would allow important Company artifacts to remain scattered across chats and local files.

**Reconciliation incorporated:**

- the proposal defines this repository as canonical for durable **repository-suitable** Company governance, planning, portfolio, organizational-model and operating-model artifacts;
- it explicitly states that canonical home is a responsibility decision, not a storage slogan;
- legal, accounting, banking, customer, personnel, high-volume runtime and product/OS records may remain externally canonical;
- safe locators/references may be stored without creating competing authority;
- one-artifact/one-canonical-home and explicit migration rules were added.

**Result:** core source-of-truth ambiguity resolved; continue.

### Iteration 2 — Public repository, sensitive data and irreversible Git history

**Primary lenses:** Security & Data, Legal & Compliance, Finance, Commercial, People & Organization.

**Material criticism:**

- the repository is public, while future Company work naturally produces bank, customer, supplier, personnel, contract and incident data;
- a directory map without a hard admission boundary could invite accidental publication;
- deleting a committed secret later would not remove it from Git history;
- making the repository private in the future could be misread as blanket permission to store any sensitive material in Git.

**Reconciliation incorporated:**

- a dedicated public-repository safety boundary was made normative;
- secrets, reusable credentials, unnecessary personal identifiers, signatures, bank/payment details, non-public commercial/customer/supplier content, personnel files and sensitive incident payloads are excluded by default;
- future private visibility explicitly does not waive classification, retention, access or need-to-store analysis;
- accidental-secret handling requires containment/rotation and history remediation as applicable;
- legal/corporate originals remain owner-managed external authorities by default.

**Result:** material confidentiality/security objection resolved; continue.

### Iteration 3 — Company vs Product vs Arvectum OS canonical ownership

**Primary lenses:** Product & Portfolio, Technology & Architecture, Owner, Operations.

**Material criticism:**

- a broad Company tree could start absorbing product source code, product roadmaps, product workflows or OS contracts simply because Company “owns the business”;
- Project Source snapshots under this repo could be mistaken for canonical OS documents;
- a Company need could accidentally become an implied OS commitment;
- product/OS operational state could be duplicated into Git as “evidence” and later diverge.

**Reconciliation incorporated:**

- the artifact adds explicit Company/Product/OS ownership sections;
- product implementation and product roadmaps remain in product repositories;
- OS architecture/contracts remain in `arvectum/arvectum-os`;
- `docs/project-sources/` remains convenience-only and must identify canonical originals;
- cross-repository needs do not create commitments without the applicable governance path in each repository;
- operational runtime evidence stays in the system responsible for it unless a safe, purposeful summary/reference is sufficient.

**Result:** repository-boundary objection resolved; continue.

### Iteration 4 — Filesystem completeness vs business-first usability

**Primary lenses:** Operations, Owner, Finance, Technology & Architecture.

**Material criticism:**

- creating dozens of empty folders, registries and policy categories now would reproduce the “fake headcount” problem as fake filesystem architecture;
- forcing every future artifact into a rigid enterprise taxonomy before real work exists would make the owner maintain ceremony instead of the business;
- at the same time, AC-003 must be concrete enough to prevent future placement ambiguity.

**Reconciliation incorporated:**

- the proposal distinguishes **logical structure** from physically materialized directories;
- directories are created only when the first real artifact of that class exists;
- no empty placeholders are required because Git does not track them usefully;
- the map uses a small set of stable domains: governance, roadmap, portfolio, business, organization, operations, security, management, reviews and convenience sources;
- more elaborate naming or departmental trees are explicitly deferred until real repository growth justifies them.

**Result:** practicality/ceremony objection resolved; continue.

### Iteration 5 — Organizational authority, legal authority and personnel records

**Primary lenses:** People & Organization, General Director, Legal & Compliance, Owner.

**Material criticism:**

- placing `Positions`, `Assignments` and `delegations` in one undifferentiated directory could imply that an internal assignment creates legal authority to represent the LLC;
- Assignment records may later contain personal or contract data inappropriate for a public repository;
- Reserved Owner Decisions and delegation architecture are more governance-sensitive than ordinary org-chart information;
- the map must not pre-create executive Positions by naming executive review lenses.

**Reconciliation incorporated:**

- Reserved Owner Decisions and authority models are mapped to `docs/governance/`;
- function/Position/organizational models are mapped to `docs/organization/`;
- explicit internal delegations have a dedicated governance home when needed, while powers of attorney/corporate legal acts remain separate legal artifacts;
- Assignment records may move to an approved private/governed store when personal/sensitive data requires it;
- review lenses are explicitly non-positions and non-delegations.

**Result:** authority/personnel boundary resolved; continue.

### Iteration 6 — Finance, management records, runtime state and continuity across hosts

**Primary lenses:** Finance, Risk & Continuity, Operations, Security & Data, Commercial.

**Material criticism:**

- later M1/M4 work will need real cash, commitments, risk and obligation data; putting live figures in public Markdown is unsafe and operationally weak;
- management dashboards must not become competing authorities for accounting/product/runtime facts;
- GitHub and GitVerse mirror automation could be interpreted as dual canonical remotes, creating conflict after an outage;
- portability requires a recovery path without silently switching authority.

**Reconciliation incorporated:**

- `docs/business/` and `docs/management/` are homes for durable **models/specifications** and public-safe baselines, while sensitive live records may remain in appropriate private/accounting/operational stores;
- management views are defined as projections over underlying canonical sources, not independent authorities;
- GitHub is explicitly the current canonical remote and GitVerse the non-authoritative mirror;
- emergency host promotion requires an attributable decision, source commit and reconciliation path;
- vendor hosting must not own Company Organizational Authority or the only copy of critical history.

**Result:** finance/continuity objection resolved; full-panel convergence required.

### Iteration 7 — Full-management convergence, roadmap coverage and contradiction check

**Primary lenses:** all 11 review lenses.

**Checks performed:**

- repository-suitable canonical Company artifacts vs external systems of record;
- public visibility vs future sensitive business records;
- legal/corporate authority vs internal governance files;
- Position/Assignment/delegation semantics vs legal representation;
- Company repository vs product repositories;
- Company repository vs Arvectum OS canonical state and contracts;
- roadmap planning vs actual authority/approval;
- durable specifications vs high-frequency runtime records;
- Git history/version evidence vs current effective version identification;
- README/project-source convenience material vs canonical documents;
- GitHub canonical remote vs GitVerse mirror/recovery;
- filesystem simplicity vs future findability;
- current AC-101–AC-707 roadmap items vs proposed artifact homes;
- AI/generated review evidence vs real Owner approval.

**Result:** no remaining material contradiction was identified.

The remaining questions — concrete Reserved Owner Decisions, authority thresholds, Position/Assignment schemas, data access matrix, operational registers, live financial storage and first real OS-backed Company workflow — are correctly deferred to later roadmap items. Resolving them in AC-003 would create speculative governance or storage commitments without evidence.

**Stop:** iteration `7/10` because further changes would be terminology/style refinements or work belonging to later roadmap items.

## 5. Final perspective matrix

| Review lens | Final result | Main condition preserved |
|---|---|---|
| Owner | PASS | one discoverable Company governance home without turning Git into the Company database |
| General Director | PASS | internal repository artifacts do not replace legally required executive/corporate acts |
| Finance | PASS | live sensitive financial/accounting truth may remain in appropriate private authoritative systems |
| Operations | PASS | logical map is usable and directories are created on demand rather than ceremonially |
| Product & Portfolio | PASS | Company portfolio authority is separated from product implementation and product roadmaps |
| Technology & Architecture | PASS | one-canonical-home rule, migration rules and Company/Product/OS boundaries are explicit |
| Commercial | PASS | customer/supplier confidential material is excluded from the public repository by default |
| Legal & Compliance | PASS with supremacy condition | applicable legal/corporate authority and external legal originals remain controlling within scope |
| Security & Data | PASS | secrets/sensitive payload are excluded; Git-history and visibility risks are explicit |
| People & Organization | PASS | Position/Assignment/delegation homes preserve executor/authority distinctions and privacy needs |
| Risk & Continuity | PASS | GitHub/GitVerse roles are unambiguous and recovery requires explicit reconciliation |

## 6. Deliberate deferrals are not review failures

The following remain later work:

- `AC-004` — initial `docs/portfolio/PORTFOLIO.md`;
- `AC-005` — founding baseline cross-review and closure;
- `AC-101–AC-106` — real business/economic baseline;
- `AC-202/203` — Reserved Owner Decisions and delegated authority model;
- `AC-204/205` — Position Registry and Assignments;
- `AC-206/207` — access boundary and continuity/fallback baseline;
- `AC-401–AC-407` — live management control models and Mission Control;
- `AC-501+` — first real governed Company workflow and runtime evidence;
- selection of a private operational record store if and when real data/workflow needs justify it.

## 7. Cross-review conclusion

AC-003 reached material management consensus at the **proposal** level after seven iterations.

The proposal is suitable for Owner decision because it:

- establishes one canonical Company repository role without claiming universal storage authority;
- protects the current public repository from obvious sensitive-data classes;
- preserves legal/corporate, Product and Arvectum OS boundaries;
- provides a concrete artifact map for the full current roadmap while avoiding empty speculative structure;
- distinguishes durable governance/specification artifacts from live operational records;
- makes GitHub/GitVerse source-of-truth behavior explicit;
- preserves explicit approval as the source of binding governance rather than AI review or merge mechanics.

Cross-review result:

`PASS — MATERIAL CONSENSUS REACHED AT ITERATION 7/10`

No Owner approval is inferred from this review.

## 8. Required next decision

To close AC-003, the Owner must explicitly approve the exact proposal:

- `docs/governance/CANONICAL-REPOSITORY-STRUCTURE.md`;
- status/version: `Proposed 0.9.0`;
- blob SHA: `2e6c70848beb3adcf9856a23fae2d26c0e20ff0e`.

If approved, the publication sequence should:

1. create the Owner decision record referencing the exact approved proposal blob;
2. publish the artifact as `Approved 1.0.0` without changing approved normative substance;
3. update `README.md` as the repository entry point;
4. register AC-003 and its decision in `docs/CANONICAL-SOURCES.md`;
5. mark AC-003 `Complete / PASS` and advance AC-004 to `Current` in `docs/roadmap/ROADMAP.md`;
6. perform read-after-write verification;
7. merge the AC-003 branch only after the approval evidence exists.
