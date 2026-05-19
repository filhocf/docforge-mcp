# AGENTS.md — docforge-mcp

## Project Overview

MCP server providing 38 tools for complete Office document manipulation — create, read, edit, convert, merge, and template DOCX, XLSX, PPTX, PDF, and EML files. Designed for AI agents that need full document lifecycle control.

## Architecture

```
mcp_office_documents/
├── app.py              # FastMCP server — all 38 tools registered here
├── server.py           # Entry point (stdio/HTTP transport selection)
└── __init__.py

docx_tools/             # Word: create, markdown→docx, templates
├── base_docx_tool.py   # create_word_from_markdown
├── conditional_templates.py  # render_docx_template (if/unless/each)
├── dynamic_docx_tools.py     # Dynamic tools from YAML templates
└── helpers.py

xlsx_tools/             # Excel: create, charts, formatting
├── base_xlsx_tool.py   # create_excel_from_markdown
├── formatting.py       # apply_excel_formatting (color scale, highlight, data bar)
└── helpers.py

pptx_tools/             # PowerPoint: create, slides, shapes, images
├── base_pptx_tool.py   # create_powerpoint_presentation
├── slide_builder.py    # Slide construction logic
├── chart_utils.py      # Charts in slides
└── helpers.py

pdf_tools/              # PDF: create from markdown, convert DOCX→PDF
├── base_pdf_tool.py

email_tools/            # Email: HTML drafts (.eml)
├── base_email_tool.py
├── dynamic_email_tools.py

edit_tools/             # Edit existing documents
├── docx_editor.py      # edit/insert/delete paragraphs, search/replace
├── pptx_editor.py      # edit slides, reorder, duplicate, delete
├── xlsx_editor.py      # edit cells, insert/delete rows

read_tools/             # Read existing documents
├── docx_reader.py      # get_docx_paragraphs, get_docx_tables
├── pptx_reader.py      # get_pptx_slides
├── xlsx_reader.py      # get_xlsx_sheets

merge_tools/            # Merge multiple files
├── merger.py           # merge_docx_files, merge_pptx_files

xml_tools/              # XML creation
├── base_xml_tool.py

upload_tools/           # S3/GCS/Azure/MinIO upload
├── main.py

tests/                  # 16 test files, pytest
```

## Data Flow

```
AI Agent → FastMCP (stdio/HTTP) → app.py → {docx,xlsx,pptx,pdf,email,edit,read,merge}_tools → output file
```

## Key Conventions

- **Transport**: stdio (default) or streamable-http (env `MCP_TRANSPORT=streamable-http`, `MCP_PORT=8958`)
- **Output**: files saved to `output/` directory (configurable via `OUTPUT_DIR` env)
- **Templates**: DOCX/PPTX with `{{var}}`, `{{#if cond}}`, `{{#each items}}`
- **Naming**: snake_case functions, tools named descriptively (`create_word_from_markdown`, `edit_docx_paragraph`)
- **Errors**: raise ValueError for user errors, let exceptions propagate for bugs

## Adding a New Tool

1. Create function in the appropriate `*_tools/` module
2. Register in `mcp_office_documents/app.py` with `@mcp.tool()` decorator
3. Add test in `tests/test_{category}.py`
4. Run: `pytest --tb=short -q && ruff check .`

## Tests

```bash
pip install -e ".[dev]"
pytest --tb=short -q --cov=. --cov-report=term-missing
ruff check .
```
