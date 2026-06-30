from __future__ import annotations

import argparse
import sys
from pathlib import Path

from vector_index_sizer import __version__
from vector_index_sizer.core import (
    audit_records,
    read_records,
    render_json,
    render_markdown,
    should_fail,
)
from vector_index_sizer.rules import PROJECT_NAME


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='vector-index-sizer',
        description='Estimate vector index footprint and flag capacity risks from planning notes.',
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        help='vector index sizing notes or config',
    )
    parser.add_argument(
        "--format",
        choices=("auto", "text", "jsonl", "csv", "json"),
        default="auto",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON instead of Markdown")
    parser.add_argument("--fail-on", choices=("low", "medium", "high"), default="high")
    parser.add_argument("--out", type=Path, help="write report to a file")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.input is None:
        parser.print_help()
        return 0
    try:
        records = read_records(args.input, args.format)
        report = audit_records(records)
        output = render_json(report) if args.json else render_markdown(report, PROJECT_NAME)
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(output, encoding="utf-8")
        else:
            print(output, end="")
    except (OSError, ValueError) as exc:
        print(f"vector-index-sizer: error: {exc}", file=sys.stderr)
        return 1
    return 2 if should_fail(report, args.fail_on) else 0
