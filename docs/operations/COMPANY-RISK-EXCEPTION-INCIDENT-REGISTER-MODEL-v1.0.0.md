# AC-403 — Risk, Exception and Incident Register Model

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-403 — Risk, exception and incident register model`
Решение: `docs/governance/decisions/DECISION-2026-08-21-AC-403-APPROVAL.md`
Cross-review: `docs/reviews/AC-403-COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `857b601423f78fc3d4636dbf9754d5410d8a1c55`

## 1. Approval publication

Этот документ является канонической Approved publication AC-403 `1.0.0`.

Утверждённое собственником нормативное содержание — полная проверенная редакция:

`docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL.md`

с immutable git blob SHA:

`857b601423f78fc3d4636dbf9754d5410d8a1c55`.

Proposal включён в эту публикацию **целиком по immutable content reference**. Настоящая publication не меняет нормативное содержание проверенной редакции.

Явное решение собственника зафиксировано в:

`docs/governance/decisions/DECISION-2026-08-21-AC-403-APPROVAL.md`.

## 2. Approved model

AC-403 `1.0.0` устанавливает binding Company-level risk/exception/incident control model, определённую в incorporated proposal, включая:

1. три независимых namespace: `RSK-*`, `EXC-*`, `INC-*`;
2. material qualification gate вместо универсального security/bug/issue tracker;
3. distinction `risk evidence ≠ accepted risk`;
4. distinction `exception request ≠ approved exception`;
5. distinction `incident detection ≠ authority to act`;
6. distinction `containment ≠ risk acceptance`;
7. distinction `recovery ≠ automatic obligation/risk closure`;
8. сохранение AC-105 historical `R-01…R-20` как baseline references без переименования в live control IDs;
9. отсутствие отдельного универсального `ISS-*` namespace;
10. consequence-based materiality без fabricated numeric probability/impact scoring;
11. explicit `RSK-*` fields для exposure, consequence, controls/evidence, uncertainty, treatment intent, residual risk и acceptance reference;
12. explicit `EXC-*` fields для exact rule, requested deviation, authority basis, conditions, compensating controls, expiry/reversion и residual risk;
13. explicit `INC-*` fields для detection/source, impact, containment, current state, recovery/reconciliation, linked obligations/work/decisions и residual exposure;
14. `ROD-06` и иные applicable `ROD-*` как hard risk/exception authority boundaries;
15. сохранение `AM-0…AM-4`, Position/Assignment/access semantics;
16. accepted risk только через attributable competent decision/approval act, когда approval требуется;
17. exception только при наличии права higher-authority source допустить deviation;
18. incident containment без автоматической передачи risk-acceptance authority;
19. `P0` и Owner attention только для real material consequence/authority need;
20. stale/missing/uncertain evidence как явный control state, а не silent current truth;
21. source-of-truth separation между Company, Product, Arvectum OS, legal/customer/accounting/security/external contours;
22. minimization, confidentiality и reference-over-copy, включая отсутствие privileged incident/security payload и chain-of-thought в public repository;
23. отсутствие budget/spend/customer commitment/dashboard/runtime/SIEM/automation/Product Contract по импликации;
24. current Arvectum OS `DECISION-AUTHORITY-POLICY.md` `Proposed 0.2.1` не принимается как Company authority source;
25. bounded handoff в AC-404…AC-407.

## 3. Authority boundary

AC-403 не создаёт risk appetite, Organizational Authority, exception approval authority или incident-response authority.

`RSK-*`, `EXC-*`, `INC-*` представляют Company control state и references. Risk acceptance, exception approval, consequential external action и legal/customer/Product/OS acts требуют собственных applicable authority sources и gates.

Owner approval не может легализовать unlawful act, отменить customer rights, binding contract, mandatory legal control или Arvectum OS constitutional invariant.

## 4. Source-of-truth boundary

Company repository может быть canonical только для Company-level risk/exception/incident control representation в declared scope.

Он не заменяет:

- product bug/security/incident implementation truth;
- security tooling/SIEM/log telemetry;
- legal/corporate facts and acts;
- customer/counterparty facts and approvals;
- bank/accounting/statutory truth;
- Arvectum OS RFC/ADR/Product Contract/platform incident truth;
- external provider/source facts.

Для этих contours используются минимальные references и Company management interpretation, а не competing authority.

## 5. Cross-review and approval evidence

Cross-review:

- `docs/reviews/AC-403-COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-CROSS-REVIEW.md`;
- iterations: `10 of maximum 10`;
- result: `Complete / PASS for Owner approval`;
- immutable blob SHA: `37241051876a94f71035e532e19ed9cf69b4c785`.

Approved proposal:

- `docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `857b601423f78fc3d4636dbf9754d5410d8a1c55`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-21-AC-403-APPROVAL.md` — `Approved`;
- explicit wording: `AC-403 утверждаю`.

## 6. Approval result

`AC-403 — Risk, exception and incident register model` имеет статус `Complete / PASS` и является binding Company risk-control model в пределах заявленного scope.

Следующее каноническое действие:

`AC-404 — Cash, commitment and management reporting baseline`.

AC-404 должен использовать AC-401…AC-403 как утверждённые control substrates и отдельно определить management cash/commitment visibility без построения параллельной бухгалтерии или spending authority.