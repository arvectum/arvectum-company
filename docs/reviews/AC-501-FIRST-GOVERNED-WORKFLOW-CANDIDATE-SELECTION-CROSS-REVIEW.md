# AC-501 — First Governed Workflow Candidate Selection — Cross-Review

Статус: `Complete`
Результат: `PASS for explicit Owner approval`
Дата: `2026-08-21`
Максимум итераций: `10`
Выполнено итераций: `10 of 10`
Reviewed proposal: `docs/operations/FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION.md`
Reviewed proposal status/version: `Proposed 0.9.0`
Reviewed immutable blob SHA: `f6cbebfea1c2e6a56a0fd03c38b68a7211c6bbde`
Owner approval: `Pending`

## 1. Review purpose

Cross-review проверяет не привлекательность Discount Parser как продукта, а корректность **Company-level selection decision** для M5.

Главный вопрос:

> Является ли `WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`, впервые применяемый к `PORT-002 — Discount Parser`, наиболее сильным первым governed Company workflow candidate при текущем evidence — без подмены бизнес-ценности технической зрелостью, без расширения authority и без создания искусственного OS dependency?

Review использует Ratified Company Constitution, AC-103/104/106, Approved M2 authority/Position/Assignment/access/continuity baseline, current PORTFOLIO `0.8.0`, M4 operating-control baseline и current product evidence.

Arvectum OS current `main` re-check: commit `76504766353028540891ac1dfdbf1e5dc331a4af`. AC-501 не создаёт OS reliance; точная admission mapping остаётся AC-503.

## 2. Review method

Использованы десять независимых review lenses:

1. business/economic relevance;
2. customer/value-stream reality;
3. Owner-workload reduction;
4. authority/governance correctness;
5. data/tool/access feasibility;
6. risk/reversibility;
7. continuity/fallback;
8. evidence/reconstructability;
9. Company↔Product↔OS boundary;
10. adversarial alternative-selection / final synthesis.

`PASS` означает только, что proposal достаточно силён для явного Owner selection decision. Он не означает M5 completion, customer acceptance, product readiness или economic success.

---

## Iteration 1 — Business / economic relevance

### Проверка

Roadmap требует real customer/revenue/obligation value or evidence acquisition и likely operational/economic value relative to control cost.

### Evidence

- AC-103 определяет `VS-2 — Iterative correction to accepted outcome` как текущий реальный value stream, а не гипотетический future process.
- AC-106 ставит existing customer delivery/acceptance/support obligations в `P0` when materially time-sensitive и product work, привязанную к real revenue/obligation/evidence, выше speculative expansion.
- PORTFOLIO `0.8.0` ставит `PORT-002` в `A1` и прямо называет real client acceptance/live environment feedback decisive near-term evidence.

### Finding

`PASS`.

WF-M5-001 имеет прямую связь с существующим customer-value contour и не создаёт отдельный демонстрационный проект.

### Guardrail

Не доказаны margin, ROI или monetary value одного feedback cycle; proposal правильно не фабрикует их и переносит измерение в AC-505/507.

---

## Iteration 2 — Customer/value-stream reality

### Проверка

Нужно убедиться, что workflow действительно повторяется, а не выведен из одного эпизода.

### Product evidence

Current `arvectum/discount-parser` evidence показывает повторяющуюся цепочку customer feedback → diagnosis → correction → new candidate build:

- PR #65 — feedback #4;
- #66 — #5;
- #67 — #6;
- #68 — #7;
- #69 — #8;
- #70 — #9;
- #71 — #10;
- #73 — #11.

PR #71 отдельно показывает важный organization-design signal: customer workflow был упрощён от technical selector configuration к `URL → automatic preview → customer confirmation`.

### Finding

`PASS`.

Repeatability materially stronger, чем у candidate discovery/pilot contours, где Company-level recurring external evidence пока слабее.

### Guardrail

Merged PR или passing CI не считается customer acceptance. Proposal это явно сохраняет.

---

## Iteration 3 — Owner workload / bottleneck fit

### Проверка

AC-104 выявил, что главный bottleneck — не coding capacity, а interpretation, customer context, exception routing, rework и acceptance judgment.

### Evidence

Selected workflow атакует именно:

- `B-3 — Customer-context continuity bottleneck`;
- `B-4 — Exception and rework bottleneck`;
- `MW-4 — Customer feedback and exception handling`;
- частично `MW-2 — Work sequencing`.

