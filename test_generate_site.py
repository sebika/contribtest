import os
import shutil
from filecmp import cmp
from generate import generate_site
from environment import list_files


# Test whether generate_site method creates the reference sites
# All the paths needs to be correct for this test to work
def test_generate_site():

    # Both try/except blocks below could be a setup method
    # Delete the output folder and create an empty new one
    # This must be done independently
    try:
        shutil.rmtree('output')
    except:
        pass
    try:
        os.mkdir('output')
    except:
        pass

    source_folder = 'test/source'
    output_folder = 'output'
    generate_site(source_folder, output_folder)

    # We know there are only 2 files so it's easier to check with 2 if-s
    # Compare the first output with the first ref
    equal = cmp('output/contact.html', 'test/expected_output/contact.html')
    assert equal == True

    # Compare the first output with the first ref
    equal = cmp('output/index.html', 'test/expected_output/index.html')
    assert equal == True
