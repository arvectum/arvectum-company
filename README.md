# Arvectum Company

Канонический репозиторий долговременных документов управления, планирования, портфеля и организационной модели ООО «Арвектум» как owner-operated AI-native company, где конечный контроль сохраняется за собственником, а значительная часть повторяемой работы может выполняться ИИ и программными средствами в утверждённых границах.

Arvectum Company — конкретная организация ООО «Арвектум». Это **не** Arvectum OS, не отдельный ИИ-агент и не универсальная программная платформа.

## С чего начать

- Конституция / внутренняя учредительная хартия Company: `docs/constitution/COMPANY-CONSTITUTION.md`
- Граница полномочий Company ↔ Arvectum OS: `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md`
- Реестр канонических источников: `docs/CANONICAL-SOURCES.md`
- Каноническая дорожная карта: `docs/roadmap/ROADMAP.md`
- Карта портфеля: `docs/portfolio/PORTFOLIO.md`
- Терминологический глоссарий: `docs/governance/TERMINOLOGY-GLOSSARY.md`
- AC-208 / закрытие M2: `docs/organization/REFERENCE-MODEL-TRANSFERABILITY-AND-M2-CLOSURE-v1.0.0.md`
- AC-307 / закрытие M3: `docs/portfolio/AC-307-PORTFOLIO-GOVERNANCE-REVIEW-AND-M3-CLOSURE-v1.0.0.md`
- AC-401 — work/obligation model: `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL-v1.0.0.md`
- AC-402 — decision/approval/escalation model: `docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL-v1.0.0.md`
- AC-403 — risk/exception/incident model: `docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL-v1.0.0.md`
- AC-404 — cash/commitment/management reporting: `docs/operations/COMPANY-CASH-COMMITMENT-MANAGEMENT-REPORTING-BASELINE-v1.0.0.md`
- AC-405 — portfolio/module/priority review cadence: `docs/portfolio/AC-405-PORTFOLIO-MODULE-PRIORITY-REVIEW-CADENCE-v1.0.0.md`
- AC-406 — Owner Mission Control evidence view: `docs/operations/OWNER-MISSION-CONTROL-REFERENCE-IMPLEMENTATION-EVIDENCE-VIEW-v1.0.0.md`
- AC-407 / закрытие M4: `docs/operations/MANAGEMENT-OPERATING-CADENCE-AND-M4-CONTROL-REVIEW-v1.0.0.md`
- AC-501 — выбор первого governed workflow: `docs/operations/FIRST-GOVERNED-WORKFLOW-CANDIDATE-SELECTION-v1.0.0.md`
- AC-502 — workflow authority/data/evidence contract: `docs/operations/FIRST-GOVERNED-WORKFLOW-AUTHORITY-DATA-EVIDENCE-CONTRACT-v1.0.0.md`
- AC-503 — Arvectum OS reliance/admission mapping: `docs/operations/FIRST-GOVERNED-WORKFLOW-ARVECTUM-OS-RELIANCE-ADMISSION-MAPPING-v1.0.0.md`
- AC-504 — bounded implementation evidence: `docs/operations/AC-504-BOUNDED-WORKFLOW-IMPLEMENTATION-EVIDENCE.md`
- AC-505 — real-case evidence: `docs/operations/AC-505-WF-M5-001-20260821-AC505001-EVIDENCE.md`
- AC-506 — recovery/fallback drill evidence: `docs/operations/AC-506-INCIDENT-UNCERTAIN-OUTCOME-RECOVERY-FALLBACK-DRILL-EVIDENCE.md`
- WF-M5-001 operator runbook: `docs/operations/WF-M5-001-BOUNDED-IMPLEMENTATION-RUNBOOK.md`
- WF-M5-001 recovery/fallback runbook: `docs/operations/WF-M5-001-RECOVERY-FALLBACK-RUNBOOK.md`
- WF-M5-001 manual fallback template: `docs/operations/WF-M5-001-CASE-TEMPLATE.json`
- Cross-reviews: `docs/reviews/`
- Durable Owner/governance decisions: `docs/governance/decisions/`

