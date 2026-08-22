# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.42.0`
Создано: `2026-08-19`
Обновлено: `2026-08-22`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-505 — Supervised real-operation proof`
Параллельно: `AC-507 — Business-value/economic review — Owner decision gate`
Завершено параллельно: `AC-506 — Incident, uncertain-outcome, recovery and fallback drill`

## 1. Модель публикации

Эта редакция `0.42.0` сохраняет полное содержание дорожной карты `0.41.0` по immutable git blob и добавляет подготовленный AC-507 business/economic review, cross-review и переход к явному Owner decision gate.

Предыдущая редакция:

- версия: `0.41.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `3e7ba79af1781ea0a27fb1a1e914ef2621ea36a5`.

Все ранее определённые M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop, AC-501 workflow selection, AC-502 workflow contract, AC-503 no-additional-OS-reliance decision и конечный AC-901 сохраняются, если прямо не изменены более новым approved decision или этой canonical roadmap publication в пределах planning authority.

## 2. AC-505 — текущий реальный operating proof

`AC-505 — Supervised real-operation proof` остаётся:

`Current / external evidence wait`.

Первый real customer case:

`WF-M5-001-20260821-AC505001`.

Фактический outcome:

`W3 — CL-3 Evidence insufficient / not reproduced`
→
`W11 — unknown / customer-evidence follow-up required`.

Public-safe evidence:

- `docs/operations/AC-505-SUPERVISED-REAL-OPERATION-ADMISSION-EVIDENCE.md` — current version `0.3.0`;
- `docs/operations/AC-505-WF-M5-001-20260821-AC505001-EVIDENCE.md` — `1.0.0`;
- `docs/reviews/AC-505-SUPERVISED-REAL-OPERATION-ADMISSION-CROSS-REVIEW.md` — `1.2.0`, `10 of 10`.

Human-attributable POS-002 classification was explicitly confirmed as:

`CL-3 — Evidence insufficient / not reproduced`.

No POS-004 technical correction was admitted. No customer acceptance was inferred. The real case remains fail closed pending new authoritative reproduction/customer evidence.

AC-505 does not block independent bounded Company work that does not pretend to be AC-505 customer evidence.

## 3. AC-506 — завершённый recovery/fallback drill

`AC-506 — Incident, uncertain-outcome, recovery and fallback drill`:

`Complete / PASS`.

Canonical artifacts:

- `tools/wf_m5_001_recovery.py`;
- `tests/test_wf_m5_001_recovery.py`;
- `.github/workflows/wf-m5-001-case.yml`;
- `docs/operations/WF-M5-001-RECOVERY-FALLBACK-RUNBOOK.md` — `Active 1.0.0`;
- `docs/operations/AC-506-INCIDENT-UNCERTAIN-OUTCOME-RECOVERY-FALLBACK-DRILL-EVIDENCE.md` — `Complete / PASS 1.0.0`;
- `docs/reviews/AC-506-INCIDENT-UNCERTAIN-OUTCOME-RECOVERY-FALLBACK-CROSS-REVIEW.md` — `10 of 10`, PASS.

Remote fresh-runtime evidence:

- PR `#8 — AC-506 — recovery drill validation`;
- workflow run `32555014701`;
- job `96987697988`;
- Ubuntu 24.04 / CPython 3.12.14;
- `14 tests / 14 PASS / 0 failures / 0 errors`.

Narrow evidence after AC-506:

- W11 successor recovery mechanics → `CE-3`;
- case-state/manual fallback reconstruction → `CE-3`;
- helper/process portability → `CE-3`;
- real insufficient-evidence fail-closed behavior → `CE-2`.

No Company-wide DR, Owner-independent continuity, actual POS-004 AI model/runtime swap, credential/signing/provider recovery or customer-system recovery is claimed.

## 4. AC-507 — business/economic review prepared

`AC-507 — Business-value/economic review and continue/change/stop decision` теперь имеет статус:

`Current / Owner decision gate`.

Prepared proposal:

- `docs/business/AC-507-BUSINESS-VALUE-ECONOMIC-REVIEW.md` — `Proposed 0.9.0`.

Cross-review:

- `docs/reviews/AC-507-BUSINESS-VALUE-ECONOMIC-REVIEW-CROSS-REVIEW.md` — `10 of 10`, `PASS for Owner decision gate`.

Observed value supported by current evidence:

- unsupported engineering admission was avoided on a real CL-3 case;
- human Organizational Authority remained attributable;
- customer acceptance was not fabricated from silence/technical evidence;
- bounded case state is reconstructable without active model/session memory;
- recovery preserves immutable predecessor provenance.

Observed/known costs and friction:

