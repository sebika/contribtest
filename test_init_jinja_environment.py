from environment import init_jinja_environment


# Test whether jinja environment loaded up corectly
def test_init_jinja_environment():
    jinja_env = init_jinja_environment('test/layout')
    assert jinja_env is not None
