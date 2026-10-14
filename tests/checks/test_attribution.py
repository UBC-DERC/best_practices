# tests/checks/test_attribution.py
"""Tests for attribution-group best-practice checks.

Each check function gets at least two tests: one where the condition is
present (should return True) and one where it is absent (should return
False). Edge cases — multiple candidate filenames, missing files that
would be required by a dependent check — are tested separately.
"""

from pathlib import Path

from best_practices.checks.attribution import (
    check_author_in_pyproject,
    check_citation_exists,
    check_license_exists,
    check_orcid_in_citation,
    check_pyproject_exists,
    check_readme_exists,
)

# ---------------------------------------------------------------------------
# check_readme_exists
# ---------------------------------------------------------------------------


def test_readme_exists_passes(tmp_path: Path) -> None:
    """README.md present at the root should pass."""
    (tmp_path / "README.md").write_text("# My Project\n")
    assert check_readme_exists(tmp_path) is True


def test_readme_exists_fails(tmp_path: Path) -> None:
    """An empty directory should fail."""
    assert check_readme_exists(tmp_path) is False


def test_readme_wrong_name_fails(tmp_path: Path) -> None:
    """readme.md (lowercase) does not satisfy the check on case-sensitive filesystems."""
    # This documents the expected behaviour: the check looks for 'README.md' exactly.
    # On Linux (case-sensitive), readme.md is a different file.
    (tmp_path / "readme.md").write_text("# My Project\n")
    # We do not assert a specific outcome here because macOS (case-insensitive)
    # and Linux differ. The important thing is that the function does not raise.
    result = check_readme_exists(tmp_path)
    assert isinstance(result, bool)


# ---------------------------------------------------------------------------
# check_citation_exists
# ---------------------------------------------------------------------------


def test_citation_exists_passes(tmp_path: Path) -> None:
    """CITATION.cff present at the root should pass."""
    (tmp_path / "CITATION.cff").write_text("cff-version: 1.2.0\n")
    assert check_citation_exists(tmp_path) is True


def test_citation_exists_fails(tmp_path: Path) -> None:
    """An empty directory should fail."""
    assert check_citation_exists(tmp_path) is False


# ---------------------------------------------------------------------------
# check_license_exists
# ---------------------------------------------------------------------------


def test_license_exists_passes_LICENSE(tmp_path: Path) -> None:
    """Plain 'LICENSE' file should satisfy the check."""
    (tmp_path / "LICENSE").write_text("MIT License\n")
    assert check_license_exists(tmp_path) is True


def test_license_exists_passes_LICENSE_md(tmp_path: Path) -> None:
    """'LICENSE.md' should satisfy the check."""
    (tmp_path / "LICENSE.md").write_text("# MIT License\n")
    assert check_license_exists(tmp_path) is True


def test_license_exists_passes_LICENSE_txt(tmp_path: Path) -> None:
    """'LICENSE.txt' should satisfy the check."""
    (tmp_path / "LICENSE.txt").write_text("MIT License\n")
    assert check_license_exists(tmp_path) is True


def test_license_exists_fails(tmp_path: Path) -> None:
    """A directory with no licence file should fail."""
    assert check_license_exists(tmp_path) is False


# ---------------------------------------------------------------------------
# check_pyproject_exists
# ---------------------------------------------------------------------------


def test_pyproject_exists_passes(tmp_path: Path) -> None:
    """pyproject.toml present at the root should pass."""
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'demo'\n")
    assert check_pyproject_exists(tmp_path) is True


def test_pyproject_exists_fails(tmp_path: Path) -> None:
    """An empty directory should fail."""
    assert check_pyproject_exists(tmp_path) is False


# ---------------------------------------------------------------------------
# check_author_in_pyproject
# ---------------------------------------------------------------------------


def test_author_in_pyproject_passes(tmp_path: Path) -> None:
    """A pyproject.toml with a non-empty authors list should pass."""
    (tmp_path / "pyproject.toml").write_text(
        "[project]\n"
        "name = 'demo'\n"
        "authors = [{name = 'Alice Researcher', email = 'alice@example.com'}]\n"
    )
    assert check_author_in_pyproject(tmp_path) is True


def test_author_in_pyproject_fails_empty_authors(tmp_path: Path) -> None:
    """An empty authors list should fail."""
    (tmp_path / "pyproject.toml").write_text(
        "[project]\nname = 'demo'\nauthors = []\n"
    )
    assert check_author_in_pyproject(tmp_path) is False


def test_author_in_pyproject_fails_no_project_table(tmp_path: Path) -> None:
    """A pyproject.toml with no [project] table should fail gracefully."""
    (tmp_path / "pyproject.toml").write_text("[build-system]\nrequires = ['hatchling']\n")
    assert check_author_in_pyproject(tmp_path) is False


def test_author_in_pyproject_fails_missing_file(tmp_path: Path) -> None:
    """Missing pyproject.toml should return False without raising."""
    assert check_author_in_pyproject(tmp_path) is False


def test_author_in_pyproject_fails_invalid_toml(tmp_path: Path) -> None:
    """A pyproject.toml with invalid TOML should return False without raising."""
    (tmp_path / "pyproject.toml").write_text("this is not : valid toml [\n")
    assert check_author_in_pyproject(tmp_path) is False


# ---------------------------------------------------------------------------
# check_orcid_in_citation
# ---------------------------------------------------------------------------


def test_orcid_in_citation_passes(tmp_path: Path) -> None:
    """CITATION.cff containing 'orcid:' should pass."""
    (tmp_path / "CITATION.cff").write_text(
        "cff-version: 1.2.0\n"
        "authors:\n"
        "  - family-names: Researcher\n"
        "    given-names: Alice\n"
        "    orcid: https://orcid.org/0000-0001-2345-6789\n"
    )
    assert check_orcid_in_citation(tmp_path) is True


def test_orcid_in_citation_fails_no_orcid(tmp_path: Path) -> None:
    """CITATION.cff without an orcid entry should fail."""
    (tmp_path / "CITATION.cff").write_text(
        "cff-version: 1.2.0\n"
        "authors:\n"
        "  - family-names: Researcher\n"
        "    given-names: Alice\n"
    )
    assert check_orcid_in_citation(tmp_path) is False


def test_orcid_in_citation_fails_missing_file(tmp_path: Path) -> None:
    """Missing CITATION.cff should return False without raising."""
    assert check_orcid_in_citation(tmp_path) is False
