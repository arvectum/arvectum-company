# Решение собственника — утверждение AC-401

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`
Решение: `AC-401 — Company work/obligation register model`

## 1. Явное решение

Собственник явно утвердил AC-401 формулировкой:

> `AC-401 утверждаю`

Утверждение относится к точной проверенной редакции:

- proposal: `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL.md`;
- proposal status: `Proposed 0.9.0`;
- immutable proposal blob SHA: `0f4444fbd968e176a0a158771a7d0abe93549ecd`;
- cross-review: `docs/reviews/AC-401-COMPANY-WORK-OBLIGATION-REGISTER-CROSS-REVIEW.md`;
- cross-review result: `10 of maximum 10`, `Complete / PASS for Owner approval`;
- immutable cross-review blob SHA: `7c0cbc178bf50a7babbd0403798091c4ddef996f`.

Эти blob SHA фиксируют именно те редакции, которые были представлены собственнику перед утверждением.

## 2. Утверждённый результат AC-401

Собственник утверждает Company-level модель реестра существенных работ и обязательств как минимальный control layer M4.

Утверждается, в частности, что:

- реестр имеет два независимых класса записей: `WORK-*` для material Company-level work и `OBL-*` для material obligation control;
- создание записи `OBL-*` не создаёт само обязательство: underlying legal/contractual/accounting/customer/source-system fact остаётся в соответствующем authoritative source;
- Company register может быть canonical только для Company control metadata в своём declared scope: stable identity, operating meaning, accountable Position, priority/control/attention state, next control point, source references, review/closure history;
- product implementation/status остаётся в product repositories, Arvectum OS state — в `arvectum/arvectum-os`, accounting/banking/legal/customer truth — в соответствующих компетентных контурах;
- entry создаётся только при реальном Company-level control need; обычные product backlog tasks, commits, routine coding, проводки, receipts, emails и low-risk bounded work по умолчанию не дублируются;
- каждая active запись имеет одну primary accountable `POS-*` Position, но это не создаёт новую authority и не делает текущего исполнителя владельцем организационного смысла записи;
- общая Company priority hierarchy `P0/P1/P2/P3` сохраняется, причём `P0` real obligations/cash/material risk может преempt internal roadmap convenience;
- `control_state` отделён от `attention_state`; `waiting`/`blocked` не равны failure, а `needs_attention`/`escalated` не являются approval;
- due/trigger и dynamic evidence нельзя выдумывать; stale/unknown source state должен быть явно видим либо вести к fail-closed/escalation behavior пропорционально consequence;
- work и obligation могут ссылаться друг на друга, но закрытие `WORK-*` не доказывает удовлетворение `OBL-*` без собственного satisfaction evidence;
- register не является project tracker, бухгалтерией, CRM, договорным реестром, workflow runtime, dashboard, spending authority или external commitment mechanism;
- Arvectum OS P9.04 `My Work / Needs Attention` может позднее выступать только как совместимый derived presentation mechanism через надлежащий contract/governed path и не является источником Company business state.

## 3. Результат AC-401

`AC-401 — Company work/obligation register model` закрывается со статусом:

`Complete / PASS`.

Русская смысловая формулировка результата:

**ООО «Арвектум» имеет утверждённую минимальную Company-level семантику контроля существенных работ и обязательств, которая уменьшает необходимость восстанавливать управленческий контекст из чатов, продуктовых репозиториев и внешних систем, не создавая параллельных источников первичной истины и не превращая собственника в ручного диспетчера low-risk работы.**

## 4. Что утверждение AC-401 не означает

AC-401 само по себе не:

- создаёт реальное юридическое, договорное, финансовое или customer obligation;
- подтверждает исполнение обязательства только фактом закрытия связанной работы;
- создаёт бюджет, расход, цену, SLA, customer/vendor commitment или право подписи;
- меняет `ROD-*`, `AM-*`, Position authority, Assignment или technical access;
- создаёт dashboard, runtime, automation или Product Contract Arvectum OS;
- переносит product implementation truth в Company repository;
- переносит Company-specific semantics в domain-neutral Kernel/Arvectum OS;
- отменяет требования минимизации данных, source freshness, authority и evidence.

## 5. Следующее действие

Следующее каноническое действие M4:

`AC-402 — Decision, approval and escalation register model`.

AC-402 должен добавить к уже утверждённому work/obligation control layer отдельную Company-level семантику решений, approvals и escalations, не смешивая recommendation, Organizational Authority, legal/corporate act и technical execution.

Это решение разрешает каноническую публикацию AC-401 `1.0.0`, синхронизацию roadmap/source register/README и перевод current action на AC-402.

## 6. Границы решения

Решение не создаёт новых юридических полномочий, не утверждает конкретный расход, договор, клиентское обязательство, риск-исключение, Product Contract Arvectum OS, production deployment или product implementation change.