# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.43.0`
Создано: `2026-08-19`
Обновлено: `2026-08-22`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-505 — Supervised real-operation proof`
Параллельно: `AC-507 — Business-value/economic review — Owner decision gate`
Завершено параллельно: `AC-506 — Incident, uncertain-outcome, recovery and fallback drill`

## 1. Модель публикации

Эта редакция `0.43.0` сохраняет содержание `0.42.0`, не изменяет незавершённые authority/evidence gates и добавляет сводный master-index M0–M9 и явные доступные пути реализации по аналогии с roadmap-control практикой Arvectum OS / Proxy Launcher.

Предыдущая редакция:

- версия: `0.42.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `57eaca14aae1eeb681b16e5f5cded36ad4a8f8da`.

Все ранее определённые Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop, AC-501 workflow selection, AC-502 workflow contract, AC-503 no-additional-OS-reliance decision и конечный AC-901 сохраняются, если прямо не изменены более новым approved decision или этой canonical roadmap publication в пределах planning authority.

Этот ChatGPT-чат может использоваться как основной рабочий/control thread по дорожной карте: здесь удобно запрашивать статус, выбирать следующий шаг и инициировать выполнение. Durable canonical planning source остаётся этот repository artifact; существенные изменения, решения и фактические статусы должны быть promoted/reconciled сюда, поскольку chat history сама по себе не является независимым canonical decision record.

## 2. AC-505 — текущий реальный operating proof

`AC-505 — Supervised real-operation proof` остаётся:

`Current / external evidence wait`.

Первый real customer case:

`WF-M5-001-20260821-AC505001`.

Фактический outcome:

`W3 — CL-3 Evidence insufficient / not reproduced`
→
`W11 — unknown / customer-evidence follow-up required`.

Public-safe evidence:

- `docs/operations/AC-505-SUPERVISED-REAL-OPERATION-ADMISSION-EVIDENCE.md` — current version `0.3.0`;
- `docs/operations/AC-505-WF-M5-001-20260821-AC505001-EVIDENCE.md` — `1.0.0`;
- `docs/reviews/AC-505-SUPERVISED-REAL-OPERATION-ADMISSION-CROSS-REVIEW.md` — `1.2.0`, `10 of 10`.

Human-attributable POS-002 classification was explicitly confirmed as:

`CL-3 — Evidence insufficient / not reproduced`.

No POS-004 technical correction was admitted. No customer acceptance was inferred. The real case remains fail closed pending new authoritative reproduction/customer evidence.

AC-505 does not block independent bounded Company work that does not pretend to be AC-505 customer evidence.

## 3. AC-506 — завершённый recovery/fallback drill

`AC-506 — Incident, uncertain-outcome, recovery and fallback drill`:

`Complete / PASS`.

Canonical artifacts:

- `tools/wf_m5_001_recovery.py`;
- `tests/test_wf_m5_001_recovery.py`;
- `.github/workflows/wf-m5-001-case.yml`;
- `docs/operations/WF-M5-001-RECOVERY-FALLBACK-RUNBOOK.md` — `Active 1.0.0`;
- `docs/operations/AC-506-INCIDENT-UNCERTAIN-OUTCOME-RECOVERY-FALLBACK-DRILL-EVIDENCE.md` — `Complete / PASS 1.0.0`;
- `docs/reviews/AC-506-INCIDENT-UNCERTAIN-OUTCOME-RECOVERY-FALLBACK-CROSS-REVIEW.md` — `10 of 10`, PASS.

Remote fresh-runtime evidence:

- PR `#8 — AC-506 — recovery drill validation`;
- workflow run `32555014701`;
- job `96987697988`;
- Ubuntu 24.04 / CPython 3.12.14;
- `14 tests / 14 PASS / 0 failures / 0 errors`.

Narrow evidence after AC-506:

- W11 successor recovery mechanics → `CE-3`;
- case-state/manual fallback reconstruction → `CE-3`;
- helper/process portability → `CE-3`;
- real insufficient-evidence fail-closed behavior → `CE-2`.

