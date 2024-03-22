# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

<!--
## [${version}]
### Added - for new features
### Changed - for changes in existing functionality
### Deprecated - for soon-to-be removed features
### Removed - for now removed features
### Fixed - for any bug fixes
### Security - in case of vulnerabilities
[${version}]: https://github.com/westerveltco/django-twc-package/releases/tag/v${version}
-->

## [Unreleased]

### Changed

-   Now using `uv` for dependency management in template.

## [2024.14]

### Added

-   Now using [`westerveltco/setup-ci-action`](https://github.com/westereltco/setup-ci-action) for common Python and Node.js CI/CD setup. This action sets up a Python and Node.js environment with caching and installs all dependencies for a project.
-   Added example generation job to `test.yml` GitHub Actions workflow.

### Changed

-   Updated the `ruff` configuration from deprecated settings to the new `ruff` configuration.

## [2024.13]

### Fixed

-   Removed the unneeded `RUN_TESTS` environment variable from the GitHub Actions workflow.

## [2024.12]

### Added

-   Added the `current_version` in `.copier/package.yml` answers file to `bumpver` configuration.

### Fixed

-   Fixed a bug with the Python and Django versions in `.pre-commit-config.yaml`.

## [2024.11]

### Changed

-   All `pre-commit` hooks have been updated to use the latest versions of the tools.
    -   `django-upgrade` to 1.16.0
    -   `language-formatters-pre-commit-hooks` to v2.12.0
    -   `prettier` to v4.0.0-alpha.8
    -   `ruff-pre-commit` to 0.2.1
    -   `rustywind` to 0.21.0
    -   `validate-pyproject` to v0.16
-   `djhtml` has been swapped out in favor of `djLint` for HTML formatting.
-   `nox -l --json` is now used to generate GitHub Actions matrix for testing.

## [2024.10]

### Removed

-   `create-release-pr` command from `Justfile` was removed and moved to a personal script.

### Fixed

-   Path to `just` command documentation in `_cog` command.

## [2024.9]

### Added

-   `just` is now installed when building documentation on Read the Docs.
-   `just _cog` private command added to run the relevant docs through the `cog` tool. Useful for automatically generating documentation for cli tools such as `just`. Currently, only the `just` commands are documented, but this can be expanded in the future (e.g. `nox` or Django management commands).

### Changed

-   Moved generation of the lists Python and Django versions in `noxfile.py` from Jinja2 template logic to Jinja2 extensions using `copier-template-extensions`.

## [2024.8]

### Fixed

-   Added missing `SECRET_KEY` setting to `tests/settings.py` to fix the `test` and `testall` commands on certain Django versions.

## [2024.7]

## Fixed

-   Added the correct Jinja escape tags so that the `test` and `testall` commands render correctly when generating a template.

## [2024.6]

### Changed

-   Added additional descriptions to example headings in `CHANGELOG.md`.
-   `test` and `testall` Justfile commands now can take positional arguments to run specific tests.
-   `lint` Justfile command now runs the relevant `nox` command instead of `pre-commit` directly.

## [2024.5]

### Changed

-   Moved the common test settings from plugin to `tests/settings.py` and added a note to the installation notes in README.

### Removed

-   Removed the `tests/plugins/dj_settings.py` file.

## [2024.4]

### Changed

-   `generate-examples` command now removes the previous example directory before generating an example.
-   Moved common test settings to separate plugin at `tests/plugins/dj_settings.py`.

### Removed

-   Removed the dummy `tests/settings.py`.

## [2024.3]

### Added

-   A new `generate-examples` command to the `Justfile` for generating all of the examples at once.

### Changed

-   Added a few missing configuration settings to the `pyproject.toml` file.

## [2024.2]

### Changed

-   Addressed a number of linting issues and nitpicks, detailed in issue [#3](https://github.com/westerveltco/django-twc-package/issues/3).

## [2024.1]

Initial release! 🎉

### Added

-   Initial project template.
-   Initial documentation.
-   Initial tests.
-   Initial CI/CD (GitHub Actions).

### New Contributors

-   Josh Thomas <josh@joshthomas.dev> (maintainer)

[unreleased]: https://github.com/westerveltco/django-twc-package/compare/v2024.14...HEAD
[2024.1]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.1
[2024.2]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.2
[2024.3]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.3
[2024.4]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.4
[2024.5]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.5
[2024.6]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.6
[2024.7]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.7
[2024.8]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.8
[2024.9]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.9
[2024.10]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.10
[2024.11]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.11
[2024.12]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.12
[2024.13]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.13
[2024.14]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.14
