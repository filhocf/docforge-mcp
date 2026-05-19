# Refactoring Plan: v0.2.0 Package Restructure

## Objective

Consolidate all source code under a single `docforge/` top-level package, eliminating the legacy `mcp_office_documents/` name and the scattered root-level tool packages. This removes the `sys.path` hack and produces a clean, installable Python package.

---

## Current Structure

```
docforge-mcp/
├── mcp_office_documents/          # Legacy entry-point package
│   ├── __init__.py
│   ├── server.py                  # sys.path hack lives here
│   └── app.py                     # Registers all 38 tools
├── config.py                      # Root-level module (get_config)
├── middleware.py                   # Root-level module (ApiKeyAuthMiddleware)
├── template_utils.py              # Root-level module (find_*_template helpers)
├── docx_tools/
│   ├── __init__.py
│   ├── base_docx_tool.py
│   ├── dynamic_docx_tools.py
│   ├── helpers.py
│   ├── conditional_templates.py
│   └── advanced/
│       ├── __init__.py
│       └── features.py
├── xlsx_tools/
│   ├── __init__.py
│   ├── base_xlsx_tool.py
│   ├── helpers.py
│   ├── formatting.py
│   └── charts/
│       ├── __init__.py
│       └── chart_builder.py
├── pptx_tools/
│   ├── __init__.py
│   ├── base_pptx_tool.py
│   ├── slide_builder.py
│   ├── helpers.py
│   ├── chart_utils.py
│   ├── image_utils.py
│   ├── constants.py
│   └── advanced/
│       ├── __init__.py
│       └── features.py
├── email_tools/
│   ├── __init__.py
│   ├── base_email_tool.py
│   └── dynamic_email_tools.py
├── xml_tools/
│   ├── __init__.py
│   └── base_xml_tool.py
├── upload_tools/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── backends/
│       ├── __init__.py
│       ├── s3.py
│       ├── azure.py
│       ├── gcs.py
│       ├── minio.py
│       └── local.py
├── read_tools/
│   ├── __init__.py
│   ├── docx_reader.py
│   ├── pptx_reader.py
│   └── xlsx_reader.py
├── edit_tools/
│   ├── __init__.py
│   ├── docx_editor.py
│   ├── pptx_editor.py
│   └── xlsx_editor.py
├── pdf_tools/
│   ├── __init__.py
│   └── base_pdf_tool.py
├── merge_tools/
│   ├── __init__.py
│   └── merger.py
├── tests/
│   ├── __init__.py
│   ├── test_docx_base.py
│   ├── test_docx_templates.py
│   ├── test_docx_advanced.py
│   ├── test_conditional_templates.py
│   ├── test_xlsx_creation.py
│   ├── test_xlsx_formatting.py
│   ├── test_xlsx_charts.py
│   ├── test_pptx_creation.py
│   ├── test_pptx_advanced.py
│   ├── test_xml_creation.py
│   ├── test_edit_tools.py
│   ├── test_read_tools.py
│   ├── test_merge_tools.py
│   ├── test_pdf_tools.py
│   ├── test_s3_upload.py
│   └── test_auth_middleware.py
├── config/
│   └── docx_templates.yaml
├── custom_templates/
│   └── letter_template.docx
├── default_templates/
│   ├── default_docx_template.docx
│   ├── default_pptx_template_4_3.pptx
│   ├── default_pptx_template_16_9.pptx
│   └── default_email_template.html
├── pyproject.toml
├── Readme.md
├── CHANGELOG.md
└── LICENSE
```

---

## Target Structure

