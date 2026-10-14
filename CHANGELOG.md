# Changelog

All notable changes to `best_practices` are documented here.
Versions follow [Calendar Versioning](https://calver.org): `YY.MM[.MICRO]`.
The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [26.10] – 2026-10-14

**Generated using Claude Sonnet 5.5 based on existing git history**

First release. Provides a command-line tool and Python API for auditing a
GitHub repository against a set of community best practices drawn from the
[DERC Copier template](https://ubc-derc.github.io/derc_copier/features/).
Results are returned as a Markdown report and an optional shields.io badge.

### Added

**Command-line interface**

- `best-practices <repo>` — runs all applicable checks and prints a Markdown
  report to stdout.
- `--output <file>` — write the report to a file instead of stdout.
- `--badge <file>` — write a shields.io-compatible JSON badge to a file.
- `--fail-under <0–100>` — exit with a non-zero status if the overall score
  falls below the given percentage (useful in CI pipelines).

**Python API**

- `run_checks(repo_root, detected)` — run all registry checks against a
  repository path and return a list of `CheckResult` objects.
- `score_by_topic(results)` — aggregate results into per-topic `TopicScore`
  objects (includes `.score` as a float and `.score_pct` as an integer).
- `detect_language(repo_root)` — detect whether a repository is Python, R,
  or both, and return a `list[Language]`; an empty list means the language
  could not be determined and all universal checks apply.

**Data models** (`best_practices.models`)

- `CheckMeta` / `Check` / `CheckResult` — Pydantic v2 models for describing,
  running, and recording the outcome of a single check.
- `TopicScore` — per-topic summary (passed, total, score, score\_pct).
- `Language = Literal["python", "r"]` — language identifiers; a check with
  an empty `languages` list applies to every repository.
- `Topic = Literal["attribution", "community", "building", "organization"]` —
  the four areas checked; only "attribution", "community", and "organization"
  have active checks in this release.

**Checks — Attribution** (6 checks, language-universal)

Verifies that the repository carries the information others need to cite and
credit the work: a README, a LICENSE, a CITATION.cff with an ORCID, author
metadata in `pyproject.toml`, and a CHANGELOG.

**Checks — Organization** (1 check, language-universal)

- `repo_has_files` — confirms that the repository is non-empty (at least one
  tracked file exists).

**Checks — Community** (4 checks)

- `mkdocs_yaml` (Python) — checks for an `mkdocs.yaml` configuration file.
- `docs_folder` (Python, R) — checks for a `docs/` directory.
- `man_folder` (R) — checks for a `man/` directory (R package documentation).
- `check_funder_ref` (Python, R) — scans the README for common Canadian and
  US funder names (NSF, NSERC, CIHR, SSHRC, NCE, CRC) and a funding
  statement.

**Reports and badges**

- `render_markdown(results, scores)` — returns a Markdown string grouping
  results by topic with ✓/✗ symbols, per-topic pass counts, and an overall
  score line.
- `render_badge(scores)` — returns a dict suitable for shields.io endpoint
  badges; colour thresholds are ≥ 90 % brightgreen, ≥ 75 % green,
  ≥ 50 % yellow, < 50 % red.
- `write_badge(scores, path)` — convenience wrapper that serialises the badge
  dict to JSON and writes it to a file.

**Test suite**

- Unit tests for language detection, badge rendering, Markdown reports,
  `run_checks()`, attribution checks (16 tests), and organization checks.
- Shared pytest fixtures: `empty_repo`, `minimal_repo`, `full_repo`.
- Coverage configured to fail under 70 %; branch coverage enabled.

**Tooling**

- `ruff` for linting and formatting; Google-convention docstrings enforced via
  `extend-select = ["D"]`.
- `ty` for static type checking.
- `uv` for dependency and environment management.

### Deferred to a future release

The following are planned but out of scope for v26.10:

- `checks/building.py` — CI workflow presence, tests directory, ruff config,
  `.editorconfig`, VSCode extension hints, `src/` layout.
- Remaining `checks/organization.py` checks — data directories, CHANGELOG
  presence, `.gitignore`, `.copier-answers.yml`.
- `tests/test_integration.py` — self-review smoke test (running the tool
  against its own repository and expecting a score of 100 %).
- Git version-tag check.
- Selective check configuration — ruff-style `select` / `ignore` lists via a
  `best-practices.yaml` file or `[tool.best_practices]` in `pyproject.toml`.
- Multi-signal check design — allowing a single check to pass on any one of
  several signals (e.g. `mkdocs.yaml` OR `docs/`).

---

<!-- Add new versions above this line, oldest at the bottom. -->
