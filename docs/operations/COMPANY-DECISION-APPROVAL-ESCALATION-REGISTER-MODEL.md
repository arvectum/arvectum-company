# AC-402 — Decision, Approval and Escalation Register Model

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-402 — Decision, approval and escalation register model`
Предшественник: `AC-401 — Approved 1.0.0`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение

AC-402 определяет минимальную Company-level модель реестра существенных решений, approval gates/acts и эскалаций поверх утверждённого AC-401 Company Work / Obligation Register.

Модель должна позволять собственнику и accountable Positions без восстановления контекста из чатов понимать:

- **какой вопрос реально требует решения** и что пока является только proposal/recommendation;
- кто имеет право принять внутреннее решение и на каком основании (`ROD-*`, `AM-*`, residual authority или иной утверждённый источник);
- требуется ли отдельный corporate/legal/customer/other approval gate после или наряду с внутренним Company decision;
- какое approval ещё `pending`, какое получено, отклонено, отложено, истекло, отозвано или заменено;
- почему возникла escalation и к какой authority она направлена;
- какие `WORK-*`, `OBL-*`, `PORT-*`, product/OS/external scopes затронуты;
- что именно разрешено после решения и какие эффекты остаются запрещёнными;
- когда решение/approval перестаёт быть пригодным из-за expiry, changed facts, supersession или stale evidence.

AC-402 не создаёт decision authority. Он делает уже существующие authority gates и material decisions **видимыми, attributable и reconstructable**.

Главный результат:

> `recommendation ≠ decision ≠ approval ≠ legal/corporate act ≠ technical authorization ≠ execution`.

## 2. Governing baseline

AC-402 подчинён applicable legal/corporate authority, Ratified Company Constitution и уже Approved Company governance.

Ключевые действующие правила:

1. Company Constitution Article VI: Organizational Authority возникает из valid legal/corporate authority и approved Company governance, а approval является отдельным governance act; recommendation, draft, analysis, technical execution или workflow completion не являются approval.
2. Company Constitution Article XI: material durable decisions должны сохранять context, rationale, authority, accepted risk, effective date и review/supersession condition пропорционально impact.
3. `AC-202 — Reserved Owner Decisions`:
   - `ROD-01…ROD-09` являются hard final-decision boundary;
   - explicit attributable Owner act обязателен для Reserved Owner Decision;
   - approve / reject / defer / approve-with-conditions должны различаться;
   - chat может переносить explicit act, но material durable decision должен быть promoted в canonical Company decision record.
4. `AC-203 — Delegated Position Authority, Approval and Escalation Model`:
   - `AM-0…AM-4` различают preparation, execution, bounded decision, delegated approval и pre-authorized automatic execution;
   - authority deny-by-default;
   - silence, technical capability, IAM access, AI confidence и workflow completion authority не создают;
   - stale/missing evidence, exceeded limits, `ROD-*`, unclear customer rights, uncertain external effects и authority/access mismatch требуют stop/fail-closed либо escalation.
5. `AC-204/AC-205` закрепляют durable Positions и текущие human/AI/software Assignments; executor identity не заменяет Position authority.
6. `AC-401 — Approved 1.0.0` задаёт `WORK-*`/`OBL-*`, accountable Position, priority/control/attention/freshness semantics и передаёт `escalation_need` в AC-402, но сам не создаёт decision/approval records.
7. Product implementation/status остаётся в product repositories; Arvectum OS contracts/platform state — в `arvectum/arvectum-os`; legal/corporate/customer/accounting facts — в соответствующих authoritative contours.

## 3. Arvectum OS compatibility boundary

Перед AC-402 проверен current `arvectum/arvectum-os` `main` на commit:

`8d35eb3867c4aed60f7aaa201c0c03a9aa3b1353`.

Применимые выводы:

- Accepted RFC baseline продолжает отделять Organizational Authority, Authorization, approval и Governed Execution;
- P9.04 `My Work / Needs Attention` остаётся derived, non-authoritative projection и не является decision source;
- OS `DECISION-AUTHORITY-POLICY.md` остаётся `Proposed 0.2.1` и **не является Company authority source**.

AC-402 MAY использовать domain-neutral OS mechanisms позже через надлежащий governed boundary, но Company-specific `ROD-*`, `AM-*`, Positions и decision semantics остаются Company-owned.

Никакая часть AC-402 не утверждает OS Decision Authority Policy, не создаёт Stable Product Contract и не изменяет OS lifecycle.

## 4. Модель реестра

AC-402 вводит три независимых Company control namespaces:

```text
Company Decision Control Layer
├── DEC-* — material decision case / durable decision record
├── APR-* — approval gate / attributable approval act control record
└── ESC-* — escalation case
```

Типы связаны, но не должны сливаться.

### 4.1 `DEC-* — Material Decision Case`

`DEC-*` представляет один material Company decision subject: точный вопрос, который уполномоченная authority должна либо уже смогла разрешить.

`DEC-*` существует для решения, а не для каждого мнения или draft.

### 4.2 `APR-* — Approval Gate / Act`

`APR-*` представляет отдельный approval requirement и его текущий Company control state либо attributable approval act, когда такой gate действительно требуется.

Approval MAY быть:

- внутренним Owner approval по `ROD-*`;
- delegated approval по `AM-3`;
- отдельным legal/corporate approval/act requirement;
- customer/counterparty approval/consent/acceptance gate;
- иным approval gate, если его authority source определён.

`APR-*` не превращает Company repository в authoritative source для внешнего или legally regulated approval: для таких случаев он хранит reference + control interpretation.

### 4.3 `ESC-* — Escalation Case`

`ESC-*` представляет ситуацию, когда текущая Position/Assignment/workflow не может законно или безопасно продолжить в имеющемся authority envelope и должна передать bounded decision/evidence packet другой authority.

Escalation является успешным соблюдением boundary, а не признаком failure.

## 5. Что НЕ является самостоятельным типом реестра

AC-402 намеренно не создаёт отдельные Company IDs для:

- каждого AI recommendation;
- каждого proposal draft;
- каждой validation result;
- каждого GitHub review/comment;
- каждого routine `AM-2` choice;
- каждого technical permission/access check;
- каждого workflow step;
- каждого product architecture decision, который не требует Company-level material control.

Такие объекты MAY быть `proposal_refs`, `evidence_refs`, `execution_refs` или product/source records.

Qualification rule:

> Company decision register существует только там, где decision/approval/escalation materially влияет на Company control, obligations, capital/risk, customer/external effect, authority, portfolio, continuity или Owner attention.

## 6. Canonicality: внутреннее решение и underlying authority

### 6.1 Company-internal canonicality

Approved Company decision record MAY быть canonical для внутреннего Company Organizational Authority act в declared scope, если именно Company governance является источником такого решения.

Примеры:

- Owner `ROD-*` decision;
- properly delegated `AM-2` Company decision;
- attributable `AM-3` Company approval.

### 6.2 Внешняя / юридическая authority остаётся внешней

Если для эффекта требуется:

- participant/general-meeting decision;
- General Director legal act;
- power of attorney / bank / signature authorization;
- customer consent/acceptance;
- contract amendment;
- regulator/state-system act;
- Product governance decision;
- Arvectum OS RFC/ADR/Product Contract/lifecycle decision,

то Company register **не становится authoritative source** для такого факта.

Он хранит минимальный control record и ссылку на authoritative source.

### 6.3 Internal decision ≠ effect readiness

Внутреннее решение может быть принято, но consequential effect оставаться запрещённым до выполнения других gates.

Например:

```text
DEC-* Owner approves Company-side proposal
        ↓
