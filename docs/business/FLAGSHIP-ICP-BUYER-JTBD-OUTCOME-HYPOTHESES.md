# AC-107 — Flagship ICP, Buyer, Job-to-be-Done and Measurable Outcome Hypotheses

Status: `Complete / PASS`
Version: `0.1.0`
Created: `2026-08-20`
Updated: `2026-08-20`
Owner: `ООО «Арвектум»`
Repository: `arvectum/arvectum-company`
Roadmap item: `AC-107 — Flagship ICP, buyer, job-to-be-done and measurable outcome hypotheses`
Review: `docs/reviews/AC-107-FLAGSHIP-ICP-BUYER-JTBD-OUTCOME-CROSS-REVIEW.md`
Strategic basis: `docs/governance/decisions/DECISION-2026-08-20-FLAGSHIP-AI-COMPANY-BUILDER.md`

## 1. Purpose

This artifact narrows the first plausible market hypothesis for Arvectum's flagship **«ИИ-компания под ключ»** direction far enough to support real design-partner discovery in AC-108.

It identifies:

- the first plausible ideal-customer profile (`ICP`);
- the likely economic/organizational buyer and the operational champion around that buyer;
- the concrete job-to-be-done (`JTBD`) for which a customer would hire Arvectum;
- the smallest credible first deployment wedge;
- measurable operating-outcome hypotheses and guardrails;
- fit/exclusion criteria and explicit falsification signals.

This is a **hypothesis baseline**, not market validation. It does not claim proven demand, pricing, willingness to pay, implementation duration, repeatability, ROI, customer readiness, legal/compliance readiness, or Arvectum OS production maturity.

## 2. Canonical basis and evidence boundary

AC-107 is derived from the current Company baseline rather than from generic AI-market assumptions.

- AC-101 fixes the flagship direction: Arvectum is an AI-native company builder, not a procurement-only company and not an agent-swarm vendor.
- AC-102 establishes that implementation, recurring runtime/support, modules and customization may create value/cost, but actual pricing and unit economics remain unproven.
- AC-103 shows that Arvectum's strongest current evidence is concrete discovery → scoped delivery → internal verification → customer validation → correction → acceptance, while repeatable acquisition and post-delivery value measurement remain weak.
- AC-104 shows that the most material scaling bottleneck is not raw coding capacity but concentrated interpretation, prioritization, customer context, exception routing, approval preparation and local/credential gates around one senior Principal.
- AC-105 requires the offer to preserve legitimate authority/security gates, customer sovereignty, external-source authority, replaceability and safe degraded/fallback behavior rather than treating every control as something to automate away.

The approved flagship decision explicitly did **not** approve a specific ICP, industry, price, module catalog or external commitment. AC-107 therefore records falsifiable hypotheses rather than pretending that a customer segment has already been selected by market evidence.

The initial go-to-market context is **Russia-first**, consistent with Company strategy and technology-sovereignty requirements. This is a sequencing choice, not a market-size or legal-compliance conclusion and does not preclude later international expansion.

## 3. Core market hypothesis

The strongest first flagship hypothesis is not defined primarily by industry or employee count. It is defined by an operating pattern.

> **Primary ICP hypothesis:** an owner-operated or strongly owner-led B2B company in which one or more repeatable, information/coordination-heavy business functions still depend materially on the owner or another scarce senior manager to interpret requests, sequence work, resolve exceptions, preserve customer/process context and approve consequential actions; the company already uses digital tools and may use AI ad hoc, but lacks one explicit organizational model connecting responsibility, authority, workflow, knowledge, evidence and execution.

The target company is:

- small enough that the owner/CEO or another top executive can still sponsor a bounded operating-model change directly;
- complex enough that coordination and exception handling create real operating cost or growth friction;
- digital enough that at least one meaningful function has observable inputs, outputs and evidence;
- repetitive enough that a before/after outcome can be measured;
- constrained enough that the first deployment can be bounded to one function/value stream rather than requiring an enterprise-wide transformation.

This is a **behavioral ICP**, not a claim that all SMEs or all owner-led companies have the same problem.

## 4. First customer-segment definition

### 4.1 Primary segment

The first segment to test is:

> **Owner-led Russian B2B businesses with a recurring case/workflow operation and a visible senior-management bottleneck.**

