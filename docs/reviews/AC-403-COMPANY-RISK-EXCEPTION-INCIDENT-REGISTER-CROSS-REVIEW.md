# AC-403 — Cross-review: Risk, Exception and Incident Register Model

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `10 of maximum 10`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-403 — Risk, exception and incident register model`

Проверенный exact proposal:

- `docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `857b601423f78fc3d4636dbf9754d5410d8a1c55`.

Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`.

## 1. Review gate

AC-403 должен быть отклонён, если модель:

- смешивает risk evidence и accepted risk;
- выводит exception approval из request, silence, technical bypass, admin access или continued operation;
- создаёт exception для non-waivable law/contract/customer/constitutional/OS boundary;
- считает incident detection/containment источником incident-response authority;
- превращает containment/recovery в implied risk acceptance;
- делает любой incident/risk `P0` или Owner escalation;
- поглощает product/security/legal/customer/accounting/OS source-of-truth;
- создаёт duplicate issue/bug/security/incident tracker;
- фабрикует numeric probability, severity, loss, MTTR/RTO или risk score без evidence;
- позволяет stale/expired evidence/exception/approval продолжать consequential action;
- закрывает obligations/residual risks автоматически вместе с incident;
- создаёт budget/spend/customer commitment/technical access/OS Product Contract/runtime by implication;
- требует хранения чувствительных forensic/customer/security payloads или chain-of-thought в публичном repository.

## 2. Итерация 1 — Risk, issue, exception и incident должны иметь разные semantics

**Критика:** единый «risk register» часто превращается в смесь будущих рисков, текущих проблем, инцидентов, waivers и product bugs.

**Сверка:** proposal определяет `RSK-*`, `EXC-*`, `INC-*` отдельно и сознательно **не создаёт** `ISS-*`. Product bug остаётся product-owned; Company blocker — `WORK-*`/`OBL-*`; material event — `INC-*`; будущая exposure — `RSK-*`; deviation request — `EXC-*`.

Risk определяется как uncertain future event/condition/exposure, incident — как уже произошедшее/обнаруженное material adverse event/state, exception — как bounded deviation только при допустимости higher authority.

**Результат:** PASS.

## 3. Итерация 2 — Accepted risk нельзя получить из risk status или бездействия

**Критика:** поле вроде `accepted` в risk lifecycle легко превращается в скрытый approval path: risk «висит», работа продолжается, и система считает exposure принятой.

**Сверка:** proposal прямо запрещает accepted risk как самовозникающий lifecycle state. `response_intent=tolerate` остаётся лишь treatment direction. Когда acceptance требует authority, обязателен attributable `DEC-*`/`APR-*` reference; material acceptance сохраняет `ROD-06` и другие applicable `ROD-*`.

Silence, elapsed time, workaround и continued operation не являются acceptance.

**Результат:** PASS.

## 4. Итерация 3 — Exception request не должен становиться waiver

**Критика:** наличие `EXC-*` может быть ошибочно воспринято исполнителем как разрешение обойти control.

**Сверка:** states `requested`/`under_review` не разрешают deviation. Для `approved` требуются exact authority basis + attributable decision/approval refs + scope + period + conditions + exit/reversion. Technical workaround/admin access/urgency explicitly не создают exception.

`EXC-*` хранит residual risk refs, поэтому approval deviation не объявляет риск исчезнувшим.

**Результат:** PASS.

## 5. Итерация 4 — Higher-authority non-waivable controls нельзя «исключить» Company решением

**Критика:** внутренний exception register особенно опасен, если Owner approval ошибочно трактуется как возможность отменить закон, customer right, binding contract или OS invariant.

**Сверка:** proposal вводит `authority_basis = none/not_permitted` для boundary, где exception не допускается. В таком случае путь — stop/reconcile/proper amendment, а не `EXC-* approved`.

Это согласуется с AC-202: Owner не может legalize unlawful act, waive customer rights или weaken binding higher-authority invariants.

**Результат:** PASS.

## 6. Итерация 5 — Incident response не должен создавать authority через emergency

**Критика:** реальный incident создаёт давление «действовать немедленно», из-за чего наличие incident record может фактически стать ambient authority.

**Сверка:** proposal отделяет `incident_state` от response authority. Bounded reversible containment допустим только внутри существующих `AM-*`, Assignment/access и AC-207 continuity boundary. За пределами — `ESC-*`/`DEC-*`/`APR-*`.

Containment (`isolate/revoke/safe shutdown/preserve evidence`) отдельно от continuation/resumption с material unresolved gap. Последнее может требовать `ROD-06` risk acceptance.

**Результат:** PASS.

## 7. Итерация 6 — P0 и Owner attention не должны превращать любой риск в emergency queue

**Критика:** если severity/risk wording автоматически делает item P0 или Owner task, M4 создаст новый bottleneck и alert fatigue.

**Сверка:** proposal сохраняет AC-106: `P0` только для реального time-sensitive material obligation/cash/risk/customer/continuity/external-effect issue. `owner_attention=required` ограничен ROD/residual Owner authority/material exception/risk acceptance/Company-side consequential decisions beyond delegated bounds.

External/customer/provider/legal waiting может быть `waiting_external`, а non-Owner escalation идёт к exact target authority через AC-402.

**Результат:** PASS.

## 8. Итерация 7 — Incident closure не должна скрывать остаточные последствия

**Критика:** operationally incident может быть «resolved», но customer obligation, legal notification, product defect или residual risk остаются открытыми.

**Сверка:** proposal прямо запрещает implied closure. `INC-*` имеет notification obligation refs, recovery refs, residual risk refs, decision/approval refs и closure evidence. Closure означает только завершение Company incident-control need либо явный handoff последствий в отдельные control objects.

Закрытие `INC-*` не доказывает legal compliance, отсутствие liability, satisfaction `OBL-*` или acceptance residual risk.

**Результат:** PASS.

## 9. Итерация 8 — Company register не должен стать competing product/security/legal/OS source

**Критика:** incident/risk данные особенно быстро размножают conflicting root-cause/severity/impact records между системами.

**Сверка:** proposal делает Company layer canonical только для Company control metadata и management interpretation. Product/security telemetry/root cause, legal duties, customer facts, cash/accounting facts, OS lifecycle/incidents и product release/bug state остаются authoritative в своих contours.

Current OS re-check выполнен на `c2be41ad8d1b144bea2ab0b030c57bcf3c59a3ae`; P9.06 governed-actions UX не создаёт Company risk authority. OS Decision Authority Policy остаётся `Proposed 0.2.1` и не принимается.

**Результат:** PASS.

## 10. Итерация 9 — Не должно быть false precision и risk-management theater

**Критика:** стандартная probability×impact matrix без incident/economic history создаст псевдоточность и заставит Owner спорить о цветах/числах вместо material exposure.

**Сверка:** proposal наследует AC-105 consequence classes и явно не вводит обязательные percentages, annual loss, probability score, MTTR/RTO или RAG matrix. `likelihood_evidence` может быть `unknown`; management control строится на consequence, current exposure, trigger, control evidence, freshness и uncertainty.

`RSK-*` qualification остаётся material-only; мелкие product issues/alerts не регистрируются.

**Результат:** PASS.

## 11. Итерация 10 — Reconstructability не должна нарушать minimization или преждевременно создавать runtime

**Критика:** incident register может стать самым чувствительным местом Company и одновременно поводом преждевременно строить SIEM/dashboard/paging/workflow engine.

**Сверка:** proposal требует reference-over-copy и запрещает хранить в публичном repository credentials, exploit-enabling details, sensitive raw logs, full customer-confidential/legal/banking payload, unnecessary PII и chain-of-thought. Подробный evidence остаётся в restricted competent contour.

Implementation baseline допускает Markdown/YAML/JSON и прямо исключает обязательный dashboard/SIEM/automation. AC-404…AC-407 получают только bounded handoff.

**Результат:** PASS.

## 12. Acceptance matrix

| Проверка | Результат |
|---|---|
| risk ≠ issue ≠ exception ≠ incident | PASS |
| no universal `ISS-*` duplicate tracker | PASS |
| accepted risk requires competent attributable decision when required | PASS |
| risk status/silence/continued operation ≠ acceptance | PASS |
| exception request ≠ approved exception | PASS |
| technical bypass/admin access/urgency ≠ waiver | PASS |
| non-waivable higher-authority boundary preserved | PASS |
| approved exception has exact scope/period/conditions/exit | PASS |
| exception residual risk remains explicit | PASS |
| incident detection ≠ response authority | PASS |
| bounded containment preserves AC-203/AC-207 authority | PASS |
| containment/recovery ≠ material risk acceptance | PASS |
| incident closure ≠ obligation/legal/product/risk closure | PASS |
| `RSK-*`, `EXC-*`, `INC-*` stable identities separated | PASS |
| AC-105 consequence-based materiality preserved | PASS |
| no fabricated numeric risk score/probability/MTTR/RTO | PASS |
| AC-202 `ROD-*` preserved | PASS |
| AC-203 `AM-*` preserved | PASS |
| AC-207 `CM-*`/`CE-*` continuity semantics preserved | PASS |
| AC-401 WORK/OBL relations preserved | PASS |
| AC-402 DEC/APR/ESC relations preserved | PASS |
| P0 remains time-sensitive material priority | PASS |
| escalation target is not automatically Owner | PASS |
| stale/missing evidence fails safely | PASS |
| product/security/legal/customer/accounting/OS truth stays in source contour | PASS |
| OS P9.06 remains presentation/execution UX, not Company authority | PASS |
| Proposed OS Decision Authority Policy not adopted | PASS |
| public-repository minimization preserved | PASS |
| no chain-of-thought retention | PASS |
| no duplicate SIEM/security/product incident runtime | PASS |
| no budget/spend/customer commitment/access created | PASS |
| no Product Contract/OS lifecycle change created | PASS |
| downstream AC-404…AC-407 handoff bounded | PASS |

## 13. Cross-review conclusion

После 10 последовательных semantic, authority, risk/continuity, incident, operational, minimization и Company↔Product↔OS boundary checks material blocking objection не осталось.

Итог:

`AC-403 cross-review — COMPLETE / PASS FOR OWNER APPROVAL`.

Exact reviewed proposal остаётся:

- `docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL.md`;
- `Proposed 0.9.0`;
- blob `857b601423f78fc3d4636dbf9754d5410d8a1c55`.

Cross-review не является Owner approval и не делает proposal binding.

## 14. Required next gate

Для закрытия AC-403 требуется явный attributable Owner act, однозначно утверждающий exact reviewed proposal.

Рекомендуемая краткая формулировка:

`AC-403 утверждаю`.

До такого акта:

- AC-403 остаётся `Proposed`;
- roadmap остаётся на AC-403;
- Approved `1.0.0` publication не создаётся;
- AC-404 не становится current canonical action.