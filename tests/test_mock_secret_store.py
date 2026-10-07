import pytest

from mcp_server.secrets.mock_secret_store import (
    MockSecretStore,
)


@pytest.mark.asyncio
async def test_secret_exists():
    store = MockSecretStore()

    result = await store.secret_exists(
        "okta-client-id"
    )

    assert result is True


@pytest.mark.asyncio
async def test_secret_does_not_exist():
    store = MockSecretStore()

    result = await store.secret_exists(
        "missing-secret"
    )

    assert result is False


@pytest.mark.asyncio
async def test_get_secret():
    store = MockSecretStore()

    secret = await store.get_secret(
        "okta-client-secret"
    )

    assert secret == (
        "mock-client-secret"
    )


@pytest.mark.asyncio
async def test_missing_secret_raises():
    store = MockSecretStore()

    with pytest.raises(KeyError):
        await store.get_secret(
            "missing-secret"
        )



@pytest.mark.asyncio
async def test_create_new_secret():
    store = MockSecretStore()

    await store.set_secret(
        "database-password",
        "secret123",
    )

    value = await store.get_secret(
        "database-password"
    )

    assert value == "secret123"


@pytest.mark.asyncio
async def test_update_existing_secret():
    store = MockSecretStore()

    await store.set_secret(
        "okta-client-secret",
        "new-secret",
    )

    value = await store.get_secret(
        "okta-client-secret"
    )

    assert value == "new-secret"


@pytest.mark.asyncio
async def test_new_secret_exists():
    store = MockSecretStore()

    await store.set_secret(
        "test-secret",
        "abc",
    )

    result = await store.secret_exists(
        "test-secret"
    )

    assert result is True


@pytest.mark.asyncio
async def test_default_version():
    store = MockSecretStore()

    version = await store.get_secret_version(
        "okta-client-secret"
    )

    assert version == 1

@pytest.mark.asyncio
async def test_version_increment():
    store = MockSecretStore()

    await store.set_secret(
        "okta-client-secret",
        "updated-secret",
    )

    version = await store.get_secret_version(
        "okta-client-secret"
    )

    assert version == 2

@pytest.mark.asyncio
async def test_new_secret_version():
    store = MockSecretStore()

    await store.set_secret(
        "new-secret",
        "value",
    )

    version = await store.get_secret_version(
        "new-secret"
    )

    assert version == 1


@pytest.mark.asyncio
async def test_secret_history_length():
    store = MockSecretStore()

    await store.set_secret(
        "okta-client-secret",
        "v2",
    )

    await store.set_secret(
        "okta-client-secret",
        "v3",
    )

    history = await store.get_secret_history(
        "okta-client-secret"
    )

    assert len(history) == 3


@pytest.mark.asyncio
async def test_latest_secret_value():
    store = MockSecretStore()

    await store.set_secret(
        "okta-client-secret",
        "v2",
    )

    value = await store.get_secret(
        "okta-client-secret"
    )

    assert value == "v2"

@pytest.mark.asyncio
async def test_version_history():
    store = MockSecretStore()

    await store.set_secret(
        "okta-client-secret",
        "v2",
    )

    history = await store.get_secret_history(
        "okta-client-secret"
    )

    assert history[0].version == 1
    assert history[1].version == 2

@pytest.mark.asyncio
async def test_rotation_increases_version():
    store = MockSecretStore()

    await store.rotate_secret(
        "okta-client-secret",
        "rotated-secret",
    )

    version = await store.get_secret_version(
        "okta-client-secret"
    )

    assert version == 2

@pytest.mark.asyncio
async def test_rotation_updates_metadata():
    store = MockSecretStore()

    await store.rotate_secret(
        "okta-client-secret",
        "rotated-secret",
    )

    metadata = await store.get_secret_metadata(
        "okta-client-secret"
    )

    assert metadata.rotation_count == 1
    assert metadata.last_rotated is not None


@pytest.mark.asyncio
async def test_multiple_rotations():
    store = MockSecretStore()

    await store.rotate_secret(
        "okta-client-secret",
        "v2",
    )

    await store.rotate_secret(
        "okta-client-secret",
        "v3",
    )

    metadata = await store.get_secret_metadata(
        "okta-client-secret"
    )

    assert metadata.rotation_count == 2