Typical characteristics:

1. work arrives as cases, requests, orders, tenders, projects, client tasks, documents or other repeatable units;
2. several tools/channels hold fragments of the process — email/messengers, spreadsheets, CRM/ERP, websites, documents, local applications or isolated AI tools;
3. routine execution may already be delegated, but ambiguous interpretation, prioritization, exceptions and final approval return to the owner/CEO/senior manager;
4. customer/operational context is partly stored in people's heads or chat history rather than in a reusable workflow/knowledge/evidence model;
5. growth creates more coordination and management load instead of proportionally more organizational leverage;
6. the organization can identify at least one bounded function where accepted output and meaningful human effort can be observed;
7. the customer is willing to keep consequential authority with authorized people while allowing bounded AI/software execution underneath that authority.

### 4.2 Strong first subsegment candidates

AC-107 does not lock the flagship to one industry, but current Arvectum evidence makes several subsegments more credible for early discovery:

| Candidate subsegment | Why it is plausible now | Boundary / risk |
|---|---|---|
| owner-led B2B suppliers / tender-oriented companies | recurring information-heavy cases; existing Tender Agent/Tender Operator domain evidence; clear human approval boundary | procurement must remain one wedge/module, not the identity of the whole flagship; regulated/external actions require strict authority boundaries |
| owner-led digital-service / automation / agency businesses | operating pattern is close to Arvectum's own proven bottlenecks: discovery, scoping, delivery, QA, feedback, rework and acceptance | project work can be too bespoke unless a repeatable function is isolated |
| owner-led data-heavy commerce / monitoring / operations businesses | parser/data-product evidence shows potential for repetitive intake, normalization, monitoring and exception workflows | source drift/integration burden can dominate if the business job is not bounded |

The first design partner may come from any of these if the **operating-pattern criteria** are stronger than industry resemblance.

### 4.3 Adjacent but secondary segment

A later adjacent segment is a larger organization or business unit seeking controlled AI adoption, where one executive has sufficient budget/operating authority over a bounded function.

This is secondary for the first design-partner search because enterprise procurement, security, integration and stakeholder complexity can obscure whether the core Arvectum method itself creates value.

## 5. Buyer, champion, users and veto roles

### 5.1 Primary buyer hypothesis

The likely first economic and organizational buyer is:

> **Owner / Founder / CEO / General Director or equivalent top executive who personally experiences the coordination bottleneck and has authority to change how the targeted business function is organized and funded.**

This is the preferred buyer because the flagship offer changes more than software. It can change responsibilities, workflow, approval boundaries, information flow and the relationship between people, AI and software.

A technical buyer alone is therefore insufficient unless that person also has explicit business authority over the target function.

### 5.2 Operational champion hypothesis

The likely implementation champion is one of:

- COO / operations lead;
- head of the selected business function;
- senior manager who owns day-to-day throughput/quality;
- in a very small company, the Owner/CEO directly.

The champion must be able to expose real workflow evidence, explain exceptions and participate in acceptance. Champion status does not create authority beyond the customer's own delegation.

### 5.3 Users and affected actors

Users may include functional staff, reviewers, analysts, coordinators, sales/procurement/operations personnel and administrators whose work participates in the selected workflow.

They are not necessarily the buyer. Their adoption/friction evidence is nevertheless essential because a technically correct system that increases operating burden does not create customer value.

### 5.4 Veto / assurance roles

Depending on scope, IT/security, legal/compliance, finance, data owners or external system owners may have approval or veto responsibilities.

AC-107 does not invent a universal customer RACI. AC-108 discovery must identify the actual customer authority and decision map for each candidate.

## 6. Job-to-be-done

### 6.1 Core JTBD

> **When recurring operational work increasingly depends on me or another scarce senior manager to interpret context, route exceptions, coordinate people/tools and approve actions, help me turn one material business function into an explicit AI-native operating model — responsibilities, authority, workflow, knowledge, controls, evidence and bounded human/AI/software execution — so that the function produces accepted business outcomes with materially less scarce management attention, faster and more consistently, without losing organizational control.**

The customer is not primarily hiring Arvectum to “install AI”.

They are hiring Arvectum to reduce a specific form of organizational friction:

