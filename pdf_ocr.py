#First you need to import your libraires
#import misc libraries
import os
import re
import glob
import io
import pandas as pd
    
#libraries for searchable PDF
import PyPDF2
import pytesseract
from pdf2image import convert_from_path

#change to black and white with Pillow to take up less space
from PIL import Image


#define paths

#poppler_path will be mapped to a libaray/bin
poppler_path = 'C:/your_path_to_poppler' 

#pytesseract will be mapped to an .exe
pytesseract.pytesseract.tesseract_cmd = 'C:/your_path_to_tesseract.exe' 