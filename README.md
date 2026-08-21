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

`AC-501 — First governed workflow candidate selection` закрыт как `Complete / PASS`.

Утверждён первый M5 workflow:

**`WF-M5-001 — Customer Feedback → Classified Correction → Verified Candidate → Customer Validation / Acceptance`**, первый real-operation contour — **`PORT-002 — Discount Parser`**.

Текущее каноническое действие:

**`AC-502 — Workflow, accountable Position, authority/data/evidence contract` — формализация выбранного workflow до implementation и supervised real-operation proof.**

M5:

```text
AC-501 first governed workflow candidate selection       Complete / PASS
→ AC-502 workflow / Position / authority / data contract Current
→ AC-503 Arvectum OS reliance/admission mapping          Planned
→ AC-504 bounded workflow implementation                 Planned
→ AC-505 supervised real-operation proof                 Planned
→ AC-506 incident/recovery/fallback drill                Planned
→ AC-507 business-value/economic continue-change-stop    Planned
```

## Что установил M4

AC-401…AC-406 сформировали Company control/reference-observability layers, а AC-407 установил их operating cadence и закрыл M4.

Ключевые границы сохраняются:

`Mission Control ≠ source of truth ≠ authority ≠ approval ≠ execution`;

`source fact ≠ Company interpretation ≠ recommendation ≠ decision ≠ approval ≠ legal/corporate/customer act ≠ technical authorization ≠ execution evidence`;

`bank/accounting fact ≠ management interpretation ≠ forecast ≠ budget/limit ≠ planned spend ≠ approved internal commitment ≠ incurred obligation ≠ actual payment`;

`P0 temporary execution priority ≠ permanent portfolio reclassification`;

`reference/reuse evidence ≠ automatic module admission`.

Approved operating cadence после M4:

```text
material event
→ immediate bounded update/review
→ Owner only if actual authority/action need exists

active operating week + material aggregate state
→ at most one short asynchronous Owner checkpoint

monthly
→ one integrated management checkpoint

quarterly
→ integrated portfolio / continuity-gap / control-fit / Owner-burden revalidation
```

Daily dashboard/meeting ritual не требуется. Routine `AM-1`/`AM-2` work не проходит полную governance ceremony, если не пересечена material/authority boundary.

## Что выбрал AC-501

AC-501 сравнил несколько реальных workflow candidates и выбрал `WF-M5-001` не потому, что Discount Parser технически зрелее остальных, а потому что здесь уже есть повторяющийся customer-feedback/correction/validation loop, прямой business/customer value, явный Owner exception/rework bottleneck, bounded technical delegation path, practical fallback и сильный reconstruction evidence path.

Выбор `PORT-002` не означает новый budget, permanent portfolio re-ranking, новый customer commitment или product/production-readiness claim.

## Что AC-502 должен определить

До implementation AC-502 должен установить для `WF-M5-001`:

- exact start/end и workflow states;
- accountable и participating Positions;
- permitted/excluded `AM-*` actions;
- customer scope/commitment/acceptance gates;
- Company/Product source-of-truth boundary;
- data/tool/access requirements;
- evidence contract и reconstructability;
- stale/unknown/ambiguous-input behavior;
- escalation/fail-closed conditions;
- continuity/manual fallback;
- lightweight M5 measurements по Owner interventions, rework, blocking/cycle и outcome quality.

Arvectum OS не считается обязательным по импликации. Exact reliance/admission mapping — отдельный AC-503.

## Business-first portfolio order

При отсутствии более высокого `P0` обязательства default discretionary portfolio order остаётся:

`PORT-002 → PORT-001 → PORT-003/PORT-004 по named trigger → PORT-007 clarification-only → PORT-005/PORT-006 contain`.

Это не budget, funding allocation или постоянная engineering queue. AC-106 `P0…P3` hierarchy остаётся выше portfolio ranking.

## Граница Arvectum OS

Company-specific Positions, Assignments, authority, portfolio decisions, operating controls и M5 workflow governance принадлежат `arvectum/arvectum-company`.

Product implementation/status остаются в product repositories. Domain-neutral platform architecture, Product Contracts, RFC/ADR и Platform Capability lifecycle принадлежат `arvectum/arvectum-os`.

AC-501 не создаёт Company Product Contract/Active Capability в Arvectum OS. Любая реальная OS reliance для `WF-M5-001` проходит отдельный AC-503/admission mapping и применимый OS governance path.

## Граница публичного репозитория

Этот репозиторий публичный. **Запрещено** размещать здесь secrets, reusable credentials, private keys, signatures, избыточные персональные данные, банковские/платёжные payloads, transaction exports, confidential exact cash balances, sensitive tax/accounting documents, непубличные customer/vendor/contract materials, privileged payment/fraud/incident/security details и chain-of-thought.

Для `WF-M5-001` здесь должны храниться только public-safe governance/evidence references и sanitized operating meaning. Raw customer evidence остаётся в соответствующем authorized contour.

## Удалённые репозитории

GitHub `arvectum/arvectum-company` — канонический remote.

GitVerse — зеркало для устойчивости и технологической суверенности. Наличие mirror не делает его самостоятельным источником Organizational Authority и не меняет canonical status автоматически.
