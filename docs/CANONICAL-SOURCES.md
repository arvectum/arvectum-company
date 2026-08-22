# Реестр канонических источников Arvectum Company

Статус: `Active`
Версия: `3.10.0`
Обновлено: `2026-08-22`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`

## 1. Модель публикации

Эта редакция сохраняет полный реестр `3.9.0` по immutable git blob и добавляет фактический AC-505 case outcome, AC-506 recovery/fallback implementation/evidence/cross-review, remote fresh-runtime test evidence и дорожную карту `0.41.0`.

Предыдущая редакция:

- версия: `3.9.0`;
- путь: `docs/CANONICAL-SOURCES.md`;
- immutable git blob SHA: `ce10305ceb72cbaf3e64c89e982790373acff065`.

Все ранее зарегистрированные Company Constitution/governance, M0–M4, AC-201…AC-504, portfolio, terminology, Company/Product/Arvectum OS boundaries, public/restricted-source rules и operating-control baseline сохраняются, если прямо не изменены более новым approved artifact/evidence.

## 2. Порядок приоритета источников

В своей области действуют:

1. применимое право и действительные legal/corporate authorities;
2. утверждённые Company governance artifacts и явные attributable Owner/Principal decisions;
3. canonical Arvectum OS sources там, где Company фактически использует OS;
4. product repositories/decisions в пределах product scope;
5. verified Company implementation/evidence внутри approved governance boundary;
6. roadmap как planning source, не источник authority;
7. chat/model memory/local copies/generated materials как context/evidence до explicit promotion.

Implementation/test evidence не создаёт authority и не заменяет external/customer/product source of truth.

## 3. Действующая дорожная карта

- `docs/roadmap/ROADMAP.md` — `Active 0.41.0`;
- immutable blob SHA: `3e7ba79af1781ea0a27fb1a1e914ef2621ea36a5`.

Текущее каноническое действие:

`AC-505 — Supervised real-operation proof` — `Current / external evidence wait`.

Параллельно завершено:

`AC-506 — Incident, uncertain-outcome, recovery and fallback drill` — `Complete / PASS`.

Следующее доступное параллельное действие:

`AC-507 — Business-value/economic review preparation`.

Текущий milestone:

`M5 — First real governed Company operating contour proven` — `Current`.

## 4. AC-504 bounded implementation baseline

`AC-504 — Bounded workflow implementation` остаётся `Complete / PASS`.

Canonical baseline artifacts:

| Artifact | Immutable blob SHA | Role |
|---|---|---|
| `docs/operations/AC-504-BOUNDED-WORKFLOW-IMPLEMENTATION-EVIDENCE.md` | `ad3855fc08448dbb190b1d486f255e5592f59d71` | AC-504 implementation evidence |
| `docs/reviews/AC-504-BOUNDED-WORKFLOW-IMPLEMENTATION-CROSS-REVIEW.md` | `f18251a813a002fdeb2e1c7d066ec5c9c34287f4` | 10/10 AC-504 cross-review |
| `tools/wf_m5_001_case.py` | `19373811e761226c3e418fa1b8086828c9caded6` | bounded OS-neutral case/evidence helper |
| `tests/test_wf_m5_001_case.py` | `14e20464fd2aea2d0b85c5b286950ae7ac55f86a` | original 7 scoped tests |
| `docs/operations/WF-M5-001-BOUNDED-IMPLEMENTATION-RUNBOOK.md` | `c51b522d66ce80ca4e2e46e5494fa32c3301ee27` | operator procedure |
| `docs/operations/WF-M5-001-CASE-TEMPLATE.json` | `b66fc43e1fa47e13c5f251588324a7a813bfd9fa` | private/manual fallback template |
| `.gitignore` | `516cb25b279ec91757230e37242ecb3fbd38f060` | excludes default `.local/` case storage |

AC-502/AC-503 governance pins carried by the helper remain unchanged, including:

`NO-ADDITIONAL-OS-RELIANCE` for the first M5 proof.

## 5. AC-505 real-operation evidence now available

First real customer case:

`WF-M5-001-20260821-AC505001`.

Current factual outcome:

`W3 — CL-3 Evidence insufficient / not reproduced`
→
`W11 — unknown / customer-evidence follow-up required`.

Canonical public-safe evidence:

- `docs/operations/AC-505-SUPERVISED-REAL-OPERATION-ADMISSION-EVIDENCE.md` — current version `0.3.0`, blob `cb98006de0da4077e3eb28a158b0e87b35e4fc06`;
- `docs/operations/AC-505-WF-M5-001-20260821-AC505001-EVIDENCE.md` — `1.0.0`, blob `c8e5fe5d83bfac91102fc1050d57202f8a5ba009`;
- `docs/reviews/AC-505-SUPERVISED-REAL-OPERATION-ADMISSION-CROSS-REVIEW.md` — `1.2.0`, `10 of 10`, blob `e43091f8932a7d14dbf077fd7d684ad29b7f30b9`.

Human-attributable POS-002 / AM-2 classification was explicitly confirmed as:

`CL-3 — Evidence insufficient / not reproduced`.

No POS-004 technical correction is admitted from the case. No customer acceptance, reproduction success or fix is inferred. AC-505 remains open pending authoritative new/recovered evidence or another suitable real case.

## 6. AC-506 recovery/fallback implementation

`AC-506 — Incident, uncertain-outcome, recovery and fallback drill` is `Complete / PASS`.

Canonical implementation artifacts:

| Artifact | Immutable blob SHA | Canonical role |
|---|---|---|
| `tools/wf_m5_001_recovery.py` | `114dec37cf86c2b5e5d20b569126efb133782407` | fail-closed W11 predecessor → linked successor recovery helper |
| `tests/test_wf_m5_001_recovery.py` | `0e940f3002482fb36288dee1828ee48aa8237db5` | 7 recovery/fallback regression tests |
| `.github/workflows/wf-m5-001-case.yml` | `fc02c94aaaf2464ee839cc754a716f3719d63509` | repeatable original + recovery test command |
| `docs/operations/WF-M5-001-RECOVERY-FALLBACK-RUNBOOK.md` | `f72918271e2195e0e8741ec2f0b8ffb86ba744a1` | recovery, uncertain-outcome and manual-fallback procedure |
| `docs/operations/AC-506-INCIDENT-UNCERTAIN-OUTCOME-RECOVERY-FALLBACK-DRILL-EVIDENCE.md` | `5af5f0cd44fd0266b2857aa16b1732dcf2644304` | `Complete / PASS 1.0.0` drill evidence |
| `docs/reviews/AC-506-INCIDENT-UNCERTAIN-OUTCOME-RECOVERY-FALLBACK-CROSS-REVIEW.md` | `4659d9ca0b493e1d85566c302ab25d94d5110b82` | `10 of 10`, PASS for AC-506 completion |

Recovery invariant:

```text
recovery ≠ rewrite
new evidence ≠ automatic reclassification
runtime replacement ≠ authority transfer
manual fallback ≠ weaker controls
uncertain external outcome ≠ assumed success
```

A terminal W11 predecessor remains unchanged; genuinely new evidence opens a linked successor with a fresh exact product baseline and fresh POS-002 classification gate.

## 7. AC-506 remote execution evidence

Deliberate PR validation:

- PR `#8 — AC-506 — recovery drill validation`;
- tested branch head `931853edbf5e162c103091539b55f8b7068db4fb`;
- workflow run `32555014701`;
- job `96987697988`;
- GitHub-hosted Ubuntu 24.04;
- CPython `3.12.14`;
- command `python -m unittest discover -s tests -p 'test_wf_m5_001_*.py' -v`;
- result: **`14 tests / 14 PASS / 0 failures / 0 errors`**.

