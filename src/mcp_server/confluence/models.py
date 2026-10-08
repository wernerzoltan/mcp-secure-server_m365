from dataclasses import dataclass
from datetime import datetime


@dataclass
class Space:
    """
    Represents a Confluence Space.
    """

    id: str
    key: str
    name: str
    description: str
        # Example: Space(
        #   id="1",
        #   key="ENG",
        #   name="Engineering",
        #   description="Engineering Space"
        # )


@dataclass
class Page:
    """
    Represents a Confluence Page.
    """

    id: str
    title: str
    content: str
    space_key: str
    last_modified: datetime
        # Example:
        # Page(
        #    id="100",
        #    title="Architecture Overview",
        #    content="...",
        #    space_key="ENG",
        #    last_modified=datetime.utcnow(),
        # )

@dataclass
class SearchResult:
    """
    Represents a search result.
    """

    page_id: str
    title: str
    excerpt: str
    space_key: str
        # Example:
        # SearchResult(
        #   page_id="100",
        #   title="Architecture Overview",
        #   excerpt="This page provides an overview of the architecture...",
        #   space_key="ENG"
        # )