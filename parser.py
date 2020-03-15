from json import loads

# The separator in the .rst files
separator = '---'


def parse_file(file_path):
    # Save data into a json before you find the separator
    # or save the data into text content
    separator_found = False
    json_data = ""
    text_content = ""

    with open(file_path, 'r') as f:
        for line in f:
            if line.strip() == separator:
                separator_found = True
                continue
            if not separator_found:
                json_data += line
            else:
                text_content += line

    metadata = loads(json_data)
    # We need a 'content' key in metadata because both layouts requires one
    metadata['content'] = text_content

    return metadata
