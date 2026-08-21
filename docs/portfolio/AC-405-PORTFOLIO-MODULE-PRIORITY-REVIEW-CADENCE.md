# AC-405 — Portfolio / Module / Priority Review Cadence

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-405 — Portfolio/module/priority review cadence`
Предшественники: `M3 — Complete / PASS`; `AC-401…AC-404 — Approved 1.0.0`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение

AC-405 определяет минимальный устойчивый порядок пересмотра Company portfolio, module candidacy и relative priority так, чтобы:

- существенное новое evidence приводило к своевременной переоценке;
- `PORT-*` state не становился stale только потому, что product repositories продолжают меняться;
- собственник видел только реальные material portfolio decisions, а не routine product activity;
- `POS-003 — Portfolio & Product Lead` мог выполнять routine stewardship внутри уже утверждённых границ без превращения Owner в постоянный portfolio scheduler;
- календарная дисциплина не превращалась в обязательную meeting bureaucracy;
- product implementation truth, Company portfolio meaning и Arvectum OS platform truth оставались разделёнными.

AC-405 не пересматривает сам текущий `PORT-001…PORT-007` baseline и не меняет disposition, role, priority band или investment envelope по факту своего утверждения.

Главный принцип:

```text
new material evidence
→ bounded portfolio review
→ either reaffirm current treatment
   or prepare exact change decision
