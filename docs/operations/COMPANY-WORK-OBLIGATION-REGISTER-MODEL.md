# AC-401 — Company Work / Obligation Register Model

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-401 — Company work/obligation register model`
Предшествующий milestone: `M3 — Complete / PASS`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение

AC-401 определяет минимальную Company-level модель реестра существенных работ и обязательств ООО «Арвектум», достаточную для operational visibility собственника и последующих `AC-402…AC-406`.

Реестр должен отвечать на практические вопросы:

- какие **существенные Company-level работы** сейчас требуют организационного контроля;
- какие **реальные обязательства** могут породить срок, триггер, денежный, клиентский, юридический, continuity или репутационный эффект;
- какая долговременная `Position` отвечает за контроль соответствующего предмета;
- что является текущим Company priority context;
- где находится authoritative source/evidence;
- какой следующий **control point**, а не следующий технический subtask;
- существует ли `waiting`, `blocked`, `needs attention` или escalation condition;
- требуется ли действие Owner/другой authority либо работа может продолжаться в уже утверждённых границах.

AC-401 намеренно **не** создаёт универсальный project tracker, бухгалтерскую книгу, CRM, договорный реестр, issue tracker, workflow runtime или dashboard.

Главный результат:

> Собственник получает один устойчивый Company control layer для material work и obligations, не восстанавливая контекст вручную из чатов и нескольких репозиториев и не превращаясь в диспетчера каждой low-risk задачи.

## 2. Governing baseline

AC-401 подчинён применимым юридическим/корпоративным источникам, Ratified Company Constitution и уже Approved Company governance.

Ключевые действующие границы:

1. `AC-102` разделяет statutory/accounting truth, management-finance interpretation и product/project economics. Company repository не должен становиться параллельной бухгалтерией.
2. `AC-106` задаёт общий порядок:
   - `P0` — protect current obligations, cash and material risk;
   - `P1` — flagship market evidence + minimal reference operating model;
   - `P2` — product/OS work directly tied to revenue, obligations, evidence or blockers;
   - `P3` — speculative expansion.
3. `AC-202` сохраняет `ROD-01…ROD-09` как Reserved Owner Decisions и прямо отделяет recommendation/technical execution от Owner approval.
4. `AC-203` задаёт `AM-0…AM-4`, deny-by-default authority и escalation/fail-closed при превышении границ.
5. `AC-204` устанавливает долговременные Positions, включая:
   - `POS-001 — Company Executive`;
   - `POS-002 — Commercial & Customer Lead`;
   - `POS-003 — Portfolio & Product Lead`;
   - `POS-004 — Engineering & Release Lead`;
   - `POS-005 — Finance & Obligation Control Lead`;
   - `POS-006 — Security, Risk & Continuity Lead`.
6. `AC-205` допускает текущую hybrid/AI-led реализацию Positions, но Assignment/runtime не заменяют Position accountability и не создают authority.
7. `AC-301…AC-307` закрепляют, что Company repository хранит Company-level portfolio identity/accountability/investment/priority meaning, а product implementation/status остаётся в product repositories.
8. M4 roadmap требует material visibility без создания parallel source of truth и прямо допускает manual/simpler controls до появления software dashboard.

## 3. Arvectum OS boundary check

Перед AC-401 проверен current `arvectum/arvectum-os` `main` на commit:

`8d35eb3867c4aed60f7aaa201c0c03a9aa3b1353`.

Текущий OS state включает завершённый `P9.04 — My Work / Needs Attention projection`. P9.04 принципиально важен для AC-401 как **совместимый будущий presentation mechanism**, но не как источник Company business state:

- `My Work` является derived, non-authoritative projection;
- projection visibility не создаёт Authorization, Organizational Authority или Consequential Approval;
- P9.04 намеренно не выводит произвольный business status из opaque persisted payload;
- текущие live adapters P9.04 ограничены уже доказанными OS source semantics;
- protected/stale/degraded data fail closed;
- P9.04 не создаёт Stable Product Contract, Active capability или Company-specific work model.

Следствие для AC-401:

> Company register semantics принадлежат `arvectum-company`. Arvectum OS может позднее хранить/проецировать/исполнять их только через применимый domain-neutral contract/governed path. AC-401 не добавляет Company-specific semantics в OS и не создаёт hidden coupling к P9.04.

## 4. Что является реестром

Реестр — это **Company control register**, состоящий из двух классов entries:

```text
Company Control Register
├── WORK-* — material Company-level work item
└── OBL-*  — material obligation control item
```

Оба типа используют общий control envelope, но имеют разный смысл.

### 4.1 `WORK-* — Material Company Work Item`

`WORK-*` — ограниченная единица Company-level работы, которую стоит видеть на уровне управления Компанией, потому что она materially влияет на obligation/risk/continuity/client value/revenue/economics/portfolio/Owner attention или межрепозиторную координацию.

`WORK-*` **не** равен:

- issue/ticket/commit;
- sprint task;
- product backlog item;
- каждому техническому действию;
- каждой строке roadmap;
- каждому запросу Owner к AI.

Одна Company-level работа может ссылаться на десятки product issues/commits, не копируя их в реестр.

### 4.2 `OBL-* — Material Obligation Control Item`

`OBL-*` — Company-level control representation реального обязательства, которое уже существует на основании надлежащего внешнего/корпоративного/договорного/операционного источника и требует management visibility из-за возможного последствия.

Категории обязательств наследуются из AC-102:

1. `corporate/statutory`;
2. `customer`;
3. `supplier/contractor`;
4. `recurring operating`;
5. `procurement/financing`;
6. `product/support`.

Создание `OBL-*` **не создаёт обязательство**. Реестр только отражает Company-level operating meaning существующего обязательства и указывает на authoritative source.

## 5. Двухслойная canonicality

AC-401 запрещает смешивать Company control truth и underlying fact truth.

### 5.1 Что может быть canonical в Company register

Внутри declared Company scope реестр может быть canonical source для следующих control facts:

- entry включён в material Company control layer;
- stable `WORK-*` / `OBL-*` identity;
- Company-level краткое operating meaning;
- accountable Position;
- текущий Company priority context;
- control state;
- attention/escalation state;
- следующий control point;
- ссылки на evidence/authoritative sources;
- дата последней проверки Company control metadata;
- closure/supersession history реестровой записи.

### 5.2 Что НЕ становится authoritative из-за попадания в реестр

Underlying facts остаются в своих источниках:

- договор, юридическая обязанность, корпоративный акт — применимый legal/corporate source;
- банковский остаток, платёж, налоговая/accounting truth — банк/учётный контур/профессиональный бухгалтерский источник;
- customer acceptance и договорные evidence — соответствующий договорный/customer evidence contour;
- product implementation/status — product repository;
- Arvectum OS contract/capability/runtime state — `arvectum/arvectum-os`;
- source-system fact — соответствующий authoritative external system.

Реестр хранит **reference + management interpretation**, а не конкурирующую копию первичной истины.

## 6. Qualification gate: что попадает в реестр

Entry создаётся только если существует Company-level control need.

### 6.1 Достаточные основания для `WORK-*`

Работа SHOULD попасть в реестр, если выполняется хотя бы одно из условий:

- она прямо защищает/исполняет существующее material obligation, cash exposure или material risk;
- она является текущей material Company roadmap/governance работой с cross-position/cross-repository эффектом;
- она требует scarce Owner attention, Owner decision preparation или material escalation;
- она materially влияет на customer delivery/acceptance/revenue/continuity;
- она имеет bounded outcome и stop/completion condition, важные для Company investment/control;
- она является Company-level blocker для нескольких product/work streams;
- потеря/забывание её состояния создаст существенный reconstruction burden или downside.

### 6.2 Достаточные основания для `OBL-*`

Обязательство SHOULD попасть в реестр, если:

- его пропуск/просрочка/неисполнение может materially повлиять на cash, customer relationship, legal/corporate position, tax/accounting coordination, security/data, continuity или reputation;
- оно имеет date/trigger/condition, которую необходимо не потерять;
- требуется взаимодействие нескольких Positions/контуров;
- оно создаёт procurement/financing cash-gap или иной material exposure;
- оно требует Owner attention или material decision/escalation;
- underlying source остаётся внешним, но Company management должна видеть текущий control state.

### 6.3 Что по умолчанию НЕ попадает

Не регистрируются автоматически:

- обычные product backlog tasks;
- routine coding/review/test work в уже утверждённом bounded scope;
- каждый GitHub issue/PR/commit;
- каждая банковская операция или бухгалтерская проводка;
- каждый invoice/receipt/subscription без material Company control need;
- каждый email/chat/request;
- идеи и hypotheses без принятого work scope;
- telemetry/log events без отдельного material control meaning;
- низкорисковые обратимые действия, которые Position может выполнять в своей authority boundary без Owner visibility.

Правило:

> Если item удобнее и точнее живёт в product tracker/accounting/legal/customer/source system и не требует Company-level control, он остаётся там.

## 7. Stable identity и дедупликация

### 7.1 IDs

Используются два независимых namespace:

- `WORK-001`, `WORK-002`, ...;
- `OBL-001`, `OBL-002`, ... .

ID стабилен для одного logical Company control subject и не должен переиспользоваться после closure.

### 7.2 Один control concern — одна запись

Нельзя создавать отдельную Company entry для каждого source document, issue или технического шага одного и того же management concern.

Связанные lower-level объекты указываются через references.

### 7.3 Work и obligation могут быть связаны, но не сливаются

Пример семантики:

```text
OBL-* real customer/support obligation
        ↓ requires / motivates