No Company-wide DR, Owner-independent continuity, actual POS-004 AI model/runtime swap, credential/signing/provider recovery or customer-system recovery is claimed.

## 4. AC-507 — business/economic review prepared

`AC-507 — Business-value/economic review and continue/change/stop decision` имеет статус:

`Current / Owner decision gate`.

Prepared proposal:

- `docs/business/AC-507-BUSINESS-VALUE-ECONOMIC-REVIEW.md` — `Proposed 0.9.0`.

Cross-review:

- `docs/reviews/AC-507-BUSINESS-VALUE-ECONOMIC-REVIEW-CROSS-REVIEW.md` — `10 of 10`, `PASS for Owner decision gate`.

Observed value supported by current evidence:

- unsupported engineering admission was avoided on a real CL-3 case;
- human Organizational Authority remained attributable;
- customer acceptance was not fabricated from silence/technical evidence;
- bounded case state is reconstructable without active model/session memory;
- recovery preserves immutable predecessor provenance.

Observed/known costs and friction:

- current POS-002 human gate consumes Owner attention;
- evidence normalization/state handling has process overhead;
- AC-504/AC-506 implementation/review required engineering effort;
- workflow cannot manufacture missing customer reproduction evidence.

Not yet measured sufficiently:

- Owner minutes per case;
- engineering effort avoided/incurred;
- per-case tool/runtime cost;
- customer cycle-time effect;
- margin/revenue/customer-satisfaction impact.

Therefore no profitability claim is supported.

## 5. AC-507 recommendation

Reviewed recommendation:

**`CONTINUE WITH CHANGE — bounded evidence phase`.**

Meaning:

1. continue WF-M5-001 as the first governed Company workflow;
2. preserve CL-3/W11 fail-closed, current authority/data/customer/OS boundaries;
3. use linked-successor recovery only on genuinely new evidence;
4. measure lightweight Owner intervention count/minutes in the next qualifying case;
5. capture coarse practical engineering-effort evidence where applicable;
6. reduce evidence-handling ceremony where another real case proves simplification safe;
7. do not create new CRM/workflow service/database/OS capability merely to complete M5;
8. do not activate AM-3/AM-4;
9. defer cross-product generalization/platformization until stronger real evidence exists.

The recommendation is reversible and introduces no material spend by itself.

Because continue/change/stop affects portfolio/investment direction, the recommendation requires explicit Owner approval under applicable ROD-04 semantics.

Exact proposed Owner wording:

`AC-507: CONTINUE WITH CHANGE — bounded evidence phase — утверждаю`.

## 6. Status milestones

- `M0 — Company canonically founded` — `Complete / PASS`;
- `M1 — Business/economic reality and first market-validation plan captured` — `Complete / PASS`;
- `M2 — Arvectum Company reference operating model and authority established` — `Complete / PASS`;
- `M3 — Product/module-candidate portfolio governed as investments` — `Complete / PASS`;
- `M4 — Owner control and reference-implementation observability established` — `Complete / PASS`;
- `M5 — First real governed Company operating contour proven` — `Current`;
- `M6 — First real AI-held Position proven economically and operationally` — `Planned`;
- `M7 — First external AI-company design-partner deployment proven` — `Future`;
- `M8 — Repeatable multi-customer AI-company product proven and scalable` — `Future`;
- `M9 — Final human-readable Russian reconciliation` — `Future / final planned reconciliation stage after M8 unless Owner changes sequence`.

## 7. Master work-item index

### Phase 0 / M0 — Founding and canonical boundary — COMPLETE

| ID | Work item | Status |
|---|---|---|
| `AC-001` | Company Constitution / Founding Charter | `Complete / PASS` |
| `AC-002` | Company ↔ Arvectum OS authority and responsibility boundary | `Complete / PASS` |
| `AC-003` | Canonical repository structure and artifact map | `Complete / PASS` |
| `AC-004` | Initial `docs/portfolio/PORTFOLIO.md` | `Complete / PASS` |
| `AC-005` | Founding baseline cross-review and closure | `Complete / PASS` |

