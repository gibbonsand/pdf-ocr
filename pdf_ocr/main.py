""" Main entrypoint for the pdf_ocr project"""
# Standard libraries
import argparse
import glob
import logging
import os
import pathlib

# Local libraries
import pdf_ocr.constants as c
from pdf_ocr.pdf_ocr import pdf_ocr
from shared_libraries.setup_utilities import init_logger, ensure_folders


def main():
    """ Main entrypoint of the pdf_ocr project. """
    # Ensure the input and output folder exist
    ensure_folders([c.OUTPUT_DIR,
                    c.INPUT_DIR,
                    str(pathlib.Path(c.LOGFILE_PATH).parent)])

    # Initialize logging
    init_logger(log_to_file=True,
                log_to_stream=True,
                logfile_path=c.LOGFILE_PATH)

    # Initialize argument parser
    parser = argparse.ArgumentParser(description="pdf ocr tool")
    parser.add_argument("--input_file",
                        required=False,
                        help="Input file path")
    parser.add_argument("--output_file",
                        required=False,
                        help="Output file path")
    parser.add_argument("--languages",
                        nargs='+',
                        required=False,
                        type=lambda x: x.split(','),
                        #type=str,
                        help="Languages to process (comma-separated values e.g. eng,jpn)")

    args = parser.parse_args()
    logging.debug("Input arguments: %s", vars(args))

    languages = args.languages[0] if args.languages is not None else 'eng'
    logging.info(languages)

    # Entrypoint if specific input and output files are profided
    if args.input_file is not None:
        if args.output_file is None:
            logging.error("Output file is required when using an input file")
            raise ValueError("Output file is required when using an input file")
        else:
            pdf_ocr(input_file=args.input_file,
                    output_file=args.output_file,
                    lang=languages)

    # Entrypoint if no specific input and output files are provided
    else:
        # Get list of files present in the default ouput directory
        already_processed_files = [
            os.path.basename(file) for file in glob.glob(f"{c.OUTPUT_DIR}*.pdf")
        ]

        # Parse all files in default input directory
        for input_path in glob.glob(f"{c.INPUT_DIR}*.pdf"):
            file_name = os.path.basename(input_path)
            output_path = os.path.join(c.OUTPUT_DIR, file_name)

            # Skip any files that have already been processed
            if file_name in already_processed_files:
                logging.info("Skipping file %s as it was already processed", file_name)
                continue

            # Call pdf_ocr function that wraps the necessary steps
            logging.info("Processing file %s...", file_name)
            pdf_ocr(input_file=input_path,
                    output_file=output_path,
                    lang=languages)

            logging.info("Finished processing file %s", file_name)