## Язык документов

Человекочитаемые Company-документы для русскоязычного управления пишутся преимущественно на русском языке. Английский допустим в коде, API, идентификаторах, именах файлов и технических схемах. Системообразующие термины связываются через `docs/governance/TERMINOLOGY-GLOSSARY.md`.

## Текущее состояние Company

- `M0` — Company founding: `Complete / PASS`;
- `M1` — business/economic baseline: `Complete / PASS`;
- `M2` — reference operating model and authority: `Complete / PASS`;
- `M3` — governed portfolio: `Complete / PASS`;
- `M4` — Owner control and reference-implementation observability: `Complete / PASS`;
- `M5` — first real governed Company operating contour: `Current`.

`AC-501`…`AC-504` закрыты как `Complete / PASS`. `AC-506` также закрыт как `Complete / PASS` в параллельном recovery/fallback контуре. `AC-505` остаётся `Current / external evidence wait`.

Утверждён первый M5 workflow:

**`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`**, первый real-operation contour — **`PORT-002 — Discount Parser`**.

Для workflow действуют:

- `POS-002 — Commercial & Customer Lead` — end-to-end accountable Position;
- `POS-004 — Engineering & Release Lead` — accountable Position технического сегмента;
- states `W0…W11` и classifications `CL-1…CL-7`;
- initial human-attributable POS-002 classification/customer gates;
- AI-led bounded POS-004 engineering только внутри existing `AM-0/1/2` и access ceilings;
- `AM-3/AM-4` не активированы;
- `technical PASS ≠ customer-facing approval ≠ customer acceptance`;
- `Candidate Ready ≠ permission to deploy/send/promise`;
- customer silence не является acceptance.

AC-503 установил:

**`NO-ADDITIONAL-OS-RELIANCE — no additional Arvectum OS reliance required for the first M5 proof of WF-M5-001`.**

Это bounded решение для первого M5 proof, а не отказ Company от Arvectum OS.

## AC-504 — bounded workflow implementation

Основной helper:

`tools/wf_m5_001_case.py`.

Он ведёт локальный reference-oriented case/evidence record и применяет bounded state/authority gates. Реальные case files по умолчанию находятся в `.local/wf-m5-001/` и исключены из git.

Helper pin-ит exact governance/product refs, сохраняет W*/CL* history, ограничивает Company/customer gates POS-002, technical gates POS-004, запрещает AM-3/4, не пропускает non-CL-1 в correction path, требует provenance для Candidate Ready и explicit customer validation для W10. Он не отправляет customer messages, не делает deploy/payment/signing/commitment/acceptance.

AC-504 scoped tests: **`7/7 PASS`**.

## AC-505 — первый real case

Current real case:

`WF-M5-001-20260821-AC505001`.

Фактический attributable outcome:

```text
real protected customer feedback
→ POS-002 human AM-2 classification
→ CL-3 — Evidence insufficient / not reproduced
→ W11 — unknown / customer-evidence follow-up required
```

Поэтому POS-004 technical correction **не** был открыт. Точный affected build/settings/environment и current reproduction не доказаны, customer validation/acceptance также не доказаны.

Это реальное evidence того, что workflow умеет fail closed вместо превращения недостаточного customer signal в выдуманный defect. Но этого пока недостаточно для полного AC-505 PASS.

## AC-506 — recovery / uncertain outcome / fallback

Добавлен recovery helper:

`tools/wf_m5_001_recovery.py`.

Recovery design:

```text
immutable W11 predecessor
→ genuinely new attributable evidence
→ new linked successor case
→ fresh exact product baseline
→ fresh POS-002 classification gate
```

Старый W11 case не переписывается и не «открывается заново». Recovery helper не классифицирует, не допускает W4, не отправляет customer messages и не создаёт authority.

