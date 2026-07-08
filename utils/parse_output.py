#!/usr/bin/env python3
"""Parse and validate Curriculum Coherence Evals judge outputs.

The combined judge prompt requires the model output to begin with an 8-value
binary array in this order:

    [PC, RC, RF, SC, VF, AF, DA, DPA]

This script extracts the first valid array, validates it, and converts it into
machine-readable JSON.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Any

DIMENSION_ORDER = [
    "propositional_coherence",
    "referential_coherence",
    "repair_of_fragmentation",
    "sequential_coherence",
    "violation_flag",
    "avoidance_of_fragmentation",
    "disciplinary_anchoring",
    "disciplinary_pedagogic_alignment",
]

DIMENSION_CODES = ["PC", "RC", "RF", "SC", "VF", "AF", "DA", "DPA"]

ARRAY_PATTERN = re.compile(r"\[[\s,01]+\]")


class JudgeOutputError(ValueError):
    """Raised when a judge output cannot be parsed or validated."""


def extract_array(text: str) -> list[int]:
    """Extract the first valid 8-value binary array from raw judge output."""
    for match in ARRAY_PATTERN.finditer(text):
        try:
            value: Any = ast.literal_eval(match.group(0))
        except (SyntaxError, ValueError):
            continue
        if isinstance(value, list) and len(value) == 8 and all(item in (0, 1) for item in value):
            return [int(item) for item in value]

    raise JudgeOutputError(
        "No valid 8-value binary array found. Expected something like [1,0,0,1,0,1,1,1]."
    )


def parse_output(text: str, case_id: str | None = None) -> dict[str, Any]:
    """Return a structured JSON-compatible representation of the judge output."""
    scores = extract_array(text)
    result: dict[str, Any] = {
        "scores": scores,
        "dimension_order": DIMENSION_ORDER,
        "dimension_codes": DIMENSION_CODES,
        "by_dimension": dict(zip(DIMENSION_ORDER, scores)),
        "by_code": dict(zip(DIMENSION_CODES, scores)),
    }
    if case_id is not None:
        result = {"id": case_id, **result}
    return result


def read_text_argument(text: str | None, file_path: Path | None) -> str:
    """Read raw judge output from --text, --file, or stdin."""
    if text is not None and file_path is not None:
        raise JudgeOutputError("Use only one of --text or --file, not both.")
    if text is not None:
        return text
    if file_path is not None:
        return file_path.read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise JudgeOutputError("Provide judge output using --text, --file, or stdin.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse Curriculum Coherence Evals judge output into JSON.")
    parser.add_argument("--text", help="Raw model output containing the 8-value binary array.")
    parser.add_argument("--file", type=Path, help="Text file containing raw model output.")
    parser.add_argument("--id", dest="case_id", help="Optional case identifier to include in the parsed JSON.")
    parser.add_argument("--compact", action="store_true", help="Print compact JSON instead of pretty JSON.")
    args = parser.parse_args()

    try:
        raw_text = read_text_argument(args.text, args.file)
        parsed = parse_output(raw_text, args.case_id)
    except (OSError, JudgeOutputError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    if args.compact:
        print(json.dumps(parsed, separators=(",", ":")))
    else:
        print(json.dumps(parsed, indent=2))


if __name__ == "__main__":
    main()
