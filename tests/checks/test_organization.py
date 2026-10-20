# tests/checks/test_organization.py
"""Tests for organization-group best-practice checks."""

from pathlib import Path

import git

from best_practices.checks.organization import (
    check_repo_has_data,
    check_repo_has_files,
    check_repo_has_git,
)


def test_repo_has_files_passes(tmp_path: Path) -> None:
    """A directory containing at least one item should pass."""
    (tmp_path / "README.md").write_text("# hello")
    assert check_repo_has_files(tmp_path) is True


def test_repo_has_files_fails(tmp_path: Path) -> None:
    """A completely empty directory should fail."""
    assert check_repo_has_files(tmp_path) is False


def test_repo_has_data(tmp_path: Path) -> None:
    """A project should have a data folder."""
    (tmp_path / "data").mkdir()
    assert check_repo_has_data(repo_root=tmp_path) is True


def test_repo_has_no_data(tmp_path: Path) -> None:
    """A project without a data folder should fail."""
    assert check_repo_has_data(repo_root=tmp_path) is False


def test_repo_has_git(tmp_path: Path) -> None:
    """A repository should have a git file."""
    git.Repo.init(tmp_path)
    assert check_repo_has_git(repo_root=tmp_path) is True


def test_repo_has_no_git(tmp_path: Path) -> None:
    """A repository with no git structure should fail."""
    assert check_repo_has_git(repo_root=tmp_path) is False
