# DERC Makes Coding Better

The [derc-best-practices](https://github.com/UBC-DERC/best_practices) is a toolset that was developed to help early-career researchers build better software projects as part of their research. It is intended to pair with the `derc-copier`, which helps set up Python and R projects from a template.

The `derc-copier` website contains documentation about best practices, and how and why to engage in particular best practices. Starting with `derc-copier` is the best way to engage in best practices. If you can't start from scratch(ish), then we recommend using `derc-best-practices` to help get yourself on track, and learn along the way.

## Principles of Best Practices

Best practices may sometimes seem like extra work, but they exist, by and large, to reduce the amount of work you have to do. Code formatting tools exist to help make code more readable, the inclusion of [ORCIDs](https://orcid.org) makes sure pepole know who you are, the use of a Code of Conduct makes sure that collaborators engage with the project in a respectful manner.

All of these elements come from hard-earned life lessons from people who have been working in these spaces or others.

The goal of this project is to help communicate these best practices in a way that is:

* **easy to use**: It should be able to run as a simple command line module, or as part of a CI workflow.
* **easy to understand**: Results should be clear and unambiguous. Tests will be pass/fail and should link directly to supporting documents to help folks adopt best coding practices early.
* **easy to modify**: groups that have additional requirements should be able to add new tests as needed using a simple template.
* **well documented**: The workflow and the underlying code should be well documented to support long term sustainability.
* **authoritative**: Coding best practices should be supported by clear guidance, with emphasis on well-supported toolsets or external standards.

## Quick Start

If you have [`uv` installed](https://docs.astral.sh/uv/getting-started/installation/), you can get started with any project by running this script from the project folder:

```bash
uvx derc-best-practices .
```

That's all you've got to do (you should really install `uv` though, it's pretty great).

Once you run the script you'll get a handy output that shows you all the things you've done right in your project:

```text
# Best Practices Report

**Overall score: 12 / 12 (100%)**

## Attribution
Score: 6 / 6 (100%)

- ✓ README.md is present at the repository root. ([guidance](https://ubc-derc.github.io/derc_copier/attribution/readmes.md))
- ✓ CITATION.cff is present at the repository root. ([guidance](https://ubc-derc.github.io/derc_copier/attribution/citation.md))
- ✓ A licence file (LICENSE, LICENSE.md, or LICENSE.txt) is present. ([guidance](https://ubc-derc.github.io/derc_copier/attribution/))
- ✓ pyproject.toml is present at the repository root. ([guidance](https://ubc-derc.github.io/derc_copier/attribution/))
- ✓ pyproject.toml declares at least one author in [project.authors]. ([guidance](https://ubc-derc.github.io/derc_copier/attribution/))
- ✓ CITATION.cff includes an ORCID identifier for at least one author. ([guidance](https://ubc-derc.github.io/derc_copier/attribution/citation.md))

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

The report is formatted using Markdown, which lets you add the report to your documentation. The script also can generate a fancy badge, which would let you add something like this:

![Best Practices](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/UBC-DERC/best_practices/main/best-practices-badge.json)

To your homepage.
