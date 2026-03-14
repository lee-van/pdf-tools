# PDF Tools

A small collection of simple Python command-line utilities for working with PDFs.

Currently included:

- **merge_pdfs.py** — combine multiple PDF files into a single PDF
- **images_to_pdf.py** — convert multiple image files into a multi-page PDF

These scripts are designed to be lightweight and easy to use from the command line.

---

# Requirements

Python 3.8+

Install dependencies:

```bash
pip install pypdf pillow
```

Libraries used:

- `pypdf` — reading and writing PDF files
- `Pillow` — image processing and conversion

---

# Tools

## 1. Merge PDFs

`merge_pdfs.py` combines multiple PDF files (including multi-page PDFs) into a single output file.

### Usage

```bash
python merge_pdfs.py output.pdf file1.pdf file2.pdf file3.pdf
```

### Example

```bash
python merge_pdfs.py combined.pdf chapter1.pdf chapter2.pdf appendix.pdf
```

The resulting file will contain all pages from the input PDFs in the order provided.

### Features

- Works with **multi-page PDFs**
- Preserves page order
- No recompression or quality loss
- Simple command-line interface

---

## 2. Convert Images to a Multi-Page PDF

`images_to_pdf.py` converts multiple bitmap images into a single multi-page PDF.

Supported formats include:

- JPG / JPEG
- PNG
- BMP
- TIFF
- Other formats supported by Pillow

### Usage

```bash
python images_to_pdf.py output.pdf image1.jpg image2.png image3.jpg
```

### Example

```bash
python images_to_pdf.py document.pdf page1.jpg page2.jpg page3.png
```

Each image becomes one page in the resulting PDF.

### Features

- Supports multiple image formats
- Handles PNG transparency automatically
- Maintains original image resolution
- Creates multi-page PDFs

---

# Example Workflow

Convert scanned pages to a PDF:

```bash
python images_to_pdf.py scans.pdf scan1.jpg scan2.jpg scan3.jpg
```

Merge the result with another document:

```bash
python merge_pdfs.py final_document.pdf cover.pdf scans.pdf appendix.pdf
```

---

# License

MIT License
