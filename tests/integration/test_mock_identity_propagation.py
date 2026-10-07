import pytest

from mcp_server.auth.mock_oauth_provider import (
    MockOAuthProvider,
)


@pytest.mark.asyncio
async def test_identity_propagation():
    """
    Verify identity survives the full flow.
    """

    provider = MockOAuthProvider()

    token = await provider.create_token(
        user_id="alice"
    )

    user_id = await provider.get_user_id(
        token
    )

    assert user_id == "alice"