При этом POS-004 уже AI-led для bounded engineering work, поэтому реальная экспериментальная ценность M5 состоит не в «дать AI написать код», а в проверке организационной цепочки вокруг входящего customer evidence и безопасной передачи admitted correction в engineering.

### Finding

`PASS`.

Это более сильный test of the Company model, чем очередной pure engineering automation slice.

### Guardrail

Owner-load reduction должна измеряться prospective evidence; структурная возможность снижения не равна доказанной экономии времени.

---

## Iteration 4 — Authority and accountability correctness

### Проверка

Selection не должен преждевременно создавать Position authority или превращать AI classification в approval.

### Evidence

AC-203 задаёт `AM-0…AM-4`, deny-by-default и escalation on ambiguity/material commitment. AC-204/205 закрепляют POS-002/POS-004 и текущие executor models.

Proposal:

- оставляет accountable Position окончательно открытым до AC-502;
- формулирует только leading hypothesis `POS-002 primary / POS-004 technical`;
- не создаёт AM-3/AM-4;
- сохраняет Owner/ROD/material commitment/ambiguous acceptance gates;
- отделяет classification/recommendation от customer acceptance и legal/contract interpretation.

### Finding

`PASS`.

Primary-accountability hypothesis семантически правдоподобна: конечный outcome — customer validation/acceptance, а не просто release artifact.

### Required AC-502 check

AC-502 MUST explicitly decide:

- где POS-002 может сделать bounded classification/next-action decision;
- где POS-004 может execute correction without per-task Owner approval;
- какие states требуют Owner/customer/human gate;
- является ли customer-facing send/manual delivery отдельным external-effect step.

---

## Iteration 5 — Data / tool / access feasibility

### Проверка

Первый workflow не должен требовать широкого нового credential surface только ради M5.

### Evidence

AC-206 разрешает POS-004 bounded repo/worktree/build/test execution без ambient secrets, bank/signing/commercial privileges. POS-002 AI support может работать с scoped evidence, но dedicated commercial sender/CRM ещё не fully proven.

Selected contour позволяет:

- оставить customer communication в существующем human channel;
- не давать AI bank/signing/general mailbox access;
- не копировать reusable secrets или raw restricted customer payload в Company repo;
- использовать product repo/CI как основной technical substrate.

### Finding

`PASS`.

Это один из главных факторов превосходства CAND-1 над CAND-2 и CAND-4 как **первого** workflow.

### Guardrail

Actual specific customer data/right/access must be checked case-by-case before AC-505 real operation.

---

## Iteration 6 — Risk and reversibility

### Проверка

M5 требует minimum sufficient reversible contour.

### Positive factors

- bounded feedback item/batch;
- no automatic new customer commitment;
- no payment/signing/legal effect;
- no mandatory OS dependency;
- technical changes remain product-owned and versioned;
- customer-facing validation remains gated;
- new scope or unclear rights escalates/fails closed.

### Failure modes reviewed

1. AI misclassifies new scope as defect.
2. Technical fix passes tests but does not solve customer issue.
3. Customer feedback lacks enough evidence.
4. Fix introduces regression.
5. Workflow ceremony costs more than it saves.
6. Product accepted/closed before M5 starts, making the candidate artificial.

Proposal contains stop/escalation conditions for all six classes at the selection level.

### Finding

`PASS`.

Risk is meaningful enough to test governance but bounded enough for first real supervised proof.

---

## Iteration 7 — Continuity / fallback

### Проверка

First contour должен иметь credible fallback rather than require perfect automation.

### Evidence

AC-207 already establishes that POS-004 runtime is replaceable and customer/acceptance ambiguity queues/stops rather than transferring authority. Existing current operation is Owner-led feedback→correction handling.

Proposed fallback:

```text
AI/software unavailable or outcome uncertain
→ preserve state/evidence
→ stop autonomous progression
→ human/Owner continues existing manual loop
```

### Finding

`PASS for selection`.

Fallback exists conceptually and operationally as current practice.

### Limitation

This is not `CE-3`. AC-506 must perform a real failure/uncertainty/recovery drill and expose if manual fallback depends on undocumented Owner memory.

---

## Iteration 8 — Evidence / reconstructability

### Проверка

M5 must produce evidence good enough for AC-507 continue/change/stop.

