# AC-406 — Owner Mission Control / Reference-Implementation Evidence View

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-406 — Owner Mission Control / reference-implementation evidence view`
Предшественники: `M2 — Complete / PASS`; `M3 — Complete / PASS`; `AC-401…AC-405 — Approved 1.0.0`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение

AC-406 определяет минимальное owner-facing **derived evidence view** — Owner Mission Control — поверх уже утверждённых Company control/evidence layers.

Цель — убрать выявленный AC-104 `MW-6 / B-7 state reconstruction bottleneck`: собственник не должен вручную собирать из чатов, репозиториев, локальных сред и внешних систем ответ на вопросы:

1. что реально угрожает обязательствам, cash, customer outcome или continuity сейчас;
2. какое **точное действие собственника** требуется и почему именно сейчас;
3. какая работа уже может продолжаться без собственника в действующих `AM-*`/Assignment bounds;
4. какие material decisions/approvals/escalations остаются открыты;
5. какие risk/exception/incident и financial signals требуют внимания, а какие являются routine Position work;
6. что существенно изменилось в portfolio/module/priority state;
7. какие факты stale/unknown/contested и поэтому ограничивают решение;
8. какие evidence действительно показывают, что Arvectum Company работает как AI-native owner-controlled organization, а не только описана governance-документами.

Главный принцип:

```text
Mission Control = derived evidence projection
Mission Control ≠ source of truth
Mission Control ≠ authority
Mission Control ≠ approval
Mission Control ≠ execution
Mission Control ≠ business readiness proof
```

AC-406 не создаёт новый register namespace и не делает software dashboard обязательным.

## 2. Governing baseline

Owner Mission Control строится только поверх уже действующих source/control boundaries.

### 2.1 Company control inputs

Mission Control MAY project:

- `WORK-*` / `OBL-*` — AC-401;
- `DEC-*` / `APR-*` / `ESC-*` — AC-402;
- `RSK-*` / `EXC-*` / `INC-*` — AC-403;
- AC-404 cash/commitment/management-finance projection;
- `PORT-*` + AC-405 portfolio review state;
- `POS-*`, Assignments, authority/access/continuity evidence where decision-relevant;
- product, customer, accounting/bank, legal/corporate, security and Arvectum OS references where their facts materially affect Company control.

Mission Control не вводит `MC-*`, `DASH-*`, `ALERT-*` или другой новый authority/control identity namespace.

### 2.2 Owner workload boundary

AC-104 уже установил, что Owner должен сохранять control, но не быть scheduler/memory layer для routine work. Поэтому Mission Control оптимизируется не под полноту данных, а под **decision relevance + exception visibility + reconstructability**.

Owner не должен получать:

- каждый task/commit/test;
- каждую бухгалтерскую строку;
- каждый низкоуровневый alert;
- каждый product-local bug;
- каждый routine AM-2 choice;
- raw AI chain-of-thought;
- raw confidential payload только ради удобства dashboard.

## 3. Source / interpretation / authority separation

Каждый material элемент Mission Control должен позволять восстановить, что именно отображается.

Обязательное смысловое разделение:

```text
source fact
≠ Company interpretation
≠ recommendation
≠ decision
≠ approval
≠ legal/corporate/customer act
≠ technical authorization
≠ execution evidence
```

### 3.1 `source fact`

Факт из authoritative source в его scope: contract/customer/accounting/bank/product/security/OS/corporate etc.

### 3.2 `Company interpretation`

Bounded Company control meaning: materiality, priority context, linked `OBL/RSK/DEC/PORT`, Owner attention, next control point.

### 3.3 `recommendation`

Подготовленный Position/AI/human option or preferred course. Не является решением.

### 3.4 `decision / approval`

Только attributable act в рамках AC-402/AC-202/AC-203/применимой legal/corporate authority.

### 3.5 `execution evidence`

Evidence того, что утверждённая работа/действие фактически выполнены или находятся в определённом execution state. Не изменяет ретроспективно authority источника.

Mission Control MUST NOT visually or semantically collapse these classes into one “status”.

## 4. Owner-facing information architecture

Initial reference view состоит из шести logical sections. Это semantic layout, а не обязательный UI design.

### 4.1 Section A — `Protect Now`

Показывает только material/time-sensitive Company conditions, где промедление может materially повредить existing obligation, cash, customer outcome, security/data, continuity или external effect.

Источники MAY включать:

- active `P0` `WORK-*`/`OBL-*`;
- `INC-*` с material current impact;
- company-critical/currently material `RSK-*`;
- material exception expiry/revocation risk;
- AC-404 liquidity/mandatory-payment/cash-gap attention;
- customer/vendor/legal triggers, если они source-backed.

`Protect Now` не является новой severity model. Он использует существующие P0/materiality/attention semantics.

### 4.2 Section B — `Owner Action Required`

Показывает **только** случаи, где реальное действие собственника необходимо сейчас или к определённому trigger.

Включаются:

- `DEC-*`/`APR-*` с applicable `ROD-*`/residual Owner authority;
- material `ESC-*`, target = Owner;
- material risk acceptance / exception approval cases;
- capital/portfolio/external-commitment decisions;
- legal/corporate Owner/participant/General Director action only when exact capacity/source is identified.

Не включаются:

- items, которые может решить delegated Position;
- `waiting_external`, если Owner не может materially изменить outcome сейчас;
- routine notifications “for information”;
- AI recommendation без decision gate.

### 4.3 Section C — `Delegated Work / No Owner Action`

Кратко показывает material work, которое идёт без Owner intervention внутри valid authority/Assignment/access/workflow bounds.

Цель — дать confidence of control без превращения Owner в dispatcher.

По умолчанию показываются только:

- material current outcomes;
- blocked/degraded states;
- missed/stale next control point;
- exceptions to expected delegated flow;
- current accountable Position.

Routine healthy steps могут быть агрегированы или скрыты.

### 4.4 Section D — `Cash / Commitments / Obligation Signals`

Derived summary AC-404, где visible:

- `as_of` / source freshness;
- material due outflows/obligations;
- material receivable/inflow basis and uncertainty;
- recurring-cost / approved-not-yet-incurred exposure signal;
- procurement/project cash-gap cases;
- linked `OBL/RSK/DEC/APR/ESC`;
- exact Owner action only if one exists.

Restricted exact values MAY remain outside the public Company repository and outside a lower-privilege view.

Forecast/receivable MUST NOT visually appear as available cash.

### 4.5 Section E — `Portfolio / Opportunity / Review Triggers`

Показывает:

- current `PORT-*` treatment/rank by reference;
- material AC-405 event triggers since last review;
- current node requiring material portfolio decision;
- module-candidate evidence changes;
- named-trigger state for Band B;
- current evidence gaps that block a material investment recommendation.

Mission Control не re-rank portfolio автоматически и не превращает P0 incident в permanent portfolio promotion.

### 4.6 Section F — `Reference-Implementation Evidence`

Показывает evidence о том, работает ли **сама организационная модель Arvectum Company** в реальном исполнении.

Это не продуктовый vanity dashboard и не единый readiness score.

Минимальные evidence dimensions:

1. **Authority separation** — можно ли по реальным cases отличить recommendation, Owner/Position decision, approval и execution;
2. **Position accountability** — material work связывается с устойчивой `POS-*`, а не только с текущим человеком/model/runtime;
3. **Bounded AI/software execution** — есть ли source-backed examples, где AI/software выполняли admitted work без per-task Owner micromanagement и корректно остановились/эскалировали на boundary;
4. **Owner reconstruction reduction** — есть ли observed evidence, что decision packet/state projection реально уменьшили ручную реконструкцию контекста, а не добавили clerical burden;
5. **Continuity / replacement** — есть ли evidence, что replacement/fallback path определён и, где заявлено, проверен; approval документа без теста не выдаётся за operational proof;
6. **Business linkage** — organizational/AI work связан с реальными customer/revenue/obligation/economic outcomes или evidence acquisition, а не только с количеством automation/actions;
7. **Source/provenance discipline** — material claims/decisions можно восстановить до authoritative evidence;
8. **Learning loop** — validated operational/customer/incident evidence при необходимости превращается в reviewed durable improvement, а не silent production change.

Для каждой dimension MUST показываться конкретный evidence basis и ограничения. Нет требования превращать dimensions в баллы, проценты или общий `green` score.

## 5. Owner decision card

Любой item в `Owner Action Required` должен быть decision-ready и по возможности помещаться в один bounded packet.

Minimum fields:

| Поле | Требование |
|---|---|
| `subject_refs` | exact `DEC/APR/ESC/OBL/RSK/PORT/WORK` и source refs |
| `exact_question` | что именно должен решить/утвердить Owner |
| `why_now` | material trigger, due condition или consequence of delay |
| `owner_capacity` | Owner / participant / General Director / Position capacity — не смешивать |
| `authority_basis` | exact `ROD-*` / corporate/legal / residual authority / other applicable basis |
| `current_recommendation` | recommendation + accountable preparer; явно non-binding |
| `options` | bounded options, если реально существуют |
| `downside_reversibility` | material downside, reversibility, lock-in/continuity where relevant |
| `evidence_refs` | authoritative evidence + `as_of` |
| `known_unknowns` | materially relevant missing/stale/contested facts |
| `constraints_excluded_effects` | что решение не разрешает/не меняет |
| `requested_owner_act` | approve/reject/choose/accept exact bounded subject, не generic “OK” |
| `effect_readiness` | какие external/legal/technical gates останутся после Owner act |
| `execution_handoff` | какая Position/workflow выполняет approved action дальше |
| `review_expiry` | если decision/evidence freshness требует повторной проверки |

Если evidence недостаточно для material consequential decision, Mission Control должен показывать `not decision-ready` / missing evidence вместо forcing binary approval.

## 6. Attention routing and suppression

### 6.1 Owner action states

Mission Control SHOULD reuse existing attention semantics and различать:

- `required_now` — action Owner materially needed now;
- `required_by_trigger` — Owner act нужен к определённому bounded trigger/time condition;
- `waiting_external` — meaningful state, но Owner сейчас не может изменить outcome;
- `not_required` — delegated/routine/monitoring.

Это presentation semantics, не новый authority register state.

### 6.2 Suppression rule

Item не должен попадать в Owner Action queue только потому, что он:

- `P1/P2/P3`;
- technically failed;
- has a warning;
- generated by AI;
- appears in a dashboard;
- is overdue at a lower-level tracker;
- has large textual severity;
- was mentioned repeatedly.

Нужны material consequence + actual Owner authority/action need.

### 6.3 Waiting-external discipline

`waiting_external` MAY appear as concise watch item with next trigger/review date, но не как false Owner task.

## 7. Freshness / uncertainty / conflict behavior

Mission Control is only as useful as its source freshness.

Каждый material projection item должен иметь или наследовать:

- authoritative source reference;
- `evidence_as_of` / report `as_of`;
- freshness/review condition;
- known uncertainty;
- conflict marker where sources materially disagree.

Allowed presentation states MAY include:

- `current_for_declared_use`;
- `stale_for_declared_use`;
- `unknown`;
- `conflicted`;
- `not_time_sensitive`.

AC-406 не задаёт arbitrary universal TTL. Freshness определяется source semantics, decision consequence, due/trigger и existing Company governance.

Material stale/unknown/conflicted evidence MUST NOT silently become `safe`, `approved`, `paid`, `accepted`, `closed` or `ready`.

## 8. Reference-implementation evidence claim format

Чтобы не выдавать governance design за actual operation, reference-evidence claim SHOULD содержать:

| Поле | Смысл |
|---|---|
| `claim` | bounded statement being evidenced |
| `dimension` | authority / accountability / AI execution / Owner load / continuity / business linkage / provenance / learning |
| `observed_scope` | exact workflow/product/period/case |
| `evidence_refs` | source-backed traces |
| `observed_at_or_period` | temporal boundary |
| `repeatability_basis` | none / one observed case / repeated cases / separately reviewed — только если evidence поддерживает |
| `limitations` | what this evidence does not prove |
| `next_validation` | next useful real-world evidence trigger |

No global AI-autonomy %, organizational maturity score, readiness color or productivity gain MAY be asserted without actual measurement model/evidence.

## 9. What counts as evidence of an AI-native Company

Mission Control должен предотвращать dashboard theater.

Сильным evidence являются, например:

- bounded real work executed by AI/software under valid Position/Assignment/access conditions;
- attributable human/Owner gate only where authority actually requires it;
- correct fail-closed/escalation when authority/data/risk/external-effect boundary is exceeded;
- durable work/decision/risk history reconstructable without chat memory;
- replaceable runtime/model without loss of Position/authority/history;
- customer/product/business evidence generated or delivered through the governed workflow;
- repeated real use with lower Owner reconstruction burden.

Слабым/недостаточным evidence сами по себе являются:

- количество агентов;
- количество prompts/tokens/commits;
- passing technical tests без business effect;
- красиво заполненный dashboard;
- approved governance document без operational trace;
- AI recommendation без execution/decision boundary evidence;
- automation that still requires Owner to reconstruct and sequence every step.

## 10. Reference view packet

Initial non-software reference implementation MAY быть Markdown/structured projection in a restricted operating contour.

Illustrative semantic skeleton:

```text
OWNER MISSION CONTROL — as_of <timestamp>

