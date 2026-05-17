"""Tools for reading existing Office documents (DOCX, XLSX, PPTX)."""

from read_tools.docx_reader import read_docx, get_docx_info, get_docx_paragraphs, get_docx_tables
from read_tools.xlsx_reader import read_xlsx, get_xlsx_info, get_xlsx_sheets
from read_tools.pptx_reader import read_pptx, get_pptx_info, get_pptx_slides

__all__ = [
    "read_docx", "get_docx_info", "get_docx_paragraphs", "get_docx_tables",
    "read_xlsx", "get_xlsx_info", "get_xlsx_sheets",
    "read_pptx", "get_pptx_info", "get_pptx_slides",
]
