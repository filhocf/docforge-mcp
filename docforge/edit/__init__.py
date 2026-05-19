"""Tools for editing existing Office documents (DOCX, XLSX, PPTX)."""

from docforge.edit.docx_editor import (
    delete_docx_paragraph,
    edit_docx_paragraph,
    insert_docx_paragraph,
    search_replace_docx,
)
from docforge.edit.pptx_editor import delete_pptx_slide, edit_pptx_slide_text, reorder_pptx_slides
from docforge.edit.xlsx_editor import delete_xlsx_row, edit_xlsx_cell, insert_xlsx_row

__all__ = [
    "edit_docx_paragraph",
    "delete_docx_paragraph",
    "search_replace_docx",
    "insert_docx_paragraph",
    "edit_xlsx_cell",
    "insert_xlsx_row",
    "delete_xlsx_row",
    "edit_pptx_slide_text",
    "delete_pptx_slide",
    "reorder_pptx_slides",
]
