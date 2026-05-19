# Changelog

All notable changes to this project will be documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [SemVer](https://semver.org/).

## [0.1.0] - 2026-05-19

### Added

- 38 MCP tools for Office document manipulation
- **Create**: Word (from markdown), Excel (from markdown), PowerPoint, PDF, Email, XML
- **Read**: DOCX paragraphs/tables, XLSX sheets, PPTX slides, document metadata
- **Edit**: DOCX paragraphs (edit/insert/delete/search-replace), XLSX cells/rows, PPTX slides (edit/reorder/duplicate/delete)
- **Convert**: DOCX → PDF
- **Merge**: Multiple DOCX or PPTX into one
- **Templates**: DOCX/PPTX with conditionals (`{{#if}}`), loops (`{{#each}}`), variables
- **Charts**: Excel charts (bar, line, pie, column)
- **Formatting**: Excel conditional formatting (highlight, color scale, data bar)
- stdio + streamable-http transport support
- CLI entry point: `docforge-mcp`
- CI: lint + test + publish on tag
- CodeQL security scanning
- Dependabot for dependencies

### Changed

- Rebranded from mcp-ms-office-documents to docforge-mcp
- Independent project (diverged from ForLegalAI upstream in scope)