1. PROTECT NOW
   - material current threats / P0 only

2. OWNER ACTION REQUIRED
   - exact question + authority + evidence + requested act

3. DELEGATED / EXCEPTION VIEW
   - material work moving without Owner
   - blocked/degraded exceptions only

4. CASH / COMMITMENTS
   - decision-relevant signals + freshness + unknowns

5. PORTFOLIO / TRIGGERS
   - current treatments + changed material evidence

6. REFERENCE-IMPLEMENTATION EVIDENCE
   - bounded claims + source refs + limitations

7. STALE / UNKNOWN / CONFLICTED EVIDENCE
   - only items that materially affect current control/decision
```

The exact visual layout is non-normative. Semantic separation and authority/source behavior are normative after approval.

## 11. Public / restricted / least-privilege boundary

The canonical Company repository is public. Therefore AC-406 semantic specification MAY be public, but a useful live Mission Control view will often be **restricted by default**.

Public repo MUST NOT contain merely to populate Mission Control:

- credentials/tokens/keys/signatures;
- banking/payment payload or full transaction exports;
- confidential exact cash balances when not intended for publication;
- non-public customer/vendor contracts or payload;
- unnecessary PII;
- privileged legal/tax/accounting documents;
- exploit-enabling security detail;
- sensitive incident/fraud/payment detail;
- raw prompts/hidden reasoning/chain-of-thought.

Mission Control visibility does not grant source access. If a viewer lacks permission for underlying evidence, projection should minimize/redact or show that restricted evidence exists without exposing it.

## 12. Authority-safe interaction

Initial AC-406 reference view is **read-oriented by default**.

A visual button/link/form labelled `Approve`, `Execute`, `Pay`, `Send`, `Accept risk`, `Close` or equivalent MUST NOT create authority merely because it exists in Mission Control.

Consequential interaction is allowed only when a separate governed path establishes:

1. authenticated attributable Principal;
2. correct capacity/Position;
3. valid current authority/delegation;
4. exact subject/scope;
5. current evidence and required approvals;
6. technical authorization;
7. idempotency/retry/external-effect safety where relevant;
8. durable decision/execution evidence.

Otherwise Mission Control links to/identifies the required authoritative action path and remains non-consequential.

## 13. Arvectum OS boundary

For AC-406 current `arvectum/arvectum-os` `main` was re-checked at:

`76504766353028540891ac1dfdbf1e5dc331a4af`.

OS roadmap `2.81.0` records:

- `M9-alpha — Usable Internal Workspace` = `Achieved / PASS` only in exact private internal scope;
- `P9.07 — Product-owned workspace surfaces / composition` = Current;
- `P9.10 — ООО «Арвектум» organization composition` = Planned;
- no Platform Capability is `Active` and no Product Contract is `Stable` by implication.

AC-406 MAY serve as Company-side requirements/evidence input for future OS composition, but does not itself create:

- an OS Product Contract;
- Company composition inside OS;
- stable/public API/UI;
- platform capability lifecycle transition;
- OS authority over ООО «Арвектум».

If Mission Control is later rendered through Arvectum OS, an explicit admitted boundary/Product Contract or other applicable OS governance mechanism MUST define what Company data/semantics are projected and which side owns source truth, authorization and consequential effects.

OS workspace visibility remains a technical/presentation capability, not Organizational Authority.

## 14. Minimal implementation decision

AC-406 deliberately does **not** require building new software now.

Initial recommended implementation order:

```text
semantic model
→ restricted Markdown/structured projection
→ actual Owner-use evidence in AC-407
→ only then decide whether UI/OS composition reduces burden enough to justify software work
```

A software implementation becomes justified when evidence shows at least one concrete burden/error/latency problem that a stable projection/UI materially reduces compared with the simple reference view.

This preserves business-first discipline and prevents a dashboard from becoming the deliverable instead of better Company control.

## 15. Update and history behavior

Mission Control is a projection, so it MAY be regenerated. The underlying authoritative records retain durable history.

A projection refresh MUST NOT silently rewrite historical decisions, obligations, incidents, portfolio treatments or source facts.

For decision-relevant snapshot history, the Company MAY retain bounded dated snapshots or render provenance sufficient to reconstruct what evidence the Owner saw at the time of a material decision.

No requirement is created to archive every routine dashboard refresh.

## 16. Owner Mission Control acceptance criteria

AC-406 semantic model is acceptable only if it ensures that an Owner can, without raw-chat/repo reconstruction:

1. identify true P0/protect-now conditions;
2. see exact Owner-required actions separately from routine Position work;
3. understand why a material decision is needed now;
4. distinguish source fact / interpretation / recommendation / decision / approval / execution;
5. see evidence freshness/unknowns/conflicts;
6. see decision-relevant cash/commitment signals without false liquidity semantics;
7. see current portfolio treatment and material review triggers without automatic re-ranking;
8. see evidence about actual AI-native organizational operation without vanity metrics/readiness theater;
9. trace any material claim back to authoritative source/evidence;
10. preserve public/restricted and least-privilege boundaries;
11. preserve all AC-202/AC-203 authority gates;
12. avoid making software UI a prerequisite.

Actual repeated usability / control-burden evidence remains for AC-407.

## 17. Explicit non-effects

Even after approval, AC-406 does **not**:

- populate a live Mission Control snapshot automatically;
- prove that all `WORK/OBL/DEC/APR/ESC/RSK/EXC/INC` registers are complete/current;
- prove current cash/liquidity, profitability or customer/business readiness;
- prove reduced Owner workload until actual usage evidence exists;
- prove AI executor quality/cost/reliability or M6-style transferability;
- create a new register namespace;
- approve any decision/risk/exception/spend/portfolio change;
- create payment/customer/legal/corporate authority;
- create automated consequential execution;
- grant data/source access;
- create a dashboard requirement;
- create bank/accounting integration;
- change product implementation/status;
- admit a Company reusable module;
- create or change Arvectum OS Product Contract/capability lifecycle;
- close AC-407 or M4.

## 18. Handoff to AC-407

AC-407 should use AC-406 to define and test the real management operating cadence, including:

- when Mission Control is refreshed/read;
- which event-driven updates actually matter;
- whether monthly/quarterly portfolio cadence creates value or burden;
- actual Owner decision/reconstruction burden;
- stale-evidence handling;
- whether delegated work remains visible without micromanagement;
- whether a software/OS rendering is justified by observed use;
- what cadence/process changes need durable approval.

Required next gate:

> explicit Owner approval of the exact reviewed proposal.
