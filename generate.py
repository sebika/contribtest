#!/usr/bin/python3
# -*- coding: utf-8 -*-

# generate site from static pages, loosely inspired by Jekyll
# run like this:
#   ./generate.py test/source output
# the generated `output` should be the same as `test/expected_output`

import sys
from pathlib import Path
from parser import parse_file
from writer import write_output
from environment import list_files
from environment import init_jinja_environment
from environment import generate_html
from logger import init_logger


def generate_site(source_folder, output_folder):
    log.info('Generating site from %r', source_folder)

    layouts_folder_path = source_folder + '/layout'
    log.info('Getting layouts from %r', layouts_folder_path)

    # Prepare jinja environment
    jinja_env = init_jinja_environment(layouts_folder_path)
    log.info('Jinja environment created successfully')

    for file_path in list_files(source_folder, '.rst'):
        html, template_name = generate_html(file_path, jinja_env)
        output_file_name = Path(file_path).stem + '.html'
        write_output(output_folder, output_file_name, html)
        log.info("Writing %r with template %r", output_file_name, template_name)


def main():
    generate_site(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    log = init_logger(__name__)
    main()
