# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.41.0`
Создано: `2026-08-19`
Обновлено: `2026-08-22`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-505 — Supervised real-operation proof`
Параллельно завершено: `AC-506 — Incident, uncertain-outcome, recovery and fallback drill`
Следующее доступное параллельное действие: `AC-507 — Business-value/economic review preparation`

## 1. Модель публикации

Эта редакция `0.41.0` сохраняет полное содержание дорожной карты `0.40.0` по immutable git blob и добавляет фактический промежуточный outcome AC-505, завершение AC-506 в параллельном контуре и готовность к подготовительной части AC-507.

Предыдущая редакция:

- версия: `0.40.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `069a08d22f0d0bc5b9f8a6e71c6d3f0c64870eb9`.

Все ранее определённые M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop, AC-501 workflow selection, AC-502 workflow contract, AC-503 no-additional-OS-reliance decision и конечный AC-901 сохраняются, если прямо не изменены более новым approved decision или этой canonical roadmap publication в пределах planning authority.

## 2. AC-505 — текущий реальный operating proof

`AC-505 — Supervised real-operation proof` остаётся:

`Current / In Progress`.

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

## 3. Закрытие AC-506

`AC-506 — Incident, uncertain-outcome, recovery and fallback drill` имеет статус:

`Complete / PASS`.

Implementation/recovery artifacts:

- `tools/wf_m5_001_recovery.py` — W11 immutable-predecessor / linked-successor recovery helper;
- `tests/test_wf_m5_001_recovery.py` — recovery/fallback guard tests;
- `.github/workflows/wf-m5-001-case.yml` — now runs both bounded workflow and recovery tests;
- `docs/operations/WF-M5-001-RECOVERY-FALLBACK-RUNBOOK.md` — `Active 1.0.0`;
- `docs/operations/AC-506-INCIDENT-UNCERTAIN-OUTCOME-RECOVERY-FALLBACK-DRILL-EVIDENCE.md` — `Complete / PASS 1.0.0`;
- `docs/reviews/AC-506-INCIDENT-UNCERTAIN-OUTCOME-RECOVERY-FALLBACK-CROSS-REVIEW.md` — `10 of 10`, `PASS for AC-506 completion`.

Remote fresh-runtime evidence:

- PR `#8 — AC-506 — recovery drill validation`;
- tested head `931853edbf5e162c103091539b55f8b7068db4fb`;
- GitHub Actions workflow run `32555014701`;
- job `96987697988`;
- Ubuntu 24.04 / CPython 3.12.14;
- `14 tests / 14 PASS / 0 failures / 0 errors`.

The drill exercised:

- real AC-505 uncertainty/fail-closed behavior;
- manual case-state reconstruction without raw customer payload;
- fresh helper/process execution;
- immutable W11 predecessor + successor recovery design;
- no automatic reclassification/admission after recovery;
- secret-like evidence rejection;
- duplicate-successor/retry protection.

Narrow CE evidence after AC-506:

- WF-M5-001 W11 successor recovery mechanics → `CE-3`;
- WF-M5-001 case-state/manual fallback → `CE-3`;
- WF-M5-001 helper/process portability → `CE-3`;
- real insufficient-evidence fail-closed behavior → `CE-2`.

AC-506 does **not** upgrade actual POS-004 AI runtime/model swap, Owner-independent commercial/legal continuity, Company-wide DR, credentials/signing/provider replacement or customer-system recovery.

## 4. What AC-504 established

`AC-504 — Bounded workflow implementation` remains `Complete / PASS`.

For one supervised `WF-M5-001` case the Company has a minimal OS-neutral mechanism that can:

- pin exact AC-502/AC-503 governance versions and exact product baseline;
- create a safe case identifier and local non-git case record;
- represent material `W0…W11` state history and `CL-1…CL-7` classification evidence;
- enforce attributable POS-002 Company/customer gates and POS-004 technical gates;
- reject `AM-3/AM-4`;
- admit only unambiguous `CL-1` into ordinary technical correction;
- require test + candidate provenance before `W7 — Candidate Ready`;
- preserve `Candidate Ready ≠ customer handoff ≠ customer acceptance`;
- require explicit customer validation before `W10`;
- represent `blocked / unknown / stale / uncertain` explicitly;
- link product/customer/control evidence without copying authoritative raw payloads;
- fall back to manual case mechanics if helper/runtime is unavailable.

