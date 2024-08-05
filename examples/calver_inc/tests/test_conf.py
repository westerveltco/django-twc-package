from __future__ import annotations

import pytest

from calver_inc1_project.conf import app_settings


def test_app_settings():
    # stub test until `calver-inc1-project` requires custom app settings
    with pytest.raises(AttributeError):
        assert app_settings.foo
