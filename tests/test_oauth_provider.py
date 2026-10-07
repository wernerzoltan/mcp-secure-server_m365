from mcp_server.auth.oauth_provider import (
    OAuthProvider,
)


def test_interface_exists():
    assert OAuthProvider is not None


def test_interface_has_validate_token():
    assert hasattr(
        OAuthProvider,
        "validate_token",
    )


def test_interface_has_get_user_id():
    assert hasattr(
        OAuthProvider,
        "get_user_id",
    )