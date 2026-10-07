from mcp_server.config.settings import (
    Settings,
)


def test_default_app_name():
    settings = Settings()

    assert settings.app_name == (
        "mcp-secure-server"
    )


def test_default_environment():
    settings = Settings()

    assert settings.app_env == (
        "development"
    )


def test_default_log_level():
    settings = Settings()

    assert settings.log_level == (
        "INFO"
    )


def test_default_mock_mode():
    settings = Settings()

    assert settings.use_real_services is False