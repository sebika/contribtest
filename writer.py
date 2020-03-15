import os
import sys


def write_output(output_folder, file_name, html):
    # Opens the file, or creates it if the file doesn't exist
    # and writes the content
    with open(os.path.join(output_folder, file_name), 'w+') as f:
        f.write(html)
