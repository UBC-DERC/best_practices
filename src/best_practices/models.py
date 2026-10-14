# src/best_practices/models.py
"""Pydantic models for the best_practices check system.

Four classes form the data model:

    CheckMeta          <- shared metadata (name, description, topic, ...)
    ├── Check          <- adds method: Callable  (check specification)
    └── CheckResult    <- adds present, detail   (outcome record)

    TopicScore         <- aggregated pass/total counts for one topic area

Contributors only ever instantiate Check. CheckResult is produced
by run_check() and should not be constructed directly. TopicScore is
produced by score_by_topic() and should not be constructed directly.
"""

from collections.abc import Callable
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict

Language = Literal["python", "r"]
Topic = Literal["attribution", "community", "building", "organization"]


class CheckMeta(BaseModel):
    """Metadata shared by every check definition and its result.

    Attributes:
        name:        Short identifier, e.g. ``"readme_exists"``.
        description: Human-readable sentence describing what is checked.
        topic:       Which of the four goal areas this check belongs to.
        reference:   URL to the guidance page for this check.
        languages:   Language ecosystems this check applies to. An empty
                     list means the check runs regardless of detected
                     language. Add new languages to the ``Language`` type
                     alias to extend support.
    """

    name: str
    description: str
    topic: Topic
    reference: str
    languages: list[Language] = []


class Check(CheckMeta):
    """A check specification: shared metadata plus the function that runs it.

    Attributes:
        method: A named function that accepts a repo root ``Path`` and
                returns ``True`` (present) or ``False`` (absent).
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    method: Callable[[Path], bool]


class CheckResult(CheckMeta):
    """The outcome of running a Check against a repository.

    Returned by ``run_check()``; fully serialisable to JSON.

    Attributes:
        present: ``True`` if the check passed, ``False`` if it failed.
        detail:  A short sentence explaining the result.
    """

    present: bool
    detail: str


class TopicScore(BaseModel):
    """Aggregated score for one topic area.

    Produced by ``score_by_topic()``; do not construct directly.

    Attributes:
        topic:  The topic being scored.
        passed: Number of checks that returned ``True``.
        total:  Total number of applicable checks in this topic.
    """

    topic: Topic
    passed: int
    total: int

    @property
    def score(self) -> float:
        """Fraction of checks passed, in the range 0.0–1.0.

        Returns 0.0 when there are no applicable checks (total == 0)
        rather than raising a ZeroDivisionError.
        """
        return self.passed / self.total if self.total > 0 else 0.0

    @property
    def score_pct(self) -> int:
        """Score as a whole-number percentage (0–100)."""
        return round(self.score * 100)
