from mcp_server.config.settings import (
    Settings,
)


def test_default_is_development():
    settings = Settings()

    assert settings.is_development is True


def test_default_is_not_production():
    settings = Settings()

    assert settings.is_production is False


def test_default_uses_mock_services():
    settings = Settings()

    assert settings.using_mock_services is True


def test_default_not_using_real_services():
    settings = Settings()

    assert settings.using_real_services is False