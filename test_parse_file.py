import pytest
from parser import parse_file


# Check if the method raises the correct exception
def test_parse_file1():
    file_path = 'test/aaaaaaa.rst'
    with pytest.raises(FileNotFoundError) as e:
        assert parse_file(file_path) == None

# Check if the generated metadata is correct
def test_parse_file2():
    file_path = 'test/source/contact.rst'
    metadata = parse_file(file_path)

    expected_dict = {}
    expected_dict['title'] = 'Contact us!'
    expected_dict['layout'] = 'base.html'
    expected_dict['content'] = '\nWrite an email to contact@example.com.\n'

    assert metadata == expected_dict

# Check if the generated metadata is correct
def test_parse_file3():
    file_path = 'test/source/index.rst'
    metadata = parse_file(file_path)

    expected_dict = {}
    expected_dict['title'] = 'My awesome site'
    expected_dict['layout'] = 'home.html'
    expected_dict['content'] = '\nblah blah\n'

    assert metadata == expected_dict
