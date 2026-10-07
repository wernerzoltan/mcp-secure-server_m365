# A tiny test client: 
# The sole objective is: Can an MCP client connect to the server and see the confluence://spaces resource?

import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Example client script to test the MCP server connection and list resources
async def main() -> None:
    """
    Connect to local MCP server.
    """

    # Define the parameters for connecting to the local MCP server
    # Start MCP Server:
    server_params = StdioServerParameters(
        command = "python",
        args = ["-m", "src.mcp_server.main"]
    )

    # Create MCP Connection: This is exactly how many local MCP clients communicate.
    async with stdio_client(server_params) as (
        read_stream,
        write_stream,
    ):
        async with ClientSession(
            read_stream,
            write_stream
        ) as session:

            # Initialize MCP Session
            await session.initialize()

            # Requests all registered resources.
            # Expected output:
            # confluence://spaces
            resources = await session.list_resources()

            print("\nAvailable Resources:")

            for resource in resources.resources:
                print(f" {resource.uri}")

            #
            # Read resource
            #
            print("\nReading resource...")
            print("confluence://spaces")

            # Reads a specific resource.
            result = await session.read_resource(
                "confluence://spaces"
            )
            
            print("\nResource Content:")
            print(result)

if __name__ == "__main__":
    asyncio.run(main())