### Phase 1 / M1 — Business reality, economics and early market evidence — COMPLETE

| ID | Work item | Status |
|---|---|---|
| `AC-101` | Current business model and value proposition baseline | `Complete / PASS` |
| `AC-102` | Revenue, cash, recurring cost and obligation baseline | `Complete / PASS` |
| `AC-103` | Current customer/client lifecycle and real value-stream map | `Complete / PASS` |
| `AC-104` | Owner workload, manual work and bottleneck map | `Complete / PASS` |
| `AC-105` | Material risk, dependency, continuity and fallback baseline | `Complete / PASS` |
| `AC-107` | Flagship ICP, buyer, job-to-be-done and measurable outcome hypotheses | `Complete / PASS` |
| `AC-108` | First design-partner criteria, discovery script and market-validation plan | `Complete / PASS` |
| `AC-106` | M1 business baseline review and Owner priority decision | `Complete / PASS` |

### Phase 2 / M2 — Reference operating model and authority — COMPLETE

| ID | Work item | Status |
|---|---|---|
| `AC-201` | Minimal real organizational/function model | `Complete / PASS` |
| `AC-202` | Reserved Owner Decisions | `Complete / PASS` |
| `AC-203` | Delegated Position authority, approval and escalation model | `Complete / PASS` |
| `AC-204` | Initial Position Registry | `Complete / PASS` |
| `AC-205` | Initial Assignments and executor classification | `Complete / PASS` |
| `AC-206` | Company data/tool/credential access boundary baseline | `Complete / PASS` |
| `AC-207` | Critical-function continuity, replacement and manual fallback baseline | `Complete / PASS` |
| `AC-208` | Reference-model transferability boundary and operating-model cross-review | `Complete / PASS` |

### Phase 3 / M3 — Product and reusable module-candidate governance — COMPLETE

| ID | Work item | Status |
|---|---|---|
| `AC-301` | Portfolio product/node identity and ownership reconciliation | `Complete / PASS` |
| `AC-302` | Accountable Position for each active product/initiative | `Complete / PASS` |
| `AC-303` | Investment, cost/risk boundary and stop/continue criteria | `Complete / PASS` |
| `AC-304` | Standalone product vs reference implementation vs module-candidate vs OS-capability boundary | `Complete / PASS` |
| `AC-305` | Cross-product/module dependencies and Product Contract reconciliation | `Complete / PASS` |
| `AC-306` | Portfolio/module prioritization and capital/Owner-attention model | `Complete / PASS` |
| `AC-307` | Portfolio/module governance review and closure | `Complete / PASS` |

### Phase 4 / M4 — Owner control and reference observability — COMPLETE

| ID | Work item | Status |
|---|---|---|
| `AC-401` | Company work/obligation register model | `Complete / PASS` |
| `AC-402` | Decision, approval and escalation register model | `Complete / PASS` |
| `AC-403` | Risk, exception and incident register model | `Complete / PASS` |
| `AC-404` | Cash, commitment and management reporting baseline | `Complete / PASS` |
| `AC-405` | Portfolio/module/priority review cadence | `Complete / PASS` |
| `AC-406` | Owner Mission Control / reference-implementation evidence view | `Complete / PASS` |
| `AC-407` | Management operating cadence and control review | `Complete / PASS` |

### Phase 5 / M5 — First governed Company operating contour — CURRENT

| ID | Work item | Status |
|---|---|---|
| `AC-501` | First governed workflow candidate selection | `Complete / PASS` |
| `AC-502` | Workflow, accountable Position, authority/data/evidence contract | `Complete / PASS` |
| `AC-503` | Arvectum OS reliance/admission mapping where applicable | `Complete / PASS` |
| `AC-504` | Bounded workflow implementation | `Complete / PASS` |
| `AC-505` | Supervised real-operation proof | `Current / external evidence wait` |
| `AC-506` | Incident, uncertain-outcome, recovery and fallback drill | `Complete / PASS` |
| `AC-507` | Business-value/economic review and continue/change/stop decision | `Current / Owner decision gate` |

