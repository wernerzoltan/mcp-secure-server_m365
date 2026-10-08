"""
What This Interface Does: 
It defines the four MCP Resources planned in the project roadmap.
    confluence://spaces
    confluence://pages
    confluence://page
    confluence://search


"""

from abc import ABC
from abc import abstractmethod

from mcp_server.confluence.models import (
    Page,
    SearchResult,
    Space,
)


class ConfluenceClient(ABC):
    """
    Contract for Confluence access.

    Implementations may be:

    - MockConfluenceClient
    - RealConfluenceClient
    """

    @abstractmethod
    async def get_spaces(
        self,
    ) -> list[Space]:
        """
        Return Confluence spaces.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_pages(
        self,
        space_key: str,
    ) -> list[Page]:
        """
        Return pages from a space.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_page(
        self,
        page_id: str,
    ) -> Page:
        """
        Return a single page.
        """
        raise NotImplementedError

    @abstractmethod
    async def search(
        self,
        query: str,
        limit: int = 10,
    ) -> list[SearchResult]:
        """
        Search Confluence content.
        """
        raise NotImplementedError