```
docforge-mcp/
├── docforge/                       # Single top-level package
│   ├── __init__.py                 # __version__, package metadata
│   ├── server.py                   # Entry point (NO sys.path hack)
│   ├── app.py                      # Tool registration
│   ├── config.py                   # Moved from root
│   ├── middleware.py               # Moved from root
│   ├── template_utils.py           # Moved from root
│   ├── docx/
│   │   ├── __init__.py
│   │   ├── base.py                 # was base_docx_tool.py
│   │   ├── dynamic.py             # was dynamic_docx_tools.py
│   │   ├── helpers.py
│   │   ├── conditional_templates.py
│   │   └── advanced/
│   │       ├── __init__.py
│   │       └── features.py
│   ├── xlsx/
│   │   ├── __init__.py
│   │   ├── base.py                 # was base_xlsx_tool.py
│   │   ├── helpers.py
│   │   ├── formatting.py
│   │   └── charts/
│   │       ├── __init__.py
│   │       └── chart_builder.py
│   ├── pptx/
│   │   ├── __init__.py
│   │   ├── base.py                 # was base_pptx_tool.py
│   │   ├── slide_builder.py
│   │   ├── helpers.py
│   │   ├── chart_utils.py
│   │   ├── image_utils.py
│   │   ├── constants.py
│   │   └── advanced/
│   │       ├── __init__.py
│   │       └── features.py
│   ├── email/
│   │   ├── __init__.py
│   │   ├── base.py                 # was base_email_tool.py
│   │   └── dynamic.py             # was dynamic_email_tools.py
│   ├── xml/
│   │   ├── __init__.py
│   │   └── base.py                 # was base_xml_tool.py
│   ├── upload/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── utils.py
│   │   └── backends/
│   │       ├── __init__.py
│   │       ├── s3.py
│   │       ├── azure.py
│   │       ├── gcs.py
│   │       ├── minio.py
│   │       └── local.py
│   ├── read/
│   │   ├── __init__.py
│   │   ├── docx_reader.py
│   │   ├── pptx_reader.py
│   │   └── xlsx_reader.py
│   ├── edit/
│   │   ├── __init__.py
│   │   ├── docx_editor.py
│   │   ├── pptx_editor.py
│   │   └── xlsx_editor.py
│   ├── pdf/
│   │   ├── __init__.py
│   │   └── base.py                 # was base_pdf_tool.py
│   └── merge/
│       ├── __init__.py
│       └── merger.py
├── tests/                          # Stays at root (standard pytest layout)
│   ├── __init__.py
│   └── ... (all test files unchanged in location)
├── config/
│   └── docx_templates.yaml
├── custom_templates/
├── default_templates/
├── pyproject.toml
├── Readme.md
├── CHANGELOG.md
└── LICENSE
```

---

## Step-by-Step Migration Plan

### Step 1: Create `docforge/` package skeleton

**Actions:**
- Create `docforge/__init__.py` with `__version__ = "0.2.0"`
- Create all subdirectory `__init__.py` files (empty stubs)

**Verification:** `python -c "import docforge"` succeeds.

---

### Step 2: Move root-level modules into `docforge/`

**Actions:**
- `config.py` → `docforge/config.py`
- `middleware.py` → `docforge/middleware.py`
- `template_utils.py` → `docforge/template_utils.py`

**Verification:** `python -c "from docforge.config import get_config"` succeeds.

---

### Step 3: Move `upload_tools/` → `docforge/upload/`

**Actions:**
- Move all files preserving internal structure
- Update internal relative imports (backends `..utils` stays the same)
- Update `from config import get_config` → `from docforge.config import get_config` in `main.py`

**Verification:** `python -c "from docforge.upload import upload_file"` succeeds.

---

### Step 4: Move `docx_tools/` → `docforge/docx/`

**Actions:**
- Move all files; rename `base_docx_tool.py` → `base.py`, `dynamic_docx_tools.py` → `dynamic.py`
- Update imports:
  - `from upload_tools import upload_file` → `from docforge.upload import upload_file`
  - `from template_utils import ...` → `from docforge.template_utils import ...`
- Update `advanced/__init__.py`: `from docx_tools.advanced.features` → `from docforge.docx.advanced.features`

**Verification:** `python -c "from docforge.docx import markdown_to_word"` succeeds.

---

### Step 5: Move `xlsx_tools/` → `docforge/xlsx/`

**Actions:**
- Move all files; rename `base_xlsx_tool.py` → `base.py`
- Update imports:
  - `from upload_tools import upload_file` → `from docforge.upload import upload_file`
- Update `charts/__init__.py`: `from xlsx_tools.charts.chart_builder` → `from docforge.xlsx.charts.chart_builder`

**Verification:** `python -c "from docforge.xlsx import markdown_to_excel"` succeeds.

---

### Step 6: Move `pptx_tools/` → `docforge/pptx/`

