from mcp_server.config.settings import (
    Settings,
)


def test_okta_settings_exist():
    settings = Settings()

    assert settings.okta_issuer
    assert settings.okta_client_id
    assert settings.okta_client_secret


def test_key_vault_setting_exists():
    settings = Settings()

    assert settings.azure_key_vault_url


def test_confluence_setting_exists():
    settings = Settings()

    assert settings.confluence_base_url


def test_mock_mode_default():
    settings = Settings()

    assert settings.use_real_services is False