PR #8 was subsequently merged; merge commit:

`8cfced2d48c3fdc965a7895e4dd9ccb21e12d7bf`.

This fresh checkout/process evidence supports only the narrow workflow helper/recovery portability claim. It is not evidence of an actual POS-004 AI model/agent runtime swap.

## 8. AC-207 continuity evidence interpretation after AC-506

AC-506 supports the following bounded evidence states:

| Scope | Evidence state after AC-506 | Boundary |
|---|---|---|
| WF-M5-001 W11 successor recovery mechanics | `CE-3` | deliberate synthetic recovery test, not fake customer recovery |
| WF-M5-001 case-state/manual fallback reconstruction | `CE-3` | bounded workflow case only |
| WF-M5-001 helper/process portability | `CE-3` | fresh GitHub-hosted checkout/process |
| real insufficient-evidence fail-closed behavior | `CE-2` | actual AC-505 W11 case |
| actual POS-004 AI runtime/model swap | unchanged `CE-1` | not exercised |
| Owner-independent commercial/legal continuity | unchanged | not exercised |
| Company-wide DR / credentials / signing / provider / customer-system recovery | unchanged | outside AC-506 scope |

No Company-wide disaster-recovery or AI-workforce replacement claim follows from this workflow-level drill.

## 9. Source-of-truth and data boundary