**Actions:**
- Move all files; rename `base_pptx_tool.py` → `base.py`
- Update imports:
  - `from upload_tools import upload_file` → `from docforge.upload import upload_file`
  - `from template_utils import ...` → `from docforge.template_utils import ...`
- Update `advanced/__init__.py`: `from pptx_tools.advanced.features` → `from docforge.pptx.advanced.features`

**Verification:** `python -c "from docforge.pptx import create_presentation"` succeeds.

---

### Step 7: Move `email_tools/` → `docforge/email/`

**Actions:**
- Move all files; rename `base_email_tool.py` → `base.py`, `dynamic_email_tools.py` → `dynamic.py`
- Update imports:
  - `from template_utils import ...` → `from docforge.template_utils import ...`
  - `from upload_tools import upload_file` → `from docforge.upload import upload_file`

**Verification:** `python -c "from docforge.email import create_eml"` succeeds.

---

### Step 8: Move `xml_tools/` → `docforge/xml/`

**Actions:**
- Move all files; rename `base_xml_tool.py` → `base.py`
- Update imports:
  - `from upload_tools import upload_file` → `from docforge.upload import upload_file`

**Verification:** `python -c "from docforge.xml import create_xml_file"` succeeds.

---

### Step 9: Move `read_tools/` → `docforge/read/`

**Actions:**
- Move all files
- Update `__init__.py`: `from read_tools.docx_reader` → `from docforge.read.docx_reader` (etc.)

**Verification:** `python -c "from docforge.read import read_docx, read_xlsx, read_pptx"` succeeds.

---

### Step 10: Move `edit_tools/` → `docforge/edit/`

**Actions:**
- Move all files
- Update `__init__.py`: `from edit_tools.docx_editor` → `from docforge.edit.docx_editor` (etc.)

**Verification:** `python -c "from docforge.edit import edit_docx_paragraph"` succeeds.

---

### Step 11: Move `pdf_tools/` → `docforge/pdf/`

**Actions:**
- Move all files; rename `base_pdf_tool.py` → `base.py`
- Update imports:
  - `from upload_tools.main import upload_file` → `from docforge.upload.main import upload_file`

**Verification:** `python -c "from docforge.pdf import markdown_to_pdf, docx_to_pdf"` succeeds.

---

### Step 12: Move `merge_tools/` → `docforge/merge/`

**Actions:**
- Move all files

**Verification:** `python -c "from docforge.merge import merge_docx, merge_pptx"` succeeds.

---

### Step 13: Move `mcp_office_documents/app.py` → `docforge/app.py`

**Actions:**
- Move file
- Rewrite all 18+ internal imports to use `docforge.*` paths
- Update `Path(__file__).resolve().parent / "config"` path logic (now points to `docforge/config/` — adjust to `parent.parent / "config"`)

**Verification:** `python -c "from docforge.app import mcp"` succeeds.

---

### Step 14: Rewrite `server.py` → `docforge/server.py`

**Actions:**
- Move from `mcp_office_documents/server.py` to `docforge/server.py`
- Remove the entire `sys.path` hack block
- Change `from mcp_office_documents.app import config, mcp` → `from docforge.app import config, mcp`

**Verification:** `python -c "from docforge.server import main"` succeeds.

---

### Step 15: Delete `mcp_office_documents/` directory

**Actions:**
- Remove the entire old package directory

**Verification:** Confirm `mcp_office_documents` no longer importable.

---

### Step 16: Update `pyproject.toml`

**Changes:**
```toml
[project]
version = "0.2.0"

[project.scripts]
docforge-mcp = "docforge.server:main"
mcp-ms-office-documents = "docforge.server:main"  # backward compat

[tool.hatch.build.targets.wheel]
packages = ["docforge"]

# Remove [tool.hatch.build.targets.wheel.force-include] entirely
```

**Verification:** `pip install -e ".[dev]"` succeeds; `docforge-mcp --help` or `python -m docforge.server` works.

---

### Step 17: Update all test files

**Actions:**
- Remove all `sys.path.insert(0, ...)` hacks (7 test files)
- Rewrite all project imports to `docforge.*` namespace:

