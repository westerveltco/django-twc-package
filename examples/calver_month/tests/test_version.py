from __future__ import annotations

from semver_project import __version__


def test_version():
    assert __version__ == "2024.2.1"