Company repository is canonical for approved Company workflow/recovery semantics and public-safe implementation/evidence definitions.

It is not canonical for raw customer payloads, Discount Parser product implementation truth, external legal/corporate facts or OS Product Contract/capability lifecycle.

Raw customer DC-2 and all DC-3 reusable secrets remain outside the public Company repository and ordinary helper/model context. Protected opaque references and sanitized summaries are used instead.

A synthetic incident-like test does not establish that a real incident occurred and does not create an `INC-*` record.

## 10. Authority boundary

AC-504/AC-506 software and test evidence do not create Organizational Authority.

Binding limits remain:

- attributable human POS-002 classification/customer gates;
- bounded POS-004 technical execution only after valid CL-1 admission;
- no AM-3/AM-4 in this contour;
- runtime/process replacement does not transfer authority;
- recovery does not auto-classify or auto-admit;
- Candidate Ready, handoff and customer acceptance remain distinct;
- customer silence is not acceptance;
- access/credentials do not create authority.

No separate Owner decision artifact was created for AC-506 because the completed work remained inside previously approved continuity/workflow/authority boundaries and created no ROD, budget, external commitment, Product Contract or OS lifecycle transition.

## 11. M5 navigation

1. `AC-501` — candidate selection — `Complete / PASS`;
2. `AC-502` — workflow/Position/authority/data/evidence contract — `Complete / PASS`;
3. `AC-503` — OS reliance/admission mapping — `Complete / PASS`;
4. `AC-504` — bounded workflow implementation — `Complete / PASS`;
5. `AC-505` — supervised real-operation proof — `Current / external evidence wait`;
6. `AC-506` — incident/uncertain-outcome/recovery/fallback drill — `Complete / PASS`;
7. `AC-507` — business-value/economic continue/change/stop — `Planned / preparation available in parallel`.

AC-506 is not a substitute for AC-505 evidence and does not close M5.

## 12. AC-507 preparation boundary

While AC-505 waits for authoritative external evidence, AC-507 may collect observed evidence on Owner interventions/time, workflow/recovery effort, avoided or incurred engineering work, tool/runtime cost where available, governance friction and reconstructability.

Final continue/change/stop judgment must distinguish facts from hypotheses and must not manufacture customer/business evidence that does not exist.

## 13. Public repository boundary

Публичный Company repository не должен содержать secrets, reusable credentials, private keys/signatures, unnecessary PII, bank/payment payloads, transaction exports, confidential exact cash balances, non-public customer/vendor/contract materials, sensitive tax/accounting documents, privileged payment/fraud/incident/security details или chain-of-thought.

## 14. Final planned language stage

`M9 — Человекочитаемая документация полностью русифицирована и согласована` remains the final planned stage after M8 unless the Owner explicitly changes sequence.

`AC-901 — Полная русификация человекочитаемой документации и итоговая междокументная сверка` remains `Planned`.
