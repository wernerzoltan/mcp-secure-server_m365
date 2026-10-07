"""
Validate the complete OAuth flow end-to-end.
Instead of testing individual methods separately, we now test the full sequence:

    Create Token
        ↓
    Validate Token
        ↓
    Extract User
        ↓
    Retrieve JWKS

"""

import pytest

from mcp_server.auth.mock_oauth_provider import (
    MockOAuthProvider,
)


@pytest.mark.asyncio
async def test_complete_authentication_flow():
    """
    End-to-end OAuth flow.
    """

    provider = MockOAuthProvider()

    #
    # Generate token
    #
    token = await provider.create_token(
        user_id="john"
    )

    #
    # Validate token
    #
    is_valid = await provider.validate_token(
        token
    )

    #
    # Extract user
    #
    user_id = await provider.get_user_id(
        token
    )

    #
    # Retrieve JWKS
    #
    jwks = await provider.get_jwks()

    assert is_valid is True
    assert user_id == "john"
    assert "keys" in jwks

@pytest.mark.asyncio
async def test_expired_token_flow():
    """
    Expired tokens must fail validation.
    """

    provider = MockOAuthProvider()

    token = await provider.create_token(
        user_id="john",
        expires_in_seconds=-1,
    )

    result = await provider.validate_token(
        token
    )

    assert result is False


@pytest.mark.asyncio
async def test_invalid_token_flow():
    """
    Invalid token must fail.
    """

    provider = MockOAuthProvider()

    result = await provider.validate_token(
        "not-a-token"
    )

    assert result is False