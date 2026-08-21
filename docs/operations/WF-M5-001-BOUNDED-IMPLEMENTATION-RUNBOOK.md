# WF-M5-001 — Bounded Implementation Runbook

Статус: `Active`
Версия: `1.0.0`
Создано: `2026-08-21`
Roadmap: `AC-504 — Bounded workflow implementation`
Workflow: `WF-M5-001`
First contour: `PORT-002 — Discount Parser`
Implementation home: `arvectum/arvectum-company`
Product technical truth: `arvectum/discount-parser`
OS reliance: `NO-ADDITIONAL-OS-RELIANCE` for first M5 proof

## 1. Purpose

Этот runbook описывает минимальную обратимую механику одного реального `WF-M5-001` case для следующего supervised proof `AC-505`.

Implementation намеренно не является workflow engine, CRM, issue tracker, Arvectum OS substitute или источником customer/product truth.

Company repo хранит только code/schema/runbook/public-safe mechanics. Реальные case files по умолчанию создаются в `.local/wf-m5-001/`, который исключён из git. Raw customer `DC-2` payload и любые `DC-3` secrets в case file не помещаются: используются только защищённые references.

## 2. Exact pinned governance evidence

Helper `tools/wf_m5_001_case.py` жёстко pin-ит:

- AC-502 Approved publication blob: `9b06e02a6d9afa8b6b4533d3a9f71690518c3ce1`;
- AC-502 exact reviewed proposal blob: `b1df71839422e509cbfa76faec31bf788ca9842d`;
- AC-503 Approved publication blob: `8984d4c094da87a2c9d201fd9cffcd617c641f8f`;
- workflow id/version: `WF-M5-001 / 1.0.0`;
- first product contour: `PORT-002 / arvectum/discount-parser`.

Default product baseline at AC-504 implementation start:

`a8c1b29702a8ce40bd30b5d972ac2541367900e1`.

AC-505 may override the product baseline for the actual case, but the exact baseline used must remain recorded.

## 3. What the helper does

The helper can:

- open a sanitized case at `W0`;
- normalize intake and data-boundary evidence (`W1/W2`);
- record attributable `POS-002 / AM-2` classification (`W3`);
- admit only `CL-1` into the normal technical correction path (`W4`);
- record `POS-004` technical execution (`W5`), verification (`W6`) and Candidate Ready (`W7`);
- record, but never perform, a customer handoff (`W8`);
- record explicit customer rework (`W9`) or acceptance (`W10`);
- represent `blocked / unknown / stale / uncertain` as `W11`;
- link product, customer and control references;
- capture lightweight Owner intervention measurements;
- validate the reconstructability/invariants of a stored case.

It cannot send messages, deploy software, modify Discount Parser, create commitments, infer customer acceptance, activate `AM-3/AM-4`, or use Arvectum OS state/history.

## 4. Minimal operator path

Use Python 3.11+; no third-party packages are required.

Create a case:

```bash
python tools/wf_m5_001_case.py new \
  --source-ref protected://customer-feedback/<opaque-id> \
  --received-at 2026-08-21T18:00:00Z \
  --principal-ref principal/owner
```

The command returns a generated safe `case_id`, for example:

`WF-M5-001-20260821-ABCDEF12`.

Prepare intake:

```bash
python tools/wf_m5_001_case.py intake <case_id> \
  --principal-ref principal/owner \
  --summary "sanitized description of the reported mismatch" \
  --affected-version 0.1.11 \
  --environment-ref protected://customer-environment/<opaque-id> \
  --scope-basis-ref product://accepted-scope/<opaque-id> \
  --classification-ready
```

Classify:

```bash
python tools/wf_m5_001_case.py classify <case_id> \
  --principal-ref principal/owner \
  --class CL-1 \
  --summary "in-scope defect; no new customer commitment"
```

Admit bounded correction:

```bash
python tools/wf_m5_001_case.py admit <case_id> \
  --principal-ref principal/owner \
  --scope "correct only the admitted behavior" \
  --exclude "no product redesign" \
  --exclude "no autonomous customer delivery"
```

Start POS-004 segment:

