from mcp_server.secrets.secret_store import (
    SecretStore,
)


def test_interface_exists():
    assert SecretStore is not None


def test_has_get_secret():
    assert hasattr(
        SecretStore,
        "get_secret",
    )


def test_has_secret_exists():
    assert hasattr(
        SecretStore,
        "secret_exists",
    )