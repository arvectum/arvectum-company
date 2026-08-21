# Решение собственника — утверждение AC-403

Статус: `Approved`
Дата: `2026-08-21`
Владелец решения: собственник ООО «Арвектум»
Репозиторий: `arvectum/arvectum-company`
Решение: `AC-403 — Risk, exception and incident register model`

## 1. Явное решение

Собственник явно утвердил AC-403 формулировкой:

> `AC-403 утверждаю`

Утверждение относится к точной проверенной редакции:

- proposal: `docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL.md`;
- proposal status: `Proposed 0.9.0`;
- immutable proposal blob SHA: `857b601423f78fc3d4636dbf9754d5410d8a1c55`;
- cross-review: `docs/reviews/AC-403-COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-CROSS-REVIEW.md`;
- cross-review result: `10 of maximum 10`, `Complete / PASS for Owner approval`;
- immutable cross-review blob SHA: `37241051876a94f71035e532e19ed9cf69b4c785`.

Эти blob SHA фиксируют именно те редакции, которые были представлены собственнику перед утверждением.

## 2. Утверждённый результат AC-403

Собственник утверждает Company-level модель контроля material risks, control exceptions и incidents поверх Approved AC-401/AC-402.

Утверждается, в частности, что:

- существуют три независимых control namespace: `RSK-*`, `EXC-*`, `INC-*`;
- risk evidence/assessment не являются accepted risk;
- exception request не является approved exception;
- incident detection не создаёт authority to act;
- bounded containment не является risk acceptance;
- recovery/technical workaround не являются waiver и не закрывают автоматически связанные obligations/residual risks;
- исторические AC-105 `R-01…R-20` остаются baseline identifiers, а live Company control identities используют `RSK-*`;
- Company register не создаёт универсальный `ISS-*` tracker: product bugs/tasks остаются product-owned, Company blockers — в `WORK-*`/`OBL-*`, material events — в `INC-*`;
- consequence-based materiality сохраняется без fabricated probability, MTTR/RTO, expected-loss или arbitrary red/amber/green scoring;
- `ROD-06` и другие применимые `ROD-*`, `AM-0…AM-4`, Position/Assignment/access boundaries остаются controlling authority;
- accepted material risk требует exact attributable `DEC-*`/`APR-*` act компетентной authority, когда такой gate применим;
- approved exception допустим только если higher-authority source позволяет отклонение; Owner approval не легализует unlawful act и не отменяет binding contract/customer rights/OS invariant;
- exception имеет exact scope, conditions, compensating controls, expiry/review и reversion/exit path;
- incident lifecycle различает detection, assessment, containment, recovery, reconciliation/closure и residual exposure;
- emergency containment может выполняться только внутри уже действующей authority/workflow boundary; оно не передаёт material risk acceptance;
- `P0`/Owner attention применяются только при реальном material consequence, а не к каждому alert/defect;
- source freshness, uncertainty, minimization, confidentiality и reference-over-copy обязательны пропорционально consequence;
- Product, Arvectum OS, legal/corporate, customer, security tooling и external systems остаются authoritative в своих scopes;
- current Arvectum OS `DECISION-AUTHORITY-POLICY.md` `Proposed 0.2.1` не принимается этим решением как Company governance;
- AC-403 не создаёт budget, spend, customer commitment, exception authority, incident-response authority, dashboard/runtime/automation, Product Contract или OS lifecycle transition.

## 3. Результат AC-403

`AC-403 — Risk, exception and incident register model` закрывается со статусом:

`Complete / PASS`.

Русская смысловая формулировка результата:

**ООО «Арвектум» имеет утверждённую Company-level семантику существенных рисков, исключений и инцидентов, которая делает exposure и response state видимыми, не превращая наблюдение риска в его принятие, технический обход — в waiver, а инцидентный tracker — в новый источник Organizational Authority.**

## 4. Что утверждение AC-403 не означает

AC-403 само по себе не:

- принимает какой-либо конкретный риск;
- разрешает конкретное control exception;
- подтверждает закрытие или отсутствие реального инцидента;
- создаёт incident-response полномочия, бюджет, расход, договор или customer commitment;
- делегирует или расширяет `ROD-*`/`AM-*`;
- делает Company repository authoritative для product/security/OS/legal/customer facts вне Company scope;
- утверждает numeric risk appetite/thresholds, SLA, RTO/RPO или production-readiness claim;
- создаёт dashboard, runtime, SIEM, workflow engine или automation;
- принимает Arvectum OS Decision Authority Policy;
- создаёт Product Contract или меняет Platform Capability lifecycle;
- закрывает AC-404…AC-407.

## 5. Следующее действие

Следующее каноническое действие M4:

`AC-404 — Cash, commitment and management reporting baseline`.

AC-404 должен добавить минимальную Company-level семантику cash/commitment visibility и management reporting поверх AC-401…AC-403, не создавая параллельную бухгалтерию, bank ledger, tax system или spending authority.

Это решение разрешает каноническую публикацию AC-403 `1.0.0`, синхронизацию roadmap/source register/README и перевод current action на AC-404.

## 6. Границы решения

Решение не создаёт новых юридических полномочий, не утверждает конкретный риск/exception/расход/договор/customer commitment, Product Contract Arvectum OS, production deployment или product implementation change.