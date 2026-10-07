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

def test_is_production_true():
    settings = Settings(app_env="production")
    assert settings.is_production is True


def test_is_production_false_for_development():
    settings = Settings(app_env="development")
    assert settings.is_production is False


def test_using_mock_services_false_when_real_services_enabled():
    settings = Settings(use_real_services=True)
    assert settings.using_mock_services is False


def test_using_mock_services_true_when_real_services_disabled():
    settings = Settings(use_real_services=False)
    assert settings.using_mock_services is True


def test_is_production_case_insensitive():
    settings = Settings(app_env="PRODUCTION")
    assert settings.is_production is True