```text
person-dependent coordination
+ fragmented tools/context
+ repeated interpretation
+ manual exception routing
+ weak reconstructability
→ explicit function / Position / authority / workflow / evidence model
→ bounded AI/software execution
→ less scarce managerial attention per accepted outcome
→ preserved control, continuity and replaceability
```

### 6.2 Progress the customer is seeking

The intended progress is:

1. move repeatable execution and evidence preparation away from scarce executive attention;
2. keep material decisions and legal/organizational authority with the appropriate human Principals;
3. reduce context reconstruction and “ask the owner what this means” loops;
4. reduce cycle time and interruption load around one selected function;
5. improve consistency and reconstructability of accepted outputs;
6. increase operating capacity without requiring management complexity to grow at the same rate;
7. preserve the ability to replace an AI model/runtime/vendor without losing organizational meaning/history.

These are outcome hypotheses, not validated customer claims.

## 7. Smallest credible first deployment wedge

The flagship concept is intentionally broad; the first customer engagement must not begin by attempting to “replace the whole company with AI”.

The first credible wedge is:

> **one recurring, information/coordination-heavy function or value-stream slice where the executive bottleneck is visible, the accepted output can be defined, the authority boundary can remain explicit and the before/after operating burden can be observed.**

A suitable wedge should have:

- a repeatable trigger/input;
- a named business outcome/output;
- enough real cases to observe recurring behavior;
- identifiable handoffs/exceptions;
- a bounded set of systems/data/tools;
- an accountable customer authority for approvals;
- a manual/degraded fallback;
- a measurable baseline before broad automation.

Examples may include a tender-analysis/RFQ function, client-intake/scoping/coordination function, data-monitoring/normalization function or another customer-specific workflow. The example does not become a fixed module or standard department by being named here.

## 8. Primary measurable outcome hypothesis

The flagship should be judged first at the organizational operating level, not by number of agents or generated tokens.

### 8.1 North-star operating metric

The strongest general first hypothesis is:

> **The selected function can produce the same or better accepted business output with materially less scarce owner/senior-manager attention per unit of work, while preserving required authority, quality and safety.**

Possible measurements include:

- owner/senior-manager interventions per case;
- active owner/senior-manager time per case or per accepted output, where practical;
- elapsed blocking time waiting for owner/senior-manager interpretation or approval;
- number of exception decisions requiring executive attention;
- amount of context that must be manually reconstructed before a decision.

No percentage target is invented before a real baseline exists.

### 8.2 Paired outcome metrics

The north-star metric must be paired with other operating outcomes so that “less manager time” does not hide worse work.

| Outcome dimension | Hypothesis | Example evidence |
|---|---|---|
| managerial attention | fewer/lower-effort senior interventions per accepted unit | intervention count/time, blocked waiting time |
| cycle time | selected workflow completes faster | trigger-to-accepted-output elapsed time |
| throughput | same team can complete more accepted units where demand exists | accepted units per period / constrained resource |
| quality | accepted-output rate is maintained or improves | acceptance, critical-defect, correction/rework evidence |
| rework | avoidable correction caused by ambiguity/process failure falls | rework count/cause/classification |
| exception handling | routine exceptions are resolved by explicit workflow and only material exceptions escalate | escalation rate and reason |
| reconstructability | another authorized actor can understand current state and why material actions occurred without private owner memory | evidence completeness / successful handover-reconstruction test |
| continuity | safe work can continue or fail closed when one runtime/person/system is unavailable | bounded fallback/recovery evidence |
| adoption/friction | staff can use the workflow without creating greater hidden manual burden | user steps, workarounds, support incidents, acceptance feedback |

### 8.3 Mandatory guardrails

A result is not a success if time or throughput improves by weakening control.

Mandatory guardrails for a design-partner hypothesis include:

- no unauthorized customer commitment or external consequential action;
- no fabricated Organizational Authority for AI/software;
- no hidden cross-customer data/knowledge reuse;
- no silent use of stale/uncertain external authority as current truth;
- no reduction in required approval/security controls merely to improve cycle time;
- no material quality deterioration hidden by automation volume;
- no unbounded reliance on one model/runtime/vendor for organizational meaning or history.

## 9. Economic outcome hypothesis

The commercial thesis requires operating value to exceed implementation and support burden.