Earlier planning contained a possible `AC-508 — reusable module candidate package or explicit non-reuse decision`. Current M5 sequencing deliberately stops at AC-507 pending empirical evidence and Owner direction; AC-508 is therefore **not active** and must be re-admitted/re-scoped before execution rather than assumed.

### Phase 6 / M6 — First real AI-held Position — PLANNED

| ID | Work item | Status |
|---|---|---|
| `AC-601` | AI delegation candidate selection from real workload | `Planned` |
| `AC-602` | Position business case and unit-economics/workload evidence | `Planned` |
| `AC-603` | Assignment, authority, runtime, tools and data boundary | `Planned` |
| `AC-604` | Quality/evaluation, cost and risk gates | `Planned` |
| `AC-605` | Supervised AI Position pilot | `Planned` |
| `AC-606` | Human/software fallback and executor-replacement proof | `Planned` |
| `AC-607` | Value, Owner-workload, module-reuse and risk review | `Planned` |

M6 may begin only when the M5 evidence/Owner direction is sufficient to select a real delegation candidate without inventing workload or authority.

### Phase 7 / M7 — First external AI-company design-partner deployment — FUTURE

| ID | Work item | Status |
|---|---|---|
| `AC-701` | Select first design partner from AC-108 evidence | `Future` |
| `AC-702` | Customer business/value-stream/obligation discovery | `Future` |
| `AC-703` | Customer functions, Positions, authority and escalation model | `Future` |
| `AC-704` | Customer data/security/sovereignty/access boundary | `Future` |
| `AC-705` | Module configuration, gap analysis and customer-specific module scope | `Future` |
| `AC-706` | Arvectum OS Product Contract/reliance/admission mapping | `Future` |
| `AC-707` | Bounded supervised customer deployment | `Future` |
| `AC-708` | Acceptance, support, continuity, replacement and portability proof | `Future` |
| `AC-709` | Customer-value, implementation-economics and continue/change/stop review | `Future` |

### Phase 8 / M8 — Repeatable multi-customer AI-company product — FUTURE

| ID | Work item | Status |
|---|---|---|
| `AC-801` | Standard discovery and organization-configuration methodology | `Future` |
| `AC-802` | Reusable organizational pattern/blueprint library without fixed org-chart cloning | `Future` |
| `AC-803` | Governed module catalog, versioning, compatibility and retirement model | `Future` |
| `AC-804` | Packaging, pricing, implementation and support unit economics | `Future` |
| `AC-805` | Deployment, upgrade, migration, backup, exit and portability path | `Future` |
| `AC-806` | Multi-customer isolation, security, privacy and rights model | `Future` |
| `AC-807` | Sales/onboarding/implementation capacity model | `Future` |
| `AC-808` | Second/third customer repeatability evidence | `Future` |
| `AC-809` | Scale review and capital/organization decision | `Future` |

### Phase 9 / M9 — Final Russian reconciliation — FUTURE

`AC-901` remains the final planned human-readable Russian reconciliation stage after M8 unless the Owner changes sequence. Its exact detailed scope/title must be activated from then-current Company evidence rather than invented prematurely. Expected purpose: reconcile the final human-readable Company model, roadmap, portfolio, operating/governance semantics and terminology after the preceding evidence-producing phases.

## 8. Available implementation paths now

The roadmap distinguishes **canonical next step**, **parallel available work** and **future planned work**.

### A. Canonical authority-gated step — available immediately

`AC-507 — Owner decision` can be completed immediately because the proposal and `10/10` cross-review already exist.

Required explicit wording for the reviewed recommendation:

`AC-507: CONTINUE WITH CHANGE — bounded evidence phase — утверждаю`.

This approves direction only. It does not close M5, fabricate AC-505 evidence, authorize material spend, expand authority, activate AM-3/AM-4 or create new OS reliance.

### B. Canonical empirical step — waiting on external evidence

`AC-505` remains valid and open. The current case can resume when one or more of these appears:

