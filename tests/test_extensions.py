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
    return Environment(loader=FileSystemLoader(""), autoescape=True)


@pytest.mark.parametrize(
    ("versions", "expected"),
    [
        ([], ("", "")),
        (
            ["3.10", "3.11", "3.12", "3.13", "3.14"],
            ("3.10", "3.14"),
        ),
        (["3.10"], ("3.10", "3.10")),
        (["3.12", "3.11", "3.10"], ("3.10", "3.12")),
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
    ("context", "expected"),
    [
        (
            {
                "python_versions": ["3.10", "3.11", "3.12", "3.13", "3.14"],
                "django_versions": ["5.2", "6.0", "6.1"],
            },
            (
                dedent(
                    """\
                    PY310 = "3.10"
                    PY311 = "3.11"
                    PY312 = "3.12"
                    PY313 = "3.13"
                    PY314 = "3.14"
                    PY_VERSIONS = [PY310, PY311, PY312, PY313, PY314]
                    PY_DEFAULT = PY_VERSIONS[0]
                    PY_LATEST = PY_VERSIONS[-1]"""
                ),
                dedent(
                    """\
                    DJ52 = "5.2"
                    DJ60 = "6.0"
                    DJ61 = "6.1"
                    DJ_VERSIONS = [DJ52, DJ60, DJ61]
                    DJ_LTS = [DJ52]
                    DJ_DEFAULT = DJ_LTS[0]
                    DJ_LATEST = DJ_VERSIONS[-1]"""
                ),
            ),
        ),
        (
            {
                "python_versions": ["3.10", "3.11", "3.12", "3.13", "3.14"],
                "django_versions": ["5.2", "6.0", "6.1"],
                "test_django_main": True,
            },
            (
                dedent(
                    """\
                    PY310 = "3.10"
                    PY311 = "3.11"
                    PY312 = "3.12"
                    PY313 = "3.13"
                    PY314 = "3.14"
                    PY_VERSIONS = [PY310, PY311, PY312, PY313, PY314]
                    PY_DEFAULT = PY_VERSIONS[0]
                    PY_LATEST = PY_VERSIONS[-1]"""
                ),
                dedent(
                    f"""\
                    DJ52 = "5.2"
                    DJ60 = "6.0"
                    DJ61 = "6.1"
                    DJMAIN = "main"
                    DJMAIN_MIN_PY = PY{DJMAIN_MIN_PY.replace(".", "")}
                    DJ_VERSIONS = [DJ52, DJ60, DJ61, DJMAIN]
                    DJ_LTS = [DJ52]
                    DJ_DEFAULT = DJ_LTS[0]
                    DJ_LATEST = DJ_VERSIONS[-2]"""
                ),
            ),
        ),
        (
            {
                # Python versions that do not include DJMAIN_MIN_PY fall back to
                # a string literal instead of an undefined `PYXYZ` name
                "python_versions": ["3.10", "3.11"],
                "django_versions": ["5.2"],
                "test_django_main": True,
            },
            (
                dedent(
                    """\
                    PY310 = "3.10"
                    PY311 = "3.11"
                    PY_VERSIONS = [PY310, PY311]
                    PY_DEFAULT = PY_VERSIONS[0]
                    PY_LATEST = PY_VERSIONS[-1]"""
                ),
                dedent(
                    f"""\
                    DJ52 = "5.2"
                    DJMAIN = "main"
                    DJMAIN_MIN_PY = "{DJMAIN_MIN_PY}"
                    DJ_VERSIONS = [DJ52, DJMAIN]
                    DJ_LTS = [DJ52]
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


@pytest.mark.parametrize(
    "context, expected",
    [
        # Django 6.0+ requires Python 3.12+
        (
            {
                "python_versions": ["3.10", "3.11", "3.12", "3.13", "3.14"],
                "django_versions": ["5.2", "6.0", "6.1"],
                "test_django_main": True,
            },
            [
                {
                    "min_py": "3.12",
                    "min_py_ref": "PY312",
                    "django_versions": ["6.0", "6.1"],
                    "django_refs": ["DJ60", "DJ61"],
                }
            ],
        ),
        # nothing to skip if every supported Python satisfies every Django
        (
            {
                "python_versions": ["3.12", "3.13", "3.14"],
                "django_versions": ["5.2", "6.0", "6.1"],
                "test_django_main": True,
            },
            [],
        ),
        (
            {
                "python_versions": ["3.10", "3.11", "3.12"],
                "django_versions": ["5.2"],
                "test_django_main": False,
            },
            [],
        ),
        (
            {
                "python_versions": ["3.10", "3.11", "3.12"],
                "django_versions": ["5.2", "6.0"],
                "test_django_main": False,
            },
            [
                {
                    "min_py": "3.12",
                    "min_py_ref": "PY312",
                    "django_versions": ["6.0"],
                    "django_refs": ["DJ60"],
                }
            ],
        ),
    ],
)
def test_django_min_py_groups(environment, context, expected):
    context = NoxfileVersions(environment).hook(context)

    assert context["nox_django_min_py_groups"] == expected
