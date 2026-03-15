from PIL import Image, ImageDraw, ImageFont
import sys
import os

HEADER_HEIGHT = 140
FONT_SIZE = 80
PAGE_NUM_SIZE = 50
FONT_PATH = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

def images_to_pdf(image_paths, output_pdf, starting_number=1):
    pages = []

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        page_num_font = ImageFont.truetype(FONT_PATH, PAGE_NUM_SIZE)
    except:
        font = ImageFont.load_default()
        page_num_font = ImageFont.load_default()
        print("Warning: Could not load Noto CJK font, using default font.")

    total_pages = len(image_paths)

    for i, path in enumerate(image_paths):
        img = Image.open(path)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        filename = os.path.basename(path)
        label = os.path.splitext(filename)[0]

        width, height = img.size
        new_height = height - HEADER_HEIGHT
        scale = new_height / height
        new_width = int(width * scale)

        resized_img = img.resize((new_width, new_height), Image.LANCZOS)

        page = Image.new("RGB", (width, height), "white")
        x_offset = (width - new_width) // 2
        page.paste(resized_img, (x_offset, HEADER_HEIGHT))

        draw = ImageDraw.Draw(page)

        # Draw header label (centered)
        bbox = draw.textbbox((0, 0), label, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = (width - text_width) // 2
        text_y = (HEADER_HEIGHT - text_height) // 2
        draw.text((text_x, text_y), label, fill="black", font=font)

        # Draw page number inside header (right aligned)
        page_number = starting_number + i
        page_number_text = f"{page_number}"
        # page_number_text = f"{page_number} / {starting_number + total_pages - 1}"
        bbox = draw.textbbox((0, 0), page_number_text, font=page_num_font)
        page_num_width = bbox[2] - bbox[0]
        page_num_height = bbox[3] - bbox[1]
        page_num_x = width - page_num_width - 20  # 20 px margin from right
        page_num_y = (HEADER_HEIGHT - page_num_height) // 2
        draw.text((page_num_x, page_num_y), page_number_text, fill="black", font=page_num_font)

        pages.append(page)

    if not pages:
        raise ValueError("No images provided")

    pages[0].save(
        output_pdf,
        save_all=True,
        append_images=pages[1:]
    )

    print(f"Saved {len(pages)} pages to {output_pdf}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python images_to_pdf.py output.pdf image1.jpg image2.png ... [starting_number]")
        sys.exit(1)

    output_pdf = sys.argv[1]
    image_files = sys.argv[2:]

    # Optional starting number as last argument
    if image_files[-1].isdigit():
        starting_number = int(image_files.pop())
    else:
        starting_number = 1

    images_to_pdf(image_files, output_pdf, starting_number)