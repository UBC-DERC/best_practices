# src/best_practices/__init__.py
"""Public API for the best_practices package.

The two functions exported here are the intended entry points for any code
that wants to evaluate a repository programmatically:

    from best_practices import run_checks, score_by_topic

    results = run_checks(Path("/path/to/repo"))
    scores  = score_by_topic(results)

The CLI (``best-practices`` command) is a thin wrapper around these two
functions plus the report and badge renderers.
"""

from pathlib import Path

from best_practices.checks import REGISTRY
from best_practices.language import detect_language
from best_practices.models import Check, CheckResult, Language, Topic, TopicScore

__all__ = ["run_checks", "score_by_topic"]


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _run_check(check: Check, repo_root: Path) -> CheckResult:
    """Run a single check and return its result.

    Args:
        check:     The check specification to run.
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        A ``CheckResult`` carrying the shared metadata from the ``Check``
        plus the outcome (present/absent) and a human-readable detail string.
    """
    present = check.method(repo_root)
    detail = f"{'✓' if present else '✗'} {check.description}"
    return CheckResult(
        **check.model_dump(exclude={"method"}),
        present=present,
        detail=detail,
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def run_checks(repo_root: Path) -> list[CheckResult]:
    """Run all applicable checks against a repository root.

    The detected language of the repository (``"python"``, ``"r"``, or
    ``"both"``) filters the global registry so that only relevant checks
    are evaluated. Checks whose ``language`` field is ``"both"`` always run.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        A list of ``CheckResult`` instances, one per applicable check,
        in registry order.
    """
    detected: list[Language] = detect_language(repo_root)
    applicable = [
        c
        for c in REGISTRY
        if not c.languages  # universal check
        or not detected  # unknown language — run all
        or any(lang in c.languages for lang in detected)  # language matches
    ]
    return [_run_check(check, repo_root) for check in applicable]


def score_by_topic(results: list[CheckResult]) -> list[TopicScore]:
    """Aggregate check results into per-topic scores.

    Topics with no applicable checks receive a ``TopicScore`` with
    ``passed=0`` and ``total=0``, which yields a ``score`` of ``0.0``.

    Args:
        results: The list of ``CheckResult`` instances returned by
                 ``run_checks()``.

    Returns:
        A list of four ``TopicScore`` instances, one per topic, in the
        canonical order: attribution, community, building, organization.
    """
    topics: list[Topic] = ["attribution", "community", "building", "organization"]
    scores: list[TopicScore] = []
    for topic in topics:
        topic_results = [r for r in results if r.topic == topic]
        scores.append(
            TopicScore(
                topic=topic,
                passed=sum(1 for r in topic_results if r.present),
                total=len(topic_results),
            )
        )
    return scores
