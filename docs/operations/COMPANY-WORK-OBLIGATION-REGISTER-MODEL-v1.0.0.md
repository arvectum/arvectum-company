# AC-401 — Company Work / Obligation Register Model

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-401 — Company work/obligation register model`
Решение: `docs/governance/decisions/DECISION-2026-08-21-AC-401-APPROVAL.md`
Cross-review: `docs/reviews/AC-401-COMPANY-WORK-OBLIGATION-REGISTER-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `0f4444fbd968e176a0a158771a7d0abe93549ecd`

## 1. Approval publication

Этот документ является канонической Approved publication AC-401 `1.0.0`.

Утверждённое собственником нормативное содержание — полная проверенная редакция:

`docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL.md`

с immutable git blob SHA:

`0f4444fbd968e176a0a158771a7d0abe93549ecd`.

Proposal включён в эту публикацию **целиком по immutable content reference**. Настоящая publication не меняет нормативное содержание проверенной редакции.

Явное решение собственника зафиксировано в:

`docs/governance/decisions/DECISION-2026-08-21-AC-401-APPROVAL.md`.

## 2. Approved model

AC-401 `1.0.0` устанавливает обязательную в пределах Company governance модель Company Work / Obligation Register, определённую в incorporated proposal, включая:

1. два класса Company control entries: `WORK-*` и `OBL-*`;
2. qualification gate по material Company-level control need вместо автоматического копирования lower-level tasks/facts;
3. stable identity и запрет повторного использования закрытых `WORK-*`/`OBL-*` IDs;
4. separation Company control canonicality от underlying legal/accounting/customer/product/OS/source truth;
5. common control envelope с accountable Position, `P0…P3` context, control/attention state, due-or-trigger, next control point, source/evidence references, freshness/review/escalation/closure metadata;
6. специализированные поля для work и obligations без превращения реестра в project tracker или бухгалтерскую систему;
7. один primary accountable `POS-*` на active entry при сохранении функциональной координации и authority boundaries;
8. relationship semantics между obligations и fulfillment work без автоматического вывода satisfaction из task closure;
9. explicit freshness/unknown/stale behavior и запрет фабрикации сроков, фактов и статуса источника;
10. `P0` obligation/cash/material-risk preemption в соответствии с AC-106;
11. Owner-attention discipline: реестр поднимает material exceptions/control points, а не делает Owner диспетчером routine work;
12. minimization/public-repository boundary для confidential, banking, credential, personal и customer payload;
13. separation от AC-402 decisions/approvals/escalations, AC-403 risks/incidents и AC-404 cash/reporting semantics;
14. отсутствие dashboard/runtime/automation/spending/external-effect authority по импликации;
15. Arvectum OS P9.04 как возможный будущий derived presentation mechanism, но не источник Company business semantics или authority.

## 3. Authority boundary

AC-401 не создаёт Organizational Authority.

Действующие `AC-202 ROD-01…ROD-09`, `AC-203 AM-0…AM-4`, Position/Assignment/access boundaries продолжают применяться независимо от того, что item видим или помечен как `needs_attention`/`escalated`.

Запись в Company register не создаёт legal/corporate power, customer approval, spending right, Product Contract, technical credential или Arvectum OS authority.

## 4. Source-of-truth boundary

Company register является authoritative только для утверждённого Company-level control representation в своём declared scope.

Он не заменяет:

- договоры, корпоративные решения и иные legal/corporate authoritative sources;
- bank/accounting/statutory transaction truth;
- product repositories для implementation/status/domain semantics;
- `arvectum/arvectum-os` для OS Product Contracts/platform state;
- customer/vendor/external source systems для их собственных фактов.

Underlying fact должен указываться через source/evidence reference и не должен копироваться без необходимости.

## 5. Cross-review and approval evidence

Cross-review:

- `docs/reviews/AC-401-COMPANY-WORK-OBLIGATION-REGISTER-CROSS-REVIEW.md`;
- iterations: `10 of maximum 10`;
- result: `Complete / PASS for Owner approval`;
- immutable blob SHA: `7c0cbc178bf50a7babbd0403798091c4ddef996f`.

Approved proposal:

- `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `0f4444fbd968e176a0a158771a7d0abe93549ecd`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-21-AC-401-APPROVAL.md` — `Approved`;
- explicit wording: `AC-401 утверждаю`.

## 6. Approval result

`AC-401 — Company work/obligation register model` имеет статус `Complete / PASS` и является binding Company control model в пределах заявленного scope.

Следующее каноническое действие:

`AC-402 — Decision, approval and escalation register model`.

AC-402 должен использовать AC-401 как уже утверждённый work/obligation control substrate, сохраняя separation recommendation / approval / authority / execution.