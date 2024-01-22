import os
import sys
from PIL import Image
from reportlab.pdfgen import canvas


def compress_image(orig_image_path, compressed_image_path, image_quality=85):
    orig_img = Image.open(orig_image_path)
    orig_img.save(compressed_image_path, quality=image_quality)

    return compressed_image_path


def convert_jpg_to_pdf(input_image_path, compressed_image_path, output_pdf_path, image_quality, border_size):
    # Open the JPG image using Pillow
    img = Image.open(input_image_path)

    # Calculate the dimensions of the PDF with the border
    pdf_width = img.width + 2 * border_size
    pdf_height = img.height + 2 * border_size

    # Create a PDF file with the calculated dimensions
    pdf_canvas = canvas.Canvas(output_pdf_path, pagesize=(pdf_width, pdf_height))

    # Compress the image before drawing onto the PDF
    compressed_image_path = compress_image(input_image_path, compressed_image_path, image_quality)

    # Save the current state of the canvas
    pdf_canvas.saveState()

    # Set the compression quality
    pdf_canvas.drawImage(compressed_image_path, border_size, border_size,
                         width=img.width, height=img.height, preserveAspectRatio=True, mask='auto')

    # Restore the previous state of the canvas
    pdf_canvas.restoreState()

    # Save the PDF file
    pdf_canvas.save()


if __name__ == "__main__":
    # Default values
    input_image_path: str = 'resources/original_input.jpg'

    # Generate default output PDF file path
    base_path, file_name = os.path.split(input_image_path)
    file_name_without_extension, extension = os.path.splitext(file_name)
    output_pdf_path = os.path.join(base_path, f"{file_name_without_extension}.pdf")

    image_quality: int = 85
    border_size: int = 344  # Set the border size (1 inch = 72 points)

    # Check if parameters are provided
    if len(sys.argv) > 1:
        input_image_path = sys.argv[1]
    if len(sys.argv) > 2:
        output_pdf_path = sys.argv[2]
    if len(sys.argv) > 3:
        image_quality = int(sys.argv[3])
    if len(sys.argv) > 4:
        border_size = int(sys.argv[4])

    print(f"Using input file: {input_image_path}")
    print(f"Will output to: {output_pdf_path}")
    print(f"Image quality: {image_quality}%")
    print(f"Border size of : {border_size} points")

    # Path to the compressed image
    compressed_image_path = os.path.join(base_path, f"{file_name_without_extension}_compressed{extension}")

    convert_jpg_to_pdf(input_image_path, compressed_image_path, output_pdf_path, image_quality, border_size)
