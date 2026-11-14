#!/usr/bin/env python3
"""Gate 4: the catalogue schema is a faithful projection of the metamodel
schema, and every record validates against it.

Expected values are embedded from dea-metamodel v1.0.0 by the kit
generator; bump them in the same CR that bumps metamodel_pin in
dependencies.yaml. Never widen a normative enum locally.
"""

from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft7Validator
from referencing import Registry, Resource

REPO = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO / "schemas" / "entity.schema.json"
REL_SCHEMA_PATH = REPO / "schemas" / "relationship-instance.schema.json"
REL_SCHEMA_URI = f"https://technehub-labs.github.io/dea-catalog-patterns/schemas/relationship-instance.schema.json"
FIXTURE_VALID = REPO / "schemas" / "fixtures" / "example-valid.yaml"
FIXTURE_INVALID = REPO / "schemas" / "fixtures" / "example-invalid.yaml"
RECORD_GLOB = "entities/v1-alpha/**/*.yaml"

# Multi-type corpus (CR-AP-CAT-02 §2.1): the projection is an anyOf over the
# two allocated entities; projection checks dispatch per branch.
EXPECTED_LIFECYCLE_ENUM = ["proposed", "planned", "active", "deprecated", "retired"]
EXPECTED_BRANCHES = {
    "ArchitecturePattern": {
        "required": ["id", "type", "name", "version", "lifecycle_status",
                     "problem", "solution", "applicability"],
        "id_pattern": "^dea:architecture-pattern-[a-z0-9-]+$",
        "enums": {"maturity": ["emerging", "established", "canonical", "deprecated"]},
    },
    "Technology": {
        "required": ["id", "type", "name", "version", "lifecycle_status",
                     "technology_category"],
        "id_pattern": "^dea:technology-[a-z0-9-]+$",
        "enums": {"technology_category": ["language", "framework", "runtime", "database",
                                          "library", "build-tool", "ci-cd", "monitoring",
                                          "orchestration", "platform"],
                  "adoption_status": ["approved", "deprecated", "banned", "experimental"]},
    },
}


def check_projection() -> list[str]:
    if not SCHEMA_PATH.exists():
        return ["entity.schema.json is missing"]
    schema = json.load(SCHEMA_PATH.open(encoding="utf-8"))
    findings: list[str] = []
    if not schema.get("anyOf"):
        findings.append("projection is not a multi-type anyOf")
        return findings
    got_types = set()
    for branch in schema["anyOf"]:
        props = branch.get("properties") or {}
        rtype = (props.get("type") or {}).get("const")
        got_types.add(rtype)
        exp = EXPECTED_BRANCHES.get(rtype)
        if exp is None:
            findings.append(f"unexpected branch type const {rtype!r}")
            continue
        if branch.get("type") != "object":
            findings.append(f"{rtype} branch: type is not object")
        if branch.get("additionalProperties") is not False:
            findings.append(f"{rtype} branch: additionalProperties is not false")
        if branch.get("required") != exp["required"]:
            findings.append(f"{rtype} branch: required is {branch.get('required')!r}")
        if (props.get("lifecycle_status") or {}).get("enum") != EXPECTED_LIFECYCLE_ENUM:
            findings.append(f"{rtype} branch: lifecycle_status enum mismatch")
        if (props.get("id") or {}).get("pattern") != exp["id_pattern"]:
            findings.append(f"{rtype} branch: id pattern mismatch")
        for field, expected in exp["enums"].items():
            got = (props.get(field) or {}).get("enum")
            if got != expected:
                findings.append(f"{rtype} branch: {field} enum drift")
        rel = props.get("relationships")
        if not rel or "$ref" not in (rel.get("items") or {}):
            findings.append(f"{rtype} branch: relationships items must $ref relationship-instance.schema.json")
    if got_types != set(EXPECTED_BRANCHES):
        findings.append(f"branch types {sorted(got_types)} do not match {sorted(EXPECTED_BRANCHES)}")
    return findings


def build_validator() -> Draft7Validator:
    schema = json.load(SCHEMA_PATH.open(encoding="utf-8"))
    rel_schema = json.load(REL_SCHEMA_PATH.open(encoding="utf-8"))
    registry = Registry().with_resource(REL_SCHEMA_URI, Resource.from_contents(rel_schema))
    return Draft7Validator(schema, registry=registry)



def main() -> int:
    findings = check_projection()
    if findings:
        for f in findings:
            print(f"FAIL: {f}")
        print(f"Findings: {len(findings)}")
        return 1

    validator = build_validator()

    if FIXTURE_VALID.exists():
        doc = yaml.safe_load(FIXTURE_VALID.read_text(encoding="utf-8"))
        errs = sorted(validator.iter_errors(doc), key=str)
        if errs:
            findings.append("valid fixture does not validate: " + "; ".join(e.message for e in errs[:3]))
    else:
        findings.append("valid fixture is missing")

    if FIXTURE_INVALID.exists():
        doc = yaml.safe_load(FIXTURE_INVALID.read_text(encoding="utf-8"))
        errs = sorted(validator.iter_errors(doc), key=str)
        if not errs:
            findings.append("invalid fixture validates (it must not)")
    else:
        findings.append("invalid fixture is missing")

    records = sorted(glob.glob(str(REPO / RECORD_GLOB), recursive=True))
    records = [r for r in records if "/research/" not in r and "/retired/" not in r]
    for f in records:
        doc = yaml.safe_load(open(f, encoding="utf-8")) or {}
        errs = sorted(validator.iter_errors(doc), key=str)
        if errs:
            findings.append(f"{Path(f).relative_to(REPO)}: " + "; ".join(e.message for e in errs[:3]))

    if findings:
        for f in findings:
            print(f"FAIL: {f}")
        print(f"Findings: {len(findings)}")
        return 1

    print(f"OK: projection faithful; {len(records)} record(s) validate; fixtures behave")
    print("Findings: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