APR-* required corporate/legal/customer gate still pending
        ↓
technical authorization still absent
        ↓
external effect MUST NOT execute
```

Поэтому `decision_outcome` и `effect_readiness` всегда различаются.

## 7. Stable identities и дедупликация

Используются независимые namespaces:

- `DEC-001`, `DEC-002`, ...;
- `APR-001`, `APR-002`, ...;
- `ESC-001`, `ESC-002`, ... .

IDs не переиспользуются после closure.

### 7.1 Decision instance rule

Один `DEC-*` соответствует одному logical decision instance с exact subject/scope.

Новый materially different decision, новый scope или пересмотр ранее принятого outcome SHOULD получать новый `DEC-*`, связанный через `supersedes` / `reconsiders` / `implements`.

Нельзя задним числом переписать историческое решение так, будто оно всегда имело новый смысл.

### 7.2 Approval rule

Один `APR-*` соответствует одному logical approval gate/act. Новый independent approval period, новая authority или materially changed scope получают новый ID.

### 7.3 Escalation rule

Один `ESC-*` соответствует одному bounded escalation concern. Нельзя создавать новое `ESC-*` на каждый reminder по одной и той же unresolved escalation.

## 8. `DEC-*` common envelope

Каждый material active `DEC-*` MUST иметь минимум:

| Поле | Назначение |
|---|---|
| `id` | stable `DEC-*` identity |
| `title` | короткое human-readable название |
| `decision_question` | точный вопрос, который должен быть решён |
| `scope_refs` | `WORK-*`, `OBL-*`, `PORT-*`, product/customer/OS/external scope refs |
| `proposer_or_preparer` | Position/Principal/reference, подготовивший proposal; не подразумевает authority |
| `accountable_position` | primary Company Position, отвечающая за подготовку/контроль decision case |
| `authority_basis` | `ROD-*`, `AM-*`, residual Owner authority либо другой valid internal source |
| `decision_authority` | required Position/Owner/capacity, имеющая право на final internal decision |
| `decision_state` | `preparing`, `ready`, `decided`, `deferred`, `cancelled`, `superseded`, `expired` |
| `decision_outcome` | `none`, `approve`, `reject`, `defer`, `approve_with_conditions` |
| `proposal_refs` | options/recommendations/drafts; proposal не является decision |
| `evidence_refs` | material evidence/source references |
| `evidence_as_of` | freshness boundary, если evidence динамично |
| `rationale_summary` | краткое durable rationale; без raw chain-of-thought |
| `constraints_excluded_effects` | точные условия и то, что решение не разрешает |
| `required_approval_refs` | связанные `APR-*` gates, если применимо |
| `effect_readiness` | `not_applicable`, `blocked`, `conditionally_ready`, `ready` |
| `execution_handoff` | accountable execution path после gates; не сама execution authority |
| `effective_at` | когда internal decision действует, если применимо |
| `review_expiry_trigger` | expiry/review/supersession condition |
| `decision_act_ref` | attributable evidence final decision act |
| `last_reviewed_at` | Company control review timestamp |

### 8.1 `decision_state` не заменяет outcome

`decided` означает наличие valid attributable decision act; его смысл задаётся отдельным `decision_outcome`.

`ready` означает readiness for decision, а не approved.

`deferred` означает explicit decision отложить; silence не превращается в defer.

### 8.2 Outcome semantics

Допустимые final/internal outcomes:

- `approve`;
- `reject`;
- `defer`;
- `approve_with_conditions`.

Любое другое wording MUST быть нормализовано настолько, чтобы было ясно, разрешён ли заявленный scope.

`approve_with_conditions` требует явных conditions и prohibited/excluded effects.

## 9. Decision preparation packet

Для material `ROD-*` и других consequential decisions `DEC-*` SHOULD ссылаться на bounded packet, достаточный для решения без Owner reconstruction burden.

Минимально, где применимо:

1. точный вопрос и scope;
2. why now / due-or-trigger;
3. accountable Position;
4. authority basis;
5. options/alternatives;
6. obligations/cash/economics impact;
7. downside, reversibility, recovery;
8. customer/legal/data/security/sovereignty implications;
9. dependencies / Product / OS boundary impact;
10. current evidence + uncertainty/freshness;
11. recommended outcome;
12. constraints/excluded effects;
13. approvals/legal acts still required after internal decision;
14. bounded execution plan after approval;
15. expiry/review trigger.

Packet является preparation evidence, а не approval.

## 10. `APR-*` approval model

Каждый material `APR-*` MUST различать **approval gate** и **approval act**.

Минимальные поля:

| Поле | Назначение |
|---|---|
| `id` | stable `APR-*` identity |
| `title` | human-readable gate |
| `scope_refs` | затронутые `DEC-*`/`WORK-*`/`OBL-*`/other refs |
| `approval_domain` | `company_internal`, `legal_corporate`, `customer_counterparty`, `product`, `arvectum_os`, `other_external` |
| `authority_basis` | source, определяющий необходимость и компетенцию approval |
| `required_approver_capacity` | Owner/Position/participant/General Director/customer/other capacity; не просто имя |
| `approver_eligibility_ref` | applicable delegation/authority evidence, где нужно |
| `approval_state` | `pending`, `approved`, `rejected`, `deferred`, `expired`, `revoked`, `superseded` |
| `approval_scope` | exact scope approval |
| `conditions_excluded_effects` | условия и ограничения |
| `approval_act_ref` | attributable evidence actual act; required for `approved/rejected/deferred` |
| `authoritative_source_ref` | mandatory, если Company repo не является authority source |
| `effective_period` | validity/review/expiry, где применимо |
| `evidence_as_of` | freshness для dynamic external gate |
| `last_reviewed_at` | Company control review |

### 10.1 Approval by silence prohibited

`approval_state = approved` MUST NOT выводиться из:

- silence;
- отсутствия objection;
- AI recommendation;
- favorable score;
- draft completion;
- repository write;
- technical success;
- workflow completion;
- наличие credential;
- прошлое approval похожего scope.

### 10.2 `AM-3` delegated approval

Для `AM-3` `APR-*` MUST ссылаться на active delegation, eligible Principal/capacity и exact limits. Превышение envelope переводит case в escalation, а не расширяет authority.

### 10.3 `ROD-*` approval

Для `ROD-*` `required_approver_capacity = Owner`, а `approval_act_ref` должен фиксировать explicit attributable Owner act.

Если чат является местом explicit act, durable decision должен быть promoted в canonical Company record с immutable/exact-content reference либо иным однозначным способом идентификации утверждённого scope.

### 10.4 Separate legal/corporate act

Если internal Owner approval и required legal/corporate act относятся к одному subject, они MUST оставаться двумя gates/capacities.

Совпадение их текущего physical Principal не позволяет объединять юридический и organizational смысл.

## 11. Technical authorization и execution

Technical authorization/access **не является APR-типом Company approval по умолчанию**.

`DEC-*`/`APR-*` MAY ссылаться на `technical_authorization_refs`, но наличие технического permission:

- не создаёт Organizational Authority;
- не создаёт approval;
- не означает effect readiness, если другие gates отсутствуют.

После решения/approval execution происходит через applicable Position/Assignment/access/workflow boundary.

`decision_act_ref` и `approval_act_ref` не должны использоваться как executable credential.

## 12. `ESC-*` escalation model

`ESC-*` создаётся, когда существует реальная boundary problem, требующая handoff другой authority/Position/external source.

Минимальные поля:

| Поле | Назначение |
|---|---|
| `id` | stable `ESC-*` identity |
| `title` | human-readable escalation |
| `source_refs` | `WORK-*`, `OBL-*`, `DEC-*`, `APR-*`, `PORT-*`, product/OS/external refs |
| `originating_position` | Position, корректно остановившая/эскалировавшая case |
| `reason_class` | нормализованная причина escalation |
| `reason_summary` | конкретная boundary/problem statement |
| `current_authority_boundary_ref` | delegation/ROD/contract/source, которого недостаточно |
| `target_authority` | Owner/Position/legal/customer/product/OS/other target |
| `required_packet_refs` | bounded evidence необходимое target authority |
| `escalation_state` | `open`, `waiting`, `resolved`, `withdrawn`, `superseded` |
| `owner_attention` | `required`, `not_required`, `waiting_external` |
| `due_or_trigger` | legitimate review/response trigger, если существует |
| `resolution_refs` | `DEC-*`/`APR-*`/external source/other valid resolution |
| `last_reviewed_at` | Company control review |

### 12.1 Reason classes

AC-402 нормализует как минимум AC-203 escalation triggers:

- `reserved_owner_decision`;
- `authority_absent_or_unclear`;
- `authority_expired_or_revoked`;
- `limit_exceeded`;
- `material_facts_changed`;
- `evidence_missing_stale_conflicting`;
- `non_standard_external_commitment`;
- `customer_rights_or_consent_unclear`;
- `material_risk_acceptance_required`;
- `company_product_os_boundary_change`;
- `irreversible_consequence_outside_envelope`;
- `technical_access_without_org_authority`;
- `uncertain_external_effect_or_retry_risk`;
- `continuation_after_emergency_containment_requires_acceptance`.

### 12.2 Owner attention discipline

Escalation SHOULD идти к Owner только если:

- case попадает в `ROD-*`/residual Owner authority;
- approved delegation прямо назначает Owner escalation target;
- другой компетентной authority нет;
- Company-side Owner decision действительно нужен перед external/legal/product/OS gate.

Escalation к customer, product owner, accountant/legal contour, Security/Risk Position или другому authority не должна создавать false Owner queue.

### 12.3 Waiting without noise

Если escalation корректно ждёт внешнего события/ответа и никаких Owner actions сейчас нет, `owner_attention = waiting_external`.

Known waiting state не должен генерировать постоянный `needs attention` noise до legitimate trigger.

## 13. Relationships

Минимальные типизированные отношения:

```text
WORK-* / OBL-* / PORT-* / external subject
        ↓ requires / informs
