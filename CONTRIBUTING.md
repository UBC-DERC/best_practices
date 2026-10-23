# Contribute to the project

Contributions and issues are most welcome! All issues and pull requests are handled through [GitHub](https://github.com/UBC-DERC/best_practices/issues).

Please check for existing issues before filing a new one. If you have a great idea but it involves big changes, please
file a ticket before making a pull request! We want to make sure you don't spend
your time coding something that might not fit the scope of the project.

## Coding Practice

This project uses `uv` as a package manager and to manage virtual environments. To use development tools including `ruff` and `ty`, you first need to install and synchronize the project. First check that you have [`uv` installed](https://docs.astral.sh/uv/getting-started/installation/).

```bash
uv sync
```

We use a `ruff` and `ty` pre-commit hook (see [`.pre-commit-config.yaml`](.pre-commit-config.yaml)) to ensure code quality and standardization. To enable this hook when you are developing code, use the following commands:

```bash
uv run pre-commit install
uv run pre-commit run --all-files   # one-time pass over the existing code
```

The `pre-commit` hook will run both `ruff` and `ty`.

## Code Development

Any checks, tests or other project infrastructure should run cleanly. All coding changes should be followed by running `ruff`, `ty` and `pytest` to ensure code passes these checks:

```bash
uv run ruff format  # Covered by the pre-commit hook.
uv run ruff check . # Covered by the pre-commit hook.
uv run ty check     # Covered by the pre-commit hook.
uv run pytest
```

These tests also run on a push to the `develop` and `main` branches and on pull requests, so it's nice to have them pass before we get to the repository.

Pull requests should target the `develop` branch and include a `CHANGELOG` entry under "Unreleased" that can be included in the current [`CHANGELOG.md`](CHANGELOG.md).

### Checks

#### Check Functions

Adding a new check involves editing the `/src/best_practices/checks/...` topic file for that test. For example, a new test associated with *attribution* should be added to [`src/best_practices/checks/attribution.py`](src/best_practices/checks/attribution.py).

All check function names should begin with `check_.....`.

The test should return only a `bool` response. Either the check is there, or it isn't. We intend (at some point) to move to a more hierarchical system, but for now, if you feel like you need "parts" to your test, split the test up, rather than testing multiple things in a single test.

**Remember** Tests should be easy to understand for a lay user, and resolution should be straightforward.

Guidance for the check should be added as a URL, either as a constant (for example, the `_REFERENCE` constant placeholder), or as a direct URL in the `CHECK()` object.

Once a new check is added, add it to the `CHECKS` registry at the bottom of the topic `py` file. The `Check()` object should be structured as:

```python
(
    Check(
        name="descriptive_name_with_underscores",
        description="Explain what the test is testing, what is missing? what should be added?",
        topic="attribution",  # one of: attribution, community, building, or organization
        reference="URL to the best practice guidance",
        method=check_name_of_the_function,
        languages=["python"],  # Will run using both R and Python if omitted.
    ),
)
```

#### Testing

All new "best practices" **checks** should have at least two tests in the pytest `checks` folder, ideally in the file associated with the test topic (*e.g.*, [`tests/checks/test_attribution.py`](tests/checks/test_attribution.py)):

1. A positive test (the element is present)
2. A negative test (the element is absent)

Once these tests have been added and they pass, then please feel free to open a pull request.

### Package Changes

Changes to the report, language detection or other elements should be added to their relevant files. Any changes to package behaviour must be accompanied by additions to the testing suite. We hope to maintain a system that follows a modified Test-Driven Development approach, tracking project outcomes and behaviour.

See above for testing and package checks needed before making a pull request.
