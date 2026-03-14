from pypdf import PdfWriter, PdfReader
import sys
import os

def merge_pdfs(pdf_paths, output_path):
    writer = PdfWriter()

    for pdf in pdf_paths:
        reader = PdfReader(pdf)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"Merged {len(pdf_paths)} files into {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python merge_pdfs.py output.pdf file1.pdf file2.pdf ...")
        sys.exit(1)

    output_pdf = sys.argv[1]
    input_pdfs = sys.argv[2:]

    merge_pdfs(input_pdfs, output_pdf)