DEC-* decision case
        ↓ may require
APR-* approval gate(s)

WORK-* / OBL-* / DEC-* / APR-*
        ↓ boundary exceeded
ESC-* escalation
        ↓ resolved by
DEC-* / APR-* / authoritative external record
```

### 13.1 No implicit satisfaction

- `DEC-* approve` не закрывает `WORK-*` автоматически;
- `APR-* approved` не означает completed execution;
- `WORK-* closed` не означает `OBL-*` satisfied;
- `ESC-* resolved` не означает requested outcome approved;
- technical success не означает decision fulfilled in business/legal sense.

Каждый lifecycle закрывается только по своему source/evidence rule.

## 14. Freshness, changed facts and stale approvals

Material decision/approval MUST NOT использоваться вне basis, на котором он был дан.

Если после decision/approval materially изменились:

- customer terms;
- cash/economic exposure;
- risk/data/security context;
- product/OS contract state;
- scope;
- authority/delegation;
- evidence reliability;
- legal/corporate requirement,

то downstream executor MUST проверить `review_expiry_trigger` / applicable gate.

При существенном несовпадении:

- effect readiness становится `blocked`;
- decision/approval MAY стать `expired`/`superseded` либо потребовать новый decision;
- silent reuse prior approval запрещён.

Unknown ≠ approved.

## 15. Supersession, revocation and correction

### 15.1 Decisions

Принятое decision history не переписывается задним числом. Материальный пересмотр создаёт новый `DEC-*` либо history-preserving supersession record.

### 15.2 Approvals

Revocation/expiry не означает, что исторического approval никогда не было. Current usability прекращается, а исторический attributable act сохраняется.

### 15.3 Escalations

Resolved escalation остаётся reconstructable с resolution refs. Новая materially different boundary problem получает новый `ESC-*`.

## 16. Position accountability

AC-402 не создаёт новые Positions.

Default mapping сохраняет AC-204:

- Company-wide strategic/governance decisions — `POS-001` preparation/control;
- customer/commercial decision cases — `POS-002`;
- portfolio/investment — `POS-003`;
- engineering/release consequential decision prep — `POS-004`;
- finance/obligation control decisions — `POS-005`;
- security/risk/continuity — `POS-006`.

`accountable_position` отвечает за качество decision case/control record и корректную escalation, но не получает final authority по факту ownership.

Decision authority всегда определяется отдельно.

## 17. Owner-facing projection

AC-402 определяет semantics, не dashboard.

Default Owner view SHOULD показывать только cases, где Owner action действительно нужен:

1. `ROD-*` `DEC-*` со state `ready`;
2. Owner `APR-*` со state `pending`;
3. `ESC-*` с `owner_attention = required`;
4. approaching expiry/review triggers, если они требуют Owner renewal/reconsideration;
5. blocked P0 work/obligation, для которого blocker — Owner decision/approval.

View SHOULD объяснять:

- exact question;
- why now;
- linked work/obligation/portfolio subject;
- authority basis (`ROD-*`/residual/etc.);
- recommended outcome + alternatives;
- main downside/uncertainty;
- evidence freshness;
- exact Owner act needed;
- remaining gates after Owner act;
- what execution may proceed without Owner afterward.

Owner не должен получать raw review noise, routine AM-2 choices и external waiting cases без текущего Owner action.

## 18. Data minimization and public repository boundary

Репозиторий `arvectum-company` публичный. Поэтому decision-control records MUST NOT хранить без необходимости:

- signatures, full passport/personal details;
- banking/payment payload;
- contract/customer confidential text;
- secrets, tokens, private keys;
- reusable credentials;
- privileged security details;
- raw model prompts/chain-of-thought;
- sensitive legal/HR/customer evidence, если достаточно reference/minimal label.

Для sensitive decision нужен durable metadata/evidence pointer в публичном repo, а restricted payload остаётся в компетентном controlled source.

`rationale_summary` — управленческий rationale, а не private reasoning transcript.

## 19. Minimal implementation baseline

AC-402 утверждает semantic model, не конкретный runtime.

После approval допустимы:

- Markdown/YAML/JSON Company registers;
- repository scripts/projections;
- future Arvectum OS governed records/relationships/projection через admitted boundary;
- другой заменяемый mechanism.

Минимальная реализация должна сохранять:

- stable identity;
- exact authority basis;
- attributable act references;
- separation proposal/decision/approval/execution;
- source authority distinction;
- history/supersession;
- freshness/expiry;
- minimization;
- owner-attention filtering.

## 20. Arvectum OS adoption rule

Если Company позже отображает AC-402 через Arvectum OS:

1. OS не становится источником Company Organizational Authority;
2. Company-specific `ROD-*`, Positions и decision classes не переносятся в OS Kernel;
3. applicable Product Contract/extension boundary должен существовать до material reliance;
4. Organization/Actor/Authorization/Data Governance/approval gates остаются раздельными;
5. exact decision/approval acts должны быть attributable и version-aware proportionate to consequence;
6. P9.04/P9.06-like Workspace UI остаётся presentation/execution interface, а не authority source;
7. OS Proposed Decision Authority Policy не становится Company policy по импликации.

## 21. Handoff в AC-403…AC-406

### AC-403 — Risk, exception and incident register model

AC-402 передаёт `DEC-*`/`APR-*`/`ESC-*` refs, связанные с risk acceptance/exception, но не определяет risk taxonomy заранее.

### AC-404 — Cash, commitment and management reporting baseline

AC-402 передаёт decisions/approvals, влияющие на capital/exposure/obligations. Transaction truth остаётся accounting/banking source.

### AC-405 — Portfolio/module/priority review cadence

Portfolio review использует decision history/expiry/review triggers, но AC-402 не задаёт cadence.

### AC-406 — Owner Mission Control

AC-402 задаёт owner-facing decision/approval/escalation semantics. AC-406 агрегирует presentation без изменения authority.

### AC-407 — Management operating cadence

AC-407 позже проверит, работает ли separation и уменьшается ли Owner reconstruction/approval burden на реальных cases.

## 22. Prospective evidence

После реального использования SHOULD измеряться:

- число Owner decisions, действительно относящихся к `ROD-*`;
- escalations из-за missing delegation vs genuinely material boundary;
- approval latency;
- число cases с stale/missing evidence;
- prior approvals, которые нельзя было безопасно переиспользовать после changed facts;
- cases, где legal/corporate/customer gate оставался pending после internal decision;
- false Owner attention cases;
- decisions, где execution продолжился без ненужного повторного Owner involvement;
- attempts to infer approval from silence/technical success, предотвращённые моделью.

Цель — не максимальное число decision records, а **минимально достаточная reconstructable governance с минимумом Owner bottleneck**.

## 23. Acceptance criteria

AC-402 может быть утверждён только если cross-review подтверждает:

- [ ] proposal/recommendation отделены от decision;
- [ ] decision отделён от approval act/gate;
- [ ] internal Organizational Authority отделена от legal/corporate/customer/Product/OS authority;
- [ ] technical authorization/execution не считаются approval;
- [ ] `DEC-*`, `APR-*`, `ESC-*` имеют разные stable identities;
- [ ] routine low-risk decisions не превращаются в Company-wide bureaucracy;
- [ ] `ROD-01…ROD-09` preserved as hard final-decision boundary;
- [ ] `AM-0…AM-4` preserved without silent authority broadening;
- [ ] explicit attributable act required for approval/decision where applicable;
- [ ] silence/favorable AI output/workflow completion cannot create approval;
- [ ] approve/reject/defer/approve-with-conditions are unambiguous;
- [ ] decision outcome separated from effect readiness;
- [ ] separate corporate/legal/customer gates can remain pending after internal decision;
- [ ] one physical person holding multiple capacities does not merge those capacities;
- [ ] escalation goes to correct authority, not automatically Owner;
- [ ] external waiting does not create Owner noise;
- [ ] stale evidence/changed facts can block reuse prior approval;
- [ ] supersession/revocation preserve history;
- [ ] AC-401 `WORK-*`/`OBL-*` semantics remain intact;
- [ ] product/OS/source-of-truth boundaries preserved;
- [ ] data minimization/public-repository boundary preserved;
- [ ] OS Proposed Decision Authority Policy is not silently adopted;
- [ ] no dashboard/runtime/Product Contract/budget/external commitment created by implication;
- [ ] clean downstream handoff to AC-403…AC-407 exists.

## 24. Explicit non-effects

Даже после Owner approval AC-402 сам по себе не:

- создаёт фактический live population `DEC-*`/`APR-*`/`ESC-*`;
- принимает какое-либо business decision;
- выдаёт Owner approval;
- создаёт corporate/legal act;
- создаёт customer consent/acceptance;
- создаёт technical access;
- разрешает payment/signing/external mutation;
- делегирует `ROD-*`;
- расширяет `AM-*`;
- меняет Position/Assignment;
- создаёт budget/spend limit;
- закрывает risk/incident/cash/portfolio review scope последующих задач;
- меняет Product Contract или OS lifecycle;
- утверждает OS Decision Authority Policy;
- создаёт dashboard/runtime/automation.

## 25. Proposal result

Предлагаемый AC-402 baseline:

```text
proposal / evidence
       ↓
DEC-* exact material decision case
       ↓ authority check
explicit decision act
       ↓
APR-* separate approval/legal/customer gates where required
       ↓
effect_readiness
       ↓
Position / Assignment / technical authorization / execution

boundary exceeded anywhere
       ↓
ESC-* → correct authority → resolution reference
```

Это минимально достаточная decision-control модель для M4: Owner видит только реальные decision gates, approvals остаются attributable, external/legal authority не смешивается с внутренней governance, а low-risk работа не превращается в endless approval queue.

Approval требуется от Owner как Company-level durable governance/operating-model decision. До explicit approval exact reviewed proposal остаётся `Proposed 0.9.0` и не является binding Company state.
