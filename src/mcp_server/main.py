from mcp.server.mcpserver import MCPServer
from mcp_server.resources.spaces import read_spaces_resource
import sys

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

# Main function to create and run the MCP server
# For stdio communication the server must run as a server process.
def main() -> None:
    server = create_server()
    # proves the MCP server itself works.
    server.run()


# Run the server if this script is executed directly
if __name__ == "__main__":
    print("Starting MCP server...", file=sys.stderr)
    main()
