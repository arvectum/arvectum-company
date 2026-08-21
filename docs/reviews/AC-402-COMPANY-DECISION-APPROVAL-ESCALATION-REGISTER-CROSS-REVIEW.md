# AC-402 — Cross-review: Decision, Approval and Escalation Register Model

Статус: `Complete / PASS for Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `10`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-402 — Decision, approval and escalation register model`

Проверенный exact proposal:

- `docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `a48081ba3599e6f3c91b8a6562435ad1f0c152f4`.

Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`.

## 1. Review gate

AC-402 должен быть отклонён, если модель:

- превращает recommendation/draft в decision;
- выводит approval из silence, AI confidence, favorable score, workflow completion или technical execution;
- смешивает внутреннюю Company Organizational Authority с participant/General Director/customer/Product/Arvectum OS authority;
- использует наличие credential/IAM permission как decision authority;
- ослабляет `ROD-01…ROD-09` или расширяет `AM-0…AM-4`;
- создаёт одну неразличимую запись для decision, approval, legal act и execution;
- считает internal Owner approval достаточным для legal/customer/external effect, когда существует отдельный gate;
- отправляет любую escalation Owner независимо от реального target authority;
- позволяет повторно использовать stale/expired approval после material changed facts;
- создаёт Company-wide бюрократию из каждого routine AM-2/product decision;
- создаёт competing source of truth для product/OS/legal/customer facts;
- переносит sensitive evidence в публичный repository без необходимости;
- молча принимает Proposed OS Decision Authority Policy как Company governance;
- создаёт dashboard/runtime/automation/budget/Product Contract/external commitment по импликации.

## 2. Итерация 1 — Recommendation, decision и approval должны быть разными объектами смысла

**Критика:** если `DEC-*` хранит proposal, outcome и approval рядом, интерфейс или исполнитель может принять подготовленный recommendation за решение.

**Сверка:** proposal прямо устанавливает фундаментальное неравенство:

`recommendation ≠ decision ≠ approval ≠ legal/corporate act ≠ technical authorization ≠ execution`.

`DEC-*` имеет отдельные `proposal_refs`, `decision_state`, `decision_outcome` и `decision_act_ref`. `ready` не означает approved; `deferred` требует explicit act; silence не создаёт defer. `APR-*` является отдельным namespace.

**Результат:** PASS.

## 3. Итерация 2 — Один attributable act не должен превратиться в две конкурирующие истины DEC/APR

**Критика:** Owner `ROD-*` approval одновременно является final internal decision act и approval act. Наличие `decision_act_ref` и `approval_act_ref` может породить два расходящихся текста.

**Сверка:** proposal не требует двух независимых authority acts. `DEC-*` представляет decision subject/outcome, `APR-*` — отдельный authority gate/act control record; Section 13 запрещает неявные выводы между lifecycle. Для одного Owner act обе references могут указывать на **один и тот же attributable canonical act/record**, а DEC и APR остаются разными control semantics, не двумя решениями.

Критически, Company-internal canonicality определяется самим approved authority act, а не дублирующей summary. При конфликте summary с source применяется source-of-truth boundary.

**Результат:** PASS; implementation invariant: один реальный act не должен копироваться как два независимых authoritative payload.

## 4. Итерация 3 — Owner, участник, генеральный директор и технический исполнитель нельзя сливать

**Критика:** в текущей небольшой компании несколько capacities могут физически совпадать в одном Principal; register может ошибочно представить один Owner click как одновременно corporate act, legal signature и execution authorization.

**Сверка:** Section 6.2 сохраняет external/legal authority отдельно; Section 10.4 требует отдельные gates/capacities даже при совпадении physical Principal; Section 11 отделяет technical authorization. `approval_domain` и `required_approver_capacity` фиксируют именно capacity, а не просто имя.

Это согласуется с Company Constitution Articles III/VI/VIII и AC-202.

**Результат:** PASS.

## 5. Итерация 4 — ROD и AM boundaries не должны быть переопределены новым реестром

**Критика:** AC-402 вводит новые IDs и states; их легко ошибочно использовать как новый authority engine.

**Сверка:** `authority_basis` и `decision_authority` обязаны ссылаться на уже valid source. `ROD-*` остаются hard Owner boundary, `AM-*` — существующей delegation semantics. `APR-*` не создаёт authority; `DEC-*` не расширяет её. `AM-3` требует active delegation/eligible Principal; exceed → escalation. `ROD-*` требует explicit Owner act.

Explicit non-effects запрещают delegation/broadening по импликации.

**Результат:** PASS.

## 6. Итерация 5 — Decision outcome не должен означать readiness к внешнему эффекту

**Критика:** внутреннее `approve` может быть принято при ещё не полученном customer/corporate/legal gate или отсутствии technical authorization.

**Сверка:** proposal вводит отдельный `effect_readiness` и в Section 6.3 прямо показывает последовательность: internal DEC → pending APR legal/customer gate → absent technical authorization → external effect MUST NOT execute. Section 11 снова отделяет access/execution.

Следовательно `approve` означает только approved exact internal decision scope; оно не является универсальным permission token.

**Результат:** PASS.

## 7. Итерация 6 — Escalation не должна автоматически становиться Owner queue

**Критика:** если вся uncertainty уходит Owner, AC-402 воспроизведёт bottleneck, против которого построены AC-202/203/401.

**Сверка:** `ESC-*` имеет `target_authority` и `owner_attention = required | not_required | waiting_external`. Section 12.2 направляет к Owner только `ROD-*`, residual Owner authority, explicit Owner escalation target либо Company-side Owner decision перед другим gate. Customer/product/accounting/legal/security targets не становятся false Owner work.

