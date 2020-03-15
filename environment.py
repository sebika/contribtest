import os
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
from parser import parse_file

def list_files(folder_path, extension):
    # Find all the files in folder_path with a specified extension
    for name in os.listdir(folder_path):
        base, ext = os.path.splitext(name)
        if ext != extension:
            continue
        yield os.path.join(folder_path, name)


def init_jinja_environment(layouts_folder_path):
    # Create and initialize jinja parameters
    jinja_env = Environment()
    jinja_env.loader = FileSystemLoader(layouts_folder_path)

    # Set trim_block to True to avoid blank lines in output
    jinja_env.trim_blocks = True

    return jinja_env


def generate_html(file_path, jinja_env):
    metadata = parse_file(file_path)
    template_name = get_template_name(metadata)
    template = jinja_env.get_template(template_name)
    html = template.render(metadata)

    return html, template_name

def get_template_name(metadata):
    try:
        return metadata['layout']
    except:
        raise ValueError('layout key not found in metadata dictionary')
