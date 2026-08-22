#!/usr/bin/env python3
"""Fail-closed successor recovery helper for WF-M5-001 / AC-506.

A W11 case remains immutable/closed. New authoritative evidence opens a new linked
case instead of rewriting the blocked case's history. The helper performs no
customer messaging, deployment, approval, classification, or technical work.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

MODULE = Path(__file__).resolve().with_name("wf_m5_001_case.py")
spec = importlib.util.spec_from_file_location("wf_m5_001_case", MODULE)
wf = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(wf)


def recover_successor(
    store: Path,
    predecessor_id: str,
    source_ref: str,
    received_at: str,
    principal_ref: str,
    product_baseline: str,
    summary: str,
    *,
    affected_version: str | None = None,
    environment_ref: str | None = None,
    scope_basis_ref: str | None = None,
    unknowns: tuple[str, ...] | list[str] = (),
    classification_ready: bool = False,
    case_id: str | None = None,
):
    """Create a new case from new evidence while preserving W11 predecessor history."""
    predecessor = wf.load(store, predecessor_id)
    if predecessor["state"] != "W11" or not predecessor.get("blocker"):
        raise wf.CaseError("recovery predecessor must be an explicit W11 blocked case")

    baseline = wf.ref(product_baseline, "product_baseline")
    source = wf.ref(source_ref, "source_ref")
    if source in wf.refs(predecessor, "feedback"):
        raise wf.CaseError("recovery requires new evidence; predecessor feedback ref cannot be reused")

    successor = wf.new_case(source, received_at, principal_ref, case_id, baseline)
    target = wf.path(store, successor["case_id"])
    if target.exists():
        raise wf.CaseError(f"successor case already exists: {target}")

    wf.add_ref(successor, "control", f"predecessor-case:{predecessor_id}", "DC-1")
    wf.add_ref(
        successor,
        "control",
        f"predecessor-blocker:{predecessor['blocker']['kind']}",
        "DC-1",
    )
    wf.intake(
        successor,
        principal_ref,
        summary,
        affected_version,
        environment_ref,
        scope_basis_ref,
        unknowns,
        classification_ready,
    )
    wf.save(store, successor)
    return predecessor, successor


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--store", type=Path, default=Path(".local/wf-m5-001"))
    p.add_argument("predecessor_id")
    p.add_argument("--source-ref", required=True)
    p.add_argument("--received-at", required=True)
    p.add_argument("--principal-ref", required=True)
    p.add_argument("--product-baseline", required=True)
    p.add_argument("--summary", required=True)
    p.add_argument("--affected-version")
    p.add_argument("--environment-ref")
    p.add_argument("--scope-basis-ref")
    p.add_argument("--unknown", action="append", default=[])
    p.add_argument("--classification-ready", action="store_true")
    p.add_argument("--case-id")
    return p


def main(argv=None):
    a = parser().parse_args(argv)
    try:
        predecessor, successor = recover_successor(
            a.store,
            a.predecessor_id,
            a.source_ref,
            a.received_at,
            a.principal_ref,
            a.product_baseline,
            a.summary,
            affected_version=a.affected_version,
            environment_ref=a.environment_ref,
            scope_basis_ref=a.scope_basis_ref,
            unknowns=a.unknown,
            classification_ready=a.classification_ready,
            case_id=a.case_id,
        )
        print(
            json.dumps(
                {
                    "predecessor_case_id": predecessor["case_id"],
                    "predecessor_state": predecessor["state"],
                    "successor_case_id": successor["case_id"],
                    "successor_state": successor["state"],
                    "successor_path": str(wf.path(a.store, successor["case_id"])),
                },
                ensure_ascii=False,
            )
        )
        return 0
    except (wf.CaseError, OSError, json.JSONDecodeError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
