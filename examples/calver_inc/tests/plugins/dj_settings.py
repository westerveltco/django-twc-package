from __future__ import annotations

import logging

import pytest
from django.test.utils import override_settings


def pytest_configure(config):
    logging.disable(logging.CRITICAL)


@pytest.fixture(autouse=True)
def default_test_settings():
    with override_settings(**TEST_SETTINGS):
        yield


TEST_SETTINGS = {
    "ALLOWED_HOSTS": ["*"],
    "DEBUG": False,
    "CACHES": {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    },
    "DATABASES": {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        },
    },
    "EMAIL_BACKEND": "django.core.mail.backends.locmem.EmailBackend",
    "LOGGING_CONFIG": None,
    "PASSWORD_HASHERS": [
        "django.contrib.auth.hashers.MD5PasswordHasher",
    ],
}
