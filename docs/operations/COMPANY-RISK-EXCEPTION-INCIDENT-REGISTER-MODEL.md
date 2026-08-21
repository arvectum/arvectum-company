# AC-403 — Risk, Exception and Incident Register Model

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-403 — Risk, exception and incident register model`
Предшественники: `AC-401 — Approved 1.0.0`; `AC-402 — Approved 1.0.0`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение

AC-403 определяет минимальную Company-level модель контроля существенных рисков, control exceptions и incidents поверх уже утверждённых work/obligation и decision/approval/escalation semantics.

Цель — дать собственнику и accountable Positions возможность видеть только те risk/exception/incident subjects, которые materially влияют на обязательства, cash, customer/external effect, continuity, security/data, portfolio, authority или Owner attention, не превращая Company repository во второй security tracker, bug tracker, product incident system, legal register или SIEM.

Ключевое различие:

```text
risk evidence ≠ accepted risk
exception request ≠ approved exception
incident detection ≠ authority to act
containment ≠ risk acceptance
recovery ≠ closure of every obligation
technical workaround ≠ waiver
```

AC-403 не создаёт risk appetite, exception authority или incident-response authority. Он делает material exposure, deviations and events видимыми и связывает их с уже существующими authority/evidence contours.

## 2. Governing baseline

AC-403 подчинён applicable legal/corporate authority, Ratified Company Constitution и Approved Company governance.

Применимые Company layers:

1. `AC-105 — Material Risk, Dependency, Continuity and Fallback Baseline` уже установил consequence-based risk materiality без fabricated probabilities/MTTR/RTO, разделил deliberate gates, unresolved single points, untested fallback, external/product-owned и unknown states и зафиксировал текущие material dependency exposures.
2. `AC-202 — Reserved Owner Decisions` сохраняет `ROD-06 — Risk appetite and material exception acceptance`, а также применимые `ROD-03`, `ROD-07`, `ROD-08`, `ROD-09`. Owner approval не может легализовать unlawful act, отменить customer rights, binding contract или OS constitutional invariant.
3. `AC-203 — Delegated Position Authority Model` сохраняет deny-by-default, `AM-0…AM-4`, stop/fail-closed/escalation при exceeded/unclear risk boundaries и разрешает bounded reversible emergency containment только если такой класс заранее допустим authority/workflow envelope.
4. `AC-207 — Critical-Function Continuity Baseline` различает `CM-0…CM-4` и запрещает continuity bypass: replacement/recovery не передаёт authority и не доказывает readiness.
5. `AC-401 — Approved 1.0.0` задаёт `WORK-*`/`OBL-*`, `P0…P3`, control/attention/freshness semantics.
6. `AC-402 — Approved 1.0.0` задаёт `DEC-*`/`APR-*`/`ESC-*` и фундаментальную границу `recommendation ≠ decision ≠ approval ≠ legal/corporate act ≠ technical authorization ≠ execution`.
7. Product implementation/status/security details остаются в product repositories/competent systems; Arvectum OS platform truth — в `arvectum/arvectum-os`; legal/customer/accounting/external facts — в своих authoritative contours.

## 3. Current Arvectum OS boundary

Перед AC-403 проверен current `arvectum/arvectum-os` `main` на commit:

`c2be41ad8d1b144bea2ab0b030c57bcf3c59a3ae`.

P9.06 теперь предоставляет Productive Workspace UX для governed actions/executions/decisions, но сохраняет independent governance decisions, fail-closed behavior и отсутствие authority из visibility/session/button state.

OS `docs/governance/DECISION-AUTHORITY-POLICY.md` остаётся `Proposed 0.2.1` и не принимается AC-403 как Company authority.

AC-403 MAY позднее использовать domain-neutral OS records/projections через отдельный admitted boundary, но Company-specific risk appetite, exception semantics, `ROD-*`, Positions и Company materiality остаются Company-owned. AC-403 не создаёт OS Product Contract, Capability lifecycle transition или platform incident policy.

## 4. Три Company control namespaces

AC-403 вводит три независимых namespace:

```text
Company Risk / Exception / Incident Control Layer
├── RSK-* — material risk exposure/control record
├── EXC-* — material control-exception request/decision control record
└── INC-* — material incident control record
```

Исторические `R-01…R-20` AC-105 остаются baseline dependency-risk identifiers и не переименовываются. При необходимости material active risk AC-403 может ссылаться на них через `source_refs`/`origin_refs`; новые live Company control identities используют `RSK-*`.

## 5. Определения и границы

### 5.1 `RSK-* — Material Risk`

Risk — неопределённое будущее событие/условие или продолжающаяся exposure, которое при реализации может materially повлиять на Company objectives, obligations, cash, customer/external effect, continuity, security/data, sovereignty, portfolio или authority.

`RSK-*` — это Company control representation риска, а не доказательство likelihood и не акт принятия риска.

### 5.2 `EXC-* — Control Exception`

Exception — временное и точно ограниченное разрешённое отклонение от существующего Company control/rule/standard/approved envelope **только если higher-authority source вообще допускает такое отклонение**.

`EXC-*` может существовать как request до решения. Сам факт наличия записи не разрешает deviation.

### 5.3 `INC-* — Material Incident`

Incident — произошедшее событие или обнаруженное состояние, которое уже вызвало либо непосредственно создаёт material adverse effect и требует coordinated containment/recovery/decision control.

Incident не обязательно означает security incident. Возможны customer, obligation, financial, operational, continuity, data/security, dependency, repository/history или other Company-material incidents.

### 5.4 `Issue` не становится четвёртым Company namespace

AC-403 сознательно не создаёт `ISS-*`.

`Issue` — общий термин для текущей известной проблемы. Она остаётся:

- product bug/task — в product tracker;
- Company work blocker/current problem — в `WORK-*`/`OBL-*` (`blocked`/`needs_attention`);
- material event requiring coordinated response — `INC-*`;
- current control weakness that creates future exposure — `RSK-*`;
- proposed deviation from a control — `EXC-*` request.

Это предотвращает появление универсального duplicate issue tracker.

### 5.5 Accepted risk — не lifecycle state, возникающий сам

Accepted risk существует только когда competent authority **явно** принимает defined residual exposure.

Если acceptance materially попадает в `ROD-06`/другой `ROD-*`, требуется explicit Owner `DEC-*`/`APR-*` act. Если later delegation действительно допускает bounded risk acceptance, применяется exact `AM-*` authority evidence.

`RSK-*` MAY ссылаться на `risk_acceptance_decision_ref`, но не может сам считать себя accepted по полю/status, silence, elapsed time, workaround или continued operation.

## 6. Qualification gate

Company register получает entry только при material Company control need.

### 6.1 `RSK-*` включается, когда минимум одно существенно

- возможен breach/невыполнение `OBL-*`;
- есть material cash/financial exposure;
- есть customer/external commitment or acceptance exposure;
- риск затрагивает continuity/critical dependency/organizational history;
- риск затрагивает security/privacy/data/IP/sovereignty materially;
- риск может изменить portfolio/company priority or stop/continue decision;
- требуется material risk-treatment/acceptance decision;
- Owner/another authority должен видеть uncertainty для решения.

### 6.2 `EXC-*` включается, когда

- требуется осознанно отступить от mandatory/approved Company control или delegated envelope;
- deviation materially меняет risk, customer/external effect, data/security, financial or continuity posture;
- требуется explicit approval/expiry/conditions/compensating-control visibility.

Routine product-local waivers внутри product governance остаются product-owned, если нет Company-level material effect.

### 6.3 `INC-*` включается, когда

- событие materially затронуло Company/customer/obligation/cash/continuity/security/data/authority/history;
- требуется координация нескольких Positions/contours;
- required containment/recovery/notification/decision может выйти за обычный product task;
- incident creates/activates `P0`, material `ESC-*`, `DEC-*`, `APR-*` or new `OBL-*`;
- Owner needs concise situational visibility.

Мелкий defect, обычный failed test, routine retryable job failure, benign alert и low-impact product issue по умолчанию не становятся `INC-*`.

## 7. Stable identity и relationships

Namespaces:

- `RSK-001`, `RSK-002`, ...;
- `EXC-001`, `EXC-002`, ...;
- `INC-001`, `INC-002`, ... .

IDs не переиспользуются после closure.

Один logical material concern — одна Company entry. Lower-level tickets, alerts, logs, contract/customer records и product incidents указываются references.

Типовые relationships:

```text
RSK-* may threaten → OBL-* / WORK-* / PORT-*
RSK-* may require → DEC-* / APR-* / ESC-*
EXC-* may reference → RSK-* residual exposure
EXC-* approval must reference → DEC-* / APR-* authoritative act
INC-* may realize/activate → RSK-*
INC-* may create → WORK-* / OBL-* / ESC-* / DEC-* / APR-*
INC-* recovery may leave → RSK-* residual risk
```

Закрытие одного объекта не закрывает другие автоматически.

## 8. Common control envelope

Каждый active `RSK-*`, `EXC-*` или `INC-*` MUST иметь минимум:

| Поле | Назначение |
|---|---|
| `id` | stable namespace identity |
| `kind` | `risk`, `exception`, `incident` |
| `title` | короткое human-readable название |
| `control_summary` | Company-level meaning без unnecessary sensitive payload |
| `accountable_position` | ровно одна primary accountable `POS-*` |
| `scope_refs` | `WORK-*`, `OBL-*`, `DEC-*`, `APR-*`, `ESC-*`, `PORT-*`, product/OS/customer/external refs |
| `company_priority` | `P0/P1/P2/P3` context по AC-106; не authority/spend |
| `attention_state` | `normal`, `needs_attention`, `escalated` |
| `source_refs` | authoritative/evidence references |
| `evidence_as_of` | freshness point для dynamic evidence |
| `owner_attention` | `required`, `not_required`, `waiting_external` |
| `next_control_point` | следующий material control checkpoint |
| `classification_handling` | minimization/confidentiality handling |
| `last_reviewed_at` | последняя Company control review |
| `closure_ref` | evidence/decision/source при closure |

Primary accountability не создаёт authority. Supporting Positions указываются отдельными references.

## 9. `RSK-*` risk model

Каждый material `RSK-*` MUST дополнительно иметь:

| Поле | Смысл |
|---|---|
| `risk_statement` | cause/condition → uncertain event/exposure → material consequence |
| `consequence_class` | AC-105-compatible: `company_critical`, `workstream_critical`, `degrading`, `not_currently_critical` |
| `affected_values` | obligations/cash/customer/continuity/security/data/IP/portfolio/etc. |
| `risk_state` | `identified`, `assessing`, `active`, `monitoring`, `closed` |
| `current_controls_refs` | existing controls/fallback/source refs |
| `control_evidence_state` | where relevant AC-207 `CE-0…CE-3` or equivalent source evidence |
| `likelihood_evidence` | optional factual basis; `unknown` permitted; no fabricated score required |
| `trigger_indicators` | observable trigger/leading evidence if known |
| `response_intent` | `avoid`, `reduce`, `monitor`, `transfer_or_share`, `tolerate`, `undecided` |
| `treatment_work_refs` | linked `WORK-*`/product execution refs |
| `residual_exposure` | concise remaining exposure after current controls |
| `risk_acceptance_decision_ref` | required only when tolerance/acceptance needs authority |
| `review_trigger` | date/window/event/changed fact; no fabricated precision |

### 9.1 Нет обязательного numeric risk score

AC-403 не вводит Company-wide probability×impact matrix, percentages, expected annual loss или arbitrary red/amber/green score без evidence.

Consequence class + current exposure + due/trigger + control evidence + uncertainty должны быть достаточны для management attention. Позднее measured evidence MAY justify quantitative model отдельным approved change.

### 9.2 `response_intent=tolerate` не равно accepted risk

`tolerate` — только proposed/current treatment direction. Если acceptance требует authority, `risk_acceptance_decision_ref` должен указывать exact valid `DEC-*`/`APR-*` act. Без него risk остаётся unaccepted/decision-pending.

## 10. `EXC-*` exception model

Каждый material `EXC-*` MUST иметь:

| Поле | Смысл |
|---|---|
| `control_rule_ref` | точный control/policy/delegation/standard, от которого запрашивается deviation |
| `requested_deviation` | что именно предлагается разрешить |
| `request_reason` | bounded business/operational rationale |
| `exception_state` | `requested`, `under_review`, `approved`, `rejected`, `expired`, `revoked`, `superseded`, `closed` |
| `authority_basis` | кто вправе разрешить exception и почему; либо `none/not_permitted` |
| `decision_refs` | связанные `DEC-*` |
| `approval_refs` | связанные `APR-*`; для approved exception обязательны attributable valid acts |
| `effective_scope` | точный object/customer/product/workflow/action scope |
| `effective_period` | начало + expiry/event/review trigger |
| `conditions` | обязательные conditions |
| `compensating_controls` | временные controls/containment, если применимо |
| `residual_risk_refs` | связанные `RSK-*` |
| `reversion_or_exit` | как закончить deviation и восстановить normal control |
| `authoritative_source_ref` | external/legal/Product/OS source, если Company не authority |

### 10.1 Exception request ≠ exception approval

`requested`/`under_review` запрещают deviation, если другой valid source его уже не разрешает.

Technical workaround, ability to bypass a control, manual override, admin access, urgency или отсутствие возражения не создают exception.

### 10.2 Non-waivable boundaries

Если applicable law, corporate competence, binding contract/customer right, Company Constitution, accepted OS invariant/Product Contract или иной higher-authority source **не допускает** exception, Company record должен отражать `authority_basis = none/not_permitted`; решение — stop/reconcile/amend through proper path, а не `EXC-* approved`.

### 10.3 Expiry по умолчанию

Material exception SHOULD иметь expiry/review trigger. Indefinite exception требует отдельного justification и часто означает, что нужно изменить underlying policy/authority model, а не бесконечно продлевать workaround.

Expired/revoked exception нельзя продолжать использовать как permission.

## 11. `INC-*` incident model

Каждый material `INC-*` MUST иметь:

| Поле | Смысл |
|---|---|
| `detected_at` | когда Company получил достаточный signal; не обязательно actual start |
| `incident_state` | `detected`, `triaged`, `contained`, `recovering`, `monitoring`, `closed` |
| `consequence_class` | `company_critical`, `workstream_critical`, `degrading` |
| `observed_impact` | подтверждённый impact; unknown отдельно от assumed |
| `affected_scope_refs` | customers/OBL/WORK/PORT/product/OS/external refs |
| `authoritative_incident_source_ref` | product/security/provider/source-system record, если он authoritative |
| `containment_refs` | bounded containment actions/work/evidence |
| `recovery_refs` | restoration/reconciliation/work refs |
| `decision_approval_refs` | `DEC-*`/`APR-*`, если требуется accept/resume/notify/etc. |
| `escalation_refs` | `ESC-*` |
| `notification_obligation_refs` | `OBL-*`/external source refs, если notification/reporting действительно required |
| `suspected_cause_summary` | `unknown` допустим; hypothesis не объявляется fact |
| `confirmed_cause_ref` | только если authoritative evidence подтверждает |
| `residual_risk_refs` | open `RSK-*` после containment/recovery |
| `closure_evidence_refs` | evidence для Company closure |
| `learning_refs` | reviewed follow-up/knowledge/workflow improvements, если появились |

### 11.1 Incident state не создаёт response authority

`detected`/`triaged`/`contained` не означают, что любой исполнитель вправе совершать consequential actions.

Containment разрешён только внутри existing `AM-*`, Assignment/access и approved AC-207 continuity/incident boundaries. За пределами них требуется `ESC-*`/`DEC-*`/`APR-*`.

### 11.2 Containment ≠ material risk acceptance

Изоляция, revocation, safe shutdown, evidence preservation и другой заранее допустимый reversible containment могут выполняться без нового Owner approval только внутри approved envelope.

Продолжение/возобновление работы при unresolved material gap, принятие новой liability или broadening risk appetite требует applicable authority, часто `ROD-06`.

### 11.3 Incident closure

`INC-*` можно закрыть только при достаточном evidence, что Company incident-control need завершён либо передан в explicit ongoing risks/obligations/work.

Closure incident не означает автоматически:

- выполнены все customer/legal notification obligations;
- закрыты все `OBL-*`;
- residual risks приняты;
- исправлен product defect;
- legal liability отсутствует;
- security/compliance status доказан.

Открытые последствия должны иметь собственные refs.

## 12. `P0`, attention и escalation

### 12.1 Не каждый risk/incident — P0

`P0` применяется только если существует реальный time-sensitive material obligation/cash/risk/customer/continuity/external-effect issue по AC-106.

Высокая концептуальная важность, scary wording, severity label source system или mere uncertainty сами по себе не делают item `P0`.

### 12.2 `needs_attention`

Используется, когда materially требуется ближайшая проверка из-за:

- trigger proximity;
- stale/missing evidence;
- control degradation;
- exception expiry;
- incident state drift/no recovery evidence;
- newly observed exposure;
- pending decision/approval gate.

### 12.3 `escalated`

Используется только когда current Position/Assignment/workflow authority insufficient либо explicit higher/external authority gate нужен.

Escalation target определяется AC-402 `ESC-*`. Не вся эскалация направляется Owner.

### 12.4 Owner attention

`owner_attention=required` только если:

- применим `ROD-*`;
- residual Owner authority нужна сейчас;
- Owner должен принять/отклонить material exception/risk;
- Company-side decision Owner требуется до external/corporate/customer gate;
- incident materially меняет strategy/capital/risk/external commitment/continuity beyond delegated bounds.

`waiting_external` используется для legitimate customer/regulator/provider/legal gate, когда Owner action сейчас ничего не изменит.

## 13. Source of truth и freshness

### 13.1 Company control canonicality

Company register canonical только для Company-level control metadata: inclusion, identity, accountable Position, materiality interpretation, attention, relationships, next control point, Company decisions/accepted exceptions within valid Company authority и closure history.

### 13.2 Underlying facts остаются authoritative elsewhere

- security/product incident telemetry and root cause — competent product/security source;
- legal breach/reporting duty — legal/official source;
- customer impact/acceptance — contract/customer source;
- accounting/cash loss — accounting/bank source;
- Arvectum OS platform incident/lifecycle — OS canonical source;
- product bug/release state — product repository.

Company summary не переопределяет их.

### 13.3 Changed facts / stale evidence

Если dynamic evidence stale, missing or contradictory:

- unknown не превращается в safe/closed/accepted;
- material reliance блокируется либо идёт `needs_attention`/`ESC-*`;
- risk/exception/incident summary обновляется ссылкой на новый source;
- history не переписывается так, чтобы скрыть прежнюю ошибку.

## 14. Position accountability

Default functional mapping следует Approved AC-204/AC-205:

| Subject | Primary accountable Position по умолчанию |
|---|---|
| Company-wide material risk coordination | `POS-006 — Security, Risk & Continuity Lead` |
| customer/commercial incident or obligation risk | `POS-002 — Commercial & Customer Lead` |
| portfolio/investment risk | `POS-003 — Portfolio & Product Lead` |
| engineering/release incident needing Company control | `POS-004 — Engineering & Release Lead` |
| cash/financial/obligation exposure | `POS-005 — Finance & Obligation Control Lead` |
| strategic/material cross-functional risk acceptance | `POS-001 — Company Executive` for coordination; final authority separately by `ROD-*`/delegation |

`POS-006` не становится universal owner всех risks и не получает material risk-acceptance authority по названию Position. Primary accountable Position выбирается по business subject; другие Positions support/consult.

## 15. Security, privacy, confidentiality and public repository

AC-403 не оправдывает centralization of sensitive incident evidence.

Публичный Company repository MUST NOT хранить без необходимости:

- credentials, tokens, recovery codes, private keys;
- exploit details, secrets, privileged security architecture sufficient for abuse;
- raw logs with sensitive identifiers;
- signatures/full banking payload;
- unnecessary PII;
- customer-confidential incident/contract text;
- legally privileged material;
- raw model prompts/chain-of-thought;
- forensic payload where reference + classification label достаточно.

Для material confidential incidents Company public control layer SHOULD хранить minimized metadata/reference, а подробный evidence packet — в подходящем restricted authoritative contour.

Visibility в Owner projection не даёт permission на underlying source.

## 16. Owner-facing projection semantics

AC-403 определяет semantics, не dashboard.

Default Owner-facing risk/incident projection SHOULD в первую очередь показывать:

1. active `P0` `RSK-*`/`INC-*`;
2. open material incidents с `owner_attention=required`;
3. `EXC-*` requests, реально требующие Owner/ROD decision;
4. approved material exceptions near expiry/review trigger;
5. company-critical risks с missing/stale control evidence;
6. risk-acceptance decisions pending;
7. unresolved residual risks after incident recovery;
8. waiting external cases только когда наступил legitimate review trigger;
9. остальные material open items grouped by accountable Position/scope.

Closed items, routine product incidents и low-impact risks не занимают default Owner attention.

Owner должен видеть: `what happened/could happen`, `why now`, `what is confirmed vs uncertain`, `who owns control`, `what source says`, `what authority is needed`, `next safe control point`.

## 17. Update / reconciliation / closure

Entry обновляется при material change, а не на каждый log event.

Material change включает:

- new evidence changing exposure/impact;
- control failure/recovery;
- new/expired/revoked exception;
- incident transition requiring management action;
- changed obligation/customer/cash scope;
- new risk acceptance/decision;
- changed authority or external gate;
- source correction/root-cause confirmation;
- residual risk creation/removal.

Conflict with authoritative source resolves in favor of source in its scope. Company interpretation is reconciled with history preserved.

Closed IDs не переиспользуются. Reopen same logical concern MAY preserve identity when prior closure was premature/error; materially new incident/risk/exception cycle gets new ID and relationship to prior item.

## 18. Minimal implementation baseline

AC-403 утверждает semantic model, не implementation.

Допустимы:

- Markdown/YAML/JSON register;
- lightweight scripts/projections;
- restricted/private complementary evidence stores;
- later Arvectum OS domain-neutral records/projections through explicit governed boundary.

Software dashboard, SIEM, incident automation, paging, risk scoring engine или ticket synchronization не являются prerequisite.

Критерий: самый простой механизм, который сохраняет stable identity, accountable Position, source references/freshness, explicit authority gates, minimization and reconstructable history.

## 19. Arvectum OS adoption rule

Если позже Company использует Arvectum OS:

1. Company risk/exception/business semantics остаются Company-owned;
2. OS предоставляет только admitted domain-neutral records/relationships/governed execution/projection;
3. Company Organization/Actor/access/data scope сохраняется;
4. OS technical incident or governed-action evidence не становится Company risk acceptance;
5. OS projection/dashboard remains non-authoritative unless applicable canonical contract expressly says otherwise;
6. no Company `RSK-*`/`EXC-*`/`INC-*` automatically changes OS lifecycle/contract state;
7. cross-repo material commitment проходит `ROD-09`/applicable governance.

## 20. Handoff в AC-404…AC-407

### AC-404 — Cash, commitment and management reporting baseline

AC-403 передаёт cash/financial-risk/incident/obligation references. AC-404 определит management reporting; bank/accounting transaction truth остаётся external authoritative.

### AC-405 — Portfolio/module/priority review cadence

AC-403 передаёт material open risks/exceptions/incidents как review inputs; AC-405 определит cadence/aging/review mechanics.

### AC-406 — Owner Mission Control

AC-403 передаёт owner-attention ordering, uncertainty and authority-needed semantics; AC-406 решит presentation/evidence aggregation.

### AC-407 — Management operating cadence

AC-403 передаёт active control subjects and review triggers; AC-407 определит operating cadence and closure/reconciliation routines.

## 21. Acceptance criteria

AC-403 может быть утверждён только если cross-review подтверждает:

- [ ] risk ≠ issue ≠ exception ≠ incident;
- [ ] accepted risk требует attributable competent decision when authority is required;
- [ ] exception request ≠ approved exception;
- [ ] technical workaround/admin access/urgency ≠ waiver;
- [ ] non-waivable higher-authority boundary preserved;
- [ ] incident detection/containment/recovery не создают authority;
- [ ] containment ≠ risk acceptance;
- [ ] `RSK-*`, `EXC-*`, `INC-*` stable identities separated;
- [ ] AC-105 consequence model preserved without fabricated probabilities;
- [ ] AC-207 continuity/fail-closed semantics preserved;
- [ ] AC-202 `ROD-*` and AC-203 `AM-*` preserved;
- [ ] AC-401 `WORK-*`/`OBL-*` and AC-402 `DEC-*`/`APR-*`/`ESC-*` relationships clean;
- [ ] P0 is material/time-sensitive, not universal incident severity;
- [ ] Owner queue contains only actual Owner authority work;
- [ ] stale/missing evidence cannot silently become safe/accepted/closed;
- [ ] incident closure does not close obligations/residual risks by implication;
- [ ] product/security/legal/customer/accounting/OS sources remain authoritative in their scopes;
- [ ] public-repo minimization and least privilege preserved;
- [ ] no duplicate security tracker/bug tracker/incident runtime created;
- [ ] no numeric risk theater invented;
- [ ] no dashboard/runtime/automation/spend/customer commitment/Product Contract created by implication;
- [ ] downstream AC-404…AC-407 handoff remains bounded.

## 22. Explicit non-effects

Даже после Owner approval AC-403 сам по себе не:

- создаёт live population `RSK-*`/`EXC-*`/`INC-*`;
- доказывает полноту Company risk inventory;
- принимает конкретный риск;
- разрешает конкретный exception;
- создаёт incident-response authority;
- разрешает bypass control;
- доказывает legal/compliance/security/customer impact;
- создаёт statutory/customer notification obligation;
- создаёт бюджет/spend/contract/SLA/pilot/production commitment;
- меняет Assignments/access/credentials;
- закрывает customer/product/legal obligations;
- создаёт SIEM/dashboard/paging/automation;
- принимает OS Decision Authority Policy;
- создаёт OS Product Contract/Capability transition;
- закрывает AC-404…AC-407.

Первое фактическое наполнение risk/exception/incident register требует отдельного bounded evidence step по current confirmed sources и не предполагается complete этим model-design artifact.

## 23. Proposal result

Предлагаемый AC-403 baseline:

```text
authoritative evidence / source incidents / current controls
                     ↓
       RSK-* / EXC-* / INC-* Company control
                     ↓
Position accountability + P0…P3 + attention/freshness
                     ↓
WORK/OBL ↔ DEC/APR/ESC relationships
                     ↓
explicit risk acceptance / exception approval where required
                     ↓
Owner sees only material exposure and real authority gates
```

Это минимально достаточная risk-control модель для M4 без parallel security/product/legal system и без превращения risk register в источник authority.

Approval требуется от Owner как durable Company governance/operating-model decision. До explicit approval exact reviewed proposal остаётся `Proposed 0.9.0` и не является binding Company state.