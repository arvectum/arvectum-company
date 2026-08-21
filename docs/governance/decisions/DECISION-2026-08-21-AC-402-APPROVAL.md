# Решение собственника — утверждение AC-402

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`
Решение: `AC-402 — Decision, approval and escalation register model`

## 1. Явное решение

Собственник явно утвердил AC-402 формулировкой:

> `AC-402 утверждаю`

Утверждение относится к точной проверенной редакции:

- proposal: `docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL.md`;
- proposal status: `Proposed 0.9.0`;
- immutable proposal blob SHA: `a48081ba3599e6f3c91b8a6562435ad1f0c152f4`;
- cross-review: `docs/reviews/AC-402-COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-CROSS-REVIEW.md`;
- cross-review result: `10 of maximum 10`, `Complete / PASS for Owner approval`;
- immutable cross-review blob SHA: `82cf1046178cde22387a04037e86cf7e1b224f9a`.

Эти blob SHA фиксируют именно те редакции, которые были представлены собственнику перед утверждением.

## 2. Утверждённый результат AC-402

Собственник утверждает Company-level модель реестра material decisions, approval gates/acts и escalations поверх Approved AC-401.

Утверждается, в частности, что:

- существуют три независимых control namespace: `DEC-*`, `APR-*`, `ESC-*`;
- recommendation/proposal/draft не являются decision;
- decision не равен approval gate/act;
- internal Company approval не заменяет отдельно требуемый legal/corporate/customer/Product/Arvectum OS act;
- technical authorization, IAM permission, credential possession, workflow completion и technical success не создают Organizational Authority и не считаются approval;
- `ROD-01…ROD-09` и `AM-0…AM-4` остаются действующими authority boundaries и не расширяются AC-402;
- для `ROD-*` требуется explicit attributable Owner act, для `AM-3` — valid attributable act eligible Principal внутри active delegation envelope;
- `approve`, `reject`, `defer`, `approve_with_conditions` различаются; silence не создаёт approval или defer;
- `decision_outcome` отделён от `effect_readiness`: внутреннее approve само по себе не разрешает внешний consequential effect, пока не пройдены другие required gates;
- один physical Principal не сливает capacities Owner, участника, генерального директора, customer approver и technical executor;
- escalation имеет explicit target authority и не становится Owner queue автоматически;
- stale/missing evidence, changed facts, expiry/revocation/supersession блокируют небезопасное повторное использование прежнего decision/approval;
- Company register не становится competing source of truth для product, OS, legal/corporate, customer или external facts;
- current Arvectum OS `DECISION-AUTHORITY-POLICY.md` `Proposed 0.2.1` не принимается этим решением как Company governance;
- public-repository minimization, reference-over-copy и запрет хранения chain-of-thought/sensitive payloads сохраняются;
- AC-402 не создаёт budget, spend, external commitment, dashboard/runtime/automation, Product Contract или OS lifecycle transition.

## 3. Результат AC-402

`AC-402 — Decision, approval and escalation register model` закрывается со статусом:

`Complete / PASS`.

Русская смысловая формулировка результата:

**ООО «Арвектум» имеет утверждённую Company-level семантику material decisions, approvals и escalations, позволяющую видеть реальные authority gates и attributable acts без смешения recommendation, решения, юридически значимого действия, технического доступа и исполнения.**

## 4. Что утверждение AC-402 не означает

AC-402 само по себе не:

- создаёт новую Organizational Authority или legal/corporate power;
- делегирует или расширяет `ROD-*`/`AM-*`;
- создаёт реальный customer/vendor/legal obligation;
- делает Company repository authoritative для Product/Arvectum OS/customer/legal facts вне Company scope;
- утверждает конкретный бюджет, расход, контракт, цену, SLA, pilot или production deployment;
- создаёт technical credential/access;
- создаёт dashboard, runtime, automation или workflow engine;
- принимает Arvectum OS Decision Authority Policy;
- создаёт Product Contract или меняет Platform Capability lifecycle;
- закрывает AC-403…AC-407.

## 5. Следующее действие

Следующее каноническое действие M4:

`AC-403 — Risk, exception and incident register model`.

AC-403 должен добавить отдельную Company-level семантику material risks, exceptions и incidents поверх AC-401/AC-402, сохраняя distinction между risk evidence, exception acceptance, incident handling и authority/approval.

Это решение разрешает каноническую публикацию AC-402 `1.0.0`, синхронизацию roadmap/source register/README и перевод current action на AC-403.

## 6. Границы решения

Решение не создаёт новых юридических полномочий, не утверждает конкретный расход, договор, customer commitment, risk exception, Product Contract Arvectum OS, production deployment или product implementation change.