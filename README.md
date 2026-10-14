<!-- badges: start -->
[![lifecycle](https://img.shields.io/badge/lifecycle-lifecycle_planning-crimson.svg)]()

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- badges: end -->

# best-practices

## Goal

Monitoring project best practices with a Python observer. The goal of this project is to implement a set of tools that can survey a package to provide users with a set of tools and documentation to help support the adoption of coding best practices.

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
uv add --dev best-practices
uv run best-practices .
```

This will identify the different tests that `best-practices` ran. The script will provide an output indicating any deficiencies so that folks can then address these. All tests will be linked to some documentation around the best practice that they identify:

```bash
# Best Practices Report

**Overall score: 7 / 7 (100%)**

## Attribution
Score: 6 / 6 (100%)

- ✓ README.md is present at the repository root. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ CITATION.cff is present at the repository root. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ A licence file (LICENSE, LICENSE.md, or LICENSE.txt) is present. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ pyproject.toml is present at the repository root. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ pyproject.toml declares at least one author in [project.authors]. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
- ✓ CITATION.cff includes an ORCID identifier for at least one author. ([guidance](https://ubc-derc.github.io/derc_copier/features/))

## Organization
Score: 1 / 1 (100%)

- ✓ The repository root contains at least one file or directory. ([guidance](https://ubc-derc.github.io/derc_copier/features/))
```

## Contribution

This project was developed by:

* [![ORCID](https://img.shields.io/badge/ORCID-0000--0002--2700--4605-green.svg)](https://orcid.org/0000-0002-2700-4605): Simon Goring

This project was developed in part as an attempt to build a tool using an AI assistant ([Claude Sonnet 4.6]()). Simon Goring conceived of the idea. Simon Goring developed the class structure and architecture for the package. Initial checks and cli scripts were written using Sonnet.

Contributions to this repository are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Installing this Package

To install `best_practices` from this GitHub repository, either install using a graphical tool such as GitKraken or GitHub Desktop, or install from the console using:

```bash
git clone https://github.com/UBC-DERC/best_practices.git
cd best_practices
uv sync
```

## How to Use this Repository

`best-practices` organizes project best practices into four main categories, further expanded in the [`derc_copier`](https://ubc-derc.github.io/derc_copier):

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

<!--
A short statement about your funding sources.
-->

---

![UBC Logo and name as a wide figure.](assets/ubc-logo-2018-fullsig-blue-rgb72.jpg)