```bash
python tools/wf_m5_001_case.py start <case_id> \
  --principal-ref principal/ai-engineering
```

After product-local work exists, record verification and provenance:

```bash
python tools/wf_m5_001_case.py verify <case_id> \
  --principal-ref principal/ai-engineering \
  --test-ref product://tests/<test-or-run-ref> \
  --candidate-ref commit=<git-commit-ref> \
  --known-limitations "none known within admitted scope"
```

At this point state may become `W7 — Candidate Ready`. This is only a technical handback.

A real customer-facing handoff is performed outside this tool by the authorized human/process. Afterwards record only the evidence reference:

```bash
python tools/wf_m5_001_case.py handoff <case_id> \
  --principal-ref principal/owner \
  --handoff-ref protected://customer-handoff/<opaque-id>
```

Record the explicit customer result:

```bash
python tools/wf_m5_001_case.py customer-result <case_id> \
  --principal-ref principal/owner \
  --result accepted \
  --validation-ref protected://customer-validation/<opaque-id>
```

`W10` is impossible without an explicit validation reference.

## 5. Non-CL-1 handling

`CL-4`, `CL-5`, `CL-6` and other non-CL-1 classes cannot be silently admitted to `W4` by the helper.

Use an explicit safe stop/escalation when required:

```bash
python tools/wf_m5_001_case.py block <case_id> \
  --principal-ref principal/owner \
  --kind unknown \
  --reason "evidence insufficient to classify safely" \
  --target "POS-002/customer-clarification"
```

Allowed blocker kinds are `blocked`, `unknown`, `stale`, `uncertain`.

## 6. Linking evidence

References can be attached without copying source payloads:

```bash
python tools/wf_m5_001_case.py link <case_id> --type issue --ref github://arvectum/discount-parser/issues/123
python tools/wf_m5_001_case.py link <case_id> --type control --ref ESC-2026-001
```

Do not use `link` to copy customer messages, credentials, logs containing secrets, or private commercial terms.

## 7. Owner burden measurement

For AC-505/AC-507 evidence:

```bash
python tools/wf_m5_001_case.py measure-owner <case_id> \
  --interventions 2 \
  --minutes 8
```

This is lightweight evidence, not accounting/timekeeping authority.

## 8. Validation and inspection

```bash
python tools/wf_m5_001_case.py validate <case_id>
python tools/wf_m5_001_case.py show <case_id>
```

Validation fails closed on, among other things:

- changed governance pins;
- illegal state path;
- `AM-3/AM-4`;
- wrong Position on Company/customer or technical gates;
- non-CL-1 technical admission;
- Candidate Ready without test + candidate provenance + limitations statement;
- customer closure without explicit validation ref;
- likely secret material.

## 9. Manual fallback

If the helper is unavailable, copy `docs/operations/WF-M5-001-CASE-TEMPLATE.json` to a private/non-git location and maintain the same fields manually.

Manual fallback must preserve:

- exact workflow/product/version references;
- attributable Position/Principal/AM acts;
- material state history;
- protected customer refs instead of raw payloads;
- product issue/PR/commit/test/build refs;
- explicit Candidate Ready vs handoff vs acceptance separation;
- blocker/unknown/stale/uncertain reason;
- Owner-intervention evidence where practical.

The helper may later validate a manually maintained case only after it conforms to the exact schema.

## 10. AC-504 acceptance checks

AC-504 implementation is technically acceptable when all of the following are true:

1. one sanitized case can be created and persisted outside git;
2. W0→W7 normal correction path is representable with Position/AM gates;
3. W8/W10 require explicit customer evidence references and do not perform customer effects;
4. non-CL-1 scope cannot enter W4;
5. unknown/stale/uncertain can fail closed to W11;
6. Candidate Ready requires test evidence and candidate provenance;
7. likely DC-3 secrets are rejected;
8. all runtime dependencies are Python standard library only;
9. local unittest command passes;
10. manual fallback remains possible without changing authority.

Technical AC-504 PASS does not constitute AC-505 empirical proof, customer acceptance, Product readiness, profitability, or M5 closure.
