# AC-407 — Management Operating Cadence and M4 Control Review

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-407 — Management operating cadence and control review`
Предшественники: `AC-401…AC-406 — Approved 1.0.0`; `M1…M3 — Complete / PASS`
Evidence snapshot: `docs/operations/OWNER-MISSION-CONTROL-REFERENCE-SNAPSHOT-2026-08-21.md`, blob `09b056e99ecb066402bc1d2b12d2dab772898f1b`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal and M4 closure result`

## 1. Назначение

AC-407 завершает M4 не ещё одним абстрактным control layer, а проверкой того, можно ли использовать уже утверждённые AC-401…AC-406 как **пропорциональный operating cadence** без превращения governance в основную работу Company.

Review отвечает на четыре практических вопроса:

1. что должно обновляться немедленно по событию, а что требует только календарного backstop;
2. какие реальные Owner acts можно отделить от preparation/publication/routine execution;
3. какие M4 claims уже подтверждены actual repository traces, а какие остаются empirical gaps;
4. достаточно ли evidence, чтобы закрыть `M4 — Owner control and reference-implementation observability established` и перейти к первому реальному governed Company workflow в M5.

Главный принцип:

```text
control exists to reduce business/authority/reconstruction risk
≠
governance ceremony exists for its own sake
```

## 2. Evidence base actually observed

AC-407 использует не только approved design artifacts, но и следующие observed traces.

### 2.1 Repeated governance execution trace

AC-401…AC-406 последовательно прошли реальный workflow:

```text
AI-assisted evidence/proposal preparation
→ proportional cross-review
→ stop at explicit Owner gate
→ attributable Owner approval
→ bounded repository publication/state synchronization
→ read-after-write verification
→ next canonical action
```

Эта последовательность многократно наблюдалась в canonical repository через отдельные proposal/review/decision/publication/roadmap/source-registry commits.

Она поддерживает bounded operational claim:

**material governance decision authority и low-risk preparation/publication mechanics реально разделены в одном действующем Company workflow class.**

Это соответствует AC-205 `POS-001` hybrid Assignment: Owner как human Position holder; AI — advisory/cross-review и bounded publication/state assistance.

### 2.2 First AC-406 projection instantiated

Для AC-407 создан public-safe reference snapshot:

`docs/operations/OWNER-MISSION-CONTROL-REFERENCE-SNAPSHOT-2026-08-21.md`

blob `09b056e99ecb066402bc1d2b12d2dab772898f1b`.

Он показал, что owner-facing projection можно сформировать без:

- создания нового authority namespace;
- публикации confidential financial/customer/security payload;
- ложного заявления, что unknown = safe;
- автоматического re-ranking portfolio;
- смешения recommendation / approval / execution.

Но snapshot одновременно честно показал, что public contour не доказывает полноту live obligations, current cash/liquidity, risks/incidents или restricted customer/accounting facts.

### 2.3 Continuity evidence remains bounded

AC-207 имеет Approved continuity modes/evidence levels, но explicit current gaps остаются unresolved/untested, включая Owner replacement, credential recovery, GitHub↔GitVerse/local reconciliation drill, AI-runtime swap, accounting-provider replacement и customer continuity packet.

Следовательно M4 не может использовать `continuity designed` как `continuity operationally proven`.

### 2.4 Business/portfolio evidence remains separate

`PORTFOLIO.md` остаётся Company portfolio truth для identity/treatment/priority. Product/customer/accounting systems остаются authoritative для implementation, acceptance, revenue/cash и иных фактов.

M4 control evidence не доказывает profitability, market validation или customer readiness.

## 3. AC-407 operating cadence

Cadence строится как `event-driven first + minimum calendar backstops`.

### 3.1 Event-driven controls — обязательны при material change

Немедленный bounded update/review требуется при:

- новом или materially changed `P0` obligation/cash/material-risk condition;
- material new/changed obligation or customer/vendor/legal commitment;
- `DEC/APR/ESC` case, где появился/изменился actual authority gate;
- material `RSK/EXC/INC` creation/change/expiry/recovery condition;
- material cash/liquidity/receivable/payable/procurement cash-gap change, влияющем на решение;
- material portfolio trigger по AC-405;
- Company↔Product↔Arvectum OS boundary/dependency proposal;
- evidence becoming materially stale/conflicted before consequential decision;
- incident or changed fact, invalidating prior approval/recommendation.

Event-driven control не означает Owner meeting. Сначала accountable Position/update mechanics; Owner вовлекается только при actual Owner authority/action need.

### 3.2 Active-week Owner control checkpoint

Initial operating default:

**не более одного короткого asynchronous Owner control checkpoint за активную операционную неделю, и только если существует material Company state, который полезно агрегировать.**

Checkpoint использует AC-406 sections:

- Protect Now;
- Owner Action Required;
- material delegated exceptions;
- finance/obligation signals;
- portfolio triggers;
- reference-evidence deltas where relevant.

Если material state не изменился и Owner action отсутствует, отдельный meeting/file/approval не нужен.

