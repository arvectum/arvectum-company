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

`AC-501` и `AC-502` закрыты как `Complete / PASS`.

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

Текущее каноническое действие:

**`AC-503 — Arvectum OS reliance/admission mapping where applicable` — проверить, нужна ли вообще фактическая опора `WF-M5-001` на Arvectum OS до реализации.**

M5:

```text
AC-501 first governed workflow candidate selection       Complete / PASS
→ AC-502 workflow / Position / authority / data contract Complete / PASS
→ AC-503 Arvectum OS reliance/admission mapping          Current
→ AC-504 bounded workflow implementation                 Planned
→ AC-505 supervised real-operation proof                 Planned
→ AC-506 incident/recovery/fallback drill                Planned
→ AC-507 business-value/economic continue-change-stop    Planned
```

## Что установил AC-502

AC-502 сделал selected workflow достаточно точным для следующего implementation/admission decision, но не объявил его уже работающим.

Company owns workflow/accountability/authority/evidence semantics. `arvectum/discount-parser` остаётся canonical source product implementation/status. Raw customer feedback/acceptance остаётся в соответствующем authorized customer/workstream contour. Material `WORK/OBL/DEC/APR/ESC/RSK/EXC/INC` создаются только по existing qualification rules.

Raw customer `DC-2` по умолчанию не переносится в public Company repo и не передаётся AI без необходимости. `DC-3` reusable secrets не должны попадать в обычный model context.

AC-502 не создаёт customer promise, budget, spend/payment/signing authority, new Position/Assignment/access, autonomous consequential customer effect, full product readiness claim или M5 completion.

## Что делает AC-503

AC-503 проверяет current canonical Arvectum OS state и отвечает на один практический вопрос:

> Нужна ли `WF-M5-001` какая-либо реальная OS reliance/admission для первого M5 proof, и если да — какая минимальная?

Допустимы три результата:

1. `no additional OS reliance required for first M5 proof`;
2. существующей bounded OS reliance достаточно;
3. нужен новый/изменённый OS Product Contract/capability admission через proper OS governance.

OS не должен внедряться ради dogfooding. Company-specific Position, customer и workflow semantics не переносятся в domain-neutral OS.

## Business-first portfolio order

При отсутствии более высокого `P0` обязательства default discretionary portfolio order остаётся:

`PORT-002 → PORT-001 → PORT-003/PORT-004 по named trigger → PORT-007 clarification-only → PORT-005/PORT-006 contain`.

Это не budget, funding allocation или постоянная engineering queue. AC-106 `P0…P3` hierarchy остаётся выше portfolio ranking.

## Граница Arvectum OS

Company-specific Positions, Assignments, authority, portfolio decisions, operating controls и M5 workflow governance принадлежат `arvectum/arvectum-company`.

Product implementation/status остаются в product repositories. Domain-neutral platform architecture, Product Contracts, RFC/ADR и Platform Capability lifecycle принадлежат `arvectum/arvectum-os`.

Никакой Arvectum OS dependency не выводится автоматически из AC-501/AC-502. Любая actual reliance проходит AC-503 и применимый OS governance path.

## Граница публичного репозитория

Этот репозиторий публичный. **Запрещено** размещать здесь secrets, reusable credentials, private keys, signatures, избыточные персональные данные, банковские/платёжные payloads, transaction exports, confidential exact cash balances, sensitive tax/accounting documents, непубличные customer/vendor/contract materials, privileged payment/fraud/incident/security details и chain-of-thought.

Для `WF-M5-001` здесь должны храниться только public-safe governance/evidence references и sanitized operating meaning. Raw customer evidence остаётся в соответствующем authorized contour.

## Удалённые репозитории

GitHub `arvectum/arvectum-company` — канонический remote.

GitVerse — зеркало для устойчивости и технологической суверенности. Наличие mirror не делает его самостоятельным источником Organizational Authority и не меняет canonical status автоматически.
