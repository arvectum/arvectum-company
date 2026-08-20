# AC-106 — M1 Business Baseline Review and Near-Term Priority

Status: `Complete / PASS`
Version: `0.1.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-106 — M1 business baseline review and Owner priority decision`
Review: `docs/reviews/AC-106-M1-BUSINESS-BASELINE-CROSS-REVIEW.md`
Owner decision: `docs/governance/decisions/DECISION-2026-08-20-M1-CLOSURE-AND-NEAR-TERM-PRIORITY.md`

## 1. Purpose

AC-106 reviews AC-101 through AC-108 as one coherent Company-level M1 baseline and converts that evidence into a near-term sequencing decision.

The task is intentionally a business and governance review, not another architecture-design exercise. It must answer:

1. whether M1 is complete within its declared scope;
2. what takes priority when flagship discovery, current customer/revenue obligations, Phase 2 organizational work and other portfolio activity compete for Owner attention;
3. how aggressively the AC-108 market-validation instrument should be run;
4. which uncertainties now require real operating/market evidence rather than more desk analysis;
5. whether cash, authority, risk or continuity evidence blocks progression.

AC-106 does not convert a plan into market evidence. It also does not approve a customer pilot, price, SLA, production deployment, new Position, delegation, product/module status or Arvectum OS lifecycle change merely by closing M1.

## 2. Governing baseline

This review is subordinate to applicable legal/corporate authority, the Ratified Company Constitution and approved Company decisions.

The Company Constitution requires business-first prioritization using obligations/risk, continuity, client value/revenue, economics, scalability and Owner workload. It also requires Owner control over material strategy, capital, risk and commitments while avoiding unnecessary Owner execution bottlenecks.

The flagship direction remains the approved `«ИИ-компания под ключ»` strategy: build and deploy customer-specific AI-native operating organizations on top of Arvectum OS, deriving functions, Positions, authority, workflows, knowledge, controls and human/AI/software execution from each customer's real business rather than cloning a fixed org chart.

Arvectum Company remains both:

- the real operating organization of ООО «Арвектум»; and
- the first reference implementation / dogfooding environment for the organization-first method.

The two roles are coupled but neither may destroy the other: internal reference work must improve the real Company and market work must test whether the method creates transferable commercial value.

## 3. M1 evidence set

| Work item | What M1 now knows | What remains unproven |
|---|---|---|
| `AC-101` | the flagship business direction, Company-level value proposition, Company↔OS↔module/product boundary | demand, price, ROI, repeatability, final commercial packaging |
| `AC-102` | revenue engines, cash/cost/obligation classes, procurement working-capital logic, management-finance boundary | live transaction amounts, product unit economics, customer-specific pricing/margin |
| `AC-103` | real current client lifecycle, value streams, control points and current delivery strengths/weaknesses | repeatable acquisition, standardized acceptance/support, measured post-delivery value |
| `AC-104` | Owner workload concentration, manual-work classes and structural bottlenecks | measured historical hours/queues and proven delegation/automation savings |
| `AC-105` | material dependency/continuity risks and minimum fail-closed/degraded/recovery expectations | tested Company-wide continuity, complete credential/access map, legal succession mechanics, measured RTO/RPO |
| `AC-107` | falsifiable first ICP/buyer/JTBD/wedge/outcome hypotheses and anti-ICP signals | real market confirmation, willingness to pay, implementation/support economics |
| `AC-108` | bounded candidate qualification, discovery, evidence-capture and continue/change/stop instrument | completed interviews, validated segment, design partner, commercial commitment, production evidence |

The critical distinction is:

```text
M1 has a ready-to-run business + market-validation baseline
≠
M1 has validated demand or a proven scalable business model
```

## 4. M1 exit-criteria review

### 4.1 What business Arvectum is building

`PASS`.

The Company has an explicit strategic identity: AI-native company builder / `«ИИ-компания под ключ»`, with Arvectum Company as its first reference implementation and Arvectum OS as the domain-neutral substrate where applicable.

Existing procurement, parser, marketing and infrastructure products remain business lines, reference implementations, standalone products or module candidates subject to later evidence. They do not redefine the flagship by repository count or historical familiarity.

### 4.2 Revenue/cash/cost/obligation structure

`PASS within M1 scope`.

AC-102 provides sufficient management architecture to reason about revenue engines, cost ownership, recurring burden, procurement cash gaps and material obligation classes without recreating bookkeeping.

Live cash and transaction truth remain with the banking/accounting contour. Missing transaction-level detail is not an M1 defect. However, a specific material commitment must not proceed when decision-relevant liquidity, obligation or downside evidence is unavailable.

### 4.3 Owner workload and scale bottleneck

`PASS`.

