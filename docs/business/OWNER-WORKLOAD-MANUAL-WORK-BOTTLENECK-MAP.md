# AC-104 — Owner Workload, Manual Work and Bottleneck Map

Status: `Complete / PASS`
Version: `0.1.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-104 — Owner workload, manual work and bottleneck map`
Review: `docs/reviews/AC-104-OWNER-WORKLOAD-CROSS-REVIEW.md`

## 1. Purpose

This baseline maps where the Owner currently spends attention, performs manual work, carries context, reviews exceptions or becomes a queue in the real operation of Arvectum Company.

The purpose is not to design the future organization, invent Positions, or prematurely automate every manual action. It is to distinguish:

1. work that is legitimately Owner-reserved because it changes strategy, capital, risk appetite, material commitments or governance;
2. judgment currently concentrated in the Owner but potentially transferable to a later accountable Position through explicit policy, evidence and escalation;
3. repeatable execution that should not remain dependent on Owner time;
4. manual local or credential-gated actions that create operational blocking even when the intellectual work is already complete;
5. coordination/context-reconstruction load caused by work spanning clients, products, repositories, runtimes and governance boundaries.

The output is an evidence baseline for AC-105 and Phase 2 organizational design. It does not itself create authority delegation, an AI Assignment, a staffing plan, or an automation commitment.

## 2. Evidence boundary and confidence model

AC-104 uses the current Company repository, AC-101 through AC-103, product/repository operating traces and promoted project operating context.

Statements are classified as:

- **Repository-evidenced current pattern** — repeated directly in canonical Company/product artifacts or repository workflow evidence;
- **Promoted operating-context pattern** — recurring real practice visible across project work and promoted here at Company level;
- **Strong inference** — supported by several operating traces but not yet instrumented quantitatively;
- **Unknown / prospective measurement** — exact workload magnitude is not currently evidenced and must be measured going forward.

No historical time-sheet exists. Therefore this baseline does **not** fabricate hours, percentages of the Owner's week, utilization, queue time or monetary cost of Owner attention.

Instead, it records qualitative concentration using four labels:

- `Reserved` — should remain with Owner unless explicitly changed by later governance;
- `Owner-dependent` — current work materially depends on Owner judgment/context but is not inherently reserved;
- `Owner-executed` — Owner performs the work today although the execution itself is plausibly delegable/automatable;
- `Owner-gated` — another executor can do most work, but completion waits on Owner-controlled access, local action, approval or external effect.

## 3. Current Owner role concentration

The Owner currently acts simultaneously across several materially different functions:

- shareholder / residual corporate authority;
- general director and legal representative;
- strategic portfolio allocator;
- commercial interpreter and commitment gate;
- product owner across several active initiatives;
- delivery coordinator for client-specific work;
- reviewer of exceptions, acceptance and productization decisions;
- repository/roadmap/governance coordinator across Company, products and Arvectum OS;
- operator of some local/credential-bound execution environments;
- final human authority at consequential external boundaries where automation is intentionally constrained.

This concentration is understandable at the present scale, but it creates a structural difference between **Owner control** and **Owner execution**. Arvectum's operating model should preserve the former while systematically reducing unnecessary dependence on the latter.

## 4. Workload map by Company lifecycle