| Old import | New import |
|---|---|
| `from docx_tools.*` | `from docforge.docx.*` |
| `from xlsx_tools.*` | `from docforge.xlsx.*` |
| `from pptx_tools.*` | `from docforge.pptx.*` |
| `from email_tools.*` | `from docforge.email.*` |
| `from xml_tools.*` | `from docforge.xml.*` |
| `from upload_tools.*` | `from docforge.upload.*` |
| `from read_tools.*` | `from docforge.read.*` |
| `from edit_tools.*` | `from docforge.edit.*` |
| `from pdf_tools.*` | `from docforge.pdf.*` |
| `from merge_tools.*` | `from docforge.merge.*` |
| `from config import *` | `from docforge.config import *` |
| `from middleware import *` | `from docforge.middleware import *` |
| `from template_utils import *` | `from docforge.template_utils import *` |

**Verification:** `pytest --tb=short -q` — all 355 tests pass.

---

### Step 18: Update CI workflow

**Actions:**
- `.github/workflows/ci.yml`: no changes needed (uses `pip install -e ".[dev]"` which will pick up new structure)

**Verification:** Push to branch, confirm CI passes.

---

### Step 19: Clean up old directories and caches

**Actions:**
- Delete all root-level tool directories (`docx_tools/`, `xlsx_tools/`, etc.)
- Delete root-level `config.py`, `middleware.py`, `template_utils.py`
- Delete all `__pycache__/` directories
- Update `.gitignore` if needed

**Verification:** `git status` shows clean rename; `pip install -e ".[dev]" && pytest` passes.

---

## Files Requiring Import Changes

### Source files (inside tool packages):

| File | Imports to change |
|---|---|
| `docx_tools/base_docx_tool.py` → `docforge/docx/base.py` | `from upload_tools` → `from docforge.upload` |
| `docx_tools/dynamic_docx_tools.py` → `docforge/docx/dynamic.py` | `from template_utils`, `from upload_tools` → `from docforge.*` |
| `docx_tools/helpers.py` → `docforge/docx/helpers.py` | `from template_utils` → `from docforge.template_utils` |
| `docx_tools/advanced/__init__.py` → `docforge/docx/advanced/__init__.py` | `from docx_tools.advanced.features` → `from docforge.docx.advanced.features` |
| `xlsx_tools/__init__.py` → `docforge/xlsx/__init__.py` | `from xlsx_tools.base_xlsx_tool` → `from docforge.xlsx.base` |
| `xlsx_tools/base_xlsx_tool.py` → `docforge/xlsx/base.py` | `from upload_tools` → `from docforge.upload` |
| `xlsx_tools/charts/__init__.py` → `docforge/xlsx/charts/__init__.py` | `from xlsx_tools.charts.chart_builder` → `from docforge.xlsx.charts.chart_builder` |
| `pptx_tools/base_pptx_tool.py` → `docforge/pptx/base.py` | `from upload_tools` → `from docforge.upload` |
| `pptx_tools/slide_builder.py` → `docforge/pptx/slide_builder.py` | `from template_utils` → `from docforge.template_utils` |
| `pptx_tools/advanced/__init__.py` → `docforge/pptx/advanced/__init__.py` | `from pptx_tools.advanced.features` → `from docforge.pptx.advanced.features` |
| `email_tools/base_email_tool.py` → `docforge/email/base.py` | `from template_utils`, `from upload_tools` → `from docforge.*` |
| `email_tools/dynamic_email_tools.py` → `docforge/email/dynamic.py` | `from template_utils`, `from upload_tools` → `from docforge.*` |
| `xml_tools/base_xml_tool.py` → `docforge/xml/base.py` | `from upload_tools` → `from docforge.upload` |
| `upload_tools/main.py` → `docforge/upload/main.py` | `from config` → `from docforge.config` |
| `pdf_tools/base_pdf_tool.py` → `docforge/pdf/base.py` | `from upload_tools.main` → `from docforge.upload.main` |
| `read_tools/__init__.py` → `docforge/read/__init__.py` | `from read_tools.*` → `from docforge.read.*` |
| `edit_tools/__init__.py` → `docforge/edit/__init__.py` | `from edit_tools.*` → `from docforge.edit.*` |
| `pdf_tools/__init__.py` → `docforge/pdf/__init__.py` | `from pdf_tools.base_pdf_tool` → `from docforge.pdf.base` |
| `merge_tools/__init__.py` → `docforge/merge/__init__.py` | `from merge_tools.merger` → `from docforge.merge.merger` |
| `mcp_office_documents/app.py` → `docforge/app.py` | All 18 internal imports |
| `mcp_office_documents/server.py` → `docforge/server.py` | Remove sys.path hack; `from mcp_office_documents.app` → `from docforge.app` |

