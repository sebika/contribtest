from environment import list_files


# Test how many .html files are in test/expected_output
def test_list_files1():

    # We need list(list_files()) because you can't use len(generator())
    no_files = len(list(list_files('test/expected_output', '.html')))
    assert no_files == 2


# Test how many .rst files are in test/source
def test_list_files2():
    no_files = len(list(list_files('test/source', '.rst')))
    assert no_files == 2


# Test how many .html files are in test/source/layout
def test_list_files3():
    no_files = len(list(list_files('test/source/layout', '.html')))
    assert no_files == 2


# Test how many .html files are in output
def test_list_files4():
    no_files = len(list(list_files('output', '.html')))
    assert no_files == 2

# Test how many .txt files are in output
def test_list_files5():
    no_files = len(list(list_files('output', '.txt')))
    assert no_files == 0
