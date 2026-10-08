from datetime import datetime

from mcp_server.confluence.models import (
    Page,
    SearchResult,
    Space,
)


def test_space_creation():
    space = Space(
        id="1",
        key="ENG",
        name="Engineering",
        description="Engineering Space",
    )

    assert space.key == "ENG"


def test_page_creation():
    page = Page(
        id="100",
        title="Architecture",
        content="Sample",
        space_key="ENG",
        last_modified=datetime.utcnow(),
    )

    assert page.space_key == "ENG"


def test_search_result_creation():
    result = SearchResult(
        page_id="100",
        title="Architecture",
        excerpt="Sample excerpt",
        space_key="ENG",
    )

    assert result.page_id == "100"