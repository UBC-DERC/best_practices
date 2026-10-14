# src/best_practices/checks/community.py
"""Community-group best-practice checks.

Checks in this module verify that a repository follows basic community
conventions: documentation, funding acknowledgements, codes of conduct.

Each check function:
  - Takes a single argument: ``repo_root`` (a ``pathlib.Path``).
  - Returns ``True`` if the practice is present, ``False`` if absent.
  - Has a full docstring with Args and Returns sections.

To add a check, write the function and append a ``Check(...)`` instance
to the ``CHECKS`` list at the bottom of this file.
"""

import re
from pathlib import Path

from best_practices.models import Check

_REFERENCE = "https://ubc-derc.github.io/derc_copier/features/"


# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------

def check_mkdocs_yaml(repo_root: Path) -> bool:
    """Return True if the repository root contains an mkdocs yaml file.

    This check is to see if the user has set up mkdocs. It's likely only a
    Python test, and may not be the only type of setup file, for example if
    folks are shifting to Sphinx.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if ```mkdocs.y[a]ml``` exists directly under repo_root.
    """
    return (repo_root / "mkdocs.yaml").is_file() or (repo_root / "mkdocs.yml").is_file()


def check_docs_folder(repo_root:Path) -> bool:
    """Return True if the repository root contains a ```docs``` folder.

    This check is to see if the user has set up a documentation folder called docs.
    Ultimately, the documentation folder could be called anything. Maybe something
    worth looking at later.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if ```docs``` exists as a folder directly under repo_root.
    """
    return (repo_root/"docs").is_dir()

def check_man_folder_pkg(repo_root:Path) -> bool:
    """Return True if the repository root contains a ```man``` folder.

    This check is to see if the user has set up a documentation folder called
    ```man```. This isn't the only kind of documentation available in R, but
    it's one of the options.

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if ```man``` exists as a folder directly under repo_root.
    """
    return (repo_root/"man").is_dir()

def check_funder_ref(repo_root:Path) -> bool:
    """Return True if the repository root contains a reference to a funding organization.

    This check is to see if the user has referenced an external funding source. We look
    for either a funding organization, or a statement that says "funded in part".

    Args:
        repo_root: Path to the root of the repository being evaluated.

    Returns:
        True if there's some funding statement in README.md.
    """
    readme = repo_root / "README.md"
    if not readme.is_file():
      return False
    contents:str = readme.read_text(encoding="utf-8")
    funder_name:bool = re.search(pattern=r"NSF|NSERC|CIHR|SSHRC|NCE|CRC",string=contents) is not None
    funding_statement:bool = re.search(pattern=r"funded in part",string=contents) is not None
    return funder_name or funding_statement

# ---------------------------------------------------------------------------
# Check registry for this module
# ---------------------------------------------------------------------------

CHECKS: list[Check] = [
    Check(
        name="mkdocs_yaml",
        description="The repository root has an mkdocs.y[a]ml file that would be used to build documentation.",
        topic="community",
        reference=_REFERENCE,
        method=check_mkdocs_yaml,
        languages=["python"],
    ),
    Check(
        name="docs_folder",
        description="The repository root has a docs folder that would contain the documentation.",
        topic="community",
        reference=_REFERENCE,
        method=check_docs_folder,
        languages=["r", "python"],
        ),
    Check(
        name="man_folder",
        description="The repository root has a man folder for R documentation.",
        topic="community",
        reference=_REFERENCE,
        method=check_man_folder_pkg,
        languages=["r"],
      ),
    Check(
        name="funding_reference",
        description="Funders are identified in the repository README file.",
        topic="community",
        reference=_REFERENCE,
        method = check_funder_ref,
        languages=["r","python"]
    ),
]
