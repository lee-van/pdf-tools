# Image & PDF Utility Scripts

A small collection of **command-line Python utilities** for working with images, PDFs, and Word documents.

These scripts are designed to be **simple, composable tools** that solve common document-processing tasks such as:

- Converting image collections to **PDF**
- Converting image collections to **Word (.docx)**
- Creating **labeled PDFs from images**
- **Merging** PDFs
- **Splitting PDFs by maximum file size**

Each script is **standalone** and can be used independently.

---

# Features

- Simple **CLI-based utilities**
- Works with **JPG, PNG, and other common image formats**
- Supports **Unicode filenames** (including Mandarin and other non-Latin scripts)
- Automatically scales images to fit document pages
- Lightweight dependencies
- Designed for **batch processing**

---

# Requirements

Python **3.9+** recommended.

Install dependencies:

```bash
pip install pillow python-docx pypdf
```

Dependencies used:

| Library | Purpose |
|-------|-------|
| Pillow | Image processing |
| python-docx | Word document generation |
| pypdf | PDF manipulation |

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourname/image-pdf-tools.git
cd image-pdf-tools
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pillow python-docx pypdf
```

---

# Scripts Overview

| Script | Description |
|------|------|
| `images2docx.py` | Convert images into a Word document |
| `images2pdf.py` | Convert images into a simple PDF |
| `images2pdf_labeled.py` | Convert images to PDF with filename headers and page numbers |
| `merge_pdfs.py` | Merge multiple PDFs |
| `split_pdf_maxsize.py` | Split a PDF into parts below a maximum file size |

---

# images2docx.py

Convert images into a **Word document (.docx)**.

Features:

- Filename becomes a **heading above each image**
- Images automatically **scaled to fit the page**
- Supports **multiple images per page**
- Handles **Unicode filenames**

### Usage

```bash
python images2docx.py output.docx image1.jpg image2.png image3.jpg
```

Specify number of images per page:

```bash
python images2docx.py output.docx image1.jpg image2.jpg image3.jpg 2
```

Example:

```bash
python images2docx.py photos.docx *.jpg
```

---

# images2pdf.py

Create a **PDF from images**, with **one image per page**.

Transparent images (e.g. PNG) are automatically converted to RGB.

### Usage

```bash
python images2pdf.py output.pdf image1.jpg image2.png image3.jpg
```

Example:

```bash
python images2pdf.py gallery.pdf *.png
```

---

# images2pdf_labeled.py

Create a PDF where each page contains:

- A **header with the image filename**
- A **page number**
- The **image centered below the header**

Images are slightly resized to create space for the header.

### Header Layout

```
--------------------------------
|  filename label     page #   |
--------------------------------
|                              |
|           image              |
|                              |
```

Supports Unicode labels (useful for multilingual filenames).

### Usage

```bash
python images2pdf_labeled.py output.pdf image1.jpg image2.jpg
```

Specify starting page number:

```bash
python images2pdf_labeled.py output.pdf image1.jpg image2.jpg 50
```

Example:

```bash
python images2pdf_labeled.py slides.pdf slide1.png slide2.png slide3.png
```

---

# merge_pdfs.py

Merge multiple PDFs into a single file.

### Usage

```bash
python merge_pdfs.py output.pdf file1.pdf file2.pdf file3.pdf
```

Example:

```bash
python merge_pdfs.py combined.pdf chapter1.pdf chapter2.pdf chapter3.pdf
```

---

# split_pdf_maxsize.py

Split a PDF into multiple files so that each output file remains under a specified **maximum size**.

Default limit:

```
15 MB
```

Output files are named automatically:

```
document_part1.pdf
document_part2.pdf
document_part3.pdf
```

### Usage

Default size limit:

```bash
python split_pdf_maxsize.py input.pdf
```

Specify custom maximum size (MB):

```bash
python split_pdf_maxsize.py input.pdf 10
```

Example:

```bash
python split_pdf_maxsize.py large_file.pdf 20
```

---

# Batch Processing Tips

### Process all images in a directory

```bash
python images2pdf.py output.pdf *.jpg
```

### Sort images before processing

```bash
ls *.jpg | sort | xargs python images2pdf.py output.pdf
```

### Combine generated PDFs

```bash
python merge_pdfs.py final.pdf part1.pdf part2.pdf part3.pdf
```

---

# Unicode Filename Support

All scripts support **Unicode filenames**, including:

```
第01頁.jpg
圖像02.png
пример.png
imagen.jpg
```

This works both for:

- file input
- automatically generated labels

---

# Font Configuration (Optional)

`images2pdf_labeled.py` uses a font to render header labels.

Default path:

```
/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc
```

If this font is unavailable, the script falls back to the default PIL font.

To customize:

```python
FONT_PATH = "/path/to/your/font.ttf"
```

---

# Performance Notes

For very large image sets:

- Use glob expansion (`*.jpg`) or shell scripts
- Process images in batches if needed
- Ensure sufficient RAM when handling high-resolution images

---

# Example Workflow Ideas

These utilities can be combined for flexible document processing.

Example tasks include:

- Converting image scans to PDFs
- Creating labeled PDF collections
- Preparing image sets for sharing
- Combining multiple PDF outputs
- Splitting large PDFs to meet upload limits

---

# License

MIT License

---

# Contributions

Pull requests and improvements are welcome.

Possible future improvements:

- automatic image sorting
- PDF compression options
- drag-and-drop GUI wrapper
- recursive directory processing
- watermarking support

---

# Acknowledgements

Built using excellent open source libraries:

- Pillow  
- python-docx  
- pypdf