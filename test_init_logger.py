import logging
from logger import init_logger


# Check if the logger is initialized correctly
def test_init_logger():
    log = init_logger("__test_init_logger__", logging.INFO)
    assert log.name == "__test_init_logger__"