→ applicable DEC/APR/ROD/Product/OS gate
→ only then canonical state change
```

`review ≠ decision ≠ approval ≠ investment ≠ product roadmap change ≠ OS lifecycle change`.

## 2. Governing baseline

AC-405 подчинён applicable legal/corporate authority, Ratified Company Constitution и Approved Company governance.

### 2.1 M3 portfolio baseline

Approved AC-301…AC-307 уже установили последовательную Company-level portfolio model:

```text
PORT identity / disposition
→ accountable Position
→ bounded investment / cost / risk treatment
→ standalone / reference / module / OS-candidate classification
→ cross-product / Arvectum OS boundary
→ capital / economics / Owner-attention prioritization
```

Current canonical portfolio source — `docs/portfolio/PORTFOLIO.md` `Active 0.8.0`.

### 2.2 Priority hierarchy

AC-106 остаётся выше portfolio ranking:

1. `P0` — protect current obligations, cash and material risk;
2. `P1` — flagship market evidence + minimal real operating model;
3. `P2` — product/OS work directly tied to revenue, obligation, evidence or blocker removal;
4. `P3` — speculative productization/module/platform expansion.

AC-306 default portfolio order остаётся действующим внутри этой hierarchy:

`A1 PORT-002 → A2 PORT-001 → B1 PORT-003 / B2 PORT-004 по named trigger → C1 PORT-007 clarification-only → D1 PORT-005 / D2 PORT-006 contain`.

### 2.3 M4 control inputs

Portfolio review использует уже утверждённые Company control layers:

- AC-401: `WORK-*` / `OBL-*`;
- AC-402: `DEC-*` / `APR-*` / `ESC-*`;
- AC-403: `RSK-*` / `EXC-*` / `INC-*`;
- AC-404: management-finance/cash/commitment projection over authoritative sources.

AC-405 не создаёт дублирующих portfolio-risk, finance или decision registries.

### 2.4 Position and authority boundary

`POS-003 — Portfolio & Product Lead` остаётся accountable за Company-level portfolio stewardship, evidence synthesis и routine prioritization/status coordination внутри уже утверждённого envelope.

Initial Position authority permits `AM-0`, `AM-1`, `AM-2` only. `AM-3`/`AM-4` для major portfolio approval/reclassification не активированы.

Material portfolio/investment changes сохраняют applicable Owner gates, прежде всего:

- `ROD-02` — capital allocation / material financial exposure;
- `ROD-04` — major portfolio, initiative and investment decisions;
- `ROD-06` — material risk/exception acceptance;
- `ROD-08` — critical dependency / technology-sovereignty exception;
- `ROD-09` — material Company↔Product↔Arvectum OS boundary/cross-repository commitment;
- `ROD-01` — если изменение фактически затрагивает Company strategy/business-model identity.

## 3. Current Arvectum OS boundary

Перед AC-405 current `arvectum/arvectum-os` `main` re-checked на commit:

`76504766353028540891ac1dfdbf1e5dc331a4af`.

OS M9-alpha имеет `Achieved / PASS` только в exact private internal workspace scope; current OS action — P9.07. Это не меняет Company portfolio semantics.

AC-405 не выводит из OS workspace, repository reuse или Product Contract visibility:

- новый Company module;
- shared runtime/service/library;
- Platform Capability candidate/lifecycle state;
- Stable Product Contract;
- Company portfolio approval authority.

Arvectum OS остаётся authoritative для собственных Product Contracts, RFC/ADR и capability lifecycle. Company может только сформировать Company-side evidence/proposal и пройти отдельный OS governance path, если он действительно потребуется.

## 4. Cadence model: event-driven first, calendar backstop second

AC-405 вводит три уровня review cadence.

### 4.1 Immediate event-triggered review

Material trigger SHOULD вызывать review без ожидания календарной даты.

Review охватывает только затронутый node/scope и необходимые cross-node consequences. Один event не требует переоткрывать весь portfolio.

### 4.2 Monthly asynchronous exception scan

Начальный operating default — **один лёгкий portfolio exception scan в календарный месяц** под accountability `POS-003`.

Цель scan — не заново анализировать семь продуктов, а ответить:

- появилось ли material evidence, меняющее current treatment;
- появились ли новые P0/P1/P2 obligations/revenue/evidence/blockers;
- появился ли named trigger для Band B;
- стали ли stale decision-relevant finance/risk/customer/dependency inputs;
- существует ли portfolio question, который уже нужно превратить в `DEC-*`/`ESC-*`.

Если material change нет, допустим один общий durable result: `no material portfolio change identified as of <date/source set>`. Отдельный Owner meeting и отдельный файл на каждый node не требуются.

### 4.3 Quarterly integrated revalidation

Начальный calendar backstop — **одна интегральная portfolio revalidation в квартал**.

Она проверяет, остаются ли разумно current:

- identity/disposition;
- accountable Position;
- investment/cost/risk treatment;
- standalone/reference/module-candidate classification;
- cross-product / OS boundary;
- portfolio band / Owner-attention treatment;
- carry-forward evidence gaps.

Quarterly review также не требует Owner meeting по умолчанию. `POS-003` подготавливает summary; Owner получает только decision-ready material cases, попадающие в reserved/residual authority.

Эти calendar intervals являются **initial operating defaults**, а не вечными constitutional invariants. AC-407 и последующее operating evidence MAY предложить увеличить/уменьшить frequency через надлежащий governance change, если burden или missed-change risk покажут это.

## 5. Material event triggers

Event-triggered review SHOULD запускаться, когда materially меняется хотя бы один из следующих evidence domains.

### 5.1 Customer / revenue / obligation

- новый paid customer, design partner, commercial pilot или materially stronger buying evidence;
- существенный customer acceptance/rejection/support/change event;
- material customer/vendor obligation, который меняет portfolio economics или priority;
- повторный независимый consumer, который усиливает reuse/module hypothesis;
- loss/churn/non-conversion evidence, materially weakening the investment thesis.

### 5.2 Cash / economics / commitment

- material recurring-cost expansion;
- material spend/investment request;
- materially changed direct delivery/support burden;
- procurement/project cash-gap exposure;
- new evidence on margin/unit economics/Owner cost where it is decision-relevant;
- decision-relevant cash evidence becomes unavailable/stale for a proposed commitment.

### 5.3 Product / engineering / release

- accepted delivery / production milestone materially changes Company treatment;
- major technical blocker materially changes feasibility/cost/continuity;
- maintenance/support burden exceeds current bounded treatment;
- architecture change would create new shared cross-product dependency;
- repository/product status materially diverges from Company portfolio interpretation.

Routine commits, tests, bug fixes and feature progress inside existing envelope are not portfolio-review triggers by themselves.

### 5.4 Risk / security / continuity / sovereignty

- material `RSK-*`, `EXC-*` or `INC-*` affects the investment thesis;
- critical dependency becomes unavailable/non-replaceable/restricted;
- legal/IP/data/security evidence materially changes;
- fallback/continuity evidence materially improves or degrades;
- technology-sovereignty assumption changes materially.

### 5.5 Reuse / module candidacy

- at least two materially independent consumers/workflows demonstrate a common reusable need;
- common contract/interface can be described without importing product-specific semantics;
- measured/credible reuse benefit appears relative to duplication/support burden;
- ownership, data, continuity and replacement boundaries become clear enough for an investment decision;
- evidence shows a supposed reusable pattern is actually customer/product-specific and should remain local.

Reuse evidence creates review, not automatic module promotion.

### 5.6 Company↔Product↔Arvectum OS boundary

- product begins to depend materially on a new OS contract/capability;
- proposed shared component could belong to Company module layer or OS;
- current Product Contract becomes insufficient/stale for a material commercial path;
- cross-repository commitment/dependency is proposed.

Such trigger creates Company-side review and, when applicable, separate OS/product governance work. Company review cannot approve OS lifecycle by itself.

### 5.7 Owner attention / opportunity cost

- current node repeatedly consumes scarce Owner intervention outside its approved treatment;
- another material opportunity/obligation displaces current discretionary investment;
- known unavailable physical/legal/customer gate causes repeated unproductive retries;
- a node becomes effectively self-sustaining and no longer needs its current Owner-attention band.

## 6. Review packet

A material portfolio review SHOULD be decision-ready without requiring Owner reconstruction from raw chats/repos.

Minimum packet, where applicable:

| Field | Meaning |
|---|---|
| `portfolio_ref` | exact `PORT-*` node(s) |
| `review_mode` | `event_triggered`, `monthly_scan`, `quarterly_revalidation` |
| `trigger_or_period` | exact trigger or covered period |
| `current_canonical_treatment` | current disposition/role/band/investment treatment references |
| `changed_since_last_review` | material delta only |
| `customer_revenue_obligation_evidence` | linked source / `OBL-*` / customer refs |
| `finance_economics_evidence` | AC-404/source refs; known vs unknown clearly separated |
| `work_delivery_evidence` | `WORK-*` / product status refs |
| `risk_continuity_evidence` | `RSK-*`/`EXC-*`/`INC-*` / source refs |
| `reuse_module_evidence` | consumers/common contract/reuse burden evidence where applicable |
| `dependency_os_boundary` | current/proposed dependency/Product Contract implications |
| `owner_attention_effect` | exact Owner work/gate/decision burden |
| `recommendation` | reaffirm / bounded resequence / prepare material change / contain / stop-retire proposal / role-module review |
| `authority_path` | AM-2 or exact `ROD-*`/DEC/APR/ESC/Product/OS gate |
| `next_review_or_trigger` | next backstop or explicit event trigger |
| `evidence_as_of` | freshness boundary |

Raw chain-of-thought не является required evidence.

## 7. Review outcomes and authority

### 7.1 `Reaffirm current treatment`

Если material evidence не изменило approved treatment, `POS-003` MAY в `AM-2`:

- reaffirm current Company portfolio interpretation;
- refresh review/evidence references;
- record current next trigger/backstop;
- synchronize stale descriptive pointers to product canonical sources.

Это не новое Owner decision.

### 7.2 `Bounded resequence within approved envelope`

`POS-003` MAY использовать `AM-2` для routine sequencing/status coordination внутри уже утверждённых Company hierarchy, portfolio treatment и risk/cost/commitment bounds.

Примеры:

- временно поднять конкретный P0 obligation work slice по AC-106 без изменения portfolio band/disposition;
- re-evaluate a Band B bounded slice после named trigger;
- менять порядок routine technical/evidence work внутри approved node treatment.

Это не позволяет permanently менять approved A/B/C/D band или создавать funding mandate.

### 7.3 `Material portfolio change proposal`

Следующие изменения MUST NOT выводиться из scan/review автоматически и требуют соответствующего `DEC-*`/`APR-*`/Owner gate:

- change `continue / contain / clarify / stop-retire` disposition;
- material change investment envelope;
- material permanent change approved priority band/treatment;
- admission/promotion to Company reusable module;
- major portfolio initiative/investment start or stop;
- material Company↔Product↔OS dependency/ownership boundary change;
- material risk/dependency exception;
- strategy/business-model effect.

`POS-003` готовит evidence/recommendation, но review completion не является approval.

## 8. Named-trigger discipline for current Band B

Для `PORT-003` и `PORT-004` approved `named-trigger` semantics сохраняются.

Named trigger означает:

`new evidence → bounded review of exact slice → optional temporary elevation/work proposal`.

Он НЕ означает:

- automatic permanent promotion to Band A;
- budget allocation;
- new customer commitment;
- production approval;
- unlimited feature expansion;
- Owner obligation to act immediately, если реального material decision нет.

## 9. Module-candidate discipline

### 9.1 PORT-007

`PORT-007 — Data Platform` остаётся `clarify`, `C1`, clarification-only Company/product-family module candidate.

AC-405 не разрешает material build.

Material promotion/build review требует как минимум evidence of:

1. named materially independent consumers/workflows;
2. common bounded contract/interface;
3. economic/reuse benefit hypothesis grounded enough for investment decision;
4. continuity/dependency/sovereignty path;
5. data/security/rights boundary;
6. accountable ownership and implementation locus;
7. evidence that capability belongs above one product but below/away from OS unless separate OS admission is justified.

### 9.2 Reference implementations

`PORT-002`, `PORT-005`, `PORT-006` reuse evidence MAY strengthen or weaken a product-family module hypothesis, but reference status itself is not promotion evidence.

`PORT-005`/`PORT-006` remain contained unless a separate approved portfolio change says otherwise.

## 10. P0 override is not portfolio reclassification

A real P0 event MAY immediately preempt discretionary portfolio work.

The override applies to exact affected `WORK-*`/`OBL-*`/risk/incident scope.

After P0 resolution, the node returns to its approved treatment unless material review + competent decision changes it.

Therefore:

`P0 temporary execution priority ≠ permanent portfolio band/disposition change`.

## 11. Owner-attention discipline

The Owner should receive portfolio work only when an actual Owner/residual authority action is needed.

Owner-facing portfolio item SHOULD state:

- exact decision/question;
- why now / trigger;
- current treatment;
- material changed evidence;
- recommended outcome + alternative;
- cash/economics/obligation/risk effect;
- downside/reversibility;
- exact `ROD-*`/authority basis;
- exact Owner act needed;
- what proceeds without Owner after the decision.

Do not surface as Owner work:

- monthly `no change` scan;
- routine product progress;
- raw technical test status;
- known unchanged blocked physical gate;
- routine AM-2 sequencing;
- external/customer waiting state with no Owner-side decision.

## 12. Durable review evidence without file explosion

AC-405 does not require one review file per node per month.

Permitted patterns include:

1. one concise portfolio-wide monthly/quarterly review checkpoint referencing changed nodes only;
2. a durable `DEC-*`/`ESC-*` packet when material decision exists;
3. an update to canonical portfolio review metadata when source representation later supports it;
4. a future governed OS/domain-neutral projection through an admitted boundary.

Minimum reconstructability:

- who/which Position reviewed;
- mode/period/trigger;
- evidence as-of;
- changed nodes;
- result (`no material change` or exact decision/escalation refs);
- next backstop/trigger.

Routine no-change review MUST NOT create artificial decision IDs.

## 13. Freshness and reconciliation

Portfolio interpretation MUST be rechecked when source facts materially change.

Rules:

- stale product pointer/status reference is refreshed from product canonical source, not guessed;
- stale/unknown finance evidence is explicit and may block material investment recommendation;
- stale customer/acceptance evidence is not silently treated as current demand;
- unresolved legal/IP/data/sovereignty evidence remains unknown, not cleared by time;
- OS Product Contract/lifecycle state is rechecked from OS source when decision depends on it;
- previous Owner approval is not reused for materially changed scope without authority review.

`no change` means no material portfolio change found in the reviewed source set — not proof that every possible fact is complete.

## 14. Confidentiality and public-repository boundary

Public Company repository MAY contain:

- safe portfolio treatment/status metadata;
- evidence references;
- minimized management rationale;
- review date/mode/result;
- public product/OS source references.

It MUST NOT contain merely for review convenience:

- raw confidential customer/vendor contract payload;
- bank/accounting exports or confidential exact balances;
- credentials/secrets/signatures;
- unnecessary PII;
- privileged incident/security details;
- confidential commercial terms where reference is sufficient;
- raw chain-of-thought.

## 15. Relationship with AC-401…AC-404

AC-405 consumes the existing control layer rather than duplicating it:

```text
WORK / OBL
+ DEC / APR / ESC
+ RSK / EXC / INC
+ AC-404 management-finance evidence
+ product / customer / OS authoritative source evidence
↓
portfolio review
↓
reaffirm current treatment
OR
bounded AM-2 resequence
OR
material DEC/APR/ROD/Product/OS proposal
```

Closing a portfolio review does not close linked work, obligations, risk, incident or decision records automatically.

## 16. Management-burden rule

Cadence is successful only if it reduces stale-state/reconstruction risk at lower cost than the review overhead it creates.

Therefore:

- reviews are asynchronous by default;
- meetings are exception-based, not cadence-based;
- unchanged nodes receive minimal touch;
- event review scopes only affected nodes;
- Owner participation is authority-driven;
- exact numeric KPI collection is required only when decision-relevant and evidence-backed;
- calendar cadence may later be adjusted based on observed burden/missed changes.

## 17. Handoff to AC-406 and AC-407

### AC-406

Owner Mission Control SHOULD later surface only:

- material portfolio change proposals ready for Owner decision;
- P0 overrides with real Owner action;
- major stale/unknown evidence blocking material decision;
- significant changed portfolio/economics/risk state;
- current treatment and concise next control point.

It SHOULD NOT become a seven-product activity feed.

### AC-407

AC-407 SHOULD integrate this cadence with the broader Company operating cadence and test whether:

- monthly exception scan is too frequent/rare;
- quarterly backstop adds value;
- Owner interruption burden decreases;
- material changes are caught before they become stale commitments or wasted investment;
- review artifacts remain reconstructable without growing into process bureaucracy.

## 18. Explicit non-effects

Approval of AC-405 by itself does NOT:

- change any current `PORT-*` disposition, role, band or priority;
- start/stop/fund any product/module/initiative;
- create a budget, spend approval, recurring cost or customer/vendor commitment;
- create a reusable Company module;
- authorize material build of `PORT-007`;
- promote `PORT-005`/`PORT-006` from contain;
- permanently elevate Band B after a trigger;
- change a product roadmap/implementation status;
- create cross-product runtime/code/data dependency;
- create/modify Arvectum OS Product Contract or capability lifecycle;
- accept risk/exception;
- create AM-3/AM-4 authority;
- create a mandatory Owner meeting calendar;
- execute AC-406/AC-407.

## 19. Approval gate

AC-405 remains `Proposed` until explicit attributable Owner approval of the exact reviewed proposal.

Required gate:

> explicit Owner approval of the exact reviewed proposal.
