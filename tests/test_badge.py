# tests/test_badge.py
"""Tests for the shields.io badge renderer."""

import json
from pathlib import Path

from best_practices.badge import render_badge, write_badge
from best_practices.models import TopicScore


def _make_score(passed: int, total: int) -> list[TopicScore]:
    """Helper: one topic score wrapping the given counts."""
    return [TopicScore(topic="attribution", passed=passed, total=total)]


def test_render_badge_schema_version(tmp_path: Path) -> None:
    """Badge payload must carry schemaVersion = 1."""
    badge = render_badge(_make_score(10, 10))
    assert badge["schemaVersion"] == 1


def test_render_badge_label(tmp_path: Path) -> None:
    """Badge label should be 'best practices'."""
    badge = render_badge(_make_score(10, 10))
    assert badge["label"] == "best practices"


def test_render_badge_message_format(tmp_path: Path) -> None:
    """Badge message should be '<passed> / <total>'."""
    badge = render_badge(_make_score(7, 10))
    assert badge["message"] == "7 / 10"


def test_render_badge_color_brightgreen() -> None:
    """100 % score → brightgreen."""
    badge = render_badge(_make_score(10, 10))
    assert badge["color"] == "brightgreen"


def test_render_badge_color_green() -> None:
    """75 % score → green."""
    badge = render_badge(_make_score(3, 4))
    assert badge["color"] == "green"


def test_render_badge_color_yellow() -> None:
    """50 % score → yellow."""
    badge = render_badge(_make_score(1, 2))
    assert badge["color"] == "yellow"


def test_render_badge_color_red() -> None:
    """Below 50 % → red."""
    badge = render_badge(_make_score(1, 4))
    assert badge["color"] == "red"


def test_render_badge_zero_total() -> None:
    """No applicable checks → 0 % → red, does not raise."""
    badge = render_badge(_make_score(0, 0))
    assert badge["color"] == "red"
    assert badge["message"] == "0 / 0"


def test_write_badge_creates_valid_json(tmp_path: Path) -> None:
    """write_badge should produce a valid JSON file at the given path."""
    out = tmp_path / "badge.json"
    write_badge(_make_score(8, 10), out)
    assert out.is_file()
    data = json.loads(out.read_text())
    assert data["schemaVersion"] == 1
    assert "color" in data
