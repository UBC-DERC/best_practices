<!-- badges: start -->
[![lifecycle](https://img.shields.io/badge/lifecycle-lifecycle_experimental-orange.svg)]()

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![core_actions](https://github.com/UBC-DERC/best_practices/actions/workflows/actions.yml/badge.svg)](https://github.com/UBC-DERC/best_practices/actions/workflows/actions.yml)

![Best Practices](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/UBC-DERC/best_practices/main/best-practices-badge.json)
<!-- badges: end -->

# best-practices

## Goal

The goal of this project is to implement a set of tools that can survey a research project to provide users with a set of tools and documentation that will help support the adoption of coding best practices. Most importantly, it is to support the adoption of best-practices among early-career researchers through actionable checklists and clear guidance.

## Audience

This project is intended to support **early-career researchers** who may not be familiar with software development tools, principles of FAIR data management, testing and linting. For example:

* Antônia is working on a project using R. She has her data and scripts in a single folder on her laptop. She has only started learning to use R during her Masters, but wants to improve her skills, and keep her project bug free.
* Adamu is building a Python package as part of his work. In trying to collaborate with others, he'd like to make sure that everyone sticks to the same project standards.
* Koto is a scientist, supervising students. They want to teach their students to write code as part of their projects, but there isn't a comprehensive course for them to take.

## Approach

The package `best-practices` should be:

* **easy to use**: It should be able to run as a simple commandline module, or as part of a CI workflow.
* **easy to understand**: Results should be clear and unambiguous. Tests will be pass/fail and should link directly to supporting documents to help folks adopt best coding practices early.
* **easy to modify**: groups that have additional requirements should be able to add new tests as needed using a simple template.
* **well documented**: The workflow and the underlying code should be well documented to support long term sustainability.
* **authoratative**: Coding best practices should be supported by clear guidance, with emphasis on well-supported toolsets or external standards.

## Quick Start

A very simple use case is to run the tool on this repository:

```bash
git clone https://github.com/UBC-DERC/best_practices.git
cd best_practices
uv sync
uv run best-practices .
```

This will identify the different tests that `best-practices` ran. The script will provide an output indicating any deficiencies so that folks can then address these. All tests will be linked to some documentation around the best practice that they identify:

```bash
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

## Github Actions

This project can also be run through Github Actions, where it will generate both a best practices report, and JSON
to be used in a [shields.io](https://shields.io) badge.

```yaml
# .github/workflows/best-practices.yml (in the USER's repo)
name: Best Practices

on: [push, pull_request]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: UBC-DERC/best_practices@main
        with:
          fail-under: 0
          badge: best-practices-badge.json
          output: best-practices-report.md
```

## Contribution

This project was developed by:

* [![ORCID](https://img.shields.io/badge/ORCID-0000--0002--2700--4605-green.svg)](https://orcid.org/0000-0002-2700-4605): Simon Goring

This project was developed in part as an attempt to build a tool using an AI assistant ([Claude Sonnet 4.6](https://claude.ai)). Simon Goring conceived of the idea. Simon Goring developed the class structure and architecture for the package. Initial checks and cli scripts were written using Sonnet. The CHANGELOG was maintained using Sonnet, and internal project checklists were also managed using Sonnet 4.6.

Contributions to this repository are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Installing this Package

To install `best_practices` from this GitHub repository, either install using a graphical tool such as GitKraken or GitHub Desktop, or install from the console using:

```bash
git clone https://github.com/UBC-DERC/best_practices.git
cd best_practices
uv sync
```

## How to Use `best-practices`

### What Gets Checked

`best-practices` organizes project best practices into four main categories, further expanded in the [`derc_copier`](https://ubc-derc.github.io/derc_copier)

[Building Better Code](https://ubc-derc.github.io/derc_copier/copier/building/) — style, testing, and the tooling that keeps your code clean and reliable.
[Attribution](https://ubc-derc.github.io/derc_copier/copier/attribution/) — citation, licensing, and describing your work so it can be found and credited.
[Building Community](https://ubc-derc.github.io/derc_copier/copier/community/) — codes of conduct, contribution guides, and documentation that make a project welcoming.
[Staying Organized](https://ubc-derc.github.io/derc_copier/copier/organization/) — folder structure, package and library management, version control, and changelogs.

There is overlap across all these categories, but individual tests ultimately help us understand how we are doing at meeting our goals for building sustainable software for the scientific community.

### Setting up the `uv` environment

This project uses `uv` as a package manager and to manage virtual environments. To use development tools including `ruff` and `ty`, you first need to install and synchronize the project. First check that you have [`uv` installed](https://docs.astral.sh/uv/getting-started/installation/).

```bash
uv sync
```

Now you are ready to work on the project.

## Funding Statement

This project is funded in part through support from Farm Credit Canada.

---

![UBC Logo and name as a wide figure.](assets/ubc-logo-2018-fullsig-blue-rgb72.jpg)
