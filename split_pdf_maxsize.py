import os
import sys
import tempfile
from pypdf import PdfReader, PdfWriter

DEFAULT_MAX_MB = 15


def get_file_size_mb(path):
    return os.path.getsize(path) / (1024 * 1024)


def split_pdf_by_size(input_pdf, max_mb=DEFAULT_MAX_MB):
    reader = PdfReader(input_pdf)
    base_name = os.path.splitext(os.path.basename(input_pdf))[0]

    part = 1
    writer = PdfWriter()

    for page in reader.pages:

        # Try adding the page in a temporary writer
        test_writer = PdfWriter()
        for p in writer.pages:
            test_writer.add_page(p)
        test_writer.add_page(page)

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = tmp.name

        with open(tmp_path, "wb") as f:
            test_writer.write(f)

        size_mb = get_file_size_mb(tmp_path)
        os.remove(tmp_path)

        if size_mb > max_mb and len(writer.pages) > 0:
            output_name = f"{base_name}_part{part}.pdf"
            with open(output_name, "wb") as f:
                writer.write(f)

            print(f"Created {output_name}")

            part += 1
            writer = PdfWriter()

        writer.add_page(page)

    # Write final chunk
    if len(writer.pages) > 0:
        output_name = f"{base_name}_part{part}.pdf"
        with open(output_name, "wb") as f:
            writer.write(f)

        print(f"Created {output_name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_pdf_maxsize.py input.pdf [max_mb]")
        sys.exit(1)

    input_pdf = sys.argv[1]
    max_mb = float(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_MAX_MB

    split_pdf_by_size(input_pdf, max_mb)
