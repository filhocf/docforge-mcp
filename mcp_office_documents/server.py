"""Entry point for mcp-ms-office-documents CLI."""

import sys
from pathlib import Path

# Add project root to path so existing modules (docx_tools, etc.) are importable
_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))


def main():
    """Start the MCP Office Documents server."""
    from main import mcp  # noqa: E402
    from config import get_config  # noqa: E402

    config = get_config()
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8958,
        log_level=config.logging.mcp_level_str,
        path="/mcp",
    )


if __name__ == "__main__":
    main()
