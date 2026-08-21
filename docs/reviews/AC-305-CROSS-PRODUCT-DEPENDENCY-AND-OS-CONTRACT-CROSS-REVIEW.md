# AC-305 — Перекрёстная проверка межпродуктовых зависимостей и Product Contract boundaries

Статус: `Complete / PASS for dual Owner approval`
Дата проверки: `2026-08-21`
Итераций выполнено: `7 of maximum 7`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-305 — Inter-product dependency and Arvectum OS Product Contract reconciliation`

Проверенный Company proposal:

- `docs/portfolio/AC-305-CROSS-PRODUCT-DEPENDENCY-AND-OS-CONTRACT-RECONCILIATION.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `c27973c48b7bb5306e36f71d0f1007fc41896de9`.

Проверенный Arvectum OS proposal:

- repository: `arvectum/arvectum-os`;
- `docs/contracts/P6-02-REPOSITORY-LOCATOR-RECONCILIATION-PROPOSAL.md`;
- статус: `Proposed 0.9.0`;
- immutable git blob SHA: `95f32a2625a3df2c18615021aa2ca46f83faa946`.

Статус утверждения: `Pending explicit Owner approval in both Company and Arvectum OS governance scopes`.

## 1. Review gate

AC-305 должен быть отклонён, если он:

- создаёт product dependency из одного лишь similarity/reference evidence;
- считает repository name Product Identity;
- превращает OS Product Contract в обязательность Arvectum OS для всего продукта без evidence;
- неверно приписывает продукту CAP dependency;
- чинит P6.02 Company-side записью, игнорируя Arvectum OS authority;
- переписывает исторический P6.02 `0.1.0` без сохранения lineage;
- создаёт скрытый Product Contract version bump/cascade без semantic reason;
- превращает PORT-007 в работающий shared module до clarification gate;
- допускает private import/table/stream/shared-state coupling;
- создаёт budget, priority, authority, data/IP transfer или customer commitment;
- преждевременно выполняет AC-306.

## 2. Итерация 1 — source-of-truth и authority domains должны остаться раздельными

**Критика.** AC-305 одновременно касается Company portfolio, product repositories и Arvectum OS Product Contracts. Самая опасная ошибка — позволить Company документу переписать OS contract либо OS contract переопределить Company product identity.

**Сверка.** Proposal разделяет authority:

- Company governance определяет `PORT-*`, Company-level repository locator/portfolio relation;
- product repo определяет implementation/status/domain semantics;
- Arvectum OS определяет Product Contract/capability semantics;
- legal/IP/data/customer rights остаются во внешних применимых authorities.

P6.02 locator correction вынесена в отдельный `arvectum/arvectum-os` proposal и прямо требует отдельного OS Owner approval.

**Результат:** PASS.

## 3. Итерация 2 — reference/reuse не должен превращаться в runtime dependency

**Критика.** AC-304 намеренно дал несколько reference roles. Без строгой типологии AC-305 мог бы объявить эти связи текущими техническими обязательствами.

**Сверка.** Введены отдельные labels `HARD_RUNTIME`, `DECLARED_OS_BOUNDARY`, `OPTIONAL_OS_EXTENSION`, `REFERENCE_REUSE`, `FAMILY_EVIDENCE`, `HYPOTHESIS_ONLY`, `NONE_EVIDENCED`.

Доказанный reuse `PORT-005 → PORT-001` соответствует `tender_app_reuse_audit.md`: перенесены идеи/patterns, а не монолитный код. Product manifests Tender Agent/Tender App не объявляют друг друга package dependency.

Discount Parser и Doors Parser классифицированы как `FAMILY_EVIDENCE`; Data Platform остаётся `HYPOTHESIS_ONLY`, поскольку его current repository фактически bootstrap-only и shared runtime contract отсутствует.

**Результат:** PASS.

## 4. Итерация 3 — P6.02 locator repair не должен создавать второй Tender product или переписывать Product Contract history

**Критика.** P6.02 содержит `arutyunoveth/ai-corporation`, Company AC-301 утверждает `arvectum/tender-agent`. Возможны две неправильные крайности: объявить это двумя продуктами либо заменить строку в историческом P6.02 и потерять provenance.

**Сверка.** Company proposal связывает разные namespaces без их слияния:

- Company identity: `PORT-001 — Arvectum Tender Agent`;
- current implementation locator: `arvectum/tender-agent`;
- historical implementation locator: `arutyunoveth/ai-corporation`;
- OS Product identity: `product/arvectum-tender-operator@<organization>`.

Current Tender Agent repo сохраняет явную implementation lineage: `pyproject.toml` всё ещё использует package name `ai-corporation`, а README описывает тот же bounded tender-operator contour.

OS proposal не мутирует P6.02 `0.1.0`; он создаёт отдельный governed resolver/provenance overlay. Product Contract subject/version/dependencies остаются неизменными.

**Результат:** PASS.

## 5. Итерация 4 — exact CAP dependency matrix должна совпадать с текущими OS contracts

**Критика.** Предыдущие сводки легко перепутать: разные real-product contracts используют разные CAP surfaces. Ошибка здесь создаст несуществующую platform obligation.

**Сверка по current `arvectum/arvectum-os/main`:**

- P6.02 Tender Operator: `CAP-001 + CAP-004`;
- P8.03 Tender Operator EIS revalidation: `CAP-001 + CAP-004`;
- P6.06 Discount Parser: **`CAP-004 only`**, CAP-001/002/003 explicitly omitted;
- P8.06 Creative Test Agent: **`CAP-004 only`**.

Proposal отражает именно эту матрицу и отдельно фиксирует, что никакой reviewed current real-product/external-consumer boundary не требует CAP-002 или CAP-003.

