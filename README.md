# Arvectum Company

Канонический репозиторий долговременных документов управления, планирования, портфеля и организационной модели ООО «Арвектум» как компании, в которой значительная часть повторяемой работы выполняется ИИ и программными средствами, а конечный контроль сохраняется за собственником.

Arvectum Company — конкретная организация ООО «Арвектум». Это **не** Arvectum OS, не отдельный ИИ-агент и не универсальная программная платформа.

## С чего начать

- Конституция / внутренняя учредительная хартия Company: `docs/constitution/COMPANY-CONSTITUTION.md`
- Граница полномочий Company ↔ Arvectum OS: `docs/governance/COMPANY-OS-AUTHORITY-BOUNDARY.md`
- Реестр канонических источников: `docs/CANONICAL-SOURCES.md`
- Каноническая дорожная карта: `docs/roadmap/ROADMAP.md`
- Карта портфеля: `docs/portfolio/PORTFOLIO.md`
- Терминологический глоссарий: `docs/governance/TERMINOLOGY-GLOSSARY.md`
- Решение о языке и терминологии: `docs/governance/decisions/DECISION-2026-08-21-LANGUAGE-AND-TERMINOLOGY-POLICY.md`
- AC-201 — модель функций: `docs/organization/MINIMAL-REAL-ORGANIZATIONAL-FUNCTION-MODEL.md`
- AC-202 — решения, зарезервированные за собственником: `docs/governance/RESERVED-OWNER-DECISIONS-v1.0.0.md`
- AC-203 — модель делегирования полномочий: `docs/governance/DELEGATED-POSITION-AUTHORITY-MODEL-v1.0.0.md`
- AC-204 — начальный реестр организационных позиций: `docs/organization/INITIAL-POSITION-REGISTRY-v1.0.0.md`
- AC-205 — начальные назначения исполнителей: `docs/organization/INITIAL-ASSIGNMENTS-AND-EXECUTOR-CLASSIFICATION-v1.0.0.md`
- AC-206 — границы доступа: `docs/security/COMPANY-DATA-TOOL-CREDENTIAL-ACCESS-BOUNDARY-v1.0.0.md`
- AC-207 — непрерывность, замена и резервный порядок работы: `docs/operations/CRITICAL-FUNCTION-CONTINUITY-REPLACEMENT-FALLBACK-BASELINE-v1.0.0.md`
- AC-208 — граница переносимости эталонной модели и закрытие M2: `docs/organization/REFERENCE-MODEL-TRANSFERABILITY-AND-M2-CLOSURE-v1.0.0.md`
- AC-301 — идентичность, границы и владение портфелем: `docs/portfolio/AC-301-PORTFOLIO-IDENTITY-BOUNDARY-OWNERSHIP-RECONCILIATION-v1.0.0.md`
- AC-302 — ответственная организационная позиция: `docs/portfolio/AC-302-PORTFOLIO-ACCOUNTABLE-POSITION-MAPPING-v1.0.0.md`
- AC-303 — инвестиции, затраты и риски: `docs/portfolio/AC-303-PORTFOLIO-INVESTMENT-COST-RISK-BOUNDARIES-v1.0.0.md`
- AC-304 — роли standalone/reference/module/OS candidate: `docs/portfolio/AC-304-PORTFOLIO-ROLE-CLASSIFICATION-v1.0.0.md`
- AC-305 — межпродуктовые зависимости и Product Contracts Arvectum OS: `docs/portfolio/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-RECONCILIATION-v1.0.0.md`
- AC-306 — приоритизация по капиталу, экономике и вниманию собственника: `docs/portfolio/AC-306-PORTFOLIO-PRIORITIZATION-CAPITAL-ECONOMICS-OWNER-ATTENTION-v1.0.0.md`
- Материалы перекрёстных проверок: `docs/reviews/`
- Долговременные решения собственника и системы управления: `docs/governance/decisions/`

## Язык документов

Документы, предназначенные для чтения собственником и другими русскоязычными участниками управления, должны быть написаны на полноценном русском языке.

Английский язык допустим в коде, API, идентификаторах, именах файлов, технических схемах и документах для ИИ/программных исполнителей. Системообразующие термины при этом не переводятся свободно каждый раз, а связываются через `docs/governance/TERMINOLOGY-GLOSSARY.md`.

Принцип защиты от смыслового дрейфа:

```text
устойчивый идентификатор термина
+ канонический английский термин
+ утверждённый русский эквивалент
+ нормативное определение
```

## Текущее состояние Company

Этапы имеют следующий статус:

- `M0` — каноническое учреждение Company: `Complete / PASS`;
- `M1` — фиксация бизнес- и экономической реальности и плана первой рыночной проверки: `Complete / PASS`;
- `M2` — формирование эталонной организационной модели Company и системы полномочий: `Complete / PASS`;
- `M3` — управление портфелем продуктов и кандидатами в повторно используемые модули как инвестициями: `Current`.

Phase 3 на текущем каноническом состоянии:

```text
AC-301 identity/boundary/ownership            Complete / PASS
→ AC-302 accountable Position                 Complete / PASS
→ AC-303 investment/cost/risk boundaries      Complete / PASS
→ AC-304 portfolio role classification        Complete / PASS
→ AC-305 dependency/Product Contract map      Complete / PASS
→ AC-306 capital/economics/Owner priority     Complete / PASS
→ AC-307 final M3 review                      Current
```

Текущее каноническое действие:

**`AC-307 — Итоговая проверка управления портфелем и закрытие M3`.**

При отсутствии более высокого Company-level `P0` обязательства утверждённый AC-306 default discretionary product order: `PORT-002 → PORT-001 → PORT-003/PORT-004 по named trigger → PORT-007 clarification-only → PORT-005/PORT-006 contain`.

Этот порядок не является бюджетом, постоянной инженерной очередью или новым Company flagship. Общая приоритетная иерархия AC-106 `P0…P3` остаётся выше portfolio ranking.

Параллельный ограниченный цикл AC-108 по поиску и изучению потенциальных партнёров для совместной рыночной проверки продолжает действовать как источник рыночных данных. Сам по себе он не означает пилот, цену, SLA, привилегированный доступ или клиентское обязательство.

## Граница репозитория

Специфические для Arvectum Company правила управления, организационные позиции, назначения, портфельные решения и рабочие процессы принадлежат этому репозиторию, когда их допустимо хранить здесь.

Реализация конкретного продукта остаётся канонической в соответствующем продуктовом репозитории. Доменно-нейтральная архитектура и контракты платформы принадлежат `arvectum/arvectum-os`.

Этот репозиторий публичный. **Запрещено** размещать здесь секреты, повторно используемые учётные данные, избыточные персональные данные, подписи, банковские/платёжные реквизиты, непубличные клиентские/поставщицкие/договорные материалы и другие ограниченные операционные данные.

## Удалённые репозитории

GitHub `arvectum/arvectum-company` — канонический удалённый репозиторий.

GitVerse — зеркало для устойчивости и технологической суверенности. Наличие копии в GitVerse не делает её самостоятельным источником организационных полномочий и не меняет канонический статус автоматически.
