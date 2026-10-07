from mcp_server.data.mock_data import get_spaces
# Why This File Exists
# We deliberately do not put resource logic in main.py
# Keeping resource logic isolated from server startup.
# This helps when:
# unit testing
# authorization
# schema validation
# audit logging


def read_spaces_resource() -> list[dict]:
    """
    Resource handler for:

    confluence://spaces
    """

    return get_spaces()