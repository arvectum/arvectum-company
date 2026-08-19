# AC-001 — Company Constitution / Founding Charter Cross-Review

Status: `Complete`
Review date: `2026-08-19`
Iterations completed: `6 of maximum 10`
Result: `PASS — material consensus reached; only explicit Owner ratification remains`
Reviewed artifact: `docs/constitution/COMPANY-CONSTITUTION.md` — Proposed `0.9.0`
Repository branch: `ac-001-company-constitution`

## 1. Review purpose

This review tests the AC-001 Company Constitution / Founding Charter proposal from the perspective of the Owner and the executive functions that a viable Arvectum Company must eventually cover.

The role labels in this review are **functional review lenses only**. Except for legally existing corporate roles evidenced by current corporate documents, they do not create Positions, appointments, delegations, employment relationships, committees or Organizational Authority. This prevents the review itself from creating fake headcount before the operating model is defined under later roadmap items.

The simulated `Owner` lens also does **not** constitute actual Owner approval. Ratification remains a separate explicit act by the real Owner/competent Principal against the exact proposal text.

## 2. Canonical and authority baseline checked before review

### Arvectum Company

- canonical repository: `arvectum/arvectum-company`;
- reviewed Company baseline before AC-001 work: `main` at `f2dd30a6a0d1910bc7db3628d538b22ab95b435f`;
- `docs/roadmap/ROADMAP.md` identifies AC-001 as the current Company action;
- `docs/CANONICAL-SOURCES.md` records the applicable source hierarchy and legal/corporate baseline.

### Arvectum OS

Current canonical repository state was re-checked before drafting:

- canonical repository: `arvectum/arvectum-os`;
- `main` HEAD: `de59771281ce1b4c58d943bd003560384e332270`;
- Constitution: Ratified `1.2.0`;
- RFC-0001 through RFC-0008: Accepted `1.0.0` within their declared scopes;
- `DECISION-AUTHORITY-POLICY.md`: still `Proposed 0.2.1`, therefore used only as design reference and not as binding OS policy.

No later OS commit was found beyond the source-registry baseline that would require AC-001 reconciliation.

### Legal/corporate source baseline

The private source set confirms, at the level needed for this internal governance artifact:

- ООО «Арвектум» operates under Типовой устав №23;
- the Company has one participant;
- current corporate governance includes a general director as the sole executive body;
- the founding and registry documents remain authoritative evidence for the corporate facts within their scope.

AC-001 deliberately does not restate personal identifiers, signatures, tax identifiers, addresses or banking data in the public repository.

The legal review principle is therefore: **internal governance may organize work and decision boundaries, but it cannot create legal authority that applicable law, the charter, corporate decisions, powers of attorney or contracts do not provide.**

## 3. Review lenses

The cross-review used the following perspectives:

1. Owner / Founder / capital and residual authority;
2. General Director / current executive management and external representation;
3. Financial management / capital allocation, cash and commitments;
4. Operations / delivery, continuity and recoverability;
5. Product & Portfolio / product ownership and investment discipline;
6. Technology & Architecture / Company↔OS boundary and replaceability;
7. Commercial / customer promises, sales and external commitments;
8. Legal & Compliance / corporate/legal authority and regulatory boundary;
9. Security & Data / access, secrets, privacy, sovereignty and isolation;
10. People & Organization / Positions, Assignments, accountability and anti-fake-headcount;
11. Risk & Continuity / downside, exceptions, emergency and fallback.

## 4. Iterative review record

### Iteration 1 — Foundation, legal authority and Owner control

**Primary lenses:** Owner, General Director, Legal & Compliance.

**Material criticism:**

- the document must not become a second legal charter or imply that internal `Owner approval` is automatically a corporate act;
- `Owner`, participant, General Director, Position and Principal must remain distinguishable even if one person currently holds several capacities;
- Company governance, Arvectum OS governance and product governance require scoped authority rather than one flattened hierarchy;
- constitutional authority must not be inferred from roadmap/chat/model memory.

**Reconciliation incorporated into proposal:**

