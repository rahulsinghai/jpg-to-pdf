import sys
from PIL import Image
from reportlab.pdfgen import canvas


def compress_image(orig_image_path, output_image_path, quality=85):
    orig_img = Image.open(orig_image_path)
    orig_img.save(output_image_path, quality=quality)


if __name__ == "__main__":
    # Default values
    input_image_path: str = 'resources/original_input.jpg'
    output_pdf_path: str = 'resources/output.pdf'
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

    # Open the JPG image using Pillow
    img = Image.open(input_image_path)

    # Calculate the dimensions of the PDF with the border
    pdf_width = img.width + 2 * border_size
    pdf_height = img.height + 2 * border_size

    # Create a PDF file with the calculated dimensions
    pdf_canvas = canvas.Canvas(output_pdf_path, pagesize=(pdf_width, pdf_height))

    # Path to the compressed image
    compressed_image_path = 'compressed_input.jpg'

    # Compress the image before drawing onto the PDF
    compress_image(input_image_path, compressed_image_path, quality=78)

    # Save the current state of the canvas
    pdf_canvas.saveState()

    # Set the compression quality
    pdf_canvas.drawImage(compressed_image_path, border_size, border_size,
                         width=img.width, height=img.height, preserveAspectRatio=True, mask='auto')

    # Restore the previous state of the canvas
    pdf_canvas.restoreState()

    # Save the PDF file
    pdf_canvas.save()
