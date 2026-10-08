# What This Code Does
# Creates three Confluence spaces:
# and several Confluence pages associated with those spaces.

from datetime import datetime

from mcp_server.confluence.models import (
    Page,
    Space,
)


SPACES: list[Space] = [
    Space(
        id="1",
        key="ENG",
        name="Engineering",
        description="Engineering documentation",
    ),
    Space(
        id="2",
        key="HR",
        name="Human Resources",
        description="HR policies and procedures",
    ),
    Space(
        id="3",
        key="OPS",
        name="Operations",
        description="Operations knowledge base",
    ),
]


PAGES: list[Page] = [
    Page(
        id="100",
        title="Architecture Overview",
        content=(
            "Overview of the enterprise "
            "architecture platform."
        ),
        space_key="ENG",
        last_modified=datetime.utcnow(),
    ),
    Page(
        id="101",
        title="API Guidelines",
        content=(
            "Standards for API design and "
            "integration."
        ),
        space_key="ENG",
        last_modified=datetime.utcnow(),
    ),
    Page(
        id="200",
        title="Vacation Policy",
        content=(
            "Employee vacation entitlement "
            "and approval flow."
        ),
        space_key="HR",
        last_modified=datetime.utcnow(),
    ),
    Page(
        id="300",
        title="Incident Response",
        content=(
            "Steps for operational incident "
            "management."
        ),
        space_key="OPS",
        last_modified=datetime.utcnow(),
    ),
]