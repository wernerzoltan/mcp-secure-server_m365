import pytest

from mcp_server.confluence.mock_confluence_client import (
    MockConfluenceClient,
)


@pytest.mark.asyncio
async def test_get_spaces():
    client = MockConfluenceClient()

    spaces = await client.get_spaces()

    assert len(spaces) == 3


@pytest.mark.asyncio
async def test_engineering_space_exists():
    client = MockConfluenceClient()

    spaces = await client.get_spaces()

    assert any(
        space.key == "ENG"
        for space in spaces
    )


@pytest.mark.asyncio
async def test_hr_space_exists():
    client = MockConfluenceClient()

    spaces = await client.get_spaces()

    assert any(
        space.key == "HR"
        for space in spaces
    )


@pytest.mark.asyncio
async def test_ops_space_exists():
    client = MockConfluenceClient()

    spaces = await client.get_spaces()

    assert any(
        space.key == "OPS"
        for space in spaces
    )

@pytest.mark.asyncio
async def test_get_pages_for_eng():
    client = MockConfluenceClient()

    pages = await client.get_pages(
        "ENG"
    )

    assert len(pages) == 2


@pytest.mark.asyncio
async def test_architecture_page_present():
    client = MockConfluenceClient()

    pages = await client.get_pages(
        "ENG"
    )

    assert any(
        page.title ==
        "Architecture Overview"
        for page in pages
    )

@pytest.mark.asyncio
async def test_hr_space_pages():
    client = MockConfluenceClient()

    pages = await client.get_pages(
        "HR"
    )

    assert len(pages) == 1


@pytest.mark.asyncio
async def test_unknown_space():
    client = MockConfluenceClient()

    pages = await client.get_pages(
        "UNKNOWN"
    )

    assert pages == []


@pytest.mark.asyncio
async def test_get_single_page():
    client = MockConfluenceClient()

    page = await client.get_page(
        "100"
    )

    assert page.id == "100"


@pytest.mark.asyncio
async def test_page_title():
    client = MockConfluenceClient()

    page = await client.get_page(
        "100"
    )

    assert (
        page.title
        == "Architecture Overview"
    )

@pytest.mark.asyncio
async def test_page_space_key():
    client = MockConfluenceClient()

    page = await client.get_page(
        "100"
    )

    assert page.space_key == "ENG"


@pytest.mark.asyncio
async def test_unknown_page():
    client = MockConfluenceClient()

    with pytest.raises(KeyError):
        await client.get_page(
            "999"
        )


@pytest.mark.asyncio
async def test_search_returns_correct_page():
    client = MockConfluenceClient()

    results = await client.search(
        "architecture"
    )

    assert results[0].title == (
        "Architecture Overview"
    )


@pytest.mark.asyncio
async def test_search_case_insensitive():
    client = MockConfluenceClient()

    results = await client.search(
        "ARCHITECTURE"
    )

    assert len(results) > 0

@pytest.mark.asyncio
async def test_search_content():
    client = MockConfluenceClient()

    results = await client.search(
        "incident"
    )

    assert len(results) > 0

@pytest.mark.asyncio
async def test_search_no_results():
    client = MockConfluenceClient()

    results = await client.search(
        "does-not-exist"
    )

    assert results == []

@pytest.mark.asyncio
async def test_search_limit():
    client = MockConfluenceClient()

    results = await client.search(
        query="a",
        limit=1,
    )

    assert len(results) == 1