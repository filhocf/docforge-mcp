"""Read and extract content from existing PDF files."""

from pathlib import Path

from pypdf import PdfReader


def read_pdf(file_path: str) -> str:
    """Extract all text from a PDF file."""
    reader = PdfReader(file_path)
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text and text.strip():
            pages.append(text)
    return "\n\n".join(pages)


def get_pdf_info(file_path: str) -> dict:
    """Get metadata and statistics from a PDF file."""
    reader = PdfReader(file_path)
    meta = reader.metadata or {}

    total_chars = sum(len(p.extract_text() or "") for p in reader.pages)

    return {
        "file": Path(file_path).name,
        "title": meta.get("/Title", "") or "",
        "author": meta.get("/Author", "") or "",
        "creator": meta.get("/Creator", "") or "",
        "pages": len(reader.pages),
        "characters": total_chars,
    }


def get_pdf_pages(file_path: str, page_numbers: list[int] | None = None) -> list[dict]:
    """Extract text from specific pages (0-indexed). If page_numbers is None, returns all."""
    reader = PdfReader(file_path)
    result = []

    indices = page_numbers if page_numbers is not None else range(len(reader.pages))

    for i in indices:
        if 0 <= i < len(reader.pages):
            text = reader.pages[i].extract_text() or ""
            result.append({"page": i, "text": text})

    return result
