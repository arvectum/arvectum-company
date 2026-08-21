# AC-401 — Cross-review: Company Work / Obligation Register Model

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `10 of maximum 10`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-401 — Company work/obligation register model`

Проверенный proposal:

- `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `0f4444fbd968e176a0a158771a7d0abe93549ecd`.

Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`.

## 1. Review gate

AC-401 должен быть отклонён, если модель:

- превращает Company repository в второй product/project tracker;
- создаёт параллельную бухгалтерскую, договорную, банковскую или юридическую truth;
- считает наличие register entry источником обязательства;
- автоматически трактует любой incoming request как `P0`;
- создаёт fuzzy shared accountability без primary Position;
- смешивает Position, Principal, Assignment и runtime;
- использует status в реестре как доказательство исполнения договора/обязательства;
- фабрикует due dates или трактует stale/unknown evidence как current;
- заставляет Owner вручную диспетчеризировать low-risk work;
- превращает `needs_attention`/`escalated` в approval/authority;
- дублирует secret/customer/accounting payload ради dashboard convenience;
- создаёт скрытую зависимость от Arvectum OS или P9.04;
- prematurely проектирует AC-402/403/404/405/406 вместо чистого handoff;
- создаёт spend, customer/vendor commitment, Product Contract или external effect.

## 2. Итерация 1 — Canonicality: register не должен стать вторым source of truth

**Критика:** единый Company register полезен ровно до момента, когда он начинает хранить договорную, банковскую, customer или product truth параллельно с первичным source. Тогда удобная управленческая таблица становится источником drift и ложной authority.

**Проверка и reconciliation:** proposal вводит двухслойную canonicality:

- register canonical только для Company control metadata — inclusion, `WORK-*`/`OBL-*` identity, accountable Position, priority context, control/attention state, control point и refs;
- underlying legal/accounting/customer/product/OS facts остаются authoritative в собственных contours;
- конфликт решается в пользу authoritative source в его scope с явным reconciliation register summary.

Это сохраняет Company-level control без дублирования первичной истины.

**Результат:** PASS.

## 3. Итерация 2 — Qualification gate: модель легко превратить в универсальный task tracker

**Критика:** если `WORK-*` создаётся на любую полезную работу, Owner получит ещё один backlog, а все product issues/commits начнут реплицироваться в Company repository.

**Проверка и reconciliation:** proposal задаёт material Company-level qualification gate и explicit exclusion list:

- routine coding/test/PR/task work остаётся в product repositories;
- Company entry создаётся только при obligation/risk/cash/customer/continuity/Owner-attention/cross-repository management need;
- один management concern имеет одну Company entry, lower-level execution только referenced;
- `next_control_point` — management checkpoint, а не следующий micro-task.

Это делает register контрольным слоем, а не заменой GitHub/roadmap/product tracker.

**Результат:** PASS.

## 4. Итерация 3 — Obligation record не должен сам создавать obligation

**Критика:** термин `OBL-*` может создать опасную инверсию: внутренняя запись будет восприниматься как доказательство юридического/договорного обязательства или его исполнения.

**Проверка и reconciliation:** proposal прямо фиксирует:

- `OBL-*` создаётся только как control representation уже существующего obligation;
- обязательство должно иметь `authoritative_obligation_ref`;
- six obligation classes наследуются из AC-102 без изобретения нового legal taxonomy;
- satisfaction требует `satisfaction_evidence_ref` из authoritative source;
- `closed` в register не заменяет legal/accounting/customer fact;
- register entry не создаёт customer/vendor/legal commitment.

**Результат:** PASS.

## 5. Итерация 4 — Accountability не должна снова концентрировать всё на Owner

**Критика:** Owner-facing register может незаметно сделать Owner owner-of-everything: каждый material item будет требовать личного назначения/проверки и воспроизведёт bottleneck, который M2 должен снижать.

**Проверка и reconciliation:** proposal требует одну `accountable_position` и использует Approved `POS-001…POS-006` mapping.

Ключевые ограничения:

- Position — долговременная accountability unit;
- current Principal/runtime не подменяет Position;
- одна primary Position сохраняется даже при cross-functional support;
- Owner view выводит только material attention/control state;
- normal bounded low-risk work не попадает автоматически в register;
- `waiting` не порождает бессмысленные retry/attention loops.

Owner остаётся decision authority там, где это действительно требуется, но не ручным scheduler.

**Результат:** PASS.

## 6. Итерация 5 — Priority: `P0` может превратиться в универсальный override

**Критика:** поскольку roadmap говорит, что obligations/risk/cash имеют приоритет, любое customer сообщение, invoice, renewal или product request можно ошибочно пометить `P0`, и strategic sequencing исчезнет.

**Проверка и reconciliation:** proposal сохраняет exact AC-106 semantics:

- `P0` применяется к **real time-sensitive material** obligation/cash/risk issue;
- сам факт категории `obligation` не делает item `P0`;
- `P1/P2/P3` остаются sequencing semantics AC-106;
- portfolio bands `A1/A2/B...` не заменяют `P0…P3`;
- изменение priority не меняет product disposition или underlying obligation truth.

Таким образом `P0` остаётся exception-driven, а не универсальной кнопкой срочности.

**Результат:** PASS.

## 7. Итерация 6 — Status/freshness: нельзя превращать stale summary в operational truth

**Критика:** work/obligation register особенно опасен тем, что human-readable статус выглядит авторитетно даже через неделю после изменения source. Для due/trigger это может создать прямой downside.

**Проверка и reconciliation:** proposal разделяет:

- `control_state` — только handling state (`open/waiting/blocked/closed`);
- `attention_state` — `normal/needs_attention/escalated`;
- `evidence_as_of` — freshness динамического evidence;
- `due_or_trigger` — exact date/window/condition/unknown/none без fabricated precision;
- source conflict/staleness → `needs_attention`/`escalated` при material effect;
- `unknown ≠ zero/false/complete`;
- closed obligation требует authoritative satisfaction/termination evidence.

Это существенно снижает риск ложной certainty.

**Результат:** PASS.

## 8. Итерация 7 — Waiting/blocked должны снижать noise, а не создавать его

**Критика:** M4 нужен для уменьшения reconstruction burden, но плохо спроектированный `needs attention` queue может каждое утро показывать known unavailable external/physical/access gates и заставлять Owner снова проверять то, что не изменилось.

**Проверка и reconciliation:** proposal:

- различает `waiting` и `blocked`;
- требует trigger/next legitimate control point;
- explicitly запрещает blind retry;
- Owner projection показывает waiting/blocked item только когда наступил legitimate review trigger либо существует material consequence;
- unknown/stale не маскируется, но и не превращается в бесконечный manual poll.

Это согласуется с AC-306 Owner-attention discipline и текущей practical work model.

**Результат:** PASS.

## 9. Итерация 8 — Attention/escalation не должны становиться скрытой authority model

**Критика:** `escalated`, `Owner action`, `next control point` могут быть прочитаны как workflow approval state и фактически обойти AC-202/203 и будущий AC-402.

**Проверка и reconciliation:** proposal содержит explicit separation:

- register показывает escalation need, но не выдаёт approval;
- `escalated` означает выход за текущую Position/Assignment/workflow boundary;
- `ROD-01…ROD-09` сохраняются;
- `AM-0…AM-4` не активируются записью;
- recommendation/status/silence/AI summary не являются approval;
- exact decision/approval record отложен в AC-402;
- legal/corporate authority остаётся отдельным gate.

**Результат:** PASS.

## 10. Итерация 9 — Security/minimization: единый control layer может стать концентратором чувствительных данных

**Критика:** owner dashboard удобно соблазняет копировать contracts, банковские payload, customer docs, credentials и внутренние details в одну поверхность. Это ухудшает security, privacy, portability и replacement path.

**Проверка и reconciliation:** proposal требует reference-over-copy и explicitly запрещает без необходимости:

- secrets/tokens/private keys/recovery codes;
- full banking/accounting payload;
- лишние персональные данные;
- full customer contracts/docs;
- raw model prompts/chain-of-thought;
- confidential source payload ради convenience.

Future software representation обязана наследовать least privilege, scope, classification и audit rules. Видимость item не даёт underlying-source permission.

**Результат:** PASS.

## 11. Итерация 10 — Company↔Arvectum OS boundary и downstream handoff

**Критика:** current Arvectum OS уже имеет P9.04 `My Work / Needs Attention`. Возникают два противоположных риска:

1. перенести Company semantics в OS ради готового UI;
2. построить Company dashboard отдельно и затем получить две несовместимые очереди.

Дополнительный риск — попытаться решить AC-402…AC-406 прямо внутри AC-401.

**Проверка current OS:** `arvectum/arvectum-os` `main` проверен на commit `8d35eb3867c4aed60f7aaa201c0c03a9aa3b1353`.

P9.04 является derived/non-authoritative owner-facing projection и intentionally не выводит произвольный business state из opaque payload. Он не создаёт Stable Product Contract/Active capability/Company-specific semantics.

**Проверка и reconciliation proposal:** AC-401:

- оставляет `WORK-*`/`OBL-*` semantics в Company scope;
- допускает P9.04-like projection только как future presentation mechanism через explicit governed boundary;
- запрещает hidden Company→OS coupling;
- не меняет OS lifecycle/Product Contracts;
- передаёт в AC-402 только escalation/decision relationship points;
- в AC-403 — risk references, не taxonomy;
- в AC-404 — obligation/cash control identities, не transaction ledger;
- в AC-405 — inputs, не cadence;
- в AC-406 — owner-facing semantics, не dashboard implementation.

**Результат:** PASS.

## 12. Acceptance matrix

| Проверка | Результат |
|---|---|
| Company control layer defined | PASS |
| `WORK-*` / `OBL-*` separation | PASS |
| underlying obligation not created by register | PASS |
| underlying fact authority preserved | PASS |
| statutory/accounting truth not duplicated | PASS |
| product implementation/status truth remains product-owned | PASS |
| stable ID namespaces defined | PASS |
| deduplication rule defined | PASS |
| material qualification gate defined | PASS |
| routine product tasks excluded | PASS |
| primary accountable Position required | PASS |
| Principal/runtime not substituted for Position | PASS |
| AC-106 P0…P3 preserved | PASS |
| P0 remains exception-driven | PASS |
| portfolio bands do not replace Company priority | PASS |
| control state separated from substantive truth | PASS |
| attention state separated from approval | PASS |
| due/trigger uncertainty supported | PASS |
| freshness discipline defined | PASS |
| unknown not treated as zero/complete | PASS |
| waiting/blocked no-blind-retry semantics defined | PASS |
| ROD boundary preserved | PASS |
| AM authority boundary preserved | PASS |
| legal/corporate authority remains separate | PASS |
| secret/data minimization defined | PASS |
| future software visibility does not imply permission | PASS |
| P9.04 derived/non-authoritative boundary preserved | PASS |
| no Stable Product Contract/Active capability implied | PASS |
| AC-402…AC-406 clean handoff | PASS |
| no dashboard/runtime/automation created | PASS |
| no spend/customer/vendor external effect created | PASS |

## 13. Residual limitations / carry-forward

Cross-review intentionally does **not** claim:

- completeness of the actual current obligation inventory;
- legal/accounting audit of Company obligations;
- existence of a populated live register;
- validated cadence/aging thresholds;
- exact Owner Mission Control UI;
- automated source ingestion;
- availability of a Company Product Contract with Arvectum OS;
- end-to-end P9.04 integration;
- operational proof that the register reduces Owner reconstruction time.

These are downstream evidence/implementation questions. AC-401 is a semantic/model gate.

## 14. Review conclusion

Material objections remaining after iteration 10: `0`.

Результат:

`Complete / PASS for Owner approval`.

Exact proposal recommended for approval:

- `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL.md`;
- `Proposed 0.9.0`;
- blob `0f4444fbd968e176a0a158771a7d0abe93549ecd`.

Cross-review не является Owner approval. До явного действия Owner proposal не становится Approved Company operating-model state и roadmap не должен автоматически переходить к AC-402.
