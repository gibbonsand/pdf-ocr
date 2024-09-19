
# import glob
# import io
# import os
# import re
# import pandas as pd
# from pdf2image import convert_from_path
# from pillow import Image
# import PyPDF2
import pytesseract

import pdf_ocr.constants as c

# Configure pytesseract executable
pytesseract.pytesseract.tesseract_cmd = '/usr/homebrew/bin/tesseract'
