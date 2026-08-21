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
- AC-208 — граница переносимости эталонной модели и закрытие M2: `docs/organization/REFERENCE-MODEL-TRANSFERABILITY-AND-M2-CLOSURE-v1.0.0.md`
- AC-307 — итоговая проверка портфеля и закрытие M3: `docs/portfolio/AC-307-PORTFOLIO-GOVERNANCE-REVIEW-AND-M3-CLOSURE-v1.0.0.md`
- AC-401 — модель реестра работ и обязательств: `docs/operations/COMPANY-WORK-OBLIGATION-REGISTER-MODEL-v1.0.0.md`
- AC-402 — модель реестра решений, approvals и эскалаций: `docs/operations/COMPANY-DECISION-APPROVAL-ESCALATION-REGISTER-MODEL-v1.0.0.md`
- AC-403 — модель реестра рисков, исключений и инцидентов: `docs/operations/COMPANY-RISK-EXCEPTION-INCIDENT-REGISTER-MODEL-v1.0.0.md`
- Материалы перекрёстных проверок: `docs/reviews/`
- Долговременные решения собственника и системы управления: `docs/governance/decisions/`

## Язык документов

Документы, предназначенные для чтения собственником и другими русскоязычными участниками управления, должны быть написаны на полноценном русском языке.

Английский язык допустим в коде, API, идентификаторах, именах файлов, технических схемах и документах для ИИ/программных исполнителей. Системообразующие термины связываются через `docs/governance/TERMINOLOGY-GLOSSARY.md`.

## Текущее состояние Company

Этапы:

- `M0` — каноническое учреждение Company: `Complete / PASS`;
- `M1` — бизнес-/экономическая реальность и первая market-validation baseline: `Complete / PASS`;
- `M2` — эталонная организационная модель Company и система полномочий: `Complete / PASS`;
- `M3` — управление портфелем продуктов/кандидатов в модули как инвестициями: `Complete / PASS`;
- `M4` — Owner control and reference-implementation observability: `Current`.

M4:

```text
AC-401 work/obligation register model             Complete / PASS
→ AC-402 decision/approval/escalation register   Complete / PASS
→ AC-403 risk/exception/incident register        Complete / PASS
→ AC-404 cash/commitment/reporting baseline      Current
→ AC-405 portfolio/priority review cadence       Planned
→ AC-406 Owner Mission Control                    Planned
→ AC-407 management operating cadence            Planned
```

Текущее каноническое действие:

**`AC-404 — Cash, commitment and management reporting baseline` — базовая модель видимости денег, обязательств и управленческой отчётности.**

## Утверждённый M4 control baseline

AC-401 установил:

- `WORK-*` — material Company-level work;
- `OBL-*` — material obligation control.

AC-402 добавил:

- `DEC-*` — material decision case / durable decision record;
- `APR-*` — approval gate / attributable approval act control record;
- `ESC-*` — escalation case.

AC-403 добавил:

- `RSK-*` — material risk exposure/control record;
- `EXC-*` — material control-exception request/decision record;
- `INC-*` — material incident control record.

Ключевые правила:

`recommendation ≠ decision ≠ approval ≠ legal/corporate act ≠ technical authorization ≠ execution`

`risk evidence ≠ accepted risk`

`exception request ≠ approved exception`

`incident detection ≠ authority to act`

`containment ≠ risk acceptance`.

Company repository authoritative только для Company governance/control state в своём scope. Договоры, legal/corporate acts, customer facts, accounting/banking truth, product implementation/status, security tooling и Arvectum OS governance/platform state остаются в соответствующих authoritative contours.

Наличие cash, dashboard visibility, credential, technical access, `decision_outcome=approve`, incident state или AI recommendation само по себе не создаёт spend/external-effect authority.

## Business-first приоритет

При отсутствии более высокого `P0` обязательства default discretionary portfolio order остаётся: `PORT-002 → PORT-001 → PORT-003/PORT-004 по named trigger → PORT-007 clarification-only → PORT-005/PORT-006 contain`.

Этот порядок не является бюджетом, постоянной engineering queue или Company flagship. Общая иерархия AC-106 `P0…P3` остаётся выше portfolio ranking.

Параллельный bounded AC-108 discovery loop остаётся источником рыночных данных и сам по себе не означает pilot, price, SLA, privileged access или customer commitment.

## Граница репозитория

Специфические для Arvectum Company правила управления, organizational Positions, Assignments, portfolio decisions и Company-level control models принадлежат этому репозиторию, когда их допустимо хранить здесь.

Реализация конкретного продукта остаётся канонической в соответствующем продуктовом репозитории. Доменно-нейтральная архитектура, Product Contracts и platform governance принадлежат `arvectum/arvectum-os`.

Этот репозиторий публичный. **Запрещено** размещать здесь secrets, reusable credentials, private keys, signatures, избыточные персональные данные, банковские/платёжные payloads, непубличные клиентские/поставщицкие/договорные материалы, privileged incident/security details и другие ограниченные операционные данные.

## Удалённые репозитории

GitHub `arvectum/arvectum-company` — канонический удалённый репозиторий.

GitVerse — зеркало для устойчивости и технологической суверенности. Наличие копии в GitVerse не делает её самостоятельным источником организационных полномочий и не меняет канонический статус автоматически.