AC-506 extends recovery/fallback around this implementation without changing its authority contract.

## 5. Status milestones

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

## 6. Phase 5 — First governed Company operating contour

| ID | Работа | Статус |
|---|---|---|
| `AC-501` | First governed workflow candidate selection | `Complete / PASS` |
| `AC-502` | Workflow, accountable Position, authority/data/evidence contract | `Complete / PASS` |
| `AC-503` | Arvectum OS reliance/admission mapping where applicable | `Complete / PASS` |
| `AC-504` | Bounded workflow implementation | `Complete / PASS` |
| `AC-505` | Supervised real-operation proof | `Current / external evidence wait` |
| `AC-506` | Incident, uncertain-outcome, recovery and fallback drill | `Complete / PASS` |
| `AC-507` | Business-value/economic review and continue/change/stop decision | `Planned / preparation available in parallel` |

AC-506 was intentionally executed in parallel while AC-505 remained at a legitimate external-evidence wait. This does not treat AC-506 as a substitute for AC-505 evidence and does not close M5 out of sequence.

## 7. Текущее действие — AC-505

Цель AC-505 остаётся прежней: получить достаточный factual supervised proof на реальном customer/workstream source для `PORT-002 — Discount Parser`.

Current next valid evidence for the existing case is one or more of:

- exact affected build/version;
- exact source/settings/environment reference sufficient for reproduction;
- current reproduction result;
- new explicit customer validation/rework evidence.

Until such evidence exists, existing case `WF-M5-001-20260821-AC505001` remains W11 and no POS-004 correction is admitted.

A different real customer feedback item may also be selected if it can progress further through WF-M5-001 without violating scope/authority/data boundaries.

## 8. AC-505 success / stop semantics

AC-505 may eventually complete `PASS` even with rework or explicit non-acceptance if the workflow correctly classifies/escalates, authority boundaries are preserved and evidence is reconstructable.

AC-505 must not receive a false PASS when:

- authoritative customer/scope/evidence basis is missing;
- proof would require a new customer promise, material external commitment, budget/spend, AM-3/AM-4 or inaccessible/restricted data;
- implementation would require new actual OS governed reliance not admitted under AC-503;
- product technical evidence cannot confirm claimed state;
- customer validation cannot be attributed to a real authoritative source.

## 9. AC-507 parallel preparation boundary

While AC-505 waits for external evidence, AC-507 may begin **preparatory evidence collection only**, including:

- Owner intervention count/time where actually measurable;
- workflow/recovery handling effort;
- avoided or incurred engineering work;
- test/runtime/tool cost evidence where available;
- governance overhead and friction;
- evidence quality/reconstructability;
- hypotheses about business value and cost that remain clearly labelled as hypotheses.

The final `continue / change / stop` decision for M5 must not be fabricated from incomplete customer/business evidence. AC-507 finalization must distinguish observed facts from hypotheses and preserve any required Owner decision boundary.

## 10. M5 exit direction

M5 remains open.

It can close only after the required combined evidence set is sufficient, including:

- real operation/customer outcome evidence from AC-505 or an accepted equivalent factual case outcome;
- actual uncertainty/failure/recovery evidence, now partially supplied by AC-506;
- Owner burden evidence;
- technical/AI quality, cost and reliability evidence where applicable;
- AC-507 business-value/economic review and authorized continue/change/stop result.

AC-506 technical/governance PASS is not customer acceptance, profitability or M5 closure.

## 11. Authority and boundary rule

Roadmap does not create Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant, production approval or OS lifecycle transition.

AC-504/AC-506 mechanics may execute only inside approved AC-202…AC-207, AC-502 and AC-503 boundaries. Runtime/process recovery does not transfer authority, and synthetic drill evidence may never be represented as real customer evidence.
