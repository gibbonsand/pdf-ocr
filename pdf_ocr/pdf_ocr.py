""" pdf_ocr module makes PDF files readable in the language(s) requested. """
# Standard libraries
import io
import logging

# External libraries
from pdf2image import convert_from_path
# from pillow import Image
import PyPDF2
import pytesseract

# Local libraries
import pdf_ocr.constants as c


def pdf_ocr(input_file: str,
            output_file: str,
            lang: list or str = 'eng') -> None:
    """
    Perform Optical Character Recognition (OCR) on a PDF file using Pytesseract.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path to save the OCR-processed PDF file.
        lang (list or str, optional): List of languages to recognize. Can be a str or a list.
        If a single language is specified, use it as a string (e.g., 'eng' instead of ['eng']).
        Defaults to 'eng'.
        Valid example input lang parameters:
        - 'eng'
        - 'eng+jpn'
        - ['eng', 'jpn']

    Returns:
        None
    """
    # Convert languages provided as lists to the str input required by pytesseract (e.g. 'eng+jpn')
    lang = lang if isinstance(lang, str) else '+'.join(lang)

    # Initialise PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Convert PDF pages to list of images
    logging.info("Step 1/3: converting PDF to image list")
    page_images = convert_from_path(input_file, poppler_path=c.POPPLER_DIR)

    # Parse each page image
    logging.info("Step 2/3: Pytesseract OCR process")
    count = 1
    for page_image in page_images:
        logging.info("Parsing page %s out of %s", count, len(page_images))

        # OCR process: convert images back to readable PDFs
        page = pytesseract.image_to_pdf_or_hocr(page_image,
                                                extension="pdf",
                                                lang=lang)

        # Read out OCR-processed PDF and write it to the PDF writer
        pdf = PyPDF2.PdfReader(io.BytesIO(page))
        pdf_writer.add_page(pdf.pages[0])
        count += 1

    # Write compiled readable PDF
    logging.info("Step 3/3: Writing compiled readable PDF to output")
    try:
        with open(output_file, "wb") as f:
            pdf_writer.write(f)
        logging.info("Output saved to %s", output_file)
    except Exception as e:
        logging.error("Issue raised when attempting to write output: %s", e)
        raise IOError("Issue raised when attempting to write output") from e
