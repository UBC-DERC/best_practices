# src/best_practices/language.py
"""Language detection for repository evaluation.

The detected language(s) determine which checks are applicable. Detection
is intentionally simple for the MVP: it inspects the presence of well-known
indicator files rather than parsing file extensions across the whole tree.

Indicator files
---------------
``pyproject.toml``
    Present in virtually every modern Python project (PEP 517/518).
``DESCRIPTION``
    The mandatory metadata file for an R package (CRAN convention).

An empty list is returned when neither indicator file is present. The
caller treats an empty detected-language list as "unknown — run all checks"
so that language-agnostic checks still run rather than silently skipping
everything.
"""

from pathlib import Path

from best_practices.models import Language


def detect_language(repo_root: Path) -> list[Language]:
    """Detect the language(s) of a repository from indicator files.

    Examines the presence of ``pyproject.toml`` (Python) and ``DESCRIPTION``
    (R) at the repository root. Both may be present in a polyglot project.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        A list of detected ``Language`` values. Returns an empty list when
        no indicator file is found; callers treat this as "run all checks".
    """
    detected: list[Language] = []
    if (repo_root / "pyproject.toml").is_file():
        detected.append("python")
    if (repo_root / "DESCRIPTION").is_file():
        detected.append("r")
    return detected