WORK-* bounded Company-level fulfillment work
```

Закрытие `WORK-*` не означает автоматически удовлетворение `OBL-*`; для obligation требуется собственное satisfaction evidence из authoritative source.

## 8. Common control envelope

Каждый active `WORK-*` или `OBL-*` MUST иметь минимум следующие поля.

| Поле | Назначение |
|---|---|
| `id` | stable `WORK-*` или `OBL-*` identity |
| `kind` | `work` или `obligation` |
| `title` | короткое human-readable название |
| `control_summary` | Company-level operating meaning; без лишних закрытых деталей |
| `accountable_position` | ровно одна primary accountable `POS-*` Position |
| `scope_refs` | Company / `PORT-*` / product repo / customer-project / OS / external scope references |
| `company_priority` | текущий `P0/P1/P2/P3` context по AC-106 с кратким `why now` |
| `control_state` | `open`, `waiting`, `blocked`, `closed` |
| `attention_state` | `normal`, `needs_attention`, `escalated` |
| `due_or_trigger` | дата, окно, событие/условие либо `none`; только с достаточным evidence |
| `next_control_point` | следующий management/control checkpoint, не технический micro-task |
| `source_refs` | authoritative/evidence references; underlying truth не копируется |
| `evidence_as_of` | когда динамический source последний раз проверен |
| `escalation_need` | `none` или причина/target escalation без имитации approval |
| `classification_handling` | минимизация/ограничение раскрытия, если materially relevant |
| `last_reviewed_at` | последняя проверка Company control metadata |
| `closure_ref` | для closed item — evidence/decision/source, объясняющий closure |

### 8.1 Primary accountability

`accountable_position` — долговременная Position, а не имя текущего AI/model/runtime и не обязательное имя физического исполнителя.

Assignment/Principal MAY быть указан только отдельной reference, если это действительно нужно для текущего исполнения/эскалации. Его замена не меняет `WORK-*`/`OBL-*` identity или Position accountability.

### 8.2 `company_priority`

Priority — это **sequencing context**, а не spend authorization и не lifecycle state.

- реальный time-sensitive material obligation/cash/risk issue получает `P0`;
- `P1/P2/P3` применяются по exact AC-106 semantics;
- portfolio band `A1/A2/B1…` не заменяет `P0…P3` и может быть только referenced evidence;
- изменение priority не изменяет product disposition или obligation truth автоматически.

### 8.3 `due_or_trigger`

Нельзя придумывать точную дату, если source определяет только условие/окно.

Допустимы:

- exact date/time;
- date window;
- event/condition trigger;
- periodic external renewal trigger;
- `unknown/uncertain` с `needs_attention`, если отсутствие точности materially опасно;
- `none`, если item не deadline-driven.

## 9. Type-specific fields

### 9.1 `WORK-*`

Дополнительно MUST быть определены:

| Поле | Смысл |
|---|---|
| `bounded_outcome` | какой Company-level результат должен существовать |
| `completion_or_stop_condition` | когда работа считается завершённой, остановленной или требует нового решения |
| `execution_refs` | product/roadmap/issue/PR/workflow refs, где живёт фактическое исполнение |

`WORK-*` не должен дублировать granular execution status. Если подробный status нужен — он читается из `execution_refs`.

### 9.2 `OBL-*`

Дополнительно MUST быть определены:

| Поле | Смысл |
|---|---|
| `obligation_class` | одна из шести AC-102 management classes |
| `authoritative_obligation_ref` | договор/акт/система/провайдер/accounting/legal/customer source, создающий или подтверждающий obligation |
| `satisfaction_condition` | что должно быть подтверждено authoritative evidence для снятия control need |
| `satisfaction_evidence_ref` | заполняется при наличии; register summary не является доказательством исполнения |

Counterparty/authority details SHOULD храниться как reference/minimal label, если полные реквизиты не нужны для management visibility.

## 10. Control state ≠ substantive truth

Чтобы реестр не создавал параллельную authority, `control_state` описывает только **Company control handling**, а не юридическую или продуктовую истину.

### `open`

Item находится под активным Company control.

### `waiting`

Следующий legitimate control movement зависит от внешнего события, клиента, провайдера, authority, физического host/access gate или иного ожидаемого условия.

`waiting` не означает failure и не требует регулярных бессмысленных retry.

### `blocked`

Известный blocker не позволяет безопасно перейти к следующему bounded outcome/control point.

Blocker должен иметь source/reason и escalation/exit condition, если materially relevant.

### `closed`

Company control need завершён, superseded или больше не material в declared scope.

Для obligation `closed` означает только, что Company register больше не считает item активным; основание должно ссылаться на удовлетворение/прекращение/замену authoritative obligation, а не на субъективную отметку.

## 11. Attention state и escalation

### `normal`

Нет отдельного attention signal сверх обычного control cadence.

### `needs_attention`

Требуется ближайшая проверка/подготовка/действие из-за срока, uncertainty, drift, blocker, missing evidence или приближения decision gate.

### `escalated`

Item пересёк утверждённую Position/Assignment/workflow boundary либо имеет material exception, требующую более высокой/иной authority.

`escalated` **не означает**, что Owner уже одобрил решение.

`escalation_need` должен указывать минимум:

- почему текущая boundary недостаточна;
- к какой authority/Position/внешнему контуру относится следующий gate;
- какой bounded evidence packet нужен.

Точная decision/approval record semantics относится к `AC-402`.

## 12. Source/freshness/uncertainty discipline

### 12.1 Reference over copy

Если authoritative source доступен по стабильной ссылке/идентификатору, register SHOULD хранить reference и минимальную management summary, а не копировать payload.

### 12.2 Dynamic evidence

Для динамических фактов (`cash`, product status, customer acceptance, provider availability, current OS state и т. п.) `evidence_as_of` обязателен, если stale data может изменить решение.

### 12.3 Uncertainty

Если source недоступен, двусмыслен или устарел:

- нельзя silently считать прошлое значение current;
- нельзя превращать unknown в zero/false/complete;
- при material consequence item становится `needs_attention` либо `escalated`;
- downstream view обязан показывать uncertainty честно.

### 12.4 No blind retry

Known unavailable physical/access/external gate не должен автоматически порождать повторные Owner actions. `waiting` с trigger/next legitimate check лучше, чем постоянный `needs_attention` noise.

## 13. Owner control projection

AC-401 определяет **semantics**, а не UI.

Default Owner-facing projection SHOULD выводить в первую очередь:

1. `P0` items;
2. `attention_state = escalated`;
3. `attention_state = needs_attention`;
4. due/trigger uncertainty с material consequence;
5. `blocked`/`waiting` items, где наступил legitimate review trigger;
6. остальные material open `P1/P2` items, сгруппированные по accountable Position / scope;
7. `P3` только когда это нужно для конкретного review/decision, а не как постоянный noise.

Closed history по умолчанию не занимает Owner attention, но остаётся reconstructable через repository/history/source refs.

Owner view должен объяснять:

- what;
- why now;
- accountable Position;
- source/evidence freshness;
- next control point;
- whether attention/escalation is actually required.

Он не должен требовать чтения raw commit history для обычного управления.

## 14. Position accountability mapping

AC-401 не создаёт новые Positions.

Default functional mapping следует уже Approved AC-204:

| Control subject | Primary accountable Position по умолчанию |
|---|---|
| Company-wide strategy/current operating coordination | `POS-001` |
| customer/commercial delivery obligation | `POS-002` |
| portfolio/product investment/control work | `POS-003` |
| engineering/release execution needing Company-level control | `POS-004` |
| cash/financial/obligation control | `POS-005` |
| security/risk/continuity material control | `POS-006` |

Это default ownership mapping, а не автоматическая authority grant.

Если один item пересекает несколько функций, одна Position остаётся primary accountable, а остальные указываются references/consulted/supporting capacities. Несколько «совладельцев» не должны размывать accountability.

## 15. Authority and approval boundary

Сам факт наличия или изменения register entry:

- не создаёт legal/corporate authority;
- не создаёт customer/vendor obligation;
- не утверждает spend/budget;
- не является Owner approval;
- не делегирует `ROD-*`;
- не активирует `AM-3/AM-4`;
- не разрешает external mutation;
- не подтверждает contract satisfaction;
- не изменяет Product Contract или Arvectum OS lifecycle.

Реестр может **указывать**, что нужен decision/approval/escalation, но exact decision должен быть оформлен через `AC-402`/applicable authority source.

Recommendation, AI summary, status update, silence и наличие `next_control_point` не являются approval.

## 16. Security, privacy and minimization

Company control visibility не оправдывает дублирование чувствительных данных.

Реестр MUST NOT содержать без необходимости:

- passwords, tokens, private keys, recovery codes;
- полные банковские реквизиты/transaction payload;
- лишние персональные данные;
- полные customer documents/contracts, если достаточно reference;
- закрытые product/customer payloads только ради удобства dashboard;
- raw model prompts/chain-of-thought;
- confidential source material, не требуемый для management decision.

Если Owner-facing summary может быть сформирована из identifiers/references/classification labels, предпочтителен минимизированный вариант.

Access к future software representation MUST наследовать Company/OS least-privilege, scope, classification and audit requirements. Видимость item не создаёт permission на underlying source.

## 17. Update, reconciliation and closure rules

### 17.1 Event-driven update

Entry обновляется при material change, например:

- смена accountable Position;
- возникновение/снятие blocker;
- изменение due/trigger;
- получение new authoritative evidence;
- изменение Company priority;
- появление escalation/Owner gate;
- satisfaction/termination/supersession;
- изменение classification/handling materially affecting control.

Реестр не требует update на каждый технический commit.

### 17.2 Reconciliation

Если register summary конфликтует с authoritative source:

1. authoritative source побеждает в своём scope;
2. Company entry помечается `needs_attention`/`escalated` при material effect;
3. summary/evidence refs обновляются;
4. history не переписывается так, чтобы скрыть прежнюю ошибку/устаревание.

### 17.3 Closure

`WORK-*` закрывается по `completion_or_stop_condition` + evidence/decision reference.

`OBL-*` закрывается только когда authoritative source/evidence подтверждает satisfaction, lawful termination, expiry, waiver/replacement или иной valid reason; register отметка сама по себе недостаточна.

### 17.4 Reopen vs new ID

- тот же logical subject, временно закрытый ошибочно/преждевременно, MAY быть reopened с history;
- новое отдельное обязательство/новый bounded work concern MUST получить новый ID;
- recurring obligations SHOULD использовать новый item для нового самостоятельного obligation period, если новый период имеет отдельный source/due/satisfaction cycle.

## 18. Minimal implementation baseline

AC-401 утверждает semantic model, а не software implementation.

Минимально допустимые реализации после approval:

- Markdown/YAML/JSON register в Company repository;
- lightweight script/projection;
- later Arvectum OS governed records/projection через explicit admitted boundary;
- другой заменяемый storage/presentation mechanism.

Критерий выбора:

> Самый простой вариант, который сохраняет stable identity, source references, accountability, material visibility, history и minimization без скрытого параллельного source of truth.

Software dashboard не является prerequisite.

## 19. Arvectum OS adoption rule

AC-401 **не требует** немедленно переносить register в Arvectum OS.

Если позже Company решит использовать OS для persistence/projection/governed execution:

1. Company semantics остаются Company/product-owned;
2. OS получает только domain-neutral records/relationships/execution semantics;
3. applicable Product Contract / extension / governed integration boundary определяется до material reliance;
4. exact Organization/Actor/authorization/data-governance scope сохраняется;
5. P9.04-like `My Work` остаётся derived projection, а не source of Company obligation truth;
6. stale/degraded/denied source state не должен превращаться в ложный current item;
7. OS integration не создаёт Organizational Authority.

## 20. Handoff в AC-402…AC-406

AC-401 оставляет downstream задачи раздельными.

### `AC-402 — Decision, approval and escalation register model`

AC-401 передаёт:

- `escalation_need`;
- Owner/authority gate indication;
- `WORK-*` / `OBL-*` identity для relationship.

AC-402 должен определить сам decision/approval record; AC-401 его не имитирует.

### `AC-403 — Risk, exception and incident register model`

AC-401 передаёт material risk/exception references и attention state, но не создаёт risk taxonomy/incident semantics заранее.

### `AC-404 — Cash, commitment and management reporting baseline`

AC-401 передаёт obligation/cash-related control identities и authoritative accounting/bank references. Transaction truth остаётся вне Company register.

### `AC-405 — Portfolio/module/priority review cadence`

AC-401 даёт material work/obligation inputs. AC-405 отдельно определит periodic review cadence и portfolio review mechanics.

### `AC-406 — Owner Mission Control / reference-implementation evidence view`

AC-401 задаёт work/obligation semantics и owner-facing attention ordering. AC-406 решит presentation/evidence aggregation, не меняя authority/canonicality.

## 21. Acceptance criteria

AC-401 может быть утверждён только если cross-review подтверждает все пункты:

- [ ] register не является parallel accounting/legal/product/project source of truth;
- [ ] `WORK-*` и `OBL-*` различены;
- [ ] stable identities и deduplication rule заданы;
- [ ] qualification gate предотвращает превращение register в universal task list;
- [ ] Company control canonicality отделена от underlying fact authority;
- [ ] primary accountable Position обязательна;
- [ ] current Principal/runtime не подменяет Position;
- [ ] AC-106 `P0…P3` preserved;
- [ ] P0 не превращает любой incoming request в emergency;
- [ ] control state отделён от substantive legal/product/accounting truth;
- [ ] due/trigger допускает uncertainty и не фабрикует даты;
- [ ] source/evidence freshness discipline определена;
- [ ] waiting/blocked semantics не создают blind retry noise;
- [ ] attention/escalation не равны approval;
- [ ] `ROD-*`, `AM-*` и legal/corporate authority boundaries preserved;
- [ ] data minimization / secret handling preserved;
- [ ] product repositories остаются implementation/status truth;
- [ ] Arvectum OS P9.04 остаётся derived/non-authoritative presentation mechanism;
- [ ] no hidden Company→OS Product Contract/lifecycle commitment created;
- [ ] downstream AC-402…AC-406 получают чистый handoff без преждевременного проектирования их scope.

## 22. Explicit non-effects

Даже после Owner approval AC-401 сам по себе не:

- создаёт конкретный live `WORK-*`/`OBL-*` population;
- подтверждает полноту всех существующих обязательств Компании;
- проводит legal/accounting audit;
- утверждает бюджет или spend;
- создаёт customer/vendor commitment;
- создаёт/делегирует authority;
- меняет Assignments или access;
- закрывает реальный customer/product obligation;
- меняет product roadmap/status;
- создаёт Arvectum OS Product Contract;
- делает Platform Capability Active;
- создаёт dashboard/runtime/automation;
- закрывает `AC-402…AC-407`.

После утверждения отдельным bounded шагом может быть создан **первый фактический register population** на основе только подтверждённых current sources. Его полнота и freshness должны быть доказаны отдельно; они не предполагаются AC-401 model design.

## 23. Proposal result

Предлагаемый AC-401 baseline:

```text
authoritative sources remain authoritative
            ↓ references + freshness
WORK-* / OBL-* Company control entries
            ↓
Position accountability + priority + control state
            ↓
attention / escalation / next control point
            ↓
Owner-facing projection
            ↓
AC-402 / AC-403 / AC-404 governed specialized registers
```

Это минимально достаточная модель для старта M4: material work и obligations становятся видимыми, но Company не строит вторую бухгалтерию, второй GitHub, второй договорный архив или скрытый authority engine.

Approval требуется от Owner как Company-level durable governance/operating-model decision. До явного approval этот proposal остаётся `Proposed 0.9.0` и не является binding Company state.
