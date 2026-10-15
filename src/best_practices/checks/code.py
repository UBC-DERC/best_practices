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

from best_practices.models import Check

CHECKS: list[Check] = []
