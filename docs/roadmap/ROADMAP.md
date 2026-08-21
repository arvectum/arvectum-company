# Каноническая дорожная карта Arvectum Company

Статус: `Active`
Версия: `0.40.0`
Создано: `2026-08-19`
Обновлено: `2026-08-21`
Владелец: `ООО «Арвектум»`
Репозиторий: `arvectum/arvectum-company`
Текущее каноническое действие: `AC-505 — Supervised real-operation proof`
Русское название текущего действия: `Первый реальный контролируемый прогон WF-M5-001 на клиентском feedback case`

## 1. Модель публикации

Эта редакция `0.40.0` сохраняет полное содержание дорожной карты `0.39.0` по immutable git blob и добавляет завершение AC-504 и переход к AC-505.

Предыдущая редакция:

- версия: `0.39.0`;
- путь: `docs/roadmap/ROADMAP.md`;
- immutable git blob SHA: `5e7cc89eb384ea0fc1cf6cb74cf30d0e55338d33`.

Все ранее определённые M0–M9, Company priority hierarchy, Company/Product/Arvectum OS boundaries, bounded AC-108 evidence loop, AC-501 workflow selection, AC-502 workflow contract, AC-503 no-additional-OS-reliance decision и конечный AC-901 сохраняются, если прямо не изменены более новым approved decision.

## 2. Закрытие AC-504

`AC-504 — Bounded workflow implementation` имеет статус:

`Complete / PASS`.

Implementation evidence:

- `docs/operations/AC-504-BOUNDED-WORKFLOW-IMPLEMENTATION-EVIDENCE.md` — `Complete / PASS 1.0.0`, blob `ad3855fc08448dbb190b1d486f255e5592f59d71`;
- implementation payload head: `8aa82ccfe49001063e8416c21bf673bfa3941b26`;
- cross-review: `docs/reviews/AC-504-BOUNDED-WORKFLOW-IMPLEMENTATION-CROSS-REVIEW.md` — `10 of 10`, `PASS for AC-505 transition`, blob `f18251a813a002fdeb2e1c7d066ec5c9c34287f4`.

Implementation artifacts:

- `tools/wf_m5_001_case.py` — blob `19373811e761226c3e418fa1b8086828c9caded6`;
- `tests/test_wf_m5_001_case.py` — blob `14e20464fd2aea2d0b85c5b286950ae7ac55f86a`;
- `.github/workflows/wf-m5-001-case.yml` — blob `f09e3969cb4e56cdc8cc59917439bb4ee32d493e`;
- `docs/operations/WF-M5-001-BOUNDED-IMPLEMENTATION-RUNBOOK.md` — blob `c51b522d66ce80ca4e2e46e5494fa32c3301ee27`;
- `docs/operations/WF-M5-001-CASE-TEMPLATE.json` — blob `b66fc43e1fa47e13c5f251588324a7a813bfd9fa`;
- `.gitignore` excludes `.local/` real-case storage from Git.

Executed local-equivalent test evidence:

`7 tests / 7 PASS / 0 failures / 0 errors`.

No remote GitHub Actions run is claimed as the evidence for AC-504.

## 3. What AC-504 established

For one supervised `WF-M5-001` case the Company now has a minimal OS-neutral mechanism that can:

- pin exact AC-502/AC-503 governance versions and the exact product baseline used;
- create a safe case identifier and local non-git case record;
- represent material `W0…W11` state history and `CL-1…CL-7` classification evidence;
- enforce attributable POS-002 Company/customer gates and POS-004 technical gates;
- reject `AM-3/AM-4` in this contour;
- admit only unambiguous `CL-1` into the ordinary technical correction path;
- require test + candidate provenance before `W7 — Candidate Ready`;
- preserve `Candidate Ready ≠ customer handoff ≠ customer acceptance`;
- require explicit customer validation reference before `W10`;
- represent `blocked / unknown / stale / uncertain` explicitly;
- link product/customer/control evidence without copying authoritative raw payloads;
- fall back to a manual case template if the helper/runtime is unavailable.

The helper performs no customer send, deploy, payment, signing, commitment or acceptance act.

## 4. Status milestones

- `M0` — `Complete / PASS`;
- `M1` — `Complete / PASS`;
- `M2` — `Complete / PASS`;
- `M3` — `Complete / PASS`;
- `M4` — `Complete / PASS`;
- `M5 — First real governed Company operating contour proven` — `Current`;
- `M6 — First real AI-held Position proven economically and operationally` — `Planned`;
- `M7` — `Future`;
- `M8` — `Future`;
- `M9` — final planned human-readable Russian reconciliation stage after M8 unless Owner changes sequence.

