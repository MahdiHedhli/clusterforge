#!/usr/bin/env python3
"""Offline structural checks only. Never contacts Kubernetes or external services."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

TRACK_IDS = {"K8S-200", "K8S-300", "SEC-200", "SEC-300"}
HEADINGS = (
    "## Objective", "## Prerequisites", "## Learn", "## Practice",
    "## Evidence and pass conditions", "## Reset and resume", "## Sources",
)


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def local_target(root: Path, source: Path, target: str) -> Path | None:
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0]
    resolved = (source.parent / target).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f"link escapes repository: {target}")
    return resolved


def validate(root: Path) -> tuple[list[str], dict[str, int]]:
    root = root.resolve()
    errors: list[str] = []
    counts = {"tracks": 0, "lessons": 0, "assessments": 0, "packets": 0, "local_links": 0}
    try:
        catalog = read_json(root / "curriculum/catalog-200-300.json")
        if not isinstance(catalog, dict):
            raise ValueError("catalog must be an object")
        tracks = catalog["tracks"]
        ids = [track["id"] for track in tracks]
        if len(ids) != 4 or set(ids) != TRACK_IDS:
            errors.append("catalog must contain each of the four track IDs exactly once")
        for field, expected in (("content_status", "Draft"), ("runtime_validation", "NOT_RUN"), ("learner_progress", "NOT_RECORDED")):
            if catalog.get(field) != expected:
                errors.append(f"release baseline must not imply qualification: {field}")
        for track in tracks:
            counts["tracks"] += 1
            index = root / track["path"]
            assessment = root / track["assessment"]
            for path in (index, assessment):
                if not path.is_file():
                    errors.append(f"missing track document: {path.relative_to(root)}")
            counts["assessments"] += int(assessment.is_file())
            if len(track["lessons"]) != 6 or len(set(track["lessons"])) != 6:
                errors.append(f"{track['id']}: expected six distinct lessons")
            for number, filename in enumerate(track["lessons"], 1):
                lesson = index.parent / filename
                if not lesson.resolve().is_relative_to(root):
                    errors.append(f"lesson path escapes repository: {filename}")
                    continue
                if not lesson.is_file():
                    errors.append(f"missing lesson: {lesson.relative_to(root)}")
                    continue
                counts["lessons"] += 1
                text = lesson.read_text(encoding="utf-8")
                expected_title = f"# {track['id']}-{number:02d}:"
                if not text.startswith(expected_title):
                    errors.append(f"incorrect lesson ID: {lesson.relative_to(root)}")
                for heading in HEADINGS:
                    if heading not in text.splitlines():
                        errors.append(f"{lesson.relative_to(root)}: missing {heading}")
                if "**Status:** Draft." not in text or "Runtime not verified." not in text:
                    errors.append(f"missing draft/runtime statement: {lesson.relative_to(root)}")
                sources = text.split("## Sources", 1)[-1]
                if "https://" not in sources:
                    errors.append(f"missing primary-source links: {lesson.relative_to(root)}")
        packets = root / "curriculum/practicals/levels-200-300"
        scenario_ids: set[str] = set()
        for name in ("identity.json", "incident.json", "customer.json"):
            packet = read_json(packets / name)
            if not isinstance(packet, dict) or packet.get("synthetic") is not True:
                errors.append(f"packet not explicitly synthetic: {name}")
                continue
            scenario_id = packet.get("scenario_id")
            if not isinstance(scenario_id, str) or not scenario_id or scenario_id in scenario_ids:
                errors.append(f"invalid or duplicate scenario ID: {name}")
            else:
                scenario_ids.add(scenario_id)
            counts["packets"] += 1
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"catalog/packet error: {exc}")
    for source in root.rglob("*.md"):
        if ".git" in source.parts:
            continue
        text = source.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", text):
            try:
                resolved = local_target(root, source, target)
                if resolved is not None:
                    counts["local_links"] += 1
                    if not resolved.exists():
                        errors.append(f"broken local link in {source.relative_to(root)}: {target}")
            except ValueError as exc:
                errors.append(f"{source.relative_to(root)}: {exc}")
    return errors, counts


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors, counts = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("PASS: " + ", ".join(f"{value} {key}" for key, value in counts.items()))
    print("Structural checks only; no cluster execution, external link fetch or competency grading.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
