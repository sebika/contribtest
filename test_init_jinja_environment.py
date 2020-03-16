from environment import init_jinja_environment


def test_init_jinja_environment():
    jinja_env = init_jinja_environment('test/layout')
    assert jinja_env is not None
