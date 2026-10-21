# src/best_practices/cli.py
"""Command-line interface for best_practices.

Entry point: ``derc-best-practices <path> [options]``

This module is intentionally thin. It parses arguments, calls the public
API (``run_checks`` and ``score_by_topic``), delegates rendering to
``report`` and ``badge``, and handles exit codes. All business logic lives
elsewhere.

Usage examples
--------------
Print a report to stdout (always exits 0)::

    derc-best-practices /path/to/repo

Save the report and write a badge file::

    derc-best-practices . --output report.md --badge best-practices-badge.json

Fail CI if the overall score falls below 75 %::

    derc-best-practices . --fail-under 75
"""

import argparse
import sys
from pathlib import Path

from best_practices import run_checks, score_by_topic
from best_practices.badge import write_badge
from best_practices.report import render_markdown


def _build_parser() -> argparse.ArgumentParser:
    """Construct and return the argument parser.

    Returns:
        A configured ``ArgumentParser`` instance.
    """
    parser = argparse.ArgumentParser(
        prog="derc-best-practices",
        description=(
            "Evaluate a repository against research software best practices "
            "and produce a Markdown report and optional badge file."
        ),
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Path to the repository root to evaluate.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        metavar="FILE",
        help="Write the Markdown report to FILE instead of printing to stdout.",
    )
    parser.add_argument(
        "--badge",
        type=Path,
        default=None,
        metavar="FILE",
        help="Write a shields.io endpoint JSON badge to FILE.",
    )
    parser.add_argument(
        "--fail-under",
        type=int,
        default=None,
        metavar="N",
        dest="fail_under",
        help=(
            "Exit with status 1 if the overall score is below N percent. "
            "By default the tool is informational and always exits 0."
        ),
    )
    return parser


def main() -> None:
    """Entry point for the ``best-practices`` command.

    Parses command-line arguments, runs all applicable checks against the
    given repository path, renders a Markdown report, and optionally writes
    a badge file. Exits non-zero only when ``--fail-under`` is passed and
    the overall score falls below the threshold.
    """
    parser = _build_parser()
    args = parser.parse_args()

    repo_root = args.path.resolve()
    if not repo_root.is_dir():
        parser.error(f"Path does not exist or is not a directory: {repo_root}")

    results = run_checks(repo_root)
    topic_scores = score_by_topic(results)
    report = render_markdown(results, topic_scores)

    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report)

    if args.badge:
        write_badge(topic_scores, args.badge)

    if args.fail_under is not None:
        total = sum(ts.total for ts in topic_scores)
        passed = sum(ts.passed for ts in topic_scores)
        pct = round(passed / total * 100) if total else 0
        if pct < args.fail_under:
            sys.exit(1)
