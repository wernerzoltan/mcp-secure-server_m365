from mcp_server.confluence.confluence_client import (
    ConfluenceClient,
)


def test_interface_exists():
    assert ConfluenceClient is not None


def test_has_get_spaces():
    assert hasattr(
        ConfluenceClient,
        "get_spaces",
    )


def test_has_get_pages():
    assert hasattr(
        ConfluenceClient,
        "get_pages",
    )


def test_has_get_page():
    assert hasattr(
        ConfluenceClient,
        "get_page",
    )


def test_has_search():
    assert hasattr(
        ConfluenceClient,
        "search",
    )