Проверены:

- immutable predecessor;
- requirement for genuinely new evidence;
- no automatic reclassification/admission;
- non-CL-1 remains outside W4;
- secret-like evidence rejection;
- duplicate-successor/retry protection;
- bounded manual reconstruction when helper/local state is unavailable.

GitHub Actions fresh-runtime drill: **`14/14 PASS`** on Ubuntu 24.04 / CPython 3.12.14, workflow run `32555014701`.

После AC-506 узкие evidence states для WF-M5-001 successor recovery, case-state/manual fallback и helper/process portability достигли `CE-3 — Tested and Reviewed`; real insufficient-evidence fail-closed behavior имеет `CE-2` evidence.

Это **не** означает, что протестирован реальный POS-004 AI model/runtime swap, Company-wide disaster recovery, Owner-independent commercial/legal continuity или customer-system/credential/signing/provider recovery. Эти gaps остаются.

## Текущее каноническое действие и параллельная работа

Основное текущее действие остаётся:

**`AC-505 — Supervised real-operation proof`** — ждёт нового authoritative customer/reproduction evidence либо другого suitable real feedback case.

Параллельно доступна подготовительная часть:

**`AC-507 — Business-value/economic review and continue/change/stop decision`.**

До появления достаточного customer/business evidence можно собирать только реальные измеримые данные: Owner interventions/time, workflow/recovery effort, avoided/incurred engineering work, tool/runtime cost, governance friction и reconstructability. Финальный economic continue/change/stop вывод нельзя подменять гипотезой.

M5:

```text
AC-501 first governed workflow candidate selection       Complete / PASS
→ AC-502 workflow / Position / authority / data contract Complete / PASS
→ AC-503 Arvectum OS reliance/admission mapping          Complete / PASS
→ AC-504 bounded workflow implementation                 Complete / PASS
→ AC-505 supervised real-operation proof                 Current / external evidence wait
↘ AC-506 incident/recovery/fallback drill                Complete / PASS
→ AC-507 business-value/economic continue-change-stop    Planned / preparation available
```

M5 остаётся открытым.

## Business-first portfolio order

При отсутствии более высокого `P0` обязательства default discretionary portfolio order остаётся:

`PORT-002 → PORT-001 → PORT-003/PORT-004 по named trigger → PORT-007 clarification-only → PORT-005/PORT-006 contain`.

Это не budget, funding allocation или постоянная engineering queue. AC-106 `P0…P3` hierarchy остаётся выше portfolio ranking.

## Граница Arvectum OS

Company-specific Positions, Assignments, authority, portfolio decisions, operating controls и M5 workflow governance принадлежат `arvectum/arvectum-company`.

Product implementation/status остаются в product repositories. Domain-neutral platform architecture, Product Contracts, RFC/ADR и Platform Capability lifecycle принадлежат `arvectum/arvectum-os`.

AC-504/AC-506 не создают новой OS dependency. Если реальный AC-505 case потребует OS canonical state, Governed Execution, CAP-004 или иной admitted platform reliance, applicable AC-503/OS governance boundary должен быть открыт заново до consequential reliance.

## Граница публичного репозитория

Этот репозиторий публичный. **Запрещено** размещать здесь secrets, reusable credentials, private keys, signatures, избыточные персональные данные, банковские/платёжные payloads, transaction exports, confidential exact cash balances, sensitive tax/accounting documents, непубличные customer/vendor/contract materials, privileged payment/fraud/incident/security details и chain-of-thought.

Для `WF-M5-001` здесь хранятся implementation/governance artifacts и public-safe evidence references. Raw customer evidence остаётся в соответствующем authorized contour.

## Удалённые репозитории

GitHub `arvectum/arvectum-company` — канонический remote.

GitVerse — зеркало для устойчивости и технологической суверенности. Наличие mirror не делает его самостоятельным источником Organizational Authority и не меняет canonical status автоматически.
