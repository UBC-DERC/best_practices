# src/best_practices/badge.py
"""shields.io endpoint badge generator.

Writes a JSON file compatible with the
`shields.io endpoint <https://shields.io/endpoint>`_ format. The file
can be committed to a repository and referenced by a dynamic badge in
the README::

    ![Best Practices](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/<owner>/<repo>/main/best-practices-badge.json)

The badge updates automatically each time the JSON file is re-committed,
with no SVG generation required.

Colour thresholds (applied to the overall percentage score):

    ≥ 90 %  →  brightgreen
    ≥ 75 %  →  green
    ≥ 50 %  →  yellow
    < 50 %  →  red
"""

import json
from pathlib import Path

from best_practices.models import TopicScore


def _badge_color(pct: int) -> str:
    """Return the shields.io colour name for a given percentage score.

    Args:
        pct: Overall score as a whole-number percentage (0–100).

    Returns:
        One of ``"brightgreen"``, ``"green"``, ``"yellow"``, or ``"red"``.
    """
    if pct >= 90:
        return "brightgreen"
    if pct >= 75:
        return "green"
    if pct >= 50:
        return "yellow"
    return "red"


def render_badge(topic_scores: list[TopicScore]) -> dict:
    """Build the shields.io endpoint payload from topic scores.

    Args:
        topic_scores: The list of ``TopicScore`` instances from
                      ``score_by_topic()``.

    Returns:
        A dictionary ready to serialise as the shields.io endpoint JSON.
    """
    passed = sum(ts.passed for ts in topic_scores)
    total = sum(ts.total for ts in topic_scores)
    pct = round(passed / total * 100) if total else 0
    return {
        "schemaVersion": 1,
        "label": "best practices",
        "message": f"{passed} / {total}",
        "color": _badge_color(pct),
    }


def write_badge(topic_scores: list[TopicScore], path: Path) -> None:
    """Serialise the badge payload to a JSON file.

    Args:
        topic_scores: The list of ``TopicScore`` instances from
                      ``score_by_topic()``.
        path:         Destination file path for the JSON output.
    """
    payload = render_badge(topic_scores)
    Path(path).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