The dominant current constraint is not raw coding capacity. It is concentration of interpretation, priority switching, customer context, exception routing, acceptance judgment, local/credential gates, decision preparation and state reconstruction around the Owner.

That is sufficient evidence to derive the minimal real operating model in Phase 2. It is not sufficient to invent future Positions or AI Assignments before AC-201 through AC-205.

### 4.4 Risk/continuity baseline

`PASS within M1 scope`.

The Company has explicit material dependency classes and understands which gates are legitimate authority/security controls versus unresolved single points of failure.

The unresolved continuity items are real but intentionally carried into AC-206/AC-207 and later operational controls. AC-105 explicitly found that they do not block M1 closure as a planning milestone.

### 4.5 First plausible market path

`PASS as a hypothesis + instrument`.

The Company can state a falsifiable behavioral ICP, primary buyer hypothesis, JTBD, one-function wedge, measurable outcome hypothesis, hard qualification gates and a bounded first discovery loop.

This satisfies M1 because the milestone is `Business/economic reality and first market-validation plan captured`.

It does **not** satisfy later evidence requirements for market demand, design-partner commitment, pricing, ROI, repeatability or external deployment.

### 4.6 Strongest near-term business case

`PASS as a sequencing decision`.

The strongest near-term business case is not to choose only internal organization design or only external discovery.

The evidence requires a paired loop:

```text
protect real obligations and cash-generating work
        ↓
run bounded flagship discovery now
        ↕
derive the minimal real Arvectum operating model from M1 evidence
        ↓
use real internal + external evidence to govern later portfolio/module investment
```

Waiting for a “finished” internal Company before speaking to the market would contradict the roadmap's market-evidence-early principle. Conversely, stopping internal organizational work until the market is fully validated would preserve the Owner bottlenecks that Arvectum itself needs to solve and would weaken the reference implementation.

## 5. Near-term Owner priority model

The approved sequencing uses four priority bands.

### `P0 — Protect current obligations, cash and material risk`

This band preempts internal roadmap convenience when a real time-sensitive issue exists.

Examples include:

- existing customer delivery/acceptance/support obligations;
- time-sensitive legal, corporate, banking, tax/accounting or procurement obligations;
- material security/data incidents;
- a customer/revenue workstream whose delay has a material contractual, cash or reputational consequence;
- a continuity failure that threatens critical history/data or an existing obligation.

P0 is exception-driven. It is not permission for every incoming request or product idea to interrupt Company sequencing.

### `P1 — Flagship market evidence + minimal reference operating model`

This is the default strategic priority when no P0 exception exists.

Two tracks run in parallel:

1. **External evidence track:** execute the AC-108 first discovery loop as bounded market research.
2. **Internal reference track:** start Phase 2 with AC-201 and derive the minimal real organizational/function model from M1 evidence.

These tracks are intentionally coupled. Discovery tests commercial transferability while Phase 2 removes internal ambiguity and creates a real reference model.

### `P2 — Product work tied directly to real revenue, obligations or evidence`

Product/OS work is prioritized when it is required to:

- satisfy an existing customer/revenue obligation;
- close a material product continuity/security defect;
- produce evidence needed for a qualified discovery/diagnostic/pilot hypothesis;
- preserve a real product line with credible near-term economic value;
- remove a blocker that prevents the P1 loops from running.

Repository activity or technical elegance alone is not a priority claim.

### `P3 — Speculative productization, module expansion and platform expansion`

Work remains below the above priorities when its main justification is speculative completeness, future reuse or architecture preference without current obligation, customer evidence or clear economic need.

This includes prematurely:

- turning every existing product into a flagship module;
- designing a universal module catalog before Phase 3;
- building AI headcount before Positions/authority/workflows exist;
- promoting Company/product semantics into Arvectum OS without the proper admission evidence;
- expanding customer-facing production commitments before market and operational evidence exist.

## 6. AC-108 discovery aggressiveness decision

The discovery instrument should run **immediately and deliberately, but remain bounded**.

The operating principle is:

> **Aggressive in learning; conservative in commitment.**

Approved discovery boundary:

- use the AC-108 working pool of up to `20` candidates;
- target the first `8–12` completed **high-information** conversations;
- test at least two materially different subsegments before treating a familiar domain as leading;
- prefer concrete recent-case evidence over AI opinions;
- do not run a mass outbound campaign merely to increase activity volume;
- do not let superficial conversations count as evidence;
- preserve AC-108 hard gates and continue/change/stop logic;
- discovery may run in parallel with AC-201 through AC-208 and current P0/P2 work;
- a customer diagnostic, supervised pilot, price, discount, SLA, production scope, real privileged access or other material commitment still requires its own explicit approval/agreement.

