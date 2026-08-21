# AC-402 — Decision, Approval and Escalation Register Model

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-402 — Decision, approval and escalation register model`
Решение: `docs/governance/decisions/DECISION-2026-08-21-AC-402-APPROVAL.md`
Cross-review: `docs/reviews/AC-402-COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `a48081ba3599e6f3c91b8a6562435ad1f0c152f4`

## 1. Approval publication

Этот документ является канонической Approved publication AC-402 `1.0.0`.

Утверждённое собственником нормативное содержание — полная проверенная редакция:

`docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL.md`

с immutable git blob SHA:

`a48081ba3599e6f3c91b8a6562435ad1f0c152f4`.

Proposal включён в эту публикацию **целиком по immutable content reference**. Настоящая publication не меняет нормативное содержание проверенной редакции.

Явное решение собственника зафиксировано в:

`docs/governance/decisions/DECISION-2026-08-21-AC-402-APPROVAL.md`.

## 2. Approved model

AC-402 `1.0.0` устанавливает binding Company-level decision/approval/escalation control model, определённую в incorporated proposal, включая:

1. три независимых namespace: `DEC-*`, `APR-*`, `ESC-*`;
2. material qualification gate вместо регистрации каждого routine choice;
3. фундаментальное разделение `recommendation ≠ decision ≠ approval ≠ legal/corporate act ≠ technical authorization ≠ execution`;
4. stable identities и запрет переписывать исторический decision instance под новый смысл;
5. `DEC-*` с exact question/scope, authority basis, decision authority, state, outcome, evidence, rationale summary, constraints, approvals, effect readiness и execution handoff;
6. `APR-*` с отдельным approval domain/capacity, attributable act, scope, effective period, conditions и authoritative source reference;
7. `ESC-*` с explicit origin boundary, target authority, bounded evidence packet и Owner-attention semantics;
8. сохранение `ROD-01…ROD-09` и `AM-0…AM-4` без расширения authority;
9. explicit attributable act для Owner `ROD-*` и delegated `AM-3` approvals;
10. различение `approve`, `reject`, `defer`, `approve_with_conditions`; silence не является approval/defer;
11. separation internal decision outcome от external-effect readiness;
12. сохранение отдельных corporate/legal/customer/Product/Arvectum OS gates даже если physical Principal совпадает;
13. отсутствие вывода authority из IAM/admin/credential/technical capability;
14. stale/missing evidence, changed facts, expiry/revocation/supersession как stop/review conditions;
15. escalation к реальной target authority, а не автоматическое превращение любой uncertainty в Owner queue;
16. source-of-truth separation между Company, Product, Arvectum OS и external/legal/customer contours;
17. data minimization, reference-over-copy и отсутствие требования сохранять chain-of-thought;
18. отсутствие dashboard/runtime/automation/budget/spend/external commitment/Product Contract по импликации;
19. current Arvectum OS `DECISION-AUTHORITY-POLICY.md` `Proposed 0.2.1` не принимается как Company authority source;
20. bounded handoff в AC-403…AC-407 без преждевременного проектирования их полной семантики.

## 3. Authority boundary

AC-402 не создаёт Organizational Authority.

`DEC-*`, `APR-*` и `ESC-*` только представляют/контролируют уже существующие authority semantics и attributable acts. Действующие AC-202/AC-203, Position/Assignment/access rules и legal/corporate/customer/Product/OS governance продолжают применяться независимо от состояния записи.

Наличие `decision_outcome=approve` не является универсальным permission token. Consequential effect разрешён только при прохождении всех применимых internal, legal/corporate/customer, technical/data/security и иных gates.

## 4. Source-of-truth boundary

Company repository может быть canonical для внутреннего Company decision/approval act только в своём declared Organizational Authority scope.

Он не заменяет:

- participant/general-meeting/General Director legal acts и иные corporate sources;
- customer/counterparty consent/acceptance;
- Product governance/implementation truth;
- Arvectum OS RFC/ADR/Product Contract/lifecycle truth;
- bank/accounting/statutory truth;
- external system facts.

Для таких gates используются references и Company control interpretation, а не competing authority.

## 5. Cross-review and approval evidence

Cross-review:

- `docs/reviews/AC-402-COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-CROSS-REVIEW.md`;
- iterations: `10 of maximum 10`;
- result: `Complete / PASS for Owner approval`;
- immutable blob SHA: `82cf1046178cde22387a04037e86cf7e1b224f9a`.

Approved proposal:

- `docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `a48081ba3599e6f3c91b8a6562435ad1f0c152f4`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-21-AC-402-APPROVAL.md` — `Approved`;
- explicit wording: `AC-402 утверждаю`.

## 6. Approval result

`AC-402 — Decision, approval and escalation register model` имеет статус `Complete / PASS` и является binding Company decision-control model в пределах заявленного scope.

Следующее каноническое действие:

`AC-403 — Risk, exception and incident register model`.

AC-403 должен использовать AC-401/AC-402 как утверждённые control substrates и отдельно различать risk evidence, exception acceptance, incident handling, decision/approval и execution.