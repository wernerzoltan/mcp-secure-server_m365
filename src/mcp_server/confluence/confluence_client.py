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
    ) -> list[dict]:
        """
        Return Confluence spaces.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_pages(
        self,
        space_key: str,
    ) -> list[dict]:
        """
        Return pages from a space.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_page(
        self,
        page_id: str,
    ) -> dict:
        """
        Return a single page.
        """
        raise NotImplementedError

    @abstractmethod
    async def search(
        self,
        query: str,
        limit: int = 10,
    ) -> list[dict]:
        """
        Search Confluence content.
        """
        raise NotImplementedError