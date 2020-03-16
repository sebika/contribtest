import os
from writer import write_output


# This test checks the writer method
# ! Output folder should be a valid name !
def test_writer():
    output_folder = 'output'
    file_name = 'test.html'
    html = '<h1>TITLE</h1>\nBLAHBLAH\n'

    # Call the tested function
    write_output(output_folder, file_name, html)

    # Get the output
    output_file_path = os.path.join(output_folder, file_name)
    output_html = open(output_file_path, 'r').read()

    # Check the output
    assert html == output_html

    os.remove(output_file_path)
