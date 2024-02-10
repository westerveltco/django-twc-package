from __future__ import annotations

from textwrap import dedent

import pytest
from jinja2 import Environment
from jinja2 import FileSystemLoader

from extensions.context import DJMAIN_MIN_PY
from extensions.context import MinMaxVersion
from extensions.context import NoxfileVersions


@pytest.fixture
def environment():
    return Environment(loader=FileSystemLoader(""))


@pytest.mark.parametrize(
    "versions, expected",
    [
        ([], ("", "")),
        (
            ["3.8", "3.9", "3.10", "3.11", "3.12"],
            ("3.8", "3.12"),
        ),
        (["3.8"], ("3.8", "3.8")),
        (["3.10", "3.9", "3.8"], ("3.8", "3.10")),
    ],
)
def test_min_max_version(environment, versions, expected):
    context = {
        "python_versions": versions,
        "django_versions": versions,
    }

    context = MinMaxVersion(environment).hook(context)

    assert context["python_min_version"] == expected[0]
    assert context["python_max_version"] == expected[1]
    assert context["django_min_version"] == expected[0]
    assert context["django_max_version"] == expected[1]


@pytest.mark.parametrize(
    "context, expected",
    [
        (
            {
                "python_versions": ["3.8", "3.9", "3.10", "3.11", "3.12"],
                "django_versions": ["3.2", "4.2", "5.0"],
            },
            (
                dedent(
                    """\
                    PY38 = "3.8"
                    PY39 = "3.9"
                    PY310 = "3.10"
                    PY311 = "3.11"
                    PY312 = "3.12"
                    PY_VERSIONS = [PY38, PY39, PY310, PY311, PY312]
                    PY_DEFAULT = PY_VERSIONS[0]
                    PY_LATEST = PY_VERSIONS[-1]"""
                ),
                dedent(
                    """\
                    DJ32 = "3.2"
                    DJ42 = "4.2"
                    DJ50 = "5.0"
                    DJ_VERSIONS = [DJ32, DJ42, DJ50]
                    DJ_LTS = [DJ32, DJ42]
                    DJ_DEFAULT = DJ_LTS[0]
                    DJ_LATEST = DJ_VERSIONS[-1]"""
                ),
            ),
        ),
        (
            {
                "python_versions": ["3.8", "3.9", "3.10", "3.11", "3.12"],
                "django_versions": ["3.2", "4.2", "5.0"],
                "test_django_main": True,
            },
            (
                dedent(
                    """\
                    PY38 = "3.8"
                    PY39 = "3.9"
                    PY310 = "3.10"
                    PY311 = "3.11"
                    PY312 = "3.12"
                    PY_VERSIONS = [PY38, PY39, PY310, PY311, PY312]
                    PY_DEFAULT = PY_VERSIONS[0]
                    PY_LATEST = PY_VERSIONS[-1]"""
                ),
                dedent(
                    f"""\
                    DJ32 = "3.2"
                    DJ42 = "4.2"
                    DJ50 = "5.0"
                    DJMAIN = "main"
                    DJMAIN_MIN_PY = PY{DJMAIN_MIN_PY.replace(".", "")}
                    DJ_VERSIONS = [DJ32, DJ42, DJ50, DJMAIN]
                    DJ_LTS = [DJ32, DJ42]
                    DJ_DEFAULT = DJ_LTS[0]
                    DJ_LATEST = DJ_VERSIONS[-2]"""
                ),
            ),
        ),
    ],
)
def test_noxfile_versions(environment, context, expected):
    context = NoxfileVersions(environment).hook(context)

    assert context["nox_python_versions"] == expected[0]
    assert context["nox_django_versions"] == expected[1]
