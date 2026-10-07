import logging

from mcp_server.config.settings import (
    Settings,
)


def test_default_log_level():
    settings = Settings()

    assert settings.log_level == "INFO"


def test_log_level_exists_in_logging():
    settings = Settings()

    level = getattr(
        logging,
        settings.log_level,
        None,
    )

    assert level is not None