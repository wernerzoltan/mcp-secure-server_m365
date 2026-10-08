from copy import deepcopy

from mcp_server.confluence.confluence_client import (
    ConfluenceClient,
)
from mcp_server.confluence.fixtures import (
    PAGES,
    SPACES,
)
from mcp_server.confluence.models import (
    Page,
    SearchResult,
    Space,
)

class MockConfluenceClient(
    ConfluenceClient
):
    """
    Mock Confluence implementation.

    Development only.

    Uses local fixture data.
    """

    async def get_spaces(
        self,
    ) -> list[Space]:
        """
        Return available spaces.
        """

        return deepcopy(SPACES)

    async def get_pages(
        self,
        space_key: str,
    ) -> list[Page]:
        """
        Return pages for a space.
        """

        pages = [
            page
            for page in PAGES
            if page.space_key == space_key
        ]

        return deepcopy(pages)
    
    async def get_page(
        self,
        page_id: str,
    ) -> Page:
        """
        Return a single page by ID.
        """

        for page in PAGES:

            if page.id == page_id:
                return deepcopy(page)

        raise KeyError(
            f"Page not found: {page_id}"
        )

    async def search(
        self,
        query: str,
        limit: int = 10,
    ) -> list[SearchResult]:
        """
        Search page titles and content.
        """

        query = query.lower()

        results: list[SearchResult] = []

        for page in PAGES:

            title_match = (
                query in page.title.lower()
            )

            content_match = (
                query in page.content.lower()
            )

            if title_match or content_match:

                excerpt = page.content[:100]

                results.append(
                    SearchResult(
                        page_id=page.id,
                        title=page.title,
                        excerpt=excerpt,
                        space_key=page.space_key,
                    )
                )

        return deepcopy(results[:limit])