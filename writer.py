import os


# Opens the file, or creates it if the file doesn't exist
# Writes the contents of the html to the file
def write_output(output_folder, file_name, html):
    with open(os.path.join(output_folder, file_name), 'w+') as f:
        f.write(html)
