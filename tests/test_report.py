# tests/test_report.py
"""Tests for the Markdown report renderer."""

from best_practices.models import CheckResult, Topic, TopicScore
from best_practices.report import render_markdown

_REFERENCE = "https://ubc-derc.github.io/derc_copier/features/"


def _make_result(
    name: str,
    topic: Topic,
    present: bool,
    description: str = "A check.",
) -> CheckResult:
    """Helper: build a minimal CheckResult."""
    symbol = "✓" if present else "✗"
    return CheckResult(
        name=name,
        description=description,
        topic=topic,
        reference=_REFERENCE,
        languages=[],
        present=present,
        detail=f"{symbol} {description}",
    )


def _make_score(topic: Topic, passed: int, total: int) -> TopicScore:
    return TopicScore(topic=topic, passed=passed, total=total)


def test_render_markdown_returns_string() -> None:
    """render_markdown should always return a string."""
    result = render_markdown([], [])
    assert isinstance(result, str)


def test_render_markdown_contains_overall_score() -> None:
    """Report should include an overall score line."""
    results = [_make_result("readme_exists", "attribution", True)]
    scores = [_make_score("attribution", 1, 1)]
    report = render_markdown(results, scores)
    assert "Overall score:" in report
    assert "1 / 1" in report


def test_render_markdown_contains_topic_heading() -> None:
    """Report should include a heading for each topic that has results."""
    results = [_make_result("readme_exists", "attribution", True)]
    scores = [_make_score("attribution", 1, 1)]
    report = render_markdown(results, scores)
    assert "## Attribution" in report


def test_render_markdown_shows_pass_symbol() -> None:
    """Passing checks should show ✓ in the report."""
    results = [
        _make_result("readme_exists", "attribution", True, "README.md is present.")
    ]
    scores = [_make_score("attribution", 1, 1)]
    report = render_markdown(results, scores)
    assert "✓" in report


def test_render_markdown_shows_fail_symbol() -> None:
    """Failing checks should show ✗ in the report."""
    results = [
        _make_result("readme_exists", "attribution", False, "README.md is present.")
    ]
    scores = [_make_score("attribution", 0, 1)]
    report = render_markdown(results, scores)
    assert "✗" in report


def test_render_markdown_omits_empty_topics() -> None:
    """Topics with no results should not appear as headings."""
    results = [_make_result("readme_exists", "attribution", True)]
    scores = [_make_score("attribution", 1, 1)]
    report = render_markdown(results, scores)
    assert "## Community" not in report
    assert "## Building" not in report
    assert "## Organization" not in report


def test_render_markdown_includes_guidance_link() -> None:
    """Each check line should include a link to the guidance page."""
    results = [_make_result("readme_exists", "attribution", True)]
    scores = [_make_score("attribution", 1, 1)]
    report = render_markdown(results, scores)
    assert _REFERENCE in report