## 5. Phase 5 — First governed Company operating contour

| ID | Работа | Статус |
|---|---|---|
| `AC-501` | First governed workflow candidate selection | `Complete / PASS` |
| `AC-502` | Workflow, accountable Position, authority/data/evidence contract | `Complete / PASS` |
| `AC-503` | Arvectum OS reliance/admission mapping where applicable | `Complete / PASS` |
| `AC-504` | Bounded workflow implementation | `Complete / PASS` |
| `AC-505` | Supervised real-operation proof | `Current` |
| `AC-506` | Incident, uncertain-outcome, recovery and fallback drill | `Planned` |
| `AC-507` | Business-value/economic review and continue/change/stop decision | `Planned` |

## 6. Текущее действие — AC-505

### AC-505 — Supervised real-operation proof

Статус: `Current`.

Цель AC-505 — провести **один фактический supervised case** через максимально возможную часть `WF-M5-001` на реальном customer feedback для `PORT-002 — Discount Parser`, сохранив approved authority/customer/data boundaries и измерив фактическую полезность/трение implementation.

AC-505 не является демонстрационным прогоном на выдуманных данных. Его evidence должен происходить из реального customer/workstream source и реальной product execution history.

Минимальный scope:

1. выбрать один актуальный реальный feedback item или малый coherent batch, по которому допустим supervised workflow proof;
2. открыть case через AC-504 implementation с exact product baseline и protected customer-source reference;
3. POS-002 human Principal должен выполнить/подтвердить initial classification и, если это `CL-1`, bounded correction admission;
4. POS-004 может выполнить bounded technical correction/verification в `arvectum/discount-parser` внутри existing Assignment/access/AM ceilings;
5. сохранить product issue/PR/commit/test/build/release-candidate evidence references;
6. остановиться fail-closed при new scope, ambiguous contract/customer rights, missing evidence/access, security/material risk или иной applicable escalation trigger;
7. customer-facing handoff выполняется только существующим authorized human/process path и затем фиксируется ссылкой;
8. customer validation/acceptance/rejection/change evidence должно быть explicit и attributable; silence не закрывает case;
9. зафиксировать Owner interventions/time where practical, rework count, cycle/blocking evidence and actual outcome;
10. сформировать public-safe AC-505 evidence summary без raw customer confidential payload.

## 7. AC-505 success / stop semantics

AC-505 может завершиться `PASS` даже если customer outcome — rework или explicit non-acceptance, если workflow корректно классифицировал/эскалировал ситуацию, authority границы соблюдены и evidence reconstructable.

AC-505 должен остановиться без ложного PASS, если:

- нет актуального реального customer feedback case;
- невозможно установить authoritative customer/scope/evidence basis;
- proof потребовал бы нового customer promise, material external commitment, budget/spend, AM-3/AM-4 или inaccessible/restricted data;
- implementation требует actual Arvectum OS governed reliance, не разрешённую AC-503;
- Product technical evidence не позволяет подтвердить claimed state;
- customer validation result нельзя атрибутировать реальному источнику.

В этих случаях фиксируется blocked/reselection/escalation evidence; authority не расширяется ради завершения milestone.

## 8. Expected AC-505 evidence

До перехода к AC-506 должны быть доступны public-safe references/evidence, достаточные подтвердить:

- real customer-source input existed;
- exact case/workflow/product baseline was pinned;
- POS-002 classification/customer gates were attributable;
- POS-004 technical activity, если выполнялась, осталась внутри bounded scope;
- claimed W-state соответствует реальным source/product/customer facts;
- Candidate Ready не был подменён customer acceptance;
- any block/rework/unknown/uncertain outcome was represented honestly;
- Owner intervention and cycle/rework measurements were captured where practical;
- no raw DC-2/DC-3 payload leaked into public Company artifacts;
- actual outcome даёт empirical evidence для AC-506/AC-507 rather than only unit-test evidence.

## 9. M5 exit direction

M5 остаётся открытым. Он может быть закрыт только после AC-505…AC-507 и actual evidence, включая real operation, actual uncertainty/failure/recovery path, customer/business outcome evidence, Owner burden, technical/AI quality/cost/reliability и continue/change/stop economic decision.

## 10. Authority and boundary rule

Roadmap не создаёт Organizational Authority, budget, legal/corporate authority, customer/vendor commitment, Product Contract, access grant, production approval или OS lifecycle transition.

AC-504 technical PASS разрешает использовать bounded helper для supervised evidence collection; он не разрешает autonomous customer effect или broader authority.
