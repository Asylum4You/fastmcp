import asyncio
from fastmcp import Client, FastMCP

client = Client("https://geographical-white-snake.fastmcp.app/mcp")

async def main():
    async with client:
        # Ensure client can connect
        await client.ping()

        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        # Ex. execute a tool call
       async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(main())
