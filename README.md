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
- Первый public-safe Mission Control evidence snapshot: `docs/operations/OWNER-MISSION-CONTROL-REFERENCE-SNAPSHOT-2026-08-21.md`
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

`AC-501`, `AC-502` и `AC-503` закрыты как `Complete / PASS`.

Утверждён первый M5 workflow:

**`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`**, первый real-operation contour — **`PORT-002 — Discount Parser`**.

Для workflow утверждён operating contract:

- `POS-002 — Commercial & Customer Lead` — один end-to-end accountable Position;
- `POS-004 — Engineering & Release Lead` — accountable Position технического сегмента `W4 → W7`;
- states `W0…W11`;
- classifications `CL-1…CL-7`;
- initial human-attributable `W3 — Classified` через current POS-002 Assignment;
- AI-led bounded engineering через POS-004 в existing `AM-0/1/2` и access ceilings;
- `AM-3`/`AM-4` не активированы;
- customer/data/access/evidence/failure/continuity boundaries зафиксированы.

Ключевые правила:

`technical PASS ≠ customer-facing approval ≠ customer acceptance`;

`Candidate Ready ≠ permission to deploy/send/promise`;

`customer silence ≠ acceptance` без более сильного authoritative rule;

`technical task closed ≠ Company/customer obligation satisfied`.

AC-503 дополнительно установил:

**`NO-ADDITIONAL-OS-RELIANCE — no additional Arvectum OS reliance required for the first M5 proof of WF-M5-001`.**

Это означает, что первый proof может быть реализован на текущих Company/product/customer-owned sources и tools без обязательного OS Execution Context/shared history/CAP-004 и без нового OS Product Contract, пока implementation не пересекает actual governed-OS reliance trigger.

Это не отказ от Arvectum OS. Это bounded decision только для первого M5 proof.

Текущее каноническое действие:

**`AC-504 — Bounded workflow implementation` — сделать минимальную обратимую OS-neutral реализацию первого реального workflow case/evidence contour.**

M5:

```text
AC-501 first governed workflow candidate selection       Complete / PASS
→ AC-502 workflow / Position / authority / data contract Complete / PASS
→ AC-503 Arvectum OS reliance/admission mapping          Complete / PASS
→ AC-504 bounded workflow implementation                 Current
→ AC-505 supervised real-operation proof                 Planned
→ AC-506 incident/recovery/fallback drill                Planned
→ AC-507 business-value/economic continue-change-stop    Planned
```

## Что установил AC-503

AC-503 проверил current canonical Arvectum OS state и не нашёл фактической необходимости делать OS обязательной dependency первого WF-M5-001 proof.

Existing `P6.06` в `arvectum/arvectum-os` остаётся узким Provisional Product Contract для controlled Telegram publication/reconstruction и **не расширяется** на customer-feedback/correction workflow. Его CAP-004 reliance не переносится на WF-M5-001 по импликации.

Company workflow states, classification, Position accountability, customer acceptance semantics и M5 measurements остаются Company-owned. Product implementation/status остаются в `arvectum/discount-parser`. Raw customer feedback/validation остаётся в соответствующем authorized customer/workstream contour.

Если AC-504 реально потребует OS canonical state, OS Governed Execution, CAP-004, OS-held authorization, shared provenance/history или admitted Productive Workspace composition, Company должна остановиться на этой границе и заново пройти applicable Arvectum OS Product Contract/capability/RFC/ADR governance path до consequential reliance.

## Что делает AC-504

AC-504 реализует smallest sufficient mechanics для одного реального WF-M5-001 case.

Нужно получить lightweight, reconstructable implementation, которая:

- знает exact workflow/version;
- ведёт safe case identifier и material `W*` transitions;
- хранит attributable `CL-*` classification;
- связывает protected customer feedback refs с product issue/PR/commit/test/build/release-candidate refs;
- различает Candidate Ready, customer-facing handoff и customer acceptance;
- умеет явно быть `blocked/unknown/stale/uncertain`;
- не требует raw customer DC-2 или reusable DC-3 secrets в public repo;
- допускает manual fallback и runtime replacement;
- достаточно проста для следующего supervised AC-505 proof.

AC-504 не должен строить generic workflow engine, event bus, Company-wide orchestration platform, CAP-004 substitute или локальный «mini Arvectum OS».

Technical implementation PASS не является AC-505 empirical proof и не закрывает M5.

## Business-first portfolio order

При отсутствии более высокого `P0` обязательства default discretionary portfolio order остаётся:

`PORT-002 → PORT-001 → PORT-003/PORT-004 по named trigger → PORT-007 clarification-only → PORT-005/PORT-006 contain`.

Это не budget, funding allocation или постоянная engineering queue. AC-106 `P0…P3` hierarchy остаётся выше portfolio ranking.

## Граница Arvectum OS

Company-specific Positions, Assignments, authority, portfolio decisions, operating controls и M5 workflow governance принадлежат `arvectum/arvectum-company`.

Product implementation/status остаются в product repositories. Domain-neutral platform architecture, Product Contracts, RFC/ADR и Platform Capability lifecycle принадлежат `arvectum/arvectum-os`.

Approved AC-503 explicitly says that **additional OS reliance is not required for the first proof**, but future actual reliance must still pass the applicable OS governance path.

## Граница публичного репозитория

Этот репозиторий публичный. **Запрещено** размещать здесь secrets, reusable credentials, private keys, signatures, избыточные персональные данные, банковские/платёжные payloads, transaction exports, confidential exact cash balances, sensitive tax/accounting documents, непубличные customer/vendor/contract materials, privileged payment/fraud/incident/security details и chain-of-thought.

Для `WF-M5-001` здесь должны храниться только public-safe governance/evidence references и sanitized operating meaning. Raw customer evidence остаётся в соответствующем authorized contour.

## Удалённые репозитории

GitHub `arvectum/arvectum-company` — канонический remote.

GitVerse — зеркало для устойчивости и технологической суверенности. Наличие mirror не делает его самостоятельным источником Organizational Authority и не меняет canonical status автоматически.