A useful later economic model is:

```text
Customer operating value
= avoided scarce-management effort
+ avoided routine labor/rework where genuinely displaced
+ incremental capacity / faster-cycle contribution where demand exists
+ avoided interruption / continuity / error cost where measurable
- implementation and integration effort
- recurring runtime/support cost
- customer change/adoption burden
- residual operational/risk cost
```

AC-107 does not put numbers into this equation.

The first design-partner validation should test whether the customer can identify a real value pool large enough to justify implementation and whether Arvectum can capture some of that value without creating a customization/support model that destroys its own unit economics.

## 10. Commercial success ladder

A useful evidence sequence is:

1. **Problem evidence** — the senior-management bottleneck is real, recurrent and material.
2. **Workflow evidence** — one bounded function can be described with real inputs, outputs, exceptions and authority.
3. **Outcome evidence** — managerial attention/cycle time/throughput improves without quality/control degradation.
4. **Adoption evidence** — the customer and users continue using the operating model with tolerable friction.
5. **Economic evidence** — customer value is credible relative to implementation/runtime/support burden.
6. **Commercial evidence** — an authorized buyer is willing to pay/continue/expand on terms acceptable to Arvectum.
7. **Repeatability evidence** — the second/third customer requires materially less reinvention than the first.

AC-107 establishes only the hypotheses for steps 1–3 and the evidence questions for later steps. It does not claim that any ladder step has already passed for the flagship.

## 11. Fit criteria for AC-108 discovery

A candidate should score as stronger fit when most of the following are true:

- a senior executive can name a recurring workflow/function that personally consumes attention or blocks scale;
- the pain recurs often enough to matter economically/operationally;
- accepted output can be described and observed;
- current process contains repeated interpretation, handoff, exception or context-reconstruction work;
- relevant inputs/data/systems can be accessed lawfully and safely for a bounded pilot;
- the customer can identify who has authority to approve material actions;
- the customer accepts supervised/bounded deployment rather than requiring unsafe autonomy on day one;
- a manual or existing fallback exists while the new operating model is proven;
- the customer can provide baseline and post-change evidence;
- the buyer can make or sponsor a bounded design-partner decision;
- there is plausible economic value beyond novelty or “AI for AI's sake”.

## 12. Poor-fit / anti-ICP signals

The first flagship design partner is likely poor fit when:

- the only request is “give us a chatbot/agent” with no business-function outcome;
- there is no repeatable workflow or observable accepted output;
- the pain is too infrequent or too small to justify organization-level redesign;
- no authorized sponsor owns the target function;
- the customer expects AI/software to receive authority it cannot lawfully or organizationally hold;
- success depends on immediate unbounded external actions or commitments before a supervised proof;
- required data/system access cannot be provided or governed;
- the customer will not expose enough real workflow evidence to establish a baseline;
- the engagement requires company-wide replacement before one bounded slice can be proven;
- unsupported production/SLA/security/compliance commitments are demanded as a condition of discovery;
- custom integration/support burden is obviously likely to dominate the operating value;
- the customer primarily seeks lowest-cost body replacement rather than a governable operating capability.

These are screening hypotheses for AC-108, not universal refusal rules.

## 13. Falsifiable hypotheses to test in AC-108

| ID | Hypothesis | Evidence that supports it | Evidence that weakens/rejects it |
|---|---|---|---|
| `ICP-H1` | owner-led B2B firms experience a material senior-management coordination/exception bottleneck | repeated concrete examples, measurable waiting/intervention load, executive urgency | pain is rare, delegated already, or not economically material |
| `ICP-H2` | the problem is better framed as an operating-model/function problem than as a standalone AI-tool problem | buyer describes responsibility/workflow/context/authority pain and wants end-to-end change | buyer only wants a narrow tool and rejects organizational/process change |
| `BUY-H1` | Owner/CEO/General Director is the natural first economic/authority buyer | executive owns pain, budget and operating change | purchase is consistently owned elsewhere with no executive sponsorship required |
| `CHAMP-H1` | a function/operations leader can act as day-to-day champion | champion can expose workflow, exceptions and acceptance evidence | no operational owner can support implementation |
| `JTBD-H1` | reducing scarce management attention per accepted outcome is a compelling core job | buyer can quantify interventions/time/blocking and values reduction | owner attention is not constrained or not viewed as a problem |
| `WEDGE-H1` | one bounded function can prove value before company-wide transformation | function has repeatable inputs/outputs and separable authority/data boundary | value requires simultaneous redesign of most of the company |
| `OUT-H1` | managerial attention can fall without lowering accepted-output quality/control | before/after evidence shows lower attention with stable/improved acceptance and no authority breach | automation shifts work to hidden rework/support or degrades quality/control |
| `ECO-H1` | value pool can exceed implementation/runtime/support burden | customer and Arvectum can identify credible net-positive operating economics | customization, integration and support cost consume the value |
| `SOV-H1` | sovereignty/replaceability/governance are meaningful differentiators for a material subset of buyers | customer values controlled/local/replaceable design and explicit authority | buyers consistently treat these as irrelevant relative to simple SaaS convenience |

