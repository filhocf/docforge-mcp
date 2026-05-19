"""Tools for reading existing Office documents (DOCX, XLSX, PPTX)."""

from docforge.read.docx_reader import get_docx_info, get_docx_paragraphs, get_docx_tables, read_docx
from docforge.read.pptx_reader import get_pptx_info, get_pptx_slides, read_pptx
from docforge.read.xlsx_reader import get_xlsx_info, get_xlsx_sheets, read_xlsx

__all__ = [
    "read_docx",
    "get_docx_info",
    "get_docx_paragraphs",
    "get_docx_tables",
    "read_xlsx",
    "get_xlsx_info",
    "get_xlsx_sheets",
    "read_pptx",
    "get_pptx_info",
    "get_pptx_slides",
]
