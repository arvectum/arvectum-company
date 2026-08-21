# AC-406 — Owner Mission Control / Reference-Implementation Evidence View

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-406 — Owner Mission Control / reference-implementation evidence view`
Решение: `docs/governance/decisions/DECISION-2026-08-21-AC-406-APPROVAL.md`
Cross-review: `docs/reviews/AC-406-OWNER-MISSION-CONTROL-REFERENCE-EVIDENCE-CROSS-REVIEW.md`
Approved proposal: `Proposed 0.9.0`, blob `f9e4d0f8e2e2a13f1147a8518461b35cd5264724`

## 1. Approval publication

Этот документ является канонической Approved publication AC-406 `1.0.0`.

Утверждённое собственником нормативное содержание — полная проверенная редакция:

`docs/operations/OWNER-MISSION-CONTROL-REFERENCE-IMPLEMENTATION-EVIDENCE-VIEW.md`

с immutable git blob SHA:

`f9e4d0f8e2e2a13f1147a8518461b35cd5264724`.

Proposal включён в эту publication целиком по immutable content reference. Настоящая publication не меняет нормативное содержание проверенной редакции.

Явное решение собственника зафиксировано в:

`docs/governance/decisions/DECISION-2026-08-21-AC-406-APPROVAL.md`.

## 2. Approved model

AC-406 `1.0.0` устанавливает binding Company-level Owner Mission Control / reference-implementation evidence view в пределах incorporated proposal, включая:

1. Mission Control как derived evidence projection, а не новый source of truth;
2. reuse существующих `WORK/OBL`, `DEC/APR/ESC`, `RSK/EXC/INC`, AC-404 finance evidence и `PORT-*`/AC-405 state без нового authority namespace;
3. separation `source fact ≠ Company interpretation ≠ recommendation ≠ decision ≠ approval ≠ legal/corporate/customer act ≠ technical authorization ≠ execution evidence`;
4. owner-facing sections `Protect Now`, `Owner Action Required`, `Delegated Work / No Owner Action`, `Cash / Commitments / Obligation Signals`, `Portfolio / Opportunity / Review Triggers`, `Reference-Implementation Evidence`;
5. suppression routine delegated/technical/informational items из Owner queue;
6. `waiting_external` как watch state, а не false Owner task;
7. decision-ready Owner card с exact question, `why_now`, capacity, authority basis, evidence/as-of, unknowns, downside/reversibility, excluded effects, requested act, remaining gates и execution handoff;
8. возможность `not decision-ready` при недостаточном/stale/unknown/conflicted evidence;
9. freshness/conflict discipline без arbitrary universal TTL;
10. сохранение AC-404 distinction forecast/receivable ≠ available cash;
11. public/restricted boundary и reference-over-copy для sensitive finance/customer/legal/security data;
12. source-backed reference-implementation evidence по authority separation, Position accountability, bounded AI/software execution, fail-closed/escalation, Owner reconstruction burden, continuity/replacement, business linkage, provenance и learning;
13. запрет unsupported AI-autonomy %, maturity/readiness score и productivity claims;
14. governance design/technical PASS/agent counts/dashboard existence как insufficient operational proof;
15. Company/Product/Arvectum OS source-of-truth и governance separation;
16. отсутствие automatic portfolio re-ranking/module promotion/Product Contract/capability transition;
17. read-oriented default; consequential UI interaction только через отдельный valid governed authority/execution path;
18. отсутствие software dashboard prerequisite;
19. initial implementation path `semantic model → restricted Markdown/structured projection → actual Owner-use evidence in AC-407 → only then UI/OS composition decision`;
20. отсутствие live snapshot population, budget/payment/customer/product/external-effect authority по импликации.

## 3. Authority boundary

AC-406 не создаёт Organizational Authority.

Visibility, card/button presence, favorable recommendation, risk/finance/portfolio status или Mission Control placement сами по себе не создают approval, legal/corporate competence, spend/payment right, customer authority, Product Contract или execution authorization.

Consequential action продолжает требовать attributable Principal в правильной capacity, действующий authority basis, exact subject/evidence/approvals, technical authorization/access и applicable external-effect safeguards.

## 4. Source-of-truth boundary

- Company repository authoritative только для Company governance/control/management interpretation в своём scope;
- product repositories authoritative для implementation/status/domain semantics;
- Arvectum OS authoritative для Product Contracts, RFC/ADR, Platform Capability lifecycle и platform semantics;
- legal/corporate/customer/vendor/accounting/bank/security sources authoritative в своих contours.

Mission Control может агрегировать и интерпретировать evidence, но не переписывает underlying source truth.

## 5. Reference-implementation evidence boundary

AC-406 позволяет собственнику оценивать, работает ли Arvectum Company как owner-controlled AI-native organization, но только через actual source-backed operational evidence.

Утверждённая governance design сама по себе не доказывает:

- фактическое снижение Owner workload;
- качество/стоимость/надёжность AI execution;
- continuity/replacement readiness;
- profitability/market validation/customer readiness;
- production readiness;
- repeatability или external transferability.

Такие claims требуют exact observed scope/period, evidence refs, repeatability basis, limitations и next validation trigger.

## 6. Cross-review and approval evidence

Cross-review:

- `docs/reviews/AC-406-OWNER-MISSION-CONTROL-REFERENCE-EVIDENCE-CROSS-REVIEW.md`;
- iterations: `8`;
- result: `Complete / PASS for Owner approval`;
- immutable blob SHA: `f6db950a29f30da0065277e50da41a2d84e3b2ed`.

Approved proposal:

- `docs/operations/OWNER-MISSION-CONTROL-REFERENCE-IMPLEMENTATION-EVIDENCE-VIEW.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `f9e4d0f8e2e2a13f1147a8518461b35cd5264724`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-21-AC-406-APPROVAL.md` — `Approved`;
- explicit wording: `AC-406 утверждаю`.

## 7. Approval result

`AC-406 — Owner Mission Control / reference-implementation evidence view` имеет статус `Complete / PASS` и является binding Company owner-facing evidence-model baseline в пределах заявленного scope.

Следующее каноническое действие:

`AC-407 — Management operating cadence and control review`.

AC-407 должен использовать AC-401…AC-406 в actual operating cadence, проверить Owner reconstruction/control burden, review/attention frequencies, evidence freshness и достаточность M4 exit evidence без преждевременного software/dashboard expansion.