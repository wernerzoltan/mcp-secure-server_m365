from mcp_server.main import create_server

# Test for verifying MCP server creation
def test_server_can_be_created():
    """
    Verify MCP server instance can be created.
    """

    server = create_server()

    # Assert that the server instance is created successfully
    assert server is not None
    # Assert that the server instance has the correct name
    assert server.name == "mcp-secure-server"