### Evidence readiness

The selected contour can naturally produce:

- source feedback reference;
- classification + revision;
- admitted scope decision;
- technical work/reference;
- test/build evidence;
- candidate release version;
- customer validation result;
- rework/escalation/fallback evidence;
- Owner intervention class;
- cycle/control burden.

This aligns with AC-401/402/403/404/406 semantics without requiring every technical event to become a Company canonical record.

### Finding

`PASS`.

Proposal correctly separates Company control evidence from product implementation truth and customer source truth.

### Guardrail

Reconstructability MUST NOT become indiscriminate retention of customer payload, logs, prompts or secrets.

---

## Iteration 9 — Company / Product / Arvectum OS boundary

### Проверка

AC-501 must not move Discount Parser semantics into Company or choose the candidate because P6.06/CAP-004 already exists.

### Findings

- Company owns the selected **workflow/accountability/control semantics**.
- `arvectum/discount-parser` remains authoritative for parsing logic, code, tests, installer, product release and domain-specific implementation.
- customer/source facts remain externally authoritative.
- Arvectum OS dependency is explicitly **not presumed**.
- AC-503 separately evaluates actual OS reliance and may validly conclude `none required for first M5 slice`.

Current OS main was checked at `76504766353028540891ac1dfdbf1e5dc331a4af`; current platform progress creates no reason to force Company workflow coupling.

### Finding

`PASS`.

Proposal respects the project instruction that technology/platform serves the Company rather than defining the candidate.

---

## Iteration 10 — Adversarial alternative selection / final synthesis

### Counterfactual A — Select AC-108 flagship discovery first

Argument: P1 flagship evidence is strategically central.

Review result: **not stronger as first M5 contour** because real recurring external execution evidence and sender/CRM/handoff readiness are weaker. AC-108 should continue in parallel and can become a later governed workflow.

### Counterfactual B — Select Tender Agent pre-bid workflow first

Argument: well-bounded and already OS-contract aware.

Review result: **rejected for first selection** because Company evidence still lacks comparable paid/pilot/repeatability proof. Selecting it would risk the exact technical-readiness bias prohibited by AC-501.

### Counterfactual C — Select finance/obligation packet first

Argument: high consequence and Owner value.

Review result: **defer as first contour** because current source completeness/access in the public reference state is intentionally unknown and financial data is more sensitive. Strong later candidate when a real decision packet is triggered.

### Counterfactual D — Reuse governance publication workflow

Argument: already proven and safe.

Review result: **reject for M5 selection** because M4 already demonstrated this class; repeating it gives weak incremental business evidence.

### Counterfactual E — Select a pure engineering release workflow

Argument: POS-004 is AI-led and automation is mature.

Review result: **inferior** because it would mostly prove existing technical automation. WF-M5-001 is stronger because it spans customer evidence → organizational classification → bounded engineering → customer validation.

### Final finding

`PASS`.

No alternative candidate currently dominates CAND-1 across real recurring value, Owner bottleneck relevance, bounded authority, current tool readiness, reversibility and evidence value.

---

## 3. Cross-review conclusion

Cross-review result:

`Complete / PASS for explicit Owner approval`.

Reviewed exact proposal:

- path: `docs/operations/FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `f6cbebfea1c2e6a56a0fd03c38b68a7211c6bbde`.

Recommended exact Owner decision:

> **Утвердить AC-501 и выбрать `WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`, first instantiated on `PORT-002 — Discount Parser`, как первый governed Company workflow candidate для M5. Перейти к AC-502. Selection не означает customer acceptance, новое обязательство, spend authority, production approval, OS reliance или broader product readiness.**

## 4. Approval boundary

Cross-review PASS is not Owner approval.

До явного Owner action:

- proposal остаётся `Proposed`;
- AC-501 остаётся `Current`;
- AC-502 не становится canonical current action;
- roadmap, canonical-source registry and approved publication are not advanced as if selection were already approved.

После explicit Owner approval требуется bounded publication step:

1. создать `FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION-v1.0.0.md`;
2. записать Owner decision artifact;
3. синхронизировать `ROADMAP.md`, `CANONICAL-SOURCES.md` и navigation где требуется;
4. сделать read-after-write verification;
5. установить `AC-502 — Workflow, accountable Position, authority/data/evidence contract` как следующее каноническое действие.