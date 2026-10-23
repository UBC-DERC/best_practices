<!-- badges: start -->
[![lifecycle](https://img.shields.io/badge/lifecycle-lifecycle_beta-yellow.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Beta)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![core_actions](https://github.com/UBC-DERC/best_practices/actions/workflows/actions.yml/badge.svg)](https://github.com/UBC-DERC/best_practices/actions/workflows/actions.yml)
![Best Practices](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/UBC-DERC/best_practices/main/best-practices-badge.json)
<!-- badges: end -->

# derc-best-practices

- [derc-best-practices](#derc-best-practices)
  - [Project Goals](#project-goals)
  - [Project Audience](#project-audience)
  - [Approach](#approach)
    - [What Gets Checked](#what-gets-checked)
  - [Quick Start](#quick-start)
    - [Trying out the Package](#trying-out-the-package)
    - [Best Practices on a Local Project](#best-practices-on-a-local-project)
    - [As a GitHub Action](#as-a-github-action)
  - [Contribution](#contribution)
  - [Funding Statement](#funding-statement)

## Project Goals

The goal of this project is to implement a set of tools that can survey a research project to provide users with a set of tools and documentation that will help support the adoption of coding best practices. Most importantly, it is to support the adoption of best-practices among early-career researchers through actionable checklists and clear guidance.

## Project Audience

This project is intended to support **early-career researchers** who may not be familiar with software development tools, principles of FAIR data management, testing and linting. For example:

* Antônia is working on a project using R. She has her data and scripts in a single folder on her laptop. She has only started learning to use R during her Masters, but wants to improve her skills, and keep her project bug free.
* Adamu is building a Python package as part of his work. In trying to collaborate with others, he'd like to make sure that everyone sticks to the same project standards.
* Koto is a scientist, supervising students. They want to teach their students to write code as part of their projects, but there isn't a comprehensive course for them to take.

## Approach

The package `derc-best-practices` should be:

* **easy to use**: It should be able to run as a simple command line module, or as part of a CI workflow.
* **easy to understand**: Results should be clear and unambiguous. Tests will be pass/fail and should link directly to supporting documents to help folks adopt best coding practices early.
* **easy to modify**: groups that have additional requirements should be able to add new tests as needed using a simple template.
* **well documented**: The workflow and the underlying code should be well documented to support long term sustainability.
* **authoritative**: Coding best practices should be supported by clear guidance, with emphasis on well-supported toolsets or external standards.

### What Gets Checked

`derc-best-practices` organizes project best practices into four main categories, further expanded in the [`derc_copier`](https://ubc-derc.github.io/derc_copier) tool we developed for starting new coding projects.

  * [Building Better Code](https://ubc-derc.github.io/derc_copier/copier/building/) — style, testing, and the tooling that keeps your code clean and reliable. [**tests coming soon**]
  * [Attribution](https://ubc-derc.github.io/derc_copier/copier/attribution/) — citation, licensing, and describing your work so it can be found and credited.
  * [Building Community](https://ubc-derc.github.io/derc_copier/copier/community/) — codes of conduct, contribution guides, and documentation that make a project welcoming.
  * [Staying Organized](https://ubc-derc.github.io/derc_copier/copier/organization/) — folder structure, package and library management, version control, and changelogs.

There is overlap across all these categories, but individual tests ultimately help us understand how we are doing at meeting our goals for building sustainable software for the scientific community.

## Quick Start

If you have [`uv` installed](https://docs.astral.sh/uv/getting-started/installation/), you can get started with any project right away:

```bash
uvx derc-best-practices .
```

### Trying out the Package

A very simple test case is to run the tool on its own repository before you try it on one of your own. *Note the difference in naming between the repository and the command line*, the repository is called `best_practices`, but the actual command is `derc-best-practices`. This was done to ensure the package could be added to [PyPI](https://pypi.org/), the Python Package Index:

```bash
git clone https://github.com/UBC-DERC/best_practices.git
cd best_practices
uv sync
uv run derc-best-practices .
```

The script above will identify the different tests that `derc-best-practices` ran and return an output indicating any deficiencies. All tests will be linked to documentation around the best practice they identify. The following report was generated when we had 12 tests as part of the project:

```text
# Best Practices Report

**Overall score: 12 / 12 (100%)**

## Attribution
Score: 6 / 6 (100%)

- ✓ README.md is present at the repository root. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ CITATION.cff is present at the repository root. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ A licence file (LICENSE, LICENSE.md, or LICENSE.txt) is present. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ pyproject.toml is present at the repository root. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ pyproject.toml declares at least one author in [project.authors]. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ CITATION.cff includes an ORCID identifier for at least one author. ([guidance](https://ubc-derc.github.io/derc_copier/features/))

## Community
Score: 3 / 3 (100%)

- ✓ The repository root has an mkdocs.y[a]ml file that would be used to build documentation. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ The repository root has a docs folder that would contain the documentation. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ Funders are identified in the repository README file. ([guidance](https://ubc-derc.github.io/derc_copier/features/))

## Organization
Score: 3 / 3 (100%)

- ✓ The repository root contains at least one file or directory. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ The project has a dedicated data folder. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ The repository uses git for version control. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
```

### Best Practices on a Local Project

For a **Python project managed with `uv`**, add it as a `dev` tool (something you use to improve the project, not something your code needs to run):

```bash
uv add --dev derc-best-practices
uv run derc-best-practices .
```

The `.` at the end of the command indicates that you are running the script in the current folder.

For an **R project** (or any folder without a [`pyproject.toml`](https://ubc-derc.github.io/derc_copier/features), a recommended file for Python packages) use `uvx` from inside the project folder. Nothing is installed into your project:

```bash
uvx derc-best-practices .
```

 If you have a number of projects that you'd like to check, and they're all in folders inside a `Documents` folder:

```text
  Documents/
  ├── ProjectOne/
  ├── ProjectTwo/
  └── ProjectThree/
```

You could run the script from inside your `Documents` folder using:

```bash
uvx derc-best-practices ./ProjectOne
```

Or, more explicitly:

```bash
uvx derc-best-practices FULLPROJECTPATH
```

Where the `FULLPROJECTPATH` might be `"C:/Users/My Name/Documents/ProjectOne"` on a Windows system, or `/home/myname/Documents/ProjectOne` on Linux and `/Users/myname/Documents/ProjectOne` on a Mac.

### As a GitHub Action

This project can also be run through [GitHub Actions](https://github.com/features/actions), where it will generate both a best practices report, and JSON
to be used in a [shields.io](https://shields.io) badge.

```yaml
# .github/workflows/best-practices.yml (in your repository)
name: Best Practices

on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: write   # needed to commit the badge file

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: UBC-DERC/best_practices@v26.10

      - name: Show the report on the workflow run page
        run: cat best-practices-report.md >> "$GITHUB_STEP_SUMMARY"

      - name: Commit the badge (main branch only)
        if: github.ref == 'refs/heads/main'
        uses: stefanzweifel/git-auto-commit-action@v5  # check for the latest major version
        with:
          file_pattern: best-practices-badge.json
          commit_message: "chore: update best-practices badge [skip ci]"
```

If you use the action then you can add a badge similar to the one on this page, using:

```markdown
![Best Practices](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/<username>/<repo>/main/best-practices-badge.json)
```

After adding the badge and pushing to the `main` branch of your repository there may be a delay during which the badge on your `README` reads `invalid`. This is because the script must run successfully in the cloud.

## Contribution

This project was developed by:

* [![ORCID](https://img.shields.io/badge/ORCID-0000--0002--2700--4605-green.svg)](https://orcid.org/0000-0002-2700-4605): Simon Goring

This project was developed in part as an attempt to build a tool using an AI assistant ([Claude Sonnet 4.6](https://claude.ai)). Simon Goring conceived of the idea. Simon Goring developed the class structure and architecture for the package. Initial checks and cli scripts were written using Sonnet. The CHANGELOG was maintained using Sonnet, and internal project checklists were also managed using Sonnet 4.6. Following early project scaffolding by Sonnet 4.6 later AI use was limited to review and suggested configuration, which was applied manually (and review shifted to [Claude Opus 5.5](https://claude.ai)).

If you'd like to contribute to this project please follow the [CONTRIBUTING](CONTRIBUTING.md) guide. All contributions and contributors are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Funding Statement

This project is funded in part through support from Farm Credit Canada.

---

![UBC Logo and name as a wide figure.](assets/ubc-logo-2018-fullsig-blue-rgb72.jpg)
