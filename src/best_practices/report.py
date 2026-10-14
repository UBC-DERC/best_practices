# src/best_practices/report.py
"""Markdown report renderer.

Takes the outputs of ``run_checks()`` and ``score_by_topic()`` and
produces a human-readable Markdown string. The report is organised by
topic so a reader can see at a glance which areas need attention.

The rendered string can be printed to stdout, written to a file with
``--output``, or posted as a pull-request comment in a GitHub Action.
"""

from best_practices.models import CheckResult, Topic, TopicScore

# Canonical display order — matches the four goal areas in the docs.
_TOPIC_ORDER: list[Topic] = ["attribution", "community", "building", "organization"]


def render_markdown(
    results: list[CheckResult],
    topic_scores: list[TopicScore],
) -> str:
    """Render a Markdown best-practices report.

    Args:
        results:      The list of ``CheckResult`` instances from
                      ``run_checks()``.
        topic_scores: The list of ``TopicScore`` instances from
                      ``score_by_topic()``.

    Returns:
        A Markdown-formatted string suitable for printing or writing to
        a file.
    """
    lines: list[str] = []

    # Overall summary
    overall_passed = sum(ts.passed for ts in topic_scores)
    overall_total = sum(ts.total for ts in topic_scores)
    overall_pct = round(overall_passed / overall_total * 100) if overall_total else 0

    lines.append("# Best Practices Report")
    lines.append("")
    lines.append(
        f"**Overall score: {overall_passed} / {overall_total} ({overall_pct}%)**"
    )
    lines.append("")

    # Per-topic sections
    score_by_topic_map = {ts.topic: ts for ts in topic_scores}

    for topic in _TOPIC_ORDER:
        topic_results = [r for r in results if r.topic == topic]
        if not topic_results:
            continue

        ts = score_by_topic_map.get(topic)
        score_str = f"{ts.passed} / {ts.total} ({ts.score_pct}%)" if ts else ""

        lines.append(f"## {topic.capitalize()}")
        if score_str:
            lines.append(f"Score: {score_str}")
        lines.append("")

        for r in topic_results:
            lines.append(f"- {r.detail} ([guidance]({r.reference}))")

        lines.append("")

    return "\n".join(lines)
