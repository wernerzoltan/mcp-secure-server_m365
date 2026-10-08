from mcp_server.confluence.fixtures import (
    PAGES,
    SPACES,
)


def test_spaces_exist():
    assert len(SPACES) == 3


def test_pages_exist():
    assert len(PAGES) == 4


def test_engineering_space_exists():
    assert any(
        space.key == "ENG"
        for space in SPACES
    )


def test_architecture_page_exists():
    assert any(
        page.title == "Architecture Overview"
        for page in PAGES
    )