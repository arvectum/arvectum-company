# AC-507 — Business-Value / Economic Review and Continue-Change-Stop Recommendation

Статус: `Proposed`
Версия: `0.9.0`
Дата: `2026-08-22`
Roadmap item: `AC-507 — Business-value/economic review and continue/change/stop decision`
Milestone: `M5 — First real governed Company operating contour proven`
Workflow: `WF-M5-001 / 1.0.0`
First contour: `PORT-002 — Discount Parser`
Decision authority: Owner / applicable `ROD-04`, with `ROD-02` applying if material capital/spend is later introduced

## 1. Purpose

AC-507 проверяет не техническую корректность workflow, а имеет ли первый governed Company contour достаточную деловую ценность, чтобы продолжать инвестиции, изменить форму или остановить его.

Решение должно опираться на фактические evidence AC-501…AC-506 и отделять:

- observed fact;
- bounded inference;
- unverified hypothesis;
- missing evidence.

Technical PASS, code volume, test count или governance completeness сами по себе не являются economic PASS.

## 2. Current factual baseline

### 2.1 Workflow and authority facts

AC-501…AC-504 established one bounded workflow:

`customer feedback → classification → admitted technical correction → verification → candidate → customer validation`.

Current authority boundary remains:

- POS-002 human-attributable classification/customer gates;
- POS-004 bounded engineering only after valid CL-1 admission;
- no AM-3/AM-4;
- no automatic customer acceptance;
- no automatic customer commitment/deploy/send;
- no additional Arvectum OS reliance for the first M5 proof.

### 2.2 Real operating evidence

AC-505 supplied one real customer-derived case:

`WF-M5-001-20260821-AC505001`.

Observed outcome:

`CL-3 — Evidence insufficient / not reproduced`
→
`W11 — unknown / customer-evidence follow-up required`.

The workflow therefore prevented unsupported conversion of a terse customer symptom into an engineering defect admission.

No customer acceptance, current reproduction, technical fix or revenue outcome is evidenced for this case.

### 2.3 Recovery and reliability evidence

AC-506 established:

- W11 immutable-predecessor / linked-successor recovery mechanics;
- manual case-state reconstruction;
- fresh-process/runtime portability of the helper;
- secret-like evidence rejection;
- duplicate-successor/retry protection.

Remote test evidence:

`14 tests / 14 PASS / 0 failures / 0 errors`.

This supports bounded technical reliability of workflow mechanics. It does not prove product quality, customer satisfaction or Company profitability.

## 3. Value observed

The following value is directly evidenced.

### V1 — Avoided unsupported engineering admission

A real customer symptom existed, but affected build/settings/environment/current reproducibility were not established.

The workflow stopped at CL-3/W11 instead of automatically opening POS-004 correction work.

Observed value:

- scope discipline;
- lower risk of solving the wrong problem;
- explicit uncertainty rather than fabricated certainty;
- preserved customer/product chronology.

Economic magnitude is **unknown** because avoided engineering hours/cost were not measured.

### V2 — Authority separation worked in a real case

AI recommendation did not become the classification decision. The human POS-002 Principal explicitly confirmed CL-3.

Observed value:

- organizational authority remained attributable;
- access/tool capability did not become decision authority;
- no silent AM-3/AM-4 expansion occurred.

### V3 — Customer acceptance was not fabricated

Historical implementation, installer handoff and silence were not converted into acceptance.

Observed value:

- reduced false-closure risk;
- more trustworthy delivery/acceptance state.

### V4 — Reconstructability improved

AC-506 demonstrated that the next safe action can be reconstructed from public-safe/canonical evidence without raw customer payload or active chat/model memory.

Observed value:

- reduced dependence on one session or one executor;
- improved continuity of the operating model.

### V5 — Recovery does not erase provenance

New evidence after W11 creates a linked successor rather than rewriting history.

Observed value:

- auditability;
- lower risk of retry/recovery destroying evidence;
- clearer separation of old uncertainty from new facts.

## 4. Cost and friction observed

### C1 — Human decision remains required at W3

At least one explicit human POS-002 AM-2 classification intervention occurred.

This is intentional at the current maturity stage, but it is still Owner attention cost because the current human Assignment of POS-002 is the Owner.

Exact minutes were not measured and MUST NOT be invented.

### C2 — Evidence handling creates process overhead

The workflow requires:

- protected source references;
- sanitized intake;
- classification rationale;
- state/provenance recording;
- follow-up evidence before technical admission.

This overhead is real. Exact handling time is not yet measured.

### C3 — Governance implementation/recovery work consumed engineering effort

AC-504/AC-506 required helper, tests, runbooks and review work.

The repository evidences the work performed, but the economic cost in Owner hours, AI/tool cost or cash was not captured sufficiently for precise unit economics.

### C4 — Current workflow does not remove the external-evidence bottleneck

When the customer does not provide enough evidence, workflow governance can stop safely but cannot manufacture reproduction evidence.

This means the contour currently improves decision quality more than throughput in evidence-poor customer interactions.

