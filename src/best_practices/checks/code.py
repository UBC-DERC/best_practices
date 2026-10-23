# src/best_practices/checks/code.py
"""Coding-group best-practice checks.

Checks in this module verify that a repository follows basic coding
conventions: test modules, linters/ruff, type checking

Each check function:
  - Takes a single argument: ``repo_root`` (a ``pathlib.Path``).
  - Returns ``True`` if the practice is present, ``False`` if absent.
  - Has a full docstring with Args and Returns sections.

To add a check, write the function and append a ``Check(...)`` instance
to the ``CHECKS`` list at the bottom of this file.
"""

import tomllib
from pathlib import Path
from typing import Any

from best_practices.models import Check

_REFERENCE = "https://ubc-derc.github.io/derc_copier/copier/building/"


def check_pyproject_exists(repo_root: Path) -> bool:
    """Return True if the user is using a pyproject.toml file.

    pyproject.toml is a machine and human readable file that helps
    manage project dependencies, and also communicates important
    project metadata to help produce reproducible workflows.
    """
    return (repo_root / "pyproject.toml").is_file()


def check_ruff_configured(repo_root: Path) -> bool:
    """Return True if ruff is included as a tool for the project.

    Ruff is a new, and fairly fast code formatting and checking tool that
    helps ensure high quality, readable code. This is particularly important
    for helping to catch bugs early in development, and for sharing code
    among partners.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if ``ruff`` is included in a requirements or pyproject.toml file.
    """
    pyproject = repo_root / "pyproject.toml"
    ruff_config: bool = (repo_root / "ruff.toml").is_file() or (
        repo_root / ".ruff.toml"
    ).is_file()
    if pyproject.is_file():
        try:
            data: dict[str, Any] = tomllib.loads(pyproject.read_text(encoding="utf-8"))
            pyproj_ruff_check: bool = "ruff" in data.get("tool", {})
        except tomllib.TOMLDecodeError:
            return False
    else:
        pyproj_ruff_check = False
    return pyproj_ruff_check or ruff_config


CHECKS: list[Check] = [
    Check(
        name="pyproject_exists",
        description="There is a pyproject.toml file present at the repository root.",
        topic="building",
        reference=_REFERENCE,
        method=check_pyproject_exists,
        languages=["python"],
    ),
    Check(
        name="ruff_is_configured",
        description="We see ruff configuration in the pyproject file (under `tool.ruff`) or in `ruff.toml` or `.ruff.toml` files.",
        topic="building",
        reference=_REFERENCE,
        method=check_ruff_configured,
        languages=["python"],
    ),
]
