# AC-306 — Приоритизация портфеля по капиталу, экономике и вниманию собственника

Статус: `Proposed`
Версия: `0.9.0`
Создано: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Пункт дорожной карты: `AC-306 — Portfolio prioritization by capital, economics and Owner attention`
Предшествующий Company baseline: `AC-305 — Approved 1.0.0`
Статус утверждения: `Pending explicit Owner approval of the exact reviewed proposal`

## 1. Назначение

AC-306 ранжирует `PORT-001…PORT-007` как инвестиционный портфель, а не как очередь репозиториев.

Задача отвечает на вопрос:

> Когда несколько продуктовых узлов одновременно могут потребовать денег, инженерной работы и внимания собственника, какой тип работы имеет право вытеснить другой и при каких доказательствах?

AC-306 не подменяет общий Company priority model AC-106. Portfolio ranking подчинён уже утверждённой Company последовательности:

1. `P0` — реальные обязательства, cash и material risk;
2. `P1` — flagship market evidence + минимальная реальная operating model Arvectum Company;
3. `P2` — product/OS work, непосредственно связанная с revenue, obligation, evidence или blocker removal;
4. `P3` — speculative productization/module/platform expansion.

Следовательно, даже самый высокий portfolio node не получает права вытеснять реальное `P0` обязательство или автоматически становиться выше flagship discovery/Company operating-model work.

## 2. Evidence boundary

AC-306 использует только evidence, достаточное для **относительной** приоритизации. Он не выдумывает выручку, маржу, CAC, LTV, часы собственника, valuation или ROI там, где надёжных чисел нет.

Binding Company evidence:

- `AC-101` — flagship `«ИИ-компания под ключ»` является основной Company commercial direction; существующие продукты являются отдельными business lines/reference implementations/module evidence, но не центром Company по умолчанию;
- `AC-102` — client automation/custom development является near-term cash/revenue line; product economics должны различать recurring burden, direct cost и Owner time;
- `AC-103` — bespoke client automation является наиболее доказанным текущим end-to-end customer value stream; controlled-pilot conversion и standalone acquisition lifecycle доказаны слабее;
- `AC-104` — Owner attention является реальным ограниченным ресурсом; ключевые bottlenecks — interpretation, priority switching, customer context, exception handling, local gates и state reconstruction;
- `AC-106` — approved Company priority bands `P0…P3` и правило `aggressive in learning; conservative in commitment`;
- `AC-301…AC-305` — current identities, dispositions, accountable Position, investment treatments, role/reuse classification и dependency/Product Contract boundaries.

Product-state evidence re-checked on current `main`:

| Node | Current evidence used | Decision-relevant interpretation |
|---|---|---|
| `PORT-001` | `arvectum/tender-agent/STATUS.md` blob `8f9c3cfdb8e893d46d0898e252ecb2f86e5c5f2b` | R0 functionally closed; bounded tender intake/analysis/export exists; next work is quality/evidence, while mass external pilot is not authorized |
| `PORT-002` | `arvectum/discount-parser/README.md` blob `7580d8112918c0be3381ff0073b7a481fa388434` | real client/product delivery contour; R1–R8 done, R9 code/distribution implemented; live acceptance remains environment/customer dependent |
| `PORT-003` | `arvectum/proxy-launcher/docs/ROADMAP.md` blob `c64273dd4f53565908e28b5b55c1fb1c01a4798d` | highly productized Windows baseline; several remaining gates are human/legal or separate-host dependent; speculative per-app growth has explicit stop-gates |
| `PORT-004` | `arvectum/creative-test-agent/README.md` blob `faf29045cbe57f46579743ca3d8b87995dc0e808` and `docs/roadmap/CURRENT.md` blob `9874e73f83adf2038cf10c2b2dfecd9e9d4648c7` | substantial pilot/product foundation exists; customer/design-partner evidence remains the limiting business input; roadmap pointer itself needs product-side freshness discipline |
| `PORT-005` | `arvectum/tender-app/README.md` blob `5065e0e1673da12b60128f7972efa6286938e034` | functioning procurement experiment/reference source, already contained by AC-301/303; no independent growth case is established |
| `PORT-006` | `arvectum/doors_parser/README.md` blob `69c6d037f5812d9a1ae225c2b4ab46f6d8713f53` | mature completed client-delivery evidence; useful extraction/QA reference, but no current growth mandate |
| `PORT-007` | `arvectum/data-platform/README.md` blob `6d6a0afe1f4437c383626bad42355077d76d986e` | repository remains bootstrap-level; consumer/economic/contract boundary is not established |

