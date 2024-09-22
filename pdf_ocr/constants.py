""" Module containing the constant definitions for the pdf_ocr project """
# Standard libraries
import pathlib
import subprocess

# External libraries
import pytesseract


# Pathing configuration
LOGFILE_PATH = '/Users/andrewgibbons/Projects/logs/pdf-ocr/pdf-ocr.log'
DATA_ROOT_DIR = '/Users/andrewgibbons/Projects/data/pdf-ocr/'
INPUT_DIR = f"{DATA_ROOT_DIR}input/"
OUTPUT_DIR = f"{DATA_ROOT_DIR}output/"
POPPLER_PATH = subprocess.check_output(['which', 'pdfinfo']).decode('utf-8').strip()
POPPLER_DIR = str(pathlib.Path(POPPLER_PATH).parent)
# Define tesseract path
TESSERACT_PATH = subprocess.check_output(['which', 'tesseract']).decode('utf-8').strip()
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

# Help messages for argparse
HELP_MESSAGES = {
'languages': """\
Specify which language(s) the pdf-ocr should use for OCR.\
""",
}

# argparse config
ARG_NAMES = HELP_MESSAGES.keys()
VALUE_ARGS = {
    "languages": str,
}