Это backstop, а не обязательство читать dashboard ежедневно.

### 3.3 Monthly integrated management checkpoint

Initial operating default — **один asynchronous monthly management checkpoint**, объединяющий то, что не требует отдельной церемонии:

1. AC-404 management-finance summary from available authoritative accounting/bank/obligation sources;
2. AC-405 monthly portfolio exception scan;
3. review of open material obligations/decisions/risks/incidents whose next control point falls in the period;
4. control-burden check: repeated false Owner alerts, stale manual assembly, duplicated state or routine escalation.

Это не transaction reconciliation и не повторный full review всех products/records.

Monthly checkpoint MAY be one concise artifact/projection. Owner approval нужен только для exact material cases, а не для самого факта просмотра.

### 3.4 Quarterly integrated revalidation

Один quarterly backstop объединяет:

- AC-405 portfolio integrated revalidation;
- material continuity/dependency review for open Company-critical gaps;
- review of whether AC-401…AC-406 semantics still fit current scale;
- review of Owner attention burden and false-positive/false-negative routing;
- cadence frequency adjustment proposal if actual evidence supports it.

Quarterly review не является automatic Owner meeting и не заменяет event-driven response.

### 3.5 No mandatory daily ceremony

AC-407 не вводит daily standup, daily dashboard acknowledgement или обязательный daily financial/risk review.

При current Company scale это было бы unsupported process precision и risk of governance overhead.

## 4. Source update cadence

Cadence относится не только к meetings/reviews, но и к state freshness.

### WORK / OBL

Update on material state/next-control-point/due/source change. Routine lower-level task progress не копируется автоматически.

### DEC / APR / ESC

Update when decision question, evidence readiness, authority basis, outcome, approval act, expiry or execution handoff materially changes.

### RSK / EXC / INC

Update on material exposure/exception/incident lifecycle change; noisy technical alerts remain lower-level until qualification gate satisfied.

### Finance

Refresh before material financial/commitment decision and on material source change; monthly management checkpoint is the initial calendar backstop. Exact bank/accounting truth remains source-owned.

### Portfolio

AC-405 event-driven + monthly exception scan + quarterly integrated revalidation remains unchanged.

### Mission Control

Projection refreshes when material underlying state changes, before an Owner decision, or at the active-week/monthly backstop. It is not required to be real-time if the source itself is not real-time and consequence does not require it.

## 5. Owner attention routing

Owner attention is reserved for:

- applicable `ROD-*` decisions;
- legal/corporate acts in the Owner/participant/General Director capacity where actually required;
- residual authority cases without valid delegation;
- material exception/risk acceptance;
- material capital/external-commitment/portfolio/boundary decisions;
- escalations where delegated envelope is exceeded or evidence is insufficient.

Owner SHOULD NOT be routed:

- routine `AM-1`/`AM-2` work;
- healthy delegated execution;
- lower-level technical warnings;
- read-only informational updates;
- `waiting_external` states with no actionable Owner lever;
- publication/synchronization mechanics after an already explicit act.

## 6. Material control-burden finding

The M4 build sequence intentionally used heavy proposal/cross-review/approval/publication discipline because it was creating durable governance from scratch.

AC-407 explicitly rejects carrying that full ceremony into routine operation.

Rule after M4:

```text
routine bounded execution
→ use existing approved envelope

material/reserved durable change
→ prepare evidence + exact authority gate

boundary exceeded / unknown material evidence
→ escalate or fail closed
```

A routine Company record update does not need a new RFC-like review or Owner approval unless its substance crosses an actual authority/governance boundary.

## 7. Software/UI decision

Current evidence does **not** justify a new standalone Company dashboard project.

Reason:

- AC-406 semantic model can be instantiated in Markdown/structured projection;
- one public-safe snapshot is already reconstructable;
- no repeated-use evidence yet shows that manual projection burden, latency or error rate requires software;
- current Arvectum OS P9.07/P9.10 path is still evolving and does not create a Company Product Contract by implication.

Decision for M4:

`no new software Mission Control requirement`.

Software/OS composition may be revisited after actual M5/M6 operating traces show a concrete burden/value case.

## 8. AC-405 cadence review result

No evidence currently justifies changing the Approved AC-405 defaults:

- event-driven scoped review;
- monthly asynchronous exception scan;
- quarterly integrated revalidation.

They are therefore **reaffirmed as initial defaults**, with one integration improvement: monthly portfolio scan should normally be combined with the monthly management checkpoint instead of creating a separate Owner ceremony.

## 9. Reference-implementation claims: what is proven now

### 9.1 Supported claims

1. **Authority separation — observed in governance workflow.** Proposal/recommendation and cross-review did not become approval; explicit Owner acts preceded approved publications.
2. **Bounded AI/software execution — observed in governance preparation/publication workflow.** AI/software performed preparation, cross-review and repository synchronization without becoming authority source.
3. **Fail-closed at Owner gate — observed in governance workflow.** AC-401…AC-406 did not publish approved versions before explicit Owner acts.
4. **Provenance/reconstructability — strongly observed.** Proposal/review/decision/publication chains use immutable blobs and commits.
5. **Owner clerical separation — observed.** After Owner act, repository synchronization did not require Owner manual file editing.
6. **Mission Control semantic projection — instantiated.** Public-safe snapshot preserves unknown/restricted/source distinctions.