| Lifecycle area | Current Owner involvement | Classification | Bottleneck mechanism | Evidence confidence |
|---|---|---|---|---|
| opportunity / client request judgment | decides whether an opportunity is worth attention and how it fits current priorities | `Owner-dependent`, sometimes `Reserved` | opportunities cannot advance when value/risk/priority judgment exists only in Owner context | strong |
| discovery / ambiguous requirement interpretation | translates incomplete client language into the actual required result, source/data boundary and acceptance expectation | `Owner-dependent` | semantic ambiguity is resolved centrally; context does not yet live in a reusable scoping workflow | strong |
| commercial commitment | determines or confirms what Arvectum will promise, deliver, support or accept as risk | `Reserved` for material commitments; otherwise potentially delegable within limits | commitment queue and risk of accidental overcommitment | strong |
| technical decomposition / priority | chooses what to build next, which repository owns it and whether work belongs in Company, product or OS | `Owner-dependent` | multiple active initiatives compete for one prioritization context | strong |
| implementation execution | much coding can be performed by AI/software/local coding agents; Owner often initiates, sequences and reviews work | `Owner-executed` / coordinator | Owner attention becomes scheduler for otherwise parallelizable technical work | strong |
| local execution / machine acceptance | installs, runs, tests, signs, approves or performs environment-specific actions on Owner-controlled machines when remote/cloud execution is insufficient | `Owner-gated` | completed engineering waits for physical device, credential, OS or local-runtime access | strong |
| QA exception review | routine automated tests are increasingly strong, but ambiguous failures, real-world mismatch and acceptance exceptions return to Owner judgment | `Owner-dependent` | exception path is centralized even when happy-path QA is automated | strong |
| customer communication | receives feedback, interprets intent, decides whether the issue is defect/scope/change and communicates next step | `Owner-dependent` | customer context continuity exists largely in one Principal | strong |
| acceptance / closure | decides whether the delivered outcome is sufficient, whether more correction is owed, and whether work is done | `Owner-dependent`; material disputes/commitments may be `Reserved` | open-ended correction loop can continue without a bounded acceptance gate | strong |
| support / continuation | decides urgency, whether to fix now, defer, productize or treat as new work | `Owner-dependent` | reactive work interrupts planned roadmap and portfolio sequencing | strong |
| productization / reuse | decides whether a client-specific pattern should remain local, become product capability, module candidate or OS-related work | `Owner-dependent`, strategic cases `Reserved` | cross-repository architectural/business judgment remains concentrated | strong |
| governance / canonical publication | reviews or directs durable decisions, roadmap transitions and boundaries | `Reserved` for material decisions; publication mechanics `Owner-executed` today | decision authority and clerical synchronization are partially coupled | strong |
| finance management | Owner needs management visibility into cash, commitments and economics; outsourced accounting handles bookkeeping/tax execution | `Reserved` for capital/risk decisions; reporting preparation should be delegable | missing management view can force manual reconstruction | established by AC-102 |

## 5. Manual work classes

### MW-1 — Context translation

**Pattern:** the Owner repeatedly translates between customer language, product behavior, technical implementation and business commitment.

Examples:

- interpreting a customer's imprecise request into an exact accepted output;
- deciding whether a reported mismatch is a defect, a source-specific exception or new scope;
- translating product technical readiness into a customer-facing promise;
- deciding whether repeated implementation belongs in the product, Company methodology or Arvectum OS boundary.

**Why it matters:** this is high-value judgment, but the organization currently retains too little reusable structure around the judgment. If every new case requires full reconstruction in the Owner's head, scale remains linear with Owner attention.

**Direction:** capture decision inputs, standard questions, bounded options, evidence and escalation criteria before selecting an executor.

### MW-2 — Work sequencing and repository orchestration

**Pattern:** many implementation tasks can be delegated to AI/software, but the Owner frequently selects the next task, moves work across repositories, interprets completion reports and decides whether to continue.

**Why it matters:** automation of coding does not remove the Owner bottleneck if task decomposition, priority, acceptance and cross-repository reconciliation still form one central queue.

**Direction:** later operating model should separate portfolio priority, product accountability, technical execution and acceptance evidence rather than treat all of them as one Owner activity.

### MW-3 — Local / credential-bound execution

**Pattern:** some steps require Owner-controlled machines, operating systems, credentials, physical tokens, signing environments or human confirmation.

Examples across current work include local installation/acceptance, machine-specific packaging checks and consequential actions intentionally kept manual.

**Why it matters:** a task can be intellectually complete yet operationally blocked until the Owner is physically available.

**Direction:** AC-105/AC-206/AC-207 must distinguish justified human/credential gates from accidental environment dependence, and define safe fallback/replacement paths.

### MW-4 — Customer feedback and exception handling

**Pattern:** real customer use produces edge cases that automated tests cannot predict. The Owner receives or interprets the feedback and routes it back into work.

**Why it matters:** this is one of Arvectum's strongest learning loops, but it creates interruption-heavy work and can become unbounded rework.

**Direction:** preserve the feedback loop while standardizing intake, classification, severity, scope/change decision and closure evidence.

### MW-5 — Approval plus clerical synchronization

**Pattern:** a material decision may correctly require Owner approval, but the same Principal also performs or coordinates the surrounding low-risk mechanics: updating roadmap state, checking repository consistency, synchronizing artifacts and ensuring the next action is explicit.

**Why it matters:** reserved authority becomes unnecessarily expensive when approval cannot be separated from preparation/publication mechanics.

**Direction:** future workflows should allow delegated preparation and automatic bounded publication after explicit Owner decision, while preserving the approval record and preventing AI from becoming authority.

### MW-6 — State reconstruction

**Pattern:** because material work is distributed across chats, repositories, local environments, product roadmaps and client feedback, the Owner can be forced to reconstruct "what is current, what is blocked, what needs approval, and what comes next".

**Why it matters:** reconstruction is pure coordination overhead and directly competes with strategy, client value and product judgment.

**Direction:** Phase 4 Owner Mission Control and registers should remove repeated reconstruction without creating dashboard theater.