The first discovery loop should not wait until M2 is “finished”. Equally, Phase 2 should not pause while waiting for all 8–12 conversations if real internal organizational work can proceed safely from current evidence.

## 7. M1 assumptions that now require tracking, not more desk analysis

The following questions have reached the point of diminishing returns for abstract review.

| Evidence question | Why desk analysis is insufficient | Next evidence source |
|---|---|---|
| does the behavioral ICP recur across independent companies? | current evidence is internal/hypothetical | AC-108 conversations |
| is Owner/CEO/General Director really the primary buyer? | buyer role varies by organization | actual authority/budget conversations |
| is the JTBD broad operating friction or usually a narrow software need? | solution framing can bias the answer | recent-case discovery + alternatives |
| which first wedge is most valuable/bounded? | procurement familiarity may bias selection | cross-subsegment evidence |
| how much scarce-management attention is actually consumed? | no trustworthy historical time sheet exists | prospective case/intervention evidence |
| what outcome metrics customers can actually baseline | metric availability is organization-specific | candidate workflow evidence |
| willingness to pay / serious buying behavior | cannot be inferred from interest | buyer behavior after problem evidence |
| implementation/integration/support burden | depends on real customer systems/change | diagnostic/pilot estimates and actual delivery |
| Arvectum unit economics | requires real implementation/support effort and price evidence | future engagement evidence |
| whether reuse lowers second/third-customer effort | no external repeatability exists yet | later customer deployments |
| whether sovereignty/replaceability is a buying driver or only assurance requirement | positioning significance is market-specific | discovery evidence |
| whether Phase 2 reduces Owner bottlenecks | organizational model has not yet been implemented | prospective Owner-intervention evidence |
| whether continuity/fallback controls work | AC-105 is a baseline, not a drill | AC-206/AC-207 and later exercises |

These uncertainties should remain explicit. Lack of evidence must not be replaced by invented percentages or confident narratives.

## 8. Blocker review

No current M1 evidence establishes a **Company-wide blocker** to starting Phase 2 and running AC-108 discovery in parallel.

Specifically:

- AC-105 explicitly carries unresolved access/continuity items forward rather than treating them as M1 stop conditions;
- Arvectum OS is not currently a Company-critical universal runtime dependency and remains bounded through current Provisional/Incubating contracts/capabilities;
- no market evidence is required to prove M1 planning completion because market validation is a later empirical step;
- detailed accounting transactions are not required for Company-design progression;
- missing live financial/authority/data evidence remains a stop condition for the **specific material commitment that needs it**, not for M1 closure itself.

Therefore the correct failure behavior is contextual:

```text
M1 closes
→ Phase 2 + bounded discovery may proceed
→ any material commitment still re-checks cash / authority / risk / data / obligation evidence at decision time
```

## 9. Arvectum OS boundary re-check

Arvectum OS `main` was re-checked for AC-106 at commit `d26f9583393d4f3d9ef104f5408439da0471fd76`.

The Company-relevant state remains compatible with M1 closure:

- Constitution `1.2.0` Ratified;
- RFC-0001 through RFC-0008 Accepted `1.0.0`;
- Decision Authority Policy remains `Proposed 0.2.1`;
- CAP-001 through CAP-004 remain `Incubating / Provisional`;
- P6.02 and P6.06 remain `Provisional 0.1.0`;
- current Phase 8 progress does not create an `Active` capability, `Stable` Product Contract, external production readiness or SLA by implication.

AC-106 therefore makes no Arvectum OS lifecycle or contract decision. Phase 2 remains Company organizational-model work unless later tasks explicitly require OS reliance through the proper governance path.

## 10. M1 closure result

AC-101 through AC-108 now form a coherent M1 baseline sufficient for the declared milestone.

Result:

`M1 — BUSINESS/ECONOMIC REALITY AND FIRST MARKET-VALIDATION PLAN CAPTURED: COMPLETE / PASS`

`AC-106 — M1 business baseline review and Owner priority decision: COMPLETE / PASS`

The next primary Company roadmap action is:

`AC-201 — Minimal real organizational/function model`

The AC-108 first discovery loop is authorized as a bounded parallel evidence-producing activity under the priority and non-commitment boundaries above.

## 11. Non-effect boundary

AC-106 does **not** by itself:

- approve expenditure or a budget;
- approve a customer price, proposal, contract, discount, SLA or support term;
- select or commit to a design partner;
- authorize a production pilot or autonomous consequential customer action;
- create, appoint or delegate a Position/Principal/Assignment;
- create a credential holder or legal representative;
- approve a product as a reusable module;
- change a product roadmap or product implementation status;
- activate/stabilize an Arvectum OS capability/Product Contract;
- claim validated demand, profitability, customer readiness or product-market fit.

Those effects require their own applicable evidence and authority path.