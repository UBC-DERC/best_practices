# tests/conftest.py
"""Shared pytest fixtures for the best_practices test suite.

Fixtures are organised from simplest to most complete:

    empty_repo   -> a directory with no files at all
    minimal_repo -> just enough to be detected as a Python project
    full_repo    -> all expected best-practice files present

Tests that only need a specific file should use ``tmp_path`` directly
and create that file themselves — see the organization check tests for
an example. Use these fixtures when a test needs a realistic repo context
rather than a single targeted file.
"""

from pathlib import Path

import pytest


@pytest.fixture
def empty_repo(tmp_path: Path) -> Path:
    """An empty directory standing in for a repository root."""
    return tmp_path


@pytest.fixture
def minimal_repo(tmp_path: Path) -> Path:
    """A directory with only the files required to detect as Python."""
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'test'\n")
    return tmp_path


@pytest.fixture
def full_repo(tmp_path: Path) -> Path:
    """A directory with all expected best-practice files present.

    Use this fixture for integration-style tests that need a complete
    project layout rather than targeting a single check.
    """
    # Root-level plain files
    root_files = [
        "README.md",
        "CITATION.cff",
        "LICENSE.md",
        "CHANGELOG.md",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        ".gitignore",
        ".editorconfig",
        ".copier-answers.yml",
        "mkdocs.yml",
    ]
    for name in root_files:
        if name == "README.md":
            orcid = "0000-0000-0000-000x"
        else:
            orcid = "ABC"
        (tmp_path / name).write_text(f"# {name}\n{orcid}\n")

    # pyproject.toml with a [tool.ruff] section
    (tmp_path / "pyproject.toml").write_text(
        "[project]\nname = 'test'\nauthors = [{name = 'Test Author'}]\n\n[tool.ruff]\n"
    )

    # GitHub Actions workflow
    workflows = tmp_path / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "actions.yml").write_text("name: ci\n")

    # Tests directory
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_example.py").write_text("# placeholder\n")

    # Data directories
    (tmp_path / "data" / "raw").mkdir(parents=True)
    (tmp_path / "data" / "output").mkdir(parents=True)

    # VSCode hint
    (tmp_path / ".vscode").mkdir()
    (tmp_path / ".vscode" / "extensions.json").write_text("{}\n")

    # Docs directory:
    (tmp_path / "docs").mkdir()

    (tmp_path / "CITATION.cff").write_text(
        "cff-version: 1.2.0\norcid: 0000-0000-0000-000X\n"
    )

    # src layout
    src_pkg = tmp_path / "src" / "test_pkg"
    src_pkg.mkdir(parents=True)
    (src_pkg / "__init__.py").write_text("")

    return tmp_path
