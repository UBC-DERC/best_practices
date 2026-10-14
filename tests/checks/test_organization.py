# tests/checks/test_organization.py
"""Tests for organization-group best-practice checks."""

from pathlib import Path

from best_practices.checks.organization import check_repo_has_files


def test_repo_has_files_passes(tmp_path: Path) -> None:
    """A directory containing at least one item should pass."""
    (tmp_path / "README.md").write_text("# hello")
    assert check_repo_has_files(tmp_path) is True


def test_repo_has_files_fails(tmp_path: Path) -> None:
    """A completely empty directory should fail."""
    assert check_repo_has_files(tmp_path) is False