### Test files:

| File | Changes |
|---|---|
| `tests/test_docx_base.py` | Remove sys.path hack; `from docx_tools.*` → `from docforge.docx.*` |
| `tests/test_docx_templates.py` | Remove sys.path hack; `from docx_tools.*` → `from docforge.docx.*` |
| `tests/test_docx_advanced.py` | `from docx_tools.advanced` → `from docforge.docx.advanced` |
| `tests/test_conditional_templates.py` | `from docx_tools.conditional_templates` → `from docforge.docx.conditional_templates` |
| `tests/test_xlsx_creation.py` | Remove sys.path hack; `from xlsx_tools.*` → `from docforge.xlsx.*` |
| `tests/test_xlsx_formatting.py` | `from xlsx_tools.formatting` → `from docforge.xlsx.formatting` |
| `tests/test_xlsx_charts.py` | `from xlsx_tools.charts` → `from docforge.xlsx.charts` |
| `tests/test_pptx_creation.py` | Remove sys.path hack; `from pptx_tools.*` → `from docforge.pptx.*` |
| `tests/test_pptx_advanced.py` | `from pptx_tools.advanced` → `from docforge.pptx.advanced` |
| `tests/test_xml_creation.py` | Remove sys.path hack; `from xml_tools.*` → `from docforge.xml.*` |
| `tests/test_edit_tools.py` | `from edit_tools` → `from docforge.edit` |
| `tests/test_read_tools.py` | `from read_tools` → `from docforge.read` |
| `tests/test_merge_tools.py` | `from merge_tools` → `from docforge.merge` |
| `tests/test_pdf_tools.py` | `from pdf_tools.*` → `from docforge.pdf.*` |
| `tests/test_s3_upload.py` | Remove sys.path hack; `from upload_tools.*` → `from docforge.upload.*` |
| `tests/test_auth_middleware.py` | Remove sys.path hack; `from middleware` → `from docforge.middleware` |

### Configuration files:

| File | Changes |
|---|---|
| `pyproject.toml` | version, scripts entry point, packages list, remove force-include |

---

## Risk Assessment

| Risk | Severity | Mitigation |
|---|---|---|
| **Broken imports at runtime** | High | Each step has an independent verification command. Run full test suite after each step. |
| **`Path(__file__)` references break** | Medium | `app.py` uses `Path(__file__).resolve().parent / "config"` to find YAML configs. After move, this resolves to `docforge/config/` which doesn't exist. Must adjust to `parent.parent / "config"`. Audit all `Path(__file__)` usages. |
| **Template file discovery breaks** | Medium | `template_utils.py` and `config.py` use relative paths to find `default_templates/`, `custom_templates/`. After moving inside `docforge/`, paths need `parent.parent`. Add integration test that verifies template discovery. |
| **Editable install cache stale** | Low | Run `pip install -e ".[dev]"` fresh after restructure. Delete all `__pycache__` and `.egg-info`. |
| **Git history loss** | Low | Use `git mv` for moves to preserve file history. Do the rename in a single commit per step or a single large commit. |
| **PyPI backward compatibility** | Low | The `mcp-ms-office-documents` entry point alias is preserved. Users installing `docforge-mcp` get the new structure transparently. |
| **CI breaks during transition** | Low | Do the entire refactor in a single PR. CI runs against the final state. |
| **`docforge.email` shadows stdlib `email`** | Medium | Python resolves `from docforge.email` as a subpackage, not stdlib. However, inside `docforge/email/base.py`, `from email.mime.text import MIMEText` must still work — it will, because absolute imports resolve to stdlib when there's no `docforge.email.mime`. Verify with test. |

---

## Notes

- File renames (`base_docx_tool.py` → `base.py`, etc.) are optional cosmetic improvements. If they add risk, keep original filenames and only change the directory structure.
- The `config/` directory (YAML templates) and `default_templates/`/`custom_templates/` directories stay at project root — they are runtime data, not Python packages.
- Consider adding a `conftest.py` at project root if tests need shared fixtures, eliminating the need for any path manipulation.
