# AC-407 — Management Operating Cadence and M4 Control Review

Статус: `Approved`
Версия: `1.0.0`
Утверждено: `2026-08-21`
Опубликовано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-407 — Management operating cadence and control review`
Решение: `docs/governance/decisions/DECISION-2026-08-21-AC-407-APPROVAL-AND-M4-CLOSURE.md`
Cross-review: `docs/reviews/AC-407-MANAGEMENT-OPERATING-CADENCE-AND-M4-CONTROL-REVIEW.md`
Evidence snapshot: `docs/operations/OWNER-MISSION-CONTROL-REFERENCE-SNAPSHOT-2026-08-21.md`, blob `09b056e99ecb066402bc1d2b12d2dab772898f1b`
Approved proposal: `Proposed 0.9.0`, blob `87453d69314da217d3bd02f4645ac3f3444ed788`

## 1. Approval publication

Этот документ является канонической Approved publication AC-407 `1.0.0` и фиксирует закрытие M4 в exact approved scope.

Утверждённое собственником нормативное содержание — полная проверенная редакция:

`docs/operations/MANAGEMENT-OPERATING-CADENCE-AND-M4-CONTROL-REVIEW.md`

с immutable git blob SHA:

`87453d69314da217d3bd02f4645ac3f3444ed788`.

Proposal включён в эту publication целиком по immutable content reference. Настоящая publication не изменяет нормативное содержание проверенной редакции.

Явное решение собственника:

`docs/governance/decisions/DECISION-2026-08-21-AC-407-APPROVAL-AND-M4-CLOSURE.md`.

## 2. Approved operating cadence

AC-407 `1.0.0` устанавливает следующий initial Company operating cadence:

```text
material event
→ immediate bounded source/control update or review
→ Owner only if actual authority/action need exists

active operating week + material aggregate state
→ at most one short asynchronous Owner control checkpoint

monthly
→ one integrated management checkpoint
   (finance + portfolio exception scan + open material controls + burden check)

quarterly
→ integrated portfolio / continuity-gap / control-fit / Owner-burden revalidation
```

Mandatory daily standup, daily dashboard acknowledgement и routine Owner approval ceremony не вводятся.

## 3. Control-burden rule

После M4 действует принцип:

```text
routine bounded execution
→ existing approved envelope

material / reserved durable change
→ evidence + exact authority gate

boundary exceeded / material evidence unknown
→ escalate or fail closed
```

Полный proposal/cross-review/Owner-approval/publication цикл не является default process для routine `AM-1`/`AM-2` work.

## 4. Observed evidence and limits

M4 закрывается не только по design artifacts. Наблюдались:

- repeated AC-401…AC-406 governance execution traces с разделением AI-assisted preparation и explicit Owner approval;
- bounded repository publication/state synchronization после Owner act;
- read-after-write verification и immutable provenance;
- фактический stop-at-Owner-gate pattern;
- первая AC-406 public-safe Mission Control projection: `docs/operations/OWNER-MISSION-CONTROL-REFERENCE-SNAPSHOT-2026-08-21.md`, blob `09b056e99ecb066402bc1d2b12d2dab772898f1b`.

Этот evidence ограничен observed scope. Он не доказывает broad customer/commercial/finance/engineering autonomy или полную live Company observability.

## 5. M4 closure

`M4 — Owner control and reference-implementation observability established` получает статус:

`Complete / PASS`.

M4 closure означает, что Arvectum Company имеет coherent owner-control/reference-observability governance baseline и proportional operating cadence поверх AC-401…AC-407.

M4 closure не означает:

- полную live population Company registers;
- current cash/liquidity completeness;
- отсутствие рисков/инцидентов/обязательств;
- measured Owner-time reduction;
- доказанную broad AI workforce effectiveness;
- continuity/DR readiness;
- profitability, market validation, customer readiness, legal compliance или production readiness.

## 6. Software / Arvectum OS boundary

Новый standalone software Mission Control не требуется для закрытия M4.

Markdown/structured projection считается достаточным current implementation path до появления repeated-use evidence, показывающего конкретный burden/value case для UI/software.

Arvectum OS может позднее использоваться как domain-neutral presentation/composition substrate только через отдельный admitted boundary и применимый OS governance path. AC-407 не создаёт Product Contract, Active Platform Capability или Company-specific OS authority.

## 7. Carry-forward

Explicit future evidence targets включают:

- live control-record completeness through real work;
- current source-backed cash/commitment evidence at decision time;
- measured/repeated Owner-load reduction;
- continuity/replacement drills where justified;
- AI execution quality/cost/reliability and runtime replacement evidence;
- portfolio/customer/economic evidence;
- actual first governed Company operating contour in M5.

## 8. Cross-review and approval evidence

Cross-review:

- `docs/reviews/AC-407-MANAGEMENT-OPERATING-CADENCE-AND-M4-CONTROL-REVIEW.md`;
- iterations: `8`;
- result: `Complete / PASS for Owner approval and M4 closure`;
- immutable blob SHA: `6de916440b2d77957aed9ddde3eb0a47eba8a9b4`.

Approved proposal:

- `docs/operations/MANAGEMENT-OPERATING-CADENCE-AND-M4-CONTROL-REVIEW.md`;
- status/version: `Proposed 0.9.0`;
- immutable blob SHA: `87453d69314da217d3bd02f4645ac3f3444ed788`.

Owner approval:

- `docs/governance/decisions/DECISION-2026-08-21-AC-407-APPROVAL-AND-M4-CLOSURE.md` — `Approved`;
- explicit wording: `AC-407 и закрытие M4 утверждаю`.

## 9. Approval result and handoff

`AC-407 — Management operating cadence and control review` имеет статус `Complete / PASS`.

`M4 — Owner control and reference-implementation observability established` имеет статус `Complete / PASS`.

Следующее каноническое действие:

`AC-501 — First governed workflow candidate selection`.

AC-501 выбирает workflow по actual business/evidence criteria и не получает заранее назначенный продукт или process из AC-407.
