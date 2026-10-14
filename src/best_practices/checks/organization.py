# src/best_practices/checks/organization.py
"""Organization-group best-practice checks.

Checks in this module verify that a repository follows basic structural
conventions: folder layout, changelog, version control hygiene, etc.

Each check function:
  - Takes a single argument: ``repo_root`` (a ``pathlib.Path``).
  - Returns ``True`` if the practice is present, ``False`` if absent.
  - Has a full docstring with Args and Returns sections.

To add a check, write the function and append a ``Check(...)`` instance
to the ``CHECKS`` list at the bottom of this file.
"""

from pathlib import Path

from best_practices.models import Check

_REFERENCE = "https://ubc-derc.github.io/derc_copier/features/"


# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------


def check_repo_has_files(repo_root: Path) -> bool:
    """Return True if the repository root contains at least one item.

    An entirely empty directory is not a meaningful repository. This check
    is the simplest possible signal that the project has been initialised.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if any file or directory exists directly under repo_root.
    """
    return any(repo_root.iterdir())


# ---------------------------------------------------------------------------
# Check registry for this module
# ---------------------------------------------------------------------------

CHECKS: list[Check] = [
    Check(
        name="repo_has_files",
        description="The repository root contains at least one file or directory.",
        topic="organization",
        reference=_REFERENCE,
        method=check_repo_has_files,
    ),
]