## 6. Bottleneck map

### B-1 — Universal interpreter bottleneck

**Severity:** `High`.

The largest structural bottleneck is the concentration of business meaning across commercial, customer, product and technical contexts in one Principal.

A customer request, code change, product limitation or roadmap item often becomes actionable only after the Owner interprets what it means for scope, priority and acceptable outcome.

This is more fundamental than raw coding capacity. Coding can already be parallelized materially; interpretation and accountable decision framing are less distributed.

### B-2 — Priority / portfolio switching bottleneck

**Severity:** `High`.

Arvectum operates several active product and Company/OS streams. The Owner is the current shared priority allocator among them.

The cost is not only the decision itself, but repeated context loading across unrelated repositories and operating states.

This creates risk that urgent client corrections, strategic platform work and productization all compete in one attention queue.

### B-3 — Customer-context continuity bottleneck

**Severity:** `High` for bespoke work.

Current delivery often depends on continuity of client history, acceptance expectations, previous exceptions and the Owner's interpretation of what was actually promised.

The risk is both scale and continuity: another executor may possess the code but not the relationship context needed to make a correct decision.

### B-4 — Exception and rework bottleneck

**Severity:** `High` where customer validation is active.

Happy-path implementation can be automated and tested. Exceptions return to Owner attention, especially when the correct response depends on whether the issue is:

- technical defect;
- incomplete input;
- environmental difference;
- changed customer expectation;
- new scope;
- product limitation;
- risk/commitment question.

The bottleneck is therefore an exception-classification problem as much as an engineering problem.

### B-5 — Local execution gate

**Severity:** `Medium–High` depending on product.

Some work stops at a point that requires local machine access, user-device validation, a physical/credential-bound operation or explicit human external action.

This is acceptable when it is a deliberate authority/security control; it is waste when it exists only because the execution path is not portable or remotely observable.

### B-6 — Reserved decision + preparation coupling

**Severity:** `Medium` now, potentially `High` as volume increases.

The Owner should retain material strategic, capital, risk and external-commitment decisions. The bottleneck arises because supporting evidence collection, proposal preparation, publication, notifications and follow-through are not yet consistently separated from the decision itself.

### B-7 — State visibility / reconstruction bottleneck

**Severity:** `Medium` now, structurally increasing with portfolio size.

The Owner must often infer current state from repository status, chat handoffs, local execution results and separate roadmaps.

The Company roadmap already anticipates AC-401–AC-406 because this work does not scale safely by memory alone.

## 7. What should remain Owner-reserved

AC-104 does not finalize the Reserved Owner Decisions policy; AC-202 owns that task. However, the workload analysis shows that the following classes should be presumed Owner-reserved until explicitly delegated through later governance:

1. Company strategy and flagship direction;
2. capital allocation and material recurring-cost commitments;
3. risk appetite and acceptance of material legal/security/reputational gaps;
4. creation of material customer/company obligations outside already approved bounded terms;
5. approval of material organizational-model or governance changes;
6. approval of material cross-repository/company↔OS responsibility changes;
7. appointment/revocation of material delegated authority;
8. stop/continue decisions for major initiatives where downside or strategic consequences are material.

The key design target is **not** to automate these decisions. It is to reduce the amount of Owner time required to reach them safely by improving preparation, evidence, options and execution after the decision.

## 8. Work that is a strong delegation/automation candidate

The following work should be treated as candidate workload for later Position/workflow design, subject to AC-201–AC-207 and actual risk/data/tool boundaries:

| Candidate | Why it should not remain Owner-exclusive | Needed before delegation/automation |
|---|---|---|
| intake normalization | repeatable extraction of request, inputs, constraints and missing information | intake schema + escalation triggers |
| standard discovery preparation | questions and source/data readiness checks are reusable | workflow + customer-specific boundary |
| evidence assembly for decisions | gathering repository, test, financial or risk evidence does not itself create authority | provenance + freshness + decision template |
| routine task decomposition | many implementation steps follow repeatable product/repo patterns | accountable product context + stop/escalation rules |
| routine QA / regression / packaging | already substantially automatable in several repositories | accepted quality gates + failure routing |
| issue/change classification first pass | common categories are recognizable | explicit defect/scope/change taxonomy + human escalation |
| progress/state synchronization | roadmap/status/read-after-write checks are procedural | canonical-source contract + permissions |
| draft customer status updates | can be prepared from current evidence | approval rule for commitments/external effect |
| support triage | routine severity/data collection can be standardized | support boundary + escalation/SLA assumptions |
| productization evidence collection | reuse candidates can be detected and assembled without making the promotion decision | rights boundary + review criteria |
| management reporting preparation | data aggregation can be delegated | management-finance source/interface + controls |
| continuity/runbook execution | many recovery/check steps should not require Owner memory | tested runbooks + credentials/access model |

