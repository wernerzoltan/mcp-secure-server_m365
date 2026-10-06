from mcp.server.mcpserver import MCPServer
from mcp_server.resources import read_spaces_resource

# Main entry point for the MCP secure server application
def create_server() -> MCPServer:
    """
    Create MCP server instance.
    """

    # Initialize the MCP server instance with the specified name
    server = MCPServer(
        name="mcp-secure-server"
    )  

    # Register the resource handler for the Confluence spaces URI
    # The MCP server now exposes: confluence://spaces
    server.resource(
        uri="confluence://spaces"
    )(read_spaces_resource)

    return server

# The handler returns:
#[
#    {
#        "id": "1",
#        "key": "ENG",
#        "name": "Engineering"
#    },
#    ...
#]


# Run the server if this script is executed directly
if __name__ == "__main__":
    server = create_server()

    print("MCP Server created successfully")
    print(f"Server name: {server.name}")