OS roadmap `2.76.0` сохраняет P6.02/P6.06/P8.03/P8.06 как Provisional и CAP-001…CAP-004 как Incubating/Provisional.

**Результат:** PASS.

## 6. Итерация 5 — Product Contract existence не равен mandatory core-product dependency

**Критика.** AC-304 `RI-OS-CONSUMER` можно ошибочно прочитать как “продукт не работает без OS”. Особенно опасно это для Creative Test Agent.

**Сверка.** P8.06 прямо определяет optional external extension. Product-side `integrations/arvectum_os_p8_06_onboarding.json` подтверждает `enabled_by_default: false`, read-only operation, no canonical mutation, no internal table/import/private stream/undocumented endpoint reliance и самостоятельную работу core product без extension.

P6.02/P6.06 также остаются bounded governed contours, а не product-wide Stable dependency promises. Proposal использует `DECLARED_OS_BOUNDARY` вместо `HARD_RUNTIME`.

**Результат:** PASS.

## 7. Итерация 6 — anti-platform-gravity и hidden coupling

**Критика.** Parser similarities, Company ownership и новый Productive Workspace Arvectum OS создают давление заранее связать все продукты через shared library/data store/OS internals.

**Сверка.** Proposal сохраняет:

- PORT-007 как clarification-only Company module hypothesis;
- отсутствие Product Contract у PORT-003/005/006/007;
- отсутствие admitted shared datastore/library/service между PORT nodes;
- RFC-0001/RFC-0004 prohibition on product-to-product internals and hidden platform coupling;
- product-owned domain semantics у Tender Agent, Discount Parser и Creative Test Agent.

Inspected manifests Tender Agent, Discount Parser, Creative Test Agent, Tender App и Doors Parser не объявляют direct package dependency на другой portfolio repository. Data Platform не имеет application manifest. Proxy Launcher документирован как independently packaged local product; Company hard dependency на него не установлена.

Proposal осторожно не утверждает, что ни одно исходное упоминание другого проекта физически невозможно; он утверждает только отсутствие evidence для canonical hard runtime obligation.

**Результат:** PASS.

## 8. Итерация 7 — locator overlay должен быть минимальным, а handoff в AC-306 чистым

**Критика.** Даже правильный P6.02 repair может вызвать ненужный version cascade либо скрыто выполнить AC-306/создать authority effects.

**Сверка.** OS proposal ограничен repository-locator/provenance semantics:

- P6.02 Product Contract `0.1.0` остаётся неизменным;
- P8.03 продолжает ссылаться на тот же P6.02 boundary;
- ни dependency set, operation set, authority/data scope, compatibility line, lifecycle, support или customer commitment не меняются;
- при будущем semantic boundary change новый Product Contract version остаётся обязательным.

Company proposal отдельно запрещает budget/priority/authority/data/IP/customer effects и оставляет relative capital/economics/Owner-attention ranking для AC-306.

Полное закрытие AC-305 требует **двух явных Owner approvals**: Company proposal + OS locator proposal. Это предотвращает hidden cross-repository commitment.

**Результат:** PASS.

## 9. Acceptance matrix

| Проверка | Результат |
|---|---|
| `PORT-001…PORT-007` покрыты | PASS |
| Company/Product/OS authority scopes разделены | PASS |
| runtime vs reference vs hypothesis разделены | PASS |
| Tender App reuse не назван runtime dependency | PASS |
| parser-family evidence не назван shared implementation | PASS |
| Data Platform остаётся clarification-only | PASS |
| Proxy Launcher не создан как hidden infra dependency | PASS |
| Creative Test Agent не получает cross-product dependency | PASS |
| P6.02 CAP-001/CAP-004 точно отражены | PASS |
| P8.03 CAP-001/CAP-004 точно отражены | PASS |
| P6.06 CAP-004-only точно отражён | PASS |
| P8.06 CAP-004-only точно отражён | PASS |
| CAP-002/CAP-003 не приписаны текущим reviewed product contours | PASS |
| P6.02 stale locator выявлен | PASS |
| current `arvectum/tender-agent` locator закреплён proposal'ом | PASS |
| historical `arutyunoveth/ai-corporation` lineage сохранён | PASS |
| Company doc не переписывает OS contract | PASS |
| OS proposal не создаёт второй Product Identity | PASS |
| P6.02 semantic boundary не меняется | PASS |
| P8.03 version cascade не создаётся без причины | PASS |
| P8.06 optional/disabled-by-default semantics сохранены | PASS |
| hidden product-package coupling не выявлен как canonical obligation | PASS |
| private OS coupling запрещён | PASS |
| Product Contract possession ≠ Authorization/Authority | PASS |
| новые Product Contracts не созданы по аналогии | PASS |
| новые OS capabilities не созданы | PASS |
| budget/priority не утверждены | PASS |
| legal/IP/data rights не изменены | PASS |
| customer commitments не расширены | PASS |
| AC-306 не выполнен заранее | PASS |
| dual-approval boundary явный | PASS |

## 10. Review conclusion

`7 of maximum 7` итераций завершены.

Итог:

**PASS for dual Owner approval.**

Материальных нерешённых возражений к exact Company proposal blob `c27973c48b7bb5306e36f71d0f1007fc41896de9` и exact Arvectum OS locator proposal blob `95f32a2625a3df2c18615021aa2ca46f83faa946` не осталось.

До явного утверждения:

- AC-305 не является `Complete`;
- Company `PORTFOLIO.md` не меняется;
- Company `ROADMAP.md` не переводится на AC-306;
- OS locator proposal не становится каноническим approved reconciliation record;
- P6.02 остаётся читаемым только с известным stale locator defect.

Рекомендуемая явная формулировка Owner approval:

`AC-305 и P6.02 repository locator reconciliation в Arvectum OS утверждаю.`