Where product/customer/accounting evidence changes materially, ranking must be refreshed rather than defended from stale documentation.

## 3. Prioritization dimensions

AC-306 does not use a fabricated weighted score. Each node is assessed qualitatively through seven decision dimensions.

### D1 — Obligation / cash protection

Does delaying the node threaten an existing customer obligation, acceptance, support commitment, cash collection, material continuity or reputational exposure?

This dimension can temporarily override the normal portfolio band.

### D2 — Near-term client / revenue / value path

Is there a concrete bounded path from the next work to a real customer outcome, paid work, qualified pilot, procurement margin or evidence that can support a commercial decision?

### D3 — Evidence quality

Is the next investment supported by real customer/product evidence, or mainly by technical possibility, repository momentum and architectural preference?

### D4 — Incremental cost and Owner-attention burden

How much new cash, recurring burden, local execution, exception handling, context switching and Owner gating does the next step create?

### D5 — Downside / reversibility

Can the work be stopped cheaply without creating customer, legal, IP, data, security, support or dependency liabilities?

### D6 — Strategic/reuse leverage

Does the next bounded step improve the flagship method, real Company operation, reusable module evidence or validated Arvectum OS consumption without forcing premature generalization?

### D7 — External/blocking dependency

Is progress waiting on customer data, physical host, legal instrument, credential, vendor or another named gate? Blocked work does not deserve continuous Owner attention merely because the technical backlog exists.

## 4. Approved-proposal priority bands

### `A — Active bounded investment / attention`

Nodes in Band A may receive planned discretionary product attention inside AC-303 limits because a credible near-term obligation/revenue/evidence path exists.

Band A is not unlimited funding and does not override `P0/P1` Company sequencing.

#### `A1 — PORT-002 — Discount Parser`

**Recommendation:** `finish / accept / stabilize / maintain`, not open-ended expansion.

Why:

- bespoke client automation is the strongest currently evidenced Company value stream;
- Discount Parser has a real client/product delivery contour rather than only a demo hypothesis;
- most productization work already exists, so the highest-value next effort is closing real acceptance/feedback gaps and preventing an unbounded correction loop;
- customer validation creates direct learning on scope, source-specific extraction, packaging and support economics;
- AC-303 already says `continue accepted client/product contour` and requires review for material recurring-cost/platformization expansion.

Capital/attention rule:

- allow bounded work required for customer acceptance, defect correction, delivery continuity and clearly agreed support;
- classify new requests as defect / incomplete input / environment / changed expectation / new scope before implementing them;
- after accepted delivery, default to maintenance/freeze unless a new paid requirement, second-consumer evidence or explicit product investment case appears;
- do not use the current customer as implicit authorization for generic parser platformization.

**Primary exit evidence:** accepted usable delivery + bounded support/change boundary + captured reuse evidence.

#### `A2 — PORT-001 — Arvectum Tender Agent`

**Recommendation:** `continue as bounded revenue/market-evidence product`, not broad feature accumulation.

Why:

- Tender Agent is functionally closed at R0 and already supplies a real controlled procurement workflow;
- procurement remains a real Company revenue/domain line and the product can create both direct commercial evidence and reusable organizational-function evidence;
- the current repository explicitly says the next stage should focus on extraction quality, analysis quality, report structure and evidence coverage, not mass external pilot expansion;
- its current OS Product Contract contours create strategic validation value without making Arvectum OS mandatory for the whole product.

Capital/attention rule:

- invest when the next work is tied to a specific qualified pilot, procurement opportunity, measurable analysis-quality gap or flagship discovery hypothesis;
- prefer evidence-producing quality/reliability work over speculative modules, autonomous external actions or feature breadth;
- no mass pilot, SaaS expansion, submission/EDS automation or customer-wide operational commitment by implication.

**Primary exit evidence:** a real bounded paid/pilot/deal workflow that proves customer value and implementation/support burden, or evidence strong enough to change/stop the current hypothesis.

### `B — Conditional / trigger-based investment`

Band B nodes should remain healthy and decision-ready, but should not consume continuous discretionary Owner attention while their named business/external trigger is absent.

#### `B1 — PORT-003 — Arvectum Proxy Launcher`

**Recommendation:** `preserve productized baseline; close only high-leverage gates; do not chase blocked/sp speculative work`.

Why:

- Windows `0.2.3` is already a strong verified productization baseline with Russian-first signing evidence;
- several remaining tasks are waiting on a legal rights-basis action or a separate eligible physical host;
- the standalone acquisition/purchase/renewal lifecycle is not yet established at Company level;
- per-application routing has an explicit external signing/enforcement stop-gate and can create disproportionate Owner/dependency cost before demand is proven.

