# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `3.11.0`
Обновлено: `2026-08-22`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `3.10.0` по immutable git blob и добавляет AC-507 business/economic proposal, cross-review и roadmap `0.42.0` с явным Owner decision gate.

Предыдущая редакция:

- версия: `3.10.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `701dd876daebab3ad10fa9fa835582cfacdc2fc7`.

Полное нормативное и evidence-содержание предыдущего реестра сохраняется, если прямо не изменено более новым approved artifact, attributable decision или этой planning/source-registry публикацией в пределах её роли.

## 2. Порядок приоритета источников

В своей области действуют:

1. применимое право и действительные legal/corporate authorities;
2. утверждённые Company governance artifacts и явные attributable Owner/Principal decisions;
3. canonical Arvectum OS sources там, где Company фактически использует OS;
4. product repositories/decisions в пределах product scope;
5. verified Company implementation/evidence внутри approved governance boundary;
6. roadmap как planning source, не источник authority;
7. chat/model memory/local copies/generated materials как context/evidence до explicit promotion.

Proposal/review evidence не создаёт authority и не заменяет Owner decision.

## 3. Действующая дорожная карта

- `docs/roadmap/ROADMAP.md` — `Active 0.42.0`;
- immutable blob SHA: `57eaca14aae1eeb681b16e5f5cded36ad4a8f8da`.

Current parallel state:

- `AC-505 — Supervised real-operation proof` — `Current / external evidence wait`;
- `AC-506 — Incident, uncertain-outcome, recovery and fallback drill` — `Complete / PASS`;
- `AC-507 — Business-value/economic review` — `Current / Owner decision gate`;
- `M5 — First real governed Company operating contour proven` — `Current`.

## 4. AC-505 real-operation evidence

First real case remains:

`WF-M5-001-20260821-AC505001`.

Current factual outcome:

`CL-3 — Evidence insufficient / not reproduced`
→
`W11 — unknown / customer-evidence follow-up required`.

Canonical public-safe evidence remains:

- `docs/operations/AC-505-SUPERVISED-REAL-OPERATION-ADMISSION-EVIDENCE.md` — `0.3.0`;
- `docs/operations/AC-505-WF-M5-001-20260821-AC505001-EVIDENCE.md` — `1.0.0`;
- `docs/reviews/AC-505-SUPERVISED-REAL-OPERATION-ADMISSION-CROSS-REVIEW.md` — `1.2.0`, `10/10`.

No POS-004 correction, customer acceptance or reproduction success is inferred.

## 5. AC-506 completion baseline

`AC-506 — Complete / PASS` remains binding evidence within its bounded implementation/test scope.

Canonical artifacts remain:

- `tools/wf_m5_001_recovery.py` — blob `114dec37cf86c2b5e5d20b569126efb133782407`;
- `tests/test_wf_m5_001_recovery.py` — blob `0e940f3002482fb36288dee1828ee48aa8237db5`;
- `.github/workflows/wf-m5-001-case.yml` — blob `fc02c94aaaf2464ee839cc754a716f3719d63509`;
- `docs/operations/WF-M5-001-RECOVERY-FALLBACK-RUNBOOK.md` — blob `f72918271e2195e0e8741ec2f0b8ffb86ba744a1`;
- `docs/operations/AC-506-INCIDENT-UNCERTAIN-OUTCOME-RECOVERY-FALLBACK-DRILL-EVIDENCE.md` — blob `5af5f0cd44fd0266b2857aa16b1732dcf2644304`;
- `docs/reviews/AC-506-INCIDENT-UNCERTAIN-OUTCOME-RECOVERY-FALLBACK-CROSS-REVIEW.md` — blob `4659d9ca0b493e1d85566c302ab25d94d5110b82`.

Remote test evidence remains `14/14 PASS` on GitHub Actions run `32555014701`.

## 6. AC-507 proposal and review

Prepared business/economic review:

- `docs/business/AC-507-BUSINESS-VALUE-ECONOMIC-REVIEW.md`;
- status/version: `Proposed 0.9.0`.

Cross-review:

- `docs/reviews/AC-507-BUSINESS-VALUE-ECONOMIC-REVIEW-CROSS-REVIEW.md`;
- `10 of 10`;
- result: `PASS for Owner decision gate`.

Reviewed recommendation:

**`CONTINUE WITH CHANGE — bounded evidence phase`.**

The recommendation is based on currently evidenced control value:

- real fail-closed prevention of unsupported engineering admission;
- attributable human authority at POS-002 classification;
- no false customer acceptance;
- reconstructable case state;
- provenance-preserving recovery.

The review also records real/known friction:

- Owner attention at the current human POS-002 gate;
- evidence/state handling overhead;
- engineering effort spent on workflow/recovery implementation;
- inability of governance to manufacture missing customer evidence.

## 7. Economic evidence limitations

Current evidence is insufficient to claim:

- profitability;
- increased revenue/margin;
- improved customer satisfaction;
- reduced total delivery cost;
- quantified engineering savings;
- cross-product transferability worth platformization;
- justification for AM-4 or autonomous customer effects.

Owner minutes, engineering effort, per-case runtime/tool cost, customer cycle-time effect and commercial outcome are not measured sufficiently for precise unit economics.

Unknown does not mean zero.

## 8. Owner decision boundary

The AC-507 proposal/cross-review do **not** approve themselves.

Continue/change/stop is treated as a portfolio/investment direction decision under applicable `ROD-04` semantics. Exact proposed approval wording:

`AC-507: CONTINUE WITH CHANGE — bounded evidence phase — утверждаю`.

If approved, the decision would:

- continue WF-M5-001 in bounded evidence mode;
- preserve current authority/data/customer/OS boundaries;
- introduce no material budget by itself;
- keep AM-3/AM-4 inactive;
- defer platformization/generalization;
- prioritize stronger real-case evidence and lightweight Owner/engineering burden measurement.

It would **not** close AC-505 or M5 while customer/economic evidence remains insufficient.

## 9. Arvectum OS boundary

AC-503 result remains:

`NO-ADDITIONAL-OS-RELIANCE` for the first M5 proof.

AC-507 does not create Product Contract, Platform Capability lifecycle transition, OS repository commitment or platform funding claim.

## 10. Public repository boundary

The public Company repository must not contain secrets, reusable credentials, private keys/signatures, unnecessary PII, bank/payment payloads, transaction exports, confidential exact cash balances, non-public customer/vendor/contract materials, sensitive tax/accounting documents, privileged payment/fraud/incident/security details or chain-of-thought.

AC-507 uses only public-safe Company/product/workflow evidence and does not duplicate raw customer payload.

## 11. Next valid action

Two independent gates remain:

1. AC-507: explicit Owner decision on the reviewed recommendation;
2. AC-505: new/recovered authoritative customer/reproduction evidence or another qualifying real case.

Neither gate may be inferred from silence or technical PASS.
