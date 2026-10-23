# tests/checks/test_code.py
"""Tests for code-group best-practice checks.

Each check function gets at least two tests: one where the condition is
present (should return True) and one where it is absent (should return
False). Edge cases — multiple candidate filenames, missing files that
would be required by a dependent check — are tested separately.
"""

from pathlib import Path

from best_practices.checks.code import (
    check_pyproject_exists,
    check_ruff_configured,
)

# ---------------------------------------------------------------------------
# check_pyproject_exists
# ---------------------------------------------------------------------------


def test_pyproject_exists_passes(tmp_path: Path) -> None:
    """pyproject.toml present at the root should pass."""
    (tmp_path / "pyproject.toml").write_text("[project]\n")
    assert check_pyproject_exists(repo_root=tmp_path) is True


def test_pyproject_exists_fails(tmp_path: Path) -> None:
    """An empty directory should fail."""
    assert check_pyproject_exists(repo_root=tmp_path) is False


# ---------------------------------------------------------------------------
# check_ruff_configured
# ---------------------------------------------------------------------------


def test_ruff_configured_true(tmp_path: Path) -> None:
    """Is there a tools entry for ruff?"""
    (tmp_path / "pyproject.toml").write_text(
        data="[project]\nname='banana'\n[tool.ruff]\nexclude=['data','assets','docs']\n"
    )
    assert check_ruff_configured(repo_root=tmp_path) is True


def test_ruff_configured_false(tmp_path: Path) -> None:
    """Should fail when there's no tools entry for ruff."""
    (tmp_path / "pyproject.toml").write_text(
        "[project]\nname='banana'\n\n[tools.raff]\n"
    )
    assert check_ruff_configured(repo_root=tmp_path) is False