## 5. Missing evidence that prevents a final M5 economic conclusion

The following are still missing or insufficient:

1. a real case progressing through CL-1 → bounded POS-004 correction → verification;
2. explicit customer validation/rework/acceptance after governed handoff;
3. measured Owner time per meaningful case;
4. measured engineering effort avoided or incurred;
5. customer-facing cycle time before/after workflow adoption;
6. measurable AI/tool/runtime cost per case;
7. repeat-case evidence showing whether ceremony falls with reuse;
8. evidence that this workflow improves commercial outcome, retention, margin or support burden;
9. evidence from a second materially distinct case sufficient to test transferability beyond one blocked CL-3 outcome.

These gaps prevent a defensible claim that the workflow is profitable or that M5 is economically proven.

## 6. Economic interpretation

### 6.1 What can be concluded now

The workflow has demonstrated **control value**:

- it prevents unsupported work admission;
- preserves authority and evidence boundaries;
- avoids false customer acceptance;
- reconstructs and recovers safely.

The implementation is technically lightweight:

- Python standard library;
- local/private case storage by default;
- no database/service requirement;
- no new Arvectum OS dependency;
- no new paid infrastructure evidenced as necessary for the current contour.

Therefore the current marginal cash burden of keeping the mechanism available appears low, but exact tool/platform cost is not evidenced and is not asserted as zero.

### 6.2 What cannot be concluded now

It cannot yet be concluded that:

- WF-M5-001 reduces total delivery cost;
- it increases margin/revenue;
- it improves customer satisfaction;
- it should become a generalized platform capability;
- it warrants AM-4/autonomous operation;
- it warrants new headcount, SaaS infrastructure or OS Product Contract work.

## 7. Options

### Option A — STOP

Stop further governed-workflow investment and return to ad hoc customer handling.

Rejected as current recommendation because real evidence already shows useful fail-closed control and reconstructability, while current marginal implementation burden is bounded and no material new infrastructure is required.

### Option B — CONTINUE UNCHANGED

Keep the current workflow exactly as-is and wait for more cases.

Not preferred because AC-505 exposed a concrete friction point: evidence-poor customer feedback can leave the workflow safe but stalled, and Owner burden is not yet measured consistently.

### Option C — CONTINUE WITH CHANGE

Recommended.

Continue WF-M5-001 as the first governed contour, but constrain the next phase to evidence acquisition and friction reduction rather than platform expansion.

Recommended changes:

1. keep CL-3/W11 fail-closed semantics unchanged;
2. use the AC-506 successor mechanism when genuinely new evidence arrives;
3. for the next qualifying case, record lightweight Owner intervention count/minutes from the start;
4. record engineering effort only at coarse practical level sufficient for business review, not timesheet bureaucracy;
5. prefer customer prompts/checklists that ask only for the minimum reproduction/validation evidence needed, without shifting technical selector work to the customer;
6. do not create new CRM/workflow service/database/OS capability merely to complete M5;
7. do not activate AM-3/AM-4;
8. do not generalize the workflow cross-product until at least one case reaches technical execution/customer result and a second materially distinct case supports reuse;
9. review whether W1/W2 evidence capture can be simplified after another real case without weakening customer/data/authority boundaries.

## 8. Recommended Owner decision

**Recommendation: `CONTINUE WITH CHANGE — bounded evidence phase`.**

Exact proposed decision meaning:

- continue WF-M5-001 as the first Company governed workflow;
- preserve current authority/data/customer/OS boundaries;
- authorize no new material spend, customer commitment, AM-3/AM-4 or OS reliance;
- prioritize obtaining one stronger real case and measuring Owner/engineering burden;
- defer platformization/generalization and any profitability claim;
- keep AC-505 open until real customer/reproduction evidence is sufficient;
- treat AC-507 approval as an economic direction decision, not M5 closure while AC-505 evidence remains insufficient.

Because continue/change/stop is a portfolio/investment direction judgment, this recommendation requires explicit Owner approval under applicable ROD-04 semantics.

## 9. Stop / reconsider triggers after approval

If approved, the Company should reconsider or stop additional workflow investment if one or more of the following becomes evidenced:

- repeated cases show governance handling cost materially exceeds avoided rework/control value;
- customer evidence collection becomes a larger bottleneck than the defect work it governs;
- the workflow repeatedly requires Owner interpretation at low-risk routine steps with no measurable benefit;
- a materially simpler process achieves equal authority/data/evidence control;
- real customer/product economics do not justify continued support of the contour;
- the next proof would require material spend, new external commitment, AM-3/AM-4 or unadmitted OS reliance without a separate decision.

## 10. Non-effects

This proposal does not:

- approve itself;
- close AC-505 or M5;
- claim customer acceptance or profitability;
- create budget or material spend authority;
- authorize customer commitment/deploy/send;
- activate AM-3/AM-4;
- create new Position/Assignment/access;
- create Arvectum OS Product Contract/capability/reliance;
- convert hypotheses into measured economics.
