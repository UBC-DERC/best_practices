# tests/test_run_checks.py
"""Tests for the run_checks() and score_by_topic() public API."""

from pathlib import Path

from best_practices import run_checks, score_by_topic
from best_practices.models import CheckResult, TopicScore


def test_run_checks_returns_list(tmp_path: Path) -> None:
    """run_checks should always return a list."""
    results = run_checks(tmp_path)
    assert isinstance(results, list)


def test_run_checks_results_are_check_results(tmp_path: Path) -> None:
    """Every item returned by run_checks should be a CheckResult."""
    results = run_checks(tmp_path)
    assert all(isinstance(r, CheckResult) for r in results)


def test_run_checks_filters_by_language(tmp_path: Path) -> None:
    """Python-only checks should not run against an R repo."""
    # Create an R-only indicator (no pyproject.toml)
    (tmp_path / "DESCRIPTION").write_text("Package: test\n")
    results = run_checks(tmp_path)
    python_results = [r for r in results if r.languages == ["python"]]
    assert python_results == [], "Python-only checks should be excluded for an R repo"


def test_run_checks_includes_universal_checks(tmp_path: Path) -> None:
    """Checks with no language restriction should always appear in results."""
    results = run_checks(tmp_path)
    universal_results = [r for r in results if r.languages == []]
    assert len(universal_results) > 0


def test_score_by_topic_returns_four_scores(tmp_path: Path) -> None:
    """score_by_topic should return exactly four TopicScore objects."""
    results = run_checks(tmp_path)
    scores = score_by_topic(results)
    assert len(scores) == 4


def test_score_by_topic_results_are_topic_scores(tmp_path: Path) -> None:
    """Every item returned by score_by_topic should be a TopicScore."""
    results = run_checks(tmp_path)
    scores = score_by_topic(results)
    assert all(isinstance(s, TopicScore) for s in scores)


def test_score_by_topic_covers_all_topics(tmp_path: Path) -> None:
    """All four canonical topics should be represented."""
    results = run_checks(tmp_path)
    scores = score_by_topic(results)
    topics = {s.topic for s in scores}
    assert topics == {"attribution", "community", "building", "organization"}


def test_full_repo_has_nonzero_score(full_repo: Path) -> None:
    """A fully-populated repo fixture should score above zero."""
    results = run_checks(full_repo)
    scores = score_by_topic(results)
    total_passed = sum(s.passed for s in scores)
    assert total_passed > 0