Section 12.3 подавляет waiting noise до legitimate trigger.

**Результат:** PASS.

## 8. Итерация 7 — Changed facts должны инвалидировать reuse старого approval

**Критика:** durable decision record опасен, если исполнитель воспринимает его как бессрочное разрешение, хотя изменились customer terms, cash, risk, scope или authority.

**Сверка:** `evidence_as_of`, `review_expiry_trigger`, `effective_period` и Section 14 требуют re-check при material changed facts. При mismatch effect readiness блокируется; decision/approval может стать expired/superseded либо требовать нового decision. Explicit rule: `Unknown ≠ approved`.

Section 15 сохраняет исторический факт approval даже после revocation/expiry и не переписывает историю.

**Результат:** PASS.

## 9. Итерация 8 — Company register не должен поглотить product, OS и external governance

**Критика:** `approval_domain = product/arvectum_os` можно неверно прочитать как право Company фиксировать product/OS approval самостоятельно.

**Сверка:** Section 6.2 прямо оставляет Product governance и OS RFC/ADR/Product Contract/lifecycle decisions в их canonical contours. `authoritative_source_ref` обязателен, когда Company repo не является authority source. Section 20 запрещает превращать OS UI/persistence в Company authority и отдельно фиксирует, что Proposed OS Decision Authority Policy не принимается.

Current OS re-check performed at `8d35eb3867c4aed60f7aaa201c0c03a9aa3b1353`; OS Decision Authority Policy действительно остаётся Proposed `0.2.1`.

**Результат:** PASS.

## 10. Итерация 9 — Нельзя регистрировать каждое решение и получить governance theater

**Критика:** три namespace могут быстро превратить Company repository в универсальный decision log, где Owner и Positions тонут в routine choices.

**Сверка:** Section 5 исключает каждый draft, AI recommendation, validation, GitHub review, routine AM-2 choice, workflow step и product architecture decision без Company-level material control. Qualification основан на obligations/capital/risk/customer/external effect/authority/portfolio/continuity/Owner attention.

Owner projection Section 17 выводит только actual Owner gates; routine choices и external waiting исключены.

**Результат:** PASS.

## 11. Итерация 10 — Reconstructability не должна нарушить minimization или превратиться в runtime design

**Критика:** подробный decision packet может подтолкнуть к хранению contract/customer/legal/security payloads и к преждевременной реализации dashboard/OS workflow.

**Сверка:** Section 18 запрещает signatures, banking payload, customer-confidential text, credentials, privileged security details и chain-of-thought; используется reference-over-copy. `rationale_summary` явно не является reasoning transcript. Section 19 утверждает только semantic model и допускает простой Markdown/YAML/JSON baseline; dashboard/runtime не требуется. Explicit non-effects не создают software/automation/Product Contract.

Downstream AC-403…AC-407 получают только bounded handoff, их scope не проектируется заранее.

**Результат:** PASS.

## 12. Acceptance matrix

| Проверка | Результат |
|---|---|
| recommendation/draft ≠ decision | PASS |
| decision ≠ approval gate/act | PASS |
| approval ≠ legal/corporate/customer act by implication | PASS |
| technical permission ≠ Organizational Authority | PASS |
| technical success/workflow completion ≠ approval | PASS |
| `DEC-*`, `APR-*`, `ESC-*` identities separated | PASS |
| exact material qualification gate | PASS |
| routine low-risk AM-2/product work excluded by default | PASS |
| `ROD-01…ROD-09` preserved | PASS |
| `AM-0…AM-4` preserved | PASS |
| explicit attributable Owner act required for ROD | PASS |
| explicit attributable AM-3 act required | PASS |
| approve/reject/defer/approve-with-conditions distinct | PASS |
| silence cannot approve or defer | PASS |
| internal decision outcome separated from effect readiness | PASS |
| corporate/legal/customer gate may remain pending | PASS |
| physical Principal does not merge capacities | PASS |
| escalation target is explicit | PASS |
| escalation not automatically Owner | PASS |
| waiting external cases suppress Owner noise | PASS |
| stale/missing evidence blocks unsafe reliance | PASS |
| changed facts trigger review/redecision | PASS |
| expiry/revocation/supersession preserve history | PASS |
| AC-401 WORK/OBL semantics preserved | PASS |
| product repository authority preserved | PASS |
| Arvectum OS authority preserved | PASS |
| Proposed OS Decision Authority Policy not adopted | PASS |
| public-repository minimization preserved | PASS |
| no chain-of-thought retention requirement | PASS |
| no budget/spend/external commitment created | PASS |
| no dashboard/runtime/automation required | PASS |
| no Product Contract/OS lifecycle transition created | PASS |
| AC-403…AC-407 handoff remains bounded | PASS |

## 13. Cross-review conclusion

После 10 последовательных semantic, authority, operational, security/minimization и Company↔Product↔OS boundary checks material blocking objection не осталось.

Итог:

`AC-402 cross-review — COMPLETE / PASS FOR OWNER APPROVAL`.

Exact reviewed proposal остаётся:

- `docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL.md`;
- `Proposed 0.9.0`;
- blob `a48081ba3599e6f3c91b8a6562435ad1f0c152f4`.

Cross-review не является Owner approval и не делает proposal binding.

## 14. Required next gate

Для закрытия AC-402 требуется явный attributable Owner act, однозначно утверждающий exact reviewed proposal.

Рекомендуемая краткая формулировка:

`AC-402 утверждаю`.

До такого акта:

- AC-402 остаётся `Proposed`;
- roadmap остаётся на AC-402;
- Approved `1.0.0` publication не создаётся;
- AC-403 не становится current canonical action.