- Article 0 explicitly establishes internal-only status and legal limits;
- Articles II and III separate legal/corporate authority from internal Organizational Authority;
- Company↔OS↔Product authority is expressed as scoped responsibility plus reconciliation, not as an incorrect universal ranking;
- explicit Owner ratification is required before the Constitution becomes binding internally.

**Result:** material objections resolved; continue review.

### Iteration 2 — Organization, delegation and owner-bottleneck risk

**Primary lenses:** Operations, People & Organization, Owner, Risk.

**Material criticism:**

- a Constitution for an AI-native company can easily degenerate into an org chart of invented agents;
- Position must survive replacement of humans/AI/runtimes;
- technical permissions and job titles must not silently create Organizational Authority;
- preserving Owner control must not mean routing every routine decision to the Owner;
- assignment and delegation need revocability, scope and escalation semantics.

**Reconciliation incorporated into proposal:**

- Article V fixes `Position → Principal → Assignment → Runtime → Governed Execution` as the organizational sequence;
- Position creation requires real business responsibility/workload/control/economic value;
- Article VI requires explicit, attributable, bounded and revocable delegation;
- absence of authority fails closed or escalates instead of silently broadening permission;
- Article XVII makes anti-bureaucracy and removal of routine Owner bottlenecks constitutional principles.

**Result:** material objections resolved; continue review.

### Iteration 3 — Economics, portfolio and customer commitments

**Primary lenses:** Financial management, Product & Portfolio, Commercial, Owner.

**Material criticism:**

- an AI-native constitution must be explicitly economic, not merely architectural;
- technical success must not be confused with profitability, compliance or customer readiness;
- portfolio initiatives need hypotheses, cost/risk boundaries and stop criteria;
- sales/product/technical teams must not create unsupported customer obligations;
- expenditure capacity and payment capability are not the same as financial authority.

**Reconciliation incorporated into proposal:**

- Article IV makes business value, obligations, revenue/cash, unit economics, scalability, reversibility and Owner workload explicit decision inputs;
- Articles VIII and XIII separate commercial/external commitments from technical capability and enforce authority/risk/budget boundaries;
- Article IX defines portfolio governance as investment discipline rather than repository accumulation;
- sunk cost and technical attractiveness are explicitly rejected as automatic continue criteria.

**Result:** material objections resolved; continue review.

### Iteration 4 — Technology, security, data and sovereignty

**Primary lenses:** Technology & Architecture, Security & Data, Risk, Legal & Compliance.

**Material criticism:**

- the Company Constitution must not duplicate Arvectum OS RFC semantics or make the Company repository a shadow platform specification;
- external AI/cloud/tool providers must not own canonical organizational state or become irreplaceable authority sources;
- security, data rights, cross-customer reuse, secrets and portability require constitutional constraints because they can create existential dependency or liability;
- Russia-first operations require sovereignty/availability analysis without hard-coding one vendor stack.

**Reconciliation incorporated into proposal:**

- Article X defines a high-level Company↔OS responsibility boundary while deferring platform details to canonical OS sources;
- Article XII establishes least privilege, secret handling, explicit data-use rights and technology-sovereignty review;
- Article XIV requires proportional portability, restore/re-bootstrap, replacement and degraded/manual fallback paths;
- customer/partner data does not automatically become shared Company/OS learning.

**Result:** material objections resolved; continue review.

### Iteration 5 — Evidence, learning, emergency and operational practicality

**Primary lenses:** Operations, Risk & Continuity, Product, Owner, Technology.

**Material criticism:**

- a governance system that records everything can become more expensive than the risk it controls;
- an evidence-driven company still needs emergency handling and temporary exceptions;
- incidents, workarounds and AI suggestions are evidence, not automatic policy changes;
- the Constitution must support reversible learning and the ability to stop products, processes or agents that do not create value;
- business-critical functions need fallback without requiring premature enterprise infrastructure.

**Reconciliation incorporated into proposal:**

