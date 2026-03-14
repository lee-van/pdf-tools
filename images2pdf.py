from PIL import Image
import sys
import os

def images_to_pdf(image_paths, output_pdf):
    images = []

    for path in image_paths:
        img = Image.open(path)

        # Convert images with transparency (e.g., PNG) to RGB
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        images.append(img)

    if not images:
        raise ValueError("No images provided")

    first_image = images[0]
    rest_images = images[1:]

    first_image.save(
        output_pdf,
        save_all=True,
        append_images=rest_images
    )

    print(f"Saved {len(images)} pages to {output_pdf}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python images_to_pdf.py output.pdf image1.jpg image2.png ...")
        sys.exit(1)

    output_pdf = sys.argv[1]
    image_files = sys.argv[2:]

    images_to_pdf(image_files, output_pdf)