- exact affected build/version;
- exact source/settings/environment sufficient for reproduction;
- current reproduction result;
- explicit new customer validation/rework evidence.

A different real customer feedback item may be selected if it can traverse WF-M5-001 more completely without expanding scope/authority/data boundaries.

### C. Parallel evidence-generating work — available without pretending to close M5

The following are available now when separately authorized and economically justified:

1. **AC-108 market-validation execution** — run the already approved bounded design-partner discovery loop; this is market evidence, not a pilot/customer commitment.
2. **M5 measurement instrumentation/lightweight evidence capture** — Owner intervention count/minutes, coarse engineering effort, tool/runtime cost and cycle/rework evidence on the next qualifying case.
3. **Current real product/client work** in their own repositories where it produces revenue, customer value or material evidence.
4. **Arvectum OS roadmap work** independently of M5, provided Company does not create hidden cross-repository commitments.
5. **Portfolio review/cadence execution** under already approved M3/M4 governance when new product evidence materially changes priorities.

### D. Next planned construction step after sufficient M5 direction/evidence

`AC-601 — AI delegation candidate selection from real workload` is the first designed M6 step.

It should not be started merely to keep the roadmap moving. Start when real evidence is sufficient to identify a Position/function where AI delegation has a credible workload/economic/control case and does not require invented authority.

### E. Future market/product path

M7/M8 remain designed but inactive. They become implementation candidates only after the internal model, first AI-held Position and market evidence justify external deployment/productization.

## 9. Recommended execution order from current state

Unless P0 obligation/risk/cash work preempts it:

1. obtain explicit AC-507 Owner decision;
2. keep AC-505 open and resume it on the first valid real evidence/case;
3. in parallel, run bounded AC-108 discovery if suitable candidate access exists;
4. on the next qualifying WF-M5-001 case, measure Owner time and coarse economic friction/value;
5. close/revise M5 only from combined real evidence, not from technical PASS;
6. then activate AC-601 if M5 supports continued AI delegation;
7. do not jump to external M7 deployment merely because internal technical/governance artifacts are complete.

## 10. AC-505 next evidence

Current next valid evidence for the existing case is one or more of:

- exact affected build/version;
- exact source/settings/environment reference sufficient for reproduction;
- current reproduction result;
- new explicit customer validation/rework evidence.

Until such evidence exists, case `WF-M5-001-20260821-AC505001` remains W11 and no POS-004 correction is admitted.

A different real customer feedback item may also be selected if it can progress further through WF-M5-001 without violating scope/authority/data boundaries.

## 11. AC-507 approval does not close M5

Even if the Owner approves `CONTINUE WITH CHANGE`, M5 remains open while the evidence set is insufficient.

M5 can close only after combined evidence is sufficient, including:

- real operation/customer outcome evidence from AC-505 or accepted equivalent factual case outcome;
- uncertainty/failure/recovery evidence supplied by AC-506;
- Owner burden evidence;
- technical/AI quality, cost and reliability evidence where applicable;
- authorized AC-507 continue/change/stop direction.

AC-507 approval is an economic direction decision, not customer acceptance, profitability proof or M5 closure.

## 12. Stop/reconsider direction

If `CONTINUE WITH CHANGE` is approved, later evidence should trigger reconsideration where:

- governance handling cost materially exceeds avoided rework/control value;
- customer evidence collection becomes a larger bottleneck than the work governed;
- routine low-risk steps repeatedly require Owner interpretation without measurable benefit;
- a materially simpler process achieves equal control;
- real economics do not justify continued support;
- additional progress would require material spend, new external commitment, AM-3/AM-4 or unadmitted OS reliance.

## 13. Authority and boundary rule

Roadmap does not create Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant, production approval or OS lifecycle transition.

AC-504/AC-506 mechanics may execute only inside approved AC-202…AC-207, AC-502 and AC-503 boundaries. Runtime/process recovery does not transfer authority, and synthetic drill evidence may never be represented as real customer evidence.

AC-507 proposal/cross-review do not approve the recommended economic direction. Explicit Owner action is required.