### 9.2 Not yet proven

- measured reduction in Owner time/reconstruction burden;
- complete live `WORK/OBL/DEC/APR/ESC/RSK/EXC/INC` population;
- current cash/liquidity/receivable/payable completeness;
- broad AI execution quality/cost/reliability;
- actual POS-004 runtime replacement;
- Company-wide continuity/recovery readiness;
- direct revenue/profit/customer outcome caused by M4 controls;
- repeatable customer/commercial governed operating contour;
- profitability, market validation, legal compliance or production readiness.

These gaps are not M4 design failures. They are empirical evidence targets for real operations, especially M5/M6.

## 10. M4 exit review

AC-407 assesses the current M4 exit criteria as follows.

| Criterion | Result | Evidence / limitation |
|---|---|---|
| reliable owner-facing material-state view exists | `PASS in bounded reference scope` | AC-406 + instantiated snapshot; restricted/live completeness not claimed |
| Owner actions separated from routine delegated execution | `PASS for observed governance workflow` | repeated approval→publication chains |
| control layers avoid parallel source-of-truth claims | `PASS` | AC-401…AC-406 source boundaries align |
| stale/unknown/conflicted evidence not masked as ready | `PASS in model + snapshot evidence` | snapshot explicitly marks finance/obligation unknowns |
| reference claims limited to actual evidence | `PASS` | supported vs unproven claims separated |
| cadence proportional to current scale | `PASS with initial defaults` | event-driven first; active-week only if material state; monthly integrated; quarterly backstop |
| empirical gaps explicitly carry forward | `PASS` | Section 9.2 / Section 12 |

Conclusion:

**M4 can be closed `Complete / PASS` if Owner explicitly approves this exact reviewed AC-407 result.**

The closure means the Company has a coherent owner-control/reference-observability system and a proportional operating cadence. It does not mean that all live data is populated or that business/AI/continuity effectiveness is already proven.

## 11. Next roadmap action after M4

The preserved canonical roadmap sequence defines Phase 5:

`M5 — First real governed Company operating contour proven`.

First action:

`AC-501 — First governed workflow candidate selection`.

AC-501 must select the smallest high-value repeatable real Company workflow from actual M1/M2/M3 evidence using business value, workload, repeatability, risk, reversibility, evidence quality and Owner-time reduction. The workflow is not predetermined by AC-407.

AC-407 does not silently nominate Company governance publication, Tender Agent, Discount Parser or any other workflow as the M5 candidate.

## 12. Explicit carry-forward gaps

After M4 closure the following remain open evidence requirements, not hidden blockers:

1. live population/completeness of material control records must be proven through actual work rather than assumed;
2. decision-relevant cash/commitment evidence must come from current authoritative sources at decision time;
3. Owner workload reduction needs observed/repeated measurement, not design inference;
4. continuity/replacement gaps from AC-207 require future drills where business value/risk justifies them;
5. AI execution quality/cost/reliability and runtime replacement require M5/M6 evidence;
6. portfolio economics/customer validation remain product/business evidence questions;
7. Mission Control software/UI remains deferred until repeated-use burden provides a business case;
8. current OS M9-alpha/P9.07/P9.10 state creates no Company Product Contract/capability/authority by implication.

## 13. Current Arvectum OS boundary

For AC-407, `arvectum/arvectum-os` `main` was re-checked at:

`76504766353028540891ac1dfdbf1e5dc331a4af`.

OS roadmap remains `2.81.0`; M9-alpha is Achieved/PASS only in exact private internal scope; P9.07 is Current; P9.10 is Planned; no Stable Product Contract or Active Platform Capability is inferred.

AC-407 creates no cross-repository implementation commitment.

## 14. Non-effects

Even if Approved, AC-407/M4 closure does not:

- create budget, spend/payment/signing authority or financing;
- create customer/vendor/legal obligation;
- assert current cash, liquidity or absence of liabilities;
- approve risk exceptions beyond an exact separate authority act;
- create a live bank/accounting/customer integration;
- require a new dashboard/software platform;
- change any `PORT-*` disposition/band/module classification;
- change product roadmaps or implementation status;
- create Arvectum OS Product Contract/capability lifecycle state;
- prove profitability, market validation, customer readiness, legal compliance or production readiness;
- prove Company-wide AI autonomy or continuity readiness;
- close M5/M6 or preselect their candidates.

## 15. Approval gate

This proposal recommends:

- `AC-407 — Complete / PASS`;
- `M4 — Complete / PASS`;
- next canonical action `AC-501 — First governed workflow candidate selection`;
- empirical gaps from Section 12 carried forward without false closure.

These effects require explicit attributable Owner approval of the **exact reviewed proposal**.

Cross-review PASS is not Owner approval.