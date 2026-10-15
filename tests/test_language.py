# tests/test_language.py
"""Tests for language detection."""

from pathlib import Path

from best_practices.language import detect_language


def test_detects_python(tmp_path: Path) -> None:
    """pyproject.toml alone → ['python']."""
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'test'\n")
    assert detect_language(tmp_path) == ["python"]


def test_detects_r(tmp_path: Path) -> None:
    """DESCRIPTION alone → ['r']."""
    (tmp_path / "DESCRIPTION").write_text("Package: test\n")
    assert detect_language(tmp_path) == ["r"]


def test_detects_both_when_both_present(tmp_path: Path) -> None:
    """Both indicator files → ['python', 'r']."""
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'test'\n")
    (tmp_path / "DESCRIPTION").write_text("Package: test\n")
    assert detect_language(tmp_path) == ["python", "r"]


def test_defaults_to_empty_when_neither_present(tmp_path: Path) -> None:
    """No indicator files → [] (run-all default)."""
    assert detect_language(tmp_path) == []