AC-108 should convert these into discovery questions and evidence capture, not ask candidates to agree with Arvectum's wording.

## 14. First positioning statement to test

A discovery-safe formulation is:

> **Arvectum takes one repeatable business function where the owner or senior manager is still the bottleneck and turns it into a governed AI-native operating model: explicit responsibility, approvals, workflow, knowledge, evidence and bounded AI/software execution. The hypothesis is that the same accepted business outcome can then be produced with less scarce management attention and better operational continuity without giving up control.**

Short Russian formulation for testing:

> **Берём одну повторяемую функцию, где собственник или руководитель остаётся узким местом, и переводим её в управляемую AI-native модель: ответственность, полномочия, процессы, знания и AI/software-исполнение — так, чтобы бизнес получал тот же или лучший результат с меньшей зависимостью от ручного внимания руководителя и без потери контроля.**

This is a discovery proposition, not an external guarantee or approved marketing claim of achieved ROI.

## 15. Explicit unknowns after AC-107

Still unknown and intentionally deferred:

- which subsegment responds most strongly;
- whether the hypothesized Owner/CEO buyer actually buys this category;
- which words customers themselves use for the problem;
- willingness to engage in a design-partner pilot;
- willingness to pay and preferred commercial structure;
- acceptable implementation duration;
- integration/data/security burden by segment;
- baseline and achievable magnitude of managerial-attention reduction;
- impact on cycle time, throughput, rework and quality;
- customer change-management/adoption burden;
- Arvectum implementation/support cost and gross-margin potential;
- which existing products actually reduce deployment effort as reusable modules;
- whether Arvectum OS is commercially best bundled, managed, self-hosted or otherwise packaged;
- whether sovereignty/portability is a buying driver or only a risk-control requirement;
- repeatability across a second and third customer.

These unknowns are not defects in AC-107. They are the evidence target for AC-108, M7 and M8.

## 16. AC-108 handoff

AC-108 should turn this baseline into a practical design-partner validation plan that includes, proportionate to current maturity:

1. candidate/design-partner qualification criteria derived from Sections 11–12;
2. a discovery script that tests `ICP-H1` through `SOV-H1` without leading the interviewee;
3. evidence fields for current workflow, management intervention, cycle time, quality/rework, authority/data/tool boundary and economic pain;
4. candidate sourcing/prioritization logic consistent with the Russia-first strategy;
5. continue/change/stop criteria for the first segment hypothesis;
6. a bounded first-engagement concept that creates no unapproved external commitment;
7. explicit separation between discovery evidence, a design-partner agreement and any production/SLA/commercial promise.

AC-108 should prefer a small number of high-information real conversations/observations over a large quantity of superficial “AI interest” responses. Exact sample size is not fixed by AC-107.

## 17. Completion boundary

AC-107 is complete when the Company can state, without pretending to have validated demand:

- who the first plausible customer is;
- who likely has the authority and economic reason to buy;
- what concrete organizational job they are hiring Arvectum to do;
- what bounded first deployment could test that job;
- what operating outcome should improve;
- what quality/authority/safety guardrails must not be traded away;
- what economic logic would make the result worth buying and worth delivering;
- what evidence would falsify the hypotheses;
- what AC-108 must now test in the market.

This publication satisfies that boundary.

Next roadmap action: `AC-108 — First design-partner criteria, discovery script and market-validation plan`.