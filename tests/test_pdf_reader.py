"""Tests for PDF reader functionality.

Covers:
- Text extraction from PDF files
- Metadata extraction (pages, title, author)
- Page-specific extraction
- Error handling for invalid/missing files
"""


import pytest
from fpdf import FPDF

from docforge.read.pdf_reader import get_pdf_info, get_pdf_pages, read_pdf


@pytest.fixture
def sample_pdf(tmp_path):
    """Create a simple PDF with known content for testing."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 10, "Page 1: Hello World", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, "This is test content.", new_x="LMARGIN", new_y="NEXT")

    pdf.add_page()
    pdf.cell(0, 10, "Page 2: Second page content", new_x="LMARGIN", new_y="NEXT")

    pdf.add_page()
    pdf.cell(0, 10, "Page 3: Final page", new_x="LMARGIN", new_y="NEXT")

    path = tmp_path / "test.pdf"
    pdf.output(str(path))
    return str(path)


class TestReadPdf:
    """Tests for read_pdf function."""

    def test_extracts_text(self, sample_pdf):
        text = read_pdf(sample_pdf)
        assert "Hello World" in text
        assert "Second page content" in text
        assert "Final page" in text

    def test_returns_string(self, sample_pdf):
        result = read_pdf(sample_pdf)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_file_not_found(self):
        with pytest.raises(Exception):
            read_pdf("/nonexistent/path/file.pdf")


class TestGetPdfInfo:
    """Tests for get_pdf_info function."""

    def test_returns_page_count(self, sample_pdf):
        info = get_pdf_info(sample_pdf)
        assert info["pages"] == 3

    def test_returns_filename(self, sample_pdf):
        info = get_pdf_info(sample_pdf)
        assert info["file"] == "test.pdf"

    def test_returns_character_count(self, sample_pdf):
        info = get_pdf_info(sample_pdf)
        assert info["characters"] > 0

    def test_has_expected_keys(self, sample_pdf):
        info = get_pdf_info(sample_pdf)
        assert "file" in info
        assert "title" in info
        assert "author" in info
        assert "pages" in info
        assert "characters" in info


class TestGetPdfPages:
    """Tests for get_pdf_pages function."""

    def test_returns_all_pages(self, sample_pdf):
        pages = get_pdf_pages(sample_pdf)
        assert len(pages) == 3

    def test_specific_pages(self, sample_pdf):
        pages = get_pdf_pages(sample_pdf, page_numbers=[0, 2])
        assert len(pages) == 2
        assert pages[0]["page"] == 0
        assert pages[1]["page"] == 2

    def test_page_has_text(self, sample_pdf):
        pages = get_pdf_pages(sample_pdf, page_numbers=[0])
        assert "Hello World" in pages[0]["text"]

    def test_invalid_page_number_skipped(self, sample_pdf):
        pages = get_pdf_pages(sample_pdf, page_numbers=[99])
        assert len(pages) == 0

    def test_empty_page_numbers(self, sample_pdf):
        pages = get_pdf_pages(sample_pdf, page_numbers=[])
        assert len(pages) == 0