- current POS-002 human gate consumes Owner attention;
- evidence normalization/state handling has process overhead;
- AC-504/AC-506 implementation/review required engineering effort;
- workflow cannot manufacture missing customer reproduction evidence.

Not yet measured sufficiently:

- Owner minutes per case;
- engineering effort avoided/incurred;
- per-case tool/runtime cost;
- customer cycle-time effect;
- margin/revenue/customer-satisfaction impact.

Therefore no profitability claim is supported.

## 5. AC-507 recommendation

Reviewed recommendation:

**`CONTINUE WITH CHANGE — bounded evidence phase`.**

Meaning:

1. continue WF-M5-001 as the first governed Company workflow;
2. preserve CL-3/W11 fail-closed, current authority/data/customer/OS boundaries;
3. use linked-successor recovery only on genuinely new evidence;
4. measure lightweight Owner intervention count/minutes in the next qualifying case;
5. capture coarse practical engineering-effort evidence where applicable;
6. reduce evidence-handling ceremony where another real case proves simplification safe;
7. do not create new CRM/workflow service/database/OS capability merely to complete M5;
8. do not activate AM-3/AM-4;
9. defer cross-product generalization/platformization until stronger real evidence exists.

The recommendation is reversible and introduces no material spend by itself.

Because continue/change/stop affects portfolio/investment direction, the recommendation requires explicit Owner approval under applicable ROD-04 semantics.

Exact proposed Owner wording:

`AC-507: CONTINUE WITH CHANGE — bounded evidence phase — утверждаю`.

## 6. Status milestones

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3` — `Complete / PASS`;
- `M4` — `Complete / PASS`;
- `M5 — First real governed Company operating contour proven` — `Current`;
- `M6 — First real AI-held Position proven economically and operationally` — `Planned`;
- `M7` — `Future`;
- `M8` — `Future`;
- `M9` — final planned human-readable Russian reconciliation stage after M8 unless Owner changes sequence.

## 7. Phase 5 — First governed Company operating contour

| ID | Работа | Статус |
|---|---|---|
| `AC-501` | First governed workflow candidate selection | `Complete / PASS` |
| `AC-502` | Workflow, accountable Position, authority/data/evidence contract | `Complete / PASS` |
| `AC-503` | Arvectum OS reliance/admission mapping where applicable | `Complete / PASS` |
| `AC-504` | Bounded workflow implementation | `Complete / PASS` |
| `AC-505` | Supervised real-operation proof | `Current / external evidence wait` |
| `AC-506` | Incident, uncertain-outcome, recovery and fallback drill | `Complete / PASS` |
| `AC-507` | Business-value/economic review and continue/change/stop decision | `Current / Owner decision gate` |

AC-506 and AC-507 preparation were intentionally executed in parallel while AC-505 remained at a legitimate external-evidence wait. Neither substitutes for missing AC-505 customer evidence.

## 8. AC-505 next evidence

Current next valid evidence for the existing case is one or more of:

- exact affected build/version;
- exact source/settings/environment reference sufficient for reproduction;
- current reproduction result;
- new explicit customer validation/rework evidence.

Until such evidence exists, case `WF-M5-001-20260821-AC505001` remains W11 and no POS-004 correction is admitted.

A different real customer feedback item may also be selected if it can progress further through WF-M5-001 without violating scope/authority/data boundaries.

## 9. AC-507 approval does not close M5

Even if the Owner approves `CONTINUE WITH CHANGE`, M5 remains open while the evidence set is insufficient.

M5 can close only after combined evidence is sufficient, including:

- real operation/customer outcome evidence from AC-505 or accepted equivalent factual case outcome;
- uncertainty/failure/recovery evidence supplied by AC-506;
- Owner burden evidence;
- technical/AI quality, cost and reliability evidence where applicable;
- authorized AC-507 continue/change/stop direction.

AC-507 approval is an economic direction decision, not customer acceptance, profitability proof or M5 closure.

## 10. Stop/reconsider direction

If `CONTINUE WITH CHANGE` is approved, later evidence should trigger reconsideration where:

- governance handling cost materially exceeds avoided rework/control value;
- customer evidence collection becomes a larger bottleneck than the work governed;
- routine low-risk steps repeatedly require Owner interpretation without measurable benefit;
- a materially simpler process achieves equal control;
- real economics do not justify continued support;
- additional progress would require material spend, new external commitment, AM-3/AM-4 or unadmitted OS reliance.

## 11. Authority and boundary rule

Roadmap does not create Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant, production approval or OS lifecycle transition.

AC-504/AC-506 mechanics may execute only inside approved AC-202…AC-207, AC-502 and AC-503 boundaries. Runtime/process recovery does not transfer authority, and synthetic drill evidence may never be represented as real customer evidence.

AC-507 proposal/cross-review do not approve the recommended economic direction. Explicit Owner action is required.