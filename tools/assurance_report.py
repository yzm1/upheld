#!/usr/bin/env python3
"""Derive intended-versus-actual assurance gaps from an Upheld 0.2 register."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any


def _unique(items, what):
    values = list(items)
    if len(values) != len(set(values)):
        raise ValueError(f"duplicate {what}")
    return values


def _selected_plan(obligation):
    assurance = obligation["recommended_assurance"]
    plans = assurance["plans"]
    plan_ids = _unique((plan["id"] for plan in plans), "plan id")
    for plan in plans:
        if plan["obligation_id"] != obligation["id"]:
            raise ValueError(f"plan {plan['id']} belongs to another obligation")
        _unique((member["id"] for member in plan["members"]), "plan member id")
    selected = assurance["selected_plan_id"]
    if selected is not None:
        if selected not in plan_ids:
            raise ValueError(f"unknown selected plan: {selected}")
        return next(plan for plan in plans if plan["id"] == selected)
    preferred = [plan for plan in plans if plan["preference"] == "preferred"]
    if len(preferred) > 1:
        raise ValueError(f"multiple preferred plans for {obligation['id']}")
    return preferred[0] if preferred else None


def _gap_id(obligation_id, suffix):
    return f"{obligation_id}:gap:{suffix}"


def _gap(kind, obligation, suffix, summary, rationale, next_action,
         member_ids=(), defense_ids=(), status="open", metadata=None):
    return {
        "id": _gap_id(obligation["id"], suffix),
        "kind": kind,
        "status": status,
        "severity": "unknown",
        "scope": obligation["subject_scope"],
        "summary": summary,
        "rationale": rationale,
        "recommendation_member_ids": list(member_ids),
        "defense_ids": list(defense_ids),
        "next_action": next_action,
        "metadata": metadata or {},
    }


def _accepted_key(gap):
    return (
        gap["kind"],
        tuple(sorted(gap["related_plan_member_ids"])),
        tuple(sorted(gap["related_defense_ids"])),
    )


def _apply_acceptance(gap, accepted):
    key = (
        gap["kind"],
        tuple(sorted(gap["recommendation_member_ids"])),
        tuple(sorted(gap["defense_ids"])),
    )
    record = accepted.get(key)
    if not record:
        return gap
    gap = dict(gap)
    gap["status"] = "accepted"
    gap["rationale"] += f" Accepted gap: {record['reason']}"
    gap["next_action"] = record["revisit_when"] or "Keep the accepted gap visible until reviewed again."
    gap["metadata"] = {
        **gap.get("metadata", {}),
        "accepted_gap_id": record["id"],
        "accepted_by": record["accepted_by"],
        "accepted_at": record["accepted_at"],
    }
    return gap


def build_report(register: dict[str, Any], source_register: str,
                 bindings: dict[str, str] | None = None,
                 evidence: dict[str, dict[str, Any]] | None = None,
                 generated_at: str | None = None) -> dict[str, Any]:
    if register.get("schema_version") != "0.2":
        raise ValueError("assurance report requires schema_version 0.2")
    obligations = register["obligations"]
    _unique((obligation["id"] for obligation in obligations), "obligation id")
    bindings = bindings or {}
    evidence = evidence or {}
    rows = []

    for obligation in obligations:
        actual = obligation["actual_defenses"]
        _unique((defense["id"] for defense in actual), "defense id")
        for defense in actual:
            if defense["obligation_id"] != obligation["id"]:
                raise ValueError(f"defense {defense['id']} belongs to another obligation")

        plan = _selected_plan(obligation)
        member_ids = {member["id"] for member in plan["members"]} if plan else set()
        for defense in actual:
            unknown = set(defense["recommendation_member_ids"]) - member_ids
            if unknown:
                raise ValueError(f"defense {defense['id']} references unknown plan members: {sorted(unknown)}")

        accepted = {_accepted_key(gap): gap for gap in obligation["accepted_gaps"]}
        gaps = []
        assurance = obligation["recommended_assurance"]

        if assurance["status"] == "unknown" or plan is None:
            gaps.append(_gap(
                "no_plan", obligation, "no-plan",
                "No selected defense plan is available.",
                "Upheld cannot compare current defenses with an intended state without a reviewed plan.",
                "Review the obligation constraints and record at least one defense plan.",
            ))
        else:
            for member in plan["members"]:
                related = [d for d in actual if member["id"] in d["recommendation_member_ids"]]
                present = [d for d in related if d["implementation_state"] == "present"]
                if not present:
                    if related:
                        ids = [d["id"] for d in related]
                        gaps.append(_gap(
                            "weaker_than_recommended", obligation, f"member-{member['id']}-partial",
                            f"Recommended defense member {member['id']} is not fully present.",
                            "The implementation is partial, disabled, or otherwise not recorded as present.",
                            f"Complete, replace, or explicitly accept the difference for {member['id']}.",
                            [member["id"]], ids,
                        ))
                    else:
                        gaps.append(_gap(
                            "no_defense", obligation, f"member-{member['id']}-missing",
                            f"Recommended defense member {member['id']} has no mapped implementation.",
                            member["rationale"],
                            f"Implement the member or review the plan. Proposed challenge: {member['fault_challenge']}",
                            [member["id"]], [],
                        ))
                    continue

                supported = []
                for defense in present:
                    evidence_id = bindings.get(defense["id"])
                    record = evidence.get(evidence_id) if evidence_id else None
                    if record and record.get("defense_id") == defense["id"] and record.get("verdict") == "supports":
                        supported.append(defense)
                if not supported:
                    ids = [d["id"] for d in present]
                    gaps.append(_gap(
                        "unproven_defense", obligation, f"member-{member['id']}-unproven",
                        f"Defense for recommended member {member['id']} exists but has no bound supporting evidence.",
                        "Presence or a passing suite does not establish that the defense detects the stated fault.",
                        f"Run a compatible fault challenge and explicitly bind supporting evidence for {member['id']}.",
                        [member["id"]], ids,
                    ))

        for defense in actual:
            if not defense["recommendation_member_ids"]:
                gaps.append(_gap(
                    "divergence_unreviewed", obligation, f"defense-{defense['id']}-unmapped",
                    f"Current defense {defense['id']} is not mapped to the selected defense plan.",
                    "The defense may be useful, redundant, or a justified alternative, but that relationship is not recorded.",
                    "Map the defense to the plan, revise the plan, or record an accepted difference.",
                    [], [defense["id"]],
                ))

        gaps = [_apply_acceptance(gap, accepted) for gap in gaps]
        used_acceptances = {gap.get("metadata", {}).get("accepted_gap_id") for gap in gaps}
        for accepted_gap in obligation["accepted_gaps"]:
            if accepted_gap["id"] in used_acceptances:
                continue
            gaps.append(_gap(
                "accepted_gap", obligation, f"accepted-{accepted_gap['id']}",
                f"Accepted gap remains recorded: {accepted_gap['reason']}",
                "The project deliberately chose to leave this area uncovered or weaker than the plan.",
                accepted_gap["revisit_when"] or "Keep the accepted gap visible until reviewed again.",
                accepted_gap["related_plan_member_ids"], accepted_gap["related_defense_ids"],
                status="accepted",
                metadata={
                    "accepted_gap_id": accepted_gap["id"],
                    "accepted_by": accepted_gap["accepted_by"],
                    "accepted_at": accepted_gap["accepted_at"],
                },
            ))

        open_gaps = [gap for gap in gaps if gap["status"] == "open"]
        rows.append({
            "obligation_id": obligation["id"],
            "recommendation_status": assurance["status"],
            "selected_plan_id": plan["id"] if plan else assurance["selected_plan_id"],
            "actual_defense_ids": [d["id"] for d in actual],
            "gap_state": "gaps" if gaps else "clean",
            "gaps": gaps,
            "next_actions": list(dict.fromkeys(gap["next_action"] for gap in open_gaps)),
            "metadata": {},
        })

    all_gaps = [gap for row in rows for gap in row["gaps"]]
    open_gaps = [gap for gap in all_gaps if gap["status"] == "open"]
    accepted_gaps = [gap for gap in all_gaps if gap["status"] == "accepted"]
    generated_at = generated_at or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return {
        "schema_version": "0.2",
        "source_register": source_register,
        "source_rev": register.get("producer", {}).get("source_rev", "unknown"),
        "generated_at": generated_at,
        "obligations": rows,
        "summary": {
            "obligations": len(rows),
            "obligations_with_open_gaps": sum(any(g["status"] == "open" for g in row["gaps"]) for row in rows),
            "open_gaps": len(open_gaps),
            "accepted_gaps": len(accepted_gaps),
        },
        "metadata": {
            "limit": "This report compares recorded plans, mappings, bindings, and evidence. It does not discover omitted obligations or infer semantic coverage outside those records."
        },
    }


def _load_evidence(path):
    if path is None:
        return {}
    records = {}
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        records[record["evidence_id"]] = record
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("register", type=Path)
    parser.add_argument("--bindings", type=Path)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists() or args.out.is_symlink():
        raise SystemExit(f"output already exists: {args.out}")
    register = json.loads(args.register.read_text())
    bindings = json.loads(args.bindings.read_text())["bindings"] if args.bindings else {}
    report = build_report(register, str(args.register), bindings, _load_evidence(args.evidence))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