- Article XI requires evidence proportional to consequence and rejects indiscriminate sensitive-data retention;
- Article XV establishes the governed organizational learning loop;
- Article XVI permits bounded exception and break-glass behavior with attribution and post-event review;
- Articles XIV and XVII require continuity proportionate to business criticality while rejecting architecture/governance ceremony for its own sake.

**Result:** material objections resolved; full-panel convergence review required.

### Iteration 6 — Full-panel convergence and contradiction check

**Primary lenses:** all 11 review lenses.

**Checks performed:**

- Owner control vs General Director/legal authority;
- delegation vs reserved authority;
- automatic execution vs human/corporate approval;
- Company Constitution vs Arvectum OS Constitution/RFCs;
- product autonomy vs shared platform responsibility;
- business-first speed vs security/governance discipline;
- evidence/reconstructability vs privacy/minimization;
- technology sovereignty vs practical use of external vendors;
- continuity vs excessive infrastructure;
- owner visibility vs owner operational bottleneck;
- AI-enabled execution vs fake headcount and AI-as-authority.

**Result:** no remaining material contradiction was identified. Remaining potential edits are stylistic, terminology-level or belong to later subordinate artifacts. Under the requested stop condition, another review iteration is not justified.

**Stop:** iteration `6/10` because additional changes would be non-material.

## 5. Final perspective matrix

| Review lens | Final result | Main condition preserved |
|---|---|---|
| Owner | PASS for proposal | residual authority preserved; simulated review is not actual ratification |
| General Director | PASS | legal executive authority and external representation are not replaced by internal governance |
| Financial management | PASS | cash, cost, commitments, risk and authority are explicit |
| Operations | PASS | bounded delegation, fallback, emergency and owner-bottleneck reduction are supported |
| Product & Portfolio | PASS | products remain product-owned; portfolio decisions are economic and evidence-driven |
| Technology & Architecture | PASS | Company/OS boundary and replaceability are explicit without duplicating OS architecture |
| Commercial | PASS | customer-facing commitments require sufficient authority and approved boundaries |
| Legal & Compliance | PASS with standing supremacy condition | law, charter, corporate decisions, powers of attorney and contracts prevail in their scope |
| Security & Data | PASS | least privilege, secrets, data-use rights, isolation and sovereignty are structural |
| People & Organization | PASS | Position is durable; assignments/runtimes are replaceable; no fake headcount |
| Risk & Continuity | PASS | risk acceptance is explicit; material dependencies require recovery/replacement thinking |

## 6. Deliberately deferred subordinate work

The following are **not gaps in the Constitution** and should remain later roadmap work rather than being over-specified in AC-001:

- detailed Company↔Arvectum OS responsibility mapping — `AC-002`;
- canonical repository/artifact map — `AC-003`;
- initial portfolio map — `AC-004`;
- detailed Reserved Owner Decisions — `AC-202`;
- delegated Position authority/approval/escalation matrix — `AC-203`;
- Position Registry and Assignments — `AC-204` / `AC-205`;
- data/tool/credential access baseline — `AC-206`;
- continuity/fallback baseline — `AC-207`;
- product investment thresholds and stop/continue policy — `AC-303`;
- cash/commitment management reporting — `AC-404`.

Deferring them prevents the founding artifact from becoming an unmaintainable pseudo-policy manual.

## 7. Cross-review conclusion

`AC-001` has reached material management consensus at the proposal level after six iterations.

The proposed Constitution is suitable for Owner ratification because it:

- preserves applicable legal/corporate supremacy;
- keeps Owner control without constitutionalizing routine micromanagement;
- makes AI/software replaceable execution means rather than authority sources;
- separates Position, Principal, Assignment and Runtime;
- makes business value, cash, commitments, risk and customer impact first-class concerns;
- preserves Company↔OS↔Product boundaries;
- establishes technology sovereignty, continuity and data-control principles;
- supports governed learning and proportional evidence;
- avoids inventing a mature corporate bureaucracy before real workload justifies it.

**No real Owner approval is claimed by this review.** The next required act is explicit ratification of the exact `Proposed 0.9.0` text, after which the artifact can be published as the canonical Ratified Company Constitution and AC-001 can be closed.
