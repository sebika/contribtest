#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import logging
from pathlib import Path
from parser import parse_file
from writer import write_output
from environment import list_files
from environment import init_jinja_environment
from environment import generate_html
from logger import init_logger


def generate_site(source_folder, output_folder):
    log = init_logger(__name__, logging.INFO)
    log.info('Generating site from %r', source_folder)

    layouts_folder_path = source_folder + '/layout'
    log.info('Getting layouts from %r', layouts_folder_path)

    # Prepare jinja environment
    jinja_env = init_jinja_environment(layouts_folder_path)
    log.info('Jinja environment created successfully')

    try:
        for file_path in list_files(source_folder, '.rst'):
            # Get the html content and the template used to construct the html
            html, template_name = generate_html(file_path, jinja_env)

            # Write to the file and pass the information to the logger
            output_file_name = Path(file_path).stem + '.html'
            write_output(output_folder, output_file_name, html)
            log.info("Wrote %r with template %r", output_file_name, template_name)

        log.info("SUCCESS")

    except FileNotFoundError:
        log.critical("Input file or folder not found")
        log.critical("Could not find necessary the files")
        log.critical("Ending process ...")

    except ValueError:
        log.critical("Template not found in layout folder")
        log.critical("Could not find necessary the files ...")
        log.critical("Ending process ...")


def main():
    generate_site(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
