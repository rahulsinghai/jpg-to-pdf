from PIL import Image
from reportlab.pdfgen import canvas


def compress_image(orig_image_path, output_image_path, quality=85):
    orig_img = Image.open(orig_image_path)
    orig_img.save(output_image_path, quality=quality)


if __name__ == "__main__":
    # Replace 'input.jpg' with the path to your JPG file
    input_image_path = 'original_input.jpg'

    # Replace 'output.pdf' with the desired output PDF file path
    output_pdf_path = 'output.pdf'

    # Open the JPG image using Pillow
    img = Image.open(input_image_path)

    # Set the border size (1 inch = 72 points)
    border_size = 344

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
