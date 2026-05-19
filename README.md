# docforge-mcp

MCP server for **complete Office document manipulation** — create, read, edit, convert, and template DOCX, XLSX, PPTX, PDF, and EML files.

Built for AI agents that need full document lifecycle control, not just one-shot generation.

## Install

```bash
# Via uvx (no install needed)
uvx docforge-mcp

# Or install globally
uv tool install docforge-mcp

# Or pip
pip install docforge-mcp
```

## Tools (38)

| Category | Tools | Capabilities |
|----------|:-----:|--------------|
| **Word (DOCX)** | 12 | Create from markdown, read, edit paragraphs, insert, delete, search/replace, headers/footers, images, merge, templates |
| **Excel (XLSX)** | 7 | Create from markdown, read sheets, edit cells, insert/delete rows, charts, conditional formatting |
| **PowerPoint (PPTX)** | 9 | Create presentations, read slides, edit text, add shapes/images, reorder, duplicate, delete, merge, templates |
| **PDF** | 3 | Create from markdown, convert DOCX→PDF, read |
| **Email (EML)** | 1 | Create HTML email drafts |
| **XML** | 1 | Create well-formed XML |
| **Templates** | 2 | Render DOCX/PPTX with variables, conditionals (`{{#if}}`), loops (`{{#each}}`) |
| **Metadata** | 1 | Get document info/stats |
| **Merge** | 2 | Merge multiple DOCX or PPTX files |

## Usage

### As MCP server (stdio — default)

```bash
docforge-mcp
```

### As HTTP server

```bash
MCP_TRANSPORT=streamable-http MCP_PORT=8958 docforge-mcp
```

### MCP client configuration

```json
{
  "mcpServers": {
    "office-documents": {
      "command": "docforge-mcp",
      "autoApprove": ["read_document", "get_document_info", "get_docx_paragraphs", "get_pptx_slides", "get_xlsx_sheets"]
    }
  }
}
```

## Origins

This project was born from [ForLegalAI/mcp-ms-office-documents](https://github.com/ForLegalAI/mcp-ms-office-documents) (MIT license). It diverged in scope and philosophy:

| | ForLegalAI (upstream) | docforge-mcp |
|---|---|---|
| **Goal** | One-shot document generation | Full document lifecycle |
| **Read** | ❌ | ✅ Read any DOCX/XLSX/PPTX |
| **Edit** | ❌ | ✅ Edit paragraphs, cells, slides |
| **Convert** | ❌ | ✅ DOCX→PDF |
| **Templates** | Simple `{{var}}` | Conditionals + loops |
| **Transport** | Docker + HTTP only | stdio + HTTP |
| **Install** | Docker | `uvx docforge-mcp` |

We continue to contribute compatible features upstream (PRs #57, #58, #59) while developing the full toolkit independently.

## Development

```bash
git clone https://github.com/filhocf/docforge-mcp.git
cd docforge-mcp
uv sync --group dev
uv run pytest tests/ -v
uv run ruff check .
```

## License

MIT — see [LICENSE](LICENSE) for details. Original work © ForLegalAI, extensions © Claudio Ferreira Filho.
