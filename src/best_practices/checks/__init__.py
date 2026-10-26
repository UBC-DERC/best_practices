# src/best_practices/checks/__init__.py
"""Best-practice check functions, grouped by topic.

Each sub-module exposes a module-level ``CHECKS: list[Check]`` that is
collected here into a single ``REGISTRY`` list. Callers import ``REGISTRY``
from this module; they do not need to know which sub-module a check lives in.

To add a new check:
  1. Write a named function in the appropriate sub-module.
  2. Append a ``Check(...)`` instance to that module's ``CHECKS`` list.
  3. Write at least two tests (pass and fail) in the corresponding test file.
  The registry picks it up automatically — no changes needed here.
"""

from best_practices.checks.attribution import CHECKS as _ATTRIBUTION_CHECKS
from best_practices.checks.code import CHECKS as _BUILDING_CHECKS
from best_practices.checks.community import CHECKS as _COMMUNITY_CHECKS
from best_practices.checks.organization import CHECKS as _ORGANIZATION_CHECKS
from best_practices.models import Check

REGISTRY: list[Check] = (
    _ATTRIBUTION_CHECKS + _ORGANIZATION_CHECKS + _COMMUNITY_CHECKS + _BUILDING_CHECKS
)
