# django-twc-package

[![Copier](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/joshuadavidthomas/7c88611504b557ff7aa2a7524ad996e2/raw/4ba6834953dd8a14afc3dbb7bb41f49f181a59bf/badge.json)](https://copier.readthedocs.io)

`django-twc-package` is the template for a Django package at The Westervelt Company. This template is a starting point for creating a new Django package that can be installed and used in other projects.

It is tailored to the needs of The Westervelt Company, but unlike our Django project template [`django-twc-project`](https://github.com/westerveltco/django-twc-project), it is much more generic and thus should be useful for a wider audience.

## Features

This template is built using [Copier](https://copier.readthedocs.io) and includes the following features:

- Modern Python project with only a [`pyproject.toml`](https://packaging.python.org/en/latest/specifications/pyproject-toml/#pyproject-toml-spec) file
  - [`hatchling`](https://github.com/pypa/hatch) for a build backend
  - [`uv`](https://github.com/astral-sh/uv) for dependency management
- [`mypy`](https://github.com/python/mypy) and [`django-stubs`](https://github.com/typeddjango/django-stubs) for static type checking
- [`pytest`](https://github.com/pytest-dev/pytest) for testing
  - [`coverage`](https://github.com/nedbat/coveragepy) and [`pytest-cov`](https://github.com/pytest-dev/pytest-cov) for test coverage
  - [`model_bakery`](https://github.com/model-bakers/model_bakery) for easy model creation in tests
  - [`pytest-django`](https://github.com/pytest-dev/pytest-django) for Django pytest helpers
  - [`pytest-randomly`](https://github.com/pytest-dev/pytest-randomly) and [`pytest-reverse`](https://github.com/adamchainz/pytest-reverse) for keeping tests honest
  - [`pytest-xdist`](https://github.com/pytest-dev/pytest-xdist) for parallel testing, because ain't nobody got time for a slow test suite
- [`nox`](https://github.com/theacodes/nox) for testing across multiple versions of Python and Django, linting, and formatting
- [`bumpver`](https://github.com/mbarkhau/bumpver) for version bumping
  - Package can be configured for either [Semantic Versioning](https://semver.org) or [CalVer](https://calver.org) via Copier prompts
- [`just`](https://github.com/casey/just) for running common development tasks
- Automatic linting and formatting via [`pre-commit`](https://github.com/pre-commit/pre-commit)
  - [`blacken-docs`](https://github.com/adamchainz/blacken-docs) because `ruff` doesn't
  - [`django-upgrade`](https://github.com/adamchainz/django-upgrade) for keeping Django up to date automatically
  - [`djlint`](https://github.com/rtts/djlint) for linting and formatting Django templates
  - [`ruff`](https://github.com/astral-sh/ruff) for blazingly fast formatting and linting
  - [`prettier`](https://github.com/prettier/prettier) for formatting CSS, JavaScript, TypeScript, and YAML
  - [`validate-pyproject`](https://github.com/abravalheri/validate-pyproject) for ensuring that `pyproject.toml` is valid
  - `pretty-format-toml` via [`language-formatters-pre-commit-hooks`](https://github.com/macisamuele/language-formatters-pre-commit-hooks) for TOML formatting
- Documentation built with [`Sphinx`](https://github.com/sphinx-doc/sphinx), [`MyST-Parser`](https://github.com/executablebooks/MyST-Parser), and the [`furo`](https://github.com/pradyunsg/furo) theme
  - Includes a `.readthedocs.yml` file for deploying documentation to [Read the Docs](https://readthedocs.org)
- CI/CD with [GitHub Actions](https://github.com/features/actions)
  - Testing across multiple versions of Python and Django
  - Type checking
  - Code coverage
  - Automatic publishing to [PyPI](https://pypi.org) when a new release is created
    - Includes a check for the most recent test run on the `main` branch, ensuring that the package is only published if the tests pass
    - Published to PyPI using their new [Trusted Publishers](https://docs.pypi.org/trusted-publishers/) publishing mechanism
  - [Dependabot](https://dependabot.com/) for automatic action version updates

## Requirements

- [Copier](https://copier.readthedocs.io)
- [Copier Template Extensions](https://github.com/copier-org/copier-templates-extensions)

## Installation

You will need to install the required packages before being able to generate a project using this template. They are automatically included in the development dependencies of the generated project, so this is a one-time by-hand installation.

You can use a tool like `pipx` or `uv tool install` for this:

```bash
pipx install copier copier-templates-extensions
# or for you bleeding-edge folks
uv tool install copier copier-templates-extensions
```

## Usage

To use this template, you will need to install [Copier](https://copier.readthedocs.io) and then run the following command:

```bash
copier copy --trust gh:westerveltco/django-twc-package <destination>
```

> [!NOTE]
> The `--trust` flag is used to because this template uses `copier-template-extensions` to simplify some of the Jinja templating. You cannot use this template without trusting it. Please review the files within the [`extensions`](extensions) directory to see what is being done.

After running the above command, you will be prompted to fill in some information about your package. Once you have filled in the necessary information, Copier will generate the package for you.

Once the package has been generated, you should create or update the `tests/conftest.py` file to include the following:

```python
from __future__ import annotations

import logging

from django.conf import settings

from .settings import DEFAULT_SETTINGS

pytest_plugins = []  # type: ignore


def pytest_configure(config):
    logging.disable(logging.CRITICAL)

    settings.configure(
        **DEFAULT_SETTINGS,
        **TEST_SETTINGS,
    )


TEST_SETTINGS = {}
```

`tests.settings.DEFAULT_SETTINGS` contains some common default settings, specifically chosen to ensure a speedy test suite. Any settings that are specific to your package should be added to `tests.conftest.TEST_SETTINGS`. By keeping these separate, it should allow for future updates to this template to be easily merged into your package.

## Examples

Examples are provided in the [`examples`](examples) directory.

## Contributing

As this template is mainly for internal use at The Westervelt Company, we do not generally accept contributions from external sources. However, if you have any suggestions or issues, please feel free to open an issue or pull request.

## License

`django-twc-package` is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
