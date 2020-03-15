import logging


def init_logger(module_name):
    # Instantiate the logger
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(module_name)

    return log
