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

## [2024.9]

### Added

- `just` is now installed when building documentation on Read the Docs.
- `just _cog` private command added to run the relevant docs through the `cog` tool. Useful for automatically generating documentation for cli tools such as `just`. Currently, only the `just` commands are documented, but this can be expanded in the future (e.g. `nox` or Django management commands).

### Changed

- Moved generation of the lists Python and Django versions in `noxfile.py` from Jinja2 template logic to Jinja2 extensions using `copier-template-extensions`.

## [2024.8]

### Fixed

- Added missing `SECRET_KEY` setting to `tests/settings.py` to fix the `test` and `testall` commands on certain Django versions.

## [2024.7]

## Fixed

- Added the correct Jinja escape tags so that the `test` and `testall` commands render correctly when generating a template.

## [2024.6]

### Changed

- Added additional descriptions to example headings in `CHANGELOG.md`.
- `test` and `testall` Justfile commands now can take positional arguments to run specific tests.
- `lint` Justfile command now runs the relevant `nox` command instead of `pre-commit` directly.

## [2024.5]

### Changed

- Moved the common test settings from plugin to `tests/settings.py` and added a note to the installation notes in README.

### Removed

- Removed the `tests/plugins/dj_settings.py` file.

## [2024.4]

### Changed

- `generate-examples` command now removes the previous example directory before generating an example.
- Moved common test settings to separate plugin at `tests/plugins/dj_settings.py`.

### Removed

- Removed the dummy `tests/settings.py`.

## [2024.3]

### Added

- A new `generate-examples` command to the `Justfile` for generating all of the examples at once.

### Changed

- Added a few missing configuration settings to the `pyproject.toml` file.

## [2024.2]

### Changed

- Addressed a number of linting issues and nitpicks, detailed in issue [#3](https://github.com/westerveltco/django-twc-package/issues/3).

## [2024.1]

Initial release! 🎉

### Added

- Initial project template.
- Initial documentation.
- Initial tests.
- Initial CI/CD (GitHub Actions).

### New Contributors

- Josh Thomas <josh@joshthomas.dev> (maintainer)

[unreleased]: https://github.com/westerveltco/django-twc-package/compare/v2024.9...HEAD
[2024.1]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.1
[2024.2]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.2
[2024.3]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.3
[2024.4]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.4
[2024.5]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.5
[2024.6]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.6
[2024.7]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.7
[2024.8]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.8
[2024.9]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.9
