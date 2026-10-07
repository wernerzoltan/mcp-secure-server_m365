import pytest

from mcp_server.auth.mock_oauth_provider import (
    MockOAuthProvider,
)


@pytest.mark.asyncio
async def test_jwks_contains_keys():
    provider = MockOAuthProvider()

    jwks = await provider.get_jwks()

    assert "keys" in jwks


@pytest.mark.asyncio
async def test_jwks_contains_one_key():
    provider = MockOAuthProvider()

    jwks = await provider.get_jwks()

    assert len(jwks["keys"]) == 1


@pytest.mark.asyncio
async def test_jwks_key_attributes():
    provider = MockOAuthProvider()

    jwks = await provider.get_jwks()

    key = jwks["keys"][0]

    assert key["kid"] == "mock-key-id"
    assert key["kty"] == "RSA"
    assert key["alg"] == "RS256"