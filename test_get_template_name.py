import pytest
from environment import get_template_name

# Check if it gives the correct value for 'layout' key
def test_get_template_name1():
    test_dict = {}
    test_dict['title'] = 'aaa'
    test_dict['layout'] = 'bbb'
    assert get_template_name(test_dict) == 'bbb'


# This test checks if the method raises the correct exception
def test_get_template_name2():
    test_dict = {}
    test_dict['title'] = 'aaa'
    test_dict['header'] = 'bbb'
    with pytest.raises(Exception) as e:
        assert get_template_name(test_dict) == 'bbb'
    assert str(e.value) == "'layout' key not found in metadata dictionary"
