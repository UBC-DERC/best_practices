# src/best_practices/checks/attribution.py
"""Attribution-group best-practice checks.

Checks in this module verify that a repository clearly identifies its
authors, licence, and how to cite the work. These are the first things
a reader or collaborator looks for, and are foundational to open-science
best practices.

Each check function:
  - Takes a single argument: ``repo_root`` (a ``pathlib.Path``).
  - Returns ``True`` if the practice is present, ``False`` if absent.
  - Has a full docstring with Args and Returns sections.

To add a check, write the function and append a ``Check(...)`` instance
to the ``CHECKS`` list at the bottom of this file.
"""

import tomllib
from pathlib import Path

from best_practices.models import Check

_REFERENCE = "https://ubc-derc.github.io/derc_copier/attribution/"
_README = "https://ubc-derc.github.io/derc_copier/attribution/readmes.md"
_CITATION = "https://ubc-derc.github.io/derc_copier/attribution/citation.md"

# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------


def check_readme_exists(repo_root: Path) -> bool:
    """Return True if README.md exists at the repository root.

    A README is the front page of a project: it tells visitors what the
    project does and how to get started. Its absence is the single most
    common barrier to reuse.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if ``README.md`` is present at the repository root.
    """
    return (repo_root / "README.md").is_file()


def check_citation_exists(repo_root: Path) -> bool:
    """Return True if CITATION.cff exists at the repository root.

    A ``CITATION.cff`` file (Citation File Format) tells users exactly how
    to cite the software. GitHub and Zenodo both recognise the format and
    surface it automatically.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if ``CITATION.cff`` is present at the repository root.
    """
    return (repo_root / "CITATION.cff").is_file()


def check_license_exists(repo_root: Path) -> bool:
    """Return True if a licence file exists at the repository root.

    Without an explicit licence, software is legally "all rights reserved"
    even when publicly visible. Any of the common naming conventions is
    accepted: ``LICENSE``, ``LICENSE.md``, or ``LICENSE.txt``.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if at least one recognised licence filename is present.
    """
    candidates = ["LICENSE", "LICENSE.md", "LICENSE.txt"]
    return any((repo_root / name).is_file() for name in candidates)


def check_pyproject_exists(repo_root: Path) -> bool:
    """Return True if pyproject.toml exists at the repository root.

    ``pyproject.toml`` is the modern, PEP-517-compliant way to declare a
    Python package's metadata, build system, and tool configuration. Its
    presence signals that the project is properly packaged.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if ``pyproject.toml`` is present at the repository root.
    """
    return (repo_root / "pyproject.toml").is_file()


def check_author_in_pyproject(repo_root: Path) -> bool:
    """Return True if pyproject.toml declares at least one author.

    A package without an author entry makes it impossible for users to
    know who to contact or how to credit the work. The check reads the
    ``[project.authors]`` array defined in PEP 621.

    Returns False (without raising) if ``pyproject.toml`` is absent,
    unreadable, or does not contain a ``[project]`` table.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if ``project.authors`` exists and contains at least one entry.
    """
    pyproject = repo_root / "pyproject.toml"
    if not pyproject.is_file():
        return False
    try:
        data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError:
        return False
    authors = data.get("project", {}).get("authors", [])
    return len(authors) > 0


def check_orcid_in_citation(repo_root: Path) -> bool:
    """Return True if CITATION.cff contains an ORCID identifier.

    An ORCID (Open Researcher and Contributor ID) is a persistent
    identifier for researchers. Including one in the citation file
    disambiguates authors and supports automated credit tracking.

    Returns False (without raising) if ``CITATION.cff`` is absent.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if ``CITATION.cff`` is present and contains the string
        ``"orcid:"``.
    """
    citation = repo_root / "CITATION.cff"
    if not citation.is_file():
        return False
    return "orcid:" in citation.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Check registry for this module
# ---------------------------------------------------------------------------

CHECKS: list[Check] = [
    Check(
        name="readme_exists",
        description="README.md is present at the repository root.",
        topic="attribution",
        reference=_README,
        method=check_readme_exists,
    ),
    Check(
        name="citation_exists",
        description="CITATION.cff is present at the repository root.",
        topic="attribution",
        reference=_CITATION,
        method=check_citation_exists,
    ),
    Check(
        name="license_exists",
        description="A licence file (LICENSE, LICENSE.md, or LICENSE.txt) is present.",
        topic="attribution",
        reference=_REFERENCE,
        method=check_license_exists,
    ),
    Check(
        name="pyproject_exists",
        description="pyproject.toml is present at the repository root.",
        topic="attribution",
        reference=_REFERENCE,
        method=check_pyproject_exists,
        languages=["python"],
    ),
    Check(
        name="author_in_pyproject",
        description="pyproject.toml declares at least one author in [project.authors].",
        topic="attribution",
        reference=_REFERENCE,
        method=check_author_in_pyproject,
        languages=["python"],
    ),
    Check(
        name="orcid_in_citation",
        description="CITATION.cff includes an ORCID identifier for at least one author.",
        topic="attribution",
        reference=_CITATION,
        method=check_orcid_in_citation,
    ),
]
