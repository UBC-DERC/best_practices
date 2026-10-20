# tests/checks/test_attribution.py
"""Tests for community-group best-practice checks.

Each check function gets at least two tests: one where the condition is
present (should return True) and one where it is absent (should return
False). Edge cases are tested separately.
"""

from pathlib import Path

from best_practices.checks.community import (
    check_docs_folder,
    check_funder_ref,
    check_man_folder_pkg,
    check_mkdocs_yaml,
)

# ---------------------------------------------------------------------------
# check_readme_exists
# ---------------------------------------------------------------------------


def test_docs_folder_exists_passes(tmp_path: Path) -> None:
    """```doc``` folder present at the root should pass."""
    (tmp_path / "docs").mkdir()
    assert check_docs_folder(repo_root=tmp_path) is True


def test_docs_folder_exists_fails(tmp_path: Path) -> None:
    """No doc folder at the root should fail."""
    (tmp_path / "dawc").mkdir()
    assert check_docs_folder(repo_root=tmp_path) is False


# ---------------------------------------------------------------------------
# check_funder_ref
# ---------------------------------------------------------------------------


def test_readme_has_funder_NSF_passes(tmp_path: Path) -> None:
    """A README referencing the NSF should pass."""
    (tmp_path / "README.md").write_text("Funded by the NSF and others.")
    assert check_funder_ref(repo_root=tmp_path) is True


def test_readme_has_funder_unnamed_passes(tmp_path: Path) -> None:
    """A README referencing a funder should pass."""
    (tmp_path / "README.md").write_text(
        "This is funded in part by the spooky eyed guys."
    )
    assert check_funder_ref(repo_root=tmp_path) is True


def test_readme_has_no_funder_fails(tmp_path: Path) -> None:
    """An empty readme shouldn't pass the funder test."""
    (tmp_path / "README.md").write_text("Blah blah blah")
    assert check_funder_ref(repo_root=tmp_path) is False


# ---------------------------------------------------------------------------
# check_man_folder_pkg
# ---------------------------------------------------------------------------


def test_man_folder_exists_passes(tmp_path: Path) -> None:
    """Man folder present at the root should pass."""
    (tmp_path / "man").mkdir()
    assert check_man_folder_pkg(repo_root=tmp_path) is True


def test_man_folder_exists_fails(tmp_path: Path) -> None:
    """No man folder present at the root should fail."""
    (tmp_path / "doc").mkdir()
    assert check_man_folder_pkg(repo_root=tmp_path) is False


# ---------------------------------------------------------------------------
# check_mkdocs_yaml
# ---------------------------------------------------------------------------


def test_mkdocs_yaml_exists_passes(tmp_path: Path) -> None:
    """mkdocs.yaml file present at the root should pass."""
    (tmp_path / "mkdocs.yaml").write_text("jerk: banana")
    assert check_mkdocs_yaml(repo_root=tmp_path) is True


def test_mkdocs_yml_exists_passes(tmp_path: Path) -> None:
    """mkdocs.yml file present at the root should pass."""
    (tmp_path / "mkdocs.yml").write_text("jerk: banana")
    assert check_mkdocs_yaml(repo_root=tmp_path) is True


def test_mkdocs_yml_doesnt_exist_passes(tmp_path: Path) -> None:
    """mkdocs.yml file present at the root should pass."""
    (tmp_path / "mkdocs.yoml").write_text("jerk: banana")
    assert check_mkdocs_yaml(repo_root=tmp_path) is False
