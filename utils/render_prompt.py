#!/usr/bin/env python3
"""Render Curriculum Coherence Evals prompts from JSON or JSONL cases.

The combined judge prompt expects three placeholders:

    {{conversation_history}}
    {{learner_turn}}
    {{agent_turn}}

This utility replaces those placeholders with values from an evaluation case.
It supports rendering a single JSON object, one row from a JSONL file, or every
row in a JSONL file.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable

REQUIRED_FIELDS = ("conversation_history", "learner_turn", "agent_turn")
OPTIONAL_FIELDS = ("id", "metadata")


class CaseValidationError(ValueError):
    """Raised when an evaluation case does not match the expected shape."""


def load_cases(path: Path) -> list[dict[str, Any]]:
    """Load one JSON case or a JSONL file containing multiple cases."""
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise CaseValidationError(f"Case file is empty: {path}")

    if path.suffix.lower() == ".jsonl":
        cases: list[dict[str, Any]] = []
        for line_number, line in enumerate(text.splitlines(), start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise CaseValidationError(f"Invalid JSONL at line {line_number}: {exc}") from exc
            if not isinstance(value, dict):
                raise CaseValidationError(f"Line {line_number} must contain a JSON object.")
            cases.append(value)
        return cases

    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        raise CaseValidationError(f"Invalid JSON file: {exc}") from exc

    if isinstance(value, dict):
        return [value]
    if isinstance(value, list) and all(isinstance(item, dict) for item in value):
        return value
    raise CaseValidationError("JSON case file must be an object or a list of objects.")


def validate_case(case: dict[str, Any], case_label: str = "case") -> None:
    """Validate the minimum schema needed by the prompt template."""
    missing = [field for field in REQUIRED_FIELDS if field not in case]
    if missing:
        raise CaseValidationError(f"{case_label} is missing required field(s): {', '.join(missing)}")

    for field in REQUIRED_FIELDS:
        if not isinstance(case[field], str):
            raise CaseValidationError(f"{case_label}.{field} must be a string.")

    allowed_fields = set(REQUIRED_FIELDS) | set(OPTIONAL_FIELDS)
    unexpected = sorted(set(case) - allowed_fields)
    if unexpected:
        raise CaseValidationError(
            f"{case_label} contains unexpected field(s): {', '.join(unexpected)}. "
            "Use metadata for extra information."
        )


def render_prompt(template: str, case: dict[str, Any]) -> str:
    """Render a prompt template for a single evaluation case."""
    validate_case(case, case.get("id", "case"))
    rendered = template
    for key in REQUIRED_FIELDS:
        rendered = rendered.replace("{{" + key + "}}", case[key])
    return rendered


def iter_selected_cases(cases: list[dict[str, Any]], index: int | None) -> Iterable[tuple[int, dict[str, Any]]]:
    """Yield either the selected case or all cases."""
    if index is None:
        yield from enumerate(cases)
        return
    if index < 0 or index >= len(cases):
        raise IndexError(f"Case index {index} is out of range for {len(cases)} case(s).")
    yield index, cases[index]


def main() -> None:
    parser = argparse.ArgumentParser(description="Render Curriculum Coherence Evals judge prompts.")
    parser.add_argument("--template", required=True, type=Path, help="Prompt template markdown file.")
    parser.add_argument("--case", required=True, type=Path, help="JSON or JSONL evaluation case file.")
    parser.add_argument(
        "--index",
        type=int,
        default=0,
        help="Zero-based case index. Use --all to render every case. Default: 0.",
    )
    parser.add_argument("--all", action="store_true", help="Render every case in the input file.")
    parser.add_argument(
        "--separator",
        default="\n\n---\n\n",
        help="Separator used when rendering multiple prompts with --all.",
    )
    args = parser.parse_args()

    try:
        template = args.template.read_text(encoding="utf-8")
        cases = load_cases(args.case)
        selected_index = None if args.all else args.index
        rendered_prompts = [render_prompt(template, case) for _, case in iter_selected_cases(cases, selected_index)]
    except (OSError, CaseValidationError, IndexError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    print(args.separator.join(rendered_prompts))


if __name__ == "__main__":
    main()
