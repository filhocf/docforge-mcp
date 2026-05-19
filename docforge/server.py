"""Entry point for docforge-mcp CLI."""

import os


def main():
    """Start the DocForge MCP server.

    Supports:
    - stdio (default): for mcp.json integration
    - streamable-http: for standalone service (port 8958)

    Set MCP_TRANSPORT=streamable-http for HTTP mode.
    """
    from docforge.app import config, mcp

    transport = os.environ.get("MCP_TRANSPORT", "stdio")

    if transport == "streamable-http":
        mcp.run(
            transport="streamable-http",
            host="0.0.0.0",
            port=int(os.environ.get("MCP_PORT", "8958")),
            log_level=config.logging.mcp_level_str,
            path="/mcp",
        )
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
