import pytest
from filecmp import cmp
from generate import generate_site
from environment import list_files


# Test whether generate_site method creates the reference sites
def test_generate_site():
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
