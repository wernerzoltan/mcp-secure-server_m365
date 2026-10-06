from mcp.server.mcpserver import MCPServer

# Main entry point for the MCP secure server application
def create_server() -> MCPServer:
    """
    Create MCP server instance.
    """

    # Initialize the MCP server instance with the specified name
    server = MCPServer(
        name="mcp-secure-server"
    )

    return server

# Run the server if this script is executed directly
if __name__ == "__main__":
    server = create_server()

    print("MCP Server created successfully")
    print(f"Server name: {server.name}")