Capital/attention rule:

- support real users/customer defects and preserve the proven baseline;
- complete the author→ООО rights-basis step when the competent legal/corporate action is ready because it unlocks the clean IP/refactor path;
- do not repeatedly spend Owner time on APL-WIN-014/APL-REL-014 until the required separate host exists;
- do not fund per-app enforcement/platform expansion without concrete user/commercial evidence and explicit dependency decision.

**Promotion trigger to Band A:** credible near-term paid demand/obligation or a material release/IP issue whose closure unlocks such demand.

#### `B2 — PORT-004 — Creative Test Agent`

**Recommendation:** `maintain pilot readiness; activate on real design-partner/customer evidence`.

Why:

- the product has substantial controlled-pilot, local-first, reporting, evaluation and deployment foundation;
- AC-103 recognizes its pilot mechanics as stronger than an unstructured demo but does not establish recurring conversion;
- customer-specific inputs/design-partner evidence are the business constraint; more internal feature work cannot substitute for them;
- it is also useful as an external Arvectum OS consumer, but reference value alone is not a funding claim.

Capital/attention rule:

- preserve a runnable demo/pilot baseline and correct product-side status documentation when needed;
- when a qualified design partner/customer supplies real inputs and success criteria, temporarily elevate the bounded pilot work;
- without such evidence, avoid new speculative scoring, model, deployment or platform breadth merely to increase repository completeness.

**Promotion trigger to Band A:** qualified customer/design-partner with real data/input boundary, success criteria and a plausible commercial or flagship-learning outcome.

### `C — Clarification-only; no material build`

#### `C1 — PORT-007 — Data Platform`

**Recommendation:** `clarify, then decide; do not build yet`.

Why:

- AC-304 admits only a `clarification-only` Company/product-family data acquisition/extraction module hypothesis;
- the repository itself still supplies essentially no product/consumer/economic evidence;
- no hard product dependency currently relies on it;
- premature implementation would create exactly the shared-layer/Owner-attention risk AC-303/304/305 were designed to prevent.

Allowed work before a later change decision:

- identify named prospective consumers;
- write the smallest common contract sketch;
- distinguish source acquisition/extraction/provenance/quality hooks from product-owned domain semantics;
- estimate migration/support/operating burden from existing parser evidence;
- verify rights/data/sovereignty/continuity/replacement boundary;
- state what duplicated cost or measurable delivery burden the module would remove.

No production shared datastore, generic crawler platform, data lake, vector/search platform or compulsory cross-product runtime dependency is authorized.

**Promotion trigger:** concrete multi-consumer need + common contract + economic/continuity case strong enough for a separate change/investment decision.

### `D — Contain / reactive support / evidence preservation`

#### `D1 — PORT-005 — Tender Small-Volume Calculator`

**Recommendation:** `contain`.

- preserve code/history and selective procurement-family reference evidence;
- perform only necessary maintenance/security/continuity work;
- do not create a parallel growth procurement product while Tender Agent already carries the active bounded procurement product hypothesis;
- reuse only through explicit product-side review; no silent shared library or merge.

A real customer obligation may temporarily raise specific work to `P0`, but it does not silently change the portfolio disposition.

#### `D2 — PORT-006 — Doors Parser`

**Recommendation:** `contain completed-delivery asset`.

- preserve client support obligations, delivery evidence and extraction/QA lessons;
- correct a real customer defect when owed;
- otherwise avoid new product growth, broad source expansion or generic-parser rewrite;
- harvest reusable evidence only when it reduces the cost/risk of an actual current consumer.

A real support/customer obligation may temporarily raise specific work to `P0`; after resolution the node returns to contained treatment unless an explicit change decision is approved.

## 5. Relative portfolio order

The default discretionary order, when no `P0` exception exists, is:

```text
A1  PORT-002 Discount Parser
A2  PORT-001 Tender Agent
    ↓
B1  PORT-003 Proxy Launcher     ┐
B2  PORT-004 Creative Test Agent├─ execute only on named trigger
    ↓                           ┘
C1  PORT-007 Data Platform — clarification only
    ↓
D1  PORT-005 Tender Small-Volume Calculator
D2  PORT-006 Doors Parser
```

This is a **decision order, not a permanent engineering queue**.

A named event can temporarily override it:

- existing customer defect/acceptance obligation → `P0` regardless of node band;
- material security/data/continuity defect → `P0`;
- qualified paid/design-partner trigger for a Band B node → re-evaluate/elevate the bounded slice;
- absence of the trigger → do not keep engineering merely to stay busy.

