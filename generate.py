#!/usr/bin/python3
# -*- coding: utf-8 -*-

# generate site from static pages, loosely inspired by Jekyll
# run like this:
#   ./generate.py test/source output
# the generated `output` should be the same as `test/expected_output`

import os
import sys
import logging
import json
import jinja2
from jinja2.loaders import FileSystemLoader
from jinja2 import Template

log = logging.getLogger(__name__)
separator = '---'


def list_files(folder_path):
    for name in os.listdir(folder_path):
        base, ext = os.path.splitext(name)
        if ext != '.rst':
            continue
        yield os.path.join(folder_path, name)

def read_file(file_path):
    # This is false untill you find the '---' separator which splits
    # the json from the text
    separator_found = False
    json_content = ""
    text_content = ""

    with open(file_path, 'r') as f:
        for line in f:
            if line.strip() == separator:
                separator_found = True
                continue
            if not separator_found:
                json_content += line
            else:
                text_content += line

    return json.loads(json_content), text_content

def write_output(name, html):
    # TODO should not use sys.argv here, it breaks encapsulation
    with open(os.path.join(sys.argv[2], name), 'w+') as f:
        f.write(html)

def generate_site(folder_path):
    log.info('Generating site from %r', folder_path)

    layouts_folder_path = folder_path + '/layout'
    log.info('Getting layouts from %r', layouts_folder_path)

    # prepare jinja2 environment
    jinja_env = jinja2.Environment()
    jinja_env.loader = FileSystemLoader(layouts_folder_path)
    jinja_env.trim_blocks = True

    for file_path in list_files(folder_path):
        output_file = file_path.split('/')[-1].split('.')[0] + '.html'
        metadata, content = read_file(file_path)
        metadata['content'] = content

        template_name = metadata['layout']
        template = jinja_env.get_template(template_name)

        html = template.render(metadata)

        write_output(output_file, html)
        log.info("Writing %r with template %r", output_file, template_name)


def main():
    generate_site(sys.argv[1])


if __name__ == '__main__':
    logging.basicConfig()
    main()
