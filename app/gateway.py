from fastmcp import FastMCP
from tools import mcp as tools_mcp

mcp = FastMCP()

@mcp.tool()
async def fetch():
    '''Use this tool to fetch data from a source.'''
    return {"data": "Hello, MCP!"}

@mcp.tool()
async def process(path:str):
    '''Use this tool to process the fetched data.'''
    return {"processed_data": "Data has been processed! at path: " + path}

# Mount tools from tools.py
mcp.mount(tools_mcp)

# Mount external MCP servers
mcp.mount(
    FastMCP.as_proxy({
        "mcpServers": {
            "ddg_mcp": {"command": "uvx", "args": ["duckduckgo-mcp-server"]}
        }
    })
)

mcp.mount(
    FastMCP.as_proxy({
        "mcpServers": {
            "agentic_mcp_terminal": {"command": "uvx", "args": ["agentic_mcp_server"]}
        }
    })
)

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8050)