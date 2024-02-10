# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

<!--
## [Version Number]

### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
-->

## [Unreleased]

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

[unreleased]: https://github.com/westerveltco/django-twc-package/compare/v2024.5...HEAD
[2024.5]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.5
[2024.4]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.4
[2024.3]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.3
[2024.2]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.2
[2024.1]: https://github.com/westerveltco/django-twc-package/releases/tag/v2024.1
