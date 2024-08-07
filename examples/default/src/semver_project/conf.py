from __future__ import annotations

from dataclasses import dataclass

from django.conf import settings

from ._typing import override

SEMVER_PROJECT_SETTINGS_NAME = "SEMVER_PROJECT"


@dataclass(frozen=True)
class AppSettings:
    @override
    def __getattribute__(self, __name: str) -> object:
        user_settings = getattr(settings, SEMVER_PROJECT_SETTINGS_NAME, {})
        return user_settings.get(__name, super().__getattribute__(__name))  # pyright: ignore[reportAny]


app_settings = AppSettings()
