import pytest

from mcp_server.auth.mock_oauth_provider import (
    MockOAuthProvider,
)


@pytest.mark.asyncio
async def test_token_creation():
    provider = MockOAuthProvider()

    token = await provider.create_token(
        "mock-user"
    )

    assert token is not None
    assert "." in token


@pytest.mark.asyncio
async def test_generated_token_valid():
    provider = MockOAuthProvider()

    token = await provider.create_token(
        "mock-user"
    )

    result = await provider.validate_token(
        token
    )

    assert result is True


@pytest.mark.asyncio
async def test_user_extraction():
    provider = MockOAuthProvider()

    token = await provider.create_token(
        "mock-user"
    )

    user_id = await provider.get_user_id(
        token
    )

    assert user_id == "mock-user"


@pytest.mark.asyncio
async def test_invalid_token():
    provider = MockOAuthProvider()

    result = await provider.validate_token(
        "invalid-token"
    )

    assert result is False

@pytest.mark.asyncio
async def test_expired_token():
    provider = MockOAuthProvider()

    token = await provider.create_token(
        user_id="mock-user",
        expires_in_seconds=-10,
    )

    result = await provider.validate_token(
        token
    )

    assert result is False

@pytest.mark.asyncio
async def test_invalid_token_structure():
    provider = MockOAuthProvider()

    result = await provider.validate_token(
        "not-a-jwt"
    )

    assert result is False

@pytest.mark.asyncio
async def test_missing_claims():
    provider = MockOAuthProvider()

    invalid_token = (
        "abc."
        "e30="
        ".xyz"
    )

    result = await provider.validate_token(
        invalid_token
    )

    assert result is False