These are **candidates**, not approved Assignments. AI/software suitability must be evaluated only after accountable Position, authority, data/tool access, workflow, evidence and fallback are defined.

## 9. Owner attention hierarchy

The desired operating hierarchy is:

```text
Owner attention
    ↓ reserved for
strategy / capital / material risk / material commitments / governance
    ↓ supported by
prepared evidence / bounded options / exception summaries
    ↓ while routine work moves to
accountable Positions + human | AI | software Assignments
    ↓ with
explicit escalation when bounds are exceeded
```

The anti-pattern is:

```text
AI executes more tasks
→ Owner receives more raw outputs
→ Owner still interprets every exception
→ Owner still sequences every next step
→ apparent automation rises while real Owner bottleneck remains
```

Owner-workload reduction must therefore be measured at the organizational level, not by counting AI agents or automated actions.

## 10. Prospective measurement baseline

AC-104 cannot prove exact time savings retrospectively. Future real work should capture lightweight evidence sufficient to answer:

- how many material Owner interventions occurred per engagement/workstream;
- intervention class: reserved decision / judgment / execution / local gate / exception;
- whether the intervention was planned or interrupt-driven;
- what evidence the Owner had to reconstruct manually;
- elapsed blocking time waiting for Owner action where material;
- whether a repeat intervention could have been handled by an explicit workflow/policy;
- number of context switches across products/repos/clients where useful;
- rework caused by ambiguous scope or acceptance;
- local/credential-gated actions and whether they were deliberate controls or incidental technical dependency;
- whether delegated/automated preparation reduced Owner decision time without increasing error/risk.

This does not require time tracking of every minute. The measurement should be proportional and focused on bottleneck decisions and queues.

## 11. Implications for AC-105

AC-105 should treat the following as explicit continuity/risk questions:

1. What stops if the Owner is unavailable for one day, one week or materially longer?
2. Which functions are blocked by Owner-held credentials, local machines, signing capability or inaccessible context?
3. Which customer obligations depend on undocumented Owner memory?
4. Which active initiatives lack a safe stop/fallback path when Owner review is delayed?
5. Which reserved decisions have no prepared evidence/decision protocol?
6. Which apparently automated workflows still rely on hidden Owner exception handling?
7. Where can a failure create an external commitment, data/security exposure or customer impact before the Owner sees it?

AC-105 owns the actual material dependency, continuity and fallback baseline; AC-104 only exposes the workload-dependent risks to carry forward.

## 12. Implications for Phase 2 organizational design

Phase 2 should derive the minimum real structure from this evidence, not from a generic company org chart.

At minimum it must separate responsibilities for:

- opportunity/scoping and commitment preparation;
- product/workstream accountability;
- delivery/operations coordination;
- customer feedback/acceptance handling;
- technical execution and QA;
- governance/evidence preparation;
- continuity and access control;
- portfolio prioritization and material Owner decisions.

This list is a functional responsibility map, **not** a Position list. Multiple functions may initially belong to one Position; one function may use several executors; no Position should be created without real workload/control/economic justification.

## 13. Flagship-product learning

AC-104 provides direct dogfooding evidence for the `«ИИ-компания под ключ»` thesis.

A customer AI-native organization should not be designed by asking "which employees can we replace with AI?". It should first ask:

```text
where is scarce accountable attention consumed?
→ which attention is legitimately reserved?
→ which work is judgment that can be bounded?
→ which execution is repeatable?
→ where are exceptions and hidden manual gates?
→ what evidence/authority/fallback is required?
→ only then choose human, AI or software execution
```

The Arvectum reference implementation already shows that adding more AI execution without reducing interpretation, prioritization and exception queues can leave the core bottleneck unchanged.

## 14. AC-104 completion boundary

AC-104 is complete when the Company can distinguish:

- Owner control from Owner execution;
- reserved authority from current dependency;
- high-value judgment from clerical/manual preparation;
- repeatable work from exception handling;
- automated happy-path execution from hidden human gates;
- local/security controls from accidental local dependence;
- portfolio/product/customer context bottlenecks from raw technical capacity;
- candidate delegation/automation work from approved delegation;
- qualitative bottleneck evidence from still-unknown quantitative workload.

This publication satisfies that boundary without inventing time-sheet data, future Positions, delegation limits, headcount, AI Assignments or automation ROI.

Next roadmap action: `AC-105 — Material risk, dependency, continuity and fallback baseline`.