## 6. Owner-attention allocation rule

Owner attention is treated as scarce management capital.

The portfolio should therefore minimize concurrent discretionary context switching.

For any material product work, POS-003 decision preparation should make explicit:

1. **why now** — obligation, revenue, evidence or blocker;
2. **what exact bounded outcome** is expected;
3. **what Owner action is actually needed** — reserved decision, judgment, local gate or merely execution;
4. **what can be prepared/executed without Owner involvement**;
5. **what stops the work** if evidence is poor;
6. **what next decision the evidence will enable**.

Owner attention should not be consumed by:

- repeated retries against a known unavailable physical/external gate;
- low-risk roadmap/document synchronization that can be prepared automatically;
- speculative product polish without customer/economic hypothesis;
- reviewing raw test output when a bounded evidence summary can be prepared;
- simultaneous feature expansion across several repositories without a ranked business reason.

## 7. Capital and recurring-cost rule

AC-306 creates no budget and no numeric spend threshold.

Recommended investment posture:

| Band | Discretionary posture |
|---|---|
| `A` | bounded spend/effort may be proposed when directly tied to obligation/revenue/evidence; material exposure still requires applicable Owner gate |
| `B` | preserve baseline; new material spend waits for named commercial/customer/legal/host trigger |
| `C` | discovery/analysis/contract sketch only; no material implementation or recurring infrastructure commitment |
| `D` | no discretionary growth investment; only obligation/security/continuity/support and evidence preservation |

Unknown cost is not zero. Before a material external dependency, paid service, recurring infrastructure, contractor, signing path or customer commitment is accepted, decision evidence must expose cost class, replacement path, downside and authority.

## 8. Portfolio stop/change signals

### Continue in current band

Continue when the next step produces customer/revenue/learning/continuity evidence at proportionate cost and does not widen risk/commitment silently.

### Change / re-band

Prepare a new decision when:

- a real customer/design-partner/contract creates materially stronger demand evidence;
- recurring support or integration burden is materially worse than expected;
- another product/module proves the same job more cheaply;
- legal/IP/data/sovereignty evidence changes the viable distribution/operation path;
- a contained node gains a genuinely independent commercial case;
- PORT-007 proves concrete multi-consumer economics or fails to do so;
- Owner-attention burden becomes the dominant cost despite technical automation.

### Stop / retire candidate

A stop/retire proposal becomes reasonable when a node has no current obligation, no credible customer/revenue path, no strategic/reuse evidence worth preserving beyond archive, and continuing support/investment creates net burden. Final stop remains a competent `ROD-04` decision; AC-306 does not retire any current node automatically.

## 9. Flagship and Arvectum OS boundary

This ranking does not redefine the Company flagship.

`«ИИ-компания под ключ»` remains the flagship commercial direction. Portfolio products earn attention when they:

- protect current revenue/obligations;
- generate real market/customer evidence;
- provide a bounded functional module/reference proof;
- remove a blocker for the flagship/internal reference operating model;
- or have a credible standalone economic case.

Arvectum OS is not included as `PORT-*` and is not ranked here as an ordinary product. OS investment follows its own canonical roadmap/governance and Company-level business priority. Product OS reference-consumer status does not justify platform work beyond the exact Product Contract/evidence need.

## 10. Authority and non-effects

AC-306 is a portfolio recommendation requiring explicit Owner approval because it concerns `ROD-02` capital allocation posture and `ROD-04` major portfolio/investment prioritization.

Approval would establish the Company-level default ranking and re-evaluation rules only.

It would not:

- authorize a concrete expenditure, contract, hiring action, price, discount or SLA;
- authorize a production/customer deployment;
- change legal/IP/data rights;
- create or modify an Arvectum OS Product Contract or capability lifecycle;
- change AC-301 identity/disposition automatically;
- create a shared module or cross-product runtime dependency;
- rewrite product roadmaps;
- approve a customer obligation not already validly created;
- convert an AI recommendation into Owner approval of a material external action.

Specific material decisions still use the applicable authority/evidence path.

## 11. Handoff

If this exact reviewed proposal is approved and published, AC-306 becomes `Complete / PASS` and the next canonical Company action is:

`AC-307 — Итоговая проверка управления портфелем и закрытие M3`.

AC-307 should verify that AC-301…AC-306 form one coherent portfolio-governance baseline and that no unresolved identity/accountability/investment/reuse/dependency/priority contradiction blocks M3 closure.