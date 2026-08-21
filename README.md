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
- AC-208 — граница переносимости эталонной модели и закрытие M2: `docs/organization/REFERENCE-MODEL-TRANSFERABILITY-AND-M2-CLOSURE-v1.0.0.md`
- AC-307 — итоговая проверка портфеля и закрытие M3: `docs/portfolio/AC-307-PORTFOLIO-GOVERNANCE-REVIEW-AND-M3-CLOSURE-v1.0.0.md`
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

Результат M3:

```text
AC-301 identity/boundary/ownership            Complete / PASS
→ AC-302 accountable Position                 Complete / PASS
→ AC-303 investment/cost/risk boundaries      Complete / PASS
→ AC-304 portfolio role classification        Complete / PASS
→ AC-305 dependency/Product Contract map      Complete / PASS
→ AC-306 capital/economics/Owner priority     Complete / PASS
→ AC-307 final M3 review                      Complete / PASS
```

Текущее каноническое действие:

**`AC-401 — Company work/obligation register model` — модель реестра работ и обязательств Компании.**

M4 нужен, чтобы собственник видел существенные работы, обязательства, решения, риски, cash/commitment signals и portfolio state без постоянного восстановления контекста из чатов и отдельных репозиториев. Software dashboard не является самоцелью и не требуется до тех пор, пока более простой control layer решает задачу надёжно.

Текущий approved portfolio baseline находится в `docs/portfolio/PORTFOLIO.md` `0.8.0`. При отсутствии более высокого `P0` обязательства default discretionary product order остаётся: `PORT-002 → PORT-001 → PORT-003/PORT-004 по named trigger → PORT-007 clarification-only → PORT-005/PORT-006 contain`.

Этот порядок не является бюджетом, постоянной engineering queue или Company flagship. Общая иерархия AC-106 `P0…P3` остаётся выше portfolio ranking.

Параллельный bounded AC-108 discovery loop остаётся источником рыночных данных и сам по себе не означает pilot, price, SLA, privileged access или customer commitment.

## Граница репозитория

Специфические для Arvectum Company правила управления, организационные позиции, назначения, портфельные решения и Company-level control models принадлежат этому репозиторию, когда их допустимо хранить здесь.

Реализация конкретного продукта остаётся канонической в соответствующем продуктовом репозитории. Доменно-нейтральная архитектура и контракты платформы принадлежат `arvectum/arvectum-os`.

Этот репозиторий публичный. **Запрещено** размещать здесь секреты, повторно используемые учётные данные, private keys, избыточные персональные данные, подписи, банковские/платёжные реквизиты, непубличные клиентские/поставщицкие/договорные материалы и другие ограниченные операционные данные.

## Удалённые репозитории

GitHub `arvectum/arvectum-company` — канонический удалённый репозиторий.

GitVerse — зеркало для устойчивости и технологической суверенности. Наличие копии в GitVerse не делает её самостоятельным источником организационных полномочий и не меняет канонический статус автоматически.